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
from datetime import datetime
from netCDF4 import Dataset  # pylint: disable=no-name-in-module
from ase.data import chemical_symbols

from nomad.parsing.file_parser import TextParser, Quantity, FileParser
from nomad.units import ureg
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.method import Method
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, BandEnergies)
from .metainfo.yambo import (
    x_yambo_dipoles, x_yambo_dynamic_dielectric_matrix_fragment, x_yambo_io,
    x_yambo_dynamic_dielectric_matrix, x_yambo_local_xc_nonlocal_fock,
    x_yambo_dyson, x_yambo_local_xc_nonlocal_fock_bandenergies, x_yambo_bare_xc,
    x_yambo_bare_xc_bandenergies, x_yambo_module, x_yambo_transferred_momenta
)


class MainfileParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_f = r'[-+]*\d*\.\d+[Ee]*[-+]*\d*'

        io_quantities = [
            Quantity(
                'key_value',
                r'([A-Z\d].+?)(?:\(.+\)|\[.+\]| |)(:.+?)(?:\[|\n)',
                str_operation=lambda x: [v.strip() for v in x.split(':')],
                repeats=True
            ),
            Quantity('file', r'\[(?:RD|WR)(.+?)\]', dtype=str),
            Quantity('sn', r'- S/N *(\d+)', dtype=str)
        ]

        energies_quantities = [
            Quantity(
                'fermi',
                rf'Fermi Level.+?: +({re_f})',
                dtype=np.float64, unit=ureg.eV
            ),
            Quantity(
                'conduction',
                rf'Conduction Band Min +: +({re_f})',
                dtpye=np.float64, unit=ureg.eV
            ),
            Quantity(
                'valence',
                rf'Valence Band Max +: +({re_f})',
                dtpye=np.float64, unit=ureg.eV
            ),
            Quantity(
                'valence_conduction',
                rf'VBM / CBm +\[ev\]: +({re_f}) +({re_f})',
                dtpye=np.dtype(np.float64), unit=ureg.eV
            ),
            Quantity(
                'x_yambo_filled_bands',
                r'Filled Bands +: +(\d+)', dtype=np.int32, str_operation=lambda x: [1, int(x)]
            ),
            Quantity(
                'x_yambo_empty_bands',
                r'Empty Bands +: +([\d ]+)', dtype=np.dtype(np.int32)
            ),
            Quantity(
                'x_yambo_electronic_temperature',
                rf'Electronic Temp.+?: +{re_f} +({re_f})',
                dtype=np.float64, unit=ureg.kelvin
            ),
            Quantity(
                'x_yambo_bosonic_temperature',
                rf'Bosonic +Temp.+?: +{re_f} +({re_f})',
                dtype=np.float64, unit=ureg.kelvin
            ),
            Quantity(
                'x_yambo_finite_temperature_mode',
                r'Finite Temperature mode: +(\S+)', str_operation=lambda x: x == 'yes'
            ),
            Quantity(
                'x_yambo_electronic_density',
                rf'El\. density.+?: +(.+?)(?:\[|\n)',
                str_operation=lambda x: x.strip().split()[-1], dtype=np.float64
            ),
            Quantity(
                'states_summary',
                r'States summary +: Full +Metallic +Empty\s+(.+)',
                str_operation=lambda x: [v.split('-') for v in x.strip().split()]
            ),
            Quantity(
                'x_yambo_indirect_gaps',
                rf'Indirect Gaps.+?: +({re_f}) +({re_f})',
                dtype=np.dtype(np.float64), unit=ureg.eV
            ),
            Quantity(
                'x_yambo_direct_gaps',
                rf'Direct Gaps.+?: +({re_f}) +({re_f})',
                dtype=np.dtype(np.float64), unit=ureg.eV
            ),
            Quantity(
                'x_yambo_indirect_gap',
                rf'Indirect Gap.+?: +({re_f})',
                dtype=np.float64, unit=ureg.eV
            ),
            Quantity(
                'x_yambo_direct_gap',
                rf'Direct Gap.+?: +({re_f})',
                dtype=np.float64, unit=ureg.eV
            ),
            Quantity(
                'x_yambo_direct_gap_kpoint',
                r'Direct Gap localized at k-point.+?: +(\d+)',
                dtype=np.int32
            ),
            Quantity(
                'x_yambo_indirect_gap_kpoints',
                r'Indirect Gap between k-points.+?: +(\d+) +(\d+)',
                dtype=np.int32
            ),
        ]

        qp_properties_quantity = Quantity(
            'qp_properties',
            r'QP properties and I/O([\s\S]+? S/N \d+.+)',
            sub_parser=TextParser(quantities=[
                Quantity(
                    'qp_energy',
                    r'(QP \[eV\] @ K[\s\S]+?)\n *\n',
                    repeats=True, sub_parser=TextParser(quantities=[
                        Quantity(
                            'band',
                            rf'B= *(\d+) Eo= *({re_f}) E= *({re_f}) E-Eo= *({re_f}) '
                            rf'Re\(Z\)= *({re_f}) Im\(Z\)= *({re_f}) nlXC= *({re_f}) lXC= *({re_f}) So= *({re_f})',
                            repeats=True, dtype=np.dtype(np.float64)
                        ),
                        Quantity(
                            'kpoint',
                            r'K *\[\d+\].+?\: *(.+)',
                            dtype=np.dtype(np.float64)
                        )
                    ])
                ),
                Quantity(
                    'output',
                    r'(\[WR.+?\.QP\][\s\S]+?- S/N \d+.+)',
                    repeats=True, sub_parser=TextParser(quantities=io_quantities)
                )
            ])
        )

        module_quantities = [
            Quantity(
                'dipoles',
                r'Dipoles *\n([\s\S]+?)\n *\[\d+\]',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'input',
                        r'(\[RD.+?\][\s\S]+?- S/N \d+.+)',
                        repeats=True, sub_parser=TextParser(quantities=io_quantities)
                    ),
                    Quantity(
                        'output',
                        r'(\[WR.+?\.dipoles\][\s\S]+?- S/N \d+.+)',
                        repeats=True, sub_parser=TextParser(quantities=io_quantities)
                    )
                ])

            ),
            Quantity(
                'local_xc_nonlocal_fock',
                r'Local Exchange-Correlation \+ Non-Local Fock([\s\S]+?(?:\n *\[\d+\]|\Z))',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'output',
                        r'(\[WR.+?\.HF_and_locXC\][\s\S]+?- S/N \d+.+)',
                        repeats=True, sub_parser=TextParser(quantities=io_quantities)
                    ),
                    Quantity(
                        'x_yambo_plane_waves_vxc',
                        r'\[VXC\] Plane waves : *(\d+)',
                        dtype=np.int32
                    ),
                    Quantity(
                        'x_yambo_plane_waves_exs',
                        r'\[EXS\] Plane waves : *(\d+)',
                        dtype=np.int32
                    ),
                    Quantity(
                        'x_yambo_mesh_size',
                        r'Mesh size: *(\d+) *(\d+) *(\d+)',
                        dtype=np.dtype(np.int32)
                    ),
                    Quantity(
                        'energy_xc',
                        rf'E_xc *: *({re_f}) \[Ha\]',
                        dtype=np.float64, unit='hartree'
                    ),
                    Quantity(
                        'corrections',
                        r'Corrections @ K \[\d+\] *: *\[eV\]([\s\S]+?)\n *\n',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity(
                                'band',
                                rf'\<\d+\|nlXC\|\d+\> *= *({re_f}) *{re_f} \<\d+\|lXC\|\d+\> *= *({re_f}) *{re_f}',
                                repeats=True, dtype=np.dtype(np.float64)
                            )
                        ])
                    ),
                    Quantity(
                        'hf_occupations',
                        r'Hartree-Fock occupations report([\s\S]+?)(?:\n *\[\d+|\Z)',
                        sub_parser=TextParser(quantities=energies_quantities)
                    )
                ])
            ),
            # TODO add support for em1d
            Quantity(
                'dynamic_dielectric_matrix',
                r'Dynamic.+?Dielectric Matrix([\s\S]+?(?:\n *\[\d+\]|\Z))',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'output',
                        r'(\[WR.+?(?:pp|em1d|dip_iR_and_P)\][\s\S]+?- S/N \d+.+)',
                        repeats=True, sub_parser=TextParser(quantities=io_quantities)
                    ),
                    Quantity(
                        'x_yambo_mesh_size',
                        r'Mesh size: *(\d+) *(\d+) *(\d+)',
                        dtype=np.dtype(np.int32)
                    ),
                ])
            ),
            Quantity(
                'bare_xc',
                r'Bare local and non-local Exchange-Correlation([\s\S]+?(?:\n *\[\d+\]|\Z))',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'output',
                        r'(\[WR.+?\.HF_and_locXC\][\s\S]+?- S/N \d+.+)',
                        repeats=True, sub_parser=TextParser(quantities=io_quantities)
                    ),
                    Quantity(
                        'xc_hf_dft',
                        r'XC HF and DFT \[eV\]([\s\S]+?)\n *\n',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity(
                                'band',
                                rf'\<\d+\|HF\|\d+\> *= *({re_f}) *{re_f} *\<\d+\|DFT\|\d+\> *= *({re_f}) *{re_f}',
                                repeats=True, dtype=np.dtype(np.float64)
                            )
                        ])
                    ),
                    Quantity(
                        'hf_occupations',
                        r'HF occupations report([\s\S]+?Direct Gaps.+)',
                        sub_parser=TextParser(quantities=energies_quantities)
                    )
                ])
            ),
            Quantity(
                'dyson',
                r'Dyson equation: Newton solver([\s\S]+?(?:\n *\[\d+\]|\Z))',
                sub_parser=TextParser(quantities=[
                    qp_properties_quantity,
                    Quantity(
                        'g0w0',
                        r'G0W0([\s\S]+?\n *\[\d+\.\d+\])',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'x_yambo_bands_range',
                                r'Bands range *: *(\d+) *(\d+)',
                                dtype=np.dtype(np.int32)
                            ),
                            Quantity(
                                'x_yambo_g_damping',
                                rf'G damping.+?: *({re_f})',
                                dtype=np.float64
                            ),
                            Quantity(
                                'x_yambo_mesh_size',
                                r'Mesh size: *(\d+) *(\d+) *(\d+)',
                                dtype=np.dtype(np.int32)
                            ),
                            Quantity(
                                'input',
                                r'(\[RD.+?\.pp\][\s\S]+?- S/N \d+.+)',
                                repeats=True, sub_parser=TextParser(quantities=io_quantities)
                            )
                        ])
                    ),
                ])
            )
        ]

        self._quantities = [
            Quantity(
                'version',
                r'Version ([\d.]+ Revision \d+)', flatten=False, dtype=str
            ),
            Quantity('hash', r'Hash (\S+)', dtype=str),
            Quantity('build', r'(\S+) Build', dtype=str),
            Quantity(
                'date_start',
                r' (\d\d/\d\d/\d\d\d\d) at (\d\d:\d\d) YAMBO @ .+',
                flatten=False, dtype=str
            ),
            Quantity(
                'cpu_files_io',
                r'((?:Cores |CPU structure)[\s\S]+?)\n *\[\d+\]',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters',
                        r'([A-Z][\w/ ]+).*?(?: is | in |: ) *(\S+)',
                        repeats=True, str_operation=lambda x:[v.strip() for v in x.rsplit(' ', 1)]
                    ),
                    Quantity(
                        'input',
                        r'( \[RD.+[\s\S]+?- S/N \d+.+)',
                        repeats=False, sub_parser=TextParser(quantities=io_quantities)
                    )
                ])
            ),
            Quantity(
                'core_variables_setup',
                r'(CORE Variables Setup[\s\S]+?)\n *\[\d+\]',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energies_occupations',
                        r'Energies.+?& Occupations([\s\S]+?)(?:\[0|\Z)',
                        sub_parser=TextParser(quantities=energies_quantities + [
                            Quantity(
                                'eigenenergies',
                                rf'Energy unit is electronVolt \[eV\]([\s\S]+E *{re_f} *{re_f} *{re_f}.+)',
                                sub_parser=TextParser(quantities=[
                                    Quantity(
                                        'energies',
                                        rf'\n *E *({re_f} .+)',
                                        repeats=True, dtype=np.dtype(np.float64)),
                                    Quantity(
                                        'kpoints',
                                        rf'({re_f} *{re_f} *{re_f}) \(rlu\)',
                                        repeats=True, dtype=np.dtype(np.float64)),
                                    Quantity(
                                        'kpoints_weights',
                                        rf'weight +({re_f})',
                                        repeats=True, dtype=np.float64)]))
                        ])
                    )
                ])
            ),
            Quantity(
                'transferred_momenta',
                r'Transferred momenta grid([\s\S]+?)\n *\[\d+\]',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'input',
                        r'( \[RD.+[\s\S]+?- S/N \d+.+)',
                        repeats=True, sub_parser=TextParser(quantities=io_quantities)
                    ),
                    Quantity(
                        'qpoints',
                        rf'Q \[\d+\] *: *({re_f}) *({re_f}) *({re_f}) *\(iku\) \* weight *({re_f})',
                        repeats=True, dtype=np.dtype(np.float64)
                    ),
                    Quantity(
                        'module',
                        r'((?:Dipoles *\n|Dynamic Dielectric|Dyson|Bare local|Local Exchange)[\s\S]+?\n *\[\d+\.\d+\])',
                        repeats=True, sub_parser=TextParser(quantities=module_quantities)
                    ),
                    qp_properties_quantity
                ])
            ),
            Quantity(
                'module',
                r'((?:Dipoles *\n|Dynamic.+?Dielectric|Dyson|Bare local|Local Exchange)[\s\S]+?\n *\[\d+\])',
                repeats=True, sub_parser=TextParser(quantities=module_quantities)
            )
        ]


