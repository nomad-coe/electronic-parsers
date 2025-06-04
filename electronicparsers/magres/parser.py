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
import numpy as np
import logging

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from runschema.run import Run, Program
from runschema.method import (
    Functional,
    Method,
    DFT,
    XCFunctional,
    BasisSetContainer,
    BasisSet,
    KMesh,
)
from runschema.system import System, Atoms
from runschema.calculation import (
    Calculation,
    MagneticSusceptibility,
    MagneticShielding,
    ElectricFieldGradient,
    SpinSpinCoupling,
)
from .metainfo.magres import m_package
from ..utils import BeyondDFTWorkflowsParser


re_float = r' *[-+]?\d+\.\d*(?:[Ee][-+]\d+)? *'


class MagresFileParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity('lattice_units', r'units *lattice *([a-zA-Z]+)'),
            Quantity('atom_units', r'units *atom *([a-zA-Z]+)'),
            Quantity('ms_units', r'units *ms *([a-zA-Z]+)'),
            Quantity('efg_units', r'units *efg *([a-zA-Z]+)'),
            Quantity('efg_local_units', r'units *efg_local *([a-zA-Z]+)'),
            Quantity('efg_nonlocal_units', r'units *efg_nonlocal *([a-zA-Z]+)'),
            Quantity('isc_units', r'units *isc *([a-zA-Z\^\d\.\-]+)'),
            Quantity('isc_fc_units', r'units *isc_fc *([a-zA-Z\^\d\.\-]+)'),
            Quantity('isc_spin_units', r'units *isc_spin *([a-zA-Z\^\d\.\-]+)'),
            Quantity(
                'isc_orbital_p_units', r'units *isc_orbital_p *([a-zA-Z\^\d\.\-]+)'
            ),
            Quantity(
                'isc_orbital_d_units', r'units *isc_orbital_d *([a-zA-Z\^\d\.\-]+)'
            ),
            Quantity('sus_units', r'units *sus *([a-zA-Z\^\d\.\-]+)'),
            Quantity('cutoffenergy_units', rf'units *calc\_cutoffenergy *([a-zA-Z]+)'),
            Quantity(
                'calculation',
                r'([\[\<]*calculation[\>\]]*[\s\S]+?)(?:[\[\<]*\/calculation[\>\]]*)',
                sub_parser=TextParser(
                    quantities=[
                        Quantity('code', r'calc\_code *([a-zA-Z]+)'),
                        Quantity(
                            'code_version', r'calc\_code\_version *([a-zA-Z\d\.]+)'
                        ),
                        Quantity(
                            'code_hgversion',
                            r'calc\_code\_hgversion ([a-zA-Z\d\:\+\s]*)\n',
                            flatten=False,
                        ),
                        Quantity(
                            'code_platform', r'calc\_code\_platform *([a-zA-Z\d\_]+)'
                        ),
                        Quantity('name', r'calc\_name *([\w]+)'),
                        Quantity('comment', r'calc\_comment *([\w]+)'),
                        Quantity('xcfunctional', r'calc\_xcfunctional *([\w]+)'),
                        Quantity(
                            'cutoffenergy',
                            rf'calc\_cutoffenergy({re_float})(?P<__unit>\w+)',
                        ),
                        Quantity(
                            'pspot',
                            r'calc\_pspot *([\w]+) *([\w\.\|\(\)\=\:]+)',
                            repeats=True,
                        ),
                        Quantity(
                            'kpoint_mp_grid',
                            r'calc\_kpoint\_mp\_grid *([\w]+) *([\w]+) *([\w]+)',
                        ),
                        Quantity(
                            'kpoint_mp_offset',
                            rf'calc\_kpoint\_mp\_offset({re_float * 3})$',
                        ),
                    ]
                ),
            ),
            Quantity(
                'atoms',
                r'([\[\<]*atoms[\>\]]*[\s\S]+?)(?:[\[\<]*\/atoms[\>\]]*)',
                sub_parser=TextParser(
                    quantities=[
                        Quantity('lattice', rf'lattice({re_float * 9})'),
                        Quantity('symmetry', r'symmetry *([\w\-\+\,]+)', repeats=True),
                        Quantity(
                            'atom',
                            rf'atom *([a-zA-Z]+) *[a-zA-Z\d]* *([\d]+) *({re_float * 3})',
                            repeats=True,
                        ),
                    ]
                ),
            ),
            Quantity(
                'magres',
                r'([\[\<]*magres[\>\]]*[\s\S]+?)(?:[\[\<]*\/magres[\>\]]*)',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'ms', rf'ms *(\w+) *(\d+)({re_float * 9})', repeats=True
                        ),
                        Quantity(
                            'efg', rf'efg *(\w+) *(\d+)({re_float * 9})', repeats=True
                        ),
                        Quantity(
                            'efg_local',
                            rf'efg_local *(\w+) *(\d+)({re_float * 9})',
                            repeats=True,
                        ),
                        Quantity(
                            'efg_nonlocal',
                            rf'efg_nonlocal *(\w+) *(\d+)({re_float * 9})',
                            repeats=True,
                        ),
                        Quantity(
                            'isc',
                            rf'isc *(\w+) *(\d+) *(\w+) *(\d+)({re_float * 9})',
                            repeats=True,
                        ),
                        Quantity(
                            'isc_fc',
                            rf'isc_fc *(\w+) *(\d+) *(\w+) *(\d+)({re_float * 9})',
                            repeats=True,
                        ),
                        Quantity(
                            'isc_orbital_p',
                            rf'isc_orbital_p *(\w+) *(\d+) *(\w+) *(\d+)({re_float * 9})',
                            repeats=True,
                        ),
                        Quantity(
                            'isc_orbital_d',
                            rf'isc_orbital_d *(\w+) *(\d+) *(\w+) *(\d+)({re_float * 9})',
                            repeats=True,
                        ),
                        Quantity(
                            'isc_spin',
                            rf'isc_spin *(\w+) *(\d+) *(\w+) *(\d+)({re_float * 9})',
                            repeats=True,
                        ),
                        Quantity('sus', rf'sus *({re_float * 9})', repeats=True),
                    ]
                ),
            ),
        ]


