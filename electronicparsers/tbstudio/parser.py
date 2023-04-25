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

import os
import logging
import numpy as np

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms, AtomsGroup
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, AtomParameters, KMesh, Projection
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Dos, BandStructure, BandEnergies, Energy, HoppingMatrix
)
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint


class TBStudioParser:
    level = 1

    def __init__(self):
        self._calculation_type = 'projection'

    def parse_system(self):
        """Populates run.system with the input structural parameters.
        """
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)
        # Here the key is to populate:
        #   1- `Atoms` with the main quantities I wrote
        #   2- `AtomsGroup` (optional) with the info of the atoms used for the projection in the tight-binding model
        sec_atoms = sec_system.m_create(Atoms)
        # sec_atoms.lattice_vectors = ...
        # sec_atoms.lattice_vectors_reciprocal = ...
        # pbc = [True, True, True] if lattice_vectors is not None else [False, False, False]
        # sec_atoms.periodic = pbc
        # sec_atoms.labels = ...
        # sec_atoms.positions = ...

    def parse_method(self):
        """Populates run.method with the input methodological parameters.
        """
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        # Here it will be useful to populate `AtomParameters` within Method to account, for
        # example, for the orbitals used in the projeciton

    def parse_scc(self):
        """Populates run.calculation with the output of the calculation.
        """
        sec_run = self.archive.run[-1]

        # The objective here is to populate outputed metainfo, mainly, band structures, eigenvalues,
        # dos, hopping matrices, and everything you think is valuable.

    def init_parser(self):
        """Initialize the parsers.
        """
        pass

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        self.init_parser()

        self.parse_system()
        self.parse_method()
        self.parse_scc()

        workflow = SinglePoint()
        self.archive.workflow2 = workflow
