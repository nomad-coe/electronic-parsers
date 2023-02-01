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
import re
import os
import textwrap
import datetime

import ase
import numpy as np

from nomad.units import ureg
from nomad import atomutils
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms)
from nomad.datamodel.metainfo.simulation.method import (
    Method, BasisSet, Electronic, Scf, DFT, XCFunctional, Functional, BasisSetAtomCentered
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, EnergyEntry, Forces, ForcesEntry, BandStructure,
    BandEnergies, Dos, DosValues
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization
from nomad.datamodel.metainfo.simulation.workflow import (
    GeometryOptimization as GeometryOptimization2, GeometryOptimizationMethod)
from .metainfo.crystal import x_crystal_section_shell


def capture(regex):
    return r'(' + regex + r')'


flt = r'-?(?:\d+\.?\d*|\d*\.?\d+)(?:E[\+-]?\d+)?'  # Floating point number
flt_c = capture(flt)                               # Captures a floating point number
flt_crystal_c = r'(-?\d+(?:.\d+)?\*\*-?.*\d+)'     # Crystal specific floating point syntax
ws = r'\s+'                                        # Series of white-space characters
integer = r'-?\d+'                                 # Integer number
integer_c = capture(integer)                       # Captures integer number
word = r'[a-zA-Z]+'                                # A single alphanumeric word
word_c = capture(word)                             # Captures a single alphanumeric word
br = r'\r?\n'                                      # Newline that works for both Windows and Unix. Crystal can be run on a Windows machine as well.


class CrystalParser:
    """NOMAD-lab parser for Crystal.
    """
    def __init__(self):
        pass

    def parse_output(self, filepath):
        """Reads the calculation output.
        """
        outputparser = TextParser(
            filepath,
            quantities=[
                # Header
                Quantity("datetime", fr'(?:Date\:|date)\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("hostname", fr'(?:Running on\:|hostname)\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("os", fr'(?:system)\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("user", fr'user\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("input_path", fr'(?:Input data|input data in)\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("output_path", fr'(?:Output\:|output data in)\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("executable_path", fr'(?:Executable\:|crystal executable in)\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("tmpdir", fr'(?:Temporary directory\:|temporary directory)\s+(.*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("system_type", fr'(CRYSTAL|SLAB|POLYMER|HELIX|MOLECULE|EXTERNAL|DLVINPUT)', repeats=False),
                Quantity("calculation_type", fr'(OPTGEOM|FREQCALC|ANHARM)', repeats=False),

                # Input
                Quantity(
                    "dftd3",
                    fr'(DFTD3{br}[\s\S]*?END{br})',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            "version",
                            r'(VERSION \d)',
                            str_operation=lambda x: x,
                            repeats=False,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity(
                    "grimme",
                    fr'(GRIMME{br}[\s\S]*?END{br})',
                    repeats=False,
                ),
                Quantity(
                    "dft",
                    fr'(DFT{br}[\w\s]*?END{br})',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            "exchange",
                            fr'EXCHANGE{br}(LDA|VBH|BECKE|PBE|PBESOL|mPW91|PWGGA|SOGGA|WCGGA)',
                            repeats=False,
                        ),
                        Quantity(
                            "correlation",
                            fr'CORRELAT{br}(PZ|VBH|VWN|LYP|P86|PBE|PBESOL|PWGGA|PWLSD|WL)',
                            repeats=False,
                        ),
                        Quantity(
                            "exchange_correlation",
                            fr'(SVWN|BLYP|PBEXC|PBESOLXC|SOGGAXC|B3PW|B3LYP|PBE0|PBESOL0|B1WC|WCILYP|B97H|PBE0-13|HYBRID|NONLOCAL|HSE06|HSESOL|HISS|RSHXLDA|wB97|wB97X|LC-WPBE|LC-WPBESOL|LC-WBLYP|M05-2X|M05|M062X|M06HF|M06L|M06|B2PLYP|B2GPPLYP|mPW2PLYP|DHYBRID)',
                            repeats=False,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity("program_version", fr'{br} \*\s+CRYSTAL([\d]+)\s+\*', repeats=False, dtype=str),
                Quantity("distribution", fr'{br} \*\s*({word} : \d+[\.\d+]*)', str_operation=lambda x: x, repeats=False),
                Quantity("start_timestamp", fr' EEEEEEEEEE STARTING  DATE\s+(.*? TIME .*?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("title", fr' EEEEEEEEEE STARTING  DATE.*?{br}\s*(.*?){br}{br}', str_operation=lambda x: x, repeats=False),
                Quantity("hamiltonian_type", fr' (KOHN-SHAM HAMILTONIAN|HARTREE-FOCK HAMILTONIAN)', str_operation=lambda x: x, repeats=False),
                Quantity("xc_out", fr' \(EXCHANGE\)\[CORRELATION\] FUNCTIONAL:(\([\s\S]+?\)\[[\s\S]+?\])', str_operation=lambda x: x, repeats=False),
                Quantity("hybrid_out", fr' HYBRID EXCHANGE - PERCENTAGE OF FOCK EXCHANGE\s+{flt_c}', repeats=False),

                # Geometry optimization settings
                Quantity('initial_trust_radius', fr' INITIAL TRUST RADIUS\s+{flt_c}', repeats=False),
                Quantity('maximum_trust_radius', fr' MAXIMUM TRUST RADIUS\s+{flt_c}', repeats=False),
                Quantity('maximum_gradient_component', fr' MAXIMUM GRADIENT COMPONENT\s+{flt_c}', repeats=False),
                Quantity('rms_gradient_component', fr' R\.M\.S\. OF GRADIENT COMPONENT\s+{flt_c}', repeats=False),
                Quantity('rms_displacement_component', fr' R\.M\.S\. OF DISPLACEMENT COMPONENTS\s+{flt_c}', repeats=False),
                Quantity('geometry_change', fr' MAXIMUM DISPLACEMENT COMPONENT\s+{flt_c}', unit=ureg.bohr, repeats=False),
                Quantity('energy_change', fr' THRESHOLD ON ENERGY CHANGE\s+{flt_c}', unit=ureg.hartree, repeats=False),
                Quantity('extrapolating_polynomial_order', fr' EXTRAPOLATING POLYNOMIAL ORDER{ws}{integer_c}', repeats=False),
                Quantity('max_steps', fr' MAXIMUM ALLOWED NUMBER OF STEPS\s+{integer_c}', repeats=False),
                Quantity('sorting_of_energy_points', fr'SORTING OF ENERGY POINTS\:\s+{word_c}', repeats=False),

                # System
                Quantity("material_type", fr' ((?:MOLECULAR|SLAB) CALCULATION){br}', str_operation=lambda x: x, repeats=False),
                Quantity("crystal_family", fr' CRYSTAL FAMILY\s*:\s*([\s\S]+?)\s*{br}', str_operation=lambda x: x, repeats=False),
                Quantity("crystal_class", fr' CRYSTAL CLASS  \(GROTH - 1921\)\s*:\s*([\s\S]+?)\s*{br}', str_operation=lambda x: x, repeats=False),
                Quantity("space_group", fr' SPACE GROUP \(CENTROSYMMETRIC\)\s*:\s*([\s\S]+?)\s*{br}', str_operation=lambda x: x, repeats=False),
                Quantity("dimensionality", fr' GEOMETRY FOR WAVE FUNCTION - DIMENSIONALITY OF THE SYSTEM\s+(\d)', repeats=False),
                Quantity(
                    'lattice_parameters',
                    fr' (?:PRIMITIVE CELL - CENTRING CODE\s*[\s\S]*?\s*VOLUME=\s*{flt} - DENSITY\s*{flt} g/cm\^3{br}|PRIMITIVE CELL{br})' +\
                    fr'\s+A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA.*\s+' +\
                    fr'{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}',
                    shape=(6),
                    dtype=np.float64,
                    repeats=False,
                ),
                Quantity(
                    "labels_positions",
                    fr' ATOMS IN THE ASYMMETRIC UNIT\s+{integer} - ATOMS IN THE UNIT CELL:\s+{integer}{br}' +\
                    fr'\s+ATOM\s+X(?:/A|\(ANGSTROM\))\s+Y(?:/B|\(ANGSTROM\))\s+Z(?:/C|\(ANGSTROM\))\s*{br}' +\
                    re.escape(' *******************************************************************************') +\
                    fr'((?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]*?\s+{flt}\s+{flt}\s+{flt}{br})+)',
                    shape=(-1, 7),
                    dtype=str,
                    repeats=False,
                ),

                # Used to capture an edited geometry. Can contain
                # substitutions, supercells, deformations etc. in any order.
                Quantity(
                    'system_edited',
                    fr' \*\s+GEOMETRY EDITING([\s\S]+?)T = ATOM BELONGING TO THE ASYMMETRIC UNIT',
                    # too many [\s\S] causing problems
                    # re.escape(' *******************************************************************************') + fr'{br}' +\
                    # fr' LATTICE PARAMETERS \(ANGSTROMS AND DEGREES\) - BOHR =\s*0?\.\d+ ANGSTROM{br}' +\
                    # fr' (?:PRIMITIVE CELL - CENTRING CODE [\s\S]+?VOLUME=\s*{flt} - DENSITY\s*{flt} g/cm\^3|PRIMITIVE CELL){br}' +\
                    # fr'\s+A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA\s*{br}' +\
                    # fr'(\s+{flt}\s+{flt}\s+{flt}\s+{flt}\s+{flt}\s+{flt}{br}' +\
                    # re.escape(' *******************************************************************************') + fr'{br}' +\
                    # fr' ATOMS IN THE ASYMMETRIC UNIT\s+{integer} - ATOMS IN THE UNIT CELL:\s+{integer}{br}' +\
                    # fr'\s+ATOM\s+X(?:/A|\(ANGSTROM\))\s+Y(?:/B|\(ANGSTROM\))\s+Z(?:/C|\(ANGSTROM\))(?:\s+R\(ANGS\))?\s*{br}' +\
                    # re.escape(' *******************************************************************************') +\
                    # fr'(?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]+?\s+{flt}\s+{flt}\s+{flt}(?:\s+{flt})?{br})+)' +\
                    # fr'{br}' +\
                    # fr' T = ATOM BELONGING TO THE ASYMMETRIC UNIT',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            "lattice_parameters",
                            fr'A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA.+'
                            fr'\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}',
                            shape=(6),
                            dtype=np.float64,
                            repeats=False,
                        ),
                        Quantity(
                            "labels_positions",
                            fr'\s+ATOM\s+X(?:/A|\(ANGSTROM\))\s+Y(?:/B|\(ANGSTROM\))\s+Z(?:/C|\(ANGSTROM\))\s*{br}' +\
                            re.escape(' *******************************************************************************') +\
                            fr'((?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]*?\s+{flt}\s+{flt}\s+{flt}{br})+)',
                            shape=(-1, 7),
                            dtype=str,
                            repeats=False,
                        ),
                        Quantity(
                            "labels_positions_nanotube",
                            fr'\s+ATOM\s+X/A\s+Y\(ANGSTROM\)\s+Z\(ANGSTROM\)\s+R\(ANGS\)\s*{br}' +\
                            re.escape(' *******************************************************************************') +\
                            fr'((?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]*?\s+{flt}\s+{flt}\s+{flt}\s+{flt}{br})+)',
                            shape=(-1, 8),
                            dtype=str,
                            repeats=False,
                        ),
                    ]),
                    repeats=False,
                ),

                Quantity(
                    'lattice_vectors_restart',
                    fr' DIRECT LATTICE VECTOR COMPONENTS \(ANGSTROM\){br}' +\
                    fr'\s+{flt_c}\s+{flt_c}\s+{flt_c}{br}' +\
                    fr'\s+{flt_c}\s+{flt_c}\s+{flt_c}{br}' +\
                    fr'\s+{flt_c}\s+{flt_c}\s+{flt_c}{br}',
                    shape=(3, 3),
                    dtype=np.float64,
                    repeats=False,
                ),
                Quantity(
                    "labels_positions_restart",
                    fr'   ATOM N\.AT\.  SHELL    X\(A\)      Y\(A\)      Z\(A\)      EXAD       N\.ELECT\.{br}' +\
                    re.escape(' *******************************************************************************') +\
                    fr'((?:\s+{integer}\s+{integer}\s+{word}\s+{integer}\s+{flt}\s+{flt}\s+{flt}\s+{flt}\s+{flt}{br})+)',
                    shape=(-1, 9),
                    dtype=str,
                    repeats=False,
                ),
                Quantity("symmops", fr' NUMBER OF SYMMETRY OPERATORS\s*:\s*(\d){br}', repeats=False),

                # Method
                Quantity(
                    'basis_set',
                    re.escape(r' *******************************************************************************') +\
                    fr'{br} LOCAL ATOMIC FUNCTIONS BASIS SET{br}' +\
                    re.escape(r' *******************************************************************************') +\
                    fr'{br}   ATOM   X\(AU\)   Y\(AU\)   Z\(AU\)  N. TYPE  EXPONENT  S COEF   P COEF   D/F/G COEF{br}' +\
                    fr'([\s\S]*?){br} INFORMATION',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            "basis_sets",
                            fr'({br}{ws}{integer}{ws}{word}{ws}{flt}{ws}{flt}{ws}{flt}{br}(?:(?:\s+(?:\d+-\s+)?\d+\s+(?:S|P|SP|D|F|G)\s*{br}[\s\S]*?(?:{ws}{flt}(?:{ws})?{flt}(?:{ws})?{flt}(?:{ws})?{flt}{br})+)+)?)',
                            sub_parser=TextParser(quantities=[
                                Quantity(
                                    "species",
                                    fr'{br}({ws}{integer}{ws}{word}{ws}{flt}{ws}{flt}{ws}{flt}{br})',
                                    repeats=False,
                                ),
                                Quantity(
                                    "shells",
                                    fr'(\s+(?:\d+-\s+)?\d+\s+(?:S|P|SP|D|F|G)\s*{br}[\s\S]*?(?:{ws}{flt}(?:{ws})?{flt}(?:{ws})?{flt}(?:{ws})?{flt}{br})+)',
                                    sub_parser=TextParser(quantities=[
                                        Quantity(
                                            "shell_range",
                                            r'(\s+(?:\d+-\s+)?\d+)',
                                            str_operation=lambda x: "".join(x.split()),
                                            repeats=False,
                                        ),
                                        Quantity(
                                            "shell_type",
                                            fr'((?:S|P|SP|D|F|G))\s*{br}',
                                            str_operation=lambda x: x.strip(),
                                            repeats=False,
                                        ),
                                        Quantity(
                                            "shell_coefficients",
                                            fr'{ws}({flt})(?:{ws})?({flt})(?:{ws})?({flt})(?:{ws})?({flt}){br}',
                                            repeats=True,
                                            dtype=np.float64,
                                            shape=(4)
                                        ),
                                    ]),
                                    repeats=True,
                                ),
                            ]),
                            repeats=True,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity("fock_ks_matrix_mixing", fr' INFORMATION \*+.*?\*+.*?\:\s+FOCK/KS MATRIX MIXING SET TO\s+{integer_c}\s+\%{br}', repeats=False),
                Quantity("coulomb_bipolar_buffer", fr' INFORMATION \*+.*?\*+.*?\:\s+COULOMB BIPOLAR BUFFER SET TO\s+{flt_c} Mb{br}', repeats=False),
                Quantity("exchange_bipolar_buffer", fr' INFORMATION \*+.*?\*+.*?\:\s+EXCHANGE BIPOLAR BUFFER SET TO\s+{flt_c} Mb{br}', repeats=False),
                Quantity("toldee", fr' INFORMATION \*+ TOLDEE \*+\s*\*+ SCF TOL ON TOTAL ENERGY SET TO\s+{flt_c}{br}', repeats=False),
                Quantity("n_atoms_per_cell", r' N\. OF ATOMS PER CELL\s+' + integer_c, repeats=False),
                Quantity("n_shells", r' NUMBER OF SHELLS\s+' + integer_c, repeats=False),
                Quantity("n_ao", r' NUMBER OF AO\s+' + integer_c, repeats=False),
                Quantity("n_electrons", r' N\. OF ELECTRONS PER CELL\s+' + integer_c, repeats=False),
                Quantity("n_core_electrons", r' CORE ELECTRONS PER CELL\s+' + integer_c, repeats=False),
                Quantity("n_symmops", r' N\. OF SYMMETRY OPERATORS\s+' + integer_c, repeats=False),
                Quantity("tol_coulomb_overlap", r' COULOMB OVERLAP TOL\s+\(T1\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_coulomb_penetration", r' COULOMB PENETRATION TOL\s+\(T2\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_exchange_overlap", r' EXCHANGE OVERLAP TOL\s+\(T3\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_pseudo_overlap_f", r' EXCHANGE PSEUDO OVP \(F\(G\)\)\s+\(T4\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_pseudo_overlap_p", r' EXCHANGE PSEUDO OVP \(P\(G\)\)\s+\(T5\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("pole_order", r' POLE ORDER IN MONO ZONE\s+' + integer_c, repeats=False),
                Quantity("calculation_type", fr' TYPE OF CALCULATION \:\s+(.*?{br}\s+.*?){br}', str_operation=lambda x: " ".join(x.split()), repeats=False),
                Quantity('xc_functional', fr' \(EXCHANGE\)\[CORRELATION\] FUNCTIONAL:(\(.+\)\[.+\]){br}', str_operation=lambda x: x, repeats=False,),
                Quantity("cappa", fr'CAPPA:IS1\s+{integer_c};IS2\s+{integer_c};IS3\s+{integer_c}; K PTS MONK NET\s+{integer_c}; SYMMOPS:\s*K SPACE\s+{integer_c};G SPACE\s+{integer_c}', repeats=False),
                Quantity('scf_max_iteration', r' MAX NUMBER OF SCF CYCLES\s+' + integer_c, repeats=False),
                Quantity('convergenge_deltap', r'CONVERGENCE ON DELTAP\s+' + flt_crystal_c, str_operation=to_float, repeats=False), Quantity('weight_f', r'WEIGHT OF F\(I\) IN F\(I\+1\)\s+' + integer_c, repeats=False),
                Quantity('scf_threshold_energy_change', r'CONVERGENCE ON ENERGY\s+' + flt_crystal_c, str_operation=to_float, repeats=False, unit=ureg.hartree),
                Quantity('shrink', r'SHRINK\. FACT\.\(MONKH\.\)\s+(' + integer + ws + integer + ws + integer + r')', repeats=False),
                Quantity('n_k_points_ibz', r'NUMBER OF K POINTS IN THE IBZ\s+' + integer_c, repeats=False),
                Quantity('shrink_gilat', r'SHRINKING FACTOR\(GILAT NET\)\s+' + integer_c, repeats=False),
                Quantity('n_k_points_gilat', r'NUMBER OF K POINTS\(GILAT NET\)\s+' + integer_c, repeats=False),

                # SCF
                Quantity(
                    "scf_block",
                    r' CHARGE NORMALIZATION FACTOR([\s\S]*?) == SCF ENDED',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'scf_iterations',
                            r'( CHARGE NORMALIZATION FACTOR[\s\S]*? (?:TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT PDIG|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MPP_KSPA|== SCF ENDED))',
                            sub_parser=TextParser(quantities=[
                                Quantity('charge_normalization_factor', fr' CHARGE NORMALIZATION FACTOR{ws}{flt}{br}', repeats=False),
                                Quantity('total_atomic_charges', fr' TOTAL ATOMIC CHARGES:{br}(?:{ws}{flt})+{br}', repeats=False),
                                Quantity('QGAM', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT QGAM        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}{br}', repeats=False),
                                Quantity('BIEL2', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT BIEL2        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}{br}', repeats=False),
                                Quantity('energy_kinetic', fr' ::: KINETIC ENERGY\s+{flt_c}{br}', unit=ureg.hartree, repeats=False),
                                Quantity('energy_ee', fr' ::: TOTAL E-E\s+{flt_c}{br}', unit=ureg.hartree, repeats=False),
                                Quantity('energy_en_ne', fr' ::: TOTAL E-N \+ N-E\s+{flt_c}{br}', unit=ureg.hartree, repeats=False),
                                Quantity('energy_nn', fr' ::: TOTAL N-N\s+{flt_c}{br}', unit=ureg.hartree, repeats=False),
                                Quantity('virial_coefficient', fr' ::: VIRIAL COEFFICIENT\s+{flt_c}{br}', repeats=False),
                                Quantity('TOTENY', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT TOTENY        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}{br}', repeats=False),
                                Quantity('integrated_density', fr' NUMERICALLY INTEGRATED DENSITY{ws}{flt}{br}', repeats=False),
                                Quantity('NUMDFT', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT NUMDFT        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}{br}', repeats=False),
                                Quantity('energies', fr' CYC{ws}{integer}{ws}ETOT\(AU\){ws}{flt_c}{ws}DETOT{ws}{flt_c}{ws}tst{ws}{flt}{ws}PX{ws}{flt}{br}', repeats=False, dtype=np.float64, unit=ureg.hartree),
                                Quantity('FDIK', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT FDIK        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}{br}', repeats=False),
                            ]),
                            repeats=True,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity('number_of_scf_iterations', fr' == SCF ENDED - CONVERGENCE ON (?:ENERGY|TESTER)\s+E\(AU\)\s*{flt}\s*CYCLES\s+{integer_c}', repeats=False),
                Quantity(
                    'energy_total',
                    fr' TOTAL ENERGY\((?:DFT|HF)\)\(AU\)\(\s*{integer}\)\s*{flt_c} DE\s*{flt} (?:tester|tst)\s*{flt}',
                    unit=ureg.hartree,
                    repeats=False,
                ),

                # Geometry optimization steps
                Quantity(
                    "geo_opt",
                    fr'( (?:COORDINATE AND CELL OPTIMIZATION|COORDINATE OPTIMIZATION) - POINT\s+1{br}' +\
                    r'[\s\S]*?' +\
                    re.escape(r' ******************************************************************') + fr'{br}' +\
                    fr'\s*\* OPT END - CONVERGED \* E\(AU\)\:\s+{flt}\s+POINTS\s+{integer})\s+\*{br}',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'geo_opt_step',
                            fr' (?:COORDINATE AND CELL OPTIMIZATION|COORDINATE OPTIMIZATION) - POINT\s+{integer}{br}' +\
                            fr'([\s\S]*?)' +\
                            fr' (?:TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT OPTI|\* OPT END)',
                            sub_parser=TextParser(quantities=[
                                Quantity(
                                    'lattice_parameters',
                                    fr' (?:PRIMITIVE CELL - CENTRING CODE [\s\S]*?VOLUME=\s*{flt} - DENSITY\s*{flt} g/cm\^3{br}|PRIMITIVE CELL{br})' +\
                                    fr'         A              B              C           ALPHA      BETA       GAMMA\s*' +\
                                    fr'{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}{br}',
                                    shape=(6),
                                    dtype=np.float64,
                                    repeats=False,
                                ),
                                Quantity(
                                    "labels_positions",
                                    fr'\s+ATOM\s+X(?:/A|\(ANGSTROM\))\s+Y(?:/B|\(ANGSTROM\))\s+Z(?:/C|\(ANGSTROM\))\s*{br}' +\
                                    re.escape(' *******************************************************************************') +\
                                    fr'((?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]*?\s+{flt}\s+{flt}\s+{flt}{br})+)',
                                    shape=(-1, 7),
                                    dtype=str,
                                    repeats=False,
                                ),
                                Quantity(
                                    "labels_positions_nanotube",
                                    fr'\s+ATOM\s+X/A\s+Y\(ANGSTROM\)\s+Z\(ANGSTROM\)\s+R\(ANGS\)\s*{br}' +\
                                    re.escape(' *******************************************************************************') +\
                                    fr'((?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]*?\s+{flt}\s+{flt}\s+{flt}\s+{flt}{br})+)',
                                    shape=(-1, 8),
                                    dtype=str,
                                    repeats=False,
                                ),
                                Quantity('energy', fr' TOTAL ENERGY\({word}\)\(AU\)\(\s*{integer}\)\s*{flt_c}', unit=ureg.hartree, repeats=False),
                            ]),
                            repeats=True,
                        ),
                        Quantity('converged', fr' \* OPT END - ([\s\S]*?) \* E\(AU\)\:\s+{flt}\s+POINTS\s+{integer}', repeats=False),
                    ]),
                    repeats=False,
                ),

                # Band structure
                Quantity(
                    "band_structure",
                    re.escape(fr' *******************************************************************************') + fr'{br}' +\
                    fr' \*                                                                             \*{br}' +\
                    fr' \*  BAND STRUCTURE                                                             \*{br}' +\
                    fr'[\s\S]*?' +\
                    fr' \*  FROM BAND\s+{integer} TO BAND\s+{integer}\s+\*{br}' +\
                    fr' \*  TOTAL OF\s+{integer} K-POINTS ALONG THE PATH\s+\*{br}' +\
                    fr' \*                                                                             \*{br}' +\
                    re.escape(r' *******************************************************************************') + fr'{br}' +\
                    fr'([\s\S]*?' +\
                    fr' ENERGY RANGE \(A\.U\.\)\s*{flt} - \s*{flt} EFERMI\s*{flt_c}{br})',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'segments',
                            fr' (LINE\s+{integer} \( {flt} {flt} {flt}: {flt} {flt} {flt}\) IN TERMS OF PRIMITIVE LATTICE VECTORS{br}' +\
                            fr'\s+{integer} POINTS - SHRINKING_FACTOR\s*{integer}{br}' +\
                            fr' CARTESIAN COORD\.\s+\( {flt} {flt} {flt}\):\( {flt} {flt} {flt}\) STEP\s+{flt}{br}{br}{br})',
                            sub_parser=TextParser(quantities=[
                                Quantity(
                                    'start_end',
                                    fr'LINE\s+{integer} \( {flt_c} {flt_c} {flt_c}: {flt_c} {flt_c} {flt_c}\) IN TERMS OF PRIMITIVE LATTICE VECTORS{br}',
                                    type=np.float64,
                                    shape=(2, 3),
                                    repeats=False,
                                ),
                                Quantity(
                                    'n_steps',
                                    fr'\s+{integer_c} POINTS - ',
                                    repeats=False,
                                ),
                                Quantity(
                                    'shrinking_factor',
                                    fr'SHRINKING_FACTOR\s*{integer_c}{br}',
                                    repeats=False,
                                ),
                            ]),
                            repeats=True,
                        ),
                        Quantity("fermi_energy", fr' ENERGY RANGE \(A\.U\.\)\s*{flt} - \s*{flt} EFERMI\s*{flt_c}', repeats=False),
                    ]),
                    repeats=False,
                ),

                # DOS
                Quantity(
                    'dos',
                    fr' RESTART WITH NEW K POINTS NET{br}' +\
                    fr'([\s\S]+?' +\
                    fr' TOTAL AND PROJECTED DENSITY OF STATES - FOURIER LEGENDRE METHOD{br}' +\
                    fr'[\s\S]+?)' +\
                    fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT DOSS        TELAPSE',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'k_points',
                            fr' \*\*\* K POINTS COORDINATES (OBLIQUE COORDINATES IN UNITS OF IS = {int}){br}',
                            repeats=False,
                        ),
                        Quantity(
                            'highest_occupied',
                            fr' TOP OF VALENCE BANDS -    BAND\s*{integer}; K\s*{integer}; EIG {flt_c}\s*AU',
                            unit=ureg.hartree,
                            repeats=False,
                        ),
                        Quantity(
                            'lowest_unoccupied',
                            fr' BOTTOM OF VIRTUAL BANDS - BAND\s*{integer}; K\s*{integer}; EIG\s*{flt_c}\s*AU',
                            unit=ureg.hartree,
                            repeats=False,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity("end_timestamp", fr' EEEEEEEEEE TERMINATION  DATE\s+(.*? TIME .*?){br}', str_operation=lambda x: x, repeats=False),

                # Forces
                Quantity(
                    'forces',
                    fr' CARTESIAN FORCES IN HARTREE/BOHR \(ANALYTICAL\){br}'
                    fr'   ATOM                     X                   Y                   Z{br}' +\
                    fr'((?:' + ws + integer + ws + integer + ws + flt + ws + flt + ws + flt + fr'{br})*)',
                    shape=(-1, 5),
                    dtype=str,
                    repeats=False,
                ),
                Quantity("end_timestamp", fr' EEEEEEEEEE TERMINATION  DATE\s+(.*? TIME .*?){br}', str_operation=lambda x: x, repeats=False),

                # Filepaths
                Quantity("f25_filepath1", fr'file fort\.25 saved as ([\s\S]+?){br}', str_operation=lambda x: x, repeats=False),
                Quantity("f25_filepath2", fr'BAND/MAPS/DOSS data for plotting fort.25 saved as ([\s\S]+?){br}', str_operation=lambda x: x, repeats=False),
            ]
        )

        return outputparser

    def parse_f25(self, filepath):
        """Parses the f25 file containing e.g. the band structure energies."
        """
        f25parser = TextParser(
            filepath,
            quantities=[
                # Band structure energies
                Quantity(
                    'segments',
                    fr'(-\%-0BAND\s*{integer}\s*{integer}\s?{flt}\s?{flt}\s?{flt}{br}' +\
                    fr'\s*{flt}\s*{flt}{br}' +\
                    fr'\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}{br}' +\
                    fr'(?:\s*{flt})+)',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'first_row',
                            fr'-\%-0BAND\s*{integer_c}\s*{integer_c}\s?{flt_c}\s?{flt_c}\s?{flt_c}{br}',
                            repeats=False,
                        ),
                        Quantity(
                            'second_row',
                            fr'\s?{flt_c}\s?{flt_c}{br}',
                            repeats=False,
                        ),
                        Quantity(
                            'energies',
                            fr'\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}{br}' +\
                            fr'((?:{flt}\s?)+)',
                            str_operation=lambda x: x,
                            repeats=False,
                        ),
                    ]),
                    repeats=True,
                ),
                # DOS values
                Quantity(
                    "dos",
                    fr'(-\%-0DOSS\s*{integer}\s*{integer}\s?{flt}\s?{flt}\s?{flt}{br}' +\
                    fr'\s*{flt}\s?{flt}{br}' +\
                    fr'\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}{br}' +\
                    fr'(?:\s*{flt})+)',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'first_row',
                            fr'-\%-0DOSS\s*{integer_c}\s*{integer_c}\s?{flt_c}\s?{flt_c}\s?{flt_c}{br}',
                            repeats=False,
                        ),
                        Quantity(
                            'second_row',
                            fr'\s?{flt_c}\s?{flt_c}{br}',
                            repeats=False,
                        ),
                        Quantity(
                            'values',
                            fr'\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}\s*{integer}{br}' +\
                            fr'((?:\s*{flt})+)',
                            str_operation=lambda x: x,
                            repeats=False,
                        ),
                    ]),
                    repeats=False,
                ),
            ]
        )

        return f25parser

    def parse(self, filepath, archive, logger):
        # Read files
        out = self.parse_output(filepath)
        wrkdir, _ = os.path.split(filepath)
        f25_filepath1 = out["f25_filepath1"]
        f25_filepath2 = out["f25_filepath2"]
        f25_filepath_original = f25_filepath1 if f25_filepath1 else f25_filepath2
        f25 = None
        if f25_filepath_original is not None:
            _, f25_filename = os.path.split(f25_filepath_original)
            f25_filepath = os.path.join(wrkdir, f25_filename)
            if os.path.exists(f25_filepath):
                f25 = self.parse_f25(f25_filepath)

        # Run
        run = archive.m_create(Run)
        run.program = Program(name='Crystal', version=out["program_version"])
        run.x_crystal_datetime = out["datetime"]
        run.x_crystal_hostname = out["hostname"]
        run.x_crystal_user = out["user"]
        run.x_crystal_os = out["os"]
        run.x_crystal_input_path = out["input_path"]
        run.x_crystal_output_path = out["output_path"]
        run.x_crystal_tmpdir = out["tmpdir"]
        run.x_crystal_executable_path = out["executable_path"]
        distribution = out["distribution"]
        if distribution is not None:
            dist, minor = distribution.split(" : ", 1)
            run.x_crystal_distribution = dist
            run.x_crystal_version_minor = minor
        title = out["title"]
        if title is not None:
            run.x_crystal_run_title = title.strip()
        run.time_run = TimeRun(
            date_start=to_unix_time(out["start_timestamp"]),
            date_end=to_unix_time(out["end_timestamp"]))

        # System. There are several alternative sources for this information
        # depending on the run type.
        system = run.m_create(System)
        material_type = out["material_type"]
        system_edited = out["system_edited"]
        labels_positions = out["labels_positions"]
        lattice_vectors_restart = out["lattice_vectors_restart"]
        pbc = None if material_type == "MOLECULAR CALCULATION" else np.array([True, True, True])

        # By default the system is read from the configuration at the beginning
        # of the file: it may come from restart or clean start
        atomic_numbers = None
        pos_type = {
            "MOLECULAR CALCULATION": "cartesian",
            "SLAB CALCULATION": "slab",
            None: "scaled",
        }.get(material_type)
        if labels_positions is not None:
            atomic_numbers = labels_positions[:, 2]  # pylint: disable=E1136
            atom_labels = labels_positions[:, 3]  # pylint: disable=E1136
            atom_pos = labels_positions[:, 4:7]  # pylint: disable=E1136
            lattice = out["lattice_parameters"]
        elif lattice_vectors_restart is not None:
            labels_positions = out["labels_positions_restart"]
            atomic_numbers = labels_positions[:, 1]  # pylint: disable=E1136
            atom_labels = labels_positions[:, 2]  # pylint: disable=E1136
            atom_pos = labels_positions[:, 4:7]  # pylint: disable=E1136
            lattice = lattice_vectors_restart
            pos_type = "cartesian"

        # If any geometry edits (supercells, substitutions, dispplacements,
        # deformations, nanotube construction, etc.) are done on top of the
        # original system, they override the original system.
        if system_edited is not None:
            if system_edited["labels_positions_nanotube"] is not None:  # pylint: disable=E1136
                pos_type = "nanotube"
                labels_positions = system_edited["labels_positions_nanotube"]  # pylint: disable=E1136
            else:
                labels_positions = system_edited["labels_positions"]  # pylint: disable=E1136
            # TODO adjust re pattern for other formats e.g. with R(ANGS)
            if labels_positions is not None:
                atomic_numbers = labels_positions[:, 2]  # pylint: disable=E1136
                atom_labels = labels_positions[:, 3]  # pylint: disable=E1136
                atom_pos = labels_positions[:, 4:7]  # pylint: disable=E1136
            if system_edited["lattice_parameters"] is not None:  # pylint: disable=E1136
                lattice = system_edited["lattice_parameters"]  # pylint: disable=E1136

        if atomic_numbers is None:
            # TODO define regex pattern for labels_positions to capture other versions
            logger.error('Error parsing system.')
            return

        cart_pos, atomic_numbers, atom_labels, lattice_vectors = to_system(
            atomic_numbers,
            atom_labels,
            atom_pos,
            lattice,
            pos_type=pos_type,
        )

        system.atoms = Atoms(
            lattice_vectors=lattice_vectors, periodic=pbc, positions=cart_pos,
            species=atomic_numbers, labels=atom_labels)
        dimensionality = out["dimensionality"]
        system.x_crystal_dimensionality = dimensionality
        crystal_family = out["crystal_family"]
        system.x_crystal_family = crystal_family
        crystal_class = out["crystal_class"]
        system.x_crystal_class = crystal_class
        n_symmops = out["n_symmops"]
        system.x_crystal_n_symmops = n_symmops
        space_group = out["space_group"]
        system.x_crystal_space_group = space_group

        # Method
        method = run.m_create(Method)
        method.basis_set.append(BasisSet(type='gaussians'))

        method.electronic = Electronic(method='DFT')
        method.scf = Scf(
            n_max_iteration=out["scf_max_iteration"],
            threshold_energy_change=out["scf_threshold_energy_change"])
        dftd3 = out["dftd3"]
        if dftd3:
            if dftd3["version"] == "VERSION 2":  # pylint: disable=E1136
                method.electronic.van_der_waals_method = "G06"
            else:
                method.electronic.van_der_waals_method = "DFT-D3"
        if out["grimme"]:
            method.electronic.van_der_waals_method = "G06"

        def add_functionals(functionals):
            for functional in functionals:
                if "_X_" in functional.name:
                    method.dft.xc_functional.exchange.append(functional)
                elif "_C_" in functional.name:
                    method.dft.xc_functional.correlation.append(functional)
                elif "_XC_" in functional.name or "HYB" in functional.name:
                    method.dft.xc_functional.hybrid.append(functional)
                else:
                    method.dft.xc_functional.contributions.append(functional)

        # Try to primarily read the methodology from input
        method.dft = DFT(xc_functional=XCFunctional())
        dft = out["dft"]
        if dft:
            exchange = dft["exchange"]  # pylint: disable=E1136
            correlation = dft["correlation"]  # pylint: disable=E1136
            exchange_correlation = dft["exchange_correlation"]  # pylint: disable=E1136
            functionals = to_libxc(exchange, correlation, exchange_correlation)
            if functionals:
                add_functionals(functionals)
                method.dft.xc_functional.name = to_libxc_name(functionals)

        # If methodology not reported in input, try to read from output
        if dft is None or not functionals:
            hamiltonian_type = out["hamiltonian_type"]
            if hamiltonian_type == "HARTREE-FOCK HAMILTONIAN":
                xc = Functional(name="HF_X", weight=1.0)
                method.dft.xc_functional.exchange.append(xc)
                method.dft.xc_functional.name = to_libxc_name([xc])
            elif hamiltonian_type == "KOHN-SHAM HAMILTONIAN":
                xc_output = out["xc_out"]
                hybrid = out["hybrid_out"]
                functionals = to_libxc_out(xc_output, hybrid)
                if functionals:
                    add_functionals(functionals)
                    method.dft.xc_functional.name = to_libxc_name(functionals)

        method.x_crystal_fock_ks_matrix_mixing = out["fock_ks_matrix_mixing"]
        method.x_crystal_coulomb_bipolar_buffer = out["coulomb_bipolar_buffer"]
        method.x_crystal_exchange_bipolar_buffer = out["exchange_bipolar_buffer"]
        method.x_crystal_toldee = out["toldee"]
        method.x_crystal_n_atoms = out["n_atoms_per_cell"]
        method.x_crystal_n_shells = out["n_shells"]
        method.x_crystal_n_orbitals = out["n_ao"]
        method.x_crystal_n_electrons = out["n_electrons"]
        method.x_crystal_n_core_electrons = out["n_core_electrons"]
        method.x_crystal_n_symmops = out["n_symmops"]
        method.x_crystal_tol_coulomb_overlap = out["tol_coulomb_overlap"]
        method.x_crystal_tol_coulomb_penetration = out["tol_coulomb_penetration"]
        method.x_crystal_tol_exchange_overlap = out["tol_exchange_overlap"]
        method.x_crystal_tol_pseudo_overlap_f = out["tol_pseudo_overlap_f"]
        method.x_crystal_tol_pseudo_overlap_p = out["tol_pseudo_overlap_p"]
        method.x_crystal_pole_order = out["pole_order"]
        method.x_crystal_type_of_calculation = out["calculation_type"]
        cappa = out["cappa"]
        if cappa is not None:
            method.x_crystal_is1 = cappa[0]  # pylint: disable=E1136
            method.x_crystal_is2 = cappa[1]  # pylint: disable=E1136
            method.x_crystal_is3 = cappa[2]  # pylint: disable=E1136
            method.x_crystal_k_pts_monk_net = cappa[3]  # pylint: disable=E1136
            method.x_crystal_symmops_k = cappa[4]  # pylint: disable=E1136
            method.x_crystal_symmops_g = cappa[5]  # pylint: disable=E1136
        method.x_crystal_weight_f = out["weight_f"]
        method.x_crystal_shrink = out["shrink"]
        method.x_crystal_shrink_gilat = out["shrink_gilat"]
        method.x_crystal_convergence_deltap = out["convergenge_deltap"]
        method.x_crystal_n_k_points_ibz = out["n_k_points_ibz"]
        method.x_crystal_n_k_points_gilat = out["n_k_points_gilat"]
        basis_set = out["basis_set"]
        covered_species = set()
        if basis_set is not None:
            for bs in basis_set["basis_sets"]:  # pylint: disable=E1136
                atomic_number = label_to_atomic_number(bs["species"][1])
                shells = bs["shells"]
                if atomic_number != covered_species and shells is not None:
                    section_basis_set = method.basis_set[-1].m_create(BasisSetAtomCentered)
                    section_basis_set.atom_number = atomic_number
                    covered_species.add(atomic_number)
                    for shell in shells:
                        section_shell = section_basis_set.m_create(x_crystal_section_shell)
                        section_shell.x_crystal_shell_range = str(shell["shell_range"])
                        section_shell.x_crystal_shell_type = shell["shell_type"]
                        section_shell.x_crystal_shell_coefficients = np.array(shell["shell_coefficients"])

        # SCC
        scc = run.m_create(Calculation)
        scf_block = out["scf_block"]
        if scf_block is not None:
            number_of_scf_iterations = out["number_of_scf_iterations"]
            scc.calculation_converged = number_of_scf_iterations is not None
            for scf in scf_block["scf_iterations"]:  # pylint: disable=E1136
                energies = scf["energies"]
                section_scf = scc.m_create(ScfIteration)
                section_scf.energy = Energy()
                if energies is not None:
                    section_scf.energy.total = EnergyEntry(value=energies[0])
                    section_scf.energy.change = energies[1]
                energy_kinetic = scf["energy_kinetic"]
                section_scf.energy.electronic_kinetic = EnergyEntry(value=energy_kinetic)
                energy_ee = scf["energy_ee"]
                section_scf.x_crystal_scf_energy_ee = energy_ee
                energy_en_ne = scf["energy_en_ne"]
                section_scf.x_crystal_scf_energy_en_ne = energy_en_ne
                energy_nn = scf["energy_nn"]
                section_scf.x_crystal_scf_energy_nn = energy_nn
                virial_coefficient = scf["virial_coefficient"]
                section_scf.x_crystal_scf_virial_coefficient = virial_coefficient
            scc.n_scf_iterations = len(scc.scf_iteration)

        if out["energy_total"] is not None:
            # If the final energy is found, replace the final SCF step energy
            # with it, as it is more accurate.
            if scc.scf_iteration:
                scc.scf_iteration[-1].energy.total = EnergyEntry(value=out["energy_total"])
            scc.energy = Energy(total=EnergyEntry(value=out["energy_total"]))
        forces = out["forces"]
        if forces is not None:
            scc.forces = Forces(total=ForcesEntry(value=forces[:, 2:].astype(float) * ureg.hartree / ureg.bohr))  # pylint: disable=E1136
        scc.system_ref = system
        scc.method_ref = method

        # Band structure
        band_structure = out["band_structure"]
        if band_structure is not None:
            section_band = scc.m_create(BandStructure, Calculation.band_structure_electronic)
            section_band.reciprocal_cell = atomutils.reciprocal_cell(system.atoms.lattice_vectors.magnitude) * 1 / ureg.meter
            segments = band_structure["segments"]  # pylint: disable=E1136
            k_points = to_k_points(segments)
            for i_seg, segment in enumerate(segments):
                section_segment = section_band.m_create(BandEnergies)
                _ = segment["start_end"]
                section_segment.kpoints = k_points[i_seg]
                section_segment.n_kpoints = k_points[i_seg].shape[0]

            # Read energies from the f25-file. If the file is not found, the
            # band structure is not written in the archive. The meaning of the
            # values is given in an appendix of the Crystal manual.
            if f25 is not None:
                segments = f25["segments"]
                prev_energy = None
                prev_k_point = None
                first_row = segments[0]["first_row"]
                fermi_energy = first_row[4]
                if scc.energy is None:
                    scc.energy = Energy()
                scc.energy.fermi = fermi_energy * ureg.hartree
                for i_seg, segment in enumerate(segments):
                    first_row = segment["first_row"]
                    cols = int(first_row[0])
                    rows = int(first_row[1])
                    energies = segment["energies"]
                    energies = to_array(cols, rows, energies)

                    # If a segment starts from the previous point, then
                    # re-report the energy. This way segments get the same
                    # treatment in the metainfo whether they are continuous
                    # or not.
                    start_k_point = section_band.segment[i_seg].kpoints[0]
                    end_k_point = section_band.segment[i_seg].kpoints[-1]
                    if prev_k_point is not None and np.allclose(prev_k_point, start_k_point):
                        energies = np.concatenate(([prev_energy], energies), axis=0)
                    section_band.segment[i_seg].energies = energies[None, :] * ureg.hartree
                    prev_energy = energies[-1]
                    prev_k_point = end_k_point

        # DOS
        dos = out["dos"]
        if dos is not None:
            # Read values and energies from the f25-file. If the file is not
            # found, the dos is not written in the archive. The meaning of the
            # values is given in an appendix of the Crystal manual.
            if f25 is not None:
                dos_f25 = f25["dos"]
                if dos_f25 is not None:
                    scc_dos = run.m_create(Calculation)
                    scc_dos.system_ref = system
                    scc_dos.method_ref = method
                    sec_dos = scc_dos.m_create(Dos, Calculation.dos_electronic)

                    first_row = dos_f25["first_row"]
                    cols = int(first_row[0])
                    rows = int(first_row[1])
                    de = first_row[3]
                    fermi_energy = first_row[4]
                    scc_dos.energy = Energy(fermi=fermi_energy * ureg.hartree)

                    second_row = dos_f25["second_row"]
                    start_energy = second_row[1]
                    sec_dos.energies = (start_energy + np.arange(rows) * de) * ureg.hartree

                    dos_values = dos_f25["values"]
                    dos_values = to_array(cols, rows, dos_values)
                    dos_values = dos_values.T
                    for n_spin, dos_value in enumerate(dos_values):
                        sec_dos.spin = n_spin
                        sec_dos.total.append(DosValues(value=dos_value))

        # Sampling
        geo_opt = out["geo_opt"]
        if geo_opt is not None:
            steps = geo_opt["geo_opt_step"]  # pylint: disable=E1136
            if steps is not None:
                workflow = archive.m_create(Workflow)
                archive.workflow2 = GeometryOptimization2(method=GeometryOptimizationMethod())
                workflow.type = "geometry_optimization"
                geometry_opt = workflow.m_create(GeometryOptimization)
                geometry_opt.convergence_tolerance_energy_difference = out["energy_change"]
                geometry_opt.convergence_tolerance_displacement_maximum = out["geometry_change"]
                archive.workflow2.method.convergence_tolerance_energy_difference = out["energy_change"]
                archive.workflow2.method.convergence_tolerance_displacement_maximum = out["geometry_change"]

                # First step is special: it refers to the initial system which
                # was printed before entering the geometry optimization loop.
                i_system = system
                i_energy = steps[0]["energy"]
                scc.energy.total = EnergyEntry(value=i_energy)

                frames = []
                for step in steps[1:]:
                    i_scc = run.m_create(Calculation)
                    i_system = run.m_create(System)
                    i_energy = step["energy"]
                    if step["labels_positions_nanotube"] is not None:
                        i_labels_positions = step["labels_positions_nanotube"]
                    else:
                        i_labels_positions = step["labels_positions"]
                    i_atomic_numbers = i_labels_positions[:, 2]
                    i_atom_labels = i_labels_positions[:, 3]
                    i_atom_pos = i_labels_positions[:, 4:7]
                    i_lattice_parameters = step["lattice_parameters"]
                    i_cart_pos, i_atomic_numbers, i_atom_labels, i_lattice_vectors = to_system(
                        i_atomic_numbers,
                        i_atom_labels,
                        i_atom_pos,
                        i_lattice_parameters,
                        pos_type,
                    )
                    i_system.atoms = Atoms(
                        species=i_atomic_numbers, labels=i_atom_labels, positions=i_cart_pos,
                        lattice_vectors=i_lattice_vectors, periodic=pbc)
                    i_scc.energy = Energy(total=EnergyEntry(value=i_energy))

                    i_scc.system_ref = i_system
                    i_scc.method_ref = method

                    frames.append(i_scc)
                workflow.calculations_ref = frames
                geometry_opt.is_converged_geometry = geo_opt["converged"] == "CONVERGED"  # pylint: disable=E1136

        # Remove ghost atom information. The metainfo does not provide a very
        # good way to deal with them currently so they are simply removed.
        remove_ghosts(run)


