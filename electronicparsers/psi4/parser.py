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
from datetime import datetime
import numpy as np

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, BasisSet, BasisSetAtomCentered, Scf as ScfMethod, DFT,
    XCFunctional, Functional)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, ScfIteration, BandEnergies,
    Multipoles, MultipolesEntry, Charges, ChargesValue)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2,
    GeometryOptimization as GeometryOptimization2, GeometryOptimizationMethod
)
from .metainfo.psi4 import x_psi4_root_information
from .metainfo import m_env


class OutParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        re_f = r'-*\d+\.\d+[Ee]*[-+]*\d*'

        def str_to_basis(val_in):
            data = dict()
            for line in val_in.strip().split('\n'):
                line = line.split(':')
                if len(line) == 2:
                    data[line[0].strip()] = line[1].strip()
            return data

        def str_to_orbital_energies(val_in):
            val = val_in.strip().split()
            orbitals = [val[i] for i in range(0, len(val), 2)]
            energies = [float(val[i]) for i in range(1, len(val), 2)]
            return orbitals, energies

        def str_to_eigenvalues(val_in):
            orbital_energies = []
            for val in val_in.strip().split('\n'):
                if 'occupied orbitals' in val:
                    orbital_energies.append([[], []])
                elif 'Active orbitals' in val:
                    pass
                else:
                    val = val.strip().split()
                    if len(val) % 3 != 0:
                        continue
                    orbital_energies[-1][0].extend([val[i] for i in range(2, len(val), 3)])
                    orbital_energies[-1][1].extend([float(val[i]) for i in range(1, len(val), 3)])
            return orbital_energies

        def str_to_parameters(val_in):
            val_in = val_in.strip().split('\n')
            name = val_in[0].split()[0]
            parameters = dict()
            separator = '='
            if '=>' in val_in[-1]:
                separator = '=>'
            elif ':' in val_in[-1]:
                separator = ':'
            for val in val_in:
                val = [v.rstrip('!').strip() for v in val.split(separator)]
                if len(val) == 2:
                    try:
                        val[1] = float(val[1])
                    except Exception:
                        pass
                    if val[1] in ['TRUE', 'FALSE']:
                        val[1] = val[1] == 'TRUE'
                    parameters[val[0]] = val[1]
            return name, parameters

        charges_quantities = [
            Quantity(
                'atom',
                rf'\d+ +[A-Z][a-z]* +({re_f}) +({re_f}) +({re_f}) +({re_f})',
                repeats=True, dtype=np.dtype(np.float64)),
            Quantity(
                'total',
                rf'Total alpha = +({re_f}), Total beta = +({re_f}), Total charge = +({re_f})',
                dtype=np.dtype(np.float64))]

        properties_quantities = [
            Quantity(
                'multipole_moments',
                r'Multipole +Electric \(a\.u\.\) .+\s+\-+([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'dipole',
                        r'Dipole [XYZ] +: +(.+)',
                        repeats=True, dtype=np.dtype(np.float64)),
                    Quantity(
                        'quadrupole',
                        r'Quadrupole [XYZ]{2} +: +(.+)',
                        repeats=True, dtype=np.dtype(np.float64)),
                    Quantity(
                        'octupole',
                        r'Octupole [XYZ]{3} +: +(.+)',
                        repeats=True, dtype=np.dtype(np.float64)),
                    Quantity(
                        'hexadecapole',
                        r'Hexadecapole [XYZ]{4} +: +(.+)',
                        repeats=True, dtype=np.dtype(np.float64)),
                    Quantity(
                        'npole',
                        r'32-pole [XYZ]{5} +: +(.+)',
                        repeats=True, dtype=np.dtype(np.float64))
                ])
            ),
            Quantity(
                'nuclear_dipole_moment',
                rf'Nuclear Dipole Moment: \(a\.u\.\)\s+X: +({re_f}) +Y: +({re_f}) +Z: +({re_f})',
                dtype=np.dtype(np.float64)),
            Quantity(
                'electronic_dipole_moment',
                rf'Electronic Dipole Moment: \(a\.u\.\)\s+X: +({re_f}) +Y: +({re_f}) +Z: +({re_f})',
                dtype=np.dtype(np.float64)),
            Quantity(
                'total_dipole_moment',
                rf'Dipole Moment: \(a\.u\.\)\s+X: +({re_f}) +Y: +({re_f}) +Z: +({re_f})',
                dtype=np.dtype(np.float64)),
            Quantity(
                'mulliken_charges',
                r'Mulliken Charges: \(a\.u\.\)\s+.+([\s\S]+?Total charge.+)',
                sub_parser=TextParser(quantities=charges_quantities)),
            Quantity(
                'lowdin_charges',
                r'Lowdin Charges: \(a\.u\.\)\s+.+([\s\S]+?Total charge.+)',
                sub_parser=TextParser(quantities=charges_quantities))
        ]

        scf_quantities = [
            Quantity(
                'geometry',
                r'Geometry <==([\s\S]+?)==>', sub_parser=TextParser(quantities=[
                    Quantity(
                        'atoms',
                        rf'([A-Z][a-z]* +{re_f} +{re_f} +{re_f} +{re_f}\n)',
                        repeats=True),
                    Quantity('molecular_point_group', r'Molecular point group: *(\w+)', dtype=str),
                    Quantity('full_point_group', r'Full point group: *(\w+)', dtype=str),
                    Quantity('symmetry', r'Running in (\w+) symmetry\.', dtype=str),
                    Quantity(
                        'rotational_constants',
                        rf'Rotational constants: *A = *({re_f}) *B = *({re_f}) *C = *({re_f}) \[cm\^-1\]',
                        dtype=np.dtype(np.float64)),
                    Quantity('nuclear_repulsion', rf'Nuclear repulsion = *({re_f})', dtype=np.float64),
                    Quantity('charge', r'Charge *= (\d+)', dtype=np.float64),
                    Quantity('multiplicity', r'Multiplicity *= (\d+)', dtype=np.float64),
                    Quantity('electrons', r'Electrons *= (\d+)', dtype=np.float64),
                    Quantity('nalpha', r'Nalpha *= (\d+)', dtype=np.float64),
                    Quantity('nbeta', r'Nbeta *= (\d+)', dtype=np.float64)])),
            Quantity(
                'algorithm',
                r'Algorithm <==([\s\S]+?)==>', sub_parser=TextParser(quantities=[
                    Quantity(
                        'minimization_algorithm',
                        r'SCF Algorithm Type is (.+)\.', dtype=str),
                    Quantity(
                        'x_psi4_diis',
                        r'DIIS (.+)\.', str_operation=lambda x: x == 'enabled'),
                    Quantity(
                        'x_psi4_mom',
                        r'MOM (.+)\.', str_operation=lambda x: x == 'enabled'),
                    Quantity(
                        'x_psi4_fractional_occupation',
                        r'Fractional occupation (.+)\.', str_operation=lambda x: x == 'enabled'),
                    Quantity(
                        'x_psi4_guess_type',
                        r'Guess Type is (.+)\.', dtype=str),
                    Quantity(
                        'threshold_energy_change',
                        rf'Energy threshold += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity(
                        'threshold_densDFT Potential <==ty_change',
                        rf'Density threDFT Potential <==hold += +({re_f})', dtype=np.float64),
                    Quantity(
                        'x_psi4_integral_threshold',
                        rf'Integral threshold += +({re_f})', dtype=np.float64)])),
            Quantity(
                'basis',
                r'(?:Primary )*Basis (?:Set )*<==([\s\S]+?)==>',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'basis_set',
                        r'((?:Basis Set|Core potential|AO BASIS SET INFORMATION):[\s\S]+?\n\n)',
                        repeats=True, str_operation=str_to_basis)])),
            Quantity(
                'jk_matrices',
                r'(J/K Matrices <==[\s\S]+?==>)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters',
                        r'J/K Matrices <==\s+([\s\S]+?\n *\n)', str_operation=str_to_parameters),
                ])
            ),
            # Move auxiliary out of the parent section because I cannot cover all
            Quantity(
                'auxiliary_basis',
                r' Auxiliary Basis (?:Set )*<=([\s\S]+?)==>',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'basis_set',
                    r'((?:Basis Set|Core potential|AO BASIS SET INFORMATION):[\s\S]+?\n\n)',
                    repeats=True, str_operation=str_to_basis)])),
            Quantity(
                'dft_potential',
                r'DFT Potential <==([\s\S]+?==>)', sub_parser=TextParser(quantities=[
                    Quantity(
                        'composite',
                        r'Composite Functional.+([\s\S]+?)=>', str_operation=str_to_parameters),
                    Quantity(
                        'exact_exchange',
                        r'Exact \(HF\) Exchange <=([\s\S]+?)=>',
                        str_operation=lambda x: [v.split()[:2] for v in x.strip().split('\n')]),
                    Quantity(
                        'exchange',
                        r'Exchange Functionals <=([\s\S]+?)=>',
                        str_operation=lambda x: [v.split()[:2] for v in x.strip().split('\n')]),
                    Quantity(
                        'correlation',
                        r' Correlation Functionals <=([\s\S]+?)=>',
                        str_operation=lambda x: [v.split()[:2] for v in x.strip().split('\n')]),
                    Quantity(
                        'hybrid',
                        r'Exchange-Correlation Functionals <=([\s\S]+?)=>',
                        str_operation=lambda x: [v.split()[:2] for v in x.strip().split('\n')]),
                    Quantity(
                        'molecular_quadrature',
                        r'Molecular Quadrature <=([\s\S]+?)=>',
                        str_operation=str_to_parameters)])),
            Quantity(
                'method',
                r'(?:\n +(.+) Reference *\n|@(.+) Final Energy:)'),
            Quantity(
                'iterations',
                r'Iterations <==(\s+Total Energy[\s\S]+?)==>',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        rf'iter +\d+\: +({re_f}) +({re_f}) +({re_f})',
                        repeats=True, dtype=np.float64)])),
            Quantity(
                'spin_contamination_metric',
                rf'@Spin Contamination Metric: +({re_f})', dtype=np.float64),
            Quantity(
                's2_expected',
                rf'@S\^2 Expected: +({re_f})', dtype=np.float64),
            Quantity(
                's2_observed',
                rf'@S\^2 Observed: +({re_f})', dtype=np.float64),
            Quantity(
                's_expected',
                rf'@S   Expected: +({re_f})', dtype=np.float64),
            Quantity(
                's_observed',
                rf'@S   Observed: +({re_f})', dtype=np.float64),
            Quantity(
                'orbital_energies',
                r'(?:Occupied:|Virtual:).+([\s\S]+?\n *\n)',
                repeats=True, str_operation=str_to_orbital_energies),
            Quantity(
                'energy',
                r'Energetics <=([\s\S]+?Total Energy =.+)',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    rf'(.+) Energy = *({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])])),
            Quantity(
                'properties',
                r'(Properties will be evaluated at[\s\S]+?)(?:==>|tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=properties_quantities)),
            Quantity(
                'total_gradient',
                r'Total Gradient.+\s+Atom.+\s+\-.+\s+([\s\S]+?)\n *\n',
                str_operation=lambda x: np.array([v.split()[1:] for v in x.strip().split('\n')]),
                dtype=np.dtype(np.float64))]

        mp_quantities = [
            Quantity('method', r'(MP[\d\.]+)\s+Program'),
            Quantity(
                'energy',
                r'Computing MP[\d\.]+ energy using SCF MOs([\s\S]+?)\n *\n',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value', rf'\s+(.+?) (?:Energy|Contribution) (Correction )*\(a\.u\.\) *: +({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])]))
        ]

        method_quantities = [
            Quantity(
                'parameters',
                r'Parameters <==([\s\S]+?)==>', sub_parser=TextParser(quantities=[Quantity(
                    'key_value', r'([\w ]+= +\S+)',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.split('=')])])),
            Quantity(
                'iterations',
                r'Starting .+? iterations([\s\S]+?)==>',
                sub_parser=TextParser(quantities=[Quantity(
                    'iteration',
                    rf'@.+\d+: +\d+ +({re_f}) +({re_f}) +({re_f})(.+)',
                    repeats=True, dtype=np.dtype(np.float64))])),
            Quantity(
                'energy',
                r'Energetics <==([\s\S]+?Total.+)',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    rf'(.+) [Ee]nergy += *({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])])),
            Quantity(
                'root_info',
                r'(root \d+ information[\s\S]+?==>)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'root_energy',
                        rf'Root \d+ energy += +({re_f})',
                        dtype=np.float64, unit=ureg.hartree)])),
            # TODO parse other properties e.g. orbital extents, mayer bond indices
            Quantity(
                'properties',
                r'(erties computed using the[\s\S]+?)(?:==>|\n *Prop|tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=properties_quantities)),
        ]

        mcscf_quantities = [
            Quantity(
                'iterations',
                r'(Cycle +Energy.+\s+\=+[\s\S]+?)\={5}',
                sub_parser=TextParser(quantities=[Quantity(
                    'iteration',
                    rf'@SCF +\d+ +({re_f}) +({re_f}) +({re_f})',
                    repeats=True, dtype=np.dtype(np.float64))])),
            Quantity(
                'energy',
                r'\* (SCF total energy.+)',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    rf'(.+) energy += +({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])])),
            Quantity(
                'orbital_energies',
                r'Eigenvalues \(Eh\)([\s\S]+?)={5}', str_operation=str_to_eigenvalues)
        ]

        cc_quantities = [
            Quantity(
                'parameters',
                r'Wfn Parameters:\s+\-+\s+([\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    r'(.+ += +\S+)',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.split('=')])])),
            Quantity(
                'energy',
                r'(Nuclear Rep[\s\S]+?)\n *\n',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    rf'([\w\. \-]+) energy += +({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])]))
        ]

        cc_energy_quantities = [
            Quantity(
                'parameters',
                r'Input parameters:\s+\-+([\s\S]+?)',
                sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    r'(.+ += +\S+)',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.split('=')])])),
            Quantity(
                'iterations',
                r'(Iter +Energy[\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'iteration',
                    rf'\d+ +({re_f}) +({re_f}) +({re_f})',
                    repeats=True, dtype=np.dtype(np.float64))])),
            Quantity(
                'energy',
                r'\n *\n +(SCF energy[\s\S]+?CCSD total energy.+)',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    rf'([\w\. \-]+) energy.* += +({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])]))
        ]

        cc_lambda_quantities = [
            Quantity(
                'parameters',
                r'Input parameters:\s+\-+([\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    r'(.+ += +\S+)',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.split('=')])])),
            Quantity(
                'iterations',
                r'(Iter +PseudoEnergy[\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'iteration',
                    rf'\d+ +({re_f}) +({re_f})',
                    repeats=True, dtype=np.dtype(np.float64))])),
            Quantity(
                'energy',
                r'(Nuclear Rep\. energy[\s\S]+?Total CCSD energy.+)',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    rf'([\w\. \-]+) energy.* += +({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])]))
        ]

        cc_density_quantities = [
            Quantity(
                'parameters',
                r'Input parameters:\s+\-+([\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    r'(.+ += +\S+)',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.split('=')])])),
            Quantity(
                'energy',
                r'((?:Nuclear Rep\. energy|Energies re-computed from|Virial Theorem Data)[\s\S]+?)\n *\n',
                repeats=True, sub_parser=TextParser(quantities=[Quantity(
                    'key_value',
                    rf'([\w\. \-]+) energy(?: +\(.+\))* += +({re_f})',
                    repeats=True, str_operation=lambda x: [v.strip() for v in x.rsplit(' ', 1)])])),
            Quantity(
                'properties',
                r'(Properties will be evaluated at[\s\S]+?)(?:==>|tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=properties_quantities)),
        ]

        optking_quantities = [
            Quantity(
                'geometry',
                r'Geometry and Gradient-+\s+([\s\S]+?)\n *\n',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'atoms',
                        rf'([A-Z][a-z]*) +({re_f}) +({re_f}) +({re_f})', repeats=True),
                    Quantity(
                        'forces',
                        rf'({re_f}) +({re_f}) +({re_f})',
                        repeats=True, dtype=np.dtype(np.float64))])),
            Quantity(
                'convergence_criteria',
                rf'Convergence Criteria +({re_f}) +\* +({re_f}) +\* +\S+ +({re_f})',
                dtype=np.dtype(np.float64)),
            Quantity('energy', rf'~\s+\d+ +({re_f}) +({re_f})', dtype=np.float64)
        ]

        module_quantities = [
            Quantity(
                'scf',
                rf'(SCF\s+by[\s\S]+?(Computation Completed|tstop|\Z))',
                repeats=True, sub_parser=TextParser(quantities=scf_quantities)),
            Quantity(
                'scf_grad',
                r'(SCF GRAD\s+[\s\S]+?(?:tstop|\Z))',
                repeats=True, sub_parser=TextParser(quantities=scf_quantities)),
            Quantity(
                'mp',
                r'(MP[\d\.]+\s+Program[\s\S]+?(?:tstop|\Z))',
                repeats=True, sub_parser=TextParser(quantities=mp_quantities)),
            Quantity(
                'ci',
                r'(Configuration Interaction\s+\(a [\s\S]+?)(?:PASSED|tstart|\Z)',
                repeats=True, sub_parser=TextParser(quantities=method_quantities)),
            Quantity(
                'mcscf_detci',
                r'(Multi-Configurational Self-Consistent Field[\s\S]+?)(?:PASSED|tstart|\Z)',
                repeats=True, sub_parser=TextParser(quantities=method_quantities)),
            Quantity(
                'mcscf',
                r'(MCSCF: a self-consistent field program[\s\S]+?)(?:tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=mcscf_quantities)),
            Quantity(
                'cc',
                r'(Wfn Parameters:\s+\-+[\s\S]+?)(?:tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=cc_quantities)),
            Quantity(
                'cc_energy',
                r'(CCENERGY +\*[\s\S]+?)(?:tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=cc_energy_quantities)),
            Quantity(
                'cc_lambda',
                r'(CCLAMBDA +\*[\s\S]+?)(?:tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=cc_lambda_quantities)),
            Quantity(
                'cc_density',
                r'(CCDENSITY +\*[\s\S]+?)(?:tstop|\Z)',
                repeats=True, sub_parser=TextParser(quantities=cc_density_quantities)),
            Quantity(
                'optking',
                r'OPTKING .+?: for geometry optimizations([\s\S]+?)OPTKING Finished Execution',
                sub_parser=TextParser(quantities=optking_quantities)),
            Quantity(
                'options',
                r'Options:\s+\-+([\s\S]+?)\n *\n',
                str_operation=str_to_parameters),
            Quantity(
                'salc',
                r'(Cartesian Displacement SALCs[\s\S]+?)(?:tstart|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'total_gradient',
                        r'Total gradient:\s+Atom.+\s+.+\s+([\s\S]+?)\n *\n',
                        str_operation=lambda x: [v.split()[1:] for v in x.strip().split('\n')],
                        dtype=np.dtype(np.float64)),
                    Quantity(
                        'contributions_gradient',
                        r'\-(.+ (?:Energy 1st Derivatives|contribution to gradient)):'
                        r'\s+Atom.+\s+.+([\s\S]+?)\n *\n',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity('name', r'(.+) (?:Energy|contribution)', flatten=False),
                            Quantity(
                                'value',
                                rf'\d+ +({re_f}) +({re_f}) +({re_f})',
                                repeats=True, dtype=np.dtype(np.float64))]))])),
        ]

        self._quantities = [
            Quantity(
                'version',
                r'Psi4: An Open-Source Ab Initio Electronic Structure Package\s*'
                r'Psi4 ([\w\.]+)', dtype=str),
            Quantity('start_time', r'Psi4 started on: \w+, (.+)', flatten=False, dtype=str),
            Quantity('process_id', r'Process ID:\s*(\d+)', dtype=np.int32),
            Quantity('psidatadir', r'PSIDATADIR:\s*(.+)', dtype=str),
            Quantity('memory', r'Memory:\s*(\S+) MiB', dtype=np.float64),
            Quantity('threads', r'Threads:\s*(\d+)', dtype=np.int32),
            Quantity('input_file', r'Input File <==\s+\-+\s*([\s\S]+?)\-{5}', flatten=False),
            Quantity(
                'module',
                r'(\*\*\* at [A-Z][a-z]{2} [\s\S]+?(?:\*\*\* tstart|\Z))',
                repeats=True, sub_parser=TextParser(quantities=module_quantities))
        ]


