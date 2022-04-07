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

from nomad.parsing.file_parser import BasicParser
from nomad.units import ureg


class CharmmParser:
    def __init__(self):
        re_f = r'\-*\d+\.\d+E*e*\-*\+*\d*'

        def get_positions(val):
            res = dict(atom_labels=[], atom_positions=[])
            try:
                labels, positions = zip(*re.findall(rf'([A-Z])\w* +({re_f} +{re_f} +{re_f}) +\w', val))
                res['atom_labels'] = labels
                res['atom_positions'] = np.array([v.split() for v in positions], dtype=np.dtype(np.float64)) * ureg.angstrom
            except Exception:
                pass
            return res

        self._parser = BasicParser(
            'Charmm',
            units_mapping=dict(length=ureg.angstrom, energy=ureg.J * 4184.0 / 6.02214076e+23),
            auxilliary_files=r'\/*([a-z][\w\-]+.crd)',
            program_version=r'\(CHARMM\) \- (.+Version[\w \,]+?\d\d\d\d)',
            atom_labels_atom_positions=(
                rf'(\*.*\s*\*.*\s*\*.*\s*\d+\n +\d+ +\d+ +\w+ +[A-Z]\w* +{re_f} +{re_f} +{re_f}[\s\S]+)(?:\>|\Z|\n *\n)',
                get_positions),
            energy_total=rf'\n *[A-Z]+\> +\d* +({re_f})')

    def parse(self, mainfile, archive, logger=None):
        self._parser.parse(mainfile, archive, logger=None)
