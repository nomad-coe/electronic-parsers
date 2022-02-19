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


class x_nwchem_section_start_information(MSection):
    '''
    Contains information about the starting conditions for this run
    '''

    m_def = Section(validate=False)

    x_nwchem_input_filename = Quantity(
        type=str,
        shape=[],
        description='''
        .
        ''')

    x_nwchem_start_datetime = Quantity(
        type=str,
        shape=[],
        description='''
        The run start date and time.
        ''')

    x_nwchem_compilation_datetime = Quantity(
        type=str,
        shape=[],
        description='''
        The compilation date and time.
        ''')

    x_nwchem_run_host_name = Quantity(
        type=str,
        shape=[],
        description='''
        The host on which this calculation was made on.
        ''')

    x_nwchem_source = Quantity(
        type=str,
        shape=[],
        description='''
        The source directory of the code.
        ''')

    x_nwchem_branch = Quantity(
        type=str,
        shape=[],
        description='''
        The main branch of the code.
        ''')

    x_nwchem_revision = Quantity(
        type=str,
        shape=[],
        description='''
        The SVN revision of the code.
        ''')

    x_nwchem_ga_revision = Quantity(
        type=str,
        shape=[],
        description='''
        The ga revision.
        ''')

    x_nwchem_input_prefix = Quantity(
        type=str,
        shape=[],
        description='''
        The input prefix.
        ''')

    x_nwchem_db_filename = Quantity(
        type=str,
        shape=[],
        description='''
        The database filename.
        ''')

    x_nwchem_status = Quantity(
        type=str,
        shape=[],
        description='''
        Status of the run.
        ''')

    x_nwchem_nproc = Quantity(
        type=str,
        shape=[],
        description='''
        Number of processes used.
        ''')

    x_nwchem_time_left = Quantity(
        type=str,
        shape=[],
        description='''
        Time left in seconds.
        ''')

    x_nwchem_program_name = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the program that was run.
        ''')


class x_nwchem_section_xc_part(MSection):
    '''
    Describes a part of the XC functional that is used in the calculation. Can be a local
    or non-local part, can be exchange or correlation, can have a weight.
    '''

    m_def = Section(validate=False)

    x_nwchem_xc_functional_name = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the XC functional
        ''')

    x_nwchem_xc_functional_weight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The weight of the XC functional.
        ''')

    x_nwchem_xc_functional_type = Quantity(
        type=str,
        shape=[],
        description='''
        The type of the XC functional, local or non-local
        ''')


class x_nwchem_section_geometry(MSection):
    '''
    Contains system information for a calculation to follow. Contains all of the
    geometries used in different NWChem tasks contained by this calculations.
    '''

    m_def = Section(validate=False)


class x_nwchem_section_geo_opt_module(MSection):
    '''
    Section for a geometry optimization task.
    '''

    m_def = Section(validate=False)

    x_nwchem_section_geo_opt_step = SubSection(
        sub_section=SectionProxy('x_nwchem_section_geo_opt_step'),
        repeats=True)


class x_nwchem_section_geo_opt_step(MSection):
    '''
    Section for a geometry optimization step.
    '''

    m_def = Section(validate=False)

    x_nwchem_geo_opt_step_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The energy for a geometry optimization step.
        ''')


class x_nwchem_section_qmd_module(MSection):
    '''
    Section for QMD Module.
    '''

    m_def = Section(validate=False)


class x_nwchem_section_qmd_step(MSection):
    '''
    DFT QMD step
    '''

    m_def = Section(validate=False)

    x_nwchem_qmd_step_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='second',
        description='''
        Elapsed simulation time.
        ''')

    x_nwchem_qmd_step_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Kinetic energy.
        ''')

    x_nwchem_qmd_step_potential_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Potential energy.
        ''')

    x_nwchem_qmd_step_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Total energy.
        ''')

    x_nwchem_qmd_step_target_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        Target temperature.
        ''')

    x_nwchem_qmd_step_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        Temperature.
        ''')

    x_nwchem_qmd_step_dipole = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Electric dipole moment.
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_nwchem_section_start_information = SubSection(
        sub_section=SectionProxy('x_nwchem_section_start_information'),
        repeats=True)

    x_nwchem_section_geometry = SubSection(
        sub_section=SectionProxy('x_nwchem_section_geometry'),
        repeats=True)

    x_nwchem_section_geo_opt_module = SubSection(
        sub_section=SectionProxy('x_nwchem_section_geo_opt_module'),
        repeats=True)

    x_nwchem_section_qmd_module = SubSection(
        sub_section=SectionProxy('x_nwchem_section_qmd_module'),
        repeats=True)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_nwchem_xc_functional_shortcut = Quantity(
        type=str,
        shape=[],
        description='''
        Shorcut for a XC functional definition.
        ''')

    x_nwchem_electron_spin_restriction = Quantity(
        type=str,
        shape=[],
        description='''
        Electron spin restriction.
        ''')

    x_nwchem_section_xc_part = SubSection(
        sub_section=SectionProxy('x_nwchem_section_xc_part'),
        repeats=True)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_nwchem_energy_one_electron = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The one-electron energy in a DFT calculation.
        ''')

    x_nwchem_energy_coulomb = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The Coulomb energy energy in a DFT calculation.
        ''')

    x_nwchem_energy_nuclear_repulsion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The nuclear repulsion energy in a DFT calculation.
        ''')

    x_nwchem_section_qmd_step = SubSection(
        sub_section=SectionProxy('x_nwchem_section_qmd_step'),
        repeats=True)


class MolecularDynamics(workflow.MolecularDynamics):

    m_def = Section(validate=False, extends_base_section=True)

    x_nwchem_qmd_number_of_nuclear_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of nuclear steps.
        ''')

    x_nwchem_qmd_nuclear_time_step = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Nuclear time step.
        ''')

    x_nwchem_qmd_target_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Target temperature.
        ''')

    x_nwchem_qmd_thermostat = Quantity(
        type=str,
        shape=[],
        description='''
        Thermostat for QMD.
        ''')

    x_nwchem_qmd_tau = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Tau for QMD thermostat.
        ''')

    x_nwchem_qmd_random_seed = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Random seed.
        ''')

    x_nwchem_qmd_nuclear_integrator = Quantity(
        type=str,
        shape=[],
        description='''
        Integrator for nuclei.
        ''')

    x_nwchem_qmd_initial_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Initial temperature
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_nwchem_reciprocal_simulation_cell = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        The simulation cell in reciprocal space.
        ''')

    x_nwchem_lattice_basis_vector_lengths = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        The lengths of the basis vectors.
        ''')

    x_nwchem_lattice_basis_vector_angles = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        The angles between the basis vectors.
        ''')

    x_nwchem_lattice_omega = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The lattice omega value.
        ''')
