#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import numpy as np
import os
import logging
import h5py
import re

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.method import (
    Method, HubbardKanamoriModel, LatticeModelHamiltonian, KMesh, FrequencyMesh, TimeMesh,
    DMFT, AtomParameters
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, GreensFunctions
)
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint
from ..utils import get_files
from ..wien2k.parser import StructParser  # Wien2k is imported to parse the system information


class IndmflParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_orbitals_list(val_in):
            return val_in.replace("'", "").split(" ")[:-1]

        self._quantities = [
            Quantity(
                'hybridization_window',
                r'(\d+) *(\d+) *(\d+) *(\d+) *\# hybridization band index nemin and nemax\, renormalize for interstitials\, projection type'),
            Quantity(
                'real_or_imaginary_axis',
                r'(\d+) *([\d\.]+) *([\d\.]+) *(\d+) *([\d\-\.]) *([\d\-\.]) *\# matsubara\, broadening\-corr\, broadening\-noncorr\, nomega\, omega\_min\, omega\_max \(in eV\)'),
            Quantity(
                'n_corr_atoms', r'(\d+)\s*\# number of correlated atoms'),
            Quantity(
                'i_atom_corr', r'(\d+)\s*(\d+)\s*(\d+)\s*\# iatom\, nL\, locrot', repeats=True),
            Quantity(
                'l_atom_corr', r'\s*(\d+)\s*(\d+)\s*(\d+)\s*\# L\, qsplit\, cix', repeats=True),
            Quantity(
                'siginds_corr',
                r'(\# Siginds and crystal\-field transformations for correlated orbitals \=*[\s\S]+)(?:\# Sigind follows)',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'indep_cix_blocks',
                            r'(\d+) *(\d+) *(\d+) *\# Number of independent kcix blocks\, max dimension\, max num\-independent-components'),
                        Quantity(
                            'cix',
                            r'(\d+) *(\d+) *(\d+) *\# cix\-num\, dimension\, num\-independent\-components',
                            repeats=True),
                        Quantity(
                            'orbitals',
                            r'\# Independent components are \-*[\s\S]([\'\^\-\+a-zA-Z\s\d]+)',
                            str_operation=str_to_orbitals_list)]))
        ]


class ParamsParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'general_parameters', r'([\s\S]+)(?:\# Impurity problem number 0)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'params', r'([a-zA-Z\_]+)\s*\=\s*\'*([a-zA-Z\d\.\-]+)\'*',
                        repeats=True)
                    ])
                ),
            Quantity(
                'impurity_parameters', r'iparams0\=([\s\S]+)(?:\s*\})',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'params',
                        r'\s*\"(.+)\"\s*\:\s*\[[\"\'\s]*([a-zA-Z\d\.\-]+)[\"\'\s]*\,',
                        repeats=True)
                    ])
                )]


