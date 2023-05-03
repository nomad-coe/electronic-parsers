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
    DMFT
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, GreensFunctions
)
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint
from ..utils import get_files
from ..wien2k.parser import StructParser


class IndmflParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'version',
                r'LABEL\d+\:\s*using WIEN2k_(\S+) \(Release ([\d\/]+)\)', flatten=False)]


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

        self.struct_parser = StructParser()
        self.indmfl_parser = IndmflParser()
        self.params_parser = ParamsParser()

        self._solver_map = {
            'CTQMC': 'CT-HYB',
            'OCA': 'OCA'
        }

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
        '''
        for n in range(data.attrs.get('general.nat', 1)):
            sec_hubbard_kanamori_model = sec_hamiltonian.m_create(HubbardKanamoriModel)

            angular_momentum = 'd'
            sec_hubbard_kanamori_model.orbital = angular_momentum
            sec_hubbard_kanamori_model.double_counting_correction = data.attrs.get('general.dc', None)
            # w2dynamics keeps spin-rotational invariance
            for key in self._hubbard_kanamori_map.keys():
                parameters = data.attrs.get(f'atoms.{n+1}.{key}{angular_momentum}{angular_momentum}', None) * ureg.eV
                setattr(sec_hubbard_kanamori_model, self._hubbard_kanamori_map.get(key), parameters)

            if data.attrs.get(f'atoms.{n+1}.hamiltonian') == 'Density':
                sec_hubbard_kanamori_model.j = 0.0
            elif data.attrs.get(f'atoms.{n+1}.hamiltonian') == 'Kanamori':
                sec_hubbard_kanamori_model.j = sec_hubbard_kanamori_model.jh
        '''

    def parse_method(self):
        sec_run = self.archive.run[-1]

        def parse_hubbard_model(method, gen_params, imp_params):
            pass

        def parse_dmft(method, gen_params, imp_params):
            sec_dmft = method.m_create(DMFT)
            sec_dmft.inverse_temperature = imp_params.get('beta') / ureg.eV
            sec_dmft.impurity_solver = self._solver_map.get(gen_params.get('solver'))

        def parse_meshes(method):
            pass

        params_file = get_files('*params.dat', self.filepath, self.mainfile)
        if params_file:
            if len(params_file) > 1:
                self.logger.warning('Multiple *params.dat files found; we will parse the last one!')
            self.params_parser.mainfile = params_file[-1]

            gen_parameters = dict(self.params_parser.get('general_parameters', {}).get('params', []))
            imp_parameters = dict(self.params_parser.get('impurity_parameters', {}).get('params', []))

            sec_method = sec_run.m_create(Method)
            sec_method.x_edmft_general_parameters = gen_parameters
            sec_method.x_edmft_impurity_solver_parameters = imp_parameters
            if gen_parameters and imp_parameters:
                parse_hubbard_model(sec_method, gen_parameters, imp_parameters)
                parse_dmft(sec_method, gen_parameters, imp_parameters)
                parse_meshes(sec_method)

    def parse_scc(self):
        pass

    def init_parser(self):
        self.struct_parser.mainfile = None
        self.struct_parser.logger = self.logger
        self.indmfl_parser.mainfile = self.mainfile
        self.indmfl_parser.logger = self.logger
        self.params_parser.mainfile = None
        self.params_parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.mainfile = os.path.basename(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        self.init_parser()

        # Program section
        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name='eDMFT')

        # System section
        self.parse_system()

        # Method.DMFT section
        self.parse_initial_model()
        self.parse_method()

        # Calculation section
        self.parse_scc()

        # Workflow section
        workflow = SinglePoint()
        self.archive.workflow2 = workflow
