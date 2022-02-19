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

from nomad.units import ureg
from nomad.parsing.file_parser import BasicParser


class Dmol3Parser(BasicParser):
    def __init__(self):
        re_f = r'\-*\d+\.\d+E*\-*\+*\d*'

        super().__init__(
            specifications=dict(
                name='parsers/dmol', code_name='DMol3',
                code_homepage='http://dmol3.web.psi.ch/dmol3.html', domain='dft',
                mainfile_name_re=r'.*\.outmol',
                mainfile_contents_re=r'Materials Studio DMol\^3'),
            units_mapping=dict(length=ureg.bohr, energy=ureg.hartree),
            program_version=r'Materials Studio DMol\^3 (version \S+)',
            atom_labels_atom_positions=r'ATOMIC  COORDINATES \(au\) +DERIVATIVES \(au\)([\s\S]+?)\n *\n',
            energy_total=rf'Total E \(au\).+\s*\-+\s*Ef +({re_f}).+\s*\-+')
