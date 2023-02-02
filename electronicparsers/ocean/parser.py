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


class OutParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'program_version', r'\s*Version\s*([0-9.]+)',
                dtype=str, flatten=False),
            Quantity(
                'commit_hash', r'\s*commit hash:\s*(\w+)'
            )
        ]


class InParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'acell', r'[\n\r]acell\s*\{\s*([\d\.\s]+)\s*\}', repeats=False),
            Quantity(
                'rprim', r'[\n\r]rprim\s*\{([\s\S]+?)(?:[\n\r]\s*\}[\n\r]ntypat)', repeats=False),
            Quantity(
                'znucl', r'[\n\r]znucl\s*\{\s*([\d\s]+)\s*\}', repeats=False),
            Quantity(
                'typat', r'[\n\r]typat\s*\{\s*([\d\s]+)\s*\}', repeats=False)
            # Quantity(
            #    'xred')
        ]


class OceanParser:
    def __init__(self):
        self._calculation_type = 'bse'
        self.out_parser = OutParser()
        self.in_parser = InParser()

    def parse_system(self):
        sec_run = self.archive.run[-1]
        if not self.in_parser.mainfile:
            return
        sec_atoms = sec_run.m_create(System).m_create(Atoms)

        # System in the input file in ABINIT style
        acell = self.in_parser.get('acell', None)
        rprim = np.reshape(self.in_parser.get('rprim', None), (3, 3))
        if acell and rprim:
            sec_atoms.lattice_vectors = acell[:] * rprim[:] * ureg.bohr
            sec_atoms.periodic = [acell[:] * rprim[:] is not None] * 3

        znucl = self.in_parser.get('znucl', None)
        typat = self.in_parser.get('typat', None)
        if znucl and typat:
            sec_atoms.labels = [chemical_symbols[int(znucl[n_at - 1])] for n_at in typat]
        # xred = self.in_parser.get('xred', [])
        # if xred:
            # sec_atoms.positions = ...

    def parse_method(self):
        pass

    def parse_scc(self):
        pass

    def parse(self, filepath, archive, logger, **kwargs):
        self.filepath = filepath
        self.maindir = os.path.dirname(self.filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging

        in_files = [f for f in os.listdir(self.maindir) if f.endswith('.in')]
        if len(in_files) > 0:
            if len(in_files) > 1:
                self.logger.warning('Found more than one input files -> using the first one in the parser. '
                                    'Please, check it out!')
            self.in_parser.mainfile = os.path.join(self.maindir, in_files[0])

        sec_run = self.archive.m_create(Run)

        # Program
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'OCEAN'
        sec_program.version = self.out_parser.get('program_version', '')
        sec_program.x_ocean_commit_hash = self.out_parser.get('commit_hash', '')

        # System
        self.parse_system()

        # Method
        self.parse_method()

        # Calculation
        self.parse_scc()

        # Workflow
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
