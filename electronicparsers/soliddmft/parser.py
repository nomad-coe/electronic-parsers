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

from typing import Any, Dict, Union
from nomad.units import ureg
from simulationworkflowschema import SinglePoint
from runschema.run import Run, Program
from runschema.calculation import (
    Calculation,
    ScfIteration,
    Energy,
    EnergyEntry,
    GreensFunctions,
    Dos,
    DosValues,
)
from runschema.method import (
    Method,
    AtomParameters,
    HubbardKanamoriModel,
    KMesh,
    FrequencyMesh,
    TimeMesh,
    DMFT,
)
from runschema.system import System, Atoms
from .metainfo.soliddmft import x_soliddmft_observables_parameters
from ..utils import numpy_type_to_json_serializable


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
            'ctseg': 'CT-HYB',
        }

        self.iteration_gfs = [
            'Delta_time',
            'Delta_freq',
            'G0_freq',
            'Gimp_freq',
            'Gimp_time',
            'Sigma_freq',
        ]

        self.observable_gfs = ['imp_gb2', 'imp_occ', 'orb_Z', 'orb_gb2', 'orb_occ']

        self._gf_map = {
            'Sigma_freq': 'self_energy_iw',
            'Gimp_freq': 'greens_function_iw',
            'Gimp_time': 'greens_function_tau',
        }

        self._gf_freq_map = {
            'real': {
                'Delta_freq': 'hybridization_function_freq',
                'Gimp_freq': 'greens_function_freq',
                'Sigma_freq': 'self_energy_freq',
                'Gimp_time': 'greens_function_tau',
            },
            'matsubara': {
                'Delta_freq': 'hybridization_function_iw',
                'Gimp_freq': 'greens_function_iw',
                'Sigma_freq': 'self_energy_iw',
                'Gimp_time': 'greens_function_tau',
            },
        }

    def extract_groups_datasets(
        self,
        data: Union[h5py.Dataset, h5py.Group],
        default: Union[bool, int, float, None] = None,
    ):
        """Extracts the content from the h5 file groups and datasets.

        For a dataset, returns the extracted data or the default. For a group, returns a
        dictionary with dataset names as keys and their content as values. If the content
        is a byte string, it is decoded to a regular string.

        Args:
            data (Union[h5py.Dataset, h5py.Group]): The dataset or group to extract from.
            default (Union[bool, int, float, None], optional): The default value
                to return if data does not exists. Defaults to None.

        Returns:
            - For Dataset: The content of the dataset.
            - For Group: Dictionary with dataset names as keys and their content as values.
            - Otherwise: The default value.
        """
        if isinstance(data, h5py.Dataset):
            return data[()]
        elif isinstance(data, h5py.Group):
            params = {}
            for key, value in data.items():
                if not isinstance(value, h5py.Dataset) or value.shape or not value:
                    continue
                val = value[()].decode() if isinstance(value[()], bytes) else value[()]
                params[key] = numpy_type_to_json_serializable(
                    val
                )  # unprotected overwrite of key
            return params
        else:
            return default

    def parse_system(self):
        """Parses the system information and stores it under self.archive.run[0].system."""
        # TODO speak with solid_dmft devs to include this info in the output
        sec_run = self.archive.run[-1]
        if self.dft_input.get('kpt_basis'):
            sec_system = System()
            sec_run.system.append(sec_system)
            sec_atoms = Atoms()
            sec_system.atoms = sec_atoms
            kpt_basis = self.extract_groups_datasets(self.dft_input.get('kpt_basis'))
            if kpt_basis is not None:
                sec_atoms.lattice_vectors_reciprocal = kpt_basis / ureg.angstrom
        else:
            pass

    def parse_input_model(self, data: h5py.File):
        """Extracts the input model from the given data. The method focuses on:
            1- the projection matrix
            2- the Hubbard-Kanamori parameters.

        The parsed information is stored under self.archive.run[0].method[0]

        Args:
            data (HDF5file): The data read from the h5 mainfile.
        """
        sec_run = self.archive.run[-1]
        sec_method = Method()
        sec_run.method.append(sec_method)

        # DFTTools code-specific input
        for group_name in ['dft_input', 'dft_misc_input', 'dft_symmcorr_input']:
            group = data.get(group_name)
            if not group:
                continue
            params = self.extract_groups_datasets(group)
            sec_method.m_set(
                sec_method.m_get_quantity_definition(f'x_soliddmft_{group_name}'),
                params,
            )

        # HoppingMatrix || ProjectionMatrix
        proj_mat = self.extract_groups_datasets(self.dft_input.get('proj_mat'))
        if proj_mat is not None:
            sec_method.x_soliddmft_projection_matrix = (
                proj_mat[:, 0, :, :, :, 0] + 1j * proj_mat[:, 0, :, :, :, 1]
            )

        # HubbardKanamoriModel
        # TODO add parse for full_slater
        # TODO add parse for crpa file
        n_impurities = self.extract_groups_datasets(
            self.dft_input.get('n_inequiv_shells'), 1
        )
        general_params = self.dmft_input.get('general_params')
        for n in range(n_impurities):
            n_imp = str(n)
            sec_atom_parameters = AtomParameters()
            sec_method.atom_parameters.append(sec_atom_parameters)
            atom_impurity = self.dft_input.get('corr_shells')
            if atom_impurity:
                atom_index = self.extract_groups_datasets(
                    atom_impurity.get(n_imp).get('atom')
                )
                sec_atom_parameters.atom_index = atom_index
                n_orbitals = self.extract_groups_datasets(
                    atom_impurity.get(n_imp).get('dim')
                )
                l_number = self.extract_groups_datasets(
                    atom_impurity.get(n_imp).get('l')
                )
                if n_orbitals and l_number:
                    sec_atom_parameters.n_orbitals = n_orbitals
                    angular_momentum = self.angular_momentum[l_number]
                    orbital_labels = [
                        f'{angular_momentum}{ml}' for ml in range(n_orbitals)
                    ]
                    sec_atom_parameters.orbitals = orbital_labels

            sec_hubbard_kanamori_model = HubbardKanamoriModel()
            sec_atom_parameters.hubbard_kanamori_model = sec_hubbard_kanamori_model
            hubbard_u = self.extract_groups_datasets(general_params.get('U').get(n_imp))
            hubbard_j = self.extract_groups_datasets(general_params.get('J').get(n_imp))
            if hubbard_u is not None and hubbard_j is not None:
                sec_hubbard_kanamori_model.u = hubbard_u * ureg.eV
                sec_hubbard_kanamori_model.jh = hubbard_j * ureg.eV
                # solid_dmft keeps spin-rotational invariance
                sec_hubbard_kanamori_model.up = (
                    sec_hubbard_kanamori_model.u - 2.0 * sec_hubbard_kanamori_model.jh
                )
            # issue with def of 'h_int_type' in the output h5 in different versions
            h_int_type = general_params.get('h_int_type')
            if isinstance(h_int_type, h5py.Dataset):
                h_int_type = self.extract_groups_datasets(h_int_type)
            elif isinstance(h_int_type, h5py.Group):
                h_int_type = self.extract_groups_datasets(h_int_type.get(n_imp))
            if h_int_type == b'density_density':
                sec_hubbard_kanamori_model.j = 0.0
            elif h_int_type == b'kanamori':
                sec_hubbard_kanamori_model.j = sec_hubbard_kanamori_model.jh
            dc_type = self.extract_groups_datasets(
                general_params.get('dc_type'), 0
            )  # set to 'fll' by default
            sec_hubbard_kanamori_model.double_counting_correction = self.dc_type[
                dc_type
            ]

    def parse_method(self):
        """Extracts the DMFT and related code-specific parameters from the 'DMFT_input' group.

        The parsed information is stored under self.archive.run[0].method[1]

        Note:
            The extraction heavily relies on the structure and layout of the HDF5 dataset.
            If the dataset changes or is restructured, this method may need adjustments.
        """
        sec_run = self.archive.run[-1]
        sec_method = Method()
        sec_run.method.append(sec_method)
        # ref to the Non- and InteractionHamiltonian
        sec_method.starting_method_ref = sec_run.method[0]

        # Code-specific
        for group_name in ['general_params', 'solver_params', 'advanced_params']:
            group = self.dmft_input.get(group_name)
            if not group:
                continue
            params = self.extract_groups_datasets(group)
            sec_method.m_set(
                sec_method.m_get_quantity_definition(f'x_soliddmft_{group_name}'),
                params,
            )

        # KMesh
        sec_k_mesh = KMesh()
        sec_method.k_mesh = sec_k_mesh
        n_k = self.extract_groups_datasets(self.dft_input.get('n_k'), 1)
        sec_k_mesh.n_points = n_k
        kpts = self.extract_groups_datasets(self.dft_input.get('kpts'))
        if kpts is not None:
            sec_k_mesh.points = np.complex128(kpts)
        kpt_weights = self.extract_groups_datasets(self.dft_input.get('kpt_weights'))
        sec_k_mesh.weights = kpt_weights

        # DMFT
        sec_dmft = DMFT()
        sec_method.dmft = sec_dmft
        n_impurities = self.extract_groups_datasets(
            self.dft_input.get('n_inequiv_shells'), 1
        )
        sec_dmft.n_impurities = n_impurities
        impurity_orbitals = []
        impurity_occupation = []
        for n in range(n_impurities):
            n_imp = str(n)
            # Number of impurity orbitals
            n_orbitals = self.extract_groups_datasets(
                self.dft_input.get('corr_shells', {}).get(n_imp, {}).get('dim'), 1
            )
            impurity_orbitals.append(n_orbitals)
            # Impurity occupation
            occupation = (
                self.dmft_results.get('observables', {}).get('imp_occ', {}).get(n_imp)
            )
            total_occupation = self.extract_groups_datasets(
                occupation['down']['0']
            ) + self.extract_groups_datasets(occupation['up']['0'])
            impurity_occupation.append(total_occupation)
        sec_dmft.n_correlated_orbitals = impurity_orbitals
        sec_dmft.n_electrons = impurity_occupation
        # Beta
        dmft_general_params = self.dmft_input.get('general_params', {})
        beta = self.extract_groups_datasets(dmft_general_params.get('beta'))
        if beta:
            sec_dmft.inverse_temperature = beta / ureg.eV
        magnetic_flag = self.extract_groups_datasets(
            dmft_general_params.get('magnetic'), False
        )
        if magnetic_flag:
            magmom = dmft_general_params.get('magmom')
            if len(magmom) > 0:
                magmom = [
                    self.extract_groups_datasets(magmom.get(keys))
                    for keys in magmom.keys()
                ]
                sec_dmft.magnetic_state = (
                    'ferromagnetic'
                    if all(signs == 1.0 for signs in np.sign(magmom))
                    else 'antiferromagnetic'
                )
            else:
                self.logger.warning(
                    'The magnetic flag is set to true, but the initial magnetic moment is not resolved. '
                    'Is this really a magnetic calculation without an initial magmom seed?'
                )
        else:
            sec_dmft.magnetic_state = 'paramagnetic'
        solver_type = self.extract_groups_datasets(
            dmft_general_params.get('solver_type')
        )
        if solver_type:
            sec_dmft.impurity_solver = self._solver_map[solver_type.decode()]

        # MatsFrequencyMesh
        n_iw = self.extract_groups_datasets(dmft_general_params.get('n_iw'))
        if n_iw:
            iw = np.array([(2 * (n - n_iw) + 1) * 1j / beta for n in range(2 * n_iw)])
            iw = iw.reshape((2 * n_iw, 1))
            sec_freq_mesh = FrequencyMesh(
                dimensionality=1, n_points=n_iw, points=iw * ureg.eV
            )
            sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
        # TimeMesh
        n_tau = self.extract_groups_datasets(dmft_general_params.get('n_tau'))
        if n_tau:
            tau = np.array([n * beta * 1j / (n_tau - 1) for n in range(n_tau)])
            tau = tau.reshape((n_tau, 1))
            sec_time_mesh = TimeMesh(dimensionality=1, n_points=n_tau, points=tau)
            sec_method.m_add_sub_section(Method.time_mesh, sec_time_mesh)
        # FrequencyMesh
        n_w = self.extract_groups_datasets(dmft_general_params.get('n_w'))
        if n_w:
            w_min = self.extract_groups_datasets(
                dmft_general_params.get('w_range', {}).get('0'), 0.0
            )
            w_max = self.extract_groups_datasets(
                dmft_general_params.get('w_range', {}).get('1'), 0.0
            )
            freq = np.linspace(w_min, w_max, n_w)
            freq = freq.reshape((n_w, 1))
            sec_freq_mesh = FrequencyMesh(
                dimensionality=1, n_points=n_w, points=freq * ureg.eV
            )
            sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)

    def parse_scc(self):
        """Extracts the output quantities from the 'DMFT_results' group. These are mainly
        Green's functions and related quantities.

        The parsed information is stored under self.archive.run[0].calculation[0]
        """
        sec_run = self.archive.run[-1]
        sec_scc = Calculation()
        sec_run.calculation.append(sec_scc)
        sec_scc.system_ref = sec_run.system[-1] if sec_run.system else None
        sec_scc.method_ref = sec_run.method[-1]  # ref to DMFT

        def parse_scf(
            filename: str,
            sec_scc: Calculation,
            i_scf: int,
            n_impurities: int,
            convergence_obs: Dict[str, Any],
            observables: Dict[str, Any],
            farg: str = 'r+b',
        ):
            """Parses the scf iterations.

            Args:
                filename: Path to the h5 file.
                farg: Arguments for reading and decoding the h5 file.
                sec_scc (Calculation): Calculation section.
                i_scf (int): Scf iteration index.
                n_impurities (int): Number of impurities.
                convergence_obs (Dict[str, Any]): Convergence of observables.
                observables (Dict[str, Any]): Observables.
            """
            sec_scf = ScfIteration()
            sec_scc.scf_iteration.append(sec_scf)
            # Convergence of the observables per scf iteration step
            conv_obs = {}
            for key, value in convergence_obs.items():
                if len(value) == 0 or key == 'iteration':
                    continue
                if key == 'd_mu':
                    val = self.extract_groups_datasets(value.get(f'{i_scf}'))
                    conv_obs[key] = numpy_type_to_json_serializable(val)
                else:
                    for n in range(n_impurities):
                        n_imp = str(n)
                        if key == 'd_orb_occ':
                            d_orb_occ = self.extract_groups_datasets(
                                value.get(n_imp)[f'{i_scf}']
                            )
                            sec_scf.x_soliddmft_convergence_orb_occ = d_orb_occ
                        else:
                            val = self.extract_groups_datasets(
                                value.get(n_imp)[f'{i_scf}']
                            )
                            conv_obs[f'{key}_imp{n_imp}'] = (
                                numpy_type_to_json_serializable(val)
                            )
            sec_scf.x_soliddmft_convergence_obs = conv_obs

            # Energy per scf iteration step
            sec_energy = Energy()
            sec_scf.energy = sec_energy
            total_energy = self.extract_groups_datasets(
                observables.get('E_tot', {}).get(f'{i_scf + 1}')
            )
            if total_energy:
                total_energy = total_energy * ureg.eV
                sec_energy.total = EnergyEntry(value=total_energy)
            chemical_potential = self.extract_groups_datasets(
                observables.get('mu', {}).get(f'{i_scf + 1}')
            )
            if chemical_potential:
                sec_energy.chemical_potential = chemical_potential * ureg.eV
            dc_energy = []
            for n in range(n_impurities):
                dc_energy_atom = self.extract_groups_datasets(
                    observables.get('E_DC', {}).get(f'{n}').get(f'{i_scf + 1}')
                )
                dc_energy.append(dc_energy_atom)
            sec_energy.double_counting = EnergyEntry(
                values_per_atom=dc_energy * ureg.eV
            )

            # Observables per scf iteration step
            scf_iteration = self.dmft_results.get(f'it_{i_scf + 1}')
            for n in range(n_impurities):
                n_imp = str(n_imp)
                sec_obs_scf = x_soliddmft_observables_parameters()
                sec_scf.x_soliddmft_observables.append(sec_obs_scf)
                h5_base = f'{os.path.basename(self.mainfile)}#/DMFT_results'
                for gf_iteration in self.iteration_gfs:
                    if f'{gf_iteration}_{n_imp}' not in scf_iteration.keys():
                        continue
                    value_per_spin_orbital = scf_iteration.get(
                        f'{gf_iteration}_{n_imp}'
                    )
                    value_tot = []
                    for spin_orb in value_per_spin_orbital.keys():
                        if spin_orb == 'block_names':
                            continue
                        value_tot.append(
                            f'{h5_base}/it_{i_scf + 1}/{gf_iteration}_{n_imp}/{spin_orb}/data'
                        )
                    sec_obs_scf.m_set(
                        sec_obs_scf.m_get_quantity_definition(
                            f'x_soliddmft_{gf_iteration}'
                        ),
                        value_tot,
                    )
                for gf_observable in self.observable_gfs:
                    if gf_observable not in observables.keys():
                        continue
                    value_per_spin_orbital = observables.get(gf_observable).get(
                        f'{n_imp}'
                    )
                    value_tot = []
                    for spin_orb in value_per_spin_orbital.keys():
                        value_tot.append(
                            f'{h5_base}/observables/{gf_observable}/{n_imp}/{spin_orb}/{i_scf + 1}'
                        )
                    sec_obs_scf.m_set(
                        sec_obs_scf.m_get_quantity_definition(
                            f'x_soliddmft_{gf_observable}'
                        ),
                        value_tot,
                    )

        def parse_gfs(sec_scc: Calculation, n_impurities: int):
            """Parses Green's functions quantities.

            Args:
                sec_scc (Calculation): Calculation section.
                n_impurities (int): Number of impurities.
            """
            sec_gfs = GreensFunctions()
            sec_scc.greens_functions.append(sec_gfs)

            # First, store energies
            dmft_last_iter = self.dmft_results.get('last_iter')
            sec_energy = Energy()
            sec_scc.energy = sec_energy
            if dmft_last_iter.get('DC_energ'):
                dc_energy = [
                    self.extract_groups_datasets(
                        dmft_last_iter.get('DC_energ').get(keys)
                    )
                    for keys in dmft_last_iter.get('DC_energ')
                ]
                sec_energy.double_counting = EnergyEntry(
                    values_per_atom=dc_energy * ureg.eV
                )
            chemical_potential = self.extract_groups_datasets(
                dmft_last_iter.get('chemical_potential_post')
            )
            if chemical_potential:
                sec_energy.chemical_potential = chemical_potential * ureg.eV
                sec_gfs.chemical_potential = chemical_potential * ureg.eV

            # Read axes label
            axes_label = ''
            for freq_mesh in sec_scc.method_ref.frequency_mesh:
                points = np.transpose(freq_mesh.points.to('eV').magnitude)[-1]
                if np.isreal(points).all():
                    sec_gfs.frequencies = np.real(points)
                    axes_label = 'real'
                else:
                    sec_gfs.matsubara_freq = np.imag(points)
                    axes_label = 'matsubara'
            axes = self._gf_freq_map[axes_label]
            if sec_scc.method_ref.time_mesh:
                sec_gfs.tau = np.transpose(sec_scc.method_ref.time_mesh[0].points.imag)[
                    -1
                ]

            # Finally, store GF quantities
            n_orbitals = sec_scc.method_ref.dmft.n_correlated_orbitals
            if n_orbitals is not None:
                for gf_quantity in self.iteration_gfs:
                    quantity_name = axes.get(gf_quantity)
                    if not quantity_name:
                        continue
                    value_per_atom = []
                    for n in range(n_impurities):
                        n_orb = n_orbitals[n]
                        if not dmft_last_iter.get(f'{gf_quantity}_{n}'):
                            continue
                        value = dmft_last_iter.get(f'{gf_quantity}_{n}')
                        value_per_atom_per_spin = []
                        for spin in ['down', 'up']:
                            value_per_atom_per_spin_per_orbital = []
                            for i_orb in range(n_orb):
                                val = value.get(f'{spin}_{i_orb}').get('data')
                                val = val[:, 0, 0, 0] + 1j * val[:, 0, 0, 1]
                                value_per_atom_per_spin_per_orbital.append(val)
                            value_per_atom_per_spin.append(
                                value_per_atom_per_spin_per_orbital
                            )
                        value_per_atom.append(value_per_atom_per_spin)
                    if not value_per_atom:
                        continue
                    gf = np.array(value_per_atom)
                    if (
                        gf_quantity == 'Gimp_time'
                    ):  # setting G(tau) to positive values as in other codes
                        gf = -gf
                    sec_gfs.m_set(sec_gfs.m_get_quantity_definition(quantity_name), gf)

            # In case axes_label = real, we parse the DOS as -Im G(w) / np.pi
            if axes_label == 'real':
                magnetic_state = sec_scc.method_ref.dmft.magnetic_state
                n_spin_channels = 1 if magnetic_state == 'paramagnetic' else 2

                im_greens_functions_freq = sec_gfs.greens_function_freq.imag
                for spin_channel in range(n_spin_channels):
                    sec_dos = Dos()
                    sec_scc.dos_electronic.append(sec_dos)
                    sec_dos.spin_channel = (
                        spin_channel if n_spin_channels == 2 else None
                    )
                    sec_dos.kind = 'spectral'
                    sec_dos.energy_fermi = chemical_potential * ureg.eV
                    energies = sec_gfs.frequencies
                    sec_dos.n_energies = len(energies)
                    sec_dos.energies = energies * ureg.eV
                    # Total values
                    imgf_per_spin = im_greens_functions_freq[:, spin_channel, :, :]
                    value = -imgf_per_spin / np.pi
                    value_total = 0.0
                    for i_at in range(value.shape[0]):
                        for i_orb in range(value.shape[1]):
                            value_total += value[i_at][i_orb]
                    value_total = (
                        2 * value_total if n_spin_channels == 2 else value_total
                    )
                    sec_dos_total = DosValues()
                    sec_dos.total.append(sec_dos_total)
                    sec_dos_total.value = value_total / ureg.eV
            return sec_gfs

        # SCF steps
        scf_keys = [
            int(key.lstrip('it_'))
            for key in self.dmft_results.keys()
            if key.startswith('it_')
        ]
        scf_keys.sort()
        n_iter_scf = (
            self.dmft_results.get('iteration_count')[()]
            if self.dmft_results.get('iteration_count')
            else 1
        )

        if len(scf_keys) != n_iter_scf:
            self.logger.warning(
                'Number of it_n steps for DMFT results is different from the iteration '
                'count stored in the h5 file.'
            )

        n_impurities = self.dft_input.get('n_inequiv_shells')[()]
        convergence_obs = self.dmft_results.get('convergence_obs', {})
        observables = self.dmft_results.get('observables', {})
        # Resolving h5 path for to_hdf5 method
        filename = os.path.join(
            os.path.dirname(self.filepath.split('/raw/')[-1]), self.mainfile
        )
        for i_scf in range(len(scf_keys)):
            parse_scf(
                filename, sec_scc, i_scf, n_impurities, convergence_obs, observables
            )

        # Greens functions quantities
        sec_gfs = parse_gfs(sec_scc, n_impurities)
        # and related quantities
        quasiparticle_weights = []
        orbital_occupations = []
        orb_Z = observables.get('orb_Z')
        orb_occ = observables.get('orb_occ')
        for n in range(n_impurities):
            n_imp = str(n)
            orb_Z_per_impurity = orb_Z.get(n_imp)
            quasiparticle_weights_per_impurity = []
            orb_occ_per_impurity = orb_occ.get(n_imp)
            orbital_occupations_per_impurity = []
            for spin in ['down', 'up']:
                quasiparticle_weights_per_impurity.append(
                    self.extract_groups_datasets(
                        orb_Z_per_impurity.get(spin).get(f'{n_iter_scf}')
                    )
                )
                orbital_occupations_per_impurity.append(
                    self.extract_groups_datasets(
                        orb_occ_per_impurity.get(spin).get(f'{n_iter_scf}')
                    )
                )
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

        sec_run = Run()
        archive.run.append(sec_run)

        # Program section
        sec_program = Program()
        sec_run.program = sec_program
        sec_program.name = 'solid_dmft'
        if self.dmft_input['version'] is not None:
            for name in self.code_keys:
                hash = self.extract_groups_datasets(
                    self.dmft_input['version'].get(f'{name}_hash')
                )
                if hash:
                    if name == 'solid_dmft':
                        sec_program.x_soliddmft_hash = hash.decode()
                    else:
                        setattr(sec_program, f'x_soliddmft_{name}_hash', hash.decode())
                version = self.extract_groups_datasets(
                    self.dmft_input['version'].get(f'{name}_version')
                )
                if version:
                    if name == 'solid_dmft':
                        sec_program.version = version.decode()
                    else:
                        setattr(
                            sec_program, f'x_soliddmft_{name}_version', version.decode()
                        )

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
