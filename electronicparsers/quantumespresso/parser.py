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
import re
from datetime import datetime
import os

from nomad.units import ureg
from nomad.parsing import FairdiParser
from nomad.parsing.file_parser.text_parser import TextParser, Quantity, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program, TimeRun
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, DFT, Smearing, XCFunctional, Functional, BasisSet,
    BasisSetCellDependent, AtomParameters
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, Stress, StressEntry,
    Thermodynamics, BandEnergies, ScfIteration, Dos, DosValues
)
from nomad.datamodel.metainfo.workflow import Workflow
from .metainfo.quantum_espresso import (
    x_qe_section_scf_diagonalization, x_qe_section_bands_diagonalization,
    x_qe_section_compile_options, x_qe_section_parallel)


# origin: espresso-5.4.0/Modules/funct.f90
# update:
# . New exchange-correlation functionals exist in
# .     espresso-6.5.0/Modules/funct.f90
#   short comments mark the corresponding new metainfo
_exchange_map = [
    None,
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'sla',
            'x_qe_xc_iexch_comment': 'Slater (alpha=2/3)',
            'x_qe_xc_iexch': 1,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_X',
            'XC_functional_parameters': {'alpha': 1.0},
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'sl1',
            'x_qe_xc_iexch_comment': 'Slater (alpha=1.0)',
            'x_qe_xc_iexch': 2,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'x_qe_LDA_X_RELATIVISTIC',
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'rxc',
            'x_qe_xc_iexch_comment': 'Relativistic Slater',
            'x_qe_xc_iexch': 3,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'OEP_EXX',
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'oep',
            'x_qe_xc_iexch_comment': 'Optimized Effective Potential',
            'x_qe_xc_iexch': 4,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'HF_X',
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'hf',
            'x_qe_xc_iexch_comment': 'Hartree-Fock',
            'x_qe_xc_iexch': 5,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.25,
        }, {
            'XC_functional_name': 'LDA_X',
            'exx_compute_weight': lambda exx: (1.0 - exx),
            'XC_functional_weight': 0.75,
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'pb0x',
            'x_qe_xc_iexch_comment': 'PBE0 (Slater*0.75+HF*0.25)',
            'x_qe_xc_iexch': 6,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.20,
        }, {
            'XC_functional_name': 'LDA_X',
            'exx_compute_weight': lambda exx: (1.0 - exx),
            'XC_functional_weight': 0.8,
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'b3lp',
            'x_qe_xc_iexch_comment': 'B3LYP(Slater*0.80+HF*0.20)',
            'x_qe_xc_iexch': 7,
        },
    },
    # LDA_X_KZK is not part of libXC. Look up it at
    # 'https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-meta-info/wikis/metainfo/XC-functional'
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_X_KZK',
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'kzk',
            'x_qe_xc_iexch_comment': 'Finite-size corrections',
            'x_qe_xc_iexch': 8,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.218,
        }, {
            'XC_functional_name': 'LDA_X',
            'exx_compute_weight': lambda exx: (1.0 - exx),
            'XC_functional_weight': 0.782,
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'x3lp',
            'x_qe_xc_iexch_comment': 'X3LYP(Slater*0.782+HF*0.218)',
            'x_qe_xc_iexch': 9,
        },
    },
    # update for espresso-6.5.0: KLI
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_X_KLI',
        }],
        'xc_section_method': {
            'x_qe_xc_iexch_name': 'kli',
            'x_qe_xc_iexch_comment': 'KLI aproximation for exx',
            'x_qe_xc_iexch': 10,
        },
    },
]

# Correlation functionals UNchanged between espresso v5.4 & v6.5
_correlation_map = [
    None,
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_PZ',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'pz',
            'x_qe_xc_icorr_comment': 'Perdew-Zunger',
            'x_qe_xc_icorr': 1,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_VWN',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'vwn',
            'x_qe_xc_icorr_comment': 'Vosko-Wilk-Nusair',
            'x_qe_xc_icorr': 2,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_LYP',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'lyp',
            'x_qe_xc_icorr_comment': 'Lee-Yang-Parr',
            'x_qe_xc_icorr': 3,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'pw',
            'x_qe_xc_icorr_comment': 'Perdew-Wang',
            'x_qe_xc_icorr': 4,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_WIGNER',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'wig',
            'x_qe_xc_icorr_comment': 'Wigner',
            'x_qe_xc_icorr': 5,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_HL',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'hl',
            'x_qe_xc_icorr_comment': 'Hedin-Lunqvist',
            'x_qe_xc_icorr': 6,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_OB_PZ',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'obz',
            'x_qe_xc_icorr_comment': 'Ortiz-Ballone form for PZ',
            'x_qe_xc_icorr': 7,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_OB_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'obw',
            'x_qe_xc_icorr_comment': 'Ortiz-Ballone form for PW',
            'x_qe_xc_icorr': 8,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_GL',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'gl',
            'x_qe_xc_icorr_comment': 'Gunnarson-Lunqvist',
            'x_qe_xc_icorr': 9,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_KZK',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'kzk',
            'x_qe_xc_icorr_comment': 'Finite-size corrections',
            'x_qe_xc_icorr': 10,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_VWN_RPA',
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'vwn-rpa',
            'x_qe_xc_icorr_comment': 'Vosko-Wilk-Nusair, alt param',
            'x_qe_xc_icorr': 11,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_VWN',
            'XC_functional_weight': 0.19,
        }, {
            'XC_functional_name': 'LDA_C_LYP',
            'XC_functional_weight': 0.81,
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'b3lp',
            'x_qe_xc_icorr_comment': 'B3LYP (0.19*vwn+0.81*lyp)',
            'x_qe_xc_icorr': 12,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_VWN_RPA',
            'XC_functional_weight': 0.19,
        }, {
            'XC_functional_name': 'LDA_C_LYP',
            'XC_functional_weight': 0.81,
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'b3lpv1r',
            'x_qe_xc_icorr_comment': 'B3LYP-VWN-1-RPA (0.19*vwn_rpa+0.81*lyp)',
            'x_qe_xc_icorr': 13,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'LDA_C_VWN_RPA',
            'XC_functional_weight': 0.129,
        }, {
            'XC_functional_name': 'LDA_C_LYP',
            'XC_functional_weight': 0.871,
        }],
        'xc_section_method': {
            'x_qe_xc_icorr_name': 'x3lp',
            'x_qe_xc_icorr_comment': 'X3LYP (0.129*vwn_rpa+0.871*lyp)',
            'x_qe_xc_icorr': 14,
        },
    },
]

# New 'exchange_gradient_correction' functionals for q-espresso (qe) v6.5
#    igcx=[1..28] unchanged between qe-v5.4 & v6.5
# New additions: igcx=[29..42]

