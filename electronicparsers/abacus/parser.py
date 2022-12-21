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
import logging
import numpy as np
from collections import namedtuple
from datetime import datetime

from .metainfo import m_env
from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    AtomParameters, Method, BasisSet, BasisSetCellDependent, Electronic, Smearing, Scf,
    DFT, XCFunctional, Functional, KMesh)
from nomad.datamodel.metainfo.simulation.system import System, Atoms, Symmetry
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, Dos, DosValues, BandStructure, BandEnergies, EnergyEntry, ScfIteration,
    Forces, ForcesEntry, Stress, StressEntry)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization, MolecularDynamics, SinglePoint
from nomad.datamodel.metainfo.simulation.workflow import (
    GeometryOptimization as GeometryOptimization2, MolecularDynamics as MolecularDynamics2,
    MolecularDynamicsMethod, GeometryOptimizationMethod, SinglePoint as SinglePoint2, SinglePointMethod)
from .metainfo.abacus import (
    Method as xsection_method, x_abacus_section_parallel, x_abacus_section_basis_sets, x_abacus_section_specie_basis_set)


# TODO determine if we can update regex to the following
re_float = r'[-+]?\d+\.*\d*(?:[Ee][-+]\d+)?'


class ABACUSInputParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):

        self._quantities = [
            Quantity(
                'stru_filename',
                r'\n *stru_file\s*(\S+)', repeats=False,
            ),
            Quantity(
                'kpt_filename',
                r'\n *kpoint_file\s*(\S+)', repeats=False,
            ),
            Quantity(
                'basis_type',
                r'\n *basis_type\s*(\w+)', repeats=False,
            ),
            Quantity(
                'x_abacus_init_velocities',
                r'\n *init_vel\s*(\d+)', repeats=False, dtype=bool
            ),
            Quantity(
                'xc',
                r'\n *dft_functional\s*(\w+)', repeats=False,
            ),
            Quantity(
                'kpar',
                r'\n *kpar\s*(\d+)', repeats=False
            ),
            Quantity(
                'bndpar',
                r'\n *bndpar\s*(\d+)', repeats=False
            ),
            Quantity(
                'diago_proc',
                r'\n *diago_proc\s*(\d+)', repeats=False
            ),
            Quantity(
                'scf_max_iteration',
                r'\n *scf_nmax\s*(\d+)', repeats=False
            ),
            Quantity(
                'nelec',
                r'\n *nelec\s*(\d+)', repeats=False
            ),
            Quantity(
                'md_type',
                r'\n *md_type\s*(\d+)', repeats=False
            ),
            Quantity(
                'md_nstep',
                r'\n *md_nstep\s*(\d+)', repeats=False
            ),
            Quantity(
                'occupations',
                r'\n *occupations\s*(\w+)', repeats=False,
            ),
            Quantity(
                'smearing_method',
                r'\n *smearing_method\s*(\w+)', repeats=False,
            ),
            Quantity(
                'smearing_width',
                rf'\n *smearing_sigma\s*({re_float})', repeats=False, unit='rydberg'
            ),
            Quantity(
                'dft_plus_u',
                r'\n *dft_plus_u\s*(\d)', repeats=False, dtype=bool
            ),
            Quantity(
                xsection_method.x_abacus_mixing_method,
                rf'\n *mixing_type\s*(\S+)', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_mixing_beta,
                rf'\n *mixing_beta\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_diagonalization_algorithm,
                rf'\n *ks_solver\s*(\w+)', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_dispersion_correction_method,
                r'\n *vdw_method\s*(\S+)', repeats=False,
            ),
            Quantity(
                xsection_method.x_abacus_gamma_algorithms,
                rf'\n *gamma_only\s*(\d)', repeats=False, dtype=bool
            ),
            Quantity(
                xsection_method.x_abacus_scf_threshold_density,
                rf'\n *scf_thr\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_initial_magnetization_total,
                rf'\n *tot_magnetization\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_hse_omega,
                rf'\n *exx_hse_omega\s*({re_float})', repeats=False, unit='1/bohr'
            ),
            Quantity(
                xsection_method.x_abacus_hybrid_xc_coeff,
                rf'\n *exx_hybrid_alpha\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_exx_ccp_rmesh_times,
                rf'\n *exx_ccp_rmesh_times\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_exx_dm_threshold,
                rf'\n *exx_dm_threshold\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_exx_cauchy_threshold,
                rf'\n *exx_cauchy_threshold\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_exx_schwarz_threshold,
                rf'\n *exx_schwarz_threshold\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_exx_c_threshold,
                rf'\n *exx_c_threshold\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_exx_v_threshold,
                rf'\n *exx_v_threshold\s*({re_float})', repeats=False
            ),
            Quantity(
                xsection_method.x_abacus_exx_pca_threshold,
                rf'\n *exx_pca_threshold\s*({re_float})', repeats=False
            )
        ]


class ABACUSOutParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        def str_to_sites(val_in):
            data = dict()
            val = [v.strip().split() for v in val_in.split('\n')][0]
            if len(val) == 5:
                labels, x, y, z, mag = val
            elif len(val) == 8:
                labels, x, y, z, mag, vx, vy, vz = val
                data['velocities'] = np.array(
                    [vx, vy, vz], dtype=float)
            data['labels'] = labels
            data['positions'] = np.array([x, y, z], dtype=float)
            data['magnetic_moments'] = float(mag)
            return data

        def str_to_coordclass(val_in):
            if val_in == 'DIRECT':
                name = 'direct'
            elif val_in == 'CARTESIAN':
                name = 'cartesian'
            return name

        def str_to_matrix(val_in):
            val = [v.strip().split() for v in val_in.split('\n')]
            return np.reshape(val, (3, 3)).astype(float)

        def str_to_dict(val_in):
            data = dict()
            val = val_in.split()
            data[val[0]] = int(val[1])
            return data

        def str_to_kpoints(val_in):
            lines = re.search(
                rf'KPOINTS\s*DIRECT_X\s*DIRECT_Y\s*DIRECT_Z\s*WEIGHT([\s\S]+?)DONE', val_in).group(1).strip().split('\n')
            data = []
            for line in lines:
                data.append(line.strip().split()[1:5])
            # TODO pylinit error, unbalanced-tuple-unpacking
            data = np.array(data, dtype=float)
            kpoints = data[:, :3]
            weights = data[:, 3]
            return kpoints, weights

        def str_to_sticks(val_in):
            Data = namedtuple('PW', ['proc', 'columns', 'pw'])
            val = re.findall(
                rf'\s+({re_float})\s+({re_float})\s+({re_float})\n', val_in)
            data = []
            for v in val:
                data.append(
                    Data(proc=int(v[0]), columns=int(v[1]), pw=int(v[2])))
            return data

        def str_to_orbital(val_in):
            Data = namedtuple(
                'Orbital', ['index', 'l', 'n', 'nr', 'dr', 'rcut', 'check_unit', 'new_unit'])
            val = re.findall(
                rf'\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+({re_float})\s+({re_float})\s+({re_float})\s+({re_float})\n', val_in)
            data = []
            for v in val:
                data.append(Data(index=int(v[0]), l=int(v[1]), n=int(v[2]), nr=int(v[3]), dr=float(
                    v[4]), rcut=float(v[5]), check_unit=float(v[6]), new_unit=float(v[7])))
            return data

        def str_to_energy_occupation(val_in):
            def extract_data(val_in, nks):
                State = namedtuple(
                    'State', ['kpoint', 'energies', 'occupations', 'npws'])
                data = []
                for i in range(nks):
                    kx, ky, kz, npws = re.search(
                        rf'{i+1}/{nks} kpoint \(Cartesian\)\s*=\s*({re_float})\s*({re_float})\s*({re_float})\s*\((\d+)\s*pws\)', val_in).groups()
                    # TODO pylinit error, unbalanced-tuple-unpacking
                    res = np.array(list(map(lambda x: x.strip().split(), re.search(
                        rf'{i+1}/{nks} kpoint \(Cartesian\)\s*=.*\n([\s\S]+?)\n\n', val_in).group(1).split('\n'))), dtype=float)
                    energies = res[:, 1]
                    occupations = res[:, 2]
                    state = State(kpoint=np.array([kx, ky, kz], dtype=float), energies=energies.astype(
                        float), occupations=occupations.astype(float), npws=int(npws))
                    data.append(state)
                return data

            nspin = int(re.search(
                r'STATE ENERGY\(eV\) AND OCCUPATIONS\s*NSPIN\s*==\s*(\d+)', val_in).group(1))
            nks = int(
                re.search(r'\d+/(\d+) kpoint \(Cartesian\)', val_in).group(1))
            data = dict()
            if nspin in [1, 4]:
                data['up'] = extract_data(val_in, nks)
            elif nspin == 2:
                val_up = re.search(
                    r'SPIN UP :([\s\S]+?)\n\nSPIN', val_in).group()
                data['up'] = extract_data(val_up, nks)
                val_dw = re.search(
                    r'SPIN DOWN :([\s\S]+?)(?:\n\n\s*EFERMI|\n\n\n)', val_in).group()
                data['down'] = extract_data(val_dw, nks)
            return data

        def str_to_bandstructure(val_in):
            def extract_data(val_in, nks):
                State = namedtuple('State', ['kpoint', 'energies'])
                data = []
                for i in range(nks):
                    kx, ky, kz = re.search(
                        rf'k\-points{i+1}\(\d+\):\s*({re_float})\s*({re_float})\s*({re_float})', val_in).groups()
                    res = np.array(list(map(lambda x: x.strip().split(), re.search(
                        rf'k\-points{i+1}\(\d+\):.*\n([\s\S]+?)\n\n', val_in).group(1).split('\n'))))
                    energies = res[:, 2]
                    # TODO check this error
                    state = State(kpoint=np.array(
                        [kx, ky, kz], dtype=float), energies=energies.astype(float))
                    data.append(state)
                return data

            nks = int(re.search(r'k\-points\d+\((\d+)\)', val_in).group(1))
            data = dict()
            if re.search('spin up', val_in) and re.search('spin down', val_in):
                val = re.search(r'spin up :\n([\s\S]+?)\n\n\n', val_in).group()
                val_new = extract_data(val, nks)
                data['up'] = val_new[:int(nks / 2)]
                data['down'] = val_new[int(nks / 2):]
            else:
                data['up'] = extract_data(val_in, nks)
            return data

        def str_to_force(val_in):
            data = []
            val = [v.strip().split() for v in val_in.split('\n')]
            for v in val:
                data.append(np.array(v[1:], dtype=float))
            return np.array(data) * ureg.eV / ureg.angstrom

        def str_to_polarization(val_in):
            P = namedtuple('P', ['value', 'mod', 'vector'])
            data = np.array(val_in.split(), dtype=float)
            unit = ureg.C / ureg.meter ** 2
            return P(value=data[0] * unit, mod=data[1], vector=data[2:] * unit)

        atom_quantities = [
            Quantity(
                'label', r'atom label\s*=\s*(\w+)'
            ),
            Quantity(
                'orbital', r'L=\d+, number of zeta\s*=\s*(\d+)', repeats=True
            ),
            Quantity(
                'natoms', r'number of atom for this type\s*=\s*(\d+)',
            ),
            Quantity(
                'start_magnetization', r'start magnetization\s*=\s*(\w+)', repeats=True,
                str_operation=lambda x: x == 'TRUE'
            ),
            Quantity(
                'noncollinear_magnetization',
                rf'noncollinear magnetization_x\s*=\s*({re_float})\n\s*noncollinear magnetization_y\s*=\s*({re_float})\n\s*noncollinear magnetization_z\s*=\s*({re_float})\n\s*',
                dtype=float
            )
        ]

        structure_quantities = [
            Quantity(
                'sites', rf'tau[cd]_([a-zA-Z]+)\d+\s+({re_float})\s+({re_float})\s+({re_float})\s+({re_float})\s+({re_float})\s+({re_float})\s+({re_float})',
                repeats=True, str_operation=str_to_sites
            ),
            Quantity(
                'sites', rf'tau[cd]_([a-zA-Z]+)\d+\s+({re_float})\s+({re_float})\s+({re_float})\s+({re_float})',
                repeats=True, str_operation=str_to_sites
            ),
            Quantity(
                'units', rf'UNIT = ({re_float}) Bohr',
                dtype=float, repeats=False, unit='bohr'
            ),
            Quantity(
                'coord_class', r'(DIRECT) COORDINATES|(CARTESIAN) COORDINATES',
                repeat=False, str_operation=str_to_coordclass
            )
        ]

        symmetry_quantities = [
            Quantity(
                'lattice_vectors',
                rf'LATTICE VECTORS: \(CARTESIAN COORDINATE: IN UNIT OF A0\)\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n',
                str_operation=str_to_matrix, convert=False, repeats=False,
            ),
            Quantity(
                'right_hand_lattice',
                r'right hand lattice\s*=\s*(\d+)'
            ),
            Quantity(
                'norm_a',
                rf'NORM_A\s*=\s*({re_float})',
            ),
            Quantity(
                'norm_b',
                rf'NORM_B\s*=\s*({re_float})',
            ),
            Quantity(
                'norm_c',
                rf'NORM_C\s*=\s*({re_float})',
            ),
            Quantity(
                'alpha',
                rf'ALPHA\s*\(DEGREE\)\s*=\s*({re_float})'
            ),
            Quantity(
                'beta',
                rf'BETA\s*\(DEGREE\)\s*=\s*({re_float})'
            ),
            Quantity(
                'gamma',
                rf'GAMMA\s*\(DEGREE\)\s*=\s*({re_float})'
            ),
            Quantity(
                'bravais_name',
                r'BRAVAIS LATTICE NAME\s*=\s*([.\w\(\)\- ]+)'
            ),
            Quantity(
                'ibrav',
                r'IBRAV\s*=\s*([\w ]+)', dtype=int
            ),
            Quantity(
                'number_of_rotation_matrices',
                r'ROTATION MATRICES\s*=\s*(\d+)'
            ),
            Quantity(
                'number_of_point_group_operations',
                r'PURE POINT GROUP OPERATIONS\s*=\s*(\d+)'
            ),
            Quantity(
                'number_of_space_group_operations',
                r'SPACE GROUP OPERATIONS\s*=\s*(\d+)'
            ),
            Quantity(
                'point_group',
                r'POINT GROUP\s*=\s*([\w\_]+)', convert=False
            )
        ]

        orbital_quantities = [
            Quantity(
                'delta_k',
                rf'delta k\s*\(1/Bohr\)\s*=\s*({re_float})', unit='1/bohr', dtype=float
            ),
            Quantity(
                'delta_r',
                rf'delta r\s*\(Bohr\)\s*=\s*({re_float})', unit='bohr', dtype=float
            ),
            Quantity(
                'dr_uniform',
                rf'dr_uniform\s*\(Bohr\)\s*=\s*({re_float})', unit='bohr', dtype=float
            ),
            Quantity(
                'rmax',
                rf'rmax\s*\(Bohr\)\s*=\s*({re_float})', unit='bohr', dtype=float
            ),
            Quantity(
                'kmesh',
                rf'kmesh\s*=\s*(\d+)', dtype=int
            ),
            Quantity(
                'orbital_information',
                r'ORBITAL\s*L\s*N\s*nr\s*dr\s*RCUT\s*CHECK_UNIT\s*NEW_UNIT\n([\s\S]+)SET NONLOCAL PSEUDOPOTENTIAL PROJECTORS',
                convert=False, str_operation=str_to_orbital, repeats=True
            )
        ]

        header_quantities = [
            Quantity(
                'number_of_species',
                r'ntype\s*=\s*(\d+)', dtype=int
            ),
            Quantity(
                'alat',
                rf'lattice constant \(Bohr\)\s*=\s*({re_float})', unit='bohr', dtype=float
            ),
            Quantity(
                'atom_labels', r'atom label\s*=\s*(\w+)', repeats=True
            ),
            Quantity(
                'number_of_atoms_for_labels', r'number of atom for this type\s*=\s*(\d+)', repeats=True
            ),
            Quantity(
                'atom_data',
                r'READING ATOM TYPE\s*\d+([\s\S]+?)\n\n', repeats=True,
                sub_parser=TextParser(quantities=atom_quantities), convert=False
            ),
            Quantity(
                'number_of_atoms',
                r'TOTAL ATOM NUMBER\s*=\s*(\d+)', dtype=int
            ),
            Quantity(
                'positions',
                rf'(CARTESIAN COORDINATES \( UNIT = {re_float} Bohr \)\.+\n\s*atom\s*x\s*y\s*z\s*mag(\s*vx\s*vy\s*vz\s*|\s*)\n[\s\S]+?)\n\n|(DIRECT COORDINATES\n\s*atom\s*x\s*y\s*z\s*mag(\s*vx\s*vy\s*vz\s*|\s*)\n[\s\S]+?)\n\n',
                sub_parser=TextParser(quantities=structure_quantities), convert=False, repeats=False,
            ),
            Quantity(
                'orbital_files',
                r'orbital file:\s*(\S+)', repeats=True
            ),
            Quantity(
                'cell_volume',
                rf'Volume \(Bohr\^3\)\s*=\s*({re_float})', unit='bohr**3', dtype=float
            ),
            Quantity(
                'units',
                r'Lattice vectors: \(Cartesian coordinate: in unit of (\w+)\)'
            ),
            Quantity(
                'lattice_vectors',
                rf'Lattice vectors: \(Cartesian coordinate: in unit of a_0\)\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n',
                str_operation=str_to_matrix, convert=False, repeats=False,
            ),
            Quantity(
                'reciprocal_units',
                r'Reciprocal vectors: \(Cartesian coordinate: in unit of ([\w\/ ]+)\)', flatten=False
            ),
            Quantity(
                'reciprocal_vectors',
                rf'Reciprocal vectors: \(Cartesian coordinate: in unit of 2 pi/a_0\)\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n',
                str_operation=str_to_matrix, convert=False, repeats=False,
            ),
            Quantity(
                'pseudopotential',
                r'(Read in pseudopotential file is [\s\S]+?\n\n)', repeats=True,
                sub_parser=TextParser(quantities=[
                    Quantity('filename', r'file is\s*(\S+)'),
                    Quantity(
                        'type', r'pseudopotential type\s*=\s*(\w+)', flatten=False),
                    Quantity(
                        'xc', r'exchange-correlation functional\s*=\s*(\w+)', flatten=False),
                    Quantity(
                        'valence', rf'valence electrons\s*=\s*({re_float})'),
                    Quantity('lmax', rf'lmax\s*=\s*({re_float})'),
                    Quantity('nzeta',
                             rf'number of zeta\s*=\s*({re_float})', dtype=int),
                    Quantity('nprojectors',
                             rf'number of projectors\s*=\s*({re_float})', dtype=int)
                ]
                )
            ),
            Quantity(
                'fermi_energy_in',
                rf'read in fermi energy\s*=\s*({re_float})', dtype=float, repeats=True
            ),
            Quantity(xsection_method.x_abacus_pao_radial_cutoff,
                     rf'PAO radial cut off \(Bohr\)\s*=\s*({re_float})', unit='bohr', dtype=float, repeats=False),
            Quantity(
                'number_of_electrons_out',
                rf'total electron number of element \w+\s*=\s*(\d+)', repeats=True
            ),
            Quantity(
                'occupied_bands',
                rf'occupied bands\s*=\s*({re_float})'
            ),
            Quantity('nlocal', rf'NLOCAL\s*=\s*({re_float})', repeats=False),
            Quantity(
                'nbands',
                rf'NBANDS\s*=\s*({re_float})', repeats=False
            ),
            Quantity(
                'symmetry',
                r'(LATTICE VECTORS: \(CARTESIAN COORDINATE: IN UNIT OF A0\)\s*[\s\S]+?)\n\n', repeats=False,
                sub_parser=TextParser(quantities=symmetry_quantities)
            ),
            Quantity(
                'number_of_spin_channels',
                r'nspin\s*=\s*(\d+)', dtype=int, repeats=False
            ),
            Quantity(
                'ksampling_method',
                r'Input type of k points\s*=\s*([\w\-\(\) ]+)', str_operation=lambda x:x
            ),
            Quantity(
                'nkstot',
                r'nkstot\s*=\s*(\d+)', dtype=int
            ),
            Quantity(
                'nkstot_ibz',
                r'nkstot_ibz\s*=\s*(\d+)', dtype=int
            ),
            Quantity(
                'k_points',
                r'minimum distributed K point number\s*=\s*\d+([\s\S]+?DONE : INIT K-POINTS Time)',
                str_operation=str_to_kpoints,
            ),
            Quantity(
                'density_cutoff',
                rf'energy cutoff for charge/potential \(unit:Ry\)\s*=\s*({re_float})', unit='rydberg', dtype=float
            ),
            Quantity(
                'density_fft_grid',
                r'\[fft grid for charge/potential\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'
            ),
            Quantity(
                'fft_grid_division',
                r'\[fft grid division\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'
            ),
            Quantity(
                'nbxx',
                r'nbxx\s*=\s*(\d+)'
            ),
            Quantity(
                'nrxx',
                r'nrxx\s*=\s*(\d+)'
            ),
            Quantity(
                'number_of_pw_for_density',
                r'SETUP PLANE WAVES FOR CHARGE/POTENTIAL\n\s*number of plane waves\s*=\s*(\d+)'
            ),
            Quantity(
                'number_of_sticks_for_density',
                r'SETUP PLANE WAVES FOR CHARGE/POTENTIAL\n.*\n\s*number of sticks\s*=\s*(\d+)\n'
            ),
            Quantity(
                'parallel_pw_for_density',
                r'PARALLEL PW FOR CHARGE/POTENTIAL\n\s*PROC\s*COLUMNS\(POT\)\s*PW\n([\s\S]+?)\-+',
                str_operation=str_to_sticks, convert=False
            ),
            Quantity(
                'number_of_g',
                r'number of \|g\|\s*=\s*(\d+)'
            ),
            Quantity(
                'max_g',
                rf'max \|g\|\s*=\s*({re_float})'
            ),
            Quantity(
                'min_g',
                rf'min \|g\|\s*=\s*({re_float})'
            ),
            Quantity(
                'wavefunction_cutoff',
                rf'energy cutoff for wavefunc \(unit:Ry\)\s*=\s*({re_float})', unit='rydberg', dtype=float
            ),
            Quantity(
                'wavefunction_fft_grid',
                r'\[fft grid for wave functions\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'
            ),
            Quantity(
                'number_of_pw_for_wavefunction',
                r'SETUP PLANE WAVES FOR WAVE FUNCTIONS\n[\s\S]+\s*number of plane waves\s*=\s*(\d+)'
            ),
            Quantity(
                'number_of_sticks_for_wavefunction',
                r'SETUP PLANE WAVES FOR WAVE FUNCTIONS\n[\s\S]+\s*number of sticks\s*=\s*(\d+)\n'
            ),
            Quantity(
                'parallel_pw_for_wavefunction',
                r'PARALLEL PW FOR WAVE FUNCTIONS\n\s*PROC\s*COLUMNS\(W\)\s*PW\n([\s\S]+?)\-+',
                str_operation=str_to_sticks, convert=False
            ),
            Quantity(
                'number_of_total_pw',
                r'number of total plane waves\s*=\s*(\d+)'
            ),
            Quantity(
                'total_number_of_nlocal_projectors',
                r'TOTAL NUMBER OF NONLOCAL PROJECTORS\s*=\s*(\d+)'
            ),
            Quantity(
                'init_chg',
                rf'init_chg\s*=\s*(\w+)'
            ),
            Quantity(
                'max_mesh_in_pp',
                rf'max mesh points in Pseudopotential\s*=\s*(\d+)'
            ),
            Quantity(
                'dq',
                rf'dq\(describe PAO in reciprocal space\)\s*=\s*({re_float})'
            ),
            Quantity(
                'max_q',
                rf'max q\s*=\s*({re_float})'
            ),
            Quantity(
                'number_of_pseudo_ao',
                r'number of pseudo atomic orbitals for (\w+) is (\d+)', repeats=True,
                str_operation=str_to_dict, convert=False
            ),
            Quantity(
                'orbital_settings',
                r'SETUP ONE DIMENSIONAL ORBITALS/POTENTIAL\s*([\s\S]+?)SETUP THE TWO-CENTER INTEGRATION TABLES',
                sub_parser=TextParser(quantities=orbital_quantities), convert=False
            ),
            Quantity(
                'allocation_method',
                r'divide the H&S matrix using ([\w ]+ algorithms\.\n[\s\S]+?)\n\n',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'method', r'([\w ]+) algorithms', dtype=str, str_operation=lambda x:x
                    ),
                    Quantity(
                        'nb2d', r'nb2d\s*=\s*(\d+)', dtype=int
                    ),
                    Quantity(
                        'trace_loc_row', r'trace_loc_row dimension\s*=\s*(\d+)', dtype=int
                    ),
                    Quantity(
                        'trace_loc_col', r'trace_loc_row dimension\s*=\s*(\d+)', dtype=int
                    ),
                    Quantity(
                        'nloc', r'nloc\s*=\s*(\d+)', dtype=int
                    ),
                ])
            ),
        ]

        search_quantities = [
            Quantity(
                'search_adjacent_atoms',
                r'SETUP SEARCHING RADIUS FOR PROGRAM TO SEARCH ADJACENT ATOMS\s*([\s\S]+?)\n\n',
                sub_parser=TextParser(quantities=[
                    Quantity('longest_orb_rcut',
                             rf'longest orb rcut \(Bohr\)\s*=\s*({re_float})', unit='bohr', dtype=float),
                    Quantity('longest_nonlocal_projector_rcut',
                             rf'longest nonlocal projector rcut \(Bohr\)\s*=\s*({re_float})', unit='bohr', dtype=float),
                    Quantity('searching_radius',
                             rf'searching radius is \(Bohr\)\)\s*=\s*({re_float})', unit='bohr', dtype=float),
                    Quantity('searching_radius_unit',
                             rf'searching radius unit is \(Bohr\)\)\s*=\s*({re_float})', unit='bohr', dtype=float),
                ]
                )
            ),
            Quantity(
                'grid_integration',
                r'SETUP EXTENDED REAL SPACE GRID FOR GRID INTEGRATION\s*([\s\S]+?)\n\n',
                sub_parser=TextParser(quantities=[
                    Quantity('read_space_grid',
                             r'\[real space grid\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'),
                    Quantity('big_cell_numbers_in_grid',
                             r'\[big cell numbers in grid\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'),
                    Quantity('meshcell_numbers_in_big_cell',
                             r'\[meshcell numbers in big cell\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'),
                    Quantity('extended_fft_grid',
                             r'\[extended fft grid\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'),
                    Quantity('extended_fft_grid_dim',
                             r'\[dimension of extened grid\]\s*=\s*(\d+)[,\s]*(\d+)[,\s]*(\d+)[,\s]*'),
                    Quantity('atom_number',
                             r'Atom number in sub-FFT-grid\s*=\s*(\d+)', dtype=int),
                    Quantity('local_orbitals_number',
                             r'Local orbitals number in sub-FFT-grid\s*=\s*(\d+)', dtype=int),
                    Quantity('nnr', r'ParaV\.nnr\s*=\s*(\d+)', dtype=int),
                    Quantity('nnrg', r'nnrg\s*=\s*(\d+)', dtype=int),
                    Quantity('nnrg_last', r'nnrg_last\s*=\s*(\d+)', dtype=int),
                    Quantity('nnrg_now', r'nnrg_now\s*=\s*(\d+)', dtype=int),
                    Quantity('lgd_last', r'nnrg_now\s*=\s*(\d+)', dtype=int),
                    Quantity('lgd_now', r'nnrg_now\s*=\s*(\d+)', dtype=int),
                ]
                )
            )
        ]

        calculation_quantities = [
            Quantity(
                'energy_occupation',
                r'(STATE ENERGY\(eV\) AND OCCUPATIONS\s*NSPIN\s*==\s*\d+[\s\S]+?(?:\n\n\s*EFERMI|\n\n\n))', repeats=False,
                str_operation=str_to_energy_occupation, convert=False
            ),
            Quantity(
                'reference_fermi',
                rf'EFERMI\s*=\s*({re_float})\s*eV', unit='eV', dtype=float
            ),
            Quantity(
                'total',
                rf'\s*final etot is\s*({re_float})\s*eV', unit='eV', dtype=float
            ),
            Quantity(
                'forces',
                r'TOTAL\-FORCE\s*\(eV/Angstrom\)\n\n.*\s*atom\s*x\s*y\s*z\n([\s\S]+?)\n\n',
                str_operation=str_to_force, convert=False
            ),
            Quantity(
                'stress',
                rf'(?:TOTAL\-|MD\s*)STRESS\s*\(KBAR\)\n\n.*\n\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n',
                str_operation=str_to_matrix, unit='kilobar', convert=False
            ),
            Quantity(
                'pressure',
                rf'TOTAL\-PRESSURE:\s*({re_float})\s*KBAR', unit='kilobar', dtype=float
            ),
            Quantity(
                'positions',
                rf'(CARTESIAN COORDINATES \( UNIT = {re_float} Bohr \)\.+\n\s*atom\s*x\s*y\s*z\s*mag\s*vx\s*vy\s*vz\s*\n[\s\S]+?)\n\n|(DIRECT COORDINATES\n\s*atom\s*x\s*y\s*z\s*mag\s*vx\s*vy\s*vz\s*\n[\s\S]+?)\n\n',
                sub_parser=TextParser(quantities=structure_quantities), convert=False,
            ),
            Quantity(
                'cell_volume',
                rf'Volume \(Bohr\^3\)\s*=\s*({re_float})', unit='bohr**3', dtype=float
            ),
            Quantity(
                'units',
                r'Lattice vectors: \(Cartesian coordinate: in unit of (\w+)\)'
            ),
            Quantity(
                'lattice_vectors',
                rf'Lattice vectors: \(Cartesian coordinate: in unit of a_0\)\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n',
                str_operation=str_to_matrix, convert=False, repeats=False,
            ),
            Quantity(
                'reciprocal_units',
                r'Reciprocal vectors: \(Cartesian coordinate: in unit of ([\w\/ ]+)\)', flatten=False
            ),
            Quantity(
                'reciprocal_vectors',
                rf'Reciprocal vectors: \(Cartesian coordinate: in unit of 2 pi/a_0\)\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n\s*({re_float})\s*({re_float})\s*({re_float})\n',
                str_operation=str_to_matrix, convert=False, repeats=False,
            ),
            Quantity(
                'k_points',
                r'minimum distributed K point number\s*=\s*\d+([\s\S]+?DONE : INIT K-POINTS Time)',
                str_operation=str_to_kpoints,
            )
        ] + search_quantities

        scf_quantities = [
            Quantity(
                'iteration',
                rf'(ELEC\s*=\s*[+\d]+\s*\-+[\s\S]+?\s*E_Fermi\s*{re_float}\s*{re_float})\n', repeats=True,
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'elec_step', r'ELEC\s*=\s*[+]?(\d+)', dtype=int
                    ),
                    Quantity(
                        'density_error', rf'Density error is\s*({re_float})', dtype=float
                    ),
                    Quantity(
                        'energy_total_scf_iteration', rf'E_KohnSham\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'x_abacus_energy_total_harris_foulkes_estimate', rf'E_Harris\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_fermi', rf'E_Fermi\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_band', rf'E_band\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_one_elec', rf'E_one_elec\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'correction_hartree', rf'E_Hartree\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'XC_functional', rf'E_xc\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_ewald', rf'E_ewald\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_demet', rf'E_demet\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_descf', rf'E_descf\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_efield', rf'E_efield\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'hartree_fock_X_scaled', rf'E_exx\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'e_vdw', rf'E_vdwD\d+\s*{re_float}\s*({re_float})', dtype=float, unit='eV'
                    ),
                    Quantity(
                        'magnetization_total',
                        rf'total magnetism \(Bohr mag/cell\)\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float, unit='bohr_magneton'
                    ),
                    Quantity(
                        'magnetization_absolute',
                        rf'absolute magnetism \(Bohr mag/cell\)\s*=\s*({re_float})',
                        dtype=float, unit='bohr_magneton'
                    ),
                ]
                )
            )
        ] + calculation_quantities

        nscf_quantities = [
            Quantity(
                'band_structure',
                r'(band eigenvalue in this processor \(eV\)\s*:\n[\s\S]+?\n\n\n)',
                str_operation=str_to_bandstructure, convert=False
            ),
            Quantity(
                'min_state_energy',
                rf'min state energy (eV)\s*=\s*({re_float})', unit='eV', dtype=float, repeats=True
            ),
            Quantity(
                'max_state_energy',
                rf'max state energy (eV)\s*=\s*({re_float})', unit='eV', dtype=float, repeats=True
            ),
            Quantity(
                'delta_energy',
                rf'delta energy interval (eV)\s*=\s*({re_float})', unit='eV', dtype=float, repeats=True
            ),
            Quantity(
                'nbands',
                rf'number of bands\s*=\s*(\d+)', dtype=int, repeats=True
            ),
            Quantity(
                'sum_bands',
                rf'sum up the states\s*=\s*(\d+)', dtype=int, repeats=True
            ),
            Quantity(
                'fermi_energy_dos',
                rf'Fermi energy (?:\(spin = \d+\)\s*|\s*)is\s*({re_float})\s*Rydberg', dtype=float, repeats=False
            ),
            Quantity(
                'ionic_phase',
                rf'The Ionic Phase:\s*({re_float})', dtype=float
            ),
            Quantity(
                'electronic_phase',
                rf'Electronic Phase:\s*({re_float})', dtype=float
            ),
            Quantity(
                'polarization',
                r'(The calculated polarization direction is in \w+ direction[\s\S]+?C/m\^2)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'direction', r'The calculated polarization direction is in (\w+) direction'),
                    Quantity(
                        'P',
                        rf'P\s*=\s*({re_float})\s*\(mod\s*({re_float})\)\s*\(\s*({re_float}),\s*({re_float}),\s*({re_float})\)\s*C/m\^2',
                        str_operation=str_to_polarization, convert=False)
                ])
            )
        ] + search_quantities

        relax_quantities = [
            Quantity(
                'ion_step', r'(?:STEP OF ION RELAXATION\s*:\s*|RELAX IONS\s*:\s*\d+\s*\(in total:\s*)(\d+)', dtype=int
            ),
            Quantity(
                'self_consistent',
                r'((?:STEP OF ION RELAXATION|RELAX IONS)\s*:\s*\d+[\s\S]+?(?:Setup the|\!FINAL_ETOT_IS))',
                repeats=False, sub_parser=TextParser(quantities=scf_quantities)
            )
        ]

        fullscf_quantities = [
            Quantity(
                'self_consistent',
                r'([^NON]SELF-CONSISTENT[\s\S]+?\!FINAL_ETOT_IS)',
                repeats=False, sub_parser=TextParser(quantities=scf_quantities)
            )
        ]

        nonscf_quantities = [
            Quantity(
                'nonself_consistent',
                r'(NONSELF\-CONSISTENT[\s\S]+?\|CLASS_NAME)',
                repeats=False, sub_parser=TextParser(quantities=nscf_quantities)
            )
        ]

        md_quantities = [
            Quantity(
                'md_step', r'STEP OF MOLECULAR DYNAMICS\s*:\s*(\d+)', dtype=int
            ),
            Quantity(
                'self_consistent',
                r'(STEP OF MOLECULAR DYNAMICS\s*:\s*\d+[\s\S]+?Energy\s*Potential\s*Kinetic)',
                repeats=False, sub_parser=TextParser(quantities=scf_quantities)
            ),
            Quantity(
                'energy',
                rf'Energy\s*Potential\s*Kinetic\s*Temperature\s*(?:Pressure \(KBAR\)\s*\n|\n)\s*({re_float})',
                dtype=float, unit='hartree'
            ),
            Quantity(
                'potential',
                rf'Energy\s*Potential\s*Kinetic\s*Temperature\s*(?:Pressure \(KBAR\)\s*\n|\n)\s*{re_float}\s*({re_float})',
                dtype=float, unit='hartree'
            ),
            Quantity(
                'electronic_kinetic_energy',
                rf'Energy\s*Potential\s*Kinetic\s*Temperature\s*(?:Pressure \(KBAR\)\s*\n|\n)\s*{re_float}\s*{re_float}\s*({re_float})',
                dtype=float, unit='hartree'
            ),
            Quantity(
                'temperature',
                rf'Energy\s*Potential\s*Kinetic\s*Temperature\s*(?:Pressure \(KBAR\)\s*\n|\n)\s*{re_float}\s*{re_float}\s*{re_float}\s*({re_float})',
                dtype=float, unit='kelvin'
            ),
            Quantity(
                'pressure',
                rf'Energy\s*Potential\s*Kinetic\s*Temperature\s*Pressure \(KBAR\)\s*\n\s*{re_float}\s*{re_float}\s*{re_float}\s*{re_float}\s*({re_float})',
                dtype=float, unit='kilobar'
            ),
        ]

        self._quantities = [
            Quantity(
                'program_version',
                r'Version:\s*(.*)\n', str_operation=lambda x: ''.join(x)
            ),
            Quantity(
                'nproc',
                r'Processor Number is\s*(\d+)\n', dtype=int
            ),
            Quantity(
                'start_date_time',
                r'Start Time is\s*(.*)\n', str_operation=lambda x: ''.join(x)
            ),
            Quantity(
                'input_filename', r'global_in_card\s*=\s*(.*)\n',
            ),
            Quantity(
                'pseudopotential_dirname', r'pseudo_dir\s*=\s*([.\w\-\\ ]*?)',
            ),
            Quantity(
                'basis_set_dirname', r'orbital_dir\s*=\s*([.\w\-\\ ]*?)',
            ),
            Quantity(
                'drank', r'DRANK\s*=\s*(\d+)\n', dtype=int
            ),
            Quantity(
                'dsize', r'DSIZE\s*=\s*(\d+)\n', dtype=int
            ),
            Quantity(
                'dcolor', r'DCOLOR\s*=\s*(\d+)\n', dtype=int
            ),
            Quantity(
                'grank', r'GRANK\s*=\s*(\d+)\n', dtype=int
            ),
            Quantity(
                'gsize', r'GSIZE\s*=\s*(\d+)\n', dtype=int
            ),
            Quantity(
                'header',
                r'READING GENERAL INFORMATION([\s\S]+?)(?:[NON]*SELF-|STEP OF|RELAX CELL)', sub_parser=TextParser(quantities=header_quantities)
            ),
            Quantity(
                'full_scf',
                r'([^NON]SELF-CONSISTENT[\s\S]+?)Total\s*Time', sub_parser=TextParser(quantities=fullscf_quantities), repeats=True
            ),
            Quantity(
                'non_scf',
                r'(NONSELF-CONSISTENT[\s\S]+?)Total\s*Time', sub_parser=TextParser(quantities=nonscf_quantities), repeats=True
            ),
            Quantity(
                'geometry_optimization',
                r'((STEP OF ION RELAXATION|RELAX IONS)\s*:\s*\d+[\s\S]+?(Setup the|\!FINAL_ETOT_IS))',
                sub_parser=TextParser(quantities=relax_quantities), repeats=True
            ),
            Quantity(
                'ion_converged', r'Ion relaxation \(is converged!\)', str_operation=lambda x: True
            ),
            Quantity(
                'force_threshold',
                rf'Ion relaxation is not converged yet \(threshold is\s*({re_float})\)', unit='eV/angstrom', repeats=False
            ),
            Quantity(
                'lattice_converged', r'Lattice relaxation \(is converged!\)', str_operation=lambda x: True
            ),
            Quantity(
                'stress_threshold',
                rf'Lattice relaxation is not converged yet \(threshold is\s*({re_float})\)', unit='kilobar', repeats=False
            ),
            Quantity(
                'molecular_dynamics',
                r'(STEP OF MOLECULAR DYNAMICS\s*:\s*\d+[\s\S]+?(?:\n{4,5}))',
                sub_parser=TextParser(quantities=md_quantities), repeats=True
            ),
            Quantity(
                'final_energy',
                rf'\!FINAL_ETOT_IS\s*({re_float})', dtype=float, unit='eV'
            ),
            Quantity(
                'finish_date_time',
                r'Finish\s*Time\s*:\s*(.*)\n', str_operation=lambda x: ''.join(x)
            ),
            Quantity(
                'total_time',
                rf'Total\s*Time\s*:\s*(\d+)\s*h\s*(\d+)\s*mins\s*(\d+)\s*secs',
                str_operation=lambda x: int(x.strip().split()[0]) * 3600 + int(x.strip().split()[1]) * 60 + int(x.strip().split()[2]), unit='seconds'
            )
        ]


