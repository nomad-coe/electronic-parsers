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


class Program(simulation.run.Program):
    '''
    Contains the specifications of the program.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_ocean_commit_hash = Quantity(
        type=str,
        description='''
        Commit hash label from the OCEAN git repository.
        ''')

    x_ocean_original_dft_code = Quantity(
        type=str,
        description='''
        DFT code (QuantumESPRESSO or ABINIT) used in the initial step.
        '''
    )
