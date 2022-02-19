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
from nomad.parsing import FairdiParser
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, DFT, XCFunctional, Functional
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, ScfIteration, Forces, ForcesEntry, Stress,
    StressEntry, Multipoles, MultipolesEntry
)
from .metainfo.qbox import x_qbox_section_MLWF


re_n = r'[\n\r]'
re_f = r'[-+]?\d+\.\d*(?:[DdEe][-+]\d+)?'


class QboxXMLParser(TextParser):
    def init_quantities(self):
        run_quantities = [
            Quantity(
                'parameter',
                r'\[qbox\] \<cmd\>set +(.+?)\<\/cmd\>',
                str_operation=lambda x: x.split(' ', 1), repeats=True),
            Quantity(
                'species',
                r'(\<species name=[\s\S]=?)</species>',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity('symbol', r'\<symbol\>([A-Z][a-z]*)', dtype=str),
                    Quantity('atomic_numer', r'\<atomic_number\>(\d+)', dtype=np.int32),
                    Quantity('mass', r'\<mass\>(\d+)', dtype=np.float64)
                ])
            ),
            Quantity(
                'iteration',
                r'(\<iteration[\s\S]+?)</iteration>',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity('charge', rf'total_electronic_charge: +({re_f})', dtype=np.float64),
                    Quantity('energy_kinetic_electronic', rf'\<ekin\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_conf', rf'\<econf\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_ps', rf'\<eps\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_nl', rf'\<enl\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_coulomb', rf'\<ecoul\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_xc', rf'\<exc\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_sr', rf'\<esr\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_self', rf'\<eself\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_ts', rf'\<ets\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_exf', rf'\<eexf\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_total', rf'\<etotal\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_pv', rf'\<epv\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_efield', rf'\<eefield\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('energy_x_qbox_enthalpy', rf'\<enthalpy\> +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity(
                        'stress_tensor',
                        r'(\<stress_tensor[\s\S]+?)\<\/stress_tensor\>',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'contribution',
                                r'(\<sigma_.*\_*xx\>[\s\S]+?)\<\/sigma_.*\_*xz\>',
                                repeats=True, sub_parser=TextParser(quantities=[
                                    Quantity('kind', r'\<sigma_e(.+?)\_', dtype=str),
                                    Quantity('value', rf'\> +({re_f})', dtype=np.float64, repeats=True)
                                ])
                            )
                        ])
                    ),
                    Quantity(
                        'multipole',
                        r'(\<[a-z]+pole\>[\s\S]+?)\<\/[a-z]+pole\>',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity(
                                'dipole',
                                rf'\<dipole_([a-z]+)\> +({re_f} +{re_f} +{re_f})',
                                repeats=True
                            ),
                            Quantity(
                                'quadrupole',
                                rf'\<quadrupole_([a-z]+)\>\s+'
                                rf'({re_f} +{re_f} +{re_f})\s+'
                                rf'({re_f} +{re_f} +{re_f})\s+'
                                rf'({re_f} +{re_f} +{re_f})\s+',
                                repeats=True
                            )
                        ])
                    ),
                    Quantity(
                        'mlwf',
                        r'(\<mlwf_set[\s\S]+?)\<\/mlwf_set\>',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'center',
                                rf'mlwf center=\" +({re_f} +{re_f} +{re_f}) +\"\s+spread=\" +({re_f})',
                                repeats=True, dtype=np.dtype(np.float64)
                            )
                        ])
                    ),
                    Quantity(
                        'scf',
                        r'(total_electronic_charge:.+\s+\<eigenvalue_sum[\s\S]+?)\<\/etotal_int\>',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity('charge', rf'total_electronic_charge: +({re_f})', dtype=np.float64),
                            Quantity(
                                'energy_sum_eigenvalues',
                                rf'\<eigenvalue_sum\> +({re_f})',
                                unit=ureg.hartree, dtype=np.float64),
                            Quantity(
                                'energy_total',
                                rf'\<etotal_int\> +({re_f})',
                                unit=ureg.hartree, dtype=np.float64),
                        ])
                    ),
                    Quantity(
                        'atomset',
                        r'(\<atomset\>[\s\S]+?)</atomset>',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'lattice_vectors',
                                rf'\<unit_cell\s+'
                                rf'a=\" +({re_f}) +({re_f}) +({re_f})\"\s+'
                                rf'b=\" +({re_f}) +({re_f}) +({re_f})\"\s+'
                                rf'c=\" +({re_f}) +({re_f}) +({re_f})\"\s+',
                                dtype=np.dtype(np.float64), shape=(3, 3), unit=ureg.bohr
                            ),
                            Quantity(
                                'atom',
                                r'(\<atom[\s\S]+?)\<\/atom\>',
                                repeats=True, sub_parser=TextParser(quantities=[
                                    Quantity(
                                        'label',
                                        r'\<atom name=\"([A-Z][a-z]*)',
                                        dtype=str
                                    ),
                                    Quantity(
                                        'position',
                                        rf'\<position\> +({re_f} +{re_f} +{re_f})',
                                        dtype=np.dtype(np.float64)
                                    ),
                                    Quantity(
                                        'velocity',
                                        rf'\<velocity\> +({re_f} +{re_f} +{re_f})',
                                        dtype=np.dtype(np.float64)
                                    ),
                                    Quantity(
                                        'force',
                                        rf'\<force\> +({re_f} +{re_f} +{re_f})',
                                        dtype=np.dtype(np.float64)
                                    )
                                ])
                            ),

                        ]))
                ])
            )
        ]

        self._quantities = [
            Quantity('program_version', r'I qbox (\S+)', dtype=str),
            Quantity('start_time', r'\<start_time\> (\d\d\d\d\-\d\d\-\d\dT\d\d:\d\d:\d\dZ)', dtype=str),
            Quantity('end_time', r'\<end_time\> (\d\d\d\d\-\d\d\-\d\dT\d\d:\d\d:\d\dZ)', dtype=str),
            Quantity('x_qbox_nodename', r'\<nodename\> (.+) \<\/nodename\>', dtype=str, flatten=False),
            Quantity('x_qbox_loading_xml_file', r'LoadCmd: loading from (\S+)', dtype=str),
            Quantity(
                'run',
                r'(\[qbox\] \<cmd\>[\s\S]+?\<timing name=\" +charge_vft.+)',
                repeats=True, sub_parser=TextParser(quantities=run_quantities)
            )
        ]


