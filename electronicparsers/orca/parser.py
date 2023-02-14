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

import logging
import numpy as np

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity

from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, BasisSet, DFT, XCFunctional, Functional
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, ScfIteration, BandEnergies, Charges, ChargesValue,
    Spectra
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization
from nomad.datamodel.metainfo.simulation.workflow import (
    GeometryOptimization as GeometryOptimizaton2, GeometryOptimizationMethod
)


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_float = r'[-+]?\d+\.?\d*(?:[Ee][-+]\d+)?'

        self._energy_mapping = {
            'Total Energy': 'energy_total', 'Nuclear Repulsion': 'energy_nuclear_repulsion',
            'Electronic Energy': 'elec_energy', 'One Electron Energy': 'one_elec_energy',
            'Two Electron Energy': 'two_elec_energy', 'Potential Energy': 'potential_energy',
            'Kinetic Energy': 'energy_kinetic_electronic', r'E\(X\)': 'energy_exchange',
            r'E\(C\)': 'energy_correlation', r'E\(XC\)': 'energy_XC'}

        self._timing_mapping = {
            'Total time': 'final_time', 'Sum of individual times': 'sum_individual_times',
            'Fock matrix formation': 'fock_matrix_formation', 'Coulomb formation': 'coulomb_formation',
            r'Split\-RI-J': 'split_rj', 'XC integration': 'xc_integration',
            r'Basis function eval\.': 'basis_fn_evaluation', r'Density eval\.': 'density_evaluation',
            r'XC\-Functional eval\.': 'xc_functional_evaluation', r'XC\-Potential eval\.': 'potential_evaluation',
            'Diagonalization': 'diagonalization', 'Density matrix formation': 'density_matrix_formation',
            'Population analysis': 'population_analysis', 'Initial guess': 'initial_guess',
            'Orbital Transformation': 'orbital_transformation', 'Orbital Orthonormalization': 'orbital_orthonormalization',
            'DIIS solution': 'diis_solution', 'Grid generation': 'grid_generation'}

        def str_to_cartesian_coordinates(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            symbols = [v[0][:2] for v in val]
            coordinates = np.array([v[1:4] for v in val], dtype=float)
            return symbols, coordinates * ureg.angstrom

        basis_set_quantities = [
            Quantity('basis_set_atom_labels', r'Type\s*(\w+)', repeats=True),
            Quantity('basis_set', r':\s*(\w+)\s*contracted\s*to', repeats=True),
            Quantity('basis_set_contracted', r'(\w+)\s*pattern', repeats=True)]

        basis_set_statistics_quantities = [
            Quantity(
                'nb_of_primitive_gaussian_shells',
                r'# of primitive gaussian shells\s*\.+\s*(\d+)', repeats=True, dtype=int),
            Quantity(
                'nb_of_primitive_gaussian_functions',
                r'# of primitive gaussian functions\s*\.+\s*(\d+)', repeats=True, dtype=int),
            Quantity(
                'nb_of_contracted_shells',
                r'# of contracted shells\s*\.+\s*(\d+)', repeats=True, dtype=int),
            Quantity(
                'nb_of_contracted_basis_functions',
                r'# of contracted (?:aux-)?basis functions\s*\.+\s*(\d+)', repeats=True, dtype=int),
            Quantity(
                'highest_angular_moment',
                r'Highest angular momentum\s*\.+\s*(\d+)', repeats=True, dtype=int),
            Quantity(
                'maximum_contraction_depth',
                r'Maximum contraction depth\s*\.+\s*(\d+)', repeats=True, dtype=int)]

        grid_quantities = [
            Quantity(
                'gral_integ_accuracy',
                rf'General Integration Accuracy\s*IntAcc\s*\.+\s*({re_float})', dtype=float),
            Quantity(
                'radial_grid_type',
                r'Radial Grid Type\s*RadialGrid\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'angular_grid',
                r'Angular Grid \(max\. acc\.\)\s*AngularGrid\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'grid_pruning_method',
                r'Angular grid pruning method\s*GridPruning\s*\.+\s*(.+)',
                flatten=False, convert=False),
            Quantity(
                'weight_gener_scheme',
                r'Weight generation scheme\s*WeightScheme\s*\.+\s*(\w+)', convert=False),
            Quantity(
                'basis_fn_cutoff',
                rf'Basis function cutoff\s*BFCut\s*\.+\s*({re_float})', dtype=float),
            Quantity(
                'integr_weight_cutoff',
                rf'Integration weight cutoff\s*WCut\s*\.+\s*({re_float})', dtype=float),
            Quantity(
                'nb_grid_pts_after_initial_pruning',
                r'# of grid points \(after initial pruning\)\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'nb_grid_pts_after_weights_screening',
                r'# of grid points \(after weights\+screening\)\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'total_nb_grid_pts',
                r'Total number of grid points\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'total_nb_batches',
                r'Total number of batches\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'avg_nb_points_per_batch',
                r'Average number of points per batch\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'avg_nb_grid_pts_per_atom',
                r'Average number of grid points per atom\s*\.+\s*(\d+)', dtype=int)]

        scf_convergence_quantities = [
            Quantity(
                name.lower().replace(' ', '_').replace('-', '_'),
                rf'%s\s*\.+\s*({re_float})\s* Tolerance :\s*({re_float})' % name,
                dtype=float, unit=ureg.hartree) for name in [
                    'Last Energy change', 'Last MAX-Density change', 'Last RMS-Density change']]

        population_quantities = [
            Quantity(
                'atomic_charges',
                r'[A-Z]+ ATOMIC CHARGES.*\n\-+([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=[
                    Quantity('species', r'\n *\d+\s*(\w+)', repeats=True),
                    Quantity('charge', rf':\s*({re_float})', repeats=True, dtype=float),
                    Quantity(
                        'total_charge',
                        rf'Sum of atomic charges\s*:\s*({re_float})', dtype=float)])),
            Quantity(
                'orbital_charges',
                r'[A-Z]+ REDUCED ORBITAL CHARGES.*\s*\-+([\s\S]+?\n\n)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'atom',
                        r'([A-Z][a-z]?\s*[spdf][\s\S]+?)\n *(?:\d|\Z)',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity('species', r'([A-Z][a-z]?)', convert=False),
                            Quantity('charge', rf'([spdf]\S*)\s*:\s*({re_float})', repeats=True)]))]))]

        self_consistent_quantities = [
            Quantity(
                'scf_settings',
                r'SCF SETTINGS\s*\-+([\s\S]+?)\-{10}', sub_parser=TextParser(quantities=[
                    Quantity(
                        'XC_functional_type',
                        r'Ab initio Hamiltonian\s*Method\s*\.+\s*(\S+)', convert=False),
                    Quantity(
                        'XC_functional_type',
                        r'Density Functional\s*Method\s*\.+\s*(\S+)', convert=False),
                    Quantity(
                        'exchange_functional',
                        r'Exchange Functional\s*Exchange\s*\.+\s*(\S+)', convert=False),
                    Quantity(
                        'xalpha_param',
                        rf'X-Alpha parameter\s*XAlpha\s*\.+\s*({re_float})', dtype=float),
                    Quantity(
                        'beckes_beta_param',
                        rf'Becke\'s b parameter\s*XBeta\s*\.+\s*({re_float})', dtype=float),
                    Quantity(
                        'correl_functional',
                        r'Correlation Functional Correlation\s*\.+\s*(\S+)', convert=False),
                    Quantity(
                        'lda_part_of_gga_corr',
                        r'LDA part of GGA corr\.\s*LDAOpt\s*\.+\s*(\S+)', convert=False),
                    Quantity(
                        'scalar_relativistic_method',
                        r'Scalar relativistic method\s*\.+\s*(\w+)', convert=False),
                    Quantity(
                        'speed_of_light_used',
                        rf'Speed of light used\s*Velit\s*\.+\s*({re_float})', dtype=float),
                    Quantity(
                        'hf_type',
                        r'Hartree-Fock type\s*HFTyp\s*\.+\s*(\w+)', convert=False),
                    Quantity(
                        'total_charge',
                        rf'Total Charge\s*Charge\s*\.+\s*({re_float})', dtype=float),
                    Quantity(
                        'multiplicity',
                        rf'Multiplicity\s*Mult\s*\.+\s*({re_float})', dtype=float),
                    Quantity(
                        'nelectrons',
                        rf'Number of Electrons\s*NEL\s*\.+\s*({re_float})', dtype=float),
                    Quantity(
                        'nuclear_repulsion',
                        rf'Nuclear Repulsion\s*ENuc\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
                    Quantity(
                        'convergence_check_mode',
                        r'Convergence Check Mode ConvCheckMode\s*\.+\s*(\S+)', convert=False),
                    Quantity(
                        'energy_change_tolerance',
                        rf'Energy Change\s*TolE\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
                    Quantity(
                        '1_elect_energy_change',
                        rf'1\-El\. energy change\s*\.+\s*({re_float})', dtype=float)])),
            Quantity(
                'dft_grid_generation',
                r'DFT GRID GENERATION\s*\-+([\s\S]+?\-{10})',
                sub_parser=TextParser(quantities=grid_quantities)),
            Quantity(
                'scf_iterations',
                r'SCF ITERATIONS\s*\-+([\s\S]+?)\*{10}',
                sub_parser=TextParser(quantities=[Quantity(
                    'energy',
                    rf'\n *\d+\s*({re_float})\s*{re_float}', repeats=True, dtype=float, unit=ureg.hartree)])),
            Quantity(
                'final_grid',
                r'Setting up the final grid:([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=grid_quantities)),
            Quantity(
                'total_scf_energy',
                r'TOTAL SCF ENERGY\s*\-+([\s\S]+?)\-{10}', sub_parser=TextParser(quantities=[
                    Quantity(
                        name,
                        rf'%s\s*:\s*({re_float})' % key, dtype=float, unit=ureg.hartree)
                    for key, name in self._energy_mapping.items()] + [
                        Quantity(
                            'virial_ratio',
                            rf'Virial Ratio\s*:\s*({re_float})', dtype=float),
                        Quantity(
                            'nb_elect_alpha_channel',
                            rf'N\(Alpha\)\s*:\s*({re_float})', dtype=float),
                        Quantity(
                            'nb_elect_beta_channel',
                            rf'N\(Beta\)\s*:\s*({re_float})', dtype=float),
                        Quantity(
                            'nb_elect_total',
                            rf'N\(Total\)\s*:\s*({re_float})', dtype=float)])),
            Quantity(
                'scf_convergence',
                r'SCF CONVERGENCE\s*\-+([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=scf_convergence_quantities)),
            Quantity(
                'orbital_energies',
                r'NO\s*OCC\s*E\(Eh\)\s*E\(eV\)\s*([\s\S]+?)\n\n',
                str_operation=lambda x: np.array([v.split()[:4] for v in x.split('\n')], dtype=float),
                repeats=True),
            Quantity(
                'mulliken',
                r'MULLIKEN POPULATION ANALYSIS \*\s*\*+([\s\S]+?)\*{10}',
                sub_parser=TextParser(quantities=population_quantities)),
            Quantity(
                'timings',
                r'\n *TIMINGS\s*\-+\s*([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=[Quantity(
                    name, rf'%s\s*\.+\s*({re_float})' % key, dtype=float, unit=ureg.s)
                    for key, name in self._timing_mapping.items()]))
        ]

        # TODO parse more properties, add to metainfo
        tddft_quantities = [
            Quantity(
                'absorption_spectrum_electric',
                r'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS\s*'
                r'\-+[\s\S]+?\-+\n([\s\S]+?)\-{10}',
                str_operation=lambda x: [v.split() for v in x.strip().split('\n')])]

        # TODO parse more properties, add to metainfo
        mp2_quantities = [
            Quantity(
                'mp2_basis_dimension',
                r'Dimension of the basis\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'scaling_mp2_energy',
                rf'Overall scaling of the MP2 energy\s*\.+\s*({re_float})', dtype=float),
            Quantity(
                'mp2_aux_basis_dimension',
                r'Dimension of the aux\-basis\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'energy_method_current',
                rf'RI\-MP2 CORRELATION ENERGY:\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'energy_total',
                rf'MP2 TOTAL ENERGY:\s*({re_float})', dtype=float, unit=ureg.hartree)]

        def str_to_iteration_energy(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            keys = val[0]
            val = np.transpose(
                np.array([v for v in val[1:] if len(v) == len(keys)], dtype=float))
            return {keys[i]: val[i] for i in range(len(keys))}

        ci_quantities = [
            Quantity(
                'electronic_structure_method',
                r'Correlation treatment\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'single_excitations_on_off',
                r'Single excitations\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'orbital_opt_on_off',
                r'Orbital optimization\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'z_vector_calc_on_off',
                r'Calculation of Z vector\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'Brueckner_orbitals_calc_on_off',
                r'Calculation of Brueckner orbitals\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'perturbative_triple_excitations_on_off',
                r'Perturbative triple excitations\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'f12_correction_on_off',
                r'Calculation of F12 correction\s*\.+\s*(\S+)', convert=False),
            Quantity(
                'frozen_core_treatment',
                r'Frozen core treatment\s*\.+\s*(.+)', flatten=False, convert=False),
            Quantity(
                'reference_wave_function',
                r'Reference Wavefunction\s*\.+\s*(.+)', flatten=False, convert=False),
            Quantity(
                'nb_of_atomic_orbitals',
                r'Number of AO\'s\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'nb_of_electrons',
                r'Number of electrons\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'nb_of_correlated_electrons',
                r'Number of correlated electrons\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'integral_transformation',
                r'Integral transformation\s*\.+\s*(.+)', flatten=False, convert=False),
            Quantity(
                'level_shift_amplitude_update',
                rf'Level shift for amplitude update\s*\.+\s*({re_float})', dtype=float),
            Quantity(
                'coulomb_transformation_type',
                r'Transformation type\s*\.+\s*(.+)', flatten=False, convert=False),
            Quantity(
                'coulomb_transformation_dimension_basis',
                r'Dimension of the basis\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'nb_internal_alpha_mol_orbitals',
                r'Number of internal alpha\-MOs\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'nb_internal_beta_mol_orbitals',
                r'Number of internal beta\-MOs\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'pair_cutoff',
                rf'Pair cutoff\s*\.+\s*({re_float})', dtype=float),
            Quantity(
                'atomic_orbital_integral_source',
                r'AO\-integral source\s*\.+\s*(.+)', flatten=False, convert=False),
            Quantity(
                'integral_package_used',
                r'Integral package used\s*\.+\s*(.+)', flatten=False, convert=False),
            Quantity(
                'nb_alpha_pairs_included',
                r'Number of Alpha\-MO pairs included\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'nb_beta_pairs_included',
                r'Number of Beta\-MO pairs included\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'mp2_energy_spin_aa',
                rf'EMP2\(aa\)=\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'mp2_energy_spin_bb',
                rf'EMP2\(bb\)=\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'mp2_energy_spin_ab',
                rf'EMP2\(ab\)=\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'mp2_initial_guess',
                rf'E\(0\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'mp2_energy',
                rf'E\(MP2\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'mp2_total_energy',
                rf'Initial E\(tot\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'T_and_T_energy',
                rf'<T\|T>\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'total_nb_pairs_included',
                r'Number of pairs included\s*\.+\s*(\d+)', dtype=int),
            Quantity(
                'iteration_energy',
                r'(Iter\s*E\(tot\)[\s\S]+?)\-{3}',
                str_operation=str_to_iteration_energy, convert=False),
            Quantity(
                'ccsd_correlation_energy',
                rf'E\(CORR\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'ccsd_total_energy',
                rf'E\(TOT\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'single_norm_half_ss',
                rf'Singles Norm <S\|S>\*\*1/2\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                't1_diagnostic',
                rf'T1 diagnostic\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'ccsdt_total_triples_correction',
                rf'Triples Correction \(T\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'ccsdt_aaa_triples_contribution',
                rf'alpha\-alpha\-alpha\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'ccsdt_aab_triples_contribution',
                rf'alpha\-alpha\-beta\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            # typo in metainfo?
            Quantity(
                'ccsdt_aba_triples_contribution',
                rf'alpha\-beta\-beta\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'ccsdt_bbb_triples_contribution',
                rf'beta\-beta\-beta\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'ccsdt_final_corr_energy',
                rf'Final correlation energy\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'ccsd_final_energy',
                rf'E\(CCSD\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree),
            Quantity(
                'energy_total',
                rf'E\(CCSD\(T\)\)\s*\.+\s*({re_float})', dtype=float, unit=ureg.hartree)]

        calculation_quantities = [
            Quantity(
                'cartesian_coordinates',
                r'CARTESIAN COORDINATES \(ANGSTROEM\)\s*\-+\s*([\s\S]+?)\n\n',
                str_operation=str_to_cartesian_coordinates),
            Quantity(
                'basis_set',
                r'\n *BASIS SET INFORMATION\s*\-+([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=basis_set_quantities)),
            Quantity(
                'auxiliary_basis_set',
                r'\n *AUXILIARY BASIS SET INFORMATION\s*\-+([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=basis_set_quantities)),
            Quantity(
                'basis_set_statistics',
                r'BASIS SET STATISTICS AND STARTUP INFO([\s\S]+?)\-{10}',
                sub_parser=TextParser(quantities=basis_set_statistics_quantities)),
            Quantity(
                'self_consistent',
                r'((?:ORCA SCF|DFT GRID GENERATION)\s*\-+[\s\S]+?(?:\-{70}|\Z))',
                sub_parser=TextParser(quantities=self_consistent_quantities)),
            Quantity(
                'tddft',
                r'ORCA TD\-DFT(?:/TDA)* CALCULATION\s*\-+\s*([\s\S]+?E\(tot\).*)',
                sub_parser=TextParser(quantities=tddft_quantities)),
            Quantity(
                'mp2',
                r'ORCA MP2 CALCULATION([\s\S]+?MP2 TOTAL ENERGY:.+)',
                sub_parser=TextParser(quantities=mp2_quantities)),
            Quantity(
                'ci',
                r'ORCA\-MATRIX DRIVEN CI([\s\S]+?E\(CCSD\(T\)\).*)',
                sub_parser=TextParser(quantities=ci_quantities)
            )]

        geometry_optimization_quantities = [Quantity(
            '%s_tol' % key.lower().replace(' ', '_').replace('.', ''),
            rf'%s\s*(\w+)\s*\.+\s*({re_float})' % key, dtype=float) for key in [
                'Energy Change', 'Max. Gradient', 'RMS Gradient', 'Max. Displacement',
                'RMS Displacement']]

        geometry_optimization_quantities += [
            Quantity(
                'update_method', r'Update method\s*(\w+)\s*\.+\s*(.+)'),
            Quantity(
                'coords_choice', r'Choice of coordinates\s*(\w+)\s*\.+\s*(.+)'),
            Quantity(
                'initial_hessian', r'Initial Hessian\s*(\w+)\s*\.+\s*(.+)')]

        geometry_optimization_quantities += [
            Quantity(
                'cycle',
                r'OPTIMIZATION CYCLE\s*\d+\s*\*\s*\*+([\s\S]+?)(?:\*\s*GEOMETRY|OPTIMIZATION RUN DONE|\Z)',
                repeats=True, sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity(
                'final_energy_evaluation',
                r'FINAL ENERGY EVALUATION AT THE STATIONARY POINT([\s\S]+?FINAL SINGLE POINT ENERGY.*)',
                sub_parser=TextParser(quantities=calculation_quantities))]

        self._quantities = [
            Quantity(
                'program_version',
                r'Program Version\s*([\w_.].*)', convert=False, flatten=False),
            Quantity(
                'program_svn',
                r'\(SVN:\s*\$([^$]+)\$\)\s', convert=False, flatten=False),
            Quantity(
                'program_compilation_date',
                r'\(\$Date\:\s*(\w.+?)\s*\$\)', convert=False, flatten=False),
            Quantity(
                'input_file',
                r'INPUT FILE\s*\=+([\s\S]+?)END OF INPUT',
                sub_parser=TextParser(quantities=[
                    Quantity('xc_functional', r'\d+>\s*!\s*(\S+)')])),
            Quantity(
                'single_point',
                r'\* Single Point Calculation \*\s*\*+([\s\S]+?(?:FINAL SINGLE POINT ENERGY.*|\Z))',
                sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity(
                'geometry_optimization',
                r'\* Geometry Optimization Run \*\s*\*+([\s\S]+?(?:OPTIMIZATION RUN DONE|\Z))',
                sub_parser=TextParser(quantities=geometry_optimization_quantities))
        ]


class OrcaParser:
    def __init__(self):
        self.out_parser = OutParser()

        # TODO list adapted from old parser, is incomplete and entries may be incorrect
        self._xc_functional_map = {
            'HF': ['HS_X'],
            'HFS': ['HF_X'],
            'XALPHA': ['HF_X', 'LDA_C_XALPHA'],
            'LSD': ['LDA_X', 'LDA_C_VWN_RPA', 'VWN5_RPA'],
            'LDA': ['LDA_X', 'LDA_C_VWN_RPA', 'VWN5_RPA'],
            'VWN': ['LDA_X', 'LDA_C_VWN_RPA', 'VWN5_RPA'],
            'VWN5': ['LDA_X', 'LDA_C_VWN_RPA', 'VWN5_RPA'],
            'VWN3': ['LDA_X', 'LDA_C_VWN_3'],
            'PWLDA': ['LDA_X', 'LDA_C_PW'],
            'BNULL': ['GGA_X_B88'],
            'BVWN': ['GGA_X_B88', 'LDA_C_VWN_RPA', 'VWN5_RPA'],
            'BP': ['LDA_X', 'GGA_X_B88', 'LDA_C_VWN', 'GGA_C_P86'],
            'BP86': ['LDA_X', 'GGA_X_B88', 'LDA_C_VWN', 'GGA_C_P86'],
            'PW91': ['GGA_X_PW91', 'GGA_C_PW91'],
            'PWP': ['GGA_X_PW91', 'GGA_C_P86'],
            'MPWPW': ['GGA_X_MPW91', 'GGA_C_PW91'],
            'MPWLYP': ['GGA_X_MPW91', 'GGA_C_LYP'],
            'BLYP': ['GGA_X_B88', 'GGA_C_LYP'],
            'GP': ['GGA_X_G96', 'GGA_C_P86'],
            'GLYP': ['GGA_X_G96', 'GGA_C_LYP'],
            'PBE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'REVPBE': ['GGA_X_PBE_R', 'GGA_C_PBE'],
            'RPBE': ['GGA_X_RPBE', 'GGA_C_PBE'],
            'OLYP': ['GGA_X_OPTX', 'GGA_C_LYP', 'GGA_XC_OPWLYP_D'],
            'OPBE': ['GGA_XC_OPBE_D'],
            'XLYP': ['GGA_XC_XLYP'],
            'B97-D': ['GGA_XC_B97_D'],
            'B97-D3': ['GGA_XC_B97_D'],
            'TPSS': ['LDA_X', 'MGGA_X_TPSS', 'LDA_C_PW', 'MGGA_C_TPSS'],
            'TPSSh': ['HYB_MGGA_XC_TPSSH'],
            'M06L': ['MGGA_X_M06_L', 'MGGA_C_M06_L'],
            'M06': ['MGGA_X_M06', 'MGGA_C_M06'],
            'M062X': ['MGGA_X_M06_2X', 'MGGA_C_M06_2X'],
            'B1LYP': ['HYB_GGA_XC_B1LYP'],
            'B3LYP': ['HYB_GGA_XC_B3LYP'],
            'B1P': ['HYB_GGA_XC_B1PW91'],
            'B3P': ['HYB_GGA_XC_B3P86'],
            'B3PW': ['HYB_GGA_XC_B3PW91'],
            'G1LYP': ['GGA_X_G96', 'GGA_C_OP_G96'],
            'PBE0': ['HYB_GGA_XC_PBEH'],
            'PW1PW': ['HYB_GGA_XC_B1PW91'],
            'PWP91_1': ['HYB_GGA_XC_B1PW91'],
            'PWP1': ['HYB_GGA_XC_B1PW91'],
            'mPW1PW': ['HYB_GGA_XC_MPW1PW'],
            'mPW1LYP': ['HYB_GGA_XC_MPWLYP1M'],
            'O3LYP': ['HYB_GGA_XC_O3LYP'],
            'X3LYP': ['HYB_GGA_XC_X3LYP'],
            'PW6B95': ['HYB_MGGA_XC_PW6B95'],
            'B97': ['HYB_GGA_XC_B97'],
            'BHANDHLYP': ['HYB_GGA_XC_BHANDHLYP'],
            'B2PLYP': ['HYB_GGA_XC_B2PLYP'],
            'MB2PLYP': ['HYB_GGA_XC_MB2PLYP'],
            'PWPB95': ['HYB_MGGA_XC_MPW1B95']}

        self._functional_type = {
            'SLATER': 'LDA', 'B88': 'GGA', 'G96': 'GGA', 'PW91': 'GGA', 'MPW': 'GGA',
            'PBE': 'GGA', 'RPBE': 'GGA', 'OPTX': 'GGA', 'X': 'GGA', 'TPSS': 'MGGA',
            'B97D': 'GGA', 'B97BECKE': 'GGA', 'SCAN': 'MGGA', 'VWN5': 'LDA', 'VWN3': 'LDA',
            'PWLDA': 'LDA', 'P86': 'GGA', 'LYP': 'GGA'}

    def parse_method(self, section):
        sec_method = self.archive.run[-1].m_create(Method)

        # TODO fix metainfo so variables take lists
        for kind in ['basis_set', 'auxiliary_basis_set']:
            basis_set = section.get(kind)
            if basis_set is None:
                continue
            for n in range(len(basis_set.get('basis_set', []))):
                sec_basis_set = sec_method.m_create(BasisSet)
                sec_basis_set.type = 'gaussians'
                for key in ['basis_set', 'basis_set_atom_labels', 'basis_set_contracted']:
                    val = basis_set.get(key)
                    if val is None:
                        continue
                    prefix = '' if key == 'basis_set_atom_labels' else kind.split('basis_set')[0]
                    metainfo_name = 'x_orca_%s%s' % (prefix, key)
                    setattr(sec_basis_set, metainfo_name, val[n])

        # gaussian basis sets
        basis_set = section.get('basis_set_statistics')
        if basis_set is not None:
            sec_basis_set = sec_method.m_create(BasisSet)
            for key, val in basis_set.items():
                if val is None:
                    continue
                for n in range(len(val)):
                    ext = '' if n == 0 else '_aux'
                    setattr(sec_basis_set, 'x_orca_%s%s' % (key, ext), val[n])

        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)
        # TODO identify DFT+U
        sec_electronic.method = 'DFT'

        scf_settings = section.get('self_consistent', {}).get('scf_settings', {})
        for key, val in scf_settings.items():
            if val is not None:
                if hasattr(val, 'units'):
                    if val.units == 'hartree':
                        val = val.to('joule').magnitude
                setattr(sec_method, 'x_orca_%s' % key, val)

        dft_grid_generation = section.get('self_consistent', {}).get('dft_grid_generation', {})
        for key, val in dft_grid_generation.items():
            if val is not None:
                setattr(sec_method, 'x_orca_%s' % key, val)

        final_grid = section.get('self_consistent', {}).get('final_grid', {})
        for key, val in final_grid.items():
            if val is not None:
                setattr(sec_method, 'x_orca_%s' % key, val)

        # xc functional
        # get type from input card
        xc_functional = self.out_parser.get('input_file', {}).get('xc_functional', '').upper()
        xc_functionals = self._xc_functional_map.get(xc_functional, [])
        # if not in map, get it from explicit exchange and correlation settings
        if len(xc_functionals) == 0:
            xc_functional_type = scf_settings.get('XC_functional_type', '')
            if xc_functional_type.startswith('Hartree-Fock'):
                xc_functionals = self._xc_functional_map.get('HF', [])

            elif xc_functional_type.startswith('DFT'):
                exchange = scf_settings.get(
                    'exchange_functional').upper().replace('-', '').split('_')[0]
                exchange_type = self._functional_type.get(exchange, None)
                if exchange_type is not None:
                    xc_functionals.append('%s_X_%s' % (exchange_type, exchange))

                if scf_settings.get('xalpha_param') is not None:
                    xc_functionals.append('LDA_X')

                correlation = scf_settings.get(
                    'correl_functional').upper().replace('-', '').split('_')[0]
                correlation_type = self._functional_type.get(correlation, None)
                if correlation_type is not None:
                    xc_functionals.append('%s_C_%s' % (correlation_type, correlation))

                lda_correlation = scf_settings.get('lda_part_of_gga_corr')
                if lda_correlation is not None:
                    xc_functionals.append('LDA_C_%s' % (lda_correlation))

                if len(xc_functionals) == 0:
                    self.logger.warning('Cannot resolve xc functional', data=dict(name=xc_functional))

        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for functional in xc_functionals:
            if '_X_' in functional or functional.endswith('_X'):
                sec_xc_functional.exchange.append(Functional(name=functional))
            elif '_C_' in functional or functional.endswith('_C'):
                sec_xc_functional.correlation.append(Functional(name=functional))
            elif 'HYB' in functional:
                sec_xc_functional.hybrid.append(Functional(name=functional))
            else:
                sec_xc_functional.contributions.append(Functional(name=functional))

        for calculation_type in ['tddft', 'mp2', 'ci']:
            calculation = section.get(calculation_type)
            if calculation is None:
                continue
            method = calculation.get('electronic_structure_method')
            method = calculation_type.upper() if method is None else method
            sec_method = self.archive.run[-1].m_create(Method)
            sec_method.electronic = Electronic(method=method)

            for key, val in calculation.items():
                if val is not None:
                    if hasattr(val, 'units'):
                        if val.units == 'hartree':
                            val = val.to('joule').magnitude
                    setattr(sec_method, 'x_orca_%s' % key, val)

            sec_method.starting_method_ref = self.archive.run[-1].method[0]
            sec_method.methods_ref = [self.archive.run[-1].method[0]]

        return sec_method

    def parse_system(self, section):
        sec_system = self.archive.run[-1].m_create(System)
        sec_atoms = sec_system.m_create(Atoms)
        if section.get('cartesian_coordinates') is not None:
            symbols, coordinates = section.get('cartesian_coordinates')
            sec_atoms.labels = symbols
            sec_atoms.positions = coordinates
        sec_atoms.periodic = [False] * 3
        return sec_system

    def parse_scc(self, section):
        sec_scc = self.archive.run[-1].m_create(Calculation)

        self_consistent = section.get('self_consistent')
        if self_consistent is None:
            return sec_scc

        sec_energy = sec_scc.m_create(Energy)
        scf_energy = self_consistent.get('total_scf_energy', None)
        if scf_energy is not None:
            sec_energy.total = EnergyEntry(value=scf_energy.get('energy_total'))
            energy_keys = list(self.out_parser._energy_mapping.values())
            for key, val in scf_energy.items():
                if val is not None:
                    if key.startswith('energy_'):
                        sec_energy.m_add_sub_section(getattr(
                            Energy, key.replace('energy_', '').lower()), EnergyEntry(value=val))
                    else:
                        if key in energy_keys:
                            val = val.to('joule').magnitude
                        setattr(sec_scc, 'x_orca_%s' % key, val)

        scf_iterations = self_consistent.get('scf_iterations', None)
        if scf_iterations is not None:
            for energy in scf_iterations.get('energy', []):
                sec_scf_iteration = sec_scc.m_create(ScfIteration)
                sec_scf_iteration.energy = Energy(total=EnergyEntry(value=energy))

            # why are tolerances in scf iteration
            scf_convergence = self_consistent.get('scf_convergence', {})
            for key, val in scf_convergence.items():
                if val is not None:
                    val = val.to('joule').magnitude
                    setattr(sec_scf_iteration, 'x_orca_%s' % key, val[0])
                    key = key.rstrip('_change') if 'density' in key else key
                    setattr(sec_scf_iteration, 'x_orca_%s_tolerance' % key, val[1])

        # method-specific quantities
        for calculation_type in ['tddft', 'mp2', 'ci']:
            calculation = section.get(calculation_type)
            if calculation is None:
                continue
            for key, val in calculation.items():
                if hasattr(val, 'units'):
                    if val.units == 'hartree':
                        val = val.to('joule').magnitude
                setattr(sec_scc, 'x_orca_%s' % key, val)

        # eigenvalues
        orbital_energies = self_consistent.get('orbital_energies')
        if orbital_energies is not None:
            sec_eigenvalues = sec_scc.m_create(BandEnergies)
            orbital_energies = np.transpose(orbital_energies[:2])
            occupation = orbital_energies[1].T
            occupation = np.reshape(occupation, (len(occupation), 1, len(occupation[0])))
            values = orbital_energies[2].T
            values = np.reshape(values, (len(values), 1, len(values[0]))) * ureg.hartree
            sec_eigenvalues.energies = values
            sec_eigenvalues.occupations = occupation

        # mulliken
        mulliken = self_consistent.get('mulliken')
        if mulliken is not None:
            atomic_charges = mulliken.get('atomic_charges')
            orbital_charges = mulliken.get('orbital_charges')

            sec_charges = sec_scc.m_create(Charges)
            sec_charges.analysis_method = 'mulliken'
            sec_charges.n_charges_atoms = len(atomic_charges.get('species', []))
            sec_charges.value = atomic_charges.charge
            for atom in range(len(atomic_charges.get('species', []))):
                for orbital, orbital_charge in orbital_charges.atom[atom].get('charge', []):
                    sec_charges_value = sec_charges.m_create(ChargesValue, Charges.orbital_projected)
                    sec_charges_value.atom_index = atom
                    sec_charges_value.atom_label = orbital_charges.atom[atom].species
                    sec_charges_value.orbital = orbital
                    sec_charges_value.value = orbital_charge

            sec_charges.total = atomic_charges.total_charge

        # excitations
        spectrum = section.get('tddft', {}).get('absorption_spectrum_electric')
        if spectrum is not None:
            sec_spectra = sec_scc.m_create(Spectra)
            spectrum = [val for val in spectrum if len(val) == 8]
            spectrum = np.transpose(spectrum)
            sec_spectra.excitation_energies = (spectrum[1] * ureg.c * ureg.h / ureg.cm)
            sec_spectra.oscillator_strengths = spectrum[3]
            sec_spectra.transition_dipole_moments = np.transpose(
                spectrum[5:7]) * ureg.elementary_charge * ureg.bohr

        # timings
        timings = self_consistent.get('timings', {})
        for key, val in timings.items():
            if val is not None:
                setattr(sec_scc, 'x_orca_%s' % key, val.magnitude)

        return sec_scc

    def parse_configurations(self):
        def parse_configuration(section):
            if section is None:
                return
            sec_method = self.parse_method(section)
            sec_system = self.parse_system(section)
            sec_scc = self.parse_scc(section)
            sec_scc.method_ref = sec_method
            sec_scc.system_ref = sec_system

        parse_configuration(self.out_parser.get('single_point'))

        sec_workflow = self.archive.m_create(Workflow)
        workflow = None

        geometry_optimization = self.out_parser.get('geometry_optimization')
        if geometry_optimization is not None:
            for cycle in geometry_optimization.get('cycle', []):
                parse_configuration(cycle)

            parse_configuration(geometry_optimization.get('final_energy_evaluation'))

            sec_workflow.type = 'geometry_optimization'
            sec_geometry_opt = sec_workflow.m_create(GeometryOptimization)
            workflow = GeometryOptimizaton2(method=GeometryOptimizationMethod())
            for key, val in geometry_optimization.items():
                if key in ['cycle', 'final_energy_evaluation'] or val is None:
                    continue
                if key.endswith('tol'):
                    if 'gradient' in key:
                        val[1] = (val[1] * ureg.hartree / ureg.bohr).to('joule/meter').magnitude
                        if 'max' in key:
                            workflow.method.convergence_tolerance_force_maximum = val[1]
                    elif 'displacement' in key:
                        val[1] = (val[1] * ureg.bohr).to('meter').magnitude
                        if 'max' in key:
                            workflow.method.convergence_tolerance_displacement_maximum = val[1]
                    else:
                        val[1] = (val[1] * ureg.hartree).to('joule').magnitude
                        if 'energy' in key:
                            workflow.method.convergence_tolerance_energy_difference = val[1]
                    setattr(sec_geometry_opt, 'x_orca_%s_value' % key, val[1])
                    val = val[0]
                elif key in ['update_method', 'coords_choice', 'initial_hessian']:
                    setattr(sec_geometry_opt, 'x_orca_%s_name' % key, ' '.join(val[1:]))
                    val = val[0]
                setattr(sec_geometry_opt, 'x_orca_%s' % key, val)

        self.archive.workflow2 = workflow

    def init_parser(self, filepath, logger):
        self.out_parser.mainfile = filepath
        self.out_parser.logger = logger

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.init_parser(filepath, logger)

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name='ORCA')
        version = []
        for key in ['program_version', 'program_svn', 'program_compilation_date']:
            val = self.out_parser.get(key)
            if val is not None:
                setattr(sec_run, 'x_orca_%s' % key, val)
                version.append(val)
        sec_run.program.version = ' '.join(version)
        sec_run.program.compilation_date = self.out_parser.get('program_compilation_date')

        self.parse_configurations()
