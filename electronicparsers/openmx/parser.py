#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
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

from copy import deepcopy
from functools import cached_property
import logging
from typing import Optional
import numpy as np
from datetime import datetime
import re
import io
from os import path, listdir

from nomad.datamodel import EntryArchive
from nomad.units import ureg as units
from runschema.run import Run, Program, TimeRun
from runschema.calculation import (
    Calculation,
    ScfIteration,
    Energy,
    EnergyEntry,
    BandEnergies,
    Forces,
    ForcesEntry,
    Stress,
    StressEntry,
)
from runschema.system import AtomsGroup, System, Atoms
from runschema.method import (
    AtomParameters,
    Method,
    BasisSet,
    DFT,
    Pseudopotential,
    XCFunctional,
    Functional,
    Electronic,
    Smearing,
    Scf,
    BasisSetContainer,
    CoreHole,
)
from nomad.parsing.file_parser import TextParser, Quantity
from simulationworkflowschema import (
    GeometryOptimization,
    GeometryOptimizationMethod,
    MolecularDynamics,
    MolecularDynamicsMethod,
)
from simulationworkflowschema.molecular_dynamics import ThermostatParameters
from nomad.quantum_states import RussellSaundersState


"""
This is parser for OpenMX DFT code.
"""

# A = (1 * units.angstrom).to_base_units().magnitude


def find_stdout(mainfile):
    mainfile_dir = path.dirname(mainfile)
    for file in listdir(mainfile_dir):
        stdout_path = path.join(mainfile_dir, file)
        if path.isfile(stdout_path):
            with open(stdout_path) as input_file:
                for index, line in enumerate(input_file):
                    if r'Welcome to OpenMX' in line:
                        return stdout_path
                    if index == 500:
                        break
    return None


def _j_mapping() -> dict[tuple[int, int], tuple[float, float]]:
    """Reproduce table 12 given in https://www.openmx-square.org/openmx_man3.9/node192.html"""
    mapping: dict[tuple[int, int], tuple[float, float]] = {}
    for ll in range(4):
        second_index = 1
        for jj in RussellSaundersState.generate_Js(
            abs(ll + 0.5), abs(ll - 0.5), rising=False
        ):
            for mj in RussellSaundersState.generate_MJs(jj, rising=False):
                mapping[(ll, second_index)] = (jj, mj)
                second_index += 1
    return mapping


element = '[A-Z][a-z]?'
xc_functional_dictionary = {
    'GGA-PBE': ['GGA_C_PBE', 'GGA_X_PBE'],
    'LDA': ['LDA_X', 'LDA_C_PZ'],
    'LSDA-CA': ['LDA_X', 'LDA_C_PZ'],
    'LSDA-PW': ['LDA_X', 'LDA_C_PW'],
    None: ['LDA_X', 'LDA_C_PZ'],
}
xc_functional_dictionary['PBE'] = xc_functional_dictionary['GGA-PBE']
xc_functional_dictionary['CA'] = xc_functional_dictionary['LSDA-CA']

scf_step_parser = TextParser(
    quantities=[
        Quantity('NormRD', r'NormRD=\s*([\d\.]+)', repeats=False),
        Quantity('Uele', r'Uele=\s*([-\d\.]+)', repeats=False),
    ]
)

md_step_parser = TextParser(
    quantities=[
        Quantity(
            'SCF',
            r'   (SCF=.+?Uele=\s*[-\d\.]+)',
            sub_parser=scf_step_parser,
            repeats=True,
        ),
        Quantity('Utot', r'Utot\.\s+(-?\d+\.\d+)', repeats=False),
    ]
)

species_and_coordinates_parser = TextParser(
    quantities=[
        Quantity(
            'atom',
            rf'\s*\d+\s*({element}\d*)\s*([-\d\.]+)\s+([-\d\.]+)\s+([-\d\.]+)\s+[\d\.]+\s*[\d\.]+\s*',
            repeats=True,
        )
    ]
)

species_definition_parser = TextParser(
    quantities=[
        Quantity('species', rf'({element}\d*)\s+([-\w\.]+)\s+(\w+)', repeats=True),
    ]
)

