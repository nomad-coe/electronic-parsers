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
    Reference, MEnum, JSON
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_fhi_aims_controlIn_method(MCategory):
    '''
    Parameters of control.in belonging to section method.
    '''

    m_def = Category()


class x_fhi_aims_controlInOut_method(MCategory):
    '''
    Parameters of aims output of parsed control.in belonging to section method.
    '''

    m_def = Category()


class x_fhi_aims_controlIn_run(MCategory):
    '''
    Parameters of control.in belonging to settings run.
    '''

    m_def = Category()


class x_fhi_aims_controlInOut_run(MCategory):
    '''
    Parameters of aims output of parsed control.in belonging to settings run.
    '''

    m_def = Category()


class x_fhi_aims_section_controlIn_basis_func(MSection):
    '''
    definition of a single basis function in the basis set
    '''

    m_def = Section(validate=False)

    x_fhi_aims_controlIn_basis_func_l = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlIn_basis_func_n = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlIn_basis_func_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlIn_basis_func_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')


class x_fhi_aims_section_controlIn_basis_set(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_fhi_aims_controlIn_angular_grids_method = Quantity(
        type=str,
        shape=[],
        description='''
        angular grids method (specifed or auto)
        ''')

    x_fhi_aims_controlIn_basis_dep_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        cutoff for the dependent basis
        ''')

    x_fhi_aims_controlIn_cut_pot = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        cut\\_pot parameters
        ''')

    x_fhi_aims_controlIn_cut_pot1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        first parameter of cut\\_pot
        ''')

    x_fhi_aims_controlIn_cut_pot2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        second parameter of cut\\_pot
        ''')

    x_fhi_aims_controlIn_cut_pot3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        third parameter of cut\\_pot
        ''')

    x_fhi_aims_controlIn_division1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        first parameter of division (position)
        ''')

    x_fhi_aims_controlIn_division2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        second parameter of division (n points)
        ''')

    x_fhi_aims_controlIn_division = Quantity(
        type=np.dtype(np.float64),
        shape=['x_fhi_aims_controlIn_number_of_basis_func', 2],
        description='''
        division parameters
        ''')

    x_fhi_aims_controlIn_number_of_basis_func = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of basis functions
        ''')

    x_fhi_aims_controlIn_l_hartree = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        angular leven for the hartreee part
        ''')

    x_fhi_aims_controlIn_mass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        mass of the nucleus in atomic mass units
        ''')

    x_fhi_aims_controlIn_nucleus = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        charge of the nucleus
        ''')

    x_fhi_aims_controlIn_outer_grid = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        outer grid
        ''')

    x_fhi_aims_controlIn_radial_base = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        radial\\_base parameters
        ''')

    x_fhi_aims_controlIn_radial_base1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        first parameter of radial\\_base
        ''')

    x_fhi_aims_controlIn_radial_base2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        second parameter of radial\\_base
        ''')

    x_fhi_aims_controlIn_radial_multiplier = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        radial multiplier
        ''')

    x_fhi_aims_controlIn_species_name = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_section_controlIn_basis_func = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_controlIn_basis_func'),
        repeats=True)


class x_fhi_aims_section_controlInOut_atom_species(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_fhi_aims_controlInOut_pure_gaussian = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_species_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_species_cut_pot_scale = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_species_cut_pot_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_species_cut_pot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_species_mass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kilogram',
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_species_name = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_section_controlInOut_basis_func = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_controlInOut_basis_func'),
        repeats=True)

    x_fhi_aims_section_vdW_TS = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_vdW_TS'),
        repeats=True)


class x_fhi_aims_section_controlInOut_basis_func(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_fhi_aims_controlInOut_basis_func_eff_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_gauss_alpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter ** 2',
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_gauss_l = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_gauss_N = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_gauss_weight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_l = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_n = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_occ = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_primitive_gauss_alpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter ** 2',
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_controlInOut_basis_func_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')


class x_fhi_aims_section_eigenvalues_group_ZORA(MSection):
    '''
    section for full list of eigenvalues for different spin and kpoints of scaled ZORA
    '''

    m_def = Section(validate=False)

    x_fhi_aims_section_eigenvalues_spin_ZORA = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_spin_ZORA'),
        repeats=True)


