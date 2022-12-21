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
import re

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, DFT, XCFunctional, Functional, BasisSet, Scf
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, ScfIteration
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization, MolecularDynamics
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2, GeometryOptimization as GeometryOptimization2,
    GeometryOptimizationMethod, MolecularDynamics as MolecularDynamics2
)

from .metainfo.nwchem import (
    x_nwchem_section_start_information, x_nwchem_section_qmd_step)


def fix_dfloat(val_in):
    return float(re.sub(r'[dD]([\-\+]*\d)', r'E\1', val_in))


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_float = r'[\d\.\-\+ED]+'

        def str_to_functional(val_in):
            val = [v.strip() for v in val_in.strip().rsplit('  ', 1)]
            if len(val) == 2:
                val = [val[0]] + val[1].split()

            return val

        def str_to_energy(val_in):
            separator = '=' if '=' in val_in else ':'
            val = [v.strip() for v in val_in.strip().split(separator)]
            return val[0], float(val[1]) * ureg.hartree

        def str_to_labels_positions(val_in):
            val = [v.strip().split() for v in val_in.strip().split('\n')]
            labels, positions = [], []
            for val_i in val:
                labels.append(val_i[1])
                positions.append(val_i[3: 6])
            positions = np.array(positions, dtype=np.dtype(np.float64))
            return labels, positions * ureg.angstrom

        def str_to_labels_positions_forces(val_in):
            val = np.transpose([v.split() for v in val_in.strip().split('\n')])
            labels = val[0]
            positions = np.transpose(np.array(val[2:5], dtype=np.dtype(np.float64)))
            forces = np.transpose(np.array(val[5:8], dtype=np.dtype(np.float64)))
            return labels, positions * ureg.bohr, forces * ureg.hartree / ureg.bohr

        geometry_quantities = [
            Quantity(
                'labels_positions',
                r'No\.\s*Tag\s*Charge\s*X\s*Y\s*Z[\s\-]+([\s\S]+?)\n *\n',
                str_operation=str_to_labels_positions, convert=False),
            Quantity(
                'lattice_vectors',
                r'a1\=\<([\d\.\- ]+)\>\s*'
                r'a2\=\<([\d\.\- ]+)\>\s*'
                r'a3\=\<([\d\.\- ]+)\>\s*',
                dtype=np.dtype(np.float64), shape=(3, 3), unit=ureg.bohr)
        ]

        dft_quantities = geometry_quantities + [
            Quantity(
                'general_info',
                r'General Information\s+\-+([\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'info',
                    r' +([\w\. ]+\s*\:\s*[\w\.\- ]+)',
                    str_operation=lambda x: [v.strip() for v in x.split(':')],
                    repeats=True)])),
            Quantity(
                'xc_info',
                r'XC Information\s+\-+([\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'functional',
                    r'(.+(?:Functional|Exchange|POtential).+)',
                    str_operation=str_to_functional, repeats=True)])),
            Quantity(
                'energy',
                rf'([\w \-\.]+ energy\s*=\s*{re_float})',
                str_operation=str_to_energy, repeats=True, convert=False),
            Quantity(
                'labels_positions_forces',
                r'atom\s*coordinates\s*gradient\s*x\s*y\s*z\s*x\s*y\s*z\s*([\s\S]+?\n *\n)',
                str_operation=str_to_labels_positions_forces, convert=False),
            Quantity(
                'qmd_info',
                r'QMD Run Information\s*\-+\s*([\s\S]+?)\n *\n',
                str_operation=lambda x: [[vi.strip() for vi in v.split(':')] for v in x.split('\n')],
                convert=False),
            Quantity(
                'self_consistency',
                r'convergence\s*iter\s*energy\s*DeltaE\s*RMS\-Dens\s*Diis\-err\s*time\s*'
                r'([\s\S]+?)\n *\n *\n',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        rf'd\=\s*\d+,ls=[\d\.]+,diis\s*\d+\s*({re_float})\s*({re_float})\s*{re_float}\s*{re_float}\s*({re_float})',
                        dtype=np.dtype(np.float64), repeats=True)])),
        ]

        dft_gradient_quantities = [
            Quantity(
                'labels_positions_forces',
                r'atom\s*coordinates\s*gradient\s*x\s*y\s*z\s*x\s*y\s*z\s*([\s\S]+?\n *\n)',
                str_operation=str_to_labels_positions_forces, convert=False),
            Quantity(
                'energy',
                r'\@ Step\s*Energy.+\s*\@[\-\s]+\@\s*(.+)'),
        ]

        pw_quantities = geometry_quantities + [
            Quantity(
                'energy',
                rf'([\w \-]+ energy\s*\:\s*{re_float})',
                str_operation=str_to_energy, repeats=True, convert=False),
            Quantity(
                'spin_S2',
                rf'\<S\^2\>\s*\=\s*({re_float})', dtype=np.float64),
            Quantity(
                'parameters',
                r'options\:\s*([\s\S]+?)\n *\n',
                str_operation=lambda x: [[vi.strip() for vi in v.split('=')] for v in x.split('\n')]),
            Quantity(
                'self_consistency',
                r'ITERATION STARTED([\s\S]+?)ITERATION ENDED',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        rf'\d+\s+({re_float}\s+{re_float})\s+{re_float}\n',
                        repeats=True, dtype=np.dtype(np.float64))])),
            Quantity('total_charge', rf'total charge\:\s*({re_float})', dtype=np.float64)
            # TODO add xc functionals cannot find mapping
        ]

        calculation_quantities = geometry_quantities + [
            Quantity(
                'dft',
                r'(DFT Module[\s\S]+?)(?:NWChem|\Z)',
                repeats=True, sub_parser=TextParser(quantities=dft_quantities)),
            Quantity(
                'dft_gradient',
                r'(DFT Gradient Module[\s\S]+?)(?:NWChem|\Z)',
                repeats=True, sub_parser=TextParser(quantities=dft_gradient_quantities)),
            Quantity(
                'pw',
                r'(PSPW Calculation[\s\S]+?)(?:\*\s*NWPW|\Z)',
                repeats=True, sub_parser=TextParser(quantities=pw_quantities))]

        self._quantities = [
            Quantity(
                'version',
                r'Northwest Computational Chemistry Package \(NWChem\) (.+)\n',
                flatten=False, convert=False),
            Quantity(
                'job_info',
                r'Job information\s*\-+\s*([\s\S]+?)\n *\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'info',
                    r'(\w.+?\s*\=\s*.+)',
                    str_operation=lambda x: [v.strip() for v in x.split('=')],
                    convert=False, repeats=True)])),
            Quantity(
                'input',
                r'(Input Module[\s\S]+? {30}NWChem)',
                sub_parser=TextParser(quantities=geometry_quantities)),
            Quantity(
                'single_point',
                r'(DFT Module\s+\-+[\s\S]+?)(?:GA Statistics for process|NWChem Input Module|\Z)',
                sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity(
                'geometry_optimization',
                r'(Geometry Optimization[\s\S]+?)(?:GA Statistics for process|NWChem Input Module|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters',
                        r'(maximum gradient threshold\s*\(gmax\)[\s\S]+?)\n *\n',
                        str_operation=lambda x: [[vi.strip() for vi in v.split('=')] for v in x.split('\n')]),
                    Quantity(
                        'iteration',
                        r'p\s+\d+\s*\-+\s*(Geometry[\s\S]+?(?:\-+\s*Ste|\Z))',
                        repeats=True, sub_parser=TextParser(quantities=calculation_quantities))])),
            Quantity(
                'molecular_dynamics',
                r'(QMD Module[\s\S]+?)(?:GA Statistics for process|NWChem Input Module|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters',
                        r'QMD Run Parameters\s*\-+\s*([\s\S]+?)\n *\n',
                        str_operation=lambda x: [[vi.strip() for vi in v.split(':')] for v in x.split('\n')]),
                    Quantity(
                        'iteration',
                        r'(DFT Module[\s\S]+?(?:NWChem|\Z))',
                        repeats=True, sub_parser=TextParser(quantities=calculation_quantities))])),
            Quantity(
                'pw',
                r'(PSPW Calculation[\s\S]+?)(?:\*\s*NWPW|GA Statistics for process|\Z)',
                repeats=True, sub_parser=TextParser(quantities=pw_quantities))
            # TODO implement frequency analysis
            # TODO add timings
        ]


