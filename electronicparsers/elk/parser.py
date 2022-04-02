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

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Method, BasisSet, DFT, XCFunctional, Functional, Electronic, Smearing
)
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Charges, ScfIteration, Energy, EnergyEntry, BandEnergies, Dos, DosValues
)
from .metainfo import m_env  # pylint: disable=unused-import


re_f = r'[-+]?\d*\.\d*(?:[Ee][-+]\d+)?'
re_n = r'[\n\r]'


class EigenvalParser(TextParser):
    def init_quantities(self):
        self._quantities = [
            Quantity('n_kpoints', r'(\d+) *\: *nkpt', dtype=np.int32),
            Quantity('n_states', r'(\d+) *\: *nstsv', dtype=np.int32),
            Quantity(
                'kpoint',
                rf'\d+ +({re_f}) +({re_f}) +({re_f}) +\: k\-point',
                repeats=True, dtype=np.dtype(np.float64)
            ),
            Quantity(
                'eigenvalue_occupancy',
                rf'state, eigenvalue and occupancy below\)\s+((?:\d+ +{re_f} +{re_f} *{re_n}\s+)+)',
                dtype=np.dtype(np.float64), str_operation=lambda x: [v.split() for v in x.strip().splitlines()],
                repeats=True
            )
        ]


class MainfileParser(TextParser):
    def init_quantities(self):
        self._quantities = [
            Quantity('program_version', r'Elk version (\S+)', dtype=str, flatten=False),
            Quantity(
                'lattice_vectors',
                rf'Lattice vectors \:\s+((?:{re_f} +{re_f} +{re_f}\s+)+)',
                shape=(3, 3), dtype=np.dtype(np.float64)
            ),
            Quantity(
                'species',
                r'(Species \: +\d+[\s\S]+?atomic positions.+\s+)'
                rf'((?:\d+ \: +{re_f} +{re_f}.+\s+)+)',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity('atom_label', r'Species \: +\d+ +\((\w+)\)', dtype=str),
                    Quantity(
                        'x_elk_muffin_tin_radius',
                        rf'muffin-tin radius \: +({re_f})', dtype=np.float64, unit=ureg.bohr
                    ),
                    Quantity(
                        'x_elk_muffin_tin_points',
                        rf'number of radial points in muffin\-tin \: +(\d+)',
                        dtype=np.int32
                    ),
                    Quantity(
                        'atom_positions',
                        rf'\d+ +\: +({re_f}) +({re_f}) +({re_f}).+',
                        repeats=True, dtype=np.dtype(np.float64)
                    )
                ])
            ),
            Quantity('spin_treatment', r'Spin treatment +\:\s+(\S+)', dtype=str),
            Quantity('x_elk_kpoints_grid', r'k\-point grid +\: +(\d+) +(\d+) +(\d+)', dtype=np.dtype(np.int32)),
            Quantity(
                'x_elk_rgkmax',
                rf'Muffin\-tin radius times maximum \|G\+k\| +\: +({re_f})',
                dtype=np.float64, unit=ureg.bohr
            ),
            Quantity(
                'x_elk_gkmax',
                rf'Maximum \|G\+k\| for APW functions +\: +({re_f})',
                dtype=np.float64, unit=1 / ureg.bohr
            ),
            Quantity(
                'x_elk_gmaxvr',
                rf'Maximum \|G\| for potential and density +\: +({re_f})',
                dtype=np.float64, unit=1 / ureg.bohr
            ),
            Quantity(
                'x_elk_gvector_size',
                r'G\-vector grid sizes +\: +(\d+) +(\d+) +(\d+)',
                dtype=np.dtype(np.int32)
            ),
            Quantity(
                'x_elk_gvector_total',
                r'Number of G\-vectors +\: +(\d+)',
                dtype=np.int32
            ),
            Quantity(
                'x_elk_lmaxapw', r'APW functions +\: +(\d+)',
                dtype=np.int32
            ),
            Quantity(
                'x_elk_nuclear_charge', rf'Total nuclear charge +\: +({re_f})',
                dtype=np.float64
            ),
            Quantity(
                'x_elk_core_charge', rf'Total core charge +\: +({re_f})',
                dtype=np.float64
            ),
            Quantity(
                'x_elk_valence_charge', rf'Total valence charge +\: +({re_f})',
                dtype=np.float64
            ),
            Quantity(
                'x_elk_excess_charge', rf'Total excess charge +\: +({re_f})',
                dtype=np.float64
            ),
            Quantity(
                'x_elk_electronic_charge', rf'Total electronic charge +\: +({re_f})',
                dtype=np.float64
            ),
            Quantity(
                'x_elk_wigner_radius', rf'Effective Wigner radius, r_s +\: +({re_f})',
                dtype=np.float64
            ),
            Quantity(
                'x_elk_empty_states', r'Number of empty states +\: +(\d+)',
                dtype=np.int32
            ),
            Quantity(
                'x_elk_valence_states', r'Total number of valence states +\: +(\d+)',
                dtype=np.int32
            ),
            Quantity(
                'x_elk_core_states', r'Total number of core states +\: +(\d+)',
                dtype=np.int32
            ),
            Quantity(
                'x_elk_lo', r'Total number of local\-orbitals +\: +(\d+)',
                dtype=np.int32
            ),
            Quantity('smearing_type', r'Smearing type +\: +(\d+)\s+\S+', dtype=np.int32),
            Quantity('smearing_width', rf'Smearing width +\: +({re_f})', dtype=np.float64),
            Quantity(
                'electronic_temperature',
                rf'Effective electronic temperature \(K\) +\: +({re_f})',
                dtype=np.float64
            ),
            Quantity(
                'xc_functional', r'Exchange\-correlation functional +\: +(\d+)',
                dtype=np.int32
            ),
            Quantity(
                'scf',
                r'Self\-consistent loop started([\s\S]+?)(?:Self\-consistent loop stopped|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'loop',
                        r'(Loop number +\: +\d+ +\|+\s+\+\-+\+[\s\S]+?)\+\-+\+',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity(
                                'energies',
                                r'Energies +\:\s+([\s\S]+?total energy.+)',
                                sub_parser=TextParser(quantities=[Quantity(
                                    'key_val', rf' *([\w \-]+?) +\: +({re_f})', dtype=np.float64,
                                    repeats=True, str_operation=lambda x: x.rsplit(' ', 1)
                                )])
                            ),
                            Quantity(
                                'charges',
                                r'Charges +\:\s+([\s\S]+?error.+)',
                                sub_parser=TextParser(quantities=[
                                    Quantity(
                                        'key_val', rf' *([\w \-]+?) +\: +({re_f})', dtype=np.float64,
                                        repeats=True, str_operation=lambda x: x.rsplit(' ', 1)
                                    ),
                                    Quantity(
                                        'muffin_tin', rf'atom +\d+ +\: +({re_f})',
                                        repeats=True, dtype=np.float64
                                    )
                                ])
                            ),
                            Quantity(
                                'energy_chage',
                                rf'Absolute change in total energy \(target\) +\: +({re_f})',
                                dtype=np.float64, unit=ureg.hartree
                            ),
                            Quantity(
                                'time',
                                rf'Time \(CPU seconds\) +\: +({re_f})',
                                dtype=np.float64, unit=ureg.s
                            )
                        ])
                    )
                ])
            )
        ]


