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

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    Functional, Method, DFT, Electronic, XCFunctional, Smearing,
    BasisSetCellDependent, BasisSet, AtomParameters
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, Thermodynamics, Stress,
    StressEntry, Charges, ChargesValue, ScfIteration, BandStructure, BandEnergies,
    VibrationalFrequencies, VibrationalFrequenciesValues
)
from nomad.datamodel.metainfo.workflow import (
    Workflow, GeometryOptimization, MolecularDynamics
)
from nomad.datamodel.metainfo.simulation.workflow import (
    GeometryOptimization as GeometryOptimization2, GeometryOptimizationMethod,
    MolecularDynamics as MolecularDynamics2, MolecularDynamicsMethod
)

from .metainfo.castep import x_castep_section_phonons, x_castep_section_scf_parameters,\
    x_castep_section_density_mixing_parameters, x_castep_section_population_analysis_parameters,\
    x_castep_section_core_parameters, x_castep_section_band_parameters,\
    x_castep_section_ts_parameters, x_castep_section_optics_parameters,\
    x_castep_section_electronic_spectroscpy_parameters, x_castep_section_tddft_parameters,\
    x_castep_section_atom_positions, x_castep_section_vibrational_frequencies,\
    x_castep_section_tddft, x_castep_section_DFT_SEDC,\
    x_castep_section_van_der_Waals_parameters, x_castep_section_time, x_castep_section_raman_tensor


# TODO map all castep units
units_map = {
    'A': ureg.angstrom, 'amu': ureg.amu, 'ps': ureg.ps, 'e': ureg.e, 'eV': ureg.eV,
    'K': ureg.K, 'GPa': ureg.GPa, 'hbar': ureg.hbar, 'cm': ureg.cm, 'D': ureg.D,
    'mol': ureg.mol, 'J': ureg.J, 'atom': 1, 'steps': 1, 'iterations': 1}


def resolve_unit(unit_str, parts=[]):
    unit_str = unit_str.replace(' ', '')
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


class CellParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_block(val_in):
            val = val_in.split('\n')
            key = val[0].strip().lower()
            return key, [v.split() for v in val[1:] if v and v[0] not in ('#', '!')]

        def str_to_value(val_in):
            key, val = val_in.split(' ', 1)
            return key.strip().lower(), val

        self._quantities = [
            Quantity(
                'block',
                r'\s\%(?:block|BLOCK)\s*([\s\S]+?)\%(?:endblock|ENDBLOCK)',
                str_operation=str_to_block, repeats=True),
            Quantity(
                'value',
                r'\s(\w.+?)\s*:\s*([^\n]+)', str_operation=str_to_value, repeats=True)]

    def get_value(self, key, default=None):
        for source in ['value', 'block']:
            for val in self.get(source, []):
                if val[0] == key:
                    return val[1]
        return default


class BandsParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_kpt_energies(val_in):
            val = [v.split() for v in val_in.split('\n')]
            kpt = np.array(val[0][:3], dtype=np.dtype(np.float64))
            energies = np.array([v[0] for v in val if len(v) == 1], dtype=np.dtype(np.float64))
            return kpt, energies

        self._quantities = [
            Quantity('n_kpoints', r'Number of k-points\s*(\d+)', dtype=np.int32),
            Quantity('n_spins', r'Number of spin components\s*(\d+)', dtype=np.int32),
            Quantity('n_electrons', r'Number of electrons\s*([\d\. ]+)', dtype=np.float64),
            Quantity('n_eigenvalues', r'Number of eigenvalues\s*([\d\. ]+)', dtype=np.float64),
            Quantity(
                'fermi_energies',
                r'Fermi energies \(in atomic units\)\s*([\d\.\- ]+)',
                dtype=np.float64, units=ureg.hartree),
            Quantity(
                'kpt_energies',
                r'point\s*\d+\s*([\s\S]+?)(?:K\-|\Z)',
                repeats=True, str_operation=str_to_kpt_energies, convert=False)]


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_float = r'[\d\.\-\+Ee]+'

        def str_to_title(val_in):
            def add_unit(val):
                val_unit = val.rsplit(' ', 1)
                if len(val_unit) == 2:
                    try:
                        val_str = val_unit[1].strip()
                        unit = resolve_unit(val_str)
                        units_map[val_str] = unit
                        val = float(val_unit[0]) * unit
                    except Exception:
                        pass
                return val

            re_section = re.compile(r' *\*+ *(.+?) *\*+ *')
            re_value = re.compile(r' *(.+?)\s*:\s*(.+)')
            title = dict()
            # necessary to cache last quantity for multi-line values such as custom xc func
            last_parameter = []
            for line in val_in.split('\n'):
                section = re_section.match(line)
                if section:
                    key = section.group(1).lower()
                    title[key] = dict()
                    continue
                value = re_value.match(line)
                if value:
                    sub_key = value.group(1).strip().lower()
                    if sub_key not in title[key]:
                        title[key][sub_key] = []
                    val = value.group(2).strip().strip(':')  # misformattig of custom xc func
                    if not val:
                        last_parameter = [sub_key, []]
                        continue
                    title[key][sub_key].append(add_unit(val))
                    if last_parameter:
                        title[key][last_parameter[0]].extend(last_parameter[1])
                        last_parameter = []
                elif line and last_parameter:
                    last_parameter[1].append(add_unit(line.strip()))

            for key in title.keys():
                for sub_key, val in title[key].items():
                    title[key][sub_key] = val[0] if len(val) == 1 else val

            return title

        def str_to_lattice_vectors(val_in):
            val = val_in.strip().split('\n')
            val = np.array([v.split() for v in val[1:]], dtype=np.dtype(np.float64)).T
            return [val[0:3].T, val[3:6].T]

        def str_to_lattice_parameters(val_in):
            re_parameter = rf'(\w+)\s*=\s*({re_float})'
            parameters = {p[0]: float(p[1]) for p in re.findall(re_parameter, val_in)}
            return parameters

        def str_to_array(val_in):
            val = [v.strip().strip('x').strip('*').split() for v in val_in.split('\n')]
            val = np.transpose([[vi.split('(')[0] for vi in v] for v in val if len(v) == 5])
            array = np.array(val[-3:], dtype=np.dtype(np.float64)).T
            return val[0], array

        def str_to_kpt_energies(val_in):
            spin = re.search(r'Spin=(\d+)', val_in)
            spin = int(spin.group(1)) if spin else 1
            kpt = re.search(r'kpt=\s*\d+\s*\(([\d\.\- ]+)\)', val_in)
            kpt = np.array(kpt.group(1).split(), dtype=np.dtype(np.float64)) if kpt else [0., 0., 0.]
            re_energies = re.compile(rf'\+\s*\d+\s*({re_float})\s*\+')
            energies = re.findall(re_energies, val_in)
            if energies:
                energies = np.array(energies, dtype=np.dtype(np.float64))
            return spin, kpt, energies

        def str_to_scf(val_in):
            result = []
            for val in val_in.strip().split('\n'):
                val = val.split()
                if not val:
                    continue
                if val[0].isdecimal() or val[0] == 'Initial':
                    val = val[:-2]
                    if val[0] == 'Initial':
                        val.insert(-1, 0.0)
                    result.append(val[1:])
            return np.array(result, dtype=np.dtype(np.float64))

        def str_to_md_data(val_in):
            re_data = re.compile(rf'x\s*(.+?):\s*({re_float})\s*(\w+)')
            data = dict()
            for val in val_in.split('\n'):
                val = re_data.search(val)
                if val:
                    data[val.group(1).strip()] = float(val.group(2)) * units_map.get(val.group(3), 1)
            return data

        def str_to_energy(val_in):
            key, val = val_in.split('=', 1)
            val = val.split()
            try:
                unit = resolve_unit(val[1])
                units_map[val[1]] = unit
                unit = unit if unit else 1
            except Exception:
                unit = 1
            return key.strip(), float(val[0]) * unit

        def str_to_mulliken(val_in):
            val = [v.split() for v in val_in.split('\n')]
            keys = [v for v in val[0] if not v.startswith('(')]
            return {key: [v[n] for v in val[1:] if len(v) == len(keys)] for n, key in enumerate(keys)}

        def str_to_vibrational_frequencies(val_in):
            # replace keys to fit length of values
            val_in = re.sub(r'ir\s*intensity\s*active', 'ir_intensity ir_active', val_in)
            val_in = re.sub(r'raman\s*activity\s*active', 'raman_activity raman_active', val_in)
            val_in = re.sub(r'raman\s*active', 'raman_active', val_in)
            val_in = re.sub(r'Frequency', 'vibrational_frequencies', val_in)
            val = [v.strip(' +').split() for v in val_in.split('\n')]
            return {key: [v[n] for v in val[1:] if len(v) == len(val[0])] for n, key in enumerate(val[0])}

        system_quantities = [
            Quantity(
                'unit_cell',
                r'Unit Cell\s*\s*\-+([\s\S]+?)\-{20}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'lattice_vectors',
                        r'(Real.+\s*[\d\.\-\s]+)',
                        str_operation=str_to_lattice_vectors, convert=False),
                    Quantity(
                        'lattice_parameters',
                        r'(Lattice parameters.+[\s\S]+?\n *\n)',
                        str_operation=str_to_lattice_parameters, convert=False),
                    Quantity(
                        'cell_volume',
                        rf'Current cell volume\s*=\s*({re_float})')])),
            Quantity(
                'cell_contents',
                r'Cell Contents\s*\-+([\s\S]+?)\n *\n *\-{20}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'positions',
                        r'u\s*v\s*w\s*x([\s\S]+?)x{50}',
                        str_operation=str_to_array, convert=False),
                    Quantity(
                        'velocities',
                        r'Vx\s*Vy\s*Vz\s*x([\s\S]+?)x{50}',
                        str_operation=str_to_array, convert=False)])),
            Quantity(
                'species',
                r'Details of Species\s*\-+([\s\S]+?)\-{20}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'mass',
                        r'Mass of species in AMU\s*([\s\S]+?)\n *\n',
                        str_operation=lambda x: [v.split() for v in x.strip().split('\n')])])),
            Quantity(
                'dft_d',
                r'(Dispersion-correction scheme[\s\S]+?)\n *\n *\n',
                sub_parser=TextParser(quantities=[
                    Quantity('method', r'Dispersion\-correction scheme\s*\:\s*(\w+)'),
                    Quantity(
                        'parameter',
                        rf'Parameter\s*(\w+)\s*\:\s*({re_float})', repeats=True)]))]

        basic_quantities = [
            Quantity(
                'scf',
                r'(SCF loop.+\s*.+\s*\-+ \<\-\- SCF[\s\S]+?)\-{70}\s*\<\-\- SCF',
                str_operation=str_to_scf, convert=False),
            Quantity(
                'energy',
                rf'(.+?energy.+?\s*=\s*{re_float}\s*.+)\n',
                repeats=True, str_operation=str_to_energy, convert=False),
            Quantity('energy_total', rf'Final Total Energy\s*({re_float})', dtype=float),
            Quantity(
                'enthalpy',
                rf'(Final Enthalpy\s*=\s*{re_float}\s*.+)',
                str_operation=str_to_energy, convert=False),
            Quantity(
                'frequency',
                rf'(Final \<frequency\>\s*=\s*{re_float}\s*.+)',
                str_operation=str_to_energy, convert=False),
            Quantity(
                'forces',
                r'Forces \*+\s*([\s\S]+?)\*{20}',
                str_operation=str_to_array, convert=False),
            Quantity(
                'stress_tensor',
                r'Stress Tensor \*+\s*([\s\S]+?)\*{20}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'stress_tensor',
                        rf'\*\s*(?:x|y|z)\s*({re_float})\s*({re_float})\s*({re_float})',
                        repeats=True, dtype=np.dtype(np.float64)),
                    Quantity(
                        'pressure',
                        rf'\*\s*Pressure:\s*({re_float})', dtype=np.float64)])),
            Quantity(
                'mulliken',
                r'Atomic Populations \(Mulliken\)\s*\-+\s*([\s\S]+?)\n *\n',
                str_operation=str_to_mulliken),
            Quantity(
                'tddft',
                r'Time-Dependent DFT Calculation([\s\S]+?TDDFT calculation time.+)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        r'TDDFT iteration\:\s*(\d+).+?Time\:\s*([\d\.]+)', repeats=True),
                    Quantity(
                        'energies',
                        rf'(\d+)\s*({re_float})\s*({re_float})\s*\w+',
                        repeats=True, dtype=np.dtype(np.float64)),
                    Quantity(
                        'time',
                        r'TDDFT calculation time\:\s*([\d\.]+)')])),
            Quantity(
                'interaction_energy',
                r'SEDC PBC Interaction Energy([\s\S]+?NB dispersion corrected est.+)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy',
                        rf'\%\s*(.+?=\s*{re_float}\s*)\[(.+)\]',
                        repeats=True, str_operation=str_to_energy, convert=False),
                    Quantity(
                        'shell',
                        rf'\%\s*(\d+\s+{re_float}\s+{re_float}\s+{re_float})', repeats=True)]))]

        bandstructure_quantities = [
            Quantity(
                'fermi_energy',
                rf'Fermi energy for spin\s*(?:up|down)\s*electrons is:\s*({re_float})',
                repeats=True, dtype=np.float64),
            Quantity(
                'fermi_energy',
                rf'Fermi energy for spin-degenerate system:\s*({re_float})',
                repeats=True, dtype=np.float64),
            Quantity(
                'kpt_energies',
                r'(Spin=\d+ kpt=.+\s*\+ *\-+ *\+[\s\S]+?)(?:\-{50}|\Z)',
                repeats=True, str_operation=str_to_kpt_energies)]

        basis_set_correction_quantities = [
            Quantity(
                'iteration',
                r'(ulating total energy[\s\S]+?)(?:Calc|\Z)',
                repeats=True, sub_parser=TextParser(quantities=basic_quantities + [
                    Quantity(
                        'cutoff',
                        rf'Calculating total energy with cut-off of\s*([\d\.]+)',
                        dtype=np.float64)]))]

        md_quantities = basic_quantities + [
            Quantity(
                'md_data',
                r'MD Data:\s*x([\s\S]+?)x{50}',
                str_operation=str_to_md_data, convert=False),
            Quantity(
                'iteration',
                r'(Starting MD iteration\s*\d+[\s\S]+?)finished',
                repeats=True, sub_parser=TextParser(quantities=basic_quantities + system_quantities))]

        dmd_quantities = basic_quantities + [
            Quantity(
                'iteration',
                r'(Starting DMD iteration\s*\d+[\s\S]+?)finished',
                repeats=True, sub_parser=TextParser(quantities=basic_quantities + system_quantities))]

        di_quantities = basic_quantities + [
            Quantity(
                'iteration',
                r'(Starting DI iteration\s*\d+[\s\S]+?)finished',
                repeats=True, sub_parser=TextParser(quantities=basic_quantities + system_quantities))]

        tss_quantities = basic_quantities + [
            Quantity(
                'iteration',
                r'(SCF loop\s*Energy[\s\S]+?Energy\:.+)',
                repeats=True, sub_parser=TextParser(quantities=basic_quantities))]

        cg_refinement_quantities = basic_quantities + [
            Quantity(
                'iteration',
                r'(SCF loop\s*Energy[\s\S]+?NB est\. 0K energy.+)',
                repeats=True, sub_parser=TextParser(quantities=basic_quantities))]

        bfgs_iteration_quantities = basic_quantities + system_quantities + [
            Quantity(
                'spin_density',
                rf'Integrated Spin Density\s*=\s*({re_float})')]

        bfgs_quantities = basic_quantities + [
            Quantity(
                'iteration',
                r'(Starting BFGS iteration\s*\d+.+\s*\=+[\s\S]+?)\={70}',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        r'((?:starting|improving) iteration[\s\S]+?)BFGS:',
                        repeats=True, sub_parser=TextParser(quantities=bfgs_iteration_quantities))]))]

        self._quantities = system_quantities + [
            Quantity(
                'program_version',
                r'Welcome to (?:Academic Release|Materials Studio)\s*(\w*) version (\S+)'),
            Quantity(
                'program_compilation',
                r'Compiled for (\S+) on \w+,\s*([\w :]+)', flatten=False),
            Quantity('compiler', r'Compiler:\s*(.+)\n', flatten=False),
            Quantity('maths_library', r'MATHLIBS\s*:\s*(.+)\n', flatten=False),
            Quantity('fft_library', r'FFT Lib\s*:\s*(.+)\n', flatten=False),
            Quantity(
                'constants_reference',
                r'Fundamental constants values\s*:\s*(.+)\n', flatten=False),
            Quantity('run_start', r'Run started\: \w+,\s*([\w :]+)', flatten=False),
            Quantity('title', r'Title\s*\*+\s*([\s\S]+?)\*{75}', str_operation=str_to_title),
            # TODO verify this, I cannot find an example
            Quantity('dft_u', r'Units for (\w+) U values are'),
            Quantity(
                'calculation',
                r'(MEMORY AND SCRATCH DISK ESTIMATES PER[\s\S]+?(?:A BibTeX formatted|\Z))',
                sub_parser=TextParser(quantities=basic_quantities + [
                    Quantity(
                        'vibrational_frequencies',
                        r'\+\s*(N\s*Frequency\s*irrep[\s\S]+?)(?:\s*\+\s*\.{70}|\Z)',
                        repeats=True, str_operation=str_to_vibrational_frequencies),
                    Quantity(
                        'raman_tensor',
                        rf'Mode number\:\s*\d+ Raman tensor\s*Depolarisation Ratio.+'
                        rf'\s*\+\s*({re_float}\s*{re_float}\s*{re_float}).+'
                        rf'\s*\+\s*({re_float}\s*{re_float}\s*{re_float}).+'
                        rf'\s*\+\s*({re_float}\s*{re_float}\s*{re_float}).+',
                        repeats=True, str_operation=lambda x: np.reshape(
                            np.array(x.split(), dtype=np.dtype(np.float64)), (3, 3))),
                    Quantity(
                        'bandstructure',
                        r'(Fermi energy for spin[\s\S]+?Spin\=1[\s\S]+?)\=\=',
                        sub_parser=TextParser(quantities=bandstructure_quantities)),
                    Quantity(
                        'basis_set_correction',
                        r'(Calculating finite basis set correction with[\s\S]+?)'
                        r'(Total energy corrected for finite basis set.+)',
                        sub_parser=TextParser(quantities=basis_set_correction_quantities)),
                    Quantity(
                        'tss',
                        r'Starting Transition State Search([\s\S]+?[LQ]ST Maximum Found[\s\S]+?\+{10})',
                        sub_parser=TextParser(quantities=tss_quantities)),
                    Quantity(
                        'cg_refinement',
                        r'Commencing conjugate gradient refinement([\s\S]+?)(?:Writing model|\Z)',
                        sub_parser=TextParser(quantities=cg_refinement_quantities)),
                    Quantity(
                        'md',
                        r'Starting MD([\s\S]+?)(?:Finished MD|\Z)',
                        sub_parser=TextParser(quantities=md_quantities)),
                    Quantity(
                        'dmd',
                        r'Starting DMD([\s\S]+?)(?:Finished DMD|\Z)',
                        sub_parser=TextParser(quantities=dmd_quantities)),
                    # TODO verify this cannot find an example
                    Quantity(
                        'di',
                        r'Starting DI([\s\S]+?)(?:Finished DI|\Z)',
                        sub_parser=TextParser(quantities=di_quantities)),
                    Quantity(
                        'bfgs',
                        r'(BFGS:[\s\S]+?)(?:BFGS: Geometry optimization|\Z)',
                        sub_parser=TextParser(quantities=bfgs_quantities)),
                    Quantity(
                        'final',
                        r'Final Configuration([\s\S]+?)(?:Writing model to|\Z)',
                        sub_parser=TextParser(quantities=system_quantities + basic_quantities))])),
            Quantity(
                'time',
                r'([A-Z]\w+) time\s+\=\s*([\d\.]+) s',
                dtype=np.float64, repeats=True)]


