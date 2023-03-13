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
from nomad.datamodel.datamodel import EntryArchive
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.metainfo.metainfo import MSection, Quantity as mQuantity
from nomad.parsing.file_parser.text_parser import TextParser, ParsePattern, Quantity
import re
from typing import Union, List


class QuantityToArchive(Quantity):
    '''A quantity that can be written to the archive.'''
    floating_point_number: str = r'[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
    repeated_section_pattern = re.compile(r'(\w+)\[?(-?[\d\*]*)\]?$')

    def __init__(self, archive: EntryArchive, quantity: str,
                 re_pattern: Union[str, ParsePattern], **kwargs):
        self.archive = archive
        self.quantity_path = quantity
        self.path = self.quantity_path.split('/')
        self.section_path = self.path[:-1]
        self.section_path_limit = len(self.section_path) - 1

        self.quantity = Quantity(self.path[-1], re_pattern, **kwargs)

    def is_planned(self, section, property_name: str):
        '''Return a quantity or subsection `property_name` of `section`
        if the schema allows it.'''
        try:
            section_def = section.m_def
            subsection = section.m_def.all_properties[property_name]
        except AttributeError:
            return
        if isinstance(section_def, MSection) and isinstance(subsection, (MSection, mQuantity)):
            return subsection

    def update(self, val_in: List[str]) -> None:
        '''Write a quantity to the archive.'''
        array_index: str = ''
        head = self.archive  # traces the Archive Section in the loop

        for next_section_name in self.section_path:
            # process path string
            next_section_matched = self.__class__.repeated_section_pattern.match(next_section_name)
            next_section_name = next_section_matched.group(1)
            try:
                array_index = next_section_matched.group(2)
            except Exception:
                pass
            next_section_value = getattr(head, next_section_name)

            # check if the next section is already defined
            if not next_section_value:
                # add section, in line with the schema
                next_section = self.is_planned(head, next_section_name)
                if next_section:
                    updated_section = next_section.sub_section.section_cls()
                    updated_section = [updated_section] if array_index in ['0', '-1'] else updated_section
                    setattr(head, next_section_name, updated_section)
                    head = updated_section[0] if array_index in ['0', '-1'] else updated_section
                else:
                    raise(ValueError(f'Path {self.quantity_path} does not follow the schema.'))
        setattr(head, self.quantity.name, self.quantity.to_data(val_in))

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