_exchange_gradient_correction_map = [
    None,
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_B88',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'b88',
            'x_qe_xc_igcx_comment': 'Becke88 (beta=0.0042)',
            'x_qe_xc_igcx': 1,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_PW91',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'ggx',
            'x_qe_xc_igcx_comment': 'Perdew-Wang 91',
            'x_qe_xc_igcx': 2,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_PBE',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'pbx',
            'x_qe_xc_igcx_comment': 'Perdew-Burke-Ernzenhof exch',
            'x_qe_xc_igcx': 3,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_PBE_R',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'rpb',
            'x_qe_xc_igcx_comment': 'revised PBE by Zhang-Yang',
            'x_qe_xc_igcx': 4,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_XC_HCTH_120',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'hcth',
            'x_qe_xc_igcx_comment': 'Cambridge exch, Handy et al, HCTH/120',
            'x_qe_xc_igcx': 5,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_OPTX',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'optx',
            'x_qe_xc_igcx_comment': "Handy's exchange functional",
            'x_qe_xc_igcx': 6,
        },
    },
    {
        # igcx=7 is not defined in 5.4's funct.f90
        #        definition taken from 5.0, which did not have separate imeta
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_TPSS',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'tpss',
            'x_qe_xc_igcx_comment': 'TPSS Meta-GGA (Espresso-version < 5.1)',
            'x_qe_xc_igcx': 7,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_PBE',
            'XC_functional_weight': 0.75,
            'exx_compute_weight': lambda exx: (1.0 - exx),
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
            'XC_functional_weight': 0.75,
            'exx_compute_weight': lambda exx: (1.0 - exx),
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'pb0x',
            'x_qe_xc_igcx_comment': 'PBE0 (PBE exchange*0.75)',
            'x_qe_xc_igcx': 8,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_B88',
            'XC_functional_weight': 0.72,
            'exx_compute_weight': lambda exx: 0.72 if abs(exx) > 0.01 else 1.0
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
            'XC_functional_weight': 0.8,
            'exx_compute_weight': lambda exx: (1.0 - exx),
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'b3lp',
            'x_qe_xc_igcx_comment': 'B3LYP (Becke88*0.72)',
            'x_qe_xc_igcx': 9,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_PBE_SOL',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'psx',
            'x_qe_xc_igcx_comment': 'PBEsol exchange',
            'x_qe_xc_igcx': 10,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_WC',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'wcx',
            'x_qe_xc_igcx_comment': 'Wu-Cohen',
            'x_qe_xc_igcx': 11,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'HYB_GGA_XC_HSE06',
            'exx_compute_weight': lambda exx: 1.0 if (abs(exx) > 0.01) else 0.0
        }, {
            'XC_functional_name': 'GGA_X_PBE',
            'exx_compute_weight': lambda exx: 0.0 if (abs(exx) > 0.01) else 1.0
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }, {
            'XC_functional_name': 'GGA_C_PBE',
            'exx_compute_weight': lambda exx: 1.0 if (abs(exx) > 0.01) else 0.0
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'hse',
            'x_qe_xc_igcx_comment': 'HSE screened exchange',
            'x_qe_xc_igcx': 12,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RPW86',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'rw86',
            'x_qe_xc_igcx_comment': 'revised PW86',
            'x_qe_xc_igcx': 13,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_PBE',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'pbe',
            'x_qe_xc_igcx_comment': 'same as PBX, back-comp.',
            'x_qe_xc_igcx': 14,
        },
    },
    {
        # igcx=15 is not defined in 5.4's funct.f90
        #        definition taken from 5.0, which did not have separate imeta
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_TB09',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'tb09',
            'x_qe_xc_igcx_comment': 'TB09 Meta-GGA (Espresso-version < 5.1)',
            'x_qe_xc_igcx': 15,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_C09X',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'c09x',
            'x_qe_xc_igcx_comment': 'Cooper 09',
            'x_qe_xc_igcx': 16,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_SOGGA',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'sox',
            'x_qe_xc_igcx_comment': 'sogga',
            'x_qe_xc_igcx': 17,
        },
    },
    {
        # igcx=18 is not defined in 5.4's funct.f90
        #        definition taken from 5.0, which did not have separate imeta
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_M06_L',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'm6lx',
            'x_qe_xc_igcx_comment': 'M06L Meta-GGA (Espresso-version < 5.1)',
            'x_qe_xc_igcx': 18,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_Q2D',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'q2dx',
            'x_qe_xc_igcx_comment': 'Q2D exchange grad corr',
            'x_qe_xc_igcx': 19,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'HYB_GGA_XC_GAU_PBE',
            'exx_compute_weight': lambda exx: 1.0 if (abs(exx) > 0.01) else 0.0
        }, {
            'XC_functional_name': 'GGA_X_PBE',
            'exx_compute_weight': lambda exx: 0.0 if (abs(exx) > 0.01) else 1.0
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }, {
            'XC_functional_name': 'GGA_C_PBE',
            'exx_compute_weight': lambda exx: 1.0 if (abs(exx) > 0.01) else 0.0
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'gaup',
            'x_qe_xc_igcx_comment': 'Gau-PBE hybrid exchange',
            'x_qe_xc_igcx': 20,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_PW86',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'pw86',
            'x_qe_xc_igcx_comment': 'Perdew-Wang (1986) exchange',
            'x_qe_xc_igcx': 21,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_B86_MGC',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'b86b',
            'x_qe_xc_igcx_comment': 'Becke (1986) exchange',
            'x_qe_xc_igcx': 22,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_OPTB88_VDW',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'obk8',
            'x_qe_xc_igcx_comment': 'optB88  exchange',
            'x_qe_xc_igcx': 23,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_OPTB86_VDW',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'ob86',
            'x_qe_xc_igcx_comment': 'optB86b exchange',
            'x_qe_xc_igcx': 24,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_EV93',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'evx',
            'x_qe_xc_igcx_comment': 'Engel-Vosko exchange',
            'x_qe_xc_igcx': 25,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_B86_R',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'b86r',
            'x_qe_xc_igcx_comment': 'revised Becke (b86b)',
            'x_qe_xc_igcx': 26,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_LV_RPW86',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'cx13',
            'x_qe_xc_igcx_comment': 'consistent exchange',
            'x_qe_xc_igcx': 27,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_B88',
            'XC_functional_weight': 0.542,
            'exx_compute_weight':
                lambda exx: 0.542 if (abs(exx) > 0.01) else 1.0
        }, {
            'XC_functional_name': 'GGA_X_PW91',
            'XC_functional_weight': 0.167,
            'exx_compute_weight':
                lambda exx: 0.167 if (abs(exx) > 0.01) else 0.0
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
            'exx_compute_weight':
                lambda exx: 0.709 if (abs(exx) > 0.01) else 1.0
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'x3lp',
            'x_qe_xc_igcx_comment': 'X3LYP (Becke88*0.542 '
                                    ' + Perdew-Wang91*0.167)',
            'x_qe_xc_igcx': 28,
        },
    },
    # New additions for qe-v6.5.0: igcx=[29..42]
    # - - - - - -
    # igcx: 29. The ingredient 'vdW-DF-cx' is documented in the nomad-meta-info, where it
    # has the name 'vdw_c_df_cx'
    # 'https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-meta-info/-/wikis/metainfo/XC-functional':
    # 'vdW-DF-cx' implies igcx=27 => 'cx13', hence LDA_X is implicit. Full weight.
    {
        'xc_terms': [{
            'XC_functional_name': 'vdw_c_df_cx',
        }, {
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.25,
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'cx0',
            'x_qe_xc_igcx_comment': 'vdW-DF-cx+HF/4 (cx13-0)',
            'x_qe_xc_igcx': 29,
        },
    },
    # - - - - - -
    # igcx:30. Needs full LDA_X removal, due to 'GGA_X_RPW86' (see igcx:27)
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RPW86',
        }, {
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.25,
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'r860',
            'x_qe_xc_igcx_comment': 'rPW86+HF/4 (rw86-0); (for DF0)',
            'x_qe_xc_igcx': 30,
        },
    },
    # - - - - - -
    # igcx:31. Similar comments as in 'igcx:29'
    {
        'xc_terms': [{
            'XC_functional_name': 'vdw_c_df_cx',
        }, {
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.20,
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'cx0p',
            'x_qe_xc_igcx_comment': 'vdW-DF-cx+HF/5 (cx13-0p)',
            'x_qe_xc_igcx': 31,
        },
    },
    # - - - - - -
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RESERVED',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'ahcx',
            'x_qe_xc_igcx_comment': 'vdW-DF-cx based; not yet in use (reserved PH)',
            'x_qe_xc_igcx': 32,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RESERVED',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'ahf2',
            'x_qe_xc_igcx_comment': 'vdW-DF2 based; not yet in use (reserved PH)',
            'x_qe_xc_igcx': 33,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RESERVED',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'ahpb',
            'x_qe_xc_igcx_comment': 'PBE based; not yet in use (reserved PH)',
            'x_qe_xc_igcx': 34,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RESERVED',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'ahps',
            'x_qe_xc_igcx_comment': 'PBE-sol based; not in use (reserved PH)',
            'x_qe_xc_igcx': 35,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RESERVED',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'cx14',
            'x_qe_xc_igcx_comment': 'Exporations (typo?: explorations), (reserved PH)',
            'x_qe_xc_igcx': 36,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RESERVED',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'cx15',
            'x_qe_xc_igcx_comment': 'Exporations (typo? explorations?)(reserved PH)',
            'x_qe_xc_igcx': 37,
        },
    },
    #
    # igcx': 38. Ingredients:
    #   'b86r' -> 'igcx:26' -> 'GGA_X_B86_R'
    #   'vdW-DF2' -> 'vdw_c_df2' . See nomad's gitlab:
    #   'https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-meta-info/-/wikis/metainfo/XC-functional':
    {
        'xc_terms': [{
            'XC_functional_name': 'vdw_c_df2',
        }, {
            'XC_functional_name': 'GGA_X_B86_R',
        }, {
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.25,
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'br0',
            'x_qe_xc_igcx_comment': 'vdW-DF2-b86r+HF/4 (b86r-0)',
            'x_qe_xc_igcx': 38,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_RESERVED',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'cx16',
            'x_qe_xc_igcx_comment': 'Exporations (typo?, explorations?)(reserved PH)',
            'x_qe_xc_igcx': 39,
        },
    },
    # - - - -
    {
        'xc_terms': [{
            'XC_functional_name': 'vdw_c_df1',
        }, {
            'XC_functional_name': 'GGA_X_C09X',
        }, {
            'XC_functional_name': 'HF_X',
            'exx_compute_weight': lambda exx: exx,
            'XC_functional_weight': 0.25,
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'c090',
            'x_qe_xc_igcx_comment': 'vdW-DF-c09+HF/4 (c09-0)',
            'x_qe_xc_igcx': 40,
        },
    },
    # - - - - - - -
    # 'igcx:41' Note: 'B86b' is defined in 'igcx:22'
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_B86_MGC',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
            'XC_functional_weight': 0.75,
            'exx_compute_weight': lambda exx: (1.0 - exx),
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'b86x',
            'x_qe_xc_igcx_comment': 'B86b exchange * 0.75',
            'x_qe_xc_igcx': 41,
        },
    },
    # - - - - - - -
    # 'B88' is defined in 'igcx:1'
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_X_B88',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
            'XC_functional_weight': 0.50,
            'exx_compute_weight': lambda exx: (1.0 - exx),
        }],
        'xc_section_method': {
            'x_qe_xc_igcx_name': 'b88x',
            'x_qe_xc_igcx_comment': 'B88 exchange * 0.50',
            'x_qe_xc_igcx': 42,
        },
    },
]

# UNchanged between espresso v5.4 & v6.5
_correlation_gradient_correction_map = [
    None,
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_P86',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'p86',
            'x_qe_xc_igcc_comment': 'Perdew86',
            'x_qe_xc_igcc': 1,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_PW91',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'ggc',
            'x_qe_xc_igcc_comment': 'Perdew-Wang 91 corr.',
            'x_qe_xc_igcc': 2,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_LYP',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_LYP',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'blyp',
            'x_qe_xc_igcc_comment': 'Lee-Yang-Parr',
            'x_qe_xc_igcc': 3,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_PBE',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'pbc',
            'x_qe_xc_igcc_comment': 'Perdew-Burke-Ernzenhof corr',
            'x_qe_xc_igcc': 4,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_XC_HCTH_120',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'hcth',
            'x_qe_xc_igcc_comment': 'Cambridge exch, Handy et al, HCTH/120',
            'x_qe_xc_igcc': 5,
        },
    },
    {
        # igcc=6 is not defined in 5.4's funct.f90
        #        definition taken from 5.0, which did not have separate imeta
        'xc_terms': [{
            'XC_functional_name': 'MGGA_C_TPSS',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'tpss',
            'x_qe_xc_igcc_comment': 'TPSS Meta-GGA (Espresso-version < 5.1)',
            'x_qe_xc_igcc': 6,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_LYP',
            'XC_functional_weight': 0.81,
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_LYP',
            'XC_functional_weight': 0.81,
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'b3lp',
            'x_qe_xc_igcc_comment': 'B3LYP (Lee-Yang-Parr*0.81)',
            'x_qe_xc_igcc': 7,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_PBE_SOL',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'psc',
            'x_qe_xc_igcc_comment': 'PBEsol corr',
            'x_qe_xc_igcc': 8,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_PBE',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'pbe',
            'x_qe_xc_igcc_comment': 'same as PBX, back-comp.',
            'x_qe_xc_igcc': 9,
        },
    },
    {
        # igcc=10 is not defined in 5.4's funct.f90
        #        definition taken from 5.0, which did not have separate imeta
        #        functionals.f90 tells that correlation is taken from tpss
        'xc_terms': [{
            'XC_functional_name': 'MGGA_C_TPSS',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'tb09',
            'x_qe_xc_igcc_comment': 'TB09 Meta-GGA (Espresso-version < 5.1)',
            'x_qe_xc_igcc': 10,
        },
    },
    {
        # igcc=11 is not defined in 5.4's funct.f90
        #        definition taken from 5.0, which did not have separate imeta
        'xc_terms': [{
            'XC_functional_name': 'MGGA_C_M06_L',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'm6lc',
            'x_qe_xc_igcc_comment': 'M06L Meta-GGA (Espresso-version < 5.1)',
            'x_qe_xc_igcc': 11,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_Q2D',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'q2dc',
            'x_qe_xc_igcc_comment': 'Q2D correlation grad corr',
            'x_qe_xc_igcc': 12,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_LYP',
            'XC_functional_weight': 0.871,
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_LYP',
            'XC_functional_weight': 0.871,
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'x3lp',
            'x_qe_xc_igcc_comment': 'X3LYP (Lee-Yang-Parr*0.871)',
            'x_qe_xc_igcc': 13,
        },
    },
    {
        #  igcc=14 is not defined in NEITHER of v5.1, v6.1, v6.4's Modules/funct.f90
        # 'BEEF-vdW, a GGA with vdW-DF2 type nonlocal correlation'
        'xc_terms': [{
            'XC_functional_name': 'GGA_C_BEEF-vdW',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_igcc_name': 'BEEF-vdW',
            'x_qe_xc_igcc_comment': 'libbeef V0.1.1 library',
            'x_qe_xc_igcc': 14,
        },
    },
]

# New additions for espresso-6.5.0: imeta=[4, 5, 6]
_meta_gga_map = [
    None,
    {
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_TPSS',
        }, {
            'XC_functional_name': 'MGGA_C_TPSS',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }, {
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_imeta_name': 'tpss',
            'x_qe_xc_imeta_comment': 'TPSS Meta-GGA',
            'x_qe_xc_imeta': 1,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_M06_L',
        }, {
            'XC_functional_name': 'MGGA_C_M06_L',
        }],
        'xc_section_method': {
            'x_qe_xc_imeta_name': 'm6lx',
            'x_qe_xc_imeta_comment': 'M06L Meta-GGA',
            'x_qe_xc_imeta': 2,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_TB09',
        }, {
            # confirmed by looking into functionals.f90
            'XC_functional_name': 'MGGA_C_TPSS',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }, {
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_imeta_name': 'tb09',
            'x_qe_xc_imeta_comment': 'TB09 Meta-GGA',
            'x_qe_xc_imeta': 3,
        },
    },
    # imeta = [4,5,6] are new espresso-6.5.0/Modules/funct.f90
    {
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_TPSS',
        }, {
            'XC_functional_name': 'MGGA_C_TPSS',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }, {
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_imeta_name': '+meta',
            'x_qe_xc_imeta_comment': 'activate MGGA even without MGGA-XC',
            'x_qe_xc_imeta': 4,
        },
    },
    # - - - - - - - -
    {
        'xc_terms': [{
            'XC_functional_name': 'MGGA_X_SCAN',
        }, {
            'XC_functional_name': 'MGGA_C_SCAN',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }, {
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_imeta_name': 'scan',
            'x_qe_xc_imeta_comment': 'SCAN Meta-GGA ',
            'x_qe_xc_imeta': 5,
        },
    },
    # - - - - - - - -
    {
        'xc_terms': [{
            'XC_functional_name': 'HYB_MGGA_X_SCAN0',
        }, {
            'XC_functional_name': 'MGGA_C_SCAN',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_X',
        }, {
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_imeta_name': 'sca0',
            'x_qe_xc_imeta_comment': 'SCAN0  Meta-GGA',
            'x_qe_xc_imeta': 6,
        },
    },
]

_van_der_waals_map = [
    None,
    {
        'xc_terms': [{
            'XC_functional_name': 'VDW_C_DF1',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_inlc_name': 'vdw1',
            'x_qe_xc_inlc_comment': 'vdW-DF1',
            'x_qe_xc_inlc': 1,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'VDW_C_DF2',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'LDA_C_PW',
        }],
        'xc_section_method': {
            'x_qe_xc_inlc_name': 'vdw2',
            'x_qe_xc_inlc_comment': 'vdW-DF2',
            'x_qe_xc_inlc': 2,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'VDW_C_RVV10',
        }],
        'xc_terms_remove': [{
            'XC_functional_name': 'GGA_C_PBE',
        }],
        'xc_section_method': {
            'x_qe_xc_inlc_name': 'vv10',
            'x_qe_xc_inlc_comment': 'rVV10',
            'x_qe_xc_inlc': 3,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'VDW_DFX_x_qe',
        }],
        'xc_section_method': {
            'x_qe_xc_inlc_name': 'vdwx',
            'x_qe_xc_inlc_comment': 'vdW-DF-x (reserved Thonhauser,'
                                    ' not implemented)',
            'x_qe_xc_inlc': 4,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'VDW_DFY_x_qe',
        }],
        'xc_section_method': {
            'x_qe_xc_inlc_name': 'vdwy',
            'x_qe_xc_inlc_comment': 'vdW-DF-y (reserved Thonhauser,'
                                    ' not implemented)',
            'x_qe_xc_inlc': 5,
        },
    },
    {
        'xc_terms': [{
            'XC_functional_name': 'VDW_DFZ_x_qe',
        }],
        'xc_section_method': {
            'x_qe_xc_inlc_name': 'vdwz',
            'x_qe_xc_inlc_comment': 'vdW-DF-z (reserved Thonhauser,'
                                    ' not implemented)',
            'x_qe_xc_inlc': 6,
        },
    },
]

