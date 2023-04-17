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

from nomad.parsing.file_parser import TextParser, Quantity, DataTextParser

from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, XCFunctional, Functional, HubbardKanamoriModel, AtomParameters, DFT,
    BasisSet, GW, KMesh, FrequencyMesh
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, BandStructure, BandEnergies, Dos, DosValues,
    ScfIteration, Energy, EnergyEntry, Stress, StressEntry, Thermodynamics,
    Forces, ForcesEntry
)
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2, GeometryOptimization as GeometryOptimization2,
    MolecularDynamics, MolecularDynamicsMethod, MolecularDynamicsResults,
    ThermostatParameters)

# for old MD workflow
from nomad.datamodel.metainfo.workflow import (
    ThermostatParameters as ThermostatParametersOld, IntegrationParameters as IntegrationParametersOld,
    MolecularDynamics as MolecularDynamicsOld)

from .metainfo.fhi_aims import Run as xsection_run, Method as xsection_method,\
    x_fhi_aims_section_parallel_task_assignement, x_fhi_aims_section_parallel_tasks,\
    x_fhi_aims_section_controlIn_basis_set, x_fhi_aims_section_controlIn_basis_func,\
    x_fhi_aims_section_controlInOut_atom_species, x_fhi_aims_section_controlInOut_basis_func,\
    x_fhi_aims_section_vdW_TS
from ..utils import BeyondDFTWorkflowsParser


re_float = r'[-+]?\d+\.\d*(?:[Ee][-+]\d+)?'
re_n = r'[\n\r]'


class FHIAimsControlParser(TextParser):
    def __init__(self):
        super().__init__(None)

    @staticmethod
    def str_to_unit(val_in):
        val = val_in.strip().lower()
        unit = None
        if val.startswith('a'):
            unit = 1 / ureg.angstrom
        elif val.startswith('b'):
            unit = 1 / ureg.bohr
        return unit

    def init_quantities(self):
        def str_to_species(val_in):
            val = val_in.strip().splitlines()
            data = []
            species = dict()
            for v in val:
                v = v.strip().split('#')[0]
                if not v or not v[0].isalpha():
                    continue
                if v.startswith('species'):
                    if species:
                        data.append(species)
                    species = dict(species=v.split()[1:])
                else:
                    v = v.replace('.d', '.e').split()
                    vi = v[1] if len(v[1:]) == 1 else v[1:]
                    if v[0] in species:
                        species[v[0]].extend([vi])
                    else:
                        species[v[0]] = [vi]
            data.append(species)
            return data

        self._quantities = [
            Quantity(
                xsection_method.x_fhi_aims_controlIn_charge,
                rf'{re_n} *charge\s*({re_float})', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_hse_unit,
                rf'{re_n} *hse_unit\s*([\w\-]+)', str_operation=self.str_to_unit, repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_hybrid_xc_coeff,
                rf'{re_n} *hybrid_xc_coeff\s*({re_float})', repeats=False),
            Quantity(
                xsection_run.x_fhi_aims_controlIn_MD_time_step,
                rf'{re_n} *MD_time_step\s*({re_float})', repeats=False),
            Quantity(
                'k_grid',
                rf'{re_n} *k\_grid\s*([\d ]+)', repeats=False),  # manual version 210716_2
            Quantity(
                'k_offset',
                rf'{re_n} *k\_offset\s*([\d ]+)', repeats=False),  # manual version 210716_2
            Quantity(
                'occupation_type',
                rf'{re_n} *occupation_type\s*([\w\. \-\+]+)', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_override_relativity,
                rf'{re_n} *override_relativity\s*([\.\w]+)', repeats=False),
            Quantity(
                'relativistic',
                rf'{re_n} *relativistic\s*([\w\. \-\+]+)', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_sc_accuracy_rho,
                rf'{re_n} *sc_accuracy_rho\s*({re_float})', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_sc_accuracy_eev,
                rf'{re_n} *sc_accuracy_eev\s*({re_float})', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_sc_accuracy_etot,
                rf'{re_n} *sc_accuracy_etot\s*({re_float})', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_sc_accuracy_forces,
                rf'{re_n} *sc_accuracy_forces\s*({re_float})', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_sc_accuracy_stress,
                rf'{re_n} *sc_accuracy_stress\s*({re_float})', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_sc_iter_limit,
                rf'{re_n} *sc_iter_limit\s*([\d]+)', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_spin,
                rf'{re_n} *spin\s*([\w]+)', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlIn_verbatim_writeout,
                rf'{re_n} *verbatim_writeout\s*([\w]+)', repeats=False),
            Quantity(
                'xc',
                rf'{re_n} *xc\s*([\w\. \-\+]+)', repeats=False),
            Quantity(
                'species', rf'{re_n} *(species\s*[A-Z][a-z]?[\s\S]+?)'
                r'(?:species\s*[A-Z][a-z]?|Completed|\-{10})',
                str_operation=str_to_species, repeats=False)]


class FHIAimsOutParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        units_mapping = {'Ha': ureg.hartree, 'eV': ureg.eV}

        def str_to_energy_components(val_in):
            val = [v.strip() for v in val_in.strip().splitlines()]
            res = dict()
            for v in val:
                v = v.lstrip(' |').strip().split(':')
                if len(v) < 2 or not v[1]:
                    continue
                vi = v[1].split()
                if not vi[0][-1].isdecimal() or len(vi) < 2:
                    continue
                unit = units_mapping.get(vi[1], None)
                res[v[0].strip()] = float(vi[0]) * unit if unit is not None else float(vi[0])
            return res

        def str_to_scf_convergence(val_in):
            res = dict()
            for v in val_in.strip().splitlines():
                v = v.lstrip(' |').split(':')
                if len(v) != 2:
                    break
                vs = v[1].split()
                unit = None
                if len(vs) > 1:
                    unit = units_mapping.get(vs[1], None)
                res[v[0].strip()] = float(vs[0]) * unit if unit is not None else float(vs[0])
            return res

        def str_to_atomic_forces(val_in):
            val = [v.lstrip(' |').split() for v in val_in.strip().splitlines()]
            forces = np.array([v[1:4] for v in val if len(v) == 4], dtype=float)
            return forces * ureg.eV / ureg.angstrom

        def str_to_dos_files(val_in):
            val = [v.strip() for v in val_in.strip().splitlines()]
            files = []
            species = []
            for v in val[1:]:
                if v.startswith('| writing') and 'raw data' in v:
                    files.append(v.split('to file')[1].strip(' .'))
                    if 'for species' in v:
                        species.append(v.split('for species')[1].split()[0])
                elif not v.startswith('|'):
                    break
            return files, list(set(species))

        def str_to_array_size_parameters(val_in):
            val = [v.lstrip(' |').split(':') for v in val_in.strip().splitlines()]
            return {v[0].strip(): int(v[1]) for v in val if len(v) == 2}

        def str_to_species_in(val_in):
            val = [v.strip() for v in val_in.splitlines()]
            data = []
            species = dict()
            for i in range(len(val)):
                if val[i].startswith('Reading configuration options for species'):
                    if species:
                        data.append(species)
                    species = dict(species=val[i].split('species')[1].split()[0])
                elif not val[i].startswith('| Found'):
                    continue
                val[i] = val[i].split(':')
                if len(val[i]) == 1:
                    val[i] = val[i][0].split('treatment for')
                if len(val[i]) < 2:
                    continue
                k = val[i][0].split('Found')[1].strip()
                v = val[i][1].replace(',', '').split()
                if 'Gaussian basis function' in k and 'elementary' in v:
                    n_gaussians = int(v[v.index('elementary') - 1])
                    for j in range(n_gaussians):
                        v.extend(val[i + j + 1].lstrip('|').split())
                v = v[0] if len(v) == 1 else v
                if val[i][0] in species:
                    species[k].extend([v])
                else:
                    species[k] = [v]
            data.append(species)
            return data

        def str_to_species(val_in):
            data = dict()
            val = [v.strip() for v in val_in.splitlines()]
            for i in range(len(val)):
                if val[i].startswith('species'):
                    data['species'] = val[i].split()[1]
                elif not val[i].startswith('| Found'):
                    continue
                val[i] = val[i].split(':')
                if len(val[i]) == 1:
                    val[i] = val[i][0].split('treatment for')
                if len(val[i]) < 2:
                    continue
                k = val[i][0].split('Found')[1].strip()
                v = val[i][1].replace(',', '').split()
                if 'Gaussian basis function' in k and 'elementary' in v:
                    n_gaussians = int(v[v.index('elementary') - 1])
                    for j in range(n_gaussians):
                        v.extend(val[i + j + 1].lstrip('|').split())
                v = v[0] if len(v) == 1 else v
                if k in data:
                    data[k].extend([v])
                else:
                    data[k] = [v]
            return data

        structure_quantities = [
            Quantity(
                'labels',
                rf'(?:Species\s*([A-Z][a-z]*)|([A-Z][a-z]*)\w*{re_n})', repeats=True),
            Quantity(
                'positions',
                rf'({re_float})\s+({re_float})\s+({re_float}) *{re_n}',
                dtype=np.dtype(np.float64), repeats=True),
            Quantity(
                'positions',
                rf'atom +({re_float})\s+({re_float})\s+({re_float})',
                dtype=np.dtype(np.float64), repeats=True),
            Quantity(
                'velocities',
                rf'velocity\s+({re_float})\s+({re_float})\s+({re_float})',
                dtype=np.dtype(np.float64), repeats=True)]

        eigenvalues = Quantity(
            'eigenvalues',
            rf'Writing Kohn\-Sham eigenvalues\.([\s\S]+?State[\s\S]+?)(?:{re_n}{re_n} +[A-RT-Z])',
            repeats=True, sub_parser=TextParser(quantities=[
                Quantity(
                    'kpoints',
                    rf'{re_n} *K-point:\s*\d+ at\s*({re_float})\s*({re_float})\s*({re_float})',
                    dtype=float, repeats=True),
                Quantity(
                    'occupation_eigenvalue',
                    rf'{re_n} *\d+\s*({re_float})\s*({re_float})\s*{re_float}',
                    repeats=True)]))

        scf_quantities = [
            Quantity(
                'date_time', rf'{re_n} *Date\s*:(\s*\d+), Time\s*:(\s*[\d\.]+)\s*',
                repeats=False, convert=False),
            # TODO add section_eigenvalues to scf_iteration
            eigenvalues,
            Quantity(
                'energy_components',
                rf'{re_n} *Total energy components:([\s\S]+?)((?:{re_n}{re_n}|\| Electronic free energy per atom\s*:\s*[Ee\d\.\-]+ eV))',
                repeats=False, str_operation=str_to_energy_components, convert=False),
            Quantity(
                'forces', rf'{re_n} *Total forces\([\s\d]+\)\s*:([\s\d\.\-\+Ee]+){re_n}', repeats=True),
            Quantity(
                'stress_tensor', rf'{re_n} *Sum of all contributions\s*:\s*([\d\.\-\+Ee ]+{re_n})', repeats=False),
            Quantity(
                'pressure', r' *\|\s*Pressure:\s*([\d\.\-\+Ee ]+)', repeats=False),
            Quantity(
                'scf_convergence',
                rf'{re_n} *Self-consistency convergence accuracy:([\s\S]+?)(\| Change of total energy\s*:\s*[\d\.\-\+Ee V]+)',
                repeats=False, str_operation=str_to_scf_convergence, convert=False),
            Quantity(
                'humo', r'Highest occupied state \(VBM\) at\s*([\d\.\-\+Ee ]+) (?P<__unit>\w+)',
                repeats=False, dtype=float),
            Quantity(
                'lumo', r'Lowest unoccupied state \(CBM\) at\s*([\d\.\-\+Ee ]+) (?P<__unit>\w+)',
                repeats=False, dtype=float),
            Quantity(
                'fermi_level',  # older version
                rf'{re_n} *\| Chemical potential \(Fermi level\) in (\w+)\s*:([\d\.\-\+Ee ]+)',
                str_operation=lambda x: float(x.split()[1]) * units_mapping.get(x.split()[0])),
            Quantity(
                'fermi_level',  # newer version
                rf'{re_n} *\| Chemical potential \(Fermi level\)\:\s*([\-\d\.]+)\s*(\w+)',
                str_operation=lambda x: float(x.split()[0]) * units_mapping.get(x.split()[1], 1))]

        def str_to_scf_convergence2(val_in):
            val = val_in.split('|')
            if len(val) != 7:
                return
            energy = float(val[3]) * ureg.eV
            return {'Change of total energy': energy}

        def str_to_hirshfeld(val_in):
            val = [v.strip() for v in val_in.strip().splitlines()]
            data = dict(atom=val[0])
            for v in val[1:]:
                if v.startswith('|'):
                    v = v.strip(' |').split(':')
                    if v[0][0].isalpha():
                        key = v[0].strip()
                        data[key] = []
                    data[key].extend([float(vi) for vi in v[-1].split()])
            return data

        def str_to_frequency(val_in):
            val = [v.split() for v in val_in.split('\n')]
            val = np.transpose(np.array([v for v in val if len(v) == 2], float))
            return [int(val[0]), val[1]]

        def str_to_gw_eigs(val_in):
            val = [v.split() for v in val_in.splitlines()]
            keys = val[0]
            data = []
            for v in val[1:]:
                if len(keys) == len(v) and v[0].isdecimal():
                    data.append(v)
            data = np.array(data, dtype=float)
            data = np.transpose(data)
            res = {keys[i]: data[i] for i in range(len(data))}
            return res

        def str_to_gw_scf(val_in):
            val = [v.split(':') for v in val_in.splitlines()]
            data = {}
            for v in val:
                if len(v) == 2:
                    data[v[0].strip(' |')] = float(v[1].split()[0]) * ureg.eV
                if 'Fit accuracy for G' in v[0]:
                    data['Fit accuracy for G(w)'] = float(v[0].split()[-1])
            return data

        def str_to_md_calculation_info(val_in):
            val = [v.strip() for v in val_in.strip().splitlines()]
            res = dict()
            for v in val:
                v = v.lstrip(' |').strip().split(':')
                if len(v) < 2 or not v[1]:
                    continue
                vi = v[1].split()
                if not vi[0][-1].isdecimal():
                    continue
                elif len(vi) < 2:
                    res[v[0].strip()] = float(vi[0])
                else:
                    unit = units_mapping.get(vi[1], None)
                    res[v[0].strip()] = float(vi[0]) * unit if unit is not None else float(vi[0])
            return res

        def str_to_quantity(val_in):
            val = val_in.split()
            if len(val) == 1:
                return float(val[0])
            elif len(val) == 2:
                return float(val[0]) * ureg(val[1])
            else:
                return None

        def str_to_ureg(val_in):
            try:
                val = ureg(val_in.replace('^', '**'))
            except Exception:
                self.logger.warning(rf'Problem parsing some units from .out file, could not convert.', details={'value': val_in})
                val = None
            return val

        def str_to_md_control_in(val_in):
            val = val_in.split()
            return {val[0]: ' '.join(val[1:])}

        calculation_quantities = [
            Quantity(
                'self_consistency',
                r'Begin self\-consistency iteration #\s*\d+([\s\S]+?Total energy evaluation[s:\d\. ]+)',
                repeats=True, sub_parser=TextParser(quantities=scf_quantities)),
            # different format for scf loop
            Quantity(
                'self_consistency',
                rf'{re_n} *SCF\s*\d+\s*:([ \|\-\+Ee\d\.s]+)', repeats=True,
                sub_parser=TextParser(quantities=[Quantity(
                    'scf_convergence', r'([\s\S]+)', str_operation=str_to_scf_convergence2,
                    repeats=False, convert=False)])),
            Quantity(
                'date_time', rf'{re_n} *Date\s*:(\s*\d+), Time\s*:(\s*[\d\.]+)\s*', repeats=False,
                convert=False),
            Quantity(
                'structure',
                rf'Atomic structure.*:\s+.*x \[A\]\s*y \[A\]\s*z \[A\]([\s\S]+?Species[\s\S]+?(?:{re_n} *{re_n}| 1\: ))',
                repeats=False, convert=False, sub_parser=TextParser(quantities=structure_quantities)),
            Quantity(
                'structure',
                rf'{re_n} *(atom +{re_float}[\s\S]+?(?:{re_n} *{re_n}|\-\-\-))',
                repeats=False, convert=False, sub_parser=TextParser(quantities=structure_quantities)),
            Quantity(  # This quantity is double defined in self._quantities
                'lattice_vectors',
                rf'{re_n} *lattice_vector([\d\.\- ]+){re_n} *lattice_vector([\d\.\- ]+){re_n} *lattice_vector([\d\.\- ]+)',
                unit='angstrom', repeats=False, shape=(3, 3), dtype=float),
            Quantity(
                'energy',
                rf'{re_n} *Energy and forces in a compact form:([\s\S]+?(?:{re_n}{re_n}|Electronic free energy\s*:\s*[\d\.\-Ee]+ eV))',
                str_operation=str_to_energy_components, repeats=False, convert=False),
            # in some cases, the energy components are also printed for after a calculation
            # same format as in scf iteration, they are printed also in initialization
            # so we should get last occurence
            Quantity(
                'energy_components',
                rf'{re_n} *Total energy components:([\s\S]+?)((?:{re_n}{re_n}|\| Electronic free energy per atom\s*:\s*[\d\.\-Ee]+ eV))',
                repeats=True, str_operation=str_to_energy_components, convert=False),
            Quantity(
                'energy_xc',
                rf'{re_n} *Start decomposition of the XC Energy([\s\S]+?)End decomposition of the XC Energy',
                str_operation=str_to_energy_components, repeats=False, convert=False),
            eigenvalues,
            Quantity(
                'forces', rf'{re_n} *Total atomic forces.*?\[eV/Ang\]:\s*([\d\.Ee\-\+\s\|]+)',
                str_operation=str_to_atomic_forces, repeats=False, convert=False),
            # TODO no metainfo for scf forces but old parser put it in atom_forces_free_raw
            Quantity(
                'forces_raw', rf'{re_n} *Total forces\([\s\d]+\)\s*:([\s\d\.\-\+Ee]+){re_n}', repeats=True,
                dtype=float),
            Quantity(
                'time_force_evaluation',
                rf'{re_n} *\| Time for this force evaluation\s*:\s*([\d\.]+) s\s*([\d\.]+) s',
                repeats=False, dtype=float),
            Quantity(
                'total_dos_files', r'Calculating total density of states([\s\S]+?)\-{5}',
                str_operation=str_to_dos_files, repeats=False, convert=False),
            Quantity(
                'atom_projected_dos_files', r'Calculating atom\-projected density of states([\s\S]+?)\-{5}',
                str_operation=str_to_dos_files, repeats=False, convert=False),
            Quantity(
                'species_projected_dos_files', r'Calculating angular momentum projected density of states([\s\S]+?)\-{5}',
                str_operation=str_to_dos_files, repeats=False, convert=False),
            Quantity(
                'vdW_TS',
                rf'(Evaluating non\-empirical van der Waals correction[\s\S]+?)(?:\|\s*Converged\.|\-{5}{re_n}{re_n})',
                repeats=False, sub_parser=TextParser(quantities=[
                    Quantity(
                        'kind', r'Evaluating non\-empirical van der Waals correction \(([\w /]+)\)',
                        repeats=False, convert=False, flatten=False),
                    Quantity(
                        'atom_hirshfeld', r'\| Atom\s*\d+:([\s\S]+?)\-{5}',
                        str_operation=str_to_hirshfeld, repeats=True, convert=False)])),
            Quantity(
                'converged', r'Self\-consistency cycle (converged)\.', repeats=False, dtype=str)]

        molecular_dynamics_quantities = [
            Quantity(
                'md_run',
                r' *Running\s*Born-Oppenheimer\s*molecular\s*dynamics\s*in\s*([A-Z]{3})\s*ensemble*\D*\s*with\s*([A-Za-z\-]*)\s*thermostat',
                repeats=False, convert=False),
            Quantity(
                'md_timestep',
                rf'{re_n} *Molecular dynamics time step\s*=\s*({re_float} [A-Za-z]*)\s*{re_n}',
                str_operation=str_to_quantity, repeats=False, convert=False),
            Quantity(
                'md_simulation_time',
                rf'{re_n} *\| *simulation time\s*=\s*({re_float} [A-Za-z]*)\s*{re_n}',
                str_operation=str_to_quantity, repeats=False, convert=False),
            Quantity(
                'md_temperature',
                rf'{re_n} *\| *at temperature\s*=\s*({re_float} [A-Za-z]*)\s*{re_n}',
                str_operation=str_to_quantity, repeats=False, convert=False),
            Quantity(
                'md_thermostat_mass',
                rf'{re_n} *\| *thermostat effective mass\s*=\s*({re_float})\s*{re_n}',
                str_operation=str_to_quantity, repeats=False, convert=False),
            Quantity(
                'md_thermostat_units',
                rf'Thermostat\s*units\s*for\s*molecular\s*dynamics\s*:\s*([A-Za-z\^\-0-9]*)',
                str_operation=str_to_ureg, repeats=False, convert=False),
            Quantity(
                'md_calculation_info',
                rf'{re_n} *Advancing structure using Born-Oppenheimer Molecular Dynamics:\s*{re_n}'
                rf' *Complete information for previous time-step:'
                rf'([\s\S]+?)((?:{re_n}{re_n}|\| Nose-Hoover Hamiltonian\s*:\s*[Ee\d\.\-\+]+ eV))',
                str_operation=str_to_md_calculation_info, repeats=False, convert=False),
            Quantity(
                'md_system_info',
                rf'Atomic structure.*as used in the preceding time step:\s*{re_n}'
                rf'([\s\S]+?)((?:{re_n}{re_n}|\s*Begin self-consistency loop))',
                repeats=False, convert=False, sub_parser=TextParser(quantities=[
                    Quantity(
                        'positions',
                        rf'atom +({re_float})\s+({re_float})\s+({re_float})',
                        dtype=np.dtype(np.float64), repeats=True),
                    Quantity(
                        'velocities',
                        rf'velocity\s+({re_float})\s+({re_float})\s+({re_float})',
                        dtype=np.dtype(np.float64), repeats=True)]))]

        tail = '|'.join([
            r'Time for this force evaluation\s*:\s*[s \d\.]+',
            r'Final output of selected total energy values',
            r'No geometry change',
            r'Leaving FHI\-aims',
            r'\Z'])

        self._quantities = [
            Quantity(
                Program.version, r'(?:Version|FHI\-aims version)\s*\:*\s*([\d\.]+)\s*',
                repeats=False),
            Quantity(
                xsection_run.x_fhi_aims_program_compilation_date, r'Compiled on ([\d\/]+)',
                repeats=False),
            Quantity(
                xsection_run.x_fhi_aims_program_compilation_time, r'at (\d+\:\d+\:\d+)',
                repeats=False),
            Quantity(
                Program.compilation_host, r'on host ([\w\.\-]+)',
                repeats=False),
            Quantity(
                xsection_run.x_fhi_aims_program_execution_date, r'Date\s*:\s*([0-9]+)',
                repeats=False),
            Quantity(
                xsection_run.x_fhi_aims_program_execution_time, rf'Time\s*:\s*([0-9\.]+){re_n}',
                repeats=False),
            Quantity(
                TimeRun.cpu1_start,
                r'Time zero on CPU 1\s*:\s*([0-9\-E\.]+)\s*(?P<__unit>\w+)\.',
                repeats=False),
            Quantity(
                TimeRun.wall_start,
                r'Internal wall clock time zero\s*:\s*([0-9\-E\.]+)\s*(?P<__unit>\w+)\.',
                repeats=False),
            Quantity(
                Run.raw_id, r'aims_uuid\s*:\s*([\w\-]+)', repeats=False),
            Quantity(
                xsection_run.x_fhi_aims_number_of_tasks, r'Using\s*(\d+)\s*parallel tasks',
                repeats=False),
            Quantity(
                x_fhi_aims_section_parallel_task_assignement.x_fhi_aims_parallel_task_nr,
                r'Task\s*(\d+)\s*on host', repeats=True),
            Quantity(
                x_fhi_aims_section_parallel_task_assignement.x_fhi_aims_parallel_task_host,
                r'Task\s*\d+\s*on host\s*([\s\S]+?)reporting', repeats=True, flatten=False),
            Quantity(
                'fhi_aims_files', r'(?:FHI\-aims file:|Parsing)\s*([\w\/\.]+)', repeats=True),
            Quantity(
                'array_size_parameters',
                r'Basic array size parameters:\s*([\|:\s\w\.\/]+:\s*\d+)', repeats=False,
                str_operation=str_to_array_size_parameters, convert=False),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_hse_unit,
                r'hse_unit: Unit for the HSE06 hybrid functional screening parameter set to\s*(\w)',
                str_operation=FHIAimsControlParser.str_to_unit, repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_hybrid_xc_coeff,
                r'hybrid_xc_coeff: Mixing coefficient for hybrid-functional exact exchange modified to\s*([\d\.]+)',
                repeats=False),
            Quantity(
                'k_grid',
                rf'{re_n} *Found k-point grid:\s*([\d ]+)', repeats=False),   # taken from tests/data/fhi_aims
            Quantity(
                xsection_run.x_fhi_aims_controlInOut_MD_time_step,
                rf'{re_n} *Molecular dynamics time step\s*=\s*([\d\.]+)\s*(?P<__unit>[\w]+)',
                repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_relativistic,
                rf'{re_n} *Scalar relativistic treatment of kinetic energy:\s*([\w\- ]+)',
                repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_relativistic,
                rf'{re_n} *(Non-relativistic) treatment of kinetic energy',
                repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_relativistic_threshold,
                rf'{re_n} *Threshold value for ZORA:\s*([\d\.Ee\-\+])', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_xc,
                rf'{re_n} *XC:\s*(?:Using)*\s*([\w\- ]+) with OMEGA =\s*([\d\.Ee\-\+]+)',
                repeats=False, dtype=None),
            Quantity(
                'petukhov',
                rf'{re_n} *Fixing petukhov mixing factor to\s+(\d?\.[\d]+)', repeats=False,
                dtype=np.dtype(np.float64)),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_xc,
                r'XC: (?:Running|Using) ([\-\w \(\) ]+)', repeats=False),
            Quantity(
                xsection_method.x_fhi_aims_controlInOut_xc,
                rf'{re_n} *(Hartree-Fock) calculation starts \.\.\.', repeats=False),
            Quantity(
                'band_segment_points',
                r'Plot band\s*\d+\s*\|\s*begin[ \d\.\-]+\s*\|\s*end[ \d\.\-]+\s*\|\s*number of points:\s*(\d+)',
                repeats=True),
            Quantity(
                'species',
                rf'(Reading configuration options for species [\s\S]+?)(?:{re_n} *Finished|{re_n} *{re_n})',
                str_operation=str_to_species_in, repeats=False),
            Quantity(
                'control_inout',
                rf'{re_n} *Reading file control\.in\.\s*\-*\s*([\s\S]+?)'
                r'(?:Finished reading input file \'control\.in\'|Input file control\.in ends\.)', repeats=False,
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'species', r'Reading configuration options for (species[\s\S]+?)grid points\.',
                        repeats=True, str_operation=str_to_species), *molecular_dynamics_quantities])),
            Quantity(
                'control_in_verbatim',
                rf'{re_n}  *Parsing control\.in([\S\s]*)Completed first pass over input file control\.in', repeats=False,
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'md_controlin',
                        rf' *([\_a-zA-Z\d\-]*MD[\_a-zA-Z\d\-]*)\s+([a-zA-Z\d\.\-\_\^]+.*){re_n}',
                        str_operation=str_to_md_control_in, repeats=True, convert=False)])),
            # GW input quantities
            Quantity(
                'gw_flag', rf'{re_n}\s*qpe_calc\s*([\w]+)', repeats=False),
            Quantity(
                'gw_flag', rf'{re_n}\s*sc_self_energy\s*([\w]+)', repeats=False),
            Quantity(
                'anacon_type', rf'{re_n}\s*anacon_type\s*(\d+)', repeats=False),
            Quantity(
                'gw_analytical_continuation',
                rf'{re_n} (?:Using)*\s*([\w\-\s]+) for analytical continuation',
                repeats=False, flatten=True, str_operation=lambda x: [y.lower() for v in x.split(' ') for y in v.split('-')]),
            Quantity(
                'k_grid',
                rf'{re_n} *k\_grid\s*([\d ]+)', repeats=False),
            Quantity(
                'freq_grid_type', rf'{re_n}\s*Initialising([\w\-\s]+)time and frequency grids',
                repeats=False),
            Quantity(
                'n_freq', rf'{re_n}\s*frequency_points\s*(\d+)', repeats=False,
                dtype=int),
            Quantity(
                'frequency_data', r'\s*\|*\s*i_freq\s*([\d*\s*.+eE\-\+]+)',
                repeats=True, str_operation=str_to_frequency),
            Quantity(
                'frozen_core', rf'{re_n}\s*frozen_core_scf\s*(\d+)', repeats=False,
                dtype=int),
            Quantity(
                'n_states_gw',
                r'\|\s*Number of Kohn-Sham states \(occupied \+ empty\)\s*\:\s*(\d+)',
                repeats=False),
            Quantity(
                'gw_self_consistency', r'GW Total Energy Calculation([\s\S]+?)\-{5}',
                repeats=True, str_operation=str_to_gw_scf, convert=False),
            Quantity(
                'gw_eigenvalues', r'(state\s*occ_num\s*e_gs[\s\S]+?)\s*\| Total time',
                str_operation=str_to_gw_eigs, repeats=False, convert=False),
            # assign the initial geometry to full scf as no change in structure is done
            # during the initial scf step
            Quantity(
                'lattice_vectors',
                r'Input geometry:\s*\|\s*Unit cell:\s*'
                r'\s*\|\s*([\d\.\-\+eE\s]+)\s*\|\s*([\d\.\-\+eE\s]+)\s*\|\s*([\d\.\-\+eE\s]+)',
                repeats=False, unit='angstrom', shape=(3, 3), dtype=float),
            Quantity(
                'structure',
                rf'Atomic structure.*:\s+.*x \[A\]\s*y \[A\]\s*z \[A\]([\s\S]+?Species[\s\S]+?(?:{re_n} *{re_n}| 1\: ))',
                repeats=False, convert=False, sub_parser=TextParser(quantities=structure_quantities)),
            Quantity(
                'lattice_vectors_reciprocal',
                r'Quantities derived from the lattice vectors:\s*'
                r'\s*\|\s*Reciprocal lattice vector \d:([\d\.\-\+eE\s]+)\s*\|\s*Reciprocal lattice vector \d:([\d\.\-\+eE\s]+)\s*\|\s*Reciprocal lattice vector \d:([\d\.\-\+eE\s]+)',
                repeats=False, unit='1/angstrom', shape=(3, 3), dtype=float),
            Quantity(
                'full_scf',
                r'Begin self-consistency loop: Initialization'
                rf'([\s\S]+?(?:{tail}))',
                repeats=True, sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity(
                'geometry_optimization',
                rf'{re_n} *Geometry optimization: Attempting to predict improved coordinates\.'
                rf'([\s\S]+?(?:{tail}))',
                repeats=True, sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity(
                'molecular_dynamics',
                rf'{re_n} *Molecular dynamics: Attempting to update all nuclear coordinates\.'
                rf'([\s\S]+?(?:{tail}))',
                repeats=True, sub_parser=TextParser(quantities=[*calculation_quantities, *molecular_dynamics_quantities]))]
        # TODO add SOC perturbed eigs, dielectric function

    def get_number_of_spin_channels(self):
        return self.get('array_size_parameters', {}).get('Number of spin channels', 1)


class FHIAimsParser(BeyondDFTWorkflowsParser):
    def __init__(self):
        self.out_parser = FHIAimsOutParser()
        self.control_parser = FHIAimsControlParser()
        self.dos_parser = DataTextParser()
        self.bandstructure_parser = DataTextParser()
        self._calculation_type = 'dft'
        self._child_archives = {}

        self._xc_map = {
            'Perdew-Wang parametrisation of Ceperley-Alder LDA': [
                {'name': 'LDA_C_PW'}, {'name': 'LDA_X'}],
            'Perdew-Zunger parametrisation of Ceperley-Alder LDA': [
                {'name': 'LDA_C_PZ'}, {'name': 'LDA_X'}],
            'VWN-LDA parametrisation of VWN5 form': [
                {'name': 'LDA_C_VWN'}, {'name': 'LDA_X'}],
            'VWN-LDA parametrisation of VWN-RPA form': [
                {'name': 'LDA_C_VWN_RPA'}, {'name': 'LDA_X'}],
            'AM05 gradient-corrected functionals': [
                {'name': 'GGA_C_AM05'}, {'name': 'GGA_X_AM05'}],
            'BLYP functional': [{'name': 'GGA_C_LYP'}, {'name': 'GGA_X_B88'}],
            'PBE gradient-corrected functionals': [
                {'name': 'GGA_C_PBE'}, {'name': 'GGA_X_PBE'}],
            'PBEint gradient-corrected functional': [
                {'name': 'GGA_C_PBEINT'}, {'name': 'GGA_X_PBEINT'}],
            'PBEsol gradient-corrected functionals': [
                {'name': 'GGA_C_PBE_SOL'}, {'name': 'GGA_X_PBE_SOL'}],
            'RPBE gradient-corrected functionals': [
                {'name': 'GGA_C_PBE'}, {'name': 'GGA_X_RPBE'}],
            'revPBE gradient-corrected functionals': [
                {'name': 'GGA_C_PBE'}, {'name': 'GGA_X_PBE_R'}],
            'PW91 gradient-corrected functionals': [
                {'name': 'GGA_C_PW91'}, {'name': 'GGA_X_PW91'}],
            'M06-L gradient-corrected functionals': [
                {'name': 'MGGA_C_M06_L'}, {'name': 'MGGA_X_M06_L'}],
            'M11-L gradient-corrected functionals': [
                {'name': 'MGGA_C_M11_L'}, {'name': 'MGGA_X_M11_L'}],
            'TPSS gradient-corrected functionals': [
                {'name': 'MGGA_C_TPSS'}, {'name': 'MGGA_X_TPSS'}],
            'TPSSloc gradient-corrected functionals': [
                {'name': 'MGGA_C_TPSSLOC'}, {'name': 'MGGA_X_TPSS'}],
            'hybrid B3LYP functional': [
                {'name': 'HYB_GGA_XC_B3LYP5'}],
            'Hartree-Fock': [{'name': 'HF_X'}],
            'HSE': [{'name': 'HYB_GGA_XC_HSE03'}],
            'HSE-functional': [{'name': 'HYB_GGA_XC_HSE06'}],
            'hybrid-PBE0 functionals': [
                {'name': 'GGA_C_PBE'}, {
                    'name': 'GGA_X_PBE', 'weight': lambda x: 0.75 if x is None else 1.0 - x},
                {'name': 'HF_X', 'weight': lambda x: 0.25 if x is None else x}],
            'hybrid-PBEsol0 functionals': [
                {'name': 'GGA_C_PBE_SOL'}, {
                    'name': 'GGA_X_PBE_SOL', 'weight': lambda x: 0.75 if x is None else 1.0 - x},
                {'name': 'HF_X', 'weight': lambda x: 0.25 if x is None else x}],
            'Hybrid M06 gradient-corrected functionals': [{'name': 'MGGA_C_M06'}, {'name': 'HYB_MGGA_X_M06'}],
            'Hybrid M06-2X gradient-corrected functionals': [
                {'name': 'MGGA_C_M06_2X'}, {'name': 'HYB_MGGA_X_M06'}],
            'Hybrid M06-HF gradient-corrected functionals': [
                {'name': 'MGGA_C_M06_HF'}, {'name': 'HYB_MGGA_X_M06'}],
            'Hybrid M08-HX gradient-corrected functionals': [
                {'name': 'MGGA_C_M08_HX'}, {'name': 'HYB_MGGA_X_M08_HX'}],
            'Hybrid M08-SO gradient-corrected functionals': [
                {'name': 'MGGA_C_M08_SO'}, {'name': 'HYB_MGGA_X_M08_SO'}],
            'Hybrid M11 gradient-corrected functionals': [{'name': 'MGGA_C_M11'}, {'name': 'HYB_MGGA_X_M11'}]}

        # TODO update metainfo to reflect all energy corrections
        # why section_vdW_TS under x_fhi_aims_section_controlInOut_atom_species?
        self._energy_map = {
            'Total energy uncorrected': 'energy_total',
            'Total energy corrected': 'energy_total_t0',
            'Electronic free energy': 'energy_free',
            'X Energy': 'energy_exchange',
            'C Energy GGA': 'energy_correlation',
            'Total XC Energy': 'energy_xc',
            'X Energy LDA': 'x_fhi_aims_energy_X_LDA',
            'C Energy LDA': 'x_fhi_aims_energy_C_LDA',
            'Sum of eigenvalues': 'energy_sum_eigenvalues',
            'XC energy correction': 'energy_correction_xc',
            'XC potential correction': 'energy_xc_potential',
            'Free-atom electrostatic energy': 'x_fhi_aims_energy_electrostatic_free_atom',
            'Hartree energy correction': 'energy_correction_hartree',
            'vdW energy correction': 'energy_van_der_waals',
            'Entropy correction': 'energy_correction_entropy',
            'Total energy': 'energy_total',
            'Total energy, T -> 0': 'energy_total_t0',
            'Kinetic energy': 'energy_kinetic_electronic',
            'Electrostatic energy': 'energy_electrostatic',
            'error in Hartree potential': 'energy_correction_hartree',
            'Sum of eigenvalues per atom': 'energy_sum_eigenvalues_per_atom',
            'Total energy (T->0) per atom': 'energy_total_t0_per_atom',
            'Electronic free energy per atom': 'energy_free_per_atom',
            'Hartree-Fock part': 'energy_hartree_fock_x_scaled',
            # GW
            'Galitskii-Migdal Total Energy': 'x_fhi_aims_scgw_galitskii_migdal_total_energy',
            'GW Kinetic Energy': 'x_fhi_aims_scgw_kinetic_energy',
            'Hartree energy from GW density': 'x_fhi_aims_scgw_hartree_energy_sum_eigenvalues',
            'GW correlation Energy': 'x_fhi_aims_energy_scgw_correlation_energy',
            'RPA correlation Energy': 'x_fhi_aims_scgw_rpa_correlation_energy',
            'Sigle Particle Energy': 'x_fhi_aims_single_particle_energy',
            'Fit accuracy for G(w)': 'x_fhi_aims_poles_fit_accuracy',
            # Convergence
            'Change of total energy': 'energy_change',
        }

        self._relativity_map = {
            'Non-relativistic': None,
            'ZORA': 'scalar_relativistic',
            'on-site free-atom approximation to ZORA': 'scalar_relativistic_atomic_ZORA'
        }

        self._property_map = {
            'atom': 'x_fhi_aims_atom_type_vdW',
            'Free atom volume': 'x_fhi_aims_free_atom_volume',
            'Hirshfeld charge': 'x_fhi_aims_hirschfeld_charge',
            'Hirshfeld volume': 'x_fhi_aims_hirschfeld_volume'
        }

        self._gw_flag_map = {
            'gw': 'G0W0',
            'gw_expt': 'G0W0',
            'ev_scgw0': 'ev-scGW',
            'ev_scgw': 'ev-scGW',
            'scgw': 'scGW'
        }

        self.gw_analytical_continuation = ['multi_pole', 'pade']

        self._gw_qp_energies_map = {
            'occ_num': 'occupations',
            'e_gs': 'value_ks',
            'e_x^ex': 'value_exchange',
            'e_xc^gs': 'value_ks_xc',
            'e_c^nloc': 'value_correlation',
            'e_qp': 'value_qp'
        }

        self._md_calculation_map = {
            'Time step number': 'step',
            'Simulation time': 'time',
            'Temperature (nuclei)': 'temperature',
        }
        self._md_calculation_energy_map = {
            'Nuclear kinetic energy': 'kinetic',
            'Total energy (el.+nuc.)': 'total',
        }
        self._md_methods_map = {
            'Nose-Hoover': 'nose_hoover',
            'Bussi-Donadio-Parrinello': 'velocity_rescaling',
            'Andersen': 'andersen',
            'Andersen stochastic': 'andersen',
            'Berendsen': 'berendsen'
            # TODO: Add GLE thermostat
        }

        self._frame_rate = None
        # max cumulative number of atoms for all parsed trajectories to calculate sampling rate
        self._cum_max_atoms = 100000

    @property
    def frame_rate(self):
        if self._frame_rate is None:
            n_frames = 0
            for calc_type in ['full_scf', 'geometry_optimization', 'molecular_dynamics']:
                n_frames += len(self.out_parser.get(calc_type, []))
            n_atoms = len(self.out_parser.get('structure', {}).get('positions', []))
            if n_atoms == 0 or n_frames == 0:
                self._frame_rate = 1
            else:
                cum_atoms = n_atoms * n_frames
                self._frame_rate = 1 if cum_atoms <= self._cum_max_atoms else cum_atoms // self._cum_max_atoms
        return self._frame_rate

    def get_fhiaims_file(self, default):
        base, *ext = default.split('.')
        ext = '.'.join(ext)
        base = base.lower()
        files = os.listdir(self.maindir)
        files = [os.path.basename(f) for f in files]
        files = [os.path.join(
            self.maindir, f) for f in files if base.lower() in f.lower() and f.endswith(ext)]
        files.sort()
        return files

    def parse_bandstructure(self, energy_fermi):
        sec_run = self.archive.run[-1]

        band_segments_points = self.out_parser.get('band_segment_points')
        if band_segments_points is None:
            return

        # band structure, unlike dos is not a property of a section_scc but of the
        # the whole run. dos output file is contained in a section
        sec_scc = sec_run.calculation[-1]

        energy_fermi_ev = energy_fermi.to(ureg.electron_volt).magnitude
        sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
        sec_k_band.energy_fermi = energy_fermi

        nspin = self.out_parser.get_number_of_spin_channels()
        nbands = None
        for n in range(len(band_segments_points)):
            if self._calculation_type == 'dft':
                bs_files = [
                    os.path.join(self.out_parser.maindir, 'band%d%03d.out' % (s + 1, n + 1))
                    for s in range(nspin)
                ]
            elif self._calculation_type == 'gw':
                bs_files = [
                    os.path.join(self.out_parser.maindir, 'GW_band%d%03d.out' % (s + 1, n + 1))
                    for s in range(nspin)
                ]
            else:
                self.logger.warning('_calculation_type not found. Only DFT or GW allowed.')

            data = []
            for band_file in bs_files:
                self.bandstructure_parser.mainfile = band_file
                if self.bandstructure_parser.data is None:
                    break
                data.append(self.bandstructure_parser.data)

            if len(data) == 0:
                continue

            data = np.transpose(data)
            eigs = (np.transpose(data[5::2]) + energy_fermi_ev) * ureg.eV
            nbands = np.shape(eigs)[-1] if n == 0 else nbands if nbands is not None else np.shape(eigs)[-1]
            if nbands != np.shape(eigs)[-1]:
                self.logger.warning('Inconsistent number of bands found in bandstructure data.')
                continue

            sec_k_band_segment = sec_k_band.m_create(BandEnergies)
            sec_k_band_segment.kpoints = np.transpose(data[1:4])[0]
            occs = np.transpose(data[4::2])
            # the band energies stored in the band*.out files have already
            # been shifted to the fermi energy. This shift is undone so
            # that the energy scales for for energy_reference_fermi, band
            # energies and the DOS energies match.
            sec_k_band_segment.energies = eigs
            sec_k_band_segment.occupations = occs

    def parse_gw(self):
        sec_run = self.archive.run[-1]

        # GW method
        sec_method = sec_run.m_create(Method)
        # GW
        sec_gw = sec_method.m_create(GW)
        sec_gw.type = self._gw_flag_map.get(self.out_parser.get('gw_flag'), None)
        sec_gw.n_states = self.out_parser.get('n_states_gw')
        # KMesh
        if self.out_parser.get('k_grid') is not None:
            sec_k_mesh = sec_method.m_create(KMesh)
            sec_k_mesh.grid = self.out_parser.get('k_grid')
        # QMesh copied from KMesh
            sec_gw.m_add_sub_section(GW.q_mesh, sec_k_mesh)
        # Analytical continuation
        sec_gw.analytical_continuation = self.gw_analytical_continuation[
            self.out_parser.get('anacon_type', 1)]
        # FrequencyMesh
        frequency_data = self.out_parser.get('frequency_data', [])
        if len(frequency_data) > 0:
            freq_points = np.array(frequency_data)[:, 1] * ureg.hartree
        else:
            freq_points = None
        freq_grid_type = self.out_parser.get('freq_grid_type', 'Gauss-Legendre')
        if isinstance(freq_grid_type, list):
            freq_grid_type = freq_grid_type[-1]
        elif freq_grid_type == 'logarithmic':
            freq_grid_type = freq_grid_type.capitalize()
        sec_freq_mesh = FrequencyMesh(
            dimensionality=1,
            sampling_method=freq_grid_type,
            n_points=self.out_parser.get('n_freq', 100),
            points=freq_points)
        sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)

        # GW calculation
        sec_scc = sec_run.m_create(Calculation)
        # References
        sec_energy = sec_scc.m_create(Energy)
        for n, section in enumerate(self.out_parser.get('full_scf', [])):
            # skip frames for large trajectories
            if (n % self.frame_rate) > 0:
                continue
            self.parse_system(section)

            # Fermi level
            scf_iterations = section.get('self_consistency', [])
            last_scf_iteration = scf_iterations[len(scf_iterations) - 1]
            if last_scf_iteration.get('fermi_level') is not None:
                sec_energy.fermi = last_scf_iteration.get('fermi_level')
                try:
                    last_scf_iteration.get('fermi_level').units
                except Exception:
                    self.logger.warning('Erorr setting the Fermi level: no units')
        sec_scc.method_ref = sec_method
        if sec_run.system is not None:
            sec_scc.system_ref = sec_run.system[-1]

        # Parse GW band structure
        self.parse_bandstructure(sec_energy.fermi)

        # scGW calculation
        gw_scf_energies = self.out_parser.get('gw_self_consistency', [])
        gw_eigenvalues = self.out_parser.get('gw_eigenvalues', None)
        if gw_scf_energies is None and gw_eigenvalues is None:
            return

        for energies in gw_scf_energies:
            sec_gw_scf_iteration = sec_scc.m_create(ScfIteration)
            for key, val in energies.items():
                metainfo_key = self._energy_map.get(key, None)
                if metainfo_key is not None:
                    try:
                        setattr(sec_gw_scf_iteration, metainfo_key, val)
                    except Exception:
                        self.logger.warning(
                            'Error setting scGW metainfo.',
                            details={key: metainfo_key})

        if gw_eigenvalues is not None:
            sec_eigs_gw = sec_scc.m_create(BandEnergies)
            for key, name in self._gw_qp_energies_map.items():
                # TODO verify shape of eigenvalues
                val = gw_eigenvalues[key] if key == 'occ_num' else gw_eigenvalues[key] * ureg.eV
                setattr(sec_eigs_gw, name, np.reshape(val, (1, 1, len(val))))

    def parse_system(self, section):
        sec_run = self.archive.run[-1]

        lattice_vectors = section.get(
            'lattice_vectors', self.out_parser.get('lattice_vectors'))
        lattice_vectors_reciprocal = section.get(
            'lattice_vectors_reciprocal',
            self.out_parser.get('lattice_vectors_reciprocal'))

        structure = section.get(
            'structure', self.out_parser.get('structure'))
        pbc = [lattice_vectors is not None] * 3
        if structure is None:
            return

        sec_system = sec_run.m_create(System)
        sec_atoms = sec_system.m_create(Atoms)
        if lattice_vectors is not None:
            sec_atoms.lattice_vectors = lattice_vectors
        if lattice_vectors_reciprocal is not None:
            sec_atoms.lattice_vectors_reciprocal = lattice_vectors_reciprocal

        sec_atoms.periodic = pbc
        sec_atoms.labels = structure.get('labels')
        sec_atoms.positions = structure.get('positions') * ureg.angstrom
        velocities = structure.get('velocities')
        if velocities is None:
            molecular_dynamics_system_info = section.get('md_system_info', None)
            velocities = molecular_dynamics_system_info._results['velocities'] if molecular_dynamics_system_info else None
        if velocities is not None:
            sec_atoms.velocities = velocities * ureg.angstrom / ureg.ps

    def parse_configurations(self):
        sec_run = self.archive.run[-1]

        def read_dos(dos_file):
            dos_file = self.get_fhiaims_file(dos_file)
            if not dos_file:
                return
            self.dos_parser.mainfile = dos_file[0]
            if self.dos_parser.data is None:
                return
            return np.transpose(self.dos_parser.data)

        def read_projected_dos(dos_files):
            dos = []
            dos_dn = []
            n_atoms = 0
            l_max = []
            for dos_file in dos_files:
                data = read_dos(dos_file)
                if data is None or np.size(data) == 0:
                    continue
                # we first read the spin_dn just to make sure the spin dn component exists
                if 'spin_up' in dos_file:
                    data_dn = read_dos(dos_file.replace('spin_up', 'spin_dn'))
                    if data_dn is None:
                        continue
                    # the maximum l is arbitrary for different species, so we cant stack
                    dos_dn.append(data_dn[1:])
                l_max.append(len(data[1:]))
                # column 0 is energy column 1 is total
                energy = data[0]
                dos.append(data[1:])
                n_atoms += 1

            if not dos:
                return None, None
            energies = energy * ureg.eV
            # we cut the l components up to the minimum (or pad zeros?)
            n_l = min(l_max)
            n_spin = 2 if dos_dn else 1
            dos = [d[:n_l] for d in dos]
            if dos_dn:
                dos_dn = [d[:n_l] for d in dos_dn]
                dos = [dos, dos_dn]
            dos = np.transpose(np.reshape(
                dos, (n_spin, n_atoms, n_l, len(energies))), axes=(2, 0, 1, 3))
            dos = dos / ureg.eV
            return energies, dos

        def parse_dos(section):
            version_normalization_cutoff = 71914.7
            version_normalization = .5

            sec_scc = sec_run.calculation[-1]
            sec_dos = None
            energies = None

            n_spin = self.out_parser.get_number_of_spin_channels()
            # parse total first, we expect only one file
            total_dos_files, _ = section.get('total_dos_files', [['KS_DOS_total_raw.dat'], []])
            for dos_file in total_dos_files:
                data = read_dos(dos_file)
                if data is None or np.size(data) == 0:
                    continue
                sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
                energies = data[0] * ureg.eV
                sec_dos.n_energies = len(energies)
                sec_dos.energies = energies
                # dos unit is 1/(eV-cell volume)
                dos = data[1: n_spin + 1] / ureg.eV
                for spin in range(len(dos)):
                    sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
                    sec_dos_values.spin = spin
                    if float(sec_run.program.version) <= version_normalization_cutoff:
                        sec_dos_values.x_fhi_aims_normalization_factor_raw_data = version_normalization
                        dos[spin] /= version_normalization
                    sec_dos_values.value = dos[spin]

            # parse projected
            # projected does for different spins on separate files
            # we only include spin_up, add spin_dn in loop
            for projection_type in ['atom', 'species']:
                proj_dos_files, species = section.get(
                    '%s_projected_dos_files' % projection_type, [[], []])
                proj_dos_files = [f for f in proj_dos_files if 'spin_dn' not in f]
                if proj_dos_files:
                    if sec_dos is None:
                        sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
                    energies, dos = read_projected_dos(proj_dos_files)
                    if dos is None:
                        continue
                    sec_def = Dos.atom_projected if projection_type == 'atom' else Dos.species_projected

                    n_l = len(dos[1:])
                    lm_values = np.column_stack((np.arange(n_l), np.zeros(n_l, dtype=np.int32)))
                    for lm in range(len(dos)):
                        for spin in range(len(dos[lm])):
                            for atom in range(len(dos[lm][spin])):
                                sec_dos_values = sec_dos.m_create(DosValues, sec_def)
                                sec_dos.m_kind = 'integrated'
                                if lm > 0:
                                    # the first one is total so no lm label
                                    sec_dos_values.lm = lm_values[lm - 1]
                                sec_dos_values.spin = spin
                                if projection_type == 'atom':
                                    sec_dos_values.atom_index = atom
                                else:
                                    sec_dos_values.atom_label = species[atom]
                                sec_dos_values.value = dos[lm][spin][atom]

        def get_eigenvalues(section):
            data = section.get('eigenvalues', [None])[-1]
            if data is None:
                return
            n_spin = self.out_parser.get_number_of_spin_channels()

            kpts = data.get('kpoints', [np.zeros(3)] * n_spin)
            if len(kpts) % n_spin != 0:
                self.logger.warning('Inconsistent number of spin channels found.')
                n_spin -= 1
            kpts = np.reshape(kpts, (len(kpts) // n_spin, n_spin, 3))
            kpts = np.transpose(kpts, axes=(1, 0, 2))[0]
            kpts = None if len(kpts) == 0 else kpts

            occs_eigs = data.get('occupation_eigenvalue')
            n_eigs = len(occs_eigs) // (len(kpts) * n_spin)
            occs_eigs = np.transpose(
                np.reshape(occs_eigs, (len(kpts), n_spin, n_eigs, 2)), axes=(3, 1, 0, 2))

            return kpts, occs_eigs[1] * ureg.hartree, occs_eigs[0]

        def parse_scf(iteration):
            sec_scc = sec_run.calculation[-1]
            sec_scf = sec_scc.m_create(ScfIteration)

            date_time = iteration.get('date_time')
            if date_time is not None:
                sec_scf.x_fhi_aims_scf_date_start = date_time[0]
                sec_scf.x_fhi_aims_scf_time_start = date_time[1]

            sec_energy = sec_scf.m_create(Energy)
            energies = iteration.get('energy_components', {})
            convergence = iteration.get('scf_convergence', {})
            energies.update(convergence)
            for key, val in energies.items():
                metainfo_key = self._energy_map.get(key, None)
                if metainfo_key is not None:
                    if metainfo_key == 'energy_change':
                        sec_energy.change = val
                    elif metainfo_key.startswith('energy_') and not metainfo_key.endswith('per_atom'):
                        try:
                            setattr(sec_energy, metainfo_key.replace('energy_', ''), EnergyEntry(
                                value=val, value_per_atom=energies.get('%s_per_atom' % metainfo_key)))
                        except Exception:
                            self.logger.warning('Error setting scf energy metainfo.', details={key: metainfo_key})
                    else:
                        try:
                            setattr(sec_scf, metainfo_key, val)
                        except Exception:
                            self.logger.warning('Error setting scf energy metainfo.', details={key: metainfo_key})

            if iteration.get('fermi_level') is not None:
                sec_energy.fermi = iteration.get('fermi_level')
                try:
                    iteration.get('fermi_level').units
                except Exception:
                    self.logger.warning('Erorr setting the Fermi level: no units')

            # eigenvalues scf iteration
            eigenvalues = get_eigenvalues(iteration)
            if eigenvalues is not None:
                sec_eigenvalues = sec_scf.m_create(BandEnergies)
                if eigenvalues[0] is not None:
                    sec_eigenvalues.kpoints = eigenvalues[0]
                sec_eigenvalues.energies = eigenvalues[1]
                sec_eigenvalues.occupations = eigenvalues[2]

            # stress tensor
            stress_tensor = iteration.get('stress_tensor')
            if stress_tensor is not None:
                sec_stress = sec_scf.m_create(Stress)
                sec_stress.total = StressEntry(value=stress_tensor)

            # pressure
            pressure = iteration.get('pressure')
            if pressure is not None:
                sec_thermo = sec_scf.m_create(Thermodynamics)
                sec_thermo.pressure = pressure

        def parse_vdW(section):
            # these are not actually vdW outputs but vdW control parameters but are
            # printed within the calculation section.
            # TODO why is x_fhi_aims_section_vdW_TS under x_fhi_aims_section_controlInOut_atom_species
            # we would then have to split the vdW parameters by species
            atoms = section.get('vdW_TS', {}).get('atom_hirshfeld', [])
            if not atoms:
                return
            # get species from section_atom_type
            sec_atom_type = sec_run.method[-1].atom_parameters
            if not sec_atom_type:
                return

            for sec in sec_atom_type:
                for atom in atoms:
                    if sec.label == atom['atom']:
                        sec_vdW_ts = sec.x_fhi_aims_section_controlInOut_atom_species[-1].m_create(
                            x_fhi_aims_section_vdW_TS)
                        for key, val in atom.items():
                            metainfo_name = self._property_map.get(key, None)
                            if metainfo_name is None:
                                continue
                            val = val[0] if len(val) == 1 else val
                            try:
                                setattr(sec_vdW_ts, metainfo_name, val)
                            except Exception:
                                self.logger.warning('Error setting vdW metainfo.', details={key: metainfo_name})
                            # TODO add the remanining properties
            sec_run.method[-1].electronic.van_der_waals_method = 'TS'

        def parse_section(section):
            self.parse_system(section)

            sec_scc = sec_run.m_create(Calculation)
            sec_scc.system_ref = sec_run.system[-1]
            sec_scc.method_ref = sec_run.method[-1]

            sec_energy = sec_scc.m_create(Energy)
            energy = section.get('energy', {})
            energy.update(section.get('energy_components', [{}])[-1])
            energy.update(section.get('energy_xc', {}))
            for key, val in energy.items():
                metainfo_key = self._energy_map.get(key, None)
                if metainfo_key is None:
                    continue
                elif key == 'vdW energy correction':
                    kind = section.get('vdW_TS', {}).get('kind', 'Tkatchenko/Scheffler 2009')
                    sec_energy.van_der_waals = EnergyEntry(value=val, kind=kind)
                elif metainfo_key.startswith('x_fhi_aims_energy'):
                    setattr(sec_scc, metainfo_key, val)
                elif metainfo_key.startswith('energy_') and not metainfo_key.endswith('per_atom'):
                    try:
                        setattr(sec_energy, metainfo_key.replace('energy_', ''), EnergyEntry(
                            value=val, value_per_atom=energy.get('%s_per_atom' % metainfo_key)))
                    except Exception:
                        self.logger.warning('Error setting energy metainfo.', details={key: key})

            # eigenvalues
            eigenvalues = get_eigenvalues(section)
            # get if from last scf iteration
            if eigenvalues is not None:
                sec_eigenvalues = sec_scc.m_create(BandEnergies)
                if eigenvalues[0] is not None:
                    sec_eigenvalues.kpoints = eigenvalues[0]
                sec_eigenvalues.energies = eigenvalues[1]
                sec_eigenvalues.occupations = eigenvalues[2]

            # TODO add force contributions and stress
            forces = section.get('forces', None)
            if forces is not None:
                sec_forces = sec_scc.m_create(Forces)
                sec_forces.free = ForcesEntry(value=forces)

                forces_raw = section.get('forces_raw', None)
                if forces_raw is not None:
                    # we are actually reading the scf forces so we take only the last iteration
                    try:
                        # TODO This is a temporary fix to a huge md run I cannot test.
                        # see calc_id=a8r8KkvKXWams50UhzMGCxY0IGqH
                        sec_forces.free.value_raw = forces_raw[-len(forces):] * ureg.eV / ureg.angstrom
                    except Exception:
                        self.logger.warning('Error setting raw forces.')

            time_calculation = section.get('time_force_evaluation')
            if time_calculation is not None:
                sec_scc.time_calculation = time_calculation

            scf_iterations = section.get('self_consistency', [])
            sec_scc.n_scf_iterations = len(scf_iterations)
            for scf_iteration in scf_iterations:
                parse_scf(scf_iteration)

            sec_scc.calculation_converged = section.get(
                'converged') == 'converged'
            # how about geometry optimization convergence

            # density of states
            parse_dos(section)

            # fermi level
            fermi_energy = 0.0
            if scf_iterations:
                if scf_iterations[-1].get('fermi_level') is not None:
                    fermi_energy = scf_iterations[-1].get('fermi_level')
                fermi_energy = fermi_energy.to('joule').magnitude if fermi_energy else 0.0
            sec_scc.energy.fermi = fermi_energy

            # vdW parameters
            parse_vdW(section)

            # step, time, temperature info + additional energies from molecular dynamics
            md_info = section.get('md_calculation_info', {})
            sec_scc.x_fhi_aims_calculation_md = {
                key: str(val.magnitude) + ' ' + str(val.units) if type(val) == ureg.Quantity else str(val)
                for key, val in md_info.items()}
            for key, val in md_info.items():
                if key in self._md_calculation_map:
                    metainfo_key = self._md_calculation_map.get(key, None)
                    if metainfo_key == 'step':
                        val = int(val)
                    if metainfo_key is not None:
                        try:
                            setattr(sec_scc, metainfo_key, val)
                        except Exception:
                            self.logger.warning(
                                'Error setting md calculation metainfo.',
                                details={key: metainfo_key, 'value': val})
                elif key in self._md_calculation_energy_map:
                    metainfo_key = self._md_calculation_energy_map.get(key, None)
                    if metainfo_key is not None:
                        try:
                            setattr(sec_energy, metainfo_key, EnergyEntry(value=val))
                        except Exception:
                            self.logger.warning(
                                'Error setting md calculation energy metainfo.',
                                details={key: metainfo_key, 'value': val})

            # get potential energies
                total_energy = sec_energy.get('total')
                kinetic_energy = sec_energy.get('kinetic')
                if total_energy and kinetic_energy:
                    potential_energy = total_energy.value - kinetic_energy.value
                    try:
                        setattr(sec_energy, 'potential', EnergyEntry(value=potential_energy))
                    except Exception:
                        self.logger.warning(
                            'Error setting potential energy metainfo.')

        for n, section in enumerate(self.out_parser.get('full_scf', [])):
            # skip frames for large trajectories
            if (n % self.frame_rate) > 0:
                continue
            parse_section(section)

        for n, section in enumerate(self.out_parser.get('geometry_optimization', [])):
            # skip frames for large trajectories
            if (n % self.frame_rate) > 0:
                continue
            parse_section(section)

        for n, section in enumerate(self.out_parser.get('molecular_dynamics', [])):
            # skip frames for large trajectories
            if (n % self.frame_rate) > 0:
                continue
            parse_section(section)

        if not sec_run.calculation:
            return

        # bandstructure
        fermi_energy = sec_run.calculation[0].energy.fermi
        self.parse_bandstructure(fermi_energy)

    def parse_workflow(self):
        sec_workflow = self.archive.m_create(Workflow)
        workflow = SinglePoint2()
        sec_workflow.type = 'single_point'
        sec_workflow.calculations_ref = self.archive.run[-1].calculation
        if self.out_parser.get('geometry_optimization') is not None:
            sec_workflow.type = 'geometry_optimization'
            workflow = GeometryOptimization2()
        elif self.out_parser.get('molecular_dynamics', None) is not None:
            workflow = MolecularDynamics(
                method=MolecularDynamicsMethod(), results=MolecularDynamicsResults())

            control_in_md = self.out_parser.get('control_in_verbatim').get('md_controlin')
            if control_in_md:
                workflow.method.x_fhi_aims_controlIn_md = {}
                for input_param in control_in_md:
                    for key, val in input_param.items():
                        workflow.method.x_fhi_aims_controlIn_md[key] = val
            control_inout = self.out_parser.get('control_inout')
            if control_inout:
                workflow.method.thermodynamic_ensemble = control_inout.get('md_run')[0]
                workflow.method.integration_timestep = control_inout.get('md_timestep')

                sec_thermostat_parameters = workflow.method.m_create(ThermostatParameters)
                sec_thermostat_parameters.thermostat_type = self._md_methods_map.get(control_inout.get('md_run')[1])
                simulation_time = control_inout.get('md_simulation_time')
                if (simulation_time is not None) and (workflow.method.integration_timestep is not None):
                    n_steps = (simulation_time.to(ureg.picosecond) / workflow.method.integration_timestep.to(ureg.picosecond)).magnitude
                    workflow.method.n_steps = int(n_steps)
                sec_thermostat_parameters.reference_temperature = control_inout.get('md_temperature')
                thermostat_mass = control_inout.get('md_thermostat_mass')
                if type(thermostat_mass != ureg.Quantity):
                    thermostat_mass_unit = control_inout.get('md_thermostat_units')
                    sec_thermostat_parameters.coupling_constant = 1.0 / (ureg.speed_of_light * thermostat_mass * thermostat_mass_unit) if thermostat_mass_unit is not None else None
                else:
                    sec_thermostat_parameters.effective_mass = thermostat_mass  # TODO: generalize this for different thermostats (assuming here that the mass units will be printed to the outfile in case thermostat_mass is not defined)

                # fill in old workflow section for GUI features until it is deprecated
                sec_workflow.type = 'molecular_dynamics'
                sec_md = sec_workflow.m_create(MolecularDynamicsOld)
                sec_md.thermodynamic_ensemble = workflow.method.thermodynamic_ensemble
                sec_integration_parameters1 = sec_md.m_create(IntegrationParametersOld)
                sec_integration_parameters1.n_steps = workflow.method.n_steps
                sec_integration_parameters1.integration_timestep = workflow.method.integration_timestep
                sec_thermostat_parameters1 = sec_integration_parameters1.m_create(ThermostatParametersOld)
                sec_thermostat_parameters1.thermostat_type = sec_thermostat_parameters.thermostat_type
                sec_thermostat_parameters1.reference_temperature = sec_thermostat_parameters.reference_temperature
                sec_thermostat_parameters1.coupling_constant = sec_thermostat_parameters.coupling_constant
                sec_thermostat_parameters1.effective_mass = sec_thermostat_parameters.effective_mass

        self.archive.workflow2 = workflow

    def parse_method(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        # extract the k-grid
        sec_kmesh = sec_method.m_create(KMesh)
        sec_kmesh.grid = self.out_parser.get('k_grid')
        sec_kmesh.offset = self.out_parser.get('k_offset')

        sec_method.basis_set.append(BasisSet(type='numeric AOs'))
        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)
        sec_electronic.method = 'DFT'

        # control parameters from out file
        self.control_parser.mainfile = self.filepath
        # we use species as marker that control parameters are printed in out file
        species = self.control_parser.get('species')
        # if not in outfile read it from control.in
        if species is None:
            control_file = self.get_fhiaims_file('control.in')
            if not control_file:
                control_file = [os.path.join(self.out_parser.maindir, 'control.in')]
            self.control_parser.mainfile = control_file[0]

        def parse_basis_set(species):
            sec_basis_set = sec_method.m_create(x_fhi_aims_section_controlIn_basis_set)
            basis_funcs = ['gaussian', 'hydro', 'valence', 'ion_occ', 'ionic', 'confined']
            for key, val in species.items():
                if key == 'species':
                    sec_basis_set.x_fhi_aims_controlIn_species_name = val[0]
                elif key == 'angular_grids':
                    sec_basis_set.x_fhi_aims_controlIn_angular_grids_method = val[0]
                elif key == 'division':
                    pass
                elif key in basis_funcs:
                    for i in range(len(val)):
                        sec_basis_func = sec_basis_set.m_create(
                            x_fhi_aims_section_controlIn_basis_func)
                        sec_basis_func.x_fhi_aims_controlIn_basis_func_type = key
                        sec_basis_func.x_fhi_aims_controlIn_basis_func_n = int(val[i][0])
                        sec_basis_func.x_fhi_aims_controlIn_basis_func_l = str(val[i][1])
                        if len(val[i]) == 3 and hasattr(val[i][2], 'real'):
                            sec_basis_func.x_fhi_aims_controlIn_basis_func_radius = val[i][2]
                elif key in ['cut_pot', 'radial_base']:
                    setattr(sec_basis_set, 'x_fhi_aims_controlIn_%s' % key, np.array(
                        val[0], dtype=float))
                else:
                    try:
                        setattr(sec_basis_set, 'x_fhi_aims_controlIn_%s' % key, val[0])
                    except Exception:
                        self.logger.warning('Error setting controlIn metainfo.', details={key: key})

            # is the number of basis functions equal to number of divisions?
            division = species.get('division', None)
            if division is not None:
                sec_basis_set.x_fhi_aims_controlIn_number_of_basis_func = len(division)
                sec_basis_set.x_fhi_aims_controlIn_division = division

        for key, val in self.control_parser.items():
            if val is None:
                # TODO consider also none entries? or (isinstance(val, str) and val == 'none'):
                continue
            if key.startswith('x_fhi_aims_controlIn'):
                try:
                    if key == 'x_fhi_aims_controlIn_hse_unit':
                        val = str(val)
                    setattr(sec_method, key, val)
                except Exception:
                    self.logger.warning('Error setting controlIn metainfo.', data=dict(key=key))
            elif key == 'occupation_type':
                sec_method.x_fhi_aims_controlIn_occupation_type = val[0]
                sec_method.x_fhi_aims_controlIn_occupation_width = val[1]
                if len(val) > 2:
                    sec_method.x_fhi_aims_controlIn_occupation_order = int(val[2])
            elif key == 'relativistic':
                if isinstance(val, str):
                    val = [val]
                sec_method.x_fhi_aims_controlIn_relativistic = ' '.join(val[:2])
                if len(val) > 2:
                    sec_method.x_fhi_aims_controlIn_relativistic_threshold = val[2]
            elif key == 'species':
                for species in val:
                    parse_basis_set(species)
            elif key == 'xc':
                if isinstance(val, str):
                    val = [val]
                xc = ' '.join([v for v in val if isinstance(v, str)])
                sec_method.x_fhi_aims_controlIn_xc = str(xc)
                if not isinstance(val[-1], str) and xc.lower().startswith('hse'):
                    unit = self.control_parser.get('x_fhi_aims_controlIn_hse_unit')
                    hse_omega = val[-1] * unit if unit else val[-1]
                    sec_method.x_fhi_aims_controlIn_hse_omega = hse_omega
                hybrid_coeff = self.control_parser.get('x_fhi_aims_controlIn_hybrid_xc_coeff')
                if hybrid_coeff is not None:
                    # is it necessary to check if xc is a hybrid type aside from hybrid_coeff
                    sec_method.x_fhi_aims_controlIn_hybrid_xc_coeff = hybrid_coeff

        inout_exclude = [
            'x_fhi_aims_controlInOut_relativistic', 'x_fhi_aims_controlInOut_xc',
            'x_fhi_aims_controlInOut_hse_unit', 'x_fhi_aims_controlInOut_hybrid_xc_coeff']
        # add controlInOut parameters
        for key in self.out_parser.keys():
            if key.startswith('x_fhi_aims_controlInOut'):
                if key not in inout_exclude:
                    try:
                        setattr(sec_method, key, self.out_parser.get(key))
                    except Exception:
                        self.logger.warning('Error setting controlInOut metainfo.', details={key: key})

        nspin = self.out_parser.get_number_of_spin_channels()
        sec_method.x_fhi_aims_controlInOut_number_of_spin_channels = nspin
        sec_electronic.n_spin_channels = nspin

        # convert relativistic
        relativistic = self.out_parser.get('x_fhi_aims_controlInOut_relativistic')
        if relativistic is not None:
            if not isinstance(relativistic, str):
                relativistic = ' '.join(relativistic)
            sec_method.x_fhi_aims_controlInOut_relativistic = relativistic
            relativistic = self._relativity_map.get(relativistic, None)
            if relativistic is not None:
                sec_electronic.relativity_method = relativistic

        # atom species
        self.parse_topology()

        # xc functional from output
        self.parse_xc_functional(sec_method, sec_dft)

    def parse_xc_functional(self, section, subsection):
        xc_inout = self.out_parser.get('x_fhi_aims_controlInOut_xc', None)
        if xc_inout is not None:
            xc_inout = [xc_inout] if isinstance(xc_inout, str) else xc_inout
            xc = ' '.join([v for v in xc_inout if isinstance(v, str)])
            section.x_fhi_aims_controlInOut_xc = str(xc)

            # hse func
            hse_omega = None
            if not isinstance(xc_inout[-1], str) and xc.lower().startswith('hse'):
                unit = self.out_parser.get('x_fhi_aims_controlInOut_hse_unit')
                hse_omega = xc_inout[-1] * unit if unit else xc_inout[-1]
                section.x_fhi_aims_controlInOut_hse_omega = hse_omega

            hybrid_coeff = self.out_parser.get('x_fhi_aims_controlInOut_hybrid_xc_coeff')
            if hybrid_coeff is not None:
                section.x_fhi_aims_controlIn_hybrid_xc_coeff = hybrid_coeff

            # convert parsed xc to meta info
            xc_meta_list = self._xc_map.get(xc, [])
            sec_xc_functional = subsection.m_create(XCFunctional)
            for xc_meta in xc_meta_list:
                name = xc_meta.get('name')
                functional = Functional(name=name)
                weight = xc_meta.get('weight', None)
                if weight is not None and hybrid_coeff is not None:
                    functional.weight = weight(float(hybrid_coeff))
                xc_parameters = dict()
                if hse_omega is not None:
                    hybrid_coeff = 0.25 if hybrid_coeff is None else hybrid_coeff
                    xc_parameters.setdefault('$\\omega$ in m^-1', hse_omega.to('1/m').magnitude)
                if hybrid_coeff is not None:
                    xc_parameters.setdefault('exact_exchange_mixing_factor', hybrid_coeff)
                    sec_xc_functional.normalize_hybrid()
                if xc_parameters:
                    functional.parameters = xc_parameters
                if '_X_' in name or name.endswith('_X'):
                    sec_xc_functional.exchange.append(functional)
                elif '_C_' in name or name.endswith('_C'):
                    sec_xc_functional.correlation.append(functional)
                elif 'HYB' in name:
                    sec_xc_functional.hybrid.append(functional)
                else:
                    sec_xc_functional.contributions.append(functional)

    def parse_topology(self):
        sec_method = self.archive.run[-1].method[-1]

        def parse_atom_type(species):
            sec_atom_type = sec_method.m_create(AtomParameters)
            sec_atom_species = sec_atom_type.m_create(
                x_fhi_aims_section_controlInOut_atom_species)
            for key, val in species.items():
                if key == 'nuclear charge':
                    charge = val[0] * ureg.elementary_charge
                    sec_atom_type.charge = charge
                    sec_atom_species.x_fhi_aims_controlInOut_species_charge = charge
                elif key == 'atomic mass':
                    mass = val[0][0] * ureg.amu
                    sec_atom_type.mass = mass
                    sec_atom_species.x_fhi_aims_controlInOut_species_mass = mass
                elif key == 'species':
                    sec_atom_type.label = val
                    sec_atom_species.x_fhi_aims_controlInOut_species_name = val
                elif 'request to include pure gaussian fns' in key:
                    sec_atom_species.x_fhi_aims_controlInOut_pure_gaussian = val[0]
                elif 'cutoff potl' in key:
                    sec_atom_species.x_fhi_aims_controlInOut_species_cut_pot = val[0][0] * ureg.angstrom
                    sec_atom_species.x_fhi_aims_controlInOut_species_cut_pot_width = val[0][1] * ureg.angstrom
                    sec_atom_species.x_fhi_aims_controlInOut_species_cut_pot_scale = val[0][2]
                elif "request for '+U'" in key:
                    sec_hubbard = sec_atom_type.m_create(HubbardKanamoriModel)
                    sec_hubbard.orbital = f'{val[0][0]}{val[0][1]}'
                    sec_hubbard.u_effective = val[0][-2] * ureg.eV
                    sec_hubbard.double_counting_correction = 'Dudarev'
                    sec_hubbard.x_fhi_aims_projection_type = 'Mulliken (dual)'
                    sec_hubbard.x_fhi_aims_petukhov_mixing_factor = self.out_parser.get('petukhov')
                elif 'free-atom' in key or 'free-ion' in key:
                    for i in range(len(val)):
                        sec_basis_func = sec_atom_species.m_create(
                            x_fhi_aims_section_controlInOut_basis_func)
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_type = ' '.join(key.split()[:-1])
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_n = val[i][0]
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_l = val[i][1]
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_occ = val[i][2]
                elif 'hydrogenic' in key:
                    for i in range(len(val)):
                        sec_basis_func = sec_atom_species.m_create(
                            x_fhi_aims_section_controlInOut_basis_func)
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_type = ' '.join(key.split()[:-1])
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_n = val[i][0]
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_l = val[i][1]
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_eff_charge = val[i][2]
                elif 'ionic' in key:
                    for i in range(len(val)):
                        sec_basis_func = sec_atom_species.m_create(
                            x_fhi_aims_section_controlInOut_basis_func)
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_type = 'ionic basis'
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_n = val[i][0]
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_l = val[i][1]
                elif 'basis function' in key:
                    for i in range(len(val)):
                        sec_basis_func = sec_atom_species.m_create(
                            x_fhi_aims_section_controlInOut_basis_func)
                        sec_basis_func.x_fhi_aims_controlInOut_basis_func_type = key.split(
                            'basis')[0].strip()
                        if val[i][0] == 'L':
                            sec_basis_func.x_fhi_aims_controlInOut_basis_func_gauss_l = val[i][2]
                            sec_basis_func.x_fhi_aims_controlInOut_basis_func_gauss_N = val[i][3]
                            alpha = [val[i][j + 2] for j in range(len(val[i])) if val[i][j] == 'alpha']
                            weight = [val[i][j + 2] for j in range(len(val[i])) if val[i][j] == 'weight']
                            alpha = np.array(alpha) * (1 / ureg.angstrom ** 2)
                            sec_basis_func.x_fhi_aims_controlInOut_basis_func_gauss_alpha = alpha
                            sec_basis_func.x_fhi_aims_controlInOut_basis_func_gauss_weight = weight
                        elif len(val[i]) == 2:
                            sec_basis_func.x_fhi_aims_controlInOut_basis_func_gauss_l = val[i][0]
                            alpha = np.array(val[i][1]) / ureg.angstrom ** 2
                            sec_basis_func.x_fhi_aims_controlInOut_basis_func_primitive_gauss_alpha = alpha

        # add inout parameters read from main output
        # species
        species = self.out_parser.get('control_inout', {}).get('species')
        if species is not None:
            for specie in species:
                parse_atom_type(specie)

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger
        self.control_parser.logger = self.logger
        self.dos_parser.logger = self.logger
        self.bandstructure_parser.logger = self.logger
        self._frame_rate = None

    def reuse_parser(self, parser):
        self.out_parser.quantities = parser.out_parser.quantities
        self.control_parser.quantities = parser.control_parser.quantities

    def get_mainfile_keys(self, filepath):
        self.out_parser.mainfile = filepath
        if self.out_parser.get('gw_flag', None) in self._gw_flag_map.keys():
            return ['GW', 'GW_workflow']
        return True

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.logger = logger if logger is not None else logging

        self.init_parser()

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(
            name='FHI-aims', version=self.out_parser.get('version', ''),
            compilation_host=self.out_parser.get('compilation_host', ''))
        sec_run.time_run = TimeRun(
            cpu1_start=self.out_parser.get('cpu1_start', 0),
            wall_start=self.out_parser.get('wall_start', 0))

        section_run_keys = [
            'x_fhi_aims_program_compilation_date', 'x_fhi_aims_program_compilation_time',
            'x_fhi_aims_program_execution_date', 'x_fhi_aims_program_execution_time',
            'raw_id', 'x_fhi_aims_number_of_tasks']
        for key in section_run_keys:
            value = self.out_parser.get(key)
            if value is None:
                continue
            try:
                setattr(sec_run, key, value)
            except Exception:
                self.logger.warning('Error setting run metainfo', details={key: key})

        sec_parallel_tasks = sec_run.m_create(x_fhi_aims_section_parallel_tasks)
        # why embed section not just let task be an array

        task_nrs = self.out_parser.get('x_fhi_aims_parallel_task_nr', [])
        task_hosts = self.out_parser.get('x_fhi_aims_parallel_task_host', [])
        for i in range(len(task_nrs)):
            sec_parallel_task_assignement = sec_parallel_tasks.m_create(
                x_fhi_aims_section_parallel_task_assignement)
            sec_parallel_task_assignement.x_fhi_aims_parallel_task_nr = task_nrs[i]
            sec_parallel_task_assignement.x_fhi_aims_parallel_task_host = task_hosts[i]

        if self._calculation_type == 'gw':
            self.parse_gw()
        else:
            self.parse_method()
            self.parse_configurations()

        self.parse_workflow()

        gw_archive = self._child_archives.get('GW')
        if gw_archive is not None and self.out_parser.get('gw_flag', None) in self._gw_flag_map.keys():
            # GW single point
            p = FHIAimsParser()
            p._calculation_type = 'gw'
            p.parse(filepath, gw_archive, logger)

            # GW workflow
            gw_workflow_archive = self._child_archives.get('GW_workflow')
            try:
                self.parse_gw_workflow(gw_archive, gw_workflow_archive)
            except Exception:
                self.logger.error('Error parsing the automatic GW workflow')
