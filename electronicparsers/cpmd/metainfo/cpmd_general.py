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


class x_cpmd_section_start_information(MSection):
    '''
    Contains information about the starting conditions for this run
    '''

    m_def = Section(validate=False)

    x_cpmd_start_datetime = Quantity(
        type=str,
        shape=[],
        description='''
        CPMD run start time and date
        ''')

    x_cpmd_input_filename = Quantity(
        type=str,
        shape=[],
        description='''
        CPMD input file name.
        ''')

    x_cpmd_compilation_date = Quantity(
        type=str,
        shape=[],
        description='''
        CPMD compilation date.
        ''')

    x_cpmd_process_id = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The process id for this calculation.
        ''')

    x_cpmd_run_user_name = Quantity(
        type=str,
        shape=[],
        description='''
        The user who launched this calculation.
        ''')

    x_cpmd_run_host_name = Quantity(
        type=str,
        shape=[],
        description='''
        The host on which this calculation was made on.
        ''')


class x_cpmd_section_run_type_information(MSection):
    '''
    Contains information about the run type.
    '''

    m_def = Section(validate=False)

    x_cpmd_time_step_ions = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The time step for ions.
        ''')

    x_cpmd_time_step_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The time step for electrons.
        ''')

    x_cpmd_geo_opt_method = Quantity(
        type=str,
        shape=[],
        description='''
        The geometry optimization method.
        ''')

    x_cpmd_max_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The maximum number of steps requested. In MD, this is the number of MD steps, in
        single point calculations this is the number of scf cycles, in geometry
        optimization this is the number of optimization steps.
        ''')

    x_cpmd_ion_temperature_control = Quantity(
        type=str,
        shape=[],
        description='''
        The temperature control method for ion dynamics.
        ''')


class x_cpmd_section_xc_information(MSection):
    '''
    Contains information about the exchange-correlation functional.
    '''

    m_def = Section(validate=False)


class x_cpmd_section_system_information(MSection):
    '''
    Contains information about the system.
    '''

    m_def = Section(validate=False)


class x_cpmd_section_pseudopotential_information(MSection):
    '''
    Contains information about the pseudopotentials.
    '''

    m_def = Section(validate=False)


class x_cpmd_section_atom_kinds(MSection):
    '''
    Contains information about the atomic kinds present in the calculation.
    '''

    m_def = Section(validate=False)

    x_cpmd_section_atom_kind = SubSection(
        sub_section=SectionProxy('x_cpmd_section_atom_kind'),
        repeats=True)


class x_cpmd_section_atom_kind(MSection):
    '''
    Contains information about one atomic kind.
    '''

    m_def = Section(validate=False)

    x_cpmd_atom_kind_label = Quantity(
        type=str,
        shape=[],
        description='''
        The label of the atomic kind.
        ''')

    x_cpmd_atom_kind_mass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mass of the atomic kind.
        ''')

    x_cpmd_atom_kind_raggio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The width of the ionic charge distribution (RAGGIO) of the atomic kind.
        ''')

    x_cpmd_atom_kind_nlcc = Quantity(
        type=str,
        shape=[],
        description='''
        The nonlinear core correction (NLCC) of the atomic kind.
        ''')

    x_cpmd_atom_kind_pseudopotential_l = Quantity(
        type=str,
        shape=[],
        description='''
        The angular part of the pseudopotential for the atomic kind.
        ''')

    x_cpmd_atom_kind_pseudopotential_type = Quantity(
        type=str,
        shape=[],
        description='''
        The type of the pseudopotential for the atomic kind.
        ''')