core_hole_parser = TextParser(
    quantities=[
        Quantity(
            'core_hole', rf'(\d+)\s+({element})\s+(\d+)', repeats=False
        ),  # TODO: consider `repeats = True` case
    ]
)


def convert_eigenvalues(string):
    values = np.loadtxt(
        io.StringIO(string), dtype=np.float64, usecols=(1, 2)
    ).transpose()
    return values


eigenvalues_parser = TextParser(
    quantities=[
        Quantity(
            'kpoints',
            r'k1=\s*([-\.\d]+)\s+k2=\s*([-\.\d]+)\s+k3=\s*([-\.\d]+)',
            repeats=True,
        ),
        Quantity(
            'eigenvalues',
            r'((?:\d+\s+[-\.\d]+\s+[-\.\d]+\s+)+)',
            str_operation=convert_eigenvalues,
            repeats=True,
        ),
    ]
)

mainfile_parser = TextParser(
    quantities=[
        Quantity(
            'date_start',
            r'\s+([A-Z]{1}[a-z]{2}\s[A-Z]{1}[a-z]{2}\s\d{1,2}\s\d{2}:\d{2}:\d{2}\s\d{4})',
            repeats=False,
            flatten=False,
            dtype=str,
        ),
        Quantity(
            'elapsed_time',
            r'\s+Elapsed.Time.\s+([\d.]+)',
            repeats=False,
        ),
        Quantity(
            'program_version',
            r'This calculation was performed by OpenMX Ver. ([\d\.]+)\s*',
            repeats=False,
        ),
        Quantity(
            'md_step',
            r'(SCF history at MD[\s\S]+?Chemical potential \(Hartree\)\s+[-\d\.]+)',
            sub_parser=md_step_parser,
            repeats=True,
        ),
        Quantity(
            'atoms',
            r'<Atoms.SpeciesAndCoordinates([\s\S]+)Atoms.SpeciesAndCoordinates>',
            sub_parser=species_and_coordinates_parser,
            repeats=False,
        ),
        Quantity(
            'species',
            r'<Definition\.of\.Atomic\.Species([\s\S]+)Definition\.of\.Atomic\.Species>',
            sub_parser=species_definition_parser,
        ),
        Quantity(
            'core_hole',
            r'<Definition\.of\.Core\.Hole([\s\S]+)Definition\.of\.Core\.Hole>',
            sub_parser=core_hole_parser,
        ),
        Quantity(
            'input_lattice_vectors',
            r'(?i:<Atoms.UnitVectors\s+((?:-?\d+\.\d+\s+)+)Atoms.UnitVectors>)',
            repeats=False,
        ),
        Quantity('scf.XcType', r'scf.XcType\s+(\S+)', repeats=False),
        Quantity(
            'scf.SpinPolarization', r'scf.SpinPolarization\s+(\S+)', repeats=False
        ),
        Quantity('scf.stress.tensor', r'scf.stress.tensor\s+(.*)', repeats=False),
        Quantity(
            'Atoms.SpeciesAndCoordinates.Unit',
            r'(?i:Atoms.SpeciesAndCoordinates.Unit\s+([a-z]{2,4}))',
            repeats=False,
        ),
        Quantity(
            'Atoms.UnitVectors.Unit',
            r'(?i:Atoms.UnitVectors.Unit\s+([a-z]{2,3}))',
            repeats=False,
        ),
        Quantity('scf.Hubbard.U', r'(?i:scf.Hubbard.U\s+(on|off))', repeats=False),
        Quantity('MD.maxIter', r'MD\.maxIter\s+(\d+)', repeats=False),
        Quantity('MD.Type', r'(?i:MD\.Type\s+([a-z_\d]{3,6}))', repeats=False),
        Quantity('MD.TimeStep', r'MD\.TimeStep\s+([\d\.e-]+)', repeats=False),
        Quantity(
            'MD.Opt.criterion', r'(?i:MD\.Opt\.criterion\s+([\d\.e-]+))', repeats=False
        ),
        Quantity(
            'MD.TempControl', r'<MD.TempControl([\s\S]+)MD.TempControl>', repeats=False
        ),
        Quantity('scf.maxIter', r'scf.maxIter\s+(\d+)', repeats=False),
        Quantity('scf.criterion', r'scf.criterion\s+([-\.eE\d]+)', repeats=False),
        Quantity(
            'scf.ElectronicTemperature',
            r'scf.ElectronicTemperature\s+(\S+)',
            repeats=False,
        ),
        Quantity('scf.dftD', r'scf.dftD\s+([a-z]+)', repeats=False),
        Quantity('version.dftD', r'version.dftD\s+([23])', repeats=False),
        Quantity(
            'have_timing',
            r'Computational Time \(second\)([\s\S]+)Others.+',
            repeats=False,
        ),
        Quantity(
            'eigenvalues',
            r'Eigenvalues \(Hartree\) \S+ SCF KS-eq\.\s+\*{59}\s*\*{59}([^*]+)',
            sub_parser=eigenvalues_parser,
            repeats=False,
        ),
        Quantity(
            'elapsed.time',
            r'Total Computational Time.*[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+([0-9.]+)',
        ),
    ]
)