class NetCDFParser(FileParser):
    def __init__(self):
        super().__init__()

    def init_parameters(self):
        self._keys = []

    @property
    def netcdf_file(self):
        if self._file_handler is None:
            try:
                self._file_handler = Dataset(self.mainfile)
            except Exception:
                self.logger.warning('Error loading file.')

        return self._file_handler

    def parse(self, key=None):
        self._results = dict() if self._results is None else self._results
        if self.netcdf_file is None:
            return

        self._keys = list(self.netcdf_file.variables.keys())
        for key in self._keys:
            self._results[key] = self.netcdf_file.variables[key][:].data


class InputParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_key_block(val_in):
            val = val_in.strip().split('\n')
            return val[0].strip(), [np.array(
                v.split('#')[0].split('|')[:-1], dtype=np.float64) for v in val[1:]]

        self._quantities = [
            Quantity('key_value', r'\n *(\w+) *= *(.+) *#*', repeats=True),
            Quantity('key_block', r'\n *\% *(\w+)([\s\S]+?)\%', repeats=True, str_operation=str_to_key_block)]


class YamboParser:
    def __init__(self):
        self.mainfile_parser = MainfileParser()
        self.input_parser = InputParser()
        self.netcdf_parser = NetCDFParser()
        self.metainfo_map = {
            'cpu': 'cores', 'threads': 'threads_per_core', 'threads_tot': 'threads_total',
            'io_nodes': 'nodes_io'
        }
        self._module = None

    def init_parser(self):
        self.mainfile_parser.mainfile = self.filepath
        self._module = None

    def parse_method(self, source, target=None):
        if source is None:
            return

        method = self.archive.run[-1].m_create(Method) if target is None else target

        section = method.m_create(self._module)

        for input in source.get('input', []):
            parameters = {key.strip(): val for key, val in input.get('key_value', [])}
            x_yambo_input = section.m_create(x_yambo_io, x_yambo_module.x_yambo_input)
            x_yambo_input.x_yambo_file = input.file
            x_yambo_input.x_yambo_sn = input.sn
            x_yambo_input.x_yambo_parameters = parameters

        for output in source.get('output', []):
            parameters = {key.strip(): val for key, val in output.get('key_value', [])}
            x_yambo_output = section.m_create(x_yambo_io, x_yambo_module.x_yambo_output)
            x_yambo_output.x_yambo_file = output.file
            x_yambo_output.x_yambo_sn = output.sn
            x_yambo_output.x_yambo_parameters = parameters

        for key, val in source.items():
            if key.startswith('x_yambo'):
                setattr(section, key, val)

    def parse_calculation(self, source, target=None):
        if source is None:
            return

        calc = self.archive.run[-1].m_create(Calculation) if target is None else target
        valence_conduction = source.get('valence_conduction', [
            source.get('valence', 0.), source.get('conduction', 0.)
        ])
        calc.energy = Energy(
            fermi=source.get('fermi', 0.0),
            highest_occupied=valence_conduction[0], lowest_unoccupied=valence_conduction[1])

        states = source.states_summary
        if states is not None:
            calc.x_yambo_filled_bands = [int(s) for s in states[0]]
            calc.x_yambo_empty_bands = [int(s) for s in states[-1]]

        if self.netcdf_parser.EIGENVALUES is not None:
            eigenvalues = calc.m_create(BandEnergies)
            eigenvalues.kpoints = np.transpose(self.netcdf_parser.get('K-POINTS'))
            eigenvalues.energies = self.netcdf_parser.EIGENVALUES * ureg.eV

        elif source.eigenenergies is not None:
            eigenvalues = calc.m_create(BandEnergies)
            eigenvalues.kpoints = source.eigenenergies.kpoints
            eigenvalues.kpoints_weights = source.eigenenergies.kpoints_weights
            # TODO deal with spin polarized data
            energies = source.eigenenergies.energies
            eigenvalues.energies = np.reshape(energies, (1, len(
                eigenvalues.kpoints), np.size(energies) // len(eigenvalues.kpoints))) * ureg.eV

        if self.netcdf_parser.QP_E_Eo_Z is not None or self.netcdf_parser.QP_E is not None:
            gw_band_energies = calc.m_create(BandEnergies)
            n_spin = self.netcdf_parser.QP_table.shape[1] // 2
            gw_band_energies.kpoints = self.netcdf_parser.QP_kpts.T
            if self.netcdf_parser.QP_E_Eo_Z is not None:
                qp_energy, bare_energy, z = self.netcdf_parser.QP_E_Eo_Z[0].T
            else:
                qp_energy = self.netcdf_parser.QP_E.T[0]
                bare_energy = self.netcdf_parser.QP_Eo
                z = self.netcdf_parser.QP_Z.T[0]
            # TODO verify if indeed energies are only for one kpoint
            shape = (n_spin, 1, len(qp_energy) // n_spin)
            gw_band_energies.value_qp = np.reshape(qp_energy, shape) * ureg.hartree
            gw_band_energies.value_ks = np.reshape(bare_energy, shape) * ureg.hartree
            gw_band_energies.qp_linearization_prefactor = np.reshape(z, shape)

        elif source.qp_energy is not None:
            gw_band_energies = calc.m_create(BandEnergies)
            qp_energy = source.qp_energy
            gw_band_energies.kpoints = [q.kpoint for q in qp_energy]
            energies = np.transpose([q.band for q in qp_energy])
            qp_energy = energies[2].T
            gw_band_energies.value_qp = np.reshape(qp_energy, (1, *np.shape(qp_energy))) * ureg.eV
            gw_band_energies.value_ks = np.reshape(energies[1].T, (1, *np.shape(qp_energy))) * ureg.eV
            gw_band_energies.qp_linearization_prefactor = np.reshape(energies[4].T, (1, *np.shape(qp_energy)))

        if self.netcdf_parser.Sx_Vxc is not None or self.netcdf_parser.Sx is not None:
            n_spin = self.netcdf_parser.QP_table.shape[1] // 2
            gw_band_energies = calc.eigenvalues[-1] if calc.eigenvalues else calc.m_create(BandEnergies)
            if self.netcdf_parser.Sx_Vxc is not None:
                if self.netcdf_parser.Sx_Vxc.shape[0] % 8 == 0:
                    qp = self.netcdf_parser.Sx_Vxc.reshape(-1, 8).T
                    sx, vxc = qp[4], qp[6]
                else:
                    qp = self.netcdf_parser.Sx_Vxc.reshape(-1, 7).T
                    sx, vxc = qp[3], qp[5]
            else:
                sx = self.netcdf_parser.Sx.T[0]
                vxc = self.netcdf_parser.Vxc.T[0]
            shape = (n_spin, 1, len(sx) // n_spin)
            gw_band_energies.value_exchange = np.reshape(sx, shape)
            gw_band_energies.value_xc_potential = np.reshape(vxc, shape)

        for key, val in source.items():
            if key.startswith('x_yambo') and val is not None:
                setattr(calc, key, val)

        return calc

    def parse_input(self):
        if self.mainfile_parser.cpu_files_io.input is None:
            return

        run = self.archive.run[-1]

        # read structure data from netcdf input file
        self.netcdf_parser.mainfile = os.path.join(self.maindir, self.mainfile_parser.cpu_files_io.input.file)
        if self.netcdf_parser.mainfile is not None:
            system = run.m_create(System)
            positions = self.netcdf_parser.get('ATOM_POS', [])
            n_atoms = self.netcdf_parser.N_ATOMS
            atom_numbers = np.hstack([[self.netcdf_parser.atomic_numbers[int(n)]] * int(
                n_atoms[int(n)]) for n in range(len(n_atoms))])
            system.atoms = Atoms(
                positions=np.reshape(positions, (np.size(positions) // 3, 3)) * ureg.bohr,
                labels=[chemical_symbols[int(n)] for n in atom_numbers])
            if self.netcdf_parser.LATTICE_VECTORS is not None:
                system.atoms.lattice_vectors = self.netcdf_parser.LATTICE_VECTORS * ureg.bohr

        # reference calculation
        energies_occupations = self.mainfile_parser.get('core_variables_setup', {}).get('energies_occupations')
        self.parse_calculation(energies_occupations)

        # input parameters from mainfile
        input = run.m_create(x_yambo_io)
        input.x_yambo_file = self.mainfile_parser.cpu_files_io.input.file
        input.x_yambo_sn = self.mainfile_parser.cpu_files_io.input.sn
        parameters = {key.strip(): val for key, val in self.mainfile_parser.cpu_files_io.input.get('key_value', [])}
        input.x_yambo_parameters = parameters

    def parse_dynamic_dielectric_matrix(self, module):
        source = module.dynamic_dielectric_matrix
        if source is None:
            return

        self._module = x_yambo_dynamic_dielectric_matrix
        self.parse_method(source)

        for output in source.get('output', []):
            path = os.path.join(self.maindir, os.path.dirname(output.get('file', '')))
            if not os.path.isdir(path):
                continue
            ddm = self.archive.run[-1].method[-1].x_yambo_dynamic_dielectric_matrix[-1]
            for filename in os.listdir(path):
                if 'pp_fragment_' not in filename:
                    continue
                self.netcdf_parser.mainfile = os.path.join(path, filename)
                if self.netcdf_parser.mainfile is None:
                    continue
                fragment = ddm.m_create(x_yambo_dynamic_dielectric_matrix_fragment)
                self.netcdf_parser.parse()
                for key in self.netcdf_parser._keys:
                    val = self.netcdf_parser.get(key)
                    if key.startswith('FREQ_PARS_sec_iq'):
                        fragment.x_yambo_FREQ_PARS_sec_iq = val
                    elif key.startswith('FREQ_sec_iq'):
                        fragment.x_yambo_FREQ_sec_iq = val
                    elif key.startswith('X_Q'):
                        fragment.x_yambo_X_Q = val

    def parse_local_xc_nonlocal_fock(self, module):
        source = module.local_xc_nonlocal_fock
        if source is None:
            return

        self._module = x_yambo_local_xc_nonlocal_fock
        self.parse_method(source)
        calc = self.parse_calculation(source.hf_occupations)

        if source.corrections is not None:
            calc = self.archive.run[-1].m_create(Calculation) if calc is None else calc
            if len(calc.x_yambo_local_xc_nonlocal_fock_bandenergies) == 0:
                band_energy = calc.m_create(x_yambo_local_xc_nonlocal_fock_bandenergies)
                sx, vxc = np.transpose([c.band for c in source.corrections])
                band_energy.x_yambo_sx = np.reshape(sx, (1, *np.shape(sx.T))) * ureg.eV
                band_energy.x_yambo_vxc = np.reshape(vxc, (1, *np.shape(vxc.T))) * ureg.eV

        if source.energy_xc is not None:
            calc.energy = Energy(xc=EnergyEntry(value=source.energy_xc))

    def parse_bare_xc(self, module):
        source = module.bare_xc
        if source is None:
            return

        self._module = x_yambo_bare_xc
        self.parse_method(source)
        calc = self.parse_calculation(source.hf_occupations)
        if source.xc_hf_dft is not None:
            calc = self.archive.run[-1].m_create(Calculation) if calc is None else calc
            if len(calc.x_yambo_bare_xc_bandenergies) == 0:
                band_energy = calc.m_create(x_yambo_bare_xc_bandenergies)
                hf, dft = np.transpose([h.band for h in source.xc_hf_dft])
                hf, dft = hf.T, dft.T
                band_energy.x_yambo_hf = np.reshape(hf, (1, *np.shape(hf))) * ureg.eV
                band_energy.x_yambo_dft = np.reshape(dft, (1, *np.shape(dft))) * ureg.eV

    def parse_dipoles(self, module):
        source = module.dipoles
        if source is None:
            return
        self._module = x_yambo_dipoles
        self.parse_method(source)

    def parse_dyson(self, module):
        source = module.dyson
        if source is None:
            return

        self._module = x_yambo_dyson

        if source.g0w0 is not None:
            self.parse_method(source.g0w0)

        if source.qp_properties is not None:
            self.parse_method(source.qp_properties, self.archive.run[-1].method[-1])
            for output in source.qp_properties.get('output', []):
                self.netcdf_parser.mainfile = os.path.join(self.maindir, output.get('file', ''))
                self.netcdf_parser.parse()
                self.parse_calculation(source.qp_properties)

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        self.init_parser()

        run = self.archive.m_create(Run)
        run.program = Program(
            name='YAMBO', version=self.mainfile_parser.get('version', ''),
            x_yambo_build=self.mainfile_parser.get('build', ''),
            x_yambo_hash=self.mainfile_parser.get('hash', ''))
        date = datetime.strptime(self.mainfile_parser.get(
            'date_start', '01/01/1970 00:00'), '%d/%m/%Y %H:%M') - datetime(1970, 1, 1)
        run.time_run = TimeRun(date_start=date.total_seconds())

        if self.mainfile_parser.cpu_files_io is not None:
            self.parse_input()
            for key, val in self.mainfile_parser.cpu_files_io.parameters:
                key = key.strip().replace('/', '').replace(' ', '_').lower()
                val = val == 'yes' if val in ['yes', 'no'] else val
                setattr(run, 'x_yambo_%s' % key, val)

        def parse_module(module):
            self.parse_dipoles(module)
            self.parse_dynamic_dielectric_matrix(module)
            self.parse_local_xc_nonlocal_fock(module)
            self.parse_bare_xc(module)
            self.parse_dyson(module)

        if self.mainfile_parser.transferred_momenta is not None:
            self._module = x_yambo_transferred_momenta
            self.parse_method(self.mainfile_parser.transferred_momenta)
            self.parse_calculation(self.mainfile_parser.transferred_momenta.qp_properties)
            for module in self.mainfile_parser.transferred_momenta.get('module', []):
                parse_module(module)

        for module in self.mainfile_parser.get('module', []):
            parse_module(module)
