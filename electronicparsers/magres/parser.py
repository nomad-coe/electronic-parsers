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
import numpy as np
import logging
import re
from datetime import datetime

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    Functional, Method, DFT, Electronic, XCFunctional, Smearing,
    BasisSetContainer, BasisSet, AtomParameters
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, SpinSpinCoupling, ElectricFieldGradient, MagneticShielding, MagneticSusceptibility
)
from simulationworkflowschema import SinglePoint


re_float = r' *[-+]?\d+\.\d*(?:[Ee][-+]\d+)? *'

class MagresFileParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity('lattice_units',r'units *lattice *([a-zA-Z]+)'),
            Quantity('atom_units',r'units *atom *([a-zA-Z]+)'),
            Quantity('ms_units',r'units *ms *([a-zA-Z]+)'),
            Quantity('efg_units',r'units *efg *([a-zA-Z]+)'),
            Quantity('efg_local_units',r'units *efg_local *([a-zA-Z]+)'),
            Quantity('efg_nonlocal_units',r'units *efg_nonlocal *([a-zA-Z]+)'),
            Quantity('isc_units',r'units *isc *([a-zA-Z\^\d\.\-]+)'),
            Quantity('isc_fc_units',r'units *isc_fc *([a-zA-Z\^\d\.\-]+)'),
            Quantity('isc_spin_units',r'units *isc_spin *([a-zA-Z\^\d\.\-]+)'),
            Quantity('isc_orbital_p_units',r'units *isc_orbital_p *([a-zA-Z\^\d\.\-]+)'),
            Quantity('isc_orbital_d_units',r'units *isc_orbital_d *([a-zA-Z\^\d\.\-]+)'),
            Quantity('sus_units', r'units *sus *([a-zA-Z\^\d\.\-]+)'),
            Quantity('cutoffenergy_units', rf'units *calc\_cutoffenergy *([a-zA-Z]+)'),
            Quantity(
                'calculation',
                r'(\[calculation\][\s\S]+?)(?:\[\/calculation\])',
                sub_parser=TextParser(quantities=[
                    Quantity('code', r'calc\_code *([a-zA-Z]+)'),
                    Quantity('code_version', r'calc\_code\_version *([a-zA-Z\d\.]+)'),
                    Quantity(
                        'code_hgversion',
                        r'calc\_code\_hgversion ([a-zA-Z\d\:\+\s]*)\n',
                        flatten=False
                    ),
                    Quantity('code_platform', r'calc\_code\_platform *([a-zA-Z\d\_]+)'),
                    Quantity('name', r'calc\_name *([\w]+)'),
                    Quantity('comment', r'calc\_comment *([\w]+)'),
                    Quantity('xcfunctional', r'calc\_xcfunctional *([\w]+)'),
                    Quantity(
                        'cutoffenergy', rf'calc\_cutoffenergy({re_float})(?P<__unit>\w+)'
                    ),
                    Quantity(
                        'pspot', r'calc\_pspot *([\w]+) *([\w\.\|\(\)\=\:]+)',
                        repeats=True
                    ),
                    Quantity(
                        'kpoint_mp_grid',
                        r'calc\_kpoint\_mp\_grid *([\w]+) *([\w]+) *([\w]+)'
                    ),
                    Quantity(
                        'kpoint_mp_offset', rf'calc\_kpoint\_mp\_offset({re_float*3})$'
                    ),
                ]),
            ),
            Quantity(
                'atoms',
                r'(\[atoms\][\s\S]+?)(?:\[\/atoms\])',
                sub_parser=TextParser(quantities=[
                    Quantity('lattice', rf'lattice({re_float*9})'),
                    Quantity('symmetry', r'symmetry *([\w\-\+\,]+)', repeats=True),
                    Quantity(
                        'atom',
                        rf'atom *([a-zA-Z]+) *[a-zA-Z]* *([\d]+) *({re_float*3})',
                        repeats=True
                    ),
                ]),
            ),
            Quantity(
                'magres',
                r'(\[magres\][\s\S]+?)(?:\[\/magres\])',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'ms', rf'ms *([a-zA-Z]+) *(\d+)({re_float*9})', repeats=True),
                    Quantity(
                        'efg', rf'efg *([a-zA-Z]+) *(\d+)({re_float*9})', repeats=True),
                    Quantity(
                        'efg_local',
                        rf'efg_local *([a-zA-Z]+) *(\d+)({re_float*9})',
                        repeats=True
                    ),
                    Quantity(
                        'efg_nonlocal',
                        rf'efg_nonlocal *([a-zA-Z]+) *(\d+)({re_float*9})',
                        repeats=True
                    ),
                    Quantity(
                        'isc',
                        rf'isc *([a-zA-Z]+) *(\d+) *([a-zA-Z]+) *(\d+)({re_float*9})',
                        repeats=True
                    ),
                    Quantity(
                        'isc_fc',
                        rf'isc_fc *([a-zA-Z]+) *(\d+) *([a-zA-Z]+) *(\d+)({re_float*9})',
                        repeats=True
                    ),
                    Quantity(
                        'isc_orbital_p',
                        rf'isc_orbital_p *([a-zA-Z]+) *(\d+) *([a-zA-Z]+) *(\d+)({re_float*9})',
                        repeats=True
                    ),
                    Quantity(
                        'isc_orbital_d',
                        rf'isc_orbital_d *([a-zA-Z]+) *(\d+) *([a-zA-Z]+) *(\d+)({re_float*9})',
                        repeats=True
                    ),
                    Quantity(
                        'isc_spin',
                        rf'isc_spin *([a-zA-Z]+) *(\d+) *([a-zA-Z]+) *(\d+)({re_float*9})',
                        repeats=True
                    ),
                    Quantity('sus', rf'sus *({re_float*9})', repeats=True),
                ]),
            ),
        ]