class NWChemParser:
    def __init__(self):
        self.out_parser = OutParser()

        self._metainfo_map = {
            'hostname': 'run_host_name', 'program': 'program_name', 'date': 'start_datetime',
            'compiled': 'compilation_datetime', 'nwchem branch': 'branch',
            'nwchem revision': 'revision', 'input': 'input_filename', 'prefix': 'input_prefix',
            'data base': 'db_filename', 'Charge': 'total_charge',
            'Spin multiplicity': 'spin_target_multiplicity',
            'Maximum number of iterations': 'scf_max_iteration',
            'Convergence on energy requested': 'scf_threshold_energy_change',
            'Total DFT energy': 'energy_total', 'One electron energy': 'x_nwchem_energy_one_electron',
            'Coulomb energy': 'energy_coulomb', 'Exchange energy': 'energy_exchange',
            'Exchange-Corr. energy': 'energy_XC',
            'Correlation energy': 'energy_correlation', 'Nuclear repulsion energy': 'energy_nuclear_repulsion',
            'total     energy': 'energy_total', 'exc-corr  energy': 'energy_XC',
            # TODO verify if energy contributions mapping is correct
            # 'total orbital energy': 'energy_sum_eigenvalues'
            'hartree   energy': 'energy_correction_hartree',
            'ion-ion   energy': 'energy_nuclear_repulsion',
            'No. of nuclear steps': 'qmd_number_of_nuclear_steps',
            'Nuclear time step': 'qmd_nuclear_time_step',
            'Target temp. (K)': 'qmd_target_temperature', 'Thermostat': 'qmd_thermostat',
            'Tau': 'qmd_tau', 'Random seed': 'qmd_random_seed',
            'Nuclear integrator': 'qmd_nuclear_integrator', 'Current temp. (K)': 'qmd_initial_temperature',
            'electron spin': 'electron_spin_restriction'}

        self._xc_functional_map = {
            'B3LYP Method XC Potential': 'HYB_GGA_XC_B3LYP',
            'PBE0 Method XC Functional': 'HYB_GGA_XC_PBEH',
            'Becke half-and-half Method XC Potential': 'HYB_GGA_XC_BHANDH',
            'HCTH120  Method XC Functional': 'GGA_XC_HCTH_120',
            'HCTH147  Method XC Functional': 'GGA_XC_HCTH_147',
            'HCTH407 Method XC Functional': 'GGA_XC_HCTH_407',
            'PerdewBurkeErnzerhof Exchange Functional': 'GGA_X_PBE',
            'Becke 1988 Exchange Functional': 'GGA_X_B88',
            'Lee-Yang-Parr Correlation Functional': 'GGA_C_LYP',
            'Perdew 1986 Correlation Functional': 'GGA_C_P86',
            'Perdew 1991 Correlation Functional': 'GGA_C_PW91',
            'Perdew 1991   Exchange Functional': 'GGA_X_PW91',
            'Hartree-Fock (Exact) Exchange': 'HF_X',
            'TPSS metaGGA Exchange Functional': 'MGGA_X_TPSS',
            'TPSS03 metaGGA Correlation Functional': 'MGGA_C_TPSS',
            'Slater Exchange Functional': 'LDA_X',
            'VWN V Correlation Functional': 'LDA_C_VWN',
            'OPTX     Exchange Functional_1.432_non-local+Slater Exchange Functional_1.052_local': 'GGA_X_OPTX',
            'Perdew 1991 LDA Correlation Functional_1.000_local+PerdewBurkeErnz. Correlation Functional_1.000_non-local': 'GGA_C_PBE',
            'Perdew 1981 Correlation Functional_1.000_local+Perdew 1986 Correlation Functional_1.000_non-local': 'GGA_C_P86',
            'Perdew 1991 Correlation Functional_1.000_non-local+Perdew 1991 LDA Correlation Functional_1.000_local': 'GGA_C_PW91'
        }

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger

    def parse_system(self, source):
        sec_system = self.archive.run[0].m_create(System)

        labels, positions = source.get('labels_positions', [[], []])
        if len(positions) == 0:
            dft = source.get('dft', [{}])[-1]
            dft_gradient = source.get('dft_gradient', [{}])[-1]
            labels_positions = dft.get('labels_positions_forces', dft_gradient.get('labels_positions_forces'))
            if labels_positions is not None:
                labels, positions = labels_positions[:2]

        if len(positions) == 0:
            labels, positions = self.out_parser.get('input', {}).get('labels_positions', [[], []])

        sec_atoms = sec_system.m_create(Atoms)
        sec_atoms.labels = labels
        sec_atoms.positions = positions

        lattice_vectors = source.get('lattice_vectors')
        if lattice_vectors is not None:
            sec_atoms.lattice_vectors = lattice_vectors
            sec_atoms.periodic = [True, True, True]
        else:
            sec_atoms.periodic = [False, False, False]

        return sec_system

    def parse_scc(self, source):
        sec_scc = self.archive.run[0].m_create(Calculation)

        # we only read the results from the last dft and gradients module
        dft = source.get('dft', [{}])[-1]
        dft_gradient = source.get('dft_gradient', [{}])[-1]

        # energies
        sec_energy = sec_scc.m_create(Energy)
        for key, val in source.get('energy', dft.get('energy', [])):
            key = self._metainfo_map.get(key)
            if key is not None:
                if key.startswith('x_nwchem_energy_'):
                    setattr(sec_scc, key, val.to('J').magnitude)
                else:
                    sec_energy.m_add_sub_section(getattr(
                        Energy, key.replace('energy_', '').lower()), EnergyEntry(value=val))

        # for geometry optimization, energy can also be parsed from gradient module
        energy = dft_gradient.get('energy')
        if energy is not None:
            sec_energy.total = EnergyEntry(value=energy[1] * ureg.hartree)
            sec_scc.time_calculation = energy[-1]

        # forces
        forces = dft_gradient.get('labels_positions_forces', dft.get('labels_positions_forces'))
        if forces is not None:
            sec_scc.forces = Forces(total=ForcesEntry(value=forces[2]))

        # spin
        spin_S2 = source.get('spin_S2')
        if spin_S2 is not None:
            sec_scc.spin_S2 = spin_S2

        # md properties
        qmd_info = dft.get('qmd_info')
        if qmd_info is not None:
            sec_qmd = sec_scc.m_create(x_nwchem_section_qmd_step)
            for key, val in qmd_info:
                val = val.split()
                if key == 'Time elapsed (fs)':
                    sec_qmd.x_nwchem_qmd_step_time = float(val[0]) * ureg.fs
                elif key == 'Kin. energy (a.u.)':
                    sec_qmd.x_nwchem_qmd_step_kinetic_energy = float(val[1]) * ureg.hartree
                elif key == 'Pot. energy (a.u.)':
                    sec_qmd.x_nwchem_qmd_step_potential_energy = float(val[1]) * ureg.hartree
                elif key == 'Tot. energy (a.u.)':
                    sec_qmd.x_nwchem_qmd_step_total_energy = float(val[1]) * ureg.hartree
                elif key == 'Target temp. (K)':
                    sec_qmd.x_nwchem_qmd_step_target_temperature = float(val[1]) * ureg.kelvin
                elif key == 'Current temp. (K)':
                    sec_qmd.x_nwchem_qmd_step_temperature = float(val[1]) * ureg.kelvin
                elif key == 'Dipole (a.u.)':
                    sec_qmd.x_nwchem_qmd_step_dipole = [float(v) for v in val[1:4]]

        # self consistency
        scf = dft.get('self_consistency', source.get('self_consistency'))
        if scf is not None:
            for iteration in scf.get('iteration', []):
                sec_scf = sec_scc.m_create(ScfIteration)
                sec_scf_energy = sec_scf.m_create(Energy)
                iteration = [fix_dfloat(i) if isinstance(i, str) else i for i in iteration]
                sec_scf_energy.total = EnergyEntry(value=iteration[0] * ureg.hartree)
                sec_scf_energy.change = iteration[1] * ureg.hartree
                if len(iteration) > 2:
                    sec_scf.time_calculation = iteration[2]

        return sec_scc

    def parse_method(self, source):
        sec_method = self.archive.run[0].m_create(Method)

        def resolve_functional_combination(functionals):
            names = []
            for f_a in functionals:
                name = self._xc_functional_map.get(f_a[0])
                if name is not None:
                    names.append([name, None])
                    if len(f_a) > 1:
                        names[-1][1] = f_a[1]
                for f_b in functionals:
                    if len(f_a) < 3 or len(f_b) < 3:
                        continue
                    combination = '+'.join(['%s_%1.3f_%s' % tuple(f) for f in [f_a, f_b]])
                    name = self._xc_functional_map.get(combination)
                    if name is not None:
                        names.append([name, None])
            return names

        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)
        sec_electronic.method = 'DFT'

        dft = source.get('dft', [{}])[-1]

        general_info = dft.get('general_info', {})
        sec_scf = sec_method.m_create(Scf)
        for key, val in general_info.get('info', []):
            key = self._metainfo_map.get(key)
            if key is None:
                continue
            if key == 'scf_threshold_energy_change':
                val = fix_dfloat(val) * ureg.hartree
                sec_scf.threshold_energy_change = val
            elif key == 'scf_max_iteration' and isinstance(val, int):
                sec_scf.n_max_iteration = val
            else:
                setattr(sec_method, key, val)

        xc_functionals = dft.get('xc_info', {}).get('functional', [])
        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for name, weight in resolve_functional_combination(xc_functionals):
            functional = Functional(name=name)
            if weight is not None:
                functional.weight = weight
            if '_X_' in name or name.endswith('_X'):
                sec_xc_functional.exchange.append(functional)
            elif '_C_' in name or name.endswith('_C'):
                sec_xc_functional.correlation.append(functional)
            elif 'HYB' in name:
                sec_xc_functional.hybrid.append(functional)
            else:
                sec_xc_functional.contributions.append(functional)

        parameters = source.get('parameters', [])
        for parameter in parameters:
            key = self._metainfo_map.get(parameter[0])
            if len(parameter) == 2 and key is not None:
                setattr(sec_method, 'x_nwchem_%s' % key, parameter[1])

        total_charge = source.get('total_charge')
        if total_charge is not None:
            sec_electronic.charge = total_charge

        sec_basis = sec_method.m_create(BasisSet)
        sec_basis.type = 'plane waves' if self.out_parser.get('pw') is not None else 'gaussians'

        return sec_method

    def parse_configurations(self):

        def parse_calculation(source):
            sec_method = self.parse_method(source)
            sec_system = self.parse_system(source)
            sec_scc = self.parse_scc(source)
            sec_scc.method_ref = sec_method
            sec_scc.system_ref = sec_system

        if self.out_parser.get('geometry_optimization') is not None:
            for iteration in self.out_parser.get('geometry_optimization').get('iteration', []):
                parse_calculation(iteration)

        elif self.out_parser.get('molecular_dynamics') is not None:
            for iteration in self.out_parser.get('molecular_dynamics').get('iteration', []):
                parse_calculation(iteration)

        elif self.out_parser.get('pw') is not None:
            for calculation in self.out_parser.get('pw'):
                parse_calculation(calculation)

        elif self.out_parser.get('single_point') is not None:
            parse_calculation(self.out_parser.get('single_point'))

    def parse_workflow(self):
        sec_workflow = self.archive.m_create(Workflow)

        workflow = None
        parameters = []
        if self.out_parser.get('geometry_optimization') is not None:
            sec_workflow.type = 'geometry_optimization'
            parameters = self.out_parser.get('geometry_optimization').get('parameters', [])
            workflow = GeometryOptimization2(method=GeometryOptimizationMethod())

        elif self.out_parser.get('molecular_dynamics') is not None:
            sec_workflow.type = 'molecular_dynamics'
            parameters = self.out_parser.get('molecular_dynamics').get('parameters', [])
            workflow = MolecularDynamics2()

        elif self.out_parser.get('pw') is not None:
            # pw is not fully implemented as I do not have example files
            sec_workflow.type = 'geometry_optimization' if len(
                self.out_parser.get('pw')) > 1 else 'single_point'
            workflow = GeometryOptimization2() if len(
                self.out_parser.get('pw')) > 1 else SinglePoint2()

        elif self.out_parser.get('single_point') is not None:
            sec_workflow.type = 'single_point'
            workflow = SinglePoint2()

        sec_geometry_opt = sec_workflow.m_create(GeometryOptimization)
        sec_md = sec_workflow.m_create(MolecularDynamics)
        for parameter in parameters:
            if len(parameter) != 2:
                continue
            if parameter[0] == 'maximum gradient threshold         (gmax)':
                val = fix_dfloat(parameter[1]) if isinstance(parameter[1], str) else parameter[1]
                sec_geometry_opt.convergence_tolerance_force_maximum = val * ureg.hartree / ureg.bohr
                workflow.method.convergence_tolerance_force_maximum = val * ureg.hartree / ureg.bohr
            elif parameter[0] == 'maximum cartesian step threshold   (xmax)':
                val = fix_dfloat(parameter[1]) if isinstance(parameter[1], str) else parameter[1]
                sec_geometry_opt.convergence_tolerance_displacement_maximum = val * ureg.bohr
                workflow.method.convergence_tolerance_displacement_maximum = val * ureg.bohr
            elif parameter[0] == 'energy precision                  (eprec)':
                val = fix_dfloat(parameter[1]) if isinstance(parameter[1], str) else parameter[1]
                sec_geometry_opt.input_energy_difference_tolerance = val * ureg.hartree
                workflow.method.convergence_tolerance_energy_difference = val * ureg.hartree
            else:
                parameter[0] = self._metainfo_map.get(parameter[0])
                if parameter[0] is not None:
                    setattr(sec_md, 'x_nwchem_%s' % parameter[0], parameter[1])

        self.archive.workflow2 = workflow

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        sec_run = self.archive.m_create(Run)

        sec_run.program = Program(name='NWChem', version=self.out_parser.get('version', ''))

        # job information
        sec_info = sec_run.m_create(x_nwchem_section_start_information)
        for key, val in self.out_parser.get('job_info', {}).get('info', []):
            if val is None:
                continue
            key = self._metainfo_map.get(key, key.replace(' ', '_'))
            setattr(sec_info, 'x_nwchem_%s' % key, val)

        self.parse_configurations()

        self.parse_workflow()
