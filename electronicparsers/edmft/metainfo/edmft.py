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
    MSection, Package, Quantity, Section, SubSection, JSON
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class Method(simulation.method.Method):
    '''
    Section containing the various parameters that define the theory and the
    approximations (convergence, thresholds, etc.) behind the calculation.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_edmft_general_parameters = Quantity(
        type=JSON,
        description='''
        General input parameters for the calculation.
        ''')

    x_edmft_impurity_solver_parameters = Quantity(
        type=JSON,
        description='''
        Impurity solver parameters as defined in the dictionary 'iparams0'.
        ''')
