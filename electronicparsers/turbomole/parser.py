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
from datetime import datetime
from ase.data import atomic_numbers

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, FileParser
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    AtomParameters, Functional, Method, Electronic, BasisSet,
    BasisSetAtomCentered, Smearing, XCFunctional, DFT
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry,
    Thermodynamics, BandEnergies, ScfIteration
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization
from nomad.datamodel.metainfo.simulation.workflow import (
    GeometryOptimization as GeometryOptimization2, GeometryOptimizationMethod
)

from .metainfo import turbomole  # pylint: disable=unused-import


MOL = 6.02214076E23


class AuxiliaryOutParser(FileParser):
    def __init__(self, re_line, start):
        super().__init__()
        self._re_line = re.compile(re_line)
        self._start = start

    @property
    def matrix(self):
        if self._file_handler is None:
            self._file_handler = []
            with open(self.mainfile) as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    line = self._re_line.match(line)
                    if not line:
                        continue
                    value = line.group(1).split()
                    if int(value[0]) > len(self._file_handler):
                        self._file_handler.append([])
                    self._file_handler[-1].extend(value[self._start:])
        return self._file_handler


class EigenvaluesParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'irrep',
                r'irrep\s*([\w ]+\n)'
            ),
            Quantity(
                'eigenvalues',
                r'eigenvalues H\s*([\d\.\-\+EeDd ]+)\n',
                dtype=float, repeats=True,
                str_operation=lambda x: x.replace('D', 'E').replace('E', 'e').split()),
            Quantity(
                'occupation',
                r'occupation\s*([\d\.\- ]*\n)', dtype=float, repeats=True)]


class ControlParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_drvopt(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            return {v[0].strip(): v[1] for v in val}

        # TODO add more quantities
        self._quantities = [
            Quantity('operating_system', r'operating system\s*(\S+)'),
            Quantity('scf_iter_limit', r'scfiterlimit\s*(\S+)'),
            Quantity('scf_conv', r'scfconv\s*(\S+)'),
            Quantity('time_for_integral_calc', r'thime\s*(\S+)'),
            Quantity('pople_kind', r'pople\s*(\S+)'),
            Quantity('damping_parameter', r'scfdamp\s*start=\s*(\S+)\s*step=\s*(\S+)\s*min=\s*(\S+)'),
            Quantity('scfint', r'unit=\s*(\S+)\s*size=\s*(\S+)\s*file=\s*(\S+)\s*'),
            Quantity('interconversion_status', r'interconversion\s*(\S+)'),
            Quantity('drvopt', r'drvopt\s*([\s\S]+?)\n *\$', str_operation=str_to_drvopt)]


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_float = r'[\d\.\-\+eEDd]+'

        def str_to_atomic_info(val_in):
            vals = [v.split() for v in val_in.strip().split('\n')]
            # first two are 'atomic', 'coordinates'
            if vals[0][0] == '1':
                vals = np.transpose(vals)
                info = dict(
                    coordinates=np.array(vals[-3:].T, dtype=float) * ureg.bohr, atom=vals[1])
            else:
                keys = vals[0][2:]
                vals = np.transpose(vals[1:])
                info = dict(coordinates=np.array(vals[:3].T, dtype=float) * ureg.bohr)
                for n, key in enumerate(keys):
                    info[key] = vals[n + 3]
            info['atom'] = [v.title() for v in info.get('atom', [])]
            return info

        def str_to_cpu_time(val_in):
            time = 0.
            for n, v in enumerate(reversed(val_in.split())):
                multiplier = 24 * 3600 if n == 3 else 60 ** n
                time += float(v) * multiplier
            return time

        def str_to_hessian(val_in):
            re_row = re.compile(r'(\d*)\s*\w*\s*d(?:x|y|z) +([\d\.\- ]+\d)')
            re_value = re.compile(r'\-*\d+\.\d+')
            n_axis = 3

            hessian = []
            row_n = -1
            for val in val_in.strip().split('\n'):
                row = re.search(re_row, val)
                if not row:
                    continue
                if row.group(1):
                    row_n = (int(row.group(1)) - 1) * n_axis
                else:
                    row_n += 1

                if len(hessian) < row_n + 1:
                    hessian.append([])
                hessian[row_n].extend(re_value.findall(row.group(2)))

            for n in range(len(hessian)):
                hessian[n].extend([0] * (len(hessian) - len(hessian[n])))

            hessian = np.array(hessian, dtype=float)
            # symmetrize
            hessian = hessian + hessian.T - np.diag(hessian.diagonal())
            n_atoms = len(hessian) // n_axis
            hessian = np.reshape(hessian, (n_atoms, n_axis, n_atoms, n_axis))
            return np.transpose(hessian, axes=(0, 2, 1, 3)) * ureg.hartree / ureg.bohr**2

        # TODO integrate with hessian
        def str_to_normal_modes_vibrational_frequencies(val_in):
            re_row = re.compile(r'(\d*)\s*\w*\s+(?:x|y|z) +([\d\.\- ]+\d)')
            re_value = re.compile(r'\-*\d+\.\d+')
            n_axis = 3

            row_n = -1
            normal_modes = []
            for val in val_in.strip().split('\n'):
                row = re.search(re_row, val)
                if not row:
                    continue
                if row.group(1):
                    row_n = (int(row.group(1)) - 1) * n_axis
                else:
                    row_n += 1

                if len(normal_modes) < row_n + 1:
                    normal_modes.append([])
                normal_modes[row_n].extend(re_value.findall(row.group(2)))

            n_atoms = len(normal_modes) // n_axis
            normal_modes = np.array(normal_modes, dtype=float)
            n_modes = np.size(normal_modes) // (n_atoms * n_axis)
            normal_modes = np.transpose(
                np.reshape(normal_modes, (n_atoms, n_axis, n_modes)), axes=(2, 0, 1))

            def get_values(pattern, dtype=str):
                values_str = re.findall(pattern, val_in)
                values = []
                for value in values_str:
                    if dtype == float:
                        values.extend(re_value.findall(value))
                    else:
                        values.extend(value.split())
                return np.array(values, dtype=dtype)

            frequencies = get_values(r'frequency\s+([\d\.\- ]+\d)', float)

            infrared = [v == 'YES' for v in get_values(r'IR\s+([YES\- ]+)')]

            raman = [v == 'YES' for v in get_values(r'RAMAN\s+([YES\- ]+)')]

            intensity = get_values(r'intensity \(km/mol\)\s+([\d\.\- ]+\d)', float)

            return dict(
                normal_modes=normal_modes, mode_energies=frequencies, infrared_activity=infrared,
                raman_activity=raman, intensities=intensity)

        def str_to_energy_gradient(val_in):
            re_row = re.compile(r'dE/d((?:x|y|z)) +([\d\.\-\+ Dd]+\d)')
            re_value = re.compile(r'\-*\d+\.\d+D*d*\-*\+*\d*')

            gradients = []
            for val in val_in.strip().split('\n'):
                row = re.search(re_row, val)
                if not row:
                    continue
                row_n = ['x', 'y', 'z'].index(row.group(1))
                if len(gradients) < row_n + 1:
                    gradients.append([])
                gradients[row_n].extend([
                    v.replace('D', 'E').replace('d', 'e') for v in re_value.findall(row.group(2))])

            gradients = np.array(gradients, dtype=float)
            return np.transpose(gradients) * (ureg.hartree / ureg.bohr)

        def str_to_iteration(val_in):
            val = val_in.split('\n')
            keys = [v.strip() for v in val[0].split('  ') if v]
            # replace key with metainfo name
            units = {'energy_total': ureg.hartree}
            for n in range(len(keys)):
                if keys[n] == 'CCSD energy':
                    keys[n] = 'energy_total'
                elif keys[n] == 'wall':
                    keys[n] = 'time'
            val = [v.split() for v in val[1:]]
            val = np.transpose(np.array([v for v in val if len(v) == len(keys)], dtype=float))
            return [{key: val[n][i] * units.get(
                key, 1.0) for n, key in enumerate(keys)} for i in range(len(val[0]))]

        def str_to_embedding_coordinates(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            val = np.transpose([v for v in val if len(v) >= 4])
            label = [v.title() for v in val[0]]
            charge = val[4] if len(val) > 4 else [0] * len(label)
            return dict(
                label=label, coordinates=np.array(val[1:4].T, dtype=float) * ureg.bohr,
                charge=np.array(charge, dtype=float) * ureg.elementary_charge)

        def str_to_scf_energies(val_in):
            val = [float(v) for v in val_in.strip().replace('D', 'E').split()]
            return dict(
                energy_total=val[1] * ureg.hartree,
                x_turbomole_energy_1electron_scf_iteration=val[2] * ureg.hartree,
                x_turbomole_energy_2electron_scf_iteration=val[3] * ureg.hartree)

        def str_to_norm(val_in):
            name, val = val_in.split('=')
            val = val.split()
            name = 'norm_fia' if 'Fia' in name else 'norm_fock'
            return {name: float(val[0].replace('D', 'E')), '%s_orbital' % name: val[1]}

        def str_to_fon(val_in):
            val = [v.split('=') for v in val_in.split('\n')]
            return {v[0].strip(): float(v[1]) for v in val if len(v) == 2}

        def str_to_energies(val_in):
            re_energy = re.compile(rf'([\w\(\) ]+)\s*(?:=|:)\s*({re_float})')
            energies = dict()
            for val in val_in.strip().split('\n'):
                val = re_energy.search(val)
                if val:
                    key = val.group(1).strip()
                    energies[key] = float(val.group(2)) * ureg.hartree if 'energy' in key else float(val.group(2))
            return energies

        def str_to_gw_parameters(val_in):
            val = [v.rsplit(' ', 1) for v in val_in.strip().split('\n')]
            parameters = dict()
            for v in val:
                if v[1] in ['T', 'F']:
                    v[1] = v[1] == 'T'
                parameters[v[0].strip()] = v[1]
            return parameters

        def str_to_qp_states(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            val = np.transpose(np.array([v[1:] for v in val if len(v) == 9], dtype=float))
            keys = [
                'eigenvalue_ks_GroundState', 'eigenvalue_quasiParticle_energy',
                'eigenvalue_ExchangeCorrelation_perturbativeGW', 'eigenvalue_ExactExchange_perturbativeGW',
                'eigenvalue_correlation_perturbativeGW', 'eigenvalue_ks_ExchangeCorrelation',
                'Z_factor', 'ExchangeCorrelation_perturbativeGW_derivation']
            states = dict()
            for n, key in enumerate(keys):
                states[key] = val[n]
            return states

        def str_to_options(val_in):
            val = [v.split(':', 1) for v in val_in.strip().split('\n')]
            return {v[0].strip(): v[1].strip() for v in val if len(v) == 2}

        def str_to_convergence(val_in):
            re_value = re.compile(r'([\w ]+)\s*(yes|no)\s*')
            convergence = dict()
            for val in val_in.split('\n'):
                val = re_value.search(val)
                if val:
                    convergence[val.group(1).strip()] = val.group(2) == 'yes'
            return convergence

        def str_to_thermodynamics(val_in):
            keys, vals = val_in.strip().split('\n')
            # we could have taken units from prinout but some quantities do not have units
            keys = [k.strip().lower() for k in keys.split()]
            vals = [float(v) for v in vals.split()]
            units = {
                't': ureg.K, 'p': ureg.MPa, 'chem.pot.': ureg.kJ / MOL, 'energy': ureg.kJ / MOL,
                'entropy': ureg.kJ / MOL, 'cv': ureg.kJ / ureg.K / MOL, 'cp': ureg.kJ / ureg.K / MOL,
                'enthalpy': ureg.kJ / MOL}
            vals = {key: vals[n] * units.get(key, 1.0) for n, key in enumerate(keys)}
            # we calculate entropy energy correction
            if 'entropy' in vals and 't' in vals:
                vals['entropy'] *= vals['t'].magnitude
            return vals

        iteration_quantities = [
            Quantity(
                'damping_scf_iteration',
                rf'current damping\s*:*=*\s*({re_float})',
                str_operation=lambda x: 1.0 / (1.0 + float(x)), convert=False),
            Quantity(
                'energies',
                r'ATION\s*ENERGY.+\s*(\d*\s*.+)',
                str_operation=str_to_scf_energies, convert=False),
            Quantity(
                'energy_XC',
                rf'Exc\s*=\s*({re_float})',
                dtype=float, unit=ureg.hartree),
            Quantity(
                'norm_diis_scf_iteration',
                rf'Norm of current diis error\s*:\s*({re_float})', dtype=float),
            Quantity(
                'norm_fia',
                rf'max\. resid\. (norm for Fia\-block=\s*{re_float})\s*for orbital\s*(\w+)',
                str_operation=str_to_norm, convert=False),
            Quantity(
                'norm_fock',
                rf'max\. resid\. (fock norm\s*=\s*{re_float})\s*for orbital\s*(\w+)',
                str_operation=str_to_norm, convert=False),
            Quantity(
                'delta_eigenvalues',
                rf'Delta Eig\.\s*=\s*({re_float})', dtype=float, unit=ureg.eV),
            Quantity(
                'fon',
                r'FON Calculation\s*\-+\s*([\s\S]+?\-{50})',
                str_operation=str_to_fon, convert=False)]

        scf_quantities = [
            Quantity(
                'iteration',
                rf'(current damping\s*:\s*{re_float}\s*ITERATION[\s\S]+?)\n\s*\n',
                repeats=True, sub_parser=TextParser(quantities=iteration_quantities)),
            # alternative format
            Quantity(
                'iteration',
                r'(ATION\s*ENERGY[\s\S]+?)(?:\n *\n *ITER|End of SCF iterations)',
                repeats=True, sub_parser=TextParser(quantities=iteration_quantities)),
            Quantity(
                'number_of_scf_iterations',
                r'convergence criteria satisfied after\s*(\d+)\s*iterations',
                dtype=int)]

        module_quantities = [
            Quantity(
                'atomic_info',
                r'Atomic coordinate, charge and isotope? information\s*\|\s*\+\-+\+\s*'
                r'([\s\S]+?center of nuclear charge.+)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'info',
                        r'(atomic\s+coordinates\s+atom(?:\s+shells)?\s+charge(?:\s+pseudo)?\s+isotop\s*)'
                        r'([\s\S]+?)\n\s*\n', str_operation=str_to_atomic_info),
                    Quantity(
                        'center_of_nuclear_mass',
                        rf'center of nuclear mass\s*:\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float),
                    Quantity(
                        'center_of_nuclear_charge',
                        rf'center of nuclear charge\s*:\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float)])),
            Quantity(
                'basis_set_info',
                r'(\w* (?:basis set|BASIS SET) information\s*[\s\S]+?)\n\s*\n *\n',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'auxiliary',
                        r'(\w*) (?:basis|BASIS)',
                        str_operation=lambda x: 'auxiliary' in x.lower(), convert=False),
                    Quantity(
                        'spherical',
                        r'(with spherical basis functions)',
                        str_operation=lambda x: True, convert=False),
                    Quantity(
                        'atom',
                        r'(\w*)\s*(\d+)\s*(\d+)\s*(\d+)\s*([\w\-]+)\s*\[([\w\|]+)\]',
                        repeats=True),
                    Quantity(
                        'total',
                        r'total number of (.+?):\s*(\d+)',
                        repeats=True, str_operation=lambda x: x.rsplit(' ', 1))])),
            Quantity(
                'mo_occupation',
                r'mo occupation\s*:\s*irrep\s*mo\'s\s*occupied\s*([\s\S]+?)\n\s*\n',
                str_operation=lambda x: [v.split() for v in x.strip().split('\n')]),
            Quantity(
                'wavefunction_model',
                r'([w ]+)closed shell calculation for the wavefunction models:\s*(\S+)'),
            Quantity(
                'dft_functional',
                r'density functional\s*\-+(\s*[\s\S]+?)\n\s*\n *\n', sub_parser=TextParser(quantities=[
                    Quantity(
                        'functional',
                        r'(?:functional\s*:\s*(.+)|\n *(\S+)\s*(?:meta-GGA |hybrid )*functional\n)'),
                    Quantity('exchange', r'exchange:\s*(.+)', flatten=False),
                    Quantity('correlation', r'correlation:\s*(.+)', flatten=False)])),
            Quantity(
                'embedding_point_charges',
                r'EMBEDDING IN PERIODIC POINT CHARGES\s*\|\s*.+\s*.+\s*'
                r'([\s\S]+?)\n\s*\n *\n', sub_parser=TextParser(quantities=[
                    Quantity(
                        'pceem_max_multipole',
                        r'Maximum multipole moment used\s*:\s*(\d+)', dtype=int),
                    Quantity(
                        'pceem_multipole_precision',
                        rf'Multipole precision parameter\s*:\s*({re_float})', dtype=float),
                    Quantity(
                        'pceem_min_separation_cells',
                        rf'Minimum separation between cells\s*:\s*({re_float})', dtype=float),
                    Quantity(
                        'lattice_vectors',
                        r'Cell vectors \(au\):\s*(.+)\s*(.+)\s*(.+)', dtype=float, unit=ureg.bohr),
                    Quantity(
                        'redefined',
                        r'Redefined unit cell content \(au\):\s*.+\s*([\s\S]+?)\n\s*\n',
                        str_operation=str_to_embedding_coordinates, convert=False),
                    Quantity(
                        'pc_cluster',
                        r'PC cluster transformed to the center of cell 0 \(au\):\s*.+\s*([\s\S]+?)\n\s*\n',
                        str_operation=str_to_embedding_coordinates, convert=False),
                    Quantity(
                        'qm_cluster',
                        r'QM cluster transformed to the center of cell 0 \(au\):\s*.+\s*([\s\S]+?)\n\s*\n',
                        str_operation=str_to_embedding_coordinates, convert=False)])),
            Quantity(
                'dft_d3',
                r'(DFTD3 V[\d\.]+ Rev \d+[\s\S]+?)\n\s*\n *\n',
                sub_parser=TextParser(quantities=[
                    Quantity('version', r'DFTD3 V([\d\.]+ Rev \d+)', flatten=False),
                    Quantity(
                        'energy_van_der_Waals',
                        rf'Edisp /kcal,au:\s*\S+\s*({re_float})', dtype=float, unit=ureg.hartree)])),
            Quantity(
                'uhf',
                r'UHF mod.+? switched (on) !',
                str_operation=lambda x: x == 'on', convert=False),
            Quantity(
                'smearing',
                r'(\w+ smearing switched on[\s\S]+?)\n\s*\n',
                sub_parser=TextParser(quantities=[
                    Quantity('kind', r'(\w+) smearing', str_operation=lambda x: x.lower()),
                    Quantity(
                        'width',
                        rf'Final electron temperature:\s*({re_float})', dtype=float)])),
            Quantity(
                'energy_reference_wavefunction',
                rf'Energy of reference wave function is\s*({re_float})', dtype=float),
            Quantity(
                'energies',
                r'(total energy\s*=[\s\S]+?)\n\s*\n',
                str_operation=str_to_energies, convert=False),
            Quantity(
                'self_consistency',
                r'OPTIMIZATION OF THE GROUND STATE CLUSTER AMPLITUDES\s*\*\s*\*\s*\*\s*\*+'
                r'([\s\S]+?)\*{50}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        r'(Iter\.\s+CCSD energy[\s\S]+?)(?:CC equations|\n *\n)',
                        str_operation=str_to_iteration),
                    Quantity(
                        'convergence',
                        r'(?:converged in (\d+) iterations|within (\d+) cycles)', dtype=int)])),
            Quantity(
                'energies_MP2',
                r'(RHF\s*energy[\s\S]+?SOS\-MP2 energy.+)', str_operation=str_to_energies),
            Quantity(
                'energies_CCSD',
                r'(RHF\s*energy[\s\S]+?Final CCSD energy.*)', str_operation=str_to_energies),
            Quantity(
                'energies_CCSD(T0)',
                r'(RHF\s*energy[\s\S]+?Final CCSD\(T0\) energy.+)', str_operation=str_to_energies),
            Quantity(
                'energy_gradient',
                r'cartesian gradient of the energy \(hartree/bohr\)\s*\-+\s*([\s\S]+?)'
                r'calculation of the energy gradient finished',
                str_operation=str_to_energy_gradient, convert=False),
            Quantity(
                'eigenvalue_file',
                r'orbitals \$\S+\s*will be written to file (\w+)', repeats=True),
            Quantity(
                'cpu_time',
                rf'total\s*cpu-time\s*:\s*(?:({re_float}) days)*\s*(?:({re_float}) hours)*'
                rf'\s*(?:({re_float}) minutes and)*\s*({re_float}) seconds',
                str_operation=str_to_cpu_time, convert=False)]

        aoforce_quantities = module_quantities + [
            Quantity(
                'hessian',
                r'CARTESIAN FORCE CONSTANT MATRIX \(hartree/bohr\*\*2\)\s*'
                r'.+\s*\-+([\s\S]+?)\n\s*\n *\n',
                str_operation=str_to_hessian, convert=False),
            Quantity(
                'hessian_file',
                r'\*\*\*\s*projected\s+hessian\s+written\s+onto\s+\$hessian\s+\(projected\),\s+file=\<(.+)\>'),
            Quantity(
                'normal_modes_vibrational_frequencies',
                r'(NORMAL MODES and VIBRATIONAL FREQUENCIES \(cm\*\*\(-1\)\)\s*\-+[\s\S]+?)(?:\*{50}|\Z)',
                str_operation=str_to_normal_modes_vibrational_frequencies, convert=False),
            Quantity(
                'normal_modes_file',
                r'\*\*\*\s*normal\s+modes\s+written\s+onto\s+\$vibrational\s+normal\s+modes,\s+file=\<(.+?)\>'),
            Quantity(
                'vibrational_spectrum_file',
                r'\*\*\*\s+vibrational\s+spectroscopic\s+data\s+written\s+onto\$vibrational\s+spectrum\s+file=\<(.+?)\>'),
            Quantity(
                'energy_zero_point',
                rf'\*\s*zero point VIBRATIONAL energy\s*:\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'energy_total',
                rf'\*\s*SCF\-energy\s*:\s*({re_float})', drype=float, unit=ureg.hartree),
            Quantity(
                'energy_current',
                rf'\*\s*SCF \+ E\(vib0\)\s*:\s*({re_float})', dtype=float, unit=ureg.hartree)]

        ccsdf12_quantities = module_quantities + [
            Quantity(
                'energies',
                r'time in triples corr.+\s*\*+([\s\S]+?)\*{50}',
                str_operation=str_to_energies, convert=False)]

        dscf_quantities = module_quantities + [
            Quantity(
                'self_consistency',
                r'(scf convergence criterion : increment of total energy[\s\S]+?iterations)',
                sub_parser=TextParser(quantities=scf_quantities))]

        escf_quantities = module_quantities + [
            Quantity(
                'gw',
                r'(GW version\s*\d+[\s\S]+?)\n\s*\n *\n', sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters',
                        r'par[ae]meters:\s*\-+([\s\S]+?)\-{20}',
                        str_operation=str_to_gw_parameters),
                    Quantity(
                        'qp_states',
                        r'orb\s*eps\s*QP\-eps\s*Sigma\s*Sigma_x\s*Sigma_c\s*Vxc\s*Z\s*dS/de'
                        r'([\s\S]+?)\n\s*\n',
                        repeats=True, str_operation=str_to_qp_states, convert=False)]))]

        freeh_quantities = module_quantities + [
            Quantity(
                'thermodynamics',
                r'(T\s*[Pp]\s*.+\n)[\s\S]+?(\d[\d\.\- ]+)',
                repeats=True, str_operation=str_to_thermodynamics, convert=False),
            Quantity(
                'energy_zero_point',
                rf'zero point vibrational energy\s*\-+\s*zpe=\s*({re_float})\s*kJ/mol',
                dtype=float, unit=ureg.kJ / MOL)
        ]

        grad_quantities = module_quantities

        pnoccsd_quantities = module_quantities + [
            Quantity('methods', r' Method  \d+:\s*(\S+)', repeats=True),
            Quantity(
                'energies',
                r'(RHF\s*energy[\s\S]+?Final CCSD\(T\) energy.+)', str_operation=str_to_energies)]

        # TODO verify this
        # the only example I found shows ricc2 quantities are same with ccsdf12
        ricc2_quantities = ccsdf12_quantities + [
            Quantity(
                'energy_total',
                rf'Total\s+Energy\s*:\s*({re_float})', dtype=float, unit=ureg.eV)]

        ridft_quantities = module_quantities + [
            Quantity(
                'self_consistency',
                r'Starting SCF iterations([\s\S]+?)\-{40}',
                sub_parser=TextParser(quantities=scf_quantities))]

        rirpa_quantities = module_quantities + [
            # TODO verify this I cannot find an example file
            Quantity(
                'energies_RPA',
                r'(HXX\+RIRPA\s+total\s+energy\s*=[\s\S]+?HXX\s+total\s+energy\s*=.+)',
                str_operation=str_to_energies)]

        statpt_quantities = module_quantities + [
            Quantity(
                'atomic_info',
                r'ATOM\s*CARTESIAN COORDINATES\s*([\s\S]+?)\*{50}',
                sub_parser=TextParser(quantities=[Quantity(
                    'info',
                    r'([\s\S]+)', str_operation=str_to_atomic_info)])),
            Quantity(
                'options',
                r'Stationary point options\s*\*+\s*\*+\s*([\s\S]+?)\*{40}',
                str_operation=str_to_options),
            Quantity(
                'convergence',
                r'CONVERGENCE INFORMATION\s*Converged\?\s*Value\s*Criterion\s*([\s\S]+?)\*{50}',
                str_operation=str_to_convergence)]

        run_quantities = [
            Quantity(
                'x_turbomole_nodename',
                r'\w+\s*\((.+)\)\s*:\s*TURBO', flatten=False),
            Quantity(
                'program_version',
                r'MOLE (?:V|rev\.)( *[\d\.]+\s*\([\d ]+\))', flatten=False),
            Quantity(
                'time', r'(\d\d\d\d-\d\d-\d\d\s*\d\d:\d\d:\d\d\.\d\d\d)',
                flatten=False, repeats=True),
            Quantity(
                'module_aoforce',
                r'(a o f o r c e \- program[\s\S]+?(?:force : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=aoforce_quantities)),
            Quantity(
                'module_ccsdf12',
                r'(C C S D F 1 2\s*P R O G R A M[\s\S]+?(?:ccsdf12 : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=ccsdf12_quantities)),
            Quantity(
                'module_dscf',
                r'(d s c f \- program[\s\S]+?(?:dscf : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=dscf_quantities)),
            Quantity(
                'module_escf',
                r'(e s c f[\s\S]+?(?:escf : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=escf_quantities)),
            Quantity(
                'module_freeh',
                r'(f r e e   e n t h a l p y - program[\s\S]+?(?:freeh : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=freeh_quantities)),
            Quantity(
                'module_grad',
                r'(g r a d \- program[\s\S]+?(?:grad : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=grad_quantities)),
            Quantity(
                'module_pnoccsd',
                r'(P N O C C S D  - P R O G R A M[\s\S]+(?:pnoccsd : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=pnoccsd_quantities)),
            Quantity(
                'module_ricc2',
                r'(R I C C 2 \- PROGRAM[\s\S]+?(?:ricc2 : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=ricc2_quantities)),
            Quantity(
                'module_ridft',
                r'(r i d f t\s*DFT program[\s\S]+?(?:ridft : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=ridft_quantities)),
            # TODO implement RIRPA, pnoccsd, freeh
            Quantity(
                'module_rirpa',
                r'(PROGRAM\s+RIRPA[\s\s]+?(?:rirpa : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=rirpa_quantities)),
            Quantity(
                'module_statpt',
                r'(this is S T A T P T[\s\S]+?(?:statpt : all done\s*\*\*\*\*|\Z))',
                sub_parser=TextParser(quantities=statpt_quantities))]

        # necessary to wrap it around a module so we keep the order
        self._quantities = [Quantity(
            'module_run',
            r'(TURBOMOLE (?:V|rev)[\s\S]+?(?:all done\s*\*\*\*\*\s*[\d\.\-: ]+|\Z))',
            repeats=True, sub_parser=TextParser(quantities=run_quantities))]


class TurbomoleParser:
    def __init__(self):
        self.out_parser = OutParser()
        self.matrix_parser = AuxiliaryOutParser(r' *(\d+\s+\d+\s+[\d\.\- ]+)\n', 2)
        self.vibrational_parser = AuxiliaryOutParser(
            r' *(\d+\s+\w*\s+[\d\.\-]+\s+[\d\.\-]+\s+[YES\-]+\s+[YES\-]+)', 0)
        self.eigenvalues_parser = EigenvaluesParser()
        self.control_parser = ControlParser()

        self.xc_functional_map = {
            'S-VWN': ['LDA_X', 'LDA_C_VWN_3'],
            'PWLDA': ['LDA_X', 'LDA_C_PW'],
            'B-VWN': ['GGA_X_B88', 'LDA_C_VWN'],
            'B-LYP': ['GGA_X_B88', 'GGA_C_LYP'],
            'B-P': ['GGA_X_B88', 'GGA_C_P86'],
            'B-P86': ['GGA_X_B88', 'GGA_C_P86'],
            'PBE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'TPSS': ['MGGA_X_TPSS', 'MGGA_C_TPSS'],
            'M06': ['MGGA_X_M06', 'MGGA_C_M06'],
            'BH-LYP': ['HYB_GGA_XC_BHANDHLYP'],
            'B3-LYP': ['HYB_GGA_XC_B3LYP'],
            'PBE0': ['HYB_GGA_XC_PBEH'],
            'TPSSh': ['HYB_MGGA_XC_TPSSH'],
            'M06-2X': ['MGGA_X_M06_2X', 'MGGA_C_M06_2X'],
            'B2-PLYP': ['HYB_GGA_XC_B2PLYP']}

        self.models_map = {
            'MP2': 'MP2', 'CCS': 'CCS', 'CIS': 'CIS', 'CIS(D)': 'CISD', 'CIS(Dinf)': 'CISD',
            'ADC(2)': 'MP2',  # TODO: check paper to verify this mapping
            'CC2': 'CCSD', 'CCSD': 'CCSD', 'CCSD(T)': 'CCSD(T)'}

        self.metainfo_map = {
            'total energy': 'energy_total', 'kinetic energy': 'energy_kinetic_electronic',
            'potential energy': 'x_turbomole_potential_energy_final',
            'virial theorem': 'x_turbomole_virial_theorem', 'wavefunction norm': 'x_turbomole_wave_func_norm',
            'Final CCSD(T) energy': 'energy_total', 'CCSD correlation energy': 'energy_current',
            'Final CCSD(T0) energy': 'energy_total',
            'Final CCSD energy': 'energy_total', 'correlation energy': 'energy_current',
            'Final MP2 energy': 'energy_total', 'MP2 correlation energy (doubles)': 'energy_current',
            r'HXX\+RIRPA total energy': 'energy_total', 'RIRPA correlation energy': 'energy_current',
            'HXX total energy': 'energy_total', 'rpa response function': 'x_turbomole_gw_use_rpa_response',
            'eta (Hartree)': 'x_turbomole_gw_eta_factor',
            'Maximum allowed trust radius': 'x_turbomole_geometry_optimization_trustregion_max',
            'Minimum allowed trust radius': 'x_turbomole_geometry_optimization_trustregion_min',
            'Initial trust radius': 'x_turbomole_geometry_optimization_trustregion_initial',
            'Hessian update method': 'method',
            'Threshold for energy change': 'convergence_tolerance_energy_difference',
            'Threshold for max displacement element': 'convergence_tolerance_displacement_maximum',
            'Threshold for max gradient element': 'convergence_tolerance_force_maximum',
            'Threshold for RMS of displacement': 'x_turbomole_geometry_optimization_geometry_change_rms',
            'Threshold for RMS of gradient': 'x_turbomole_geometry_optimization_threshold_force_rms',
            't': 'temperature', 'p': 'pressure', 'entropy': 'energy_correction_entropy',
            'energy': 'energy_total', 'cv': 'heat_capacity_c_v', 'cp': 'heat_capacity_c_p'}

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger
        self.module = None

    def get_number_of_atoms(self):
        return len(self.module.get('atomic_info', {}).get('info', {}).get('atom', []))

    def get_number_of_spin_channels(self):
        nspin = 1
        if self.module.get('uhf'):
            nspin = 2
        gw_parameters = self.module.get('gw', {}).get('parameters', None)
        if gw_parameters is not None:
            nspin = gw_parameters.get('number of spin channels', 1)
        # TODO add other conditions
        return nspin

    def get_electronic_structure_method(self):
        if self.module.get('wavefunction_model') is not None:
            return self.models_map.get(self.module.get('wavefunction_model'), None)
        if self.module.get('methods') is not None:
            return self.models_map.get(self.module.get('methods')[-1], None)
        if self.module.get('dft_functional') is not None:
            return 'DFT'
        if self.module.get('gw') is not None:
            return 'G0W0'

    def parse_system(self):
        sec_run = self.archive.run[0]
        sec_system = sec_run.m_create(System)
        sec_atoms = sec_system.m_create(Atoms)

        info = self.module.get('atomic_info', {}).get('info', {})
        if info.get('coordinates') is not None:
            sec_atoms.positions = info.get('coordinates', [])
        if info.get('atom') is not None:
            sec_atoms.labels = info.get('atom', [])
        sec_atoms.periodic = [False, False, False]
        # TODO is it always non-periodic?

        point_charges = self.module.get('embedding_point_charges', {})
        cluster_description = {
            'redefined': 'periodic point charges for embedding',
            'pc_cluster': 'removed point charge cluster', 'qm_cluster': 'shifted embedded QM cluster'}
        sec_system.systems_ref = []
        for name in cluster_description.keys():
            cluster = point_charges.get(name, None)
            if cluster is None:
                continue
            sec_system_cluster = sec_run.m_create(System)
            sec_atoms = sec_system_cluster.m_create(Atoms)
            sec_atoms.positions = cluster.get('coordinates')
            sec_atoms.labels = cluster.get('labels')
            if name == 'redefined':
                sec_system_cluster.x_turbomole_pceem_charges = cluster.get('charges')
                sec_atoms.lattice_vectors = point_charges.get('lattice_vectors')
            sec_atoms.periodic = [True, True, True]
            # TODO is the reference correct or the other way around?
            sec_system.systems_ref.append(sec_system_cluster)

        for key, val in point_charges.items():
            if key.startswith('pceem_') and val is not None:
                setattr(sec_system, 'x_turbomole_%s' % key, val)

        return sec_system

    def parse_scc(self):
        sec_run = self.archive.run[0]
        sec_scc = sec_run.m_create(Calculation)

        n_atoms = self.get_number_of_atoms()

        # energies
        sec_energy = sec_scc.m_create(Energy)
        for key, val in self.module.get('energies', {}).items():
            key = self.metainfo_map.get(key, None)
            if key is None:
                continue
            if key.startswith('energy_'):
                sec_energy.m_add_sub_section(getattr(
                    Energy, key.replace('energy_', '').lower()), EnergyEntry(value=val))
            else:
                setattr(sec_scc, key, val)

        for key in ['zero_point', 'current', 'total']:
            val = self.module.get('energy_%s' % key)
            if val is not None:
                sec_energy.m_add_sub_section(getattr(Energy, key), EnergyEntry(value=val))

        # module-specific energies (will create additional scc, method)
        for name, energies in self.module.items():
            if not name.startswith('energies_') or energies is None:
                continue
            sec_scc_module = sec_run.m_create(Calculation)
            sec_scc_module_energy = sec_scc_module.m_create(Energy)
            for key, val in energies.items():
                key = self.metainfo_map.get(key, None)
                if key is None:
                    continue
                if key.startswith('energy_'):
                    sec_scc_module_energy.m_add_sub_section(getattr(
                        Energy, key.replace('energy_', '').lower()), EnergyEntry(value=val))
                else:
                    setattr(sec_scc_module, key, val)
            sec_method_module = sec_run.m_create(Method)
            sec_method_module.electronic = Electronic(method=name.lstrip('energies_'))
            sec_scc_module.method_ref = sec_method_module
            # add reference to main sec_scc
            sec_scc_module.starting_calculation_ref = sec_scc
            sec_scc_module.calculations_ref = [sec_scc]

        # forces
        energy_gradient = self.module.get('energy_gradient')
        if energy_gradient is not None:
            sec_scc.forces = Forces(total=ForcesEntry(value_raw=energy_gradient))

        # thermodynamics
        thermodynamics = self.module.get('thermodynamics')
        if thermodynamics is not None:
            current_t, current_p = 0., 0.
            # sec_scc_thermo = None
            for thermo in thermodynamics:
                if current_t != thermo.get('t', 0.) or current_p != thermo.get('p', 0.):
                    sec_scc_thermo = sec_run.m_create(Calculation)
                    sec_scc_thermo.starting_calculation_ref = sec_scc
                    sec_scc_thermo.calculations_ref = [sec_scc]
                    sec_thermo = sec_scc_thermo.m_create(Thermodynamics)
                    sec_scc_thermo_energy = sec_scc_thermo.m_create(Energy)
                current_t, current_p = thermo.get('t', 0.), thermo.get('p', 0.)
                if sec_scc_thermo is not None:
                    for key, val in thermo.items():
                        key = self.metainfo_map.get(key, key)
                        if key.startswith('energy_'):
                            sec_scc_thermo_energy.m_add_sub_section(getattr(
                                Energy, key.replace('energy_', '').lower()), EnergyEntry(value=val))
                        else:
                            setattr(sec_thermo, key, val)

        # hessian
        if self.module.get('hessian') is not None:
            sec_scc.hessian_matrix = self.module.get('hessian').to('J/m**2').magnitude
        elif self.module.get('hessian_file') is not None:
            # read if from file
            self.matrix_parser.mainfile = os.path.join(self.maindir, self.module.get(
                'hessian_file'))
            try:
                hessian = np.reshape(np.array(
                    self.matrix_parser.matrix, dtype=float), (n_atoms, 3, n_atoms, 3))
                hessian = np.transpose(hessian, axes=(
                    0, 2, 1, 3)) * ureg.hartree / ureg.bohr**2
                sec_scc.hessian_matrix = hessian.to('J/m**2').magnitude
            except Exception:
                self.logger.warning('Cannot read hessian file.')

        # vibrational frequencies
        vibration = self.module.get('normal_modes_vibrational_frequencies')
        if vibration is not None:
            for key, val in vibration.items():
                setattr(sec_scc, 'x_turbomole_vibrations_%s' % key, val)
        else:
            if self.module.get('normal_modes_file') is not None:
                # read from file
                self.matrix_parser.mainfile = os.path.join(self.maindir, self.module.get(
                    'normal_modes_file'))
                try:
                    normal_modes = np.array(self.matrix_parser.matrix, dtype=float)
                    sec_scc.x_turbomole_vibrations_normal_modes = np.transpose(np.reshape(
                        normal_modes, (n_atoms, 3, len(normal_modes[0]))), axes=(2, 0, 1))
                except Exception:
                    self.logger.warning('Cannot read normal modes file.')

            if self.module.get('vibrational_spectrum_file') is not None:
                self.vibrational_parser.mainfile = os.path.join(self.maindir, self.module.get(
                    'vibrational_spectrum_file', ''))
                try:
                    spectrum = self.vibrational_parser.matrix
                    sec_scc.x_turbomole_vibrations_mode_energies = np.array(
                        [s[-4] for s in spectrum], dtype=float)
                    sec_scc.x_turbomole_vibrations_intensities = np.array(
                        [s[-3] for s in spectrum], dtype=float)
                    sec_scc.x_turbomole_vibrations_infrared_activity = [s[-2] == 'YES' for s in spectrum]
                    sec_scc.x_turbomole_vibrations_raman_activity = [s[-1] == 'YES' for s in spectrum]

                except Exception:
                    self.logger.warning('Cannot read vibrational spectrum file.')

        # eigenvalues
        eigenvalue_files = self.module.get('eigenvalue_file')
        if eigenvalue_files is not None:
            eigenvalues = []
            occupation = []
            irrep = []
            try:
                for eigenvalue_file in eigenvalue_files:
                    self.eigenvalues_parser.mainfile = os.path.join(self.maindir, eigenvalue_file)
                    eigenvalues.append(np.hstack(self.eigenvalues_parser.get('eigenvalues', [])))
                    occupation.append(np.hstack(self.eigenvalues_parser.get('occupation', [])))
                    irrep.append(np.hstack(self.eigenvalues_parser.get('irrep', [])))
                    sec_eigenvalues = sec_scc.m_create(BandEnergies)
                    values = np.reshape(np.array(
                        eigenvalues, dtype=float), (len(eigenvalue_files), 1, len(eigenvalues[0]))) * ureg.hartree
                    occupations = np.reshape(np.array(
                        occupation, dtype=float), (len(eigenvalue_files), 1, len(occupation[0])))
                    irrep = np.reshape(np.array(
                        irrep, dtype=np.dtype(np.int32)), (len(eigenvalue_files), 1, len(irrep[0])))
                    sec_eigenvalues.energies = values
                    sec_eigenvalues.occupations = occupations
                    sec_eigenvalues.x_turbomole_eigenvalues_irreducible_representation = irrep
                    sec_eigenvalues.kpoints = [np.zeros(3)]
            except Exception:
                self.logger.warning('Cannot read eigenvalues.')

        # self consistency
        self_consistency = self.module.get('self_consistency', {})
        # total energies for calculation of energy change
        energies = [0.] + [iteration.get('energies', {}).get(
            'energy_total_scf_iteration') for iteration in self_consistency.get('iteration', [])]
        for n, iteration in enumerate(self_consistency.get('iteration', [])):
            sec_iteration = sec_scc.m_create(ScfIteration)
            sec_iteration_energy = sec_iteration.m_create(Energy)

            for key, val in iteration.get('energies', {}).items():
                if key.startswith('energy_'):
                    sec_iteration_energy.m_add_sub_section(
                        getattr(Energy, key.replace('energy_', '').lower()), EnergyEntry(value=val))
                else:
                    setattr(sec_iteration, key, val)
            # energy change
            sec_iteration.energy_change = energies[n]
            # scf quantities
            for key in ['total', 'XC']:
                val = iteration.get('energy_%s' % key, None)
                if val is None:
                    continue
                sec_iteration_energy.m_add_sub_section(
                    getattr(Energy, key.lower()), EnergyEntry(value=val))
            if iteration.get('time'):
                sec_iteration.time_calculation = iteration.get('time')
            # miscellaneous scf quantities
            scf_keys = [
                'damping_scf_iteration', 'norm_diis_scf_iteration', 'delta_eigenvalues',
                'norm_fia', 'norm_fock']
            for key in scf_keys:
                val = iteration.get(key, None)
                if val is None:
                    continue
                if key == 'norm_fia' or key == 'norm_fock':
                    setattr(sec_iteration, 'x_turbomole_%s_orbital_scf_iteration' % key, val.get('%s_orbital' % key))
                    val = val.get(key)
                    key = '%s_scf_iteration' % key
                setattr(sec_iteration, 'x_turbomole_%s' % key, val)
        n_scf = self_consistency.get('number_of_scf_iterations', None)
        if n_scf is not None:
            sec_scc.n_scf_iterations = n_scf

        # gw
        if self.module.get('gw') is not None:
            gw_metainfo_map = {
                'Z_factor': 'qp_linearization_prefactor',
                'eigenvalue_ks_GroundState': 'value_ks',
                'eigenvalue_quasiParticle_energy': 'value_qp',
                'eigenvalue_ExchangeCorrelation_perturbativeGW': 'value_xc',
                'eigenvalue_ExactExchange_perturbativeGW': 'value_exchange',
                'eigenvalue_correlation_perturbativeGW': 'value_correlation',
                'eigenvalue_ks_ExchangeCorrelation': 'value_ks_xc',
                'ExchangeCorrelation_perturbativeGW_derivation': 'x_turbomole_ExchangeCorrelation_perturbativeGW_derivation'
            }
            sec_eigs_gw = sec_scc.m_create(BandEnergies)
            for key, name in gw_metainfo_map.items():
                val = [q.get(key) for q in self.module.gw.get('qp_states', [])]
                # TODO verify shape for spin polarized
                val = np.reshape(val, (1, len(self.module.gw.get('qp_states', [])), len(val[0])))
                val = val * ureg.eV if name.startswith('value_') else val
                setattr(sec_eigs_gw, name, val)

        # vdW
        energy_vdW = self.module.get('dft_d3', {}).get('energy_van_der_Waals')
        if energy_vdW is not None:
            sec_scc.energy.van_der_waals = EnergyEntry(value=energy_vdW, kind='DFTD3')

        return sec_scc

    def parse_method(self):
        sec_method = self.archive.run[0].m_create(Method)
        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)

        method = self.get_electronic_structure_method()
        if method is not None:
            sec_electronic.method = method
        sec_electronic.n_spin_channels = self.get_number_of_spin_channels()
        sec_smearing = sec_electronic.m_create(Smearing)
        for key, val in self.module.get('smearing', {}).items():
            setattr(sec_smearing, key, val)

        atomic_info = self.module.get('atomic_info')
        if atomic_info is not None:
            info = atomic_info.get('info', {})
            atom_kind = list(set(info.get('atom', [])))
            for atom in atom_kind:
                sec_atom_kind = sec_method.m_create(AtomParameters)
                sec_atom_kind.atom_number = atomic_numbers.get(atom, 0)
                sec_atom_kind.label = atom

            # only atom kinds
            for basis_set in self.module.get('basis_set_info', []):
                atom = basis_set.get('atom', [])
                sec_basis_set = sec_method.m_create(BasisSet)
                sec_basis_set.type = 'gaussians'
                sec_basis_set.kind = 'density' if basis_set.auxiliary else 'wavefunction'

                for atom in basis_set.get('atom', []):
                    symbol = atom[0].title()
                    sec_atom_basis = sec_basis_set.m_create(BasisSetAtomCentered)
                    sec_atom_basis.name = atom[4]
                    sec_atom_basis.atom_number = atomic_numbers.get(symbol, 0)
                    if basis_set.spherical:
                        sec_atom_basis.n_basis_functions = atom[3]

        # XC Functionals
        sec_xc_functional = sec_dft.m_create(XCFunctional)
        dft_functional = self.module.get('dft_functional')
        if dft_functional is not None:
            for functional in self.xc_functional_map.get(dft_functional.get('functional'), ['HF_X']):
                if '_X_' in functional or functional.endswith('_X'):
                    sec_xc_functional.exchange.append(Functional(name=functional))
                elif '_C_' in functional or functional.endswith('_C'):
                    sec_xc_functional.correlation.append(Functional(name=functional))
                elif 'HYB' in functional:
                    sec_xc_functional.hybrid.append(Functional(name=functional))
                else:
                    sec_xc_functional.contributions.append(Functional(name=functional))

            if dft_functional.exchange is not None:
                sec_method.x_turbomole_functional_type_exchange = dft_functional.exchange

            if dft_functional.correlation is not None:
                sec_method.x_turbomole_functional_type_correlation = dft_functional.correlation

        # vdW method
        dftd3_version = self.module.get('dft_d3', {}).get('version', None)
        if dftd3_version is not None:
            sec_method.electronic.van_der_waals_method = 'DFT-D3'
            sec_method.x_turbomole_dft_d3_version = dftd3_version

        if self.module.get('gw') is not None:
            sec_method.calculation_method_kind = 'perturbative'
            parameters = self.module.gw.get('parameters', {})
            for key, val in parameters.items():
                val = val * ureg.hartree if 'Hartree' in key else val
                key = self.metainfo_map.get(key, None)
                if key is None:
                    continue
                setattr(sec_method, key, val)
            gw_type = parameters.get('type of gw 0:G0W0 1: GW0', 0)
            sec_method.x_turbomole_gw_approximation = ['G0W0', 'GW0'][gw_type]

        # control
        self.control_parser.mainfile = os.path.join(self.maindir, 'control')
        for key, val in self.control_parser.items():
            if val is None:
                continue
            if key == 'drvopt':
                for drvopt_key, drvopt_val in val.items():
                    setattr(sec_method, 'x_turbomole_controlIn_%s_status' % drvopt_key, drvopt_val)
            else:
                setattr(sec_method, 'x_turbomole_controlIn_%s' % key, val)

        return sec_method

    def parse_workflow(self):
        options = self.module.get('options')
        if options is None:
            return

        sec_workflow = self.archive.m_create(Workflow)
        sec_geometry_opt = sec_workflow.m_create(GeometryOptimization)
        workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
        for key, val in options.items():
            if 'radius' in key or 'displacement' in key:
                val = val * ureg.bohr
            elif 'energy' in key:
                val = val * ureg.hartree
            elif 'gradient' in key or 'force' in key:
                val = val * ureg.hartree / ureg.bohr
            key = self.metainfo_map.get(key, None)
            if key is None:
                continue
            setattr(sec_geometry_opt, key, val)
            setattr(workflow.method, key, val)
        self.archive.workflow2 = workflow

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        sec_run = self.archive.m_create(Run)

        sec_run.program = Program(name='turbomole')

        for header in ['program_version', 'x_turbomole_nodename']:
            value = [module_run.get(header) for module_run in self.out_parser.get('module_run', [])]
            if len(set(value)) > 1:
                self.logger.warning('Multiple values found for header.')
            if value:
                if header == 'program_version':
                    sec_run.program.version = value[0]
                else:
                    setattr(sec_run, header, value[0])

        time = [module_run.get('time') for module_run in self.out_parser.get('module_run', [])]
        time = [t for t in time if len(t) == 2]
        if len(time) > 0:
            start = datetime.strptime(time[0][0], '%Y-%m-%d %H:%M:%S.%f') - datetime.utcfromtimestamp(0)
            end = datetime.strptime(time[-1][1], '%Y-%m-%d %H:%M:%S.%f') - datetime.utcfromtimestamp(0)
            sec_run.time_run = TimeRun(date_start=start.total_seconds(), date_end=end.total_seconds())

        for module_run in self.out_parser.get('module_run', []):
            for name, module in module_run.items():
                if name.startswith('module_') and module is not None:
                    self.module = module

                    sec_method = self.parse_method()
                    sec_system = self.parse_system()
                    sec_scc = self.parse_scc()
                    self.parse_workflow()
                    sec_scc.method_ref = sec_method
                    sec_scc.system_ref = sec_system
