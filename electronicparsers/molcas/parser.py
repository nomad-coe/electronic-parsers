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

import re
import numpy as np

from nomad.units import ureg
from nomad.parsing.file_parser import BasicParser


class MolcasParser(BasicParser):
    def __init__(self):
        re_f = r'\-*\d+\.\d+E*e*\-*\+*\d*'

        def get_positions(val):
            try:
                labels, positions = zip(*re.findall(rf'\d+ +([A-Z][a-z]*)\d* +({re_f} +{re_f} +{re_f})', val))
                positions = np.array([v.split() for v in positions], dtype=np.dtype(np.float64)) * ureg.angstrom
            except Exception:
                labels, positions = [], []
            return dict(atom_labels=labels, atom_positions=positions)

        super().__init__(
            specifications=dict(
                name='parsers/molcas', code_name='MOLCAS', code_homepage='http://www.molcas.org/',
                domain='dft', mainfile_contents_re=r'M O L C A S'),
            units_mapping=dict(length=ureg.bohr, energy=ureg.hartree),
            # include code name to distinguish gamess and firefly
            program_version=r'version ([\d\.]+ patchlevel \d+)',
            atom_labels_atom_positions=(r'No\. +Label +X +Y +Z\s*([\s\S]+?)\n *\n', get_positions),
            energy_total=rf'Total.* energy *\:*\=* *({re_f})')
