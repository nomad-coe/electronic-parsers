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

from matid.data.element_data import get_symbols
from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms, AtomsGroup
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, AtomParameters, KMesh, TB, SlaterKoster, TightBindingOrbital, SlaterKosterBond, TwoCenterBond
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Dos, BandStructure, BandEnergies, Energy, HoppingMatrix
)
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint, SimulationWorkflow
from nomad.datamodel.metainfo.workflow import TaskReference, Link
import json
import re


def parse_int(string, default):
    val = default
    try:
        val = np.int64(string)
    except:
        pass
    return val


def parse_float(string, default):
    val = default
    try:
        val = np.float64(string)
    except:
        pass
    return val


def load_tbm(file):
    f = open(file)
    tbm = json.load(f)
    f.close()

    # validation
    application_full_name = None
    release_version = None
    if 'ApplicationFullName' in tbm and 'ReleaseVersion' in tbm:
        application_full_name = tbm['ApplicationFullName']
        release_version = tbm['ReleaseVersion']

    if application_full_name != 'Tight Binding Studio' or not release_version:
        raise Exception('The file is not a valid TBStudio tight binding model.')

    model = {}

    # Load workflow if does exist
    model['DFTNomadEntryID'] = None
    if 'type' in tbm['DFTSource'] and tbm['DFTSource']['type'].lower() == 'nomad':
        model['DFTNomadEntryID'] = tbm['DFTSource']['source']

    # Load lattice vectors
    model['a'] = [parse_float(tbm['vars']['a[0]'], 0), parse_float(tbm['vars']['a[1]'], 0), parse_float(tbm['vars']['a[2]'], 0)]
    model['b'] = [parse_float(tbm['vars']['b[0]'], 0), parse_float(tbm['vars']['b[1]'], 0), parse_float(tbm['vars']['b[2]'], 0)]
    model['c'] = [parse_float(tbm['vars']['c[0]'], 0), parse_float(tbm['vars']['c[1]'], 0), parse_float(tbm['vars']['c[2]'], 0)]

    # SOC
    model['isSOC'] = tbm['checks']['SOC[0]']

    # Load coordinates
    _xyz_coords = tbm['grids']['XYZ_Coords']['value']
    xyz_coords = []
    for r in _xyz_coords:
        try:
            x = np.float64(r[0])
            y = np.float64(r[1])
            z = np.float64(r[2])
            xyz_coords.append([x, y, z])
        except:
            break
    model['xyz_coords'] = xyz_coords

    tb_l = parse_int(tbm['vars']['TBl[0]'], 0)
    tb_m = parse_int(tbm['vars']['TBm[0]'], 0)
    tb_n = parse_int(tbm['vars']['TBn[0]'], 0)

    model['neighbor_unit_cells'] = [tb_l, tb_m, tb_n]

    dim = 0
    for i in model['neighbor_unit_cells']:
        if i != 0:
            dim = dim + 1

    if dim == 0:
        model['dimension'] = '0D'
    elif dim == 1:
        model['dimension'] = '1D'
    elif dim == 2:
        model['dimension'] = '2D'
    elif dim == 3:
        model['dimension'] = '3D'

    # Load fractional coordinates and kinds
    _kabc_coords = tbm['grids']['KABC_Coords']['value']
    kinds = []
    abc_coords = []
    for r in _kabc_coords:
        try:
            k = np.int64(r[0])
            a = np.float64(r[1])
            b = np.float64(r[2])
            c = np.float64(r[3])
            kinds.append(k)
            abc_coords.append([a, b, c])
        except:
            break
    model['kinds'] = kinds
    model['abc_coords'] = abc_coords

    # Load SK model
    _os = tbm['grids']['OS']['value']
    _osr = tbm['grids']['OS']['isReadOnly']

    model['initial_os'] = {}
    model['final_os'] = {}
    tbAtom = ''
    shell = ''
    for state, row in zip(_osr, _os):
        if state[0] and state[1] and state[2]:
            if row[0] == '' and row[1] == '' and row[2] == '':
                break
            else:
                os_name = row[0]
                orbital_info = re.search("^(.*) \((.*)\)$", os_name)
                tbAtom = orbital_info[1]
                shell = orbital_info[2]
                if tbAtom not in model['initial_os']:
                    model['initial_os'][tbAtom] = {shell: {}}
                else:
                    if shell not in model['initial_os'][tbAtom]:
                        model['initial_os'][tbAtom][shell] = {}
                if tbAtom not in model['final_os']:
                    model['final_os'][tbAtom] = {shell: {}}
                else:
                    if shell not in model['final_os'][tbAtom]:
                        model['final_os'][tbAtom][shell] = {}
        else:
            orbital = row[0]
            initial = 0
            try:
                initial = np.float64(row[1])
            except:
                pass
            final = 0
            try:
                final = np.float64(row[2])
            except:
                pass

            model['initial_os'][tbAtom][shell][orbital] = initial
            model['final_os'][tbAtom][shell][orbital] = final

    _sk = tbm['grids']['SK']['value']
    _skr = tbm['grids']['SK']['isReadOnly']
    model['initial_sk'] = {}
    model['final_sk'] = {}
    tbBond = ''
    for state, row in zip(_skr, _sk):
        if state[0] and state[1] and state[2]:
            if row[0] == '' and row[1] == '' and row[2] == '':
                break
            else:
                tbBond = row[0]
                model['initial_sk'][tbBond] = {}
                model['final_sk'][tbBond] = {}
        else:
            skIntegral = row[0]
            initial = parse_float(row[1], 0)
            final = parse_float(row[2], 0)
            model['initial_sk'][tbBond][skIntegral] = initial
            model['final_sk'][tbBond][skIntegral] = final

    _ol = tbm['grids']['OL']['value']
    _olr = tbm['grids']['OL']['isReadOnly']
    model['initial_overlap'] = {}
    model['final_overlap'] = {}
    tbBond = ''
    for state, row in zip(_olr, _ol):
        if state[0] and state[1] and state[2]:
            if row[0] == '' and row[1] == '' and row[2] == '':
                break
            else:
                tbBond = row[0]
                model['initial_overlap'][tbBond] = {}
                model['final_overlap'][tbBond] = {}
        else:
            skIntegral = row[0]
            initial = parse_float(row[1], 0)
            final = parse_float(row[2], 0)
            model['initial_overlap'][tbBond][skIntegral] = initial
            model['final_overlap'][tbBond][skIntegral] = final

    orbitals = []
    lastInd = 0
    for i in range(1, 100):
        varName = 'AtomInd{}'.format(i)
        orbital = tbm['combos'][varName]
        if orbital['selected'] != 0:
            lastInd = i
    for i in range(1, lastInd + 1):
        varName = 'AtomInd{}'.format(i)
        orbital = tbm['combos'][varName]
        items = orbital["items"]
        selected = orbital['selected']
        if selected == 0:
            orbitals.append(None)
        else:
            orbitals.append(items[selected])

    model['orbitals'] = orbitals

    _k_points = tbm['variables']['KPoints']
    frac_k_points = []
    k_points = []
    k_length = []
    for row in _k_points:
        frac_k_points.append([row[0], row[1], row[2]])
        k_points.append([row[3], row[4], row[5]])
        k_length.append(row[6])
    model['frac_k_points'] = frac_k_points
    model['k_points'] = k_points
    model['k_length'] = k_length

    model['bandSections'] = tbm['variables']['bandSections']
    model['dft_bands'] = tbm['variables']['DFTEigVal']
    model['initial_tb_bands'] = tbm['variables']['iTBEigVal']
    model['final_tb_bands'] = tbm['variables']['fTBEigVal']
    model['fermi_level'] = tbm['variables']['ChemP']

    tb_unit_cells = tbm['lists']['EssentialUnitcellList']
    model['initial_hamiltonian_matrix'] = {}
    model['final_hamiltonian_matrix'] = {}
    model['initial_overlap_matrix'] = {}
    model['final_overlap_matrix'] = {}
    for index, unit_cell in enumerate(tb_unit_cells):
        if len(tbm['variables']['Hi']) > index:
            model['initial_hamiltonian_matrix'][unit_cell] = tbm['variables']['Hi'][index]
        if len(tbm['variables']['Hi']) > index:
            model['final_hamiltonian_matrix'][unit_cell] = tbm['variables']['Hf'][index]
        if len(tbm['variables']['Si']) > index:
            model['initial_overlap_matrix'][unit_cell] = tbm['variables']['Si'][index]
        if len(tbm['variables']['Sf']) > index:
            model['final_overlap_matrix'][unit_cell] = tbm['variables']['Sf'][index]

    model['initial_soc_matrix'] = {}
    model['final_soc_matrix'] = {}

    if len(tbm['variables']['SOCi']) > 0:
        model['initial_soc_matrix']['real'] = tbm['variables']['SOCi'][0]
    if len(tbm['variables']['SOCi']) > 1:
        model['initial_soc_matrix']['image'] = tbm['variables']['SOCi'][1]
    if len(tbm['variables']['SOCf']) > 0:
        model['final_soc_matrix']['real'] = tbm['variables']['SOCf'][0]
    if len(tbm['variables']['SOCf']) > 1:
        model['final_soc_matrix']['image'] = tbm['variables']['SOCf'][1]

    model['bonds'] = []
    if 'TB Model' in tbm['trees']['Bonds']:
        if 'children' in tbm['trees']['Bonds']['TB Model']:
            allBonds = tbm['trees']['Bonds']['TB Model']['children']
            allCells = allBonds.keys()
            for cells in allCells:
                bonds = allBonds[cells]
                cells_info = re.search("^(\(.*\))-\((.*)\)$", cells)
                cell1 = cells_info[1]
                cell2 = cells_info[2]
                is_active = bonds['state'] == 4
                if is_active:
                    allAtoms = bonds['children']
                    for atoms in allAtoms.keys():
                        is_bond_active = allAtoms[atoms]['state'] == 4
                        if is_bond_active:
                            atoms_info = re.search("^\[ \(i,n\)=\((\d+),(\d+)\) , \(j,m\)=\((\d+),(\d+)\) , (.*) ]$", atoms)
                            index1 = atoms_info[1]
                            shell1 = atoms_info[2]
                            index2 = atoms_info[3]
                            shell2 = atoms_info[4]
                            bond_type = atoms_info[5]
                            bond = {
                                "atom1": {"index": index1, "shell": shell1, "cell": cell1},
                                "atom2": {"index": index2, "shell": shell2, "cell": cell2},
                                "type": bond_type
                            }
                            model['bonds'].append(bond)

    return model


