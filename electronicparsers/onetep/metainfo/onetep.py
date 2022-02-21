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
import numpy as np            # pylint: disable=unused-import
import typing                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference, JSON
)
from nomad.datamodel.metainfo import simulation
from nomad.datamodel.metainfo import workflow


m_package = Package()


class x_onetep_section_vibrational_frequencies(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_vibrationl_frequencies = Quantity(
        type=np.dtype(np.float64),
        shape=['len(self.nr_iter)'],
        description='''
        Vibration Frequenices (cm-1)
        ''')

    x_onetep_vibrationl_frequencies_store = Quantity(
        type=str,
        shape=[],
        description='''
        Vibration Frequenices (cm-1)
        ''')

    x_onetep_ir_store = Quantity(
        type=str,
        shape=[],
        description='''
        Irreducible representation in the Point Group
        ''')

    x_onetep_ir = Quantity(
        type=str,
        shape=['len(self.nr_iter)'],
        description='''
        Irreducible representation in the Point Group
        ''')

    x_onetep_raman_activity = Quantity(
        type=np.dtype(np.float64),
        shape=['len(self.nr_iter)'],
        description='''
        Raman activity (A**4/amu)
        ''')

    x_onetep_raman_active = Quantity(
        type=str,
        shape=[],
        description='''
        Raman activity (A**4/amu)
        ''')

    x_onetep_n_iterations_phonons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of iterations in phonons
        ''')

    x_onetep_raman_activity_store = Quantity(
        type=str,
        shape=[],
        description='''
        Raman activity (A**4/amu)
        ''')

    x_onetep_ir_intensity = Quantity(
        type=np.dtype(np.float64),
        shape=['len(self.nr_iter)'],
        description='''
        IR intensities (D/A)**2/amu
        ''')

    x_onetep_ir_intensity_store = Quantity(
        type=str,
        shape=[],
        description='''
        IR intensities (D/A)**2/amu
        ''')


class x_onetep_section_tddft(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_tddft_energies = Quantity(
        type=np.dtype(np.float64),
        shape=[-1],
        description='''
        lrtddft energy
        ''')

    x_onetep_tddft_penalties = Quantity(
        type=np.dtype(np.float64),
        shape=[-1],
        description='''
        lrtddft energy
        ''')

    x_onetep_tddft_steps = Quantity(
        type=np.dtype(np.float64),
        shape=[-1],
        description='''
        lrtddft energy
        ''')

    x_onetep_tddft_omega_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        change in omega
        ''')

    x_onetep_tddft_rms_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        rms gradient tddft
        ''')

    x_onetep_tddft_number_conv_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number converged states
        ''')

    x_onetep_tddft_excit_energies = Quantity(
        type=np.dtype(np.float64),
        shape=[-1],
        description='''
        excitations
        ''')

    x_onetep_tddft_excit_oscill_str = Quantity(
        type=np.dtype(np.float64),
        shape=[-1],
        description='''
        oscillator strenght
        ''')

    x_onetep_tddft_excit_lifetime = Quantity(
        type=np.dtype(np.float64),
        shape=[-1],
        description='''
        excit_lifetime
        ''')

    x_onetep_section_tddft_excitations = SubSection(
        sub_section=SectionProxy('x_onetep_section_tddft_excitations'),
        repeats=True)

    x_onetep_section_tddft_iterations = SubSection(
        sub_section=SectionProxy('x_onetep_section_tddft_iterations'),
        repeats=True)


class x_onetep_section_tddft_excitations(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_tddft_excit_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        exciations
        ''')

    x_onetep_tddft_excit_oscill_str = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        oscillator strenght
        ''')

    x_onetep_tddft_excit_lifetime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='s',
        description='''
        excit_lifetime
        ''')


class x_onetep_section_tddft_iterations(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_tddft_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        lrtddft energy
        ''')

    x_onetep_tddft_penalties = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        lrtddft energy
        ''')

    x_onetep_tddft_step = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        lrtddft energy
        ''')


class x_onetep_section_atom_ionic_velocities(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)


class x_onetep_section_atom_positions_optim(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_cell_angle_alpha_optim = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Simulation cell angle alpha
        ''')

    x_onetep_cell_angle_beta_optim = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Simulation cell angle beta
        ''')

    x_onetep_cell_angle_gamma_optim = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Simulation cell angle gamma
        ''')

    x_onetep_cell_length_a_optim = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        a unit cell edge length
        ''')

    x_onetep_cell_length_b_optim = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        b unit cell edge length
        ''')

    x_onetep_cell_length_c_optim = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        c unit cell edge length
        ''')


class x_onetep_section_atom_positions(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_cell_angle_alpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Simulation cell angle alpha
        ''')

    x_onetep_cell_angle_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Simulation cell angle beta
        ''')

    x_onetep_cell_angle_gamma = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Simulation cell angle gamma
        ''')

    x_onetep_cell_length_a = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        a unit cell edge length
        ''')

    x_onetep_cell_length_b = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        b unit cell edge length
        ''')

    x_onetep_cell_length_c = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        c unit cell edge length
        ''')


class x_onetep_section_dipole(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_electronic_dipole_moment_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        store dipole
        ''')

    x_onetep_electronic_dipole_moment = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        -
        ''')

    x_onetep_electronic_dipole_moment_magnitude = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_ionic_dipole_moment_magnitude = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_total_dipole_moment_magnitude = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_ionic_dipole_moment_store = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        -
        ''')

    x_onetep_ionic_dipole_moment = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        -
        ''')

    x_onetep_total_dipole_moment_store = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        -
        ''')

    x_onetep_total_dipole_moment = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        -
        ''')


class x_onetep_section_cell_optim(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_cell_vector_optim = Quantity(
        type=str,
        shape=[],
        description='''
        Temporay storage for cell vectors
        ''')


class x_onetep_section_cell(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_units = Quantity(
        type=str,
        shape=[],
        description='''
        units
        ''')

    x_onetep_cell_vector = Quantity(
        type=str,
        shape=[],
        description='''
        Temporay storage for cell vectors
        ''')


class x_onetep_section_collect_scf_eigenvalues(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)


class x_onetep_section_eigenvalues_1(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_eigenvalues_1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storing eigenvalues
        ''')


