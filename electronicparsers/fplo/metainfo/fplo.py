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


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_program_version_sub = Quantity(
        type=str,
        shape=[],
        description='''
        FPLO sub version
        ''')

    x_fplo_program_compilation_options = Quantity(
        type=str,
        shape=[],
        description='''
        FPLO compilation options
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_reciprocal_cell = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        unit='1 / meter',
        description='''
        Reciprocal Lattice vectors (in Cartesian coordinates). The first index runs over
        the $x,y,z$ Cartesian coordinates, and the second index runs over the 3 lattice
        vectors.
        ''')

    x_fplo_atom_idx = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atoms'],
        description='''
        FPLO-internal index for each atom
        ''')

    x_fplo_atom_wyckoff_idx = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atoms'],
        description='''
        Wyckoff position index of each atom
        ''')

    x_fplo_atom_cpa_block = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atoms'],
        description='''
        CPA block of each atom
        ''')

    x_fplo_structure_type = Quantity(
        type=str,
        shape=[],
        description='''
        FPLO structure type: Crystal/Molecule
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_xc_functional_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FPLO number xc functional
        ''')

    x_fplo_xc_functional = Quantity(
        type=str,
        shape=[],
        description='''
        FPLO notation of xc functional
        ''')

    x_fplo_dft_plus_u_projection_type = Quantity(
        type=str,
        shape=[],
        description='''
        FPLO notation of DFT+U projection
        ''')

    x_fplo_dft_plus_u_functional = Quantity(
        type=str,
        shape=[],
        description='''
        FPLO notation of DFT+U functional
        ''')


class HubbardModel(simulation.method.HubbardModel):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_dft_plus_u_orbital_element = Quantity(
        type=str,
        shape=[],
        description='''
        FPLO: Atom/Orbital dependent DFT+U property: element
        ''')

    x_fplo_dft_plus_u_orbital_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FPLO: Atom/Orbital dependent DFT+U property: species index
        ''')

    x_fplo_dft_plus_u_orbital_F0 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FPLO: Atom/Orbital dependent DFT+U property: value F0
        ''')

    x_fplo_dft_plus_u_orbital_F2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FPLO: Atom/Orbital dependent DFT+U property: value F2
        ''')

    x_fplo_dft_plus_u_orbital_F4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FPLO: Atom/Orbital dependent DFT+U property: value F4
        ''')

    x_fplo_dft_plus_u_orbital_F6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FPLO: Atom/Orbital dependent DFT+U property: value F6
        ''')