stdout_parser = TextParser(
    quantities=[
        Quantity(
            'scf.stress.tensor',
            r'Stress tensor \(Hartree/bohr\^3\)\s+\*{55}([^*]+)',
            repeats=True,
        ),
        Quantity(
            'Uele',
            r'\*{19} MD=\s*\d+\s+SCF=\s*1\s+\*{19}(?:.|\n)*?Uele\s+=\s+(-?\d+\.\d+)',
            repeats=True,
        ),
        Quantity(
            'elapsed.time',
            r'Total Computational Time.*[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+([0-9.]+)',
        ),
    ]
)


def read_md_file(md_file):
    result = []
    with open(md_file, 'r') as f:
        cell_vectors_re = re.compile(r'Cell_Vectors=((?:\s+-?\d+\.\d+)+)')
        temperature_re = re.compile(r'Temperature=\s+(\d+\.\d+)')
        time_re = re.compile(r'time=\s+(\d+\.\d+)')
        for line in f:
            line_list = line.split()
            if len(line_list) == 1:
                step_header = True
                natoms = int(line_list[0])
                result.append(
                    {
                        'species': [],
                        'positions': np.empty((natoms, 3), dtype=np.float64),
                        'velocities': np.empty((natoms, 3), dtype=np.float64),
                        'forces': np.empty((natoms, 3), dtype=np.float64),
                    }
                )
                atomindex = 0
            elif step_header:
                cell_vectors = cell_vectors_re.search(line)
                if cell_vectors is not None:
                    cell_vectors = [float(v) for v in cell_vectors.group(1).split()]
                    result[-1]['cell_vectors'] = np.array(cell_vectors).reshape(3, 3)
                temperature = temperature_re.search(line)
                if temperature is not None:
                    temperature = temperature.group(1)
                    result[-1]['temperature'] = temperature
                time = time_re.search(line)
                if time is not None:
                    result[-1]['time'] = float(time.group(1))
                step_header = False
            else:
                result[-1]['positions'][atomindex][0:3] = [
                    float(val) for val in line_list[1:4]
                ]
                result[-1]['forces'][atomindex][0:3] = [
                    float(val) for val in line_list[4:7]
                ]
                result[-1]['velocities'][atomindex][0:3] = [
                    float(val) for val in line_list[7:10]
                ]
                result[-1]['species'].append(line_list[0])
                atomindex += 1
    f.close()
    return result


def parse_md_file(i, mdfile_md_steps, system):
    system.atoms = Atoms(
        lattice_vectors=mdfile_md_steps[i].get('cell_vectors') * units.angstrom,
        periodic=[True, True, True],
        positions=mdfile_md_steps[i].get('positions') * units.angstrom,
        labels=mdfile_md_steps[i].get('species'),
        velocities=mdfile_md_steps[i].get('velocities') * units.meter / units.second,
    )


