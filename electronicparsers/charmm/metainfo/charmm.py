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


class x_charmm_mdin_input_output_files(MCategory):
    '''
    Parameters of mdin belonging to x_charmm_section_control_parameters.
    '''

    m_def = Category()


class x_charmm_mdin_control_parameters(MCategory):
    '''
    Parameters of mdin belonging to x_charmm_section_control_parameters.
    '''

    m_def = Category()


class x_charmm_mdin_method(MCategory):
    '''
    Parameters of mdin belonging to section method.
    '''

    m_def = Category()


class x_charmm_mdout_single_configuration_calculation(MCategory):
    '''
    Parameters of mdout belonging to section_single_configuration_calculation.
    '''

    m_def = Category()


class x_charmm_mdout_method(MCategory):
    '''
    Parameters of mdin belonging to section method.
    '''

    m_def = Category()


class x_charmm_mdout_run(MCategory):
    '''
    Parameters of mdin belonging to settings run.
    '''

    m_def = Category()


class x_charmm_mdin_run(MCategory):
    '''
    Parameters of mdin belonging to settings run.
    '''

    m_def = Category()


class x_charmm_section_input_output_files(MSection):
    '''
    Section to store input and output file names
    '''

    m_def = Section(validate=False)


class x_charmm_section_control_parameters(MSection):
    '''
    Section to store the input and output control parameters
    '''

    m_def = Section(validate=False)

    x_charmm_inout_file_structure = Quantity(
        type=str,
        shape=[],
        description='''
        charmm input topology file.
        ''')

    x_charmm_inout_file_trajectory = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output trajectory file.
        ''')

    x_charmm_inout_file_traj_coord = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output trajectory file.
        ''')

    x_charmm_inout_file_traj_vel = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output file for velocities in the trajectory.
        ''')

    x_charmm_inout_file_traj_force = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output file for forces in the trajectory.
        ''')

    x_charmm_inout_file_output_coord = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output coordinates file.
        ''')

    x_charmm_inout_file_out_coor_str = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output coordinates on log.
        ''')

    x_charmm_inout_file_output_vel = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output velocities file.
        ''')

    x_charmm_inout_file_output_force = Quantity(
        type=str,
        shape=[],
        description='''
        charmm output forces file.
        ''')

    x_charmm_inout_file_input_coord = Quantity(
        type=str,
        shape=[],
        description='''
        charmm input coordinates file.
        ''')

    x_charmm_inout_file_in_coor_str = Quantity(
        type=str,
        shape=[],
        description='''
        charmm input coordinate on log file.
        ''')

    x_charmm_inout_file_input_vel = Quantity(
        type=str,
        shape=[],
        description='''
        charmm input velocities file.
        ''')

    x_charmm_inout_file_restart_coord = Quantity(
        type=str,
        shape=[],
        description='''
        charmm restart coordinates file.
        ''')

    x_charmm_inout_file_restart_vel = Quantity(
        type=str,
        shape=[],
        description='''
        charmm restart velocities file.
        ''')

    x_charmm_inout_file_rtf_file = Quantity(
        type=str,
        shape=[],
        description='''
        charmm RTF residue file.
        ''')

    x_charmm_inout_file_prm_file = Quantity(
        type=str,
        shape=[],
        description='''
        charmm PRM parameter file.
        ''')

    x_charmm_inout_file_cor_file = Quantity(
        type=str,
        shape=[],
        description='''
        charmm CRD coordinates file.
        ''')

    x_charmm_inout_file_stream = Quantity(
        type=str,
        shape=[],
        description='''
        charmm stream input/output.
        ''')

    x_charmm_inout_file_rtf_str = Quantity(
        type=str,
        shape=[],
        description='''
        charmm stream RTF input.
        ''')

    x_charmm_inout_file_par_str = Quantity(
        type=str,
        shape=[],
        description='''
        charmm stream parameter input.
        ''')

    x_charmm_inout_file_output_log = Quantity(
        type=str,
        shape=[],
        description='''
        charmm MD output log file.
        ''')

    x_charmm_inout_control_gaussian_option_is = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_crystal = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_crystal_type = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_a_length = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_b_length = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_c_length = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_alpha = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_beta = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_gamma = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_mini = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nstep = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_inbfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_step = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_prtmin = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tolfun = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tolgrd = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tolitr = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tolstp = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tfreq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pcut = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ihbfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ncgcyc = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nprint = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nonbond_option_flags = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_cutnb = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ctexnb = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ctonnb = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ctofnb = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_cgonnb = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_cgofnb = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_wmin = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_cdie = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_switch = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_vswitch = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_atoms = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_wrnmxd = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_e14fac = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_eps = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nbxmod = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hydrogen_bond_cutoff_distance = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hydrogen_bond_cutoff_angle = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hydrogen_bond_switching_on_distance = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hydrogen_bond_switching_off_distance = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hydrogen_bond_switching_on_angle = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hydrogen_bond_switching_off_angle = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hbond_exclusions_due_to_distance_cutoff = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hbond_exclusions_due_to_angle_cutoff = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_acceptor_antecedents = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hbond_exclusions_due_to_duplications = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hbond_deletions_due_to_best_option = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hbond_deletions_due_to_duplications = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hbond_deletions_due_to_fixed_atoms = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hbond_deletions_due_to_exclusion = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hydrogen_bonds_present = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_minimization_exit_status = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_dyna = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_akmastp = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_firstt = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iseed = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iprfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ihtfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ieqfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iunrea = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iunwri = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iunos = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iuncrd = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iunvel = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iunxyz = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_kunit = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nsavc = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nsavv = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nsavx = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iscale = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iscvel = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iasors = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_iasvel = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ichecw = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ntrfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ilbfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_imgfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_isvfrq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_ncycle = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_nsnos = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_teminc = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tstruc = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_finalt = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_twindh = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_twindl = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_time_step = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_random_num_gen_seeds = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_number_of_degrees_of_freedom = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_gaussian_option = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_velocities_assigned_at_temperature = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_seeds = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_shake_tolerance = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_strt = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_rest = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_qref = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tref = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_hoover = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_reft = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_tmass = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pcons = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pmass = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_number_of_steps = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_steps_per_cycle = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_initial_temperature = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_dielectric = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_excluded_species_or_groups = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_1_4_electrostatics_scale = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_velocity_rescale_temp = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_velocity_reassignment_freq = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_velocity_reassignment_temp = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_langevin_dynamics = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_langevin_temperature = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_langevin_integrator = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_langevin_damping_coefficient_unit = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_temperature_coupling = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_coupling_temperature = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_target_pressure = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_langevin_oscillation_period = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_langevin_decay_time = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_langevin_piston_temperature = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pressure_control = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_particle_mesh_ewald = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pme_tolerance = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pme_ewald_coefficient = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pme_interpolation_order = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pme_grid_dimensions = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_pme_maximum_grid_spacing = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_minimization = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_verlet_integrator = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_random_number_seed = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_structure_file = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_parameter_file = Quantity(
        type=str,
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_number_of_parameters = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_inout_control_parameters = Quantity(
        type=str,
        shape=['x_charmm_inout_control_number_of_parameters'],
        description='''
        charmm running environment and control parameters.
        ''')

    x_charmm_section_input_output_files = SubSection(
        sub_section=SectionProxy('x_charmm_section_input_output_files'),
        repeats=True)


class x_charmm_section_atom_to_atom_type_ref(MSection):
    '''
    Section to store atom label to atom type definition list
    '''

    m_def = Section(validate=False)

    x_charmm_atom_to_atom_type_ref = Quantity(
        type=np.dtype(np.int64),
        shape=['number_of_atoms_per_type'],
        description='''
        Reference to the atoms of each atom type.
        ''')


class x_charmm_section_single_configuration_calculation(MSection):
    '''
    section for gathering values for MD steps
    '''

    m_def = Section(validate=False)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_charmm_atom_positions_image_index = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atoms', 3],
        unit='dimensionless',
        description='''
        PBC image flag index.
        ''')

    x_charmm_atom_positions_scaled = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        unit='dimensionless',
        description='''
        Position of the atoms in a scaled format [0, 1].
        ''')

    x_charmm_atom_positions_wrapped = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        unit='meter',
        description='''
        Position of the atoms wrapped back to the periodic box.
        ''')

    x_charmm_lattice_lengths = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Lattice dimensions in a vector. Vector includes [a, b, c] lengths.
        ''',)

    x_charmm_lattice_angles = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Angles of lattice vectors. Vector includes [alpha, beta, gamma] in degrees.
        ''',)

    x_charmm_dummy = Quantity(
        type=str,
        shape=[],
        description='''
        dummy
        ''')

    x_charmm_mdin_finline = Quantity(
        type=str,
        shape=[],
        description='''
        finline in mdin
        ''')

    x_charmm_traj_timestep_store = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_traj_number_of_atoms_store = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_traj_box_bound_store = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_traj_box_bounds_store = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_traj_variables_store = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_traj_atoms_store = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')


class MolecularDynamics(workflow.MolecularDynamics):

    m_def = Section(validate=False, extends_base_section=True)

    x_charmm_barostat_target_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='pascal',
        description='''
        MD barostat target pressure.
        ''',)

    x_charmm_barostat_tau = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='second',
        description='''
        MD barostat relaxation time.
        ''',)

    x_charmm_barostat_type = Quantity(
        type=str,
        shape=[],
        description='''
        MD barostat type, valid values are defined in the barostat_type wiki page.
        ''',)

    x_charmm_integrator_dt = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='second',
        description='''
        MD integration time step.
        ''',)

    x_charmm_integrator_type = Quantity(
        type=str,
        shape=[],
        description='''
        MD integrator type, valid values are defined in the integrator_type wiki page.
        ''',)

    x_charmm_periodicity_type = Quantity(
        type=str,
        shape=[],
        description='''
        Periodic boundary condition type in the sampling (non-PBC or PBC).
        ''',)

    x_charmm_langevin_gamma = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='second',
        description='''
        Langevin thermostat damping factor.
        ''',)

    x_charmm_number_of_steps_requested = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Number of requested MD integration time steps.
        ''',)

    x_charmm_thermostat_level = Quantity(
        type=str,
        shape=[],
        description='''
        MD thermostat level (see wiki: single, multiple, regional).
        ''',)

    x_charmm_thermostat_target_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        MD thermostat target temperature.
        ''',)

    x_charmm_thermostat_tau = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='second',
        description='''
        MD thermostat relaxation time.
        ''',)

    x_charmm_thermostat_type = Quantity(
        type=str,
        shape=[],
        description='''
        MD thermostat type, valid values are defined in the thermostat_type wiki page.
        ''',)


class AtomParameters(simulation.method.AtomParameters):

    m_def = Section(validate=False, extends_base_section=True)

    x_charmm_atom_name = Quantity(
        type=str,
        shape=[],
        description='''
        Atom name of an atom in topology definition.
        ''')

    x_charmm_atom_type = Quantity(
        type=str,
        shape=[],
        description='''
        Atom type of an atom in topology definition.
        ''')

    x_charmm_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom type of an atom in topology definition.
        ''')

    x_charmm_atom_type_element = Quantity(
        type=str,
        shape=[],
        description='''
        Element symbol of an atom type.
        ''')

    x_charmm_atom_type_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        van der Waals radius of an atom type.
        ''')

    number_of_atoms_per_type = Quantity(
        type=int,
        shape=[],
        description='''
        Number of atoms involved in this type.
        ''')


class Interaction(simulation.method.Interaction):

    m_def = Section(validate=False, extends_base_section=True)

    x_charmm_interaction_atom_to_atom_type_ref = Quantity(
        type=simulation.method.AtomParameters,
        shape=['number_of_atoms_per_interaction'],
        description='''
        Reference to the atom type of each interaction atoms.
        ''')

    x_charmm_number_of_defined_pair_interactions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of defined pair interactions (L-J pairs).
        ''')

    x_charmm_pair_interaction_atom_type_ref = Quantity(
        type=simulation.method.AtomParameters,
        shape=['x_charmm_number_of_defined_pair_interactions', 'number_of_atoms_per_interaction'],
        description='''
        Reference to the atom type for pair interactions.
        ''')

    x_charmm_pair_interaction_parameters = Quantity(
        type=np.dtype(np.float64),
        shape=['x_charmm_number_of_defined_pair_interactions', 2],
        description='''
        Pair interactions parameters.
        ''')

    x_charmm_molecule_interaction_atom_to_atom_type_ref = Quantity(
        type=simulation.method.AtomParameters,
        shape=['number_of_atoms_per_interaction'],
        description='''
        Reference to the atom type of each molecule interaction atoms.
        ''')

    x_charmm_number_of_defined_molecule_pair_interactions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of defined pair interactions within a molecule (L-J pairs).
        ''')

    x_charmm_pair_molecule_interaction_parameters = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_defined_molecule_pair_interactions', 2],
        description='''
        Molecule pair interactions parameters.
        ''')

    x_charmm_pair_molecule_interaction_to_atom_type_ref = Quantity(
        type=simulation.method.AtomParameters,
        shape=['x_charmm_number_of_defined_pair_interactions', 'number_of_atoms_per_interaction'],
        description='''
        Reference to the atom type for pair interactions within a molecule.
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_charmm_program_version_date = Quantity(
        type=str,
        shape=[],
        description='''
        Program version date.
        ''')

    x_charmm_parallel_task_nr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Program task no.
        ''')

    x_charmm_build_osarch = Quantity(
        type=str,
        shape=[],
        description='''
        Program Build OS/ARCH
        ''')

    x_charmm_output_created_by_user = Quantity(
        type=str,
        shape=[],
        description='''
        Output file creator
        ''')

    x_charmm_most_severe_warning_level = Quantity(
        type=str,
        shape=[],
        description='''
        Highest charmm warning level in the run.
        ''')

    x_charmm_program_build_date = Quantity(
        type=str,
        shape=[],
        description='''
        Program Build date
        ''')

    x_charmm_program_citation = Quantity(
        type=str,
        shape=[],
        description='''
        Program citations
        ''')

    x_charmm_program_copyright = Quantity(
        type=str,
        shape=[],
        description='''
        Program copyright
        ''')

    x_charmm_number_of_tasks = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Number of tasks in parallel program (MPI).
        ''')

    x_charmm_program_module_version = Quantity(
        type=str,
        shape=[],
        description='''
        charmm program module version.
        ''')

    x_charmm_program_license = Quantity(
        type=str,
        shape=[],
        description='''
        charmm program license.
        ''')

    x_charmm_xlo_xhi = Quantity(
        type=str,
        shape=[],
        description='''
        test
        ''')

    x_charmm_data_file_store = Quantity(
        type=str,
        shape=[],
        description='''
        Filename of data file
        ''')

    x_charmm_program_working_path = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_program_execution_host = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_program_execution_path = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_program_module = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_program_execution_date = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_program_execution_time = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_mdin_header = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_mdin_wt = Quantity(
        type=str,
        shape=[],
        description='''
        tmp
        ''')

    x_charmm_section_control_parameters = SubSection(
        sub_section=SectionProxy('x_charmm_section_control_parameters'),
        repeats=True)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_charmm_section_single_configuration_calculation = SubSection(
        sub_section=SectionProxy('x_charmm_section_single_configuration_calculation'),
        repeats=True)
