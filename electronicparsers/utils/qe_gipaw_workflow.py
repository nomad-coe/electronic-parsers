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
from simulationworkflowschema import (
    SimulationWorkflowResults,
    SimulationWorkflowMethod,
    SerialSimulation,
)
from nomad_simulations.schema_packages.model_method import ModelMethod
from nomad_nmr_schema.schema_packages.schema_package import Outputs


class NMRQEResults(SimulationWorkflowResults):
    """
    Groups the NMR QE outputs.
    """

    pass


class NMRQEMethod(SimulationWorkflowMethod):
    """
    References the NMR input model method.
    """

    nmr_method_ref = Quantity(
        type=Reference(ModelMethod),
        description="""
        Reference to the NMR model method.
        """,
    )


class NMRQE(SerialSimulation):
    """
    NMR QE workflow
    """

    method = SubSection(sub_section=NMRQEMethod)

    results = SubSection(sub_section=NMRQEResults)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)



class EFGQEResults(SimulationWorkflowResults):
    """
    Groups the EFG QE outputs.
    """

    pass


class EFGQEMethod(SimulationWorkflowMethod):
    """
    References the EFG input model method.
    """

    nmr_method_ref = Quantity(
        type=Reference(ModelMethod),
        description="""
        Reference to the EFG model method.
        """,
    )


class EFGQE(SerialSimulation):
    """
    EFG QE workflow
    """

    method = SubSection(sub_section=EFGQEMethod)

    results = SubSection(sub_section=EFGQEResults)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)


class EPRHyperfineQEResults(SimulationWorkflowResults):
    """
    Groups the EPR Hyperfine QE outputs.
    """

    pass


class EPRHyperfineQEMethod(SimulationWorkflowMethod):
    """
    References the EPR Hyperfine input model method.
    """

    nmr_method_ref = Quantity(
        type=Reference(ModelMethod),
        description="""
        Reference to the EFG model method.
        """,
    )


class EPRHyperfineQE(SerialSimulation):
    """
    EPR Hyperfine QE workflow
    """

    method = SubSection(sub_section=EPRHyperfineQEMethod)

    results = SubSection(sub_section=EPRHyperfineQEResults)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)


class EPRGtensorQEResults(SimulationWorkflowResults):
    """
    Groups the EPR Hyperfine QE outputs.
    """

    pass


class EPRGtensorQEMethod(SimulationWorkflowMethod):
    """
    References the EPR Hyperfine input model method.
    """

    nmr_method_ref = Quantity(
        type=Reference(ModelMethod),
        description="""
        Reference to the EFG model method.
        """,
    )


class EPRGtensorQE(SerialSimulation):
    """
    EPR Hyperfine QE workflow
    """

    method = SubSection(sub_section=EPRGtensorQEMethod)

    results = SubSection(sub_section=EPRGtensorQEResults)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)



class GIPAWQE(SerialSimulation):
    """
    The QE-GIPAW workflow is generated in an extra EntryArchive.
    """

    def normalize(self, archive, logger):
        super().normalize(archive, logger)