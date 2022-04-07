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

import os
import logging
import numpy as np
from datetime import datetime

from nomad.parsing.file_parser import TextParser, Quantity
from nomad.units import ureg
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import Method
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, BandEnergies,
    Multipoles, MultipolesEntry, Charges, ChargesValue
)
from .metainfo import m_env  # pylint: disable=unused-import


re_f = r'[-+]?\d*\.\d*(?:[Ee][-+]\d+)?'
re_n = r'[\n\r]'
MOL = 6.02214076e+23


class MainfileParser(TextParser):
    def init_quantities(self):
        self._quantities = [
            Quantity('program_version', r'Version (\S+)', dtype=str),
            Quantity(
                'calculation',
                r'(CALCULATION DONE:[\s\S]+?)\*\*\*\*\*',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters',
                        r'([\w=]+) +\- +(.+)',
                        str_operation=lambda x: x.split(' ', 1), repeats=True
                    ),
                    Quantity(
                        'date_start',
                        r'CALCULATION DONE\: +\w+ (\w+) +(\d+ +\d+\:\d+\:\d+ \d+)',
                        flatten=False, dtype=str
                    )
                ])
            ),
            Quantity(
                'coordinates',
                rf'CARTESIAN COORDINATES\s+NO\. +ATOM +X +Y +Z\s+'
                rf'((?:\d+ +[A-Z]\w* +{re_f} +{re_f} +{re_f}\s+)+)',
                str_operation=lambda x: [v.split() for v in x.strip().splitlines()]
            ),
            Quantity(
                'x_mopac_fhof',
                rf'FINAL HEAT OF FORMATION += +({re_f}) KCAL/MOL',
                dtype=np.float64, unit=ureg.J * 4184.0 / MOL
            ),
            Quantity(
                'energy_total',
                rf'TOTAL ENERGY += +({re_f}) EV',
                dtype=np.float64, unit=ureg.eV
            ),
            Quantity(
                'energy_electronic',
                rf'ELECTRONIC ENERGY += +({re_f}) EV',
                dtype=np.float64, unit=ureg.eV
            ),
            Quantity(
                'energy_nuclear_repulsion',
                rf'CORE\-CORE REPULSION += +({re_f}) EV',
                dtype=np.float64, unit=ureg.eV
            ),
            Quantity(
                'n_filled_levels',
                r'NO\. OF FILLED LEVELS += +(\d+)', dtype=np.int32
            ),
            Quantity(
                'n_alpha_electrons',
                r'NO\. OF ALPHA +ELECTRONS += +(\d+)', dtype=np.int32
            ),
            Quantity(
                'n_beta_electrons',
                r'NO\. OF BETA +ELECTRONS += +(\d+)', dtype=np.int32
            ),
            Quantity(
                'eigenvalues',
                rf'EIGENVALUES\s+((?:{re_f}\s+)+)',
                repeats=True, dtype=np.dtype(np.float64)
            ),
            Quantity(
                'forces',
                r'FINAL +POINT +AND +DERIVATIVES\s+PARAMETER +ATOM.+\s+'
                rf'((?:\d+ +\d+ +[A-Z]\S* +CARTESIAN.+\s+)+)',
                str_operation=lambda x: np.array([v.split()[6] for v in x.strip().splitlines()], np.dtype(np.float64))
            ),
            Quantity(
                'dipole',
                rf'DIPOLE +X +Y +Z +TOTAL\s+((?:\S+ +{re_f} +{re_f} +{re_f} +{re_f}\s+)+)',
                str_operation=lambda x: [v.split() for v in x.strip().splitlines()]
            ),
            Quantity(
                'atomic_population',
                rf'ATOM NO\. +TYPE +CHARGE.+\s+((?:\d+ +[A-Z]\S* +{re_f}.+\s+)+)',
                str_operation=lambda x: [v.split() for v in x.strip().splitlines()],
            ),
            Quantity(
                'orbital_population',
                rf'ATOMIC ORBITAL ELECTRON POPULATIONS\s+(Atom.+\s+)((?:\d+ +[A-Z]\S* +{re_f}.+\s+)+)',
                str_operation=lambda x: [v.split() for v in x.strip().splitlines()]
            ),
            Quantity('spin_S2', rf'\(S\*\*2\) += +({re_f})', dtype=np.float64),
            Quantity('calculation_time', rf'COMPUTATION TIME += +({re_f}) SECONDS', dtype=np.float64, unit=ureg.s)
        ]


