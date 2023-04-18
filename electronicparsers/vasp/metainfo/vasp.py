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


m_package = Package()


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    vasp_build_date = Quantity(
        type=str,
        shape=[],
        description='''
        build date as string
        ''')

    vasp_src_date = Quantity(
        type=str,
        shape=[],
        description='''
        date of last modification of the source as string
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_vasp_incar_in = Quantity(
        type=JSON,
        shape=[],
        description='''
        contains all the user-input INCAR parameters
        ''')

    x_vasp_incar_out = Quantity(
        type=JSON,
        shape=[],
        description='''
        contains the actual INCAR parameters used by VASP at runtime
        ''')

    x_vasp_unknown_incars = Quantity(
        type=JSON,
        shape=[],
        description='''
        INCAR variables uknown wrt to Vasp Wiki
        ''')

    x_vasp_atom_kind_refs = Quantity(
        type=simulation.method.AtomParameters,
        shape=['number_of_atoms'],
        description='''
        reference to the atom kinds of each atom
        ''')

    x_vasp_numer_of_magmom = Quantity(
        type=int,
        shape=[],
        description='''
        number of magnetic moments, number_of_atoms for ISPIN = 2, 3*number of atoms for
        non-collinear magnetic systems
        ''')

    x_vasp_nose_thermostat = Quantity(
        type=np.dtype(np.float64),
        shape=[4],
        description='''
        Nose thermostat output
        ''')


class KMesh(simulation.method.KMesh):

    m_def = Section(validate=False, extends_base_section=True)

    x_vasp_tetrahedrons_list = Quantity(
        type=np.dtype(np.int32),
        shape=['N', 5],
        description='''
        Rows of 5 data points. First the weight (symmetry degeneration), then the four corner
        points of each tetrahedron.
        ''')

    x_vasp_tetrahedron_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[1],
        description='''
        Volume weight of a single tetrahedron (all tetra's must have the same volume)
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_vasp_selective_dynamics = Quantity(
        type=np.dtype(bool),
        shape=['number_of_atoms', 3],
        description='''
        Boolean array to eiter allow or forbid coordinate modifications during relaxation
        ''')


class HubbardKanamoriModel(simulation.method.HubbardKanamoriModel):

    m_def = Section(validate=False, extends_base_section=True)

    x_vasp_projection_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of orbitals used for projection in order to calculate occupation numbers.
        ''')


class GW(simulation.method.GW):

    m_def = Section(validate=False, extends_base_section=True)

    x_vasp_response_functions_incar = Quantity(
        type=JSON,
        shape=[],
        description='''
        Input parameters used in the "response functions".
        ''')
