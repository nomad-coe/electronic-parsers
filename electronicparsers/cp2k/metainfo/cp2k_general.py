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

from nomad.datamodel.metainfo import simulation, workflow


m_package = Package()


class x_cp2k_section_restart_information(MSection):
    '''
    Contains restart information for this calculation.
    '''

    m_def = Section(validate=False)

    x_cp2k_restart_file_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the restart file.
        ''')

    x_cp2k_restarted_quantity_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of a restarted quantity.
        ''')


class x_cp2k_section_dbcsr(MSection):
    '''
    The DBCSR (Distributed Block Compressed Sparse Row) information.
    '''

    m_def = Section(validate=False)

    x_cp2k_dbcsr_multiplication_driver = Quantity(
        type=str,
        shape=[],
        description='''
        DBCSR Multiplication driver
        ''')

    x_cp2k_dbcsr_multrec_recursion_limit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DBCSR Multrec recursion limit
        ''')

    x_cp2k_dbcsr_multiplication_stack_size = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DBCSR Multiplication stack size.
        ''')

    x_cp2k_dbcsr_multiplication_size_stacks = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DBCSR Multiplication size of stacks.
        ''')

    x_cp2k_dbcsr_use_subcommunicators = Quantity(
        type=str,
        shape=[],
        description='''
        Boolean indicating if subcommunicators are used.
        ''')

    x_cp2k_dbcsr_use_mpi_combined_types = Quantity(
        type=str,
        shape=[],
        description='''
        Boolean indicating if MPI combined types are used.
        ''')

    x_cp2k_dbcsr_use_mpi_memory_allocation = Quantity(
        type=str,
        shape=[],
        description='''
        Boolean indicating if MPI memory allocation is used.
        ''')

    x_cp2k_dbcsr_use_communication_thread = Quantity(
        type=str,
        shape=[],
        description='''
        Boolean indicating if communication thread is used.
        ''')

    x_cp2k_dbcsr_communication_thread_load = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Load of the communication thread.
        ''')


class x_cp2k_section_global_settings(MSection):
    '''
    Global settings for this calculation.
    '''

    m_def = Section(validate=False)

    x_cp2k_basis_set_filename = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the basis set file.
        ''')

    x_cp2k_coordinate_filename = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the coordinate file.
        ''')

    x_cp2k_geminal_filename = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the geminal file.
        ''')

    x_cp2k_mm_potential_filename = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the MM potential file.
        ''')

    x_cp2k_potential_filename = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the potential file.
        ''')

    x_cp2k_method_name = Quantity(
        type=str,
        shape=[],
        description='''
        The method name for this run.
        ''')

    x_cp2k_preferred_fft_library = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the preferred FFT library.
        ''')

    x_cp2k_preferred_diagonalization_library = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the preferred diagonalization library.
        ''')

    x_cp2k_run_type = Quantity(
        type=str,
        shape=[],
        description='''
        The run type for this calculation.
        ''')


class x_cp2k_section_geometry_optimization_energy_reevaluation(MSection):
    '''
    Information for the energy re-evaluation at the end of an optimization procedure.
    '''

    m_def = Section(validate=False)


class x_cp2k_section_geometry_optimization_step(MSection):
    '''
    Contains information about the geometry optimization process for every optimization
    step.
    '''

    m_def = Section(validate=False)

    x_cp2k_optimization_energy_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy change for this optimization step.
        ''')

    x_cp2k_optimization_energy_decrease = Quantity(
        type=str,
        shape=[],
        description='''
        Whether there has been energy decrease. YES or NO.
        ''')

    x_cp2k_optimization_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Energy for this optimization step.
        ''')

    x_cp2k_optimization_gradient_convergence_limit = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence criterium for the maximum force component of the current
        configuration.
        ''')

    x_cp2k_optimization_max_gradient_convergence = Quantity(
        type=str,
        shape=[],
        description='''
        Whether there is convergence in max gradient. YES or NO.
        ''')

    x_cp2k_optimization_max_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Max gradient for this optimization step.
        ''')

    x_cp2k_optimization_max_step_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Maximum step size for this optimization step.
        ''')

    x_cp2k_optimization_method = Quantity(
        type=str,
        shape=[],
        description='''
        Optimization method for this step
        ''')

    x_cp2k_optimization_rms_gradient_convergence = Quantity(
        type=str,
        shape=[],
        description='''
        Whether there is convergence in rms gradient. YES or NO.
        ''')

    x_cp2k_optimization_rms_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        RMS gradient for this optimization step.
        ''')

    x_cp2k_optimization_rms_step_size_convergence = Quantity(
        type=str,
        shape=[],
        description='''
        Whether there is convergence in rms step size. YES or NO.
        ''')

    x_cp2k_optimization_rms_step_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        RMS step size for this optimization step.
        ''')

    x_cp2k_optimization_step_size_convergence_limit = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence criterium for the maximum geometry change between the current and the
        last optimizer iteration.
        ''')

    x_cp2k_optimization_step_size_convergence = Quantity(
        type=str,
        shape=[],
        description='''
        Whether there is convergence in step size. YES or NO.
        ''')

    x_cp2k_optimization_used_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Time used for this optimization step.
        ''')