class CastepParser:
    def __init__(self):
        self.out_parser = OutParser()
        self.cell_parser = CellParser()
        self.bands_parser = BandsParser()

        self._xc_functional_map = {
            'Perdew Burke Ernzerhof': ['GGA_X_PBE', 'GGA_C_PBE'],
            'Local Density Approximation': ['LDA_C_PZ', 'LDA_X_PZ'],
            'Perdew Wang (1991)': ['GGA_X_PW91', 'GGA_C_PW91'],
            'revised Perdew Burke Ernzerhof': ['GGA_X_RPBE'],
            'PBE for solids (2008)': ['GGA_X_PBE_SOL'],
            'hybrid B3LYP': ['HYB_GGA_XC_B3LYP5'],
            'Hartree-Fock': ['HF_X'],
            'Hartree-Fock + Local Density Approximation': ['HF_X_LDA_C_PW'],
            'hybrid HSE03': ['HYB_GGA_XC_HSE03'],
            'hybrid HSE06': ['HYB_GGA_XC_HSE06'],
            'hybrid PBE0': ['HYB_GGA_XC_PBEH'],
            'PBE with Wu-Cohen exchange': ['GGA_C_PBE_GGA_X_WC'],
            'LDA-X': ['LDA_X_PZ'],
            'LDA-C': ['LDA_C_PZ'],
            'Optimised Effective Potential': ['OEP_EXX'],
            'PBE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'PW91': ['GGA_X_PW91', 'GGA_C_PW91'],
            'RPBE': 'GGA_X_RPBE',
            'PBEsol': ['GGA_X_RPBE'],
            'HF': ['HF_X'],
            'HF-LDA': ['HF_X_LDA_C_PW'],
            'HSE03': ['HYB_GGA_XC_HSE03'],
            'HSE06': ['HYB_GGA_XC_HSE06'],
            'PBE0': ['HYB_GGA_XC_PBEH'],
            'WC': ['GGA_C_PBE_GGA_X_WC'],
            'LDA': ['LDA_X_PZ', 'LDA_C_PZ'],
            'b3lyp': ['HYB_GGA_XC_B3LYP5']}

        self._relativistic_map = {
            'Koelling-Harmon': 'scalar_relativistic'}

        self._sampling_method_map = {
            'single point energy': 'single_point',
            'geometry optimization': 'geometry_optimization',
            'molecular dynamics': 'molecular_dynamics',
            'phonon calculation': 'phonon',
            'transition state search': 'geometry_optimization',
            'band structure': 'single_point',
            'Core level spectra (ELNES etc)': 'single_point'}

        self._metainfo_map = {
            'Final energy': 'energy_total', 'Final energy, E': 'energy_total',
            'Total energy corrected for finite basis set': 'x_castep_total_energy_corrected_for_finite_basis',
            'Final free energy (E-TS)': 'energy_free',
            'Dispersion corrected final energy*': 'x_castep_total_dispersion_corrected_energy',
            'NB est. 0K energy (E-0.5TS)': 'energy_total_t0',
            "'TS'/PBE structure energy corr.'": 'x_castep_structure_energy_corr',
            "'TS'/PBE PBC image interaction corr.": 'x_castep_PBC_image_inter_corr',
            "'TS'/PBE total energy correction": 'x_castep_total_energy_correction',
            "'TS'/PBE correction |F|max": 'x_castep_total_fmax_correction',
            'Dispersion corrected final energy*, Ecor': 'x_castep_total_dispersion_corrected_energy',
            'Dispersion corrected final free energy* (Ecor-TS)': 'x_castep_total_dispersion_corrected_free_energy',
            'NB dispersion corrected est. 0K energy* (Ecor-0.5TS)': 'x_castep_disp_corrected_energy_total_T0',
            'basis set parameters': {
                'size of standard grid': 'x_castep_size_std_grid',
                'size of   fine   gmax': 'x_castep_size_fine_grid'},
            'phonon parameters': {
                'phonon calculation method': 'x_castep_phonon_method',
                'phonon convergence tolerance': 'x_castep_phonon_tolerance',
                'max. number of phonon cycles': 'x_castep_phonon_cycles',
                'dfpt solver method': 'x_castep_DFPT_solver_method',
                'band convergence tolerance': 'x_castep_band_tolerance'},
            'geometry optimization parameters': {
                'optimization method': 'method',
                'total energy convergence tolerance': 'convergence_tolerance_energy_difference',
                'max. number of steps': 'x_castep_max_number_of_steps',
                'max ionic |force| tolerance': 'convergence_tolerance_force_maximum',
                'max ionic |displacement| tolerance': 'convergence_tolerance_displacement_maximum',
                'max |stress component| tolerance': 'x_castep_geometry_stress_com_tolerance'},
            'electronic parameters': {
                'number of  electrons': 'x_castep_number_of_electrons',
                'net charge of system': 'x_castep_net_charge',
                'number of bands': 'x_castep_number_of_bands'},
            'electronic minimization parameters': {
                'total energy / atom convergence tol.': 'x_castep_energy_threshold',
                'max. number of scf cycles': 'x_castep_max_iter',
                'smearing scheme': 'x_castep_smearing_kind',
                'smearing width': 'x_castep_smearing_width'},
            'density mixing parameters': {
                'density-mixing scheme': 'x_castep_density_mixing_scheme',
                'max. length of mixing history': 'x_castep_density_mixing_length',
                'charge density mixing amplitude': 'x_castep_charge_density_mixing_amplitude',
                'cut-off energy for mixing': 'x_castep_cut_off_energy_for_mixing'},
            'population analysis parameters': {
                'population analysis with cutoff': 'x_castep_population_analysis_cutoff'},
            'core level spectra parameters': {
                'number of bands': 'x_castep_core_spectra_n_bands',
                'band convergence tolerance': 'x_castep_core_spectra_conv_tolerance'},
            'band structure parameters': {
                'max. number of iterations': 'x_castep_band_n_iterations',
                'max. cg steps in bs calc': 'x_castep_band_max_cg',
                'number of bands / k-point': 'x_castep_band_n_bands',
                'band convergence tolerance': 'x_castep_band_conv_tolerance'},
            'molecular dynamics parameters': {
                'ensemble': 'ensemble_type',
                'temperature': 'x_castep_thermostat_target_temperature',
                'pressure': 'x_castep_frame_pressure',
                'using': ['x_castep_barostat_type', 'x_castep_thermostat_type'],
                'with characteristic cell time': 'x_castep_barostat_tau',
                'with characteristic ionic time': 'x_castep_thermostat_tau',
                'time step': 'x_castep_integrator_dt',
                'number of md steps': 'x_castep_number_of_steps_requested',
                'md scf energy / atom convergence tol.': 'x_castep_frame_energy_tolerance',
                'md scf eigenenergies tolerance': 'x_castep_frame_eigen_tolerance'},
            'transition state search parameters': {
                'search method': 'x_castep_ts_method',
                'lstqst protocol': 'x_castep_ts_protocol',
                'max. number of qst iterations': 'x_castep_ts_number_qst',
                'max. number of cg iterations': 'x_castep_ts_number_cg',
                'max. ionic |force| tolerance': 'x_castep_ts_force_tolerance',
                'max. ionic |displacement| tolerance': 'x_castep_ts_displacement_tolerance'},
            'optics parameters': {
                'search method': 'x_castep_optics_n_bands',
                'band convergence tolerance': 'x_castep_optics_tolerance'},
            'electronic spectroscopy parameters': {
                'electronic spectroscopy with theory level': 'x_castep_theory_level',
                'spectroscopy calculation': 'x_castep_spectroscopy_calculation',
                'max. number of iterations': 'x_castep_spec_max_iter',
                'max. steps per iteration': 'x_castep_spec_max_steps',
                'number of bands / k-point': 'x_castep_spec_max_bands',
                'band convergence tolerance': 'x_castep_spec_tolerance'},
            'time-dependent dft parameters': {
                'number of excited states': 'x_castep_tddft_n_excited_states',
                'state selected for calculation of forces': 'x_castep_tddft_n_states_forces',
                'state convergence tolerance': 'x_castep_tddft_state_tolerance',
                'convergence tolerance window': 'x_castep_tddft_state_tolerance_window',
                'max. number of iterations': 'x_castep_tddft_max_iter',
                'no. of extra (convergence indifferent) states': 'x_castep_tddft_extra_states',
                'using tddft functional': 'x_castep_tddft_functional',
                'time-dependent dft method': 'x_castep_tddft_method',
                'matrix eigenvalue method': 'x_castep_tddft_eigenmethod',
                'time-Dependent dft approximation': 'x_castep_tddft_approximation',
                'time-Dependent dft position operator': 'x_castep_tddft_position_op'}}

        self._units = None
        self._nspin = None

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger
        self._units = None
        self._nspin = None

    @property
    def units(self):
        if self._units is None:
            self._units = dict()
            re_unit = re.compile(r'output\s*([\w ]+) unit')
            parameters = self.out_parser.get('title', {}).get('general parameters', {})
            for key, val in parameters.items():
                name = re_unit.match(key)
                if name:
                    try:
                        self._units[name.group(1)] = resolve_unit(val)
                    except Exception:
                        pass
        return self._units

    @property
    def n_spin_channels(self):
        if self._nspin is None:
            self._nspin = 1 if self.out_parser.get('title', {}).get(
                'electronic parameters', {}).get('number of down spins') is None else 2
        return self._nspin

    def get_castep_file(self, ext):
        paths = [p for p in os.listdir(self.maindir) if p.endswith(ext)]
        if not paths:
            return
        elif len(paths) == 1:
            return os.path.join(self.maindir, paths[0])
        else:
            prefix = os.path.basename(self.filepath).rsplit('.', 1)[0]
            for path in paths:
                if path.startswith(prefix):
                    return os.path.join(self.maindir, path)

    def parse_method(self):
        sec_method = self.archive.run[0].m_create(Method)
        title = self.out_parser.get('title', {})

        # basis set
        basis_parameters = self.out_parser.get('title', {}).get('basis set parameters', {})
        sec_basis = sec_method.m_create(BasisSet)
        sec_basis.type = 'plane_waves'
        sec_basis_cell_dependent = sec_basis.m_create(BasisSetCellDependent)
        sec_method.basis_set[0].cell_dependent.kind = 'plane_waves'
        cutoff = basis_parameters.get('plane wave basis set cut-off')
        if cutoff:
            sec_basis_cell_dependent.planewave_cutoff = cutoff
            sec_basis_cell_dependent.name = 'PW_%d' % (round(cutoff.to('rydberg').magnitude))

        sec_dft = sec_method.m_create(DFT)
        method = 'DFT+U' if self.out_parser.get('dft_u') is not None else 'DFT'
        sec_method.electronic = Electronic(method=method, n_spin_channels=self.n_spin_channels)

        xc_parameters = title.get('exchange-correlation parameters', {})

        # xc functional
        xc_functionals = xc_parameters.get('using functional')
        if xc_functionals is None:
            xc_functionals = xc_parameters.get('using custom xc functional definition', [])
        xc_functionals = xc_functionals if isinstance(xc_functionals, list) else [xc_functionals]

        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for xc_functional in xc_functionals:
            # when custom, a weight is attached
            xc_weight = None
            if xc_parameters.get('using custom xc functional definition') is not None:
                xc_functional, xc_weight = xc_functional.rsplit(' ', 1)
            for functional in self._xc_functional_map.get(xc_functional, []):
                sec_functional = Functional(name=functional)
                if xc_weight is not None:
                    sec_functional.weight = float(xc_weight)
                if '_X_' in functional or functional.endswith('_X'):
                    sec_xc_functional.exchange.append(sec_functional)
                elif '_C_' in functional or functional.endswith('_C'):
                    sec_xc_functional.correlation.append(sec_functional)
                elif 'HYB' in functional:
                    sec_xc_functional.hybrid.append(sec_functional)
                else:
                    sec_xc_functional.contributions.append(sec_functional)

        # relativistic treatment
        relativistic = self._relativistic_map.get(xc_parameters.get('relativistic treatment'))
        if relativistic is not None:
            sec_method.electronic.relativity_method = relativistic

        # dispersion correction
        dispersion = xc_parameters.get('sedc with')
        if dispersion is not None:
            sec_method.electronic.van_der_waals_method = dispersion.split()[0]

        # smearing scheme
        electronic_parameters = title.get('electronic minimization parameters', {})
        smearing = electronic_parameters.get('smearing scheme')
        if smearing is not None:
            sec_smearing = sec_method.electronic.m_create(Smearing)
            sec_smearing.kind = smearing.lower()
            width = electronic_parameters.get('smearing width')
            if width is not None:
                sec_smearing.width = width.to('joule').magnitude

        species = self.out_parser.get('species')
        if species is None:
            return

        for name, mass in species.get('mass', []):
            sec_atom_parameters = sec_method.m_create(AtomParameters)
            sec_atom_parameters.label = name
            sec_atom_parameters.mass = mass

    def parse_workflow(self):
        sec_workflow = self.archive.m_create(Workflow)
        workflow = None

        title = self.out_parser.get('title', {})

        method = title.get('general parameters', {}).get('type of calculation', 'single point')
        method = self._sampling_method_map.get(method)
        if method is None:
            self.logger.warning('Sampling method cannot be resolved.')
            method = 'single_point'
        sec_workflow.type = method

        if method == 'geometry_optimization':
            sec_geometry_opt = sec_workflow.m_create(GeometryOptimization)
            parameters = title.get('geometry optimization parameters', {})
            key_map = self._metainfo_map.get('geometry optimization parameters')
            for key, val in parameters.items():
                key = key_map.get(key)
                if key is None or val is None:
                    continue
                setattr(sec_geometry_opt, key, val)
            workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
            workflow.method.convergence_tolerance_displacement_maximum = parameters.get('max ionic |displacement| tolerance')
            workflow.method.convergence_tolerance_energy_difference = parameters.get('total energy convergence tolerance')
            workflow.method.convergence_tolerance_force_maximum = parameters.get('max ionic |force| tolerance')
        elif method == 'molecular_dynamics':
            sec_md = sec_workflow.m_create(MolecularDynamics)
            parameters = title.get('molecular dynamics parameters', {})
            workflow = MolecularDynamics2(method=MolecularDynamicsMethod())
            for key, val in parameters.items():
                key = self._metainfo_map.get('molecular dynamics parameters').get(key)
                if key is None or val is None:
                    continue
                if isinstance(key, list):
                    for i, key_i in enumerate(key):
                        setattr(sec_md, key_i, val[i])
                else:
                    setattr(sec_md, key, val)
            workflow.method.thermodynamic_ensemble = parameters.get('ensemble')

        self.archive.workflow2 = workflow

    def parse_configurations(self):
        calculation = self.out_parser.get('calculation')
        if calculation is None:
            return

        sec_run = self.archive.run[0]

        def parse_eigenvalues(source):
            sec_scc = sec_run.calculation[-1]

            energy_unit = self.units.get('energy', 1)
            bandstructure = source.get('bandstructure')
            kpts, band_energies = [], []
            if bandstructure is not None:
                for spin, kpt, energies in bandstructure.get('kpt_energies', []):
                    if spin == 1:
                        kpts.append(kpt)
                    band_energies.append(energies)
                band_energies = np.reshape(
                    band_energies, (spin, len(kpts), len(band_energies[0]))) * energy_unit

            else:
                self.bands_parser.mainfile = self.get_castep_file('bands')
                for kpt, energies in self.bands_parser.get('kpt_energies', []):
                    kpts.append(kpt)
                    band_energies.append(energies)
                if len(band_energies) == 0:
                    return

                n_spin = self.bands_parser.get('n_spins', 1)
                band_energies = np.reshape(band_energies, (
                    len(kpts), n_spin, len(band_energies[0]) // n_spin))
                band_energies = np.transpose(band_energies, axes=(1, 0, 2)) * energy_unit

            # get path segment nodes from .cell
            self.cell_parser.mainfile = self.get_castep_file('cell')
            kpoint_path = self.cell_parser.get_value('bs_kpoint_path', [])

            if len(kpoint_path) == 0:
                # write energies to eigenvalues
                sec_eigenvalues = sec_scc.m_create(BandEnergies)
                sec_eigenvalues.n_kpoints = len(kpts)
                sec_eigenvalues.kpoints = kpts
                sec_eigenvalues.energies = band_energies
            else:
                # write band energies on segments
                nodes = np.array([path[:3] for path in kpoint_path], dtype=np.dtype(np.float64))
                labels = ['\u0393' if path[-1].lower() == 'gamma' else path[-1] for path in kpoint_path]
                sec_bandstructure = sec_scc.m_create(
                    BandStructure, Calculation.band_structure_electronic)
                start = 0
                for n, node in enumerate(nodes[1:]):
                    node_index = np.where(kpts == node)[0]
                    for index in node_index:
                        if np.count_nonzero(node_index == index) == 3 and index > start:
                            break
                    sec_band_segment = sec_bandstructure.m_create(BandEnergies)
                    sec_band_segment.n_bands = len(band_energies[0][start])
                    sec_band_segment.n_kpoints = int(index + 1 - start)
                    sec_band_segment.kpoints = kpts[start:index + 1]
                    # assign labels at nodes
                    sec_band_segment.endpoints_labels = [labels[n], labels[n + 1]]
                    sec_band_segment.energies = band_energies[:, start:index + 1, :]
                    start = index

        def parse_scc(source):
            sec_scc = sec_run.m_create(Calculation)
            energy_unit = self.units.get('energy', 1)

            sec_energy = sec_scc.m_create(Energy)
            if source.get('energy_total') is not None:
                sec_energy.total = EnergyEntry(value=source.get('energy_total') * energy_unit)

            # energies
            for key, val in source.get('energy', []):
                name = self._metainfo_map.get(key)
                if name is not None:
                    if name.startswith('x_castep_'):
                        sec_energy.m_add_sub_section(
                            Energy.contributions, EnergyEntry(
                                kind=name.replace('x_castep_', ''), value=val))
                        setattr(sec_scc, name, val.to('joule').magnitude)
                    else:
                        sec_energy.m_add_sub_section(getattr(
                            Energy, name.replace('energy_', '')), EnergyEntry(value=val))

            # forces
            forces = source.get('forces')
            if forces is not None:
                sec_forces = sec_scc.m_create(Forces)
                sec_forces.total = ForcesEntry(value=forces[1] * self.units.get('force', 1))

            sec_thermo = sec_scc.m_create(Thermodynamics)
            # stress tensor
            stress_tensor = source.get('stress_tensor')
            if stress_tensor is not None:
                if stress_tensor.get('stress_tensor') is not None:
                    sec_stress = sec_scc.m_create(Stress)
                    sec_stress.total = StressEntry(
                        value=stress_tensor.get('stress_tensor') * self.units.get('pressure', 1))
                if stress_tensor.get('pressure') is not None:
                    sec_thermo.pressure = stress_tensor.get('pressure') * self.units.get('pressure', 1)

            # other properties
            enthalpy = source.get('enthalpy')
            if enthalpy is not None:
                sec_thermo.enthalpy = enthalpy[1]

            freq = source.get('frequency')
            if freq is not None:
                sec_scc.x_castep_frequency = freq[1].magnitude

            # eigenvalues
            parse_eigenvalues(source)

            # mulliken population analysis
            mulliken = source.get('mulliken')
            if mulliken is not None:
                species = mulliken.get('Species', [])
                sec_charges = sec_scc.m_create(Charges)
                sec_charges.analysis_method = 'mulliken'
                orbitals = [o for o in 'spdf' if mulliken.get(o) is not None]
                sec_charges.n_charges_orbitals = len(orbitals)
                sec_charges.n_charges_atoms = len(species)
                sec_charges.value = mulliken['Total']
                for n, specie in enumerate(species):
                    for orbital in orbitals:
                        sec_charges_value = sec_charges.m_create(ChargesValue, Charges.orbital_projected)
                        sec_charges_value.orbital = orbital
                        sec_charges_value.atom_index = n
                        sec_charges_value.atom_label = specie
                        sec_charges_value.value = mulliken[orbital][n]

            # vibrational frequencies
            # why are vibrational frequencies section under section_run?
            for vibrational_frequencies in source.get('vibrational_frequencies', []):
                sec_frequencies = sec_run.m_create(x_castep_section_vibrational_frequencies)
                sec_vibrations = sec_scc.m_create(VibrationalFrequencies)
                for key, val in vibrational_frequencies.items():
                    if key == 'vibrational_frequencies':
                        sec_vibrations.value = val * (1 / ureg.cm)
                    elif key == 'ir_intensity':
                        sec_ir = sec_vibrations.m_create(VibrationalFrequenciesValues, VibrationalFrequencies.infrared)
                        sec_ir.intensity = val
                        if vibrational_frequencies.get('ir_active') is not None:
                            sec_ir.activity = vibrational_frequencies.get('ir_active')
                    elif key == 'raman_activity':
                        sec_raman = sec_vibrations.m_create(VibrationalFrequenciesValues, VibrationalFrequencies.raman)
                        sec_raman.intensity = val
                        if vibrational_frequencies.get('raman_active') is not None:
                            sec_raman.activity = vibrational_frequencies.get('raman_active')
                    setattr(sec_frequencies, 'x_castep_%s' % key, val)

            # raman tensors
            for raman_tensor in source.get('raman_tensor', []):
                sec_raman = sec_run.m_create(x_castep_section_raman_tensor)
                unit = (self.units.get('length', ureg.angstrom) / self.units.get('mass', ureg.amu)) * 0.5
                sec_raman.x_castep_raman_tensor = raman_tensor * unit

            # interaction energy
            interaction = source.get('interaction_energy')
            if interaction is not None:
                for shell in interaction.get('shell', []):
                    sec_sedc = sec_scc.m_create(x_castep_section_DFT_SEDC)
                    sec_sedc.x_castep_shell = shell[0]
                    sec_sedc.x_castep_correction_energy = (shell[1] * energy_unit).to('J').magnitude
                    sec_sedc.x_castep_de_atom = (shell[2] * energy_unit).to('J').magnitude
                    sec_sedc.x_castep_dfmax_atom = (shell[3] * self.units.get('force')).to('J/m').magnitude

                for key, val in interaction.get('energy', []):
                    name = self._metainfo_map.get(key)
                    if name is None:
                        continue
                    val = val.to('J') if val.units == ureg.eV else val.to('J/m')
                    setattr(sec_sedc, name, val.magnitude)

                # add the dispersion energies
                for key, val in source.get('energy', []):
                    name = self._metainfo_map.get(key, '')
                    if '_disp' in name:
                        setattr(sec_sedc, name, val.to('joule').magnitude)

            # scf iteration
            for scf in source.get('scf', []):
                sec_scf = sec_scc.m_create(ScfIteration)
                sec_scf_energy = sec_scf.m_create(Energy)
                sec_scf.energy.total = EnergyEntry(value=scf[0] * energy_unit)
                if len(scf) == 4:
                    sec_scf_energy.fermi = scf[1] * energy_unit
                sec_scf_energy.change = scf[-2] * energy_unit
                sec_scf.time_calculation = scf[-1]

            return sec_scc

        def parse_system(source):
            sec_system = sec_run.m_create(System)
            sec_atoms = sec_system.m_create(Atoms)
            length_unit = self.units.get('length', 1)

            unit_cell = source.get('unit_cell', self.out_parser.get('unit_cell', {}))
            if unit_cell.get('lattice_vectors') is not None:
                sec_atoms.lattice_vectors = unit_cell.get('lattice_vectors')[0] * length_unit
                sec_atoms.periodic = [True, True, True]

            cell_contents = source.get('cell_contents', self.out_parser.get('cell_contents', {}))
            if cell_contents.get('positions') is not None:
                sec_atoms.labels = cell_contents.get('positions')[0]
                sec_atoms.positions = np.dot(cell_contents.get('positions')[1], sec_system.atoms.lattice_vectors)
            if cell_contents.get('velocities') is not None:
                sec_atoms.velocities = cell_contents.get('velocities')[1] * (
                    length_unit / self.units.get('time', 1))

            # miscellaneous quantities
            cell_volume = unit_cell.get('cell_volume')
            if cell_volume is not None:
                cell_volume *= length_unit ** 3
                sec_system.x_castep_cell_volume = cell_volume.to('m**3').magnitude

            lattice_parameters = unit_cell.get('lattice_parameters')
            if lattice_parameters is not None:
                sec_positions = sec_system.m_create(x_castep_section_atom_positions)
                for key, val in lattice_parameters.items():
                    if key in ('a', 'b', 'c'):
                        val *= length_unit
                        setattr(sec_positions, 'x_castep_cell_length_%s' % key, val.to('m').magnitude)
                    elif key in ('alpha', 'beta', 'gamma'):
                        setattr(sec_positions, 'x_castep_cell_angle_%s' % key, val)

            # tddft
            # why are tddft results here?, adapted from old parser
            tddft = source.get('tddft')
            if tddft is not None:
                for energies in tddft.get('energies', []):
                    sec_tddft = sec_system.m_create(x_castep_section_tddft)
                    energies = energies * self.units.get('energy', ureg.eV)
                    sec_tddft.x_castep_state_energy = energies[1].to('J').magnitude
                    sec_tddft.x_castep_state_energy_error = energies[2].to('J').magnitude
                sec_tddft.x_castep_state_number = energies[0].magnitude
                sec_tddft.x_castep_tddft_calculation_time = tddft.get('time', 0.)
                sec_tddft.x_castep_tddft_iteration = tddft.get('iteration', [0, 0])[-1][0]

            # add miscellaneos stuff to first instance
            if len(sec_run.system) == 1:
                for key, val in self.out_parser.get('title', {}).get('electronic parameters', {}).items():
                    key = self._metainfo_map.get('electronic parameters', {}).get(key)
                    if key is None:
                        continue
                    setattr(sec_system, key, val)

            return sec_system

        def parse_calculation(source):
            if source is None:
                return
            sec_scc = parse_scc(source)
            sec_system = parse_system(source)
            sec_scc.system_ref = sec_system
            sec_scc.method_ref = sec_run.method[-1]

        # basis set correction
        # TODO determine if there is a need to add this
        basis_set_correction = calculation.get('basis_set_correction')
        if basis_set_correction is not None:
            for iteration in basis_set_correction.get('iteration', []):
                parse_calculation(iteration)

        # transition state search
        tss = calculation.get('tss')
        if tss is not None:
            for iteration in tss.get('iteration', []):
                parse_calculation(iteration)

        cg_refinement = calculation.get('cg_refinement')
        if cg_refinement is not None:
            for iteration in cg_refinement.get('iteration', []):
                parse_calculation(iteration)

        # molecular dyanamics
        # because of basis set correction number of frames may not correspond to number
        # of iterations
        md = calculation.get('md')
        if md is not None:
            # TODO add more quantities, read from md file
            for iteration in md.get('iteration', []):
                parse_calculation(iteration)

        # dmd optimization
        dmd = calculation.get('dmd')
        if dmd is not None:
            for iteration in dmd.get('iteration', []):
                parse_calculation(iteration)

        # di optimization
        di = calculation.get('di')
        if di is not None:
            for iteration in di.get('iteration', []):
                parse_calculation(iteration)

        # bfgs optimization
        bfgs = calculation.get('bfgs')
        if bfgs is not None:
            for iteration in bfgs.get('iteration', []):
                # an iteration can both have a pre-conditioning stage which we skip
                if iteration.get('iteration'):
                    parse_calculation(iteration.get('iteration')[-1])

        # final configuration
        if calculation.get('final') is not None:
            parse_calculation(calculation.get('final'))

        if self.archive.workflow[0].type in ['single_point', 'phonon']:
            # single point calculation
            parse_calculation(calculation)

    def parse_parameters(self):
        section_map = {
            'phonon parameters': x_castep_section_phonons,
            'electronic minimization parameters': x_castep_section_scf_parameters,
            'density mixing parameters': x_castep_section_density_mixing_parameters,
            'population analysis parameters': x_castep_section_population_analysis_parameters,
            'core level spectra parameters': x_castep_section_core_parameters,
            'band structure parameters': x_castep_section_band_parameters,
            'transition state search parameters': x_castep_section_ts_parameters,
            'optics parameters': x_castep_section_optics_parameters,
            'electronic spectroscopy parameters': x_castep_section_electronic_spectroscpy_parameters,
            'time-dependent dft parameters': x_castep_section_tddft_parameters}

        # TODO map all castep parameters
        sec_run = self.archive.run[0]
        title = self.out_parser.get('title', {})

        def create_section(definition):
            if definition is None:
                return

            create = True
            for section in sec_run.m_contents():
                if section.m_def == definition.m_def:
                    create = False
                    break
            return sec_run.m_create(definition) if create else section

        for key in title.keys():
            section = create_section(section_map.get(key))
            if section is None:
                continue
            for sub_key, val in title[key].items():
                sub_key = self._metainfo_map.get(key, {}).get(sub_key)
                if val is not None and sub_key is not None:
                    val = val.magnitude if hasattr(val, 'magnitude') else val
                    setattr(section, sub_key, val)

        # van der Waals
        dft_d = self.out_parser.get('dft_d')
        if dft_d is not None:
            sec_vdW = sec_run.m_create(x_castep_section_van_der_Waals_parameters)
            if dft_d.get('method') is not None:
                sec_vdW.x_castep_disp_method_name = dft_d.get('method')
            for parameter in dft_d.get('parameter', []):
                key = parameter[0].upper() if parameter[0] == 'lambda' else parameter[0]
                setattr(sec_vdW, 'x_castep_Parameter_%s' % key, float(parameter[1]))

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        sec_run = self.archive.m_create(Run)
        version = self.out_parser.get('program_version', ['CASTEP', ''])
        sec_run.program = Program(name=version[0])
        if version[1]:
            sec_run.program.version = str(version[1])

        compilation = self.out_parser.get('program_compilation', '').strip().split(' ', 1)
        if len(compilation) == 2:
            sec_run.program.compilation_host = compilation[0]
            date, time = compilation[1].rsplit(' ', 1)
            sec_run.x_castep_program_compilation_date = date
            sec_run.x_castep_program_compilation_time = time

        for key in ['compiler', 'maths_library', 'fft_library', 'constants_reference']:
            val = self.out_parser.get(key)
            if val is not None:
                setattr(sec_run, 'x_castep_%s' % key, val)

        date_start = self.out_parser.get('run_start')
        if date_start is not None:
            date_start = datetime.strptime(date_start.strip(), '%d %b %Y %H:%M:%S')
            sec_run.time_run = TimeRun(
                date_start=(date_start - datetime(1970, 1, 1)).total_seconds())

        self.parse_method()

        self.parse_workflow()

        self.parse_configurations()

        self.parse_parameters()

        # times
        time = self.out_parser.get('time')
        if time is not None:
            sec_time = sec_run.m_create(x_castep_section_time)
            for key, val in time:
                setattr(sec_time, 'x_castep_%s_time' % key.lower(), val)
