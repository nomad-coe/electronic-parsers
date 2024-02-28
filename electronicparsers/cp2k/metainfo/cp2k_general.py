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
import numpy as np  # pylint: disable=unused-import
import typing  # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection,
    MCategory,
    Category,
    Package,
    Quantity,
    Section,
    SubSection,
    SectionProxy,
    Reference,
    JSON,
)

import simulationworkflowschema
import runschema.run  # pylint: disable=unused-import
import runschema.calculation  # pylint: disable=unused-import
import runschema.method  # pylint: disable=unused-import
import runschema.system  # pylint: disable=unused-import


m_package = Package()


class x_cp2k_section_restart_information(MSection):
    """
    Contains restart information for this calculation.
    """

    m_def = Section(validate=False)

    x_cp2k_restart_file_name = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the restart file.
        """,
    )

    x_cp2k_restarted_quantity_name = Quantity(
        type=str,
        shape=[],
        description="""
        Name of a restarted quantity.
        """,
    )


class x_cp2k_section_geometry_optimization_energy_reevaluation(MSection):
    """
    Information for the energy re-evaluation at the end of an optimization procedure.
    """

    m_def = Section(validate=False)


class x_cp2k_section_geometry_optimization_step(MSection):
    """
    Contains information about the geometry optimization process for every optimization
    step.
    """

    m_def = Section(validate=False)

    x_cp2k_optimization_energy_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Energy change for this optimization step.
        """,
    )

    x_cp2k_optimization_energy_decrease = Quantity(
        type=str,
        shape=[],
        description="""
        Whether there has been energy decrease. YES or NO.
        """,
    )

    x_cp2k_optimization_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Energy for this optimization step.
        """,
    )

    x_cp2k_optimization_gradient_convergence_limit = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Convergence criterium for the maximum force component of the current
        configuration.
        """,
    )

    x_cp2k_optimization_max_gradient_convergence = Quantity(
        type=str,
        shape=[],
        description="""
        Whether there is convergence in max gradient. YES or NO.
        """,
    )

    x_cp2k_optimization_max_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Max gradient for this optimization step.
        """,
    )

    x_cp2k_optimization_max_step_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Maximum step size for this optimization step.
        """,
    )

    x_cp2k_optimization_method = Quantity(
        type=str,
        shape=[],
        description="""
        Optimization method for this step
        """,
    )

    x_cp2k_optimization_rms_gradient_convergence = Quantity(
        type=str,
        shape=[],
        description="""
        Whether there is convergence in rms gradient. YES or NO.
        """,
    )

    x_cp2k_optimization_rms_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        RMS gradient for this optimization step.
        """,
    )

    x_cp2k_optimization_rms_step_size_convergence = Quantity(
        type=str,
        shape=[],
        description="""
        Whether there is convergence in rms step size. YES or NO.
        """,
    )

    x_cp2k_optimization_rms_step_size = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        RMS step size for this optimization step.
        """,
    )

    x_cp2k_optimization_step_size_convergence_limit = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Convergence criterium for the maximum geometry change between the current and the
        last optimizer iteration.
        """,
    )

    x_cp2k_optimization_step_size_convergence = Quantity(
        type=str,
        shape=[],
        description="""
        Whether there is convergence in step size. YES or NO.
        """,
    )

    x_cp2k_optimization_used_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Time used for this optimization step.
        """,
    )


class x_cp2k_section_geometry_optimization(MSection):
    """
    CP2K geometry optimization information.
    """

    m_def = Section(validate=False)

    x_cp2k_section_geometry_optimization_energy_reevaluation = SubSection(
        sub_section=SectionProxy(
            'x_cp2k_section_geometry_optimization_energy_reevaluation'
        ),
        repeats=True,
    )

    x_cp2k_section_geometry_optimization_step = SubSection(
        sub_section=SectionProxy('x_cp2k_section_geometry_optimization_step'),
        repeats=True,
    )


