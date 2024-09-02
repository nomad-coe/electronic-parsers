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
from nomad.metainfo import SubSection, Quantity, Reference
from runschema.method import Method
from simulationworkflowschema import (
    SimulationWorkflowResults,
    SimulationWorkflowMethod,
    SerialSimulation,
)


class NMRMagResResults(SimulationWorkflowResults):
    """
    Groups the NMR magres outputs.
    """

    pass


class NMRMagResMethod(SimulationWorkflowMethod):
    """
    References the NMR (first principles) input methodology.
    """

    nmr_method_ref = Quantity(
        type=Reference(Method),
        description="""
        Reference to the NMR (first principles) methodology.
        """,
    )


class NMRMagRes(SerialSimulation):
    """
    The NMR MagRes workflow is generated in an extra EntryArchive IF both the NMR (first
    principles) and the NMR magres SinglePoint EntryArchives are present in the
    upload.
    """

    method = SubSection(sub_section=NMRMagResMethod)

    results = SubSection(sub_section=NMRMagResResults)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
