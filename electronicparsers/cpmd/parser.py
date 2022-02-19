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


class CPMDParser(BasicParser):
    def __init__(self):
        re_f = r'\-*\d+\.\d+E*\-*\+*\d*'
        super().__init__(
            specifications=dict(
                name='parsers/cpmd', code_name='CPMD',
                code_homepage='https://www.lcrc.anl.gov/for-users/software/available-software/cpmd/',
                mainfile_contents_re=(r'\*\*\*       \*\*   \*\*\*  \*\* \*\*\*\* \*\*  \*\*   \*\*\*')),
            units_mapping=dict(length=ureg.bohr, energy=ureg.hartree),
            program_version=r'\*\s*VERSION\s*(\d+\.\d+.+)',
            atom_labels_atom_positions_atom_forces=r'ATOM\s*COORDINATES\s*GRADIENTS([\s\S]+?)(?:\*{50}|\n *\n)',
            atom_labels_atom_positions=r'ATOMIC COORDINATES\s*\*\s*\*+([\s\S]+?)\*{50}',
            lattice_vectors=(
                rf'(LATTICE VECTOR A1\(BOHR\):\s*{re_f}\s+{re_f}\s+{re_f}\s+)'
                rf'(LATTICE VECTOR A2\(BOHR\):\s*{re_f}\s+{re_f}\s+{re_f}\s+)'
                rf'(LATTICE VECTOR A3\(BOHR\):\s*{re_f}\s+{re_f}\s+{re_f}\s+)'),
            energy_total=rf' ETOT\s*\=\s*({re_f})|\(K\+E1\+L\+N\+X\)\s*TOTAL ENERGY\s*\=\s*({re_f})',
            energy_kinetic_electronic=rf'\(K\)\s*KINETIC ENERGY\s*=\s*({re_f})',
            energy_electrostatic=rf'\(E1\=A\-S\+R\)\s*ELECTROSTATIC ENERGY\s*=\s*({re_f})',
            energy_XC=rf'\(X\)\s*EXCHANGE\-CORRELATION ENERGY\s*=\s*({re_f})')
