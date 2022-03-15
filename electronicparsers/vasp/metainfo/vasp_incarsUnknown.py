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
from . import vasp_incars
from . import vasp_incarsOut
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_vasp_incarUnknown_param(MCategory):
    '''
    Unknown incar parameters.  By 'unknown' we refer to incar parameters in the OLD
    (predated Sept.2019) 'vasp.nomadmetainfo.json' that are **not** listed in the current
    (Oct.2019) VaspWiki
    '''

    m_def = Category()


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_vasp_incarOut_ENMAX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Maximum cutoff (normally specified only in POTCAR). Value prinded out after
        evaluating the input.
        ''',
        categories=[vasp_incarsOut.x_vasp_incarOut_param])

    x_vasp_incar_ENMAX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Maximum cutoff (normally specified only in POTCAR). Value prinded out after
        evaluating the input.
        ''',
        categories=[vasp_incars.x_vasp_incar_param])

    x_vasp_incarOut_LCOMPAT = Quantity(
        type=bool,
        shape=[],
        description='''
        In vasp.4.2 the augmentation charges are forced to be zero at the boundary of the
        augmentation sphere, therefore results are slightly different from vasp.3.2
        (usually differences are smaller than 0.01 meV). The old behavior can be restored
        by setting LCOMPAT = .TRUE. in the INCAR file.
        ''',
        categories=[vasp_incarsOut.x_vasp_incarOut_param])
