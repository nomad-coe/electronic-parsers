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
    Reference
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_qe_section_parallel(MSection):
    '''
    section for run-time parallization options of Quantum Espresso
    '''

    m_def = Section(validate=False)

    x_qe_nthreads = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of OpenMP threads
        ''')

    x_qe_nproc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of MPI ranks
        ''')

    x_qe_npool = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of K-Point pools
        ''')


class x_qe_section_compile_options(MSection):
    '''
    section for compile-time options of Quantum Espresso
    '''

    m_def = Section(validate=False)

    x_qe_ntypx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum number of different atom species
        ''')

    x_qe_ndmx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum dimension of radial grid (Pseudopotential)
        ''')

    x_qe_npk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum number of k-points
        ''')

    x_qe_lmaxx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum non local angular momentum (Pseudopotential)
        ''')

    x_qe_nbrx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum number of beta functions (Pseudopotential)
        ''')

    x_qe_nqfx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum number of coefficients in Q smoothing (Pseudopotential)
        ''')

    x_qe_nchix = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum number of atomic wavefunctions per Pseudopotential
        ''')

    x_qe_compile_parallel_version = Quantity(
        type=str,
        shape=[],
        description='''
        Parallelization compile-time options
        ''')


class x_qe_t_section_pp_report(MSection):
    '''
    section to collect 'pseudopotential report' information in new QE, used only for
    'old', non-UPF pseudopotentials
    '''

    m_def = Section(validate=False)

    x_qe_t_pp_report_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: PP report: species number
        ''')

    x_qe_t_pp_report_version = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: PP report: pp version
        ''')

    x_qe_t_pp_report_line = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: PP report: parsed line
        ''')


class x_qe_t_section_pp_warning(MSection):
    '''
    section to collect 'pseudopotential warning' information in old QE
    '''

    m_def = Section(validate=False)

    x_qe_t_pp_warning_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential: pp index
        ''')

    x_qe_t_pp_warning_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential: filename
        ''')

    x_qe_t_pp_warning_wfcidx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential: pseudo-wavefunction index
        ''')

    x_qe_t_pp_warning_wfclabel = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential: pseudo-wavefunction label
        ''')

    x_qe_t_pp_warning_wfcnorm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential: pseudo-wavefunction original norm
        ''')


class x_qe_t_section_pseudopotential(MSection):
    '''
    pseudo-section for collecting pseudopotential data (atomic number lookup requires
    table printed later in output)
    '''

    m_def = Section(validate=False)

    x_qe_t_pp_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Index of Pseudopotential on Espresso side
        ''')

    x_qe_t_pp_ndmx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Radial grid of Pseudopotential on Espresso side
        ''')

    x_qe_t_pp_label = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Label of Pseudopotential on Espresso side
        ''')

    x_qe_t_pp_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Filename of pseudopotential
        ''')

    x_qe_t_pp_type = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Type of pseudopotential, e.g. 'Norm-conserving' or 'Ultrasoft'
        ''')

    x_qe_t_pp_md5sum = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: MD5 checksum of pseudopotential file
        ''')

    x_qe_t_pp_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: comment about pseudopotential
        ''')

    x_qe_t_pp_integral_ndirections = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: number of integration directions (PAW)
        ''')

    x_qe_t_pp_integral_lmax_exact = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: maximum l for which integration is exact (PAW)
        ''')

    x_qe_t_pp_augmentation_shape = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: shape of augmentation charge
        ''')

    x_qe_t_pp_valence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Number of Valence electrons in pseudopotential
        ''')

    x_qe_t_pp_nbeta = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Number of beta functions in pseudopotential on Espresso side
        ''')

    x_qe_t_pp_l_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: beta function l index in pseudopotential on Espresso side
        ''')

    x_qe_t_pp_l = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: beta function l in pseudopotential on Espresso side
        ''')

    x_qe_t_pp_ncoefficients = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Number of coefficients in pseudopotential
        ''')

    x_qe_t_rinner = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Inner Radii of pseudopotential
        ''')


class x_qe_section_scf_diagonalization(MSection):
    '''
    section for diagonalization info in QE scf iterations
    '''

    m_def = Section(validate=False)

    x_qe_t_scf_diagonalization_algorithm = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Diagonalization algorithm
        ''')

    x_qe_scf_diagonalization_algorithm = Quantity(
        type=str,
        shape=[],
        description='''
        Diagonalization algorithm
        ''')

    x_qe_scf_diagonalization_warn_n_unconverged_eigenvalues = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of uncoverged eigenvalues (Warning)
        ''')

    x_qe_scf_diagonalization_c_bands_n_unconverged_eigenvalues = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of uncoverged eigenvalues (Warning from function c_bands)
        ''')

    x_qe_scf_diagonalization_ethr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence Threshold in scf diagonalization
        ''')

    x_qe_scf_diagonalization_iteration_avg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Average of iterations in scf diagonalization
        ''')


class x_qe_section_bands_diagonalization(MSection):
    '''
    section for diagonalization info in QE band structure calculation
    '''

    m_def = Section(validate=False)

    x_qe_t_bands_diagonalization_algorithm = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Diagonalization algorithm
        ''')

    x_qe_bands_diagonalization_algorithm = Quantity(
        type=str,
        shape=[],
        description='''
        Diagonalization algorithm
        ''')

    x_qe_bands_diagonalization_warn_n_unconverged_eigenvalues = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of uncoverged eigenvalues (Warning)
        ''')

    x_qe_bands_diagonalization_c_bands_n_unconverged_eigenvalues = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of uncoverged eigenvalues (Warning from function c_bands)
        ''')

    x_qe_bands_diagonalization_ethr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence Threshold in bands diagonalization
        ''')

    x_qe_bands_diagonalization_iteration_avg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Average of iterations in bands diagonalization
        ''')