class MopacParser:
    def __init__(self):
        self.mainfile_parser = MainfileParser()
        self._methods = [
            'AM1', 'MNDO', 'MNDOD', 'PM3', 'PM6', 'PM6-D3', 'PM6-DH+', 'PM6-DH2',
            'PM6-DH2X', 'PM6-D3H4', 'PM6-D3H4X', 'PMEP', 'PM7', 'PM7-TS', 'RM1'
        ]

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.maindir = os.path.dirname(self.filepath)

        self.mainfile_parser.mainfile = self.filepath
        self.mainfile_parser.logger = self.logger

        sec_run = archive.m_create(Run)
        sec_run.program = Program(version=self.mainfile_parser.get('program_version'))

        date_start = self.mainfile_parser.get('calculation', {}).get('date_start')
        if date_start is not None:
            sec_run.time_run = TimeRun(
                date_start=datetime.strptime(date_start, '%b %d %H:%M:%S %Y').timestamp())

        sec_method = sec_run.m_create(Method)
        sec_method.x_mopac_calculation_parameters = {
            v[0]: v[1] for v in self.mainfile_parser.get('calculation', {}).get('parameters', [])}

        for method in self._methods:
            if method in sec_method.x_mopac_calculation_parameters:
                sec_method.x_mopac_method = method
                break

        sec_system = sec_run.m_create(System)
        sec_system.atoms = Atoms(
            labels=[v[1] for v in self.mainfile_parser.get('coordinates', [])],
            positions=[v[2:5] for v in self.mainfile_parser.get('coordinates', [])] * ureg.angstrom)

        sec_calc = sec_run.m_create(Calculation)
        sec_calc.x_mopac_fhof = self.mainfile_parser.x_mopac_fhof

        sec_calc.energy = Energy(
            total=EnergyEntry(value=self.mainfile_parser.energy_total),
            electronic=EnergyEntry(value=self.mainfile_parser.energy_electronic),
            nuclear_repulsion=EnergyEntry(value=self.mainfile_parser.energy_nuclear_repulsion)
        )

        forces = self.mainfile_parser.forces
        if forces is not None:
            sec_calc.forces = Forces(total=ForcesEntry(
                value=np.reshape(forces, (len(sec_system.atoms.labels), 3)) * ureg.J * 4184.0 / ureg.angstrom / MOL)
            )

        eigenvalues = self.mainfile_parser.eigenvalues
        if eigenvalues is not None:
            occupied = [self.mainfile_parser.n_filled] if len(eigenvalues) == 1 else [
                self.mainfile_parser.n_alpha_electrons, self.mainfile_parser.n_beta_electrons]
            occupations = np.zeros(np.shape(eigenvalues))
            for spin, max_occupied in enumerate(occupied):
                occupations[spin, 0:max_occupied] = 2 // len(occupied)
            sec_eigenvalues = sec_calc.m_create(BandEnergies)
            # only Gamma-point calculation
            sec_eigenvalues.kpoints = np.zeros((1, 3))
            shape = (len(eigenvalues), 1, len(eigenvalues[0]))
            sec_eigenvalues.energies = np.reshape(eigenvalues, shape) * ureg.eV
            sec_eigenvalues.occupations = np.reshape(occupations, shape)

        dipole = self.mainfile_parser.dipole
        if dipole is not None:
            sec_multipoles = sec_calc.m_create(Multipoles)
            sec_multipoles.dipole = MultipolesEntry(total=dipole[-1][-1])

        atomic_population = self.mainfile_parser.atomic_population
        if atomic_population is not None:
            sec_charges = sec_calc.m_create(Charges)
            # atom projections
            sec_charges.value = [c[3] for c in atomic_population] * ureg.elementary_charge
            orbital_population = self.mainfile_parser.get('orbital_population')
            if orbital_population is not None:
                # orbital labels
                orbitals = orbital_population[0][1:]
                for n_atom, atom in enumerate(orbital_population[1:]):
                    for n_orb, value in enumerate(atom[2:]):
                        # orbital projections
                        sec_charges.orbital_projected.append(ChargesValue(
                            orbital=orbitals[n_orb], value=value * ureg.elementary_charge,
                            atom_index=n_atom, atom_label=atom[1]))

        sec_calc.spin_S2 = self.mainfile_parser.spin_S2
        sec_calc.time_calculation = self.mainfile_parser.time_calculation

        sec_calc.system_ref = sec_system
