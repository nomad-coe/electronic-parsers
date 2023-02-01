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

import numpy as np
import logging
from ase.data import chemical_symbols

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity

from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Method, AtomParameters, DFT, XCFunctional, Functional, Electronic, BasisSet,
    BasisSetAtomCentered)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, EnergyEntry, Forces, ForcesEntry, BandEnergies,
    Charges, ChargesValue, Multipoles, MultipolesEntry
)


re_n = r'[\n\r]'
re_f = r'[-+]?\d+\.\d*(?:[Ee][-+]\d+)?'


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        key_val_quantity = Quantity('key_val', r'([A-Z]+) *= *(\S+)', repeats=True)

        def to_gradient(val_in):
            gradient = []
            for val in val_in.strip().splitlines():
                val = val.strip()
                if val and val[0].isdecimal():
                    gradient.append(val.split()[-3:])
            return np.array(gradient, dtype=np.float64) * ureg.hartree / ureg.bohr

        def to_charges(val_in):
            charges = []
            for val in val_in.strip().splitlines():
                val = val.strip()
                if val and val[0].isdecimal():
                    charges.append(val.split()[2:])
            return np.transpose(charges)

        calc_quantities = [
            Quantity(
                'scf',
                r'(SCF CALCULATION[\s\S]+?)END OF .+? CALCULATION',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        rf'ITER.+?TOTAL ENERGY.+([\s\S]+?){re_n} *{re_n}',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'iter',
                                rf'({re_f} +{re_f}).+',
                                dtype=np.dtype(np.float64), repeats=True
                            )
                        ])
                    ),
                    Quantity(
                        'energy_total',
                        rf'FINAL .+? ENERGY IS +({re_f})', unit=ureg.hartree
                    ),
                    Quantity(
                        'converged',
                        r'(DENSITY CONVERGED)', str_operation=lambda x: True
                    ),
                    Quantity(
                        'eigenvectors',
                        r'EIGENVECTORS\s+\-+([\s\S]+?)(?:\.{6}|\-{10})',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'eigenvalues',
                                rf'{re_n} +({re_f}.+)', str_operation=lambda x: x.split(), repeats=True)])
                    ),

                ])
            ),
            Quantity(
                'coordinates',
                rf'((?:COORDINATES OF ALL ATOMS ARE \(ANGS\)\s+ATOM +|ATOM +ATOMIC +COORDINATES \(BOHR\)\s+)'
                rf'CHARGE +X +Y +Z\s+\-*[\s\S]+?)INTERNUCLEAR',
                sub_parser=TextParser(quantities=[
                    Quantity('unit', r'\((\S+)\)'),
                    Quantity('label_charge', rf'([A-Z]+[a-z]*) +({re_f})', repeats=True),
                    Quantity('position', rf'({re_f} +{re_f} +{re_f}) *{re_n}', dtype=np.dtype(np.float64), repeats=True)
                ])
            ),
            Quantity(
                'gradient',
                r'ATOM +ZNUC + DE/DX +DE/DY +DE/DZ\s+\-+([\s\S]+?)MAXIMUM',
                str_operation=to_gradient
            ),
            Quantity(
                'properties',
                r'(?:properties for the|PROPERTY VALUES FOR THE|PROPERTIES FOR THE)([\s\S]+?)END OF PROPERTY EVALUATION',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_components',
                        r'ENERGY COMPONENTS\s+\-+([\s\S]+?VIRIAL RATIO.+)',
                        str_operation=lambda x: [v.strip().split('=') for v in x.strip().splitlines() if '=' in v]
                    ),
                    Quantity(
                        'population_analysis',
                        r'MULLIKEN AND LOWDIN POPULATION ANALYSES\s+\-+([\s\S]+?(?:\-{30}|\Z))',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'atomic',
                                rf'TOTAL MULLIKEN AND LOWDIN ATOMIC POPULATIONS\s+'
                                rf'ATOM +MULL.POP\. +CHARGE +LOW\.POP\. +CHARGE\s+([\s\S]+?)(?:{re_n} +[A-Z]|\Z)',
                                str_operation=to_charges
                            ),
                            Quantity(
                                'spherical_harmonics',
                                rf'SPHERICAL HARMONIC POPULATIONS\s+ATOM.+\s+([\s\S]+?)(?:{re_n} +[A-Z]|\Z)',
                                str_operation=to_charges, repeats=True
                            ),
                            Quantity(
                                'atomic_orbitals',
                                r'POPULATIONS IN EACH AO +\-+\s+MULLIKEN +LOWDIN\s+([\s\S]+?)\-\-\-\-\-',
                                str_operation=to_charges
                            ),
                            Quantity(
                                'spins',
                                r'ATOMIC SPIN POPULATION \(ALPHA MINUS BETA\)\s+ATOM.+\s+([\s\S]+?)\-\-\-\-\-',
                                str_operation=to_charges
                            )
                        ])
                    ),
                    Quantity(
                        'electrostatic_moments',
                        r'ELECTROSTATIC MOMENTS\s+\-+([\s\S]+?)\.\.\.\.\.\.',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'dipole',
                                r'(POINT +\d+[\s\S]+?DEBYE.+\s+.+)',
                                repeats=True,
                                sub_parser=TextParser(quantities=[
                                    Quantity(
                                        'origin',
                                        rf'CHARGE\s+({re_f} +{re_f} +{re_f})',
                                        dtype=np.dtype(np.float64)
                                    ),
                                    Quantity(
                                        'value',
                                        rf'DEBYE\)\s+({re_f} +{re_f} +{re_f})',
                                        dtype=np.dtype(np.float64)
                                    )
                                ])
                            )
                        ])
                    )
                ])
            )
        ]

        self._quantities = [
            Quantity(
                'program_version',
                r'GAMESS VERSION *\= *(.+?) *\*|(Firefly version [\d\.]+)',
                str_operation=lambda x: x.strip()
            ),
            Quantity(
                'x_gamess_program_implementation',
                r'\*{16} (\d+[A-Z ]+) +\*{16}',
                str_operation=lambda x: x.strip()
            ),
            Quantity(
                'x_gamess_program_execution_date',
                r'EXECUTION OF GAMESS BEGUN ([\w\: ]+)',
                str_operation=lambda x: x.strip()
            ),
            Quantity(
                'x_gamess_memory',
                r'(\d+) WORDS OF MEMORY AVAILABLE', dtype=np.int32
            ),
            Quantity(
                'basis_options',
                rf'BASIS OPTIONS\s+\-+([\s\S]+?){re_n} *{re_n} *{re_n}',
                sub_parser=TextParser(quantities=[key_val_quantity])
            ),
            Quantity(
                'control_options',
                rf'CONTRL OPTIONS\s+\-+([\s\S]+?)\$',
                sub_parser=TextParser(quantities=[key_val_quantity])
            ),
            Quantity(
                'system_options',
                rf'SYSTEM OPTIONS\s+\-+([\s\S]+?)\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-',
                sub_parser=TextParser(quantities=[key_val_quantity])
            ),
            Quantity(
                'parameters',
                rf'(NUMBER OF BASIS SET SHELLS += +\d+[\s\S]+?){re_n} *{re_n}',
                str_operation=lambda x: [v.strip().split('=') for v in x.strip().splitlines()]
            ),
            Quantity(
                'geometry_opt',
                r'GEOMETRY SEARCH POINT([\s\S]+?)(?:BEGINNING|END OF GEOMETRY SEARCH|\Z)',
                repeats=True, sub_parser=TextParser(quantities=calc_quantities)
            )
        ] + calc_quantities


