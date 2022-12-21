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
import ase
from ase import io as aseio

from .metainfo import m_env
from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, FileParser, DataTextParser
from nomad.datamodel.metainfo.simulation.run import (
    Run, Program)
from nomad.datamodel.metainfo.simulation.method import (
    Method, DFT, XCFunctional, Functional, BasisSet, BasisSetCellDependent, BasisSetAtomCentered,
    AtomParameters, Scf, Electronic
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Stress, StressEntry, ScfIteration, Forces,
    ForcesEntry
)
from nomad.datamodel.metainfo.workflow import (
    Workflow, GeometryOptimization, MolecularDynamics
)
from nomad.datamodel.metainfo.simulation.workflow import (
    GeometryOptimization as GeometryOptimization2, GeometryOptimizationMethod,
    MolecularDynamics as MolecularDynamics2, MolecularDynamicsMethod
)

from .metainfo.cp2k_general import x_cp2k_section_quickstep_settings, x_cp2k_section_dbcsr,\
    x_cp2k_section_startinformation, x_cp2k_section_end_information, x_cp2k_section_program_information,\
    x_cp2k_section_global_settings, x_cp2k_section_vdw_settings, x_cp2k_section_atomic_kinds,\
    x_cp2k_section_atomic_kind, x_cp2k_section_kind_basis_set, x_cp2k_section_total_numbers,\
    x_cp2k_section_maximum_angular_momentum, x_cp2k_section_quickstep_calculation,\
    x_cp2k_section_scf_iteration, x_cp2k_section_stress_tensor, x_cp2k_section_md_settings,\
    x_cp2k_section_restart_information, x_cp2k_section_geometry_optimization,\
    x_cp2k_section_geometry_optimization_step


try:
    import mdtraj
except ImportError:
    logging.getLogger(__name__).warning('Required MDTraj module not found.')
    mdtraj = False


units_map = {
    'hbar': ureg.hbar,
    'hartree': ureg.hartree,
    'angstrom': ureg.angstrom,
    'au_t': ureg.hbar / ureg.hartree,
    'fs': ureg.femtosecond,
    'K': ureg.kelvin,
}


def resolve_unit(unit_str, parts=[]):
    unit_str = unit_str.lower().replace(' ', '')
    parts = list(parts)

    if unit_str in units_map:
        return units_map[unit_str]

    try:
        return float(unit_str)
    except Exception:
        pass

    if unit_str == '':
        return 1

    open_p = unit_str.rfind('(')
    if open_p > -1:
        n_groups = unit_str.count('(')
        if n_groups != unit_str.count(')'):
            return unit_str
        for n in range(n_groups):
            part = unit_str[open_p + 1:]
            part = part[:part.find(')')]
            parts.append(resolve_unit(part, parts))
            unit_str = unit_str.replace('(%s)' % part, '[%d]' % n)
            open_p = unit_str.rfind('(')
        return resolve_unit(unit_str, parts)

    vals = unit_str.split('/')
    if len(vals) > 1:
        vals = [resolve_unit(v, parts) for v in vals]
        val = vals[0]
        for v in vals[1:]:
            val /= v
        return val

    vals = unit_str.split('**')
    if len(vals) > 1:
        vals = [resolve_unit(v, parts) for v in vals]
        val = vals[0]
        for v in reversed(vals[1:]):
            val = val ** v
        return val

    vals = unit_str.split('^')
    if len(vals) > 1:
        vals = [resolve_unit(v, parts) for v in vals]
        val = vals[0]
        for v in reversed(vals[1:]):
            val = val ** v
        return val

    vals = unit_str.split('*')
    if len(vals) > 1:
        vals = [resolve_unit(v, parts) for v in vals]
        unit = 1
        for v in vals:
            unit *= v
        return unit

    vals = unit_str.split('-1')
    if len(vals) == 2:
        return 1 / resolve_unit(vals[0], parts)

    vals = re.match(r'\[(\d+)\]', unit_str)
    if vals:
        return parts[int(vals.group(1))]


class Property:
    def __init__(self, **kwargs):
        self._data = kwargs

    def __getattr__(self, key):
        return self._data.get(key, None)


class Trajectory(Property):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class XYZTrajParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):

        def get_trajectory(val_in):
            val = np.transpose([v.split() for v in val_in.strip().split('\n')])
            positions = np.array(val[1:4], dtype=float).T
            return Trajectory(labels=val[0], positions=positions)

        self.quantities = [
            Quantity(
                'trajectory', r'([A-Z][a-z]?[\w\.\-\s]+?)(?:\s+\d\n|\Z)',
                str_operation=get_trajectory, repeats=True),
            Quantity(
                'energy', r'E\s*=\s*(\S+)', repeats=True, dtype=float)]


class TrajParser(FileParser):
    def __init__(self, **kwargs):
        super().__init__()
        self._xyz_parser = XYZTrajParser()
        self.format = None
        self.units = None
        self.type = kwargs.get('type', 'positions')

    @property
    def trajectory(self):
        if self._file_handler is None:
            if self.format is None:
                self.format = self.mainfile.split('.')[-1].lower()

            result = None
            labels = []
            # ase is better as it reads also symbols
            try:
                atoms_list = [atoms for atoms in aseio.iread(self.mainfile, format=self.format)]
                result = [atoms.positions for atoms in atoms_list]
                labels = [list(atoms.symbols) for atoms in atoms_list]

            # custom parser
            except Exception:
                if self.format == 'xyz':
                    self._xyz_parser.mainfile = self.mainfile
                    result = [traj.positions for traj in self._xyz_parser.get('trajectory', [])]
                    labels = [traj.labels for traj in self._xyz_parser.get('trajectory', [])]

            if result is None and mdtraj:
                reader = None
                if self.format in ['xyz', 'xmol', 'atomic']:
                    reader = mdtraj.formats.XYZTrajectoryFile(self.mainfile)
                elif self.format == 'dcd':
                    reader = mdtraj.formats.DCDTrajectoryFile(self.mainfile)
                elif self.format == 'pdb':
                    reader = mdtraj.formats.PDBTrajectoryFile(self.mainfile)
                else:
                    self.logger.error('Unsupported trajectory format.')

                if reader is not None:
                    try:
                        # we do not stream to simplify archive writing
                        result = reader.read()
                    except Exception:
                        pass

            result = result * self.units if self.units is not None else result

            result = [Trajectory(**{self.type: res}) for res in result]

            # add labels to trajectory
            for n, labels_i in enumerate(labels):
                result[n]._data.update({'labels': labels_i})

            self._file_handler = result

        return self._file_handler


re_float = r'[-+]?\d+\.?\d*(?:[Ee][-+]\d+)?'


class ForceParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [Quantity(
            'atom_forces',
            rf'\d+\s*\d+\s*\w+\s*({re_float})\s*({re_float})\s*({re_float})', repeats=True)]


class XCFunctionalProperty(Property):
    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)


class InpValue:
    def __init__(self, name, **kwargs):
        self._data = kwargs
        self._name = name
        self._dict = None

    @property
    def name(self):
        return self._name

    def add(self, key, val):
        if key in self._data:
            self._data[key] = self._data[key] if isinstance(self._data[key], list) else [self._data[key]]
            self._data[key].append(val)
        else:
            self._data[key] = val

    def to_dict(self):
        if self._dict is None:
            def extract(data):
                out = dict()
                for key, val in data.items():
                    if isinstance(val, InpValue):
                        val = extract(val.to_dict())
                    out[key] = val
                return out

            self._dict = extract(self._data)

        return self._dict

    def items(self):
        for key, val in self._data.items():
            yield key, val

    def __getattr__(self, key):
        return self._data.get(key, None)

    def __repr__(self):
        return self._name


