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
from nomad.datamodel.metainfo.simulation.method import (
    Method, KMesh, Photon, CoreHole, Screening, BSE
)
from nomad.datamodel.metainfo.simulation.calculation import Calculation, Spectra
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint
from .metainfo.ocean import (
    x_ocean_bse_parameters, x_ocean_screen_parameters, x_ocean_core_haydock_parameters,
    x_ocean_core_gmres_parameters, x_ocean_lanczos_results
)
from ..utils import (
    BeyondDFTWorkflowsParser
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


class OceanParser(BeyondDFTWorkflowsParser):
    def __init__(self):
        self.photon_parser = PhotonParser()
        self.spectra_parser = DataTextParser()
        self.lanczos_parser = LanczosParser()
        self._child_archives = {}
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

    def parse_system(self, path, data):
        sec_run = self._child_archives.get(path).run[-1]
        sec_atoms = sec_run.m_create(System).m_create(Atoms)

        if data.get('avecs'):
            sec_atoms.lattice_vectors = data.get('avecs') * ureg.bohr
            sec_atoms.periodic = [data.get('avecs')[:] is not None] * 3
        if data.get('bvecs'):
            sec_atoms.lattice_vectors_reciprocal = np.array(data.get('bvecs')) / ureg.bohr

        if data.get('znucl') and data.get('typat'):
            sec_atoms.labels = [chemical_symbols[int(data.get('znucl')[n_at - 1])] for n_at in data.get('typat')]
        if data.get('xangst'):
            sec_atoms.positions = data.get('xangst') * ureg.bohr

    def parse_polarization(self, path):
        sec_run = self._child_archives.get(path).run[-1]
        sec_photon = sec_run.m_create(Method).m_create(Photon)

        # NOT IDEAL: photonN should be in the same folder: patch due for the upload mr5PRdbVQUm-d7awz3Q9Uw
        photon_file = [f for f in os.listdir(self.maindir) if f.startswith('photon') and f.endswith(path[-1:])]
        if len(photon_file) == 0:
            return
        self.photon_parser.mainfile = os.path.join(self.maindir, photon_file[0])
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

        # BSE
        sec_bse = sec_method.m_create(BSE)
        bse_data = self.data.get('bse', {})
        sec_bse.type = self._type_bse_map[bse_data.get('val', {}).get('solver')]
        sec_bse.n_states = bse_data.get('nbands', 1)
        sec_bse.broadening = bse_data.get('val', {}).get('broaden', 0.1) * ureg.eV
        # KMesh
        sec_k_mesh = sec_method.m_create(KMesh)
        sec_k_mesh.grid = bse_data.get('kmesh', [])
        # QMesh copied from KMesh
        sec_bse.m_add_sub_section(BSE.q_mesh, sec_k_mesh)
        # Screening
        screen_data = self.data.get('screen', {})
        sec_screening = Screening(
            type=screen_data.get('mode'),
            n_states=screen_data.get('nbands', 1),
            dielectric_infinity=self.data['structure'].get('epsilon'))
        sec_k_mesh_screening = KMesh(grid=screen_data.get('kmesh', []))
        sec_screening.m_add_sub_section(Screening.k_mesh, sec_k_mesh_screening)
        sec_screening.m_add_sub_section(Screening.q_mesh, sec_k_mesh_screening)
        sec_bse.m_add_sub_section(BSE.screening, sec_screening)

        # Core-Hole (either K=1s or L23=2p depenging on the first edge found)
        bse_core_data = bse_data.get('core')
        if bse_core_data:
            sec_core_hole = CoreHole(
                mode=self.mode_bse[bse_core_data.get('strength')],
                solver=self._type_bse_map[bse_core_data.get('solver')],
                broadening=bse_core_data.get('broaden', 0.1) * ureg.eV)
            sec_bse.m_add_sub_section(BSE.core_hole, sec_core_hole)
            # TODO wait for new changes in metainfo for CoreHole
            # sec_core.edge = self._core_level_map[str(edges[0][-2:])]

        # code-specific parameters
        # BSE
        sec_bse_ocean = sec_method.m_create(x_ocean_bse_parameters)
        sec_bse_ocean.x_ocean_screen_radius = bse_core_data.get('screen_radius')
        sec_bse_ocean.x_ocean_xmesh = bse_data.get('xmesh')
        # screening
        sec_bse_screen = sec_method.m_create(x_ocean_screen_parameters)
        screen_keys = [
            'all_augment', 'augment', 'convertstyle', 'dft_energy_range', 'inversionstyle',
            'kshift', 'mimic_exciting_bands', 'shells']
        screen_dicts = [
            'core_offset', 'final', 'grid']
        for key in screen_keys:
            setattr(sec_bse_screen, f'x_ocean_{key}', screen_data.get(key))
        for key in screen_dicts:
            for subkey in screen_data[key].keys():
                setattr(sec_bse_screen, f'x_ocean_{key}_{subkey}', screen_data[key].get(subkey))
        sec_bse_screen.x_ocean_model_flavor = screen_data['model'].get('flavor')
        # edges
        edges = []
        for ed in [x.split(' ') for x in self.data['calc'].get('edges', [])]:
            edges.append([int(x) for x in ed])
        sec_method.x_ocean_edges = edges
        # core
        if bse_core_data.get('solver') == 'haydock':
            sec_haydock = sec_bse_ocean.m_create(x_ocean_core_haydock_parameters)
            sec_haydock.x_ocean_converge_spacing = bse_core_data['haydock']['converge'].get('spacing')
            sec_haydock.x_ocean_converge_thresh = bse_core_data['haydock']['converge'].get('thresh')
            sec_haydock.x_ocean_niter = bse_core_data['haydock'].get('niter')
        elif bse_core_data.get('solver') == 'gmres':
            sec_gmres = sec_bse_ocean.m_create(x_ocean_core_gmres_parameters)
            gmres_keys = ['echamp', 'elist', 'erange', 'estyle', 'ffff', 'gprc', 'nloop']
            for key in gmres_keys:
                setattr(sec_gmres, f'x_ocean_{key}', bse_core_data['gmres'].get(key))

    def parse_scc(self, path):
        sec_run = self._child_archives.get(path).run[-1]
        sec_scc = sec_run.m_create(Calculation)
        sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]  # ref to BSE method section

        # absorption spectra (main calculation)
        self.spectra_parser.mainfile = os.path.join(self.maindir, path)
        data_spct = self.spectra_parser.data
        sec_spectra = sec_scc.m_create(Spectra)
        sec_spectra.type = self.data['calc'].get('mode').upper()
        sec_spectra.n_energies = len(data_spct)
        sec_spectra.excitation_energies = data_spct[:, 0] * ureg.eV
        sec_spectra.intensities = data_spct[:, 2]

        # lanczos matrices
        lanc_file = [f for f in os.listdir(self.maindir) if f.startswith('abslanc') and f.endswith(path[-2:])]
        if len(lanc_file) == 0:
            return
        self.lanczos_parser.mainfile = os.path.join(self.maindir, lanc_file[0])
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

    def parse_photons(self, path):
        # For each spectra, we parse the data in one entry
        sec_run = self._child_archives.get(path).m_create(Run)

        # Program
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'OCEAN'
        sec_program.version = self.data['version'].get('.')
        sec_program.x_ocean_commit_hash = self.data['version'].get('hash')
        sec_program.x_ocean_original_dft_code = self._dft_code_map.get(self.data['dft'].get('program'))

        # System
        if not self.data.get('structure'):
            self.logger.error('Error finding the structure in the main output file.')
            return
        self.parse_system(path, self.data.get('structure'))

        # Method
        self.parse_polarization(path)
        self.parse_method(self._child_archives.get(path))

        # Calculation
        self.parse_scc(path)

        # Workflow
        workflow = SinglePoint()
        self._child_archives.get(path).workflow2 = workflow

    def get_mainfile_keys(self, filepath):
        # We recognize the absspct files as the main auxiliary files
        absspct_files = [f for f in os.listdir(os.path.dirname(filepath)) if f.startswith('absspct')]
        absspct_files.sort()
        if len(absspct_files) > 0:
            keys = []
            for f in absspct_files:
                keys.append(f)
            return keys
        return True

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging
        child = ''

        try:
            data = json.load(open(self.filepath))
        except Exception:
            self.logger.error('Error opening json output file.')
            data = None
            return
        self.data = data

        for child in self._child_archives:
            if self._child_archives.get(child):
                self.parse_photons(child)

        sec_run = self.archive.m_create(Run)
        if self._child_archives.get(child):
            if self._child_archives.get(child).run[-1].program and self._child_archives.get(child).run[-1].system:
                sec_run.program = self._child_archives.get(child).run[-1].program
                sec_run.system = self._child_archives.get(child).run[-1].system
        else:
            self.logger.warning('Cannot resolve program and system from the first photon archive. '
                                'Generating empty sections.')
            sec_run.m_create(Program)
            sec_run.m_create(System)
        self.parse_method(self.archive)
        self.parse_photon_workflow()
