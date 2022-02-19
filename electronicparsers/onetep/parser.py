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
from datetime import datetime

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import (
    Run, Program, TimeRun)
from nomad.datamodel.metainfo.simulation.method import (
    Method, DFT, XCFunctional, Functional
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, ScfIteration, Charges
)
from .metainfo.onetep import (
    x_onetep_section_tddft, x_onetep_section_tddft_excitations)


re_n = r'[\n\r]'
re_f = r'[-+]?\d+\.\d*(?:[DdEe][-+]\d+)?'


class InputParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def to_block(val_in):
            val = val_in.strip().replace('"', '').splitlines()
            key = val[0].strip()
            return [key.lower(), [v.split() for v in val[1:]]]

        self._quantities = [
            Quantity('parameter', r'([a-z_]+) +: +(\S+)', repeats=True),
            Quantity(
                'block',
                r'\%block +([a-z_]+\s+[\s\S]+?)\s+\%endblock',
                repeats=True, str_operation=to_block)
        ]

    @property
    def cell(self):
        self._results = dict() if self._results is None else self._results
        if self._results.get('cell') is None:

            def resolve_unit(value):
                if isinstance(value[0][0], str):
                    if value[0][0].lower().startswith('ang'):
                        return ureg.angstrom
                    if value[0][0].lower().startswith('bohr'):
                        return ureg.bohr

            cell = dict()
            for block in self.get('block', []):
                if block[0].lower() == 'lattice_cart':
                    unit = resolve_unit(block[1])
                    cell['lattice_vectors'] = block[1] * ureg.bohr if unit is None else block[1][1:] * unit
                elif block[0].lower() == 'positions_abs':
                    unit = resolve_unit(block[1])
                    value = block[1] if unit is None else block[1][1:]
                    unit = ureg.bohr if unit is None else unit
                    cell['labels'] = [v[0] for v in value]
                    cell['positions'] = np.array([v[1:4] for v in value], dtype=np.dtype(np.float64)) * unit
            self._results['cell'] = cell
        return self._results['cell']


