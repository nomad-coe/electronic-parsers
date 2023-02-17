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
from nomad.datamodel.metainfo.simulation.method import Method, Photon, BSE, KMesh
from nomad.datamodel.metainfo.simulation.calculation import Calculation, Spectra
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint as SinglePoint2
from .metainfo.ocean import (
    x_ocean_bse_parameters, x_ocean_screen_parameters, x_ocean_core_haydock_parameters,
    x_ocean_core_gmres_parameters, x_ocean_lanczos_results
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
        self._child_archives = {}
        self._calculation_type = 'bse'
        self._photon_workflow_level = 0
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

    def parse_system(self, archive, data):
        sec_run = archive.run[-1]
        sec_atoms = sec_run.m_create(System).m_create(Atoms)

        if data.get('avecs'):
            sec_atoms.lattice_vectors = data.get('avecs') * ureg.bohr
            sec_atoms.periodic = [data.get('avecs')[:] is not None] * 3
            sec_atoms.lattice_vectors_reciprocal = np.array(data.get('bvecs')) / ureg.bohr

        if data.get('znucl') and data.get('typat'):
            sec_atoms.labels = [chemical_symbols[int(data.get('znucl')[n_at - 1])] for n_at in data.get('typat')]
            sec_atoms.positions = data.get('xangst') * ureg.bohr

    def parse_photon_polarization(self, archive, files, index):
        sec_run = archive.run[-1]
        sec_photon = sec_run.m_create(Method).m_create(Photon)

        # NOT IDEAL: photonN should be in the same folder: patch due for the upload mr5PRdbVQUm-d7awz3Q9Uw
        if len(files[1]) == 0:
            return
        self.photon_parser.mainfile = os.path.join(self.maindir, files[1][index])
        sec_photon.multipole_type = self.photon_parser.get('operator')
        sec_photon.polarization = self.photon_parser.get('vectors')[0]
        if sec_photon.multipole_type in ['quad', 'NRIXS', 'qRaman']:
            sec_photon.momentum_transfer = self.photon_parser.get('vectors')[1]
        sec_photon.energy = self.photon_parser.get('photon_energy') * ureg.electron_volt

    def parse_method(self, archive):
        sec_run = archive.run[-1]
        sec_method = sec_run.m_create(Method)
        if sec_run.m_xpath('method[0].photon'):
            sec_method.starting_method_ref = sec_run.method[0]
        else:
            self.logger.warning('photonN file not found, please check if the files are all '
                                'in the same folder.')

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

    def parse_scc(self, archive, files, index):
        sec_run = archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)
        sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]  # ref to BSE method section

        # absorption spectra (main calculation)
        if len(files[0]) == 0:
            return
        self.spectra_parser.mainfile = os.path.join(self.maindir, files[0][index])
        data_spct = self.spectra_parser.data
        sec_spectra = sec_scc.m_create(Spectra)
        sec_spectra.type = self.data['calc'].get('mode').upper()
        sec_spectra.n_energies = len(data_spct)
        sec_spectra.excitation_energies = data_spct[:, 0] * ureg.eV
        sec_spectra.intensities = data_spct[:, 2]

        # lanczos matrices
        if len(files[2]) == 0:
            return
        self.lanczos_parser.mainfile = os.path.join(self.maindir, files[2][index])
        data_lancz = self.lanczos_parser.get('data')
        sec_lanczos = sec_scc.m_create(x_ocean_lanczos_results)
        n_dimension = int(data_lancz[0][0]) + 1
        sec_lanczos.x_ocean_n_tridiagonal_matrix = n_dimension
        sec_lanczos.x_ocean_scaling_factor = data_lancz[0][1]
        matrix = [[data_lancz[1], 0.0]]
        for n in range(2, n_dimension + 1):
            matrix.append([data_lancz[n][0], data_lancz[n][1]])
        sec_lanczos.x_ocean_tridiagonal_matrix = matrix
        sec_lanczos.x_ocean_eigenvalues = data_lancz[n_dimension + 1:]

    def parse_spectra_entries(self, archive, files, index):
        # For each spectra, we parse the data in one entry
        try:
            data = json.load(open(self.filepath))
        except Exception:
            self.logger.error('Error opening json output file.')
            data = None
            return
        self.data = data

        sec_run = archive.m_create(Run)

        # Program
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'OCEAN'
        sec_program.version = data['version'].get('.')
        sec_program.x_ocean_commit_hash = data['version'].get('hash')
        sec_program.x_ocean_original_dft_code = self._dft_code_map.get(data['dft'].get('program'))

        # System
        self.parse_system(archive, self.data['structure'])

        # Method
        self.parse_photon_polarization(archive, files, index)
        self.parse_method(archive)

        # Calculation
        self.parse_scc(archive, files, index)

        # Workflow
        sec_workflow = archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
        workflow = SinglePoint2()
        archive.workflow2 = workflow

    def get_mainfile_keys(self, filepath):
        absspct_files = [f for f in os.listdir(os.path.dirname(filepath)) if f.startswith('absspct')]
        absspct_files.sort()
        if len(absspct_files) > 1:
            keys = []
            for f in absspct_files:
                keys.append(f'BSE{f[-2:]}')
            keys.remove('BSE01')  # removing BSE01 as this will be save in the initial call of parse()
            return keys
        return True

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        def finding_files(names):
            if not isinstance(names, list):
                self.logger.warning('Please, define your attribute names as a list.')
                return
            aux_files = []
            for n in names:
                files = [f for f in os.listdir(self.maindir) if f.startswith(n)]
                files.sort()
                aux_files.append(files)
            return aux_files

        files = finding_files(['absspct', 'photon', 'abslanc'])
        if files:
            for index in range(len(files[0])):
                if index == 0:
                    self.parse_spectra_entries(archive, files, index)
                else:
                    bse_archive = self._child_archives.get(f'BSE0{index + 1}')
                    self.parse_spectra_entries(bse_archive, files, index)