class x_onetep_section_eigenvalues(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_eigenvalues = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storing eigenvalues
        ''')


class x_onetep_section_functional_definition(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_functional_type = Quantity(
        type=str,
        shape=[],
        description='''
        XC functional definition in onetep convention
        ''')

    x_onetep_functional_weight = Quantity(
        type=str,
        shape=[],
        description='''
        XC functional weight in onetep convention
        ''')


class x_onetep_section_functionals(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_functional_name = Quantity(
        type=str,
        shape=[],
        description='''
        XC functional in onetep convention
        ''')


class x_onetep_section_mulliken_population_analysis(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_mulliken_atom_index = Quantity(
        type=str,
        shape=['number_of_atoms'],
        description='''
        Mulliken_atom_index
        ''')

    x_onetep_mulliken_atom = Quantity(
        type=str,
        shape=['number_of_atoms'],
        description='''
        Mulliken_atom kind
        ''')

    x_onetep_total_orbital = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Mulliken_total_contribution
        ''')

    x_onetep_total_orbital_store = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Mulliken_total_contribution
        ''')

    x_onetep_spin = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Mulliken_spin
        ''')

    x_onetep_spin_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mulliken_spin
        ''')

    x_onetep_mulliken_charge_store = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Mulliken_charges
        ''')

    x_onetep_mulliken_charge = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Mulliken_charges
        ''')


class x_onetep_section_nbo_population_analysis(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_nbo_atom_label_store = Quantity(
        type=str,
        shape=['number_of_atoms'],
        description='''
        nbo_atom kind
        ''')

    x_onetep_nbo_atom_labels = Quantity(
        type=str,
        shape=['number_of_atoms'],
        description='''
        nbo_atom kind
        ''')

    x_onetep_total_nbo_population_store = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        nbo_population
        ''')

    x_onetep_total_nbo_population = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        nbo_population
        ''')

    x_onetep_nbo_partial_charge_store = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        nbo_charges
        ''')

    x_onetep_nbo_partial_charge = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        nbo_charges
        ''')

    x_onetep_nbo_total_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        nbo_charges
        ''')


class x_onetep_section_geom_optimisation_method(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_geometry_optim_method = Quantity(
        type=str,
        shape=[],
        description='''
        Determines optimisation method used
        ''')


class x_onetep_section_optics_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_optics_n_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        optics_number_of_bands
        ''')

    x_onetep_optics_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        optics_band_convergence_tolerance
        ''')


class x_onetep_section_ngwf_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ngwf_cg_max_step = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ngwf_cg_max_step
        ''')

    x_onetep_ngwf_cg_type = Quantity(
        type=str,
        shape=[],
        description='''
        ngwf_cg_type
        ''')

    x_onetep_ngwf_halo = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ngwf_halo
        ''')

    x_onetep_ngwf_max_grad = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x_onetep_ngwf_max_grad
        ''')

    x_onetep_ngwf_threshold_orig = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ngwf_threshold_orig
        ''')


class x_onetep_section_kernel_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_kernel_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_kernel_diis_maxit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_onetep_kernel_diis_coeff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_kernel_diis_thershold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_kernel_diis_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_kernel_diis_type_store = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_onetep_kernel_diis_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_onetep_kernel_diis_lshift = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of the shift in energy of the conduction bands with the level-shifting
        technique during the inner loop DIIS. Reference:
        ''')

    x_onetep_kernel_diis_linear_iter = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class x_onetep_section_phonons(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_phonon_method = Quantity(
        type=str,
        shape=[],
        description='''
        Phonon calculation method
        ''')

    x_onetep_DFPT_solver_method = Quantity(
        type=str,
        shape=[],
        description='''
        Phonon DFPT solver method
        ''')

    x_onetep_phonon_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Phonon calculation tolerance (eV/A**2)
        ''')

    x_onetep_phonon_cycles = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Phonon calculation cycles
        ''')

    x_onetep_band_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Phonon band convergence tolerance window
        ''')


