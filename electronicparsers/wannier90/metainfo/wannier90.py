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