class x_fhi_aims_section_eigenvalues_group(MSection):
    '''
    section for full list of eigenvalues for different spin and kpoints
    '''

    m_def = Section(validate=False)

    x_fhi_aims_section_eigenvalues_spin = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_spin'),
        repeats=True)


class x_fhi_aims_section_eigenvalues_list_ZORA(MSection):
    '''
    section for one list of eigenvalues at specific kpoint and spin of scaled ZORA
    '''

    m_def = Section(validate=False)

    x_fhi_aims_eigenvalue_eigenvalue_ZORA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Single eigenvalue of scaled ZORA
        ''')

    x_fhi_aims_eigenvalue_occupation_ZORA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Occupation of single eigenfunction of scaled ZORA
        ''')


class x_fhi_aims_section_eigenvalues_list(MSection):
    '''
    section for one list of eigenvalues at specific kpoint and spin
    '''

    m_def = Section(validate=False)

    x_fhi_aims_eigenvalue_eigenvalue = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Single eigenvalue
        ''')

    x_fhi_aims_eigenvalue_occupation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Occupation of single eigenfunction
        ''')


class x_fhi_aims_section_eigenvalues_spin_ZORA(MSection):
    '''
    section for one spin orientation of scaled ZORA
    '''

    m_def = Section(validate=False)

    x_fhi_aims_eigenvalue_kpoint1_ZORA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Component 1 of kpoints on which the eigenvalues were evaluated of scaled ZORA
        ''')

    x_fhi_aims_eigenvalue_kpoint2_ZORA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Component 2 of kpoints on which the eigenvalues were evaluated of scaled ZORA
        ''')

    x_fhi_aims_eigenvalue_kpoint3_ZORA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Component 3 of kpoints on which the eigenvalues were evaluated of scaled ZORA
        ''')

    x_fhi_aims_section_eigenvalues_list_ZORA = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_list_ZORA'),
        repeats=True)


class x_fhi_aims_section_eigenvalues_spin(MSection):
    '''
    section for one spin orientation
    '''

    m_def = Section(validate=False)

    x_fhi_aims_eigenvalue_kpoint1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Component 1 of kpoints on which the eigenvalues were evaluated
        ''')

    x_fhi_aims_eigenvalue_kpoint2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Component 2 of kpoints on which the eigenvalues were evaluated
        ''')

    x_fhi_aims_eigenvalue_kpoint3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Component 3 of kpoints on which the eigenvalues were evaluated
        ''')

    x_fhi_aims_section_eigenvalues_list_perturbativeGW = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_list_perturbativeGW'),
        repeats=True)

    x_fhi_aims_section_eigenvalues_list = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_list'),
        repeats=True)


class x_fhi_aims_section_eigenvalues_ZORA(MSection):
    '''
    section for gathering eigenvalues of scaled ZORA
    '''

    m_def = Section(validate=False)

    x_fhi_aims_section_eigenvalues_group_ZORA = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_group_ZORA'),
        repeats=False)


class x_fhi_aims_section_MD_detect(MSection):
    '''
    Section to detect MD immediately during parsing of controlInOut
    '''

    m_def = Section(validate=False)


