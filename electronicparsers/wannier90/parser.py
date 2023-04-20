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
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Dos, DosValues, BandStructure, BandEnergies, Energy, HoppingMatrix
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, AtomParameters, KMesh, Wannier, Projection
)
from nomad.datamodel.metainfo.simulation.system import System, Atoms, AtomsGroup
from nomad.datamodel.metainfo.workflow import Workflow
from ..utils import get_files

re_n = r'[\n\r]'


class WOutParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        kmesh_quantities = [
            Quantity(
                'n_points', r'Total points[\s=]*(\d+)', dtype=int,
                repeats=False),
            Quantity(
                'grid', r'Grid size *\= *(\d+) *x *(\d+) *x *(\d+)', repeats=False),
            Quantity(
                'k_points', r'\|[\s\d]*(-*\d.[^\|]+)', repeats=True, dtype=float)]

        disentangle_quantities = [
            Quantity(
                'outer', r'\|\s*Outer:\s*([-\d.]+)\s*\w*\s*([-\d.]+)\s*\((?P<__unit>\w+)\)',
                dtype=float, repeats=False),
            Quantity(
                'inner', r'\|\s*Inner:\s*([-\d.]+)\s*\w*\s*([-\d.]+)\s*\((?P<__unit>\w+)\)',
                dtype=float, repeats=False)]

        structure_quantities = [
            Quantity(
                'labels', r'\|\s*([A-Z][a-z]*)', repeats=True),
            Quantity(
                'positions', rf'\|\s*([\-\d\.]+)\s*([\-\d\.]+)\s*([\-\d\.]+)',
                repeats=True, dtype=float)]

        self._quantities = [
            # Program quantities
            Quantity(
                Program.version, r'\s*\|\s*Release\:\s*([\d\.]+)\s*', repeats=False),
            # System quantities
            Quantity(
                'lattice_vectors', r'\s*a_\d\s*([\d\-\s\.]+)',
                repeats=True),
            Quantity(
                'reciprocal_lattice_vectors', r'\s*b_\d\s*([\d\-\s\.]+)',
                repeats=True),
            Quantity(
                'structure', rf'(\s*Fractional Coordinate[\s\S]+?)(?:{re_n}\s*(PROJECTIONS|K-POINT GRID))',
                repeats=False, sub_parser=TextParser(quantities=structure_quantities)),
            # Method quantities
            Quantity(
                'k_mesh', rf'\s*(K-POINT GRID[\s\S]+?)(?:-\s*MAIN)', repeats=False,
                sub_parser=TextParser(quantities=kmesh_quantities)),
            Quantity(
                'Nwannier', r'\|\s*Number of Wannier Functions\s*\:\s*(\d+)',
                repeats=False),
            Quantity(
                'Nband', r'\|\s*Number of input Bloch states\s*\:\s*(\d+)',
                repeats=False),
            Quantity(
                'Niter', r'\|\s*Total number of iterations\s*\:\s*(\d+)',
                repeats=False),
            Quantity(
                'conv_tol', r'\|\s*Convergence tolerence\s*\:\s*([\d.eE-]+)',
                repeats=False),
            Quantity(
                'energy_windows', rf'(\|\s*Energy\s*Windows\s*\|[\s\S]+?)(?:Number of target bands to extract:)',
                repeats=False, sub_parser=TextParser(quantities=disentangle_quantities)),
            # Band related quantities
            Quantity(
                'n_k_segments', r'\|\s*Number of K-path sections\s*\:\s*(\d+)',
                repeats=False),
            Quantity(
                'div_first_k_segment', r'\|\s*Divisions along first K-path section\s*\:\s*(\d+)',
                repeats=False),
            Quantity(
                'band_segments_points', r'\|\s*From\:\s*\w+([\d\s\-\.]+)To\:\s*\w+([\d\s\-\.]+)',
                repeats=True)]


class WInParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        def str_proj_to_list(val_in):
            # To avoid inconsistent regex that can contain or not spaces
            val_n = [x for x in val_in.split('\n') if x]
            return [v.strip('[]').replace(' ', '').split(':') for v in val_n]

        self._quantities = [
            Quantity('energy_fermi', rf'{re_n}fermi_energy\s*=\s*([\d\.\-]+)', repeats=False),
            Quantity('projections',
                     rf'[bB]egin [pP]rojections([\s\S]+?)(?:[eE]nd [pP]rojections)',
                     repeats=False, str_operation=str_proj_to_list)]


class HrParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity('degeneracy_factors', r'\s*written on[\s\w]*:\d*:\d*\s*([\d\s]+)'),
            Quantity('hoppings', rf'\s*([-\d\s.]+)', repeats=False)]


class Wannier90Parser():
    level = 1

    def __init__(self):
        self.wout_parser = WOutParser()
        self.win_parser = WInParser()
        self.band_dat_parser = DataTextParser()
        self.dos_dat_parser = DataTextParser()
        self.hr_parser = HrParser()

        self._input_projection_mapping = {
            'Nwannier': 'n_projected_orbitals',
            'Nband': 'n_bands',
            'conv_tol': 'convergence_tolerance_max_localization'
        }

        self._input_projection_units = {
            'Ang': 'angstrom',
            'Bohr': 'bohr'
        }

        # Angular momentum [l, mr] following Wannier90 tables 3.1 and 3.2
        # TODO move to normalization or utils in nomad?
        self._angular_momentum_orbital_map = {
            's': [0, 1],
            'px': [1, 1],
            'py': [1, 2],
            'pz': [1, 3],
            'dz2': [2, 1],
            'dxz': [2, 2],
            'dyz': [2, 3],
            'dx2-y2': [2, 4],
            'dxy': [2, 5],
            'fz3': [3, 1],
            'fxz2': [3, 2],
            'fyz2': [3, 3],
            'fz(x2-y2)': [3, 4],
            'fxyz': [3, 5],
            'fx(x2-3y2)': [3, 6],
            'fy(3x2-y2)': [3, 7],
            'sp-1': [-1, 1],
            'sp-2': [-1, 2],
            'sp2-1': [-2, 1],
            'sp2-2': [-2, 2],
            'sp2-3': [-2, 3],
            'sp3-1': [-3, 1],
            'sp3-2': [-3, 2],
            'sp3-3': [-3, 3],
            'sp3-4': [-3, 4],
            'sp3d-1': [-4, 1],
            'sp3d-2': [-4, 2],
            'sp3d-3': [-4, 3],
            'sp3d-4': [-4, 4],
            'sp3d-5': [-4, 5],
            'sp3d2-1': [-5, 1],
            'sp3d2-2': [-5, 2],
            'sp3d2-3': [-5, 3],
            'sp3d2-4': [-5, 4],
            'sp3d2-5': [-5, 5],
            'sp3d2-6': [-5, 6]
        }

    def parse_system(self):
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)

        structure = self.wout_parser.get('structure')
        if structure is None:
            self.logger.error('Error parsing the structure from .wout')
            return

        sec_atoms = sec_system.m_create(Atoms)
        if self.wout_parser.get('lattice_vectors', []):
            lattice_vectors = np.vstack(self.wout_parser.get('lattice_vectors', [])[-3:])
            sec_atoms.lattice_vectors = lattice_vectors * ureg.angstrom
        if self.wout_parser.get('reciprocal_lattice_vectors') is not None:
            sec_atoms.lattice_vectors_reciprocal = np.vstack(self.wout_parser.get('reciprocal_lattice_vectors')[-3:]) / ureg.angstrom

        pbc = [True, True, True] if lattice_vectors is not None else [False, False, False]
        sec_atoms.periodic = pbc
        sec_atoms.labels = structure.get('labels')
        if structure.get('positions') is not None:
            sec_atoms.positions = structure.get('positions') * ureg.angstrom

    def parse_method(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        sec_proj = sec_method.m_create(Projection)
        sec_wann = sec_proj.m_create(Wannier)

        # k_mesh section
        kmesh = self.wout_parser.get('k_mesh')
        if kmesh:
            sec_k_mesh = sec_method.m_create(KMesh)
            sec_k_mesh.n_points = kmesh.get('n_points')
            sec_k_mesh.grid = kmesh.get('grid', [])
            if kmesh.get('k_points') is not None:
                sec_k_mesh.points = np.complex128(kmesh.k_points[::2])

        # Wannier90 section
        for key in self._input_projection_mapping.keys():
            setattr(sec_wann, self._input_projection_mapping[key], self.wout_parser.get(key))
        if self.wout_parser.get('Niter'):
            sec_wann.is_maximally_localized = self.wout_parser.get('Niter', 0) > 1
        sec_wann.energy_window_outer = self.wout_parser.get('energy_windows').outer
        sec_wann.energy_window_inner = self.wout_parser.get('energy_windows').inner

    def parse_winput(self, archive):
        sec_run = archive.run[-1]
        try:
            sec_system = sec_run.system[-1]
            sec_atoms = sec_system.atoms
            sec_method = sec_run.method[-1]
        except Exception:
            self.logger.warning('Could not extract system.atoms and method sections for parsing win.')
            return

        # Parsing from input
        win_files = get_files('*.win', self.filepath, '*.wout')
        if not win_files:
            self.logger.warning('Input .win file not found.')
            return
        if len(win_files) > 1:
            self.logger.warning('Multiple win files found. We will parse the first one.')
        self.win_parser.mainfile = win_files[0]

        def fract_cart_sites(sec_atoms, units, val):
            for pos in sec_atoms.positions.to(units):
                if np.array_equal(val, pos.magnitude):
                    index = sec_atoms.positions.magnitude.tolist().index(pos.magnitude.tolist())
                    return sec_atoms.labels[index]

        # Set units in case these are defined in .win
        projections = self.win_parser.get('projections', [])
        if projections:
            if not isinstance(projections, list):
                projections = [projections]
            if projections[0][0] in ['Bohr', 'Angstrom']:
                sec_run.x_wannier90_units = self._input_projection_units[projections[0][0]]
                projections.pop(0)
            else:
                sec_run.x_wannier90_units = 'angstrom'
            if projections[0][0] == 'random':
                return

        # Populating AtomsGroup for projected atoms
        sec_run.x_wannier90_n_atoms_proj = len(projections)
        for nat in range(sec_run.x_wannier90_n_atoms_proj):
            sec_atoms_group = sec_system.m_create(AtomsGroup)
            sec_atoms_group.type = 'projection'
            sec_atoms_group.index = 0  # Always first index (projection on a projection does not exist)
            sec_atoms_group.is_molecule = False

            # atom label always index=0
            try:
                atom = projections[nat][0]
                if atom.startswith('f='):  # fractional coordinates
                    val = [float(x) for x in atom.replace('f=', '').split(',')]
                    val = np.dot(val, sec_atoms.lattice_vectors.magnitude)
                    sites = fract_cart_sites(sec_atoms, sec_run.x_wannier90_units, val)
                elif atom.startswith('c='):  # cartesian coordinates
                    val = [float(x) for x in atom.replace('c=', '').split(',')]
                    sites = fract_cart_sites(sec_atoms, sec_run.x_wannier90_units, val)
                else:  # atom label directly specified
                    sites = atom
                sec_atoms_group.n_atoms = len(sites)  # always 1 (only one atom per proj)
                sec_atoms_group.label = sites
                sec_atoms_group.atom_indices = np.where([
                    x == sec_atoms_group.label for x in sec_atoms.labels])[0]
            except Exception:
                self.logger.warning('Error finding the atom labels for the projection from win.')

            # orbital angular momentum always index=1
            try:
                orbitals = projections[nat][1].split(';')
                sec_atom_parameters = sec_method.m_create(AtomParameters)
                sec_atom_parameters.n_orbitals = len(orbitals)
                angular_momentum = []
                for orb in orbitals:
                    if orb.startswith('l='):  # using angular momentum numbers
                        lmom = orb.split(',mr')[0]
                        mrmom = orb.split(',mr')[-1]
                        val_lmom = [int(x) for x in lmom.replace('l=', '').split(',')]
                        val_mrmom = [int(x) for x in mrmom.replace('=', '').split(',')]
                        val_angmtm = [val_lmom[0], val_mrmom[0]]
                        for key, val in self._angular_momentum_orbital_map.items():
                            orb_ang_mom = [val[i] == val_angmtm[i] for i in range(2)]
                            if all(orb_ang_mom):
                                angular_momentum.append(key)
                    else:  # ang mom label directly specified
                        angular_momentum.append(orb)
                sec_atom_parameters.orbitals = np.array(angular_momentum)
            except Exception:
                self.logger.warning('Projected orbital labels not found from win.')

    def parse_hoppings(self):
        hr_files = get_files('*hr.dat', self.filepath, '*.wout')
        if not hr_files:
            return
        self.hr_parser.mainfile = hr_files[0]

        # Assuming method.projection is parsed before
        sec_scc = self.archive.run[-1].calculation[-1]
        sec_hopping_matrix = sec_scc.m_create(HoppingMatrix)
        sec_hopping_matrix.n_orbitals = self.archive.run[-1].method[-1].projection.wannier.n_projected_orbitals
        deg_factors = self.hr_parser.get('degeneracy_factors', [])
        if deg_factors is not None:
            sec_hopping_matrix.n_wigner_seitz_points = deg_factors[1]
            sec_hopping_matrix.degeneracy_factors = deg_factors[2:]
            full_hoppings = self.hr_parser.get('hoppings', [])
            if full_hoppings is not None:
                sec_hopping_matrix.value = np.reshape(
                    full_hoppings, (sec_hopping_matrix.n_wigner_seitz_points, sec_hopping_matrix.n_orbitals * sec_hopping_matrix.n_orbitals, 7))

        try:
            sec_scc_energy = sec_scc.m_create(Energy)
            # Setting Fermi level to the first orbital onsite energy
            n_wigner_seitz_points_half = int(0.5 * sec_hopping_matrix.n_wigner_seitz_points)
            energy_fermi = sec_hopping_matrix.value[n_wigner_seitz_points_half][0][5] * ureg.eV
            sec_scc_energy.fermi = energy_fermi
            sec_scc_energy.highest_occupied = energy_fermi
        except Exception:
            return

    def get_k_points(self):
        if self.wout_parser.get('reciprocal_lattice_vectors') is None:
            return
        reciprocal_lattice_vectors = np.vstack(self.wout_parser.get('reciprocal_lattice_vectors'))

        n_k_segments = self.wout_parser.get('n_k_segments', [])
        k_symm_points = []
        k_symm_points_cart = []
        for ns in range(n_k_segments):
            k_segments = np.split(self.wout_parser.get('band_segments_points')[ns], 2)
            [k_symm_points_cart.append(np.dot(k_segments[i], reciprocal_lattice_vectors)) for i in range(2)]
            [k_symm_points.append(k_segments[i]) for i in range(2)]

        n_k_segments_points_1 = self.wout_parser.get('div_first_k_segment')
        delta_k = np.linalg.norm(k_symm_points_cart[1] - k_symm_points_cart[0]) / n_k_segments_points_1
        band_segments_points = []
        for ns in range(n_k_segments):
            n_k_segments_points = round(np.linalg.norm(k_symm_points_cart[2 * ns + 1] - k_symm_points_cart[2 * ns]) / delta_k)
            band_segments_points.append(n_k_segments_points)

        kpoints = []
        for n in range(len(band_segments_points)):
            kpoints_segment = [
                k_symm_points[2 * n] + i * (k_symm_points[2 * n + 1] - k_symm_points[2 * n]) / band_segments_points[n]
                for i in range(band_segments_points[n])]
            kpoints.append(kpoints_segment)

        # TODO check having to add manually last point (?)
        band_segments_points[-1] = band_segments_points[-1] + 1
        kpoints[-1].append(k_symm_points[-1])
        n_kpoints = sum(band_segments_points)

        return (n_kpoints, band_segments_points, kpoints)

    def parse_bandstructure(self):
        sec_scc = self.archive.run[-1].calculation[-1]

        try:
            energy_fermi = sec_scc.energy.fermi
        except Exception:
            self.logger.warning('Error setting the Fermi level: not found from hoppings. Setting it to 0 eV')
            energy_fermi = 0.0 * ureg.eV
        energy_fermi_eV = energy_fermi.to('electron_volt').magnitude

        band_files = get_files('*band.dat', self.filepath, '*.wout')
        if not band_files:
            return
        if len(band_files) > 1:
            self.logger.warning('Multiple bandstructure data files found.')
        # Parsing only first *_band.dat file
        self.band_dat_parser.mainfile = band_files[0]

        sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
        sec_k_band.energy_fermi = energy_fermi
        try:
            sec_k_band.reciprocal_cell = self.archive.run[-1].system[0].atoms.lattice_vectors_reciprocal
        except Exception:
            self.logger.warning('Reciprocal cell in band_structure_electronic not set up.')

        if self.band_dat_parser.data is None:
            return
        data = np.transpose(self.band_dat_parser.data)

        (n_kpoints, band_segments_points, kpoints) = self.get_k_points()
        n_segments = len(band_segments_points)
        n_bands = round((len(data[0])) / n_kpoints)
        n_spin = 1

        # reshaping bands into the NOMAD band_structure style
        bands = np.transpose(np.reshape(data[1], (n_bands, n_kpoints)))
        bkp_init = 0
        for n in range(n_segments):
            sec_k_band_segment = sec_k_band.m_create(BandEnergies)
            sec_k_band_segment.n_kpoints = band_segments_points[n]
            sec_k_band_segment.kpoints = kpoints[n]

            bkp_last = bkp_init + band_segments_points[n]
            energies = np.reshape(bands[bkp_init:bkp_last, :], (n_spin, band_segments_points[n], n_bands))
            occs = np.reshape(
                np.array([
                    2.0 if energies[i, j, k] < energy_fermi_eV else 0.0
                    for i in range(n_spin) for j in range(band_segments_points[n])
                    for k in range(n_bands)]), (n_spin, band_segments_points[n], n_bands))
            bkp_init = bkp_last
            sec_k_band_segment.energies = energies * ureg.eV
            sec_k_band_segment.occupations = occs

    def parse_dos(self):
        sec_scc = self.archive.run[-1].calculation[-1]

        try:
            energy_fermi = sec_scc.energy.fermi
        except Exception:
            self.logger.warning('Error setting the Fermi level: not found from hoppings. Setting it to 0 eV')
            energy_fermi = 0.0 * ureg.eV

        dos_files = get_files('*dos.dat', self.filepath, '*.wout')
        if not dos_files:
            return
        if len(dos_files) > 1:
            self.logger.warning('Multiple dos data files found.')
        # Parsing only first *dos.dat file
        self.dos_dat_parser.mainfile = dos_files[0]

        sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
        sec_dos.energy_fermi = energy_fermi
        sec_dos.energy_shift = energy_fermi

        data = np.transpose(self.dos_dat_parser.data)
        sec_dos.n_energies = len(data[0])
        sec_dos.energies = data[0] * ureg.eV

        sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
        sec_dos_values.value = data[1] / ureg.eV

    def parse_scc(self):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)

        # Refs for calculation
        sec_scc.method_ref = sec_run.method[-1]
        sec_scc.system_ref = sec_run.system[-1]

        # Wannier90 hoppings section
        self.parse_hoppings()

        # Wannier band structure
        self.parse_bandstructure()

        # Wannier DOS
        self.parse_dos()

    def init_parser(self):
        self.wout_parser.mainfile = self.filepath
        self.wout_parser.logger = self.logger
        self.hr_parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        self.wout_parser.mainfile = self.filepath
        sec_run = archive.m_create(Run)

        # Program section
        sec_run.program = Program(
            name='Wannier90', version=self.wout_parser.get('version', ''))
        # TODO TimeRun section

        self.parse_system()

        self.parse_method()

        # Parsing AtomsGroup and AtomParameters for System and Method from the input file .win
        self.parse_winput(self.archive)

        self.parse_scc()

        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
        workflow = SinglePoint()
        self.archive.workflow2 = workflow
