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
import json
import os
import logging
from ase.data import chemical_symbols

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, XMLParser, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Method, DFT, Electronic, Smearing, XCFunctional, Functional,
    GW as GWMethod, Scf, BasisSet, KMesh
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Dos, DosValues, BandStructure, BandEnergies, Energy, EnergyEntry, Charges,
    Forces, ForcesEntry, ScfIteration, BandGap
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization, Task, GW as GWWorkflow
from nomad.datamodel.metainfo.workflow2 import TaskReference, Link
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2, GeometryOptimization as GeometryOptimization2,
    GeometryOptimizationMethod, GW as GW2, GWResults
)


class OceanParser:
    def __init__(self):
        self._calculation_type = 'bse'
        self._dft_code_map = {
            'qe': 'QuantumESPRESSO',
            'abi': 'ABINIT'
        }

    def parse_system(self, data):
        sec_run = self.archive.run[-1]
        sec_atoms = sec_run.m_create(System).m_create(Atoms)

        if data.get('avecs'):
            sec_atoms.lattice_vectors = data.get('avecs')
            sec_atoms.periodic = [data.get('avecs')[:] is not None] * 3
            sec_atoms.lattice_vectors_reciprocal = data.get('bvecs')

        if data.get('znucl') and data.get('typat'):
            sec_atoms.labels = [chemical_symbols[int(data.get('znucl')[n_at - 1])] for n_at in data.get('typat')]
            sec_atoms.positions = data.get('xangst') * ureg.angstrom

    def parse_method(self, data):
        pass

    def parse_scc(self, data):
        pass

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.maindir = os.path.dirname(self.filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging

        try:
            data = json.load(open(self.filepath))
        except Exception:
            self.logger.error('Error opening json output file.')
            data = None

        sec_run = self.archive.m_create(Run)

        # Program
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'OCEAN'
        sec_program.version = data['version'].get('.')
        sec_program.x_ocean_commit_hash = data['version'].get('hash')
        sec_program.x_ocean_original_dft_code = self._dft_code_map.get(data['dft'].get('program'))

        # System
        self.parse_system(data['structure'])

        # Method
        self.parse_method(data)

        # Calculation
        self.parse_scc(data)

        # Workflow
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
