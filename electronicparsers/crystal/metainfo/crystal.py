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


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_crystal_family = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal family.
        ''')

    x_crystal_class = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal class.
        ''')

    x_crystal_spacegroup = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal spacegroup string resembling Hermann–Mauguin notation.
        ''')

    x_crystal_dimensionality = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        System dimensionality.
        ''')

    x_crystal_n_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of symmetry operators.
        ''')


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_crystal_scf_ee = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL E-E
        4.6595142576204E+01
        ''')

    x_crystal_scf_en_ne = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL E-N + N-E
        -5.2283101954878E+02
        ''')

    x_crystal_scf_nn = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL N-N
        -7.3084276676762E+01
        ''')

    x_crystal_scf_virial_coefficient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: VIRIAL COEFFICIENT
        9.9998501747632E-01
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_crystal_run_title = Quantity(
        type=str,
        shape=[],
        description='''
        Title of the runcry(14) task.
        ''')

    x_crystal_datetime = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary type for storing date and time, in locale-dependent format.
        ''')

    x_crystal_executable_path = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal executable filepath.
        ''')

    x_crystal_hostname = Quantity(
        type=str,
        shape=[],
        description='''
        Hostname where Crystal was run.
        ''')

    x_crystal_input_path = Quantity(
        type=str,
        shape=[],
        description='''
        Input file name.
        ''')

    x_crystal_os = Quantity(
        type=str,
        shape=[],
        description='''
        String describing the operating system where Crystal was run.
        ''')

    x_crystal_output = Quantity(
        type=str,
        shape=[],
        description='''
        Output file name.
        ''')

    x_crystal_tmpdir = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary directory.
        ''')

    x_crystal_user = Quantity(
        type=str,
        shape=[],
        description='''
        Username: who ran Crystal.
        ''')

    x_crystal_distribution = Quantity(
        type=str,
        shape=[],
        description='''
        Distribution describer.
        ''')

    x_crystal_version_minor = Quantity(
        type=str,
        shape=[],
        description='''
        Minor version number of Crystal.
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_crystal_convergence_deltap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence seettings, on power of 10 (e.g. CONVERGENCE ON DELTAP        10**-16)
        ''')

    x_crystal_weight_f = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WEIGHT OF F(I) IN F(I+1)
        ''')

    x_crystal_coulomb_bipolar_buffer = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB BIPOLAR BUFFER SET TO x Mb
        ''')

    x_crystal_eigenvectors_disk_space_ftn = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DISK SPACE FOR EIGENVECTORS (FTN 10)      351575 REALS
        ''')

    x_crystal_eigenvectors_disk_space_reals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DISK SPACE FOR EIGENVECTORS (FTN 10)      351575 REALS
        ''')

    x_crystal_exchange_bipolar_buffer = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE BIPOLAR BUFFER SET TO x Mb
        ''')

    x_crystal_fock_ks_matrix_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FOCK/KS MATRIX MIXING SET TO x %
        ''')

    x_crystal_input_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INPUT       TELAPSE        0.01 TCPU        0.01
        ''')

    x_crystal_input_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INPUT       TELAPSE        0.01 TCPU        0.01
        ''')

    x_crystal_irr_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''')

    x_crystal_irr_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''')

    x_crystal_is1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''')

    x_crystal_is2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''')

    x_crystal_is3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''')

    x_crystal_n_k_points_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS(GILAT NET)    145
        ''')

    x_crystal_n_k_points_ibz = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS IN THE IBZ    145
        ''')

    x_crystal_k_pts_monk_net = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''')

    x_crystal_matrix_size_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''')

    x_crystal_matrix_size_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''')

    x_crystal_max_g_vector_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAX G-VECTOR INDEX FOR 1- AND 2-ELECTRON INTEGRALS 247
        ''')

    x_crystal_max_scf_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAX NUMBER OF SCF CYCLES
        ''')

    x_crystal_n_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF ATOMS PER CELL
        ''')

    x_crystal_n_core_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CORE ELECTRONS PER CELL
        ''')

    x_crystal_n_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF ELECTRONS PER CELL
        ''')

    x_crystal_n_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF AO (Atomic orbitals)
        ''')

    x_crystal_n_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF SHELLS
        ''')

    x_crystal_n_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF SYMMETRY OPERATORS
        ''')

    x_crystal_pole_order = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        POLE ORDER IN MONO ZONE
        ''')

    x_crystal_shrink_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        SHRINKING FACTOR(GILAT NET)   16
        ''')

    x_crystal_shrink_value1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''')

    x_crystal_shrink_value2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''')

    x_crystal_shrink_value3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''')

    x_crystal_shrink = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        SHRINK. FACT.(MONKH.)   16 16 16
        ''')

    x_crystal_symmetry_adaption = Quantity(
        type=bool,
        shape=[],
        description='''
        SYMMETRY ADAPTION OF THE BLOCH FUNCTIONS ENABLED
        ''')

    x_crystal_symmops_g = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''')

    x_crystal_symmops_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''')

    x_crystal_tol_coulomb_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB OVERLAP TOL         (T1) 10**   -6. (Tolerance T1, power of 10)
        ''')

    x_crystal_tol_coulomb_penetration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB PENETRATION TOL     (T2) 10**   -6. (Tolerance T2, power of 10)
        ''')

    x_crystal_tol_exchange_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE OVERLAP TOL        (T3) 10**   -6. (Tolerance T3, power of 10)
        ''')

    x_crystal_tol_pseudo_overlap_f = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE PSEUDO OVP (F(G))  (T4) 10**   -6. (Tolerance T4, power of 10)
        ''')

    x_crystal_tol_pseudo_overlap_p = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE PSEUDO OVP (P(G))  (T5) 10**  -12. (Tolerance T5, power of 10)
        ''')

    x_crystal_type_of_calculation = Quantity(
        type=str,
        shape=[],
        description='''
        The type of the calculation that was performed.
        ''')

    x_crystal_weight_previous = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WEIGHT OF F(I) IN F(I+1)      30%
        ''')

    x_crystal_toldee = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOLDEE info
        ''')


class BasisSetAtomCentered(simulation.method.BasisSetAtomCentered):

    m_def = Section(validate=False, extends_base_section=True)

    x_crystal_section_shell = SubSection(
        sub_section=SectionProxy('x_crystal_section_shell'),
        repeats=True
    )


class x_crystal_section_shell(MSection):
    '''
    Shell contains a number of orbitals.
    '''
    m_def = Section(validate=False)

    x_crystal_shell_range = Quantity(
        type=str,
        shape=[],
        description='''
        The range of orbitals
        ''')

    x_crystal_shell_type = Quantity(
        type=str,
        shape=[],
        description='''
        Shell type: S / P / SP / D / F / G.
        ''')

    x_crystal_shell_coefficients = Quantity(
        type=np.dtype(np.float64),
        shape=['n_orbitals', 4],
        description='''
        Contraction coefficients in this order: exponent, S, P, D/F/G.
        '''
    )


m_package.__init_metainfo__()
