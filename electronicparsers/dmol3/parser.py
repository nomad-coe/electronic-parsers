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
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import Method, BasisSet
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, EnergyEntry, BandEnergies, Charges, Multipoles,
    MultipolesEntry, VibrationalFrequencies
)
from nomad.datamodel.metainfo.workflow import Workflow, Thermodynamics, GeometryOptimization
from nomad.datamodel.metainfo.simulation.workflow import (
    GeometryOptimization as GeometryOptimization2, GeometryOptimizationMethod,
    Thermodynamics as Thermodynamics2, ThermodynamicsResults
)

from .metainfo import dmol3  # pylint: disable=unused-import


re_f = r'[-+]?\d*\.\d*(?:[Ee][-+]\d+)?'
re_n = r'[\n\r]'
MOL = 6.02214076e+23


class MainfileParser(TextParser):
    def init_quantities(self):

        coordinates_quantities = [
            Quantity('labels_positions', rf'([A-Z][a-z]* +{re_f} +{re_f} +{re_f})', repeats=True)
        ]

        scf_quantity = Quantity(
            'scf',
            r'Start Computing SCF Energy/Gradient([\s\S]+?)End Computing SCF Energy/Gradient',
            repeats=True, sub_parser=TextParser(quantities=[
                Quantity(
                    'iteration',
                    rf'Ef +({re_f} +{re_f} +{re_f} +{re_f} +\d+)',
                    repeats=True, dtype=np.dtype(np.float64)
                ),
                Quantity(
                    'eigenvalues',
                    rf'state +eigenvalue +occupation\s+\(au\) +\(ev\)\s+'
                    rf'((?:\d+ +\S+ +\d+ +\S+ +{re_f} +{re_f} +{re_f}\s+)+)',
                    repeats=True, str_operation=lambda x: np.transpose(
                        [v.split()[4:] for v in x.strip().splitlines()])
                ),
                Quantity(
                    'n_electrons',
                    rf'Total number electrons\: +({re_f})', dtype=np.float64
                ),
                Quantity(
                    'coordinates',
                    r'ATOMIC  COORDINATES \(au\).+\s*df +x +y +z +.+\s*\-+\s+'
                    rf'((?:df +[A-Z][a-z]* +{re_f} +{re_f} +{re_f}.+\s+)+)',
                    sub_parser=TextParser(quantities=coordinates_quantities)
                ),
                Quantity('energy_total', rf'Ef +({re_f})', dtype=np.float64, unit=ureg.hartree),
                Quantity('energy_binding', rf'binding energy +({re_f})Ha', dtype=np.float64, unit=ureg.hartree),
            ])
        )

        self._quantities = [
            Quantity(
                'program_version',
                r'Materials Studio DMol\^3 version (\S+)', dtype=str, flatten=False
            ),
            Quantity(
                'x_dmol3_program_compilation_date',
                r'compiled on (\w+ \d+ \d+ \d+\:\d+:\d+)', dtype=str, flatten=False
            ),
            Quantity(
                'date_start',
                r'DATE\: +(\w+ \d+ \d+\:\d+\:\d+ \d+)', dtype=str, flatten=False
            ),
            Quantity(
                'coordinates',
                rf'\$coordinates\s+([\s\S]+?)\$end', flatten=False,
                sub_parser=TextParser(quantities=coordinates_quantities)
            ),
            Quantity(
                'simulation_parameters',
                r'INPUT_DMOL keywords.+\s+.+([\s\S]+?)\>8',
                sub_parser=TextParser(quantities=[
                    Quantity('calculation_type', rf'{re_n}Calculate +(\S+)', dtype=str),
                    Quantity('functional_name', rf'{re_n}Functional +(\S+)', dtype=str),
                    Quantity('pseudopotential_name', rf'{re_n}Pseudopotential +(\S+)', dtype=str),
                    Quantity('basis_name', rf'{re_n}Basis +(\S+)', dtype=str),
                    Quantity('spin_polarization', rf'{re_n}Spin_Polarization +(\S+)', dtype=str),
                    Quantity('spin', rf'{re_n}Spin +(\d+)', dtype=np.int32),
                    Quantity('rcut', rf'{re_n}Atom_Rcut +({re_f})', dtype=np.float64),
                    Quantity('integration_grid', rf'{re_n}Integration_Grid +(\S+)', dtype=str),
                    Quantity('aux_partition', rf'{re_n} +(\d+)', dtype=np.int32),
                    Quantity('aux_density', rf'{re_n}Aux_Density +(\d+)', dtype=str),
                    Quantity('charge', rf'{re_n}Charge +({re_f})', dtype=np.float64),
                    Quantity('symmetry', rf'{re_n}Symmetry +(\S+)', dtype=str),
                    Quantity('mulliken_analysis', rf'{re_n}Mulliken_Analysis +(\S+)', dtype=str),
                    Quantity('hirshfeld_analysis', rf'{re_n}Hirshfeld_Analysis +(\S+)', dtype=str),
                    Quantity('partial_dos', rf'{re_n}Partial_Dos +(\S+)', dtype=str),
                    Quantity('electrostatic_moments', rf'{re_n}Electrostatic_Moments +(\S+)', dtype=str),
                    Quantity('nuclear_efg', rf'{re_n}Nuclear_EFG +(\S+)', dtype=str),
                    Quantity('optical_absorption', rf'{re_n}Optical_Absorption +(\S+)', dtype=str),
                    Quantity('kpoints', rf'{re_n}Kpoints +(\S+)', dtype=str),
                    Quantity('scf_density_convergence', rf'{re_n}SCF_Density_Convergence +({re_f})', dtype=np.float64),
                    Quantity('scf_spin_mixing', rf'{re_n}SCF_Spin_Mixing +({re_f})', dtype=np.float64),
                    Quantity('scf_charge_mixing', rf'{re_n}SCF_Charge_Mixing +({re_f})', dtype=np.float64),
                    Quantity('scf_diis', rf'{re_n}SCF_DIIS +(\d+) +(\S+)'),
                    Quantity('scf_iterations', rf'{re_n}SCF_Iterations +(\d+)', dtype=np.int32),
                    Quantity('scf_number_bad_steps', rf'{re_n}SCF_Number_Bad_Steps +(\d+)', dtype=np.int32),
                    Quantity('scf_direct', rf'{re_n}SCF_Direct +(\S+)', dtype=str),
                    Quantity('scf_restart', rf'{re_n}SCF_Restart +(\S+)', dtype=str),
                    Quantity('occupation', rf'{re_n}Occupation +(.+?) +<\-\-', str_operation=lambda x: x.strip().split()),
                    Quantity('opt_energy_convergence', rf'{re_n}OPT_Energy_Convergence +({re_f})', dtype=np.float64),
                    Quantity('opt_gradient_convergence', rf'{re_n}OPT_Gradient_Convergence +({re_f})', dtype=np.float64),
                    Quantity('opt_displacement_convergence', rf'{re_n}OPT_Displacement_Convergence +({re_f})', dtype=np.float64),
                    Quantity('opt_iterations', rf'{re_n}OPT_Iterations +(\d+)', dtype=np.int32),
                    Quantity('opt_coordinate_system', rf'{re_n}OPT_Coordinate_System +(\S+)', dtype=str),
                    Quantity('opt_gdiis', rf'{re_n}OPT_Gdiis +(\S+)', dtype=str),
                    Quantity('opt_max_displacement', rf'{re_n}OPT_Max_Displacement +({re_f})', dtype=np.float64),
                    Quantity('opt_steep_tol', rf'{re_n}OPT_Steep_Tol +({re_f})', dtype=np.float64),
                    Quantity('opt_hessian_project', rf'{re_n}OPT_Hessian_Project +(\S+)', dtype=str),
                ])
            ),
            Quantity(
                'optimization',
                r'Entering Optimization Section \+\+\+([\s\S]+?)(?:\+\+\+|\Z)',
                sub_parser=TextParser(quantities=[
                    scf_quantity,
                    Quantity(
                        'geometry',
                        r'Start Getting New Geometry([\s\S]+?)End Getting New Geometry',
                        repeats=True, sub_parser=TextParser(
                            quantities=[
                                Quantity(
                                    'coordinates',
                                    r'Input Coordinates \(Angstroms\)\s+\-+\s+ATOM +X +Y +Z\s+'
                                    rf'((?:\d+ +[A-Z][a-z]* +{re_f} +{re_f} +{re_f}\s+)+)',
                                    sub_parser=TextParser(quantities=coordinates_quantities)
                                ),
                                Quantity(
                                    'tolerance',
                                    rf'tolerance:\S+ +({re_f} +{re_f} +{re_f})',
                                    dtype=np.dtype(np.float64)
                                ),
                                Quantity(
                                    'energy_gradient',
                                    rf'opt\=\= +(\d+ +{re_f} +{re_f} +{re_f} +{re_f})',
                                    dtype=np.dtype(np.float64)
                                )
                            ]
                        )
                    )
                ])
            ),
            Quantity(
                'properties',
                r'Entering Properties Section \+\+\+([\s\S]+?)(?:\+\+\+|\Z)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'hirschfeld',
                        rf'Charge partitioning by Hirshfeld method\:\s+((?:[A-Z][a-z]* +\d+ +charge +{re_f}\s+)+)',
                        sub_parser=TextParser(quantities=[
                            Quantity('label', r'([A-Z][a-z]*)', repeats=True, dtype=str),
                            Quantity('charge', rf'({re_f})', repeats=True, dtype=np.float64)
                        ])
                    ),
                    Quantity('dipole_moment', rf'dipole magnitude\:.+?({re_f}) debye', dtype=np.float64),
                    Quantity(
                        'mulliken',
                        rf'Mulliken atomic charges\:\s*charge +spin\s+((?:[A-Z][a-z]*\([ \d]+\) +{re_f} +{re_f}\s+)+)',
                        sub_parser=TextParser(quantities=[
                            Quantity('charge', rf'\) +({re_f})', dtype=np.float64, repeats=True),
                            Quantity('spin', rf'({re_f}) *{re_n}', dtype=np.float64, repeats=True)
                        ])
                    )
                ])
            ),
            Quantity(
                'vibrations',
                r'Entering Vibrations Section \+\+\+([\s\S]+?)(?:\+\+\+|\Z)',
                sub_parser=TextParser(quantities=[
                    scf_quantity,
                    # TODO map it to scf
                    Quantity('dipole_moment', rf'dipole magnitude\:.+?({re_f}) debye', dtype=np.float64, repeats=True),
                    Quantity(
                        'vibrational_frequencies',
                        rf'vibrational frequencies, intensities\s+mode.+\s+((?:\d+ +{re_f} +{re_f} +{re_f}\s+)+)',
                        dtype=np.dtype(np.float64), flatten=False,
                        str_operation=lambda x: [v.split()[2] for v in x.strip().splitlines()], unit=1 / ureg.cm
                    ),
                    Quantity(
                        'normal_modes',
                        r'Frequencies \(cm\-1\) and normal modes\s+.+\s+'
                        r'((?:[A-Z][a-z]* +x.+\s+y.+\s+z.+\s+)+)',
                        sub_parser=TextParser(quantities=[
                            Quantity('label', r'([A-Z][a-z]*)', repeats=True),
                            Quantity('value', rf'(?:x|y|z) +({re_f}.+)', repeats=True, dtype=np.dtype(np.float64))
                        ])
                    ),
                    Quantity(
                        'thermodynamic_quantities',
                        r'(STANDARD THERMODYNAMIC QUANTITIES AT[\s\S]+?G,Total\:.+)',
                        sub_parser=TextParser(quantities=[
                            Quantity('temperature', rf'AT +({re_f}) K', dtype=np.float64, unit=ureg.kelvin),
                            Quantity('pressure', rf'AND +({re_f}) ATM', dtype=np.float64, unit=ureg.atm),
                            Quantity(
                                'energy_zero_point',
                                rf'Zero point vibrational energy\: +({re_f}) kcal/mol',
                                dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_h_trans',
                                rf'H,Trans *\: +({re_f}) kcal/mol', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_h_rot',
                                rf'H,Rot *\: +({re_f}) kcal/mol', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_h_pv',
                                rf'H,pV *\: +({re_f}) kcal/mol', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_h_vib_minus_zpve',
                                rf'H,Vib \- ZPVE *\: +({re_f}) kcal/mol', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_s_trans',
                                rf'S,Trans *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_s_rot',
                                rf'S,Rot *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_s_vib',
                                rf'S,Vib *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_c_trans',
                                rf'C,Trans *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_c_rot',
                                rf'C,Rot *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_c_vib',
                                rf'C,Vib *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_h_total_minus_zpve',
                                rf'H,Total \- ZPVE *\: +({re_f}) kcal/mol', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_s_total',
                                rf'S,Total *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_c_total',
                                rf'C,Total \(p\) *\: +({re_f}) +cal/mol\.K', dtype=np.float64
                            ),
                            Quantity(
                                'x_dmol3_g_total',
                                rf'G,Total *\: +({re_f}) +kcal/mol', dtype=np.float64
                            ),
                        ])
                    ),
                    Quantity(
                        'thermodynamic_quantities_steps',
                        r'T +Entropy +Heat_Capacity +Enthalpy +Free_Energy\s+'
                        rf'\(K\).+\s+.+\s+\_+\s+((?:\d+ +{re_f} +{re_f} +{re_f} +{re_f} +{re_f}\s+)+)',
                        flatten=False, str_operation=lambda x: [v.split() for v in x.strip().splitlines()],
                        dtype=np.dtype(np.float64)
                    )
                ])
            )

        ]

    @property
    def parameters(self):
        return {key: val for key, val in self.get('simulation_parameters', {}).get('key_value', [])}