def to_k_points(segments):
    """Converts the given start and end points, the shrinking factor and the
    number of steps into a list of concrete sampling points in k-space. The
    shrinking factor tells to how many portions one reciprocal basis vector is
    divided into. This needs to be done manually as sometimes the k-points are
    not reported in the output.
    """
    all_k_points = []
    prev_point = None
    for segment in segments:
        start = segment["start_end"][0, :]
        end = segment["start_end"][1, :]
        shrinking_factor = segment["shrinking_factor"]
        n_steps = segment["n_steps"]

        # Segments that do not start from a previous segment get special
        # treatment.
        end_idx = n_steps + 1
        if prev_point is None or not np.allclose(prev_point, start):
            end_idx = n_steps
            n_steps = n_steps - 1

        delta = end - start
        start_step = (shrinking_factor * start).astype(np.int32)
        step_size = (shrinking_factor * delta / n_steps).astype(np.int32)
        steps = (start_step + step_size * np.arange(0, end_idx)[:, None])
        k_points = steps / shrinking_factor
        all_k_points.append(k_points)
        prev_point = end

    return all_k_points


def to_system(atomic_numbers, labels, positions, lattice, pos_type="scaled", wrap=False):
    """Converts a Crystal-specific structure format into cartesian positions
    and lattice vectors (if present). The conversion depends on the material
    type.
    """
    atomic_numbers = std_atomic_number(atomic_numbers.astype(np.int32))
    atom_labels = std_label(labels)
    positions = positions.astype(np.float64)

    # Get the lattice vectors
    if lattice is not None:
        if lattice.shape == (6,):
            lattice_vectors = atomutils.cellpar_to_cell(lattice, degrees=True)
        elif lattice.shape == (3, 3):
            lattice_vectors = lattice
    else:
        lattice_vectors = None

    # Convert positions based on the given type
    if pos_type == "cartesian":
        if lattice_vectors is not None and wrap:
            cart_pos = atomutils.wrap_positions(positions, lattice_vectors)
        else:
            cart_pos = positions
    elif pos_type == "slab":
        n_atoms = atomic_numbers.shape[0]
        scaled_pos = np.zeros((n_atoms, 3), dtype=np.float64)
        scaled_pos[:, 0:2] = positions[:, 0:2]
        if wrap:
            wrapped_pos = atomutils.wrap_positions(scaled_pos)
        else:
            wrapped_pos = scaled_pos
        cart_pos = atomutils.to_cartesian(wrapped_pos, lattice_vectors)
        cart_pos[:, 2:3] = positions[:, 2:3]
    elif pos_type == "nanotube":
        n_atoms = atomic_numbers.shape[0]
        scaled_pos = np.zeros((n_atoms, 3), dtype=np.float64)
        scaled_pos[:, 0:1] = positions[:, 0:1]
        if wrap:
            wrapped_pos = atomutils.wrap_positions(scaled_pos)
        else:
            wrapped_pos = scaled_pos
        cart_pos = atomutils.to_cartesian(wrapped_pos, lattice_vectors)
        cart_pos[:, 1:3] = positions[:, 1:3]
    elif pos_type == "scaled":
        scaled_pos = atomutils.wrap_positions(positions) if wrap else positions
        cart_pos = atomutils.to_cartesian(scaled_pos, lattice_vectors)

    if lattice_vectors is not None:
        lattice_vectors *= ureg.angstrom

    return cart_pos * ureg.angstrom, atomic_numbers, atom_labels, lattice_vectors


