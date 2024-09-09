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
from runschema.run import Run, Program
from runschema.system import System, Atoms
from runschema.method import (
    Method,
    TB,
    SlaterKoster,
    TightBindingOrbital,
    SlaterKosterBond,
    TwoCenterBond,
)
from runschema.calculation import Calculation, BandStructure, BandEnergies, Energy
from simulationworkflowschema import SinglePoint
import json
import re
from ..utils import BeyondDFTWorkflowsParser
from ase.data import chemical_symbols


class TBStudioParser(BeyondDFTWorkflowsParser):
    def __init__(self):
        self._calculation_type = 'tight binding'

    def parse_system(self):
        """Populates run.system with the input structural parameters."""
        sec_run = self.archive.run[-1]
        sec_system = System()
        sec_run.system.append(sec_system)
        sec_atoms = Atoms()
        sec_system.atoms = sec_atoms

        # Load lattice vectors
        if self.tbm.get('vars') is None:
            self.logger.warning('Could not find the .tbm file vars parameters.')
            return

        self.a = [np.float64(self.tbm['vars'].get(f'a[{i}]', '0')) for i in range(3)]
        self.b = [np.float64(self.tbm['vars'].get(f'b[{i}]', '0')) for i in range(3)]
        self.c = [np.float64(self.tbm['vars'].get(f'c[{i}]', '0')) for i in range(3)]

        sec_atoms.lattice_vectors = [self.a, self.b, self.c] * ureg.angstrom

        xyz_coords = []
        atomic_labels = []
        for r, atomic_number in zip(
            self.tbm['grids']['XYZ_Coords'].get('value', []),
            self.tbm['grids']['KABC_Coords'].get('value', []),
        ):
            # Check if x, y, and z are provided then accept it otherwise it is taken as the end of table
            # This is the same behaviour that tbstudio does to accept or ignore a row
            try:
                x = np.float64(r[0])
                y = np.float64(r[1])
                z = np.float64(r[2])
                atom_num = int(atomic_number[0])
                xyz_coords.append([x, y, z])
                atomic_labels.append(chemical_symbols[atom_num])
            except Exception:
                break

        sec_atoms.positions = xyz_coords * ureg.angstrom
        sec_atoms.labels = atomic_labels

        tb_l = np.int64(self.tbm['vars'].get('TBl[0]', '0'))
        tb_m = np.int64(self.tbm['vars'].get('TBm[0]', '0'))
        tb_n = np.int64(self.tbm['vars'].get('TBn[0]', '0'))

        pbc = [bool(dim != 0) for dim in [tb_l, tb_m, tb_n]]
        sec_atoms.periodic = pbc

    def parse_method(self):
        """Populates run.method with the input methodological parameters."""
        sec_run = self.archive.run[-1]

        sec_method = Method()
        sec_run.method.append(sec_method)
        sec_tb = TB()
        sec_method.tb = sec_tb
        sec_sk = SlaterKoster()
        sec_tb.slater_koster = sec_sk

        orbitals = []
        lastInd = 0
        for i in range(1, 100):
            varName = 'AtomInd{}'.format(i)
            orbital = self.tbm['combos'][varName]
            if orbital['selected'] != 0:
                lastInd = i
        for i in range(1, lastInd + 1):
            varName = 'AtomInd{}'.format(i)
            orbital = self.tbm['combos'][varName]
            items = orbital['items']
            selected = orbital['selected']
            if selected == 0:
                orbitals.append(None)
            else:
                orbitals.append(items[selected])

        final_os = {}
        tbAtom = ''
        shell = ''
        for state, row in zip(
            self.tbm['grids']['OS']['isReadOnly'], self.tbm['grids']['OS']['value']
        ):
            if state[0] and state[1] and state[2]:
                if row[0] == '' and row[1] == '' and row[2] == '':
                    break
                else:
                    os_name = row[0]
                    orbital_info = re.search(r'^(.*) \((.*)\)$', os_name)
                    tbAtom = orbital_info[1]
                    shell = orbital_info[2]
                    if tbAtom not in final_os:
                        final_os[tbAtom] = {shell: {}}
                    else:
                        if shell not in final_os[tbAtom]:
                            final_os[tbAtom][shell] = {}
            else:
                orbital = row[0]
                final = 0
                try:
                    final = np.float64(row[2])
                except Exception:
                    pass

                final_os[tbAtom][shell][orbital] = final

        for atom_index, orbital in enumerate(orbitals):
            shells = final_os[orbital]
            for iShell, shellOrbitals in enumerate(shells.values()):
                for orbital_name, onSite in shellOrbitals.items():
                    sec_orbitals = TightBindingOrbital()
                    sec_sk.orbitals.append(sec_orbitals)
                    sec_orbitals.orbital_name = orbital_name
                    sec_orbitals.atom_index = atom_index
                    sec_orbitals.shell = iShell
                    sec_orbitals.onsite_energy = onSite

        final_sk = {}
        tb_bond = ''
        for state, row in zip(
            self.tbm['grids']['SK']['isReadOnly'], self.tbm['grids']['SK']['value']
        ):
            if state[0] and state[1] and state[2]:
                if row[0] == '' and row[1] == '' and row[2] == '':
                    break
                else:
                    tb_bond = row[0]
                    final_sk[tb_bond] = {}
            else:
                sk_integral = row[0]
                try:
                    final_sk[tb_bond][sk_integral] = np.float64(row[2])
                except Exception:
                    final_sk[tb_bond][sk_integral] = 0

        final_overlap = {}
        tb_bond = ''
        for state, row in zip(
            self.tbm['grids']['OL']['isReadOnly'], self.tbm['grids']['OL']['value']
        ):
            if state[0] and state[1] and state[2]:
                if row[0] == '' and row[1] == '' and row[2] == '':
                    break
                else:
                    tb_bond = row[0]
                    final_overlap[tb_bond] = {}
            else:
                sk_integral = row[0]
                try:
                    final_overlap[tb_bond][sk_integral] = np.float64(row[2])
                except Exception:
                    final_overlap[tb_bond][sk_integral] = 0

        bonds = []
        if 'TB Model' in self.tbm['trees']['Bonds']:
            if 'children' in self.tbm['trees']['Bonds']['TB Model']:
                allBonds = self.tbm['trees']['Bonds']['TB Model']['children']
                allCells = allBonds.keys()
                for cells in allCells:
                    cellBonds = allBonds[cells]
                    cells_info = re.search(r'^(\(.*\))-(\(.*\))$', cells)
                    cell1 = cells_info[1]
                    cell2 = cells_info[2]
                    is_active = cellBonds['state'] == 4
                    if is_active:
                        allAtoms = cellBonds['children']
                        for atoms in allAtoms.keys():
                            is_bond_active = allAtoms[atoms]['state'] == 4
                            if is_bond_active:
                                atoms_info = re.search(
                                    r'^\[ \(i,n\)=\((\d+),(\d+)\) , \(j,m\)=\((\d+),(\d+)\) , (.*) ]$',
                                    atoms,
                                )
                                index1 = atoms_info[1]
                                shell1 = atoms_info[2]
                                index2 = atoms_info[3]
                                shell2 = atoms_info[4]
                                bond_type = atoms_info[5]
                                bond = {
                                    'atom1': {
                                        'index': index1,
                                        'shell': shell1,
                                        'cell': cell1,
                                    },
                                    'atom2': {
                                        'index': index2,
                                        'shell': shell2,
                                        'cell': cell2,
                                    },
                                    'type': bond_type,
                                }
                                bonds.append(bond)

        for bond in bonds:
            atom1 = bond['atom1']
            atom2 = bond['atom2']
            bond_type = bond['type']
            h_sk = None
            s_sk = None
            if final_sk:
                h_sk = final_sk[bond_type]
            if final_overlap:
                s_sk = final_overlap[bond_type]

            if h_sk is not None:
                sec_bonds = SlaterKosterBond()
                sec_sk.bonds.append(sec_bonds)
                sec_bonds.bond_label = bond_type

                center1 = TightBindingOrbital()
                sec_bonds.center1 = center1
                center1.atom_index = atom1['index']
                center1.shell = atom1['shell']
                indices = re.findall(r'-?\d+', atom1['cell'])
                center1.cell_index = [int(index) for index in indices]

                center2 = TightBindingOrbital()
                sec_bonds.center2 = center2
                center2.atom_index = atom2['index']
                center2.shell = atom2['shell']
                indices = re.findall(r'-?\d+', atom2['cell'])
                center2.cell_index = [int(index) for index in indices]
                for sk_label, sk_integral in h_sk.items():
                    setattr(sec_bonds, sk_label, sk_integral)

            if s_sk is not None:
                sec_overlaps = SlaterKosterBond()
                sec_sk.overlaps.append(sec_overlaps)
                sec_overlaps.bond_label = bond_type

                center1 = TightBindingOrbital()
                sec_overlaps.center1 = center1
                center1.atom_index = atom1['index']
                center1.shell = atom1['shell']
                indices = re.findall(r'-?\d+', atom1['cell'])
                center1.cell_index = [int(index) for index in indices]

                center2 = TightBindingOrbital()
                sec_overlaps.center2 = center2
                center2.atom_index = atom2['index']
                center2.shell = atom2['shell']
                indices = re.findall(r'-?\d+', atom2['cell'])
                center2.cell_index = [int(index) for index in indices]
                for sk_label, sk_integral in s_sk.items():
                    setattr(sec_overlaps, sk_label, sk_integral)

    def parse_scc(self):
        """Populates run.calculation with the output of the calculation."""
        sec_run = self.archive.run[-1]
        sec_scc = Calculation()
        sec_run.calculation.append(sec_scc)

        _k_points = self.tbm['variables']['KPoints']
        frac_k_points = []
        k_points = []
        k_length = []
        for row in _k_points:
            frac_k_points.append([row[0], row[1], row[2]])
            k_points.append([row[3], row[4], row[5]])
            k_length.append(row[6])

        tb_bands = self.tbm['variables']['fTBEigVal']
        band_segments_points = self.tbm['variables']['bandSections']['index']
        if band_segments_points is None or len(tb_bands) < 1 or len(frac_k_points) < 1:
            return

        fermi_level = self.tbm['variables'].get('ChemP')
        if not fermi_level:
            self.logger.warning(
                'Could not extract the Fermi level, so that the BandStructure is not resolved'
            )
            return

        sec_energy = Energy()
        sec_scc.energy = sec_energy
        sec_energy.fermi = fermi_level * ureg.eV if fermi_level else None
        sec_k_band = BandStructure()
        sec_k_band.energy_fermi = sec_energy.fermi

        for n1, n2 in band_segments_points:
            sec_k_band_segment = BandEnergies()
            sec_k_band.segment.append(sec_k_band_segment)
            sec_k_band_segment.kpoints = frac_k_points[n1 : n2 + 1]
            sec_k_band_segment.energies = (
                np.array([tb_bands[n1 : n2 + 1]]) + fermi_level
            ) * ureg.eV

        sec_scc.band_structure_electronic.append(sec_k_band)

    def get_mainfile_keys(self, **kwargs):
        filepath = kwargs.get('filename')

        f = open(filepath)
        tbm = json.load(f)
        f.close()

        dft_nomad_entry_id = None
        dft_nomad_upload_id = None
        if 'type' in tbm['DFTSource'] and tbm['DFTSource']['type'].lower() == 'nomad':
            dft_nomad_entry_id = tbm['DFTSource']['source']['entry_id']
            dft_nomad_upload_id = tbm['DFTSource']['source']['upload_id']

        if (
            dft_nomad_entry_id is not None
            and dft_nomad_entry_id != ''
            and dft_nomad_upload_id is not None
            and dft_nomad_upload_id != ''
        ):
            return ['TB_workflow']
        else:
            return True

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        sec_run = Run()
        self.archive.run.append(sec_run)

        try:
            f = open(self.filepath)
            tbm = json.load(f)
            f.close()
        except Exception:
            self.logger.error('Error opening json output file.')
            return

        self.tbm = tbm
        sec_run.program = Program(
            name='TBStudio', version=self.tbm.get('ReleaseVersion', '')
        )

        dft_nomad_entry_id = None
        dft_nomad_upload_id = None
        if (
            'type' in self.tbm['DFTSource']
            and self.tbm['DFTSource']['type'].lower() == 'nomad'
        ):
            dft_nomad_entry_id = self.tbm['DFTSource']['source']['entry_id']
            dft_nomad_upload_id = self.tbm['DFTSource']['source']['upload_id']

        self.parse_system()
        self.parse_method()
        self.parse_scc()

        workflow = SinglePoint()
        self.archive.workflow2 = workflow

        if (
            dft_nomad_entry_id is not None
            and dft_nomad_entry_id != ''
            and dft_nomad_upload_id is not None
            and dft_nomad_upload_id != ''
        ):
            first_principles_calculation_archive = None
            try:
                first_principles_calculation_archive = archive.m_context.load_archive(
                    dft_nomad_entry_id, dft_nomad_upload_id, None
                )
            except Exception:
                self.logger.warning('TBStudio Workflow was not found.')
            if first_principles_calculation_archive and self._child_archives:
                tb_workflow_archive = self._child_archives.get('TB_workflow')
                self.parse_tb_workflow(
                    archive, first_principles_calculation_archive, tb_workflow_archive
                )