class OutParser(TextParser):
    def init_quantities(self):
        calculation_quantities = [
            Quantity(
                'iteration',
                rf'\>\>\> Optimising kernel([\s\S]+?'
                rf'(?:Predicted gain in energy|\-\> RMS NGWF gradient|maximum number of NGWF).+)',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_total',
                        rf'Total energy += +({re_f}) +Eh',
                        dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'band_gap',
                        rf'Estimated bandgap += +({re_f}) +Eh',
                        dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'x_onetep_rms_occupancy_error',
                        rf'RMS occupancy error += +({re_f})',
                        dtype=np.float64
                    ),
                    Quantity(
                        'x_onetep_commutator',
                        rf'\[H,K\] commutator += +({re_f})',
                        dtype=np.float64
                    ),
                    Quantity(
                        'rms_gradient',
                        rf'RMS gradient += +({re_f})',
                        dtype=np.float64
                    )
                ])
            ),
            Quantity(
                'energy_components',
                r'ENERGY COMPONENTS \(Eh\)([\s\S]+?\={10})',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'contribution', rf'\| (.+): +({re_f})',
                        str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)], repeats=True),
                    Quantity('integrated_density', rf'Integrated density +: +({re_f})', dtype=np.float64)
                ])
            ),
            Quantity(
                'forces',
                r'Forces \*+([\s\S]+?TOTAL)',
                sub_parser=TextParser(quantities=[Quantity(
                    'value',
                    rf'[A-Z][a-z]* +\d+ +({re_f} +{re_f} +{re_f})',
                    dtype=np.dtype(np.float64))])
            ),
            Quantity(
                'convergence_tolerance_energy_difference',
                rf'dE\/ion +\| +({re_f}) +\| +({re_f}) +\| +Ha',
                dtype=np.dtype(np.float64), unit=ureg.hartree
            ),
            Quantity(
                'convergence_tolerance_force_maximum',
                rf'\|F\|max +\| +({re_f}) +\| +({re_f}) +\| +Ha\/Bohr',
                dtype=np.dtype(np.float64), unit=ureg.hartree / ureg.bohr
            ),
            Quantity(
                'convergence_tolerance_displacement_maximum',
                rf'\|dR\|max +\| +({re_f}) +\| +({re_f}) +\| +Bohr',
                dtype=np.dtype(np.float64), unit=ureg.bohr
            ),
            Quantity(
                'cell',
                r'Element +Atom +Absolute co\-ordinates of atoms([\s\S]+?)x{10}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'positions',
                        rf'({re_f} +{re_f} +{re_f})',
                        dtype=np.dtype(np.float64), repeats=True),
                    Quantity('labels', r'([A-Z][a-z]*) +\d+', dtype=str, repeats=True)])
            ),
            Quantity(
                'mulliken',
                r'Mulliken Atomic Populations\s+\-+\s+'
                r'Species +Ion +Total +Charge \(e\)\s+\=+\s+([\s\S]+?)\={10}',
                str_operation=lambda x: [v.strip().split() for v in x.strip().splitlines()]
            )
        ]

        self._quantities = [
            Quantity('program_version', r'Version (\S+)', dtype=str),
            Quantity('program_name', r'(\S+) is based on developments described', dtype=str),
            Quantity('x_onetep_number_of_processors', r'Default threads: (\d+)', dtype=np.dtype(np.int32)),
            Quantity('input_file', r'Reading parameters from file \"(.+?)\"', dtype=str),
            Quantity(
                'input',
                r'INPUT FILE \-+([\s\S]+?)\-+ END INPUT FILE',
                sub_parser=TextParser(quantities=[
                    Quantity('parameter', r'([a-z\_]+) +: +(\S+)', repeats=True),
                ])
            ),
            Quantity(
                'date_start',
                r'Job started: (\d\d\-\d\d\-\d\d\d\d \d\d:\d\d \(\+\d\d\d\d\))',
                flatten=False, dtype=str),
            Quantity(
                'date_end',
                r'Job completed: (\d\d\-\d\d\-\d\d\d\d \d\d:\d\d \(\+\d\d\d\d\))',
                flatten=False, dtype=str),
            Quantity(
                'geometry_optimization',
                r'Starting ONETEP Geometry Optimisation([\s\S]+?)(?:\- TIMING|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'single_point',
                        r'\>\>\> Optimising kernel for current NGWFs:([\s\S]+?\|dR\|max.+)',
                        sub_parser=TextParser(quantities=calculation_quantities)
                    ),
                    Quantity(
                        'iteration',
                        r'(Starting BFGS iteration +\d+[\s\S]+?\|dR\|max.+)',
                        repeats=True, sub_parser=TextParser(quantities=calculation_quantities + [
                            Quantity(
                                'improve',
                                r'BFGS: improving iteration([\s\S]+?\|dR\|max.+)',
                                sub_parser=TextParser(quantities=calculation_quantities)
                            )
                        ])
                    ),
                    Quantity('converged', r'Geometry +optimization +(\S+)', str_operation=lambda x: x == 'completed'),
                    Quantity(
                        'final_configuration',
                        r'(Final Configuration:[\s\S]+?Final Enthalpy.+)',
                        sub_parser=TextParser(quantities=[

                        ])
                    )
                ])
            ),
            Quantity(
                'single_point',
                r'(\>\>\> Optimising kernel for current NGWFs:[\s\S]+?)(?:\- TIMING|\Z)',
                sub_parser=TextParser(quantities=calculation_quantities)
            ),
            Quantity(
                'tddft',
                r'(LR\-TDDFT CG optimisation[\s\S]+?)(?:\- TIMING|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        r'(LR_TDDFT CG iteration +\d+ +\#+[\s\S]+?(?:\#{75}|TDDFT_grad))',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity(
                                'energy_total',
                                rf'LR\-TDDFT energy += +({re_f})',
                                dtype=np.float64, unit=ureg.hartree
                            ),
                            Quantity(
                                'x_onetep_tddft_omega_change',
                                rf'Change in omega += +({re_f})',
                                dtype=np.float64
                            ),
                            Quantity(
                                'rms_gradient',
                                rf'RMS gradient += +({re_f})',
                                dtype=np.float64
                            ),
                            Quantity(
                                'x_onetep_tddft_number_conv_states',
                                r'Number of newly converged states: +(\d+)',
                                dtype=np.int32
                            )
                        ])
                    ),
                    Quantity(
                        'excitation',
                        r'\|Excitation\| +Energy \(in Ha\).+([\s\d\.\-\+E]+)',
                        str_operation=lambda x: np.array(
                            [v.strip().split() for v in x.strip().splitlines()],
                            dtype=np.dtype(np.float64))
                    )
                ])
            )
        ]


