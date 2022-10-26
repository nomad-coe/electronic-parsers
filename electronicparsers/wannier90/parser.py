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
import re
import numpy as np

from nomad.units import ureg

from nomad.parsing.file_parser import TextParser, Quantity, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Dos, DosValues, BandStructure, BandEnergies, Energy, HoppingMatrix
)
from nomad.datamodel.metainfo.simulation.method import Method, KMesh, Projection
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from .metainfo.wannier90 import x_wannier90_hopping_parameters

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
                'k_points', r'\|[\s\d]*(-*\d.[^\|]+)', repeats=True)]

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
                'positions', rf'\|\s*([\-\d\.]+)\s*([\-\d\.]+)\s*([\-\d\.]+)', repeats=True)]

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
        self._quantities = [
            Quantity('energy_fermi', rf'{re_n}fermi_energy\s*=\s*([\d\.\-]+)', repeats=False)]


class HrParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity('degeneracy_factors', r'\s*written on[\s\w]*:\d*:\d*\s*([\d\s]+)'),
            Quantity('hoppings', rf'\s*([-\d\s.]+)', repeats=False)]


class Wannier90Parser:
    # TODO check if level defined w.r.t. DFT calculation (default, level = 0)
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

    def parse_system(self):
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)

        sec_atoms = sec_system.m_create(Atoms)
        if self.wout_parser.get('lattice_vectors') is not None:
            sec_atoms.lattice_vectors = np.vstack(self.wout_parser.get('lattice_vectors')) * ureg.angstrom
        if self.wout_parser.get('reciprocal_lattice_vectors') is not None:
            sec_atoms.lattice_vectors_reciprocal = np.vstack(self.wout_parser.get('reciprocal_lattice_vectors')) / ureg.angstrom

        pbc = [np.vstack(self.wout_parser.get('lattice_vectors')) is not None] * 3
        sec_atoms.periodic = pbc

        sec_atoms.labels = self.wout_parser.get('structure').get('labels')
        sec_atoms.positions = self.wout_parser.get('structure').get('positions') * ureg.angstrom

    def parse_method(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        sec_proj = sec_method.m_create(Projection)

        # k_mesh section
        sec_k_mesh = sec_proj.m_create(KMesh)
        sec_k_mesh.n_points = self.wout_parser.get('k_mesh', None).get('n_points')
        if self.wout_parser.get('k_mesh', None).get('k_points') is not None:
            sec_k_mesh.points = self.wout_parser.get('k_mesh', None).k_points[::2]

        # Wannier90 section
        for key in self._input_projection_mapping.keys():
            setattr(sec_proj, self._input_projection_mapping[key], self.wout_parser.get(key))
        if self.wout_parser.get('Niter') is not None:
            sec_proj.is_maximally_localized = self.wout_parser.get('Niter', 0) > 1
        sec_proj.energy_window_outer = self.wout_parser.get('energy_windows').outer
        sec_proj.energy_window_inner = self.wout_parser.get('energy_windows').inner

    def parse_hoppings(self):
        hr_files = [f for f in os.listdir(self.maindir) if f.endswith('hr.dat')]
        if not hr_files:
            return

        sec_scc = self.archive.run[-1].calculation[-1]

        self.hr_parser.mainfile = os.path.join(self.maindir, hr_files[0])
        sec_hopping_matrix = sec_scc.m_create(HoppingMatrix)

        # Assuming method.projection is parsed before
        sec_hopping_matrix.n_orbitals = self.archive.run[-1].method[-1].projection.n_projected_orbitals
        sec_hopping_matrix.n_wigner_seitz_points = self.hr_parser.get('degeneracy_factors')[1]
        sec_hopping_matrix.degeneracy_factors = self.hr_parser.get('degeneracy_factors')[2:]
        full_hoppings = np.array(self.hr_parser.get('hoppings'))
        sec_hopping_matrix.value = np.reshape(
            full_hoppings, (sec_hopping_matrix.n_wigner_seitz_points, sec_hopping_matrix.n_orbitals * sec_hopping_matrix.n_orbitals, 7))

        sec_scc_energy = sec_scc.m_create(Energy)
        # Setting Fermi level to the first orbital onsite energy
        n_wigner_seitz_points_half = int(0.5 * sec_hopping_matrix.n_wigner_seitz_points)
        energy_fermi = sec_hopping_matrix.value[n_wigner_seitz_points_half][0][5] * ureg.eV
        sec_scc_energy.fermi = energy_fermi
        sec_scc_energy.highest_occupied = energy_fermi

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
        kpoints[3].append(k_symm_points[-1])
        n_kpoints = sum(band_segments_points)

        return (n_kpoints, band_segments_points, kpoints)

    def parse_bandstructure(self):
        sec_scc = self.archive.run[-1].calculation[-1]

        if sec_scc.energy.fermi is None:
            return
        energy_fermi = sec_scc.energy.fermi
        energy_fermi_eV = energy_fermi.to('electron_volt').magnitude

        band_files = [f for f in os.listdir(self.maindir) if f.endswith('band.dat')]
        if not band_files:
            return
        if len(band_files) > 1:
            self.logger.warn('Multiple bandstructure data files found.')
        # Parsing only first *_band.dat file
        self.band_dat_parser.mainfile = os.path.join(self.maindir, band_files[0])

        sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
        sec_k_band.energy_fermi = energy_fermi

        if self.band_dat_parser.data is None:
            return
        data = np.transpose(self.band_dat_parser.data)

        (n_kpoints, band_segments_points, kpoints) = self.get_k_points()
        n_segments = len(band_segments_points)
        n_bands = round((len(data[0])) / n_kpoints)
        n_spin = 1

        j = 0
        for n in range(n_segments):
            sec_k_band_segment = sec_k_band.m_create(BandEnergies)
            sec_k_band_segment.n_kpoints = band_segments_points[n]
            sec_k_band_segment.kpoints = kpoints[n]

            energies = [[[
                data[1][i + s * b * n_kpoints] for b in range(n_bands)]
                for i in range(j, j + band_segments_points[n])]
                for s in range(n_spin)]
            occs = [[[
                2.0 if data[1][i + s * b * n_kpoints] < energy_fermi_eV else 0.0
                for b in range(n_bands)] for i in range(j, j + band_segments_points[n])]
                for s in range(n_spin)]
            j += band_segments_points[n]
            sec_k_band_segment.energies = energies * ureg.eV
            sec_k_band_segment.occupations = occs

    def parse_dos(self):
        sec_scc = self.archive.run[-1].calculation[-1]

        if sec_scc.energy.fermi is None:
            return
        energy_fermi = sec_scc.energy.fermi

        dos_files = [f for f in os.listdir(self.maindir) if f.endswith('dos.dat')]
        if not dos_files:
            return
        if len(dos_files) > 1:
            self.logger.warn('Multiple dos data files found.')
        # Parsing only first *_band.dat file
        self.dos_dat_parser.mainfile = os.path.join(self.maindir, dos_files[0])

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

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        sec_run = archive.m_create(Run)

        # TODO move mainfile as hdf5 to MatchingParserInterface list and
        # create init_parser() for the mainfile?
        wout_files = [f for f in os.listdir(self.maindir) if f.endswith('.wout')]
        if not wout_files:
            self.logger.error('Error finding the woutput file.')

        self.wout_parser.mainfile = os.path.join(self.maindir, wout_files[0])

        # Program section
        sec_run.program = Program(
            name='Wannier90', version=self.wout_parser.get('version', ''))
        # TODO TimeRun section

        self.parse_system()

        self.parse_method()

        self.parse_scc()
