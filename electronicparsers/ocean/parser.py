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
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.method import Method, BSE, KMesh
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Dos, DosValues, BandStructure, BandEnergies, Energy, EnergyEntry, Charges,
    Forces, ForcesEntry, ScfIteration, BandGap
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization, Task, GW as GWWorkflow
from nomad.datamodel.metainfo.workflow2 import TaskReference, Link
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2, GeometryOptimization as GeometryOptimization2,
    GeometryOptimizationMethod, GW as GW2, GWResults
)
from .metainfo.ocean import (
    x_ocean_bse_parameters, x_ocean_screen_parameters, x_ocean_core_haydock_parameters,
    x_ocean_core_gmres_parameters
)


class OceanParser:
    def __init__(self):
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

    def parse_method(self, data):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        # KMesh section
        sec_k_mesh = sec_method.m_create(KMesh)
        sec_k_mesh.grid = data['bse'].get('kmesh')

        # BSE section
        sec_bse = sec_method.m_create(BSE)
        sec_bse.type = self._type_bse_map[data['bse']['core'].get('solver')]
        sec_bse.mode = self.mode_bse[data['bse']['core'].get('strength')]
        sec_bse.n_empty_states = data['bse'].get('nbands')
        sec_bse.core_hole_broadening = data['bse']['core'].get('broaden')
        # screening parsing
        sec_bse.screening_type = data['screen'].get('mode')
        sec_bse.dielectric_infinity = data['structure'].get('epsilon')
        sec_bse.n_empty_states_screening = data['screen'].get('nbands')
        sec_bse.k_mesh_screening = KMesh(grid=data['screen'].get('kmesh'))

        # code-specific parameters
        # BSE
        sec_bse_ocean = sec_method.m_create(x_ocean_bse_parameters)
        sec_bse_ocean.x_ocean_screen_radius = data['bse']['core'].get('screen_radius')
        sec_bse_ocean.x_ocean_xmesh = data['bse'].get('xmesh')
        if sec_bse.type == 'lanczos-haydock':
            sec_haydock = sec_bse_ocean.m_create(x_ocean_core_haydock_parameters)
            sec_haydock.x_ocean_converge_spacing = data['bse']['core']['haydock']['converge'].get('spacing')
            sec_haydock.x_ocean_converge_thresh = data['bse']['core']['haydock']['converge'].get('thresh')
            sec_haydock.x_ocean_niter = data['bse']['core']['haydock'].get('niter')
        elif sec_bse.type == 'gmres':
            sec_gmres = sec_bse_ocean.m_create(x_ocean_core_gmres_parameters)
            gmres_keys = ['echamp', 'elist', 'erange', 'estyle', 'ffff', 'gprc', 'nloop']
            for key in gmres_keys:
                setattr(sec_gmres, f'x_ocean_{key}', data['bse']['core']['gmres'].get(key))
        # screening
        sec_bse_screen = sec_method.m_create(x_ocean_screen_parameters)
        screen_keys = [
            'all_augment', 'augment', 'convertstyle', 'dft_energy_range', 'inversionstyle',
            'kshift', 'mimic_exciting_bands', 'shells']
        screen_dicts = [
            'core_offset', 'final', 'grid']
        for key in screen_keys:
            setattr(sec_bse_screen, f'x_ocean_{key}', data['screen'].get(key))
        for keys in screen_dicts:
            for subkeys in data['screen'][keys].keys():
                setattr(sec_bse_screen, f'x_ocean_{keys}_{subkeys}', data['screen'][keys].get(subkeys))
        sec_bse_screen.x_ocean_model_flavor = data['screen']['model'].get('flavor')

    def parse_scc(self, data):
        pass

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

        sec_run = self.archive.m_create(Run)

        # Program
        sec_program = sec_run.m_create(Program)
        sec_program.name = 'OCEAN'
        sec_program.version = data['version'].get('.')
        sec_program.x_ocean_commit_hash = data['version'].get('hash')
        sec_program.x_ocean_original_dft_code = self._dft_code_map.get(data['dft'].get('program'))

        # System
        self.parse_system(data['structure'])

        # Method
        self.parse_method(data)

        # Calculation
        self.parse_scc(data)

        # Workflow
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
