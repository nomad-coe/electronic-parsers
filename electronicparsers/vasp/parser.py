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

'''
To foster reuse of common code between paring run and OURCAR files, this module uses
several parser classes and hierarchies. The public :class:`VASPParser` provides an
interface to both parsers. This parser retrieves the content from a run or OURCAR specific
:class:`ContentParser` and builds the NOMAD archive.

The two content parsers :class:`RunContentParser` and
:class:`OutcarContentParser` provide functionality to retrieve properties from their
respective file format. They both use separate file (:class:`RunFileParser`) and text
(:class:`OutcarTextParser`) parsers to read content content from either xml or text files.
'''

from typing import List
import os
import numpy as np
import logging
from datetime import datetime
import ase
import re
from xml.sax import ContentHandler, make_parser  # type: ignore

from nomad.units import ureg
from nomad.parsing import FairdiParser
from nomad.parsing.file_parser import FileParser
from nomad.parsing.file_parser.text_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Method, BasisSet, BasisSetCellDependent, DFT, AtomParameters, XCFunctional,
    Functional, Electronic, Scf
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, Stress, StressEntry,
    BandEnergies, DosValues, ScfIteration, BandStructure, BandGap, Dos
)
from nomad.datamodel.metainfo.workflow import (
    Workflow, GeometryOptimization, SinglePoint, MolecularDynamics)


def get_key_values(val_in):
    val = [v for v in val_in.split('\n') if '=' in v]
    data = {}
    pattern = re.compile(r'([A-Z_]+)\s*=\s*([\w\-]+\s{0,3}[\d\. ]*[E\-\+\d]*)')

    def convert(v):
        if isinstance(v, list):
            v = [convert(vi) for vi in v]
        elif isinstance(v, str):
            try:
                v = float(v) if '.' in v else int(v)
            except Exception:
                pass
        else:
            pass
        return v

    for v in val:
        res = pattern.findall(v)
        for resi in res:
            vi = resi[1].split()
            vi = vi[0] if len(vi) == 1 else vi
            vi = vi.strip() if isinstance(vi, str) else vi
            vi = vi == 'T' if vi in ['T', 'F'] else vi
            data[resi[0]] = convert(vi)
    return data


def convert(val, dtype):
    if isinstance(val, list):
        return [convert(v, dtype) for v in val]
    else:
        try:
            return dtype(val)
        except Exception:
            return val


class ContentParser:
    def __init__(self):
        self.parser = None
        self._header = None
        self._incar = None
        self._kpoints_info = None
        self._atom_info = None
        self._calculations = None
        self._n_bands = None
        self._n_dos = None
        self.metainfo_mapping = {
            'e_fr_energy': 'energy_free', 'e_wo_entrp': 'energy_total',
            'e_0_energy': 'energy_total_T0', 'hartreedc': 'energy_correction_hartree',
            'XCdc': 'energy_XC', 'forces': 'atom_forces', 'stress': 'stress_tensor',
            'energy_total': 'energy_free', 'energy_T0': 'energy_total_T0',
            'energy_entropy0': 'energy_total', 'DENC': 'energy_correction_hartree',
            'EXHF': 'energy_exchange', 'EBANDS': 'energy_sum_eigenvalues', 'efermi': 'fermi'}

        # TODO 1. verify list most probably incomplete, 2. it appears that there is no
        # single parameter for hybrid functionals so it is difficult to determine, 3. not
        # sure about --, I thought it is lda exchange only.
        self.xc_functional_mapping = {
            '91': ['GGA_X_PW91', 'GGA_C_PW91'], 'PE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'AM': ['GGA_X_AM05', 'GGA_C_AM05'], 'HL': ['LDA_C_HL'],
            'PZ': ['LDA_C_PZ'], 'WI': ['LDA_C_WIGNER'],
            'RE': ['GGA_X_PBE_R'], 'VW': ['LDA_C_VWN'], 'B3': ['HYB_GGA_XC_B3LYP3'],
            'B5': ['HYB_GGA_XC_B3LYP5'], 'BF': ['GGA_X_BEEFVDW', 'GGA_XC_BEEFVDW'],
            'CO': [], 'OR': ['GGA_X_OPTPBE_VDW'],
            'BO': ['GGA_X_OPTB88_VDW'], 'RA': ['LDA_C_PW_RPA'],
            'RP': ['GGA_X_RPBE', 'GGA_C_PBE'], 'PS': ['GGA_C_PBE_SOL', 'GGA_X_PBE_SOL'],
            'MK': ['GGA_X_OPTB86_VDW'], '--': ['GGA_X_PBE', 'GGA_C_PBE'],
            'TPSS': ['MGGA_X_TPSS', 'MGGA_C_TPSS'], 'RTPSS': ['MGGA_X_RTPSS'],
            'M06L': ['MGGA_C_M06_L'], 'MBJ': ['MGGA_X_BJ06'], 'MS0': ['MGGA_X_MS0'],
            'MS1': ['MGGA_X_MS1'], 'MS2': ['MGGA_X_MS2'],
            'RSCAN': ['MGGA_X_RSCAN', 'MGGA_C_RSCAN'], 'SCAN': ['MGGA_X_SCAN'],
            'R2SCAN': ['MGGA_X_R2SCAN', 'MGGA_C_R2SCAN'],
            'HLE17': ['MGGA_XC_HLE17']}

    def init_parser(self, filepath, logger):
        self.parser.mainfile = filepath
        self.parser.logger = logger
        self._incar = None
        self._kpoints_info = None
        self._atom_info = None
        self._header = None
        self._calculations = None
        self._n_bands = None
        self._n_dos = None

    def reuse_parser(self, parser):
        self.parser.quantities = parser.parser.quantities

    def _fix_incar(self, incar):
        # fix for LORBIT, list is read
        lorbit = incar.get('LORBIT', None)
        if isinstance(lorbit, list):
            incar['LORBIT'] = lorbit[0]

    def get_incar(self):
        pass

    def get_incar_out(self):
        pass

    # why make a distinction between incar_in and incar_out?
    @property
    def incar(self):
        if self._incar is None:
            self._incar = dict(incar=None, incar_out=None)
        if self._incar['incar'] is None:
            self.get_incar()
        if self._incar['incar_out'] is None:
            self.get_incar_out()

        incar = dict()
        incar.update(self._incar['incar'])
        incar.update(self._incar['incar_out'])

        return incar

    @property
    def ispin(self):
        return self.incar.get('ISPIN', 1)

    @property
    def ibrion(self):
        val = self.incar.get('IBRION,', None)
        if val is None:
            val = -1 if self.incar.get('NSW', 0) in [0, 1] else 0
        return val

    def is_converged(self, n_calc):
        return