class x_cp2k_section_maximum_angular_momentum(MSection):
    """
    Contains the maximum angular momentum values used in the calculation.
    """

    m_def = Section(validate=False)

    x_cp2k_local_part_of_gth_pseudopotential = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Maximum angular momentum of the local part of the GTH pseudopotential.
        """,
    )

    x_cp2k_non_local_part_of_gth_pseudopotential = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Maximum angular momentum of the non-local part of the GTH pseudopotential.
        """,
    )

    x_cp2k_orbital_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Maximum angular momentum of orbital basis functions.
        """,
    )


class x_cp2k_section_startinformation(MSection):
    """
    Contains information about the starting conditions for this run.
    """

    m_def = Section(validate=False)

    x_cp2k_start_time = Quantity(
        type=str,
        shape=[],
        description="""
        The starting time for this run.
        """,
    )

    x_cp2k_start_host = Quantity(
        type=str,
        shape=[],
        description="""
        The name of the host machine this calculation started on.
        """,
    )

    x_cp2k_start_user = Quantity(
        type=str,
        shape=[],
        description="""
        The name of the user at the start of the calculation.
        """,
    )

    x_cp2k_start_id = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The process id at the start of this run.
        """,
    )

    x_cp2k_start_path = Quantity(
        type=str,
        shape=[],
        description="""
        The path where this calculation started.
        """,
    )


class x_cp2k_section_end_information(MSection):
    """
    Contains information about the ending conditions for this run.
    """

    m_def = Section(validate=False)

    x_cp2k_end_time = Quantity(
        type=str,
        shape=[],
        description="""
        The ending time for this run.
        """,
    )

    x_cp2k_end_host = Quantity(
        type=str,
        shape=[],
        description="""
        The name of the host machine this calculation ended on.
        """,
    )

    x_cp2k_end_user = Quantity(
        type=str,
        shape=[],
        description="""
        The name of the user at the end of the calculation.
        """,
    )

    x_cp2k_end_id = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The process id at the end of this run.
        """,
    )

    x_cp2k_end_path = Quantity(
        type=str,
        shape=[],
        description="""
        The path where this calculation ended.
        """,
    )


class x_cp2k_section_total_numbers(MSection):
    """
    The total number of different entities in the calculation.
    """

    m_def = Section(validate=False)

    x_cp2k_atomic_kinds = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The number of atomic kinds in the calculation.
        """,
    )

    x_cp2k_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The number of atoms in the calculation.
        """,
    )

    x_cp2k_cartesian_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The number of Cartesian basis functions.
        """,
    )

    x_cp2k_primitive_cartesian_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The number of primitive Cartesian functions.
        """,
    )

    x_cp2k_shell_sets = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The number of shell sets in the calculation.
        """,
    )

    x_cp2k_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The number of shells.
        """,
    )

    x_cp2k_spherical_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The number of Spherical basis functions.
        """,
    )


class x_cp2k_section_md_settings(MSection):
    """
    Settings for CP2K Molecular Dynamics.
    """

    m_def = Section(validate=False)

    x_cp2k_md_target_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description="""
        Thermostat target temperature.
        """,
    )

    x_cp2k_md_target_temperature_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description="""
        Target temperature tolerance.
        """,
    )

    x_cp2k_md_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The print frequency of molecular dynamics information in the CP2K output file.
        """,
    )

    x_cp2k_md_coordinates_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Print frequency for the coordinate file.
        """,
    )

    x_cp2k_md_coordinates_filename = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the coordinate file.
        """,
    )

    x_cp2k_md_velocities_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Print frequency for the velocities file.
        """,
    )

    x_cp2k_md_velocities_filename = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the velocities file.
        """,
    )

    x_cp2k_md_energies_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Print frequency for the energies file.
        """,
    )

    x_cp2k_md_energies_filename = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the energies file.
        """,
    )

    x_cp2k_md_dump_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Print frequency for the dump file.
        """,
    )

    x_cp2k_md_dump_filename = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the dump file.
        """,
    )

    x_cp2k_md_target_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Target pressure for the barostat.
        """,
    )

    x_cp2k_md_barostat_time_constant = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Barostat time constant.
        """,
    )

    x_cp2k_md_simulation_cell_print_frequency = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Simulation cell print frequency.
        """,
    )

    x_cp2k_md_simulation_cell_filename = Quantity(
        type=str,
        shape=[],
        description="""
        Simulation cell filename.
        """,
    )

    x_cp2k_md_number_of_time_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Number of requested time steps in molecular dynamics.
        """,
    )


class x_cp2k_section_quickstep_settings(MSection):
    """
    Quickstep settings.
    """

    m_def = Section(validate=False)

    x_cp2k_planewave_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        The plane-wave cutoff for the auxiliary basis.
        """,
    )

    x_cp2k_spin_restriction = Quantity(
        type=str,
        shape=[],
        description="""
        Indicates the restriction applied for the spin (e.g. RKS).
        """,
    )

    x_cp2k_quickstep_method = Quantity(
        type=str,
        shape=[],
        description="""
        The method used for the Quickstep calculations (GPW, GAPW).
        """,
    )

    x_cp2k_section_maximum_angular_momentum = SubSection(
        sub_section=SectionProxy('x_cp2k_section_maximum_angular_momentum'),
        repeats=True,
    )

    x_cp2k_section_total_numbers = SubSection(
        sub_section=SectionProxy('x_cp2k_section_total_numbers'), repeats=True
    )

    x_cp2k_section_atomic_kinds = SubSection(
        sub_section=SectionProxy('x_cp2k_section_atomic_kinds'), repeats=True
    )