def to_float(value):
    """Transforms the Crystal-specific float notation into a floating point
    number.
    """
    base, exponent = value.split("**")
    base = int(base)
    exponent = int("".join(exponent.split()))
    return pow(base, exponent)


def to_array(cols, rows, values):
    """Transforms the Crystal-specific f25 array syntax into a numpy array.
    """
    values.replace("\n", "")
    values = textwrap.wrap(values, 12)
    values = np.array(values, dtype=np.float64)
    values = values.reshape((rows, cols))
    return values


def std_atomic_number(value):
    """Given an atomic numer in the NAT form (conventional atomic number, where
    the real atomic number is the remainder when divided by 100), return the
    actual atomic number.
    """
    return value % 100


def remove_ghosts(run):
    """Removes ghost atoms from the given section_system. In Crystal ghost
    atoms are indicated by the atomic number 0.
    """
    for system in run.system:
        ghosts_mask = system.atoms.species == 0
        if np.any(ghosts_mask):
            system.atoms.species = np.delete(system.atoms.species, ghosts_mask)
            system.atoms.labels = np.delete(system.atoms.labels, ghosts_mask)
            system.atoms.positions = np.delete(system.atoms.positions.magnitude, ghosts_mask, axis=0)


def label_to_atomic_number(value):
    """Given a Crystal specific uppercase species name, returns the
    corresponding atomic number.
    """
    symbol = value.lower().capitalize()
    atomic_number = ase.data.atomic_numbers.get(symbol, 0)
    return atomic_number