class x_qe_t_section_input_occupations(MSection):
    '''
    Temporary: Section for User-specified band occupations
    '''

    m_def = Section(validate=False)

    x_qe_t_input_occupations_spin = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: User-specified band occupations, spin channel
        ''')

    x_qe_t_input_occupations = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: User-specified band occupations
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_extra_SCF = Quantity(
        type=bool,
        shape=[],
        description='''
        Extra SCF without electronic history at the end of relaxation. Triggered in
        magnetic simulations when relax converges to non-magnetic solution
        ''')

    x_qe_t_spin_channel = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for spin channel
        ''')

    x_qe_t_k_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for k-point, x-component
        ''')

    x_qe_t_k_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for k-point, y-component
        ''')

    x_qe_t_k_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for k-point, z-component
        ''')

    x_qe_t_k_pw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: number of plane waves for this k-point
        ''')

    x_qe_t_k_point_energies = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: k-point band energies
        ''')

    x_qe_energy_total_harris_foulkes_estimate = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Harris-Foulkes estimate of total energy
        ''')

    x_qe_energy_total_accuracy_estimate = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Accuracy estimate of total energy
        ''')

    x_qe_energy_exchange_error_estimate = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Estimated error on exchange
        ''')

    x_qe_energy_exchange_average_fock_potential = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Averaged Fock potential
        ''')

    x_qe_energy_fock = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Fock energy
        ''')

    x_qe_energy_total_paw_all_electron = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        All-electron total energy from PAW
        ''')

    x_qe_t_energy_reference_highest_occupied = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Energy of highest occupied state
        ''')

    x_qe_t_energy_reference_lowest_unoccupied = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy of lowest unoccupied state
        ''')

    x_qe_t_energy_reference_fermi = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Fermi Energy
        ''')

    x_qe_t_energy_reference_fermi_up = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Fermi Energy (spin up)
        ''')

    x_qe_t_energy_reference_fermi_down = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Fermi Energy (spin down)
        ''')

    x_qe_t_energy_decomposition_name = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Total energy decomposition: contribution name
        ''')

    x_qe_t_energy_decomposition_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Total energy decomposition: contribution value
        ''')

    x_qe_energy_decomposition_name = Quantity(
        type=str,
        shape=['x_qe_number_of_energy_components'],
        description='''
        Total energy decomposition: contribution name
        ''')

    x_qe_energy_decomposition_value = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_number_of_energy_components'],
        description='''
        Total energy decomposition: contribution value
        ''')

    x_qe_magnetization_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Total per-cell magnetization
        ''')

    x_qe_magnetization_absolute = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Absolute per-cell magnetization
        ''')

    x_qe_convergence_iterations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of iterations after which self-consistency has been achieved
        ''')

    x_qe_exx_refine = Quantity(
        type=bool,
        shape=[],
        description='''
        Flag: Exact-exchange refinement is active
        ''')

    x_qe_exx_self_consistency = Quantity(
        type=bool,
        shape=[],
        description='''
        Exact-exchange has been reached (flag)
        ''')

    x_qe_output_datafile = Quantity(
        type=str,
        shape=[],
        description='''
        Output datafile
        ''')

    x_qe_t_force_atom_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_force_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_force_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_force_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_dispersion_force_atom_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_atom_dispersion_force = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        -
        ''')

    x_qe_t_dispersion_force_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_dispersion_force_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_dispersion_force_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_dispersion_force_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_force_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_force_total_scf_correction = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_stress_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_stress_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_t_stress_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_stress_unimplemented = Quantity(
        type=str,
        shape=[],
        description='''
        Reason why stress tensor is not implemented
        ''')

    x_qe_t_md_iteration = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: MD step: iteration number
        ''')

    x_qe_t_projected_velocity = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: MD step: projected velocity
        ''')

    x_qe_t_md_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        MD step: time
        ''')

    x_qe_t_md_vec_a_units = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for new direct lattice vectors (vc-relax), units
        ''')

    x_qe_t_md_vec_a_alat = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new direct lattice vectors (vc-relax), lattice parameter a
        ''')

    x_qe_t_md_vec_a_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new direct lattice vectors (vc-relax), x-component
        ''')

    x_qe_t_md_vec_a_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new direct lattice vectors (vc-relax), y-component
        ''')

    x_qe_t_md_vec_a_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new direct lattice vectors (vc-relax), z-component
        ''')

    x_qe_t_md_atom_positions_units = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for new atom positions (MD, (vc-)relax), units
        ''')

    x_qe_t_md_atom_positions_units_vcsmd = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for new atom positions (MD, (vc-)relax via VCSMD), units
        ''')

    x_qe_t_md_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for new atom positions (MD, (vc-)relax), atom labels
        ''')

    x_qe_t_md_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new atom positions (MD, (vc-)relax), x-component
        ''')

    x_qe_t_md_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new atom positions (MD, (vc-)relax), y-component
        ''')

    x_qe_t_md_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new atom positions (MD, (vc-)relax), z-component
        ''')

    x_qe_t_md_atom_free_x = Quantity(
        type=bool,
        shape=[],
        description='''
        Temporary storage for new atom fixed flag (MD, (vc-)relax), x-component
        ''')

    x_qe_t_md_atom_free_y = Quantity(
        type=bool,
        shape=[],
        description='''
        Temporary storage for new atom fixed flag (MD, (vc-)relax), y-component
        ''')

    x_qe_t_md_atom_free_z = Quantity(
        type=bool,
        shape=[],
        description='''
        Temporary storage for new atom fixed flag (MD, (vc-)relax), z-component
        ''')

    x_qe_t_new_nat2_distance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new 2-atom distance (MD, (vc-)relax)
        ''')

    x_qe_t_md_atom_mass_label = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for MD setup, atom mass, labels
        ''')

    x_qe_t_md_atom_mass_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for MD setup, atom mass, value
        ''')

    x_qe_t_md_timestep_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for MD setup, timestep size
        ''')

    x_qe_t_md_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for MD, kinetic energy
        ''')

    x_qe_t_md_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for MD, temperature
        ''')

    x_qe_t_md_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for MD, total energy
        ''')

    x_qe_t_md_ekin_etot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for MD, sum of energies
        ''')

    x_qe_t_md_linear_momentum_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for linear momentum (MD, (vc-)relax), x-component
        ''')

    x_qe_t_md_linear_momentum_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for linear momentum (MD, (vc-)relax), y-component
        ''')

    x_qe_t_md_linear_momentum_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for linear momentum (MD, (vc-)relax), z-component
        ''')

    x_qe_t_md_write_datafile_cputime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for cpu time after write-datafile (MD, (vc-)relax)
        ''')

    x_qe_t_md_write_datafile_mem_dynamical = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for dynamical memory after write-datafile (MD, (vc-)relax)
        ''')

    x_qe_t_md_extrapolation_charge = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for charge extrapolation scheme (MD, (vc-)relax)
        ''')

    x_qe_t_md_extrapolation_wfc = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for wave function extrapolation scheme (MD, (vc-)relax)
        ''')

    x_qe_t_md_starting_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for extrapolated starting charge (MD, (vc-)relax)
        ''')

    x_qe_t_md_starting_charge_renormalized = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for extrapolated starting charge, renormalized (MD, (vc-)relax)
        ''')

    x_qe_t_md_max_steps_reached = Quantity(
        type=bool,
        shape=[],
        description='''
        Temporary storage for max_steps-reached flag (MD, (vc-)relax)
        ''')

    x_qe_t_md_end = Quantity(
        type=bool,
        shape=[],
        description='''
        Temporary storage for end-of-md flag (MD, (vc-)relax)
        ''')

    x_qe_t_md_diffusion_atomidx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for diffusion coeffients (MD), atom index
        ''')

    x_qe_t_md_diffusion_coefficient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for diffusion coeffients (MD), atom coeffient
        ''')

    x_qe_t_md_diffusion_coefficient_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for diffusion coeffients (MD), mean coeffient
        ''')

    x_qe_t_md_bfgs_scf_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for number of scf cycles (relax)
        ''')

    x_qe_t_md_bfgs_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for number of steps (relax)
        ''')

    x_qe_t_md_bfgs_energy_old = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for 'old' energy (relax)
        ''')

    x_qe_t_md_bfgs_energy_new = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for 'new' energy (relax)
        ''')

    x_qe_t_md_bfgs_enthalpy_old = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for 'old' enthalpy (relax)
        ''')

    x_qe_t_md_bfgs_enthalpy_new = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for 'new' enthalpy (relax)
        ''')

    x_qe_t_md_bfgs_case = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for BFGS case, energy comparison (relax)
        ''')

    x_qe_t_md_bfgs_reset = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for BFGS history reset reason (relax)
        ''')

    x_qe_t_md_bfgs_trust_new = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new trust radius (relax)
        ''')

    x_qe_t_md_bfgs_conv_thr_new = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new electronic convergence threshold (relax)
        ''')

    x_qe_t_md_starting_charge_negative_old = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for old negative starting charge (MD, (vc-)relax)
        ''')

    x_qe_t_md_starting_charge_negative_new = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new negative starting charge (MD, (vc-)relax)
        ''')

    x_qe_t_md_starting_charge_negative_new_up = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new negative starting charge (MD, (vc-)relax), spin up
        ''')

    x_qe_t_md_starting_charge_negative_new_down = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new negative starting charge (MD, (vc-)relax), spin down
        ''')

    x_qe_t_md_bfgs_converged = Quantity(
        type=bool,
        shape=[],
        description='''
        Temporary storage for 'converged' flag ((vc-)relax)
        ''')

    x_qe_t_md_bfgs_converged_criteria = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for converged criteria ((vc-)relax)
        ''')

    x_qe_t_md_bfgs_final_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for final energy ((vc-)relax)
        ''')

    x_qe_t_md_bfgs_final_enthalpy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for final enthalpy ((vc-)relax)
        ''')

    x_qe_t_md_new_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for new cell volume ((vc-)relax)
        ''')

    x_qe_t_md_isolated_system_method_martyna_tuckerman_alpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD: Isolated system with Martyna-Tuckerman method, parameter alpha
        ''')

    x_qe_t_md_isolated_system_method_martyna_tuckerman_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD: Isolated system with Martyna-Tuckerman method, parameter beta
        ''')

    x_qe_t_md_core_charge_negative = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD: QE check: negative core charge
        ''')

    x_qe_t_md_core_charge_imaginary = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD: QE check: imaginary core charge
        ''')

    x_qe_t_relax_converged_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary Relax: number of steps after which structure relaxation converged
        ''')

    x_qe_t_relax_final_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary Relax: final energy in relaxation
        ''')

    x_qe_t_relax_threshold_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary Relax: convergence threshold on energy in relaxation
        ''')

    x_qe_t_relax_threshold_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary Relax: convergence threshold on force components in relaxation
        ''')

    x_qe_t_relax_threshold_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary Relax: convergence threshold on pressure in relaxation
        ''')

    x_qe_t_md_k_info_ik = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary MD storage for k-point info, k-index
        ''')

    x_qe_t_md_k_info_vec_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD storage for k-point info, x-component
        ''')

    x_qe_t_md_k_info_vec_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD storage for k-point info, y-component
        ''')

    x_qe_t_md_k_info_vec_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD storage for k-point info, z-component
        ''')

    x_qe_t_md_k_info_wk = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary MD storage for k-point info, weight
        ''')

    x_qe_section_bands_diagonalization = SubSection(
        sub_section=SectionProxy('x_qe_section_bands_diagonalization'),
        repeats=True)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_program_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of program from Quantum Espresso suite
        ''')

    x_qe_input_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Filename input was read from
        ''')

    x_qe_t_warning = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Warnings from Quantum Espresso
        ''')

    x_qe_warning = Quantity(
        type=str,
        shape=[],
        description='''
        Warnings from Quantum Espresso
        ''')

    x_qe_profile_caller = Quantity(
        type=str,
        shape=['x_qe_number_of_profiling_entries'],
        description='''
        QE profiling: caller name
        ''')

    x_qe_profile_category = Quantity(
        type=str,
        shape=['x_qe_number_of_profiling_entries'],
        description='''
        QE profiling: category
        ''')

    x_qe_profile_function = Quantity(
        type=str,
        shape=['x_qe_number_of_profiling_entries'],
        description='''
        QE profiling: function name
        ''')

    x_qe_profile_cputime = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_number_of_profiling_entries'],
        description='''
        QE profiling: cputime spent in function
        ''')

    x_qe_profile_walltime = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_number_of_profiling_entries'],
        description='''
        QE profiling: wallclock time spent in function
        ''')

    x_qe_profile_ncalls = Quantity(
        type=np.dtype(np.int32),
        shape=['x_qe_number_of_profiling_entries'],
        description='''
        QE profiling: how often was function called
        ''')

    x_qe_t_profile_function = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: QE profiling: function name
        ''')

    x_qe_t_profile_cputime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: QE profiling: cputime spent in function
        ''')

    x_qe_t_profile_walltime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: QE profiling: wallclock time spent in function
        ''')

    x_qe_t_profile_ncalls = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: QE profiling: how often was function called
        ''')

    x_qe_t_profile_caller = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: QE profiling: who was the caller
        ''')

    x_qe_t_profile_caller_list = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: QE profiling: who was the caller (list for each function)
        ''')

    x_qe_t_profile_category = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: QE profiling: category
        ''')

    x_qe_t_profile_category_list = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: QE profiling: category (list for each function)
        ''')

    x_qe_input_positions_cell_dirname = Quantity(
        type=str,
        shape=[],
        description='''
        Directory where initial atom_positions and simulation_cell were read from
        ''')

    x_qe_input_potential_recalculated_file = Quantity(
        type=str,
        shape=[],
        description='''
        File that was used to recalculate initial potential
        ''')

    x_qe_section_parallel = SubSection(
        sub_section=SectionProxy('x_qe_section_parallel'),
        repeats=True)

    x_qe_section_compile_options = SubSection(
        sub_section=SectionProxy('x_qe_section_compile_options'),
        repeats=True)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_t_species_dispersion_correction_label = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: DFT-D species label
        ''')

    x_qe_t_species_dispersion_correction_vdw_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: DFT-D species vdW radius
        ''')

    x_qe_t_species_dispersion_correction_C6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: DFT-D species C6 coefficient
        ''')

    x_qe_dispersion_correction = Quantity(
        type=bool,
        shape=[],
        description='''
        Calculation includes semi-empirical DFT-D dispersion correction
        ''')

    x_qe_gamma_algorithms = Quantity(
        type=bool,
        shape=[],
        description='''
        Usage of gamma-only optimized algorithms
        ''')

    x_qe_exx_grid_same_as_k_grid = Quantity(
        type=bool,
        shape=[],
        description='''
        Exact-exchange k+q grid is the same as k grid (flag)
        ''')

    x_qe_diagonalization_algorithm = Quantity(
        type=str,
        shape=[],
        description='''
        Algorithm used in subspace diagonalization
        ''')

    x_qe_sticks_sum_dense = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_sum_smooth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_sum_PW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_sum_G_dense = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_sum_G_smooth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_sum_G_PW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_tot_dense = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_tot_smooth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_tot_PW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_qe_sticks_old = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_qe_t_species_integration_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: radius used to integrate charge/magnetization over (per species)
        ''')

    x_qe_t_species_integration_radius_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: radius used to integrate charge/magnetization over (per species),
        species index
        ''')

    x_qe_fock_operator_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Cutoff for defining the direct-space grid used to compute Fock exchange in EXX
        ''')

    x_qe_t_xc_functional_shortname_enforced = Quantity(
        type=str,
        shape=[],
        description='''
        Short name of User-enforced XC functional; overrides the setting implied by the
        pseudopotentials
        ''')

    x_qe_potential_convergence_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence threshold for potentials
        ''')

    x_qe_potential_mixing_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mixing scheme: parameter beta
        ''')

    x_qe_potential_mixing_iterations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Mixing scheme: number of previous iterations
        ''')

    x_qe_potential_mixing_scheme = Quantity(
        type=str,
        shape=[],
        description='''
        Mixing scheme: type of mixing
        ''')

    x_qe_xc_functional_user_enforced = Quantity(
        type=bool,
        shape=[],
        description='''
        True if the user enforced setting the XC functional; overrides the setting implied
        by the pseudopotentials
        ''')

    x_qe_xc_functional_shortname = Quantity(
        type=str,
        shape=[],
        description='''
        Short name of XC functional used in calculation
        ''')

    x_qe_xc_functional_num = Quantity(
        type=str,
        shape=[],
        description='''
        QE Index number representation of XC functional
        ''')

    x_qe_xc_iexch_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of XC functional (density exchange component) in Quantum Espresso context
        ''')

    x_qe_xc_icorr_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of XC functional (density correlation component) in Quantum Espresso context
        ''')

    x_qe_xc_igcx_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of XC functional (gradient exchange component) in Quantum Espresso context
        ''')

    x_qe_xc_igcc_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of XC functional (gradient correlation component) in Quantum Espresso context
        ''')

    x_qe_xc_imeta_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of XC functional (meta-gga component) in Quantum Espresso context
        ''')

    x_qe_xc_inlc_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of XC functional (Van-der-Waals non-local component) in Quantum Espresso
        context
        ''')

    x_qe_xc_iexch_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Quantum Espresso comment about XC functional (density exchange component)
        ''')

    x_qe_xc_icorr_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Quantum Espresso comment about XC functional (density correlation component)
        ''')

    x_qe_xc_igcx_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Quantum Espresso comment about XC functional (gradient exchange component)
        ''')

    x_qe_xc_igcc_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Quantum Espresso comment about XC functional (gradient correlation component)
        ''')

    x_qe_xc_imeta_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Quantum Espresso comment about XC functional (meta-gga component)
        ''')

    x_qe_xc_inlc_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Quantum Espresso comment about XC functional (Van-der-Waals non-local component)
        ''')

    x_qe_xc_iexch = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Quantum Espresso internal code-specific index of XC functional (density exchange
        component)
        ''')

    x_qe_xc_icorr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Quantum Espresso internal code-specific index of XC functional (density
        correlation component)
        ''')

    x_qe_xc_igcx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Quantum Espresso internal code-specific index of XC functional (gradient exchange
        component)
        ''')

    x_qe_xc_igcc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Quantum Espresso internal code-specific index of XC functional (gradient
        correlation component)
        ''')

    x_qe_xc_imeta = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Quantum Espresso internal code-specific index of XC functional (meta-gga
        component)
        ''')

    x_qe_xc_inlc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Quantum Espresso internal code-specific index of XC functional (Van-der-Waals non-
        local component)
        ''')

    x_qe_t_exact_exchange_fraction = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: store fraction of exact-exchange before defining section_xc_functionals
        ''')

    x_qe_exact_exchange_fraction = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Fraction of exact-exchange in EXX-refinement
        ''')

    x_qe_md_max_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum number of ionic+electronic steps in dynamics (MD/relax) calculation
        ''')

    x_qe_berry_efield_direction = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Finite E-field: direction
        ''')

    x_qe_berry_efield_intensity = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Berry phase with E-field: intensity
        ''')

    x_qe_berry_efield_strings_nk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Berry phase with E-field: number of k-points in string
        ''')

    x_qe_berry_efield_niter = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Berry phase with E-field: number of iterative cycles
        ''')

    x_qe_berry_efield = Quantity(
        type=bool,
        shape=[],
        description='''
        Berry phase with E-field: flag if berry-efield-calc was done
        ''')

    x_qe_t_spin_orbit_magn = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: spin-orbit msg: magnetic mode (non-)collinear / (non-)magnetic
        ''')

    x_qe_t_spin_orbit_mode = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: spin-orbit msg: with/without spin-orbit
        ''')

    x_qe_spin_orbit = Quantity(
        type=bool,
        shape=[],
        description='''
        Spin-orbit coupling flag: with/without spin-orbit
        ''')

    x_qe_spin_noncollinear = Quantity(
        type=bool,
        shape=[],
        description='''
        Noncollinear spin mode
        ''')

    x_qe_t_pp_renormalized_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential: filename
        ''')

    x_qe_t_pp_renormalized_wfc = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential
        ''')

    x_qe_t_allocated_array_name = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: allocated arrays, name
        ''')

    x_qe_t_allocated_array_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: allocated arrays, size
        ''')

    x_qe_t_allocated_array_dimensions = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: allocated arrays, dimensions
        ''')

    x_qe_allocated_array_name = Quantity(
        type=str,
        shape=['x_qe_allocated_arrays'],
        description='''
        Allocated arrays, name
        ''')

    x_qe_allocated_array_size = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_allocated_arrays'],
        description='''
        Allocated arrays, size
        ''')

    x_qe_allocated_array_dimensions = Quantity(
        type=str,
        shape=['x_qe_allocated_arrays'],
        description='''
        Allocated arrays, dimensions
        ''')

    x_qe_t_temporary_array_name = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: temporary arrays, name
        ''')

    x_qe_t_temporary_array_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: temporary arrays, size
        ''')

    x_qe_t_temporary_array_dimensions = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: temporary arrays, dimensions
        ''')

    x_qe_temporary_array_name = Quantity(
        type=str,
        shape=['x_qe_temporary_arrays'],
        description='''
        Temporary arrays, name
        ''')

    x_qe_temporary_array_size = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_temporary_arrays'],
        description='''
        Temporary arrays, size
        ''')

    x_qe_temporary_array_dimensions = Quantity(
        type=str,
        shape=['x_qe_temporary_arrays'],
        description='''
        Temporary arrays, dimensions
        ''')

    x_qe_core_charge_negative = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        QE check: negative core charge
        ''')

    x_qe_core_charge_imaginary = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        QE check: imaginary core charge
        ''')

    x_qe_core_charge_realspace = Quantity(
        type=bool,
        shape=[],
        description='''
        QE flag: core charge treated in real space
        ''')

    x_qe_starting_density_file = Quantity(
        type=str,
        shape=[],
        description='''
        Starting density from file
        ''')

    x_qe_starting_potential = Quantity(
        type=str,
        shape=[],
        description='''
        Starting potential
        ''')

    x_qe_starting_charge_negative = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Starting charge (warning about negative starting charge)
        ''')

    x_qe_starting_charge_negative_up = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Starting charge up (warning about negative starting charge)
        ''')

    x_qe_starting_charge_negative_down = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Starting charge down (warning about negative starting charge)
        ''')

    x_qe_starting_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Starting charge
        ''')

    x_qe_starting_charge_renormalized = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Starting charge, renormalized
        ''')

    x_qe_starting_wfc = Quantity(
        type=str,
        shape=[],
        description='''
        Starting Wave functions
        ''')

    x_qe_time_setup_cpu1_end = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CPU time, setup up until first iteration
        ''')

    x_qe_per_process_mem = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Per-process dynamical memory
        ''')

    x_qe_isolated_system_method = Quantity(
        type=str,
        shape=[],
        description='''
        Method used if system is assumed to be isolated
        ''')

    x_qe_isolated_system_method_martyna_tuckerman_alpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Isolated system with Martyna-Tuckerman method, parameter alpha
        ''')

    x_qe_isolated_system_method_martyna_tuckerman_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Isolated system with Martyna-Tuckerman method, parameter beta
        ''')

    x_qe_input_occupations = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_spin_channels', 'number_of_k_points', 'number_of_eigen_values'],
        description='''
        User-specified band occupations
        ''')

    x_qe_extrapolation_charge = Quantity(
        type=str,
        shape=[],
        description='''
        Charge extrapolation scheme (MD, (vc-)relax)
        ''')

    x_qe_t_section_pp_report = SubSection(
        sub_section=SectionProxy('x_qe_t_section_pp_report'),
        repeats=True)

    x_qe_t_section_pp_warning = SubSection(
        sub_section=SectionProxy('x_qe_t_section_pp_warning'),
        repeats=True)

    x_qe_t_section_pseudopotential = SubSection(
        sub_section=SectionProxy('x_qe_t_section_pseudopotential'),
        repeats=True)

    x_qe_t_section_input_occupations = SubSection(
        sub_section=SectionProxy('x_qe_t_section_input_occupations'),
        repeats=True)