class x_onetep_section_density_mixing_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_density_mixing_scheme = Quantity(
        type=str,
        shape=[],
        description='''
        density_mixing_scheme
        ''')

    x_onetep_density_mixing_length = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        density_mixing_scheme_length
        ''')

    x_onetep_charge_density_mixing_amplitude = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        charge_density_mixing_amplitude
        ''')

    x_onetep_cut_off_energy_for_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        charge_density_mixing_cut_off_energy_for_mixing (A)
        ''')


class x_onetep_section_population_analysis_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_population_analysis_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Population_analysis_cutoff_(A)
        ''')


class x_onetep_section_kernel_optimisation(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Total_energy(Eh)
        ''')

    x_onetep_total_free_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Total_energy(Eh)
        ''')

    x_onetep_band_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        band_gap
        ''')

    x_onetep_rms_occupancy_error = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        rms_occupancy
        ''')

    x_onetep_commutator = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Commutator between Hamiltonian and Kernel
        ''')


class x_onetep_section_k_band(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)


class x_onetep_section_k_points_1(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_k_points_1 = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing k points coordinates (fractional)
        ''')


class x_onetep_section_k_points(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_k_points = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing k points coordinates (fractional)
        ''')


class x_onetep_section_relativity_treatment(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_relativity_treatment_scf = Quantity(
        type=str,
        shape=[],
        description='''
        Relativity treatment in onetep convention
        ''')


class x_onetep_section_scf_eigenvalues(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_scf_eigenvalues = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')


class x_onetep_section_SCF_iteration_frame(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_frame_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        onetep_store_t_md_frame
        ''')

    x_onetep_SCF_frame_energy = Quantity(
        type=str,
        shape=[],
        description='''
        energy_frame_iterations
        ''')

    x_onetep_SCF_frame_energy_gain = Quantity(
        type=str,
        shape=[],
        description='''
        energy_frame_iterations_gain
        ''')

    x_onetep_frame_time_scf_iteration_wall_end = Quantity(
        type=str,
        shape=[],
        description='''
        energy_frame_wall_end_time
        ''')

    x_onetep_frame_energy_free = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        energy_free
        ''')

    x_onetep_frame_energy_total_T0 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        energy_free_corrected_for_finite_basis
        ''')


class x_onetep_section_scf_k_points(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_scf_k_points = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_onetep_section_scf_eigenvalues = SubSection(
        sub_section=SectionProxy('x_onetep_section_scf_eigenvalues'),
        repeats=True)


class x_onetep_section_spin_number(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_spin_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class x_onetep_section_stress_tensor(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_stress_tensor = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing stress tensor components
        ''')


class x_onetep_section_time(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)


class x_onetep_section_raman_tensor(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_store_raman_tensor = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged Raman susceptibility tensor
        ''')

    x_onetep_ramen_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        unit='ampere / unified_atomic_mass_unit',
        description='''
        Ramen tensor, unit scaled by 0.5
        ''')


class x_onetep_section_tddft_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_lr_tddft_cg_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x_onetep_lr_tddft_cg_threshold
        ''')

    x_onetep_lr_tddft_kernel_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x_onetep_lr_tddft_kernel_cutoff
        ''')

    x_onetep_lr_tddft_maxit_cg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        x_onetep_lr_tddft_maxit_cg
        ''')

    x_onetep_lr_tddft_maxit_pen = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        x_onetep_lr_tddft_maxit_pen
        ''')

    x_onetep_lr_tddft_num_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        x_onetep_lr_tddft_num_states
        ''')

    x_onetep_lr_tddft_penalty_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x_onetep_lr_tddft_penalty_tol
        ''')


class x_onetep_section_scf_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_energy_threshold_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy Threshold store
        ''')

    x_onetep_max_iter_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Number of maximum iterations steps store
        ''')

    x_onetep_smearing_kind = Quantity(
        type=str,
        shape=[],
        description='''
        Smearing kind
        ''')

    x_onetep_smearing_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smearing width
        ''')

    x_onetep_elec_cg_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x_onetep_elec_cg_max
        ''')

    x_onetep_elec_force_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x_onetep_elec_force_tol
        ''')


class x_onetep_section_electronic_spectroscpy_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_theory_level = Quantity(
        type=str,
        shape=[],
        description='''
        Electronic spectroscopy parameters theory level
        ''')

    x_onetep_spectroscopy_calculation = Quantity(
        type=str,
        shape=[],
        description='''
        Electronic spectroscopy parameters calculation type
        ''')

    x_onetep_spec_max_iter = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Max number of iterations
        ''')

    x_onetep_spec_max_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Max number of steps
        ''')

    x_onetep_spec_max_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Max number of bands
        ''')

    x_onetep_spec_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Tolerance (eV)
        ''')


class x_onetep_section_md(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_md_energies = Quantity(
        type=str,
        shape=[],
        description='''
        md_energy_components
        ''')

    x_onetep_md_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        md_temp(K)
        ''')

    x_onetep_md_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        md_pressure
        ''')

    x_onetep_md_cell_vectors = Quantity(
        type=str,
        shape=[],
        description='''
        md_cell_vectors
        ''')

    x_onetep_md_cell_vectors_vel = Quantity(
        type=str,
        shape=[],
        description='''
        md_cell_vectors_velocities
        ''')

    x_onetep_md_stress_tensor = Quantity(
        type=str,
        shape=[],
        description='''
        md_stress_tensor
        ''')

    x_onetep_md_positions = Quantity(
        type=str,
        shape=[],
        description='''
        md_positions
        ''')

    x_onetep_md_forces = Quantity(
        type=str,
        shape=[],
        description='''
        md_forces
        ''')

    x_onetep_md_lab = Quantity(
        type=str,
        shape=[],
        description='''
        md_lables
        ''')

    x_onetep_md_veloc = Quantity(
        type=str,
        shape=[],
        description='''
        md_veloc
        ''')


class x_onetep_section_edft_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_edft_commutator_thres = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        edft_commutator_thres
        ''')

    x_onetep_edft_energy_thres = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        edft_energy_thres
        ''')

    x_onetep_edft_entropy_thres = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        edft_entropy_thres
        ''')

    x_onetep_edft_extra_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        edft_extra_bands
        ''')

    x_onetep_edft_fermi_thres = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        edft_fermi_thres
        ''')

    x_onetep_edft_free_energy_thres = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        edft_free_energy_thres
        ''')

    x_onetep_edft_maxit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        edft_maxit
        ''')

    x_onetep_edft_rms_gradient_thres = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        edft_rms_gradient_thres
        ''')

    x_onetep_edft_smearing_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        edft_smearing_width
        ''')


