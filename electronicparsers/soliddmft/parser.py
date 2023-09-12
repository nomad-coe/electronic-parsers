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
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, GreensFunctions
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, AtomParameters, HubbardKanamoriModel, LatticeModelHamiltonian, KMesh, FrequencyMesh,
    TimeMesh, DMFT
)
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from .metainfo.soliddmft import (
    x_soliddmft_iter_parameters, x_soliddmft_convergence_obs_parameters,
    x_soliddmft_observables_parameters
)
from nomad.parsing.parser import to_hdf5


class SolidDMFTParser:
    def __init__(self):
        self._re_namesafe = re.compile(r'[^\w]')
        self._calculation_type = 'dmft'

        self.code_keys = ['solid_dmft', 'solver', 'triqs']

        self.angular_momentum = ['s', 'p', 'd', 'f']

        self.dc_type = ['fll', 'held_formula', 'amf', 'fll_eg_orbitals']

        self._solver_map = {
            'cthyb': 'CT-HYB',
            'ctint': 'CT-INT',
            'ftps': 'MPS',
            'hubbardI': 'hubbard_I',
            'ctseg': 'CT-HYB'
        }

        self.iteration_gfs = ['Delta_time', 'G0_freq', 'Gimp_freq', 'Gimp_time', 'Sigma_freq']

        self._gf_map = {
            'Sigma_freq': 'self_energy_iw',
            'Gimp_freq': 'greens_function_iw',
            'Gimp_time': 'greens_function_tau'
        }

    def parse_dataset(self, source, target):
        def setattr_to_target(target, name, value):
            # if value is list, this is for each atom, hence all elements of value
            # will be either arrays or scalars
            if isinstance(value, list):
                if isinstance(value[0], np.ndarray) or name == 'h_int_type':
                    setattr(target, f'x_soliddmft_{name}', value[:])
                else:
                    setattr(target, f'x_soliddmft_{name}', value)
            else:
                if isinstance(value, np.ndarray):
                    setattr(target, f'x_soliddmft_{name}', value[:])
                else:
                    setattr(target, f'x_soliddmft_{name}', value)

        # scanning the keys
        for key in source.keys():
            name = key.replace('-', '_')
            # skip afm_mapping and impurities info
            if name in self.skip_dataset_keys:
                continue

            if isinstance(source[key], h5py.Dataset):
                value = source[key][()]
                if isinstance(value, bytes):  # decoding bytes to str
                    value = value.decode()
                    if value == 'none':
                        continue
            # groups are of length = number of impurities, each one giving the value
            elif isinstance(source[key], h5py.Group):
                value = []
                for i in source[key].keys():
                    if not hasattr(source[key], i):  # to avoid empty groups (e.g. 'magmom' for PM calc)
                        continue
                    value.append(source[key][i][()])
                if all(isinstance(x, bytes) for x in value):  # decoding bytes to str
                    value = [x.decode() for x in value]
                    if all(v == 'none' for v in value):
                        continue
            setattr_to_target(target, name, value)

    def parse_system(self):
        """Parses the system information and stores it under self.archive.run[0].system.
        """
        # TODO speak with solid_dmft devs to include this info in the output
        sec_run = self.archive.run[-1]
        if self.dft_input.get('kpt_basis'):
            sec_system = sec_run.m_create(System)
            sec_atoms = sec_system.m_create(Atoms)
            sec_atoms.lattice_vectors_reciprocal = self.dft_input.get('kpt_basis')[()] / ureg.angstrom
        else:
            pass

    def parse_input_model(self, data):
        """Parses the input model and stores it under self.archive.run[0].method[0] and it
        is composed of:
            1- the projection matrix
            2- the Hubbard-Kanamori parameters.

        Args:
            data (HDF5file): the data read from the mainfile .h5 file.
        """
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        sec_hamiltonian = sec_method.m_create(LatticeModelHamiltonian)

        # DFTTools code-specific input
        for group_name in ['dft_input', 'dft_misc_input', 'dft_symmcorr_input']:
            if not data.get(group_name):
                continue
            params = {}
            for keys, values in data.get(group_name).items():
                if isinstance(values, h5py.Dataset):
                    if not isinstance(values[()], np.ndarray):
                        val = values[()].decode() if type(values[()]) == bytes else values[()]
                        params[keys] = val
            sec_method.m_set(sec_method.m_get_quantity_definition(f'x_soliddmft_{group_name}'), params)

        # HoppingMatrix || ProjectionMatrix
        sec_hamiltonian.projection_matrix = self.dft_input.get('proj_mat')[()][:, 0, :, :, :, 0] \
            + self.dft_input.get('proj_mat')[()][:, 0, :, :, :, 1] * 1j

        # HubbardKanamoriModel
        # TODO add parse for full_slater
        # TODO add parse for crpa file
        n_impurities = self.dft_input.get('n_inequiv_shells')[()] if self.dft_input.get('n_inequiv_shells') else 1
        for i in range(n_impurities):
            sec_atom_parameters = sec_method.m_create(AtomParameters)
            atom_impurity = self.dft_input.get('corr_shells')
            if atom_impurity:
                atom_index = atom_impurity.get(f'{i}').get('atom')
                sec_atom_parameters.atom_index = atom_index[()] if atom_index else None
                n_orbitals = atom_impurity.get(f'{i}').get('dim')
                l_number = atom_impurity.get(f'{i}').get('l')
                if n_orbitals and l_number:
                    sec_atom_parameters.n_orbitals = n_orbitals[()]
                    angular_momentum = self.angular_momentum[l_number[()]]
                    orbital_labels = [f'{angular_momentum}{ml}' for ml in range(n_orbitals[()])]
                    sec_atom_parameters.orbitals = orbital_labels

            sec_hubbard_kanamori_model = sec_atom_parameters.m_create(HubbardKanamoriModel)
            sec_hubbard_kanamori_model.u = self.dmft_input['general_params']['U'][str(i)][()] * ureg.eV
            sec_hubbard_kanamori_model.jh = self.dmft_input['general_params']['J'][str(i)][()] * ureg.eV
            # solid_dmft keeps spin-rotational invariance
            sec_hubbard_kanamori_model.up = sec_hubbard_kanamori_model.u - 2.0 * sec_hubbard_kanamori_model.jh
            # issue with def of 'h_int_type' in the output h5 in different versions
            if isinstance(self.dmft_input['general_params']['h_int_type'], h5py.Dataset):
                h_int_type = self.dmft_input['general_params']['h_int_type'][()]
            elif isinstance(self.dmft_input['general_params']['h_int_type'], h5py.Group):
                h_int_type = self.dmft_input['general_params']['h_int_type'][str(i)][()]
            if h_int_type == b'density_density':
                sec_hubbard_kanamori_model.j = 0.0
            elif h_int_type == b'kanamori':
                sec_hubbard_kanamori_model.j = sec_hubbard_kanamori_model.jh
            sec_hubbard_kanamori_model.double_counting_correction = self.dc_type[
                self.dmft_input['general_params'].get('dc_type', 0)[()]]  # set to 'fll' by default

    def parse_method(self):
        """Parses DMFT and code-specific metadata from 'DMFT_input' and stores it under
        self.archive.run[0].method[1].
        """
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        # ref to the Non- and InteractionHamiltonian
        sec_method.starting_method_ref = sec_run.method[0]

        # Code-specific
        for group_name in ['general_params', 'solver_params', 'advanced_params']:
            if not self.dmft_input.get(group_name):
                continue
            params = {}
            for keys, values in self.dmft_input.get(group_name).items():
                if isinstance(values, h5py.Dataset):
                    if not values.shape:
                        val = values[()].decode() if type(values[()]) == bytes else values[()]
                        params[keys] = val
            sec_method.m_set(sec_method.m_get_quantity_definition(f'x_soliddmft_{group_name}'), params)

        # KMesh
        sec_k_mesh = sec_method.m_create(KMesh)
        n_k = self.dft_input.get('n_k')
        sec_k_mesh.n_points = n_k[()] if n_k else 1
        kpts = self.dft_input.get('kpts')
        sec_k_mesh.points = np.complex128(kpts[()]) if kpts else None
        kpt_weights = self.dft_input.get('kpt_weights')
        sec_k_mesh.weights = kpt_weights[()] if kpt_weights else None

        # DMFT
        sec_dmft = sec_method.m_create(DMFT)
        n_impurities = self.dft_input.get('n_inequiv_shells')
        sec_dmft.n_impurities = n_impurities[()] if n_impurities else 1
        try:
            impurity_orbitals = []
            impurity_occupation = []
            for i in range(n_impurities):
                n_orbitals = self.dft_input.get('corr_shells', {}).get(f'{i}', {}).get('dim', 1)
                impurity_orbitals.append(n_orbitals[()])
                occupation = self.dmft_results.get('observables', {}).get('imp_occ', {}).get(f'{i}')
                total_occupation = occupation['down']['0'][()] + occupation['up']['0'][()]
                impurity_occupation.append(total_occupation)
            sec_dmft.n_correlated_orbitals = impurity_orbitals
            sec_dmft.n_electrons = impurity_occupation
        except Exception:
            self.logger.warning('Could not set the impurity number of orbitals and nominal occupation.')
        beta = self.dmft_input.get('general_params', {}).get('beta')
        sec_dmft.inverse_temperature = beta[()] / ureg.eV if beta else None
        magnetic_flag = self.dmft_input.get('general_params', {}).get('magnetic')[()] if self.dmft_input.get('general_params', {}).get('magnetic') else False
        if magnetic_flag:
            magmom = self.dmft_input.get('general_params', {}).get('magmom')
            if magmom:
                magmom = magmom[()]
                if all(signs == 1.0 for signs in np.sign(magmom)):
                    sec_dmft.magnetic_state = 'ferromagnetic'
                else:
                    sec_dmft.magnetic_state = 'antiferromagnetic'
            else:
                self.logger.warning('The magnetic flag is set to true, but the initial magnetic moment is not resolved. '
                                    'Is this really a magnetic calculation without an initial magmom seed?')
        else:
            sec_dmft.magnetic_state = 'paramagnetic'
        solver_type = self.dmft_input.get('general_params', {}).get('solver_type')
        if solver_type:
            sec_dmft.impurity_solver = self._solver_map[keys]

        # FrequencyMesh
        if sec_method.m_xpath('x_soliddmft_general.x_soliddmft_n_iw'):
            n_iw = sec_method.x_soliddmft_general.x_soliddmft_n_iw
            iw = np.array([(2 * (n - n_iw) + 1) * 1j / beta for n in range(2 * n_iw)])
            iw = iw.reshape((len(iw), 1))
            sec_freq_mesh = FrequencyMesh(dimensionality=1, n_points=n_iw, points=iw * ureg.eV)
            sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
        # TimeMesh
        if sec_method.m_xpath('x_soliddmft_general.x_soliddmft_n_tau'):
            n_tau = sec_method.x_soliddmft_general.x_soliddmft_n_tau
            tau = np.array([n * beta * 1j / (n_tau - 1) for n in range(n_tau)])
            tau = tau.reshape((len(tau), 1))
            sec_time_mesh = TimeMesh(dimensionality=1, n_points=n_tau, points=tau)
            sec_method.m_add_sub_section(Method.time_mesh, sec_time_mesh)

    def parse_scc(self):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)
        sec_scc.system_ref = sec_run.system[-1] if sec_run.system else None
        sec_scc.method_ref = sec_run.method[-1]  # ref to DMFT

        def parse_iteration_quantities(scf_section, it_key):
            sec_iter = scf_section.m_create(x_soliddmft_iter_parameters)
            # DC_energ
            param = []
            for i in self.dmft_results[it_key]['DC_energ'].keys():
                param.append(self.dmft_results[it_key]['DC_energ'][i][()])
            sec_iter.x_soliddmft_DC_energ = param
            # DC_pot
            param = []
            for i in self.dmft_results[it_key]['DC_pot'].keys():
                for s in self.dmft_results[it_key]['DC_pot'][i].keys():
                    param.append(self.dmft_results[it_key]['DC_pot'][i][s][()])
            sec_iter.x_soliddmft_DC_pot = param
            # chemical_potential_pre and _post
            sec_iter.x_soliddmft_chemical_potential_pre = self.dmft_results[it_key]['chemical_potential_pre'][()]
            sec_iter.x_soliddmft_chemical_potential_post = self.dmft_results[it_key]['chemical_potential_post'][()]
            # dens_mat_pre and _post
            for key in ['dens_mat_pre', 'dens_mat_post']:
                param = []
                for i in self.dmft_results[it_key][key].keys():
                    for s in self.dmft_results[it_key][key][i].keys():
                        param.append(self.dmft_results[it_key][key][i][s][()])
                setattr(sec_iter, f'x_soliddmft_{key}', np.array(param)[:, 0, 0, :])  # deleting useless indices
            # GF quantities
            for gf_key in self.iteration_gfs:
                param = []
                for i in range(sec_scc.method_ref.dmft.n_impurities):  # atom index
                    gf_key_mod = f'{gf_key}_{i}'
                    for s in self.dmft_results[it_key][gf_key_mod].keys():
                        if s == 'block_names':
                            continue
                        param.append(self.dmft_results[it_key][gf_key_mod][s]['data'][()])
                setattr(sec_iter, f'x_soliddmft_{gf_key}', np.array(param)[:, :, 0, 0, :])

        # SCF steps
        scf_keys = [int(key.lstrip('it_')) for key in self.dmft_results.keys() if key.startswith('it_')]
        scf_keys.sort()
        scf_keys_sorted = [f'it_{key}' for key in scf_keys]

        # We store the last post-processed step for observables
        total_iterations = self.dmft_results.get('iteration_count', 1)[()]
        for it in range(total_iterations + 1):
            sec_scf_iteration = sec_scc.m_create(ScfIteration)

            if it < total_iterations:
                # iterations quantities
                it_key = f'it__{it + 1}'
                if it_key in scf_keys_sorted:
                    parse_iteration_quantities(sec_scf_iteration, it_key)

                # convergence of observable quantities
                sec_conv_obs = sec_scc.scf_iteration[it].m_create(x_soliddmft_convergence_obs_parameters)
                for keys in self.dmft_results['convergence_obs'].keys():
                    if keys == 'iteration':  # skipping unused keys
                        continue
                    if len(self.dmft_results['convergence_obs'][keys]) > 0:
                        if keys == 'd_Etot' or keys == 'd_mu':
                            param = self.dmft_results['convergence_obs'][keys][str(it)][()]
                        else:
                            param = []
                            for i in self.dmft_results['convergence_obs'][keys].keys():
                                param.append(self.dmft_results['convergence_obs'][keys][i][str(it)][()])
                        setattr(sec_conv_obs, f'x_soliddmft_{keys}', param)

            # observables quantities
            sec_obs = sec_scc.scf_iteration[it].m_create(x_soliddmft_observables_parameters)
            for keys in self.dmft_results['observables'].keys():
                if keys == 'iteration':  # skipping unused keys
                    continue
                if keys.startswith('E_'):
                    if len(self.dmft_results['observables'][keys]) > sec_scc.method_ref.dmft.n_impurities:
                        if self.dmft_results['observables'][keys][str(it)][()] != b'none':
                            param = self.dmft_results['observables'][keys][str(it)][()]
                    else:
                        param = []
                        for i in self.dmft_results['observables'][keys].keys():
                            if len(self.dmft_results['observables'][keys][i]) == total_iterations + 1:
                                if self.dmft_results['observables'][keys][i][str(it)][()] != b'none':
                                    param.append(self.dmft_results['observables'][keys][i][str(it)][()])
                elif keys == 'mu':
                    param = self.dmft_results['observables']['mu'][str(it)]
                else:
                    param = []
                    for i in self.dmft_results['observables'][keys].keys():
                        for s in self.dmft_results['observables'][keys][i].keys():
                            param.append(self.dmft_results['observables'][keys][i][s][str(it)][()])
                setattr(sec_obs, f'x_soliddmft_{keys}', param)

            # Chemical potential
            if sec_scc.scf_iteration[it].x_soliddmft_observables.x_soliddmft_mu:
                sec_energy = sec_scc.scf_iteration[it].m_create(Energy)
                sec_energy.fermi = sec_scc.scf_iteration[it].x_soliddmft_observables.x_soliddmft_mu * ureg.eV

        # last iteration quantities
        parse_iteration_quantities(sec_scf_iteration, 'last_iter')

        # Greens functions quantities
        sec_gf = sec_scc.m_create(GreensFunctions)
        beta = sec_scc.method_ref.x_soliddmft_general.x_soliddmft_beta
        n_tau = sec_scc.method_ref.x_soliddmft_general.x_soliddmft_n_tau
        n_iw = sec_scc.method_ref.x_soliddmft_general.x_soliddmft_n_iw
        sec_gf.tau = [n * beta / (n_tau - 1) for n in range(n_tau)]
        sec_gf.matsubara_freq = [(2 * (n - n_iw) + 1) / beta for n in range(2 * n_iw)]
        sec_gf.chemical_potential = sec_scc.scf_iteration[-1].x_soliddmft_observables.x_soliddmft_mu * ureg.eV
        nat = sec_scc.method_ref.dmft.n_impurities
        norb = sec_scc.method_ref.dmft.n_correlated_orbitals
        for keys in self._gf_map.keys():
            funct = getattr(sec_scc.scf_iteration[-1].x_soliddmft_iter, f'x_soliddmft_{keys}')[:, :, 0] \
                + getattr(sec_scc.scf_iteration[-1].x_soliddmft_iter, f'x_soliddmft_{keys}')[:, :, 1] * 1j
            if keys.endswith('freq'):
                naxis = 2 * n_iw
            else:
                naxis = n_tau
            if np.all(norb != norb[0]):
                self.logger.warning('Greens function matrices are set up using the number of orbitals from the impurity 0. '
                                    'We found different number of orbitals per impurity. Is this physically correct?')
            setattr(sec_gf, self._gf_map[keys], np.reshape(funct, (nat, 2, norb[0], naxis)))
        sec_gf.orbital_occupations = np.reshape(sec_scc.scf_iteration[-1].x_soliddmft_observables.x_soliddmft_orb_occ, (nat, 2, norb[0]))
        sec_gf.quasiparticle_weights = np.reshape(sec_scc.scf_iteration[-1].x_soliddmft_observables.x_soliddmft_orb_Z, (nat, 2, norb[0]))

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
            return
        self.dft_input = data.get('dft_input')
        self.dmft_input = data.get('DMFT_input')
        self.dmft_results = data.get('DMFT_results')

        sec_run = archive.m_create(Run)

        # Program section
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'solid_dmft'
        if self.dmft_input['version'] is not None:
            for name in self.code_keys:
                hash = self.dmft_input['version'].get(f'{name}_hash', None)
                version = self.dmft_input['version'].get(f'{name}_version', None)
                if hash is not None:
                    if name == 'solid_dmft':
                        sec_program.x_soliddmft_hash = hash[()].decode()
                    else:
                        setattr(sec_program, f'x_soliddmft_{name}_hash', hash[()].decode())
                if version is not None:
                    if name == 'solid_dmft':
                        sec_program.version = version[()].decode()
                    else:
                        setattr(sec_program, f'x_soliddmft_{name}_version', version[()].decode())

        # System section
        self.parse_system()

        # Method.DMFT section with inputs (HoppingMatrix + InteractionModel)
        self.parse_input_model(data)
        self.parse_method()

        # Calculation section
        self.parse_scc()

        # Workflow section
        workflow = SinglePoint()
        self.archive.workflow2 = workflow