_libxc_shortcut = {
    '0.810*GGA_C_LYP+0.720*GGA_X_B88+0.200*HF_X+0.190*LDA_C_VWN': {
        'xc_terms': [{
            'XC_functional_name': 'HYB_GGA_XC_B3LYP',
        }]
    },
    'GGA_C_PBE+0.750*GGA_X_PBE+0.250*HF_X': {
        'xc_terms': [{
            'XC_functional_name': 'HYB_GGA_XC_PBEH',
        }]
    },
}


class QuantumEspressoRunParser(TextParser):
    def __init__(self, quantities):
        super().__init__(quantities=quantities)
        self._xc_functional_map = [
            _exchange_map, _correlation_map, _exchange_gradient_correction_map,
            _correlation_gradient_correction_map, _van_der_waals_map, _meta_gga_map]

    def copy(self):
        return QuantumEspressoRunParser(self._quantities)

    def get_header(self, key, default=None):
        return self.get('header', {}).get(key, default)

    def get_xc_functional(self):
        xc_functional = self.get_header('xc_functional')
        if xc_functional is None:
            return {}, []

        _, numbers = xc_functional.split('(')
        numbers = numbers.split(')')[0]
        # handle different formatting
        if len(numbers) == 4:
            # 4-digit format without spaces
            numbers_split = re.findall(r'(\d)', numbers)
        elif len(numbers) == 10:
            # 5-digit format with/without spaces
            numbers_split = re.findall(r'[ \d]\d', numbers)
        else:
            # 6-digit with spaces
            numbers_split = numbers.split()

        if not numbers_split:
            self.logger.warn('Unknown XC functional format', data=dict(value=numbers))
        numbers_split = [int(n) for n in numbers_split]

        # numbers should have six digits
        numbers_split.extend([0] * (6 - len(numbers_split)))

        def gen_string(data, separator='+'):
            string = ''
            for key in sorted(data.keys()):
                val = data[key]
                if len(string) > 0 and val.get('XC_functional_weight', 1.0) > 0:
                    string += separator
                if val.get('XC_functional_weight', None) is not None:
                    string += '%.3f*' % (val['XC_functional_weight'])
                string += val['XC_functional_name']
            return string

        def get_data(source):
            data = dict()
            exx_fraction = self.get_header('x_qe_exact_exchange_fraction', 0.0)
            for term in source:
                term = term.copy()
                weight = term.get('exx_compute_weight', 1.0)
                if not isinstance(weight, float):
                    weight = weight(exx_fraction)
                term['XC_functional_weight'] = weight
                data.setdefault(term['XC_functional_name'], term)
            return data

        def filter_data(data):
            out = dict()
            for key, val in data.items():
                if abs(val['XC_functional_weight']) < 0.01:
                    continue
                else:
                    if abs(val['XC_functional_weight'] - 1.0) < 0.01:
                        del val['XC_functional_weight']
                    val.pop('exx_compute_weight', None)
                out[key] = val
            return out

        # map numbers to values
        xc_section_method = dict()
        xc_terms = dict()
        xc_terms_remove = dict()
        # xc_names = [
        #     'exchange', 'correlation', 'exchange_gradient_correction',
        #     'correlation_gradient_correction', 'van_der_waals', 'meta_gga']
        for i in range(6):
            xc_component = self._xc_functional_map[i]
            xc_number = numbers_split[i]
            if xc_number >= len(xc_component) or xc_component[xc_number] is None:
                # self.logger.warn(
                #     'Cannot resolve XC functional',
                #     data=dict(name=xc_names[i], index=xc_number))
                continue
            xc_section_method.update(xc_component[xc_number]['xc_section_method'])
            xc_terms.update(get_data(xc_component[xc_number]['xc_terms']))
            xc_terms_remove.update(get_data(xc_component[xc_number].get('xc_terms_remove', [])))

        # remove terms
        for key, val in xc_terms_remove.items():
            if key in xc_terms:
                xc_terms[key]['XC_functional_weight'] -= val['XC_functional_weight']
            else:
                xc_terms[key] = val
                xc_terms[key]['XC_functional_weight'] *= -1.0

        # filter data
        xc_terms = filter_data(xc_terms)

        xc_functional_str = gen_string(xc_terms)
        if xc_functional_str in _libxc_shortcut:
            # override for libXC compliance
            xc_terms = get_data(_libxc_shortcut[xc_functional_str]['xc_terms'])
            xc_terms = filter_data(xc_terms)

            xc_functional_str = gen_string(xc_terms)

        xc_section_method['XC_functional'] = xc_functional_str
        result = [xc_terms[key] for key in sorted(xc_terms.keys())]

        return (xc_section_method, result)

    def get_number_of_spin_channels(self):
        magnetic = self.get_header('starting_magnetization')
        if magnetic is None:
            calculation = self.get('self_consistent', {})
            magnetic = calculation.get('magnetization', calculation.get('spin_pol'))
        spin = 1 if magnetic is None else 2
        return spin


class QuantumEspressoOutParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        def str_to_energy_contributions(val_in):
            val = [v.split('=') for v in val_in.strip().split('\n')]
            return {v[0].strip(): float(v[1].split()[0]) * ureg.rydberg for v in val}

        def str_to_forces(val_in):
            val = val_in.strip().split('\n')
            val = [v.split('=')[1].split() for v in val if 'force =' in v]
            return np.array(val, dtype=float) * ureg.rydberg / ureg.bohr

        def str_to_stress(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            pressure = float(val[0][0]) * ureg.kilobar
            stress = np.array([v[3:6] for v in val[1:4]], dtype=float) * ureg.kilobar
            return pressure, stress

        def str_to_labels_positions(val_in):
            units = re.search(r'ATOMIC_POSITIONS \((.+)\)', val_in)
            out = dict()
            if units:
                out['units'] = units.group(1)
            val = [v.split()[:4] for v in val_in.strip().split('\n')[1:]]
            val = np.transpose([v for v in val if v[1][-1].isdecimal()])
            out['labels'] = val[0]
            out['positions'] = np.array(val[1:], dtype=float).T
            return out

        def str_to_atom_data(val_in):
            val = [v.replace('(', ' ').replace(')', ' ').split() for v in val_in.strip().split('\n')]
            return [[float(vi) if not vi[0].isalpha() else vi for vi in v] for v in val]

        def str_to_occupations(val_in):
            return np.array(val_in.strip().split(), dtype=float)

        def str_to_arrays(val_in):
            val = [v for v in val_in.strip().split('\n')]
            pattern = re.compile(r'([\S\s]+?)(\d+\.\d+)\s*Mb\s*\(\s*([\d, ]+)\)')
            names = []
            sizes = []
            dimensions = []
            for v in val:
                res = pattern.search(v)
                if res is None:
                    continue
                g = res.groups()
                names.append(g[0].strip())
                sizes.append(float(g[1]))
                dimensions.append(g[2].strip())
            return names, sizes, dimensions

        def str_to_algorithm(val_in):
            val = val_in.strip().lower()
            out = None
            if val == 'davidson':
                out = 'davidson'
            elif val == 'cg style':
                out = 'conjugate_gradient'
            return out

        def str_to_band_energies(val_in):
            val = re.findall(r'(\-?[\d\.Ee]+)', val_in)
            return np.array(val, dtype=float)

        def str_to_profiling(val_in):
            sections = val_in.strip().split('\n\n')
            caller, category, function, cpu_time, wall_time, calls = [], [], [], [], [], []
            section_pattern = re.compile(r'(?:Called by ([\S\s]+?):|([\S\s]+?) routines)')
            function_pattern = re.compile(r'(\S+)\s*:')
            cpu_time_pattern = re.compile(r'(?:(\d+)h)?(?:(\d+)m)?(?:([\d\.]+)s)? (?:CPU|CPU time)')
            wall_time_pattern = re.compile(r'(?:(\d+)h)?(?:(\d+)m)?(?:([\d\.]+)s)? (?:WALL|WALL time|wall|wall time)')
            calls_pattern = re.compile(r'(\d+)\s*calls')
            for section in sections:
                sub_sections = section.split('\n')
                name = section_pattern.findall(sub_sections[0])
                if name:
                    caller_name, category_name = name[0][:2]
                    sub_sections = sub_sections[1:]
                else:
                    caller_name, category_name = '', ''

                for sub_section in sub_sections:
                    function_name = function_pattern.search(sub_section)
                    if function_name is None:
                        continue
                    caller.append(caller_name.strip())
                    category.append(category_name.strip())
                    function.append(function_name.group(1).strip())
                    res = cpu_time_pattern.findall(sub_section)
                    if len(res) == 0:
                        return caller, category, function, cpu_time, wall_time, calls
                    time = sum([float(res[0][i]) * 60 ** (2 - i) if res[0][i] else 0 for i in range(len(res[0]))])
                    cpu_time.append(0. if res is None else time)
                    res = wall_time_pattern.findall(sub_section)
                    wall_time.append(0. if not res else sum([float(res[0][i]) * 60 ** (2 - i) if res[0][i] else 0 for i in range(len(res[0]))]))
                    res = calls_pattern.search(sub_section)
                    calls.append(0 if res is None else int(res.group(1)))
            return caller, category, function, cpu_time, wall_time, calls

        def str_to_dispersion(val_in):
            val = [v.split() for v in val_in]
            return {v[0].strip(): {'vdw_radius': float(v[1]), 'C_6': float(v[2])} for v in val}

        def str_to_sticks(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            return {v[0]: [int(i) for i in v[1:]] for v in val}

        re_float = r'[\d\.Ee\-\+]+'

        header_quantities = [
            Quantity(
                'supercell',
                rf'(?:operation: I \+ \(|translation:)\s*({re_float})\s*({re_float})\s*({re_float})',
                dtype=float, repeats=True),
            Quantity(
                'pseudopotential_report',
                r'(pseudopotential report for atomic species:[\s\S]+?)={10}',
                sub_parser=TextParser(quantities=[
                    Quantity('species', r'atomic species:\s*(\d+)', dtype=int),
                    Quantity('version', r'pseudo potential version\s*([\d ]+)', flatten=False),
                    Quantity('contents', r'\-\s*([\s\S]+)', flatten=False)]), repeats=True),
            Quantity(
                'renormalized_wavefunction',
                r'file (\S+): wavefunction\(s\)([\w ]+)renormalized', repeats=True),
            Quantity(
                'dispersion',
                r'atom\s*VdW radius\s*C_6\s*([\s\S]+?)\n\s*\n',
                str_operation=str_to_dispersion, convert=False),
            Quantity(
                'atom_radii',
                r'new r_m :\s*[\d\.]+\s*\(alat units\)\s*([\d\.]+) \(a\.u\.\) for type\s*(\d+)',
                repeats=True),
            Quantity(
                'x_qe_xc_functional_user_enforced',
                r'IMPORTANT: XC functional enforced from input :\s*Exchange\-correlation\s*=\s*(\w+)',
                str_operation=lambda x: True),
            Quantity(
                'x_qe_gamma_algorithms',
                r'(gamma\-point specific algorithms are used)',
                str_operation=lambda x: True),
            Quantity(
                'x_qe_diagonalization_algorithm',
                r'of the eigenvalue problem:\s*a (serial) algorithm will be used'),
            Quantity(
                'g_vector_sticks',
                r'G-vecs:\s*dense\s*smooth\s*PW\s*([\s\S]+?)\n *\n', str_operation=str_to_sticks, convert=False),
            Quantity(
                'x_qe_ibrav',
                r'bravais\-lattice index\s*=\s*(\d+)', dtype=int),
            Quantity(
                'alat',
                rf'lattice parameter \((?:alat|a_0)\)\s*=\s*({re_float})', unit='bohr', dtype=float),
            Quantity(
                'x_qe_cell_volume',
                rf'unit-cell volume\s*=\s*({re_float})', unit='bohr**3', dtype=float),
            Quantity(
                'number_of_atoms',
                r'number of atoms/cell\s*=\s*(\d+)', dtype=int),
            Quantity(
                'x_qe_number_of_species',
                r'number of atomic types\s*=\s*(\d+)', dtype=int),
            Quantity(
                'number_of_electrons',
                rf'number of electrons\s*=\s*({re_float})\s*(?:\(up:\s*({re_float})\s*,\s*down:\s*({re_float}))?',
                dtype=float),
            Quantity(
                'x_qe_number_of_states',
                r'number of Kohn\-Sham states\s*=\s*(\d+)', dtype=int),
            Quantity(
                'wavefunction_cutoff',
                rf'kinetic\-energy cutoff\s*=\s*({re_float})', dtype=float, unit='rydberg'),
            Quantity(
                'density_cutoff',
                rf'charge density cutoff\s*=\s*({re_float})', dtype=float, unit='rydberg'),
            Quantity(
                'fock_cutoff',
                rf'cutoff for Fock operator\s*=\s*({re_float})', dtype=float, unit='rydberg'),
            Quantity(
                'scf_threshold_energy_change',
                rf'convergence threshold\s*=\s*({re_float})', dtype=float, unit='rydberg'),
            Quantity(
                'x_qe_potential_mixing_beta',
                rf'mixing beta\s*=\s*({re_float})', dtype=float),
            Quantity(
                'mixing_scheme',
                r'number of iterations used\s*=\s*(\d+)\s*(.*)mixing'),
            Quantity(
                'xc_functional',
                r'Exchange\-correlation\s*=\s*(.+)\s*(\([\d ]+\))', convert=False, flatten=False),
            Quantity(
                'x_qe_exact_exchange_fraction',
                rf'EXX\-fraction\s*=\s*({re_float})', dtype=float),
            Quantity(
                'x_qe_md_max_steps',
                r'\s*nstep\s*=\s*(\d+)', dtype=int),
            Quantity(
                'spin_orbit_mode',
                r'\s*(.*?)\s*calculation\s*(with(?:out)?)\s*spin-orbit'),
            Quantity(
                'berry_efield',
                r'(Using Berry phase electric field[\s\S]+?Number of iterative cycles\s*:\s*\d+)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'direction', r'Direction\s*:\s*(\d+)', dtype=int),
                    Quantity(
                        'intensity',
                        rf'Intensity \((?:Ry\s*)?a.u.\)\s*:\s*({re_float})', dtype=float),
                    Quantity(
                        'strings', r'Strings composed by\s*:\s*(\d+)', dtype=int),
                    Quantity(
                        'niter', r'Number of iterative cycles\s*:\s*(\d+)', dtype=int)])),
            Quantity(
                'assume_isolated',
                r'Assuming isolated system,\s*(.*?)\s*method'),
            Quantity(
                'x_qe_celldm',
                rf'celldm\(1\)=\s*({re_float})\s*celldm\(2\)=\s*({re_float})\s*celldm\(3\)=\s*({re_float})\s*'
                rf'celldm\(4\)=\s*({re_float})\s*celldm\(5\)=\s*({re_float})\s*celldm\(6\)=\s*({re_float})\s*',
                dtype=float, unit='bohr'),
            Quantity(
                'units',
                r'crystal axes: \(cart\. coord\. in units of ([\w ]+)\)\s*'),
            Quantity(
                'simulation_cell',
                r'a\(1\) = \(([\-\d\. ]+)\)\s*a\(2\) = \(([\-\d\. ]+)\)\s*a\(3\) = \(([\-\d\. ]+)\)\s*',
                dtype=float, shape=(3, 3)),
            Quantity(
                'reciprocal_cell_units',
                r'reciprocal axes: \(cart\. coord\. in units of ([\w ]+)\)\s*'),
            Quantity(
                'reciprocal_cell',
                r'b\(1\) = \(([\-\d\. ]+)\)\s*b\(2\) = \(([\-\d\. ]+)\)\s*b\(3\) = \(([\-\d\. ]+)\)\s*',
                dtype=float, shape=(3, 3)),
            Quantity(
                'pseudopotential',
                r'(PseudoPot\. #[\s\S]+?\n\s*\n)', repeats=True,
                sub_parser=TextParser(quantities=[
                    Quantity('idx', r'PseudoPot\. # (\d+)'),
                    Quantity('label', r'for (\w+)'),
                    Quantity('filename', r'read from file:?\s*\s*(\S+)'),
                    Quantity('md5sum', r'MD5 check sum:\s*(\S+)'),
                    Quantity('type', r'Pseudo is\s*(.*?),', flatten=False),
                    Quantity('valence', rf'Zval\s*=\s*({re_float})'),
                    Quantity('comment', r'\s*(.+?)\s*Using radial', flatten=False),
                    Quantity(
                        'integral_ndirections',
                        r'Setup to integrate on\s*(\d+)\s+directions:'),
                    Quantity(
                        'integral_lmax_exact', r'integral exact up to l =\s*(\d+)'),
                    Quantity(
                        'augmentation_shape', r'Shape of augmentation charge:\s*(.*?)\s*'),
                    Quantity(
                        'ndmx', r'grid of\s*(\d+) points', dtype=int),
                    Quantity(
                        'nbeta', r',\s*(\d+) beta functions', dtype=int),
                    Quantity(
                        'beta', r'l\((\d+)\)\s*=\s*(\d+)', repeats=True, dtype=int),
                    Quantity(
                        'ncoefficients',
                        r'Q\(r\) pseudized with\s*(\d+)\s*coefficients', dtype=int),
                    Quantity(
                        'rinner',
                        r'rinner\s*=\s*([\-\d\.\s]+)',
                        str_operation=lambda x: ' '.join(x.split()), convert=False)])),
            Quantity(
                'atom_species_pp',
                r'atomic species\s*valence\s*mass\s*pseudopotential([\s\S]+?)\n\s*\n',
                str_operation=str_to_atom_data, convert=False),
            Quantity(
                'starting_magnetization',
                r'Starting magnetic structure\s*atomic species\s*magnetization([\s\S]+?)\n\s*\n',
                str_operation=str_to_atom_data, convert=False),
            Quantity(
                'x_qe_md_cell_mass',
                rf'cell mass\s*=\s*({re_float})\s*AMU/\(a\.u\.\)\^2', dtype=float),
            Quantity(
                'symmetry',
                r'(\d+\s*Sym\.\s*Ops\.[\s\S]+?)\n\s*\n', sub_parser=TextParser(quantities=[
                    Quantity(
                        'nsymm', r'(\d+) Sym\.', dtype=int),
                    Quantity(
                        'symm_inversion', r'\((\S+)\s*inversion',
                        str_operation=lambda x: 'with' in x, convert=False),
                    Quantity(
                        'nsymm_with_fractional_translation', r'(\d+)\s*have fractional translation',
                        dtype=int),
                    Quantity(
                        'nsymm_ignored', r'(\d+)\s*additional sym\.ops\. were found but ignored',
                        dtype=int)])),
            Quantity(
                'labels_positions',
                r'(Cartesian axes\s*site n\.\s*atom\s*positions[\s\S]+?)\n\s*\n',
                repeatas=False, sub_parser=TextParser(quantities=[
                    Quantity(
                        'axes', r'(\w+)\s*axes'),
                    Quantity(
                        'units', r'site n\.\s*atom\s*positions\s*\(\s*(\S+)'),
                    Quantity(
                        'labels', r'(\w+)\s*tau', repeats=True),
                    Quantity(
                        'positions', rf'=\s*\(\s*({re_float}\s*{re_float}\s*{re_float})\s*\)',
                        repeats=True, dtype=float)])),
            Quantity(
                'k_points',
                r'(number of k points=[\s\S]+?)\n\s*\n',
                repeats=False, sub_parser=TextParser(quantities=[
                    Quantity('nk', r'number of k points=\s*(\d+)', dtype=int),
                    Quantity(
                        'smearing', r'(\S+)\s*(?:broad|smearing|method)*,',
                        dtype=str, flatten=False),
                    Quantity(
                        'width',
                        rf'width\s*\(Ry\)=\s*({re_float})', dtype=float, unit='rydberg'),
                    Quantity('units', r'cart\. coord\. in units (2pi/alat)'),
                    Quantity('ik', r'k\(\s*(\d+)\s*\)', repeats=True),
                    Quantity(
                        'points',
                        rf'=\s*\(\s*({re_float}\s*{re_float}\s*{re_float})\)', repeats=True),
                    Quantity('wk', rf',\s*wk\s*=\s*({re_float})', repeats=True),
                    Quantity('warning', r'(Number of k-points >= 100: set verbosity)')])),
            Quantity(
                'dense_grid',
                rf'(?:G\s+cutoff\s*=\s*({re_float})\s*\(|Dense\s*grid:)\s*(\d+)\s*'
                r'G\-vectors\)*\s*FFT\s+(?:dimensions|grid):\s*\(\s*([\d ,]+)\)',
                str_operation=lambda x: x.replace(',', ' ').split()),
            Quantity(
                'smooth_grid',
                rf'(?:G\s+cutoff\s*=\s*({re_float})\s*\(|Smooth\s*grid:)\s*(\d+)\s*'
                r'G\-vectors\s*(?:smooth grid|FFT dimensions)\s*:\s*\(\s*([\d ,]+)\)',
                str_operation=lambda x: x.replace(',', ' ').split()),
            Quantity(
                'x_qe_core_charge_realspace',
                r'(Real space treatment of Q\(r\))', str_operation=lambda x: True),
            Quantity(
                'input_occupation',
                r'Occupations\s*read\s*from\s*input\s*'
                r'(?:Spin-up)?([\d\.Ee\s]+)(?:Spin-down)?([\d\.Ee\s]+)',
                str_operation=str_to_occupations, convert=False),
            Quantity(
                'allocated_arrays',
                r'allocated arrays\s*est\. size \(Mb\)\s*dimensions([\s\S]+?)Largest',
                str_operation=str_to_arrays, convert=False),
            Quantity(
                'temporary_arrays',
                r'temporary arrays\s*est\. size \(Mb\)\s*dimensions([\s\S]+?)\n\s*\n',
                str_operation=str_to_arrays, convert=False),
            Quantity(
                'martyna_tuckerman_parameters',
                rf'alpha, beta MT =\s*({re_float})\s*({re_float})', dtype=float),
            Quantity(
                'core_charge_check',
                rf'Check: negative/imaginary core charge\s*=\s*({re_float})\s*({re_float})',
                dtype=float),
            Quantity(
                'x_qe_input_potential_recalculated_file',
                r'The potential is recalculated from file\s*:\s*(\S+)'),
            Quantity(
                'x_qe_starting_density_file',
                r'The initial density is read from file\s*:\s*(\S+)'),
            Quantity(
                'x_qe_starting_potential',
                r'Initial potential from\s*(.+)', flatten=False),
            Quantity(
                'x_qe_starting_charge_negative',
                rf'Check: negative starting charge\s*=\s*({re_float})', dtype=float),
            Quantity(
                'starting_charge_negative_spin',
                rf'negative rho \(up, down\):\s*({re_float})\s*({re_float})', dtype=float),
            Quantity(
                'initial_charge',
                rf'starting charge\s*({re_float})\s*, renormalised to\s*({re_float})',
                dtype=float),
            Quantity('x_qe_starting_wfc', r'Starting wfc\s*(.+)', flatten=False),
            Quantity(
                'x_qe_time_setup_cpu1_end',
                rf'total cpu time spent up to now is\s*({re_float})'),
            Quantity(
                'x_qe_per_process_mem',
                r'per\-process dynamical memory:\s*([\d\.]+)\s*Mb', dtype=float, unit='mebibyte')
        ]

        diagonalization_quantities = [
            Quantity(
                'diagonalization_algorithm',
                r'(Davidson|CG style)\s*diagonalization', str_operation=str_to_algorithm, convert=False),
            Quantity('diagonalization_ethr', r'ethr =\s*([\d\.\-E]+)', dtype=float),
            Quantity('diagonalization_iteration_avg', r'avg # of iterations\s*=\s*([\d\.]+)', dtype=float),
            Quantity(
                'diagonalization_c_bands_n_unconverged_eigenvalues',
                r'c_bands:\s*(\d+)\s*eigenvalues not converged', dtype=int, repeats=True)
        ]

        self.energy_quantities = {
            'energy_total': rf'total energy\s*=\s*({re_float})',
            'x_qe_energy_total_harris_foulkes_estimate': rf'Harris-Foulkes estimate\s*=\s*({re_float})',
            'x_qe_energy_total_accuracy_estimate': rf'estimated scf accuracy\s*<\s*({re_float})',
            'x_qe_energy_total_paw_all_electron': rf'total all-electron energy\s*=\s*({re_float})'
        }

        energy_quantities = [Quantity(
            key, pattern, dtype=float, unit='rydberg') for key, pattern in self.energy_quantities.items()]

        calculation_quantities = [
            Quantity('spin_pol', r'SPIN (UP|DOWN)'),
            Quantity(
                'k_points',
                r'k\s*=\s*(\-*[\d\.]+)\s*(\-*[\d\.]+)\s*(\-*[\d\.]+)', repeats=True, dtype=float),
            Quantity(
                'number_of_planewaves',
                r'\(\s*(\d+)\s*PWs\)', dftype=int, repeats=True),
            Quantity(
                'band_energies',
                r'band(?:s|\s+energies)\s*\(\s*[eE][vV]\s*\)\s*:\s*([\d\.\-\s]+)',
                str_operation=str_to_band_energies, repeats=True, convert=False),
            Quantity(
                'occupation_numbers',
                r'occupation numbers\s*([\d\.\-\s]+?)\n *\n', repeats=True, dtype=float),
            Quantity(
                'homo_lumo',
                r'highest occupied(?:, lowest unoccupied)* level \(ev\):\s*([\-\d\. ]+)',
                dtype=float),
            Quantity(
                'fermi_energy',
                rf'(?:the Fermi energy is|the spin up/dw Fermi energies are)\s*([\-\d\. ]+)',
                dtype=float),
            Quantity(
                'energies',
                r'!\s*(total energy[\s\S]+?)\n\s*\n',
                sub_parser=TextParser(quantities=energy_quantities)),
            Quantity(
                'energy_contributions',
                r'The total energy is the sum of the following terms:\s*([\s\S]+?Ry\n\s*\n)',
                str_operation=str_to_energy_contributions, convert=False),
            Quantity(
                'magnetization_total',
                rf'total magnetization\s*=\s*({re_float})\s*Bohr mag/cell',
                dtype=float, unit='bohr_magneton', repeats=True),
            Quantity(
                'magnetization_absolute',
                rf'absolute magnetization\s*=\s*({re_float})\s*Bohr mag/cell',
                dtype=float, unit='bohr_magneton', repeats=True),
            Quantity(
                'convergence_iterations',
                r'convergence has been achieved in\s*([\d]+) iterations', dtype=int),
            Quantity(
                'forces',
                r'Forces acting on atoms \(Ry\/au\):\s*([\s\S]+?)(?:The|\n\s*\n)',
                str_operation=str_to_forces, convert=False),
            Quantity(
                'total_force',
                rf'Total force\s*=\s*({re_float})\s*Total SCF correction\s*=\s*({re_float})',
                dtype=float, unit='rydberg/bohr'),
            Quantity(
                'forces_dispersion',
                r'Dispersion forces acting on atoms:\s*([\s\S]+?)(?:The|\n\s*\n)',
                str_operation=str_to_forces, convert=False),
            Quantity(
                'total_force_dispersion',
                rf'Total Dispersion Force =\s*({re_float})', dtype=float, unit='rydberg/bohr'),
            Quantity(
                'stress',
                r'total\s*stress\s*\(Ry/bohr\*\*3\)\s*\(kbar\)\s*P=\s*([\s\S]+?)\n\s*\n',
                str_operation=str_to_stress, convert=False),
            Quantity(
                'units',
                r'crystal axes: \(cart\. coord\. in units of ([\w ]+)\)\s*'),
            Quantity(
                'simulation_cell',
                r'a\(1\) = \(([\-\d\. ]+)\)\s*a\(2\) = \(([\-\d\. ]+)\)\s*a\(3\) = \(([\-\d\. ]+)\)\s*',
                dtype=float, shape=(3, 3)),
            Quantity(
                'reciprocal_cell_units',
                r'reciprocal axes: \(cart\. coord\. in units of ([\w ]+)\)\s*'),
            Quantity(
                'reciprocal_cell',
                r'b\(1\) = \(([\-\d\. ]+)\)\s*b\(2\) = \(([\-\d\. ]+)\)\s*b\(3\) = \(([\-\d\. ]+)\)\s*',
                dtype=float, shape=(3, 3)),
            Quantity(
                'labels_positions',
                r'(ATOMIC_POSITIONS \(.+\)[\s\S]+?)\n\s*\n',
                str_operation=str_to_labels_positions, convert=False),
            Quantity(
                'starting_magnetization',
                r'Starting magnetic structure\s*atomic species\s*magnetization([\s\S]+?)\n\s*\n',
                str_operation=str_to_atom_data, convert=False),
            # Quantity(
            #     'x_qe_t_md_bfgs_scf_cycles',
            #     r'number of scf cycles\s*=\s*(\d+)', dtype=int),
            # Quantity(
            #     'x_qe_t_md_bfgs_trust_new',
            #     r'new trust radius\s*=\s*[\d\.]+ Ry', dtype=float, unit='rydberg'),
            # Quantity(
            #     'x_qe_t_md_bfgs_conv_thr_new',
            #     r'new conv_thr\s*=\s*[\d\.]+ bohr', dtype=float, unit='bohr'),
            # Quantity(
            #     'x_qe_t_md_bfgs_steps',
            #     r'number of bfgs steps\s*=\s*(\d+)', dtype=int),
            # Quantity(
            #     'x_qe_t_md_bfgs_energy_new',
            #     r'energy\s*new\s*=\s*[\d\.\-]+\s*Ry', dtype=float, unit='rydberg'),
            # Quantity(
            #     'x_qe_t_md_bfgs_energy_old',
            #     r'energy\s*old\s*=\s*[\d\.\-]+\s*Ry', dtype=float, unit='rydberg'),
            Quantity(
                'exx_refine',
                r'(EXX: now go back to refine exchange calculation)'),
            Quantity(
                'memory',
                r'per\-process dynamical memory:\s*([\d\.]+)\s*Mb', dtype=float, unit='mebibyte'),
            Quantity(
                'output_datafile',
                r'Writing output data file ([\w\.]+)', dtype=str),
            Quantity(
                'negative_rho',
                r'negative rho \(up, down\):\s*([\d\.E\-\+]+)\s*([\d\.E\-\+]+)', dtype=float),
            Quantity(
                'total_time',
                r'total cpu time spent up to now is\s*([\d\.]+)', unit='seconds', repeats=True),
        ]

        scf_quantities = [Quantity(
            'iteration',
            r'(ation\s*#[\s\S]+?(?:\n *iter|End))', repeats=True,
            sub_parser=TextParser(quantities=[
                Quantity('number', r'n\s*#\s*(\d+)'),
                Quantity('ecutwfc', r'ecut=\s*([\d\.]+)', unit='rydberg'),
                Quantity('beta', r'beta=\s*([\d\.]+)'),
                Quantity(
                    'negative_rho',
                    rf'negative rho \(up, down\):\s*([\d\.E\-\+]+)\s*([\d\.E\-\+]+)',
                    dtype=float),
                Quantity(
                    'magnetic_moments',
                    rf'atom:\s*(\d+)\s*charge:\s*({re_float})\s*magn:\s*({re_float})\s*constr:\s*({re_float})',
                    repeats=True, dtype=float),
                Quantity(
                    'energies',
                    r'(total energy[\s\S]+?)\n\s*\n',
                    sub_parser=TextParser(quantities=energy_quantities)),
                Quantity(
                    'magnetization_total',
                    rf'total magnetization\s*=\s*({re_float})\s*Bohr mag/cell',
                    dtype=float, unit='bohr_magneton'),
                Quantity(
                    'magnetization_absolute',
                    rf'absolute magnetization\s*=\s*({re_float})\s*Bohr mag/cell',
                    dtype=float, unit='bohr_magneton'),
                Quantity(
                    'total_time',
                    r'total cpu time spent up to now is\s*([\d\.]+)', unit='seconds')
            ] + diagonalization_quantities))] + calculation_quantities

        # TODO add electric field calculation

        bandstructure_quantities = diagonalization_quantities + calculation_quantities

        sampling_quantities = [
            Quantity(
                'self_consistent',
                r'(consistent Calculation[\s\S]+?)(?:Self-|init_run|\Z)',
                repeats=True, sub_parser=TextParser(quantities=scf_quantities)),
            Quantity('dynamics', r'(Entering Dynamics)', repeats=False)
        ]

        bfgs_quantities = [
            Quantity(
                'final_energy',
                rf'Final energy\s*=\s*({re_float})\s*Ry', dtype=float, unit='rydberg'),
            Quantity(
                'convergence',
                rf'bfgs converged in\s*(\d+)\s*scf cycles and\s*(\d+)\s*bfgs steps',
                dtype=int)
        ] + sampling_quantities

        md_quantities = [
            Quantity(
                'diffusion_coefficients',
                r'atom\s*\d+\s*D =\s*({re_float})\s*cm\^2/s',
                repeats=True, unit='cm**2/s'),
            Quantity(
                'diffusion_coefficient_mean',
                r'< D > =\s*({re_float})\s*cm\^2/s', unit='cm**2/s'),
        ] + sampling_quantities

        langevin_quantities = sampling_quantities

        vcs_quantities = sampling_quantities

        damped_quantities = sampling_quantities

        run_quantities = [
            Quantity(
                'program_name_version',
                r'Program\s*(\w+\s*v\.\S+\s*(?:\(svn rev\.\s*\d+\))*)'),
            Quantity(
                'start_date_time', r'starts (?:on|\.\.\.\s*Today is)\s*(\w+)\s*at\s*([\d: ]+)', flatten=False),
            Quantity(
                'compile_parallel_version',
                r'(Serial multi\-threaded|Serial|Parallel)\s*version\s*(\(MPI\))*', flatten=False),
            Quantity(
                'nthreads',
                r', running on\s*(\d+)\s*processor cores', dtype=int),
            Quantity(
                'nproc',
                r'(?:Number of processors in use:|, running on)\s*(\d+)\s*(?:processors)*',
                dtype=int),
            Quantity('npool', r'npool[\w/]*\s*=\s*(\d+)', dtype=int),
            Quantity('input_filename', r'Reading input from (.+)', flatten=False),
            Quantity('ntypx', r'ntypx.*?=\s*(\d+)', dtype=int),
            Quantity('npk', r'npk.*?=\s*(\d+)', dtype=int),
            Quantity('lmaxx', r'lmaxx.*?=\s*(\d+)', dtype=int),
            Quantity('nchix', r'nchix.*?=\s*(\d+)', dtype=int),
            Quantity('ndmx', r'ndmx.*?=\s*(\d+)', dtype=int),
            Quantity('nbrx', r'nbrx.*?=\s*(\d+)', dtype=int),
            Quantity(
                'input_positions_cell_dirname',
                r'Atomic positions and unit cell read from directory:\s*(\S+)'),
            Quantity(
                'header',
                r'([Pp]rogram [A-Z]+[\s\S]+?)(?:Self\-|Band)',
                repeats=False, sub_parser=TextParser(quantities=header_quantities)),
            Quantity(
                'self_consistent',
                # r'(consistent Calculation[\s\S]+?(?:BFG|Molecula|Dampe|Over\-dampe|Wentzcovitc|init_run|\Z))',
                r'(consistent Calculation[\s\S]+?(?:Self-|init_run|\Z))',
                repeats=False, sub_parser=TextParser(quantities=scf_quantities)),
            Quantity(
                'bandstructure',
                r'(Structure Calculation[\s\S]+?)(?:init_run|\Z)',
                repeats=False, sub_parser=TextParser(quantities=bandstructure_quantities)),
            Quantity(
                'bfgs_geometry_optimization',
                r'(S Geometry Optimization[\s\S]+?)(?:init_run|\Z)',
                repeats=False, sub_parser=TextParser(quantities=bfgs_quantities)),
            Quantity(
                'molecular_dynamics',
                r'(r Dynamics Calculation[\s\S]+?)(?:init_run|\Z)',
                repeats=False, sub_parser=TextParser(quantities=md_quantities)),
            Quantity(
                'damped_dynamics',
                r'(d Dynamics Calculation[\s\S]+?)(?:init_run|\Z)',
                repeats=False, sub_parser=TextParser(quantities=damped_quantities)),
            Quantity(
                'langevin_dynamics',
                r'(d Langevin Dynamics Calculation[\s\S]+?)(?:init_run|\Z)',
                repeats=False, sub_parser=TextParser(quantities=langevin_quantities)),
            Quantity(
                'vcs_wentzcovitch_damped_minimization',
                r'(h Damped Cell[\- ]*Dynamics Minimization:[\s\S]+?)(?:init_run|\Z)',
                repeats=False, sub_parser=TextParser(quantities=vcs_quantities)),
            Quantity(
                'profiling',
                r'((?:init_run|PWSCF)\s*:\s*[\s\S]+?)(?:This run|\Z)',
                repeats=False, str_operation=str_to_profiling, convert=False),
            Quantity(
                'end_date_time', r'was terminated on:\s*([\d: ]+)\s*(\w+)', flatten=False),
            Quantity('job_done', r'(JOB DONE)')
        ]

        self._quantities = [Quantity(
            'run',
            r'(Program\s*\w+\s*v[\S\s]+?(?:JOB DONE|\Z))',
            sub_parser=QuantumEspressoRunParser(quantities=run_quantities), repeats=True)]