class x_onetep_section_ts(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ts_energy_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_energy_components_total
        ''')

    x_onetep_ts_cell_vectors = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        ts_cell_vectors
        ''')

    x_onetep_ts_positions = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        ts_positions
        ''')

    x_onetep_ts_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        ts_forces
        ''')

    x_onetep_ts_lab = Quantity(
        type=str,
        shape=[],
        description='''
        ts_lables
        ''')


class x_onetep_section_ts_store(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ts_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_energy_components_ts_store
        ''')

    x_onetep_ts_cell_vectors_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_cell_vectors
        ''')

    x_onetep_ts_positions_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_positions_store
        ''')

    x_onetep_ts_forces_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_forces_store
        ''')


class x_onetep_section_ts_final_store(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ts_energy_final_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_energy_components_ts
        ''')

    x_onetep_ts_forces_final_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_forces_final
        ''')

    x_onetep_ts_positions_final_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_energy_positions_final
        ''')

    x_onetep_ts_cell_vectors_final_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_cell_vectors_final
        ''')


class x_onetep_section_ts_final(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ts_energy_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_energy_final
        ''')

    x_onetep_ts_cell_vectors_final = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        ts_cell_vectors
        ''')

    x_onetep_ts_positions_final = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        ts_positions_final
        ''')

    x_onetep_ts_forces_final = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        ts_force_finals
        ''')


class x_onetep_section_ts_product(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ts_energy_product = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_energy_prod
        ''')

    x_onetep_ts_forces_product = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        ts_energy_forces_pro
        ''')

    x_onetep_ts_positions_product = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        ts_energy_positions_pro
        ''')

    x_onetep_ts_cell_vectors_product = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        ts_product_cell_vectors
        ''')


class x_onetep_section_ts_product_store(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ts_energy_product_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_energy_components_pro
        ''')

    x_onetep_ts_forces_pro_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_energy_forces_pro_store
        ''')

    x_onetep_ts_positions_pro_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_energy_positions_pro_store
        ''')

    x_onetep_ts_cell_vectors_pro_store = Quantity(
        type=str,
        shape=[],
        description='''
        ts_cell_vectors_pro
        ''')


class x_onetep_section_ts_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_ts_method = Quantity(
        type=str,
        shape=[],
        description='''
        ts_method
        ''')

    x_onetep_ts_protocol = Quantity(
        type=str,
        shape=[],
        description='''
        ts_protocol
        ''')

    x_onetep_ts_qst_iter = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ts_qst_iterations
        ''')

    x_onetep_ts_number_cg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ts_number_of_cg_iterations
        ''')

    x_onetep_ts_force_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_force_tolerance (eV/A)
        ''')

    x_onetep_ts_displacement_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_displacement_tolerance (A)
        ''')


class x_onetep_section_van_der_Waals_parameters(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_disp_method_name_store = Quantity(
        type=str,
        shape=[],
        description='''
        Name type
        ''')

    x_onetep_disp_method_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name type
        ''')

    x_onetep_Parameter_d = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Parameter for dispersion method G06
        ''')

    x_onetep_Parameter_LAMBDA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Parameter for dispersion method OBS
        ''')

    x_onetep_Parameter_n = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Parameter for dispersion method OBS
        ''')

    x_onetep_Parameter_s6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Parameter for dispersion method G06
        ''')

    x_onetep_Parameter_sR = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Parameter for dispersion method TS
        ''')


class x_onetep_section_energy_components(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_pseudo_local_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Pseudopotential
        ''')

    x_onetep_electronic_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Kinetic component store
        ''')

    x_onetep_energy_correction_hartree_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Hartree correction store
        ''')

    x_onetep_energy_XC_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        exchange energy store
        ''')

    x_onetep_ewald_correction_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ewald correction store
        ''')

    x_onetep_dispersion_correction_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dispersion correction store
        ''')

    x_onetep_integrated_density_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        store_integrated density
        ''')

    x_onetep_pseudo_non_local_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Pseudopotential
        ''')


class x_onetep_section_edft(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_section_edft_iterations = SubSection(
        sub_section=SectionProxy('x_onetep_section_edft_iterations'),
        repeats=True)


class x_onetep_section_edft_spin(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_edft_spin_type = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        spin type
        ''')

    x_onetep_edft_n_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        integrated number of electrons
        ''')

    x_onetep_edft_fermi_level = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        fermi level
        ''')

    x_onetep_edft_fermi_level_delta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        fermi level
        ''')

    x_onetep_section_edft_spin_iterations = SubSection(
        sub_section=SectionProxy('x_onetep_section_edft_spin_iterations'),
        repeats=True)


class x_onetep_section_edft_spin_iterations(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_edft_orbital_iteration_spin = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        orbital
        ''')

    x_onetep_edft_eigenvalue = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        eigenvalues
        ''')

    x_onetep_edft_occupancy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        occupancy
        ''')


