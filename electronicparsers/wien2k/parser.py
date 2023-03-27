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
from ase.io import read as ioread
from ase import Atoms

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, DFT, Smearing, XCFunctional, Functional, KMesh, BasisSet
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Forces, ForcesEntry, ScfIteration, Energy, EnergyEntry, BandEnergies, Dos,
    DosValues
)
from nomad.datamodel.metainfo.workflow import Workflow
from .metainfo.wien2k import x_wien2k_section_equiv_atoms


class In0Parser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'xc_functional',
                r'(?:TOT|KXC|POT|MULT|COUL|EXCH)\s*([\w ]+)', dtype=str),
            Quantity('fft', r'FFT[\s\S]+?(\d+\s+\d+\s+\d+\s+[\d\.]+)')]


class In1Parser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity('wf_switch', r'(WFFIL|WFPRI|ENFIL|SUPWF)'),
            Quantity('rkmax', r'([\d\.]+\s*\d+\s*\d+).+K\-MAX', dtype=np.float64)]


class StructParser(TextParser):
    def __init__(self):
        super().__init__()
        self._units_map = {
            'b': ureg.bohr, 'a': ureg.angstrom}

    def init_quantities(self):
        re_float = r'[\d\.\-]+'
        re_lat = r'\d+\.\d{6}'
        self._quantities = [
            Quantity(
                'lattice',
                r'([\s\S]+?)\n *AT',
                sub_parser=TextParser(quantities=[
                    Quantity('nonequiv_atoms', r'NONEQUIV\.ATOMS\:\s*(\d+)', dtype=int),
                    Quantity('lattice', r'(\w+)\s*LATTICE'),
                    Quantity('calc_mode', r'(N*REL\S*)'),
                    Quantity(
                        'lattice_constants',
                        # fixed precision, sometimes no spaces
                        rf'({re_lat})\s*({re_lat})\s*({re_lat})\s*({re_lat})\s*({re_lat})\s*({re_lat})',
                        dtype=np.dtype(np.float64)),
                    Quantity(
                        'unit',
                        r'unit=(\w)',
                        str_operation=lambda x: self._units_map.get(x, ureg.bohr))])),
            Quantity(
                'atom',
                r'OM\s+\-*\d+\:\s*(X\=[\s\S]+?)LOCAL',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'positions',
                        rf'X\=({re_float})\s*Y=({re_float})\s*Z=({re_float})',
                        repeats=True, dtype=np.dtype(np.float64)),
                    Quantity('atom_name', r'(\n *[A-Z][a-z]*\d* +)'),
                    Quantity('NPT', r'NPT\s*\=\s*(\d+)', dtype=int),
                    Quantity('R0', r'R0\s*\=\s*(\d+)', dtype=int),
                    Quantity('Z', r'Z\:\s*([\d\.]+)', dtype=np.float64)]))]

    def get_atoms(self):
        '''
        Returns an ASE atoms representation of the structure.
        '''
        if self.mainfile is None:
            return

        try:
            return ioread(self.mainfile, format='struct')
        except Exception:
            # read it from parsed info
            if self.get('lattice') is None:
                return

            lattice_constants = self.get('lattice').get('lattice_constants')
            unit = self.get('lattice').get('unit', ureg.bohr)
            lattice_constants[:3] = (lattice_constants[:3] * unit).to('angstrom').magnitude
            scaled_positions = []
            numbers = []
            for atom in self.get('atom', []):
                positions = atom.get('positions', [])
                scaled_positions.extend(positions)
                numbers.extend([int(atom.get('Z', 0))] * len(positions))

            return Atoms(
                cell=lattice_constants, scaled_positions=scaled_positions, numbers=numbers, pbc=True)


class In2Parser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity('switch', r'(TOT|FOR|QTL|EFG|FERMI)'),
            Quantity('emin', r'([\d\.\- ]+)\s*EMIN'),
            Quantity('smearing', r'(GAUSS|ROOT|TEMP|TETRA|ALL)\s*([\d\.]+)'),
            Quantity('gmax', r'([\d\.\-]+)\s*GMAX')]


class DosParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_f = r'\-*\d+\.\d+'
        self._quantities = [
            Quantity('labels', r'# ENERGY +(.+)', flatten=False),
            Quantity('data', rf'({re_f} +{re_f}.*)', repeats=True, dtype=np.dtype(np.float64))]


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_float = r'[\d\.Ee\-\+]+'

        iteration_quantities = [
            Quantity(
                'NATO',
                r'(NATO\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'nr_of_independent_atoms',
                        r'(\d+)\s*INDEPENDENT', dtype=int),
                    Quantity(
                        'total_atoms',
                        r'(\d+)\s*TOTAL ATOMS IN UNITCELL', dtype=int),
                    Quantity('system_name', r'SUBSTANCE:\s*(.+)', flatten=False)])),
            Quantity(
                'POT',
                r'(POT\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'potential_option',
                        r'POTENTIAL OPTION\s*(.+)', dtype=str, flatten=False)])),
            Quantity(
                'LAT',
                r'(LAT\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity('lattice_const', r'LATTICE CONSTANTS=\s*([\d\. ]+)')])),
            Quantity(
                'VOL',
                r'(VOL\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'unit_cell_volume_bohr3',
                        rf'UNIT CELL VOLUME\s*\=\s*({re_float})',
                        dtype=np.float64),
                    Quantity('spinpolarization', r'((?:NON-)*SPINPOLARIZED) CALCULATION')])),
            Quantity(
                'RKM',
                r'(RKM\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity('matrix_size', r'MATRIX SIZE\s*(\d+)', dtype=int),
                    Quantity('LOs', r'LOs:\s*(\d+)', dtype=int),
                    Quantity('rkm', r'RKM\=\s*([\d\.]+)', dtype=np.float64)])),
            Quantity(
                'KPT',
                r'(KPT\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[Quantity(
                    'nr_kpts', r'NUMBER OF K-POINTS:\s*(\d+)', dtype=int)])),
            Quantity(
                'GAP',
                r'(GAP\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[Quantity(
                    'ene_gap', rf'({re_float})\s*Ry', dtype=np.float64, unit=ureg.rydberg)])),
            Quantity(
                'NOE',
                r'(NOE\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'noe',
                        rf'NUMBER OF ELECTRONS\s*\=\s*({re_float})',
                        dtype=np.float64)])),
            Quantity(
                'FER',
                r'(FER\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_reference_fermi',
                        rf'F E R M I \- ENERGY.+?\=\s*([\d\.\-\+Ee ]+)',
                        str_operation=lambda x: [float(v) for v in x.strip().split()] * ureg.rydberg,
                        convert=False)])),
            Quantity(
                'GMA',
                r'(GMA\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'cutoff',
                        rf'POTENTIAL AND CHARGE CUT\-OFF\s*({re_float})',
                        dtype=np.float64)])),
            Quantity(
                'POSi',
                r'(POS\d+\:[\s\S]+?)\n *\:',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity('atom_mult', r'MULT.*?\s*\=\s*(\d+)', dtype=int),
                    Quantity(
                        'position',
                        rf'POSITION\s*\=\s*({re_float}\s*{re_float}\s*{re_float})',
                        dtype=np.float64)])),
            Quantity(
                'CHAi',
                r'(CHA\d+\:[\s\S]+?)\n *\:',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'tot_val_charge_cell',
                        rf'TOTAL .+?CHARGE INSIDE.+?\=\s*({re_float})',
                        dtype=np.float64)])),
            Quantity(
                'SUM',
                r'(SUM\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_sum_eigenvalues',
                        rf'SUM OF EIGENVALUES\s*\=\s*({re_float})',
                        dtype=np.float64, unit=ureg.rydberg)])),
            Quantity(
                'RTOi',
                rf'RTO\d+\:\s*\d+\s*({re_float})\s*({re_float})\s*({re_float})\s*({re_float})\s*',
                dtype=np.dtype(np.float64), repeats=True),
            Quantity(
                'NTO',
                r'(NTO\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'tot_int_charge_nm',
                        rf'CHARGE\s*\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'NTOi',
                r'(NTO\d+\:[\s\S]+?)\n *\:',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'tot_charge_in_sphere_nm',
                        rf'CHARGE.+\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'DTOi',
                r'(DTO\d+\:[\s\S]+?)\n *\:',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'tot_diff_charge',
                        rf'TOTAL\s*DIFFERENCE CHARGE.+\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'DIS',
                r'(DIS\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'charge_distance',
                        rf'CHARGE DISTANCE.+\)\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'CTO',
                r'(CTO\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'tot_int_charge',
                        rf'CHARGE\s*\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'CTOi',
                r'(CTO\d+\:[\s\S]+?)\n *\:',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'tot_charge_in_sphere',
                        rf'TOTAL\s*CHARGE IN SPHERE.+\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'NECi',
                rf'NEC\d+\:\s*NUCLEAR AND ELECTRONIC CHARGE\s*({re_float})\s*({re_float})',
                dtype=np.dtype(np.float64), repeats=True),
            Quantity(
                'MMINT',
                r'(MMINT\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'mmint',
                        rf'MAGNETIC MOMENT IN INTERSTITIAL\s*\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'MMIi',
                r'(MMI\d+\:[\s\S]+?)\n *\:',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'mmi',
                        rf'MAGNETIC MOMENT IN SPHERE\s*\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'MMTOT',
                r'(MMTOT\s*\:[\s\S]+?)\n *\:',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'mmtot',
                        rf' MAGNETIC MOMENT IN CELL\s*\=\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'ENE',
                r'(ENE\s*\:[\s\S]+?)\n',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_total',
                        rf'TOTAL ENERGY IN Ry\s*\=\s*({re_float})',
                        dtype=np.float64, unit=ureg.rydberg)])),
            Quantity(
                'FORi',
                rf'FOR\d+\:\s*\d+\.ATOM\s*({re_float}\s*{re_float}\s*{re_float}\s*{re_float})',
                repeats=True, dtype=np.dtype(np.float64)),
            Quantity(
                'FGLi',
                rf'FGL\d+\:\s*\d+\.ATOM\s*({re_float}\s*{re_float}\s*{re_float})',
                repeats=True, dtype=np.dtype(np.float64))]

        self._quantities = [
            Quantity(
                'version',
                r'LABEL\d+\:\s*using WIEN2k_(\S+) \(Release ([\d\/]+)\)', flatten=False),
            Quantity(
                'start_date',
                r'LABEL\d+\:\s*on .+ at \w+ (\w+ \d+ \d\d\:\d\d\:\d\d)\s*\w*\s*(\d+)',
                flatten=False),
            Quantity(
                'iteration',
                r'\d+\:\s*(\d+\.\s* ITERATION[\s\S]+?)(?:\:ITE|\Z)',
                repeats=True, sub_parser=TextParser(quantities=iteration_quantities))]


