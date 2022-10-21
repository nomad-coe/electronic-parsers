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


class x_abacus_input_settings(MCategory):
    '''
    Parameters of INPUT.
    '''

    m_def = Category()


class x_abacus_exx_settings(MCategory):
    '''
    Parameters are relevant when using hybrid functionals.
    '''

    m_def = Category()


class x_abacus_section_parallel(MSection):
    '''
    section for run-time parallization options of ABACUS
    '''

    m_def = Section(validate=False)

    x_abacus_nproc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of processors
        ''')

    x_abacus_kpar = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Devide all processors into kpar groups, and k points will be distributed among each group.
        ''')

    x_abacus_bndpar = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Devide all processors into bndpar groups, and bands (only stochastic orbitals now) will be distributed among each group
        ''')

    x_abacus_diago_proc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        If set to a positive number, then it specifies the number of threads used for carrying out diagonalization.
        ''')

    x_abacus_allocation_method = Quantity(
        type=str,
        shape=[],
        description='''
        The algorithms of dividing the H&S matrix
        ''')

    x_abacus_allocation_nb2d = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_allocation_trace_loc_row = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_allocation_trace_loc_col = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_allocation_nloc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class x_abacus_section_specie_basis_set(MSection):
    '''
    definition of each basis set
    '''

    m_def = Section(validate=False)

    x_abacus_specie_basis_set_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Filename of basis set
        ''')

    x_abacus_specie_basis_set_ln = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abacus_specie_basis_set_number_of_orbitals', 2],
        description='''
        -
        ''')

    x_abacus_specie_basis_set_rmesh = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_specie_basis_set_rcutoff = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_specie_basis_set_number_of_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class x_abacus_section_basis_sets(MSection):
    '''
    section for numerical atomic orbitals of ABACUS
    '''

    m_def = Section(validate=False)

    x_abacus_basis_sets_delta_k = Quantity(
        type=np.dtype(np.float64),
        unit='1/bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_basis_sets_delta_r = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_basis_sets_dr_uniform = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_basis_sets_rmax = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_basis_sets_kmesh = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_section_specie_basis_set = SubSection(
        sub_section=SectionProxy('x_abacus_section_specie_basis_set'),
        repeats=True,)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_init_velocities = Quantity(
        type=bool,
        shape=[],
        description='''
        Initialize velocities?
        ''',
        categories=[x_abacus_input_settings])

    x_abacus_longest_orb_rcut = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_longest_nonlocal_projector_rcut = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_searching_radius = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_searching_radius_unit = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        -
        ''')

    x_abacus_read_space_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        -
        ''')

    x_abacus_big_cell_numbers_in_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        -
        ''')

    x_abacus_meshcell_numbers_in_big_cell = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        -
        ''')

    x_abacus_extended_fft_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        -
        ''')

    x_abacus_extended_fft_grid_dim = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        -
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_input_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Filename input was read from
        ''',)

    x_abacus_program_execution_time = Quantity(
        type=np.dtype(np.float64),
        unit='seconds',
        shape=[],
        description='''
        The duration of the program execution
        ''',)

    x_abacus_stru_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Directory where initial atom_positions and lattice_vectors were read from
        ''')

    x_abacus_kpt_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Directory where k-points were read from
        ''')

    x_abacus_basis_set_dirname = Quantity(
        type=str,
        shape=[],
        description='''
        Directory where basis set were read from
        ''')

    x_abacus_pseudopotential_dirname = Quantity(
        type=str,
        shape=[],
        description='''
        Directory where pseudopotential were read from
        ''')

    x_abacus_section_parallel = SubSection(
        sub_section=SectionProxy('x_abacus_section_parallel'),
        repeats=True,)

    x_abacus_md_nstep_in = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The target total number of md steps.
        ''',
        categories=[x_abacus_input_settings])

    x_abacus_md_nstep_out = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The actual total number of md steps.
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_initial_magnetization_total = Quantity(
        type=np.dtype(np.float64),
        unit='bohr_magneton',
        shape=[],
        description='''
        Initial total magnetization of the system set in INPUT.
        ''')

    x_abacus_diagonalization_algorithm = Quantity(
        type=str,
        shape=[],
        description='''
        Algorithm used in subspace diagonalization
        ''')

    x_abacus_dispersion_correction_method = Quantity(
        type=str,
        shape=[],
        description='''
        Calculation includes semi-empirical DFT-D dispersion correction
        ''')

    x_abacus_basis_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of basis sets
        ''')

    x_abacus_spin_orbit = Quantity(
        type=bool,
        shape=[],
        description='''
        Spin-orbit coupling flag: with/without spin-orbit
        ''')

    x_abacus_noncollinear = Quantity(
        type=bool,
        shape=[],
        description='''
        Noncollinear spin mode
        ''')

    x_abacus_mixing_method = Quantity(
        type=str,
        shape=[],
        description='''
        Charge mixing methods
        ''')

    x_abacus_mixing_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mixing method: parameter beta
        ''')

    x_abacus_gamma_algorithms = Quantity(
        type=bool,
        shape=[],
        description='''
        Usage of gamma-only optimized algorithms
        ''')

    x_abacus_scf_threshold_density = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The density threshold for electronic iteration
        ''')

    x_abacus_xc_functional = Quantity(
        type=str,
        shape=[],
        description='''
        Type of exchange-correlation functional used in calculation.
        ''',
        categories=[x_abacus_input_settings])

    x_abacus_pao_radial_cutoff = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        Radial cut-off of pseudo atomic orbital
        ''',)

    x_abacus_hse_omega = Quantity(
        type=np.dtype(np.float64),
        unit='1 / meter',
        shape=[],
        description='''
        HSE omega
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_hybrid_xc_coeff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mixing parameter of hybrid functionals
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_number_of_pw_for_wavefunction = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_number_of_sticks_for_wavefunction = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_number_of_pw_for_density = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_number_of_sticks_for_density = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_exx_ccp_rmesh_times = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This parameter determines how many times larger the radial mesh required for calculating Columb potential is to that of atomic orbitals
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_exx_dm_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smaller values of the density matrix can be truncated to accelerate calculation.
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_exx_cauchy_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Using Cauchy-Schwartz inequality to find an upper bound of each Fock exchange matrix element before carrying out explicit evaluations
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_exx_schwarz_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Using Cauchy-Schwartz inequality to find an upper bound of each four-center integral element before carrying out explicit evaluations
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_exx_c_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smaller components of the C matrix is neglected to accelerate calculation
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_exx_v_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smaller components of the V matrix is neglected to accelerate calculation
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_exx_pca_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The size of basis of auxiliary basis functions is reduced using principal component analysis.
        ''',
        categories=[x_abacus_input_settings, x_abacus_exx_settings])

    x_abacus_section_basis_sets = SubSection(
        sub_section=SectionProxy('x_abacus_section_basis_sets'),
        repeats=True,)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_alat = Quantity(
        type=np.dtype(np.float64),
        unit='bohr',
        shape=[],
        description='''
        Lattice Parameter 'a', constant during a run and used as unit in other quantities
        ''')

    x_abacus_reciprocal_vectors = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        unit='1 / meter',
        description='''
        The reciprocal cell
        ''',)

    x_abacus_celldm = Quantity(
        type=np.dtype(np.float64),
        shape=[6],
        description='''
        Cell [a, b, c, alpha, beta, gamma], length a, b and c are in unit Angstrom
        ''')

    x_abacus_ibrav = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Bravais lattice index, constant during a run
        ''')

    x_abacus_number_of_electrons_out = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abacus_number_of_species'],
        description='''
        This denotes number of electrons of each element in the system calculated by ABACUS
        ''')

    x_abacus_total_number_of_electrons_in = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This denotes total number of electrons set in INPUT
        ''')

    x_abacus_number_of_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This denotes total number of species in the system
        ''')

    x_abacus_cell_volume = Quantity(
        type=np.dtype(np.float64),
        unit='bohr**3',
        shape=[],
        description='''
        Volume of unit cell
        ''',)

    x_abacus_atom_magnetic_moments = Quantity(
        type=np.dtype(np.float64),
        unit='bohr_magneton',
        shape=['number_of_atoms', 3],
        description='''
        The start magnetization for each atom
        ''',)


class Symmetry(simulation.system.Symmetry):
    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_ibrav = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Bravais lattice index, constant during a run
        ''')

    x_abacus_point_group_schoenflies_name = Quantity(
        type=str,
        shape=[],
        description='''
        The Schoenflies name of the point group
        ''')

    x_abacus_number_of_rotation_matrices = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_number_of_point_group_operations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_abacus_number_of_space_group_operations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')