class x_cpmd_section_supercell(MSection):
    '''
    Contains information about the supercell.
    '''

    m_def = Section(validate=False)

    x_cpmd_cell_symmetry = Quantity(
        type=str,
        shape=[],
        description='''
        The symmetry of the cell.
        ''')

    x_cpmd_cell_lattice_constant = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The cell lattice constant.
        ''')

    x_cpmd_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The cell volume.
        ''')

    x_cpmd_cell_dimension = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        The cell dimension.
        ''')

    x_cpmd_lattice_vector_A1 = Quantity(
        type=str,
        shape=[],
        description='''
        Lattice vector A1
        ''')

    x_cpmd_lattice_vector_A2 = Quantity(
        type=str,
        shape=[],
        description='''
        Lattice vector A2
        ''')

    x_cpmd_lattice_vector_A3 = Quantity(
        type=str,
        shape=[],
        description='''
        Lattice vector A3
        ''')

    x_cpmd_reciprocal_lattice_vector_B1 = Quantity(
        type=str,
        shape=[],
        description='''
        Reciprocal lattice vector B1
        ''')

    x_cpmd_reciprocal_lattice_vector_B2 = Quantity(
        type=str,
        shape=[],
        description='''
        Reciprocal lattice vector B2
        ''')

    x_cpmd_reciprocal_lattice_vector_B3 = Quantity(
        type=str,
        shape=[],
        description='''
        Reciprocal lattice vector B3
        ''')

    x_cpmd_real_space_mesh = Quantity(
        type=str,
        shape=[],
        description='''
        Number of points in the real space mesh.
        ''')

    x_cpmd_wave_function_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Place wave cutoff energy for wave function.
        ''')

    x_cpmd_density_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Place wave cutoff energy for density.
        ''')

    x_cpmd_number_of_planewaves_density = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of plane waves for density cutoff.
        ''')

    x_cpmd_number_of_planewaves_wave_function = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of plane waves for wave_function cutoff.
        ''')


class x_cpmd_section_wave_function_initialization(MSection):
    '''
    Contains information about the wave function initialization
    '''

    m_def = Section(validate=False)


class x_cpmd_section_scf(MSection):
    '''
    Contains information about self-consistent field calculation
    '''

    m_def = Section(validate=False)

    x_cpmd_section_scf_iteration = SubSection(
        sub_section=SectionProxy('x_cpmd_section_scf_iteration'),
        repeats=True)


class x_cpmd_section_scf_iteration(MSection):
    '''
    Contains information about the self-consistent field iteration within a wavefunction
    optimization.
    '''

    m_def = Section(validate=False)

    x_cpmd_scf_nfi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The scf step number (NFI).
        ''')

    x_cpmd_scf_gemax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Largest off-diagonal component (GEMAX) during SCF step.
        ''')

    x_cpmd_scf_cnorm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Average of the off-diagonal components (CNORM) during SCF step.
        ''')

    x_cpmd_scf_etot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The total energy (ETOT) during SCF step.
        ''')

    x_cpmd_scf_detot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The difference in total energy to the previous SCF energy (DETOT).
        ''')

    x_cpmd_scf_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The CPU time used during SCF step (TCPU).
        ''')


class x_cpmd_section_final_results(MSection):
    '''
    The final results after a single point calculation.
    '''

    m_def = Section(validate=False)


class x_cpmd_section_geo_opt_initialization(MSection):
    '''
    Geometry optimization initialization information.
    '''

    m_def = Section(validate=False)

    x_cpmd_total_number_of_molecular_structures = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of molecular structures.
        ''')

    x_cpmd_initialized_positions = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        The initialized positions for geometry optimization. The ith row corresponds to
        the position for atom number i.
        ''')

    x_cpmd_initialized_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        The initialized forces for geometry optimization. The ith row corresponds to the
        force for atom number i.
        ''')

    x_cpmd_geo_opt_initialization_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Time for initialization.
        ''')


class x_cpmd_section_geo_opt_step(MSection):
    '''
    Contains information for a single geometry optimization step.
    '''

    m_def = Section(validate=False)

    x_cpmd_geo_opt_step_positions = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        The positions from a geometry optimization step. The ith row corresponds to the
        position for atom number i.
        ''')

    x_cpmd_geo_opt_step_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        The forces from a geometry optimization step. The ith row corresponds to the force
        for atom number i.
        ''')

    x_cpmd_geo_opt_step_total_number_of_scf_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of SCF steps at the end of this geometry optimization step.
        ''')

    x_cpmd_geo_opt_step_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Geometry optimization step number.
        ''')

    x_cpmd_geo_opt_step_gnmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The largest absolute component of the force on any atom (GNMAX).
        ''')

    x_cpmd_geo_opt_step_gnorm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Average force on the atoms (GNORM).
        ''')

    x_cpmd_geo_opt_step_cnstr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The largest absolute component of a constraint force on the atoms (CNSTR).
        ''')

    x_cpmd_geo_opt_step_etot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The total energy at the end of a geometry optimization step (ETOT).
        ''')

    x_cpmd_geo_opt_step_detot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The difference in total energy to the previous geometry optimization step (DETOT).
        ''')

    x_cpmd_geo_opt_step_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The CPU time used during geometry optimization step (TCPU).
        ''')

    x_cpmd_section_geo_opt_scf_iteration = SubSection(
        sub_section=SectionProxy('x_cpmd_section_geo_opt_scf_iteration'),
        repeats=True)


class x_cpmd_section_geo_opt_scf_iteration(MSection):
    '''
    Contains information about the self-consistent field iteration within a geometry
    optimization step.
    '''

    m_def = Section(validate=False)

    x_cpmd_geo_opt_scf_nfi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The scf step number (NFI) within geometry optimization step.
        ''')

    x_cpmd_geo_opt_scf_gemax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Largest off-diagonal component (GEMAX) during SCF step within geometry
        optimization step.
        ''')

    x_cpmd_geo_opt_scf_cnorm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Average of the off-diagonal components (CNORM) during SCF step within geometry
        optimization step.
        ''')

    x_cpmd_geo_opt_scf_etot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The total energy (ETOT) during SCF step within geometry optimization step.
        ''')

    x_cpmd_geo_opt_scf_detot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The difference in total energy to the previous SCF energy (DETOT) within geometry
        optimization step.
        ''')

    x_cpmd_geo_opt_scf_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The CPU time used during SCF step (TCPU) within geometry optimization step.
        ''')


class x_cpmd_section_md_initialization(MSection):
    '''
    Molecular dynamics initialization information.
    '''

    m_def = Section(validate=False)


class x_cpmd_section_md_averaged_quantities(MSection):
    '''
    Averaged quantities from a MD calculation.
    '''

    m_def = Section(validate=False)

    x_cpmd_electron_kinetic_energy_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean electron kinetic energy.
        ''')

    x_cpmd_electron_kinetic_energy_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of electron kinetic energy.
        ''')

    x_cpmd_ionic_temperature_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean ionic temperature.
        ''')

    x_cpmd_ionic_temperature_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of ionic temperature.
        ''')

    x_cpmd_density_functional_energy_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean density functional energy.
        ''')

    x_cpmd_density_functional_energy_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of density functional energy.
        ''')

    x_cpmd_classical_energy_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean classical energy.
        ''')

    x_cpmd_classical_energy_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of classical energy.
        ''')

    x_cpmd_conserved_energy_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean conserved energy.
        ''')

    x_cpmd_conserved_energy_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of conserved energy.
        ''')

    x_cpmd_nose_energy_electrons_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean Nosé energy for electrons.
        ''')

    x_cpmd_nose_energy_electrons_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of Nosé energy for elctrons.
        ''')

    x_cpmd_nose_energy_ions_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean Nosé energy for ions.
        ''')

    x_cpmd_nose_energy_ions_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of Nosé energy for ions.
        ''')

    x_cpmd_constraints_energy_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean constrains energy.
        ''')

    x_cpmd_constraints_energy_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of constraints energy.
        ''')

    x_cpmd_restraints_energy_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean restraints energy.
        ''')

    x_cpmd_restraints_energy_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of restraints energy.
        ''')

    x_cpmd_ion_displacement_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean ion displacement.
        ''')

    x_cpmd_ion_displacement_std = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The standard deviation of ion displacement.
        ''')

    x_cpmd_cpu_time_mean = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The mean cpu time.
        ''')


