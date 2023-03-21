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
    MSection, Package, Quantity, Section, SubSection
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_wannier90_n_atoms_proj = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Number of atoms used in the Wannier90 projection.
        ''')

    x_wannier90_units = Quantity(
        type=str,
        shape=[],
        description='''
        Optional. Either Ang or Bohr to specify whether the projection centres specified
        in this block (if given in Cartesian co-ordinates) are in units of Angstrom or
        Bohr, respectively. The default value is Ang.
        ''')