class InpParser(FileParser):
    def __init__(self):
        super().__init__()
        self._re_open = re.compile(r'&(\w+)\s*(.*?)[#!\n]')
        self._re_close = re.compile(r'&END')
        self._re_key_value = re.compile(r'(\w+)\s+(.+?)[#!\n]')
        self._re_variable = re.compile(r'@SET (\w+)\s+(.+?)[#!\n]')

    @property
    def tree(self):
        if self._file_handler is None:
            def override(name, data):
                if data[0] == 'PROJECT':
                    return 'PROJECT_NAME', data[1]
                elif not data[0].isupper():
                    return 'DEFAULT_KEYWORD', ' '.join(data)
                return data

            self._variables = dict()
            line = True
            sections = [InpValue('tree')]
            while line:
                line = self.mainfile_obj.readline()
                # comments
                strip = line.strip()
                if not strip or strip[0] in ('#', '!'):
                    continue
                variable = self._re_variable.search(line)
                if variable:
                    self._variables['${%s}' % variable.group(1)] = variable.group(2).strip()
                    continue
                close_section = self._re_close.search(line)
                if close_section:
                    sections.pop(-1)
                    continue
                open_section = self._re_open.search(line)
                if open_section:
                    section = InpValue(open_section.group(1))
                    sections[-1].add(open_section.group(1), section)
                    sections.append(section)
                    if open_section.group(2):
                        sections[-1].add('VALUE', open_section.group(2))
                    continue
                key_value = self._re_key_value.search(line)
                if key_value:
                    key, val = key_value.group(1), key_value.group(2)
                    val = val.strip()
                    if val in self._variables:
                        val = self._variables[val]
                    key, val = override(sections[-1].name, [key, val])
                    sections[-1].add(key, val)
                    continue
            self._file_handler = sections[0]
        return self._file_handler

    def parse(self, key):
        if self._results is None:
            self._results = dict()

        source = self.tree.to_dict()
        for sub_key in key.strip('/').split('/'):
            val = source.get(sub_key, None)
            source = val
            if val is None:
                break
        self._results[key] = val