class OnetepParser:
    def __init__(self):
        self.out_parser = OutParser()
        self.input_parser = InputParser()
        self._xc_map = {
            'PBE': ['GGA_C_PBE', 'GGA_X_PBE'],
            'LDA': ['LDA_C_PZ', 'LDA_X_PZ'],
            'PW91': ['GGA_C_PW91', 'GGA_X_PW91'],
            'PW92': ['GGA_C_PW92', 'GGA_X_PW92'],
            'GGA': ['GGA_X_PBE'],
            'CAPZ': ['LDA_C_PZ'],
            'VWN': ['LDA_C_VWN'],
            'PBESOL': ['GGA_X_PBE_SOL'],
            'RPBE': ['GGA_X_RPBE'],
            'REVPBE': ['GGA_X_PBE_R'],
            'BLYP': ['GGA_X_B88', 'GGA_C_LYP'],
            'XLYP': ['GGA_XC_XLYP'],
            'OPTB88': ['GGA_X_OPTB88_VDW', 'LDA_C_PZ'],
            'OPTPBE': ['GGA_X_OPTPBE_VDW', 'LDA_C_PZ'],
            'VDWDF': ['GGA_X_PBE_R_VDW', 'LDA_C_PZ'],
            'VDWDF2': ['GGA_X_RPW86', 'LDA_C_PZ'],
            'VV10': ['HYB_GGA_XC_LC_VV10'],
            'AVV10S': ['GGA_X_AM05', 'GGA_C_AM05_rVV10-sol']
        }
        self._metainfo_map = {
            'Kinetic': 'kinetic_electronic', 'Hartree': 'correction_hartree',
            'Pseudopotential (local)': 'x_onetep_pseudopotential_local',
            'Pseudopotential (non-local)': 'x_onetep_pseudopotential_non_local',
            'Exchange-correlation': 'xc', 'Ewald': 'ewald', 'Total': 'total'
        }

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger
        self.input_parser.logger = self.logger

    def parse_configuration(self, source):
        def parse_system(source):
            cell = source.get('cell', self.input_parser.cell)
            if cell is None:
                return

            sec_system = self.archive.run[-1].m_create(System)
            positions = cell.get('positions')
            positions = positions * ureg.bohr if isinstance(positions, list) else positions
            sec_system.atoms = Atoms(positions=positions, labels=cell.get('labels'))
            sec_system.atoms.lattice_vectors = cell.get('lattice_vectors', self.input_parser.cell.get('lattice_vectors'))
            return sec_system

        def parse_scc(source):
            sec_scc = self.archive.run[-1].m_create(Calculation)

            # scf iteration
            for iteration in source.get('iteration', []):
                sec_scf = sec_scc.m_create(ScfIteration)
                sec_scf.energy = Energy(
                    total=EnergyEntry(value=iteration.energy_total))

            energies = source.get('energy_components')
            if energies is not None:
                sec_energy = sec_scc.m_create(Energy)
                for contribution in energies.get('contribution', []):
                    key = self._metainfo_map.get(contribution[0])
                    if key is not None:
                        setattr(sec_energy, key, EnergyEntry(value=contribution[1] * ureg.hartree))
            elif len(sec_scc.scf_iteration) > 0:
                sec_scc.energy = Energy(total=EnergyEntry(value=sec_scc.scf_iteration[-1].energy.total.value))

            if source.get('forces') is not None:
                sec_scc.forces = Forces(total=ForcesEntry(value=source.forces.value * (ureg.hartree / ureg.bohr)))

            if source.get('mulliken') is not None:
                sec_charges = sec_scc.m_create(Charges)
                sec_charges.analysis_method = 'Mulliken'
                sec_charges.value = [v[3] for v in source.get('mulliken', [])] * ureg.elementary_charge

            return sec_scc

        sec_system = parse_system(source)
        sec_scc = parse_scc(source)
        sec_scc.system_ref = sec_system

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.maindir = os.path.dirname(self.filepath)
        self.init_parser()

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(
            name=self.out_parser.get('program_name'), version=self.out_parser.get('program_version'))

        def get_timestamp(date):
            if date is None:
                return
            return datetime.strptime(date, '%d-%m-%Y %H:%M (%z)').timestamp()

        sec_run.time_run = TimeRun(
            date_start=get_timestamp(self.out_parser.date_start),
            date_end=get_timestamp(self.out_parser.date_end))

        self.input_parser.mainfile = os.path.join(self.maindir, self.out_parser.get('input_file', ''))

        input_parameters = {key: val for key, val in self.out_parser.get('input', {}).get('parameter', [])}
        sec_method = sec_run.m_create(Method)
        sec_method.x_onetep_input_parameters = input_parameters
        if input_parameters.get('xc_functional') is not None:
            sec_method.dft = DFT(xc_functional=XCFunctional())
            for xc_functional in self._xc_map.get(input_parameters.get('xc_functional'), []):
                if '_X_' in xc_functional or xc_functional.endswith('_X'):
                    sec_method.dft.xc_functional.exchange.append(Functional(name=xc_functional))
                elif '_C_' in xc_functional or xc_functional.endswith('_C'):
                    sec_method.dft.xc_functional.correlation.append(Functional(name=xc_functional))
                elif 'HYB' in xc_functional:
                    sec_method.dft.xc_functional.hybrid.append(Functional(name=xc_functional))
                else:
                    sec_method.dft.xc_functional.contributions.append(Functional(name=xc_functional))

        if self.out_parser.geometry_optimization is not None:
            if self.out_parser.geometry_optimization.single_point is not None:
                self.parse_configuration(self.out_parser.geometry_optimization.single_point)
            for iteration in self.out_parser.geometry_optimization.get('iteration', []):
                self.parse_configuration(iteration if iteration.improve is None else iteration.improve)

        elif self.out_parser.single_point is not None:
            self.parse_configuration(self.out_parser.single_point)

        elif self.out_parser.tddft is not None:
            self.parse_configuration(self.out_parser.tddft)
            if self.out_parser.tddft is not None:
                sec_tddft = sec_run.calculation[-1].m_create(x_onetep_section_tddft)
                for excitation in self.out_parser.tddft.get('excitation', []):
                    sec_excitation = sec_tddft.m_create(x_onetep_section_tddft_excitations)
                    sec_excitation.x_onetep_tddft_excit_energy = excitation[1] * ureg.hartree
                    sec_excitation.x_onetep_tddft_excit_oscill_str = excitation[2]
                    sec_excitation.x_onetep_tddft_excit_lifetime = excitation[3] * ureg.ns
        # TODO parse md