class ABACUSParser:
    def __init__(self):
        # super().__init__(name='parsers/abacus', code_name='ABACUS',
        #                  code_homepage='http://abacus.ustc.edu.cn/',
        #                  mainfile_contents_re=(r'\s*\n\s*WELCOME TO ABACUS'))
        self._metainfo_env = m_env
        self.out_parser = ABACUSOutParser()
        self.input_parser = ABACUSInputParser()
        self.tdos_parser = DataTextParser()
        self.sampling_method = None

        self._xc_map = {
            'PWLDA': [
                {'name': 'LDA_C_PW'}, {'name': 'LDA_X'}],
            'PZ': [
                {'name': 'LDA_C_PZ'}, {'name': 'LDA_X'}],
            'LDA': [
                {'name': 'LDA_C_PZ'}, {'name': 'LDA_X'}],
            'BLYP': [
                {'name': 'GGA_C_LYP'}, {'name': 'GGA_X_B88'}],
            'BP': [
                {'name': 'GGA_C_P86'}, {'name': 'GGA_X_B88'}],
            'PBE': [
                {'name': 'GGA_C_PBE'}, {'name': 'GGA_X_PBE'}],
            'RPBE': [
                {'name': 'GGA_C_PBE'}, {'name': 'GGA_X_RPBE'}],
            'WC': [
                {'name': 'GGA_C_PBE'}, {'name': 'GGA_X_WC'}],
            'PW91': [
                {'name': 'GGA_C_PW91'}, {'name': 'GGA_X_PW91'}],
            'HCTH': [
                {'name': 'GGA_C_HCTH_A'}, {'name': 'GGA_X_HCTH_A'}],
            'OLYP': [
                {'name': 'GGA_C_LYP'}, {'name': 'GGA_X_OPTX'}],
            'REVPBE': [
                {'name': 'GGA_C_PBE'}, {'name': 'GGA_X_PBE_R'}],
            'SCAN': [
                {'name': 'MGGA_C_SCAN'}, {'name': 'MGGA_X_SCAN'}],
            'HF': [{'name': 'HF_X'}],
            'HSE': [{'name': 'HYB_GGA_XC_HSE06'}],
            'PBE0': [
                {'name': 'GGA_C_PBE'}, {
                    'name': 'GGA_X_PBE', 'weight': lambda x: 0.75 if x is None else 1.0 - x},
                {'name': 'HF_X', 'weight': lambda x: 0.25 if x is None else x}],
        }

    def parse_configurations(self):
        sec_run = self.archive.run[-1]
        header = self.out_parser.get('header', {})
        nspin_ori = header.get('number_of_spin_channels')
        nspin = 1 if nspin_ori == 4 else nspin_ori
        nbands = header.get('nbands')

        def parse_bandstructure(section):
            sec_scc = sec_run.m_create(Calculation)
            sec_nscf = section.get('nonself_consistent')

            # atom data
            parse_system()

            # search adjacent atoms
            searching_sec = sec_nscf.get('search_adjacent_atoms')
            if searching_sec is not None:
                for key in ['longest_orb_rcut', 'longest_nonlocal_projector_rcut',
                            'searching_radius', 'searching_radius_unit']:
                    val = searching_sec.get(key)
                    if val:
                        setattr(sec_scc, f'x_abacus_{key}', val)

            # grid_integration
            grid_sec = sec_nscf.get('grid_integration')
            if grid_sec is not None:
                for key in ['read_space_grid', 'big_cell_numbers_in_grid',
                            'meshcell_numbers_in_big_cell', 'extended_fft_grid',
                            'extended_fft_grid_dim']:
                    val = grid_sec.get(key)
                    if val is not None:
                        setattr(sec_scc, f'x_abacus_{key}', val)

            sec_k_band = BandStructure()
            sec_scc.band_structure_electronic.append(sec_k_band)
            sec_k_band.reciprocal_cell = sec_run.system[-1].x_abacus_reciprocal_vectors

            # get efermi
            efermi = header.get('fermi_energy_in')
            if efermi is None:
                efermi = sec_nscf.get('fermi_energy_dos')
            if efermi is not None:
                # fermi energy is not spin-dependent
                sec_k_band.energy_fermi = efermi * ureg.rydberg

            band_k_points = []
            band_energies = []
            for slabel, data in sec_nscf.get('band_structure').items():
                for state in data:
                    if slabel == 'up':
                        band_k_points.append(state.kpoint.tolist())
                    band_energies.append(state.energies.tolist())
            sec_k_band_segment = sec_k_band.m_create(BandEnergies)
            sec_k_band_segment.kpoints = np.dot(np.linalg.inv(
                header.get('reciprocal_vectors')), np.array(band_k_points).T).T
            sec_k_band_segment.energies = np.reshape(
                band_energies, (nspin, -1, nbands)) * ureg.eV

        def parse_dos():
            sec_scc = sec_run.calculation[-1]

            # parse TDOS file
            tdos_file = 'TDOS'
            if tdos_file not in os.listdir(self.out_parser.maindir):
                return
            self.tdos_parser.mainfile = os.path.join(
                self.out_parser.maindir, tdos_file)
            sec_dos = Dos()
            sec_scc.dos_electronic.append(sec_dos)
            data = self.tdos_parser.data.T
            sec_dos.n_energies = len(data[0])
            sec_dos.energies = data[0] * ureg.eV
            sec_dos.total.append(DosValues(value=data[1:] * (1 / ureg.eV)))
            # TODO: parse PDOS file

        def parse_scf(iteration):
            sec_scc = sec_run.calculation[-1]
            sec_scf = sec_scc.m_create(ScfIteration)

            density_errors = iteration.get('density_error')
            sec_scf.x_abacus_density_change_scf_iteration = density_errors

            # energies
            sec_scf.x_abacus_energy_total_harris_foulkes_estimate = iteration.x_abacus_energy_total_harris_foulkes_estimate
            sec_scf.energy = Energy(
                total=EnergyEntry(value=iteration.energy_total_scf_iteration))
            if iteration.e_fermi is not None:
                sec_scf.energy.fermi = iteration.e_fermi

            # magnetization
            for key in ['magnetization_total', 'magnetization_absolute']:
                val = iteration.get(key)
                if val is None:
                    continue
                setattr(sec_scf, f'x_abacus_{key}', val)

        def parse_system():
            sec_system = sec_run.m_create(System)
            structure = header.get('positions')

            # structure
            alat = header.get('alat')
            sec_system.x_abacus_alat = alat  # bohr
            sec_atoms = sec_system.m_create(Atoms)
            lattice_vectors = header.get('lattice_vectors') * alat
            sec_atoms.lattice_vectors = lattice_vectors

            labels, positions, mags, velocities = [], [], [], []
            sec_run.x_abacus_init_velocities = self.input_parser.get(
                'x_abacus_init_velocities', 0)
            for site in structure.get('sites', []):
                labels.append(site['labels'])
                positions.append(site['positions'])
                mags.append(site['magnetic_moments'])
                if sec_run.x_abacus_init_velocities:
                    velocities.append(site['velocities'])

            coord_class = structure.get('coord_class')
            if coord_class == 'cartesian':
                units = structure.get('units')
                sec_atoms.positions = np.array(positions) * units
            elif coord_class == 'direct':
                sec_atoms.positions = (np.array(positions) @ lattice_vectors)
            sec_atoms.labels = labels
            if velocities:
                sec_atoms.velocities = velocities * ureg.angstrom / ureg.fs
            sec_system.x_abacus_atom_magnetic_moments = mags
            sec_system.x_abacus_cell_volume = header.get('cell_volume')
            sec_system.x_abacus_reciprocal_vectors = header.get(
                'reciprocal_vectors') * 2 * np.pi / alat

            # symmetry
            symmetry = header.get('symmetry')
            if symmetry:
                sec_system_sym = sec_system.m_create(Symmetry)
                sec_system_sym.crystal_system = symmetry.get('bravais_name')[
                    1].lower()
                brav_dict = {
                    'triclinic': 'a', 'monoclinic': 'b', 'orthorhombic': 'o',
                    'tetragonal': 't', 'hexagonal': 'h', 'cubic': 'c', 'rhombohedral': 'R'}
                ibrav = symmetry.get('ibrav')
                if ibrav:
                    sec_system.x_abacus_ibrav = ibrav
                    if ibrav in [4, 14]:
                        sec_system_sym.bravais_lattice = brav_dict[sec_system_sym.crystal_system]
                    else:
                        sec_system_sym.bravais_lattice = brav_dict[sec_system_sym.crystal_system] + symmetry.get(
                            'bravais_name')[2][0]
                sec_system_sym.x_abacus_point_group_schoenflies_name = symmetry.get(
                    'point_group')
                celldm = [symmetry.get(
                    f'norm_{key}') * alat.to('angstrom').magnitude for key in ['a', 'b', 'c']]
                celldm.extend([symmetry.get(key)
                              for key in ['alpha', 'beta', 'gamma']])
                sec_system.x_abacus_celldm = celldm
                for name in ['rotation_matrices', 'point_group_operations', 'space_group_operations']:
                    val = symmetry.get(f'number_of_{name}')
                    setattr(sec_system_sym, f'x_abacus_number_of_{name}', val)

            # numbers
            sec_atoms.n_atoms = header.get('number_of_atoms')
            sec_system.x_abacus_number_of_species = header.number_of_species
            sec_system.x_abacus_number_of_electrons_out = header.number_of_electrons_out
            sec_system.number_of_electrons_out = self.input_parser.get('nelec')

        def parse_section(section):
            sec_scc = sec_run.m_create(Calculation)

            # atom data
            parse_system()

            sub_section = section.get('self_consistent')
            if sub_section is None:
                return

            # search adjacent atoms
            searching_sec = sub_section.get('search_adjacent_atoms')
            if searching_sec is not None:
                for key in ['longest_orb_rcut', 'longest_nonlocal_projector_rcut',
                            'searching_radius', 'searching_radius_unit']:
                    val = searching_sec.get(key)
                    if val:
                        setattr(sec_scc, f'x_abacus_{key}', val)

            # grid_integration
            grid_sec = sub_section.get('grid_integration')
            if grid_sec is not None:
                for key in ['read_space_grid', 'big_cell_numbers_in_grid',
                            'meshcell_numbers_in_big_cell', 'extended_fft_grid',
                            'extended_fft_grid_dim']:
                    val = grid_sec.get(key)
                    if val is not None:
                        setattr(sec_scc, f'x_abacus_{key}', val)

            # energies
            sec_energy = sec_scc.m_create(Energy)
            vdw_m_dict = {'d2': 'DFT-D2', 'd3_0': 'DFT-D3(0)', 'd3_bj': 'DFT-D3(BJ)'}
            # TODO AN: I do not quite understand this loop over scf_iterations
            # and the loop over iteration
            scf_iteration = sub_section.get('iteration')
            if scf_iteration is not None:
                sec_scc.n_scf_iterations = len(scf_iteration)
                for iteration in scf_iteration:
                    parse_scf(iteration)
                e_vdw = iteration.get('e_vdw', None)
                if e_vdw is not None:
                    sec_energy.van_der_walls = EnergyEntry(value=e_vdw)
                    vdw_method = self.input_parser.get(
                        'x_abacus_dispersion_correction_method')
                    # TODO AN these methods are not in the enumerated list
                    if vdw_method in ['d2', 'd3_0', 'd3_bj']:
                        kind = "G06"
                        sec_run.method[-1].x_abacus_dispersion_correction_method = vdw_m_dict[vdw_method]
                    else:
                        kind = ""
                    sec_run.method[-1].electronic.van_der_waals_method = kind
                sec_energy.xc = EnergyEntry(
                    value=iteration.get('XC_functional'))
                sec_energy.electrostatic = EnergyEntry(
                    correction=iteration.get('correction_hartree'))
                sec_energy.hartree_fock_x_scaled = EnergyEntry(
                    value=iteration.get('hartree_fock_X_scaled'))

                sec_energy.total = EnergyEntry(
                    value=sub_section.get('total'))
                sec_energy.fermi = sub_section.get('reference_fermi')

            # eigenvalues
            eigenvalues = sub_section.get('energy_occupation')
            if eigenvalues is not None:
                kpoints, npws, eigs, eig, occs, occ = [], [], [], [], [], []
                sec_eigenvalues = sec_scc.m_create(BandEnergies)
                for s_label, data in eigenvalues.items():
                    for state in data:
                        if s_label == 'up':
                            kpoints.append(state.kpoint)
                            npws.append(state.npws)
                        eig.append(state.energies)
                        occ.append(state.occupations)
                    eigs.append(eig)
                    occs.append(occ)
                sec_eigenvalues.energies = np.array(eigs) * ureg.eV
                sec_eigenvalues.occupations = np.array(occs)
                sec_eigenvalues.x_abacus_eigenvalues_number_of_planewaves = np.array(
                    npws)
                # kpoints in direct coordinates
                sec_eigenvalues.kpoints = np.dot(np.linalg.inv(
                    header.get('reciprocal_vectors')), np.array(kpoints).T).T

            # force
            forces = sub_section.get('forces')
            if forces is not None:
                sec_scc.forces = Forces(total=ForcesEntry(value=forces))

            # stress and pressure
            stress = sub_section.get('stress')
            pressure = sub_section.get('pressure')
            if stress is not None:
                sec_scc.stress = Stress(total=StressEntry(value=stress))
            if pressure is not None:
                sec_scc.pressure = pressure

            # md settings
            electronic_kinetic_energy = section.get(
                'electronic_kinetic_energy')
            if electronic_kinetic_energy is not None:
                sec_energy.electronic = EnergyEntry(
                    kinetic=electronic_kinetic_energy)
            temperature = section.get('temperature')
            if temperature is not None:
                sec_scc.temperature = temperature
            pressure = section.get('pressure')
            if pressure is not None:
                sec_scc.pressure = pressure
            total_energy = section.get('energy')
            if total_energy is not None:
                sec_energy.total = EnergyEntry(value=total_energy)

        # scf
        for section in self.out_parser.get('full_scf', []):
            parse_section(section)

        # relax/cell-relax/md
        for method in ['geometry_optimization', 'molecular_dynamics']:
            sections = self.out_parser.get(method)
            if sections is not None:
                self.sampling_method = method
                for section in sections:
                    parse_section(section)
                md_nstep_in = self.input_parser.get('md_nstep')
                if md_nstep_in is not None:
                    sec_run.x_abacus_md_nstep_in = md_nstep_in
                md_nstep_out = sections[-1].get('md_step')
                if md_nstep_out is not None:
                    sec_run.x_abacus_md_nstep_out = md_nstep_out + 1

        # nscf
        for section in self.out_parser.get('non_scf', []):
            parse_bandstructure(section)

        if self.sampling_method is None:
            self.sampling_method = 'single_point'

        parse_dos()

        # total time
        sec_run.x_abacus_program_execution_time = self.out_parser.get(
            'total_time')

    def parse_method(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        sec_electronic = sec_method.m_create(Electronic)
        header = self.out_parser.get('header', {})

        # input parameters from INPUT file
        input_file = 'INPUT'
        if input_file in os.listdir(self.out_parser.maindir):
            self.input_parser.mainfile = os.path.join(
                self.out_parser.maindir, input_file)
        sec_method.scf = Scf(
            n_max_iteration=self.input_parser.get('scf_max_iteration'))
        input_names = [
            'scf_threshold_density', 'mixing_method', 'mixing_beta', 'gamma_algorithms',
            'diagonalization_algorithm', 'initial_magnetization_total', 'dispersion_correction_method',
            'exx_ccp_rmesh_times', 'exx_dm_threshold', 'exx_cauchy_threshold', 'exx_schwarz_threshold',
            'exx_c_threshold', 'exx_v_threshold', 'exx_pca_threshold']
        for key in input_names:
            val = self.input_parser.get(f'x_abacus_{key}')
            if val is None:
                continue
            setattr(sec_method, f'x_abacus_{key}', val)

        # kmesh
        sec_kmesh = sec_method.m_create(KMesh)
        nkstot = header.get('nkstot')
        nkstot_ibz = header.get('nkstot_ibz')
        sec_kmesh.n_points = nkstot_ibz if nkstot_ibz is not None else nkstot
        sec_kmesh.generation_method = header.get('ksampling_method')
        sec_kmesh.points, sec_kmesh.weights = header.get('k_points')

        # smearing
        occupations = self.input_parser.get('occupations', 'smearing')
        smearing_kind = None
        if occupations == 'tetrahedra':
            smearing_kind = occupations
        elif occupations == 'fixed':
            smearing_kind = 'empty'
        else:
            smearing_method = self.input_parser.get('smearing_method', 'fixed')
            if smearing_method == 'mp':
                smearing_kind = 'methfessel-paxton'
            elif smearing_method in ['gauss', 'gaussian']:
                smearing_kind = 'gaussian'
            else:
                smearing_kind = 'empty'
        smearing_width = self.input_parser.get('smearing_width')
        if smearing_width is not None:
            smearing_width = smearing_width.to('joule').magnitude
        sec_electronic.smearing = Smearing(
            kind=smearing_kind, width=smearing_width)

        sec_method.x_abacus_basis_type = self.input_parser.get(
            'basis_type', 'pw')

        # pw settings
        for name in ['wavefunction', 'density']:
            cutoff = header.get(f'{name}_cutoff')
            if cutoff is None:
                continue
            sec_method_basis_set = sec_method.m_create(BasisSet)
            sec_method_basis_set.type = 'Numeric AOs' if header.get(
                'orbital_settings') else 'plane waves'
            sec_method_basis_set.kind = name
            sec_basis_set = sec_method_basis_set.m_create(
                BasisSetCellDependent)
            sec_basis_set.planewave_cutoff = cutoff.to(
                'joule').magnitude
            sec_basis_set.kind = 'plane_waves'
            sec_basis_set.name = 'PW_%.1f' % cutoff.magnitude
            for key in ['pw', 'sticks']:
                val = header.get(f'number_of_{key}_for_{name}')
                setattr(
                    sec_method, f'x_abacus_number_of_{key}_for_{name}', val)

        # lcao settings
        orbital_settings = header.get('orbital_settings')
        if orbital_settings:
            sec_basis_set = sec_method.m_create(x_abacus_section_basis_sets)
            for key in ['delta_k', 'delta_r', 'dr_uniform', 'rmax', 'kmesh']:
                val = orbital_settings.get(key)
                setattr(sec_basis_set, f'x_abacus_basis_sets_{key}', val)

            for i, orb in enumerate(orbital_settings.get('orbital_information', [])):
                sec_specie_basis_set = sec_basis_set.m_create(
                    x_abacus_section_specie_basis_set)
                sec_specie_basis_set.x_abacus_specie_basis_set_filename = os.path.basename(
                    header.get('orbital_files')[i])
                ln_list = []
                for data in orb:
                    ln_list.append([data.l, data.n])
                sec_specie_basis_set.x_abacus_specie_basis_set_ln = ln_list
                sec_specie_basis_set.x_abacus_specie_basis_set_rcutoff = data.rcut
                sec_specie_basis_set.x_abacus_specie_basis_set_rmesh = data.nr
                sec_specie_basis_set.x_abacus_specie_basis_set_number_of_orbitals = len(
                    ln_list)

        if self.input_parser.get('dft_plus_u'):
            sec_electronic.method = 'DFT+U'
        else:
            sec_electronic.method = 'DFT'

        # spin mode
        nspin_ori = header.get('number_of_spin_channels')
        nspin = 1 if nspin_ori == 4 else nspin_ori
        sec_electronic.n_spin_channels = nspin
        sec_method.x_abacus_spin_orbit = nspin_ori == 4
        sec_method.x_abacus_noncollinear = bool(header.get(
            'atom_data')[-1].get('noncollinear_magnetization', np.array([])).any())
        # TODO NOMAD metainfo does not include full
        sec_electronic.relativity_method = None if nspin_ori == 4 else 'scalar_relativistic'

        # atom_kind and pseudopotential settings
        pp_xc = ''
        for i, pp in enumerate(header.get('pseudopotential', [])):
            sec_atom_parameters = sec_method.m_create(AtomParameters)
            sec_atom_parameters.label = header.get('atom_data')[i].get('label')
            sec_atom_parameters.n_valence_electrons = pp.get('valence')
            sec_atom_parameters.pseudopotential_name = os.path.basename(
                pp.get('filename', ''))
            sec_method.x_abacus_pao_radial_cutoff = header.get(
                'x_abacus_pao_radial_cutoff')
            for key, val in pp.items():
                if key in ['filename', 'valence'] or val is None:
                    continue
                if key == 'xc':
                    pp_xc = pp.get('xc', None)
                setattr(sec_atom_parameters, f'x_abacus_pp_{key}', val)

        # xc functional from output
        xc_in = self.input_parser.get('xc', None)
        xc = xc_in.upper() if xc_in is not None else pp_xc
        if xc is not None:
            sec_dft = sec_method.m_create(DFT)
            sec_xc_func = sec_dft.m_create(XCFunctional)
            sec_method.x_abacus_xc_functional = xc

            # hybrid func
            hse_omega, hybrid_coeff = None, None
            if xc in ['HYB_GGA_XC_HSE06', 'HSE']:
                hse_omega = self.input_parser.get(
                    'x_abacus_hse_omega', (0.11 / ureg.bohr).to('1/m'))
                if hse_omega is not None:
                    sec_method.x_abacus_hse_omega = hse_omega.magnitude
            if xc in ['HYB_GGA_XC_HSE06', 'HSE', 'PBE0']:
                hybrid_coeff = self.input_parser.get(
                    'x_abacus_hybrid_xc_coeff', 0.25)
                if hybrid_coeff is not None:
                    sec_method.x_abacus_hybrid_xc_coeff = hybrid_coeff

            if 'LDA_' in xc or 'GGA_' in xc or 'HF_' in xc or 'HYB_' in xc:
                xc_meta_list = []
                for xc_i in xc.split('+'):
                    xc_meta_list.append({'name': xc_i})
            else:
                xc_meta_list = self._xc_map.get(xc, [])
            for xc_meta in xc_meta_list:
                xc_func = Functional(name=xc_meta.get('name'))
                if '_X_' in xc_func.name or xc_func.name.endswith('_X'):
                    sec_xc_func.exchange.append(xc_func)
                elif '_C_' in xc_func.name or xc_func.name.endswith('_C'):
                    sec_xc_func.correlation.append(xc_func)
                elif 'HYB' in xc_func.name:
                    sec_xc_func.hybrid.append(xc_func)
                else:
                    sec_xc_func.contributions.append(xc_func)
                weight = xc_meta.get('weight', None)
                if weight is not None and hybrid_coeff is not None:
                    xc_func.weight = weight(float(hybrid_coeff))
                xc_parameters = dict()
                if hse_omega is not None:
                    hybrid_coeff = 0.25 if hybrid_coeff is None else hybrid_coeff
                    xc_parameters.setdefault(
                        '$\\omega$ in m^-1', hse_omega.to('1/m').magnitude)
                if hybrid_coeff is not None:
                    xc_parameters.setdefault(
                        'hybrid coefficient $\\alpha$', hybrid_coeff)
                if xc_parameters:
                    xc_func.parameters = xc_parameters

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger
        self.input_parser.logger = self.logger
        self.tdos_parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging

        self.init_parser()

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(
            name='ABACUS', version=self.out_parser.get('program_version'))
        header = self.out_parser.get('header', {})

        # parallel
        sec_parallel = sec_run.m_create(x_abacus_section_parallel)
        sec_parallel.x_abacus_nproc = self.out_parser.get('nproc')
        for key in ['kpar', 'bndpar', 'diago_proc']:
            val = self.input_parser.get(key)
            if val is not None:
                setattr(sec_parallel, f'x_abacus_{key}', val)
        for key in ['method', 'nb2d', 'trace_loc_row', 'trace_loc_col', 'nloc']:
            allocation_method = header.get('allocation_method')
            if allocation_method is not None:
                val = allocation_method.get(key)
                if val is not None:
                    setattr(sec_parallel, f'x_abacus_allocation_{key}', val)

        # input files
        self.parse_method()
        self.parse_configurations()
        sec_run.x_abacus_stru_filename = self.input_parser.get(
            'stru_filename', 'STRU')
        sec_run.x_abacus_kpt_filename = self.input_parser.get(
            'kpt_filename', 'KPT')
        sec_run.x_abacus_input_filename = self.out_parser.get('input_filename')
        for key in ['basis_set_dirname', 'pseudopotential_dirname']:
            val = self.out_parser.get(key)
            if val is not None:
                setattr(sec_run, f'x_abacus_{key}', val)

        # sampling method
        if self.sampling_method is not None:
            sec_worflow = archive.m_create(Workflow)
            sec_worflow.type = self.sampling_method
            workflow = None
            if self.sampling_method == 'molecular_dynamics':
                sec_md = sec_worflow.m_create(MolecularDynamics)
                workflow = MolecularDynamics2(method=MolecularDynamicsMethod())
                md_type = self.input_parser.get('md_type')
                if md_type == 0:
                    sec_md.thermodynamic_ensemble = 'NVE'
                    workflow.method.thermodynamic_ensemble = 'NVE'
                elif md_type in [1, 2, 3]:
                    sec_md.thermodynamic_ensemble = 'NVT'
                    workflow.method.thermodynamic_ensemble = 'NVT'
            elif self.sampling_method == 'geometry_optimization':
                sec_geometry_opt = sec_worflow.m_create(GeometryOptimization)
                workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
                force_threshold = self.out_parser.get('force_threshold')
                stress_threshold = self.out_parser.get('stress_threshold')
                if force_threshold:
                    sec_geometry_opt.convergence_tolerance_force_maximum = force_threshold.to(
                        'newton').magnitude
                    workflow.method.convergence_tolerance_force_maximum = force_threshold.to(
                        'newton').magnitude
                if stress_threshold:
                    sec_geometry_opt.x_abacus_geometry_optimization_threshold_stress = stress_threshold.to(
                        'pascal').magnitude
                    workflow.method.convergence_tolerance_stress_maximum = stress_threshold.to(
                        'pascal').magnitude
            elif self.sampling_method == 'single_point':
                sec_worflow.m_create(SinglePoint)
                workflow = SinglePoint2(method=SinglePointMethod())
                workflow.method.method = archive.run[-1].method[-1].electronic.method
            archive.workflow2 = workflow
        print(sec_worflow.type)

        # start date
        date_time = self.out_parser.get('start_date_time')
        sec_time = sec_run.m_create(TimeRun)
        if date_time is not None:
            date_time = datetime.strptime(
                date_time.replace(' ', ''), '%a%b%d%H:%M:%S%Y')
            sec_time.date_start = (
                date_time - datetime(1970, 1, 1)).total_seconds()

        # end date
        date_time = self.out_parser.get('finish_date_time')
        if date_time is not None:
            date_time = datetime.strptime(
                date_time.replace(' ', ''), '%a%b%d%H:%M:%S%Y')
            sec_time.date_end = (
                date_time - datetime(1970, 1, 1)).total_seconds()
            sec_run.clean_end = True