class x_cp2k_section_geometry_optimization(MSection):
    '''
    CP2K geometry optimization information.
    '''

    m_def = Section(validate=False)

    x_cp2k_section_geometry_optimization_energy_reevaluation = SubSection(
        sub_section=SectionProxy('x_cp2k_section_geometry_optimization_energy_reevaluation'),
        repeats=True)

    x_cp2k_section_geometry_optimization_step = SubSection(
        sub_section=SectionProxy('x_cp2k_section_geometry_optimization_step'),
        repeats=True)


class x_cp2k_section_maximum_angular_momentum(MSection):
    '''
    Contains the maximum angular momentum values used in the calculation.
    '''

    m_def = Section(validate=False)

    x_cp2k_local_part_of_gth_pseudopotential = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum angular momentum of the local part of the GTH pseudopotential.
        ''')

    x_cp2k_non_local_part_of_gth_pseudopotential = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum angular momentum of the non-local part of the GTH pseudopotential.
        ''')

    x_cp2k_orbital_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum angular momentum of orbital basis functions.
        ''')


class x_cp2k_section_program_information(MSection):
    '''
    Contains information about the software version used for this run.
    '''

    m_def = Section(validate=False)

    x_cp2k_input_filename = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the CP2K input file that produced this calculation.
        ''')

    x_cp2k_program_compilation_datetime = Quantity(
        type=str,
        shape=[],
        description='''
        The time when this program was compiled.
        ''')

    x_cp2k_svn_revision = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The SVN revision number.
        ''')


class x_cp2k_section_quickstep_calculation(MSection):
    '''
    Section for a CP2K QuickStep calculation.
    '''

    m_def = Section(validate=False)

    x_cp2k_atom_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        unit='newton',
        description='''
        Forces acting on the atoms in this Quickstep calculation.
        ''')

    x_cp2k_electronic_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Self-consistent electronic kinetic energy calculated with Quickstep
        ''')

    x_cp2k_energy_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Value of the total energy (nuclei + electrons) calculated with Quickstep.
        ''')

    x_cp2k_quickstep_converged = Quantity(
        type=bool,
        shape=[],
        description='''
        Boolean indicating whether the quickstep SCF cycle converged or not.
        ''')

    x_cp2k_section_scf_iteration = SubSection(
        sub_section=SectionProxy('x_cp2k_section_scf_iteration'),
        repeats=True)

    x_cp2k_section_stress_tensor = SubSection(
        sub_section=SectionProxy('x_cp2k_section_stress_tensor'),
        repeats=True)


class x_cp2k_section_scf_iteration(MSection):
    '''
    Section for a CP2K QuickStep SCF iteration.
    '''

    m_def = Section(validate=False)

    x_cp2k_energy_change_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        At each self-consistent field (SCF) iteration, change of total energy with respect
        to the previous SCF iteration.
        ''')

    x_cp2k_energy_total_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Total electronic energy calculated with XC_method during the self-consistent field
        (SCF) iterations.
        ''')

    x_cp2k_energy_XC_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Exchange-correlation (XC) energy during the self-consistent field (SCF) iteration.
        ''')


class x_cp2k_section_startinformation(MSection):
    '''
    Contains information about the starting conditions for this run.
    '''

    m_def = Section(validate=False)

    x_cp2k_start_time = Quantity(
        type=str,
        shape=[],
        description='''
        The starting time for this run.
        ''')

    x_cp2k_start_host = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the host machine this calculation started on.
        ''')

    x_cp2k_start_user = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the user at the start of the calculation.
        ''')

    x_cp2k_start_id = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The process id at the start of this run.
        ''')

    x_cp2k_start_path = Quantity(
        type=str,
        shape=[],
        description='''
        The path where this calculation started.
        ''')


class x_cp2k_section_end_information(MSection):
    '''
    Contains information about the ending conditions for this run.
    '''

    m_def = Section(validate=False)

    x_cp2k_end_time = Quantity(
        type=str,
        shape=[],
        description='''
        The ending time for this run.
        ''')

    x_cp2k_end_host = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the host machine this calculation ended on.
        ''')

    x_cp2k_end_user = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the user at the end of the calculation.
        ''')

    x_cp2k_end_id = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The process id at the end of this run.
        ''')

    x_cp2k_end_path = Quantity(
        type=str,
        shape=[],
        description='''
        The path where this calculation ended.
        ''')