class x_cp2k_section_atomic_kinds(MSection):
    """
    Information about all the atomic kinds in this Quickstep calculation.
    """

    m_def = Section(validate=False)

    x_cp2k_section_atomic_kind = SubSection(
        sub_section=SectionProxy('x_cp2k_section_atomic_kind'), repeats=True
    )


class x_cp2k_section_vdw_settings(MSection):
    """
    Van der Waals settings.
    """

    m_def = Section(validate=False)

    x_cp2k_vdw_type = Quantity(
        type=str,
        shape=[],
        description="""
        Type of the van der Waals method.
        """,
    )

    x_cp2k_vdw_name = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the van der Waals method.
        """,
    )

    x_cp2k_vdw_bj_damping_name = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the BJ damping method.
        """,
    )

    x_cp2k_vdw_cutoff_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Cutoff radius of the van der Waals method.
        """,
    )

    x_cp2k_section_vdw_d2_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_d2_settings'), repeats=True
    )

    x_cp2k_section_vdw_d3_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_d3_settings'), repeats=True
    )


class x_cp2k_section_vdw_d2_settings(MSection):
    """
    D2 settings.
    """

    m_def = Section(validate=False)

    x_cp2k_vdw_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Scaling factor.
        """,
    )

    x_cp2k_vdw_damping_factor = Quantity(
        type=str,
        shape=[],
        description="""
        Exponential damping prefactor for the van der Waals method.
        """,
    )

    x_cp2k_section_vdw_element_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_element_settings'), repeats=True
    )


class x_cp2k_section_vdw_element_settings(MSection):
    """
    Contains element-specific Van der Waals settings.
    """

    m_def = Section(validate=False)

    x_cp2k_vdw_parameter_element_name = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the element.
        """,
    )

    x_cp2k_vdw_parameter_c6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        C6 parameter.
        """,
    )

    x_cp2k_vdw_parameter_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Radius parameter.
        """,
    )


class x_cp2k_section_vdw_d3_settings(MSection):
    """
    D3 settings.
    """

    m_def = Section(validate=False)

    x_cp2k_vdw_s6_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        S6 scaling factor.
        """,
    )

    x_cp2k_vdw_sr6_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        SR6 scaling factor.
        """,
    )

    x_cp2k_vdw_s8_scaling_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        S8 scaling factor.
        """,
    )

    x_cp2k_vdw_cn_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Cutoff for CN calculation.
        """,
    )


class x_cp2k_section_atomic_kind(MSection):
    """
    Information one atomic kind.
    """

    m_def = Section(validate=False)

    x_cp2k_kind_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        The atomic kind number. For each element there may be multiple kinds specified.
        This number differentiates them. Not the atomic number.
        """,
    )

    x_cp2k_kind_label = Quantity(
        type=str,
        shape=[],
        description="""
        The label for this atomic kind.
        """,
    )

    x_cp2k_kind_number_of_atoms = Quantity(
        type=str,
        shape=[],
        description="""
        The number of atoms with this kind.
        """,
    )

    x_cp2k_section_kind_basis_set = SubSection(
        sub_section=SectionProxy('x_cp2k_section_kind_basis_set'), repeats=True
    )


