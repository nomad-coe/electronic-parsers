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

from nomad.units import ureg
from nomad.parsing.file_parser.text_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    Method, DFT, XCFunctional, Functional, Electronic, BasisSet)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Dos, DosValues, Energy, EnergyEntry, Forces, ForcesEntry)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_float = r'[\d\.\-\+Ee]+'

        def str_to_labels_positions(val_in):
            val = np.transpose([v.split() for v in val_in.strip().split('\n')])
            return val[1], np.array(val[2:5].T, dtype=np.dtype(np.float64)) * ureg.bohr

        calculation_quantities = [
            Quantity(
                'labels_positions',
                r' Index Symbol\s*x\s*\(bohr\).+([\s\S]+?)\n *\n',
                convert=False, str_operation=str_to_labels_positions),
            Quantity(
                'lattice_vectors',
                r'Lattice vectors \(bohr\)\s*([\s\S]+?)\n *\n',
                convert=False,
                str_operation=lambda x: np.array(
                    [v.split()[1:4] for v in x.strip().split('\n')], dtype=np.dtype(np.float64))),
            Quantity(
                'total_charge',
                rf'Total System Charge\s*({re_float})', dtype=float, unit=ureg.elementary_charge),
            Quantity(
                'band_engine_input',
                r'Band Engine Input\s*\-+\s*([\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[
                    Quantity('basis', r' Basis\s*Type\s*(.+)')])),
            Quantity(
                'model_parameters',
                r'M O D E L   P A R A M E T E R S\s*\=+([\s\S]+?)\={10}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'dft_potential',
                        r'FUNCTIONAL POTENTIAL \(scf\)([\s\S]+?)DENSITY',
                        sub_parser=TextParser(quantities=[
                            Quantity('LDA', r'LDA\:\s*([\w ]+)', flatten=False),
                            Quantity('GGA', r'Gradient Corrections\:\s*([\w ]+)', flatten=False),
                            Quantity('MGGA', r'Meta-GGA\:\s*([\w ]+)', flatten=False)])),
                    Quantity(
                        'spin',
                        r'SPIN\s*\(restricted.+\s*.+\:\s*(\w+)')])),
            Quantity(
                'fermi_energy',
                rf'Fermi Energy\:\s*({re_float})\s*a\.u\.', dtype=float, unit=ureg.hartree),
            Quantity(
                'energies',
                r'E N E R G Y   A N A L Y S I S([\s\S]+?)\={90}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'kinetic_electronic',
                        rf'Kinetic\s*({re_float})', dtype=float, unit=ureg.hartree),
                    Quantity(
                        'xc',
                        rf'XC\s*({re_float})', dtype=float, unit=ureg.hartree),
                    Quantity(
                        'electrostatic',
                        rf'Electrostatic\s*({re_float})', dtype=float, unit=ureg.hartree),
                    Quantity(
                        'total',
                        rf'Final bond energy \(.+\)\s*({re_float})', dtype=float, unit=ureg.hartree)])),
            Quantity(
                'energy_total',
                rf'Energy\s*\(hartree\)\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'atom_forces',
                r'FINAL GRADIENTS([\s\S]+?)\n *\n',
                convert=False, str_operation=lambda x: np.array(
                    [v.split()[2:5] for v in x.strip().split('\n')],
                    dtype=np.dtype(np.float64)) * ureg.hartree / ureg.bohr),
            Quantity(
                'self_consistency',
                r'S C F   P R O C E D U R E\s*\*\s*\*+\s*([\s\S]+?Self consistent error.+)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_change',
                        rf'cyc\=\s*\d+\s*err\=\s*({re_float})',
                        repeats=True, dtype=float, unit=ureg.hartree)])),
            Quantity(
                'total_dos',
                r'TOTALDOS([\s\S]+?)ENDINPUT',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'dos',
                        rf'\n *({re_float}) *({re_float}) *({re_float})*',
                        dtype=np.dtype(np.float64), repeats=True)]))
            # TODO add code specific metainfo
        ]

        self._quantities = [
            Quantity('program_version', r'\*\s*r(\d+ \d{4}\-\d\d\-\d\d)', flatten=False),
            Quantity('time_start', r'RunTime\:\s*(\w{3}\d+\-\d{4}\s*\d+\:\d+\:\d+)', flatten=False),
            Quantity(
                'single_point',
                r'SINGLE POINT CALCULATION \*([\s\S]+?)(:?Timing|\Z)',
                sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity(
                'geometry_optimization',
                r'GEOMETRY OPTIMIZATION\s*\*([\s\S]+?)(:?Timing|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        r'Geometry Convergence after Step\s*([\s\S]+?(?:dE\(predicted\)\:.+|\Z))',
                        repeats=True, sub_parser=TextParser(quantities=calculation_quantities)),
                    Quantity(
                        'geometry_optimization_method',
                        r'Optimization Method\s*(.+)', flatten=False),
                    Quantity(
                        'geometry_optimization_threshold_force',
                        rf'Maximum gradient\s*({re_float})',
                        dtype=float, unit=ureg.hartree / ureg.bohr),
                    Quantity(
                        'geometry_optimization_energy_change',
                        rf'Maximum energy change allowe\s*({re_float})',
                        dtype=float, unit=ureg.hartree),
                    Quantity(
                        'geometry_optimization_geometry_change',
                        rf'Maximum step allowed\s*({re_float})',
                        dtype=float, unit=ureg.bohr)]))
            # TODO add other calculation types
        ]


