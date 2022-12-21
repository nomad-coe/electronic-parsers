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
import re
import logging
import numpy as np
from datetime import datetime

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, EnergyEntry, Forces, ForcesEntry
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, BasisSet, BasisSetCellDependent
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization, MolecularDynamics
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2, GeometryOptimization as GeometryOptimization2, GeometryOptimizationMethod,
    MolecularDynamics as MolecularDyanamics2, MolecularDynamicsMethod)
from .metainfo.cpmd_general import (
    x_cpmd_section_start_information, x_cpmd_section_supercell, x_cpmd_section_md_averaged_quantities
)


re_f = r'[-+]?\d*\.\d*(?:[Ee][-+]\d+)?'
re_n = r'[\n\r]'


class MainfileParser(TextParser):
    def init_quantities(self):

        def to_parameters(val_in):
            separator = ':' if ':' in val_in else '  '
            return [v.strip() for v in val_in.strip().split(separator) if v]

        step_quantities = [
            Quantity(
                'atom_coordinates_forces',
                rf'ATOM +COORDINATES.+\s+((?:\d+ +[A-Z][a-z]*.+{re_f}\s+)+)',
                str_operation=lambda x: [v.split() for v in x.strip().splitlines()]
            ),
            Quantity(
                'scf',
                rf'((?:\s+\d+ +{re_f} +{re_f} +{re_f} +{re_f} +{re_f})+)',
                dtype=np.dtype(np.float64), str_operation=lambda x: [v.split() for v in x.strip().splitlines()]
            ),
            Quantity(
                'energies',
                rf'(.+TOTAL ENERGY =.+\s(?:.+= +{re_f} A\.U\.\s)+)',
                sub_parser=TextParser(quantities=[
                    Quantity('total', rf'TOTAL ENERGY += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('kinetic', rf'KINETIC ENERGY += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('electrostatic', rf'ELECTROSTATIC ENERGY += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('x_cpmd_eself', rf'ESELF += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('x_cpmd_esr', rf'ESR += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('x_cpmd_local_pseudopotential', rf'LOCAL PSEUDOPOTENTIAL ENERGY += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('x_cpmd_nl_pseudopotential', rf'N-L PSEUDOPOTENTIAL ENERGY += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                    Quantity('xc', rf'EXCHANGE-CORRELATION ENERGY += +({re_f})', dtype=np.float64, unit=ureg.hartree),
                ])
            ),
            Quantity('x_cpmd_restart_file', r'RESTART INFORMATION WRITTEN ON FILE +(\S+)', dtype=str),
            Quantity('x_cpmd_total_number_of_scf_steps', r'TOTAL STEP NR\. +(\d+)', dtype=np.int32),
            Quantity('x_cpmd_gnmax', rf'GNMAX= +({re_f})', dtype=np.float64),
            Quantity('x_cpmd_gnorm', rf'GNORM= +({re_f})', dtype=np.float64),
            Quantity('x_cpmd_cnstr', rf'CNSTR= +({re_f})', dtype=np.float64),
            Quantity('time_calculation', rf'CNSTR= +({re_f})', dtype=np.float64),
        ]

        self._quantities = [
            Quantity(
                'header',
                r'(PROGRAM CPMD STARTED[\s\S]+?JOB WAS SUBMITTED BY.+)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'date_start',
                        r'PROGRAM CPMD STARTED AT\: (\d+\-\d+\-\d+ \d+\:\d+\:\d+\.\d+)',
                        dtype=str, flatten=False
                    ),
                    Quantity('program_version', r'VERSION (.+)', dtype=str, flatten=False),
                    Quantity(
                        'x_cpmd_compilation_date',
                        r'\*\*\* +(\w+ \d+ \d+ \-\- \d+\:\d+\:\d+)',
                        dtype=str, flatten=False
                    ),
                    Quantity('x_cpmd_input_filename', r'THE INPUT FILE IS: +(\S+)', dtype=str),
                    Quantity('x_cpmd_run_host_name', r'THIS JOB RUNS ON: +(\S+)', dtype=str),
                    Quantity('x_cpmd_process_id', r'THE PROCESS ID IS: +(\S+)', dtype=str),
                    Quantity('x_cpmd_run_user_name', r'THE JOB WAS SUBMITTED BY: +(\S+)', dtype=str),
                ])
            ),
            Quantity(
                'info',
                r'(INFO[\s\S]+?USING SEED[\s\S]+?)\*\*\*\*\*',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'simulation_type',
                        r'((?:SINGLE POINT DENSITY OPTIMIZATION)|(?:OPTIMIZATION OF IONIC POSITIONS)'
                        r'|(?:CAR\-PARRINELLO MOLECULAR DYNAMICS)|(?:BORN-OPPENHEIMER MOLECULAR DYNAMICS))',
                        dtype=str, flatten=False
                    ),
                    Quantity(
                        'simulation_parameters',
                        rf'([A-Z][ A-Z\-]+?)((?:  |:)) *((?:{re_f}|\d+|[A-Z][ A-Z]+)).*',
                        str_operation=to_parameters, repeats=True),
                    Quantity('geometry_optimization_method', r'GEOMETRY OPTIMIZATION BY (\S+)', dtype=str)
                ])
            ),
            Quantity(
                'atoms',
                rf'ATOMS \*+\s+NR.+\s+((?:\d+ +[A-Z][a-z]* +{re_f} +{re_f} +{re_f} +\d+\s+)+)',
                str_operation=lambda x: [v.split() for v in x.strip().splitlines()]
            ),
            Quantity(
                'supercell',
                r'SUPERCELL \*+([\s\S]+?)\*{10}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'lattice_vectors',
                        rf'LATTICE VECTOR A\d\(BOHR\): +({re_f} +{re_f} +{re_f})',
                        dtype=np.dtype(np.float64), repeats=True
                    ),
                    Quantity(
                        'lattice_vectors_reciprocal',
                        rf'RECIP\. LAT\. VEC\. B\d\(2Pi/BOHR\): +({re_f} +{re_f} +{re_f})',
                        dtype=np.dtype(np.float64), repeats=True
                    ),
                    Quantity('x_cpmd_cell_symmetry', r'SYMMETRY:\s+(.+)', dtype=str, flatten=False),
                    Quantity('x_cpmd_cell_lattice_constant', rf'LATTICE CONSTANT\(a\.u\.\):\s+({re_f})', dtype=np.float64),
                    Quantity('x_cpmd_cell_dimension', rf'CELL DIMENSION:\s+(.+)', dtype=np.dtype(np.float64)),
                    Quantity('x_cpmd_cell_volume', rf'VOLUME\(OMEGA IN BOHR\^3\):\s+({re_f})', dtype=np.float64),
                    Quantity('x_cpmd_cell_real_space_mesh', rf'REAL SPACE MESH:\s+(\d+ +\d+ +\d+)', dtype=np.dtype(np.int32)),
                    Quantity('x_cpmd_wave_function_cutoff', rf'WAVEFUNCTION CUTOFF\(RYDBERG\):\s+({re_f})', dtype=np.float64),
                    Quantity('x_cpmd_density_cutoff', rf'DENSITY CUTOFF\(RYDBERG\):({re_f})', dtype=np.float64),
                    Quantity('x_cpmd_number_of_planewaves_wave_function', rf'NUMBER OF PLANE WAVES FOR WAVEFUNCTION CUTOFF:\s+(\d+)', dtype=np.int32),
                    Quantity('x_cpmd_number_of_planewaves_density', rf'NUMBER OF PLANE WAVES FOR DENSITY CUTOFF:\s+(\d+)', dtype=np.int32),
                ])
            ),
            Quantity(
                'geometry_optimization',
                r'GEOMETRY OPTIMIZATION +\=([\s\S]+?)(?:END OF GEOMETRY OPTIMIZATION|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'step',
                        rf'((?:NFI|\*\*\*\*\*)[\s\S]+?TCPU=.+)',
                        repeats=True, sub_parser=TextParser(quantities=step_quantities)
                    ),
                ])
            ),
            Quantity(
                'single_point',
                r'(ATOM +COORDINATES[\s\S]+?(?:RESTART .+|\Z))',
                sub_parser=TextParser(quantities=step_quantities)
            ),
            Quantity(
                'molecular_dynamics',
                r'(NFI +EKINC +TEMPP[\s\S]+?(?:CPU TIME|\Z))',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'frame',
                        rf'((?:\d+ +{re_f} +{re_f} +{re_f} +{re_f} +{re_f} +{re_f} +{re_f}\s+)+)',
                        dtype=np.dtype(np.float64), repeats=True
                    ),
                    Quantity(
                        'averaged',
                        r'AVERAGED QUANTITIES +\*+\s+\*+\s+MEAN VALUE.+\s+\<x\>.+\s+'
                        rf'((?:[ A-Z]+ +{re_f} +{re_f}\s+)+)',
                        str_operation=lambda x: [v.split() for v in x.strip().splitlines()]
                    ),
                ])
            )
        ]

    def get_simulation_parameters(self):
        return {val[0]: val[1] for val in self.get('info', {}).get('simulation_parameters', [])}