def atomic_numbers_to_labels(value):
    """Given a NAT atomic number, returns the
    corresponding label.
    """
    atomic_numbers = std_atomic_number(value)
    labels = np.array(ase.data.chemical_symbols)[atomic_numbers]
    return labels


def std_label(value):
    """Given Crystal specific uppercase species names, returns the capitalized
    versions.
    """
    labels = []
    for label in value:
        labels.append(label.lower().capitalize())
    return labels


def to_unix_time(value):
    """Transforms the Crystal-specific float notation into a floating point
    number.
    """
    if value is None:
        return None

    value = value.strip()
    date_time_obj = datetime.datetime.strptime(value, '%d %m %Y TIME %H:%M:%S.%f')
    return date_time_obj.timestamp()


def to_libxc(exchange, correlation, exchange_correlation):
    """Transforms the Crystal-specific XC naming into a list of
    section_XC_functionals.
    """
    xc_list = []

    # Handle the XC's defined with single shortcut
    if exchange_correlation:
        exchange_correlation = exchange_correlation.upper()
        shortcut_map = {
            "PBEXC": ["GGA_C_PBE", "GGA_X_PBE"],
            "PBE0": ["HYB_GGA_XC_PBEH"],
            "B3LYP": ["HYB_GGA_XC_B3LYP"],
            "HSE06": ["HYB_GGA_XC_HSE06"],
            "M06": ["MGGA_C_M06", "HYB_MGGA_X_M06"],
            "M05-2X": ["HYB_MGGA_XC_M05_2X"],
            "LC-WPBE": ["HYB_GGA_XC_LRC_WPBE"],
        }
        norm_xc = shortcut_map.get(exchange_correlation)
        if norm_xc:
            xc_list.extend(norm_xc)

    # Handle the exchange part
    if exchange:
        exchange = exchange.upper()
        exchange_map = {
            "PBE": "GGA_X_PBE",
            "PBESOL": "GGA_X_PBE_SOL",
            "BECKE": "GGA_X_B88",
            "LDA": "LDA_X",
            "PWGGA": "GGA_X_PW91",
        }
        norm_x = exchange_map.get(exchange)
        if norm_x:
            xc_list.append(norm_x)

    # Handle the correlation part
    if correlation:
        correlation = correlation.upper()
        correlation_map = {
            "PBE": "GGA_C_PBE",
            "PBESOL": "GGA_C_PBE_SOL",
            "PZ": "LDA_C_PZ",
            "WFN": "LDA_C_VWN",
            "PWGGA": "GGA_C_PW91",
        }
        norm_c = correlation_map.get(correlation)
        if norm_c:
            xc_list.append(norm_c)

    # Go throught the XC list and add the sections and gather a summary
    functionals = []
    for xc in xc_list:
        section = Functional()
        weight = 1.0
        section.name = xc
        section.weight = weight
        functionals.append(section)

    return functionals


