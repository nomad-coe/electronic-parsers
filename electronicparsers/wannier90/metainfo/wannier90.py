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
import numpy as np

from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference, MEnum, JSON
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_wannier90_hopping_parameters(MSection):
    '''
    Section containing the Wannier90 hopping parameters
    '''

    m_def = Section(validate=False)

    nrpts = Quantity(
        type=np.dtype(np.int32),
        description='''
        Number of Wigner-Seitz real points.
        ''')

    degeneracy_factors = Quantity(
        type=np.dtype(np.int32),
        shape=['nrpts'],
        description='''
        Degeneracy of each Wigner-Seitz grid point.
        ''')

    hopping_matrix = Quantity(
        type=np.dtype(np.float64),
        shape=['nrpts', 7],
        description='''
        Real space hopping matrix for each Wigner-Seitz grid point. The elements are
        defined as follows:
            n_x   n_y   n_z   orb_1   orb_2   real_part   imag_part
        where (n_x, n_y, n_z) define the Wigner-Seitz cell vector in fractional coordinates,
        (orb_1, orb_2) indicates the hopping amplitude between orb_1 and orb_2, and the
        real and imaginary parts of the hopping in electron_volt.
        ''')


class Atoms(simulation.system.Atoms):

    m_def = Section(validate=False, extends_base_section=True)

    x_wannier90_units = Quantity(
        type=str,
        shape=[],
        description='''
        Optional. Either Ang or Bohr to specify whether the projection centres specified
        in this block (if given in Cartesian co-ordinates) are in units of Angstrom or
        Bohr, respectively. The default value is Ang.
        ''')

    x_wannier90_site = Quantity(
        type=str,
        shape=[],
        description='''
        C, Al, etc. applies to all atoms of that type.
        f=0,0.50,0, centre on (0.0,0.5,0.0) in f ractional coordinates (crystallographic
            units) relative to the direct lattice vectors.
        c=0.0,0.805,0.0, centre on (0.0,0.805,0.0) in Cartesian coordinates in units
            specified by the optional string units in the first line of the projections block
            (see above).
        ''')

    x_wannier90_ang_mtm = Quantity(
        type=str,
        shape=[],
        description='''
        Angular momentum states may be specified by l and mr, or by the appropriate
        character string.Examples:
        l=2,mr=1 or dz2, a single projection with l = 2, m r = 1 (i.e., d z 2 )
        l=2,mr=1,4 or dz2,dx2-y2, two functions: d z 2 and d xz
        l=-3 or sp3, four sp 3 hybrids
        Specific hybrid orbitals may be specified as follows:
        l=-3,mr=1,3 or sp3-1,sp3-3, two specific sp 3 hybrids
        Multiple states may be specified by separating with ;, e.g.,
        sp3;l=0 or l=-3;l=0, four sp 3 hybrids and one s orbital
        ''')

    x_wannier90_zaxis = Quantity(
        type=np.int32,
        shape=[3],
        description='''
        Z axis direction. Default=[0, 0, 1].
        ''')

    x_wannier90_xaxis = Quantity(
        type=np.int32,
        shape=[3],
        description='''
        X axis direction. Default=[1, 0, 0].
        ''')

    x_wannier90_radial = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Use a radial function with one node (ie second highest pseudostate with that
        angular momentum). Default is r=1. Radial functions associated with different
        values of r should be orthogonal to each other.
        ''')

    x_wannier90_zona = Quantity(
        type=np.float64,
        shape=[],
        description='''
        The value of Za for the radial part of the atomic orbital (controls the diffusivity
        of the radial function). Units always in reciprocal Angstrom. Default is zona=1.0.
        ''')