class x_onetep_section_edft_iterations(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_edft_step = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        step
        ''')

    x_onetep_edft_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        step
        ''')

    x_onetep_edft_0K = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        step
        ''')

    x_onetep_residual_nonorthog = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        step
        ''')

    x_onetep_residual_n_elec = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        step
        ''')

    x_onetep_edft_commutator = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Commutator
        ''')

    x_onetep_edft_free_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        free energy A=E-TS
        ''')

    x_onetep_edft_rms_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        rms gradient in edft
        ''')

    x_onetep_edft_entropy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        rms gradient in edft
        ''')

    x_onetep_edft_iteration = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        iteration number
        ''')

    x_onetep_section_edft_spin = SubSection(
        sub_section=SectionProxy('x_onetep_section_edft_spin'),
        repeats=True)


class x_onetep_section_orbital_information(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_onetep_total_number_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_onetep_total_number_occ_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_onetep_occupancy_sum = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_homo_lumo_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_mid_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_orbital_number = Quantity(
        type=np.dtype(np.int32),
        shape=['x_onetep_total_number_occ_orbitals'],
        description='''
        -
        ''')

    x_onetep_orbital_energy = Quantity(
        type=np.dtype(np.float64),
        shape=['x_onetep_total_number_occ_orbitals'],
        description='''
        -
        ''')

    x_onetep_orbital_occupancy_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_orbital_number_store = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_onetep_orbital_energy_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_orbital_occupancy = Quantity(
        type=np.dtype(np.float64),
        shape=['x_onetep_total_number_occ_orbitals'],
        description='''
        -
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_atom_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        Forces on the atoms as minus gradient of energy_total, including forces' unitary-
        transformation (rigid body) filtering and including constraints, if present. The
        derivatives with respect to displacements of the nuclei in the gradient are
        evaluated according to the coordinate system defined in coordinate_system. In
        addition, these forces are obtained by filtering out the unitary transformations
        (translations of the center of mass and rigid rotations of the whole system, when
        non periodic), atom_forces_raw for the unfiltered counterpart. Furthermore, forces
        due to constraints like fixed atoms, distances, angles, dihedrals, and so on, are
        here included (see atom_forces_raw for the unfiltered counterpart).
        ''')

    x_onetep_atom_ionforces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        forces
        ''')

    x_onetep_atom_local_potentialforces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        forces
        ''')

    x_onetep_atom_nonlocal_potentialforces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        forces
        ''')

    x_onetep_atom_nonself_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        forces
        ''')

    x_onetep_atom_correction_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        forces
        ''')

    x_onetep_basis_set_planewave_cutoff_iteration_0 = Quantity(
        type=str,
        shape=[],
        description='''
        cutoff at iteration 0 of geometry optimisation
        ''')

    x_onetep_final_time = Quantity(
        type=str,
        shape=[],
        description='''
        onetep_calculation_time
        ''')

    x_onetep_final_date = Quantity(
        type=str,
        shape=[],
        description='''
        onetep_calculation_date
        ''')

    x_onetep_compiler = Quantity(
        type=str,
        shape=[],
        description='''
        Compiler name
        ''')

    x_onetep_constants_reference = Quantity(
        type=str,
        shape=[],
        description='''
        Fundamental constant data source
        ''')

    x_onetep_fft_library = Quantity(
        type=str,
        shape=[],
        description='''
        fft library name
        ''')

    x_onetep_avarage_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        onetep_finalisation_time
        ''')

    x_onetep_geom_converged = Quantity(
        type=str,
        shape=[],
        description='''
        onetep_geom_converged
        ''')

    x_onetep_pbc_cutoff = Quantity(
        type=str,
        shape=[],
        description='''
        onetep_pbc cutoff for effect of open boundary
        ''')

    x_onetep_is_smearing = Quantity(
        type=str,
        shape=[],
        description='''
        Turns on the smeared ion representation for electrostatics calculation.
        ''')

    x_onetep_total_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x_onetep_Initialisation_time
        ''')

    x_onetep_maths_library = Quantity(
        type=str,
        shape=[],
        description='''
        Maths library name
        ''')

    x_onetep_program_compilation_date = Quantity(
        type=str,
        shape=[],
        description='''
        Compilation date (string)
        ''')

    x_onetep_program_compilation_time = Quantity(
        type=str,
        shape=[],
        description='''
        Compilation time (string)
        ''')

    x_onetep_program_execution_date = Quantity(
        type=str,
        shape=[],
        description='''
        Run execution date (string)
        ''')

    x_onetep_program_execution_time = Quantity(
        type=str,
        shape=[],
        description='''
        Run execution start time (string)
        ''')

    x_onetep_crystal_point_group = Quantity(
        type=str,
        shape=[],
        description='''
        Point group of the crystal (Schoenflies notation)
        ''')

    x_onetep_space_group = Quantity(
        type=str,
        shape=[],
        description='''
        Point space of the crystal
        ''')

    x_onetep_ts_path = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_path_number
        ''')

    x_onetep_ts_path_ts_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_path_final
        ''')

    x_onetep_ts_path_product = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ts_path_pro
        ''')

    x_onetep_store_atom_forces_band = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces (ev/A)
        ''')

    x_onetep_number_of_processors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of processors
        ''')

    x_onetep_section_vibrational_frequencies = SubSection(
        sub_section=SectionProxy('x_onetep_section_vibrational_frequencies'),
        repeats=True)

    x_onetep_section_tddft = SubSection(
        sub_section=SectionProxy('x_onetep_section_tddft'),
        repeats=True)

    x_onetep_section_dipole = SubSection(
        sub_section=SectionProxy('x_onetep_section_dipole'),
        repeats=True)

    x_onetep_section_collect_scf_eigenvalues = SubSection(
        sub_section=SectionProxy('x_onetep_section_collect_scf_eigenvalues'),
        repeats=True)

    x_onetep_section_mulliken_population_analysis = SubSection(
        sub_section=SectionProxy('x_onetep_section_mulliken_population_analysis'),
        repeats=True)

    x_onetep_section_nbo_population_analysis = SubSection(
        sub_section=SectionProxy('x_onetep_section_nbo_population_analysis'),
        repeats=True)

    x_onetep_section_geom_optimisation_method = SubSection(
        sub_section=SectionProxy('x_onetep_section_geom_optimisation_method'),
        repeats=True)

    x_onetep_section_optics_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_optics_parameters'),
        repeats=True)

    x_onetep_section_ngwf_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_ngwf_parameters'),
        repeats=True)

    x_onetep_section_kernel_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_kernel_parameters'),
        repeats=True)

    x_onetep_section_phonons = SubSection(
        sub_section=SectionProxy('x_onetep_section_phonons'),
        repeats=True)

    x_onetep_section_density_mixing_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_density_mixing_parameters'),
        repeats=True)

    x_onetep_section_population_analysis_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_population_analysis_parameters'),
        repeats=True)

    x_onetep_section_kernel_optimisation = SubSection(
        sub_section=SectionProxy('x_onetep_section_kernel_optimisation'),
        repeats=True)

    x_onetep_section_SCF_iteration_frame = SubSection(
        sub_section=SectionProxy('x_onetep_section_SCF_iteration_frame'),
        repeats=True)

    x_onetep_section_time = SubSection(
        sub_section=SectionProxy('x_onetep_section_time'),
        repeats=True)

    x_onetep_section_raman_tensor = SubSection(
        sub_section=SectionProxy('x_onetep_section_raman_tensor'),
        repeats=True)

    x_onetep_section_tddft_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_tddft_parameters'),
        repeats=True)

    x_onetep_section_scf_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_scf_parameters'),
        repeats=True)

    x_onetep_section_electronic_spectroscpy_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_electronic_spectroscpy_parameters'),
        repeats=True)

    x_onetep_section_md = SubSection(
        sub_section=SectionProxy('x_onetep_section_md'),
        repeats=True)

    x_onetep_section_edft_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_edft_parameters'),
        repeats=True)

    x_onetep_section_ts = SubSection(
        sub_section=SectionProxy('x_onetep_section_ts'),
        repeats=True)

    x_onetep_section_ts_store = SubSection(
        sub_section=SectionProxy('x_onetep_section_ts_store'),
        repeats=True)

    x_onetep_section_ts_final_store = SubSection(
        sub_section=SectionProxy('x_onetep_section_ts_final_store'),
        repeats=True)

    x_onetep_section_ts_final = SubSection(
        sub_section=SectionProxy('x_onetep_section_ts_final'),
        repeats=True)

    x_onetep_section_ts_product = SubSection(
        sub_section=SectionProxy('x_onetep_section_ts_product'),
        repeats=True)

    x_onetep_section_ts_product_store = SubSection(
        sub_section=SectionProxy('x_onetep_section_ts_product_store'),
        repeats=True)

    x_onetep_section_ts_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_ts_parameters'),
        repeats=True)

    x_onetep_section_van_der_Waals_parameters = SubSection(
        sub_section=SectionProxy('x_onetep_section_van_der_Waals_parameters'),
        repeats=True)

    x_onetep_section_energy_components = SubSection(
        sub_section=SectionProxy('x_onetep_section_energy_components'),
        repeats=True)

    x_onetep_section_edft = SubSection(
        sub_section=SectionProxy('x_onetep_section_edft'),
        repeats=True)

    x_onetep_section_orbital_information = SubSection(
        sub_section=SectionProxy('x_onetep_section_orbital_information'),
        repeats=True)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_net_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Net charge of system
        ''')

    x_onetep_number_of_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of bands
        ''')

    x_onetep_units_atom_position = Quantity(
        type=str,
        shape=[],
        description='''
        units
        ''')

    x_onetep_number_of_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Number of electrons
        ''')

    x_onetep_atom_positions = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        Storing atomic positions in fractional coordinates
        ''')

    x_onetep_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        onetep_cell_volume
        ''')

    x_onetep_optimised_atom_labels = Quantity(
        type=str,
        shape=['number_of_atoms'],
        description='''
        Temporary storing atomic positions
        ''')

    x_onetep_optimised_atom_positions = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        Storing atomic optimised positions in fractional coordinates
        ''')

    x_onetep_velocities_cell_vector = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        cell vector velocities
        ''')

    x_onetep_number_of_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number_of_atoms
        ''')

    x_onetep_number_of_ngwf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number_of_ngwf
        ''')

    x_onetep_number_of_projectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number_of_proj
        ''')

    x_onetep_store_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing atom labels
        ''')

    x_onetep_store_atom_positions = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing atomic positions
        ''')

    x_onetep_store_atom_ionic_velocities = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing atomic positions
        ''')

    x_onetep_atom_ionic_velocities = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        Temporary storing atomic positions
        ''')

    x_onetep_store_optimised_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing atomic positions
        ''')

    x_onetep_store_optimised_atom_positions = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing atomic positions
        ''')

    x_onetep_section_atom_ionic_velocities = SubSection(
        sub_section=SectionProxy('x_onetep_section_atom_ionic_velocities'),
        repeats=True)

    x_onetep_section_atom_positions_optim = SubSection(
        sub_section=SectionProxy('x_onetep_section_atom_positions_optim'),
        repeats=True)

    x_onetep_section_atom_positions = SubSection(
        sub_section=SectionProxy('x_onetep_section_atom_positions'),
        repeats=True)

    x_onetep_section_cell_optim = SubSection(
        sub_section=SectionProxy('x_onetep_section_cell_optim'),
        repeats=True)

    x_onetep_section_cell = SubSection(
        sub_section=SectionProxy('x_onetep_section_cell'),
        repeats=True)


