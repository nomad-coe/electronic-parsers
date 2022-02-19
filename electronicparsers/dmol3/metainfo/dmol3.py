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


class dmol3_section_hirshfeld_population(MSection):
    '''
    Hirshfeld Population Analysis Section
    '''

    m_def = Section(validate=False)

    dmol3_hirshfeld_population = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Hirshfeld Population Analysis
        ''')


class dmol3_section_mulliken_population(MSection):
    '''
    Mulliken Population Analysis Section
    '''

    m_def = Section(validate=False)

    dmol3_mulliken_population = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mulliken Population Analysis
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    dmol3_aux_density = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 aux density
        ''')

    dmol3_aux_partition = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 aux parition
        ''')

    dmol3_basis_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 basis name
        ''')

    dmol3_calculation_type = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 calculation type
        ''')

    dmol3_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 system charge
        ''')

    dmol3_electrostatic_moments = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Electrostatic_Moments
        ''')

    dmol3_functional_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 functional name
        ''')

    dmol3_hirshfeld_analysis = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Hirshfeld_Analysis
        ''')

    dmol3_integration_grid = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 integration grid
        ''')

    dmol3_kpoints = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Kpoints
        ''')

    dmol3_mulliken_analysis = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Mulliken_Analysis
        ''')

    dmol3_nuclear_efg = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Nuclear_EFG
        ''')

    dmol3_occupation_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Occupation name
        ''')

    dmol3_occupation_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 Occupation width
        ''')

    dmol3_opt_coordinate_system = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 OPT_Coordinate_System
        ''')

    dmol3_opt_displacement_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Displacement_Convergence
        ''')

    dmol3_opt_energy_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Energy_Convergence
        ''')

    dmol3_opt_gdiis = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 OPT_Gdiis
        ''')

    dmol3_opt_gradient_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Gradient_Convergence
        ''')

    dmol3_opt_hessian_project = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 OPT_Hessian_Project
        ''')

    dmol3_opt_iterations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 OPT_Iterations
        ''')

    dmol3_opt_max_displacement = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Max_Displacement
        ''')

    dmol3_opt_steep_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Steep_Tol
        ''')

    dmol3_optical_absorption = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Optical_Absorption
        ''')

    dmol3_partial_dos = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Partial_Dos
        ''')

    dmol3_pseudopotential_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 pseudopotential name
        ''')

    dmol3_rcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 atom R_cut
        ''')

    dmol3_scf_charge_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_Charge_Mixing
        ''')

    dmol3_scf_density_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_Density_Convergence
        ''')

    dmol3_scf_diis_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 SCF_DIIS name
        ''')

    dmol3_scf_diis_number = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_DIIS number
        ''')

    dmol3_scf_direct = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 SCF_Direct
        ''')

    dmol3_scf_iterations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 SCF_Iterations
        ''')

    dmol3_scf_number_bad_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 SCF_Number_Bad_Steps
        ''')

    dmol3_scf_restart = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 SCF_Restart
        ''')

    dmol3_scf_spin_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_Spin_Mixing
        ''')

    dmol3_spin_polarization = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 spin polarization
        ''')

    dmol3_spin = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 number of unpaired electrons
        ''')

    dmol3_symmetry = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 sysmmetry
        ''')


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    dmol3_binding_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        dmol3 binding energy at every SCF
        ''')

    dmol3_convergence_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 convergence at every SCF
        ''')

    dmol3_number_scf_iteration = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 iteration number at every SCF
        ''')

    dmol3_time_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 time at every SCF
        ''')


class BandEnergies(simulation.calculation.BandEnergies):

    m_def = Section(validate=False, extends_base_section=True)

    dmol3_eigenvalue_eigenvalue = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Single eigenvalue
        ''')

    dmol3_eigenvalue_occupation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Occupation of single eigenfunction
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    dmol3_geometry_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        labels of atom
        ''')

    dmol3_geometry_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of atomic position
        ''')

    dmol3_geometry_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of atomic position
        ''')

    dmol3_geometry_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of atomic position
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    dmol3_program_compilation_date = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 compilation date
        ''')

    dmol3_program_compilation_time = Quantity(
        type=str,
        shape=[],
        description='''
        dmol compilation date
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    dmol3_section_hirshfeld_population = SubSection(
        sub_section=SectionProxy('dmol3_section_hirshfeld_population'),
        repeats=True)

    dmol3_section_mulliken_population = SubSection(
        sub_section=SectionProxy('dmol3_section_mulliken_population'),
        repeats=True)