class TBStudioParser:
    level = 1

    def __init__(self):
        self._calculation_type = 'tight binding'

    def parse_system(self):
        """Populates run.system with the input structural parameters.
        """
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)
        # Here the key is to populate:
        #   1- `Atoms` with the main quantities I wrote
        #   2- `AtomsGroup` (optional) with the info of the atoms used for the tight binding in the tight-binding model
        sec_atoms = sec_system.m_create(Atoms)

        a = self.tb_model['a']
        b = self.tb_model['b']
        c = self.tb_model['c']
        sec_atoms.lattice_vectors = [a, b, c] * ureg.angstrom

        sec_atoms.positions = self.tb_model['xyz_coords'] * ureg.angstrom
        sec_atoms.species = self.tb_model['kinds']

        pbc = [bool(dim != 0) for dim in self.tb_model['neighbor_unit_cells']]
        sec_atoms.periodic = pbc

    def parse_method(self):
        """Populates run.method with the input methodological parameters.
        """
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        sec_tb = sec_method.m_create(TB)
        sec_sk = sec_tb.m_create(SlaterKoster)

        orbitals = self.tb_model['orbitals']

        for atom_index, orbital in enumerate(orbitals):
            shells = self.tb_model['final_os'][orbital]
            for iShell, shellOrbitals in enumerate(shells.values()):
                for orbital_name, onSite in shellOrbitals.items():
                    sec_orbitals = sec_sk.m_create(TightBindingOrbital, SlaterKoster.orbitals)
                    sec_orbitals.orbital_name = orbital_name
                    sec_orbitals.atom_index = atom_index
                    sec_orbitals.shell = iShell
                    sec_orbitals.onsite_energy = onSite

        for bond in self.tb_model['bonds']:
            atom1 = bond['atom1']
            atom2 = bond['atom2']
            bond_type = bond['type']
            h_sk = None
            s_sk = None
            if self.tb_model['final_sk'] != {}:
                h_sk = self.tb_model['final_sk'][bond_type]
            if self.tb_model['final_overlap'] != {}:
                s_sk = self.tb_model['final_overlap'][bond_type]

            if h_sk is not None:
                sec_bonds = sec_sk.m_create(SlaterKosterBond, SlaterKoster.bonds)
                sec_bonds.bond_label = bond_type

                center1 = sec_bonds.m_create(TightBindingOrbital, TwoCenterBond.center1)
                center1.atom_index = atom1['index']
                center1.shell = atom1['shell']
                indices = re.findall(r'-?\d+', atom1['cell'])
                center1.cell = [int(index) for index in indices]

                center2 = sec_bonds.m_create(TightBindingOrbital, TwoCenterBond.center2)
                center2.atom_index = atom2['index']
                center2.shell = atom2['shell']
                indices = re.findall(r'-?\d+', atom2['cell'])
                center2.cell = [int(index) for index in indices]
                for sk_label, sk_integral in h_sk.items():
                    setattr(sec_bonds, sk_label, sk_integral)

            if s_sk is not None:
                sec_overlaps = sec_sk.m_create(SlaterKosterBond, SlaterKoster.overlaps)
                sec_overlaps.bond_label = bond_type

                center1 = sec_overlaps.m_create(TightBindingOrbital, TwoCenterBond.center1)
                center1.atom_index = atom1['index']
                center1.shell = atom1['shell']
                indices = re.findall(r'-?\d+', atom1['cell'])
                center1.cell = [int(index) for index in indices]

                center2 = sec_overlaps.m_create(TightBindingOrbital, TwoCenterBond.center2)
                center2.atom_index = atom2['index']
                center2.shell = atom2['shell']
                indices = re.findall(r'-?\d+', atom2['cell'])
                center2.cell = [int(index) for index in indices]
                for sk_label, sk_integral in s_sk.items():
                    setattr(sec_overlaps, sk_label, sk_integral)

    def parse_scc(self):
        """Populates run.calculation with the output of the calculation.
        """
        sec_run = self.archive.run[-1]
        self.archive.run[-1].m_create(Calculation)

        tb_bands = self.tb_model['final_tb_bands']
        frac_k_points = self.tb_model['frac_k_points']
        band_segments_points = self.tb_model['bandSections']['index']
        if band_segments_points is None or len(tb_bands) < 1 or len(frac_k_points) < 1:
            return

        sec_scc = sec_run.calculation[-1]

        sec_k_band = BandStructure()
        sec_k_band.energy_fermi = self.tb_model['fermi_level'] * ureg.eV

        for n1, n2 in band_segments_points:
            sec_k_band_segment = sec_k_band.m_create(BandEnergies)
            sec_k_band_segment.kpoints = frac_k_points[n1: n2 + 1]
            sec_k_band_segment.energies = np.array([tb_bands[n1: n2 + 1]]) * ureg.eV

        sec_scc.band_structure_electronic.append(sec_k_band)

    def get_mainfile_keys(self, **kwargs):
        filepath = kwargs.get('filename')
        tb_model = load_tbm(filepath)
        dft_nomad_entry_id = tb_model['DFTNomadEntryID']
        if dft_nomad_entry_id is not None and dft_nomad_entry_id != '':
            return ['TB_workflow']
        else:
            return True

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name="TBStudio")
        self.tb_model = load_tbm(filepath)
        dft_nomad_entry_id = self.tb_model['DFTNomadEntryID']

        self.parse_system()
        self.parse_method()
        self.parse_scc()

        workflow = SinglePoint()
        workflow.name = "Tight Binding Calculation"
        self.archive.workflow2 = workflow

        if dft_nomad_entry_id is not None and dft_nomad_entry_id != '':
            dft_archive = None
            try:
                dft_archive = archive.m_context.resolve_archive('/entries/{}/archive'.format(dft_nomad_entry_id))
            except:
                pass
            if dft_archive:
                if self._child_archives:
                    tb_workflow = SimulationWorkflow()
                    tb_workflow.name = "Tight Binding"
                    self._child_archives['TB_workflow'].workflow2 = tb_workflow
                    tb_workflow.tasks.append(TaskReference(task=dft_archive.workflow2))
                    tb_workflow.tasks.append(TaskReference(task=self.archive.workflow2))

                    workflow.inputs.append(Link(name='Atomic structure', section=dft_archive.run[0].system[0]))
                    workflow.inputs.append(
                        Link(name='DFT band structure', section=dft_archive.run[0].calculation[0]))
                    workflow.outputs.append(
                        Link(name='TB band structure', section=archive.run[0].calculation[0]))