class BasisSetCellDependent(simulation.method.BasisSetCellDependent):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_basis_set_planewave_cutoff = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing plane wave cutoff as string
        ''')

    x_onetep_size_std_grid = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        size of standard grid (eV)
        ''')

    x_onetep_size_fine_grid = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        sise of fine grid (1/A)
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_enthalpy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        onetep_Enthalpy
        ''')

    x_onetep_frequency = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        onetep_frequency (cm-1)
        ''')

    x_onetep_improved_energy_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        md_forces
        ''')

    x_onetep_frame_time_0 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        onetep_store_t_md_frame
        ''')

    x_onetep_geom_iteration_index = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Index for number of iterations in geometry optimisation
        ''')

    x_onetep_pseudo_local = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Pseudopotential
        ''')

    x_onetep_pseudo_non_local = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Pseudopotential
        ''')

    x_onetep_rms_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        RMS Gradient
        ''')

    x_onetep_n_ngwf_iterations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NGWF iterations
        ''')

    x_onetep_integrated_density = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        integrated density
        ''')

    x_onetep_dispersion_correction = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Dispersion correction to the final SCF energy
        ''')

    x_onetep_ewald_correction = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Ewald correction
        ''')

    x_onetep_store_atom_forces = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces (ev/A)
        ''')

    x_onetep_store_atom_ionforces = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces (ev/A)
        ''')

    x_onetep_store_atom_localforces = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces (ev/A)
        ''')

    x_onetep_store_atom_nonlocalforces = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces (ev/A)
        ''')

    x_onetep_store_atom_nonselfforces = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces (ev/A)
        ''')

    x_onetep_store_atom_corrforces = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces (ev/A)
        ''')

    x_onetep_initial_scf_iteration_wall_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Initial SCF iteration wall time
        ''')

    x_onetep_total_dispersion_corrected_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Total electronic energy that includes dispersion energy computed with
        Disp_method_name not corrected for finite basis-set
        ''')

    x_onetep_total_energy_corrected_for_finite_basis = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        onetep_total_energy_corrected_for_finite_basis
        ''')

    x_onetep_total_energy_corrected_for_finite_basis_store = Quantity(
        type=str,
        shape=[],
        description='''
        onetep_total_energy_corrected_for_finite_basis_store
        ''')

    x_onetep_number_of_scf_iterations_store = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of scf iterations in single point calculation
        ''')

    x_onetep_energy_total_scf_iteration_list = Quantity(
        type=np.dtype(np.float64),
        shape=[-1],
        description='''
        Total electronic energy calculated with XC_method_scf during the scf iterations is
        stored in a list
        ''')

    x_onetep_ts_coordinate_path = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TS coordinate path
        ''')

    x_onetep_energy_reac = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy of reactant
        ''')

    x_onetep_energy_prod = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy of product
        ''')

    x_onetep_geom_optim_energy_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy of product
        ''')

    x_onetep_energy_lst_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy of LST max
        ''')

    x_onetep_location_lst_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        location of LST max
        ''')

    x_onetep_barrier_reac = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        barrier from reac
        ''')

    x_onetep_barrier_prod = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        barrier from prod
        ''')

    x_onetep_reaction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        reaction energy
        ''')

    x_onetep_section_scf_k_points = SubSection(
        sub_section=SectionProxy('x_onetep_section_scf_k_points'),
        repeats=True)

    x_onetep_section_spin_number = SubSection(
        sub_section=SectionProxy('x_onetep_section_spin_number'),
        repeats=True)

    x_onetep_section_stress_tensor = SubSection(
        sub_section=SectionProxy('x_onetep_section_stress_tensor'),
        repeats=True)

    x_onetep_section_tddft = SubSection(sub_section=x_onetep_section_tddft.m_def, repeats=True)


class Energy(simulation.calculation.Energy):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_pseudopotential_local = SubSection(sub_section=simulation.calculation.EnergyEntry.m_def)

    x_onetep_pseudopotential_non_local = SubSection(sub_section=simulation.calculation.EnergyEntry.m_def)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_functional_and_weight = Quantity(
        type=str,
        shape=[],
        description='''
        XC functional+weight in onetep convention
        ''')

    x_onetep_section_functional_definition = SubSection(
        sub_section=SectionProxy('x_onetep_section_functional_definition'),
        repeats=True)

    x_onetep_section_functionals = SubSection(
        sub_section=SectionProxy('x_onetep_section_functionals'),
        repeats=True)

    x_onetep_section_relativity_treatment = SubSection(
        sub_section=SectionProxy('x_onetep_section_relativity_treatment'),
        repeats=True)

    x_onetep_input_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        '''
    )


