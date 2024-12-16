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
import numpy as np
import logging
from datetime import datetime
from ase.data import chemical_symbols

from nomad.units import ureg
from nomad.parsing.file_parser.text_parser import TextParser, Quantity, FileParser
from runschema.run import Run, Program, TimeRun
from runschema.method import (
    Method,
    DFT,
    XCFunctional,
    Functional,
    Electronic,
    BasisSet,
    Scf,
    AtomParameters,
    KMesh,
    BasisSetContainer,
    BasisSetAtomCentered,
)
from runschema.system import System, Atoms
from runschema.calculation import (
    Calculation,
    ScfIteration,
    Dos,
    DosValues,
    Energy,
    EnergyEntry,
    Forces,
    ForcesEntry,
    Charges,
    ChargesValue,
    Multipoles,
    MultipolesEntry,
    BandEnergies,
    BandGapDeprecated,
    BandGap,
)
from simulationworkflowschema import (
    GeometryOptimization,
    GeometryOptimizationMethod,
    MolecularDynamics,
)
from .metainfo import ams as ams_metainfo  # pylint: disable=unused-import
from electronicparsers.utils import get_files
from .rkf import rkf_to_dict


re_float = r'[-+]?\d+\.\d*(?:[Ee][-+]\d+)?'
re_n = r'[\n\r]'


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_labels_positions(val_in):
            val = [v.split() for v in val_in.strip().splitlines()]
            unit = val.pop(0)[0].lower()
            unit = ureg.bohr if unit.startswith('bohr') else ureg.angstrom
            val = np.transpose(val)
            return val[1], np.array(val[2:5].T, dtype=np.dtype(np.float64)) * unit

        def str_to_lattice_vectors(val_in):
            val = [v.split()[-3:] for v in val_in.strip().splitlines()]
            unit = val.pop(0)[0].lower()
            unit = ureg.bohr if unit.startswith('bohr') else ureg.angstrom
            return np.array(val, dtype=np.dtype(np.float64)) * unit

        def str_to_forces(val_in):
            val = [v.split()[2:5] for v in val_in.strip().splitlines()]
            return np.array(val, dtype=np.dtype(np.float64)) * ureg.hartree / ureg.bohr

        def to_parameters(val_in):
            lines = [v.strip().rsplit(' ', 1) for v in val_in.strip().splitlines()]
            return {
                line[0].strip(): line[1].strip() for line in lines if len(line) == 2
            }

        def to_run_config(val_in):
            lines = [v.strip().split('.  ') for v in val_in.strip().splitlines()]
            return {line[0].strip(): line[-1] == 'T' for line in lines}

        def to_mulliken_populations(val_in):
            lines = [v.strip().split() for v in val_in.strip().splitlines()]
            orbitals = np.transpose([line[0].split('/') for line in lines])
            return (
                orbitals[0],
                orbitals[1],
                orbitals[3],
                np.array([line[1:] for line in lines], np.float64),
            )

        def to_band_energy_ranges(val_in):
            columns = np.array(
                [v.strip().split() for v in val_in.strip().splitlines()], np.float64
            ).T[1:]
            nspin = len(columns) // 3
            emin = [columns[n * 3 + 0] for n in range(nspin)]
            emax = [columns[n * 3 + 1] for n in range(nspin)]
            occs = [[columns[n * 3 + 2]] for n in range(nspin)]
            return emin, emax, occs

        system_quantities = [
            Quantity(
                'labels_positions',
                rf'Index Symbol\s*x\s*\((.+?)\).+(\s+)'
                rf'((?:\d+ + [A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                convert=False,
                str_operation=str_to_labels_positions,
            ),
            Quantity(
                'lattice_vectors',
                r'Lattice vectors \((.+?)\)(\s+)'
                rf'((?:\d+  +{re_float} +{re_float} +{re_float}\s+)+)',
                convert=False,
                str_operation=str_to_lattice_vectors,
            ),
        ]

        method_quantities = [
            Quantity(
                'band_engine_input',
                r'Band Engine Input\s*\-+\s*([\s\S]+?)\n *\n',
                sub_parser=TextParser(
                    quantities=[Quantity('basis', r' Basis\s*Type\s*(.+)')]
                ),
            ),
            Quantity(
                'model_parameters',
                r'M O D E L   P A R A M E T E R S\s*\=+([\s\S]+?)\={10}',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'dft_potential',
                            r'FUNCTIONAL POTENTIAL \(scf\)([\s\S]+?)DENSITY',
                            sub_parser=TextParser(
                                quantities=[
                                    Quantity('LDA', r'LDA\:\s*([\w ]+)', flatten=False),
                                    Quantity(
                                        'GGA',
                                        r'Gradient Corrections\:\s*([\w ]+)',
                                        flatten=False,
                                    ),
                                    Quantity(
                                        'MGGA', r'Meta-GGA\:\s*([\w ]+)', flatten=False
                                    ),
                                ]
                            ),
                        ),
                        Quantity(
                            'spin', r'(UNrestricted)', str_operation=lambda x: True
                        ),
                        Quantity(
                            'relativistic_corrections',
                            r'Relativistic Corrections\:\s*(.+?)  ',
                            dtype=str,
                            flatten=False,
                        ),
                        Quantity(
                            'x_ams_nuclear_charge_density_model',
                            rf'Nuclear Charge Density Model\:\s*(.+?){re_n}',
                            str_operation=lambda x: x.strip(),
                            dtype=str,
                            flatten=False,
                        ),
                    ]
                ),
            ),
            Quantity(
                'confinement',
                r'C O N F I N E M E N T\s+\=+\s+([\s\S]+?)\={10}',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'x_ams_basis_functions_confinement_radius',
                            rf'Basis functions confinement radius\s+({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'x_ams_basis_functions_confinement_width',
                            rf'Width\s+({re_float})',
                            dtype=np.float64,
                        ),
                    ]
                ),
            ),
            Quantity(
                'radial_functions',
                r'(T Y P E +\d+\s+\-+[\s\S]+?NR\. OF RADIAL FIT FUNCTIONS.+)',
                repeats=True,
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'x_ams_radial_points',
                            r'RADIAL POINTS\s+(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity('label', r'\*\*> +(\w+) +<\*\*', dtype=str),
                        Quantity(
                            'x_ams_nuclear_charge',
                            rf'NUCLEAR CHARGE\s+({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'n_valence_electrons',
                            rf'VALENCE CHARGE\s+({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'charge', rf'NET CHARGE\s+({re_float})', dtype=np.float64
                        ),
                        Quantity(
                            'orbital_parameters',
                            rf'Orbital +Q.+\s*\-+\s+((?:\d+\w+ +{re_float}.+\s+)+)',
                            str_operation=lambda x: np.transpose(
                                [v.strip().split() for v in x.strip().splitlines()]
                            ),
                        ),
                        Quantity(
                            'x_ams_energy_sum_eigenvalues',
                            rf'Sum \(energy eigenvalues\)\s+({re_float})',
                            dtype=np.float64,
                            unit=ureg.hartree,
                        ),
                        Quantity(
                            'x_ams_energy_total_lda',
                            rf'Total energy LDA\s+({re_float})',
                            dtype=np.float64,
                            unit=ureg.hartree,
                        ),
                        Quantity(
                            'x_ams_energy_kinetic',
                            rf'Kinetic energy\s+({re_float})',
                            dtype=np.float64,
                            unit=ureg.hartree,
                        ),
                        Quantity(
                            'x_ams_energy_classical_electron_electron_repulsion',
                            rf'Classical e\-e repulsion\s+({re_float})',
                            dtype=np.float64,
                            unit=ureg.hartree,
                        ),
                        Quantity(
                            'x_ams_energy_electron_nucleus_repulsion',
                            rf'Classical e\-e repulsion\s+({re_float})',
                            dtype=np.float64,
                            unit=ureg.hartree,
                        ),
                        Quantity(
                            'x_ams_n_radial_valence_orbitals',
                            r'NR\. OF RADIAL VALENCE ORBITALS\s+(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'x_ams_n_radial_core_orbitals',
                            r'NR\. OF RADIAL CORE ORBITALS\s+(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'x_ams_n_radial_fit_functions',
                            r'NR\. OF RADIAL FIT FUNCTIONS\s+(\d+)',
                            dtype=np.int32,
                        ),
                    ]
                ),
            ),
            Quantity(
                'ranges_atomic_orbitals',
                r'R A N G E S    F O R    A T O M I C    O R B I T A L S\s+\=+([\s\S]+?)\={10}',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'type',
                            rf'Type +valence.+\s+\-+\s+((?:\w+ +{re_float}.+\s+)+)',
                            str_operation=lambda x: [
                                v.strip().split() for v in x.strip().splitlines()
                            ],
                        ),
                        Quantity(
                            'cutoff',
                            rf'Cutoff +({re_float}.+)',
                            dtype=np.dtype(np.float64),
                        ),
                    ]
                ),
            ),
            Quantity(
                'x_ams_run_config',
                r'R U N    C O N F I G\s+\=+\s+((?:\w.+\s+)+)',
                str_operation=to_run_config,
            ),
            Quantity(
                'k_space_sampling',
                r'(?:K \- S P A C E   S A M P L I N G|K\-space integration)([\s\S]+?)\={5}',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'x_ams_general_integration_parameter',
                            r'General integration parameter\s+(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'x_ams_bz_volume_total',
                            rf'Total volume\s+({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'x_ams_bz_volume_irreducible',
                            rf'Irreducible.+\s+({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'x_ams_bz_volume_numerical_integration',
                            rf'Numerical integration\s+({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity('n_points', r'Total nr\. of K\-points\s+(\d+)'),
                        Quantity(
                            'x_ams_n_points_unique',
                            r'Nr\. of symmetry unique points\s+(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'x_ams_n_simplices',
                            r'Nr\. of simplices\s+(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'x_ams_n_points_per_simplex',
                            r'Nr\. of points per simplex\s+(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'points',
                            rf'No\. +Sym\..+\s+\-+((?:\d+ +\d+ +{re_float}.+\s+)+)',
                            str_operation=lambda x: np.transpose(
                                np.array(
                                    [v.split() for v in x.strip().splitlines()],
                                    np.float64,
                                )
                            )[2:5].T,
                        ),
                    ]
                ),
            ),
            Quantity(
                'scf_options',
                r'S\. C\. F\.   O P T I O N S([\s\S]+?)\*\*',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'x_ams_diis_settings_dirac',
                            r'DIIS settings info for DIRAC +\*\s+((?:[\w ]+?  \w\S*\s+)+)',
                            str_operation=to_parameters,
                        ),
                        Quantity(
                            'x_ams_diis_settings_scf',
                            r'DIIS settings info for SCF +\*\s+((?:[\w ]+?  \w\S*\s+)+)',
                            str_operation=to_parameters,
                        ),
                        Quantity(
                            'x_ams_growth_factor',
                            rf'growth factor\s*({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'x_ams_shrink_factor',
                            rf'shrink factor\s*({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity('x_ams_mix', rf'Mix\s*({re_float})', dtype=np.float64),
                        Quantity(
                            'x_ams_degenerate',
                            r'Degenerate\s*(.)',
                            str_operation=lambda x: x == 'T',
                        ),
                        Quantity(
                            'x_ams_edegen', rf'Edegen\s*({re_float})', dtype=np.float64
                        ),
                        Quantity(
                            'x_ams_scfrtx', rf'SCFRTX\s*({re_float})', dtype=np.float64
                        ),
                        Quantity(
                            'x_ams_convrg', rf'Convrg\s*({re_float})', dtype=np.float64
                        ),
                        Quantity('x_ams_ncyclx', r'Ncyclx\s*(\d+)', dtype=np.int32),
                        Quantity(
                            'x_ams_vsplit', rf'Vsplit\s*({re_float})', dtype=np.float64
                        ),
                    ]
                ),
            ),
            Quantity(
                'x_ams_dftb_resources_dir',
                r'DFTB Resources dir\s*(.+)',
                dtype=str,
                flatten=False,
            ),
            Quantity(
                'x_ams_scc_convergence_enabled',
                r'SCC convergence (\w+)',
                str_operation=lambda x: x == 'enabled',
            ),
            Quantity(
                'x_ams_max_scc_cycles', r'Maximum SCC cycles \ſ*(\d+)', dtype=np.int32
            ),
            Quantity(
                'x_ams_scc_charge_convergence',
                rf'SCC charge convergence\s*({re_float})',
                dtype=np.float64,
            ),
            Quantity(
                'x_ams_scc_charge_mixing',
                rf'SCC charge mixing\s*({re_float})',
                dtype=np.float64,
            ),
            Quantity(
                'x_ams_diis_max_dimension',
                r'DIIS max dimension\s*(\d+)',
                dtype=np.int32,
            ),
            Quantity(
                'x_ams_diis_max_coeff',
                rf'DIIS maximum coeff\.\s*({re_float})',
                dtype=np.float64,
            ),
            Quantity(
                'x_ams_adaptive_scc_charge_mixing',
                r'Adaptive SCC charge mixing\s*(.)',
                str_operation=lambda x: x == 'T',
            ),
            Quantity(
                'x_ams_adaptive_scc_mixing_strategy',
                r'Adaptive SCC mixing strategy\s*(\d+)',
                dtype=np.int32,
            ),
            Quantity(
                'x_ams_spin_polarization',
                r'Spin polarization\s*(.)',
                str_operation=lambda x: x == 'T',
            ),
            Quantity(
                'x_ams_orbital_dependent_scc',
                r'Orbital\-dependent SCC\s*(.)',
                str_operation=lambda x: x == 'T',
            ),
            Quantity(
                'x_ams_orbital_fill_strategy',
                r'Orbital fill strategy\s*(.+)',
                dtype=str,
                flatten=False,
            ),
            Quantity(
                'x_ams_fermi_temperature',
                rf'Fermi temperature \(kelvin\)\s*({re_float})',
                dtype=np.float64,
                unit=ureg.kelvin,
            ),
            Quantity(
                'x_ams_use_symmetry',
                r'Use of symmetry\s*(.)',
                str_operation=lambda x: x == 'T',
            ),
            Quantity(
                'x_ams_radial_function_extrapolation_method',
                r'Radial function extrapolation method\s*(.+)',
                dtype=str,
                flatten=False,
            ),
            Quantity(
                'x_ams_grimme_d3_dispersion_correction',
                r'Settings for Grimme .+ dispersion correction\s+'
                r'((?:\w+ +\S+\s+)+)',
                str_operation=to_parameters,
            ),
            Quantity(
                'x_ams_other_parameters',
                r'Other \(technical\) parameters\s+' r'((?:\w+ +\S+\s+)+)',
                str_operation=to_parameters,
            ),
            Quantity(
                'x_ams_assume_insulator',
                r'Assume insulator\s*(.)',
                str_operation=lambda x: x == 'T',
            ),
            Quantity(
                'x_ams_ewald_tolerance',
                rf'Ewald tolerance\s*({re_float})',
                dtype=np.float64,
            ),
            Quantity(
                'x_ams_ewald_range_factor',
                rf'Ewald range factor\s*({re_float})',
                dtype=np.float64,
            ),
            Quantity(
                'x_ams_bzstruct_config',
                r'BZStruct config\s*\-+\s*((?:\w+ ))',
                str_operation=to_parameters,
            ),
        ]

        calculation_quantities = (
            system_quantities
            + method_quantities
            + [
                Quantity(
                    'total_charge',
                    rf'Total System Charge\s*({re_float})',
                    dtype=float,
                    unit=ureg.elementary_charge,
                ),
                Quantity(
                    'atomic_charges',
                    rf'Index +Atom +Charge\s+((?:\d+ +\w+ +{re_float}\s+)+)',
                    str_operation=lambda x: [
                        v.strip().split()[-1] for v in x.strip().splitlines()
                    ],
                ),
                Quantity(
                    'fermi_energy',
                    rf'Fermi Energy\:\s*({re_float})\s*a\.u\.',
                    dtype=float,
                    unit=ureg.hartree,
                ),
                Quantity(
                    'energies',
                    r'E N E R G Y   A N A L Y S I S([\s\S]+?)\={90}',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'electronic_kinetic',
                                rf'Kinetic\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'xc',
                                rf'XC\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'electrostatic',
                                rf'Electrostatic\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'x_ams_v_atomic_def',
                                rf'V\(atomic\)\*def\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'x_ams_v_def_def',
                                rf'V\(def\)\*def\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'x_ams_dispersion',
                                rf'Dispersion\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'total',
                                rf'Final bond energy \(.+\)\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'x_ams_fit_error_correction',
                                rf'Fit error correction.+?\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'energies',
                    r'(Energy Decomposition\s+\-+[\s\S]+?)\-{10}',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'total',
                                rf'Total Energy \(hartree\)\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'electronic',
                                rf'Electronic Energy \(hartree\)\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'electrostatic',
                                rf'Coulomb Energy \(hartree\)\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'nuclear_repulsion',
                                rf'Repulsion Energy \(hartree\)\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'x_ams_dispersion',
                                rf'Dispersion Energy \(hartree\)\s*({re_float})',
                                dtype=float,
                                unit=ureg.hartree,
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'forces',
                    rf'(E N E R G Y +G R A D I E N T S\s+\=+[\s\S]+?FINAL[\s\S]+?){re_n} *{re_n}',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'p_matrix',
                                rf'P Matrix\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'electronic_kinetic',
                                rf'Kinetic energy\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'xc',
                                rf'XC energy\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'electrostatic',
                                rf'Electrostatic energy\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'pair_interactions',
                                rf'Pair interactions\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'dispersion',
                                rf'Dispersion\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'total',
                                rf'FINAL GRADIENTS\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'forces',
                    r'Gradient Decomposition\s+\-+([\s\S]+?)\-{10}',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'total',
                                rf'Total Gradients \(hartree/bohr\)\s+Index.+\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'electronic',
                                rf'Electronic Gradients \(hartree/bohr\)\s+Index.+\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'electrostatic',
                                rf'Coulomb Gradients \(hartree/bohr\)\s+Index.+\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'nuclear_repulsion',
                                rf'Repulsion Gradients \(hartree/bohr\)\s+Index.+\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                            Quantity(
                                'dispersion',
                                rf'Dispersion Gradients \(hartree/bohr\)\s+Index.+\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                                str_operation=str_to_forces,
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'energy_total',
                    rf'Energy\s*\(hartree\)\s*({re_float})',
                    dtype=float,
                    unit=ureg.hartree,
                ),
                Quantity(
                    'energy_total',
                    rf'current energy +({re_float}) +Hartree',
                    dtype=float,
                    unit=ureg.hartree,
                ),
                Quantity(
                    'forces_total',
                    rf'Gradients \(hartree/bohr\)\s+Index.+\s+((?:\d+ +[A-Z][a-z]* +{re_float} +{re_float} +{re_float}\s+)+)',
                    str_operation=str_to_forces,
                ),
                Quantity(
                    'self_consistency',
                    r'S C F   P R O C E D U R E\s*\*\s*\*+\s*([\s\S]+?Self consistent error.+)',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'energy_change',
                                rf'cyc\=\s*\d+\s*err\=\s*({re_float})',
                                repeats=True,
                                dtype=float,
                                unit=ureg.hartree,
                            )
                        ]
                    ),
                ),
                Quantity(
                    'total_dos',
                    r'TOTALDOS([\s\S]+?)ENDINPUT',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'nspin_ne',
                                r'NSPIN,NE= *(\d+) +(\d+)',
                                dtype=np.dtype(np.int32),
                            ),
                            Quantity(
                                'dos',
                                rf'\n *({re_float}) *({re_float}) *({re_float})*',
                                dtype=np.dtype(np.float64),
                                repeats=True,
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'mulliken_populations',
                    r'M U L L I K E N   P O P U L A T I O N S\s+\=+([\s\S]+?)\={10}',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'orbital',
                                rf'(\d+/[A-Z].+?{re_float}[\s\S]+?)\-\-',
                                repeats=True,
                                str_operation=to_mulliken_populations,
                            ),
                            Quantity(
                                'atom',
                                rf'Charge on atom\s+({re_float}.+)',
                                repeats=True,
                                str_operation=lambda x: x.strip().split(),
                                dtype=np.dtype(np.float64),
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'mulliken_populations',
                    rf'(Mulliken Charges\s+\-+[\s\S]+?Total.+)',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'atom',
                                rf'Index +Atom +Charge.+\s+((?:\d+ +\w+ +{re_float} +{re_float}\s+)+)',
                                # shape should be (nspin, natoms)
                                str_operation=lambda x: np.array(
                                    [
                                        v.strip().split()[2:3]
                                        for v in x.strip().splitlines()
                                    ],
                                    np.float64,
                                ),
                                convert=False,
                            ),
                            Quantity(
                                'total',
                                rf'Total\s+({re_float})',
                                dtype=np.float64,
                                unit=ureg.elementary_charge,
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'atom_charge_analysis',
                    r'(Atomic Charge Analysis.*\s*\=+[\s\S]+?)\={10}',
                    repeats=True,
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'spin',
                                r'(Spin Up \- Spin Down)',
                                str_operation=lambda x: True,
                            ),
                            Quantity(
                                'methods',
                                r'Atom +([\w ]+)',
                            ),
                            Quantity(
                                'atom_charges',
                                rf'((?:\d+ +\w+ +{re_float}.+\s+)+)',
                                str_operation=lambda x: np.transpose(
                                    [v.strip().split() for v in x.strip().splitlines()]
                                )[2:],
                                dtype=np.dtype(np.float64),
                            ),
                            Quantity(
                                'total',
                                rf'Total: +({re_float}.+)',
                                dtype=np.dtype(np.float64),
                            ),
                        ]
                    ),
                ),
                Quantity(
                    'dipole_moment',
                    rf'direction +dipole.+\s+\=+\s+((?:\w+ +{re_float}.+\s+)+)',
                    str_operation=lambda x: (
                        [float(v.strip().split()[2]) for v in x.strip().splitlines()]
                        * ureg.debye
                    )
                    .to('C * m')
                    .magnitude,
                ),
                Quantity(
                    'band_energy_ranges',
                    rf'\=+\s+band +min.+\s+\=+\s+((?:\d+ +{re_float}.+\s+)+)',
                    str_operation=to_band_energy_ranges,
                ),
                Quantity(
                    'band_gap_info',
                    rf'Band gap information\s+\-([\s\S]+?){re_n} *{re_n}',
                    sub_parser=TextParser(
                        quantities=[
                            Quantity(
                                'x_ams_n_valence_electrons',
                                r'Number of valence electrons\s+(\d+)',
                                dtype=np.int32,
                            ),
                            Quantity(
                                'x_ams_valence_band_index',
                                r'Valence band index\s+(\d+)',
                                dtype=np.int32,
                            ),
                            Quantity(
                                'x_ams_valence_band_spin_index',
                                r'Valence band spin index\s+(\d+)',
                                dtype=np.int32,
                            ),
                            Quantity(
                                'x_ams_conduction_band_index',
                                r'Conduction band index\s+(\d+)',
                                dtype=np.int32,
                            ),
                            Quantity(
                                'x_ams_conduction_band_spin_index',
                                r'Conduction band spin index\s+(\d+)',
                                dtype=np.int32,
                            ),
                            Quantity(
                                'energy_highest_occupied',
                                rf'Top of valence band \(a\.u\.\)\s+({re_float})',
                                dtype=np.float64,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'energy_lowest_unoccupied',
                                rf'Bottom of conduction band \(a\.u\.\)\s+({re_float})',
                                dtype=np.float64,
                                unit=ureg.hartree,
                            ),
                            Quantity(
                                'value',
                                rf'Band gap \(a\.u\.\)\s+({re_float})',
                                dtype=np.float64,
                                unit=ureg.hartree,
                            ),
                        ]
                    ),
                ),
            ]
        )

        self._quantities = [
            Quantity(
                'program_version', r'\*\s*r(\d+ \d{4}\-\d\d\-\d\d)', flatten=False
            ),
            Quantity(
                'time_start',
                r'RunTime\:\s*(\w{3}\d+\-\d{4}\s*\d+\:\d+\:\d+)',
                str_operation=lambda x: (
                    datetime.strptime(x, '%b%d-%Y %H:%M:%S') - datetime(1970, 1, 1)
                ).total_seconds(),
            ),
            Quantity(
                'single_point',
                r'SINGLE POINT CALCULATION \*([\s\S]+?)(:?Timing|\Z)',
                sub_parser=TextParser(quantities=calculation_quantities),
            ),
            Quantity(
                'geometry_optimization',
                r'GEOMETRY OPTIMIZATION\s*\*([\s\S]+?)(:?Timing|Performing a single pooint|\Z)',
                sub_parser=TextParser(
                    quantities=system_quantities
                    + method_quantities
                    + [
                        Quantity(
                            'step',
                            r'Geometry Convergence after Step\s*([\s\S]+?(?:dE\(predicted\)\:.+|\Z))',
                            repeats=True,
                            sub_parser=TextParser(quantities=calculation_quantities),
                        ),
                        Quantity(
                            'method', r'Optimization Method\s*(.+)', flatten=False
                        ),
                        Quantity(
                            'x_ams_optimization_coordinates',
                            r'Optimization Coordinates +(.+)',
                            type=str,
                            flatten=False,
                        ),
                        Quantity(
                            'x_ams_optimize_lattice',
                            r'Optimize lattice +(.)',
                            str_operation=lambda x: x == 'T',
                        ),
                        Quantity(
                            'convergence_tolerance_force_maximum',
                            rf'Maximum gradient\s*({re_float})',
                            dtype=float,
                            unit=ureg.hartree / ureg.bohr,
                        ),
                        Quantity(
                            'x_ams_maximum_rms_gradient',
                            rf'Maximum rms gradient\s*({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'convergence_tolerance_energy_difference',
                            rf'Maximum energy change allowe\s*({re_float})',
                            dtype=float,
                            unit=ureg.hartree,
                        ),
                        Quantity(
                            'convergence_tolerance_displacement_maximum',
                            rf'Maximum step allowed\s*({re_float})',
                            dtype=float,
                            unit=ureg.bohr,
                        ),
                        Quantity(
                            'x_ams_maximum_rms_step_allowed',
                            rf'Maximum rms step allowed\s*({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'x_ams_maximum_stress_energy_allowed',
                            rf'Maximum stress energy allowe\s*({re_float})',
                            dtype=np.float64,
                        ),
                        Quantity(
                            'x_ams_initial_model_hessian',
                            r'Initial model Hessian\s*(.+)',
                            dtype=str,
                            flatten=False,
                        ),
                        Quantity(
                            'x_ams_hessian_update_method',
                            r'Hessian Update Method\s*(.+)',
                            dtype=str,
                            flatten=False,
                        ),
                        Quantity(
                            'optimization_steps_maximum',
                            r'Maximum number of steps\s*(\d+)',
                        ),
                        Quantity(
                            'x_ams_first_gdiis_cycle',
                            r'First GDIIS cycle\s*(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'x_ams_maximum_gdiis_vectors',
                            r'Maximum GDIIS vectors\s*(\d+)',
                            dtype=np.int32,
                        ),
                        Quantity(
                            'x_ams_trust_radius',
                            rf'Trust radius \(bohr\)\s*({re_float})',
                            dtype=np.float64,
                            unit=ureg.bohr,
                        ),
                        Quantity(
                            'x_ams_trust_radius_varies',
                            r'Trust radius varies\s*(.)',
                            str_operation=lambda x: x == 'T',
                        ),
                        Quantity(
                            'x_ams_constraints_converged_at_all_steps',
                            r'Constraints converged at all steps\s*(.)',
                            str_operation=lambda x: x == 'T',
                        ),
                        Quantity(
                            'x_ams_use_projector',
                            r'Use projector\s*(.)',
                            str_operation=lambda x: x == 'T',
                        ),
                        Quantity(
                            'x_ams_symmetrize_steps',
                            r'Symmetrize steps\s*(.)',
                            str_operation=lambda x: x == 'T',
                        ),
                    ]
                ),
            ),
            Quantity(
                'calculation_results',
                r'(CALCULATION RESULTS[\s\S]+?)(?:finished|\Z)',
                sub_parser=TextParser(quantities=calculation_quantities + []),
            ),
            # TODO add other calculation types
        ]