class MagresParser:
    level = 1

    def __init__(self):
        self.magres_file_parser = MagresFileParser()

    def init_parser(self):
        self.magres_file_parser.mainfile = self.filepath
        self.magres_file_parser.logger = self.logger

    def _check_units_magres(self):
        allowed_units = {
            'lattice': 'Angstrom',
            'atom': 'Angstrom',
            'ms': 'ppm',
            'efg': 'au',
            'efg_local': 'au',
            'efg_nonlocal': 'au',
            'isc': '10^19.T^2.J^-1',
            'isc_fc': '10^19.T^2.J^-1',
            'isc_orbital_p': '10^19.T^2.J^-1',
            'isc_orbital_d': '10^19.T^2.J^-1',
            'isc_spin': '10^19.T^2.J^-1',
            'sus': '10^-6.cm^3.mol^-1',
        }
        for key, value in allowed_units.items():
            data = self.magres_file_parser.get(f'{key}_units', '')
            if data != value:
                self.logger.warning(f'The units of {key} are not allowed for {value}. We '
                                    'will be use the default units.')
                return

    def parse_system(self):
        sec_run = self.archive.run[-1]
        sec_atoms = sec_run.m_create(System).m_create(Atoms)

        # Check if [atoms][/atoms] was correctly parsed
        atoms = self.magres_file_parser.get('atoms')
        if not atoms:
            self.logger.warning('Could not find atomic structure in magres file.')
            return

        # Store lattice_vectors and periodic boundary conditions
        lattice_vectors = np.reshape(np.array(atoms.get('lattice', [])), (3, 3))
        sec_atoms.lattice_vectors = lattice_vectors * ureg.angstrom
        pbc = [True, True, True] if lattice_vectors is not None else [False, False, False]
        sec_atoms.periodic = pbc

        # Storing atom positions and labels
        atoms_list = atoms.get('atom', [])
        if len(atoms_list) == 0:
            self.logger.warning('Could not find atom positions and labels in magres file.')
            return
        atom_labels = []
        atom_positions = []
        for atom in atoms_list:
            atom_labels.append(atom[0])
            atom_positions.append(atom[2:])
        sec_atoms.labels = atom_labels
        sec_atoms.positions = atom_positions * ureg.angstrom

    def parse_method(self, calculation_params):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

    def parse_calculation(self):
        sec_run = self.archive.run[-1]

        # Check if [magres][/magres] was correctly parsed
        magres_data = self.magres_file_parser.get('magres')
        if not magres_data:
            self.logger.warning('Could not find [magres] data block in magres file.')
            return

        # Creating Calculation and adding System and Method refs
        sec_scc = sec_run.m_create(Calculation)
        sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]
        atoms = sec_scc.system_ref.atoms.labels
        n_atoms = len(atoms)

        # Magnetic Shielding Tensor (ms) parsing
        data = magres_data.get('ms', [])
        if data is not None:
            values = np.reshape([d[2:] for d in data], (n_atoms, 3, 3))
            sec_ms = sec_scc.m_create(MagneticShielding)
            sec_ms.value = values * 1e-6 * ureg('dimensionless')

        # Electric Field Gradient (efg) parsing
        efg_contributions = {
            'efg_local': 'local',
            'efg_nonlocal': 'nonlocal',
            'efg': 'total'
        }
        for tag, contribution in efg_contributions.items():
            data = magres_data.get(tag, [])
            if not data:
                continue
            values = np.reshape([d[2:] for d in data], (n_atoms, 3, 3))
            sec_efg = sec_scc.m_create(ElectricFieldGradient)
            sec_efg.contribution = contribution
            sec_efg.value = values * 9.717362e21 * ureg('V/m^2')

        # Indirect Spin-Spin Coupling (isc) parsing
        isc_contributions = {
            'isc_fc': 'fermi_contact',
            'isc_orbital_p': 'orbital_paramagnetic',
            'isc_orbital_d': 'orbital_diamagnetic',
            'isc_spin': 'spin_dipolar',
            'isc': 'total',
        }
        # isc_contributions = ['_fc', '_orbital_p', '_orbital_d', '_spin', '']
        # for contribution in isc_contributions:
            # atom_indices = np.array(magres_data.get(f'isc{contribution}', []))[:, :4]
            # values = np.array(magres_data.get(f'isc{contribution}', []))[:, 4:]

        # Magnetic Susceptibility (sus) parsing
        data = magres_data.get('sus', [])
        if data is not None:
            values = np.reshape(data, (3, 3))
            sec_sus = sec_scc.m_create(MagneticSusceptibility)
            sec_sus.scale_dimension = 'macroscopic'
            sec_sus.value = values * 1e-6 * ureg('dimensionless')

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()
        self._check_units_magres()

        sec_run = self.archive.m_create(Run)
        calculation_params = self.magres_file_parser.get('calculation')
        sec_run.program = Program(
            name=calculation_params.get('code', ''),
            version=calculation_params.get('version', ''),
        )

        self.parse_system()

        self.parse_method(calculation_params)

        self.parse_calculation()

        workflow = SinglePoint()
        self.archive.workflow2 = workflow
