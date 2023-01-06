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
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, GreensFunctions
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, HoppingMatrix, HubbardKanamoriModel, LatticeModelHamiltonian, DMFT, KMesh
)
from nomad.datamodel.metainfo.workflow import Workflow
from .metainfo.soliddmft import (
    x_soliddmft_general_parameters, x_soliddmft_solver_parameters, x_soliddmft_advanced_parameters,
    x_soliddmft_dft_input_parameters, x_soliddmft_iter_parameters, x_soliddmft_convergence_obs_parameters,
    x_soliddmft_observables_parameters
)
#from ..wannier90.parser import Wannier90Parser, WOutParser, HrParser


class SolidDMFTParser:
    def __init__(self):
        self._re_namesafe = re.compile(r'[^\w]')
        self._calculation_type = 'dmft'
        self.code_keys = ['solid_dmft', 'solver', 'triqs']
        self.skip_dataset_keys = ['afm_mapping', 'corr_shells', 'dim_reps', 'shells']
        self.input_params = {
            'general_params': x_soliddmft_general_parameters,
            'solver_params': x_soliddmft_solver_parameters,
            'advanced_params': x_soliddmft_advanced_parameters
        }
        self.dc_type = ['fll', 'held_formula', 'amf', 'fll_eg_orbitals']
        self._solver_map = {
            'cthyb': 'CT-HYB',
            'ctint': 'CT-INT',
            'ftps': 'MPS',
            'hubbardI': 'hubbard_I',
            'ctseg': 'CT-HYB'
        }
        self.angular_momentum = ['s', 'p', 'd', 'f']

    def parse_dataset(self, source, target):
        for key in source.keys():
            name = key.replace('-', '_')
            # skip afm_mapping and impurities info
            if name in self.skip_dataset_keys:
                continue

            # groups are of length = number of impurities, each one giving the value
            if isinstance(source[key], h5py.Group):
                value = []
                for i in source[key].keys():
                    value.append(source[key][i][()])
                # decoding bytes
                if all(isinstance(x, (bytes, bytearray)) for x in value):
                    value = [x.decode() for x in value]
                    if all(v == 'none' for v in value):
                        continue
            if isinstance(source[key], h5py.Dataset):
                value = source[key][()]
            # decoding bytes
                if isinstance(value, (bytes, bytearray)):
                    value = value.decode()
                    if value == 'none':
                        continue
            if isinstance(value, list):
                # if value is list, this is for each atom, hence all elements of value
                # will be either arrays or scalars
                if isinstance(value[0], np.ndarray):
                    setattr(target, f'x_soliddmft_{name}', value[:])
                else:
                    setattr(target, f'x_soliddmft_{name}', value)
            else:
                if isinstance(value, np.ndarray):
                    setattr(target, f'x_soliddmft_{name}', value[:])
                else:
                    setattr(target, f'x_soliddmft_{name}', value)

    def parse_system(self, data):
        # TODO speak with solid_dmft devs to include this info in the output
        pass

    def parse_input_model(self, data):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        sec_hamiltonian = sec_method.m_create(LatticeModelHamiltonian)

        # DFTTools code-specific input
        sec_dft_param = sec_method.m_create(x_soliddmft_dft_input_parameters)
        for param in ['dft_input', 'dft_misc_input']:
            self.parse_dataset(data.get(param), sec_dft_param)

        # HoppingMatrix || ProjectionMatrix
        sec_hamiltonian.projection_matrix = sec_dft_param.x_soliddmft_proj_mat

        # HubbardKanamoriModel
        # TODO add parse for full_slater
        # TODO add parse for crpa file
        for i in range(self.dft_input.get('n_inequiv_shells', 1)[()]):
            sec_hubbard_kanamori_model = sec_hamiltonian.m_create(HubbardKanamoriModel)

            sec_hubbard_kanamori_model.orbital = self.angular_momentum[
                self.dft_input.get('corr_shells')[str(i)].get('l', 0)[()]]
            sec_hubbard_kanamori_model.u = self.dmft_input.get('general_params').get('U')[str(i)][()]
            sec_hubbard_kanamori_model.jh = self.dmft_input.get('general_params').get('J')[str(i)][()]
            # solid_dmft keeps spin-rotational invariance
            sec_hubbard_kanamori_model.up = sec_hubbard_kanamori_model.u - 2.0 * sec_hubbard_kanamori_model.jh
            if self.dmft_input.get('general_params').get('h_int_type')[()].decode() == 'density_density':
                sec_hubbard_kanamori_model.j = 0.0
            elif self.dmft_input.get('general_params').get('h_int_type')[()].decode() == 'kanamori':
                sec_hubbard_kanamori_model.j = sec_hubbard_kanamori_model.jh

    def parse_method(self, data):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        # ref to the Non- and InteractionHamiltonian
        sec_method.starting_method_ref = sec_run.method[0]

        # Code-specific
        for param in self.input_params.keys():
            sec_param = sec_method.m_create(self.input_params[param])
            self.parse_dataset(self.dmft_input.get(param), sec_param)

        # KMesh
        sec_k_mesh = sec_method.m_create(KMesh)
        sec_k_mesh.n_points = int(self.dft_input.get('n_k', 1)[()])
        sec_k_mesh.points = self.dft_input.get('kpts')
        sec_k_mesh.weights = self.dft_input.get('kpt_weights')

        # DMFT
        sec_dmft = sec_method.m_create(DMFT)
        sec_dmft.n_atoms_per_unit_cell = self.dft_input.get('n_inequiv_shells', 1)[()]
        corr_orbs_per_atoms = []
        occ_per_atoms = []
        for i in range(sec_dmft.n_atoms_per_unit_cell):
            corr_orbs_per_atoms.append(
                self.dft_input.get('corr_shells')[str(i)].get('dim', 1)[()])
            if sec_method.x_soliddmft_general.x_soliddmft_magnetic:
                try:
                    occ_per_atoms.append(
                        self.dmft_results['observables']['imp_occ'][str(i)]['down']['0'][()] +
                        self.dmft_results['observables']['imp_occ'][str(i)]['up']['0'][()])
                except Exception:
                    self.logger.warning('The magnetic flag is true, but the occupation \
                        per atom is spin independent. Please check your outputs.')
                    occ_per_atoms.append(self.dmft_results['observables']['imp_occ'][str(i)]['0'][()])
            else:
                occ_per_atoms.append(self.dmft_results['observables']['imp_occ'][str(i)]['0'][()])
        sec_dmft.n_correlated_orbitals = corr_orbs_per_atoms
        sec_dmft.n_correlated_electrons = occ_per_atoms
        sec_dmft.inverse_temperature = sec_method.x_soliddmft_general.x_soliddmft_beta
        if sec_method.x_soliddmft_general.x_soliddmft_magnetic:
            if all(signs == 1.0 for signs in np.sign(sec_method.x_soliddmft_general.x_soliddmft_magmom)):
                sec_dmft.magnetic_state = 'ferromagnetic'
            else:
                sec_dmft.magnetic_state = 'antiferromagnetic'
        else:
            sec_dmft.magnetic_state = 'paramagnetic'
        sec_dmft.n_matsubara_freq = sec_method.x_soliddmft_general.x_soliddmft_n_iw
        sec_dmft.n_tau = sec_method.x_soliddmft_general.x_soliddmft_n_tau
        sec_dmft.double_counting_correction = self.dc_type[sec_method.x_soliddmft_general.x_soliddmft_dc_type]
        for keys in self._solver_map.keys():
            if sec_method.x_soliddmft_general.x_soliddmft_solver_type == keys:
                sec_dmft.impurity_solver = self._solver_map[keys]
                break

    def parse_scc(self, data):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)
        if hasattr(self.archive.run[-1], 'system') and len(self.archive.run[-1].system) > 0:
            sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]  # ref to DMFT

        # SCF steps
        scf_keys = [int(key.lstrip('it_')) for key in data['DMFT_results'].keys() if key.startswith('it_')]
        scf_keys.sort()
        scf_keys_sorted = ['it_' + str(key) for key in scf_keys]
        scf_keys_sorted.append('last_iter')

        for keys in scf_keys_sorted:
            sec_scf_iteration = sec_scc.m_create(ScfIteration)
        '''
        for n in range(15):
            sec_observables = sec_scc.scf_iteration[n].m_create(x_soliddmft_observables_parameters)
            for obs_key in self.dmft_results['observables'].keys():
                if obs_key.startswith('E_'):
                    value = []
                    for i in self.dmft_results['observables'][obs_key].keys():
                        value.append(
                            self.dmft_results['observables'][obs_key][i].get(keys.lstrip('it_'), 0.0)[()])
                elif obs_key == 'mu':
                    value = self.dmft_results['observables'][obs_key].get(keys.lstrip('it_'), 0.0)[()]
                else:

                if isinstance(value, list):
                    # if value is list, this is for each atom, hence all elements of value
                    # will be either arrays or scalars
                    if isinstance(value[0], np.ndarray):
                        setattr(sec_observables, f'x_soliddmft_{obs_key}', value[:])
                    else:
                        setattr(sec_observables, f'x_soliddmft_{obs_key}', value)
                else:
                    if isinstance(value, np.ndarray):
                        setattr(sec_observables, f'x_soliddmft_{obs_key}', value[:])
                    else:
                        setattr(sec_observables, f'x_soliddmft_{obs_key}', value)

        # Quantities differences for convergence in each iteration step
        #for i in range(data['DMFT_results'].get('iteration_count', 1)[()]):
            #sec_conv_obs = sec_scc.scf_iteration[i].m_create(...)
            #self.parse_dataset(self.dmft_results.get('convergence_obs'), sec_conv_obs)
            #for keys in data['DMFT_results']['convergence_obs'].keys():
            #    setattr(sec_conv_obs, f'x_soliddmft_{keys}', value)

        # Postprocessed observables
    '''

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        try:
            data = h5py.File(self.filepath)
        except Exception:
            self.logger.error('Error opening h5 file.')
            data = None

        if data is None:
            return
        try:
            self.dft_input = data.get('dft_input')
            self.dmft_input = data.get('DMFT_input')
            self.dmft_results = data.get('DMFT_results')
        except Exception:
            self.logger.error('dft_input, DMFT_input or DMFT_results Groups not found in the output file.')

        sec_run = archive.m_create(Run)

        # Program section
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'solid_dmft'
        if self.dmft_input.get('version') is not None:
            for name in self.code_keys:
                hash = self.dmft_input.get('version').get(f'{name}_hash', None)
                version = self.dmft_input.get('version').get(f'{name}_version', None)
                if hash is not None:
                    setattr(sec_program, f'x_soliddmft_{name}_hash', hash[()].decode())
                if version is not None:
                    if version[()].decode() == 'solid_dmft':
                        sec_program.version = version[()].decode()
                    else:
                        setattr(sec_program, f'x_soliddmft_{name}_version', version[()].decode())

        # System section
        # self.parse_system(data)

        # Method.DMFT section with inputs (HoppingMatrix + InteractionModel)
        self.parse_input_model(data)
        self.parse_method(data)

        # Calculation section
        self.parse_scc(data)

        # Workflow section
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
