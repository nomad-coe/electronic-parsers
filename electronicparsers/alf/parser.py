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

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, HoppingMatrix
)
from nomad.datamodel.metainfo.simulation.method import Method, QMC
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.workflow import Workflow

from .metainfo.alf import (
    x_alf_parameters_var_lattice, x_alf_parameters_var_hubbard,
    x_alf_parameters_var_model_generic, x_alf_observable_eqtau_data,
    x_alf_observable_scal_data
)

re_n = r'[\n\r]'


class InfoParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        def str_to_params(val_in):
            val = [v.strip() for v in val_in.split(':', 1)]
            return (val_in, val, val[0])

        self._quantities = [
            Quantity(
                'parameters', rf'{re_n} *([\w.,# \w-]+ *: *.+)',
                repeats=True, str_operation=str_to_params),
            Quantity(
                'program_commit', r'commit\s*(\w+)',
                dtype=str, flatten=False),
            Quantity(
                'program_branch', r'branch\s*([\w-]+)',
                dtype=str, flatten=False),
            Quantity(
                'number_of_bins', r'\s*Effective number of bins\s*:\s*([\w-]+)',
                flatten=False),
            Quantity(
                'number_of_sweeps', r'\s*Sweeps\s*:\s*([\w-]+)',
                flatten=False),
            Quantity(
                'number_of_wraps', r'Wrap\s*:\s*([\w-]+)',
                flatten=False)
        ]