class RKFParser(FileParser):
    def __init__(self, mainfile=None, logger=None, open=None):
        super().__init__(mainfile, logger, open)
        self._energies_map = {
            'Bond Energy': 'x_ams_bond',
            'Corr. due to Orthogonalization': 'x_ams_orthogonalization',
            'Dispersion Energy': 'x_ams_dispersion',
            'Ebond due to Efield': 'x_ams_bond_efield',
            'Electrostatic Energy': 'electrostatic',
            'Kinetic Energy': 'kinetic',
            'MP2 energy': 'x_ams_mp2',
            'Orb.Int. A': 'x_ams_orbital_interaction_a',
            'Orb.Int. Efield': 'x_ams_orbital_interaction_efield',
            'Orb.Int. FitCorrection': 'x_ams_orbital_interaction_fit_correction',
            'Orb.Int. TSCorrection (LDA)': 'x_ams_orbital_interaction_ts_correction_lda',
            'Orb.Int. TSCorrection (NL)': 'x_ams_orbital_interaction_ts_correction_nl',
            'Orb.Int. Total': 'x_ams_orbital_interaction',
            'Pauli Coulomb': 'x_ams_pauli_coulomb',
            'Pauli Efield': 'x_ams_pauli_efield',
            'Pauli FitCorrection': 'x_ams_pauli_fit_correction',
            'Pauli Kinetic': 'x_ams_pauli_kinetic',
            'Pauli Kinetic+Coulomb': 'x_ams_pauli_kinetic_coulomb',
            'Pauli TS Correction (LDA)': 'x_ams_pauli_ts_correction_lda',
            'Pauli Total': 'x_ams_pauli',
            'RPA energy': 'x_ams_rpa',
            'SCF Bond Energy': 'x_ams_bond',
            'SumFragmentsSCF FitCorrection': 'x_ams_sum_fragments_scf_fit_correction',
            'XC Energy': 'xc',
            # 'XC energies': 'xc_values_per_atom'
        }
        # TODO verfiy list
        self._ldapot = {1: 'VWN', 2: 'Stoll', 3: 'PW92'}

    @property
    def data(self):
        if self._file_handler is None:
            try:
                self._file_handler = rkf_to_dict(self.mainfile)
            except Exception:
                self.logger.error('Error reading rkf file')
        return self._file_handler

    def parse(self, key=None):
        if self.data is None:
            return

        if self._results is None:
            self._results = {}

        general = self.data.get('General', {})
        # TODO determine if program version is same as release, formatting required
        # for compatibility with text output
        self._results['program_version'] = (
            general.get('release', '').replace('(', '').replace(')', '').split('r')[-1]
        )
        self._results['program_x_ams_name'] = general.get('program')
        self._results['program_x_ams_engine'] = general.get('engine')

        nspin = general.get('nspin', 1)
        xc_functional = {}
        if (ldapot := general.get('ldapot')) is not None:
            xc_functional['LDA'] = self._ldapot.get(ldapot, '')
        if ggapot := general.get('ggapot', '').strip():
            xc_functional['GGA'] = ggapot
        if mgga := general.get('MetaGGAConfig', {}).get('metagga', '').strip():
            xc_functional['MGGA'] = mgga
        # TODO parse hybrid, hf
        self._results['model_parameters'] = {
            'spin': nspin > 1,
            'dft_potential': xc_functional,
        }

        k_space_sampling = {}
        if (kspace := self.data.get('kspace')) is not None:
            k_space_sampling['x_ams_n_simplices'] = kspace.get('nsimpl')
            k_space_sampling['x_ams_n_points_unique'] = kspace.get('kuniqu')
            self._results['k_space_sampling'] = k_space_sampling

        if (kpoints_config := self.data.get('KPointsConfig')) is not None:
            k_space_sampling['x_ams_general_integration_parameter'] = (
                kpoints_config.get('interpolation')
            )
            k_space_sampling['grid'] = kpoints_config.get('parameters')

        engine_results = self.data.get('EngineResults', {})

        files = [val for key, val in engine_results.items() if key.startswith('Files')]
        warning = None
        for n, name in enumerate(files):
            rkf_files = get_files(name, self.mainfile)
            if not rkf_files:
                warning = 'rkf file not found in directory.'
                files[n] = None
                continue
            if len(rkf_files) > 1:
                warning = 'Multiple rkf files found in directory'
            files[n] = rkf_files[0]
        if warning:
            self.logger.warning(warning)

        labels = []
        if (molecule := self.data.get('Molecule')) is not None:
            labels = [chemical_symbols[n] for n in molecule.get('AtomicNumbers', [])]
            if not labels:
                labels = molecule.get('AtomSmbols').split()
            positions = molecule.get('Coords', [])
            try:
                positions = np.reshape(positions, (len(labels), 3)) * ureg.bohr
            except Exception:
                self.logger.warning('Cannot read atom positions.')
            self._results['labels_positions'] = [labels, positions]
            if (lattice_vectors := molecule.get('LatticeVectors')) is not None:
                self._results['lattice_vectors'] = (
                    np.reshape(lattice_vectors, (3, 3)) * ureg.bohr
                )

        calc_type = None
        calc_results = {}

        if (amsresults := self.data.get('AMSResults')) is not None:
            if (charges := amsresults.get('Charges')) is not None:
                self._results['atomic_charges'] = amsresults.get('Charges')
            if (dipole := amsresults.get('DipoleMoment')) is not None:
                dipole = np.sqrt(np.sum(np.array(dipole) ** 2))
                self._results['dipole_moment'] = (
                    ([dipole] * ureg.elementary_charge * ureg.bohr)
                    .to('C * m')
                    .magnitude
                )
            if (energy := amsresults.get('Energy')) is not None:
                self._results['energy_total'] = energy * ureg.hartree
            if (gradients := amsresults.get('Gradients')) is not None:
                self._results['forces_total'] = (
                    np.reshape(gradients, (len(labels), 3)) * ureg.hartree / ureg.bohr
                )
            if (hessian := amsresults.get('Hessian')) is not None:
                hessian = np.reshape(hessian, (len(labels), 3, len(labels), 3))
                self._results['hessian_matrix'] = (
                    (
                        np.transpose(hessian, axes=(0, 2, 1, 3))
                        * ureg.hartree
                        / ureg.bohr**2
                    )
                    .to('J / m ** 2')
                    .magnitude
                )

        if (history := self.data.get('History')) is not None:
            calc_type = 'geometry_optimization'
            n_entries = history.get('nEntries', 0)
            calc_results['step'] = [None] * n_entries
            for n in range(n_entries):
                positions = history.get(f'Coords({n + 1})')
                if positions is not None:
                    positions = np.reshape(positions, (len(labels), 3)) * ureg.bohr
                calc_results['step'][n] = {'labels_positions': [labels, positions]}
                if (energy_total := history.get(f'Energy({n + 1})')) is not None:
                    calc_results['step'][n]['energy_total'] = (
                        energy_total * ureg.hartree
                    )

        if (mdhistory := self.data.get('MDHistory')) is not None:
            calc_type = 'molecular_dynamics'
            n_entries = mdhistory.get('nEntries', 0)
            if len(calc_results.get('step', [])) != n_entries:
                self.logger.warning('Inconsistent number of entries in history.')
            else:
                block_size = mdhistory.get('blockSize', 1)
                for n in range(n_entries):
                    calc_results['step'][n]['atomic_charges'] = mdhistory.get(
                        f'Charges({n + 1})'
                    )
                    energies = {}
                    nblock = (n // block_size) + 1
                    ndata = n % block_size
                    if (total := mdhistory.get(f'TotalEnergy({nblock})')) is not None:
                        energies['total'] = (
                            total if isinstance(total, float) else total[ndata]
                        ) * ureg.hartree
                    if (
                        kinetic := mdhistory.get(f'KineticEnergy({nblock})')
                    ) is not None:
                        energies['total_kinetic'] = (
                            kinetic if isinstance(kinetic, float) else kinetic[ndata]
                        ) * ureg.hartree
                    if (
                        potential := mdhistory.get(f'PotentialEnergy({nblock})')
                    ) is not None:
                        energies['total_potential'] = (
                            potential
                            if isinstance(potential, float)
                            else potential[ndata]
                        ) * ureg.hartree
                    calc_results['step'][n]['energies'] = energies
                    if (step := mdhistory.get(f'Step({nblock})')) is not None:
                        calc_results['step'][n]['step'] = (
                            step if isinstance(step, int) else step[ndata]
                        )
                    if (time := mdhistory.get(f'Time({nblock})')) is not None:
                        calc_results['step'][n]['time'] = (
                            time if isinstance(time, float) else time[ndata]
                        ) * ureg.fs
                    if (
                        temperature := mdhistory.get(f'Temperature({nblock})')
                    ) is not None:
                        calc_results['step'][n]['temperature'] = (
                            temperature
                            if isinstance(temperature, float)
                            else temperature[ndata]
                        ) * ureg.kelvin
                    if (
                        velocities := mdhistory.get(f'Velocities({n + 1})')
                    ) is not None:
                        calc_results['step'][n]['velocities'] = (
                            np.reshape(velocities, (len(labels), 3))
                            * ureg.bohr
                            / ureg.fs
                        )

        if history is None and files:
            if len(files) != 1:
                self.logger.warning('Inconsistent number of rkf files found.')
            calc_type = 'single_point'
            calc_results = RKFParser(mainfile=files[0] if files else None).parse()

        elif history:
            # pass
            if len(files) == 1:
                calc_results['step'][-1] = RKFParser(mainfile=files[0]).parse()
            elif len(files) == n_entries:
                for n, name in enumerate(files):
                    calc_results['step'][n] = RKFParser(mainfile=name).parse()
            else:
                self.logger.warning('Inconsistent number of rkf files found.')

        if calc_type is not None:
            self._results[calc_type] = calc_results

        if (energy := self.data.get('Energy')) is not None:
            self._results['energies'] = {}
            for ams_key, nomad_key in self._energies_map.items():
                val = energy.get(ams_key)
                if val is not None:
                    self._results['energies'][nomad_key] = val * ureg.hartree

        if (geometry := self.data.get('geometry')) is not None:
            if (lattice_vectors := geometry.get('standard_lattice')) is not None:
                self._results['lattice_vectors'] = (
                    np.reshape(lattice_vectors, (3, 3)) * ureg.bohr
                )

        if (properties := self.data.get('Properties')) is not None:
            if (mulliken := properties.get('AtomCharge Mulliken')) is not None:
                self._results['mulliken_populations'] = {
                    'atom': np.reshape(mulliken, (len(mulliken) // nspin, nspin))
                }

            if (fermi := properties.get('FermiLevel')) is not None:
                self._results['fermi_energy'] = fermi * ureg.hartree

            if (dipole := properties.get('Dipole')) is not None:
                dipole = np.sqrt(np.sum(np.array(dipole) ** 2))
                self._results['dipole_moment'] = (
                    ([dipole] * ureg.elementary_charge * ureg.bohr)
                    .to('C * m')
                    .magnitude
                )

                self._results['atomic_charges'] = charges

            self._results['band_gap'] = {}
            if (homo := properties.get('HOMO')) is not None:
                self._results['band_gap']['energy_highest_occupied'] = (
                    homo * ureg.hartree
                )
            if (lumo := properties.get('LUMO')) is not None:
                self._results['band_gap']['energy_lowest_unoccupied'] = (
                    lumo * ureg.hartree
                )

            # TODO parse other quantities

        if (properties := self.data.get('Scalar Atomic Properties')) is not None:
            if (mulliken := properties.get('Mulliken Charges')) is not None:
                self._results['mulliken_populations'] = {
                    'atom': np.reshape(mulliken, (len(mulliken) // nspin, nspin))
                }

        if (dos := self.data.get('DOS')) is not None:
            if np.ndim(dos.get('Energies')) > 0:
                self._results['total_dos'] = {
                    'dos': np.transpose(
                        [
                            dos.get('Energies'),
                            *np.reshape(
                                dos.get('Total DOS', []),
                                (dos.get('nSpin', 0), dos.get('nEnergies', 0)),
                            ),
                        ]
                    )
                }

        eigensystem = self.data.get('eigensystem', {})
        if eigensystem is not None:
            eigenvalues = {}
            if (eigval := eigensystem.get('eigval')) is not None:
                nspin = eigensystem.get('nspin', 1)
                nband = eigensystem.get('nband', 0)
                # TODO check if shape is correct
                eigenvalues['energies'] = (
                    np.reshape(eigval, (nspin, len(eigval) // (nband * nspin), nband))
                    * ureg.hartree
                )
                occupations = eigensystem.get('occupationPerBandAndSpin')
                if occupations is not None:
                    # TODO check if occ shape is correct
                    eigenvalues['occupations'] = np.reshape(
                        occupations,
                        (nspin, np.size(occupations) // (nband * nspin), nband),
                    )
                self._results['eigenvalues'] = eigenvalues

        if (band_structure := self.data.get('BandStructure')) is not None:
            if (energy_ranges := band_structure.get('bandsEnergyRange')) is not None:
                # TODO check if shape is correct
                nband = band_structure.get('nBand')
                nspin = band_structure.get('nSpin')
                energy_ranges = np.transpose(
                    np.reshape(energy_ranges, (nband, nspin, 2))
                )
                occupations = self._results.get('eigenvalues', {}).get('occupations')
                self._results['band_energy_ranges'] = [*energy_ranges, occupations]
            band_gap = {}
            if (value := band_structure.get('BandGap')) is not None:
                band_gap['value'] = value * ureg.hartree
            if (top_valence_band := band_structure.get('TopValenceBand')) is not None:
                band_gap['energy_highest_occupied'] = top_valence_band * ureg.hartree
            if (
                bottom_conduction_band := band_structure.get('BottomConductionBand')
            ) is not None:
                band_gap['energy_lowest_unoccupied'] = (
                    bottom_conduction_band * ureg.hartree
                )
            self._results['band_gap'] = band_gap

        if (geoopt := self.data.get('GeoOpt')) is not None:
            if (gradients := geoopt.get('Gradients_CART')) is not None:
                self._results['forces_total'] = (
                    np.reshape(gradients, (len(labels), 3)) * ureg.hartree / ureg.bohr
                )
            if (hessian := geoopt.get('Hessian_CART')) is not None:
                hessian = np.reshape(hessian, (len(labels), 3, len(labels), 3))
                self._results['hessian_matrix'] = (
                    (
                        np.transpose(hessian, axes=(0, 2, 1, 3))
                        * ureg.hartree
                        / ureg.bohr**2
                    )
                    .to('J / m ** 2')
                    .magnitude
                )
        # TODO parse Themodynamics, Vibrations, phonons

        self.close()
        return self

    def keys(self):
        return self.results.keys()


class AMSParser:
    def __init__(self):
        self.out_parser = OutParser()
        self.rkf_parser = RKFParser()
        self._relativity_map = {
            'scalar (ZORA,APA)': 'scalar_relativistic_atomic_ZORA',
            '---': None,
        }

    def init_parser(self):
        self.out_parser.mainfile = self.mainfile
        self.out_parser.logger = self.logger
        self.rkf_parser.logger = self.logger
        self.parser = self.out_parser

    def parse_configurations(self):
        sec_run = self.archive.run[0]

        def parse_scc(source, target=None):
            sec_scc = Calculation()
            sec_run.calculation.append(sec_scc) if target is None else target

            # total energy
            sec_energy = Energy()
            sec_scc.energy = sec_energy
            if source.get('energy_total') is not None:
                sec_energy.total = EnergyEntry(value=source.get('energy_total'))

            # fermi energy
            sec_energy.fermi = source.get('fermi_energy')

            # energy contributions
            for key, val in source.get('energies', dict()).items():
                if key == 'electronic_kinetic':
                    sec_energy.electronic = EnergyEntry(kinetic=val)
                elif match := re.match(
                    r'(\w+)_((?:kinetic|potential|values_per_atom))', key
                ):
                    entry = getattr(sec_energy, match.group(1))
                    entry = entry if entry else EnergyEntry()
                    entry.m_set(entry.m_get_quantity_definition(match.group(2)), val)
                    sec_energy.m_add_sub_section(getattr(Energy, match.group(1)), entry)
                else:
                    entry = getattr(sec_energy, key)
                    entry = entry if entry else EnergyEntry()
                    entry.value = val
                    sec_energy.m_add_sub_section(getattr(Energy, key), entry)

            # forces
            sec_forces = Forces()
            sec_scc.forces = sec_forces
            if (forces := source.get('forces_total')) is not None:
                sec_forces.total = ForcesEntry(value=forces)
            for key, val in source.get('forces', dict()).items():
                key = key if key == 'total' else f'x_ams_{key}'
                sec_forces.m_add_sub_section(
                    getattr(Forces, key), ForcesEntry(value=val)
                )

            # md
            sec_scc.temperature = source.get('temperature')
            sec_scc.step = source.get('step')
            sec_scc.time = source.get('time')

            # self consistency
            for energy_change in source.get('self_consistency', {}).get(
                'energy_change', []
            ):
                sec_scf = ScfIteration()
                sec_scc.scf_iteration.append(sec_scf)
                sec_scf_energy = Energy()
                sec_scf.energy = sec_scf_energy
                sec_scf_energy.change = energy_change

            # dos
            total_dos = source.get('total_dos', {}).get('dos')
            if total_dos is not None:
                total_dos = np.transpose(total_dos)
                n_spin_channels = len(total_dos[1:])
                for spin in range(n_spin_channels):
                    sec_dos = Dos()
                    sec_scc.dos_electronic.append(sec_dos)
                    sec_dos.spin_channel = spin if n_spin_channels == 2 else None
                    sec_dos.energies = total_dos[0] * ureg.hartree
                    sec_dos_values = DosValues()
                    sec_dos.total.append(sec_dos_values)
                    sec_dos_values.value = total_dos[spin + 1] / ureg.hartree

            # atom charges
            if (charges := source.get('atomic_charges')) is not None:
                sec_charges = Charges()
                sec_scc.charges.append(sec_charges)
                sec_charges.value = charges * ureg.elementary_charge

            for analysis in source.get('atom_charge_analysis', []):
                for n, method in enumerate(analysis.get('methods', [])):
                    existing_sec_charges = [
                        sec for sec in sec_scc.charges if sec.analysis_method == method
                    ]
                    if existing_sec_charges:
                        sec_charges = existing_sec_charges[0]
                    else:
                        sec_charges = Charges()
                        sec_scc.charges.append(sec_charges)
                    sec_charges.analysis_method = method
                    if analysis.spin:
                        sec_charges.spins = analysis.atom_charges[n]
                    else:
                        sec_charges.total = analysis.total[n]
                        sec_charges.value = (
                            analysis.atom_charges[n] * ureg.elementary_charge
                        )

            # mulliken populations
            mulliken = source.get('mulliken_populations')
            if mulliken is not None:
                sec_charges = Charges()
                sec_scc.charges.append(sec_charges)
                sec_charges.analysis_method = 'Mulliken'
                # atom/spin resolved
                atom_charges = np.array(mulliken.get('atom', []))
                spin = len(atom_charges.T)
                if spin == 2:
                    for natom, charges in enumerate(atom_charges):
                        for nspin, charge in enumerate(charges):
                            sec_charges.spin_projected.append(
                                ChargesValue(
                                    spin=nspin,
                                    atom_index=natom,
                                    value=charge * ureg.elementary_charge,
                                )
                            )
                elif spin == 1:
                    sec_charges.value = atom_charges.flatten() * ureg.elementary_charge
                # orbital resolved
                for natom, atom, orbitals, charges in mulliken.get('orbital', []):
                    for norb, orbital in enumerate(orbitals):
                        for nspin, charge in enumerate(charges[norb]):
                            sec_charges.orbital_projected.append(
                                ChargesValue(
                                    orbital=orbital,
                                    spin=nspin,
                                    atom_label=atom[0],
                                    atom_index=int(natom[0]),
                                    value=charge * ureg.elementary_charge,
                                )
                            )
                sec_charges.total = mulliken.get('total')

            # dipole
            dipole = source.get('dipole_moment')
            if dipole is not None:
                sec_multipoles = Multipoles()
                sec_scc.multipoles.append(sec_multipoles)
                sec_multipoles.dipole = MultipolesEntry(total=dipole)

            # eigenvalues
            if (eigenvalues := source.get('eigenvalues')) is not None:
                sec_eigenvalues = BandEnergies()
                sec_scc.eigenvalues.append(sec_eigenvalues)
                sec_eigenvalues.energies = eigenvalues.get('energies')
                sec_eigenvalues.occupations = eigenvalues.get('occupations')

            band_energy_ranges = source.get('band_energy_ranges')
            if band_energy_ranges is not None:
                if sec_scc.eigenvalues:
                    sec_band_energies = sec_scc.eigenvalues[0]
                else:
                    sec_band_energies = BandEnergies()
                    sec_scc.eigenvalues.append(sec_band_energies)
                sec_band_energies.x_ams_energy_min = (
                    band_energy_ranges[0] * ureg.hartree
                )
                sec_band_energies.x_ams_energy_max = (
                    band_energy_ranges[1] * ureg.hartree
                )
                sec_band_energies.occupations = band_energy_ranges[2]

                # band gap
                band_gap_info = source.get('band_gap_info')
                if band_gap_info is not None:
                    sec_band_gap = BandGapDeprecated()
                    sec_band_energies.band_gap.append(sec_band_gap)
                    for key, val in band_gap_info.items():
                        sec_band_gap.m_set(
                            sec_band_gap.m_get_quantity_definition(key), val
                        )

            if (band_gap := source.get('band_gap')) is not None:
                sec_band_gap = BandGap()
                sec_scc.band_gap.append(sec_band_gap)
                for key, val in band_gap.items():
                    sec_band_gap.m_set(sec_band_gap.m_get_quantity_definition(key), val)

            sec_scc.hessian_matrix = source.get('hessian_matrix')

            return sec_scc

        def parse_system(source):
            sec_system = System()
            sec_run.system.append(sec_system)

            sec_atoms = Atoms()
            sec_system.atoms = sec_atoms
            labels_positions = source.get('labels_positions')
            if labels_positions is not None:
                sec_atoms.labels = labels_positions[0]
                sec_atoms.positions = labels_positions[1]

            lattice_vectors = source.get('lattice_vectors')
            if lattice_vectors is not None:
                unit = lattice_vectors.units
                lattice_vectors = list(lattice_vectors.magnitude)
                pbc = [True, True, True]
                for n in range(len(lattice_vectors), 3):
                    lattice_vectors.append([0, 0, 0])
                    pbc[n] = False
                sec_atoms.lattice_vectors = lattice_vectors * unit
                sec_atoms.periodic = pbc

            sec_atoms.velocities = source.get('velocities')

            return sec_system

        def parse_method(source):
            if source is None:
                return

            sec_method = Method()
            sec_run.method.append(sec_method)
            sec_atom_centered = BasisSetAtomCentered()
            for key, val in source.get('confinement', {}).items():
                sec_atom_centered.m_set(
                    sec_atom_centered.m_get_quantity_definition(key), val
                )
            sec_method.electrons_representation = [
                BasisSetContainer(
                    type='atom-centered orbitals',
                    scope=['wavefunction'],
                    basis_set=[
                        BasisSet(
                            type='numeric AOs',
                            atom_centered=[sec_atom_centered],
                        )
                    ],
                )
            ]

            for function in source.get('radial_functions', []):
                sec_atom_param = AtomParameters()
                sec_method.atom_parameters.append(sec_atom_param)
                for key, val in function.items():
                    if val is None:
                        continue
                    if key == 'orbital_parameters':
                        sec_atom_param.orbitals = [str(v) for v in val[0]]
                        sec_atom_param.charges = val[1]
                        sec_atom_param.x_ams_orbital_energies = (
                            np.array(val[2], np.float64) * ureg.hartree
                        )
                        sec_atom_param.x_ams_orbital_radii = np.array(val[4])
                    else:
                        sec_atom_param.m_set(
                            sec_atom_param.m_get_quantity_definition(key), val
                        )

            ranges_orbitals = source.get('ranges_atomic_orbitals', {})
            for atom_type in ranges_orbitals.get('type', []):
                for sec_atom_param in sec_method.atom_parameters:
                    if sec_atom_param.label == atom_type[0]:
                        for n, key in enumerate(
                            ['valence', 'core', 'valence_kinetic', 'core_kinetic']
                        ):
                            sec_atom_param.m_set(
                                sec_atom_param.m_get_quantity_definition(
                                    f'x_ams_cutoff_{key}'
                                ),
                                atom_type[n + 1],
                            )
                        break

            if (
                dft_potential := source.get('model_parameters', {}).get(
                    'dft_potential', {}
                )
            ) is not None:
                sec_dft = DFT()
                sec_method.dft = sec_dft
                # TODO provide mapping
                sec_xc_functional = XCFunctional()
                sec_dft.xc_functional = sec_xc_functional
                for xc_type in ['LDA', 'GGA', 'MGGA']:
                    functionals = dft_potential.get(xc_type, '').split()
                    kind = ['XC'] if len(functionals) == 1 else ['X', 'C']
                    for n, functional in enumerate(functionals):
                        functional = functional.rstrip('x').rstrip('c').upper()
                        if kind[n] == 'X':
                            sec_xc_functional.exchange.append(
                                Functional(
                                    name='%s_%s_%s' % (xc_type, kind[n], functional)
                                )
                            )
                        elif kind[n] == 'C':
                            sec_xc_functional.correlation.append(
                                Functional(
                                    name='%s_%s_%s' % (xc_type, kind[n], functional)
                                )
                            )
                        else:
                            sec_xc_functional.contributions.append(
                                Functional(
                                    name='%s_%s_%s' % (xc_type, kind[n], functional)
                                )
                            )

            sec_electronic = Electronic()
            sec_method.electronic = sec_electronic
            model_parameters = source.get('model_parameters', {})
            spin = source.get('x_ams_spin_polarization', model_parameters.get('spin'))
            sec_electronic.n_spin_channels = 2 if spin else 1
            sec_electronic.relativity_method = self._relativity_map.get(
                model_parameters.get('relativistic_corrections')
            )
            for key, val in model_parameters.items():
                if hasattr(Method, key):
                    sec_method.m_set(sec_method.m_get_quantity_definition(key), val)

            if (charge := source.get('total_charge')) is not None:
                sec_electronic.charge = charge

            # TODO add smearing params
            if (scf_options := source.get('scf_options')) is not None:
                sec_scf = Scf()
                sec_method.scf = sec_scf
                for key, val in scf_options.items():
                    sec_scf.m_set(sec_scf.m_get_quantity_definition(key), val)

            if (k_space_sampling := source.get('k_space_sampling')) is not None:
                sec_k_mesh = KMesh()
                sec_method.k_mesh = sec_k_mesh
                for key, val in k_space_sampling.items():
                    sec_k_mesh.m_set(sec_k_mesh.m_get_quantity_definition(key), val)

            for key in source.keys():
                if hasattr(Method, key):
                    sec_method.m_set(
                        sec_method.m_get_quantity_definition(key), source.get(key)
                    )

            return sec_method

        def parse_calculation(source):
            if source is None:
                return

            sec_scc = parse_scc(source)
            sec_system = parse_system(source)
            sec_scc.system_ref = sec_system

        workflow = None
        if (geometry_opt := self.parser.geometry_optimization) is not None:
            workflow = GeometryOptimization(method=GeometryOptimizationMethod())
            for key, val in geometry_opt.items():
                if key == 'step':
                    for step in val:
                        parse_calculation(step)
                elif key.startswith('x_ams') and hasattr(GeometryOptimization, key):
                    workflow.m_set(workflow.m_get_quantity_definition(key), val)
            sec_method = parse_method(geometry_opt)
            sec_run.calculation[-1].method_ref = sec_method
            workflow.method.convergence_tolerance_energy_difference = geometry_opt.get(
                'convergence_tolerance_energy_difference'
            )
            workflow.method.convergence_tolerance_displacement_maximum = (
                geometry_opt.get('convergence_tolerance_displacement_maximum')
            )
            workflow.method.convergence_tolerance_force_maximum = geometry_opt.get(
                'convergence_tolerance_force_maximum'
            )

        elif (md := self.parser.molecular_dynamics) is not None:
            workflow = MolecularDynamics()
            sec_method = parse_method(md)
            for step in md.get('step', []):
                parse_calculation(step)
                sec_run.calculation[-1].method_ref = sec_method

        elif (sp := self.parser.get('single_point')) is not None:
            sec_method = parse_method(sp)
            parse_calculation(sp)
            sec_run.calculation[-1].method_ref = sec_method

        self.archive.workflow2 = workflow

    def parse(self, filepath, archive, logger):
        self.mainfile = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()

        rkf_files = get_files('ams.rkf', self.mainfile)
        if rkf_files:
            if len(rkf_files) > 1:
                self.logger.warning('Multiple ams.rkf files found.')
            self.parser = self.rkf_parser
            self.parser.mainfile = os.path.join(os.path.dirname(filepath), rkf_files[0])

        sec_run = Run()
        self.archive.run.append(sec_run)
        sec_run.program = Program(
            name='AMS', version=self.parser.get('program_version', '')
        )
        for key in self.parser.results.keys():
            if key.startswith('program_x_ams'):
                sec_run.program.m_set(
                    sec_run.program.m_get_quantity_definition(key.strip('program_')),
                    self.parser.get(key),
                )
            if key == 'time_start':
                sec_run.time_run = TimeRun(date_start=self.parser.get(key))
        self.parse_configurations()
