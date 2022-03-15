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

import bz2
import datetime
import gzip
import lzma
import numpy as np
import logging

from nomad.units import ureg
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.method import Method, BasisSet
from nomad.datamodel.metainfo.simulation.calculation import Calculation, Forces, ForcesEntry
from nomad.parsing.file_parser import Quantity, TextParser

import xml.etree.ElementTree as ElementTree


def str_to_timestamp(s: str):
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").timestamp()


class QBallParser:

    mainfile_parser = TextParser(
        quantities=[
            Quantity(
                "atoms",
                r"symbol_ = (\w+)",
                repeats=True,
            ),
            Quantity(
                "start_time",
                r"<start_time>\s*(.*?)\s*</start_time>",
                repeats=False,
            ),
            Quantity(
                "end_time",
                r"<end_time>\s*(.*?)\s*</end_time>",
                repeats=False,
            ),
        ]
    )

    def __init__(self):
        pass

    def parse(self, mainfile, archive, logger=None):
        logger = logger if logger is not None else logging.getLogger('__name__')

        if mainfile.endswith(".gz"):
            open_file = gzip.open
        elif mainfile.endswith(".bz2"):
            open_file = bz2.open
        elif mainfile.endswith(".xz"):
            open_file = lzma.open

        with open_file(mainfile, "rt") as file:
            contents = file.read()

        self.mainfile_parser.mainfile = mainfile
        self.mainfile_parser.parse()

        run = archive.m_create(Run)
        run.program = Program(name='qball')
        run.time_run = TimeRun(
            date_start=str_to_timestamp(self.mainfile_parser.get("start_time")),
            date_end=str_to_timestamp(self.mainfile_parser.get("end_time")))

        # method
        method = run.m_create(Method)
        # TODO add dft functionals
        if "plane waves" not in contents:
            logger.error("Qball Error: Not a plane wave dft")
        else:
            basis_set = method.m_create(BasisSet)
            basis_set.type = "plane waves"

        element_tree = ElementTree.fromstring(contents)

        # system
        system = run.m_create(System)
        system.atoms = Atoms(
            labels=[atom.attrib["name"] for atom in element_tree.find("run").find("iteration").find("atomset").iter("atom")],
            positions=np.array([
                [float(pos) for pos in atom.find("position").text.split()]
                for atom in element_tree.find("run").find("iteration").find("atomset").iter("atom")]) * ureg.bohr)

        # calculation
        calculation = run.m_create(Calculation)
        calculation.forces = Forces(total=ForcesEntry(value=np.array([
            [float(force) for force in atom.find("force").text.split()]
            for atom in element_tree.find("run").find("iteration").find("atomset").iter("atom")]) * ureg.hartree / ureg.bohr))