class Psi4Parser:
    def __init__(self):
        self.m_env = m_env
        self.out_parser = OutParser()
        self._xc_map = {
            'HF': 'LDA_X',
            'PW6B95': 'HYB_MGGA_XC_PW6B95',
            'B3LYP': 'HYB_GGA_XC_B3LYP',
            'B3LYP5': 'HYB_GGA_XC_B3LYP5',
            'wB97X-D': 'HYB_GGA_XC_WB97X_D',
        }
        self._metainfo_map = {
            'Nuclear Repulsion': 'nuclear_repulsion',
            'Total': 'total',
            'DFT Exchange-Correlation': 'xc',
            'Nuclear Rep.': 'nuclear_repulsion',
        }

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self._method = None

    def parse_system(self, source):
        if source.geometry is None:
            return

        system = self.archive.run[-1].m_create(System)
        atoms = source.geometry.get('atoms', [])
        # TODO determine lattice vectors
        system.atoms = Atoms(
            positions=np.array([a[1:4] for a in atoms]) * ureg.bohr,
            labels=[a[0] for a in atoms], periodic=[False, False, False])
        for key, val in source.geometry.items():
            try:
                setattr(system, 'x_psi4_%s' % key, val)
            except Exception:
                pass

    def parse_method(self, source):
        method = self.archive.run[-1].m_create(Method)
        if self._method is not None:
            method.electronic = Electronic(method=self._method)
            if self._method[:2] in ['MP', 'CI', 'MC', 'CC']:
                method.core_method_ref = self.archive.run[-1].method[0]
                method.methods_ref = [self.archive.run[-1].method[0]]
                if source.parameters is not None:
                    method.x_psi4_parameters = {
                        key: val for key, val in source.parameters.get('key_value', [])}

        def parse_basis(source):
            if source is None:
                return
            basis_set = method.m_create(BasisSet)
            # TODO is this always the case?
            basis_set.type = 'Gaussians'
            for entry in source.get('basis_set', []):
                atom = basis_set.m_create(BasisSetAtomCentered)
                atom.name = entry.get('Basis Set', '').strip('(').strip(')')
                atom.n_basis_functions = int(entry.get('Number of basis function', 0))
                atom.x_psi4_n_shells = int(entry.get('Number of shells', 0))
                atom.x_psi4_max_angular_momentum = int(entry.get('Max angular momentum', 0))
                atom.x_psi4_n_cartesian_functions = int(entry.get('Number of Cartesian functions', 0))
                atom.x_psi4_blend = entry.get('Blend')
                atom.x_psi4_spherical_harmonics = entry.get('Spherical Harmonics?') == 'false'

        # basis set
        parse_basis(source.basis)
        for basis in source.get('auxiliary_basis', []):
            parse_basis(basis)

        if source.jk_matrices is not None:
            method.x_psi4_jk_matrices_parameters = source.jk_matrices.get('parameters', (None, None))[1]

        if source.algorithm is not None:
            scf = method.m_create(ScfMethod)
            for key, val in source.algorithm.items():
                try:
                    setattr(scf, key, val)
                except Exception:
                    pass

        if source.dft_potential is not None:
            dft = method.m_create(DFT)
            xc_functional = dft.m_create(XCFunctional)
            # get xc functional from composite first
            if len(xc_functional.exchange) == 0 and len(xc_functional.correlation) == 0:
                name, parameters = source.dft_potential.get('composite', (None, None))
                if name is not None:
                    name = self._xc_map.get(name)
                    if name is not None:
                        xc_functional.contributions.append(Functional(name=name, parameters=parameters))
            if len(xc_functional.contributions) == 0:
                # get contributions for exchange and correlation
                for xc_type in ['exact_exchange', 'exchange', 'correlation', 'hybrid']:
                    if 'exchange' in xc_type:
                        section = xc_functional.exchange
                    elif xc_type == 'correlation':
                        section = xc_functional.correlation
                    else:
                        section = xc_functional.hybrid
                    for weight, name in source.dft_potential.get(xc_type, []):
                        # it seems that other psi4 version print out xc functionals in libxc
                        # notation prefixed with XC_
                        # TODO complete mapping of XC functionals
                        name = self._xc_map.get(name, name).lstrip('XC_')
                        section.append(Functional(name=name, weight=weight))

            if source.dft_potential.molecular_quadrature is not None:
                dft.x_psi4_molecular_quadrature = source.dft_potential.molecular_quadrature[1]

    def parse_calculation(self, source):
        calc = self.archive.run[-1].m_create(Calculation)
        ref_calcs = []

        def parse_multipole(data, multipoles):
            if len(data) == 3:
                section = multipoles.m_create(MultipolesEntry, Multipoles.dipole)
                exponent = 1
            elif len(data) == 6:
                section = multipoles.m_create(MultipolesEntry, Multipoles.quadrupole)
                exponent = 2
            elif len(data) == 10:
                section = multipoles.m_create(MultipolesEntry, Multipoles.octupole)
                exponent = 3
            elif len(data) == 15:
                section = multipoles.m_create(MultipolesEntry, Multipoles.higher_order)
                section.kind = 'hexadecapole'
                exponent = 4
            else:
                section = multipoles.m_create(MultipolesEntry, Multipoles.higher_order)
                section.kind = '32-pole'
                exponent = 5
            value = data * ureg.elementary_charge * ureg.bohr ** exponent
            section.total = value.to('coulomb * m ** %d' % exponent).magnitude

        def parse_properties(source, calc):
            if source is None:
                return

            # multipoles
            multipole_kinds = ['electronic', 'nuclear', 'total']
            for n, multipole in enumerate(multipole_kinds):
                data = source.get('%s_dipole_moment' % multipole)
                if data is None:
                    continue
                multipoles = calc.m_create(Multipoles) if len(calc.multipoles) <= n else calc.multipoles[n]
                multipoles.kind = multipole_kinds[n]
                parse_multipole(data, multipoles)

            multipole_moments = source.get('multipole_moments', {})
            for multipole in ['dipole', 'quadrupole', 'octupole', 'hexadecapole', 'npole']:
                data = multipole_moments.get(multipole)
                if data is None:
                    continue
                data = np.transpose(data)
                for n, value in enumerate(data):
                    multipoles = calc.m_create(Multipoles) if len(calc.multipoles) <= n else calc.multipoles[n]
                    parse_multipole(value, multipoles)

            # TODO verify for non spin polarized
            # charges
            for method in ['mulliken', 'lowdin']:
                data = source.get('%s_charges' % method)
                if data is not None:
                    charges = calc.m_create(Charges)
                    charges.analysis_method = method
                    if data.atom is not None:
                        charges.value = [a[-1] for a in data.atom] * ureg.elementary_charge
                        charges.spins = [a[-2] for a in data.atom]
                        for n, atom in enumerate(data.atom):
                            for spin in range(2):
                                charges_spin = charges.m_create(ChargesValue, Charges.spin_projected)
                                charges_spin.atom_index = n
                                charges_spin.spin = spin
                                charges_spin.value = atom[spin] * ureg.elementary_charge
                    if data.total is not None:
                        charges.total = data.total[-1]

        # scf iterations
        if source.iterations is not None:
            for iteration in source.iterations.get('iteration', []):
                scf = calc.m_create(ScfIteration)
                scf.energy = Energy(
                    total=EnergyEntry(value=float(iteration[0]) * ureg.hartree),
                    change=float(iteration[1]) * ureg.hartree)

        # energies
        # mp/ci energy, the last entry belongs to the method
        # create additional calc section for references e.g. mp3 have mp2 reference
        for n in range(len(source.get('energy', []))):
            if source.energy[n] is None:
                continue
            ref_calc = calc
            # for MP calc, the last energy block corresponds to calc
            n_ref = len(source.energy) - 1 if self._method[:2] == 'MP' else 0
            if n != n_ref:
                ref_calc = self.archive.run[-1].m_create(Calculation)
                ref_calcs.append(ref_calc)
            ref_calc.energy = Energy()
            for key, val in source.energy[n].get('key_value'):
                key = self._metainfo_map.get(key, key)
                if hasattr(ref_calc.energy, key):
                    setattr(ref_calc.energy, key, EnergyEntry(value=val * ureg.hartree))
                else:
                    ref_calc.energy.contributions.append(EnergyEntry(kind=key, value=val * ureg.hartree))
                # assign total energy to corresponding to method
                if 'total' in key.lower():
                    ref_calc.energy.total = EnergyEntry(value=val * ureg.hartree)

        # forces
        if source.total_gradient is not None:
            calc.forces = Forces(total=ForcesEntry(
                value=source.total_gradient * ureg.hartree / ureg.bohr))

        # spins
        if source.s2_observed is not None:
            calc.x_psi4_s2_expected = source.s2_expected
            calc.x_psi4_s2_observed = source.s2_observed
            calc.spin_S2 = source.s2_observed
            calc.x_psi4_s_expected = source.s_expected
            calc.x_psi4_s_observed = source.s_observed

        # eigenvalues
        if source.orbital_energies is not None:
            eigenvalues = calc.m_create(BandEnergies)
            labels, energies, occupations = [], [], []
            n_spin = len(source.orbital_energies) // 2
            for n, orbital_energies in enumerate(source.orbital_energies):
                labels.extend(orbital_energies[0])
                energies.extend(orbital_energies[1])
                occupations.extend([2 / n_spin if n % 2 == 0 else 0] * len(orbital_energies[0]))
            eigenvalues.orbital_labels = labels
            eigenvalues.energies = np.reshape(energies, (n_spin, 1, len(energies) // n_spin)) * ureg.hartree
            eigenvalues.occupations = np.reshape(occupations, (n_spin, 1, len(occupations) // n_spin))

        # properties can be calculated using multiple density matrices e.g. for ci/mcscf
        # create additional calculation section
        for n, properties in enumerate(source.get('properties', [])):
            ref_calc = calc if n == 0 else self.archive.run[-1].m_create(Calculation)
            if n > 0:
                ref_calcs.append(ref_calc)
            parse_properties(properties, ref_calc)

        # misc
        if source.root_info is not None:
            root_info = calc.m_create(x_psi4_root_information)
            root_info.x_psi4_root_energy = source.root_info.energy

        # reference calculations
        if ref_calcs:
            calc.calculations_ref = ref_calcs
            for ref_calc in ref_calcs:
                ref_calc.starting_calculation_ref = calc

        if calc.m_mod_count == 1:
            self.archive.run[-1].m_remove_sub_section(Run.calculation, -1)

        return calc

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        self.init_parser()

        run = archive.m_create(Run)
        run.program = Program(name='Psi4', version=self.out_parser.get('version', ''))
        if self.out_parser.start_time is not None:
            start_time = datetime.strptime(self.out_parser.start_time, '%d %B %Y %H:%M%p')
            run.time_run = TimeRun(date_start=(start_time - datetime(1970, 1, 1)).total_seconds())

        for key in ['process_id', 'psidatadir', 'memory', 'threads', 'input_file']:
            val = self.out_parser.get(key)
            if val is not None:
                setattr(run, 'x_psi4_%s' % key, val)

        opt_calculations_ref = []
        module_names = [
            'scf', 'scf_grad', 'mp', 'ci', 'mcscf', 'mcscf_detci', 'cc', 'cc_energy',
            'cc_lambda', 'cc_density']
        for module in self.out_parser.get('module', []):
            calculations_ref = []
            for name in module_names:
                for submodule in module.get(name, []):
                    self._method = submodule.get('method', name.split('_')[0].upper())
                    self.parse_system(submodule)
                    self.parse_method(submodule)
                    calc = self.parse_calculation(submodule)
                    if calc is not None:
                        if self.archive.run[-1].system:
                            calc.system_ref = self.archive.run[-1].system[-1]
                        if self.archive.run[-1].method:
                            calc.method_ref = self.archive.run[-1].method[-1]
                    calculations_ref.append(calc)
            if module.options is not None:
                self.archive.run[-1].method[-1].x_psi4_options = module.options[1]

            if module.salc is not None:
                calc = self.archive.run[-1].calculation[-1]
                forces = calc.m_create(Forces)
                if module.salc.total_gradient is not None:
                    forces.total = ForcesEntry(
                        value=np.array(module.salc.total_gradient) * ureg.hartree / ureg.bohr)
                for contribution in module.salc.get('contributions_gradient', []):
                    forces.contributions.append(ForcesEntry(
                        kind=contribution.name, value=contribution.value * ureg.hartree / ureg.bohr))

            # each module should can be considered as a single_point workflow
            # TODO implement specific workflow for mp, ci, cc, mcscf
            workflow = self.archive.m_create(Workflow)
            workflow.type = 'single_point'
            workflow.calculations_ref = calculations_ref
            workflow.calculation_result_ref = calc
            self.archive.workflow2 = SinglePoint2()

            if module.optking is not None:
                self.parse_system(module.optking)
                calc = self.archive.run[-1].m_create(Calculation)
                forces = module.optking.get('geometry', {}).get('forces')
                if forces is not None:
                    calc.forces = Forces(total=ForcesEntry(value=forces * ureg.hartree / ureg.bohr))
                energy = module.optking.energy
                if energy is not None:
                    calc.energy = Energy(
                        total=EnergyEntry(value=energy[0] * ureg.hartree),
                        change=energy[1] * ureg.hartree)
                calc.system_ref = self.archive.run[-1].system[-1]
                opt_calculations_ref.append(calc)
        if opt_calculations_ref:
            workflow = self.archive.m_create(Workflow)
            workflow.type = 'geometry_optimization'
            workflow.calculations_ref = opt_calculations_ref
            workflow.calculation_result_ref = opt_calculations_ref[-1]
            convergence = module.optking.convergence_criteria
            if convergence is not None:
                geometry_opt = workflow.m_create(GeometryOptimization)
                geometry_opt.convergence_tolerance_energy_difference = convergence[0] * ureg.hartree
                geometry_opt.convergence_tolerance_force_maximum = convergence[1] * ureg.hartree / ureg.bohr
                geometry_opt.convergence_tolerance_displacement_maximum = convergence[2] * ureg.bohr
            workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
            workflow.method.convergence_tolerance_energy_difference = convergence[0] * ureg.hartree
            workflow.method.convergence_tolerance_force_maximum = convergence[1] * ureg.hartree / ureg.bohr
            workflow.method.convergence_tolerance_displacement_maximum = convergence[2] * ureg.bohr
            self.archive.workflow2 = workflow
