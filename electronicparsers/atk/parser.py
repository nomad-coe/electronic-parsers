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
import re
import logging
from scipy.io.netcdf import netcdf_file
from ase.data import atomic_names
from ase import lattice as aselattice, Atoms
from ase import Atoms as aseAtoms

from nomad.units import ureg
from nomad.parsing.file_parser import FileParser, TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Method, BasisSet, Electronic, Smearing, DFT, XCFunctional, Functional,
    BasisSetAtomCentered)
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry)


class NCParser(FileParser):
    def __init__(self):
        super().__init__()
        self._configuration_types = ['MoleculeConfiguration', 'BulkConfiguration']
        self._units = dict(angstrom=ureg.angstrom, bohr=ureg.bohr, kelvin=ureg.kelvin)
        self._fingerprints = dict()

    @property
    def netcdf(self):
        if self._file_handler is None:
            try:
                self._file_handler = netcdf_file(self.mainfile, mmap=True)
            except Exception:
                return
            # prepare fingerprints required for variables
            if hasattr(self._file_handler, 'fingerprint_table'):
                fprints = [p.split(':') for p in self._file_handler.fingerprint_table.decode().split('#') if p]  # pylint: disable=maybe-no-member
                self._fingerprints = {p[1]: p[0] for p in fprints}

        return self._file_handler

    def resolve_unit(self, val):
        val = val.split('*')
        if len(val) == 2:
            return (float(val[0]) * self._units.get(val[1].lower(), ureg.angstrom)).to('angstrom').magnitude
        return float(val[0])

    def _resolve_configuration(self, data):

        # TODO implement UnitCell, ghost atoms

        lattices = dict(
            FaceCenteredCubic=aselattice.FCC, BodyCenteredCubic=aselattice.BCC, Triclinic=aselattice.TRI)

        re_f = r'[\d\.\-\+Ee]+'

        data = data.data[:].copy().tobytes().decode()

        elements = re.search(r'elements = \[(.+)\]', data)
        if not elements:
            return

        coordinates = re.search(r'coordinates *\= *(\[\s*\[[\s\S]+?\]\s*\])', data)
        if not coordinates:
            return

        try:
            numbers = [atomic_names.index(e.strip().title()) for e in elements.group(1).split(',')]

            positions = np.array([v.split(',') for v in re.findall(
                rf'\[( *{re_f} *\, *{re_f} *\, *{re_f} *)\]', coordinates.group(1))], dtype=np.dtype(np.float64))

            atoms = aseAtoms(numbers=numbers, positions=positions)

        except Exception:
            return

        velocities = re.search(r'velocities *\= *(\[\s*\[[\s\S]+?\]\s*\])', data)
        if velocities:
            atoms.set_velocities(np.array([v.split(',') for v in re.findall(
                rf'\[( *{re_f} *\, *{re_f} *\, *{re_f} *)\]', velocities.group(1))], dtype=np.dtype(np.float64)))

        if 'MoleculeConfiguration' in data:
            return atoms

        atoms.set_pbc(True)

        lattice = re.search(r'\nlattice = (\w+) *\((.+)\)', data)
        lattice, parameters = lattice.groups() if lattice else ('', '')
        parameters = [self.resolve_unit(p) for p in re.findall(rf'({re_f} *\* *\w+)', parameters)]
        lattice = lattices.get(lattice)
        if lattice is None:
            return

        try:
            atoms.set_cell(lattice(*parameters).tocell(), scale_atoms='fractional' in data)
        except Exception:
            pass

        return atoms

    def parse(self, key):
        val = None
        if hasattr(self.netcdf, key):
            val = getattr(self.netcdf, key)
            if isinstance(val, bytes):
                val = val.decode()
        elif key == 'configuration_names':
            val = []
            re_name = re.compile(r'(\w+Configuration\_gID\d+)$')
            for name in self.netcdf.variables.keys():
                name = re.match(re_name, name)
                if name:
                    val.append(name.group(1))
        elif key == 'atoms':
            val = dict()
            for name in self.get('configuration_names', []):
                data = self.netcdf.variables.get(name)
                if data is None:
                    continue
                val[name] = self._resolve_configuration(data)
        elif key == 'parameters':
            val = dict()
            for name in self.get('configuration_names', []):
                data = self.netcdf.variables.get('%s_calculator' % name)
                if data is None:
                    continue
                val[name] = data.data.tobytes()
        elif key == 'energies':
            val = dict()
            # energy_keys = [k for k in self.netcdf.variables.keys() if k.startswith('TotalEnergy')]
            energy_re = r'TotalEnergy\_(gID\d+)\_component\_(\S+)'
            for key_n in self.netcdf.variables.keys():
                energy_key = re.match(energy_re, key_n)
                if energy_key:
                    fp = self.netcdf.variables[
                        'TotalEnergy_%s_finger_print' % energy_key.group(1)].data.tobytes().decode()
                    val.setdefault(fp, {})
                    val[fp][energy_key.group(2)] = self.netcdf.variables[key_n].data[0] * ureg.eV
        elif key == 'forces':
            val = dict()
            forces_re = r'Forces\_(gID\d+)\_atom\_resolved\_forces'
            for key_n in self.netcdf.variables.keys():
                forces_key = re.match(forces_re, key_n)
                if forces_key:
                    fp = self.netcdf.variables[
                        'TotalEnergy_%s_finger_print' % forces_key.group(1)].data.tobytes().decode()
                    val[fp] = self.netcdf.variables[key_n].data * (ureg.eV / ureg.angstrom)

        # TODO implement stress, bandstructure, eigenvalues
        self._results[key] = val


class CalculatorParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity('smearing_width', r'electron_temperature *\= *([\d\.]+)', dtype=float),
            Quantity('charge', r'charge *\= *([\d\.]+)', dtype=float),
            Quantity('xc_functional', r'exchange_correlation *\= *(\S+)')
        ]


class ATKParser:
    def __init__(self):
        self.nc_parser = NCParser()
        self.calculator_parser = CalculatorParser()

        self._metainfo_map = {
            'Exchange-Correlation': 'energy_xc', 'Kinetic': 'energy_kinetic_electronic',
            'Entropy-Term': 'energy_correction_entropy', 'Electrostatic': 'energy_electrostatic'}

        self._xc_functional_map = {
            'LDA.RPA': ['LDA_X', 'LDA_C_RPA'],
            'LDA.PZ': ['LDA_X', 'LDA_C_PZ'],
            'LDA.PW': ['LDA_X', 'LDA_C_PW'],
            'GGA.PW91': ['GGA_X_PW91', 'GGA_C_PW91'],
            'GGA.PBE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'GGA.PBES': ['GGA_X_PBE_SOL', 'GGA_C_PBE_SOL'],
            'GGA.RPBE': ['GGA_X_RPBE', 'GGA_C_PBE'],
            'BLYP': ['GGA_X_B88', 'GGA_C_LYP'],
            'HCTH407': ['GGA_XC_HCTH_407'],
            'WC': ['GGA_X_WC', 'GGA_C_PBE'],
            'AM05': ['GGA_X_AM05', 'GGA_C_AM05'],
            'mBEEF': ['MGGA_X_MBEEF', 'GGA_C_PBE_SOL']}

    def init_parser(self):
        self.nc_parser.mainfile = self.filepath
        self.nc_parser.logger = self.logger

    def parse_configurations(self):
        sec_run = self.archive.run[0]

        def parse_method(name):
            sec_method = sec_run.m_create(Method)

            parameters = self.nc_parser.get('parameters').get(name)
            if parameters is None:
                return sec_method

            # this is only a dummy filename as we will get the info from the calculator data
            self.calculator_parser.mainfile = self.filepath
            self.calculator_parser._file_handler = parameters

            sec_method.electronic = Electronic(
                relativity_method='pseudo_scalar_relativistic',
                charge=self.calculator_parser.get('charge', 0.0),
                smearing=Smearing(
                    kind='fermi', width=self.calculator_parser.get('smearing_width', 0.0)))

            sec_dft = sec_method.m_create(DFT)
            sec_xc_functional = sec_dft.m_create(XCFunctional)
            for xc_functional in self._xc_functional_map.get(self.calculator_parser.get('xc_functional'), []):
                if '_XC' in xc_functional:
                    sec_xc_functional.contributions.append(Functional(name=xc_functional))
                elif '_X' in xc_functional:
                    sec_xc_functional.exchange.append(Functional(name=xc_functional))
                elif '_C' in xc_functional:
                    sec_xc_functional.correlation.append(Functional(name=xc_functional))

            sec_method.basis_set.append(
                BasisSet(type='numeric AOs'))
            sec_method.basis_set[0].atom_centered.append(BasisSetAtomCentered(name='ATK LCAO basis'))

            return sec_method

        def parse_system(atoms):
            if atoms is None:
                return

            sec_system = sec_run.m_create(System)
            sec_atoms = sec_system.m_create(Atoms)
            sec_atoms.labels = atoms.get_chemical_symbols()
            sec_atoms.positions = atoms.get_positions() * ureg.angstrom
            sec_atoms.lattice_vectors = atoms.get_cell().array * ureg.angstrom
            sec_atoms.periodic = atoms.get_pbc()
            velocities = atoms.get_velocities()
            if velocities:
                sec_atoms.velocities = velocities * (ureg.angstrom / ureg.fs)

            return sec_system

        def parse_scc(fingerprint):
            sec_scc = sec_run.m_create(Calculation)

            # energies
            sec_energy = sec_scc.m_create(Energy)
            energy_total = 0.
            for key, val in self.nc_parser.get('energies').get(fingerprint, {}).items():
                key = self._metainfo_map.get(key)
                energy_total += val
                if key is not None:
                    key = key.replace('energy_', '')
                    sec_energy.m_add_sub_section(getattr(Energy, key), EnergyEntry(value=val))
            sec_energy.total = EnergyEntry(value=energy_total)

            # forces
            forces = self.nc_parser.get('forces').get(fingerprint)
            if forces is not None:
                sec_forces = sec_scc.m_create(Forces)
                sec_forces.total = ForcesEntry(value=forces)

            return sec_scc

        for name, atoms in self.nc_parser.get('atoms', {}).items():
            sec_system = parse_system(atoms)
            sec_method = parse_method(name)
            fingerprint = self.nc_parser._fingerprints.get('gID%s' % name.split('gID')[-1])
            sec_scc = parse_scc(fingerprint)
            if sec_system is not None:
                sec_scc.system_ref = sec_system
            if sec_method is not None:
                sec_scc.method_ref = sec_method

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        sec_run = self.archive.m_create(Run)
        sec_run.program_name = 'ATK'
        version = self.nc_parser.get('version', 'unavailable')
        sec_run.program = Program(name='ATK', version=version)

        self.parse_configurations()
