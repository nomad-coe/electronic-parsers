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
import numpy as np
import json
import os
import logging
from ase.data import chemical_symbols

from nomad.units import ureg
from nomad.parsing.file_parser import DataTextParser, TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.method import Method, BSE, KMesh
from nomad.datamodel.metainfo.simulation.calculation import Calculation, Spectra
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization, Task, GW as GWWorkflow
from nomad.datamodel.metainfo.workflow2 import TaskReference, Link
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2, GeometryOptimization as GeometryOptimization2,
    GeometryOptimizationMethod, GW as GW2, GWResults
)
from .metainfo.ocean import (
    x_ocean_bse_parameters, x_ocean_screen_parameters, x_ocean_core_haydock_parameters,
    x_ocean_core_gmres_parameters, x_ocean_photon_parameters, x_ocean_lanczos_results
)


class PhotonParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity('operator', r'^(dipole|quad|NRIXS)', repeats=False),
            Quantity('vectors', r'cartesian([\s\d\.]+)', repeats=True),
            Quantity('photon_energy', r'end[\n\r]([\d\.]+)', repeats=False)]


class LanczosParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity('data', r'(.*[\s\S]+?)(?:.)', repeats=True)]


class OceanParser:
    def __init__(self):
        self.photon_parser = PhotonParser()
        self.spectra_parser = DataTextParser()
        self.lanczos_parser = LanczosParser()
        self._calculation_type = 'bse'
        self._dft_code_map = {
            'qe': 'QuantumESPRESSO',
            'abi': 'ABINIT'
        }
        self._type_bse_map = {
            'haydock': 'lanczos-haydock',
            'gmres': 'gmres'
        }
        self.mode_bse = ['emission', 'absorption']
        self._core_level_map = {
            '[1, 0]': 'K',
            '[2, 1]': 'L23'
        }

    def parse_system(self, data):
        sec_run = self.archive.run[-1]
        sec_atoms = sec_run.m_create(System).m_create(Atoms)

        if data.get('avecs'):
            sec_atoms.lattice_vectors = data.get('avecs')
            sec_atoms.periodic = [data.get('avecs')[:] is not None] * 3
            sec_atoms.lattice_vectors_reciprocal = data.get('bvecs')

        if data.get('znucl') and data.get('typat'):
            sec_atoms.labels = [chemical_symbols[int(data.get('znucl')[n_at - 1])] for n_at in data.get('typat')]
            sec_atoms.positions = data.get('xangst') * ureg.angstrom

    def parse_method(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        # KMesh section
        sec_k_mesh = sec_method.m_create(KMesh)
        sec_k_mesh.grid = self.data['bse'].get('kmesh')

        # BSE section
        sec_bse = sec_method.m_create(BSE)
        sec_bse.type = self._type_bse_map[self.data['bse']['core'].get('solver')]
        sec_bse.mode = self.mode_bse[self.data['bse']['core'].get('strength')]
        sec_bse.n_empty_states = self.data['bse'].get('nbands')
        sec_bse.core_hole_broadening = self.data['bse']['core'].get('broaden')
        # screening parsing
        sec_bse.screening_type = self.data['screen'].get('mode')
        sec_bse.dielectric_infinity = self.data['structure'].get('epsilon')
        sec_bse.n_empty_states_screening = self.data['screen'].get('nbands')
        sec_bse.k_mesh_screening = KMesh(grid=self.data['screen'].get('kmesh'))

        # code-specific parameters
        # BSE
        sec_bse_ocean = sec_method.m_create(x_ocean_bse_parameters)
        sec_bse_ocean.x_ocean_screen_radius = self.data['bse']['core'].get('screen_radius')
        sec_bse_ocean.x_ocean_xmesh = self.data['bse'].get('xmesh')
        if sec_bse.type == 'lanczos-haydock':
            sec_haydock = sec_bse_ocean.m_create(x_ocean_core_haydock_parameters)
            sec_haydock.x_ocean_converge_spacing = self.data['bse']['core']['haydock']['converge'].get('spacing')
            sec_haydock.x_ocean_converge_thresh = self.data['bse']['core']['haydock']['converge'].get('thresh')
            sec_haydock.x_ocean_niter = self.data['bse']['core']['haydock'].get('niter')
        elif sec_bse.type == 'gmres':
            sec_gmres = sec_bse_ocean.m_create(x_ocean_core_gmres_parameters)
            gmres_keys = ['echamp', 'elist', 'erange', 'estyle', 'ffff', 'gprc', 'nloop']
            for key in gmres_keys:
                setattr(sec_gmres, f'x_ocean_{key}', self.data['bse']['core']['gmres'].get(key))
        # screening
        sec_bse_screen = sec_method.m_create(x_ocean_screen_parameters)
        screen_keys = [
            'all_augment', 'augment', 'convertstyle', 'dft_energy_range', 'inversionstyle',
            'kshift', 'mimic_exciting_bands', 'shells']
        screen_dicts = [
            'core_offset', 'final', 'grid']
        for key in screen_keys:
            setattr(sec_bse_screen, f'x_ocean_{key}', self.data['screen'].get(key))
        for keys in screen_dicts:
            for subkeys in self.data['screen'][keys].keys():
                setattr(sec_bse_screen, f'x_ocean_{keys}_{subkeys}', self.data['screen'][keys].get(subkeys))
        sec_bse_screen.x_ocean_model_flavor = self.data['screen']['model'].get('flavor')
        # edges
        edges = []
        for ed in [x.split(' ') for x in self.data['calc'].get('edges')]:
            edges.append([int(x) for x in ed])
        sec_method.x_ocean_edges = edges
        # setting the core level (either K=1s or L23=2p depenging on the first edge found)
        sec_bse.core_level = self._core_level_map[str(edges[0][-2:])]
        # photons
        photon_files = [f for f in os.listdir(self.maindir) if f.startswith('photon')]
        photon_files.sort()  # making sure 1, 2, 3... are correctly ordered
        if photon_files:
            for f in photon_files:
                self.photon_parser.mainfile = os.path.join(self.maindir, f)
                sec_photon = sec_method.m_create(x_ocean_photon_parameters)
                for keys in ['operator', 'photon_energy']:
                    setattr(sec_photon, f'x_ocean_{keys}', self.photon_parser.get(keys))
                sec_photon.x_ocean_polarization_direction = self.photon_parser.get('vectors')[0]
                sec_photon.x_ocean_momentum_transfer = self.photon_parser.get('vectors')[1]

    def parse_scc(self):
        sec_run = self.archive.run[-1]

        def initiate_section_calculation(sec_run, i):
            if sec_run.m_xpath(f'calculation{[i]}'):
                return sec_run.calculation[i]
            else:
                return sec_run.m_create(Calculation)

        # absorption files
        absspct_files = [f for f in os.listdir(self.maindir) if f.startswith('absspct')]
        absspct_files.sort()
        if absspct_files:  # parse absorption spectra
            ifile = 0
            for f in absspct_files:
                self.spectra_parser.mainfile = os.path.join(self.maindir, f)
                data_spct = self.spectra_parser.data

                # Check whether section calculation is present already from previous files
                sec_scc = initiate_section_calculation(sec_run, ifile)

                sec_spectra = sec_scc.m_create(Spectra)
                sec_spectra.type = self.data['calc'].get('mode').upper()
                sec_spectra.n_energies = len(data_spct)
                sec_spectra.excitation_energies = data_spct[:, 0]
                sec_spectra.intensities = data_spct[:, 2]

                ifile += 1

        # lanczos matrices
        abslanc_files = [f for f in os.listdir(self.maindir) if f.startswith('abslanc')]
        abslanc_files.sort()
        if abslanc_files:  # parse absorption spectra
            ifile = 0
            for f in abslanc_files:
                self.lanczos_parser.mainfile = os.path.join(self.maindir, f)
                data_lancz = self.lanczos_parser.get('data')

                # Check whether section calculation is present already from previous files
                sec_scc = initiate_section_calculation(sec_run, ifile)

                sec_lanczos = sec_scc.m_create(x_ocean_lanczos_results)
                n_dimension = int(data_lancz[0][0]) + 1
                sec_lanczos.x_ocean_n_tridiagonal_matrix = n_dimension
                sec_lanczos.x_ocean_scaling_factor = data_lancz[0][1]
                matrix = [[data_lancz[1], 0.0]]
                for n in range(2, n_dimension + 1):
                    matrix.append([data_lancz[n][0], data_lancz[n][1]])
                sec_lanczos.x_ocean_tridiagonal_matrix = matrix
                sec_lanczos.x_ocean_eigenvalues = data_lancz[n_dimension + 1:]
                ifile += 1

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.maindir = os.path.dirname(self.filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging

        try:
            data = json.load(open(self.filepath))
        except Exception:
            self.logger.error('Error opening json output file.')
            data = None
            return
        self.data = data

        sec_run = self.archive.m_create(Run)

        # Program
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'OCEAN'
        sec_program.version = data['version'].get('.')
        sec_program.x_ocean_commit_hash = data['version'].get('hash')
        sec_program.x_ocean_original_dft_code = self._dft_code_map.get(data['dft'].get('program'))

        # System
        self.parse_system(self.data['structure'])

        # Method
        self.parse_method()

        # Calculation
        self.parse_scc()

        # Workflow
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
