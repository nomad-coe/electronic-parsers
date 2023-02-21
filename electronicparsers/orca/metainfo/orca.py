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
from nomad.datamodel.metainfo import workflow


m_package = Package()


class x_orca_atom_positions(MSection):
    '''
    positions of an atom
    '''

    m_def = Section(validate=False)

    x_orca_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')

    x_orca_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')

    x_orca_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')


class x_orca_final_geometry(MSection):
    '''
    final optimized positions of an atom
    '''

    m_def = Section(validate=False)

    x_orca_atom_labels_geo_opt = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_atom_positions_x_geo_opt = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')

    x_orca_atom_positions_y_geo_opt = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')

    x_orca_atom_positions_z_geo_opt = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')


class x_orca_section_functionals(MSection):
    '''
    XC functional
    '''

    m_def = Section(validate=False)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_1_elect_energy_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_angular_grid = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_atomic_orbital_integral_source = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_avg_nb_grid_pts_per_atom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_avg_nb_points_per_batch = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_basis_fn_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_beckes_beta_param = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_Brueckner_orbitals_calc_on_off = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsdt_aaa_triples_contribution = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsdt_aab_triples_contribution = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ci_half_s_and_s_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ci_iteration_nb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_convergence_check_mode = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_convergence_tol_max_residuum = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_correl_functional = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_coulomb_transformation_dimension_basis = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_coulomb_transformation_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_energy_change_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_exchange_functional = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_f12_correction_on_off = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_frozen_core_treatment = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_gral_integ_accuracy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_grid_pruning_method = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_hf_method = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_hf_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_integr_weight_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_integral_package_used = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_integral_transformation = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_K_C_formation = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_lda_part_of_gga_corr = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_level_shift_amplitude_update = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_aux_basis_dimension = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_basis_dimension = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_initial_guess = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_multiplicity = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_alpha_pairs_included = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_beta_pairs_included = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_grid_pts_after_initial_pruning = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_grid_pts_after_weights_screening = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_internal_alpha_mol_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_internal_beta_mol_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_atomic_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_correlated_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nelectrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_nuclear_repulsion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_orbital_opt_on_off = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_pair_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_perturbative_triple_excitations_on_off = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_radial_grid_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_reference_wave_function = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_scalar_relativistic_method = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_scaling_mp2_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_single_excitations_on_off = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_single_norm_half_ss = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_speed_of_light_used = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_nb_batches = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_nb_grid_pts = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_nb_pairs_included = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_wave_function_correlation_treatment = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_weight_gener_scheme = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_xalpha_param = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_XC_functional_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_z_vector_calc_on_off = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_section_functionals = SubSection(
        sub_section=SectionProxy('x_orca_section_functionals'),
        repeats=True)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_angular_grid_final = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_avg_nb_grid_pts_per_atom_final = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_avg_nb_points_per_batch_final = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_basis_fn_cutoff_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_gral_integ_accuracy_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_grid_pruning_method_final = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_integr_weight_cutoff_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_iteration_nb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_last_energy_change_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_last_energy_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_last_max_density_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_last_max_density_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_last_rms_density_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_last_rms_density_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_grid_pts_after_initial_pruning_final = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_grid_pts_after_weights_screening_final = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_radial_grid_type_final = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_total_nb_batches_final = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_nb_grid_pts_final = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_weight_gener_scheme_final = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_atom_positions = SubSection(
        sub_section=SectionProxy('x_orca_atom_positions'),
        repeats=True)


class BasisSet(simulation.method.BasisSet):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_auxiliary_basis_set_contracted = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_auxiliary_basis_set = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_basis_set_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_basis_set_contracted = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_basis_set = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_highest_angular_moment_aux = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_highest_angular_moment = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_maximum_contraction_depth_aux = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_maximum_contraction_depth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_contracted_basis_functions_aux = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_contracted_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_contracted_shells_aux = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_contracted_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_primitive_gaussian_functions_aux = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_primitive_gaussian_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_primitive_gaussian_shells_aux = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_of_primitive_gaussian_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_primitive_gaussian_shells_aux = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_primitive_gaussian_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_basis_fn_evaluation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsd_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsd_final_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsd_t_final_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsd_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsdt_aba_triples_contribution = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsdt_bbb_triples_contribution = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsdt_final_corr_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ccsdt_total_triples_correction = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ci_correl_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ci_deltaE_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ci_iteration_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ci_residual_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_ci_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_coulomb_formation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_density_evaluation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_density_matrix_formation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_diagonalization = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_diis_solution = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_elec_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_exchange_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_exchange_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_final_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_fock_matrix_formation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_geo_opt_cycle = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_grid_generation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_initial_guess = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_kinetc_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_corr_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_energy_spin_aa = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_energy_spin_ab = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_energy_spin_bb = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_mp2_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_elect_alpha_channel = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_elect_beta_channel = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_nb_elect_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_nuc_repulsion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_one_elec_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_orbital_orthonormalization = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_orbital_transformation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_population_analysis = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_potential_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_potential_evaluation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_split_rj = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_sum_individual_times = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_t1_diagnostic = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_T_and_T_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_days_time = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_hours_time = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_mins_time = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_total_secs_time = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_orca_two_elec_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_virial_ratio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_xc_functional_evaluation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_xc_integration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')


class GeometryOptimization(workflow.GeometryOptimization):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_coords_choice_name = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_coords_choice = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_energy_change_tol_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_energy_change_tol = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_initial_hessian_name = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_initial_hessian = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_max_displacement_tol_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_max_displacement_tol = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_max_gradient_tol_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_max_gradient_tol = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_rms_displacement_tol_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_rms_displacement_tol = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_rms_gradient_tol_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_rms_gradient_tol = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_update_method_name = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_update_method = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_final_geometry = SubSection(
        sub_section=SectionProxy('x_orca_final_geometry'),
        repeats=True)


class Spectra(simulation.calculation.Spectra):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_excitation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_oscillator_strength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_transition_dipole_moment_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_transition_dipole_moment_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_orca_transition_dipole_moment_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_orca_program_compilation_date = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_program_compilation_time = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_orca_program_svn = Quantity(
        type=str,
        shape=[],
        description='''
        svn revision of the program
        ''')

    x_orca_program_version = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')
