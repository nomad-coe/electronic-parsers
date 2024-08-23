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
from runschema.run import Run, Program, TimeRun
from runschema.system import System, Atoms
from runschema.method import Method, BasisSet, BasisSetContainer
from runschema.calculation import Calculation, Forces, ForcesEntry
from nomad.parsing.file_parser import Quantity, TextParser
from .metainfo import qball  # pylint: disable=unused-import

from xml.etree import ElementTree


def str_to_timestamp(s: str):
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').timestamp()


class QBallParser:
    mainfile_parser = TextParser(
        quantities=[
            Quantity(
                'atoms',
                r'symbol_ = (\w+)',
                repeats=True,
            ),
            Quantity(
                'start_time',
                r'<start_time>\s*(.*?)\s*</start_time>',
                repeats=False,
            ),
            Quantity(
                'end_time',
                r'<end_time>\s*(.*?)\s*</end_time>',
                repeats=False,
            ),
        ]
    )

    def __init__(self):
        pass

    def parse(self, mainfile, archive, logger=None):
        logger = logger if logger is not None else logging.getLogger('__name__')

        if mainfile.endswith('.gz'):
            open_file = gzip.open
        elif mainfile.endswith('.bz2'):
            open_file = bz2.open
        elif mainfile.endswith('.xz'):
            open_file = lzma.open

        with open_file(mainfile, 'rt') as file:
            contents = file.read()

        self.mainfile_parser.mainfile = mainfile
        self.mainfile_parser.parse()

        run = Run()
        archive.run.append(run)
        run.program = Program(name='qball')
        run.time_run = TimeRun(
            date_start=str_to_timestamp(self.mainfile_parser.get('start_time')),
            date_end=str_to_timestamp(self.mainfile_parser.get('end_time')),
        )

        # method
        method = Method()
        run.method.append(method)
        # TODO add dft functionals
        if 'plane waves' in contents:
            method.electrons_representation = [
                BasisSetContainer(
                    type='plane waves',
                    scope=['wavefunction'],
                    basis_set=[
                        BasisSet(
                            type='plane waves',
                            scope=['valence'],
                        )
                    ],
                )
            ]
        else:
            logger.error('Qball Error: Not a plane wave dft')

        element_tree = ElementTree.fromstring(contents)

        # system
        system = System()
        run.system.append(system)
        system.atoms = Atoms(
            labels=[
                atom.attrib['name']
                for atom in element_tree.find('run')
                .find('iteration')
                .find('atomset')
                .iter('atom')
            ],
            positions=np.array(
                [
                    [float(pos) for pos in atom.find('position').text.split()]
                    for atom in element_tree.find('run')
                    .find('iteration')
                    .find('atomset')
                    .iter('atom')
                ]
            )
            * ureg.bohr,
        )

        # calculation
        calculation = Calculation()
        run.calculation.append(calculation)
        calculation.forces = Forces(
            total=ForcesEntry(
                value=np.array(
                    [
                        [float(force) for force in atom.find('force').text.split()]
                        for atom in element_tree.find('run')
                        .find('iteration')
                        .find('atomset')
                        .iter('atom')
                    ]
                )
                * ureg.hartree
                / ureg.bohr
            )
        )