def parse_structure(system, logger: logging.Logger):
    atoms_units = mainfile_parser.get('Atoms.SpeciesAndCoordinates.Unit')
    lattice_vectors = mainfile_parser.get('input_lattice_vectors')
    lattice_units = mainfile_parser.get('Atoms.UnitVectors.Unit')
    atoms = mainfile_parser.get('atoms').get('atom')

    if atoms is not None and lattice_vectors is not None:
        lattice_vectors = np.array(lattice_vectors).reshape(3, 3)
        if atoms_units is not None:
            if lattice_units.lower() == 'au':
                lattice_vectors = lattice_vectors * units.bohr
                lattice_units = units.bohr
            elif lattice_units.lower() == 'ang':
                lattice_vectors = lattice_vectors * units.angstrom
                lattice_units = units.angstrom
        else:
            lattice_vectors = lattice_vectors * units.angstrom
        atom_positions = [a[1:4] for a in atoms]
        if atoms_units is not None:
            if atoms_units.lower() == 'au':
                atom_positions = atom_positions * units.bohr
            if atoms_units.lower() == 'ang':
                atom_positions = atom_positions * units.angstrom
            elif atoms_units.lower() == 'frac':
                # There are some problems with pint here so simple matrix vector multiplications
                # doesn't work.
                atom_positions = (
                    np.array(
                        [np.array(pos).dot(lattice_vectors.magnitude) for pos in atom_positions]
                    )
                    * lattice_units
                )
        else:
            # default unit is angstrom
            atom_positions = atom_positions * units.angstrom
        system.atoms = Atoms(
            positions=atom_positions,
            lattice_vectors=lattice_vectors,
            periodic=[True, True, True],
            labels=[a[0] for a in atoms],
        )
    else:
        logger.warning('Failed to parse the input structure.')


def parse_temperature_profile(data, thermo_type):
    steps = data[0]
    thermostats = []

    for i in range(steps):
        if i == 0 and int(data[1]) == 1:
            continue

        thermostat = ThermostatParameters()
        if 'VS' in thermo_type:
            thermostat.thermostat_type = 'velocity_rescaling_woodcock'
            cols = 4
        if 'NH' in thermo_type:
            thermostat.thermostat_type = 'nose_hoover'
            cols = 2

        if i == 0:
            thermostat.reference_temperature_start = data[i * cols + 2] * units.K
            thermostat.temperature_update_frame_start = 1
        else:
            thermostat.reference_temperature_start = data[(i - 1) * cols + 2] * units.K
            thermostat.temperature_update_frame_start = data[(i - 1) * cols + 1]
        thermostat.reference_temperature_end = data[i * cols + 2] * units.K
        thermostat.temperature_update_frame_end = data[i * cols + 1]

        if (
            thermostat.reference_temperature_start
            == thermostat.reference_temperature_end
        ):
            thermostat.temperature_profile = 'constant'
        else:
            thermostat.temperature_profile = 'linear'

        thermostats.append(thermostat)
    return thermostats