class EDMFTParser:
    level = 1

    def __init__(self):
        self._re_namesafe = re.compile(r'[^\w]')
        self._calculation_type = 'dmft'

        self.indmfl_parser = IndmflParser()
        self.struct_parser = StructParser()
        self.params_parser = ParamsParser()

        self._solver_map = {
            'CTQMC': 'CT-HYB',
            'OCA': 'OCA',
            'NCA': 'NCA'
        }

        self._angular_momentum = ['s', 'p', 'd', 'f']

    def parse_system(self):
        struct_file = get_files('*.struct', self.filepath, self.mainfile)
        if struct_file:
            if len(struct_file) > 1:
                self.logger.warning('Multiple *struct files found; we will parse the last one!')
            self.struct_parser.mainfile = struct_file[-1]
            atoms = self.struct_parser.get_atoms()
            if atoms is None:
                return

            sec_system = self.archive.run[-1].m_create(System)
            sec_atoms = sec_system.m_create(Atoms)
            sec_atoms.lattice_vectors = np.array(atoms.get_cell()) * ureg.angstrom
            sec_atoms.positions = atoms.get_positions() * ureg.angstrom
            sec_atoms.labels = atoms.get_chemical_symbols()
            sec_atoms.periodic = atoms.get_pbc()

    def parse_initial_model(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        # TODO ask Lucian what projectorw.dat means to parse as initial model.
        # HubbardKanamori part
        for n in range(self.indmfl_parser.get('n_corr_atoms', 1)):
            sec_atom_params = sec_method.m_create(AtomParameters)
            if sec_run.m_xpath('system[-1].atoms.labels'):
                labels = sec_run.system[-1].atoms.labels
                if self.indmfl_parser.get('i_atom_corr') is not None:
                    atom_corr = self.indmfl_parser.get('i_atom_corr')[n]
                    label = labels[atom_corr[0] - 1]
                    sec_atom_params.label = label
                    if self.indmfl_parser.get('l_atom_corr') is not None:
                        angular_momentum = self._angular_momentum[self.indmfl_parser.get('l_atom_corr')[n][0]]
            sec_hubbard_kanamori = sec_atom_params.m_create(HubbardKanamoriModel)
            sec_hubbard_kanamori.double_counting_correction = self.general_parameters.get('DCs', '')
            sec_hubbard_kanamori.u = self.impurity_parameters.get('U', 0.0) * ureg.eV
            sec_hubbard_kanamori.jh = self.impurity_parameters.get('J', 0.0) * ureg.eV
            if self.impurity_parameters.get('CoulombF', 'Full') == 'Ising':
                sec_hubbard_kanamori.j = 0.0
            else:
                sec_hubbard_kanamori.up = sec_hubbard_kanamori.u - 2 * sec_hubbard_kanamori.jh
                sec_hubbard_kanamori.j = sec_hubbard_kanamori.jh

    def parse_method(self):
        sec_run = self.archive.run[-1]

        sec_method = sec_run.m_create(Method)
        sec_method.starting_method_ref = sec_run.method[0]  # ref to the Non- and InteractionHamiltonian

        # Code-specific parameters
        sec_method.x_edmft_general_parameters = self.general_parameters
        sec_method.x_edmft_impurity_solver_parameters = self.impurity_parameters

        # DMFT method
        sec_dmft = sec_method.m_create(DMFT)
        n_corr_atoms = self.indmfl_parser.get('n_corr_atoms', 1)
        sec_dmft.n_atoms_per_unit_cell = n_corr_atoms
        # TODO add sec_dmft.n_correlated_orbitals
        n_corr_elect = self.impurity_parameters.get('nf0') / n_corr_atoms
        corr_elect = [n_corr_elect] * n_corr_atoms
        sec_dmft.n_correlated_electrons = corr_elect
        sec_dmft.inverse_temperature = self.impurity_parameters.get('beta', 0.0) / ureg.eV
        sec_dmft.magnetic_state = 'paramagnetic'  # TODO ask Lucian if this is correct
        sec_dmft.impurity_solver = self._solver_map.get(self.general_parameters.get('solver', ''))

    def parse_scc(self):
        pass

    def init_parser(self):
        self.indmfl_parser.mainfile = self.mainfile
        self.indmfl_parser.logger = self.logger
        self.struct_parser.mainfile = None
        self.struct_parser.logger = self.logger
        self.params_parser.mainfile = None
        self.params_parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.mainfile = os.path.basename(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        self.init_parser()

        params_file = get_files('*params.dat', self.filepath, self.mainfile)
        if params_file:
            if len(params_file) > 1:
                self.logger.warning(f'Multiple *params.dat files found; we will parse the last one: {params_file[-1]}')
            self.params_parser.mainfile = params_file[-1]

            if self.params_parser.get('general_parameters'):
                self.general_parameters = dict(self.params_parser.get('general_parameters').get('params', []))
            if self.params_parser.get('impurity_parameters'):
                self.impurity_parameters = dict(self.params_parser.get('impurity_parameters').get('params', []))

        # Program section
        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name='eDMFT')

        # System section
        self.parse_system()

        # Method.DMFT section
        if self.general_parameters and self.impurity_parameters:
            self.parse_initial_model()
            self.parse_method()

        # Calculation section
        self.parse_scc()

        # Workflow section
        workflow = SinglePoint()
        self.archive.workflow2 = workflow