class TrajectoryParser(DataTextParser):
    def init_parameters(self):
        if self._file_handler is None:
            return
        data = np.transpose(self._file_handler)
        # first column is the md step
        n_frames = int(np.amax(data[0]))
        # atoms are denoted by same step index
        n_atoms = int(np.count_nonzero(data[0] == 1))
        # for FTRAJECTORY, we expect also forces in addition to positions, velocities
        n_data = len(data) // 3
        # we remove the index
        data = np.transpose(data[1:])
        self._file_handler = np.reshape(data, (n_frames, n_atoms, n_data, 3))


# we simply make our own parser instead of using MDAnalysis for a simple xyz file
class XYZParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'step',
                rf'(STEP\: +\d+[\s\S]+?)(\s+\d+\s+|\Z)',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity('step', r'STEP\: +(\d+)', dtpye=np.int32),
                    Quantity('labels', r'([A-Z][a-z]*)\S*', repeats=True),
                    Quantity(
                        'positions',
                        rf'({re_f} +{re_f} +{re_f})',
                        dtype=np.dtype(np.float64), repeats=True)
                ])
            )
        ]


class CPMDParser:
    def __init__(self):
        self.mainfile_parser = MainfileParser()
        self.trajectory_parser = TrajectoryParser()
        self.xyz_parser = XYZParser()
        self.energies_parser = DataTextParser()
        self._method_map = {
            'GDIIS/BFGS': 'bfgs', 'LOW-MEMORY BFGS': 'bfgs',
            'CONJUGATE GRADIENT': 'conjugate_gradient', 'STEEPEST DESCENT': 'steepest_descent'
        }
        self._metainfo_map = {
        }

    def init_parser(self):
        self.mainfile_parser.mainfile = self.filepath
        self.mainfile_parser.logger = self.logger
        self.trajectory_parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.maindir = os.path.dirname(self.filepath)

        self.init_parser()

        sec_run = archive.m_create(Run)
        header = self.mainfile_parser.get('header', {})
        sec_run.program = Program(version=header.get('program_version'))
        if header.get('date_start') is not None:
            sec_run.time_run = TimeRun(date_start=datetime.strptime(
                header.get('date_start'), '%Y-%m-%d %H:%M:%S.%f').timestamp())

        sec_start_info = sec_run.m_create(x_cpmd_section_start_information)
        for key, val in header.items():
            if key.startswith('x_cpmd'):
                setattr(sec_start_info, key, val)

        def parse_system(source):
            if source.atom_coordinates_forces is None:
                return

            sec_system = sec_run.m_create(System)
            sec_system.atoms = Atoms(
                labels=[val[1] for val in source.atom_coordinates_forces],
                positions=np.array([val[2:5] for val in source.atom_coordinates_forces]) * ureg.bohr
            )
            sec_supercell = sec_system.m_create(x_cpmd_section_supercell)
            for key, val in self.mainfile_parser.get('supercell', {}).items():
                if key == 'lattice_vectors':
                    sec_system.atoms.lattice_vectors = val * ureg.bohr
                elif key.startswith('x_cpmd'):
                    setattr(sec_supercell, key, val)

            return sec_system

        def parse_calculation(source):
            sec_calc = sec_run.m_create(Calculation)

            if source.energies is not None:
                sec_energy = sec_calc.m_create(Energy)
                for key, val in source.energies.items():
                    if key == 'kinetic':
                        sec_energy.total.kinetic = val
                    setattr(sec_energy, key, EnergyEntry(value=val))

            for scf in source.get('scf', []):
                sec_scf = sec_calc.m_create(ScfIteration)
                sec_scf.time_calculation = scf[-1] * ureg.s
                sec_scf.energy = Energy(
                    total=EnergyEntry(value=scf[3] * ureg.hartree), change=scf[4] * ureg.hartree)

            if source.atom_coordinates_forces is not None:
                sec_calc.forces = Forces(
                    total=ForcesEntry(value=[val[5:8] for val in source.atom_coordinates_forces] * ureg.hartree / ureg.bohr))

            sec_calc.time_calculation = source.time_calculation
            if source.energies is None and source.scf is not None:
                sec_calc.energy = sec_scf.energy

            for key, val in source.items():
                if key.startswith('x_cpmd_'):
                    setattr(sec_calc, key, val)

            return sec_calc

        def resolve_ensemble_type():
            # TODO consider other cases
            ion_dyn = self.mainfile_parser.get_simulation_parameters().get('ION DYNAMICS')
            ensemble_type = 'NVE' if ion_dyn == 'THE TEMPERATURE IS NOT CONTROLLED' else None
            return ensemble_type

        sec_workflow = archive.m_create(Workflow)
        workflow = None

        simulation_type = self.mainfile_parser.get('info', {}).get('simulation_type')
        if simulation_type == 'SINGLE POINT DENSITY OPTIMIZATION':
            workflow = SinglePoint2()
            sec_workflow.type = 'single_point'
            sec_system = parse_system(self.mainfile_parser.single_point)
            sec_calc = parse_calculation(self.mainfile_parser.single_point)
            sec_calc.system_ref = sec_system

        elif self.mainfile_parser.geometry_optimization is not None:
            workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
            sec_workflow.type = 'geometry_optimization'
            method = self.mainfile_parser.get('info', {}).get('geometry_optimization_method')
            sec_workflow.geometry_optimization = GeometryOptimization(
                method=self._method_map.get(method, method))
            workflow.method.method = self._method_map.get(method, method)
            for step in self.mainfile_parser.geometry_optimization.get('step', []):
                sec_system = parse_system(step)
                sec_calc = parse_calculation(step)
                sec_calc.system_ref = sec_system

        elif self.mainfile_parser.molecular_dynamics is not None:
            workflow = MolecularDyanamics2(method=MolecularDynamicsMethod())
            sec_workflow.type = 'molecular_dynamics'
            sec_workflow.molecular_dynamics = MolecularDynamics(
                thermodynamic_ensemble=resolve_ensemble_type()
            )
            workflow.method.thermodynamic_ensemble = resolve_ensemble_type()
            sec_averaged = sec_workflow.molecular_dynamics.m_create(x_cpmd_section_md_averaged_quantities)
            for value in self.mainfile_parser.molecular_dynamics.get('averaged', []):
                name = '_'.join(value[:-2]).lower()
                setattr(sec_averaged, f'x_cpmd_{name}_mean', value[-2])
                setattr(sec_averaged, f'x_cpmd_{name}_std', value[-1])

            # TODO read trajectory from other file formats dcd
            # read atom positions and velocities from (F)TRAJECTORY

            def read_xyz_trajectory(filename):
                self.xyz_parser.mainfile = os.path.join(self.maindir, filename)
                trajectory = [step.get('positions') for step in self.xyz_parser.get('step', [])]
                if trajectory:
                    # reshape to conform with trajectory parser
                    trajectory = np.reshape(trajectory, (len(trajectory), len(trajectory[0]), 1, 3))
                return trajectory

            trajectory = None
            trajectory_files = [f for f in os.listdir(self.maindir) if re.search(r'.*TRAJECTORY', f, re.IGNORECASE)]
            if trajectory_files:
                self.trajectory_parser.mainfile = os.path.join(self.maindir, trajectory_files[0])
                if self.trajectory_parser.data is None:
                    # maybe this is an xyz file (nomad #1196)
                    trajectory = read_xyz_trajectory(trajectory_files[0])

            if trajectory is None:
                trajectory_files = [f for f in os.listdir(self.maindir) if re.search(r'.*\.xyz', f, re.IGNORECASE)]
                if self.trajectory_parser.data is None and trajectory_files:
                    # read from xyz file
                    trajectory = read_xyz_trajectory(trajectory_files[0])
                else:
                    trajectory = self.trajectory_parser.data
                    trajectory = [] if trajectory is None else trajectory

            # we also initialize energies parser
            energies = None
            energy_files = [f for f in os.listdir(self.maindir) if re.search(r'.*ENERGIES', f, re.IGNORECASE)]
            if energy_files:
                self.energies_parser.mainfile = os.path.join(self.maindir, energy_files[0])
            if self.energies_parser.mainfile is None:
                # get energies from mainfile
                energies = self.mainfile_parser.molecular_dynamics.get('frame', [])
            else:
                energies = self.energies_parser.data
                energies = [] if energies is None else energies

            # assert that energies and trajectory data match
            match = True
            start = 0
            if len(energies) != len(trajectory):
                self.logger.warning('Trajectory and energies files do not match.')
                match = False

            def write_energies(source, target):
                target.energy = Energy(total=EnergyEntry(
                    value=source[5] * ureg.hartree,
                    potential=source[3] * ureg.hartree,
                    kinetic=source[1] * ureg.hartree))
                target.time_calculation = source[7] * ureg.s
                target.temperature = source[2] * ureg.kelvin

            lattice_vectors = self.mainfile_parser.get('supercell', {}).get('lattice_vectors')
            lattice_vectors = lattice_vectors * ureg.bohr if lattice_vectors else lattice_vectors
            for n_frame in range(len(trajectory)):
                sec_system = sec_run.m_create(System)
                sec_system.atoms = Atoms(
                    labels=[atom[1] for atom in self.mainfile_parser.get('atoms', [])],
                    positions=trajectory[n_frame, :, 0, :] * ureg.bohr,
                    lattice_vectors=lattice_vectors,
                    periodic=None if lattice_vectors is None else [True, True, True]
                )
                if len(trajectory[n_frame][0]) > 1:
                    sec_system.atoms.velocities = trajectory[n_frame, :, 1, :] * ureg.bohr / (ureg.dirac_constant / ureg.hartree)

                sec_calc = sec_run.m_create(Calculation)
                if len(trajectory[n_frame][0]) > 2:
                    sec_calc.forces = trajectory[n_frame, :, 1, :] * ureg.hartree / ureg.bohr

                if match:
                    write_energies(energies[n_frame], sec_calc)
                else:
                    for energies_n in range(start, len(energies)):
                        if n_frame == int(energies[energies_n][0]):
                            start = energies_n
                            write_energies(energies[energies_n], sec_calc)
                            break

        sec_method = sec_run.m_create(Method)
        sec_basis = sec_method.m_create(BasisSet)
        sec_basis.type = 'plane waves'
        sec_basis.kind = 'wavefunction'
        cutoff = self.mainfile_parser.get('supercell', {}).get('x_cpmd_wave_function_cutoff', 0.)
        sec_cell_basis = sec_basis.m_create(BasisSetCellDependent)
        sec_cell_basis.planewave_cutoff = cutoff * ureg.rydberg
        sec_cell_basis.name = f'PW_{cutoff}'
        sec_method.x_cpmd_simulation_parameters = self.mainfile_parser.get_simulation_parameters()
        # TODO xc functionals. The mapping cannot be ascertained

        archive.workflow2 = workflow
