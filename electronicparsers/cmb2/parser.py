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
import logging
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.metainfo.metainfo import Quantity
from nomad.parsing.file_parser.text_parser import TextParser, Quantity

separator_line = r'[\-\s]+\n'
vector_3D = r'([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)'

lattice_section = Quantity('lattice_section',
        r'lattice vectors (a.u.)\n[\s\S]+?\n\n',
        sub_parser=TextParser(quantities=[
            Quantity('lattice_vectors', vector_3D, repeats=True),
        ])
    )
rep_latt_section = Quantity('rep_latt_section',
        r'reciprocal basis (a.u.)\n[\s\S]+?\n\n',
        sub_parser=TextParser(quantities=[
            Quantity('reciprocal_lattice_vectors', vector_3D, repeats=True),
        ])
    )
atoms_coords = Quantity('atoms_coords',
        r'Atomic Positions:\n[\s\S]+?\n(.*)\nThe crystal system',
        sub_parser=TextParser(quantities=[
            Quantity('labels', r'([A-Z][a-z]?) #', repeats=True, dtype=str),
            Quantity('positions', r'\d+:\s+' + vector_3D, repeats=True),
            ])
    )
program = Quantity('program', r'(^\s*CMB2\s+Version:.+)', sub_parser=\
    TextParser(quantities=[
        Quantity('version', r'Version:\s+([\d\.]+)', dtype=str),
    ]))
run = Quantity('run', r'^(\s*CMB2\s+Version:[\s\S]+?)\Z', repeats=True,
        sub_parser=TextParser(quantities=[program])
    )

class CMB2Parser():
    ''''''
    def __init__(self):
        self.parser = TextParser(quantities=[run])
        # self.parser._msections_map = {'run': Run, 'program': Program}

    def parse(self, filepath, archive, logger):
        '''Parse a CMB2 file.'''
        self.parser.mainfile = filepath
        archive.m_create(Run).m_create(Program)
        self.parser.write_to_archive(archive)