class x_cp2k_section_kind_basis_set(MSection):
    """
    Description of the basis set used for this kind.
    """

    m_def = Section(validate=False)

    x_cp2k_kind_basis_set_name = Quantity(
        type=str,
        shape=[],
        description="""
        The name of the orbital basis set used for this kind.
        """,
    )

    x_cp2k_basis_set_number_of_orbital_shell_sets = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Number of orbital shell sets.
        """,
    )

    x_cp2k_basis_set_number_of_orbital_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Number of orbital shells.
        """,
    )

    x_cp2k_basis_set_number_of_primitive_cartesian_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Number of primitive Cartesian functions.
        """,
    )

    x_cp2k_basis_set_number_of_cartesian_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Number of Cartesian basis functions.
        """,
    )

    x_cp2k_basis_set_number_of_spherical_basis_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Number of spherical basis functions.
        """,
    )

    x_cp2k_basis_set_norm_type = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Norm type.
        """,
    )


class Run(runschema.run.Run):
    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_restart_information = SubSection(
        sub_section=SectionProxy('x_cp2k_section_restart_information'), repeats=True
    )

    x_cp2k_program_information = Quantity(
        type=JSON,
        shape=[],
        description="""
        A JSON quantity containing all code-specific code information.
        """,
    )

    x_cp2k_dbcsr = Quantity(
        type=JSON,
        shape=[],
        description="""
        A JSON quantity containing all code-specific DBCSR (a sparse matrix library) information.
        """,
    )

    x_cp2k_global_settings = Quantity(
        type=JSON,
        shape=[],
        description="""
        A JSON quantity containing all code-specific global information.
        """,
    )

    x_cp2k_section_startinformation = SubSection(
        sub_section=SectionProxy('x_cp2k_section_startinformation'), repeats=True
    )

    x_cp2k_section_end_information = SubSection(
        sub_section=SectionProxy('x_cp2k_section_end_information'), repeats=True
    )


class GeometryOptimization(simulationworkflowschema.GeometryOptimization):
    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_geometry_optimization = SubSection(
        sub_section=SectionProxy('x_cp2k_section_geometry_optimization'), repeats=True
    )


class GeometryOptimizationMethod(simulationworkflowschema.GeometryOptimizationMethod):
    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_geometry_optimization = SubSection(
        sub_section=SectionProxy('x_cp2k_section_geometry_optimization'), repeats=True
    )


class MolecularDynamicsMethod(simulationworkflowschema.MolecularDynamicsMethod):
    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_md_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_md_settings'), repeats=True
    )


class Method(runschema.method.Method):
    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_section_quickstep_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_quickstep_settings'), repeats=True
    )

    x_cp2k_quickstep_settings = Quantity(
        type=JSON,
        shape=[],
        description="""
        A JSON quantity containing all code-specific global information.
        """,
    )

    x_cp2k_section_vdw_settings = SubSection(
        sub_section=SectionProxy('x_cp2k_section_vdw_settings'), repeats=True
    )


class x_cp2k_pdos_histogram(MSection):
    """
    Section with projected DOS histogram data.
    """

    m_def = Section(validate=False)

    x_cp2k_pdos_histogram_energies = Quantity(
        type=np.float64,
        shape=['n_energies'],
        unit='joule',
        description="""
        Values of the histogram energies.
        """,
    )

    x_cp2k_pdos_histogram_values = Quantity(
        type=np.float64,
        shape=['n_orbitals', 'n_energies'],
        description="""
        Values of the projected orbital / atomic / species histogram. This is then convoluted
        with a Gaussian distribution function and stored in the corresponding projected DOS value.
        """,
    )

    x_cp2k_pdos_histogram_atom_label = Quantity(
        type=str,
        description="""
        Atom label for the projected DOS histogram.
        """,
    )

    x_cp2k_pdos_histogram_atom_index = Quantity(
        type=np.int32,
        description="""
        Atom index for the projected DOS histogram.
        """,
    )

    x_cp2k_pdos_histogram_orbital = Quantity(
        type=str,
        shape=['n_orbitals'],
        description="""
        Orbital label for the projected DOS histogram.
        """,
    )

    x_cp2k_gaussian_width = Quantity(
        type=np.float64,
        unit='joule',
        description="""
        Width of the Gaussian distribution function.
        """,
    )

    x_cp2k_gaussian_delta_energy = Quantity(
        type=np.float64,
        unit='joule',
        description="""
        New energies mesh separation.
        """,
    )


class Calculation(runschema.calculation.Calculation):
    m_def = Section(validate=False, extends_base_section=True)

    x_cp2k_pdos = SubSection(sub_section=x_cp2k_pdos_histogram.m_def, repeats=True)