class BandParser:
    def __init__(self):
        self.out_parser = OutParser()

    def init_parser(self):
        self.out_parser.mainfile = self.mainfile
        self.out_parser.logger = self.logger

    def parse_configurations(self):
        sec_run = self.archive.run[0]

        def parse_scc(source):
            sec_scc = sec_run.m_create(Calculation)

            # total energy
            sec_energy = sec_scc.m_create(Energy)
            if source.get('energy_total') is not None:
                sec_energy.total = EnergyEntry(value=source.get('energy_total'))

            # energy contributions
            for key, val in source.get('energies', {}).items():
                if val is not None:
                    setattr(sec_energy, key, EnergyEntry(value=val))

            # atom forces
            if source.get('atom_forces') is not None:
                sec_forces = sec_scc.m_create(Forces)
                sec_forces.total = ForcesEntry(value=source.get('atom_forces'))

            # self consistency
            for energy_change in source.get('self_consistency', {}).get('energy_change', []):
                sec_scf = sec_scc.m_create(ScfIteration)
                sec_scf_energy = sec_scf.m_create(Energy)
                sec_scf_energy.change = energy_change

            # dos
            total_dos = source.get('total_dos', {}).get('dos')
            if total_dos is not None:
                total_dos = np.transpose(total_dos)
                sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
                sec_dos.energies = total_dos[0] * ureg.hartree
                total_dos = total_dos[1:]
                for spin in range(len(total_dos)):
                    sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
                    sec_dos_values.spin = spin
                    sec_dos_values.value = total_dos[spin] * (1 / ureg.hartree)

            return sec_scc

        def parse_system(source):
            sec_system = sec_run.m_create(System)

            sec_atoms = sec_system.m_create(Atoms)
            labels_positions = source.get('labels_positions')
            if labels_positions is not None:
                sec_atoms.labels = labels_positions[0]
                sec_atoms.positions = labels_positions[1]

            lattice_vectors = source.get('lattice_vectors')
            if lattice_vectors is not None:
                lattice_vectors = list(lattice_vectors)
                pbc = [True, True, True]
                for n in range(len(lattice_vectors), 3):
                    lattice_vectors.append([0, 0, 0])
                    pbc[n] = False
                sec_atoms.lattice_vectors = lattice_vectors * ureg.bohr
                sec_atoms.periodic = pbc

            return sec_system

        def parse_method(source):
            sec_method = sec_run.m_create(Method)
            sec_method.basis_set.append(BasisSet(type='numeric AOs'))
            sec_dft = sec_method.m_create(DFT)

            dft_potential = source.get('model_parameters', {}).get('dft_potential', {})
            # TODO provide mapping
            sec_xc_functional = sec_dft.m_create(XCFunctional)
            for xc_type in ['LDA', 'GGA', 'MGGA']:
                functionals = dft_potential.get(xc_type, '').split()
                kind = ['XC'] if len(functionals) == 1 else ['X', 'C']
                for n, functional in enumerate(functionals):
                    functional = functional.rstrip('x').rstrip('c').upper()
                    if kind[n] == 'X':
                        sec_xc_functional.exchange.append(
                            Functional(name='%s_%s_%s' % (xc_type, kind[n], functional)))
                    elif kind[n] == 'C':
                        sec_xc_functional.correlation.append(
                            Functional(name='%s_%s_%s' % (xc_type, kind[n], functional)))
                    else:
                        sec_xc_functional.contributions.append(
                            Functional(name='%s_%s_%s' % (xc_type, kind[n], functional)))

            sec_electronic = sec_method.m_create(Electronic)
            spin = source.get('model_parameters', {}).get('spin')
            sec_electronic.n_spin_channels = 2 if spin == ('UNrestricted') else 1

            if source.get('total_charge') is not None:
                sec_electronic.charge = source.total_charge

            return sec_method

        def parse_calculation(source):
            if source is None:
                return

            sec_scc = parse_scc(source)
            sec_system = parse_system(source)
            sec_method = parse_method(source)
            sec_scc.system_ref = sec_system
            sec_scc.method_ref = sec_method

        parse_calculation(self.out_parser.get('single_point'))

        geometry_opt = self.out_parser.get('geometry_optimization')
        if geometry_opt is not None:
            sec_workflow = self.archive.m_create(Workflow)
            sec_workflow.type = 'geometry_optimization'
            sec_geometry_opt = sec_workflow.m_create(GeometryOptimization)
            sec_geometry_opt.method = geometry_opt.get('geometry_optimization_method', '')
            sec_geometry_opt.input_force_maximum_tolerance = geometry_opt.get('geometry_optimization_threshold_force', 0)
            sec_geometry_opt.input_energy_difference_tolerance = geometry_opt.get('geometry_optimization_energy_change', 0)
            sec_geometry_opt.input_displacement_maximum_tolerance = geometry_opt.get('geometry_optimization_geometry_change', 0)

            for iteration in geometry_opt.get('iteration', []):
                parse_calculation(iteration)

    def parse(self, filepath, archive, logger):
        self.mainfile = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name='BAND', version=self.out_parser.get('program_version', ''))

        if self.out_parser.get('time_start') is not None:
            dt = datetime.strptime(self.out_parser.time_start, '%b%d-%Y %H:%M:%S') - datetime(1970, 1, 1)
            sec_run.time_run = TimeRun(date_start=dt.total_seconds())

        self.parse_configurations()