class QuantumEspressoParser(FairdiParser):
    def __init__(self):
        super().__init__(
            name='parsers/quantumespresso', code_name='Quantum Espresso',
            code_homepage='https://www.quantum-espresso.org/',
            mainfile_contents_re=(r'(Program PWSCF.*starts)|(Current dimensions of program PWSCF are)'))
        self.out_parser = QuantumEspressoOutParser()
        self.dos_parser = DataTextParser()
        self.smearing_map = {
            '-99': 'fermi', '-1': 'marzari-vanderbilt', '0': 'gaussian',
            '1': 'methfessel-paxton', 'Marzari-Vanderbilt': 'marzari-vanderbilt',
            'Methfessel-Paxton': 'methfessel-paxton', 'gaussian': 'gaussian',
            'Fermi-Dirac': 'fermi', 'tetrahedron': 'tetrahedra'}
        self._re_label = re.compile(r'([A-Z][a-z]?)')

    def parse_scc(self, run, calculation):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)

        # energies
        energies = calculation.get('energies', {})
        sec_energy = sec_scc.m_create(Energy)
        for key, val in energies.items():
            if val is None:
                continue
            if key.startswith('energy_'):
                sec_energy.m_add_sub_section(getattr(
                    Energy, key.replace('energy_', '').lower()), EnergyEntry(value=val))
            else:
                setattr(sec_scc, key, val.to('joule').magnitude)

        # enery contributions
        energy_contributions = calculation.get('energy_contributions')
        if energy_contributions is not None:
            sec_scc.x_qe_energy_decomposition_name = list(energy_contributions.keys())
            val = [e.to('joule').magnitude for e in energy_contributions.values()]
            sec_scc.x_qe_energy_decomposition_value = val

        # forces
        forces = calculation.get('forces')
        if forces is not None:
            sec_scc.forces = Forces(total=ForcesEntry(value_raw=forces))
        total_force = calculation.get('total_force')
        if total_force is not None:
            total_force = total_force.to('newton').magnitude
            sec_scc.x_qe_force_total = total_force[0]
            sec_scc.x_qe_force_total_scf_correction = total_force[1]
        forces = calculation.get('forces_dispersion')
        if forces is not None:
            sec_scc.x_qe_atom_dispersion_force = forces.to('newton').magnitude
        total_force = calculation.get('total_force_dispersion')
        if total_force is not None:
            sec_scc.x_qe_dispersion_force_total = total_force.to('newton').magnitude

        # stress
        sec_thermo = sec_scc.m_create(Thermodynamics)
        stress = calculation.get('stress')
        if stress is not None:
            sec_thermo.pressure = stress[0].to('pascal')
            sec_scc.stress = Stress(total=StressEntry(value=stress[1]))

        # eigenvalues
        eigenvalues = calculation.get('band_energies')
        if eigenvalues is not None:
            sec_eigenvalues = sec_scc.m_create(BandEnergies)
            n_spin = run.get_number_of_spin_channels()
            k_points = calculation.get('k_points')
            n_eigs = len(eigenvalues[0])
            k_points = np.reshape(k_points, (n_spin, len(k_points) // n_spin, 3))[0]

            # convert k_points from cartesial to crystal coordinates
            k_points *= 2 * np.pi / run.get_header('alat').to('m').magnitude
            reciprocal_cell = sec_run.system[-1].x_qe_reciprocal_cell.to('1/m').magnitude
            k_points = np.dot(np.linalg.inv(reciprocal_cell), k_points.T).T

            try:
                eigenvalues = np.reshape(eigenvalues, (n_spin, len(k_points), n_eigs)) * ureg.eV
                occupations = calculation.get('occupation_numbers')
                if occupations is not None:
                    occupations = np.reshape(occupations, (n_spin, len(k_points), n_eigs))

                sec_eigenvalues.kpoints = k_points

                number_of_planewaves = calculation.get('number_of_planewaves')
                if number_of_planewaves is not None:
                    number_of_planewaves = np.reshape(
                        number_of_planewaves, (n_spin, len(number_of_planewaves) // n_spin))
                    sec_eigenvalues.x_qe_eigenvalues_number_of_planewaves = number_of_planewaves[0]
                sec_eigenvalues.energies = eigenvalues
                if occupations is not None:
                    sec_eigenvalues.occupations = occupations

            except Exception:
                self.logger.warn('Error reading eigenvalues.')

        # homo lumo
        homo = calculation.get('homo_lumo')
        if homo is not None:
            lumo = None
            if isinstance(homo, np.ndarray) or isinstance(homo, list):
                homo, lumo = homo
            sec_energy.highest_occupied = [float(homo)] * ureg.eV
            if lumo is not None:
                sec_energy.lowest_unoccupied = [float(lumo)] * ureg.eV

        # fermi energy
        fermi_energy = calculation.get('fermi_energy')
        if fermi_energy is not None:
            fermi_energy = [fermi_energy] if isinstance(fermi_energy, float) else fermi_energy
            if np.array(fermi_energy).dtype == float:
                sec_energy.fermi = fermi_energy * ureg.eV

        n_electrons = run.get_header('number_of_electrons')
        if homo is None and fermi_energy is None and n_electrons is None:
            self.logger.error('Reference energy is not defined')

        for key in ['magnetization_total', 'magnetization_absolute']:
            val = calculation.get(key)
            if val is None:
                continue
            # get the last one corresponding to calculation
            # TODO verify metainfo unit for magnetization
            setattr(sec_scc, 'x_qe_%s' % key, val[-1].magnitude)

        # time
        time = calculation.get('total_time')
        if time is not None:
            sec_scc.time_single_configuration_calculation_cpu1_end = time[-1]

        def parse_diagonalization(source, target):
            diagonalization = {
                key: val for key, val in source.items() if key.startswith('diagonalization')}
            if not diagonalization:
                return

            if source.get('number') is not None or source.get('ecutwfc') is not None or source.get('beta') is not None:
                metainfo_ext = '_scf'
                diagonalization_section = x_qe_section_scf_diagonalization
            else:
                metainfo_ext = '_bands'
                diagonalization_section = x_qe_section_bands_diagonalization
            sec_diagonalization = target.m_create(diagonalization_section)
            for key, val in diagonalization.items():
                if val is None:
                    continue
                if key == 'diagonalization_c_bands_n_unconverged_eigenvalues':
                    val = sum(val)
                setattr(sec_diagonalization, 'x_qe%s_%s' % (metainfo_ext, key), val)

        # diagonalization
        parse_diagonalization(calculation, sec_scc)

        sec_scc.x_qe_exx_refine = calculation.get('exx_refine') is not None

        # miscellaneous
        miscellaneous_keys = ['convergence_iterations', 'output_datafile']
        for key in miscellaneous_keys:
            val = calculation.get(key)
            if val is None:
                continue
            setattr(sec_scc, 'x_qe_%s' % key, val)

        # scf_iteration
        for iteration in calculation.get('iteration', []):
            sec_scf_iteration = sec_scc.m_create(ScfIteration)

            energies = iteration.get('energies', {})
            sec_scf_energy = sec_scf_iteration.m_create(Energy)
            for key, val in energies.items():
                if val is None:
                    continue
                if key == 'energy_total':
                    sec_scf_energy.total = EnergyEntry(value=val)
                else:
                    setattr(sec_scf_iteration, '%s_iteration' % key, val.to('joule').magnitude)

            for key in ['number', 'ecutwfc', 'beta']:
                val = iteration.get(key)
                if val is None:
                    continue
                if key == 'ecutwfc':
                    val = val.to('joule').magnitude
                setattr(sec_scf_iteration, '%s_%s' % ('x_qe_iteration', key), val)

            magnetic_moments = iteration.get('magnetic_moments')
            if magnetic_moments is not None:
                magnetic_moments = np.transpose(magnetic_moments)
                sec_scf_iteration.x_qe_iter_mpersite_idx = [int(i) for i in magnetic_moments[0]]
                sec_scf_iteration.x_qe_iter_mpersite_charge = magnetic_moments[1]
                sec_scf_iteration.x_qe_iter_mpersite_magn = magnetic_moments[2]
                sec_scf_iteration.x_qe_iter_mpersite_constr = magnetic_moments[3]

            for key in ['magnetization_total', 'magnetization_absolute']:
                val = iteration.get(key)
                if val is None:
                    continue
                setattr(sec_scf_iteration, 'x_qe_%s_iteration' % key, val.magnitude)

            time = iteration.get('total_time')
            if time is not None:
                sec_scf_iteration.time_calculation = time

            parse_diagonalization(iteration, sec_scf_iteration)

            negative_rho = iteration.get('negative_rho')
            if negative_rho is not None:
                sec_scf_iteration.x_qe_iteration_charge_negative_up = negative_rho[0]
                sec_scf_iteration.x_qe_iteration_charge_negative_down = negative_rho[1]

        return sec_scc

    def parse_system(self, run, calculation):
        def _convert(key, source, units_key='units', units=None):
            units_mapping = dict(bohr=ureg.bohr, angstrom=ureg.angstrom)
            value = source.get(key)
            if value is None:
                return
            units = source.get(units_key) if units is None else units
            alat = run.get_header('alat', 1.0)
            value = np.array(value, dtype=float)
            if units in ['alat', 'a_0']:
                value *= alat
            elif units in ['bohr', 'angstrom']:
                value = value * units_mapping.get(units)
            elif units == '2 pi/alat':
                value *= (2 * np.pi / alat)
            return value

        sec_run = self.archive.run[-1]
        labels_positions = calculation.get('labels_positions')
        if labels_positions is None:
            # get it from header
            labels_positions = run.get_header('labels_positions')
        if labels_positions is not None:
            labels_positions = (
                labels_positions.get('labels'), _convert('positions', labels_positions))
        if labels_positions is None:
            return

        sec_system = sec_run.m_create(System)
        sec_atoms = sec_system.m_create(Atoms)
        sec_atoms.labels = [self._re_label.match(label).group(1) for label in labels_positions[0]]
        sec_atoms.positions = labels_positions[1]

        simulation_cell = _convert('simulation_cell', calculation)
        if simulation_cell is None:
            # get it from headers
            simulation_cell = _convert('simulation_cell', run.get('header', {}))
        if simulation_cell is not None:
            sec_atoms.lattice_vectors = simulation_cell

        sec_atoms.periodic = [True, True, True]

        reciprocal_cell = _convert('reciprocal_cell', calculation, 'reciprocal_cell_units')
        if reciprocal_cell is None and simulation_cell is not None:
            # calculate it from simulation cell, i.e. b1 = 2 pi / V (a2 X a3)
            cell = simulation_cell.to('m').magnitude
            volume = np.dot(cell[0], np.cross(cell[1], cell[2]))
            reciprocal_cell = np.array([
                np.cross(cell[(i + 1) % 3], cell[(i + 2) % 3]) for i in range(3)], dtype=float)
            reciprocal_cell *= (2 * np.pi / volume)
        if reciprocal_cell is not None:
            sec_system.x_qe_reciprocal_cell = reciprocal_cell

        starting_magnetization = calculation.get(
            'starting_magnetization', run.get_header('starting_magnetization'))
        if starting_magnetization is not None:
            magnetization = {m[0]: m[1] for m in starting_magnetization}
            sec_system.x_qe_atom_starting_magnetization = [
                magnetization.get(atom, 0.0) for atom in labels_positions[0]]

        k_points = calculation.get(
            'k_points', run.get_header('k_points', {}).get('points'))
        if k_points is not None:
            k_points = np.array(k_points, dtype=float) * 2 * np.pi / run.get_header('alat')
            sec_system.x_qe_k_info_vec = k_points.to('1/m').magnitude

        # assign other info only to representative system
        if len(sec_run.system) != 1:
            return sec_system

        # TODO In old parser, celldm[0] is alat, I do not know why
        keys = [
            'x_qe_md_cell_mass', 'x_qe_celldm', 'x_qe_ibrav', 'alat', 'x_qe_cell_volume',
            'x_qe_number_of_species', 'x_qe_number_of_states']
        for key in keys:
            val = run.get_header(key)
            if key == 'alat':
                key = 'x_qe_alat'
                val = val.to('m').magnitude
            elif key == 'x_qe_celldm':
                val = val.to('m').magnitude
            elif key == 'x_qe_cell_volume':
                val = val.to('m**3').magnitude
            if val is not None:
                setattr(sec_system, key, val)

        symmetry = run.get_header('symmetry', None)
        if symmetry is not None:
            for key, val in symmetry.items():
                setattr(sec_system, 'x_qe_%s' % key, val)
        else:
            sec_system.x_qe_nsymm = 0

        for key in ['wk', 'ik', 'nk']:
            val = run.get_header('k_points', {}).get(key, None)
            if val is not None:
                key = key if key == 'nk' else 'k_info_%s' % key
                setattr(sec_system, 'x_qe_%s' % key, val)

        for grid_type in ['dense', 'smooth']:
            grid = run.get_header('%s_grid' % grid_type)
            if grid is None:
                continue
            if len(grid) == 5:
                setattr(sec_system, 'x_qe_%s_g_cutoff' % grid_type, float(grid[0]))
                grid = grid[1:]
            setattr(sec_system, 'x_qe_%s_g_vectors' % grid_type, int(grid[0]))
            setattr(sec_system, 'x_qe_%s_FFT_grid' % grid_type, [
                int(n) for n in grid[1:]])

        supercell = run.get_header('supercell')
        if supercell is not None:
            sec_system.x_qe_supercell = True
            sec_system.x_qe_vec_supercell = supercell

        return sec_system

    def parse_configurations(self, run):
        sec_run = self.archive.run[-1]

        def parse_configuration(calculation):
            sec_system = self.parse_system(run, calculation)
            sec_scc = self.parse_scc(run, calculation)
            if sec_scc is None:
                return
            if sec_system is not None:
                sec_scc.single_configuration_calculation_to_system_ref = sec_system
            sec_scc.single_configuration_to_calculation_method_ref = sec_run.method[-1]

        for calculation_type in ['self_consistent', 'bandstructure']:
            calculation = run.get(calculation_type)
            if calculation is not None:
                self.sampling_method = 'single_point'
                parse_configuration(calculation)

        methods = {
            'bfgs_geometry_optimization': 'geometry_optimization',
            'molecular_dynamics': 'molecular_dynamics',
            'langevin_dynamics': 'langevin_dynamics',
            'damped_dynamics': 'geometry_optimization',
            'vcs_wentzcovitch_damped_minimization': 'geometry_optimization'}
        for method in methods:
            sampling = run.get(method)
            if sampling is not None:
                self.sampling_method = methods[method]
                if method.startswith('vcs') and sampling.get('dynamics') is not None:
                    self.sampling_method = 'molecular_dynamics'
                for calculation in sampling.get('self_consistent', []):
                    parse_configuration(calculation)
            # TODO include additional method-specific metainfo

        # dos
        dos_files = [p for p in os.listdir(self.out_parser.maindir) if p.endswith('.dos')]
        for dos_file in dos_files:
            self.dos_parser.mainfile = os.path.join(self.out_parser.maindir, dos_file)
            if self.dos_parser.data is not None:
                sec_dos = sec_run.calculation[-1].m_create(
                    Dos, Calculation.dos_electronic)
                data = np.transpose(self.dos_parser.data)
                nspin = run.get_number_of_spin_channels()
                energies = np.reshape(data[0], (nspin, len(data[0]) // nspin))
                sec_dos.energies = energies[0] * ureg.eV
                dos = np.reshape(data[1], (nspin, len(energies[0])))
                integrated = np.reshape(data[2], (nspin, len(energies[0])))
                for spin in range(len(dos)):
                    sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
                    sec_dos_values.spin = spin
                    sec_dos_values.value = dos[spin] / ureg.eV
                    sec_dos_values.value_integrated = integrated[spin]

    def parse_method(self, run):
        sec_method = self.archive.run[-1].m_create(Method)
        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)

        g_vector_sticks = run.get_header('g_vector_sticks', {}).get('Sum', None)
        if g_vector_sticks is not None:
            names = [
                'sum_dense', 'sum_smooth', 'sum_PW',
                'sum_G_dense', 'sum_G_smooth', 'sum_G_PW']
            for i in range(len(names)):
                setattr(sec_method, 'x_qe_sticks_%s' % names[i], g_vector_sticks[i])

        xc_section_method, xc_functionals = run.get_xc_functional()
        for key, val in xc_section_method.items():
            if key == 'XC_functional':
                continue
            setattr(sec_method, key, val)

        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for xc_functional in xc_functionals:
            sec_functional = Functional()
            for key, val in xc_functional.items():
                setattr(sec_functional, key.replace('XC_functional_', ''), val)
            name = sec_functional.name
            if name is None:
                sec_xc_functional.contributions.append(sec_functional)
            elif '_X_' in name or name.endswith('_X'):
                sec_xc_functional.exchange.append(sec_functional)
            elif '_C_' in name or name.endswith('_C'):
                sec_xc_functional.correlation.append(sec_functional)
            elif 'HYB' in name:
                sec_xc_functional.hybrid.append(sec_functional)
            else:
                sec_xc_functional.contributions.append(sec_functional)

        xc_functional = run.get_header('xc_functional')
        if xc_functional is not None:
            name, num = xc_functional = xc_functional.split('(')
            sec_method.x_qe_xc_functional_shortname = name.strip()
            sec_method.x_qe_xc_functional_num = num.strip().rstrip(')')

        # TODO identify if dft+u
        sec_electronic.method = 'DFT'

        array = run.get_header('allocated_arrays', None)
        if array is not None:
            sec_method.x_qe_allocated_array_name = array[0]
            sec_method.x_qe_allocated_array_size = (array[1] * ureg.mebibyte).to('bit').magnitude
            sec_method.x_qe_allocated_array_dimensions = array[2]
        array = run.get_header('temporary_arrays', None)
        if array is not None:
            sec_method.x_qe_temporary_array_name = array[0]
            sec_method.x_qe_temporary_array_size = (array[1] * ureg.mebibyte).to('bit').magnitude
            sec_method.x_qe_temporary_array_dimensions = array[2]

        spin_orbit_mode = run.get_header('spin_orbit_mode')
        if spin_orbit_mode is not None:
            sec_method.x_qe_spin_noncollinear = spin_orbit_mode[0].strip().lower() == 'noncollinear'
            sec_method.x_qe_spin_orbit = spin_orbit_mode[1] == 'with'

        # other method variables
        names = [
            'scf_threshold_energy_change', 'x_qe_core_charge_realspace',
            'x_qe_exact_exchange_fraction', 'x_qe_diagonalization_algorithm',
            'x_qe_potential_mixing_beta', 'x_qe_md_max_steps',
            'x_qe_input_potential_recalculated_file', 'x_qe_starting_density_file',
            'x_qe_starting_potential', 'x_qe_starting_charge_negative', 'x_qe_starting_wfc',
            'x_qe_time_setup_cpu1_end', 'x_qe_per_process_mem', 'x_qe_gamma_algorithms',
            'x_qe_xc_functional_user_enforced']
        for key in names:
            val = run.get_header(key)
            if val is None:
                continue
            if key == 'x_qe_per_process_mem':
                val = val.to('bit').magnitude
            setattr(sec_method, key, val)

        mixing_scheme = run.get_header('mixing_scheme')
        if mixing_scheme is not None:
            sec_method.x_qe_potential_mixing_iterations = mixing_scheme[0]
            sec_method.x_qe_potential_mixing_scheme = mixing_scheme[1]

        sec_smearing = sec_electronic.m_create(Smearing)
        smearing = run.get_header('k_points', {}).get('smearing', None)
        if smearing in self.smearing_map:
            sec_smearing.kind = self.smearing_map[smearing]

        smearing_width = run.get_header('k_points', {}).get('width', None)
        if smearing_width is not None:
            # TODO smearing width should have metainfo units
            sec_smearing.width = smearing_width.to('joule').magnitude

        martyna_tuckerman_parameters = run.get_header('martyna_tuckerman_parameters')
        if martyna_tuckerman_parameters is not None:
            sec_method.x_qe_isolated_system_method_martyna_tuckerman_alpha = martyna_tuckerman_parameters[0]
            sec_method.x_qe_isolated_system_method_martyna_tuckerman_beta = martyna_tuckerman_parameters[1]

        core_charge_check = run.get_header('core_charge_check')
        if core_charge_check is not None:
            sec_method.x_qe_core_charge_negative = core_charge_check[0]
            sec_method.x_qe_core_charge_imaginary = core_charge_check[1]

        starting_charge_negative_spin = run.get_header('starting_charge_negative_spin')
        if starting_charge_negative_spin is not None:
            sec_method.x_qe_starting_charge_negative_up = starting_charge_negative_spin[0]
            sec_method.x_qe_starting_charge_negative_down = starting_charge_negative_spin[1]

        initial_charge = run.get_header('initial_charge')
        if initial_charge is not None:
            sec_method.x_qe_starting_charge = initial_charge[0]
            sec_method.x_qe_starting_charge_renormalized = initial_charge[1]

        for name in ['wavefunction', 'density']:
            cutoff = run.get_header('%s_cutoff' % name)
            if cutoff is None:
                continue
            sec_basis_set = sec_method.m_create(BasisSet)
            sec_basis_set.type = 'plane waves'
            sec_basis_set.kind = name
            sec_basis_set.cell_dependent.append(BasisSetCellDependent(
                planewave_cutoff=cutoff, kind='plane_waves', name='PW_%.1f' % cutoff.magnitude))

        pseudopotential = run.get_header('pseudopotential', [])

        pseudopotential_report = dict()
        for report in run.get_header('pseudopotential_report', []):
            species = report.get('species')
            if species is None:
                continue
            pseudopotential_report[species] = {
                'version': report.get('version', '').strip(), 'contents': report.get('contents')}

        renormalized_wavefunction = {
            r[0]: ' '.join(r[1:]) for r in run.get_header('renormalized_wavefunction', [])}

        atom_radii = {
            r[1]: r[0] * ureg.bohr for r in run.get_header('atom_radii', [])}

        atom_species = {r[3]: r for r in run.get_header('atom_species_pp', [])}
        atom_species_names = [
            'label', 'n_valence_electrons',
            'x_qe_kind_mass', 'x_qe_pp_label', 'x_qe_pp_weight']

        for pp in pseudopotential:
            sec_method_atom_kind = sec_method.m_create(AtomParameters)
            for key, val in pp.items():
                if val is None:
                    continue
                if key == 'beta':
                    val = np.transpose(val)
                    sec_method_atom_kind.x_qe_pp_l_idx = val[0]
                    sec_method_atom_kind.x_qe_pp_l = val[1]
                elif key == 'rinner':
                    setattr(sec_method_atom_kind, 'x_qe_%s' % key, val)
                else:
                    setattr(sec_method_atom_kind, 'x_qe_pp_%s' % key, val)

            pp_report = pseudopotential_report.get(pp.get('idx'), None)
            if pp_report is not None:
                sec_method_atom_kind.x_qe_pp_report_version = pp_report['version']
                sec_method_atom_kind.x_qe_pp_report_contents = pp_report['contents']

            filename = os.path.basename(pp.get('filename', ''))
            sec_method_atom_kind.method_atom_kind_pseudopotential_name = filename
            renormalized = renormalized_wavefunction.get(filename, None)
            if renormalized is not None:
                sec_method_atom_kind.x_qe_pp_renormalized_wfc = renormalized

            radius = atom_radii.get(pp.get('idx'), None)
            if radius is not None:
                sec_method_atom_kind.x_qe_species_integration_radius = radius.to('m').magnitude

            dispersion = run.get_header('dispersion', {}).get(pp.get('label'), {})
            for key, val in dispersion.items():
                setattr(sec_method_atom_kind, 'x_qe_dispersion_correction_%s' % key, val)

            atom_sp = atom_species.get(pp.get('label'), [None] * len(atom_species_names))
            for i in range(len(atom_sp)):
                if atom_sp[i] is not None:
                    setattr(sec_method_atom_kind, atom_species_names[i], atom_sp[i])

        number_of_electrons = run.get_header('number_of_electrons')
        if number_of_electrons is not None:
            number_of_electrons = [number_of_electrons] if isinstance(
                number_of_electrons, float) else number_of_electrons
            sec_method.electronic.n_electrons = number_of_electrons

    def init_parser(self):
        self.out_parser.mainfile = self.filepath
        self.out_parser.logger = self.logger
        self.dos_parser.mainfile = self.filepath
        self.dos_parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.logger = logger if logger is not None else logging

        self.init_parser()

        # TODO include x_qe_warning
        for run in self.out_parser.get('run', []):
            self.sampling_method = None
            sec_run = self.archive.m_create(Run)
            sec_run.program = Program(name='Quantum Espresso')
            name_version = run.get('program_name_version')
            if name_version is not None:
                sec_run.x_qe_program_name = name_version[0]
                sec_run.program.version = ' '.join(name_version[1:]).lstrip('v.')

            date_time = run.get('start_date_time')
            if date_time is not None:
                date_time = datetime.strptime(date_time.replace(' ', ''), '%d%b%Y%H:%M:%S')
                sec_run.time_run = TimeRun(date_start=(date_time - datetime(1970, 1, 1)).total_seconds())

            sec_compile_options = sec_run.m_create(x_qe_section_compile_options)
            for key in ['compile_parallel_version', 'ntypx', 'npk', 'lmaxx', 'nchix', 'ndmx', 'nbrx']:
                val = run.get(key)
                if val is not None:
                    setattr(sec_compile_options, 'x_qe_%s' % key, val)

            sec_parallel = None
            for key in ['nthreads', 'nproc', 'npool']:
                val = run.get(key)
                if val is not None:
                    if sec_parallel is None:
                        sec_parallel = sec_run.m_create(x_qe_section_parallel)
                    setattr(sec_parallel, 'x_qe_%s' % key, val)

            for key in ['input_filename', 'input_positions_cell_dirname']:
                val = run.get(key)
                if val is not None:
                    setattr(sec_run, 'x_qe_%s' % key, val)

            self.parse_method(run)

            self.parse_configurations(run)

            if self.sampling_method is not None:
                sec_workflow = self.archive.m_create(Workflow)
                sec_workflow.type = self.sampling_method

            profiling = run.get('profiling')
            if profiling is not None:
                sec_run.x_qe_profile_caller = profiling[0]
                sec_run.x_qe_profile_category = profiling[1]
                sec_run.x_qe_profile_function = profiling[2]
                sec_run.x_qe_profile_cputime = profiling[3]
                sec_run.x_qe_profile_walltime = profiling[4]
                sec_run.x_qe_profile_ncalls = profiling[5]

            date_time = run.get('end_date_time')
            if date_time is not None:
                date_time = datetime.strptime(date_time.replace(': ', ':0').replace(' ', ''), '%H:%M:%S%d%b%Y')
                sec_run.time_run.date_end = (date_time - datetime(1970, 1, 1)).total_seconds()

            job_done = run.get('job_done')
            if job_done:
                sec_run.clean_end = True
