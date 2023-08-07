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
import re

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.method import (
    Method, HubbardKanamoriModel, KMesh, FrequencyMesh, TimeMesh, DMFT, AtomParameters
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, EnergyEntry, Charges, GreensFunctions
)
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint
from ..utils import get_files
from ..wien2k.parser import StructParser  # Wien2k is imported to parse the system information


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = []


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
                        str_operation=str_to_orbitals_list)]))]


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
                        repeats=True)])),
            Quantity(
                'impurity_parameters', r'iparams0\=([\s\S]+)(?:\s*\})',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'params',
                        r'\s*\"(.+)\"\s*\:\s*\[[\"\'\s]*([a-zA-Z\d\.\-]+)[\"\'\s]*\,',
                        repeats=True)]))]


class ImpurityGfOutParser(TextParser):
    def __init__(self):
        super().__init__()

    @property
    def data(self):
        if self.mainfile:
            return np.loadtxt(self.mainfile)

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'parameters',
                r'\# *nf\=([\d\.]+) *mu\=([\d\.\-]+) *T\=([\d\.]+) *TrSigmaG\=([\d\.\-]+) *Epot\=([\d\.\-]+) *Ekin\=([\d\.\-]+) *mom\=([\[\]\,\d\.\-]+)',
                repeats=False)
        ]


