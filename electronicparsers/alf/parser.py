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

from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, HoppingMatrix
)
from nomad.datamodel.metainfo.simulation.method import Method, QMC
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)

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
                'parameters', f'{re_n} *([\w.,# \w-]+ *: *.+)',
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

    def parse_initial_model(self, data):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)
        #sec_hoppings = sec_scc.m_create(HoppingMatrix)

        #sec_hoppings.n_orbitals = data['lattice'].attrs.get('Norb', None)

        #sec_hoppings.n_wigner_seitz_points =
        #sec_hoppings.value =

        #sec_scc.n_references = 1
        #sec_scc.calculations_ref = [sec_hoppings]

    def parse_system(self, data):
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)

        for keys in data['lattice'].attrs.keys():
            setattr(sec_system, f'x_alf_{self._lattice_map[keys]}', data['lattice'].attrs[keys])

        sec_var_lattice = sec_system.m_create(x_alf_parameters_var_lattice)
        for keys in data['parameters']['var_lattice'].attrs.keys():
            val = data['parameters']['var_lattice'].attrs[keys]
            if keys == 'lattice_type' or keys == 'model':
                val = val.decode('UTF-8') # from binary data to str
            setattr(sec_var_lattice, f'x_alf_{keys}', val)

        # Parse the lattice model as system
        sec_system.name = sec_system.x_alf_var_lattice.x_alf_lattice_type
        sec_system.type = '2D'
        sec_atoms = sec_system.m_create(Atoms)
        sec_atoms.lattice_vectors = np.vstack((
            np.append(sec_system.x_alf_a1, 0.0),
            np.append(sec_system.x_alf_a2, 0.0),
            np.array([0.0, 0.0, 1.0])))
        sec_atoms.periodic = [sec_atoms.lattice_vectors is not None] * 3
        sec_atoms.supercell_matrix = np.vstack((
            np.append(sec_system.x_alf_l1, 0.0),
            np.append(sec_system.x_alf_l2, 0.0),
            np.array([0.0, 0.0, 1.0])))
        #sec_atoms.labels
        #sec_atoms.positions

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

        # reference to an input hopping model
        self.parse_initial_model(data)

        self.parse_system(data)

        self.parse_method(data)

        self.parse_scc(data)


        '''
        sec_calc = sec_run.m_create(Calculation)

        def parse_obser(source, target):
            # observables have arbitrary shapes, need to iterate until we until 1-d
            if len(source.shape) == 1:
                target.x_alf_obser.append(x_alf_observable_data(x_afl_data=source))
                return
            for data_n in source:
                parse_obser(data_n, target)

        ### Calculation section
        for observable in self._observables:
            sec_observable = x_alf_observable()
            data_observable = data[observable]
            if 'sign' in data_observable.keys():
                sec_observable.x_alf_sign = data_observable['sign']
            if 'obser' in data_observable.keys():
                sec_observable.x_alf_obser = data_observable['obser'][:]
                # TODO determine if we need to flatten data
                # parse_obser(data_observable['obser'][:], sec_observable)
            # TODO parse other properties
            setattr(sec_calc, f'x_alf_{observable.lower()}', sec_observable)

        ### Method section
        sec_method = sec_run.m_create(Method)
        sec_input_parameters = x_alf_input_parameters()
        for key in ['var_lattice', 'var_hubbard', 'var_model_generic']:
            data_parameter = dict(data['parameters'].get(key).attrs.items())
            setattr(sec_input_parameters, f'x_alf_{key}', data_parameter)
            sec_method.x_alf_input_parameters = sec_input_parameters

        # Decoding np.bytes to str
        for key in ['lattice_type', 'model']:
            val = sec_method.x_alf_input_parameters.x_alf_var_lattice.get(key, {})
            sec_method.x_alf_input_parameters.x_alf_var_lattice.update({key : val.decode('UTF-8')})

        ### System section
        sec_system = sec_run.m_create(System)
        data_system = dict(data['lattice'].attrs.items())
        setattr(sec_system, f'x_alf_lattice', data_system)

        sec_system.name = sec_method.x_alf_input_parameters.x_alf_var_lattice['lattice_type']
        if sec_system.name in self._system_names and data_system['Ndim'] == 2:
            sec_system.type = '2D'

        sec_atoms = sec_system.m_create(Atoms)
        sec_atoms.n_atoms = 1
                            #(sec_method.x_alf_input_parameters.x_alf_var_lattice['l1'].item()) \
                            #*(sec_method.x_alf_input_parameters.x_alf_var_lattice['l2'].item())
        sec_atoms.lattice_vectors = np.array([data_system['a1'], data_system['a2']])#*e-10
        sec_atoms.positions = np.zeros((sec_atoms.n_atoms, 3))
        sec_atoms.supercell_matrix = np.zeros((3, 3))
        for i in range(data_system['Ndim']):
            sec_atoms.supercell_matrix[i][i] = sec_method.x_alf_input_parameters.x_alf_var_lattice[f'l{i+1}'].item()

        sec_atoms_orbitals = sec_system.m_create(AtomsOrbitals)
        sec_atoms_orbitals.n_orbitals = data_system['Norb']
        sec_atoms_orbitals.positions = np.zeros((sec_atoms_orbitals.n_orbitals, 3))
        for i in range(sec_atoms_orbitals.n_orbitals):
            print(i, sec_atoms_orbitals.positions[i])
            #print(type(data_system['Orbital1']))
            #sec_orbitals.positions[i].magnitude = np.pad(data_system['Orbital1'], (0, 1))
            print(sec_atoms_orbitals.positions[i].magnitude)

        #sec_atoms_group = sec_system.m_create(AtomsGroup)
        #sec_atoms_group.label = 'Unit cell'


        #sec_lattice_geometry = sec_lattice_model.m_create(LatticeGeometry)
        #sec_system.lattice_geometry.lattice_name = sec_method.x_alf_input_parameters.x_alf_var_lattice['lattice_type']

        #for key_mapping in self._system_keys_mapping.keys():
        #    print(key_mapping, self._system_keys_mapping[key_mapping])
        #    print(sec_system.x_alf_lattice[key_mapping])
            #if key_mapping == 'Orbital1':
            #    sec_system.x_alf_lattice[key_mapping] = sec_system.x_alf_lattice[key_mapping]
        #    setattr(sec_system.lattice_geometry, self._system_keys_mapping[key_mapping], sec_system.x_alf_lattice[key_mapping])

        #sec_system.lattice_geometry.lattice_vectors = np.array([data_system['a1'], data_system['a2']])
        #sec_system.lattice_geometry.Nsupercell = np.array([sec_method.x_alf_input_parameters.x_alf_var_lattice['l1'],
        #                                    sec_method.x_alf_input_parameters.x_alf_var_lattice['l2']])
        #sec_system.lattice_geometry.supercell_vectors = np.array([data_system['L1'], data_system['L2']])
        '''