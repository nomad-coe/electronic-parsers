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

from nomad.units import ureg
from nomad.parsing.file_parser import BasicParser


class ElkParser(BasicParser):
    def __init__(self):
        re_f = r'\-*\d+\.\d+E*\-*\+*\d*'

        def get_positions(val):
            labels, positions = [], []
            for line in val.split('\n'):
                species = re.search(r'Species *\:\s*\d+ \((\w+)\)', line)
                if species:
                    label = species.group(1)
                    continue
                position = re.search(rf'\d+\s*\:\s*({re_f} +{re_f} +{re_f})', line)
                if position:
                    labels.append(label)
                    positions.append([float(v) for v in position.group(1).split()])
            return dict(atom_labels=labels, atom_positions_scaled=positions)

        super().__init__(
            specifications=dict(
                name='parsers/elk', code_name='elk', code_homepage='http://elk.sourceforge.net/',
                mainfile_contents_re=r'\| Elk version [0-9.a-zA-Z]+ started \|'),
            units_mapping=dict(length=ureg.bohr, energy=ureg.hartree),
            program_version=r'Elk version ([\d\.]+) started',
            lattice_vectors=r'Lattice vectors\s*\:\s*([\s\S]+?)\n *\n',
            atom_labels_atom_positions_scaled=(
                r'(Species *\: *\d+ [\s\S]+?Total number of atoms per unit cell.+)',
                get_positions),
            # these are scf values but we write it on scc because we dont want to
            # further complicate the parser by adding a wrapper function
            energy_reference_fermi=(rf'\n *Fermi\s*\:\s*({re_f})', lambda x: [x]),
            energy_total=rf'\n *total energy\s*\:\s*({re_f})',
            energy_sum_eigenvalues=rf'\n *sum of eigenvalues\s*\:\s*({re_f})',
            energy_kinetic_electronic=rf'\n *electron kinetic\s*\:\s*({re_f})',
            energy_correction_hartree=rf'\n *Hartree\s*\:\s*({re_f})',
            energy_correlation=rf'\n *correlation\s*\:\s*({re_f})',
            energy_exchange=rf'\n *exchange\s*\:\s*({re_f})')