class EDMFTParser:
    level = 1

    def __init__(self):
        self._re_namesafe = re.compile(r'[^\w]')
        self._calculation_type = 'dmft'

        self.out_parser = OutParser()
        self.struct_parser = StructParser()
        self.indmfl_parser = IndmflParser()
        self.params_parser = ParamsParser()
        self.iterate_parser = DataTextParser()
        self.imp_gf_parser = ImpurityGfOutParser()
        self.latt_gf_parser = DataTextParser()

        self._solver_map = {
            'CTQMC': 'CT-HYB',
            'OCA': 'OCA',
            'NCA': 'NCA'
        }

        self._angular_momentum = ['s', 'p', 'd', 'f']

        self._gf_files_map = {
            'imp.0/Gf.out.*': 'greens_function_iw',
            'imp.0/Sig.out.*': 'self_energy_iw',
            'imp.0/Delta.inp.*': 'hybridization_function_iw'
        }

    def parse_system(self):
        struct_files = get_files('*.struct', self.filepath, self.mainfile)
        if struct_files:
            if len(struct_files) > 1:
                self.logger.warning(f'Multiple *struct files found; we will parse the last one: {struct_files[-1]}')
            self.struct_parser.mainfile = struct_files[-1]
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

        # TODO ask @LucianPascut what projectorw.dat means to parse as initial model.

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
                if self.indmfl_parser.get('siginds_corr', {}).get('cix') is not None:  # TODO ask @Alvin why this is populated locally, but not when processing
                    n_orbitals = self.indmfl_parser.get('siginds_corr', {}).get('cix')[n][-1]
                    sec_atom_params.n_orbitals = n_orbitals
                if self.indmfl_parser.get('siginds_corr', {}).get('orbitals') is not None:
                    sec_atom_params.orbitals = [
                        f'{angular_momentum}{orb}' for orb in self.indmfl_parser.get('siginds_corr', {}).get('orbitals')]
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
        sec_dmft.n_impurities = n_corr_atoms
        if self.indmfl_parser.get('siginds_corr', {}).get('cix'):  # TODO ask @Alvin why this is populated locally, but not when processing
            n_orbitals = [orb[-1] for orb in self.indmfl_parser.get('siginds_corr', {}).get('cix')]
            sec_dmft.n_correlated_orbitals = n_orbitals
        if self.impurity_parameters.get('nf0'):
            n_corr_elect = self.impurity_parameters.get('nf0') / n_corr_atoms
            corr_elect = [n_corr_elect] * n_corr_atoms  # TODO ask Lucian if this makes sense
            sec_dmft.n_electrons = corr_elect
        sec_dmft.inverse_temperature = self.impurity_parameters.get('beta', 0.0) / ureg.eV
        sec_dmft.magnetic_state = 'paramagnetic'  # TODO ask Lucian if this is correct
        sec_dmft.impurity_solver = self._solver_map.get(self.general_parameters.get('solver', ''))

    def parse_scc(self):
        # TODO ask about extensions when more than one impurity: iparams0, iparams1,
        # info.iterate n_latt and n_imp columns? imp.X subfolders?
        sec_run = self.archive.run[-1]

        def create_calculation_section():
            sec_scc = sec_run.m_create(Calculation)
            if sec_run.m_xpath('system'):
                sec_scc.system_ref = sec_run.system[-1]
            sec_scc.method_ref = sec_run.method[-1]  # ref DMFT
            return sec_scc

        def call_calculation_section(i_scc):
            if sec_run.calculation:
                return sec_run.calculation[i_scc]
            else:
                return sec_run.m_create(Calculation)

        def extract_greens_functions_data(sec_scc, sec_gfs, n_orbitals, gf_data):
            # Adding FreqMesh
            iw = gf_data[:, 0]
            sec_freq_mesh = FrequencyMesh(dimensionality=1, n_points=len(iw), points=iw * 1j * ureg.eV)
            method_ref = sec_scc.method_ref
            method_ref.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
            sec_gfs.matsubara_freq = iw
            # defining the full Gf in the basis n_atoms x 2 x n_orbitals x n_iw
            gf_orb_data = np.array([gf_data[:, 2 * n + 1] + gf_data[:, 2 * n + 2] * 1j for n in range(n_orbitals)])
            return np.array([[gf_orb_data, gf_orb_data]])

        n_orbitals = sec_run.method[-1].dmft.n_correlated_orbitals[0]
        iterate_files = get_files('info.iterate', self.filepath, self.mainfile)
        if iterate_files:
            if len(iterate_files) > 1:
                self.logger.warning(f'Multiple info.iterate files found; we will parse the last one: {iterate_files[-1]}')
            self.iterate_parser.mainfile = iterate_files[-1]
            data_scf = self.iterate_parser.data
            if data_scf is not None:
                previous_iter_dmft = 0
                sec_scc = None
                for i_dmft in range(len(data_scf)):
                    iter_dmft = np.int32(data_scf[i_dmft][1])
                    if i_dmft == 0:
                        sec_scc = create_calculation_section()
                    else:
                        previous_iter_dmft = np.int32(data_scf[i_dmft - 1][1])
                        if previous_iter_dmft != iter_dmft:
                            sec_scc = create_calculation_section()

                    sec_scf_iteration = sec_scc.m_create(ScfIteration)
                    # Energies
                    sec_energy = sec_scf_iteration.m_create(Energy)
                    sec_energy.chemical_potential = data_scf[i_dmft][3] * ureg.eV
                    sec_energy.double_counting = data_scf[i_dmft][4] * ureg.eV
                    sec_energy.total = EnergyEntry(value=data_scf[i_dmft][5] * ureg.rydberg)
                    sec_energy.free = EnergyEntry(value=data_scf[i_dmft][7] * ureg.rydberg)
                    # Lattice and impurity occupations
                    sec_charges_latt = sec_scf_iteration.m_create(Charges)
                    sec_charges_latt.kind = 'lattice'
                    sec_charges_latt.n_atoms = sec_scc.method_ref.dmft.n_impurities
                    sec_charges_latt.n_orbitals = n_orbitals
                    sec_charges_latt.n_electrons = [data_scf[i_dmft][8]]
                    sec_charges_imp = sec_scf_iteration.m_create(Charges)
                    sec_charges_imp.kind = 'impurity'
                    sec_charges_imp.n_atoms = sec_scc.method_ref.dmft.n_impurities
                    sec_charges_imp.n_orbitals = n_orbitals
                    sec_charges_imp.n_electrons = [data_scf[i_dmft][9]]

        # Impurity Green's function, self-energy, hybridization function parsing
        for imp_path in self._gf_files_map.keys():
            impurity_files = get_files(imp_path, self.filepath, self.mainfile)  # Hybridization function
            if impurity_files:
                impurity_files.sort()
                for i_scc, f in enumerate(impurity_files):
                    # Calculation and GreensFunction sections
                    sec_scc = call_calculation_section(i_scc)
                    if sec_scc.greens_functions:
                        sec_gfs = sec_scc.greens_functions[-1]
                    else:
                        sec_gfs = sec_scc.m_create(GreensFunctions)
                        sec_gfs.type = 'impurity'
                    # Parsing data
                    self.imp_gf_parser.mainfile = f
                    imp_gf_data = self.imp_gf_parser.data
                    impurity_data = extract_greens_functions_data(sec_scc, sec_gfs, n_orbitals, imp_gf_data) if imp_gf_data is not None else None
                    if impurity_data is not None:
                        sec_gfs.m_set(sec_gfs.m_get_quantity_definition(self._gf_files_map[imp_path]), impurity_data)
                    if self.imp_gf_parser.get('parameters'):
                        sec_gfs.chemical_potential = self.imp_gf_parser.get('parameters')[1] * ureg.eV

        # Parse lattice GFs quantities at the last Calculation
        if sec_run.calculation is not None:
            sec_scc = sec_run.calculation[-1]
            latt_gf_files = get_files('*.gc1', self.filepath, self.mainfile)
            if latt_gf_files:
                if len(latt_gf_files) > 1:
                    self.logger.warning(f'Multiple *.gc1 files found; we will parse the last one: {latt_gf_files[-1]}')
                self.latt_gf_parser.mainfile = latt_gf_files[-1]
                latt_gf_data = self.latt_gf_parser.data
                lattice_data = extract_greens_functions_data(sec_scc, sec_gfs, n_orbitals, latt_gf_data) if latt_gf_data is not None else None
                # Populating GreensFunctions section
                sec_gfs = sec_scc.m_create(GreensFunctions)
                sec_gfs.type = 'lattice'
                sec_gfs.greens_function_iw = lattice_data


            # latt_sigma_files = get_files('*sig.inp1', self.filepath, self.mainfile)


    def init_parser(self):
        self.out_parser.mainfile = self.mainfile
        self.out_parser.logger = self.logger
        self.struct_parser.mainfile = None
        self.struct_parser.logger = self.logger
        self.indmfl_parser.mainfile = None
        self.indmfl_parser.logger = self.logger
        self.params_parser.mainfile = None
        self.params_parser.logger = self.logger
        self.iterate_parser.mainfile = None
        self.iterate_parser.logger = self.logger
        self.imp_gf_parser.mainfile = None
        self.imp_gf_parser.logger = self.logger
        self.latt_gf_parser.mainfile = None
        self.latt_gf_parser.logger = self.logger

    def get_mainfile_keys(self, **kwargs):
        return True

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.mainfile = os.path.basename(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        self.init_parser()

        params_files = get_files('*params.dat', self.filepath, self.mainfile)
        if params_files:
            if len(params_files) > 1:
                self.logger.warning(f'Multiple *params.dat files found; we will parse the last one: {params_files[-1]}')
            self.params_parser.mainfile = params_files[-1]

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
        indmfl_files = get_files('*.indmfl', self.filepath, self.mainfile)
        if indmfl_files:
            if len(indmfl_files) > 1:
                self.logger.warning(f'Multiple *.indmfl files found; we will parse the last one: {indmfl_files[-1]}')
            self.indmfl_parser.mainfile = indmfl_files[-1]
            if self.general_parameters and self.impurity_parameters:
                self.parse_initial_model()
                self.parse_method()

        # Calculation section
        self.parse_scc()

        # Workflow section
        # self.archive refers to the DMFT1 and DMFT2 SinglePoint entries grouped. Then,
        # we define DFT+DMFT workflow grouping the DFT Wien2k entry with self.archive.
        workflow = SinglePoint()
        self.archive.workflow2 = workflow
