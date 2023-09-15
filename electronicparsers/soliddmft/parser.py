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
    Calculation, ScfIteration, Energy, EnergyEntry, GreensFunctions
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, AtomParameters, HubbardKanamoriModel, KMesh, FrequencyMesh,
    TimeMesh, DMFT
)
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from .metainfo.soliddmft import x_soliddmft_observables_parameters
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

        self.iteration_gfs = ['Delta_time', 'Delta_freq', 'G0_freq', 'Gimp_freq', 'Gimp_time', 'Sigma_freq']

        self.observable_gfs = ['imp_gb2', 'imp_occ', 'orb_Z', 'orb_gb2', 'orb_occ']

        self._gf_map = {
            'Sigma_freq': 'self_energy_iw',
            'Gimp_freq': 'greens_function_iw',
            'Gimp_time': 'greens_function_tau'
        }

        self._gf_freq_map = {
            'real': {
                'Delta_freq': 'hybridization_function_freq',
                'Gimp_freq': 'greens_function_freq',
                'Sigma_freq': 'self_energy_freq',
                'Gimp_time': 'greens_function_tau'
            },
            'matsubara': {
                'Delta_freq': 'hybridization_function_iw',
                'Gimp_freq': 'greens_function_iw',
                'Sigma_freq': 'self_energy_iw',
                'Gimp_time': 'greens_function_tau'
            }
        }

    def _type_encoder_JSON(self, quantity):
        if isinstance(quantity, np.bool_):
            return bool(quantity)
        if isinstance(quantity, np.int32) or isinstance(quantity, np.int64):
            return int(quantity)
        if isinstance(quantity, np.float64):
            return float(quantity)

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

        # DFTTools code-specific input
        for group_name in ['dft_input', 'dft_misc_input', 'dft_symmcorr_input']:
            if not data.get(group_name):
                continue
            params = {}
            for keys, values in data.get(group_name).items():
                if isinstance(values, h5py.Dataset):
                    if not isinstance(values[()], np.ndarray):
                        val = values[()].decode() if type(values[()]) == bytes else values[()]
                        params[keys] = self._type_encoder_JSON(val)
            sec_method.m_set(sec_method.m_get_quantity_definition(f'x_soliddmft_{group_name}'), params)

        # HoppingMatrix || ProjectionMatrix
        sec_method.x_soliddmft_projection_matrix = self.dft_input.get('proj_mat')[()][:, 0, :, :, :, 0] \
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
                        params[keys] = self._type_encoder_JSON(val)
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
            for i in range(n_impurities[()]):
                n_orbitals = self.dft_input.get('corr_shells', {}).get(f'{i}', {}).get('dim', 1)
                impurity_orbitals.append(n_orbitals[()])
                occupation = self.dmft_results.get('observables', {}).get('imp_occ', {}).get(f'{i}')
                total_occupation = occupation['down']['0'][()] + occupation['up']['0'][()]
                impurity_occupation.append(total_occupation)
            sec_dmft.n_correlated_orbitals = impurity_orbitals
            sec_dmft.n_electrons = impurity_occupation
        except Exception:
            self.logger.warning('Could not set the impurity number of orbitals and nominal occupation.')
        dmft_general_params = self.dmft_input.get('general_params', {})
        beta = dmft_general_params.get('beta')
        if beta:
            beta = beta[()]
            sec_dmft.inverse_temperature = beta / ureg.eV
        magnetic_flag = dmft_general_params.get('magnetic')[()] if self.dmft_input.get('general_params', {}).get('magnetic') else False
        if magnetic_flag:
            magmom = dmft_general_params.get('magmom')
            if len(magmom) > 0:
                magmom = [magmom.get(keys)[()] for keys in magmom.keys()]
                if all(signs == 1.0 for signs in np.sign(magmom)):
                    sec_dmft.magnetic_state = 'ferromagnetic'
                else:
                    sec_dmft.magnetic_state = 'antiferromagnetic'
            else:
                self.logger.warning('The magnetic flag is set to true, but the initial magnetic moment is not resolved. '
                                    'Is this really a magnetic calculation without an initial magmom seed?')
        else:
            sec_dmft.magnetic_state = 'paramagnetic'
        solver_type = dmft_general_params.get('solver_type')
        if solver_type:
            sec_dmft.impurity_solver = self._solver_map[solver_type[()].decode()]

        # MatsFrequencyMesh
        n_iw = dmft_general_params.get('n_iw')
        if n_iw:
            n_iw = n_iw[()]
            iw = np.array([(2 * (n - n_iw) + 1) * 1j / beta for n in range(2 * n_iw)])
            iw = iw.reshape((len(iw), 1))
            sec_freq_mesh = FrequencyMesh(dimensionality=1, n_points=n_iw, points=iw * ureg.eV)
            sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
        # TimeMesh
        n_tau = dmft_general_params.get('n_tau')
        if n_tau:
            n_tau = n_tau[()]
            tau = np.array([n * beta * 1j / (n_tau - 1) for n in range(n_tau)])
            tau = tau.reshape((len(tau), 1))
            sec_time_mesh = TimeMesh(dimensionality=1, n_points=n_tau, points=tau)
            sec_method.m_add_sub_section(Method.time_mesh, sec_time_mesh)
        # FrequencyMesh
        n_w = dmft_general_params.get('n_w')
        if n_w:
            n_w = n_w[()]
            w_min = dmft_general_params.get('w_range', {}).get('0')[()] if dmft_general_params.get('w_range', {}).get('0') else 0.0
            w_max = dmft_general_params.get('w_range', {}).get('1')[()] if dmft_general_params.get('w_range', {}).get('1') else 0.0
            freq = np.linspace(w_min, w_max, n_w)
            sec_freq_mesh = FrequencyMesh(dimensionality=1, n_points=n_w, points=freq * ureg.eV)
            sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)

    def parse_scc(self):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)
        sec_scc.system_ref = sec_run.system[-1] if sec_run.system else None
        sec_scc.method_ref = sec_run.method[-1]  # ref to DMFT

        # Resolving h5 path for to_hdf5 method
        filename = os.path.join(os.path.dirname(self.filepath.split("/raw/")[-1]), self.mainfile)
        farg = 'r+b'  # Always reading the h5 mainfile

        # SCF steps
        scf_keys = [int(key.lstrip('it_')) for key in self.dmft_results.keys() if key.startswith('it_')]
        scf_keys.sort()
        n_iter_scf = self.dmft_results.get('iteration_count')[()] if self.dmft_results.get('iteration_count') else 1

        if len(scf_keys) != n_iter_scf:
            self.logger.warning('Number of it_n steps for DMFT results is different from the iteration '
                                'count stored in the h5 file.')

        n_impurities = self.dft_input.get('n_inequiv_shells')[()]
        convergence_obs = self.dmft_results.get('convergence_obs', {})
        observables = self.dmft_results.get('observables', {})
        if self.archive.m_context:
            with self.archive.m_context.raw_file(filename, farg) as f:
                for i_scf in range(len(scf_keys)):
                    sec_scf = sec_scc.m_create(ScfIteration)
                    # Convergence of the observables per scf iteration step
                    conv_obs = {}
                    for keys, values in convergence_obs.items():
                        if len(values) > 0 and keys != 'iteration':
                            if keys == 'd_mu':
                                conv_obs[keys] = self._type_encoder_JSON(values.get(f'{i_scf}')[()])
                            else:
                                for i_imp in range(n_impurities):
                                    if keys == 'd_orb_occ':
                                        d_orb_occ = values.get(f'{i_imp}')[f'{i_scf}']
                                        sec_scf.x_soliddmft_convergence_orb_occ = d_orb_occ[()] if d_orb_occ else None
                                    else:
                                        conv_obs[f'{keys}_imp{i_imp}'] = self._type_encoder_JSON(values.get(f'{i_imp}')[f'{i_scf}'][()])
                    sec_scf.x_soliddmft_convergence_obs = conv_obs

                    # Energy per scf iteration step
                    sec_energy = sec_scf.m_create(Energy)
                    total_energy = observables.get('E_tot', {}).get(f'{i_scf + 1}')
                    total_energy = total_energy[()] * ureg.eV if total_energy else None
                    sec_energy.total = EnergyEntry(value=total_energy)
                    chemical_potential = observables.get('mu', {}).get(f'{i_scf + 1}')
                    sec_energy.chemical_potential = chemical_potential[()] * ureg.eV if chemical_potential else None
                    dc_energy = []
                    for i_imp in range(n_impurities):
                        dc_energy_atom = observables.get('E_DC', {}).get(f'{i_imp}').get(f'{i_scf + 1}')
                        if dc_energy_atom:
                            dc_energy.append(dc_energy_atom[()])
                    sec_energy.double_counting = EnergyEntry(values_per_atom=dc_energy * ureg.eV)

                    # Observables per scf iteration step
                    scf_iteration = self.dmft_results.get(f'it_{i_scf + 1}')
                    for i_imp in range(n_impurities):
                        sec_obs_scf = sec_scf.m_create(x_soliddmft_observables_parameters)
                        for gf_iteration in self.iteration_gfs:
                            if f'{gf_iteration}_{i_imp}' in scf_iteration.keys():
                                value_per_spin_orbital = scf_iteration.get(f'{gf_iteration}_{i_imp}')
                                value_tot = []
                                for spin_orb in value_per_spin_orbital.keys():
                                    if spin_orb == 'block_names':
                                        continue
                                    value = value_per_spin_orbital.get(spin_orb).get('data')
                                    value = to_hdf5(value, f, f'DMFT_results/it_{i_scf + 1}/{gf_iteration}_{i_imp}/{spin_orb}/data')
                                    value_tot.append(value)
                                sec_obs_scf.m_set(sec_obs_scf.m_get_quantity_definition(f'x_soliddmft_{gf_iteration}'), value_tot)
                        for gf_observable in self.observable_gfs:
                            if gf_observable in observables.keys():
                                value_per_spin_orbital = observables.get(gf_observable).get(f'{i_imp}')
                                value_tot = []
                                for spin_orb in value_per_spin_orbital.keys():
                                    value = value_per_spin_orbital.get(spin_orb).get(f'{i_scf + 1}')
                                    value = to_hdf5(value, f, f'DMFT_results/observables/{gf_observable}/{i_imp}/{spin_orb}/{i_scf + 1}')
                                    value_tot.append(value)
                                sec_obs_scf.m_set(sec_obs_scf.m_get_quantity_definition(f'x_soliddmft_{gf_observable}'), value_tot)

        # Greens functions quantities
        sec_gfs = sec_scc.m_create(GreensFunctions)
        # First, store energies
        dmft_last_iter = self.dmft_results.get('last_iter')
        sec_energy = sec_scc.m_create(Energy)
        if dmft_last_iter.get('DC_energ'):
            dc_energy = [dmft_last_iter.get('DC_energ').get(keys)[()] for keys in dmft_last_iter.get('DC_energ')]
            sec_energy.double_counting = EnergyEntry(values_per_atom=dc_energy * ureg.eV)
        chemical_potential = dmft_last_iter.get('chemical_potential_post')[()] * ureg.eV if dmft_last_iter.get('chemical_potential_post') else None
        if chemical_potential:
            sec_energy.chemical_potential = chemical_potential
            sec_gfs.chemical_potential = chemical_potential
        # Then, store GFs
        axes_label = ''
        for freq_mesh in sec_scc.method_ref.frequency_mesh:
            points = freq_mesh.points.to('eV').magnitude
            if np.isreal(points).all():
                sec_gfs.frequencies = np.real(points)
                axes_label = 'real'
            else:
                sec_gfs.matsubara_freq = np.imag(points)
                axes_label = 'matsubara'
        axes = self._gf_freq_map[axes_label]
        if sec_scc.method_ref.time_mesh:
            sec_gfs.tau = sec_scc.method_ref.time_mesh[0].points.imag

        if sec_scc.method_ref.dmft.n_correlated_orbitals is not None:
            for gf_quantity in self.iteration_gfs:
                quantity_name = axes.get(gf_quantity)
                if not quantity_name:
                    continue
                value_per_atom = []
                for i_imp in range(n_impurities):
                    n_orb = sec_scc.method_ref.dmft.n_correlated_orbitals[i_imp]
                    if dmft_last_iter.get(f'{gf_quantity}_{i_imp}'):
                        value = dmft_last_iter.get(f'{gf_quantity}_{i_imp}')
                        value_per_atom_per_spin = []
                        for spin in ['down', 'up']:
                            value_per_atom_per_spin_per_orbital = []
                            for i_orb in range(n_orb):
                                val = value.get(f'{spin}_{i_orb}').get('data')
                                val = val[:, 0, 0, 0] + 1j * val[:, 0, 0, 1]
                                value_per_atom_per_spin_per_orbital.append(val)
                            value_per_atom_per_spin.append(value_per_atom_per_spin_per_orbital)
                        value_per_atom.append(value_per_atom_per_spin)
                gf = np.array(value_per_atom)
                sec_gfs.m_set(sec_gfs.m_get_quantity_definition(quantity_name), gf)

        quasiparticle_weights = []
        orbital_occupations = []
        orb_Z = observables.get('orb_Z')
        orb_occ = observables.get('orb_occ')
        for i_imp in range(n_impurities):
            orb_Z_per_impurity = orb_Z.get(f'{i_imp}')
            quasiparticle_weights_per_impurity = []
            orb_occ_per_impurity = orb_occ.get(f'{i_imp}')
            orbital_occupations_per_impurity = []
            for spin in ['down', 'up']:
                if orb_Z_per_impurity.get(spin, {}).get(f'{n_iter_scf}'):
                    quasiparticle_weights_per_impurity.append(orb_Z_per_impurity.get(spin).get(f'{n_iter_scf}')[()])
                if orb_occ_per_impurity.get(spin, {}).get(f'{n_iter_scf}'):
                    orbital_occupations_per_impurity.append(orb_occ_per_impurity.get(spin).get(f'{n_iter_scf}')[()])
            quasiparticle_weights.append(quasiparticle_weights_per_impurity)
            orbital_occupations.append(orbital_occupations_per_impurity)
        sec_gfs.quasiparticle_weights = quasiparticle_weights
        sec_gfs.orbital_occupations = orbital_occupations

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.mainfile = os.path.basename(self.filepath)
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