class ALFParser:
    def __init__(self):
        self.info_parser = InfoParser()

        self._lattice_map = {
            'L1': 'l1',
            'L2': 'l2',
            'N_coord': 'n_coord',
            'Ndim': 'n_dim',
            'Norb': 'n_orb',
            'Orbital1': 'orbital',
            'Orbital2': 'orbital',
            'Orbital3': 'orbital',
            'Orbital4': 'orbital',
            'Orbital5': 'orbital',
            'a1': 'a1',
            'a2': 'a2'
        }

        self._parameters_map = {
            'var_hubbard': x_alf_parameters_var_hubbard,
            'var_model_generic': x_alf_parameters_var_model_generic
        }

        self._observables_map = {
            'eqtau': {
                'Den_eq', 'Den_tau', 'Green_eq', 'Green_tau', 'SpinT_eq', 'SpinXY_eq',
                'SpinXY_tau', 'SpinZ_eq', 'SpinZ_tau'
            },
            'scal': {
                'Ener_scal', 'Kin_scal', 'Part_scal', 'Pot_scal'
            }
        }

    def parse_system(self, data):
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)

        norb = data['lattice'].attrs.get('Norb')
        ndim = data['lattice'].attrs.get('Ndim')
        orbital_position = np.zeros((ndim, norb))
        for keys in data['lattice'].attrs.keys():
            if 'Orbital' in keys:
                np.append(orbital_position, data['lattice'].attrs.get(keys))
            else:
                setattr(sec_system, f'x_alf_{self._lattice_map[keys]}', data['lattice'].attrs.get(keys))
        sec_system.x_alf_orbital = orbital_position

        sec_var_lattice = sec_system.m_create(x_alf_parameters_var_lattice)
        for keys in data['parameters']['var_lattice'].attrs.keys():
            val = data['parameters']['var_lattice'].attrs.get(keys)
            if keys == 'lattice_type' or keys == 'model':
                val = val.decode('UTF-8')  # from binary data to str
            setattr(sec_var_lattice, f'x_alf_{keys}', val)

        # Parse the lattice model as system
        sec_system.name = sec_system.x_alf_var_lattice.x_alf_lattice_type
        sec_system.type = '2D'
        sec_system.is_representative = True
        sec_atoms = sec_system.m_create(Atoms)
        sec_atoms.lattice_vectors = np.vstack((
            np.append(sec_system.x_alf_a1, 0.0) * ureg.angstrom,
            np.append(sec_system.x_alf_a2, 0.0) * ureg.angstrom,
            np.array([0.0, 0.0, 4.0]) * ureg.angstrom))  # arbitrary Z direction def
        sec_atoms.periodic = [True, True, False]
        # QMC supercell definition
        n_l1 = sec_system.x_alf_var_lattice.x_alf_l1
        n_l2 = sec_system.x_alf_var_lattice.x_alf_l2
        labels = ['X'] * (n_l1 * n_l2)
        positions = [[[i / n_l1, j / n_l2, 0.0] for j in range(n_l2)] for i in range(n_l1)]
        sec_atoms.labels = labels
        sec_atoms.positions = np.vstack(positions * ureg.angstrom)

    def parse_initial_model(self, data):
        sec_run = self.archive.run[-1]

        sec_scc = sec_run.m_create(Calculation)
        sec_scc.method_ref = sec_run.method[-1]
        sec_scc.system_ref = sec_run.system[-1]
        sec_hoppings = sec_scc.m_create(HoppingMatrix)

        # TODO populate after talking with Jefferson and Jonas
        if sec_run.system is not None:
            sec_hoppings.n_orbitals = sec_run.system[0].x_alf_n_orb

            # hr = [x, y, z, orb1, orb2, ret]
            # sec_hoppings.n_wigner_seitz_points =
            # sec_hoppings.value = ...

    def parse_method(self, data):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        for param_keys in data['parameters'].keys():
            if param_keys != 'var_lattice':
                sec_parameters = sec_method.m_create(self._parameters_map[param_keys])
                for keys in data['parameters'][param_keys].attrs.keys():
                    setattr(sec_parameters, f'x_alf_{keys}', data['parameters'][param_keys].attrs[keys])

        # QMC metainfo
        sec_qmc = sec_method.m_create(QMC)
        # sec_qmc.t0 = sec_method.x_alf_var_hubbard.x_alf_ham_t
        sec_qmc.U = sec_method.x_alf_var_hubbard.x_alf_ham_u
        sec_qmc.V = sec_method.x_alf_var_hubbard.x_alf_ham_u2
        sec_qmc.chemical_potential = sec_method.x_alf_var_hubbard.x_alf_ham_chem
        sec_qmc.inverse_temperature = sec_method.x_alf_var_model_generic.x_alf_beta
        sec_qmc.dtau = sec_method.x_alf_var_model_generic.x_alf_dtau
        info_files = [f for f in os.listdir(self.maindir) if f.endswith('info')]
        if info_files:
            if len(info_files) > 1:
                self.logger.warn('Multiple info output files found.')

            self.info_parser.mainfile = os.path.join(self.maindir, info_files[0])
            sec_qmc.n_bins = self.info_parser.get('number_of_bins')
            sec_qmc.n_sweeps = self.info_parser.get('number_of_sweeps')
            sec_qmc.n_wraps = self.info_parser.get('number_of_wraps')
        if sec_run.system[0].x_alf_var_lattice is not None:
            model_name = [sec_run.system[0].x_alf_var_lattice.x_alf_lattice_type, sec_run.system[0].x_alf_var_lattice.x_alf_model]
            sec_qmc.model_name = ' '.join(model_name)

    def parse_scc(self, data):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)
        sec_scc.method_ref = sec_run.method[-1]
        sec_scc.system_ref = sec_run.system[-1]
        sec_scc.calculations_ref = [sec_run.calculation[0]]

        # Equilibrium and tau quantities
        for observable in self._observables_map['eqtau']:
            sec_observable = x_alf_observable_eqtau_data()
            if 'obser' in data[observable].keys():
                sec_observable.x_alf_obser = data[observable]['obser']
            if 'back' in data[observable].keys():
                sec_observable.x_alf_back = data[observable]['back']
            if 'sign' in data[observable].keys():
                sec_observable.x_alf_sign = data[observable]['sign']
            setattr(sec_scc, f'x_alf_{observable.lower()}', sec_observable)

        # Scalar quantities
        for observable in self._observables_map['scal']:
            sec_observable = x_alf_observable_scal_data()
            if 'obser' in data[observable].keys():
                sec_observable.x_alf_obser = data[observable]['obser']
            if 'sign' in data[observable].keys():
                sec_observable.x_alf_sign = data[observable]['sign']
            setattr(sec_scc, f'x_alf_{observable.lower()}', sec_observable)

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.maindir = os.path.dirname(self.filepath)

        try:
            data = h5py.File(self.filepath)
        except Exception:
            self.logger.error('Error opening h5 file.')
            data = None

        if data is None:
            return

        sec_run = archive.m_create(Run)

        # Program section
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'ALF'
        info_files = [f for f in os.listdir(self.maindir) if f.endswith('info')]
        if info_files:
            if len(info_files) > 1:
                self.logger.warn('Multiple info output files found.')

            self.info_parser.mainfile = os.path.join(self.maindir, info_files[0])

            commit = self.info_parser.get('program_commit', '')
            if commit:
                sec_program.x_alf_commit_hash = commit
            branch = self.info_parser.get('program_branch', '')
            if branch:
                sec_program.x_alf_commit_branch = branch

        self.parse_system(data)

        self.parse_method(data)

        # reference to an input hopping model
        self.parse_initial_model(data)

        # QMC calculation
        self.parse_scc(data)

        sec_workflow = archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