class OutcarTextParser(TextParser):
    def __init__(self):
        self._chemical_symbols = None

        super().__init__(None)

    def init_quantities(self):
        def str_to_array(val_in):
            val = [re.findall(r'(\-?\d+\.[\dEe]+)', v) for v in val_in.strip().split('\n') if '--' not in v]
            return np.array([v[0:3] for v in val], float), np.array([v[3:6] for v in val], float)

        def str_to_stress(val_in):
            val = [float(v) for v in val_in.strip().split()]
            stress = np.zeros((3, 3))
            stress[0][0] = val[0]
            stress[1][1] = val[1]
            stress[2][2] = val[2]
            stress[0][1] = stress[1][0] = val[3]
            stress[1][2] = stress[2][1] = val[4]
            stress[0][2] = stress[2][0] = val[5]
            return stress

        def str_to_header(val_in):
            version, build_date, build_type, platform, date, time, parallel = val_in.split()
            parallel = 'parallel' if parallel == 'running' else parallel
            subversion = '%s %s %s' % (build_date, build_type, parallel)
            date = date.replace('.', ' ')
            return dict(version=version, subversion=subversion, platform=platform, date=date, time=time)

        def str_to_positions(val_in):
            re_position = re.compile(r'\d*\s*(\-*\d+\.\d+)\s*(\-*\d+\.\d+)\s*(\-*\d+\.\d+)')
            positions = []
            for val in val_in.strip().split('\n'):
                position = re_position.search(val)
                if position:
                    positions.append(position.groups())
            return np.array(positions, dtype=float)

        def str_to_mass_valence(val_in):
            mass_valence = [v.strip() for v in val_in.split('\n')]
            for n, values in enumerate(mass_valence):
                mass_valence[n] = [float(values[i - 6:i]) for i in range(len(values), 2, -6)]
                mass_valence[n].reverse()
            return [(mass_valence[0][i], mass_valence[1][i]) for i in range(len(mass_valence[0]))]

        scf_iteration = [
            Quantity(
                'energy_total', r'free energy\s*TOTEN\s*=\s*([\d\.\-]+)\s*eV',
                repeats=False, dtype=float),
            Quantity(
                'energy_entropy0', r'energy without entropy\s*=\s*([\d\.\-]+)',
                repeats=False, dtype=float),
            Quantity(
                'energy_T0', r'energy\(sigma\->0\)\s*=\s*([\d\.\-]+)',
                repeats=False, dtype=float),
            Quantity(
                'energy_components',
                r'Free energy of the ion-electron system \(eV\)\s*\-+([\s\S]+?)\-{10}',
                str_operation=get_key_values, convert=False)
        ]

        calculation_quantities = [
            Quantity(
                'scf_iteration',
                r'Iteration\s*\d+\(\s*\d+\s*\)([\s\S]+?energy\(sigma\->0\)\s*=\s*.+)',
                repeats=True, sub_parser=TextParser(quantities=scf_iteration)),
            Quantity(
                'energies',
                r'FREE ENERGIE OF THE ION-ELECTRON SYSTEM \(eV\)\s*\-+\s*([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_total',
                        r'free\s*energy\s*TOTEN\s*=\s*([\-\d\.]+)',
                        repeats=False, dtype=float),
                    Quantity(
                        'energy_entropy0',
                        r'energy\s*without\s*entropy\s*=\s*([\-\d\.]+)',
                        repeats=False, dtype=float),
                    Quantity(
                        'energy_T0',
                        r'energy\(sigma\->0\)\s*=\s*([\-\d\.]+)',
                        repeats=False, dtype=float)])),
            Quantity(
                'stress',
                r'in kB\s*(\-?\d+\.\d+)\s*(\-?\d+\.\d+)\s*(\-?\d+\.\d+)\s*'
                r'(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)',
                str_operation=str_to_stress, convert=False),
            Quantity(
                'positions_forces',
                r'POSITION\s*TOTAL\-FORCE \(eV/Angst\)\s*\-+\s*([\d\.\s\-E]+)',
                str_operation=str_to_array, convert=False),
            Quantity(
                'lattice_vectors',
                r'direct lattice vectors\s*reciprocal lattice vectors\s*'
                r'(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)'
                r'(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)'
                r'(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)',
                str_operation=str_to_array, convert=False),
            Quantity(
                'converged',
                r'aborting loop because (EDIFF is reached)', repeats=False,
                dtype=str, convert=False),
            Quantity(
                'fermi_energy', r'E\-fermi :\s*([\d\.]+)', dtype=str, repeats=False),
            Quantity(
                'eigenvalues',
                r'band No\.\s*band energies\s*occupation\s*([\d\.\s\-]+?)(?:k\-point|spin|\-{10})',
                repeats=True, dtype=float),
            Quantity(
                'convergence',
                r'(aborting loop because EDIFF is reached)')]

        self._quantities = [
            Quantity(
                'calculation',
                r'(\-\-\s*Iteration\s*\d+\(\s*1\s*\)\s*[\s\S]+?)'
                r'((?:FREE ENERGIE OF THE ION\-ELECTRON SYSTEM \(eV\)[\s\S]+?\-{100})|\Z)',
                repeats=True, sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity(
                'header',
                r'vasp\.([\d\.]+)\s*(\w+)\s*[\s\S]+?\)\s*(\w+)\s*'
                r'executed on\s*(\w+)\s*date\s*([\d\.]+)\s*([\d\:]+)\s*(\w+)',
                repeats=False, str_operation=str_to_header, convert=False),
            Quantity(
                'parameters', r'Startparameter for this run:([\s\S]+?)\-{100}',
                str_operation=get_key_values, repeats=False, convert=False),
            Quantity(
                'ions_per_type', r'ions per type =\s*([ \d]+)', dtype=int, repeats=False),
            Quantity(
                'species', r'TITEL\s*=\s*(\w+) ([A-Z][a-z]*)', dtype=str, repeats=True),
            Quantity(
                'species', r'\n *(\w+) +([A-Z][a-z]*).+?:\s*energy of atom +\d+', dtype=str, repeats=True),
            Quantity(
                'mass_valence', r'POMASS\s*=\s*([\d\.]+);\s*ZVAL\s*=\s*([\d\.]+)\s*mass and valenz',
                dtype=float, repeats=True),
            Quantity(
                'mass_valence', r'POMASS +(=[\d\. ]+\s+)Ionic Valenz\s+ZVAL +(=[\d\. ]+)',
                str_operation=str_to_mass_valence),
            Quantity(
                'kpoints',
                r'k-points in reciprocal lattice and weights:[\s\S]+?\n([\d\.\s\-]+)',
                repeats=False, dtype=float),
            Quantity(
                'nbands', r'NBANDS\s*=\s*(\d+)', dtype=int, repeats=False),
            Quantity(
                'lattice_vectors',
                r'direct lattice vectors\s*reciprocal lattice vectors\s*'
                r'(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)'
                r'(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)'
                r'(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)(\-?\d+\.\d+\s*)',
                str_operation=str_to_array, convert=False),
            Quantity(
                'positions',
                r'ion\s*position\s*nearest neighbor table([\s\S]+?)LATTYP',
                str_operation=str_to_positions, convert=False),
            # alternative format
            Quantity(
                'positions',
                r'position of ions in cartesian coordinates\s*\(Angst\):([\s\S]+?)\n *\n',
                str_operation=str_to_positions, convert=False)]


class OutcarContentParser(ContentParser):
    def __init__(self):
        super().__init__()
        self.parser = OutcarTextParser()

    def _get_key_values(self, path):
        if not os.path.isfile(path):
            return dict()
        with self.parser.open(path) as f:
            text = f.read()
            text = text.decode() if isinstance(text, bytes) else text
            data = get_key_values(text)
        return data

    @property
    def header(self):
        if self._header is None:
            self._header = self.parser.get('header', {})
            self._header['program'] = 'vasp'
            for key, val in self._header.items():
                if not isinstance(val, str):
                    self._header[key] = ' '.join(val)
        return self._header

    def get_incar(self):
        if self._incar is not None and self._incar.get('incar', None) is not None:
            return self._incar.get('incar')

        incar = dict()
        if self._incar is None:
            self._incar = dict(incar=None, incar_out=None)

        path = os.path.join(self.parser.maindir, 'INCAR%s' % os.path.basename(
            self.parser.mainfile).strip('OUTCAR'))
        path = path if os.path.isfile(path) else os.path.join(
            self.parser.maindir, 'INCAR')
        incar = self._get_key_values(path)
        self._fix_incar(incar)
        self._incar['incar'] = incar
        return incar

    def get_incar_out(self):
        if self._incar is not None and self._incar.get('incar_out', None) is not None:
            return self._incar.get('incar_out')

        incar = dict()
        if self._incar is None:
            self._incar = dict(incar=None, incar_out=None)

        incar = self.parser.get('parameters', {})
        self._incar['incar_out'] = incar
        self._fix_incar(incar)
        return incar

    @property
    def calculations(self):
        if self._calculations is None:
            self._calculations = self.parser.get('calculation')
        return self._calculations

    @property
    def n_calculations(self):
        if isinstance(self.calculations, dict):
            return 1
        elif isinstance(self.calculations, list):
            return len(self.calculations)
        else:
            return 0

    @property
    def kpoints_info(self):
        if self._kpoints_info is None:
            self._kpoints_info = dict()
            kpts_occs = self.parser.get('kpoints')
            if kpts_occs is not None:
                kpts_occs = np.reshape(kpts_occs, (len(kpts_occs) // 4, 4)).T
                self._kpoints_info['k_mesh_points'] = kpts_occs[0:3].T
                self._kpoints_info['k_mesh_weights'] = kpts_occs[3].T

        return self._kpoints_info

    @property
    def n_bands(self):
        if self._n_bands is None:
            for n in range(self.n_calculations):
                val = self.parser.get('calculation', [{}] * (n + 1))[n].get(
                    'eigenvalues', [None])[0]
                if val is not None:
                    self._n_bands = len(val) // 3
                    break
            if self._n_bands is None:
                # check consistency with eigenvalues
                self._n_bands = self.incar.get('NBANDS', 0)
        return self._n_bands

    @property
    def n_dos(self):
        if self._n_dos is None:
            path = os.path.join(self.parser.maindir, 'DOSCAR%s' % os.path.basename(
                self.parser.mainfile).strip('OUTCAR'))
            path = path if os.path.isfile(path) else os.path.join(
                self.parser.maindir, 'DOSCAR')
            with open(path) as f:
                for _ in range(6):
                    line = f.readline()
                self._n_dos = int(line.split()[2])
            if self._n_dos is None:
                self._n_dos = self._incar.get('NEDOS', 0)
        return self._n_dos

    @property
    def atom_info(self):
        if self._atom_info is None:
            self._atom_info = {}

            ions = self.parser.get('ions_per_type', [])
            species = self.parser.get('species', [])
            ions = [ions] if isinstance(ions, int) else ions
            ions = [int(i) for i in ions]
            mass_valence = self.parser.get('mass_valence', [])
            if len(ions) != len(species):
                # get it from POSCAR
                path = os.path.join(self.parser.maindir, 'POSCAR%s' % os.path.basename(
                    self.parser.mainfile).strip('OUTCAR'))
                path = path if os.path.isfile(path) else os.path.join(
                    self.parser.maindir, 'POSCAR')
                if os.path.isfile(path):
                    with open(path) as f:
                        for _ in range(7):
                            line = f.readline()
                            try:
                                ions = [int(n) for n in line.split()]
                            except Exception:
                                pass
            ions = [i for i in ions if not isinstance(i, str)]
            if len(ions) != len(species):
                self.parser.logger.error('Inconsistent number of ions and species.')
                return self._atom_info

            self._atom_info['n_atoms'] = sum(ions)
            self._atom_info['n_types'] = len(species)

            element = []
            atomtype = []
            for n in range(len(ions)):
                element.extend([str(species[n][1])] * ions[n])
                atomtype.extend([(n + 1)] * ions[n])
            self._atom_info['atoms'] = dict(element=element, atomtype=atomtype)
            self._atom_info['atomtypes'] = dict(
                atomspertype=ions, element=[s[1] for s in species],
                mass=[m[0] for m in mass_valence], valence=[m[1] for m in mass_valence],
                pseudopotential=[s[0] for s in species])

        return self._atom_info

    def get_n_scf(self, n_calc):
        return len(self.parser.get(
            'calculation', [{}] * (n_calc + 1))[n_calc].get('scf_iteration', []))

    def get_structure(self, n_calc):
        cell = self.parser.get(
            'calculation', [{}] * (n_calc + 1))[n_calc].get('lattice_vectors', [None])[0]
        positions = self.parser.get(
            'calculation', [{}] * (n_calc + 1))[n_calc].get('positions_forces', [None])[0]
        selective = None
        nose = None

        if cell is None:
            # get it from initialization
            cell = self.parser.get('lattice_vectors', [None])[0]
        if positions is None:
            positions = self.parser.get('positions', None)

        if positions is not None:
            positions = positions * ureg.angstrom
        if cell is not None:
            cell = cell * ureg.angstrom

        return dict(cell=cell, positions=positions, selective=selective, nose=nose)

    def get_energies(self, n_calc, n_scf):
        energies = dict()
        multiplier = 1.0
        if n_scf is None:
            section = self.parser.get(
                'calculation', [{}] * (n_calc + 1))[n_calc].get('energies', {})
            # final energies are per-atom
            multiplier = self.atom_info.get(
                'n_atoms', len(self.get_structure(n_calc).get('positions')))
        else:
            section = self.parser.get('calculation', [{}] * (
                n_calc + 1))[n_calc].get('scf_iteration', [{}] * (n_scf + 1))[n_scf]
        for key in ['energy_total', 'energy_T0', 'energy_entropy0']:
            val = section.get(key)
            if val is not None:
                energies[key] = val * multiplier

        energies.update(section.get('energy_components', {}))
        return energies

    def get_forces_stress(self, n_calc):
        forces = self.parser.get('calculation', [{}] * (n_calc + 1))[n_calc].get(
            'positions_forces', [None, None])[1]
        stress = self.parser.get('calculation', [{}] * (n_calc + 1))[n_calc].get(
            'stress', None)

        return forces, stress

    def get_eigenvalues(self, n_calc):
        n_kpts = len(self.kpoints_info.get('k_mesh_points', []))
        eigenvalues = self.parser.get(
            'calculation', [{}] * (n_calc + 1))[n_calc].get('eigenvalues')

        if eigenvalues is None:
            return
        n_eigs = len(eigenvalues) // (self.ispin * n_kpts)
        try:
            eigenvalues = np.reshape(eigenvalues, (n_eigs, self.ispin, n_kpts, self.n_bands, 3))
        except Exception:
            self.parser.logger.error('Error reading eigenvalues')
            return
        # eigenvalues can also be printed every scf iteration but we only save the
        # last one, which corresponds to the calculation
        eigenvalues = np.transpose(eigenvalues)[1:].T[-1]
        return eigenvalues

    def get_total_dos(self, n_calc):
        dos_energies = dos_values = dos_integrated = e_fermi = None

        if n_calc != (self.n_calculations - 1):
            return dos_energies, dos_values, dos_integrated, e_fermi
        path = os.path.join(self.parser.maindir, 'DOSCAR%s' % os.path.basename(
            self.parser.mainfile).strip('OUTCAR'))
        path = path if os.path.isfile(path) else os.path.join(
            self.parser.maindir, 'DOSCAR')
        if not os.path.isfile(path):
            return dos_energies, dos_values, dos_integrated, e_fermi

        dos = []
        n_dos = 0
        with self.parser.open(path) as f:
            try:
                for i, line in enumerate(f):
                    if i < 5:
                        continue
                    if i == 5:
                        e_fermi = float(line.split()[1])
                        n_dos = int(line.split()[2])
                    if i > 5:
                        dos.append([float(v) for v in line.split()])
                    if i >= n_dos + 5:
                        break
            except Exception:
                self.parser.logger.error('Error reading DOSCAR')

        if not dos:
            return dos_energies, dos_values, dos_integrated, e_fermi

        # DOSCAR fomat (spin) energy dos_up dos_down integrated_up integrated_down
        dos = np.transpose(dos)
        dos_energies = dos[0]
        cell = self.get_structure(n_calc)['cell']
        volume = np.abs(np.linalg.det(cell.magnitude))
        dos_values = dos[1: 1 + self.ispin] * volume
        dos_integrated = dos[1 + self.ispin: 2 * self.ispin + 1]

        return dos_energies, dos_values, dos_integrated, e_fermi

    def get_partial_dos(self, n_calc):
        n_atoms = self.atom_info['n_atoms']
        dos = fields = None
        if n_calc != (self.n_calculations - 1):
            return dos, fields
        path = os.path.join(self.parser.maindir, 'DOSCAR%s' % os.path.basename(
            self.parser.mainfile).strip('OUTCAR'))
        path = path if os.path.isfile(path) else os.path.join(
            self.parser.maindir, 'DOSCAR')
        if not os.path.isfile(path):
            return dos, fields

        dos = []
        n_dos = 0
        atom = 1
        with self.parser.open(path) as f:
            for i, line in enumerate(f):
                if i == 0:
                    if int(line.split()[2]) != 1:
                        return None, None
                elif i < 5:
                    continue
                elif i == 5:
                    n_dos = int(line.split()[2])
                if i == ((n_dos + 1) * atom) + 5:
                    atom += 1
                    continue
                if i > (n_dos + 6):
                    dos.append([float(v) for v in line.split()])
                if i >= ((n_dos + 1) * (n_atoms + 1) + 5):
                    break
        if len(dos) == 0:
            return None, None

        dos = np.transpose(dos)[1:]
        n_lm = len(dos) // self.ispin
        try:
            dos = np.reshape(dos, (n_lm, self.ispin, n_atoms, n_dos))
        except Exception:
            self.parser.logger.error('Error reading partial dos.')
            return None, None

        if n_lm == 3:
            fields = ['s', 'p', 'd']
        elif n_lm == 9:
            fields = ['s', 'py', 'pz', 'px', 'dxy', 'dyz', 'dz2', 'dxz', 'dx2']
        elif n_lm == 16:
            fields = [
                's', 'py', 'pz', 'px', 'dxy', 'dyz', 'dz2', 'dxz', 'dx2', 'f-3',
                'f-2', 'f-1', 'f0', 'f1', 'f2', 'f3']
        else:
            fields = [None] * n_lm
            self.parser.logger.warn(
                'Cannot determine lm fields for n_lm', data=dict(n_lm=n_lm))

        return dos, fields

    def is_converged(self, n_calc):
        return self.parser.get('calculation', [{}] * (n_calc + 1))[n_calc].get(
            'convergence') is not None


class RunXmlContentHandler(ContentHandler):
    def __init__(self):
        self._text = ''
        self._path = []

        self._data = {}
        self.n_calculations = 0

        # data, attrs, last_sibling, last_sibling_index
        self._stack = [(self._data, {}, None, -1)]

    def startElement(self, tag, attrs):
        data, last_attrs, last_sibling, last_sibling_index = self._stack[-1]

        name = attrs.get('name')
        if not name and tag in ('i', 'v', 'r', 'c'):
            self._stack.append((data, attrs, None, -1,))

        else:
            if tag == last_sibling:
                index = last_sibling_index + 1
            else:
                index = 0

            self._stack[-1] = (data, last_attrs, tag, index)

            if name:
                segment = f'{tag}[@name="{name}"]'
            else:
                segment = f'{tag}[{index}]'

            self._stack.append((data.setdefault(segment, {}), attrs, None, -1,))

    def endElement(self, tag):
        text = self._text
        self._text = ''

        data, attrs, _, _ = self._stack.pop()

        if tag == 'calculation':
            self.n_calculations += 1

        data.setdefault('_data', []).append({tag: text, **attrs})

    def clear_stack(self):
        while len(self._stack) > 0:
            self.endElement(self._stack[-1][2])

    def characters(self, content):
        self._text += content

    def _combine_sub_tree(self, data, results):
        for key, value in data.items():
            if key == '_data':
                results.extend(value)
            else:
                self._combine_sub_tree(value, results)

        return results

    def __getitem__(self, key):
        try:
            data = self._data
            segments = key.strip('/').split('/')
            for segment in segments:
                data = data[segment]

            return self._combine_sub_tree(data, [])
        except KeyError:
            return []


class RunFileParser(FileParser):

    def parse(self):
        parser = make_parser()
        content_handler = RunXmlContentHandler()
        parser.setContentHandler(content_handler)
        try:
            parser.parse(self.mainfile_obj)
        except Exception as e:
            # support broken XML structure
            if self.logger:
                self.logger.warning('could not parse all xml', exc_info=e)
            content_handler.clear_stack()

        self._results = content_handler

    @property
    def results(self):
        return self._results

    @property
    def n_calculations(self):
        return self._results.n_calculations


class RunContentParser(ContentParser):
    def __init__(self):
        super().__init__()
        self.parser = None
        self._re_attrib = re.compile(r'\[@name="(\w+)"\]')
        self._dtypes = {'string': str, 'int': int, 'logical': bool, '': float, 'float': float}

    def init_parser(self, filepath, logger):
        self.parser = RunFileParser(filepath, logger)

        super().init_parser(filepath, logger)

        self._scf_energies = dict()
        self._n_scf = None

        self.parser.parse()

    def _get_key_values(self, path, repeats=False, array=False):
        def parse_float_str_vector(str_vector: List[str]):
            return [
                'nan' if '*' in x else x
                for x in str_vector]

        root, base_name = path.strip('/').rsplit('/', 1)

        attrib = re.search(self._re_attrib, base_name)
        if attrib:
            attrib = attrib.group(1)
            base_name = re.sub(self._re_attrib, '', base_name)

        # removes all non indexed segments from the path to collect data from the
        # whole remaining sub-tree.
        sections = []
        for section in root.split('/'):
            if not section.endswith(']'):
                break
            sections.append(section)
        root = '/'.join(sections) if sections else root

        data = [
            (d.get(base_name), d.get('name', ''), d.get('type', ''),)
            for d in self.parser.results[root]]

        if len(data) == 0:
            return dict()

        result = dict()
        if array:
            value = [
                parse_float_str_vector(item[0].split())
                for item in data if item[0]]
            value = [d[0] if len(d) == 1 and not repeats else d for d in value]
            dtype = data[0][2]
            try:
                result[base_name] = np.array(value, dtype=self._dtypes.get(dtype, float))
            except Exception:
                self.parser.logger.error('Error parsing array.')

        else:
            for value, name, dtype in data:
                if not value:
                    continue
                if attrib and name != attrib:
                    continue
                name = name if name else base_name
                dtype = self._dtypes.get(dtype, str)
                value = value.split()
                if dtype == bool:
                    value = [v == 'T' for v in value]
                if dtype == float:
                    # prevent nan printouts
                    value = parse_float_str_vector(value)
                # using numpy array does not work
                value = convert(value, dtype)
                value = value[0] if len(value) == 1 else value
                result.setdefault(name, [])
                result[name].append(value)
            if not repeats:
                for key, val in result.items():
                    result[key] = val[0] if len(val) == 1 else val

        return result

    @property
    def header(self):
        if self._header is None:
            self._header = self._get_key_values('/modeling[0]/generator[0]/i')
            for key, val in self._header.items():
                if not isinstance(val, str):
                    self._header[key] = ' '.join(val)
        return self._header

    def get_incar(self):
        if self._incar is not None and self._incar.get('incar', None) is not None:
            return self._incar.get('incar')

        if self._incar is None:
            self._incar = dict(incar=None, incar_out=None)
        incar = self._get_key_values('/modeling[0]/incar[0]/i')
        incar.update(self._get_key_values('/modeling[0]/incar[0]/v'))
        self._fix_incar(incar)
        self._incar['incar'] = incar
        return incar

    def get_incar_out(self):
        if self._incar is not None and self._incar.get('incar_out', None) is not None:
            return self._incar.get('incar_out')

        incar = dict()
        if self._incar is None:
            self._incar = dict(incar=None, incar_out=None)
        incar.update(self._get_key_values('/modeling[0]/parameters[0]/i'))
        incar.update(self._get_key_values('/modeling[0]/parameters[0]/v'))

        self._incar['incar_out'] = incar
        self._fix_incar(incar)
        return incar

    @property
    def n_calculations(self):
        return self.parser.n_calculations

    @property
    def kpoints_info(self):
        if self._kpoints_info is None:
            self._kpoints_info = dict()
            # initialize parsing of k_points
            method = self._get_key_values(
                '/modeling[0]/kpoints[0]/generation[0]/param')
            if method:
                self._kpoints_info['x_vasp_k_points_generation_method'] = method['param']
            divisions = self._get_key_values(
                '/modeling[0]/kpoints[0]/generation[0]/i[@name="divisions"]')
            if divisions:
                self._kpoints_info['divisions'] = divisions['divisions']
            volumeweight = self._get_key_values('/modeling[0]/kpoints[0]/generation[0]/i[@name="volumeweight"]')
            if volumeweight:
                volumeweight = (volumeweight['volumeweight'] * ureg.angstrom ** 3).to('m**3')
                # TODO set propert unit in metainfo
                self._kpoints_info['x_vasp_tetrahedron_volume'] = volumeweight.magnitude
            points = self._get_key_values(
                '/modeling[0]/kpoints[0]/varray[@name="kpointlist"]/v', array=True)
            if points:
                self._kpoints_info['k_mesh_points'] = points['v']
            weights = self._get_key_values(
                '/modeling[0]/kpoints[0]/varray[@name="weights"]/v', array=True)
            if weights:
                self._kpoints_info['k_mesh_weights'] = weights['v']
            tetrahedrons = self._get_key_values(
                '/modeling[0]/kpoints[0]/varray[@name="tetrahedronlist"]/v', array=True)
            if tetrahedrons:
                self._kpoints_info['x_vasp_tetrahedrons_list'] = tetrahedrons['v']
        return self._kpoints_info

    @property
    def n_bands(self):
        if self._n_bands is None:
            for n in range(self.n_calculations - 1, -1, -1):
                val = self._get_key_values(
                    '/modeling[0]/calculation[%d]/eigenvalues[0]/array[0]/set[0]/set[0]/set[0]/r' % n)
                if val:
                    self._n_bands = len(val['r'])
                    break
            if self._n_bands is None:
                self._n_bands = self.incar.get('NBANDS', 0)
        return self._n_bands

    @property
    def n_dos(self):
        if self._n_dos is None:
            for n in range(self.n_calculations - 1, -1, -1):
                val = self._get_key_values(
                    '/modeling[0]/calculation[%d]/dos[0]/total[0]/array[0]/set[0]/set[0]/r' % n)
                if val:
                    self._n_dos = len(val['r'])
                    break
            if self._n_dos is None:
                self._n_dos = self._incar.get('NEDOS', 0)
        return self._n_dos

    @property
    def atom_info(self):
        if self._atom_info is None:
            self._atom_info = {}
            root = '/modeling[0]/atominfo[0]'
            self._atom_info['n_atoms'] = int(self._get_key_values(
                f'{root}/atoms[0]/atoms').get('atoms', 0))
            self._atom_info['n_types'] = int(self._get_key_values(
                f'{root}/types[0]/types').get('types', 0))

            number = dict(atoms=self._atom_info['n_atoms'], atomtypes=self._atom_info['n_types'])
            for key in ['atoms', 'atomtypes']:
                rcs = self._get_key_values(
                    f'{root}/array[@name="%s"]/set[0]/c' % key, repeats=True).get('c', [])
                fields = self._get_key_values(
                    f'{root}/array[@name="%s"]/field' % key, repeats=True).get('field', [])
                array_info = {}
                if len(rcs) != len(fields) * number[key]:
                    self._atom_info = array_info
                    continue
                for n in range(number[key]):
                    for i in range(len(fields)):
                        array_info.setdefault(fields[i], [])
                        array_info[fields[i]].append(rcs[n * len(fields) + i])
                self._atom_info[key] = array_info
        return self._atom_info

    def get_n_scf(self, n_calc):
        if self._n_scf is None:
            self._n_scf = [None] * self.n_calculations
        if self._n_scf[n_calc] is None:
            self._n_scf[n_calc] = len(self._get_key_values(
                '/modeling[0]/calculation[%d]/scstep/time[@name="total"]' % n_calc).get('total', []))
        return self._n_scf[n_calc]

    def get_structure(self, n_calc):
        structure = '/modeling[0]/calculation[%d]/structure[0]' % n_calc
        cell = self._get_key_values(
            f'{structure}/crystal[0]/varray[@name="basis"]/v', array=True).get('v', None)
        if cell is None:
            structure = '/modeling[0]/structure[@name="finalpos"]'
            cell = self._get_key_values(
                f'{structure}/crystal[0]/varray[@name="basis"]/v', array=True).get('v', None)

        positions = self._get_key_values(
            f'{structure}/varray[@name="positions"]/v', array=True).get('v', None)
        selective = self._get_key_values(
            f'{structure}/varray[@name="selective"]/v', array=True).get('v', None)
        nose = self._get_key_values(
            f'{structure}/nose/v', array=True).get('v', None)

        if positions is not None:
            positions = np.dot(positions, cell) * ureg.angstrom
        if cell is not None:
            cell = cell * ureg.angstrom

        return dict(cell=cell, positions=positions, selective=selective, nose=nose)

    def get_energies(self, n_calc, n_scf):
        calculation = '/modeling[0]/calculation[%d]' % n_calc
        if n_scf is None:
            # we need to cache this separately for faster access
            self._scf_energies = self._get_key_values(
                f'{calculation}/scstep/i', repeats=True)
            return self._get_key_values(f'{calculation}/energy[0]/i')
        else:
            scf_energies = dict()
            for key, val in self._scf_energies.items():
                try:
                    scf_energies[key] = val[n_scf]
                except Exception:
                    scf_energies[key] = val[-1] if n_scf == self.get_n_scf(n_calc) - 1 else None
            return scf_energies

    def get_forces_stress(self, n_calc):
        forces = self._get_key_values(
            '/modeling[0]/calculation[%d]/varray[@name="forces"]/v' % n_calc,
            array=True).get('v', None)
        stress = self._get_key_values(
            '/modeling[0]/calculation[%d]/varray[@name="stress"]/v' % n_calc,
            array=True).get('v', None)
        return forces, stress

    def get_eigenvalues(self, n_calc):
        n_kpts = len(self.kpoints_info.get('k_mesh_points', []))
        root = '/modeling[0]/calculation[%s]/eigenvalues[0]/array[0]/set[0]' % n_calc
        eigenvalues = self._get_key_values(
            f'{root}/r', array=True).get('r', None)
        if eigenvalues is None:
            return

        try:
            eigenvalues = np.reshape(eigenvalues, (self.ispin, n_kpts, self.n_bands, 2))
        except Exception:
            self.parser.logger.error('Error reading eigenvalues')
            return

        return eigenvalues

    def get_total_dos(self, n_calc):
        dos_energies = dos_values = dos_integrated = e_fermi = None

        root = '/modeling[0]/calculation[%d]/dos[0]' % n_calc
        dos = self._get_key_values(
            rf'{root}/total[0]/array[0]/set[0]/set/r', array=True).get('r', None)

        if dos is None:
            return dos_energies, dos_values, dos_integrated, e_fermi

        e_fermi = self._get_key_values(
            f'{root}/i[@name="efermi"]').get('efermi', 0.0)
        n_dos = 1 if isinstance(e_fermi, float) else len(e_fermi)
        if n_dos > 1:
            e_fermi = e_fermi[-1]
            self.parser.logger.warn('Multiple dos found, will read only last.')

        try:
            dos = np.reshape(dos, (n_dos, self.ispin, len(dos) // self.ispin // n_dos, 3))[-1]
        except Exception:
            self.parser.logger.error('Error reading total dos.')
            return dos_energies, dos_values, dos_integrated, e_fermi

        dos = np.transpose(dos)
        dos_energies = dos[0].T[0]
        dos_values = dos[1].T
        dos_integrated = dos[2].T

        # unit of dos in vasprun is states/eV/cell
        cell = self.get_structure(n_calc)['cell']
        volume = np.abs(np.linalg.det(cell.magnitude)) * ureg.angstrom ** 3
        dos_values *= volume.to('m**3').magnitude

        return dos_energies, dos_values, dos_integrated, e_fermi

    def get_partial_dos(self, n_calc):
        n_atoms = self.atom_info['n_atoms']
        root = '/modeling[0]/calculation[%d]/dos[0]/partial[0]/array[0]' % n_calc

        dos = self._get_key_values(f'{root}/r').get('r', None)

        if dos is None:
            return None, None

        # TODO use atomprojecteddos section
        fields = self._get_key_values(f'{root}/field').get('field', [])
        try:
            dos = np.reshape(dos, (n_atoms, self.ispin, len(dos) // (n_atoms * self.ispin), len(fields)))
        except Exception:
            self.parser.logger.error('Error reading partial dos.')
            return None, None

        fields = [field for field in fields if field != 'energy']
        dos = np.transpose(dos)[1:]
        dos = np.transpose(dos, axes=(0, 2, 3, 1))

        return dos, fields


class VASPParser(FairdiParser):
    def __init__(self):
        super().__init__(
            name='parsers/vasp', code_name='VASP', code_homepage='https://www.vasp.at/',
            mainfile_mime_re=r'(application/.*)|(text/.*)',
            mainfile_name_re=r'.*[^/]*xml[^/]*',  # only the alternative mainfile name should match
            mainfile_contents_re=(
                r'^\s*<\?xml version="1\.0" encoding="ISO-8859-1"\?>\s*'
                r'?\s*<modeling>'
                r'?\s*<generator>'
                r'?\s*<i name="program" type="string">\s*vasp\s*</i>'
                r'?|^\svasp[\.\d]+.+?(?:\(build|complex)[\s\S]+?executed on'),
            supported_compressions=['gz', 'bz2', 'xz'], mainfile_alternative=True)

        self._vasprun_parser = RunContentParser()
        self._outcar_parser = OutcarContentParser()

    def init_parser(self, filepath, logger):
        self.parser = self._vasprun_parser if '.xml' in filepath else self._outcar_parser
        self.parser.init_parser(filepath, logger)

    def parse_incarsout(self):
        sec_method = self.archive.run[-1].method[-1]

        incar_parameters = self.parser.get_incar_out()
        for key, val in incar_parameters.items():
            if isinstance(val, np.ndarray):
                val = list(val)
            incar_parameters[key] = val
        try:
            sec_method.x_vasp_incar_out = incar_parameters
        except Exception:
            self.logger.warn('Error setting metainfo defintion x_vasp_incar_out', data=dict(
                incar=incar_parameters))

        prec = 1.3 if 'acc' in self.parser.incar.get('PREC', '') else 1.0
        sec_basis = sec_method.m_create(BasisSet)
        sec_basis.type = 'plane waves'
        sec_basis_set_cell_dependent = sec_basis.m_create(BasisSetCellDependent)
        sec_basis_set_cell_dependent.kind = 'plane waves'
        sec_basis_set_cell_dependent.planewave_cutoff = self.parser.incar.get(
            'ENMAX', self.parser.incar.get('ENCUT', 0.0)) * prec * ureg.eV

    def parse_method(self):
        sec_method = self.archive.run[-1].m_create(Method)
        sec_dft = sec_method.m_create(DFT)

        # input incar
        incar_parameters = self.parser.get_incar()
        for key, val in incar_parameters.items():
            if isinstance(val, np.ndarray):
                val = list(val)
            incar_parameters[key] = val
        try:
            sec_method.x_vasp_incar_in = incar_parameters
        except Exception:
            self.logger.warn('Error setting metainfo defintion x_vasp_incar_in', data=dict(
                incar=incar_parameters))

        sec_method.electronic = Electronic(method='DFT+U' if self.parser.incar.get(
            'LDAU', False) else 'DFT')

        # kpoints
        for key, val in self.parser.kpoints_info.items():
            if val is not None:
                try:
                    setattr(sec_method, key, val)
                except Exception:
                    self.logger.warn('Error setting metainfo', data=dict(key=key))

        # atom properties
        atomtypes = self.parser.atom_info.get('atomtypes', {})
        element = atomtypes.get('element', [])
        atom_counts = {e: 0 for e in element}
        for i in range(len(element)):
            sec_method_atom_kind = sec_method.m_create(AtomParameters)
            atom_number = ase.data.atomic_numbers.get(element[i], 0)
            sec_method_atom_kind.atom_number = atom_number
            atom_label = '%s%d' % (
                element[i], atom_counts[element[i]]) if atom_counts[element[i]] > 0 else element[i]
            sec_method_atom_kind.label = str(atom_label)
            sec_method_atom_kind.mass = atomtypes.get('mass', [1] * (i + 1))[i] * ureg.amu
            sec_method_atom_kind.n_valence_electrons = atomtypes.get(
                'valence', [0] * (i + 1))[i]
            pseudopotential = atomtypes.get('pseudopotential')[i]
            pseudopotential = ' '.join(pseudopotential) if isinstance(
                pseudopotential, list) else pseudopotential
            sec_method_atom_kind.pseudopotential_name = str(pseudopotential)
            atom_counts[element[i]] += 1
        sec_method.x_vasp_atom_kind_refs = sec_method.atom_parameters

        self.parse_incarsout()

        sec_xc_functional = sec_dft.m_create(XCFunctional)
        if self.parser.incar.get('LHFCALC', False):
            gga = self.parser.incar.get('GGA', 'PE')
            aexx = self.parser.incar.get('AEXX', 0.0)
            aggax = self.parser.incar.get('AGGAX', 1.0)
            aggac = self.parser.incar.get('AGGAC', 1.0)
            aldac = self.parser.incar.get('ALDAC', 1.0)
            hfscreen = self.parser.incar.get('HFSCREEN', 0.0)

            if hfscreen == 0.2:
                sec_xc_functional.hybrid.append(Functional(name='HYB_GGA_XC_HSE06'))
            elif hfscreen == 0.3:
                sec_xc_functional.hybrid.append(Functional(name='HYB_GGA_XC_HSE03'))
            elif gga == 'B3' and aexx == 0.2 and aggax == 0.72 and aggac == 0.81 and aldac == 0.19:
                sec_xc_functional.hybrid.append(Functional(name='HYB_GGA_XC_B3LYP3'))
            elif aexx == 1.0 and aldac == 0.0 and aggac == 0.0:
                sec_xc_functional.contributions.append(Functional(name='X_HF'))
            elif gga == 'PE':
                sec_xc_functional.hybrid.append(Functional(name='HYB_GGA_XC_PBEH'))
            else:
                sec_xc_functional.hybrid.append(Functional(
                    name='HYB_GGA_XC_%s' % gga, parameters=dict(
                        aexx=aexx, aggax=aggax, aggac=aggac, aldac=aldac)))

        else:
            metagga = self.parser.incar.get('METAGGA')
            if metagga:
                xc_functionals = self.parser.xc_functional_mapping.get(metagga, [metagga])
            else:
                xc_functionals = self.parser.xc_functional_mapping.get(self.parser.incar.get('GGA'), [])
            for xc_functional in xc_functionals:
                if '_X_' in xc_functional or xc_functional.endswith('_X'):
                    sec_xc_functional.exchange.append(Functional(name=xc_functional))
                elif '_C_' in xc_functional or xc_functional.endswith('_C'):
                    sec_xc_functional.correlation.append(Functional(name=xc_functional))
                elif 'HYB' in xc_functional:
                    sec_xc_functional.hybrid.append(Functional(name=xc_functional))
                else:
                    sec_xc_functional.contributions.append(Functional(name=xc_functional))

        # convergence thresholds
        tolerance = self.parser.incar.get('EDIFF')
        if tolerance is not None:
            sec_method.scf = Scf(threshold_energy_change=tolerance * ureg.eV)

    def parse_workflow(self):
        sec_workflow = self.archive.m_create(Workflow)

        ibrion = -1
        incar = self.archive.run[-1].method[-1].x_vasp_incar_out
        if incar is not None:
            nsw = incar.get('NSW')
            ibrion = -1 if nsw == 0 else incar.get('IBRION', 0)

        if ibrion == -1:
            sec_workflow.type = 'single_point'
            sec_workflow.m_create(SinglePoint)
        elif ibrion == 0:
            sec_workflow.type = 'molecular_dynamics'
            sec_workflow.m_create(MolecularDynamics)
        else:
            sec_workflow.type = 'geometry_optimization'
            task = sec_workflow.m_create(GeometryOptimization)
            tolerance = self.parser.incar.get('EDIFFG')
            if tolerance is not None:
                if tolerance > 0:
                    task.convergence_tolerance_energy_difference = tolerance * ureg.eV
                else:
                    task.convergence_tolerance_force_maximum = abs(tolerance) * ureg.eV / ureg.angstrom

    def parse_configurations(self):
        sec_run = self.archive.run[-1]

        def parse_system(n_calc):
            sec_system = sec_run.m_create(System)
            sec_atoms = sec_system.m_create(Atoms)

            structure = self.parser.get_structure(n_calc)
            cell = structure.get('cell', None)
            if cell is not None:
                sec_atoms.lattice_vectors = cell

            sec_atoms.periodic = [True] * 3
            sec_atoms.labels = self.parser.atom_info.get('atoms', {}).get('element', [])

            positions = structure.get('positions', None)
            if positions is not None:
                sec_atoms.positions = positions

            selective = structure.get('selective', None)
            if selective is not None:
                selective = [[s[i] == 'T' for i in range(len(s))] for s in selective]
                sec_system.x_vasp_selective_dynamics = selective

            nose = structure.get('nose')
            if nose is not None:
                sec_system.x_vasp_nose_thermostat = nose

            return sec_system

        def parse_energy(n_calc, n_scf=None):
            if n_scf is None:
                section = sec_run.m_create(Calculation)
            else:
                section = sec_run.calculation[-1].m_create(ScfIteration)

            energies = self.parser.get_energies(n_calc, n_scf)
            sec_energy = section.m_create(Energy)
            for key, val in energies.items():
                metainfo_key = self.parser.metainfo_mapping.get(key, None)
                if val is None or metainfo_key is None:
                    continue

                try:
                    val = val * ureg.eV
                    if metainfo_key.startswith('energy_'):
                        sec_energy.m_add_sub_section(getattr(
                            Energy, metainfo_key.replace('energy_', '').lower()), EnergyEntry(value=val))
                    else:
                        setattr(section, metainfo_key, val)
                except Exception:
                    self.logger.warn('Error setting metainfo', data=dict(key=key))

            return section

        def parse_eigenvalues(n_calc):
            eigenvalues = self.parser.get_eigenvalues(n_calc)
            if eigenvalues is None:
                return

            sec_scc = sec_run.calculation[-1]
            eigenvalues = np.transpose(eigenvalues)
            eigs = eigenvalues[0].T
            occs = eigenvalues[1].T
            kpoints = self.parser.kpoints_info.get('k_mesh_points', [])

            # get valence(conduction) and maximum(minimum)
            # we have a case where no band is occupied, i.e. valence_max should be below
            # min(eigs)
            valence_max, conduction_min = [], []
            for i in range(len(eigs)):
                occupied = [eigs[i, o[0], o[1]] for o in np.argwhere(occs[i] >= 0.5)]
                valence_max.append(np.amin(eigs[i]) - 1.0 if not occupied else max(occupied))
                unoccupied = [eigs[i, o[0], o[1]] for o in np.argwhere(occs[i] < 0.5)]
                conduction_min.append(np.amin(eigs[i]) - 1.0 if not unoccupied else min(unoccupied))
            sec_scc.energy.highest_occupied = max(valence_max) * ureg.eV
            sec_scc.energy.lowest_unoccupied = min(conduction_min) * ureg.eV

            if self.parser.kpoints_info.get('x_vasp_k_points_generation_method', None) == 'listgenerated':
                # I removed normalization since imho it should be done by normalizer
                sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
                for n in range(len(eigs)):
                    sec_band_gap = sec_k_band.m_create(BandGap)
                    sec_band_gap.energy_highest_occupied = valence_max[n] * ureg.eV
                    sec_band_gap.energy_lowest_unoccupied = conduction_min[n] * ureg.eV
                divisions = self.parser.kpoints_info.get('divisions', None)
                if divisions is None:
                    return
                n_segments = len(kpoints) // divisions
                kpoints = np.reshape(kpoints, (n_segments, divisions, 3))
                eigs = np.reshape(eigs, (
                    self.parser.ispin, n_segments, divisions, self.parser.n_bands))
                occs = np.reshape(occs, (
                    self.parser.ispin, n_segments, divisions, self.parser.n_bands))
                eigs = np.transpose(eigs, axes=(1, 0, 2, 3)) * ureg.eV
                occs = np.transpose(occs, axes=(1, 0, 2, 3))
                for n in range(n_segments):
                    sec_k_band_segment = sec_k_band.m_create(BandEnergies)
                    sec_k_band_segment.kpoints = kpoints[n]
                    sec_k_band_segment.energies = eigs[n]
                    sec_k_band_segment.occupations = occs[n]
            else:
                eigs = eigs * ureg.eV
                sec_eigenvalues = sec_scc.m_create(BandEnergies)
                sec_eigenvalues.kpoints = kpoints
                sec_eigenvalues.energies = eigs
                sec_eigenvalues.occupations = occs

        def parse_dos(n_calc):
            energies, values, integrated, efermi = self.parser.get_total_dos(n_calc)

            # TODO: I do not know how the f-orbitals are arranged
            lm_converter = {
                's': [0, 0], 'p': [1, -1], 'px': [1, 0], 'py': [1, 1], 'pz': [1, 2],
                'd': [2, -1], 'dx2': [2, 0], 'dxy': [2, 1], 'dxz': [2, 2], 'dy2': [2, 3],
                'dyz': [2, 4], 'dz2': [2, 5], 'f': [3, -1], 'f-3': [3, 0], 'f-2': [3, 1],
                'f-1': [3, 2], 'f0': [3, 3], 'f1': [3, 4], 'f2': [3, 5], 'f3': [3, 6]}

            # total dos
            if values is not None:
                sec_scc = sec_run.calculation[-1]
                sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
                sec_dos.energies = energies * ureg.eV
                sec_dos.energy_fermi = efermi * ureg.eV

                for spin in range(len(values)):
                    sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
                    sec_dos_values.value = values[spin] / ureg.eV
                    sec_dos_values.value_integrated = integrated[spin]

                # partial dos
                dos, fields = self.parser.get_partial_dos(n_calc)
                if dos is not None:
                    for lm in range(len(dos)):
                        for spin in range(len(dos[lm])):
                            for atom in range(len(dos[lm][spin])):
                                sec_dos_values = sec_dos.m_create(DosValues, Dos.atom_projected)
                                sec_dos_values.m_kind = 'polynomial'
                                sec_dos_values.lm = lm_converter.get(fields[lm], [-1, -1])
                                sec_dos_values.spin = spin
                                sec_dos_values.atom_index = atom
                                sec_dos_values.value = dos[lm][spin][atom] / ureg.eV

            if efermi is not None:
                sec_run.calculation[-1].energy.fermi = efermi * ureg.eV

        for n in range(self.parser.n_calculations):
            # energies
            sec_scc = parse_energy(n, None)
            for n_scf in range(self.parser.get_n_scf(n)):
                parse_energy(n, n_scf)

            # forces and stress
            forces, stress = self.parser.get_forces_stress(n)
            if forces is not None:
                try:
                    sec_scc.forces = Forces(total=ForcesEntry(value=forces * ureg.eV / ureg.angstrom))
                except Exception:
                    self.logger.error('Error parsing forces.')
            if stress is not None:
                try:
                    # TODO verify if stress unit in xml is also kbar
                    sec_scc.stress = Stress(total=StressEntry(value=stress * ureg.kbar))
                except Exception:
                    self.logger.error('Error parsing stress.')

            # structure
            sec_system = parse_system(n)
            sec_scc.system_ref = sec_system
            sec_scc.method_ref = sec_run.method[-1]

            # eigenvalues
            parse_eigenvalues(n)

            # dos
            parse_dos(n)

            # convergence
            converged = self.parser.is_converged(n)
            if converged:
                sec_scc.single_configuration_calculation_converged = converged

        if self.parser.n_calculations == 0:
            self.logger.warn('No calculation was parsed.')

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.init_parser(filepath, logger)

        sec_run = self.archive.m_create(Run)
        program_name = self.parser.header.get('program', '')
        if program_name.strip().upper() != 'VASP':
            sec_run.program = Program()
            self.logger.error('invalid program name', data=dict(program_name=program_name))
            return
        sec_run.program = Program(name='VASP')

        version = ' '.join([self.parser.header.get(key, '') for key in [
            'version', 'subversion', 'platform']]).strip()
        if version:
            sec_run.program.version = version

        date = self.parser.header.get('date')
        if date is not None:
            date = datetime.strptime(date.strip(), '%Y %m %d').date()
            time = self.parser.header.get('time', '0:0:0')
            time = datetime.strptime(time.strip(), '%H:%M:%S').timetz()
            dtime = datetime.combine(date, time) - datetime.utcfromtimestamp(0)
            sec_run.program.compilation_datetime = dtime.total_seconds()

        self.parse_method()

        self.parse_configurations()

        self.parse_workflow()
