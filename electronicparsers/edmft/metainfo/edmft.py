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
    MSection,
    Package,
    Quantity,
    Section,
    SubSection,
    JSON,
)
import runschema.run  # pylint: disable=unused-import
import runschema.calculation  # pylint: disable=unused-import
import runschema.method  # pylint: disable=unused-import
import runschema.system  # pylint: disable=unused-import


m_package = Package()


class x_edmft_method_parameters(MSection):
    """
    Section grouping the different input method parameters.
    """

    m_def = Section(validate=False)

    x_edmft_general = Quantity(
        type=JSON,
        description="""
        General input parameters for the calculation.
        """,
    )

    x_edmft_impurity_solver = Quantity(
        type=JSON,
        description="""
        Impurity solver parameters as defined in the dictionary 'iparams0'.
        """,
    )

    x_edmft_maxent = Quantity(
        type=JSON,
        description="""
        MaxEnt parameters used to perform the analytical continuation.
        """,
    )


class Method(runschema.method.Method):
    """
    Section containing the various parameters that define the theory and the
    approximations (convergence, thresholds, etc.) behind the calculation.
    """

    m_def = Section(validate=False, extends_base_section=True)

    x_edmft_method = SubSection(
        sub_section=x_edmft_method_parameters.m_def, repeats=False
    )


class GreensFunctions(runschema.calculation.GreensFunctions):
    """
    Section containing the code-specific output GreensFunction quantities.
    """

    m_def = Section(validate=False, extends_base_section=True)

    x_edmft_self_energy_infinity = Quantity(
        type=np.float64,
        shape=['n_correlated_orbitals'],
        description="""
        Self-energy function used to calculate the analytically continuated auxiliary
        function via the formula:
            Gc (iw) = 1 / (iw - Sigma + s_oo)
        where s_oo is the parsed function.
        """,
    )