class QboxParser(FairdiParser):
    def __init__(self):
        super().__init__(
            name='parsers/qbox', code_name='qbox', code_homepage='http://qboxcode.org/',
            domain='dft', mainfile_mime_re=r'(application/xml)|(text/.*)',
            mainfile_contents_re=(r'http://qboxcode.org')
        )
        self.out_parser = QboxXMLParser()
        self._xc_map = {
            'LDA': ['LDA_X', 'LDA_C_PZ'],
            'VMN': ['LDA_X', 'LDA_C_VWN'],
            'PBE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'PBE0': ['GGA_X_PBE', 'GGA_C_PBE'],
            'B3LYP': ['HYB_GGA_XC_B3LYP5']
        }

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger

    def parse_run(self, index):
        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name='qbox', version=self.out_parser.get('program_version'))

        def format_time(time):
            if time is not None:
                return datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z').timestamp()

        sec_run.time_run = TimeRun(
            date_start=format_time(self.out_parser.start_time),
            date_end=format_time(self.out_parser.end_time))

        sec_method = sec_run.m_create(Method)
        parameters = {key: val for key, val in self.out_parser.run[index].get('parameter', [])}
        sec_method.x_qbox_input_parameters = parameters
        if parameters.get('xc') is not None:
            sec_method.dft = DFT(xc_functional=XCFunctional())
            for xc_functional in self._xc_map.get(parameters['xc'], []):
                if '_X_' in xc_functional or xc_functional.endswith('_X'):
                    sec_method.dft.xc_functional.exchange.append(Functional(name=xc_functional))
                elif '_C_' in xc_functional or xc_functional.endswith('_C'):
                    sec_method.dft.xc_functional.correlation.append(Functional(name=xc_functional))
                elif 'HYB' in xc_functional:
                    sec_method.dft.xc_functional.hybrid.append(Functional(name=xc_functional))
                else:
                    sec_method.dft.xc_functional.contributions.append(Functional(name=xc_functional))

        def symmetrize_stress(stress):
            if not stress:
                return
            symmetrized = np.zeros((3, 3))
            symmetrized[0][0] = stress[0]
            symmetrized[1][1] = stress[1]
            symmetrized[2][2] = stress[2]
            symmetrized[0][1] = symmetrized[1][0] = stress[3]
            symmetrized[1][2] = symmetrized[2][1] = stress[4]
            symmetrized[0][2] = symmetrized[2][0] = stress[5]
            return symmetrized * ureg.GPa

        for iteration in self.out_parser.run[index].get('iteration', []):
            sec_scc = sec_run.m_create(Calculation)
            sec_scc.energy = Energy()
            sec_system = sec_run.m_create(System)
            sec_scc.system_ref = sec_system

            for key, val in iteration.items():
                if key.startswith('energy_') and val is not None:
                    setattr(sec_scc.energy, key.replace('energy_', ''), EnergyEntry(value=val))

            if iteration.stress_tensor is not None:
                sec_stress = sec_scc.m_create(Stress)
                for contribution in iteration.stress_tensor.get('contribution', []):
                    value = symmetrize_stress(contribution.get('value', []))
                    if contribution.kind is None or contribution.kind == 'ks':
                        sec_stress.total = StressEntry(value=value)
                    else:
                        sec_stress.contributions.append(StressEntry(
                            kind=contribution.kind,
                            value=value
                        ))

            if iteration.multipole is not None:
                sec_multipoles = sec_scc.m_create(Multipoles)
                for multipole in iteration.multipole:
                    # TODO add contributions
                    for dipole in multipole.get('dipole', []):
                        if dipole[0] == 'total':
                            sec_multipoles.dipole = MultipolesEntry(total=np.array(dipole[1:], dtype=np.float64))
                    for quadrupole in multipole.get('quadrupole', []):
                        if quadrupole[0] == 'total':
                            sec_multipoles.quadrupole = MultipolesEntry(total=np.array(quadrupole[1:], dtype=np.float64))

            if iteration.mlwf is not None:
                for center in iteration.mlwf.get('center', []):
                    sec_mlwf = sec_scc.m_create(x_qbox_section_MLWF)
                    sec_mlwf.x_qbox_geometry_MLWF_atom_positions = center[:3] * ureg.bohr
                    sec_mlwf.x_qbox_geometry_MLWF_atom_spread = center[3] * ureg.bohr

            for scf in iteration.get('scf', []):
                sec_scf = sec_scc.m_create(ScfIteration)
                sec_scf.energy = Energy(
                    total=EnergyEntry(value=scf.energy_total),
                    sum_eigenvalues=EnergyEntry(value=scf.energy_sum_eigenvalues))

            if iteration.atomset is not None:
                atoms = iteration.atomset.get('atom', [])
                sec_system.atoms = Atoms(
                    lattice_vectors=iteration.atomset.lattice_vectors,
                    positions=[atom.position for atom in atoms] * ureg.bohr,
                    labels=[atom.label for atom in atoms],
                    velocities=[atom.velocity for atom in atoms] * (ureg.bohr / ureg.atomic_unit_of_time))
                forces = [atom.force for atom in atoms]
                if forces:
                    sec_scc.forces = Forces(total=ForcesEntry(value=forces * (ureg.hartree / ureg.bohr)))

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.maindir = os.path.dirname(self.filepath)
        self.init_parser()

        for n in range(len(self.out_parser.get('run', []))):
            self.parse_run(n)