class x_fhi_aims_section_parallel_task_assignement(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_fhi_aims_parallel_task_host = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_parallel_task_nr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class x_fhi_aims_section_parallel_tasks(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_fhi_aims_section_parallel_task_assignement = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_parallel_task_assignement'),
        repeats=True)


class x_fhi_aims_section_vdW_TS(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_fhi_aims_atom_type_vdW = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_free_atom_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_hirschfeld_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_hirschfeld_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_vdW_energy_corr_TS = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        -
        ''')


class x_fhi_aims_section_eigenvalues_group_perturbativeGW(MSection):
    '''
    section for full list of eigenvalues for different spin and kpoints from a
    perturbative GW calculation
    '''

    m_def = Section(validate=False)

    x_fhi_aims_section_eigenvalues_spin_perturbativeGW = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_spin_perturbativeGW'),
        repeats=True)


class x_fhi_aims_section_eigenvalues_list_perturbativeGW(MSection):
    '''
    section for one list of eigenvalues from a perturbative GW calculation
    '''

    m_def = Section(validate=False)

    x_fhi_aims_eigenvalue_correlation_perturbativeGW = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Correlation energy at a given eigenstate from perturbative GW
        ''')

    x_fhi_aims_eigenvalue_ExactExchange_perturbativeGW = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Exact exchange energy at given eigenstate from perturbative GW
        ''')

    x_fhi_aims_eigenvalue_ks_ExchangeCorrelation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        KS exchange correlation energy at a given eigenstate needed to calculate the
        quasi-particle energy in perturbative GW
        ''')

    x_fhi_aims_eigenvalue_ks_GroundState = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        KS ground state energy at a given eigenstate needed in perturbative GW
        ''')

    x_fhi_aims_eigenvalue_occupation_perturbativeGW = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Occupation of single eigenfunction of perturbative GW
        ''')

    x_fhi_aims_eigenvalue_quasiParticle_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Quasiparticle energy at a given eigenstate from perturbative GW
        ''')


class x_fhi_aims_section_eigenvalues_spin_perturbativeGW(MSection):
    '''
    section for one spin orientation from a perturbative GW calculation
    '''

    m_def = Section(validate=False)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_atom_forces_free_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''',)

    x_fhi_aims_atom_forces_free_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''',)

    x_fhi_aims_atom_forces_free_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''',)

    x_fhi_aims_energy_C_LDA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Component of the correlation (C) energy at the LDA level calculated with the self
        consistent density of the target functional.
        ''',)

    x_fhi_aims_energy_X_LDA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Component of the exchange (X) energy at the LDA level calculated with the self
        consistent density of the target functional.
        ''',)

    x_fhi_aims_cube_filename = Quantity(
        type=str,
        shape=[],
        description='''
        filename of cube file
        ''')

    x_fhi_aims_calculation_md = Quantity(
        type=JSON,
        shape=[],
        description='''
        All MD-related calculation quantities.
        ''')