class AtomParameters(simulation.method.AtomParameters):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_dispersion_correction_vdw_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        DFT-D species vdW radius
        ''')

    x_qe_dispersion_correction_C6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        DFT-D species C6 coefficient
        ''')

    x_qe_species_integration_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Radius used to integrate charge/magnetization over (per species)
        ''')

    x_qe_pp_renormalized_wfc = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: renormalized WFCs in pseudopotential
        ''')

    x_qe_pp_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Index of Pseudopotential on Espresso side
        ''')

    x_qe_pp_label = Quantity(
        type=str,
        shape=[],
        description='''
        Label of Pseudopotential on Espresso side
        ''')

    x_qe_pp_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Filename of pseudopotential
        ''')

    x_qe_pp_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of pseudopotential, e.g. 'Norm-conserving' or 'Ultrasoft'
        ''')

    x_qe_pp_md5sum = Quantity(
        type=str,
        shape=[],
        description='''
        MD5 checksum of pseudopotential file
        ''')

    x_qe_pp_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Comment about pseudopotential
        ''')

    x_qe_pp_integral_ndirections = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of integration directions (PAW)
        ''')

    x_qe_pp_integral_lmax_exact = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum l for which integration is exact (PAW)
        ''')

    x_qe_pp_augmentation_shape = Quantity(
        type=str,
        shape=[],
        description='''
        Shape of augmentation charge
        ''')

    x_qe_pp_report_version = Quantity(
        type=str,
        shape=[],
        description='''
        Pseudopotential report: version of PP
        ''')

    x_qe_pp_report_contents = Quantity(
        type=str,
        shape=[],
        description='''
        Pseudopotential report: contents of PP report
        ''')

    x_qe_pp_valence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Number of Valence electrons in pseudopotential
        ''')

    x_qe_pp_weight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_qe_pp_ncoefficients = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of coefficients in pseudopotential
        ''')

    x_qe_rinner = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Inner Radii of pseudopotential
        ''')

    x_qe_kind_mass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atomic mass of species
        ''')

    x_qe_pp_ndmx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Radial grid of Pseudopotential on Espresso side
        ''')

    x_qe_pp_nbeta = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of beta functions in pseudopotential on Espresso side
        ''')

    x_qe_pp_l_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Beta function l index in pseudopotential on Espresso side
        ''')

    x_qe_pp_l = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Beta function l in pseudopotential on Espresso side
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_ibrav = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Bravais lattice index, constant during a run
        ''')

    x_qe_alat = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Lattice Parameter 'a', constant during a run and used as unit in other quantities
        ''')

    x_qe_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Volume of unit cell
        ''')

    x_qe_number_of_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of Atom species, a.k.a. unique Atom labels; a label may include symmetry-
        breaking suffices, e.g. 'Fe1' and 'Fe2', as some quantities can only prescribed
        per species and not per site
        ''')

    x_qe_t_number_of_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Number of electrons in system
        ''')

    x_qe_t_number_of_electrons_up = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Number of electrons in system (spin up)
        ''')

    x_qe_t_number_of_electrons_down = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Number of electrons in system (spin down)
        ''')

    x_qe_number_of_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of Kohn-Sham states/bands
        ''')

    x_qe_md_cell_mass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mass of cell in MD/relax calculation
        ''')

    x_qe_t_celldm = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for QE cell dimensions
        ''')

    x_qe_celldm = Quantity(
        type=np.dtype(np.float64),
        shape=[6],
        description='''
        QE cell dimensions
        ''')

    x_qe_t_vec_supercell_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for supercell translation vector in fractional coordinates,
        x-component
        ''')

    x_qe_t_vec_supercell_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for supercell translation vector in fractional coordinates,
        y-component
        ''')

    x_qe_t_vec_supercell_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for supercell translation vector in fractional coordinates,
        z-component
        ''')

    x_qe_vec_supercell = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_number_of_supercell_translations', 3],
        description='''
        Supercell translation vector(s) in fractional coordinates
        ''')

    x_qe_supercell = Quantity(
        type=bool,
        shape=[],
        description='''
        Supercell flag
        ''')

    x_qe_t_vec_a_units = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for direct lattice vectors, units
        ''')

    x_qe_t_vec_a_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for direct lattice vectors, x-component
        ''')

    x_qe_t_vec_a_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for direct lattice vectors, y-component
        ''')

    x_qe_t_vec_a_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for direct lattice vectors, z-component
        ''')

    x_qe_t_vec_b_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for reciprocal lattice vectors, x-component
        ''')

    x_qe_t_vec_b_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for reciprocal lattice vectors, y-component
        ''')

    x_qe_t_vec_b_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for reciprocal lattice vectors, z-component
        ''')

    x_qe_reciprocal_cell = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        unit='1 / meter',
        description='''
        Reciprocal Lattice vectors (in Cartesian coordinates). The first index runs over
        the $x,y,z$ Cartesian coordinates, and the second index runs over the 3 lattice
        vectors.
        ''')

    x_qe_t_starting_magnetization_species = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Starting magnetic configuration: Species name
        ''')

    x_qe_t_starting_magnetization_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: Starting magnetic configuration: Species magnetization
        ''')

    x_qe_atom_starting_magnetization = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Starting magnetic configuration: Atom magnetization
        ''')

    x_qe_nsymm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of detected symmetry operations
        ''')

    x_qe_nsymm_with_fractional_translation = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of detected symmetry operations including fractional translations
        ''')

    x_qe_nsymm_ignored = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of ignored symmetry operations, due to uncommensurable fractional
        translations
        ''')

    x_qe_t_symm_inversion = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Inversion symmetry
        ''')

    x_qe_symm_inversion = Quantity(
        type=bool,
        shape=[],
        description='''
        Inversion symmetry
        ''')

    x_qe_atom_idx = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atoms'],
        description='''
        Index of atom on Espresso side
        ''')

    x_qe_t_atpos_units = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Units for atom position
        ''')

    x_qe_t_atom_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Index of atom on Espresso side
        ''')

    x_qe_t_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary: Label of atom on Espresso side
        ''')

    x_qe_t_atpos_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for atom position, x-component
        ''')

    x_qe_t_atpos_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for atom position, y-component
        ''')

    x_qe_t_atpos_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for atom position, z-component
        ''')

    x_qe_nk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        K-point info, number of k-points
        ''')

    x_qe_smearing_ngauss = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        K-point info, QE number represenation of smearing technique
        ''')

    x_qe_smearing_kind = Quantity(
        type=str,
        shape=[],
        description='''
        K-point info, QE string represenation of smearing technique
        ''')

    x_qe_t_k_info_ik = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for k-point info, k-index
        ''')

    x_qe_t_k_info_vec_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for k-point info, x-component
        ''')

    x_qe_t_k_info_vec_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for k-point info, y-component
        ''')

    x_qe_t_k_info_vec_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for k-point info, z-component
        ''')

    x_qe_t_k_info_wk = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for k-point info, weight
        ''')

    x_qe_k_info_ik = Quantity(
        type=np.dtype(np.int32),
        shape=['x_qe_nk'],
        description='''
        K-point info, k-index
        ''')

    x_qe_k_info_vec = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_nk', 3],
        description='''
        K-point info, cartesian coordinate
        ''')

    x_qe_k_info_wk = Quantity(
        type=np.dtype(np.float64),
        shape=['x_qe_nk'],
        description='''
        K-point info, weight
        ''')

    x_qe_dense_g_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Dense-grid info, G cutoff
        ''')

    x_qe_dense_g_vectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Dense-grid info, number of G vectors
        ''')

    x_qe_t_dense_FFT_grid_x = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Dense-grid info, FFT grid x
        ''')

    x_qe_t_dense_FFT_grid_y = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Dense-grid info, FFT grid y
        ''')

    x_qe_t_dense_FFT_grid_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Dense-grid info, FFT grid z
        ''')

    x_qe_dense_FFT_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        Dense-grid info, FFT grid
        ''')

    x_qe_smooth_g_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smooth-grid info, G cutoff
        ''')

    x_qe_smooth_g_vectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Smooth-grid info, number of G vectors
        ''')

    x_qe_t_smooth_FFT_grid_x = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Smooth-grid info, FFT grid x
        ''')

    x_qe_t_smooth_FFT_grid_y = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Smooth-grid info, FFT grid y
        ''')

    x_qe_t_smooth_FFT_grid_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: Smooth-grid info, FFT grid z
        ''')

    x_qe_smooth_FFT_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        Smooth-grid info, FFT grid
        ''')


class Functional(simulation.method.Functional):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_xc_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of XC functional component in Quantum Espresso context
        ''')

    x_qe_xc_comment = Quantity(
        type=str,
        shape=[],
        description='''
        Quantum Espresso comment about meaning of XC functional component
        ''')

    x_qe_xc_index_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of Index within Quantum Espresso where XC functional component was set from
        ''')

    x_qe_xc_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Index value within Quantum Espresso where XC functional component was set from
        ''')


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_t_iter_mpersite_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary: iteration per-site magnetization data, atom index
        ''')

    x_qe_t_iter_mpersite_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: iteration per-site magnetization data, atom charge
        ''')

    x_qe_t_iter_mpersite_magn = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: iteration per-site magnetization data, atom magnetization
        ''')

    x_qe_t_iter_mpersite_constr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary: iteration per-site magnetization data, constraints
        ''')

    x_qe_iter_mpersite_idx = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atoms'],
        description='''
        iteration per-site magnetization data, atom index
        ''')

    x_qe_iter_mpersite_charge = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        iteration per-site magnetization data, atom charge
        ''')

    x_qe_iter_mpersite_magn = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        iteration per-site magnetization data, atom magnetization
        ''')

    x_qe_iter_mpersite_constr = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        iteration per-site magnetization data, constraints
        ''')

    x_qe_iteration_efield_eeigx_re = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        E-field: expectation value of exp(iGx), real part, in iteration
        ''')

    x_qe_iteration_efield_eeigx_im = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        E-field: expectation value of exp(iGx), imaginary part, in iteration
        ''')

    x_qe_iteration_efield_dipole_electronic = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        E-field: Electronic dipole, in iteration
        ''')

    x_qe_iteration_efield_dipole_ionic = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        E-field: Ionic dipole, in iteration
        ''')

    x_qe_iteration_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Iteration number
        ''')

    x_qe_iteration_ecutwfc = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        PW cutoff used during iteration
        ''')

    x_qe_iteration_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mixing parameter Beta during iteration
        ''')

    x_qe_iteration_charge_negative_up = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Charge in iteration (up)
        ''')

    x_qe_iteration_charge_negative_down = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Charge in iteration (down)
        ''')

    x_qe_energy_total_harris_foulkes_estimate_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Harris-Foulkes estimate of total energy
        ''')

    x_qe_energy_total_accuracy_estimate_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Accuracy estimate of total energy
        ''')

    x_qe_magnetization_total_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Total per-cell magnetization in iteration
        ''')

    x_qe_magnetization_absolute_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Absolute per-cell magnetization in iteration
        ''')

    x_qe_section_scf_diagonalization = SubSection(
        sub_section=SectionProxy('x_qe_section_scf_diagonalization'),
        repeats=True)


class BandEnergies(simulation.calculation.BandEnergies):

    m_def = Section(validate=False, extends_base_section=True)

    x_qe_eigenvalues_number_of_planewaves = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_eigenvalues_kpoints'],
        description='''
        Number of plane waves for each k-point
        ''')
