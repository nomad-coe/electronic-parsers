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
    Method, HoppingMatrix, HubbardKanamoriModel, LatticeModelHamiltonian, DMFT
)
from nomad.datamodel.metainfo.workflow import Workflow
from .metainfo.w2dynamics import (
    x_w2dynamics_axes, x_w2dynamics_quantities, x_w2dynamics_config_parameters,
    x_w2dynamics_config_atoms_parameters, x_w2dynamics_config_general_parameters,
    x_w2dynamics_config_qmc_parameters
)
from ..wannier90.parser import Wannier90Parser, WOutParser, HrParser


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
            'self_energy_iw': 'x_w2dynamics_siw',
            'greens_function_iw': 'x_w2dynamics_giw',
            'greens_function_tau': 'x_w2dynamics_gtau'
        }

    def parse_program_version(self):
        # read program version from .log file if present
        log_files = [f for f in os.listdir(self.maindir) if f.endswith('.log')]
        if log_files:
            if len(log_files) > 1:
                self.logger.warning('Multiple logging files found.')

            self.log_parser.mainfile = os.path.join(self.maindir, log_files[0])

            return self.log_parser.get('program_version', None)

    def parse_dataset(self, source, target, include=[]):
        for key in source.keys():
            if include and key not in include:
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
            # mu is a single value
            if key == 'mu':
                target.x_w2dynamics_mu = value

    def parse_system(self):
        wann90_files = [f for f in os.listdir(self.maindir) if f.endswith('.wout')]
        if wann90_files:  # parse crystal from Wannier90
            if len(wann90_files) > 1:
                self.logger.warning('Multiple logging files found.')

            self.wout_parser.mainfile = os.path.join(self.maindir, wann90_files[-1])
            p = Wannier90Parser()
            p.parse_system(self.archive, self.wout_parser)
        else:  # TODO parse specific lattice model: discuss it Jonas Schwab
            self.logger.warning('Wannier90 output files not found in the same folder.')

    def parse_input_model(self, data):
        sec_run = self.archive.run[0]
        sec_hamiltonian = sec_run.m_create(Method).m_create(LatticeModelHamiltonian)

        # HoppingMatrix
        hr_files = [f for f in os.listdir(self.maindir) if f.endswith('hr.dat')]
        if hr_files:  # parse crystal from Wannier90
            self.hr_parser.mainfile = os.path.join(self.maindir, hr_files[-1])
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
        sec_run = self.archive.run[0]

        sec_method = sec_run.m_create(Method)
        # ref to the Non- and InteractionHamiltonian
        sec_method.starting_method_ref = sec_run.method[0]

        # Parse Method.x_w2dynamics_config general and qmc quantities
        sec_config = sec_method.m_create(x_w2dynamics_config_parameters)
        config_sections = [x_w2dynamics_config_general_parameters, x_w2dynamics_config_qmc_parameters]
        for subsection in config_sections:
            sec_config_subsection = sec_config.m_create(subsection)
            for key in data.attrs.keys():
                if not key.startswith(f'atoms'):
                    parameters = data.attrs.get(key)
                    keys_mod = (key.replace('-', '_')).split('.')
                    setattr(sec_config_subsection, f'x_w2dynamics_{keys_mod[-1]}', parameters)
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
        sec_dmft.inverse_temperature = data.attrs.get(f'general.beta') / ureg.eV
        sec_dmft.magnetic_state = data.attrs.get(f'general.magnetism') + 'magnetic'
        for key in self._dmft_qmc_map.keys():
            parameters = data.attrs.get(f'qmc.{key}')
            setattr(sec_dmft, self._dmft_qmc_map.get(key), parameters)
        corr_orbs_per_atoms = []
        occ_per_atoms = []
        for i in range(sec_dmft.n_atoms_per_unit_cell):
            nd = sec_method.x_w2dynamics_config.x_w2dynamics_config_atoms[i].x_w2dynamics_nd
            np = sec_method.x_w2dynamics_config.x_w2dynamics_config_atoms[i].x_w2dynamics_np
            corr_orbs_per_atoms.append(nd + np)
            occ_per_atoms.append(sec_method.x_w2dynamics_config.x_w2dynamics_config_general.x_w2dynamics_totdens)
        sec_dmft.n_correlated_orbitals = corr_orbs_per_atoms
        sec_dmft.n_correlated_electrons = occ_per_atoms
        sec_dmft.impurity_solver = 'CT-HYB'

    def parse_scc(self, data):
        sec_run = self.archive.run[0]
        sec_scc = sec_run.m_create(Calculation)
        if hasattr(self.archive.run[0], 'system') and len(self.archive.run[0].system) > 0:
            sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]  # ref DMFT

        # order calculations
        calc_keys = [key for key in data.keys() if key.startswith('dmft-') or key.startswith('stat-')]
        calc_keys.sort()

        # calculating how many inequivalent atoms are per unit cell
        n_ineq = 0
        for keys in data[calc_keys[0]]:
            if keys.startswith('ineq'):
                n_ineq += 1
        n_atoms = sec_run.method[-1].dmft.n_atoms_per_unit_cell

        calc_quantities = [
            'dc-latt', 'gdensnew', 'gdensold', 'glocnew-lattice', 'glocold-lattice', 'mu']
        for key in calc_keys:
            if key not in data.keys():
                continue
            sec_scf_iteration = sec_scc.m_create(ScfIteration)
            self.parse_dataset(data[key], sec_scf_iteration, include=calc_quantities)
            for sub_key in data[key].keys():
                if sub_key.startswith('ineq-'):
                    sec_ineq = sec_scf_iteration.m_create(x_w2dynamics_quantities)
                    self.parse_dataset(data[key][sub_key], sec_ineq)

            if sec_scf_iteration.x_w2dynamics_mu is not None:
                sec_energy = sec_scf_iteration.m_create(Energy)
                sec_energy.fermi = sec_scf_iteration.x_w2dynamics_mu * ureg.eV

            if key.endswith('last'):
                sec_gf = sec_scc.m_create(GreensFunctions)
                sec_gf.matsubara_freq = sec_run.x_w2dynamics_axes.x_w2dynamics_iw
                sec_gf.tau = sec_run.x_w2dynamics_axes.x_w2dynamics_tau
                sec_gf.chemical_potential = data.get(key)['mu']['value']
                norb = data['.config'].attrs.get('atoms.1.nd')
                for subkey in self._inequivalent_atom_map.keys():
                    parameters = []
                    if n_ineq == n_atoms:
                        for i in range(n_ineq):
                            parameters.append(getattr(
                                sec_scf_iteration.x_w2dynamics_ineq[i], self._inequivalent_atom_map.get(subkey, [])))
                    else:  # TODO check whether there are more complicated cases where this is not true
                        if n_atoms % n_ineq == 0 and n_ineq > 1:
                            for i in range(n_atoms):
                                parameters.append(getattr(
                                    sec_scf_iteration.x_w2dynamics_ineq[i % n_ineq], self._inequivalent_atom_map.get(subkey, [])))
                        elif n_ineq == 1:
                            for i in range(n_atoms):
                                parameters.append(getattr(
                                    sec_scf_iteration.x_w2dynamics_ineq[0], self._inequivalent_atom_map.get(subkey, [])))
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
                        parameters.append([[
                            sec_scf_iteration.x_w2dynamics_ineq[i].x_w2dynamics_occ[no, ns, no, ns]
                            for no in range(norb)] for ns in range(2)])

                else:
                    if n_atoms % n_ineq == 0 and n_ineq > 1:
                        for i in range(n_atoms):
                            parameters.append([[
                                sec_scf_iteration.x_w2dynamics_ineq[i % n_ineq].x_w2dynamics_occ[no, ns, no, ns]
                                for no in range(norb)] for ns in range(2)])
                    elif n_ineq == 1:
                        for i in range(n_atoms):
                            parameters.append([[
                                sec_scf_iteration.x_w2dynamics_ineq[0].x_w2dynamics_occ[no, ns, no, ns]
                                for no in range(norb)] for ns in range(2)])
                sec_gf.orbital_occupations = np.array(parameters)

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        try:
            data = h5py.File(self.filepath)
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
        self.parse_dataset(data.get('.axes'), sec_axes)

        # System section
        self.parse_system()

        # Method.DMFT section with inputs (HoppingMatrix + InteractionModel)
        self.parse_input_model(data.get('.config'))
        self.parse_method(data.get('.config'))

        # Calculation section
        self.parse_scc(data)

        # Workflow section
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = 'single_point'
        workflow = SinglePoint()
        self.archive.workflow2 = workflow