class Dmol3Parser:
    def __init__(self):
        self.mainfile_parser = MainfileParser()

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger

        # initialize the parsers
        self.mainfile_parser.logger = self.logger
        self.mainfile_parser.mainfile = self.filepath

        sec_run = archive.m_create(Run)
        sec_run.program = Program(
            version=self.mainfile_parser.get('program_version'),
            x_dmol3_compilation_date=self.mainfile_parser.get('x_dmol3_program_compilation_date')
        )

        if self.mainfile_parser.date_start is not None:
            date = datetime.strptime(self.mainfile_parser.date_start, '%b %d %H:%M:%S %Y')
            sec_run.time_run = TimeRun(date_start=date.timestamp())

        # section method
        sec_method = sec_run.m_create(Method)
        # basis set
        sec_method.basis_set.append(BasisSet(type='numeric AOs'))
        # simulation parameters
        for key, val in self.mainfile_parser.simulation_parameters.items():
            if key == 'scf_diis':
                sec_method.x_dmol3_diis_number = val[0]
                sec_method.x_dmol3_diis_name = val[1]
            elif key == 'occupation':
                sec_method.x_dmol3_occupation_name = val[0]
                if len(val) > 1:
                    sec_method.x_dmol3_occupation_width = val[1]
            else:
                setattr(sec_method, f'x_dmol3_{key}', val)

        def parse_system(source):
            if source.coordinates is None:
                return

            sec_system = sec_run.m_create(System)
            sec_system.atoms = Atoms(
                labels=[v[0] for v in source.coordinates.get('labels_positions', [])],
                positions=[v[1:4] for v in source.coordinates.get('labels_positions', [])] * ureg.bohr
            )
            return sec_system

        def parse_calculation(source, target=None):
            target = sec_run.m_create(Calculation) if target is None else target

            # energies
            target.energy = Energy(
                total=EnergyEntry(value=source.energy_total),
                x_dmol3_binding=EnergyEntry(value=source.energy_binding))

            # scf iteration
            for iteration in source.get('iteration', []):
                sec_scf = target.m_create(ScfIteration)
                sec_scf.energy = Energy(
                    total=EnergyEntry(value=iteration[0] * ureg.hartree),
                    x_dmol3_binding=EnergyEntry(value=iteration[1] * ureg.hartree),
                )
                sec_scf.time_calculation = iteration[3] * ureg.minute
            # add energies data from last scf step
            if source.iteration:
                target.energy.x_dmol3_binding = sec_scf.energy.x_dmol3_binding

            # eigenvalues
            if source.eigenvalues is not None:
                sec_eigenvalues = target.m_create(BandEnergies)
                # TODO handle number of kpoints
                energies = [e[0] for e in source.eigenvalues]
                # index 1 is energies in eV
                occupations = [e[2] for e in source.eigenvalues]
                spin = 1 if occupations[0][0] > 1 else 2
                shape = (spin, len(energies), len(energies[0]))
                sec_eigenvalues.energies = np.reshape(energies, shape) * ureg.hartree
                sec_eigenvalues.occupations = np.reshape(occupations, shape)

            # population analysis
            for method in ['hirschfeld', 'mulliken']:
                population = source.get(method)
                if population is None:
                    continue
                sec_charges = target.m_create(Charges)
                sec_charges.analysis_method = method
                if population.charge is not None:
                    sec_charges.value = population.charge * ureg.elementary_charge
                if population.spin is not None:
                    sec_charges.spins = population.spin

            # dipole momentp
            if source.dipole_moment is not None:
                sec_multipole = target.m_create(Multipoles)
                sec_multipole.dipole = MultipolesEntry(total=source.dipole_moment)

            # vibrational frequencies
            if source.vibrational_frequencies is not None:
                sec_vibrations = target.m_create(VibrationalFrequencies)
                sec_vibrations.value = source.vibrational_frequencies
                # normal modes
                if source.normal_modes is not None:
                    value = source.normal_modes.value
                    n_atoms = len(source.normal_modes.label)
                    sec_vibrations.x_dmol3_normal_modes = np.transpose(np.reshape(
                        value, (n_atoms, 3, len(value[0]))), axes=(2, 0, 1))

            # thermodynamics quantities
            if source.thermodynamic_quantities is not None:
                for key, val in source.thermodynamic_quantities.items():
                    if key == 'energy_zero_point':
                        target.energy.zero_point = EnergyEntry(
                            value=source.thermodynamic_quantities.energy_zero_point * ureg.J * 4184.0 / MOL)
                    else:
                        setattr(target, key, val)

            return target

        workflow = None
        if self.mainfile_parser.optimization is not None:
            for scf in self.mainfile_parser.optimization.get('scf', []):
                sec_system = parse_system(scf)
                sec_calc = parse_calculation(scf)
                sec_calc.system_ref = sec_system
            sec_workflow = archive.m_create(Workflow)
            workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
            sec_workflow.type = 'geometry_optimization'
            sec_opt = sec_workflow.m_create(GeometryOptimization)
            tolerance = self.mainfile_parser.optimization.get('geometry', [{}])[0].get('tolerance', [0, 0, 0])
            sec_opt.convergence_tolerance_energy_difference = tolerance[0] * ureg.hartree
            sec_opt.convergence_tolerance_force_maximum = tolerance[1] * ureg.hartree / ureg.bohr
            sec_opt.convergence_tolerance_displacement_maximum = tolerance[2] * ureg.bohr
            workflow.method.convergence_tolerance_energy_difference = tolerance[0] * ureg.hartree
            workflow.method.convergence_tolerance_force_maximum = tolerance[1] * ureg.hartree / ureg.bohr
            workflow.method.convergence_tolerance_displacement_maximum = tolerance[2] * ureg.bohr

        if self.mainfile_parser.properties is not None:
            parse_calculation(self.mainfile_parser.properties, sec_run.calculation[-1])

        if self.mainfile_parser.vibrations is not None:
            workflow = Thermodynamics2(results=ThermodynamicsResults())
            for scf in self.mainfile_parser.vibrations.get('scf', []):
                sec_system = parse_system(scf)
                sec_calc = parse_calculation(scf)
                sec_calc.system_ref = sec_system
            parse_calculation(self.mainfile_parser.vibrations, sec_calc)
            # thermodynamics workflow
            thermo_data = self.mainfile_parser.vibrations.thermodynamic_quantities_steps
            if thermo_data is not None:
                sec_workflow = archive.m_create(Workflow)
                sec_workflow.type = 'thermodynamics'
                sec_thermodynamics = sec_workflow.m_create(Thermodynamics)
                thermo_data = np.transpose(thermo_data)
                sec_thermodynamics.temperature = thermo_data[1]
                # calorie is not a ureg unit
                sec_thermodynamics.entropy = thermo_data[2] * ureg.J * 4.184 / ureg.K / MOL
                sec_thermodynamics.heat_capacity_c_p = thermo_data[3] * ureg.J * 4.184 / ureg.K / MOL
                sec_thermodynamics.enthalpy = thermo_data[4] * ureg.J * 4184.0 / MOL
                sec_thermodynamics.gibbs_free_energy = thermo_data[5] * ureg.J * 4184.0 / MOL
                workflow.results.temperature = thermo_data[1]
                workflow.results.entropy = thermo_data[2] * ureg.J * 4.184 / ureg.K / MOL
                workflow.results.heat_capacity_c_p = thermo_data[3] * ureg.J * 4.184 / ureg.K / MOL
                workflow.results.enthalpy = thermo_data[4] * ureg.J * 4184.0 / MOL
                workflow.results.gibbs_free_energy = thermo_data[5] * ureg.J * 4184.0 / MOL
