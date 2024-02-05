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
from simulationparsers.utils import BasicParser


class FploParser:
    def __init__(self):
        re_f = r'\-*\d+\.\d+E*\-*\+*\d*'

        self._parser = BasicParser(
            'fplo',
            units_mapping=dict(length=ureg.bohr, energy=ureg.eV),
            program_version=r'main version\:\s*(\S+)[\|\s]+sub  version\:\s*(\S+)[\|\s]+release\s*\:\s*(\S+)',
            lattice_vectors=r'lattice vectors\s*(a1\s*\:\s*[\s\S]+?)rec',
            atom_labels_atom_positions=rf'No\. *Element WPS CPA\-Block *X *Y *Z([\s\S]+?)\n *\n',
            energy_reference_fermi=(rf'Fermi energy\:\s*({re_f}).+electrons', lambda x: [x]),
            energy_total=rf'total energy.+\s*EE\:\s*({re_f})'
        )

    def parse(self, mainfile, archive, logger=None):
        self._parser.parse(mainfile, archive, logger=None)