class AtomParameters(simulation.method.AtomParameters):
    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_pp_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of pseudopotential, e.g. 'NC' or 'US'
        ''',)

    x_abacus_pp_xc = Quantity(
        type=str,
        shape=[],
        description='''
        Exchange-correlation functional of pseudopotential, e.g. 'PBE' or 'PZ'
        ''',)

    x_abacus_pp_lmax = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum angular momentum component in pseudopotential
        ''',)

    x_abacus_pp_nzeta = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of wavefunctions in pseudopotential
        ''',)

    x_abacus_pp_nprojectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of projectors in pseudopotential
        ''',)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_density_change_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Stores the change of charge density with respect to the previous self-consistent
        field (SCF) iteration.
        ''')

    x_abacus_energy_total_harris_foulkes_estimate = Quantity(
        type=np.dtype(np.float64),
        unit='joule',
        shape=[],
        description='''
        Stores the change of charge density with respect to the previous self-consistent
        field (SCF) iteration.
        ''')

    x_abacus_magnetization_total = Quantity(
        type=np.dtype(np.float64),
        unit='bohr_magneton',
        shape=[3],
        description='''
        Total per-cell magnetization
        ''',)

    x_abacus_magnetization_absolute = Quantity(
        type=np.dtype(np.float64),
        unit='bohr_magneton',
        shape=[],
        description='''
        Absolute per-cell magnetization
        ''',)


class BandEnergies(simulation.calculation.BandEnergies):

    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_eigenvalues_number_of_planewaves = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_eigenvalues_kpoints'],
        description='''
        Number of plane waves for each k-point
        ''',)


class GeometryOptimization(workflow.GeometryOptimization):

    m_def = Section(validate=False, extends_base_section=True)

    x_abacus_geometry_optimization_threshold_stress = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='pascal',
        description='''
        The threshold of the stress convergence, it indicates the largest stress among all the directions
        ''')


m_package.__init_metainfo__()