class OpenmxParser:
    def __init__(self):
        pass

    @cached_property
    def atom_index_dict(self) -> dict[str, list[int]]:
        """Return the indexes by species label.
        - column_index: the column index of the species labels (default = 0)"""
        result: dict[str, list[int]] = {}
        for index, item in enumerate(mainfile_parser.results['atoms'].results['atom']):
            key, value = item[0], index
            if key in result:
                result[key].append(value)
            else:
                result[key] = [value]
        return result

    def parse_species(
        self, definitions: list[str]
    ) -> tuple[Pseudopotential, Optional[CoreHole]]:
        """
        Extract `Pseudopotential` and `CoreHole` (if present) from the atomic species definition.
        An explanation of the format can be found at https://www.openmx-square.org/openmx_man3.9/node32.html
        For an overview of all conventional potentials and partial atomic orbitals, see https://www.openmx-square.org/vps_pao2019/
        and https://www.openmx-square.org/vps_pao_core2019/ for core-holes.
        """
        l_quantum = '[spdf]'
        remove_extension = lambda x: re.sub(r'(\.pao|\.vps)', '', x)
        extract_method = lambda x: re.search(r'_([A-Z]+)19', x)
        #  extract_orbital = lambda x: re.search(rf'_(\d)({l_quantum})$', x)
        extract_core_hole = lambda x: re.search(rf'_(\d)({l_quantum})_CH', x)
        extract_elem_cutoff = lambda x: re.match(rf'({element})([\d\.]+)[_-]', x)
        extract_lmax = lambda x: re.search(rf'({l_quantum})\d$', x)

        definitions = deepcopy(definitions)
        try:
            definitions[1] = remove_extension(definitions[1])
            definitions[2] = remove_extension(definitions[2])
        except IndexError:
            self.logger.error(f'Species definition must be of length 3: {definitions}')
            return None, None

        # evaluate pseudopotential
        pseudopotential, core_hole = (
            Pseudopotential(type='US MBK', norm_conserving=True),
            None,
        )  # TODO: add basis set
        pseudopotential.name = f'{definitions[1]} {definitions[2]}'
        pseudopotential.cutoff = (
            float(extract_elem_cutoff(definitions[1]).group(2)) * units.hartree
        )
        try:
            pseudopotential.l_max = CoreHole.l_quantum_numbers[
                extract_lmax(definitions[1]).group(1)
            ]
        except KeyError:
            self.logger.error(f'Unknown l-quantum symbol: {definitions[1]}')
        try:
            pseudopotential.xc_functional_name = xc_functional_dictionary[
                extract_method(definitions[2]).group(1)
            ]
        except KeyError:
            self.logger.error(
                f'Unknown exchange-correlation functional: {definitions[2]}'
            )

        # evaluate core_hole
        quantum_nums_flag = extract_core_hole(
            definitions[1]
        )  # this checks the PAO, the PP is only necessary for the final state
        if quantum_nums_flag:
            quantum_nums = quantum_nums_flag.groups()
            try:
                core_hole = CoreHole(
                    n_quantum_number=int(quantum_nums[0]),
                    l_quantum_number=CoreHole.l_quantum_numbers[quantum_nums[1]],
                    n_electrons_excited=1,
                )
            except KeyError:
                self.logger.error(f'Unknown l-quantum symbol: {quantum_nums[1]}')
                return pseudopotential, None

            core_hole_flags = mainfile_parser.results.get('core_hole')
            if core_hole_flags:
                core_hole.dscf_state = 'final'
                spinpol = mainfile_parser.get('scf.SpinPolarization', '').lower()
                if spinpol == 'on':
                    # first all up, then all down: https://www.openmx-square.org/openmx_man3.9/node192.html
                    core_hole.ms_quantum_bool = not bool(
                        int(
                            core_hole_flags.results['core_hole'][2]
                            / core_hole.get_l_degeneracy()
                        )
                    )
                elif spinpol == 'nc':
                    (
                        core_hole.j_quantum_number,
                        core_hole.mj_quantum_number,
                    ) = _j_mapping()[
                        core_hole.l_quantum_number,
                        core_hole_flags.results['core_hole'][3],
                    ]
                elif spinpol == 'off':
                    self.logger.warning(
                        """
                    Unexpected spin-restricted setting when using final-state core-hole computation.
                    This is not recommended by the manual. For now assuming single-electron excitation of unspecified spin.
                    """
                    )
                else:
                    self.logger.warning('Spin-state not yet recognized')
            else:
                core_hole.dscf_state = 'initial'  # this will be a hook in $\Delta$-SCF

        return pseudopotential, core_hole

    def parse_workflow(self):
        md_type = mainfile_parser.get('MD.Type')
        md_types_list = [
            # FIXME: handle the various OptCx methods with constraints
            ['OPT', 'geometry_optimization', 'steepest_descent'],
            ['DIIS', 'geometry_optimization', 'diis'],
            ['BFGS', 'geometry_optimization', 'bfgs'],
            # FIXME: not in https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-meta-info/-/wikis/metainfo/geometry-optimization-method
            ['RF', 'geometry_optimization', 'rf'],
            # FIXME: not in https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-meta-info/-/wikis/metainfo/geometry-optimization-method
            ['EF', 'geometry_optimization', 'ef'],
            ['NVE', 'molecular_dynamics', 'NVE'],
            ['NVT_VS', 'molecular_dynamics', 'NVT'],
            ['NVT_NH', 'molecular_dynamics', 'NVT'],
        ]
        if md_type is not None and 'nomd' not in md_type.lower():
            md_type = md_type.upper()
            workflow = None
            for current_md_type in md_types_list:
                if current_md_type[0] in md_type:
                    max_iters = mainfile_parser.get('MD.maxIter')
                    if current_md_type[1] == 'geometry_optimization':
                        workflow = GeometryOptimization(
                            method=GeometryOptimizationMethod()
                        )
                        workflow.method.method = current_md_type[2]
                        if max_iters is not None:
                            workflow.method.optimization_steps_maximum = max_iters
                        criterion = mainfile_parser.get('MD.Opt.criterion')
                        if criterion is not None:
                            workflow.method.convergence_tolerance_force_maximum = (
                                criterion * units.hartree / units.bohr
                            )
                        else:
                            workflow.method.convergence_tolerance_force_maximum = (
                                1e-4 * units.hartree / units.bohr
                            )
                    else:
                        md_temp_control = mainfile_parser.get('MD.TempControl')
                        if 'VS' in md_type:
                            thermostats = parse_temperature_profile(
                                md_temp_control, 'VS'
                            )
                        elif 'NH' in md_type:
                            thermostats = parse_temperature_profile(
                                md_temp_control, 'NH'
                            )

                        workflow = MolecularDynamics(
                            method=MolecularDynamicsMethod(
                                thermostat_parameters=thermostats
                            )
                        )
                        workflow.method.thermodynamic_ensemble = current_md_type[2]
                        # Everything is saved every time step
                        workflow.method.coordinate_save_frequency = 1
                        workflow.method.velocity_save_frequency = 1
                        workflow.method.force_save_frequency = 1
                        workflow.method.thermodynamics_save_frequency = 1

                        md_timestep = mainfile_parser.get('MD.TimeStep')
                        if md_timestep is not None:
                            workflow.method.integration_timestep = (
                                md_timestep * units.fs
                            )

                        if max_iters is not None:
                            workflow.method.n_steps = max_iters

            self.archive.workflow2 = workflow

    def parse_method(self):
        # setup
        sec_method = Method()
        self.archive.run[-1].method.append(sec_method)
        sec_method.atom_parameters = []

        for species in mainfile_parser.results['species'].results['species']:
            # add atom parameters
            atom_parameters = AtomParameters(label=species[0])
            (
                atom_parameters.pseudopotential,
                atom_parameters.core_hole,
            ) = self.parse_species(species)
            sec_method.atom_parameters.append(atom_parameters)

        # add basis set
        sec_method.electrons_representation = [
            BasisSetContainer(
                type='atom-centered orbitals',
                scope=['wavefunction'],
                basis_set=[
                    BasisSet(
                        type='numeric AOs',
                        scope=['full-electron'],  # TODO: double check
                    )
                ],
            )
        ]

        # DFT (+U)
        sec_dft = DFT()
        sec_electronic = Electronic()
        sec_method.dft = sec_dft
        sec_method.electronic = sec_electronic
        sec_electronic.method = 'DFT'
        # FIXME: add some testcase for DFT+U
        scf_hubbard_u = mainfile_parser.get('scf.Hubbard.U')
        if scf_hubbard_u is not None:
            if scf_hubbard_u.lower() == 'on':
                sec_electronic.method = 'DFT+U'

        scf_xctype = mainfile_parser.get('scf.XcType')
        sec_xc_functional = XCFunctional()
        sec_dft.xc_functional = sec_xc_functional
        for xc in xc_functional_dictionary[scf_xctype]:
            if '_X_' in xc or xc.endswith('_X'):
                sec_xc_functional.exchange.append(Functional(name=xc))
            elif '_C_' in xc:
                sec_xc_functional.correlation.append(Functional(name=xc))
            elif '_HYB_' in xc:
                sec_xc_functional.hybrid.append(Functional(name=xc))
            else:
                sec_xc_functional.contributions.append(Functional(name=xc))

        spinpol = mainfile_parser.get('scf.SpinPolarization')
        if spinpol.lower() == 'on':
            sec_electronic.n_spin_channels = 2
            self.spinpolarized = True
        else:
            sec_electronic.n_spin_channels = 1
            self.spinpolarized = False

        sec_smearing = Smearing()
        sec_electronic.smearing = sec_smearing
        sec_smearing.kind = 'fermi'
        scf_ElectronicTemperature = mainfile_parser.get('scf.ElectronicTemperature')
        if scf_ElectronicTemperature is not None:
            sec_smearing.width = (
                (scf_ElectronicTemperature * units.kelvin * units.k)
                .to_base_units()
                .magnitude
            )
        else:
            sec_smearing.width = (
                (300 * units.kelvin * units.k).to_base_units().magnitude
            )

        scf_maxiter = mainfile_parser.get('scf.maxIter')
        sec_scf = Scf()
        sec_method.scf = sec_scf
        if scf_maxiter is not None:
            sec_scf.n_max_iteration = scf_maxiter

        scf_criterion = mainfile_parser.get('scf.criterion')
        if scf_criterion is not None:
            sec_scf.threshold_energy_change = scf_criterion * units.hartree

        # vdw correction
        scf_dftd = mainfile_parser.get('scf.dftD')
        if scf_dftd == 'on':
            dftf_ver = mainfile_parser.get('version.dftD')
            # TODO: review the G06/G10 nomenclature after schema migration
            if dftf_ver is None or dftf_ver == 2:
                sec_electronic.van_der_waals_method = 'G06'
            elif dftf_ver == 3:
                sec_electronic.van_der_waals_method = 'G10'
            else:
                self.logger.warning('Unexpected version.dftD value.')
        else:
            sec_electronic.van_der_waals_method = ''

    def parse_eigenvalues(self):
        eigenvalues = BandEnergies()
        self.archive.run[-1].calculation[-1].eigenvalues.append(eigenvalues)
        values = mainfile_parser.get('eigenvalues')
        if values is not None:
            kpoints = values.get('kpoints')
            if kpoints is not None:
                eigenvalues.kpoints = kpoints
                eigenvalues.n_kpoints = len(kpoints)
            else:
                eigenvalues.kpoints = [[0, 0, 0]]
                eigenvalues.n_kpoints = 1
            values = values.get('eigenvalues')
            if values is not None:
                if self.spinpolarized:
                    eigenvalues.energies = np.stack(values, axis=1) * units.hartree
                else:
                    values = [i[0:1] for i in values]
                    eigenvalues.energies = np.stack(values, axis=1) * units.hartree

    def parse(self, mainfile: str, archive: EntryArchive, logger):
        self.archive = archive
        self.logger = logger

        # Use the previously defined parsers on the given mainfile
        mainfile_parser.mainfile = mainfile
        mainfile_parser.parse()
        elapsed_time_mainfile = mainfile_parser.get('elapsed.time')

        del mainfile_parser._file_handler

        # Get system from the MD file
        md_file = path.splitext(mainfile)[0] + '.md'
        if path.isfile(md_file):
            mdfile_md_steps = read_md_file(md_file)
        else:
            mdfile_md_steps = None

        # Some basic values
        sec_run = Run()
        archive.run.append(sec_run)

        sec_run.program = Program(
            name='OpenMX', version=str(mainfile_parser.get('program_version'))
        )
        date_start = mainfile_parser.get('date_start')
        date_start_timestamp = datetime.strptime(
            date_start, '%a %b %d %H:%M:%S %Y'
        ).timestamp()
        sec_run.time_run = TimeRun()
        sec_run.time_run.date_start = date_start_timestamp

        elapsed_time = mainfile_parser.get('elapsed_time')
        if elapsed_time is not None:
            date_end = date_start_timestamp + elapsed_time
            sec_run.time_run.date_end = date_end

        sec_run.clean_end = mainfile_parser.get('have_timing') is not None

        self.parse_workflow()

        self.parse_method()

        mainfile_md_steps = mainfile_parser.get('md_step')
        if mainfile_md_steps is not None:
            n_md_steps = len(mainfile_md_steps)
        n_mdfile_md_steps = 0
        if mdfile_md_steps is not None:
            n_mdfile_md_steps = len(mdfile_md_steps)
        # Do some consistency checks between the out and md file.
        ignore_md_file = False
        if n_mdfile_md_steps > n_md_steps:
            # This can happen when user runs two calculations in the same directory.
            # In that case the out file contains the latter calculation but the md file
            # would contain both calculations, so just take the corresponding number
            # of steps from the end of the file.
            mdfile_md_steps = mdfile_md_steps[-n_md_steps:]
        elif n_mdfile_md_steps < n_md_steps:
            # This is unlikely, but signals a problem with the md file, so just
            # ignore it.
            ignore_md_file = True
            self.logger.warning('.md file does not contain enough MD steps')

        # Stress tensor values are not written to outfile but only to stdout.
        # That means we have to check if the stdout is actually present and
        # look for the stress values there.
        stress_tensor_enabled = mainfile_parser.get('scf.stress.tensor')
        stdout_uele_list = []
        stress_tensors = None
        if stress_tensor_enabled == 'on':
            # find_stdout returns path to correct stdout if it exists
            # or None otherwise
            stdout_path = find_stdout(mainfile)

            if mainfile_md_steps is not None and stdout_path is not None:
                mainfile_uele = mainfile_md_steps[0].get('SCF')[0].get('Uele')
                stdout_parser.mainfile = stdout_path
                stdout_parser.parse()
                stdout_uele_list = stdout_parser.get('Uele')
                stdout_uele = stdout_uele_list[0]
                elapsed_time_stdout = stdout_parser.get('elapsed.time')

                # It is possible there are multiple calculation in the same directory
                # and thus multiple stdout files as well. We need to find the correct
                # stdout to look for the stress values. A simple test is to check the
                # total runtime and later also the uele consistency.
                if (
                    elapsed_time_mainfile == elapsed_time_stdout
                    and abs(stdout_uele - mainfile_uele) < 1e-8
                ):
                    stress_tensors = stdout_parser.get('scf.stress.tensor')

        if mainfile_md_steps is not None:
            for i, md_step in enumerate(mainfile_md_steps):
                system = System()
                sec_run.system.append(system)
                if not ignore_md_file:
                    parse_md_file(i, mdfile_md_steps, system)
                elif i == 0:
                    # Get the initial position from out file as a fallback if the md file is missing.
                    parse_structure(system, logger)

                sec_calc = Calculation()
                sec_run.calculation.append(sec_calc)
                sec_calc.system_ref = system
                sec_calc.method_ref = sec_run.method[-1]
                scf_steps = md_step.get('SCF')
                if scf_steps is not None:
                    for scf_step in scf_steps:
                        scf = ScfIteration()
                        sec_calc.scf_iteration.append(scf)
                        u_ele = scf_step.get('Uele')

                        if u_ele is not None:
                            scf.energy = Energy(
                                sum_eigenvalues=EnergyEntry(value=u_ele * units.hartree)
                            )

                if stress_tensors is not None:
                    stress_matrix = np.array(stress_tensors[i]).reshape(3, 3)
                    stress_matrix = stress_matrix * units.hartree / units.bohr**3
                    sec_calc.stress = Stress()
                    sec_calc.stress.total = StressEntry()
                    sec_calc.stress.total.value = stress_matrix

                u_tot = md_step.get('Utot')
                if u_tot is not None:
                    sec_calc.energy = Energy(
                        total=EnergyEntry(value=u_tot * units.hartree)
                    )
                if not ignore_md_file:
                    forces = mdfile_md_steps[i].get('forces')
                    if forces is not None:
                        sec_calc.forces = Forces(
                            total=ForcesEntry(value=forces * units.hartree / units.bohr)
                        )
                    temperature = mdfile_md_steps[i].get('temperature')
                    if temperature is not None:
                        sec_calc.temperature = float(temperature) * units.kelvin
                    # Time is also printed for geometry optimizations, but it is meaningless there.
                    if isinstance(self.archive.workflow2, MolecularDynamics):
                        time = mdfile_md_steps[i].get('time')
                        if time is not None:
                            sec_calc.time = time * units.fs

        # set core-hole atoms groups
        try:
            sec_system = sec_run[-1].system[-1]
            sec_method = sec_run[-1].method[-1]
            for atom_parameters in sec_method.atom_parameters:
                if atom_parameters.core_hole is not None:
                    try:
                        sec_system.atoms_group.append(
                            AtomsGroup(
                                label='core-hole',
                                type='active_orbitals',
                                atom_indices=self.atom_index_dict[
                                    atom_parameters.label
                                ],
                                n_atoms=len(
                                    self.atom_index_dict[atom_parameters.label]
                                ),
                            )
                        )
                    except KeyError:
                        continue
        except (IndexError, AttributeError):
            pass

        self.parse_eigenvalues()