class Wien2kParser:
    def __init__(self):
        # TODO complete list and verify if consistent with current implementation
        # http://www.wien2k.at/reg_user/textbooks/usersguide.pdf
        # implement libxc compatibility
        self._xc_functional_map = {
            '5': ['LDA_X', 'LDA_C_PW'],
            '6': ['HF_X'],
            '11': ['GGA_X_WC', 'GGA_C_PBE'],
            '13': ['GGA_X_PBE', 'GGA_C_PBE'],
            '17': ['GGA_X_PW91'],
            '18': ['HYB_GGA_XC_B3PW91'],
            '19': ['GGA_X_PBE_SOL', 'GGA_C_PBE_SOL'],
            '24': ['GGA_X_B88', 'GGA_C_LYP'],
            '28': ['MGGA_X_TB09', 'LDA_C_PW'],
            '27': ['MGGA_X_TPSS', 'MGGA_C_TPSS'],
            '29': ['MGGA_C_REVTPSS, GGA_C_REGTPSS'],
            '46': ['GGA_X_HTBS'],
            '47': ['HYB_GGA_XC_B3LYP'],
            'XC_LDA': ['LDA_X', 'LDA_C_PW'],
            'XC_PBE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'XC_WC': ['GGA_X_WC', 'GGA_C_PBE'],
            'XC_PBESOL': ['GGA_X_PBE_SOL', 'GGA_C_PBE_SOL'],
            'XC_B3PW91': ['HYB_GGA_XC_B3PW91'],
            'XC_B3LYP': ['HYB_GGA_XC_B3LYP'],
            'XC_MBJ': ['MGGA_X_TB09', 'LDA_C_PW'],
            'XC_TPSS': ['MGGA_X_TPSS', 'MGGA_C_TPSS'],
            'XC_REVTPSS': ['MGGA_C_REVTPSS, GGA_C_REGTPSS'],
            'XC_MGGA_MS': ['MGGA_X_MS', 'MGGA_C_MS'],
            'XC_MVS': ['MGGA_X_MVS', 'MGGA_C_MVS'],
            'XC_MBEEF': ['MGGA_X_MBEEF', 'GGA_C_PBE_SOL'],
            'XC_SCAN': ['MGGA_X_SCAN', 'MGGA_C_SCAN'],
            'XC_SCANL': ['MGGA_X_SCANL', 'MGGA_C_SCANL'],
            'XC_RSCAN': ['MGGA_X_RSCAN', 'MGGA_C_RSCAN'],
            'XC_R2SCAN': ['MGGA_X_R2SCAN', 'MGGA_C_R2SCAN'],
            'XC_TM': ['MGGA_X_TM', 'MGGA_C_TM'],
            'EC_PW91': ['GGA_X_PW91'],
            'VC_PW91': ['GGA_X_PW91'],
            'EX_B88': ['GGA_X_B88'],
            'VX_B88': ['GGA_X_B88'],
            'EC_LYP': ['GGA_C_LYP'],
            'VC_LYP': ['GGA_C_LYP'],
            'XC_HTBS': ['GGA_X_HTBS'],
            'EX_LDA': ['HF_X'],
            'VX_LDA': ['HF_X']}

        self.out_parser = OutParser()
        self.in0_parser = In0Parser()
        self.in1_parser = In1Parser()
        self.in2_parser = In2Parser()
        self.struct_parser = StructParser()
        self.dos_parser = DosParser()

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger

    def get_wien2k_file(self, ext, multiple=False):
        paths = [p for p in os.listdir(self.maindir) if re.match(r'.*%s$' % ext, p)]
        if not paths:
            return [] if multiple else None
        elif len(paths) == 1:
            path = os.path.join(self.maindir, paths[0])
            return [path] if multiple else path
        else:
            prefix = os.path.basename(self.filepath).rsplit('.', 1)[0]
            paths = [os.path.join(self.maindir, p) for p in paths if p.startswith(prefix)]
            if not paths:
                return [] if multiple else None
            return paths if multiple else paths[0]

    def get_nspin(self):
        return 2 if self.out_parser.get('iteration', [{}])[0].get('VOL', {}).get('spinpolarization') == 'SPINPOLARIZED' else 1

    def get_kpoints(self):
        k_list_file = self.get_wien2k_file('klist')
        if k_list_file is None:
            return None

        kpoints = []
        weights = []
        with open(k_list_file) as f:
            while True:
                line = f.readline()
                if not line or 'END' in line:
                    break
                try:
                    line = np.array(line.split()[:6], dtype=float)
                except Exception:
                    continue
                kpoints.append(line[1:4] / line[4])
                weights.append(line[5])
        weights /= sum(weights)

        return kpoints, weights

    def get_eigenvalues(self):
        nspin = self.get_nspin()
        if nspin == 1:
            files = self.get_wien2k_file(r'energy\_\d+', multiple=True)
            # sort the files so that the k-points are read in order
            files = sorted(files, key=lambda x: int(x.split('_')[-1]))
            if not files:
                files = [self.get_wien2k_file('energy')]
        else:
            files = []
            for spin in ['up', 'dn']:
                files_spin = self.get_wien2k_file(r'energy%s\_\d+' % spin, multiple=True)
                # sort the files so that the k-points are read in order
                files_spin = sorted(files_spin, key=lambda x: int(x.split('_')[-1]))
                if not files_spin:
                    files_spin = [self.get_wien2k_file('energy%s' % spin)]
                files.extend(files_spin)
        if None in files:
            return

        re_k = r'\-?\d\.\d+E[\-\+]\d\d'
        re_kpoint = re.compile(rf'\s*({re_k})\s*({re_k})\s*({re_k})\w*\s*(\d+)\s*\d+\s*\d+\s*([\d\.]+)\s*')
        re_eigenvalue = re.compile(r'\s*\d+ +(\-?\d+\.\d+[E\-\+\d]+) *\n*')
        kpoints, eigenvalues, multiplicity, index = [], [], [], []
        for file_i in files:
            with open(file_i) as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    kpoint = re_kpoint.match(line)
                    if kpoint:
                        eigenvalues.append([])
                        if 'energydn' not in file_i:
                            kpoints.append(kpoint.groups()[:3])
                            index.append(kpoint.group(4))
                            multiplicity.append(kpoint.group(5))
                            continue
                    eigenvalue = re_eigenvalue.match(line)
                    if eigenvalue:
                        eigenvalues[-1].append(eigenvalue.group(1))
        try:
            # There can be different amount of eigenvalues calculated at every k-point.
            # However, the metainfo expects a homogeneous array, so just find the k-point
            # with the least amount and discard the extra values at other k-points.
            num_eigvals = [len(eig) for eig in eigenvalues]
            min_eigval_index = min(num_eigvals)
            max_eigval_index = max(num_eigvals)
            if min_eigval_index < max_eigval_index:
                self.logger.warning('Different number of eigenvalues at different k-points. Truncating the extra values.')
            for i, e in enumerate(eigenvalues):
                eigenvalues[i] = e[:min_eigval_index]

            eigenvalues = np.array(eigenvalues, dtype=np.dtype(np.float64))
            kpoints = np.array(kpoints, dtype=np.dtype(np.float64))
            multiplicity = np.array(multiplicity, dtype=np.dtype(np.float64))
            eigenvalues = np.reshape(eigenvalues, (
                nspin, len(kpoints), min_eigval_index))
            return eigenvalues, kpoints, multiplicity
        except Exception:
            self.logger.error('Error reading eigenvalues.')
            return

    def get_dos(self):
        # dos (projections and total) are printed in dos1, dos2....
        nspin = self.get_nspin()
        if nspin == 1:
            files = self.get_wien2k_file(r'dos\d+', multiple=True)
            files.sort()
        else:
            files = []
            for spin in ['up', 'dn']:
                files_spin = self.get_wien2k_file(r'dos\d+%s' % spin, multiple=True)
                files_spin.sort()
                files.extend(files_spin)

        if not files:
            return

        dos = []
        labels = []
        for file_i in files:
            self.dos_parser.mainfile = file_i
            data = self.dos_parser.get('data')
            if data is None:
                continue
            if not file_i.endswith('dn'):
                labels.extend(self.dos_parser.get('labels', '').split())
            data = np.transpose(data)
            energy = data[0]
            dos.append(data[1:])

        try:
            dos = np.vstack(dos)
            dos = np.reshape(dos, (nspin, len(dos) // nspin, len(dos[0])))
            dos = np.transpose(dos, axes=(1, 0, 2))
            total_dos = []
            partial_dos = []
            for n in range(len(dos)):
                # wien2k may not uniformly print out projections, we get only total projections
                # on the species (independent atoms) denoted by the header N:total
                if labels[n].endswith(':total'):
                    partial_dos.append(dos[n])
                elif labels[n] == 'total-DOS' or labels[n] == 'TOTAL':
                    # TODO determine if total dos is always the last column
                    total_dos = dos[n]
            if len(partial_dos) > 0:
                partial_dos = np.transpose(partial_dos, axes=(1, 0, 2))
            return energy, total_dos, partial_dos

        except Exception:
            self.logger.error('Error reading dos.')
            return

    def parse_scc(self):
        if self.out_parser.get('iteration') is None:
            return

        sec_scc = self.archive.run[0].m_create(Calculation)

        for iteration in self.out_parser.get('iteration'):
            sec_scf = sec_scc.m_create(ScfIteration)
            sec_scf_energy = sec_scf.m_create(Energy)
            for key in iteration.keys():
                if iteration.get(key) is None:
                    continue
                elif key == 'FORi':
                    forces = np.transpose(iteration.get(key))
                    sec_scf.x_wien2k_for = np.transpose(forces[1:4])
                    sec_scf.x_wien2k_for_abs = forces[0]
                elif key == 'FGLi':
                    sec_scf.x_wien2k_for_gl = iteration.get(key)
                elif key == 'MMIi':
                    sec_scf.x_wien2k_mmi = [mm.mmi for mm in iteration.get(key)]
                elif key == 'NECi':
                    charge = np.transpose(iteration.get(key))
                    sec_scf.x_wien2k_nuclear_charge = charge[0]
                    sec_scf.x_wien2k_electronic_charge = charge[1]
                elif key == 'CTOi':
                    charge = [c.tot_charge_in_sphere for c in iteration.get(key)]
                    sec_scf.x_wien2k_tot_charge_in_sphere = charge
                elif key == 'DTOi':
                    charge = [c.tot_diff_charge for c in iteration.get(key)]
                    sec_scf.x_wien2k_tot_diff_charge = charge
                elif key == 'NTOi':
                    charge = [c.tot_charge_in_sphere_nm for c in iteration.get(key)]
                    sec_scf.x_wien2k_tot_charge_in_sphere_nm = charge
                elif key == 'RTOi':
                    density = np.transpose(iteration.get(key))
                    sec_scf.x_wien2k_density_at_nucleus_valence = density[0]
                    sec_scf.x_wien2k_density_at_nucleus_semicore = density[1]
                    sec_scf.x_wien2k_density_at_nucleus_core = density[2]
                    sec_scf.x_wien2k_density_at_nucleus_tot = density[3]
                elif key == 'CHAi':
                    charge = [c.tot_val_charge_cell for c in iteration.get(key)]
                    sec_scf.x_wien2k_tot_val_charge_sphere = charge
                elif key == 'POSi':
                    mult = [p.atom_mult for p in iteration.get(key)]
                    sec_scf.x_wien2k_atom_mult = mult
                else:
                    for sub_key, val in iteration.get(key, {}).items():
                        if sub_key.startswith('energy_reference_fermi'):
                            sec_scf_energy.fermi = val
                        elif sub_key.startswith('energy_'):
                            sec_scf_energy.m_add_sub_section(
                                getattr(Energy, sub_key.replace('energy_', '').lower()), EnergyEntry(value=val))
                        else:
                            setattr(sec_scf, 'x_wien2k_%s' % sub_key, val)

        # write final iteration values to scc
        if sec_scf.energy.total is not None:
            sec_scc.energy = Energy(total=EnergyEntry(value=sec_scf.energy.total.value))
            if sec_scf.energy.fermi is not None:
                sec_scc.energy.fermi = sec_scf.energy.fermi

        if sec_scf.x_wien2k_for_gl is not None:
            forces = []
            for n, force in enumerate(sec_scf.x_wien2k_for_gl):
                forces.extend([force] * sec_scf.x_wien2k_atom_mult[n])
            sec_scc.forces = Forces(total=ForcesEntry(value=forces * (ureg.mRy / ureg.bohr)))

        # eigenvalues
        eigenvalues = self.get_eigenvalues()
        if eigenvalues is not None:
            sec_eigenvalues = sec_scc.m_create(BandEnergies)
            sec_eigenvalues.kpoints = eigenvalues[1]
            sec_eigenvalues.kpoints_multiplicities = eigenvalues[2]
            sec_eigenvalues.energies = eigenvalues[0] * ureg.rydberg

        # dos
        dos = self.get_dos()
        if dos is not None:
            # total dos
            if len(dos[1]) > 0:
                sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
                sec_dos.energies = dos[0] * ureg.rydberg
                for spin in range(len(dos[1])):
                    sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
                    sec_dos_values.spin = spin
                    sec_dos_values.value = dos[1][spin] * (1 / ureg.rydberg)

            # projected dos
            if len(dos[2]) > 0:
                labels = [a.atom_name for a in self.struct_parser.get('atom', [])]
                if len(labels) == 0:
                    self.logger.warning('Cannot resolve atom labels.')
                else:
                    for species in range(len(dos[2])):
                        for spin in range(len(dos[2][species])):
                            sec_dos_values = sec_dos.m_create(DosValues, Dos.species_projected)
                            sec_dos_values.atom_label = labels[species]
                            sec_dos_values.spin = spin
                            sec_dos_values.value = dos[2][species][spin] * (1 / ureg.rydberg)

    def parse_system(self):
        sec_system = self.archive.run[0].m_create(System)
        sec_atoms = sec_system.m_create(Atoms)

        self.struct_parser.mainfile = self.get_wien2k_file('struct')
        for key, val in self.struct_parser.get('lattice', {}).items():
            setattr(sec_system, 'x_wien2k_%s' % key, val)

        for atom in self.struct_parser.get('atom', []):
            sec_atom = sec_system.m_create(x_wien2k_section_equiv_atoms)
            for key, val in atom.items():
                setattr(sec_atom, 'x_wien2k_%s' % key, val)

        atoms = self.struct_parser.get_atoms()
        if atoms is None:
            return

        sec_atoms.lattice_vectors = np.array(atoms.get_cell()) * ureg.angstrom
        sec_atoms.positions = atoms.get_positions() * ureg.angstrom
        sec_atoms.labels = atoms.get_chemical_symbols()
        sec_atoms.periodic = atoms.get_pbc()

    def parse_method(self):
        sec_method = self.archive.run[0].m_create(Method)
        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)
        sec_electronic.method = 'DFT'
        sec_electronic.n_spin_channels = self.get_nspin()

        # read functional settings from in0 file
        self.in0_parser.mainfile = self.get_wien2k_file('in0')

        # better to read it from scf?
        xc_functional = self.in0_parser.get('xc_functional', None)
        xc_functional = xc_functional if isinstance(xc_functional, list) else [xc_functional]
        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for name in xc_functional:
            functionals = self._xc_functional_map.get(name)
            if functionals is None:
                self.logger.warning('Cannot resolve XC functional.')
                continue
            for functional in functionals:
                if '_X_' in functional or functional.endswith('_X'):
                    sec_xc_functional.exchange.append(Functional(name=functional))
                elif '_C_' in functional or functional.endswith('_C'):
                    sec_xc_functional.correlation.append(Functional(name=functional))
                elif 'HYB' in functional:
                    sec_xc_functional.hybrid.append(Functional(name=functional))
                else:
                    sec_xc_functional.contributions.append(Functional(name=functional))

        fft = self.in0_parser.get('fft')
        if fft is not None:
            sec_method.x_wien2k_ifft = fft[:3]
            sec_method.x_wien2k_ifft_factor = fft[3]

        # read cut off settings from in1
        in1_file = self.get_wien2k_file('in1')
        if in1_file is None:
            in1_file = self.get_wien2k_file('in1c')
        self.in1_parser.mainfile = in1_file
        for key, val in self.in1_parser.items():
            if val is not None:
                setattr(sec_method, 'x_wien2k_%s' % key, val)

        # read integration data from in2 file
        in2_file = self.get_wien2k_file('1n2')
        if in2_file is None:
            in2_file = self.get_wien2k_file('in2c')
        self.in2_parser.mainfile = in2_file

        for key in ['gmax', 'switch']:
            val = self.in2_parser.get(key)
            if val is not None:
                setattr(sec_method, 'x_wien2k_in2_%s' % key, val)

        emin_keys = ['emin', 'ne', 'espermin', 'esper0']
        for n, val in enumerate(self.in2_parser.get('emin', [])):
            if n < 4:
                setattr(sec_method, 'x_wien2k_in2_%s' % emin_keys[n], val)

        smearing, width = self.in2_parser.get('smearing', [None, None])
        if smearing is not None:
            sec_smearing = sec_electronic.m_create(Smearing)
            if smearing.startswith('GAUSS'):
                smearing = 'gaussian'
            elif smearing.startswith('TEMP'):
                smearing = 'fermi'
            elif smearing.startswith('TETRA'):
                smearing = 'tetrahedra'
            sec_smearing.kind = smearing
            sec_smearing.width = (float(width) * ureg.rydberg).to('joule').magnitude

        # read kpoints from klist
        kpoints = self.get_kpoints()
        if kpoints is not None:
            sec_k_mesh = sec_method.m_create(KMesh)
            sec_k_mesh.points = kpoints[0]
            sec_k_mesh.weights = kpoints[1]

        # basis
        sec_method.basis_set.append(BasisSet(type='(L)APW+lo'))

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        sec_run = self.archive.m_create(Run)

        sec_run.program = Program(name='WIEN2k', version=self.out_parser.get('version', ''))
        start_date = self.out_parser.get('start_date')
        if start_date is not None:
            # TODO resolve proper timezone
            dt = datetime.strptime(start_date, '%b %d %H:%M:%S %Y') - datetime.utcfromtimestamp(0)
            sec_run.time_run = TimeRun(date_start=dt.total_seconds())

        # TODO implement geometry optimization
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'

        self.parse_method()

        self.parse_system()

        self.parse_scc()