class ScfIeration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_atom_forces_raw_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''')

    x_fhi_aims_atom_forces_raw_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''')

    x_fhi_aims_atom_forces_raw_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''')

    x_fhi_aims_energy_electrostatic_free_atom_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Electrostatic energy contributions from superposition of free atom densities
        during the scf iterations
        ''',)

    x_fhi_aims_energy_scgw_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        scGW correlation energy at each iteration
        ''',)

    x_fhi_aims_poles_fit_accuracy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Fit acccuracy for the Fast-Fourier Transforms necessary in the scGW formalism
        ''',)

    x_fhi_aims_scf_date_start = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_scf_time_start = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_scgw_galitskii_migdal_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        scGW total energy at each iteration calculated using the Galitskii-Migdal formula
        ''',)

    x_fhi_aims_scgw_hartree_energy_sum_eigenvalues_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        scGW sum of eigenvalues calculated from the trace over the Hamiltonian times the
        Greens function matrices
        ''',)

    x_fhi_aims_scgw_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        scGW kinetic energy at each iteration
        ''',)

    x_fhi_aims_scgw_rpa_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        The RPA correlation energy calculated from the Green's functions of the scGW at
        each iteration
        ''',)

    x_fhi_aims_single_configuration_calculation_converged = Quantity(
        type=str,
        shape=[],
        description='''
        Determines whether a single configuration calculation is converged.
        ''')

    x_fhi_aims_single_particle_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        scGW single particle energy at each iteration
        ''',)

    x_fhi_aims_section_eigenvalues_group = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_eigenvalues_group'),
        repeats=False)

    x_fhi_aims_energy_reference_fermi = Quantity(
        type=float, unit='eV')


class DosValues(simulation.calculation.DosValues):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_normalization_factor_raw_data = Quantity(
        type=np.dtype(np.float64),
        default=1,
        shape=[],
        description='''
        Normalization factor to reobtain the DOS values as presented in the raw data files.
        ''')


class BandStructure(simulation.calculation.BandStructure):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_band_k1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_band_k2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_band_k3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_band_occupations_eigenvalue_string = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_band_segment = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_controlIn_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_hse_omega = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        -
        ''',)

    x_fhi_aims_controlIn_hse_unit = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlIn_hybrid_xc_coeff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_k1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_k2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_k3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_k_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_occupation_order = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_occupation_type = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_occupation_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_override_relativity = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlIn_relativistic_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlIn_relativistic = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlIn_sc_accuracy_eev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_sc_accuracy_etot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_sc_accuracy_forces = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_sc_accuracy_rho = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_sc_accuracy_stress = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_sc_iter_limit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_spin = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_verbatim_writeout = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlIn_method])

    x_fhi_aims_controlIn_xc = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlInOut_band_segment_end1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_band_segment_end2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_band_segment_end3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_band_segment_start1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_band_segment_start2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_band_segment_start3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_hse_omega = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        -
        ''',)

    x_fhi_aims_controlInOut_hse_unit = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlInOut_hybrid_xc_coeff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_k1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_k2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_k3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_k_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_number_of_spin_channels = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''',
        categories=[x_fhi_aims_controlInOut_method])

    x_fhi_aims_controlInOut_override_relativity = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlInOut_relativistic_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlInOut_relativistic = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_controlInOut_xc = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_fhi_aims_section_controlIn_basis_set = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_controlIn_basis_set'),
        repeats=True)

    x_fhi_aims_section_MD_detect = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_MD_detect'),
        repeats=True)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_controlIn_MD_time_step = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='second',
        description='''
        -
        ''',)

    x_fhi_aims_controlInOut_MD_time_step = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='second',
        description='''
        -
        ''',)

    x_fhi_aims_geometry_optimization_converged = Quantity(
        type=str,
        shape=[],
        description='''
        Determines whether a geoemtry optimization is converged.
        ''')

    x_fhi_aims_number_of_tasks = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_program_compilation_date = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_program_compilation_time = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_program_execution_date = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_program_execution_time = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_fhi_aims_section_parallel_tasks = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_parallel_tasks'),
        repeats=False)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_geometry_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        labels of atom
        ''')

    x_fhi_aims_geometry_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of atomic position
        ''')

    x_fhi_aims_geometry_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of atomic position
        ''')

    x_fhi_aims_geometry_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of atomic position
        ''')

    x_fhi_aims_geometry_atom_velocity_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter / second',
        description='''
        x component of atomic velocity
        ''')

    x_fhi_aims_geometry_atom_velocity_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter / second',
        description='''
        y component of atomic velocity
        ''')

    x_fhi_aims_geometry_atom_velocity_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter / second',
        description='''
        z component of atomic velocity
        ''')

    x_fhi_aims_geometry_lattice_vector_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of lattice vector
        ''')

    x_fhi_aims_geometry_lattice_vector_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of lattice vector
        ''')

    x_fhi_aims_geometry_lattice_vector_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of lattice vector
        ''')


class AtomParameters(simulation.method.AtomParameters):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_section_controlInOut_atom_species = SubSection(
        sub_section=SectionProxy('x_fhi_aims_section_controlInOut_atom_species'),
        repeats=True)


class HubbardKanamoriModel(simulation.method.HubbardKanamoriModel):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_projection_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of orbitals used for projection in order to calculate occupation numbers.
        ''')

    x_fhi_aims_petukhov_mixing_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mixing term to correct for double counting in DFT+U
        ''')


class MolecularDynamicsMethod(simulation.workflow.MolecularDynamicsMethod):

    m_def = Section(validate=False, extends_base_section=True)

    x_fhi_aims_controlIn_md = Quantity(
        type=JSON,
        shape=[],
        description='''
        All MD-related input parameters.
        ''')
