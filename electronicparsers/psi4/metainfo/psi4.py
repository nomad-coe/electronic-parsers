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
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, Reference
)

from nomad.datamodel.metainfo import simulation
from nomad.metainfo.metainfo import JSON


m_package = Package()


class Run(simulation.run.Run):
    m_def = Section(validate=False, extends_base_section=True)

    x_psi4_git_rev = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_process_id = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_psi4_psidatadir = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_memory = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        # unit='MiB',
        description='''
        ''')

    x_psi4_threads = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_psi4_input_file = Quantity(
        type=str,
        shape=[],
        description='''
        ''')


class System(simulation.system.System):
    m_def = Section(validate=False, extends_base_section=True)

    x_psi4_molecular_point_group = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_full_point_group = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_molecular_symmetry = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_rotational_constants = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        # unit='1/cm',
        description='''
        ''')

    x_psi4_nuclear_repulsion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_multiplicity = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_nalpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_nbeta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')


class Scf(simulation.method.Scf):
    m_def = Section(validate=False, extends_base_section=True)

    x_psi4_diis = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_psi4_mom = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_psi4_fractional_occupation = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_psi4_guess_type = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_integral_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')


class BasisSetAtomCentered(simulation.method.BasisSetAtomCentered):
    m_def = Section(validate=False, extends_base_section=True)

    x_psi4_blend = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_n_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Gives the number of shell types used.
        ''')

    x_psi4_max_angular_momentum = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum angular momentum quantum number corresponding to the shells used.
        ''')

    x_psi4_n_cartesian_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_psi4_spherical_harmonics = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_psi4_n_ecp_primitives = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_psi4_n_ecp_core_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')


class Method(simulation.method.Method):
    m_def = Section(validate=False, extends_base_section=True)

    x_psi4_scf_algorithm_type = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_diis = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_psi4_mom = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_psi4_fractional_occupation = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_psi4_guess_type = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_psi4_options = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_psi4_jk_matrices_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_psi4_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')


class DFT(simulation.method.DFT):
    m_def = Section(validate=False, extends_base_section=True)

    x_psi4_molecular_quadrature = Quantity(
        type=typing.Any,
        shape=[],
        description='''
        ''')


class x_psi4_root_information(MSection):
    m_def = Section(validate=False)

    x_psi4_root_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')


class Calculation(simulation.calculation.Calculation):
    m_def = Section(validate=False, extends_base_section=True)

    x_psi4_s2_expected = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_s2_observed = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_s_expected = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_s_observed = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_psi4_root_information = SubSection(sub_section=x_psi4_root_information.m_def, repeats=True)