class MagresParser(BeyondDFTWorkflowsParser):
    def __init__(self):
        self.magres_file_parser = MagresFileParser()

        self._xc_functional_map = {
            'LDA': ['LDA_C_PZ', 'LDA_X_PZ'],
            'PW91': ['GGA_C_PW91', 'GGA_X_PW91'],
            'PBE': ['GGA_C_PBE', 'GGA_X_PBE'],
            'RPBE': ['GGA_X_RPBE'],
            'WC': ['GGA_C_PBE_GGA_X_WC'],
            'PBESOL': ['GGA_X_RPBE'],
            'BLYP': ['GGA_C_LYP', 'LDA_X_B88'],
            'B3LYP': ['HYB_GGA_XC_B3LYP5'],
            'HF': ['HF_X'],
            'HF-LDA': ['HF_X_LDA_C_PW'],
            'PBE0': ['HYB_GGA_XC_PBEH'],
            'HSE03': ['HYB_GGA_XC_HSE03'],
            'HSE06': ['HYB_GGA_XC_HSE06'],
            'RSCAN': ['MGGA_X_RSCAN', 'MGGA_C_RSCAN'],
        }

    def init_parser(self):
        self.magres_file_parser.mainfile = self.filepath
        self.magres_file_parser.logger = self.logger

    def _check_units_magres(self):
        """
        Check if the units of the NMR quantities are magres standard. If not, a warning
        is issued and the default units are used.
        """
        allowed_units = {
            'lattice': 'Angstrom',
            'atom': 'Angstrom',
            'ms': 'ppm',
            'efg': 'au',
            'efg_local': 'au',
            'efg_nonlocal': 'au',
            'isc': '10^19.T^2.J^-1',
            'isc_fc': '10^19.T^2.J^-1',
            'isc_orbital_p': '10^19.T^2.J^-1',
            'isc_orbital_d': '10^19.T^2.J^-1',
            'isc_spin': '10^19.T^2.J^-1',
            'sus': '10^-6.cm^3.mol^-1',
        }
        for key, value in allowed_units.items():
            data = self.magres_file_parser.get(f'{key}_units', '')
            if data and data != value:
                self.logger.warning(
                    f'The units of the NMR quantities are not parsed if they are not magres standard. '
                    f'We will use the default units.',
                    data={
                        'quantities': key,
                        'standard_units': value,
                        'parsed_units': data,
                    },
                )

    def parse_system(self, sec_run: Run):
        """
        Parse the System section by extracting information about the atomic structure:
        lattice vectors, periodic boundary conditions, atom positions and labels from the
        magres file.

        Args:
            sec_run (Run): the section Run where System will be added.
        """
        sec_atoms = Atoms()

        # Check if [atoms][/atoms] was correctly parsed
        atoms = self.magres_file_parser.get('atoms')
        if not atoms:
            self.logger.warning('Could not find atomic structure in magres file.')
            return

        # Store lattice_vectors and periodic boundary conditions
        lattice_vectors = np.reshape(np.array(atoms.get('lattice', [])), (3, 3))
        sec_atoms.lattice_vectors = lattice_vectors * ureg.angstrom
        pbc = (
            [True, True, True] if lattice_vectors is not None else [False, False, False]
        )
        sec_atoms.periodic = pbc

        # Storing atom positions and labels
        atoms_list = atoms.get('atom', [])
        if len(atoms_list) == 0:
            self.logger.warning(
                'Could not find atom positions and labels in magres file.'
            )
            return
        atom_labels = []
        atom_positions = []
        for atom in atoms_list:
            atom_labels.append(atom[0])
            atom_positions.append(atom[2:])
        sec_atoms.labels = atom_labels
        sec_atoms.positions = atom_positions * ureg.angstrom

        # Add Atoms to System and this to Run
        sec_system = System()
        sec_system.atoms = sec_atoms
        sec_run.system.append(sec_system)

    def parse_method(self, calculation_params: TextParser, sec_run: Run):
        """
        Parse the Method section by extracting information about the NMR method:basis set,
        exchange-correlation functional, cutoff energy, and K mesh.

        Note: only CASTEP-like method parameters are currently being supported.

        Args:
            calculation_params (TextParser): the parsed [calculation][/calculation] block parameters.
            sec_run (Run): the section Run where Method will be added.
        """
        sec_method = Method(label='NMR')

        # XC functional parsing
        sec_dft = DFT()
        xc_functional = calculation_params.get('xcfunctional', 'LDA')
        xc_functional_labels = self._xc_functional_map.get(xc_functional)
        if xc_functional_labels:
            sec_xc_functional = XCFunctional()
            for functional in xc_functional_labels:
                sec_functional = Functional(name=functional)
                if '_X_' in functional or functional.endswith('_X'):
                    sec_xc_functional.exchange.append(sec_functional)
                elif '_C_' in functional or functional.endswith('_C'):
                    sec_xc_functional.correlation.append(sec_functional)
                elif 'HYB' in functional:
                    sec_xc_functional.hybrid.append(sec_functional)
                else:
                    sec_xc_functional.contributions.append(sec_functional)
            sec_dft.xc_functional = sec_xc_functional
            sec_method.dft = sec_dft

        # Basis set parsing (adding cutoff energies units check)
        cutoff = calculation_params.get('cutoffenergy')
        if cutoff.dimensionless:
            cutoff_units = self.magres_file_parser.get('cutoffenergy_units', 'eV')
            if cutoff_units == 'Hartree':
                cutoff_units = 'hartree'
            cutoff = cutoff.magnitude * ureg(cutoff_units)
        sec_basis_set = BasisSetContainer(
            type='plane waves',
            scope=['wavefunction'],
            basis_set=[BasisSet(scope=['valence'], type='plane waves', cutoff=cutoff)],
        )
        sec_method.electrons_representation.append(sec_basis_set)

        # KMesh parsing
        sec_k_mesh = KMesh(
            grid=calculation_params.get('kpoint_mp_grid', [1, 1, 1]),
            offset=calculation_params.get('kpoint_mp_offset', [0, 0, 0]),
        )
        sec_method.k_mesh = sec_k_mesh

        # Add Method to Run
        sec_run.method.append(sec_method)

    def parse_calculation(self, sec_run: Run):
        """
        Parse the Calculation section by extracting information about the magnetic outputs
        in the magres file: magnetic shielding tensor, electric field gradient, indirect
        spin-spin coupling, and magnetic susceptibility. It also stores references to the
        System and Method sections.

        Args:
            sec_run (Run): the section Run where System will be added.
        """
        # Check if [magres][/magres] was correctly parsed
        magres_data = self.magres_file_parser.get('magres')
        if not magres_data:
            self.logger.warning('Could not find [magres] data block in magres file.')
            return

        # Creating Calculation and adding System and Method refs
        sec_scc = Calculation()
        sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]
        atom_labels = sec_scc.system_ref.atoms.labels
        if not atom_labels:
            self.logger.warning('Could not find the parsed atomic cell information.')
            return
        n_atoms = len(atom_labels)

        # Magnetic Shielding Tensor (ms) parsing
        data = magres_data.get('ms', [])
        if np.size(data) == n_atoms * (9 + 2):  # 2 extra columns with atom labels
            values = np.reshape([d[2:] for d in data], (n_atoms, 3, 3))
            values = np.transpose(values, axes=(0, 2, 1))
            isotropic_value = np.trace(values, axis1=1, axis2=2) / 3.0
            atoms = np.array([d[:2] for d in data])
            sec_ms = MagneticShielding(atoms=atoms)
            sec_ms.value = values * 1e-6 * ureg('dimensionless')
            sec_ms.isotropic_value = isotropic_value * 1e-6 * ureg('dimensionless')
            sec_scc.magnetic_shielding.append(sec_ms)

        # Electric Field Gradient (efg) parsing
        efg_contributions = {
            'efg_local': 'local',
            'efg_nonlocal': 'non_local',
            'efg': 'total',
        }
        for tag, contribution in efg_contributions.items():
            data = magres_data.get(tag, [])
            if np.size(data) != n_atoms * (9 + 2):  # 2 extra columns with atom labels
                continue
            values = np.reshape([d[2:] for d in data], (n_atoms, 3, 3))
            values = np.transpose(values, axes=(0, 2, 1))
            atoms = np.array([d[:2] for d in data])
            sec_efg = ElectricFieldGradient(atoms=atoms)
            sec_efg.contribution = contribution
            sec_efg.value = values * 9.717362e21 * ureg('V/m^2')
            sec_scc.electric_field_gradient.append(sec_efg)

        # Indirect Spin-Spin Coupling (isc) parsing
        isc_contributions = {
            'isc_fc': 'fermi_contact',
            'isc_orbital_p': 'orbital_paramagnetic',
            'isc_orbital_d': 'orbital_diamagnetic',
            'isc_spin': 'spin_dipolar',
            'isc': 'total',
        }
        for tag, contribution in isc_contributions.items():
            # TODO the data is organized differently to the NOMAD metainfo, we need to transform it properly
            data = magres_data.get(tag, [])
            if np.size(data) != n_atoms**2 * (
                9 + 4
            ):  # 4 extra columns with atom labels
                continue
            values = np.reshape([d[4:] for d in data], (n_atoms, n_atoms, 3, 3))
            values = np.transpose(values, axes=(0, 1, 3, 2))
            atoms = np.array([d[:4] for d in data])
            atoms_1 = atoms[:, 0:2]
            atoms_2 = atoms[:, 2:4]
            sec_isc = SpinSpinCoupling(atoms_1=atoms_1, atoms_2=atoms_2)
            sec_isc.contribution = contribution
            sec_isc.reduced_value = values * 1e19 * ureg('K^2/J')
            sec_scc.spin_spin_coupling.append(sec_isc)

        # Magnetic Susceptibility (sus) parsing
        data = magres_data.get('sus', [])
        if np.size(data) == 9:
            values = np.transpose(np.reshape(data, (3, 3)))
            sec_sus = MagneticSusceptibility()
            sec_sus.scale_dimension = 'macroscopic'
            sec_sus.value = values * 1e-6 * ureg('dimensionless')
            sec_scc.magnetic_susceptibility.append(sec_sus)

        # Add Calculation to Run
        sec_run.calculation.append(sec_scc)

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()
        self._check_units_magres()

        # Create Run with Program information
        sec_run = Run()
        calculation_params = self.magres_file_parser.get('calculation', {})
        program_name = calculation_params.get('code', '')
        if program_name != 'CASTEP':
            self.logger.error(
                'Only CASTEP-based NMR simulations are supported by the magres parser.'
            )
            return
        sec_run.program = Program(
            name=program_name,
            version=calculation_params.get('code_version', ''),
        )

        # Parse main sections under Run
        self.parse_system(sec_run)

        self.parse_method(calculation_params, sec_run)

        self.parse_calculation(sec_run)

        # Add run to the Archive
        self.archive.run.append(sec_run)

        # We try to resolve the entry_id and mainfile of other entries in the upload
        filepath_stripped = self.filepath.split('raw/')[-1]
        metadata = []
        try:
            from nomad.app.v1.routers.uploads import get_upload_with_read_access
            from nomad.datamodel import User

            upload_id = self.archive.metadata.upload_id
            upload = get_upload_with_read_access(
                upload_id=upload_id,
                user=User.get(user_id=self.archive.metadata.main_author.user_id),
            )
            with upload.entries_metadata() as entries_metadata:
                metadata.extend(
                    [[meta.entry_id, meta.mainfile] for meta in entries_metadata]
                )
        except Exception:
            self.logger.warning(
                'Could not resolve the entry_id and mainfile of other entries in the upload.'
            )
            return

        for entry_id, mainfile in metadata:
            if mainfile == filepath_stripped:  # we skip the current parsed mainfile
                continue
            # We try to load the archive from its context and connect both the CASTEP
            # and the magres entries
            try:
                entry_archive = archive.m_context.load_archive(
                    entry_id, upload_id, None
                )
                method_label = entry_archive.run[-1].method[-1].label
                if method_label == 'NMR':
                    castep_archive = entry_archive
                    # We write the workflow NMRMagRes directly in the magres entry
                    self.parse_nmr_magres_file_format(castep_archive)
                    break
            except Exception:
                continue
