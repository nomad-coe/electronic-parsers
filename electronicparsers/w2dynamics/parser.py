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
import os
import logging
import h5py
import re

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.workflow import SinglePoint
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, GreensFunctions
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, HoppingMatrix, HubbardKanamoriModel, LatticeModelHamiltonian, FrequencyMesh,
    TimeMesh, DMFT
)
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.workflow import Workflow
from .metainfo.w2dynamics import (
    x_w2dynamics_axes, x_w2dynamics_quantities, x_w2dynamics_config_parameters,
    x_w2dynamics_config_atoms_parameters
)
from ..wannier90.parser import WOutParser, HrParser
from ..utils import get_files
from nomad.parsing.parser import to_hdf5


re_n = r'[\n\r]'


class LogParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'program_version', r'Version\s*([0-9.]+)',
                dtype=str, flatten=False
            )
        ]


class W2DynamicsParser:
    level = 2

    def __init__(self):
        self._re_namesafe = re.compile(r'[^\w]')
        self.log_parser = LogParser()
        self._calculation_type = 'dmft'
        self.wout_parser = WOutParser()
        self.hr_parser = HrParser()

        self._hubbard_kanamori_map = {
            'u': 'u',
            'j': 'jh',
            'v': 'up'
        }

        self._dmft_qmc_map = {
            'ntau': 'n_tau',
            'niw': 'n_matsubara_freq'
        }

        self._dataset_run_mapping = {
            '.axes': x_w2dynamics_axes,
            '.quantities': x_w2dynamics_quantities
        }

        self._inequivalent_atom_map = {
            'self_energy_iw': 'siw',
            'greens_function_iw': 'giw',
            'greens_function_tau': 'gtau'
        }

    def parse_program_version(self):
        """Parses the program version from the .log file if present.

        Returns:
            str: program version label
        """
        log_files = get_files('*.log', self.filepath, self.mainfile)
        if log_files:
            if len(log_files) > 1:
                self.logger.warning('Multiple logging files found.')

            self.log_parser.mainfile = log_files[0]
            return self.log_parser.get('program_version', None)

    def parse_axes(self, source, target):
        """Parses the key `.axes` from the hdf5 mainfile

        Args:
            source (HDF5group): group `.axes` from the hdf5 mainfile
            target (MSection): EntryArchive.Run[-1].x_w2dynamics_axes code-specific section
        """
        for key in source.keys():
            if key in ['iw', 'tau']:
                continue
            # resolve value from 'value'
            value = source[key]
            if isinstance(value, h5py.Group) and 'value' in value.keys():
                value = value['value']
            if not isinstance(value, h5py.Dataset):
                continue
            name = self._re_namesafe.sub('_', key)
            if value.shape:
                setattr(target, f'x_w2dynamics_{name}', value[:])

    def parse_system(self):
        """Parses System from the Wannier90 output file (*.wout) if present in the upload.
        Otherwise, a warning appears.
        """
        sec_run = self.archive.run[-1]

        wann90_files = get_files('*.wout', self.filepath, self.mainfile)
        if wann90_files:  # parse crystal from Wannier90
            if len(wann90_files) > 1:
                self.logger.warning('Multiple logging files found.')

            self.wout_parser.mainfile = wann90_files[-1]
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
        else:  # TODO parse specific lattice model: discuss it Jonas Schwab
            self.logger.warning('Wannier90 output files not found in the same folder.')

    def parse_input_model(self, data):
        """Parses input model into Run.Method.LatticeModelHamiltonian in two differentiated
        subsections:
            1- Hopping matrices from the Wannier90 *hr.dat file
            2- HubbardKanamoriHamiltonian from the hdf5 mainfile

        Args:
            data (HDF5group): group `.config` from the hdf5 mainfile
        """
        sec_run = self.archive.run[0]
        sec_hamiltonian = sec_run.m_create(Method).m_create(LatticeModelHamiltonian)

        # HoppingMatrix
        hr_files = get_files('*hr.dat', self.filepath, self.mainfile)
        if hr_files:  # parse crystal from Wannier90
            self.hr_parser.mainfile = hr_files[-1]
            sec_hopping_matrix = sec_hamiltonian.m_create(HoppingMatrix)
            sec_hopping_matrix.n_orbitals = self.wout_parser.get('Nwannier')
            sec_hopping_matrix.n_wigner_seitz_points = self.hr_parser.get('degeneracy_factors')[1]
            sec_hopping_matrix.degeneracy_factors = self.hr_parser.get('degeneracy_factors')[2:]
            full_hoppings = np.array(self.hr_parser.get('hoppings'))
            sec_hopping_matrix.value = np.reshape(
                full_hoppings, (sec_hopping_matrix.n_wigner_seitz_points, sec_hopping_matrix.n_orbitals * sec_hopping_matrix.n_orbitals, 7))
        else:  # TODO parse specific lattice model
            pass

        # HubbardKanamoriModel
        # TODO add parse of slater integrals
        # TODO add parse of the u_matrix.dat file
        for n in range(data.attrs.get('general.nat', 1)):
            sec_hubbard_kanamori_model = sec_hamiltonian.m_create(HubbardKanamoriModel)

            angular_momentum = 'd'
            sec_hubbard_kanamori_model.orbital = angular_momentum
            sec_hubbard_kanamori_model.double_counting_correction = data.attrs.get('general.dc', None)
            # w2dynamics keeps spin-rotational invariance
            for key in self._hubbard_kanamori_map.keys():
                parameters = data.attrs.get(f'atoms.{n+1}.{key}{angular_momentum}{angular_momentum}', None) * ureg.eV
                setattr(sec_hubbard_kanamori_model, self._hubbard_kanamori_map.get(key), parameters)

            if data.attrs.get(f'atoms.{n+1}.hamiltonian') == 'Density':
                sec_hubbard_kanamori_model.j = 0.0
            elif data.attrs.get(f'atoms.{n+1}.hamiltonian') == 'Kanamori':
                sec_hubbard_kanamori_model.j = sec_hubbard_kanamori_model.jh

            sec_hubbard_kanamori_model.double_counting_correction = data.attrs.get('general.dc')

    def parse_method(self, data):
        """Parses DMFT and code-specific metadata from `.config` in the hdf5 mainfile

        Args:
            data (HDF5group): group `.config` from the hdf5 mainfile
        """
        sec_run = self.archive.run[0]

        sec_method = sec_run.m_create(Method)
        # ref to the Non- and InteractionHamiltonian
        sec_method.starting_method_ref = sec_run.method[0]

        def parse_config(keys):
            key = keys.split('.')[-1]
            if isinstance(data.attrs.get(keys), str):
                value = data.attrs.get(keys)
            else:
                value = data.attrs.get(keys).tolist()
            return key, value

        # Parse Method.x_w2dynamics_config general and qmc quantities
        sec_config = sec_method.m_create(x_w2dynamics_config_parameters)
        config_general = {}
        config_qmc = {}
        for keys in data.attrs.keys():
            if keys.startswith('general'):
                key, value = parse_config(keys)
                config_general[key] = value
            elif keys.startswith('qmc'):
                key, value = parse_config(keys)
                config_qmc[key] = value
        sec_config.x_w2dynamics_config_general = config_general
        sec_config.x_w2dynamics_config_qmc = config_qmc
        # Parse Method.x_w2dynamics_config atoms quantities
        for i in range(data.attrs.get(f'general.nat', 0)):
            sec_config_subsection = sec_config.m_create(x_w2dynamics_config_atoms_parameters)
            for key in data.attrs.keys():
                if key.startswith(f'atoms.{i+1}'):
                    keys_mod = (key.replace('-', '_')).split('.')
                    parameters = data.attrs.get(key)
                    setattr(sec_config_subsection, f'x_w2dynamics_{keys_mod[-1]}', parameters)

        # DMFT section
        sec_dmft = sec_method.m_create(DMFT)
        sec_dmft.n_atoms_per_unit_cell = data.attrs.get(f'general.nat', 0)
        if data.attrs.get(f'general.beta'):
            sec_dmft.inverse_temperature = data.attrs.get(f'general.beta') / ureg.eV
        if data.attrs.get(f'general.magnetism'):
            sec_dmft.magnetic_state = data.attrs.get(f'general.magnetism') + 'magnetic'
        corr_orbs_per_atoms = []
        occ_per_atoms = []
        for i in range(sec_dmft.n_atoms_per_unit_cell):
            nd = sec_method.x_w2dynamics_config.x_w2dynamics_config_atoms[i].x_w2dynamics_nd
            np = sec_method.x_w2dynamics_config.x_w2dynamics_config_atoms[i].x_w2dynamics_np
            corr_orbs_per_atoms.append(nd + np)
            if data.attrs.get(f'general.totdens'):
                occ_per_atoms.append(data.attrs.get(f'general.totdens'))
        sec_dmft.n_correlated_orbitals = corr_orbs_per_atoms
        sec_dmft.n_correlated_electrons = occ_per_atoms
        sec_dmft.impurity_solver = 'CT-HYB'
        # FrequencyMesh
        iw = self.data.get('.axes').get('iw')
        if iw is not None:
            iw = iw[:] * 1j * ureg.eV
            sec_freq_mesh = FrequencyMesh(dimensionality=1, n_points=len(iw), points=iw)
            sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
        # TimeMesh
        tau = self.data.get('.axes').get('tau')
        if tau is not None:
            tau = tau[:] * 1j
            sec_tau_mesh = TimeMesh(dimensionality=1, n_points=len(tau), points=tau)
            sec_method.m_add_sub_section(Method.time_mesh, sec_tau_mesh)

    def parse_scc(self):
        """Parses the output calculation from dmft-xxx or stat-xxx. Every iteration step quantity
        is saved as a path to the hdf5 file to spare the size of the archive.

        The last step is used to store the converged quantities.
        """
        sec_run = self.archive.run[0]
        sec_scc = sec_run.m_create(Calculation)
        if sec_run.m_xpath('system'):
            sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]  # ref DMFT

        # order calculations
        calc_keys = [key for key in self.data.keys() if key.startswith('dmft-') or key.startswith('stat-')]
        calc_keys.sort()

        # calculating how many inequivalent atoms are per unit cell
        n_ineq = 0
        for keys in self.data[calc_keys[0]]:
            if keys.startswith('ineq'):
                n_ineq += 1
        n_atoms = sec_run.method[-1].dmft.n_atoms_per_unit_cell

        for key in calc_keys:
            if key not in self.data.keys():
                continue
            sec_scf_iteration = sec_scc.m_create(ScfIteration)
            filename = os.path.join(os.path.dirname(self.filepath.split("/raw/")[-1]), self.mainfile)
            farg = 'r+b' if os.path.isfile(os.path.join(os.path.dirname(self.filepath), filename)) else 'wb'
            if self.archive.m_context:
                with self.archive.m_context.raw_file(filename, farg) as f:
                    for subkey in self.data.get(key).keys():
                        parameter = self.data.get(key).get(subkey)
                        if subkey == 'mu':
                            value = parameter.get('value')
                            sec_energy = sec_scf_iteration.m_create(Energy)
                            sec_energy.fermi = np.float64(value) * ureg.eV
                        elif subkey != 'ineq-001':
                            value = parameter.get('value')[:]
                            value = to_hdf5(value, f, f'{key}/{subkey}/value')
                            name = self._re_namesafe.sub('_', subkey)
                            setattr(sec_scf_iteration, f'x_w2dynamics_{name}', value)
                        else:
                            sec_ineq = sec_scf_iteration.m_create(x_w2dynamics_quantities)
                            for name in parameter.keys():
                                # resolve value from 'value'
                                value = parameter.get(name)
                                if isinstance(value, h5py.Group) and 'value' in value.keys():
                                    value = value.get('value')
                                if not isinstance(value, h5py.Dataset):
                                    continue
                                value = to_hdf5(value, f, f'{key}/{subkey}/{name}/value')
                                name = self._re_namesafe.sub('_', name)
                                setattr(sec_ineq, f'x_w2dynamics_{name}', value)

            # Storing converged quantities from dmft-last or stat-last
            if key.endswith('last'):
                sec_gf = sec_scc.m_create(GreensFunctions)
                if sec_run.method[-1].m_xpath('frequency_mesh'):
                    sec_gf.matsubara_freq = sec_run.method[-1].frequency_mesh.points.to('eV').magnitude.imag
                if sec_run.method[-1].m_xpath('time_mesh'):
                    sec_gf.tau = sec_run.method[-1].time_mesh.points.imag
                if self.data.get(key).get('mu') is not None:
                    sec_gf.chemical_potential = self.data.get(key).get('mu').get('value')
                norb = self.data.get('.config').attrs.get('atoms.1.nd')
                for subkey in self._inequivalent_atom_map.keys():
                    parameters = []
                    if n_ineq == n_atoms:
                        for i in range(n_ineq):
                            value = self.data.get(key).get(f'ineq-00{i + 1}').get(self._inequivalent_atom_map.get(subkey, [])).get('value')[:]
                            parameters.append(value)
                    elif n_atoms % n_ineq == 0 and n_ineq > 1:
                        for i in range(n_atoms):
                            value = self.data.get(key).get(f'ineq-00{(i % n_ineq) + 1}').get(self._inequivalent_atom_map.get(subkey, [])).get('value')[:]
                            parameters.append(value)
                    elif n_ineq == 1:
                        for i in range(n_atoms):
                            value = self.data.get(key).get('ineq-001').get(self._inequivalent_atom_map.get(subkey, [])).get('value')[:]
                            parameters.append(value)
                    else:
                        self.logger.warning('Number of inequivalent atoms and number of atoms per unit cell '
                                            'is neither equal nor multiples. Please, revise the output.')
                        break

                    parameters = np.array(parameters)
                    # reordering calculation matrices to standarize w2dynamics and solid_dmft
                    # (and potentially, other DMFT codes)
                    parameters_reorder = np.array([[[
                        parameters[i, no, ns, :] for no in range(norb)] for ns in range(2)] for i in range(n_atoms)])
                    setattr(sec_gf, subkey, parameters_reorder)
                # summing over atoms per unit cell to keep same array dimensions
                parameters = []
                if n_ineq == n_atoms:
                    for i in range(n_ineq):
                        value = self.data.get(key).get(f'ineq-00{i + 1}').get('occ').get('value')[:]
                        parameters.append([[
                            value[no, ns, no, ns]
                            for no in range(norb)] for ns in range(2)])
                elif n_atoms % n_ineq == 0 and n_ineq > 1:
                    for i in range(n_atoms):
                        value = self.data.get(key).get(f'ineq-00{(i % n_ineq) + 1}').get('occ').get('value')[:]
                        parameters.append([[
                            value[no, ns, no, ns]
                            for no in range(norb)] for ns in range(2)])
                elif n_ineq == 1:
                    for i in range(n_atoms):
                        value = self.data.get(key).get(f'ineq-001').get('occ').get('value')[:]
                        parameters.append([[
                            value[no, ns, no, ns]
                            for no in range(norb)] for ns in range(2)])
                sec_gf.orbital_occupations = np.array(parameters)

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.mainfile = os.path.basename(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        try:
            data = h5py.File(self.filepath)
            self.data = data
        except Exception:
            self.logger.error('Error opening hdf5 file.')
            data = None
            return

        sec_run = archive.m_create(Run)

        # Program section
        sec_run.program = Program(
            name='w2dynamics', version=self.parse_program_version())

        # run.x_w2dynamics_axes section
        sec_axes = sec_run.m_create(x_w2dynamics_axes)
        self.parse_axes(self.data.get('.axes'), sec_axes)

        # System section
        self.parse_system()

        # Method.DMFT section with inputs (HoppingMatrix + InteractionModel)
        self.parse_input_model(self.data.get('.config'))
        self.parse_method(self.data.get('.config'))

        # Calculation section
        self.parse_scc()

        # Workflow section
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
        workflow = SinglePoint()
        self.archive.workflow2 = workflow