class ElkParser:
    def __init__(self):
        self.mainfile_parser = MainfileParser()
        self.eigenval_parser = EigenvalParser()
        self.dos_parser = DataTextParser()
        self._xc_map = {
            2: ['LDA_C_PZ', 'LDA_X_PZ'], 3: ['LDA_C_PW', 'LDA_X_PZ'], 4: ['LDA_C_XALPHA'],
            5: ['LDA_C_VBH'], 20: ['GGA_C_PBE', 'GGA_X_PBE'], 21: ['GGA_C_PBE', 'GGA_X_PBE_R'],
            22: ['GGA_C_PBE_SOL', 'GGA_X_PBE_SOL'], 26: ['GGA_C_PBE', 'GGA_X_WC'],
            30: ['GGA_C_AM05', 'GGA_X_AM05']
        }
        self._smearing_map = {
            0: 'gaussian', 1: 'methfessel-paxton', 2: 'methfessel-paxton', 3: 'fermi'
        }
        self._metainfo_map = {
            'sum of eigenvalues': 'sum_eigenvalues',
            'electron kinetic': 'electronic_kinetic',
            'core electron kinetic': 'x_elk_core_electron_kinetic_energy',
            'Coulomb': 'electrostatic',
            'Coulomb potential': 'electrostatic_potential',
            'nuclear-nuclear': 'nuclear_repulsion',
            'electron-nuclear': 'x_elk_electron_nuclear_energy',
            'Hartree': 'x_elk_hartree_energy',
            'Madelung': 'madelung',
            'xc potential': 'xc_potential',
            'exchange': 'exchange',
            'correlation': 'correlation',
            'electron entropic': 'x_elk_electron_entropic_energy',
            'total energy': 'total',
            'core': 'x_elk_core_charge',
            'valence': 'x_elk_valence_charge',
            'interstitial': 'x_elk_interstitial_charge'
        }

    def init_parser(self):
        self.mainfile_parser.mainfile = self.filepath
        self.mainfile_parser.logger = self.logger
        self.eigenval_parser.logger = self.logger
        self.dos_parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        self.init_parser()

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(version=self.mainfile_parser.get('program_version', ''))

        sec_method = sec_run.m_create(Method)
        sec_method.basis_set.append(BasisSet(type='(L)APW+lo'))
        # xc functional
        sec_xc_functional = XCFunctional()
        for name in self._xc_map.get(self.mainfile_parser.xc_functional, []):
            functional = Functional(name=name)
            if '_X_' in name or name.endswith('_X'):
                sec_xc_functional.exchange.append(functional)
            elif '_C_' in name or name.endswith('_C'):
                sec_xc_functional.correlation.append(functional)
            elif 'HYB' in name:
                sec_xc_functional.hybrid.append(functional)
            else:
                sec_xc_functional.contributions.append(functional)
        sec_method.dft = DFT(xc_functional=sec_xc_functional)
        # electronic smearing parameters
        sec_method.electronic = Electronic(smearing=Smearing(
            kind=self._smearing_map.get(self.mainfile_parser.smearing_type),
            width=self.mainfile_parser.smearing_width
        ))
        # simulation parameters
        for key, val in self.mainfile_parser.items():
            if key.startswith('x_elk_') and val is not None:
                try:
                    setattr(sec_method, key, val)
                except Exception:
                    pass

        sec_system = sec_run.m_create(System)
        species = self.mainfile_parser.get('species', [])
        labels = []
        positions = []
        for specie in species:
            position = specie.get('atom_positions')
            labels.extend([specie.get('atom_label', 'X')] * len(position))
            positions.extend(position)
        lattice_vectors = self.mainfile_parser.get('lattice_vectors', np.eye(3)) * ureg.bohr
        sec_system.atoms = Atoms(
            labels=labels, positions=np.dot(positions, lattice_vectors),
            lattice_vectors=lattice_vectors
        )

        sec_calc = sec_run.m_create(Calculation)
        for loop in self.mainfile_parser.get('scf', {}).get('loop', []):
            scf_iteration = sec_calc.m_create(ScfIteration)

            # energies
            energies = {key: val * ureg.hartree for key, val in loop.get('energies', {}).get('key_val', [])}
            scf_iteration.energy = Energy()
            for key, val in energies.items():
                name = self._metainfo_map.get(key)
                if key.lower() == 'fermi':
                    scf_iteration.energy.fermi = val
                elif name is not None:
                    if name.endswith('_kinetic'):
                        name = name.replace('_kinetic', '')
                        energy_entry = getattr(scf_iteration.energy, name)
                        if energy_entry is None:
                            setattr(scf_iteration.energy, name, EnergyEntry(kinetic=val))
                        else:
                            energy_entry.kinetic = val
                    elif name.endswith('_potential'):
                        name = name.replace('_potential', '')
                        energy_entry = getattr(scf_iteration.energy, name)
                        if energy_entry is None:
                            setattr(scf_iteration.energy, name, EnergyEntry(potential=val))
                        else:
                            energy_entry.potential = val
                    else:
                        val = val if name.startswith('x_elk') else EnergyEntry(value=val)
                        setattr(scf_iteration.energy, name, val)

            scf_iteration.energy.change = loop.energy_change
            scf_iteration.time_calculation = loop.time

            # charges
            if loop.charges is not None:
                sec_charges = scf_iteration.m_create(Charges)
                for key, val in loop.charges.get('key_val', []):
                    name = self._metainfo_map.get(key)
                    if key.lower() == 'total charge':
                        sec_charges.total = val * ureg.elementary_charge
                        sec_charges.value = loop.charges.get('muffin_tin', []) * ureg.elementary_charge
                    elif name is not None:
                        setattr(sec_charges, name, val)

        # eigenvalues
        self.eigenval_parser.mainfile = os.path.join(self.maindir, 'EIGVAL.OUT')
        sec_eigenvalue = sec_calc.m_create(BandEnergies)
        sec_eigenvalue.kpoints = self.eigenval_parser.get('kpoint')
        eigs_occs = self.eigenval_parser.get('eigenvalue_occupancy', [])
        n_spin = 1 if self.mainfile_parser.get('spin_treatment', '').lower() == 'spin-unpolarised' else 2
        # TODO determine how eigenvalues are printed in spin polarized case
        eigs_occs = np.reshape(eigs_occs, (
            self.eigenval_parser.n_kpoints, n_spin, self.eigenval_parser.n_states, 3))
        eigs_occs = np.transpose(eigs_occs, axes=(3, 1, 0, 2))
        # first column is state index
        sec_eigenvalue.energies = eigs_occs[1] * ureg.hartree
        sec_eigenvalue.occupancies = eigs_occs[2]

        # dos
        self.dos_parser.mainfile = os.path.join(self.maindir, 'TDOS.OUT')
        # TODO determine how dos are printed in spin polarised case
        if self.dos_parser.data is not None:
            dos_data = np.transpose(self.dos_parser.data)
            sec_dos = sec_calc.m_create(Dos, Calculation.dos_electronic)
            sec_dos.energies = dos_data[0] * ureg.hartree
            # TODO determine how dos is normalized
            sec_dos.total.append(DosValues(value=dos_data[1] * (1 / ureg.hartree)))

        # TODO implement geometry_optimization, no example data