class x_cp2k_section_stress_tensor(MSection):
    '''
    Section for stress tensor information.
    '''

    m_def = Section(validate=False)

    x_cp2k_stress_tensor_determinant = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The determinant of the stress tensor.
        ''')

    x_cp2k_stress_tensor_eigenvalues = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        The eigenvalues of the stress tensor.
        ''')

    x_cp2k_stress_tensor_eigenvectors = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        The eigenvectors of the stress tensor.
        ''')

    x_cp2k_stress_tensor_one_third_of_trace = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        1/3 of the trace of the stress tensor.
        ''')

    x_cp2k_stress_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        unit='pascal',
        description='''
        A final value of the stress tensor in a Quickstep calculation
        ''')


class x_cp2k_section_total_numbers(MSection):
    '''
    The total number of different entities in the calculation.
    '''

    m_def = Section(validate=False)

    x_cp2k_atomic_kinds = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of atomic kinds in the calculation.
        ''')

    x_cp2k_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of atoms in the calculation.
        ''')

    x_cp2k_cartesian_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of Cartesian basis functions.
        ''')

    x_cp2k_primitive_cartesian_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of primitive Cartesian functions.
        ''')

    x_cp2k_shell_sets = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of shell sets in the calculation.
        ''')

    x_cp2k_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of shells.
        ''')

    x_cp2k_spherical_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of Spherical basis functions.
        ''')


class x_cp2k_section_md_settings(MSection):
    '''
    Settings for CP2K Molecular Dynamics.
    '''

    m_def = Section(validate=False)

    x_cp2k_md_target_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        Thermostat target temperature.
        ''')

    x_cp2k_md_target_temperature_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        Target temperature tolerance.
        ''')

    x_cp2k_md_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The print frequency of molecular dynamics information in the CP2K output file.
        ''')

    x_cp2k_md_coordinates_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Print frequency for the coordinate file.
        ''')

    x_cp2k_md_coordinates_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the coordinate file.
        ''')

    x_cp2k_md_velocities_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Print frequency for the velocities file.
        ''')

    x_cp2k_md_velocities_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the velocities file.
        ''')

    x_cp2k_md_energies_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Print frequency for the energies file.
        ''')

    x_cp2k_md_energies_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the energies file.
        ''')

    x_cp2k_md_dump_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Print frequency for the dump file.
        ''')

    x_cp2k_md_dump_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the dump file.
        ''')

    x_cp2k_md_target_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Target pressure for the barostat.
        ''')

    x_cp2k_md_barostat_time_constant = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Barostat time constant.
        ''')

    x_cp2k_md_simulation_cell_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Simulation cell print frequency.
        ''')

    x_cp2k_md_simulation_cell_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Simulation cell filename.
        ''')

    x_cp2k_md_number_of_time_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of requested time steps in molecular dynamics.
        ''')


class x_cp2k_section_quickstep_settings(MSection):
    '''
    Quickstep settings.
    '''

    m_def = Section(validate=False)

    x_cp2k_planewave_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The plane-wave cutoff for the auxiliary basis.
        ''')

    x_cp2k_spin_restriction = Quantity(
        type=str,
        shape=[],
        description='''
        Indicates the restriction applied for the spin (e.g. RKS).
        ''')

    x_cp2k_quickstep_method = Quantity(
        type=str,
        shape=[],
        description='''
        The method used for the Quickstep calculations (GPW, GAPW).
        ''')

    x_cp2k_section_maximum_angular_momentum = SubSection(
        sub_section=SectionProxy('x_cp2k_section_maximum_angular_momentum'),
        repeats=True)

    x_cp2k_section_total_numbers = SubSection(
        sub_section=SectionProxy('x_cp2k_section_total_numbers'),
        repeats=True)

    x_cp2k_section_atomic_kinds = SubSection(
        sub_section=SectionProxy('x_cp2k_section_atomic_kinds'),
        repeats=True)


class x_cp2k_section_atomic_kinds(MSection):
    '''
    Information about all the atomic kinds in this Quickstep calculation.
    '''

    m_def = Section(validate=False)

    x_cp2k_section_atomic_kind = SubSection(
        sub_section=SectionProxy('x_cp2k_section_atomic_kind'),
        repeats=True)


class x_cp2k_section_vdw_settings(MSection):
    '''
    Van der Waals settings.
    '''

    m_def = Section(validate=False)

    x_cp2k_vdw_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of the van der Waals method.
        ''')

    x_cp2k_vdw_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the van der Waals method.
        ''')

    x_cp2k_vdw_bj_damping_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the BJ damping method.
        ''')

    x_cp2k_vdw_cutoff_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Cutoff radius of the van der Waals method.
        ''')

    x_cp2k_section_vdw_d2_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_d2_settings'),
        repeats=True)

    x_cp2k_section_vdw_d3_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_d3_settings'),
        repeats=True)