class GamessParser:
    def __init__(self):
        self._nspin = None
        self._units = {'ANGS': ureg.angstrom, 'BOHR': ureg.bohr}
        self._xc_map = {
            'SLATER': [{'name': 'LDA_X'}],
            'VWN': [{'name': 'LDA_C_VWN_5'}],
            'VWN3': [{'name': 'LDA_C_VWN_3'}],
            'VWN1RPA': [{'name': 'LDA_C_VWN1RPA'}],
            'BECKE': [{'name': 'GGA_X_B88'}],
            'OPTX': [{'name': 'GGA_X_OPTX'}],
            'GILL': [{'name': 'GGA_X_G96'}],
            'PW91X': [{'name': 'GGA_X_PW91'}],
            'PBEX': [{'name': 'GGA_X_PBE'}],
            'PZ81': [{'name': 'GGA_C_PZ'}],
            'P86': [{'name': 'GGA_C_P86'}],
            'LYP': [{'name': 'GGA_C_LYP'}],
            'PW91C': [{'name': 'GGA_C_PW91'}],
            'PBEC': [{'name': 'GGA_C_PBE'}],
            'OP': [{'name': 'GGA_C_OP'}],
            'SVWN': [{'name': 'LDA_C_VWN_5'}, {'name': 'LDA_X'}],
            'SVWN1RPA': [{'name': 'LDA_C_VWN1RPA'}, {'name': 'LDA_X'}],
            'SVWN3': [{'name': 'LDA_C_VWN_3'}, {'name': 'LDA_X'}],
            'SPZ81': [{'name': 'GGA_C_PZ'}, {'name': 'LDA_X'}],
            'SP86': [{'name': 'GGA_C_P86'}, {'name': 'LDA_X'}],
            'SLYP': [{'name': 'GGA_C_LYP'}, {'name': 'LDA_X'}],
            'SPW91': [{'name': 'GGA_C_PW91'}, {'name': 'LDA_X'}],
            'SPBE': [{'name': 'GGA_C_PBE'}, {'name': 'LDA_X'}],
            'SOP': [{'name': 'GGA_C_OP'}, {'name': 'LDA_X'}],
            'BVWN': [{'name': 'LDA_C_VWN_5'}, {'name': 'LDA_X_B88'}],
            'BVWN1RPA': [{'name': 'LDA_C_VWN1RPA'}, {'name': 'LDA_X_B88'}],
            'BVWN3': [{'name': 'LDA_C_VWN_3'}, {'name': 'LDA_X_B88'}],
            'BPZ81': [{'name': 'GGA_C_PZ'}, {'name': 'LDA_X_B88'}],
            'BP86': [{'name': 'GGA_C_P86'}, {'name': 'LDA_X_B88'}],
            'BLYP': [{'name': 'GGA_C_LYP'}, {'name': 'LDA_X_B88'}],
            'BPW91': [{'name': 'GGA_C_PW91'}, {'name': 'LDA_X_B88'}],
            'BPBE': [{'name': 'GGA_C_PBE'}, {'name': 'LDA_X_B88'}],
            'BOP': [{'name': 'GGA_C_OP'}, {'name': 'LDA_X_B88'}],
            'GVWN': [{'name': 'LDA_C_VWN_5'}, {'name': 'GGA_X_G96'}],
            'GVWN1RPA': [{'name': 'LDA_C_VWN1RPA'}, {'name': 'GGA_X_G96'}],
            'GVWN3': [{'name': 'LDA_C_VWN_3'}, {'name': 'GGA_X_G96'}],
            'GPZ81': [{'name': 'GGA_C_PZ'}, {'name': 'GGA_X_G96'}],
            'GP86': [{'name': 'GGA_C_P86'}, {'name': 'GGA_X_G96'}],
            'GLYP': [{'name': 'GGA_C_LYP'}, {'name': 'GGA_X_G96'}],
            'GPW91': [{'name': 'GGA_C_PW91'}, {'name': 'GGA_X_G96'}],
            'GPBE': [{'name': 'GGA_C_PBE'}, {'name': 'GGA_X_G96'}],
            'GOP': [{'name': 'GGA_C_OP'}, {'name': 'GGA_X_G96'}],
            'OVWN': [{'name': 'LDA_C_VWN_5'}, {'name': 'GGA_X_OPTX'}],
            'OVWN1RPA': [{'name': 'LDA_C_VWN1RPA'}, {'name': 'GGA_X_OPTX'}],
            'OVWN3': [{'name': 'LDA_C_VWN_3'}, {'name': 'GGA_X_OPTX'}],
            'OPZ81': [{'name': 'GGA_C_PZ'}, {'name': 'GGA_X_OPTX'}],
            'OP86': [{'name': 'GGA_C_P86'}, {'name': 'GGA_X_OPTX'}],
            'OLYP': [{'name': 'GGA_C_LYP'}, {'name': 'GGA_X_OPTX'}],
            'OPW91': [{'name': 'GGA_C_PW91'}, {'name': 'GGA_X_OPTX'}],
            'OPBE': [{'name': 'GGA_C_PBE'}, {'name': 'GGA_X_OPTX'}],
            'OOP': [{'name': 'GGA_C_OP'}, {'name': 'GGA_X_OPTX'}],
            'PW91VWN': [{'name': 'LDA_C_VWN_5'}, {'name': 'GGA_X_PW91'}],
            'PW91VWN1RPA': [{'name': 'LDA_C_VWN1RPA'}, {'name': 'GGA_X_PW91'}],
            'PW91VWN3': [{'name': 'LDA_C_VWN_3'}, {'name': 'GGA_X_PW91'}],
            'PW91PZ81': [{'name': 'GGA_C_PZ'}, {'name': 'GGA_X_PW91'}],
            'PW91P86': [{'name': 'GGA_C_P86'}, {'name': 'GGA_X_PW91'}],
            'PW91LYP': [{'name': 'GGA_C_LYP'}, {'name': 'GGA_X_PW91'}],
            'PW91': [{'name': 'GGA_C_PW91'}, {'name': 'GGA_X_PW91'}],
            'PW91PBE': [{'name': 'GGA_C_PBE'}, {'name': 'GGA_X_PW91'}],
            'PW91OP': [{'name': 'GGA_C_OP'}, {'name': 'GGA_X_PW91'}],
            'PBEVWN': [{'name': 'LDA_C_VWN_5'}, {'name': 'GGA_X_PBE'}],
            'PBEVWN1RPA': [{'name': 'LDA_C_VWN1RPA'}, {'name': 'GGA_X_PBE'}],
            'PBEVWN3': [{'name': 'LDA_C_VWN_3'}, {'name': 'GGA_X_PBE'}],
            'PBEPZ81': [{'name': 'GGA_C_PZ'}, {'name': 'GGA_X_PBE'}],
            'PBEP86': [{'name': 'GGA_C_P86'}, {'name': 'GGA_X_PBE'}],
            'PBELYP': [{'name': 'GGA_C_LYP'}, {'name': 'GGA_X_PBE'}],
            'PBEPW91': [{'name': 'GGA_C_PW91'}, {'name': 'GGA_X_PBE'}],
            'PBE': [{'name': 'GGA_C_PBE'}, {'name': 'GGA_X_PBE'}],
            'PBEOP': [{'name': 'GGA_C_OP'}, {'name': 'GGA_X_PBE'}],
            'EDF1': [{'name': 'GGA_XC_EDF1'}],
            'REVPBE': [{'name': 'GGA_XC_REVPBE'}],
            'RPBE': [{'name': 'GGA_XC_RPBE'}],
            'PBESOL': [{'name': 'GGA_XC_PBESOL'}],
            'HCTH93': [{'name': 'GGA_XC_HCTH_93'}],
            'HCTH147': [{'name': 'GGA_XC_HCTH_147'}],
            'HCTH407': [{'name': 'GGA_XC_HCTH_407'}],
            'SOGGA': [{'name': 'GGA_XC_SOGGA'}],
            'SOGGA11': [{'name': 'GGA_XC_SOGGA11'}],
            'MOHLYP': [{'name': 'GGA_XC_MOHLYP'}],
            'B97-D': [{'name': 'GGA_XC_B97D'}],
            'BHHLYP': [{'name': 'HYB_GGA_XC_BHANDHLYP'}],
            'B3PW91': [{'name': 'HYB_GGA_XC_B3PW91'}],
            'B3LYP': [{'name': 'HYB_GGA_XC_B3LYP'}],
            'B3LYPV1R': [{'name': 'HYB_GGA_XC_B3LYPVWN1RPA'}],
            'B3LYPV3': [{'name': 'HYB_GGA_XC_B3LYPVWN3'}],
            'B3P86': [{'name': 'HYB_GGA_XC_B3P86'}],
            'B3P86V1R': [{'name': 'HYB_GGA_XC_B3P86VWN1RPA'}],
            'B3P86V5': [{'name': 'HYB_GGA_XC_B3P86VWN5'}],
            'B97': [{'name': 'HYB_GGA_XC_B97'}],
            'B97-1': [{'name': 'HYB_GGA_XC_B971'}],
            'B97-2': [{'name': 'HYB_GGA_XC_B972'}],
            'B97-3': [{'name': 'HYB_GGA_XC_B973'}],
            'B97-K': [{'name': 'HYB_GGA_XC_B97K'}],
            'B98': [{'name': 'HYB_GGA_XC_B98'}],
            'PBE0': [{'name': 'HYB_GGA_XC_PBEH'}],
            'X3LYP': [{'name': 'HYB_GGA_XC_X3LYP'}],
            'SOGGA11X': [{'name': 'HYB_GGA_XC_SOGGA11X'}],
            'CAMB3LYP': [{'name': 'CAM-B3LYP'}],
            'WB97': [{'name': 'WB97'}],
            'WB97X': [{'name': 'WB97X'}],
            'WB97X-D': [{'name': 'WB97XD'}],
            'B2-PLYP': [{'name': 'B2PLYP'}],
            'B2K-PLYP': [{'name': 'B2KPLYP'}],
            'B2T-PLYP': [{'name': 'B2TPLYP'}],
            'B2GP-PLYP': [{'name': 'B2GPPLYP'}],
            'WB97X-2': [{'name': 'WB97X2'}],
            'WB97X-2L': [{'name': 'WB97X2L'}],
            'VS98': [{'name': 'MGGA_XC_VSXC'}],
            'PKZB': [{'name': 'MGGA_XC_PKZB'}],
            'THCTH': [{'name': 'MGGA_XC_TAU_HCTH'}],
            'THCTHHYB': [{'name': 'MGGA_XC_TAU_HCTHHYB'}],
            'BMK': [{'name': 'MGGA_XC_BMK'}],
            'TPSS': [{'name': 'MGGA_XC_TPSS'}],
            'TPSSH': [{'name': 'MGGA_XC_TPSSHYB'}],
            'TPSSM': [{'name': 'MGGA_XC_TPSSMOD'}],
            'REVTPSS': [{'name': 'MGGA_XC_REVISEDTPSS'}],
            'DLDF': [{'name': 'MGGA_XC_DLDF'}],
            'M05': [{'name': 'HYB_MGGA_XC_M05'}],
            'M05-2X': [{'name': 'HYB_MGGA_XC_M05_2X'}],
            'M06': [{'name': 'MGGA_C_M06'}, {'name': 'HYB_MGGA_X_M06'}],
            'M06-L': [{'name': 'MGGA_C_M06_L'}, {'name': 'MGGA_X_M06_L'}],
            'M06-2X': [{'name': 'MGGA_C_M06_2X'}, {'name': 'HYB_MGGA_X_M06_2X'}],
            'M06-HF': [{'name': 'MGGA_C_M06_HF'}, {'name': 'HYB_MGGA_X_M06_HF'}],
            'M08-HX': [{'name': 'MGGA_C_M08_HX'}, {'name': 'HYB_MGGA_X_M08_HX'}],
            'M08-SO': [{'name': 'MGGA_C_M08_SO'}, {'name': 'HYB_MGGA_X_M08_SO'}],
            'M11-L': [{'name': 'MGGA_C_M11_L'}, {'name': 'MGGA_X_M11_L'}],
            'M11': [{'name': 'MGGA_C_M11_L'}, {'name': 'MGGA_X_M11'}],
            'RHF': [{'name': 'RHF_X'}],
            'UHF': [{'name': 'UHF_X'}],
            'ROHF': [{'name': 'ROHF_X'}],
            'LCBOPLRD': [{'name': 'HYB_GGA_XC_HSE03'}],
            'XALPHA': [{'name': 'XALPHA_X_GRIDFREE'}],
            'DEPRISTO': [{'name': 'DEPRISTO_X_GRIDFREE'}],
            'CAMA': [{'name': 'CAMA_X_GRIDFREE'}],
            'HALF': [{'name': 'HYB_GGA_XC_HALF_GRIDFREE'}],
            # 'VWN': [{'name': 'LDA_C_VWN5_GRIDFREE'}],
            'PWLOC': [{'name': 'PWLOC_C_GRIDFREE'}],
            'BPWLOC': [{'name': 'PWLOC_C_GRIDFREE'}, {'name': 'GGA_X_B88_GRIDFREE'}],
            'CAMB': [{'name': 'GGA_C_CAMBRIDGE_GRIDFREE'}, {'name': 'GGA_X_CAMA_GRIDFREE'}],
            'XVWN': [{'name': 'LDA_C_VWN5_GRIDFREE'}, {'name': 'XALPHA_X_GRIDFREE'}],
            'XPWLOC': [{'name': 'GGA_C_PW91_GRIDFREE'}, {'name': 'XALPHA_X_GRIDFREE'}],
            'SPWLOC': [{'name': 'PWLOC_C_GRIDFREE'}, {'name': 'LDA_X_GRIDFREE'}],
            'WIGNER': [{'name': 'GGA_XC_WIGNER_GRIDFREE'}],
            'WS': [{'name': 'GGA_XC_WIGNER_GRIDFREE'}],
            'WIGEXP': [{'name': 'GGA_XC_WIGNER_GRIDFREE'}],
            'NONE': [{'name': 'NONE'}],
        }
        self._method_map = {
            'RHF': [{'name': 'RHF'}],
            'UHF': [{'name': 'UHF'}],
            'ROHF': [{'name': 'ROHF'}],
            'GVB': [{'name': 'GVB'}],
            'MCSCF': [{'name': 'MCSCF'}],
            'EXCITE': [{'name': 'TDDFT'}],
            'SPNFLP': [{'name': 'SF-TDDFT'}],
            'POL': [{'name': 'HYPERPOL'}],
            'VB2000': [{'name': 'VB'}],
            'CIS': [{'name': 'CIS'}],
            'SFCIS': [{'name': 'SF-CIS'}],
            'ALDET': [{'name': 'DET-MCSCF'}],
            'ORMAS': [{'name': 'ORMAS'}],
            'FSOCI': [{'name': 'SECONDORDER-CI'}],
            'GENCI': [{'name': 'GENERAL-CI'}],
            'LCCD': [{'name': 'L-CCSD'}],
            'CCD': [{'name': 'CCD'}],
            'CCSD': [{'name': 'CCSD'}],
            'CCSD(T)': [{'name': 'CCSD(T)'}],
            'R-CC': [{'name': 'R-CCSD(T)&R-CCSD[T]'}],
            'CR-CC': [{'name': 'CR-CCSD(T)&CR-CCSD[T]'}],
            'CR-CCL': [{'name': 'CR-CC(2,3)'}],
            'CCSD(TQ)': [{'name': 'CCSD(TQ)&R-CCSD(TQ)'}],
            'CR-CC(Q)': [{'name': 'CR-CCSD(TQ)'}],
            'EOM-CCSD': [{'name': 'EOM-CCSD'}],
            'CR-EOM': [{'name': 'CR-EOMCCSD(T)'}],
            'CR-EOML': [{'name': 'CR-EOMCC(2,3)'}],
            'IP-EOM2': [{'name': 'IP-EOMCCSD'}],
            'IP-EOM3A': [{'name': 'IP-EOMCCSDt'}],
            'EA-EOM2': [{'name': 'EA-EOMCCSD'}],
            'EA-EOM3A': [{'name': 'EA-EOMCCSDt'}],
            'IOTC': [{'name': 'SCALAR_RELATIVISTIC'}],
            'DK': [{'name': 'SCALAR_RELATIVISTIC'}],
            'RESC': [{'name': 'SCALAR_RELATIVISTIC'}],
            'NESC': [{'name': 'SCALAR_RELATIVISTIC'}],
            'SBKJC': [{'name': 'PSEUDO_SCALAR_RELATIVISTIC'}],
            'HW': [{'name': 'PSEUDO_SCALAR_RELATIVISTIC'}],
            'MCP': [{'name': 'PSEUDO_SCALAR_RELATIVISTIC'}],
            'TAMMD': [{'name': 'TAMM-DANCOFF'}],
            'DFTB': [{'name': 'DFTB'}],
            'MP2': [{'name': 'MP2'}],
            'RIMP2': [{'name': 'RESOLUTIONOFIDENTITY-MP2'}],
            'CPHF': [{'name': 'COUPLEDPERTURBED-HF'}],
            'G3MP2': [{'name': 'G3(MP2)'}],
            'G32CCSD': [{'name': 'G3(MP2,CCSD(T))'}],
            'G4MP2': [{'name': 'G4(MP2)'}],
            'G4MP2-6X': [{'name': 'G4(MP2)-6X'}],
            'CCCA-S4': [{'name': 'CCCA-S4'}],
            'CCCA-CCL': [{'name': 'CCCA-CC(2,3)'}],
            'MCQDPT': [{'name': 'MCQDPT2'}],
            'DETMRPT': [{'name': 'MRPT2'}],
            'FORS': [{'name': 'CASSCF'}],
            'FOCI': [{'name': 'FIRSTORDER-CI'}],
            'SOCI': [{'name': 'SECONDORDER-CI'}],
            'DM': [{'name': 'TRANSITIONMOMENTS'}],
            'HSO1': [{'name': 'ONEELEC-SOC'}],
            'HSO2P': [{'name': 'PARTIALTWOELEC-SOC'}],
            'HSO2': [{'name': 'TWOELEC-SOC'}],
            'HSO2FF': [{'name': 'TWOELECFORMFACTOR-SOC'}],
            'GUGA': [{'name': 'GUGA-CI'}],
            'NONE': [{'name': 'NOCORRELATEDMETHOD'}],
        }
        self._basis_set_map = {
            'STO': [{'name': 'STO'}],
            'N21': [{'name': 'N21'}],
            'N31': [{'name': 'N31'}],
            'N311': [{'name': 'N311'}],
            'MINI': [{'name': 'MINI'}],
            'MIDI': [{'name': 'MIDI'}],
            'DZV': [{'name': 'DZV'}],
            'DH': [{'name': 'DH'}],
            'TZV': [{'name': 'TZV'}],
            'MC': [{'name': 'MC'}],
            'G3L': [{'name': 'G3MP2LARGE'}],
            'G3LX': [{'name': 'G3MP2LARGEXP'}],
            'CCD': [{'name': 'CC_PVDZ'}],
            'CCT': [{'name': 'CC_PVTZ'}],
            'CCQ': [{'name': 'CC_PVQZ'}],
            'CC5': [{'name': 'CC_PV5Z'}],
            'CC6': [{'name': 'CC_PV6Z'}],
            'ACCD': [{'name': 'AUG-CC-PVDZ'}],
            'ACCT': [{'name': 'AUG-CC-PVTZ'}],
            'ACCQ': [{'name': 'AUG-CC-PVQZ'}],
            'ACC5': [{'name': 'AUG-CC-PV5Z'}],
            'ACC6': [{'name': 'AUG-CC-PV6Z'}],
            'CCDC': [{'name': 'CC-PCVDZ'}],
            'CCTC': [{'name': 'CC-PCVTZ'}],
            'CCQC': [{'name': 'CC-PCVQZ'}],
            'CC5C': [{'name': 'CC-PCV5Z'}],
            'CC6C': [{'name': 'CC-PCV6Z'}],
            'ACCDC': [{'name': 'AUG-CC-PCVDZ'}],
            'ACCTC': [{'name': 'AUG-CC-PCVTZ'}],
            'ACCQC': [{'name': 'AUG-CC-PCVQZ'}],
            'ACC5C': [{'name': 'AUG-CC-PCV5Z'}],
            'ACC6C': [{'name': 'AUG-CC-PCV6Z'}],
            'CCDWC': [{'name': 'CC-PWCVDZ'}],
            'CCTWC': [{'name': 'CC-PWCVTZ'}],
            'CCQWC': [{'name': 'CC-PWCVQZ'}],
            'CC5WC': [{'name': 'CC-PWCV5Z'}],
            'CC6WC': [{'name': 'CC-PWCV6Z'}],
            'ACCDWC': [{'name': 'AUG-CC-PWCVDZ'}],
            'ACCTWC': [{'name': 'AUG-CC-PWCVTZ'}],
            'ACCQWC': [{'name': 'AUG-CC-PWCVQZ'}],
            'ACC5WC': [{'name': 'AUG-CC-PWCV5Z'}],
            'ACC6WC': [{'name': 'AUG-CC-PWCV6Z'}],
            'PCSEG-0': [{'name': 'PCSEG-0'}],
            'PCSEG-1': [{'name': 'PCSEG-1'}],
            'PCSEG-2': [{'name': 'PCSEG-2'}],
            'PCSEG-3': [{'name': 'PCSEG-3'}],
            'PCSEG-4': [{'name': 'PCSEG-4'}],
            'APCSEG-0': [{'name': 'AUG-PCSEG-0'}],
            'APCSEG-1': [{'name': 'AUG-PCSEG-1'}],
            'APCSEG-2': [{'name': 'AUG-PCSEG-2'}],
            'APCSEG-3': [{'name': 'AUG-PCSEG-3'}],
            'APCSEG-4': [{'name': 'AUG-PCSEG-4'}],
            'SPK-DZP': [{'name': 'SPK-DZP'}],
            'SPK-DTP': [{'name': 'SPK-DTP'}],
            'SPK-DQP': [{'name': 'SPK-DQP'}],
            'SPK-ADZP': [{'name': 'AUG-SPK-DZP'}],
            'SPK-ATZP': [{'name': 'AUG-SPK-TZP'}],
            'SPK-AQZP': [{'name': 'AUG-SPK-QZP'}],
            'SPKRDZP': [{'name': 'SPK-RELDZP'}],
            'SPKRDTP': [{'name': 'SPK-RELDTP'}],
            'SPKRDQP': [{'name': 'SPK-RELDQP'}],
            'SPKRADZP': [{'name': 'AUG-SPK-RELDZP'}],
            'SPKRATZP': [{'name': 'AUG-SPK-RELTZP'}],
            'SPKRAQZP': [{'name': 'AUG-SPK-RELQZP'}],
            'SPK-DZC': [{'name': 'SPK-DZC'}],
            'SPK-TZC': [{'name': 'SPK-TZC'}],
            'SPK-QZC': [{'name': 'SPK-QZC'}],
            'SPK-DZCD': [{'name': 'SPK-DZCD'}],
            'SPK-TZCD': [{'name': 'SPK-TZCD'}],
            'SPK-QZCD': [{'name': 'SPK-QZCD'}],
            'SPKRDZC': [{'name': 'SPK-RELDZC'}],
            'SPKRTZC': [{'name': 'SPK-RELTZC'}],
            'SPKRQZC': [{'name': 'SPK-RELQZC'}],
            'SPKRDZCD': [{'name': 'SPK-RELDZCD'}],
            'SPKRTZCD': [{'name': 'SPK-RELTZCD'}],
            'SPKRQZCD': [{'name': 'SPK-RELQZCD'}],
            'KTZV': [{'name': 'KARLSRUHETZV'}],
            'KTZVP': [{'name': 'KARLSRUHETZVP'}],
            'KTZVPP': [{'name': 'KARLSRUHETZVPP'}],
            'MCP-DZP': [{'name': 'MCP-DZP'}],
            'MCP-TZP': [{'name': 'MCP-TZP'}],
            'MCP-QZP': [{'name': 'MCP-QZP'}],
            'MCP-ATZP': [{'name': 'AUG-MCP-TZP'}],
            'MCP-AQZP': [{'name': 'AUG-MCP-QZP'}],
            'MCPCDZP': [{'name': 'MCPCDZP'}],
            'MCPCTZP': [{'name': 'MCPCTZP'}],
            'MCPCQZP': [{'name': 'MCPCQZP'}],
            'MCPACDZP': [{'name': 'AUG-MCPCDZP'}],
            'MCPACTZP': [{'name': 'AUG-MCPCTZP'}],
            'MCPACQZP': [{'name': 'AUG-MCPCQZP'}],
            'IMCP-SR1': [{'name': 'IMPROVEDMCP-SCALREL1'}],
            'IMCP-SR2': [{'name': 'IMPROVEDMCP-SCALREL2'}],
            'ZFK3-DK3': [{'name': 'ZFK3-DK3'}],
            'ZFK4-DK3': [{'name': 'ZFK4-DK3'}],
            'ZFK5-DK3': [{'name': 'ZFK5-DK3'}],
            'ZFK3LDK3': [{'name': 'ZFK3LDK3'}],
            'ZFK4LDK3': [{'name': 'ZFK4LDK3'}],
            'ZFK5LDK3': [{'name': 'ZFK5LDK3'}],
            'SLATER-MNDO': [{'name': 'SLATER-MNDO'}],
            'AM1': [{'name': 'SLATER-AM1'}],
            'PM3': [{'name': 'SLATER-PM3'}],
            'RM1': [{'name': 'SLATER-RM1'}],
            'DFTB': [{'name': 'SLATER-DFTB'}]
        }
        self._metainfo_map = {
            'one electron': 'x_gamess_one_electron',
            'two electron': 'x_gamess_two_electron',
            'virial ratio (v/t)': 'x_gamess_virial_ratio'
        }

        self.out_parser = OutParser()

    @property
    def nspin(self):
        if self._nspin is None:
            for key, val in self.out_parser.get('control_options', {}).get('key_val', []):
                if key == 'MULT':
                    self._nspin = 1 if val == 1 else 2
                    break
        return self._nspin

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger
        self._nspin = None

    def parse_method(self):
        sec_method = self.archive.run[-1].m_create(Method)

        for key in ['basis', 'control', 'system']:
            setattr(sec_method, 'x_gamess_%s_options' % key, {
                key: val for key, val in self.out_parser.get('%s_options' % key, {}).get('key_val', [])})

        for key, val in self.out_parser.get('basis_options', {}).get('key_val', []):
            setattr(sec_method, 'x_gamess_basis_set_%s' % key.lower(), val)

        for value in self.out_parser.get('coordinates', {}).get('label_charge', []):
            atom = sec_method.m_create(AtomParameters)
            atom.label = value[0]
            atom.charge = float(value[1]) * ureg.elementary_charge

        def resolve_basis(gbasis):
            # basis_set_name = self._basis_set_map.get(gbasis)
            igauss = sec_method.x_gamess_basis_options.get('IGAUSS', 'NONE')

            if gbasis == 'STO':
                return f'STO-{igauss}G'

            symbol, igauss = ('G', f'{igauss}-') if gbasis.startswith('N') else ('', '')
            gbasis = gbasis.lstrip('N')

            plus = ''
            for orb in ['SP', 'P']:
                if sec_method.x_gamess_basis_options.get(f'DIFF{orb}', 'NONE').startswith('T'):
                    plus += '+'

            orb_suffix = ''
            for orb in ['d', 'f', 'p']:
                nfunc = sec_method.x_gamess_basis_options.get(f'N{orb.upper()}FUNC', 0)
                prefix = '' if nfunc == 0 else orb if nfunc == 1 else f'{nfunc}{orb}'
                orb_suffix += f',{prefix}' if orb == 'p' and orb_suffix and prefix else prefix
            orb_suffix = f'({orb_suffix})' if orb_suffix else orb_suffix

            return f'{igauss}{gbasis}{plus}{symbol}{orb_suffix}'

        gbasis = sec_method.x_gamess_basis_options.get('GBASIS', 'NONE')
        sec_basis = sec_method.m_create(BasisSet)
        sec_basis.name = resolve_basis(gbasis)
        for basis_set in self._basis_set_map.get(gbasis, []):
            sec_atom_basis = sec_basis.m_create(BasisSetAtomCentered)
            sec_atom_basis.name = basis_set.get('name')

        # electronic structure method
        sec_method.electronic = Electronic()
        relativity = sec_method.x_gamess_control_options.get(
            'RELWFN', sec_method.x_gamess_control_options.get('PP', 'NONE'))
        if relativity != 'NONE':
            for method in self._method_map.get(relativity, []):
                sec_method.electronic.relativity_method = method.get('name', '').lower()

        scf_type = sec_method.x_gamess_control_options.get('SCFTYP', 'NONE')
        run_type = sec_method.x_gamess_control_options.get('RUNTYP', 'NONE')
        mp_level = sec_method.x_gamess_control_options.get('MPLEVL', 'NONE')
        methods = [sec_method.x_gamess_control_options.get(
            key, 'NONE') for key in ['CITYP', 'CCTYP', 'VBTYP', 'TDDFT']]
        methods = [m for m in methods if m != 'NONE']
        electronic_method = scf_type if scf_type != 'NONE' else methods[0] if methods else run_type
        if scf_type in ['RHF', 'UHF', 'ROHF'] and mp_level == 2:
            sec_method.electronic.method = 'MP2'
        elif scf_type == 'MCSCF':
            sec_method.electronic.method = 'MRPT2' if mp_level == 2 else 'MCSCF'
        elif electronic_method != 'NONE':
            for method in self._method_map.get(electronic_method, []):
                sec_method.electronic.method = method.get('name')

        # dft xc functional
        dfttyp = sec_method.x_gamess_control_options.get('DFTTYP', 'NONE')
        if dfttyp != 'NONE':
            sec_method.dft = DFT(xc_functional=XCFunctional())
            for functional in self._xc_map.get(dfttyp, []):
                xc_functional = functional.get('name', '')
                if '_X_' in xc_functional or xc_functional.endswith('_X'):
                    sec_method.dft.xc_functional.exchange.append(Functional(name=xc_functional))
                elif '_C_' in xc_functional or xc_functional.endswith('_C'):
                    sec_method.dft.xc_functional.correlation.append(Functional(name=xc_functional))
                elif 'HYB' in xc_functional:
                    sec_method.dft.xc_functional.hybrid.append(Functional(name=xc_functional))
                else:
                    sec_method.dft.xc_functional.contributions.append(Functional(name=xc_functional))

    def parse_calculation(self, source):
        sec_scc = self.archive.run[-1].m_create(Calculation)
        if source.scf is not None:
            for iteration in source.scf.get('iteration', {}).get('iter', []):
                sec_scf = sec_scc.m_create(ScfIteration)
                sec_scf.energy = Energy(
                    total=EnergyEntry(value=iteration[0] * ureg.hartree),
                    change=iteration[1] * ureg.hartree)

            sec_scc.energy = Energy(total=EnergyEntry(value=source.scf.energy_total))
            sec_scc.calculation_converged = source.scf.converged

            eigenvalues = source.scf.get('eigenvectors', {}).get('eigenvalues')
            if eigenvalues is not None:
                sec_eigenvalues = sec_scc.m_create(BandEnergies)
                eigenvalues = np.array(np.hstack(eigenvalues), dtype=np.float64)
                shape = (self.nspin, 1, np.size(eigenvalues) // self.nspin)
                sec_eigenvalues.energies = np.reshape(eigenvalues, shape) * ureg.hartree
                sec_eigenvalues.occupations = np.reshape(
                    np.array([2 if energy <= 0. else 0 for energy in eigenvalues]) / self.nspin, shape)

        properties = source.get('properties')
        if properties is not None:
            energies = {key.strip().lower(): val for key, val in properties.get('energy_components', [])}
            sec_energy = sec_scc.m_create(Energy)
            for key, val in energies.items():
                # if key.endswith('potential energy') or key.endswith('kinetic energy'):
                #     continue
                if key.endswith('energy'):
                    key = key.rstrip('energy').strip()
                    potential = energies.get(f'{key} potential energy')
                    # kinetic = energies.get(f'{key} kinetic energy')
                    key = self._metainfo_map.get(key, key).replace(' ', '_')
                    if hasattr(Energy, key) or key.startswith('x_gamess'):
                        setattr(sec_energy, key, EnergyEntry(
                            value=val * ureg.hartree,
                            potential=potential * ureg.hartree if potential else potential,
                            # kinetic=kinetic * ureg.hartree if kinetic else kinetic
                        ))
                    else:
                        sec_energy.contributions.append(EnergyEntry(kind=key, value=val * ureg.hartree))
                else:
                    setattr(sec_energy, self._metainfo_map.get(key, f'x_gamess_{key}'), val)

            population = properties.get('population_analysis')
            if population is not None:
                methods = ['Mulliken', 'Lowdin']
                for n, method in enumerate(methods):
                    sec_charges = sec_scc.m_create(Charges)
                    sec_charges.analysis_method = method
                    if population.atomic is not None:
                        sec_charges.value = population.atomic[n * 2 + 1] * ureg.elementary_charge
                    if population.atomic_orbitals is not None:
                        for norbital, orbital in enumerate(population.atomic_orbitals[1]):
                            sec_orbital_charges = sec_charges.m_create(ChargesValue, Charges.orbital_projected)
                            sec_orbital_charges.atom_index = population.atomic_orbitals[0][norbital]
                            sec_orbital_charges.orbital = str(orbital)
                            sec_orbital_charges.value = float(population.atomic_orbitals[2 + n][norbital]) * ureg.elementary_charge
                    if population.spins is not None:
                        sec_charges.spins = population.spins[n]

                orbitals = ['s', 'p', 'd', 'f', 'g', 'h', 'i']
                for nspin, charges in enumerate(population.get('spherical_harmonics', [])[:2]):
                    for norbital in range(len(charges[:-1])):
                        for natom in range(len(charges[norbital])):
                            sec_orbital_charges = sec_scc.charges[0].m_create(ChargesValue, Charges.orbital_projected)
                            sec_orbital_charges.atom_index = natom
                            sec_orbital_charges.spin = nspin
                            sec_orbital_charges.orbital = orbitals[norbital]
                            sec_orbital_charges.value = charges[norbital][natom] * ureg.elementary_charge

            moments = properties.get('electrostatic_moments')
            if moments is not None:
                for dipole in moments.get('dipole', []):
                    sec_multipoles = sec_scc.m_create(Multipoles)
                    sec_multipoles.kind = 'electrostatic'
                    sec_multipoles.dipole = MultipolesEntry(
                        # origin=dipole.get('origin'),
                        value=dipole.get('value'))

        if source.get('gradient') is not None:
            sec_scc.forces = Forces(total=ForcesEntry(value=source.gradient))

    def parse_system(self, source):
        coordinates = source.get('coordinates', self.out_parser.coordinates)
        if coordinates is not None:
            sec_system = self.archive.run[0].m_create(System)
            unit = self._units.get(coordinates.get('unit'), 1)
            sec_system.atoms = Atoms(
                labels=[chemical_symbols[int(lc[1])] for lc in coordinates.get('label_charge', [])],
                positions=np.array([p for p in coordinates.get('position', [])], dtype=np.float64) * unit)

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.init_parser()

        run = archive.m_create(Run)
        run.program = Program(version=self.out_parser.get('program_version'))
        for key, val in self.out_parser.items():
            if key.startswith('x_gamess_'):
                setattr(run, key, val)

        self.parse_method()

        if self.out_parser.get('geometry_opt') is not None:
            for geometry_opt in self.out_parser.get('geometry_opt', []):
                self.parse_system(geometry_opt)
                self.parse_calculation(geometry_opt)
                run.calculation[-1].system_ref = run.system[-1]
                run.calculation[-1].method_ref = run.method[-1]
        else:
            self.parse_system(self.out_parser)
            self.parse_calculation(self.out_parser)
            run.calculation[-1].system_ref = run.system[-1]
            run.calculation[-1].method_ref = run.method[-1]

        # TODO
        # thermochemistry
        # parameters, output for diff methods e.g. mp2, cc, ci
