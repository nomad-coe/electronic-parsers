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
import os
import numpy as np

from simulationparsers.utils import BasicParser
from nomad.units import ureg
from nomad.utils import get_logger
from nomad.parsing.file_parser import Quantity, TextParser, Parser
from runschema.system import System, Atoms
from runschema.calculation import Calculation
from runschema.method import (
    Method,
    DFT,
    Electronic,
    DMFT,
)
from ase.io import read as ase_read
from nomad.normalizing.common import nomad_atoms_from_ase_atoms


class MethodParser(TextParser):
    def __init__(self):
        self.method = None
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'method',
                r'\s*Initialization of the (\w+) code\s*\n',
                comment='#',
                repeats=True,
            ),
            Quantity(
                'temperature',
                r'\s*Readin: Setting the temperature to\s+([+-]?\d+\.\d+E[+-]?\d+)\s*\n',
                comment='#',
                repeats=False,
            ),
        ]


class RSPtParser(Parser):
    def __init__(self, **kwargs) -> None:
        self._method_parser = MethodParser()
        super().__init__(**kwargs)

        self._parser = BasicParser(
            'RSPt',
            program_version=r'RSPt version number:\s*rspt\.(\d+\.\d+)',
        )

    def parse(self, mainfile, archive, logger=None):
        logger = logger if logger is not None else get_logger(__name__)
        self._method_parser.logger = logger
        self._method_parser.mainfile = mainfile
        self.mainfile = mainfile
        self._maindir = os.path.dirname(self.mainfile)
        self._auxillary_files = os.listdir(self._maindir)

        self._parser.parse(mainfile, archive, logger=None)

        # PARSE METHOD
        method = self._method_parser.get('method', '')
        temperature = self._method_parser.get('temperature', None)
        # TODO - check rspt units - inverse T has temp units?
        temperature = temperature * ureg.kelvin if temperature else None
        inverse_temperature = (
            1.0 / (ureg.boltzmann_constant * temperature) if temperature else None
        )
        if all(m.upper() == 'DFT' for m in method):
            archive.run[0].method.append(
                Method(dft=DFT(), electronic=Electronic(method='DFT'))
            )
        elif all(m.upper() == 'DMFT' for m in method):
            archive.run[0].method.append(
                Method(dmft=DMFT(inverse_temperature=inverse_temperature))
            )
        else:
            logger.warning(
                'RSPtParser method not recognized, or multiple distinct methods found.'
            )

        # PARSE SYSTEM
        cif_files = [f for f in self._auxillary_files if f.endswith('.cif')]
        if cif_files:
            if len(cif_files) > 1:
                self.logger.warning(
                    'RSPtParser found multiple CIF files, using the first one found.'
                )
            ase_atoms = ase_read(f'{self._maindir}/{cif_files[0]}', format='cif')
            nomad_atoms = nomad_atoms_from_ase_atoms(ase_atoms)
            archive.run[0].system.append(
                System(
                    atoms=Atoms(
                        atomic_numbers=nomad_atoms.atomic_numbers,
                        species=nomad_atoms.species,
                        labels=nomad_atoms.labels,
                        positions=nomad_atoms.positions,
                        lattice_vectors=nomad_atoms.lattice_vectors,
                        periodic=nomad_atoms.periodic,
                    ),
                )
            )

        # PARSE CALCULATION
        sec_method = archive.run[0].method[0] if archive.run[0].method else None
        sec_system = archive.run[0].system[0] if archive.run[0].system else None
        archive.run[0].calculation.append(
            Calculation(
                system_ref=sec_system,
                method_ref=sec_method,
                temperature=temperature,
            )
        )