class x_cpmd_section_timing(MSection):
    '''
    Contains information about the timings.
    '''

    m_def = Section(validate=False)


class x_cpmd_section_end_information(MSection):
    '''
    Contains information printed at the end of a calculation.
    '''

    m_def = Section(validate=False)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_cpmd_section_start_information = SubSection(
        sub_section=SectionProxy('x_cpmd_section_start_information'),
        repeats=True)

    x_cpmd_section_run_type_information = SubSection(
        sub_section=SectionProxy('x_cpmd_section_run_type_information'),
        repeats=True)

    x_cpmd_section_system_information = SubSection(
        sub_section=SectionProxy('x_cpmd_section_system_information'),
        repeats=True)

    x_cpmd_section_wave_function_initialization = SubSection(
        sub_section=SectionProxy('x_cpmd_section_wave_function_initialization'),
        repeats=True)

    x_cpmd_section_md_initialization = SubSection(
        sub_section=SectionProxy('x_cpmd_section_md_initialization'),
        repeats=True)

    x_cpmd_section_md_averaged_quantities = SubSection(
        sub_section=SectionProxy('x_cpmd_section_md_averaged_quantities'),
        repeats=True)

    x_cpmd_section_timing = SubSection(
        sub_section=SectionProxy('x_cpmd_section_timing'),
        repeats=True)

    x_cpmd_section_end_information = SubSection(
        sub_section=SectionProxy('x_cpmd_section_end_information'),
        repeats=True)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_cpmd_simulation_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_cpmd_section_xc_information = SubSection(
        sub_section=SectionProxy('x_cpmd_section_xc_information'),
        repeats=True)

    x_cpmd_section_pseudopotential_information = SubSection(
        sub_section=SectionProxy('x_cpmd_section_pseudopotential_information'),
        repeats=True)

    x_cpmd_section_atom_kinds = SubSection(
        sub_section=SectionProxy('x_cpmd_section_atom_kinds'),
        repeats=True)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_cpmd_section_supercell = SubSection(
        sub_section=SectionProxy('x_cpmd_section_supercell'),
        repeats=True)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_cpmd_total_number_of_scf_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of SCF steps at the end of this geometry optimization step.
        ''')

    x_cpmd_gnmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The largest absolute component of the force on any atom (GNMAX).
        ''')

    x_cpmd_gnorm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Average force on the atoms (GNORM).
        ''')

    x_cpmd_cnstr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The largest absolute component of a constraint force on the atoms (CNSTR).
        ''')

    x_cpmd_restart_file = Quantity(
        type=str,
        shape=[],
        description='''
        The restart file.
        ''')

    x_cpmd_section_scf = SubSection(
        sub_section=SectionProxy('x_cpmd_section_scf'),
        repeats=True)

    x_cpmd_section_final_results = SubSection(
        sub_section=SectionProxy('x_cpmd_section_final_results'),
        repeats=True)


class GeometryOptimization(workflow.GeometryOptimization):

    m_def = Section(validate=False, extends_base_section=True)

    x_cpmd_section_geo_opt_initialization = SubSection(
        sub_section=SectionProxy('x_cpmd_section_geo_opt_initialization'),
        repeats=True)

    x_cpmd_section_geo_opt_step = SubSection(
        sub_section=SectionProxy('x_cpmd_section_geo_opt_step'),
        repeats=True)


class MolecularDynamics(workflow.MolecularDynamics):

    m_def = Section(validate=False, extends_base_section=True)

    x_cpmd_section_md_averaged_quantities = SubSection(
        sub_section=SectionProxy('x_cpmd_section_md_averaged_quantities'),
        repeats=True)