def to_libxc_out(xc, hybridization):
    """Transforms the Crystal-specific XC naming in the output into a list of
    section_XC_functionals.
    """
    xc_list = []
    exchange, correlation = xc[1:-1].split(")[")

    # Handle the exchange part
    if exchange:
        exchange = exchange.upper()
        exchange_map = {
            "PERDEW-BURKE-ERNZERHOF": "GGA_X_PBE",
            "PERDEW-WANG GGA": "GGA_X_PW91",
            "WU-COHEN GGA": "GGA_X_WC",
        }
        norm_x = exchange_map.get(exchange)
        if norm_x:
            xc_list.append(norm_x)

    # Handle the correlation part
    if correlation:
        correlation = correlation.upper()
        correlation_map = {
            "PERDEW-BURKE-ERNZERHOF": "GGA_C_PBE",
            "PERDEW-WANG GGA": "GGA_C_PW91",
            "LEE-YANG-PARR": "GGA_C_LYP",
        }
        norm_c = correlation_map.get(correlation)
        if norm_c:
            xc_list.append(norm_c)

    # Shortcuts
    if norm_x == "GGA_X_PBE" and norm_c == "GGA_C_PBE" and hybridization == 25.00:
        section = Functional()
        section.name = "HYB_GGA_XC_PBEH"
        section.weight = 1
        return [section]

    # Go throught the XC list and add the sections and gather a summary
    functionals = []
    if hybridization:
        section = Functional()
        section.name = "HF_X"
        section.weight = float(hybridization) / 100
        functionals.append(section)
    for xc in xc_list:
        section = Functional()
        weight = 1.0
        if hybridization and "_X_" in xc:
            weight = 1.0 - float(hybridization) / 100
        section.name = xc
        section.weight = weight
        functionals.append(section)

    return functionals


def to_libxc_name(functionals):
    """Given a list of section_XC_functionals, returns the single string that
    represents them all.
    """
    return "+".join("{}*{}".format(x.weight, x.name) for x in sorted(functionals, key=lambda x: x.name))