class GeometryOptimization(workflow.GeometryOptimization):

    m_def = Section(validate=False, extends_base_section=True)

    geometry_optimization_frequency_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Specifies the estimated average phonon frequency (as an energy) used to initialize
        the inverse Hessian matrix for geometry optimization. (eV))
        ''')

    x_onetep_max_number_of_steps = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Number_of iterations geom_optim
        ''')

    geometry_optimization_geometry_conv_win = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        geom optim number of consecutive iterations during which convergence must be met
        ''')


class MolecularDynamics(workflow.MolecularDynamics):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_thermostat_target_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        thermostat_target_temperature(K)
        ''')

    x_onetep_barostat_type = Quantity(
        type=str,
        shape=[],
        description='''
        barostat_type
        ''')

    x_onetep_thermostat_type = Quantity(
        type=str,
        shape=[],
        description='''
        thermostat_type
        ''')

    x_onetep_thermostat_tau = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        thermostat_type
        ''')

    x_onetep_barostat_tau = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        barostat_tau
        ''')

    x_onetep_integrator_dt = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        MD_time_step (ps)
        ''')

    x_onetep_number_of_steps_requested = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        MD_time_step_number
        ''')

    x_onetep_frame_pressure = Quantity(
        type=str,
        shape=[],
        description='''
        MD_pressure
        ''')

    x_onetep_frame_energy_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        MD_scf_energy tolerance (eV)
        ''')

    x_onetep_frame_eigen_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        MD_scf_eigen tolerance (eV)
        ''')