class CP2KOutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_header(val_in):
            val = val_in.split('  ', 1)
            return [val[0].strip().replace(' ', '_').lower(), val[-1].strip()]

        def md_extract(val_in):
            result = re.search(r' MD\| (?P<key>.+?)(?: \[(?P<unit>.+)\])? {2,}(?P<value>.+)', val_in)
            value = result.group('value')
            unit = units_map.get(result.group('unit'))
            key = result.group('key').strip().replace(' ', '_').lower()
            if unit:
                value = float(value) * unit
            return [key, value]

        def str_to_program(val_in):
            val = val_in.split(' ', 2)
            return ['_'.join(val[:2]).lower(), ''.join([v.strip() for v in val[2].split('\n')])]

        def str_to_atomic_coordinates(val_in):
            val = [v.split() for v in val_in.split('\n')]
            lengthunit = val[0][0].lower()
            val = np.transpose(np.array([v for v in val if len(v) == 9]))
            labels = val[2]
            positions = np.transpose(np.array(val[4:7], dtype=float)) * resolve_unit(lengthunit)
            atomic_numbers = {element: int(val[3][n]) for n, element in enumerate(val[2])}
            return Trajectory(labels=labels, positions=positions, atomic_numbers=atomic_numbers)

        def str_to_stress_eigenvalues(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            val = np.array([v for v in val if v], dtype=float)
            return val[0] * ureg.GPa, val[1:]

        def str_to_iteration(val_in):
            val = val_in.strip().split()
            return {
                'energy_total': float(val[-2]) * ureg.hartree,
                'energy_change': float(val[-1]) * ureg.hartree}

        def str_to_information(val_in):
            val = [v.split('=') for v in val_in.strip().split('\n')]
            return {v[0].strip().lower().replace(' ', '_').replace('.', ''): v[1] for v in val if len(v) == 2}

        n_orbital_basis_quantities = [Quantity(
            'basis_set_number_of_%s' % key.lower().replace(' ', '_'),
            r'Number of %s:\s+(\d+)' % key, dtype=int) for key in [
                'orbital shell sets', 'orbital shells', 'primitive Cartesian functions',
                'Cartesian basis functions', 'spherical basis functions']]

        energy_quantities = [Quantity(
            '%s' % key.lower().replace(' ', '_').replace('-', '_'),
            rf'%s:\s*({re_float})' % key, dtype=float, unit='hartree', repeats=True) for key in [
                'Hartree energy', 'Exchange-correlation energy', 'Electronic kinetic energy',
                'Total energy']]
        # what is the difference between Total energy and ENERGY| Total

        scf_wavefunction_optimization_quantities = [
            Quantity(
                'iteration',
                rf'(\d+\s+\S+\s*\S*\s+{re_float}\s+{re_float}\s+{re_float}\s+{re_float}\s+{re_float})\n',
                repeats=True, convert=False, str_operation=str_to_iteration),
            # TODO add minimizer info
            Quantity(
                'converged',
                r'SCF run converged in\s*(\d+) steps', dtype=int),
            # find example with cueb file
            Quantity(
                'cube_file',
                r' The electron density is written in cube file format to the file:\s*(.+?\.cube)'),
            # TODO add mulliken, hirschfield
            Quantity(
                'energy_total',
                rf'ENERGY\| Total FORCE_EVAL \( \w+ \) energy \(a\.u\.\):\s*({re_float})',
                dtype=float, unit='hartree'),
            Quantity(
                'atom_forces',
                rf'ATOMIC FORCES in \[a\.u\.\]\s*.+([\s\S]+?)SUM', convert=False,
                str_operation=lambda x: np.array(np.transpose(
                    [v.split() for v in x.strip().split('\n')])[3:6], dtype=float).T),
            # TODO test stress cannot find example
            Quantity(
                'stress_tensor',
                r' (?:NUMERICAL )?STRESS TENSOR \[GPa\]\s+X\s+Y\s+Z\s+([\d\.\-\s]+)',
                str_operation=lambda x:np.array([v.split() for v in x.strip().split('\n')], dtype=float),
                convert=False, unit='GPa'),
            Quantity(
                'stress_tensor_one_third_of_trace',
                rf'  1/3 Trace\(stress tensor\)\s*:\s*({re_float})', dtype=float, unit='GPa'),
            Quantity(
                'stress_tensor_determinant',
                rf'Det\(stress tensor\)\s*:\s*({re_float})', dtype=float, unit='GPa**3'),
            Quantity(
                'stress_eigenvalues_eigenvectors',
                r' EIGENVECTORS AND EIGENVALUES OF THE STRESS TENSOR\s*([\d\.\-\s]+)',
                str_operation=str_to_stress_eigenvalues, convert=False)] + energy_quantities

        single_point_quantities = [
            Quantity(
                'self_consistent',
                r'SCF WAVEFUNCTION OPTIMIZATION([\s\S]+?)\Z', repeats=False,
                sub_parser=TextParser(quantities=scf_wavefunction_optimization_quantities)),
            # TODO add rpa, etc.
        ]

        geometry_optimization_quantities = [
            Quantity(
                'method',
                r'\*{3}\s*((?:CONJUGATE GRADIENTS|L-BFGS|BFGS))\s*\*{3}', flatten=False),
            Quantity(
                'self_consistent',
                r'SCF WAVEFUNCTION OPTIMIZATION([\s\S]+?)OPTIMIZ', repeats=False,
                sub_parser=TextParser(quantities=scf_wavefunction_optimization_quantities)),
            Quantity(
                'optimization_step',
                r'(ATION STEP:\s*\d+[\s\S]+?)(?:\-\s+OPTIMIZ|\Z)', repeats=True,
                sub_parser=TextParser(quantities=[
                    # TODO parse atomic positions
                    Quantity('step', r'ATION STEP:\s*(\d+)'),
                    # I do not quite get why there can be multiple scfs in a step
                    Quantity(
                        'information',
                        r'Informations at step\s*=\s*\d+\s*\-+([\s\S]+?)\-{5}',
                        str_operation=str_to_information),
                    Quantity(
                        'self_consistent',
                        r'FUNCTION OPTIMIZATION([\s\S]+?)(?: SCF WAVE|\Z)', repeats=True,
                        sub_parser=TextParser(quantities=scf_wavefunction_optimization_quantities))]))
        ]

        molecular_dynamics_quantities = [
            Quantity(
                'initial',
                r' INITIAL\| (.+? {2})=\s+(.+)', str_operation=str_to_header, repeats=True),
            Quantity(
                'self_consistent',
                r'SCF WAVEFUNCTION OPTIMIZATION([\s\S]+?)(?:\*\n *ENSEM|\Z)', repeats=False,
                sub_parser=TextParser(quantities=scf_wavefunction_optimization_quantities)),
            Quantity(
                'md_step',
                r'(BLE TYPE[\s\S]+?)(?:\*\n *ENSEM|\Z)',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'ensemble_type', r'BLE TYPE\s*=\s*(.+)'),
                    Quantity(
                        'step_number', r'STEP NUMBER\s*=\s*(\d+)', dtype=int),
                    Quantity(
                        'time', rf'TIME \[fs\]\s*=\s*({re_float})', dtype=float),
                    Quantity(
                        'conserved_quantity',
                        rf'CONSERVED QUANTITY \[hartree\]\s*=\s*({re_float})',
                        dtype=float, unit='hartree'),
                    Quantity(
                        'cpu_time',
                        rf'CPU TIME \[s\]\s*=\s*({re_float})\s*(re_float)',
                        dtype=float),
                    Quantity(
                        'energy_drift',
                        rf'ENERGY DRIFT PER ATOM \[K\]\s*=\s*({re_float})\s*({re_float})',
                        dtype=float, unit='hartree'),
                    Quantity(
                        'potential_energy',
                        rf'POTENTIAL ENERGY\[hartree\]\s*=\s*({re_float})\s*({re_float})',
                        dtype=float, unit='hartree'),
                    Quantity(
                        'kinetic_energy',
                        rf'KINETIC ENERGY\[hartree\]\s*=\s*({re_float})\s*({re_float})',
                        dtype=float, unit='hartree'),
                    Quantity(
                        'temperature',
                        rf'TEMPERATURE \[K\]\s*=\s*({re_float})\s*({re_float})', dtype=float),
                    Quantity(
                        'pressure',
                        rf'PRESSURE \[bar\]\s*=\s*({re_float})\s*({re_float})',
                        dtype=float, unit='bar'),
                    Quantity(
                        'barostat_temperature',
                        rf'BAROSTAT TEMP\[K\]\s*=\s*({re_float})\s*({re_float})', dtype=float),
                    Quantity(
                        'volume',
                        rf'VOLUME\[bohr\^3\]\s*=\s*({re_float})\s*({re_float})',
                        dtype=float, unit='bohr**3'),
                    Quantity(
                        'cell_length_instantaneous',
                        rf'CELL LNTHS\[bohr\]\s*=\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float),
                    Quantity(
                        'cell_length_average',
                        rf'AVE\. CELL LNTHS\[bohr\]\s*=\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float),
                    Quantity(
                        'cell_angle_instantaneous',
                        rf'CELL ANGLS\[deg\]\s*=\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float),
                    Quantity(
                        'cell_angle_average',
                        rf'AVE\. CELL ANGLS\[deg\]\s*=\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float),
                    Quantity(
                        'self_consistent',
                        r'FUNCTION OPTIMIZATION([\s\S]+?)(?: SCF WAVE|\Z)', repeats=True,
                        sub_parser=TextParser(quantities=scf_wavefunction_optimization_quantities))])
            )
        ]

        quickstep_quantities = [
            Quantity(
                'dft',
                r' DFT\| (.+? {2}) +(.+)', str_operation=str_to_header, repeats=True),
            Quantity('dft_u', r'(DFT\+U\|)'),
            Quantity('mp2', r'(MP2\|)'),
            Quantity('rpa', r'(RI-RPA\|)'),
            Quantity(
                'functional', r' FUNCTIONAL\| (\S+):', repeats=True),
            # TODO find example and verify
            Quantity(
                'vdw',
                r' vdW POTENTIAL\| +(.+? {2}) +(.+)', str_operation=str_to_header, repeats=True),
            Quantity(
                'qs',
                r' QS\| ((?:Method|Density cutoff)).*?:( {2}) +(.+)',
                str_operation=str_to_header, repeats=True),
            Quantity(
                'atomic_kind_information',
                r' ATOMIC KIND INFORMATION([\s\S]+?)\n\n\n',
                sub_parser=TextParser(quantities=[Quantity(
                    'atom',
                    r'(ic kind: [A-Z][a-z]?[\s\S]+?)(?:\d+\. Atom|\Z)', repeats=True,
                    sub_parser=TextParser(quantities=[
                        Quantity('kind_label', r'ic kind:\s*(\w+)'),
                        Quantity('kind_number_of_atoms', r'Number of atoms:\s*(\d+)', dtype=int),
                        Quantity('kind_basis_set_name', r'Orbital Basis Set\s*(.+)'),
                        Quantity('basis_set_norm_type', r'Norm type:\s*(\d+)', dtype=int)
                    ] + n_orbital_basis_quantities))])),
            Quantity(
                'total_maximum_numbers',
                r' TOTAL NUMBERS AND MAXIMUM NUMBERS([\s\S]+?)\n\n\n',
                sub_parser=TextParser(quantities=[Quantity(
                    '%s' % key.lower().replace('the ', '').replace(' ', '_').replace('-', '_'),
                    r'\- %s:\s*(\d+)' % key, dtype=int) for key in [
                        'Atomic kinds', 'Atoms', 'Shell sets', 'Shells', 'Primitive Cartesian functions',
                        'Cartesian basis functions', 'Spherical basis functions',
                        'Orbital basis functions', 'Local part of the GTH pseudopotential',
                        'Non-local part of the GTH pseudopotential']])),
            Quantity(
                'atomic_coordinates',
                r' ATOMIC COORDINATES IN (angstrom[\s\S]+?)\n\n\n',
                convert=False, str_operation=str_to_atomic_coordinates),
            Quantity(
                'scf_parameters',
                r' SCF PARAMETERS([\s\S]+?)\*{79}',
                sub_parser=TextParser(quantities=[
                    Quantity('n_max_iteration', r'max_scf:\s*(\d+)', dtype=int),
                    Quantity(
                        'threshold_energy_change', rf'eps_scf:\s*({re_float})',
                        dtype=float, unit='hartree'),
                    Quantity(
                        'md',
                        r'( MD\| .+? {2} +.+)',
                        str_operation=md_extract,
                        convert=False,
                        repeats=True,
                    ),
                ])),
            # TODO add mp2, rpa, gw
            Quantity(
                'single_point',
                r'( Iteration\s*Convergence\s*Energy[\s\S]+?(?:\-{50}\n\s*\-|MD_ENERGIES))',
                sub_parser=TextParser(quantities=single_point_quantities)),
            Quantity(
                'geometry_optimization',
                r'STARTING GEOMETRY OPTIMIZATION([\s\S]+?(?:GEOMETRY OPTIMIZATION COMPLETED|\Z))',
                sub_parser=TextParser(quantities=geometry_optimization_quantities)),
            Quantity(
                'molecular_dynamics',
                r'(MD_ENERGIES\| Initialization proceeding[\s\S]+?\-{50}\n\s*\-)',
                sub_parser=TextParser(quantities=molecular_dynamics_quantities))
        ]

        self._quantities = [
            Quantity(
                'dbcsr',
                r' (DBCSR)\| (.+? {2}) +(.+)', str_operation=str_to_header, repeats=True),
            Quantity(
                'program',
                r'\*\*\s*PROGRAM ([\s\S]+?)(?:\*\*|\n\n|\Z)',
                str_operation=str_to_program, repeats=True),
            Quantity(
                'cp2k',
                r' CP2K\| (.+? {2}) +(.+)', str_operation=str_to_header, repeats=True),
            Quantity(
                'global',
                r' GLOBAL\| (.+? {2}) +(.+)', str_operation=str_to_header, repeats=True),
            Quantity(
                'restart',
                r'RESTART INFORMATION\s*\*+\s*\*+([\s\S]+?)\*{79}',
                sub_parser=TextParser(quantities=[
                    Quantity('filename', r'RESTART FILE NAME: (\S+)'),
                    Quantity(
                        'quantities',
                        r'RESTARTED QUANTITIES:\s*\*\s*([\s\S]+?)\Z',
                        str_operation=lambda x: [v.split('*')[1].strip() for v in x.strip().split('\n')])])),
            Quantity(
                'lattice_vectors',
                rf' CELL\| Vector [abc] \[angstrom\]:\s*({re_float})\s*({re_float})\s*({re_float})',
                repeats=True),
            # TODO add restart find example
            Quantity(
                'quickstep',
                r'\.\.\. make the atoms dance([\s\S]+?(?:\-{79}\s*\-|\Z))',
                sub_parser=TextParser(quantities=quickstep_quantities)),
            Quantity(
                'qs_dftb',
                r'  #####   #####        # ######  ####### ####### ######\s*'
                r' #     # #     #      #  #     # #          #    #     #\s*'
                r' #     # #           #   #     # #          #    #     #\s*'
                r' #     #  #####     #    #     # #####      #    ######\s*'
                r' #   # #       #   #     #     # #          #    #     #\s*'
                r' #    #  #     #  #      #     # #          #    #     #\s*'
                r'  #### #  #####  #       ######  #          #    ######\s*'
                r'([\s\S]+?(?:\-{79}\s*\-|\Z))',
                sub_parser=TextParser(quantities=quickstep_quantities))
            # TODO add other calculation types
        ]


class CP2KParser:
    def __init__(self):
        self.out_parser = CP2KOutParser()
        self.inp_parser = InpParser()
        # use a custom xyz parser as the output of cp2k is sometimes not up to standard
        self.traj_parser = TrajParser(type='positions')
        self.velocities_parser = TrajParser(type='velocities')
        self.cell_parser = DataTextParser()
        self.energy_parser = DataTextParser()
        self.force_parser = ForceParser()
        self._method = None
        self._calculation_type = None

        # TODO add vdw parameter
        self._metainfo_name_map = {
            'started_at': 'start_time', 'started_on': 'start_host',
            'started_by': 'start_user', 'process_id': 'id', 'started_in': 'start_path',
            'ended_at': 'end_time', 'ran_on': 'end_host', 'ran_by': 'end_user',
            'stopped_in': 'end_path', 'version_string:': 'program_version',
            'source_code_revision_number:': 'svn_revision',
            'program_compiled_at': 'program_compilation_datetime',
            'program_compiled_on': 'program_compilation_host',
            'input_file_name': 'input_filename',
            'basis_set_file_name': 'basis_set_filename',
            'geminal_file_name': 'geminal_filename',
            'potential_file_name': 'potential_filename',
            'mm_potential_file_name': 'mm_potential_filename',
            'coordinate_file_name': 'coordinate_filename',
            'preferred_diagonalization_lib.': 'preferred_diagonalization_library',
            'spin_restricted_kohn-sham_(rks)_calculation': 'spin_restriction',
            'multiplicity': 'spin_target_multiplicity',
            'number_of_spin_states': 'number_of_spin_channels', 'charge': 'total_charge',
            'self-interaction_correction_(sic)': 'self_interaction_correction_method',
            'method': 'quickstep_method', 'density_cutoff': 'planewave_cutoff',
            'temperature': 'target_temperature', 'temperature_tolerance': 'target_temperature_tolerance',
            'pressure': 'target_pressure', 'print_md_information_every': 'print_frequency',
            'potential_form:': 'vdw_name', 'bj_damping:': 'bj_damping_name',
            'cutoff_radius_[bohr]:': 'cutoff_radius', 'scaling_factor:': 'scaling_factor',
            'exp_prefactor_for_damping:': 'damping_factor', 's6_scaling_factor:': 's6_scaling_factor',
            'sr6_scaling_factor:': 'sr6_scaling_factor', 's8_scaling_factor:': 's6_scaling_factor',
            'cutoff_for_cn_calculation:': 'cn_cutoff', 'optimization_method': 'method',
            'total_energy': 'energy', 'real_energy_change': 'energy_change',
            'decrease_in_energy': 'energy_decrease', 'conv_limit_for_step_size': 'step_size_convergence_limit',
            'convergence_in_step_size': 'step_size_convergence',
            'convergence_in_rms_step_size': 'rms_step_size_convergence',
            'conv_limit_for_gradients': 'gradient_convergence_limit',
            'conv_for_gradients': 'max_gradient_convergence',
            'conv_in_rms_gradients': 'rms_gradient_convergence',
            'exchange_correlation_energy': 'energy_XC',
            'electronic_kinetic_energy': 'energy_kinetic_electronic'}

        self._self_interaction_map = {
            'NO': None, 'D SIC': 'SIC_AD', 'Explicit Orbital SIC': 'SIC_EXPLICIT_ORBITALS',
            'SPZ/MAURI SIC': 'SIC_MAURI_SPZ', 'US/MAURI SIC': 'SIC_MAURI_US'}
        self._optimization_method_map = {
            'CONJUGATE GRADIENTS': 'conjugate gradient', 'BFGS': 'bfgs', 'L-BFGS': 'bfgs'}
        self._file_extension_map = {
            'XYZ': 'xyz', 'XMOL': 'xyz', 'ATOMIC': 'xyz', 'PDB': 'pdb', 'DCD': 'dcd'}
        self._xc_functional_map = {
            'BLYP': [XCFunctionalProperty('GGA_X_B88'), XCFunctionalProperty('GGA_C_LYP')],
            'LDA': [XCFunctionalProperty('LDA_XC_TETER93')],
            'PADE': [XCFunctionalProperty('LDA_XC_TETER93')],
            'PBE': [XCFunctionalProperty('GGA_X_PBE'), XCFunctionalProperty('GGA_C_PBE')],
            'OLYP': [XCFunctionalProperty('GGA_X_OPTX'), XCFunctionalProperty('GGA_C_LYP')],
            'HCTH120': [XCFunctionalProperty('GGA_XC_HCTH_120')],
            'PBE0': [XCFunctionalProperty('HYB_GGA_XC_PBEH')],
            'B3LYP': [XCFunctionalProperty('HYB_GGA_XC_B3LYP')],
            'TPSS': [XCFunctionalProperty('MGGA_X_TPSS'), XCFunctionalProperty('MGGA_C_TPSS')]}
        self._ensemble_map = {'NVE': 'NVE', 'NVT': 'NVT', 'NPT_F': 'NPT', 'NPT_I': 'NPT'}
        self._vdw_map = {
            "S. Grimme, JCC 27: 1787 (2006)": "G06",
            "S. Grimme et al, JCP 132: 154104 (2010)": "G10"}

        self._settings = None

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.inp_parser.mainfile = None
        self.traj_parser.mainfile = None
        self.velocities_parser.mainfile = None
        self.energy_parser.mainfile = None
        self.force_parser.mainfile = None
        self.out_parser.logger = self.logger
        self.inp_parser.logger = self.logger
        self.traj_parser.logger = self.logger
        self.velocities_parser.logger = self.logger
        self.energy_parser.logger = self.logger
        self.force_parser.logger = self.logger
        self._settings = None
        self._method = None
        self._calculation_type = None

    @property
    def settings(self):
        if self._settings is None:
            def to_dict(data, repeats=True):
                data_dict = dict()
                for key, val in data:
                    name = self._metainfo_name_map.get(key, key)
                    if not repeats and name in data_dict:
                        continue
                    data_dict.setdefault(name, [])
                    data_dict[name].append(val)
                for key, val in data_dict.items():
                    data_dict[key] = val[0] if len(val) == 1 else val
                return data_dict

            self._settings = dict()
            self._settings['dft'] = to_dict(
                self.out_parser.get(self._calculation_type, {}).get('dft', []))
            self._settings['qs'] = to_dict(
                self.out_parser.get(self._calculation_type, {}).get('qs', []))
            self._settings['vdw'] = to_dict(
                self.out_parser.get(self._calculation_type, {}).get('vdw', []))
            self._settings['dbcsr'] = to_dict(self.out_parser.get('dbcsr', []), False)
            self._settings['program'] = to_dict(self.out_parser.get('program', []))
            self._settings['cp2k'] = to_dict(self.out_parser.get('cp2k', []), False)
            self._settings['global'] = to_dict(self.out_parser.get('global', []), False)
            self._settings['md'] = to_dict(
                self.out_parser.get(self._calculation_type, {}).get('scf_parameters', {}).get('md', []))
            self._settings['md_setup'] = to_dict(self.out_parser.get(self._calculation_type, {}).get('scf_parameters', {}).get('md_setup', []))

        return self._settings

    def _normalize_filename(self, filename):
        if filename.startswith('='):
            filename = filename[1:]
        elif re.match(r'./', filename):
            filename = filename
        else:
            project_name = self.inp_parser.get('GLOBAL/PROJECT_NAME')
            if filename:
                filename = '%s-%s' % (project_name, filename)
            else:
                filename = project_name
        return filename

    def get_atomic_number(self, element):
        atomic_numbers = self.out_parser.get(
            self._calculation_type, {}).get('atomic_coordinates').atomic_numbers
        return atomic_numbers.get(element, 0)

    def get_ensemble_type(self, frame):
        if self.sampling_method != 'molecular_dynamics':
            return

        if frame == 0:
            return self.settings['md'].get('ensemble_type', '')
        else:
            calculation = self.out_parser.get(self._calculation_type, '')
            if not calculation:
                return calculation
            return calculation.molecular_dynamics.md_step[frame - 1].get('ensemble_type', '')

    def get_time_step(self):
        return self.settings['md'].get('time_step')

    def get_velocities(self, frame):
        if self.out_parser.get(self._calculation_type, {}).get('molecular_dynamics') is not None:
            return

        if self.velocities_parser.mainfile is None:
            frequency, filename = self.settings['md'].get('velocities', '0 none').split()
            frequency = int(frequency)
            if frequency == 0:
                filename = '%s-vel-1.xyz' % self.inp_parser.get('GLOBAL/PROJECT_NAME')
                frequency = 1

            self.velocities_parser.mainfile = os.path.join(self.maindir, filename)
            self.velocities_parser.units = resolve_unit(
                self.inp_parser.get('MOTION/PRINT/VELOCITIES/UNIT', 'bohr*au_t^-1'))
            self.velocities_parser._frequency = frequency

        if self.get_ensemble_type(frame).lower() == 'REFTRAJ':
            frame -= 1

        if frame % self.velocities_parser._frequency != 0 or frame < 0:
            return

        try:
            return self.velocities_parser.trajectory[frame // self.velocities_parser._frequency]
        except Exception:
            self.logger.error('Error reading velocities.')

    def get_trajectory(self, frame):
        trajectory = None

        if frame == 0:
            coord = self.inp_parser.get('FORCE_EVAL/SUBSYS/COORD/DEFAULT_KEYWORD')
            units = resolve_unit(self.inp_parser.get('FORCE_EVAL/SUBSYS/COORD/UNIT', 'angstrom'))
            if coord is None:
                coord_filename = self.inp_parser.get('FORCE_EVAL/SUBSYS/TOPOLOGY/COORD_FILE_NAME', '')
                self.traj_parser.mainfile = os.path.join(self.maindir, coord_filename.strip())
                self.traj_parser.units = units
                if self.traj_parser.trajectory:
                    result = self.traj_parser.trajectory[0]
                    # reset for output trajectory
                    self.traj_parser.mainfile = None
                    trajectory = result

            else:
                coord = np.transpose([c.split() for c in coord])
                positions = np.array(coord[1:4], dtype=float).T * units
                scaled = 'T' in self.inp_parser.get('FORCE_EVAL/SUBSYS/COORD/SCALED', 'False')
                if scaled:
                    trajectory = Trajectory(labels=coord[0], scaled_positions=positions)
                else:
                    trajectory = Trajectory(labels=coord[0], positions=positions)

        if trajectory is not None:
            return trajectory

        if self.traj_parser.mainfile is None:
            # try to get it from md
            frequency, filename = self.settings['md'].get('coordinates', '0 none').split()
            frequency = int(frequency)
            if frequency == 0:
                filename = self.inp_parser.get('MOTION/PRINT/TRAJECTORY/FILENAME', '').strip()
                filename = self._normalize_filename(filename)
                traj_format = self.inp_parser.get('MOTION/PRINT/TRAJECTORY/FORMAT', 'XYZ').strip()
                traj_format = self._file_extension_map.get(traj_format, 'xyz')
                filename = '%s-pos-1.%s' % (filename, traj_format)
                frequency = 1

            self.traj_parser.mainfile = os.path.join(self.maindir, filename)
            self.traj_parser.units = resolve_unit(
                self.inp_parser.get('MOTION/PRINT/TRAJECTORY/UNIT', 'angstrom'))
            self.traj_parser._frequency = frequency

        if self.get_ensemble_type(frame) == 'REFTRAJ':
            frame -= 1

        if frame % self.traj_parser._frequency != 0 or frame < 0:
            return

        try:
            return self.traj_parser.trajectory[frame // self.traj_parser._frequency]
        except Exception:
            self.logger.error('Error reading trajectory.')

    def get_lattice_vectors(self, frame):
        lattice_vectors = None

        if frame == 0:
            lattice_vectors = self.out_parser.get('lattice_vectors')
            if lattice_vectors is None:
                # get it from input
                cell = self.inp_parser.get('FORCE_EVAL/SUBSYS/CELL')
                # is this the unit for cell? how about for angles
                units = resolve_unit(
                    self.inp_parser.get('FORCE_EVAL/SUBSYS/COORD/UNIT', 'angstrom'))
                if cell is None:
                    return

                if 'A' in cell and 'B' in cell and 'C' in cell:
                    lattice_vectors = np.array([
                        cell.get(c).split() for c in ('A', 'B', 'C')], dtype=float) * units
                elif 'ABC' in cell:
                    abc = (np.array(
                        cell.get('ABC').split(), dtype=float) * units).to('angstrom').magnitude
                    angles = np.array(cell.get('ALPHA_BETA_GAMMA', '90. 90. 90.').split(), dtype=float)
                    lattice_vectors = ase.geometry.cellpar_to_cell(np.hstack((abc, angles))) * ureg.angstrom

            else:
                units = resolve_unit(
                    self.inp_parser.get('FORCE_EVAL/SUBSYS/COORD/UNIT', 'angstrom'))
                lattice_vectors = np.array(lattice_vectors[:3], dtype=np.float64) * units

        if lattice_vectors is not None:
            return lattice_vectors

        if self.cell_parser.mainfile is None:
            frequency, filename = self.settings['md'].get('simulation_cell', '0 none').split()
            frequency = int(frequency)
            if frequency == 0:
                # TODO test this I cannot find a sample output cell filee
                filename = self.inp_parser.get('MOTION/PRINT/CELL/FILENAME', '').strip()
                frequency = 1

            if filename:
                self.cell_parser.mainfile = os.path.join(self.maindir, filename)
                self.cell_parser.units = resolve_unit(
                    self.inp_parser.get('MOTION/PRINT/TRAJECTORY/UNIT', 'angstrom'))
                self.cell_parser._frequency = frequency
            else:
                if self.sampling_method == 'molecular_dynamics':
                    # check that this is not an NPT
                    ensemble_type = self.get_ensemble_type(frame)
                    if ensemble_type[:3] == 'NPT':
                        return
                return self.get_lattice_vectors(0)

        if self.get_ensemble_type(frame) == 'REFTRAJ':
            frame -= 1

        if frame % self.cell_parser._frequency != 0 or frame < 0:
            return

        try:
            return self.cell_parser.data[frame // self.cell_parser._frequency] * resolve_unit(self.cell_parser.units)
        except Exception:
            self.logger.error('Error reading lattice vectors.')

    def get_md_output(self, frame):
        if self.energy_parser.mainfile is None:
            frequency, filename = self.settings['md'].get('energies', '0, none').split()
            frequency = int(frequency)
            if frequency == 0:
                return dict()
            self.energy_parser.mainfile = os.path.join(self.maindir, filename)
            self.energy_parser._frequency = frequency

        if self.get_ensemble_type(frame) == 'REFTRAJ':
            frame -= 1

        if frame % self.energy_parser._frequency != 0 or frame < 0:
            return dict()

        try:
            data = self.energy_parser.data[frame // self.energy_parser._frequency]
            return dict(
                step=data[0],
                time=data[1] * ureg.femtosecond,
                kinetic_energy_instantaneous=data[2] * ureg.hartree,
                temperature_instantaneous=data[3],
                potential_energy_instantaneous=data[4] * ureg.hartree,
                conserved_quantity=data[5] * ureg.hartree,
                cpu_time_instantaneous=data[6])

        except Exception:
            self.logger.error('Error reading MD energies.')

    def get_forces(self, frame):
        filename = self.inp_parser.get('FORCE_EVAL/PRINT/FORCES/FILENAME', '').strip()
        filename = self._normalize_filename(filename)
        filename = '%s-1_%d.xyz' % (filename, frame)
        self.force_parser.mainfile = os.path.join(self.maindir, filename)
        return self.force_parser.get('atom_forces')

    def get_xc_functionals(self):
        functionals = self.inp_parser.get('FORCE_EVAL/DFT/XC/XC_FUNCTIONAL/VALUE')
        if functionals is None or functionals == 'NO_SHORTCUT':
            functional_values = self.inp_parser.get('FORCE_EVAL/DFT/XC/XC_FUNCTIONAL', {})
            functionals = []
            for name, attrib in functional_values.items():
                name = name.upper()
                if name == 'VALUE':
                    continue
                # get xc_func from mapping then apply read attributes
                # if func is not in mapping, create it
                values = self._xc_functional_map.get(name, [XCFunctionalProperty(name)])
                for n, value in enumerate(values):
                    weight = attrib.get('SCALE_X', None) if n == 0 else attrib.get('SCALE_C', None)
                    value._data.update({'weight': weight})
                functionals.extend(values)
        else:
            names = [functionals] if not isinstance(functionals, list) else functionals
            functionals = []
            for name in names:
                name = name.upper()
                if name not in self._xc_functional_map:
                    self.logger.error('Cannot resolve xc functional')
                    continue
                functionals.extend(self._xc_functional_map.get(name))

        return functionals

    def parse_scc(self, source):
        if source is None:
            return

        sec_scc = self.archive.run[-1].m_create(Calculation)

        sec_energy = sec_scc.m_create(Energy)
        if source.get('energy_total') is not None:
            sec_energy.total = EnergyEntry(value=source.get('energy_total'))
        if source.get('electronic_kinetic_energy') is not None:
            sec_energy.kinetic_electronic = EnergyEntry(value=source.get('electronic_kinetic_energy')[-1])
        if source.get('exchange_correlation_energy') is not None:
            sec_energy.xc = EnergyEntry(value=source.get('exchange_correlation_energy')[-1])

        if source.get('stress_tensor') is not None:
            sec_stress = sec_scc.m_create(Stress)
            sec_stress.total = StressEntry(value=source.get('stress_tensor'))

        # self consistency
        for iteration in source.get('iteration', []):
            sec_scf = sec_scc.m_create(ScfIteration)
            sec_scf_energy = sec_scf.m_create(Energy)
            for key, val in iteration.items():
                if val is not None:
                    if key == 'energy_change':
                        sec_scf_energy.change = val
                    elif key.startswith('energy_'):
                        sec_scf_energy.m_add_sub_section(getattr(
                            Energy, key.replace('energy_', '')), EnergyEntry(value=val))
                    else:
                        setattr(sec_scf, key, val)

        atom_forces = source.get('atom_forces', self.get_forces(source._frame))
        if atom_forces is not None:
            atom_forces = np.array(atom_forces, np.float64) * ureg.hartree / ureg.bohr
            sec_forces = sec_scc.m_create(Forces)
            sec_forces.total = ForcesEntry(value=atom_forces)

        # TODO add dos
        return sec_scc

    def parse_system(self, trajectory):

        trajectory = 0 if trajectory is None else trajectory

        if isinstance(trajectory, int):
            frame = trajectory
            trajectory = self.get_trajectory(frame)
            if trajectory is not None:
                trajectory._frame = frame

        if trajectory is None:
            return

        sec_system = self.archive.run[-1].m_create(System)
        sec_atoms = sec_system.m_create(Atoms)

        lattice_vectors = self.get_lattice_vectors(trajectory._frame)

        if trajectory.positions is not None:
            sec_atoms.positions = trajectory.positions
        elif trajectory.scaled_positions is not None and lattice_vectors is not None:
            sec_atoms.positions = np.dot(trajectory.scaled_positions, lattice_vectors)

        labels = trajectory.labels if trajectory.labels is not None else self.out_parser.get(
            self._calculation_type).get('atomic_coordinates')
        if labels is not None:
            sec_atoms.labels = labels

        if lattice_vectors is not None:
            sec_atoms.lattice_vectors = lattice_vectors
            periodic = self.inp_parser.get('FORCE_EVAL/SUBSYS/CELL/PERIODIC', 'xyz').lower()
            sec_atoms.periodic = [v in periodic for v in ('x', 'y', 'z')]

        # TODO test this I cannot find an example
        # velocities
        if self.sampling_method == 'molecular_dynamics':
            velocities = self.get_velocities(trajectory._frame)
            if velocities is not None:
                sec_atoms.velocities = velocities

        return sec_system

    def parse_configurations_quickstep(self):
        sec_run = self.archive.run[-1]
        quickstep = self.out_parser.get(self._calculation_type)

        # quickstep extension to scc quantities
        def parse_quickstep_calculation(source):
            if source is None:
                return
            sec_quickstep_calc = sec_run.m_create(x_cp2k_section_quickstep_calculation)
            for key in ['energy_total', 'atom_forces']:
                val = source.get(key)
                if val is not None:
                    setattr(sec_quickstep_calc, 'x_cp2k_%s' % key, val)
                sec_quickstep_calc.x_cp2k_quickstep_converged = source.get('converged') is not None

            if source.get('electronic_kinetic_energy') is not None:
                sec_quickstep_calc.x_cp2k_electronic_kinetic_energy = source.get('electronic_kinetic_energy')[-1]

            for iteration in source.get('iteration', []):
                sec_scf = sec_quickstep_calc.m_create(x_cp2k_section_scf_iteration)
                for key, val in iteration.items():
                    if val is not None:
                        setattr(sec_scf, 'x_cp2k_%s' % key, val)

            if source.stress_tensor is not None:
                sec_stress = sec_quickstep_calc.m_create(x_cp2k_section_stress_tensor)
                if source.stress_tensor_one_third_of_trace is not None:
                    val = source.stress_tensor_one_third_of_trace
                    sec_stress.stress_tensor_one_third_of_trace = val.to('pascal').magnitude
                if source.stress_tensor_determinant is not None:
                    sec_stress.stress_tensor_determinant = val.to('pascal**3').magnitude
                if source.stress_eigenvalues_eigenvectors is not None:
                    val = source.stress_eigenvalues_eigenvectors
                    sec_stress.x_cp2k_stress_tensor_eigenvalues = val[0].to('pascal').magnitude
                    sec_stress.x_cp2k_stress_tensor_eigenvectors = val[1]

        def parse_md_step(source):
            # we put md output in scc, originally in frame sequence
            # TODO put in workflow
            md_output = self.get_md_output(source._frame)
            md_output = md_output if md_output else source
            calc = sec_run.calculation[-1]

            # Store to common metainfo
            energy_kinetic = md_output.get("kinetic_energy_instantaneous")
            if energy_kinetic:
                calc.energy.kinetic = EnergyEntry(value=energy_kinetic.to('joule'))
            potential_energy = md_output.get("potential_energy_instantaneous")
            if potential_energy:
                calc.energy.potential = EnergyEntry(value=potential_energy.to('joule'))
            step = int(md_output.get("step"))
            if step:
                calc.step = step
            time = md_output.get("time")
            if time:
                calc.time = time.to('second')
            volume = md_output.get("volume_instantaneous")
            if volume:
                calc.volume = volume.to('m**3')
            pressure = md_output.get("pressure_instantaneous")
            if pressure:
                calc.pressure = pressure.to('m**3')
            temperature = md_output.get("temperature_instantaneous")
            if temperature:
                calc.temperature = temperature

        def parse_calculations(calculations):
            for n, calculation in enumerate(calculations):
                self_consistent = calculation.get('self_consistent', [])
                self_consistent = [self_consistent] if not isinstance(self_consistent, list) else self_consistent
                # there may be several wave function optimizations in a calculation
                for scf in self_consistent:
                    parse_quickstep_calculation(scf)

                # write only the last one to scc
                scf = self_consistent[-1] if self_consistent else calculation
                scf._frame = n
                sec_scc = self.parse_scc(scf)
                if calculation.get('ensemble_type') is not None:
                    calculation._frame = n
                    parse_md_step(calculation)

                if n == 0:
                    atomic_coord = quickstep.get('atomic_coordinates')
                    if atomic_coord is not None:
                        atomic_coord._frame = 0
                    sec_system = self.parse_system(atomic_coord)
                else:
                    sec_system = self.parse_system(n)

                if sec_system is not None:
                    sec_scc.single_configuration_calculation_to_system_ref = sec_system

            sec_scc.single_configuration_to_calculation_method_ref = sec_run.method[-1]

        single_point = quickstep.get('single_point')
        if single_point is not None:
            parse_calculations([single_point])

        geometry_optimization = quickstep.get('geometry_optimization')
        if geometry_optimization is not None:
            # initial self consistent
            optimization_steps = [geometry_optimization]
            optimization_steps.extend(geometry_optimization.get('optimization_step', []))
            parse_calculations(optimization_steps)

        molecular_dynamics = quickstep.get('molecular_dynamics')
        if molecular_dynamics is not None:
            md_steps = [molecular_dynamics]
            md_steps.extend(molecular_dynamics.get('md_step', []))
            parse_calculations(md_steps)

    def parse_method_quickstep(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        sec_basis = sec_method.m_create(BasisSet)
        sec_basis.kind = 'wavefunction'
        sec_basis.type = 'gaussians'

        planewave_cutoff = self.settings.get('qs', {}).get('planewave_cutoff', None)
        if planewave_cutoff is not None:
            sec_basis_cell = sec_basis.m_create(BasisSetCellDependent)
            sec_basis_cell.planewave_cutoff = planewave_cutoff * ureg.hartree

        atoms = self.out_parser.get(
            self._calculation_type, {}).get('atomic_kind_information', {}).get('atom', [])
        for atom in atoms:
            basis_set = atom.get('kind_basis_set_name', None)
            if basis_set is not None:
                sec_basis_atom = sec_basis.m_create(BasisSetAtomCentered)
                sec_basis_atom.atom_number = self.get_atomic_number(atom.kind_label)
                sec_basis_atom.name = basis_set

        quickstep = self.out_parser.get(self._calculation_type)

        sec_dft = sec_method.m_create(DFT)
        # electronic structure method
        # TODO include methods
        if quickstep.get('dft') is not None:
            sec_method.electronic = Electronic(method='DFT')
        elif quickstep.get('dft_u') is not None:
            sec_method.electronic = Electronic(method='DFT+U')
        elif quickstep.get('mp2') is not None:
            sec_method.electronic = Electronic(method='MP2')
        elif quickstep.get('rpa') is not None:
            sec_method.electronic = Electronic(method='RPA')

        # xc functionals
        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for functional in self.get_xc_functionals():
            if '_X_' in functional.name:
                sec_xc_functional.exchange.append(Functional(
                    name=functional.name, weight=functional.weight))
            elif '_C_' in functional.name:
                sec_xc_functional.correlation.append(Functional(
                    name=functional.name, weight=functional.weight))
            else:
                sec_xc_functional.contributions.append(Functional(
                    name=functional.name, weight=functional.weight))

        # van der Waals settings
        # TODO test this no example, add parameter, put in main metainfo
        vdw = self.settings['vdw']
        if vdw:
            sec_vdw = sec_method.m_create(x_cp2k_section_vdw_settings)
            for key, val in vdw.items():
                if val == '':
                    setattr(sec_vdw, 'x_cp2k_vdw_name', key)
                    vdw_name = self._vdw_map.get(key, None)
                    if vdw_name is not None:
                        sec_method.van_der_Waals_method = vdw_name
                else:
                    setattr(sec_vdw, 'x_cp2k_vdw_%s' % key, val)

        stress_method = self.inp_parser.get('FORCE_EVAL/STRESS_TENSOR')
        if stress_method is not None:
            sec_method.stress_tensor_method = stress_method.replace('_', ' ').title()

        sec_quickstep_settings = sec_method.m_create(x_cp2k_section_quickstep_settings)
        if self.settings['dft']:
            for key, val in self.settings['dft'].items():
                section = sec_dft
                if key == 'self_interaction_correction_method':
                    val = self._self_interaction_map.get(val, None)
                elif key == 'spin_restriction':
                    section = sec_quickstep_settings
                    key = 'x_cp2k_%s' % key
                if val is None:
                    continue
                setattr(section, key, val)
        if self.settings['qs']:
            for key, val in self.settings['qs'].items():
                setattr(sec_quickstep_settings, 'x_cp2k_%s' % key, val)

        atomic_kind_info = quickstep.get('atomic_kind_information', None)
        if atomic_kind_info is not None:
            sec_atom_kinds = sec_quickstep_settings.m_create(x_cp2k_section_atomic_kinds)
            for atom in atomic_kind_info.get('atom', []):
                # why necessary to make a separate section
                sec_atom_kind = sec_atom_kinds.m_create(x_cp2k_section_atomic_kind)
                sec_kind_basis_set = sec_atom_kind.m_create(x_cp2k_section_kind_basis_set)
                for key, val in atom.items():
                    if val is None:
                        continue
                    if key in ['kind_label', 'kind_number_of_atoms']:
                        setattr(sec_atom_kind, 'x_cp2k_%s' % key, str(val))
                    else:
                        setattr(sec_kind_basis_set, 'x_cp2k_%s' % key, val)

                sec_method_atom_kind = sec_method.m_create(AtomParameters)
                sec_method_atom_kind.label = atom.kind_label
                sec_method_atom_kind.atom_number = self.get_atomic_number(atom.kind_label)

        total_maximum_numbers = quickstep.get('total_maximum_numbers', None)
        if total_maximum_numbers is not None:
            sec_total = sec_quickstep_settings.m_create(x_cp2k_section_total_numbers)
            sec_maximum = sec_quickstep_settings.m_create(x_cp2k_section_maximum_angular_momentum)
            for key, val in total_maximum_numbers.items():
                if val is None:
                    continue
                if key in ['orbital_basis_functions', 'local_part_of_gth_pseudopotential', 'non_local_part_of_gth_pseudopotential']:
                    setattr(sec_maximum, 'x_cp2k_%s' % key, val)
                else:
                    setattr(sec_total, 'x_cp2k_%s' % key, val)

        sec_scf = sec_method.m_create(Scf)
        scf_parameters = quickstep.get('scf_parameters', None)
        if scf_parameters is not None:
            for key, val in scf_parameters.items():
                if val is None:
                    continue
                setattr(sec_scf, key, val)

    @property
    def sampling_method(self):
        if self._method is None:
            quickstep = self.out_parser.get(self._calculation_type, {})
            for method in ['single_point', 'geometry_optimization', 'molecular_dynamics']:
                if quickstep.get(method) is not None:
                    self._method = method
        return self._method

    def parse_workflow(self):
        # TODO add vdW
        sec_workflow = self.archive.m_create(Workflow)
        sec_workflow.type = self.sampling_method
        workflow = None

        if self.sampling_method == 'geometry_optimization':
            sec_geometry_optimization = sec_workflow.m_create(GeometryOptimization)
            workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
            optimization = self.out_parser.get(self._calculation_type).geometry_optimization
            if optimization.method is not None:
                method = self._optimization_method_map.get(optimization.method, '')
                if not method:
                    self.logger.error('Cannot resolve optimization method.')
                sec_geometry_optimization.method = method
                workflow.method.method = method
            sec_geometry_opt = sec_workflow.m_create(x_cp2k_section_geometry_optimization)
            for step in optimization.get('optimization_step', []):
                information = step.information
                if information is None:
                    continue
                sec_geometry_opt_step = sec_geometry_opt.m_create(x_cp2k_section_geometry_optimization_step)
                for key, val in information.items():
                    if val is None:
                        continue

                    name = self._metainfo_name_map.get(key, key)
                    if name.startswith('energy') and isinstance(val, float):
                        val = (val * ureg.hartree).to('joule').magnitude
                    elif 'step_size' in name and isinstance(val, float):
                        val = (val * ureg.bohr).to('m').magnitude
                    elif 'gradient' in name and isinstance(val, float):
                        val = (val * ureg.hartree / ureg.bohr).to('joule/m').magnitude
                    elif isinstance(val, str):
                        val = val.strip()

                    setattr(sec_geometry_opt_step, 'x_cp2k_optimization_%s' % name, val)

            if sec_geometry_opt.x_cp2k_section_geometry_optimization_step:
                geometry_change = sec_geometry_opt_step.x_cp2k_optimization_step_size_convergence_limit
                if geometry_change is not None:
                    sec_geometry_optimization.convergence_tolerance_displacement_maximum = geometry_change
                    workflow.method.convergence_tolerance_displacement_maximum
                threshold_force = sec_geometry_opt_step.x_cp2k_optimization_gradient_convergence_limit
                if threshold_force is not None:
                    sec_geometry_optimization.convergence_tolerance_force_maximum = threshold_force
                    workflow.method.convergence_tolerance_force_maximum = threshold_force

        elif self.sampling_method == 'molecular_dynamics':
            # Parse common MD information
            sec_md = sec_workflow.m_create(MolecularDynamics)
            workflow = MolecularDynamics2(method=MolecularDynamicsMethod())
            workflow.method.thermodynamic_ensemble = self._ensemble_map.get(self.get_ensemble_type(0), None)
            sec_md.thermodynamic_ensemble = self._ensemble_map.get(self.get_ensemble_type(0), None)
            sec_md.integration_timestep = self.get_time_step()
            workflow.method.integration_timestep = self.get_time_step()
            sec_md_settings = sec_workflow.m_create(x_cp2k_section_md_settings)

            # Parse code specific MD information
            ignored = {'time_step', 'ensemble_type', 'file_type'}
            for key, val in self.settings['md'].items():
                if val is None or key in ignored:
                    continue
                if key in ['coordinates', 'simulation_cell', 'velocities', 'energies', 'dump']:
                    val = val.split()
                    setattr(sec_md_settings, 'x_cp2k_md_%s_print_frequency' % key, int(val[0]))
                    setattr(sec_md_settings, 'x_cp2k_md_%s_filename' % key, val[1])
                elif key == 'print_frequency':
                    setattr(sec_md_settings, 'x_cp2k_md_%s' % key, int(val.split()[0]))
                else:
                    setattr(sec_md_settings, 'x_cp2k_md_%s' % key, val)

        self.archive.workflow2 = workflow

    def parse_input(self):
        # TODO include extended input
        input_filename = self.settings['cp2k'].get('input_filename', None)
        if input_filename is None:
            return

        definitions = dict(m_env.all_definitions_by_name)

        def resolve_definition(name):
            return definitions.get(name, [None])[0]

        def override_keyword(name):
            # override keys to be compatible with metainfo name
            # TODO change metainfo name
            if name.endswith('_VALUE'):
                return name.replace('VALUE', 'SECTION_PARAMETERS')
            elif name.endswith('KIND_RI_AUX_BASIS'):
                return name.replace('BASIS', 'BASIS_SET')
            return name

        def parse(name, data, section):
            if isinstance(data, InpValue):
                sec_def = resolve_definition(name)
                if sec_def is not None:
                    sub_section = section.m_create(sec_def.section_cls)
                    for key, val in data.items():
                        sec_name = '%s_%s' % (name, key)
                        parse(sec_name, val, sub_section)

            elif isinstance(data, list) and data:
                for val in data:
                    parse(name, val, section)

            else:
                name = name.replace('_section', '')
                name = override_keyword(name)
                quantity_def = resolve_definition(name)
                if quantity_def is not None:
                    setattr(section, name, quantity_def.type(data))

        self.inp_parser.mainfile = os.path.join(self.maindir, input_filename)
        if self.inp_parser.tree is None:
            return

        parse('x_cp2k_section_input', self.inp_parser.tree, self.archive.run[-1])

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        # identify calculation type, TODO add more
        calculation_types = ['quickstep', 'qs_dftb']
        for calculation_type in calculation_types:
            if self.out_parser.get(calculation_type) is not None:
                self._calculation_type = calculation_type
                break

        sec_run = self.archive.m_create(Run)
        version = self.settings['cp2k']['program_version']
        host = self.settings['cp2k']['program_compilation_host']
        sec_run.program = Program(
            name='CP2K', version=version[0] if isinstance(version, list) else version,
            compilation_host=host[0] if isinstance(host, list) else host)

        if self.settings['dbcsr']:
            sec_dbcsr = sec_run.m_create(x_cp2k_section_dbcsr)
            for key, val in self.settings['dbcsr'].items():
                setattr(sec_dbcsr, 'x_cp2k_%s' % key, val)

        if self.settings['program']:
            sec_startinformation = sec_run.m_create(x_cp2k_section_startinformation)
            sec_endinformation = sec_run.m_create(x_cp2k_section_end_information)
            section = sec_startinformation
            for key, val in self.settings['program'].items():
                if key == 'id' and isinstance(val, list):
                    sec_endinformation.x_cp2k_end_id = val[1]
                    key, val = 'start_id', val[0]
                section = sec_endinformation if key.startswith('end') else sec_startinformation
                val = val[0] if isinstance(val, list) else val
                setattr(section, 'x_cp2k_%s' % key, val)

        if self.settings['cp2k']:
            sec_program_information = sec_run.m_create(x_cp2k_section_program_information)
            for key, val in self.settings['cp2k'].items():
                if key == 'svn_revision':
                    try:
                        val = int(val.strip('svn:'))
                    except Exception:
                        continue
                setattr(sec_program_information, 'x_cp2k_%s' % key, val)

        if self.settings['global']:
            sec_global_settings = sec_run.m_create(x_cp2k_section_global_settings)
            for key, val in self.settings['global'].items():
                setattr(sec_global_settings, 'x_cp2k_%s' % key, val)

        restart = self.out_parser.get('restart')
        if restart is not None:
            sec_restart = sec_run.m_create(x_cp2k_section_restart_information)
            sec_restart.x_cp2k_restart_file_name = restart.get('filename')
            sec_restart.x_cp2k_restarted_quantity_name = ' '.join(restart.get('quantities'))

        self.parse_input()

        if self._calculation_type in ['quickstep', 'qs_dftb']:
            self.parse_method_quickstep()
            self.parse_configurations_quickstep()

        self.parse_workflow()
