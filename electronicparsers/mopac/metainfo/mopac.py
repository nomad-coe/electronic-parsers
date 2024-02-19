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
import numpy as np  # pylint: disable=unused-import
import typing  # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection,
    MCategory,
    Category,
    Package,
    Quantity,
    Section,
    SubSection,
    SectionProxy,
    Reference,
    JSON,
)
import runschema.run  # pylint: disable=unused-import
import runschema.calculation  # pylint: disable=unused-import
import runschema.method  # pylint: disable=unused-import
import runschema.system  # pylint: disable=unused-import


m_package = Package()


class Calculation(runschema.calculation.Calculation):
    m_def = Section(validate=False, extends_base_section=True)

    x_mopac_fhof = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit="joule",
        description="""
        Final heat of formation
        """,
    )


class Method(runschema.method.Method):
    m_def = Section(validate=False, extends_base_section=True)

    x_mopac_keyword_line = Quantity(
        type=str,
        shape=[],
        description="""
        Mopac keyword line (it controls the calculation)
        """,
    )

    x_mopac_method = Quantity(
        type=str,
        shape=[],
        description="""
        Mopac method, i.e. PM7, AM1, etc..
        """,
    )

    x_mopac_calculation_parameters = Quantity(
        type=JSON,
        shape=[],
        description="""
        """,
    )