class BandStructure(simulation.calculation.BandStructure):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_k_path = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_onetep_store_k_path = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_onetep_section_eigenvalues_1 = SubSection(
        sub_section=SectionProxy('x_onetep_section_eigenvalues_1'),
        repeats=True)

    x_onetep_section_eigenvalues = SubSection(
        sub_section=SectionProxy('x_onetep_section_eigenvalues'),
        repeats=True)

    x_onetep_section_k_band = SubSection(
        sub_section=SectionProxy('x_onetep_section_k_band'),
        repeats=True)

    x_onetep_section_k_points_1 = SubSection(
        sub_section=SectionProxy('x_onetep_section_k_points_1'),
        repeats=True)

    x_onetep_section_k_points = SubSection(
        sub_section=SectionProxy('x_onetep_section_k_points'),
        repeats=True)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_scf_rms_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        RMS Gradient
        ''')


class AtomParameters(simulation.method.AtomParameters):

    m_def = Section(validate=False, extends_base_section=True)

    x_onetep_store_atom_mass = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing atom mass
        ''')

    x_onetep_n_ngwf_atom_store = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number ngwf per atom
        ''')

    x_onetep_ngwf_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        radius ngwf
        ''')

    x_onetep_n_ngwf_atom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number ngwf per atom
        ''')

    x_onetep_ngwf_radius_store = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        radius ngwf
        ''')

    x_onetep_store_atom_name = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing atom name
        ''')