class x_cp2k_section_vdw_d2_settings(MSection):
    '''
    D2 settings.
    '''

    m_def = Section(validate=False)

    x_cp2k_vdw_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Scaling factor.
        ''')

    x_cp2k_vdw_damping_factor = Quantity(
        type=str,
        shape=[],
        description='''
        Exponential damping prefactor for the van der Waals method.
        ''')

    x_cp2k_section_vdw_element_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_element_settings'),
        repeats=True)


class x_cp2k_section_vdw_element_settings(MSection):
    '''
    Contains element-specific Van der Waals settings.
    '''

    m_def = Section(validate=False)

    x_cp2k_vdw_parameter_element_name = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the element.
        ''')

    x_cp2k_vdw_parameter_c6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        C6 parameter.
        ''')

    x_cp2k_vdw_parameter_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Radius parameter.
        ''')


class x_cp2k_section_vdw_d3_settings(MSection):
    '''
    D3 settings.
    '''

    m_def = Section(validate=False)

    x_cp2k_vdw_s6_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        S6 scaling factor.
        ''')

    x_cp2k_vdw_sr6_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SR6 scaling factor.
        ''')

    x_cp2k_vdw_s8_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        S8 scaling factor.
        ''')

    x_cp2k_vdw_cn_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Cutoff for CN calculation.
        ''')


class x_cp2k_section_atomic_kind(MSection):
    '''
    Information one atomic kind.
    '''

    m_def = Section(validate=False)

    x_cp2k_kind_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The atomic kind number. For each element there may be multiple kinds specified.
        This number differentiates them. Not the atomic number.
        ''')

    x_cp2k_kind_label = Quantity(
        type=str,
        shape=[],
        description='''
        The label for this atomic kind.
        ''')

    x_cp2k_kind_number_of_atoms = Quantity(
        type=str,
        shape=[],
        description='''
        The number of atoms with this kind.
        ''')

    x_cp2k_section_kind_basis_set = SubSection(
        sub_section=SectionProxy('x_cp2k_section_kind_basis_set'),
        repeats=True)


class x_cp2k_section_kind_basis_set(MSection):
    '''
    Description of the basis set used for this kind.
    '''

    m_def = Section(validate=False)

    x_cp2k_kind_basis_set_name = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the orbital basis set used for this kind.
        ''')

    x_cp2k_basis_set_number_of_orbital_shell_sets = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of orbital shell sets.
        ''')

    x_cp2k_basis_set_number_of_orbital_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of orbital shells.
        ''')

    x_cp2k_basis_set_number_of_primitive_cartesian_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of primitive Cartesian functions.
        ''')

    x_cp2k_basis_set_number_of_cartesian_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of Cartesian basis functions.
        ''')

    x_cp2k_basis_set_number_of_spherical_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of spherical basis functions.
        ''')

    x_cp2k_basis_set_norm_type = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Norm type.
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_restart_information = SubSection(
        sub_section=SectionProxy('x_cp2k_section_restart_information'),
        repeats=True)

    x_cp2k_section_dbcsr = SubSection(
        sub_section=SectionProxy('x_cp2k_section_dbcsr'),
        repeats=True)

    x_cp2k_section_global_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_global_settings'),
        repeats=True)

    x_cp2k_section_program_information = SubSection(
        sub_section=SectionProxy('x_cp2k_section_program_information'),
        repeats=True)

    x_cp2k_section_quickstep_calculation = SubSection(
        sub_section=SectionProxy('x_cp2k_section_quickstep_calculation'),
        repeats=True)

    x_cp2k_section_startinformation = SubSection(
        sub_section=SectionProxy('x_cp2k_section_startinformation'),
        repeats=True)

    x_cp2k_section_end_information = SubSection(
        sub_section=SectionProxy('x_cp2k_section_end_information'),
        repeats=True)


class GeometryOptimization(workflow.GeometryOptimization):

    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_geometry_optimization = SubSection(
        sub_section=SectionProxy('x_cp2k_section_geometry_optimization'),
        repeats=True)


class Workflow(workflow.Workflow):

    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_md_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_md_settings'),
        repeats=True)

    x_cp2k_section_geometry_optimization = SubSection(
        sub_section=SectionProxy('x_cp2k_section_geometry_optimization'),
        repeats=True)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_quickstep_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_quickstep_settings'),
        repeats=True)

    x_cp2k_section_vdw_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_settings'),
        repeats=True)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)
