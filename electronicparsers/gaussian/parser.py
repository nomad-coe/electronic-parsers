import re
import numpy as np
import logging
import ase

from .metainfo import m_env

from nomad.units import ureg
from nomad.parsing.file_parser.text_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, XCFunctional, Functional, DFT, BasisSet, BasisSetAtomCentered
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, BandEnergies, Forces, ForcesEntry, Thermodynamics,
    ScfIteration
)
from .metainfo.gaussian import x_gaussian_section_elstruc_method,\
    x_gaussian_section_moller_plesset, x_gaussian_section_hybrid_coeffs,\
    x_gaussian_section_coupled_cluster, x_gaussian_section_quadratic_ci,\
    x_gaussian_section_ci, x_gaussian_section_semiempirical, x_gaussian_section_molmech,\
    x_gaussian_section_excited, x_gaussian_section_casscf, x_gaussian_section_orbital_symmetries,\
    x_gaussian_section_geometry_optimization_info, x_gaussian_section_molecular_multipoles,\
    x_gaussian_section_frequencies, x_gaussian_section_thermochem,\
    x_gaussian_section_force_constant_matrix, x_gaussian_section_times,\
    x_gaussian_section_symmetry


class GaussianOutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        re_float = r'[\d\.\-\+Ee]+'
        re_float_dexp = r'[\d\.\-\+EeDd]+'
        re_eigs = re.compile(r'(\-?\d*\.\d+\s*)')
        re_force = re.compile(r'(\d+\s*\-?\d*\..*)')

        def str_to_exp(val_in):
            val = np.array(val_in.rstrip('.').upper().replace('D', 'E').split(), dtype=float)
            return val[0] if len(val) == 1 else val

        def str_to_orbital_symmetries(val_in):
            val = re.findall(r'(?:Occupied|Virtual)\s*((?:\(.+\)\s*)*)', val_in)
            return [v.replace('(', '').replace(')', '').split() for v in val]

        def str_to_eigenvalues(val_in):
            val = val_in.split()
            spin_index = 0 if val[0] == 'Alpha' else 1
            occ = 0. if val[1] == 'virt' else 1.
            eigs, occs = [[], []], [[], []]
            # gaussian sometimes prints values without spaces so we need a re matching
            eigs[spin_index] = re_eigs.findall(val_in)
            occs[spin_index] = [occ] * len(eigs[spin_index])
            return eigs, occs

        def str_to_normal_modes(val_in):
            val = [v.split() for v in val_in.split('\n')]
            return np.array([v[2:] for v in val if len(v) >= 5], dtype=float)

        def str_to_force_constants(val_in):
            val = re_force.findall(val_in)
            fc = []
            for v in val:
                v = np.array(v.upper().replace('D', 'E').split(), dtype=float)
                index = int(v[0])
                if len(fc) < index:
                    fc.append([])
                fc[index - 1].extend(v[1:])
            for n in range(len(fc)):
                fc[n].extend(np.zeros(index - n - 1))
            fc = np.array(fc)
            fc = fc + fc.T - np.diag(fc.diagonal())
            return fc

        orientation_quantities = [
            Quantity(
                'standard_orientation',
                r'd orientation[\s\S]+?X\s*Y\s*Z\s*\-+\s*([\d\.\s\-]+?)\-{2}',
                convert=False, str_operation=lambda x: np.array(
                    [v.split() for v in x.strip().split('\n')], dtype=float)),
            Quantity(
                'input_orientation',
                r't orientation[\s\S]+?X\s*Y\s*Z\s*\-+\s*([\d\.\s\-]+?)\-{2}',
                convert=False, str_operation=lambda x: np.array(
                    [v.split() for v in x.strip().split('\n')], dtype=float)),
            Quantity(
                'z_matrix_orientation',
                r'x orientation[\s\S]+?X\s*Y\s*Z\s*\-+\s*([\d\.\s\-]+?)\-{2}',
                convert=False, str_operation=lambda x: np.array(
                    [v.split() for v in x.strip().split('\n')], dtype=float))]

        calculation_quantities = [
            Quantity(
                'energy_total',
                rf'\n *(?:Energy=|Electronic Energy)\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'hybrid_xc_coeff1', rf'ScaHFX=\s*({re_float})', dtype=float),
            Quantity(
                'hybrid_xc_coeff2',
                rf'ScaDFX=\s*({re_float}\s*{re_float}\s*{re_float}\s*{re_float})',
                flatten=False),
            Quantity('mp', r'(E2) ='),
            Quantity(
                'energy_total_mp',
                rf'(?:EUMP2|EUMP3|UMP4\(DQ\)|UMP4\(SDQ\)|UMP4\(SDTQ\)|MP5)\s*=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'mp2_correction_energy',
                rf'E2 =\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'mp3_correction_energy',
                rf'E3\s*=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'mp4dq_correction_energy',
                rf'E4\(DQ\)=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'mp4sdq_correction_energy',
                rf'E4\(SDQ\)=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'mp4sdtq_correction_energy',
                rf'E4\(SDTQ\)=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'mp5_correction_energy',
                rf'DEMP5 =\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity('cc', r'((?:CCSD\(T\)|E\(CORR\)))'),
            Quantity(
                'energy_total_cc',
                rf'(?:\n *CCSD\(T\)|E\(CORR\))\s*=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'ccsd_correction_energy',
                rf'DE\(Corr\)=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity('qci', r'(Quadratic Configuration Interaction)'),
            Quantity(
                'energy_total_qci',
                rf'(?:QCISD\(T\)|E\(Z\)|QCISD\(TQ\))=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'qcisd_correction_energy',
                rf'DE\(Z\)=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'qcisdtq_correction_energy',
                rf'DE5\s*=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity('ci', r'(\s{2}Configuration Interaction)'),
            Quantity(
                'energy_total_ci',
                rf'E\(CI\)=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'ci_correction_energy',
                rf'DE\(CI\)=\s*({re_float_dexp})',
                str_operation=str_to_exp, convert=False, unit='hartree', repeats=True),
            Quantity(
                'semiempirical_method',
                r'([-A-Z0-9]+\s*calculation of energy[a-zA-Z,. ]+)'),
            Quantity(
                'semiempirical_energy',
                rf'It=\s*\d+\s*PL=\s*[-+0-9EeDd.]+\s*DiagD=[A-Z]\s*ESCF=\s*({re_float})',
                repeats=True, unit='hartree', dtype=float),
            Quantity(
                'molmech_method',
                r'([a-zA-Z0-9]+\s*calculation of energy[a-z,. ]+)'),
            Quantity(
                'excited_state',
                rf'Excited State\s*(\d+):\s*\S+\s*({re_float})\s*eV\s*{re_float}\s*nm\s*'
                rf'f=({re_float})\s*<[\w*]+>=({re_float})\s*(.*)',
                repeats=True, convert=False),
            Quantity(
                'casscf_energy',
                rf'\(\s*[0-9]+\)\s*EIGENVALUE\s*({re_float})',
                repeats=True, dtype=float, unit='hartree'),
            Quantity(
                'optimization_completed',
                r'(Optimization (?:completed|stopped))', flatten=False, convert=False),
            Quantity(
                'population_analysis',
                r'(Population analysis using the SCF density[\s\S]+?Condensed)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'orbital_symmetries',
                        r'Orbital symmetries:([\s\S]*?)electro',
                        repeats=False, str_operation=str_to_orbital_symmetries),
                    Quantity(
                        'x_gaussian_elstate_symmetry',
                        r'nic state is\s*(.+)\.', flatten=False),
                    Quantity(
                        'eigenvalues',
                        r'(Alpha|Beta)\s*(occ|virt)\. eigenvalues \-\-\s*(.+)',
                        repeats=True, str_operation=str_to_eigenvalues, convert=False)])),
            Quantity(
                'charge',
                rf'\n *Charge=\s*({re_float})\s*electrons', dtype=float, unit='elementary_charge'),
            Quantity(
                'dipole',
                r''.join([r'%s=\s*([\-\d\.]+)\s*' % c for c in ['X', 'Y', 'Z']]),
                dtype=float, unit='debye'),
            Quantity(
                'quadrupole',
                r''.join([r'%s=\s*([\-\d\.]+)\s*' % c for c in [
                    'XX', 'YY', 'ZZ', 'XY', 'XZ', 'YZ']]),
                dtype=float, unit='debye * angstrom'),
            Quantity(
                'octapole',
                r''.join([r'%s=\s*([\-\d\.]+)\s*' % c for c in [
                    'XXX', 'YYY', 'ZZZ', 'XYY', 'XXY', 'XXZ', 'XZZ', 'YZZ', 'YYZ', 'XYZ']]),
                dtype=float, unit='debye * angstrom**2'),
            Quantity(
                'hexadecapole',
                r''.join([r'%s=\s*([\-\d\.]+)\s*' % c for c in [
                    'XXXX', 'YYYY', 'ZZZZ', 'XXXY', 'XXXZ', 'YYYX', 'YYYZ', 'ZZZX',
                    'ZZZY', 'XXYY', 'XXZZ', 'YYZZ', 'XXYZ', 'YYXZ', 'ZZXY']]),
                dtype=float, unit='debye * angstrom**3'),
            Quantity(
                'frequencies',
                r'\n *Frequencies \-\-\s*(.+)', dtype=float, repeats=True),
            Quantity(
                'reduced_masses',
                r'\n *Red\. masses \-\-\s*(.+)', str_operation=lambda x: [float(v) for v in x.split()], repeats=True),
            Quantity(
                'normal_modes',
                r'Atom\s*AN.*\s*([\-\d\s\.]+)',
                str_operation=str_to_normal_modes, convert=False, repeats=True),
            Quantity(
                'temperature_pressure',
                rf'Temperature\s*({re_float})\s*Kelvin\.\s*Pressure\s*({re_float})\s*Atm\.'),
            Quantity(
                'moments',
                r'(?:Eigenvalues|EIGENVALUES) \-\-\s*(\d+\.\d{5})\s*(\d+\.\d{5})\s*(\d+\.\d{5})',
                dtype=float, unit='amu*angstrom**2'),
            Quantity(
                'zero_point_energy',
                rf'Zero\-point correction=\s*({re_float})',
                dtype=float, unit='hartree'),
            Quantity(
                'thermal_correction_energy',
                rf'Thermal correction to Energy=\s*({re_float})',
                dtype=float, unit='hartree'),
            Quantity(
                'thermal_correction_enthalpy',
                rf'Thermal correction to Enthalpy=\s*({re_float})',
                dtype=float, unit='hartree'),
            Quantity(
                'thermal_correction_free_energy',
                rf'Thermal correction to Gibbs Free Energy=\s*({re_float})',
                dtype=float, unit='hartree'),
            Quantity(
                'forces',
                r'Forces \(Hartrees/Bohr\)\s*Number\s*Number\s*X\s*Y\s*Z\s*\-+\s*([\d\s\-\.]+?)\s*\-\-',
                str_operation=lambda x: np.array([xi.split()[2:5] for xi in x.split('\n')], dtype=float),
                convert=False, unit='hartree/bohr'),
            Quantity(
                'force_constants',
                r'Force constants in Cartesian coordinates:\s*([\s\S]+?)Force',
                str_operation=str_to_force_constants, convert=False),
            Quantity(
                'scf_iteration',
                r'(cle\s*\d+[\s\S]+?(?:Cy|\n\n|Leave))', sub_parser=TextParser(quantities=[
                    Quantity(
                        'number', r'cle\s*(\d+)', dtype=int),
                    Quantity(
                        'energy_total_scf_iteration',
                        rf' E=\s*({re_float})', dtype=float, unit='hartree'),
                    Quantity(
                        'x_gaussian_delta_energy_total_scf_iteration',
                        rf'Delta\-E=\s*({re_float})', dtype=float, unit='hartree')]),
                repeats=True),
            Quantity(
                'scf_iteration_final',
                r'(SCF Done:[\s\S]+?(?:Leave|\n\n|End))', sub_parser=TextParser(quantities=[
                    Quantity(
                        'x_gaussian_single_configuration_calculation_converged',
                        r'(SCF Done)', convert=False, flatten=False),
                    Quantity(
                        'x_gaussian_hf_detect', r'E\((.+?)\)'),
                    Quantity(
                        'energy_total',
                        rf'({re_float})\s*A\.U\.', dtype=float, unit='hartree'),
                    Quantity(
                        'x_gaussian_energy_error',
                        rf'Conv\s*=\s*({re_float_dexp})', unit='hartree', convert=False,
                        str_operation=str_to_exp),
                    Quantity(
                        ' energy_kinetic_electronic',
                        rf'KE\s*=\s*({re_float_dexp})', unit='hartree', convert=False,
                        str_operation=str_to_exp),
                    Quantity(
                        'spin_S2', rf'before annihilation\s*({re_float})', dtype=float),
                    Quantity(
                        'x_gaussian_after_annihilation_spin_S2',
                        rf',\s*after\s*({re_float})', dtype=float),
                    Quantity(
                        'x_gaussian_perturbation_energy',
                        r'[()A-Z0-9]+\s*=\s*[-+0-9D.]+\s*[()A-Z0-9]+\s*=\s*([-+0-9D.]+)',
                        convert=False, str_operation=str_to_exp, unit='hartree')]), repeats=False)
        ]

        run_quantities = [
            Quantity(
                'x_gaussian_settings_corrected',
                r'\-{10}\s*(#[\s\S]+?)\-{10}',
                convert=False,
                str_operation=lambda x: x.strip().replace('\n', '')),
            Quantity(
                'charge', r'Charge =\s*([\-\+\d]+)', dtype=int),
            Quantity(
                'spin_target', r'Multiplicity =\s*([\-\+\d]+)', dtype=int),
            Quantity(
                'lattice_vector', r'(?:TV|Tv)\s*0?\s*([\d\. ]+)', dtype=float, repeats=True),
            Quantity(
                'x_gaussian_atomic_masses', r'IAtWgt=([ \d\.]+)', dtype=float, repeats=True),
            Quantity(
                'system',
                r'((?:Standard|Z-Matrix|Input) orientation:[\s\S]+?)'
                r'(?:Predicted change in Energy|PREDICTED CHANGE IN ENERGY|Z-Matrix orientation|Normal termination)',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'calculation',
                        r'(<S\*\*2> of initial guess=[\s\S]+?(?:Initial guess read from the read\-write|\Z))',
                        sub_parser=TextParser(quantities=calculation_quantities), repeats=True)
                ] + calculation_quantities + orientation_quantities)),
            Quantity(
                'iteration',
                r'ation Nr\.([\s\S]+?)(?:Iter|\n\n)',
                repeats=True, sub_parser=TextParser(quantities=calculation_quantities)),
            Quantity('program_cpu_time', r'Job cpu time:(.*)\.\n', flatten=False),
            Quantity(
                'program_termination_date',
                r'Normal termination of Gaussian\s*\d+\s*at\s*(.*)\.\n', flatten=False)
        ]

        self._quantities = [
            Quantity(
                'program',
                r'\s*Gaussian\s*([0-9]+):\s*(\S+)\s*(\S+)\s*(\d+\-\w+\-\d+)',
                convert=False),
            Quantity('x_gaussian_chk_file', r'%[Cc]hk=([A-Za-z0-9.]*)', dtype=str),
            Quantity('x_gaussian_memory', r'%[Mm]em=([A-Za-z0-9.]*)', dtype=str),
            Quantity(
                'x_gaussian_number_of_processors',
                r'%[Nn][Pp]roc=([A-Za-z0-9.]*)', dtype=str),
            Quantity(
                'run',
                r'(-{10}\s*#[\s\S]+?Normal termination.*\n)', repeats=True,
                sub_parser=TextParser(quantities=run_quantities)),
        ]


class GaussianParser:
    def __init__(self):
        self._metainfo_env = m_env
        self.out_parser = GaussianOutParser()

        self._xc_functional_map = {
            'S': [{'name': 'LDA_X'}],
            'XA': [{'name': 'LDA_X_EMPIRICAL'}],
            'VWN': [{'name': 'LDA_C_VWN'}],
            'VWN3': [{'name': 'LDA_C_VWN_3'}],
            'SVWN': [{'name': 'LDA_X'}, {'name': 'LDA_C_VWN'}],
            'LSDA': [{'name': 'LDA_X'}, {'name': 'LDA_C_VWN'}],
            'B': [{'name': 'GGA_X_B88'}],
            'BLYP': [{'name': 'GGA_C_LYP'}, {'name': 'GGA_X_B88'}],
            'PBEPBE': [{'name': 'GGA_C_PBE'}, {'name': 'GGA_X_PBE'}],
            'PBEH': [{'name': 'GGA_X_WPBEH'}],
            'WPBEH': [{'name': 'GGA_X_WPBEH'}],
            'PW91PW91': [{'name': 'GGA_C_PW91'}, {'name': 'GGA_X_PW91'}],
            'M06L': [{'name': 'MGGA_C_M06_L'}, {'name': 'MGGA_X_M06_L'}],
            'M11L': [{'name': 'MGGA_C_M11_L'}, {'name': 'MGGA_X_M11_L'}],
            'SOGGA11': [{'name': 'GGA_X_SOGGA11'}, {'name': 'GGA_C_SOGGA11'}],
            'MN12L': [{'name': 'MGGA_X_MN12_L'}, {'name': 'MGGA_C_MN12_L'}],
            'N12': [{'name': 'GGA_C_N12'}, {'name': 'GGA_X_N12'}],
            'VSXC': [{'name': 'MGGA_X_GVT4'}, {'name': 'MGGA_C_VSXC'}],
            'HCTH93': [{'name': 'GGA_XC_HCTH_93'}],
            'HCTH147': [{'name': 'GGA_XC_HCTH_147'}],
            'HCTH407': [{'name': 'GGA_XC_HCTH_407'}],
            'HCTH': [{'name': 'GGA_XC_HCTH_407'}],
            'B97D': [{'name': 'GGA_XC_B97_D'}],
            'B97D3': [{'name': 'GGA_XC_B97_D3'}],
            'MPW': [{'name': 'GGA_X_MPW91'}],
            'G96': [{'name': 'GGA_X_G96'}],
            'O': [{'name': 'GGA_X_OPTX'}],
            'BRX': [{'name': 'MGGA_X_BR89'}],
            'PKZB': [{'name': 'MGGA_C_PKZB'}, {'name': 'MGGA_X_PKZB'}],
            'PL': [{'name': 'LDA_C_PZ'}],
            'P86': [{'name': 'GGA_C_P86'}],
            'B95': [{'name': 'MGGA_C_BC95'}],
            'KCIS': [{'name': 'MGGA_C_KCIS'}],
            'BRC': [{'name': 'MGGA_X_BR89'}],
            'VP86': [{'name': 'LDA_C_VWN_RPA'}, {'name': 'GGA_C_P86'}],
            'V5LYP': [{'name': 'LDA_C_VWN_RPA'}, {'name': 'GGA_C_LYP'}],
            'THCTH': [{'name': 'MGGA_X_TAU_HCTH'}, {'name': 'GGA_C_TAU_HCTH'}],
            'TPSSTPSS': [{'name': 'MGGA_C_TPSS'}, {'name': 'MGGA_X_TPSS'}],
            'B3LYP': [{'name': 'HYB_GGA_XC_B3LYP'}],
            'B3PW91': [{'name': 'HYB_GGA_XC_B3PW91'}],
            'B3P86': [{'name': 'HYB_GGA_XC_B3P86'}],
            'B1B95': [{'name': 'HYB_MGGA_XC_B88B95'}],
            'MPW1PW91': [{'name': 'HYB_GGA_XC_MPW1PW'}],
            'MPW1LYP': [{'name': 'HYB_GGA_XC_MPW1LYP'}],
            'MPW1PBE': [{'name': 'HYB_GGA_XC_MPW1PBE'}],
            'MPW3PBE': [{'name': 'HYB_GGA_XC_MPW3PBE'}],
            'B98': [{'name': 'HYB_GGA_XC_SB98_2C'}],
            'B971': [{'name': 'HYB_GGA_XC_B97_1'}],
            'B972': [{'name': 'HYB_GGA_XC_B97_2'}],
            'O3LYP': [{'name': 'HYB_GGA_XC_O3LYP'}],
            'TPSSH': [{'name': 'HYB_MGGA_XC_TPSSH'}],
            'BMK': [{'name': 'HYB_GGA_XC_B97_K'}],
            'X3LYP': [{'name': 'HYB_GGA_XC_X3LYP'}],
            'THCTHHYB': [{'name': 'HYB_MGGA_X_TAU_HCTH'}, {'name': 'GGA_C_HYB_TAU_HCTH'}],
            'BHANDH': [{'name': 'HYB_GGA_XC_BHANDH'}],
            'BHANDHLYP': [{'name': 'HYB_GGA_XC_BHANDHLYP'}],
            'APF': [{'name': 'HYB_GGA_XC_APF'}],
            'APFD': [{'name': 'HYB_GGA_XC_APFD'}],
            'HF': [{'name': 'HF_HF_X'}],
            'RHF': [{'name': 'HF_RHF_X'}],
            'UHF': [{'name': 'HF_UHF_X'}],
            'ROHF': [{'name': 'HF_ROHF_X'}],
            'CC': [{'name': 'HF_CCD'}],
            'QCID': [{'name': 'HF_CCD'}],
            'CCD': [{'name': 'HF_CCD'}],
            'CCSD': [{'name': 'HF_CCSD'}],
            'CCSD(T)': [{'name': 'HF_CCSD(T)'}],
            'CCSD-T': [{'name': 'HF_CCSD(T)'}],
            'CI': [{'name': 'HF_CI'}],
            'CID': [{'name': 'HF_CID'}],
            'CISD': [{'name': 'HF_CISD'}],
            'QCISD': [{'name': 'HF_QCISD'}],
            'QCISD(T)': [{'name': 'HF_QCISD(T)'}],
            'QCISD(TQ)': [{'name': 'HF_QCISD(TQ)'}],
            'OHSE2PBE': [{'name': 'HYB_GGA_XC_HSE03'}],
            'HSEH1PBE': [{'name': 'HYB_GGA_XC_HSE06'}],
            'OHSE1PBE': [{'name': 'HYB_GGA_XC_HSEOLD'}],
            'PBEH1PBE': [{'name': 'HYB_GGA_XC_PBEH1PBE'}],
            'PBE1PBE': [{'name': 'HYB_GGA_XC_PBEH'}],
            'M05': [{'name': 'MGGA_X_M05'}, {'name': 'MGGA_C_M05'}],
            'M052X': [{'name': 'HYB_MGGA_X_M05_2X'}, {'name': 'MGGA_C_M05_2X'}],
            'M06': [{'name': 'HYB_MGGA_X_M06'}, {'name': 'MGGA_C_M06'}],
            'M062X': [{'name': 'HYB_MGGA_X_M06_2X'}, {'name': 'MGGA_C_M06_2X'}],
            'M06HF': [{'name': 'HYB_MGGA_X_M06_HF'}, {'name': 'MGGA_C_M06_HF'}],
            'M11': [{'name': 'HYB_MGGA_X_M11'}, {'name': 'MGGA_C_M11'}],
            'MP2': [{'name': 'HF_MP2'}],
            'MP3': [{'name': 'HF_MP3'}],
            'MP4': [{'name': 'HF_MP4'}],
            'MP4(DQ)': [{'name': 'HF_MP4(DQ)'}],
            'MP4(SDQ)': [{'name': 'HF_MP4(SDQ)'}],
            'MP4(SDTQ)': [{'name': 'HF_MP4SDTQ'}],
            'MP5': [{'name': 'HF_MP5'}],
            'AM1': [{'name': 'HYB_AM1'}],
            'PM3': [{'name': 'HYB_PM3'}],
            'PM3MM': [{'name': 'HYB_PM3MM'}],
            'PM3D3': [{'name': 'HYB_PM3D3'}],
            'PM6': [{'name': 'HYB_PM6'}],
            'PM7': [{'name': 'HYB_PM7'}],
            'PM7R6': [{'name': 'HYB_PM7R6'}],
            'PM7MOPAC': [{'name': 'HYB_PM7MOPAC'}],
            'CBS-4': [{'name': 'HYB_CBS-4'}],
            'CBS-4M': [{'name': 'HYB_CBS-4M'}],
            'CBS-4O': [{'name': 'HYB_CBS-4O'}],
            'CBS-APNO': [{'name': 'HYB_CBS-APNO'}],
            'CBS-Q': [{'name': 'HYB_CBS-Q'}],
            'CBS-QB3': [{'name': 'HYB_CBS-QB3'}],
            'CBS-QB3O': [{'name': 'HYB_CBS-QB3O'}],
            'ROCBS-QB3': [{'name': 'HYB_ROCBS-QB3'}],
            'SOGGA11X': [{'name': 'HYB_GGA_X_SOGGA11_X'}, {'name': 'HYB_GGA_X_SOGGA11_X'}],
            'MN12SX': [{'name': 'HYB_MGGA_X_MN12_SX'}, {'name': 'MGGA_C_MN12_SX'}],
            'N12SX': [{'name': 'HYB_GGA_X_N12_SX'}, {'name': 'GGA_C_N12_SX'}],
            'LC-WPBE': [{'name': 'HYB_GGA_XC_LC_WPBE'}],
            'CAM-B3LYP': [{'name': 'HYB_GGA_XC_CAM_B3LYP'}],
            'WB97': [{'name': 'HYB_GGA_XC_WB97'}],
            'WB97X': [{'name': 'HYB_GGA_XC_WB97X'}],
            'WB97XD': [{'name': 'HYB_GGA_XC_WB97X_D'}],
            'HISSBPBE': [{'name': 'HYB_HISSBPBE'}],
            'B2PLYP': [{'name': 'HYB_B2PLYP'}],
            'MPW2PLYP': [{'name': 'HYB_MPW2PLYP'}],
            'B2PLYPD': [{'name': 'HYB_B2PLYPD'}],
            'MPW2PLYPD': [{'name': 'HYB_MPW2PLYPD'}],
            'B2PLYPD3': [{'name': 'HYB_B2PLYPD3'}],
            'MPW2PLYPD3': [{'name': 'HYB_MPW2PLYPD3'}],
            'G1': [{'name': 'HYB_G1'}],
            'G2': [{'name': 'HYB_G2'}],
            'G2MP2': [{'name': 'HYB_G2MP2'}],
            'G3': [{'name': 'HYB_G3'}],
            'G3B3': [{'name': 'HYB_G3B3'}],
            'G3MP2': [{'name': 'HYB_G3MP2'}],
            'G3MP2B3': [{'name': 'HYB_G3MP2B3'}],
            'G4': [{'name': 'HYB_G4'}],
            'G4MP2': [{'name': 'HYB_G4MP2'}],
            'LC-': [{'name': 'GGA_X_ITYH_LONG_RANGE'}],
            'BP': [{'name': 'GGA_X_B88'}, {'name': 'GGA_C_P86'}],
            'BP86': [{'name': 'GGA_X_B88'}, {'name': 'GGA_C_P86'}]
        }

        self._method_map = {
            'AMBER': [{'name': 'Amber'}],
            'DREIDING': [{'name': 'Dreiding'}],
            'UFF': [{'name': 'UFF'}],
            'AM1': [{'name': 'AM1'}],
            'PM3': [{'name': 'PM3'}],
            'PM3MM': [{'name': 'PM3MM'}],
            'PM3D3': [{'name': 'PM3D3'}],
            'PM6': [{'name': 'PM6'}],
            'PM7': [{'name': 'PM7'}],
            'PM7R6': [{'name': 'PM7R6'}],
            'PM7MOPAC': [{'name': 'PM7MOPAC'}],
            'PDDG': [{'name': 'PDDG'}],
            'CNDO': [{'name': 'CNDO'}],
            'INDO': [{'name': 'INDO'}],
            'MINDO': [{'name': 'MINDO'}],
            'MINDO3': [{'name': 'MINDO3'}],
            'ZINDO': [{'name': 'ZINDO'}],
            'HUCKEL': [{'name': 'HUCKEL'}],
            'EXTENDEDHUCKEL': [{'name': 'HUCKEL'}],
            'ONIOM': [{'name': 'ONIOM'}],
            'HF': [{'name': 'HF'}],
            'RHF': [{'name': 'RHF'}],
            'UHF': [{'name': 'UHF'}],
            'ROHF': [{'name': 'ROHF'}],
            'GVB': [{'name': 'GVB'}],
            'DFT': [{'name': 'DFT'}],
            'CI': [{'name': 'CI'}],
            'CID': [{'name': 'CID'}],
            'CISD': [{'name': 'CISD'}],
            'CIS': [{'name': 'CIS'}],
            'BD': [{'name': 'BD'}],
            'BD(T)': [{'name': 'BD(T)'}],
            'CC': [{'name': 'CCD'}],
            'QCID': [{'name': 'CCD'}],
            'CCD': [{'name': 'CCD'}],
            'CCSD': [{'name': 'CCSD'}],
            'EOMCCSD': [{'name': 'EOMCCSD'}],
            'QCISD': [{'name': 'QCISD'}],
            'CCSD(T)': [{'name': 'CCSD(T)'}],
            'CCSD-T': [{'name': 'CCSD(T)'}],
            'QCISD(T)': [{'name': 'QCISD(T)'}],
            'QCISD(TQ)': [{'name': 'QCISD(TQ)'}],
            'MP2': [{'name': 'MP2'}],
            'MP3': [{'name': 'MP3'}],
            'MP4': [{'name': 'MP4'}],
            'MP4DQ': [{'name': 'MP4DQ'}],
            'MP4(DQ)': [{'name': 'MP4DQ'}],
            'MP4SDQ': [{'name': 'MP4SDQ'}],
            'MP4(SDQ)': [{'name': 'MP4SDQ'}],
            'MP4SDTQ': [{'name': 'MP4SDTQ'}],
            'MP4(SDTQ)': [{'name': 'MP4SDTQ'}],
            'MP5': [{'name': 'MP5'}],
            'CAS': [{'name': 'CASSCF'}],
            'CASSCF': [{'name': 'CASSCF'}],
            'G1': [{'name': 'G1'}],
            'G2': [{'name': 'G2'}],
            'G2MP2': [{'name': 'G2MP2'}],
            'G3': [{'name': 'G3'}],
            'G3MP2': [{'name': 'G3MP2'}],
            'G3B3': [{'name': 'G3B3'}],
            'G3MP2B3': [{'name': 'G3MP2B3'}],
            'G4': [{'name': 'G4'}],
            'G4MP2': [{'name': 'G4MP2'}],
            'CBS-4': [{'name': 'CBS-4'}],
            'CBS-4M': [{'name': 'CBS-4M'}],
            'CBS-4O': [{'name': 'CBS-4O'}],
            'CBS-APNO': [{'name': 'CBS-APNO'}],
            'CBS-Q': [{'name': 'CBS-Q'}],
            'CBS-QB3': [{'name': 'CBS-QB3'}],
            'CBS-QB3O': [{'name': 'CBS-QB3O'}],
            'CBSEXTRAP': [{'name': 'CBSExtrapolate'}],
            'CBSEXTRAPOLATE': [{'name': 'CBSExtrapolate'}],
            'ROCBS-QB3': [{'name': 'ROCBS-QB3'}],
            'W1U': [{'name': 'W1U'}],
            'W1BD': [{'name': 'W1BD'}],
            'W1RO': [{'name': 'W1RO'}],
        }

        self._basis_set_map = {
            'STO-3G': [{'name': 'STO-3G'}],
            '3-21G': [{'name': '3-21G'}],
            '6-21G': [{'name': '6-21G'}],
            '4-31G': [{'name': '4-31G'}],
            '6-31G': [{'name': '6-31G'}],
            '6-311G': [{'name': '6-311G'}],
            'D95V': [{'name': 'D95V'}],
            'D95': [{'name': 'D95'}],
            'CC-PVDZ': [{'name': 'cc-pVDZ'}],
            'CC-PVTZ': [{'name': 'cc-pVTZ'}],
            'CC-PVQZ': [{'name': 'cc-pVQZ'}],
            'CC-PV5Z': [{'name': 'cc-pV5Z'}],
            'CC-PV6Z': [{'name': 'cc-pV6Z'}],
            'SV': [{'name': 'SV'}],
            'SVP': [{'name': 'SVP'}],
            'TZV': [{'name': 'TZV'}],
            'TZVP': [{'name': 'TZVP'}],
            'DEF2SV': [{'name': 'Def2SV'}],
            'DEF2SVP': [{'name': 'Def2SVP'}],
            'DEF2SVPP': [{'name': 'Def2SVPP'}],
            'DEF2TZV': [{'name': 'Def2TZV'}],
            'DEF2TZVP': [{'name': 'Def2TZVP'}],
            'DEF2TZVPP': [{'name': 'Def2TZVPP'}],
            'DEF2QZV': [{'name': 'Def2QZV'}],
            'DEF2QZVP': [{'name': 'Def2QZVP'}],
            'DEF2QZVPP': [{'name': 'Def2QZVPP'}],
            'QZVP': [{'name': 'QZVP'}],
            'MIDIX': [{'name': 'MidiX'}],
            'EPR-II': [{'name': 'EPR-II'}],
            'EPR-III': [{'name': 'EPR-III'}],
            'UGBS': [{'name': 'UGBS'}],
            'MTSMALL': [{'name': 'MTSmall'}],
            'DGDZVP': [{'name': 'DGDZVP'}],
            'DGDZVP2': [{'name': 'DGDZVP2'}],
            'DGTZVP': [{'name': 'DGTZVP'}],
            'CBSB3': [{'name': 'CBSB3'}],
            'CBSB7': [{'name': 'CBSB7'}],
            'SHC': [{'name': 'SHC'}],
            'SEC': [{'name': 'SHC'}],
            'CEP-4G': [{'name': 'CEP-4G'}],
            'CEP-31G': [{'name': 'CEP-31G'}],
            'CEP-121G': [{'name': 'CEP-121G'}],
            'LANL1': [{'name': 'LANL1'}],
            'LANL2': [{'name': 'LANL2'}],
            'SDD': [{'name': 'SDD'}],
            'OLDSDD': [{'name': 'OldSDD'}],
            'SDDALL': [{'name': 'SDDAll'}],
            'GEN': [{'name': 'General'}],
            'GENECP': [{'name': 'General ECP'}],
            'CHKBAS': [{'name': 'CHKBAS'}],
            'EXTRABASIS': [{'name': 'ExtraBasis'}],
            'DGA1': [{'name': 'DGA1'}],
            'DGA2': [{'name': 'DGA2'}],
            'SVPFIT': [{'name': 'SVPFit'}],
            'TZVPFIT': [{'name': 'TZVPFit'}],
            'W06': [{'name': 'W06'}],
            'CHF': [{'name': 'CHF'}],
            'FIT': [{'name': 'FIT'}],
            'AUTO': [{'name': 'AUTO'}],
        }

        self._xc_functional_pattern = re.compile(
            r'(?:#?[Pp]?)(?:(WPBEH)(.*)|(LC\-)(.*)|(G96)(.*)|(BRX)(.*)|(SV)(.*)|(B)([^2^3]*)|(O)([^2^3]))')

        self._basis_set_pattern = re.compile(
            r'(6\-311G)|(6\-31G)|(LANL2)|(LANL1)|(CBSB7)|(UGBS)|AUG\-(.*)|(D95)')

        self._energy_methods = {
            'mp': (x_gaussian_section_moller_plesset, [
                'mp2', 'mp3', 'mp4dq', 'mp4sdq', 'mp4sdtq', 'mp5']),
            'cc': (x_gaussian_section_coupled_cluster, ['ccsd']),
            'qci': (x_gaussian_section_quadratic_ci, ['qcisd', 'qcisdtq']),
            'ci': (x_gaussian_section_ci, ['ci']),
            'semiempirical': (x_gaussian_section_semiempirical, ['']),
            'molmech': (x_gaussian_section_molmech, [])}

    def parse_scc(self, section):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)

        # total energy
        sec_energy = sec_scc.m_create(Energy)
        energy_total = section.get('energy_total')
        if energy_total is not None:
            sec_energy.total = EnergyEntry(value=energy_total[-1])

        # hybrid coefficients
        sec_hybrid_coeffs = None
        for key in ['coeff1', 'coeff2']:
            val = section.get('hybrid_xc_%s' % key)
            if val is None:
                continue
            if sec_hybrid_coeffs is None:
                sec_hybrid_coeffs = sec_scc.m_create(x_gaussian_section_hybrid_coeffs)
            setattr(sec_hybrid_coeffs, 'hybrid_xc_%s' % key, val)

        def parse_energy_corrections(method, iteration=False):

            if not iteration and section.get(method) is None:
                return

            sec_method, energy_keys = self._energy_methods.get(method, (None, []))
            if sec_method is None:
                return

            sec_method = sec_scc.m_create(sec_method)
            for key in energy_keys:
                key = '%s_correction_energy' % key
                val = section.get(key)
                if val is not None:
                    setattr(sec_method, 'x_gaussian_%s' % key, val[-1])

            energy_method = section.get('%s_method' % method)
            if energy_method is not None:
                setattr(sec_method, 'x_gaussian_%s_method' % method, energy_method)

            energy = section.get('%s_energy' % method)
            if energy is not None:
                setattr(sec_method, 'x_gaussian_%s_energy' % method, energy)

            energy_total = section.get('energy_total_%s' % method)
            if energy_total is not None:
                sec_energy.total = EnergyEntry(value=energy_total[-1])

            return sec_method

        # energy corrections calculated from different methods
        sec_energy_method = None
        for method in ['mp', 'cc', 'qci', 'ci', 'semiempirical', 'molmech']:
            sec_energy_method = parse_energy_corrections(method)
            if sec_energy_method is not None:
                break

        # TODO make metainfo accept array not separate sections
        # excited state
        excited_state = section.get('excited_state', [])
        for state in excited_state:
            sec_excited_state = sec_scc.m_create(x_gaussian_section_excited)
            sec_excited_state.x_gaussian_excited_state_number = int(state[0])
            sec_excited_state.x_gaussian_excited_energy = float(state[1]) * ureg.eV
            sec_excited_state.x_gaussian_excited_oscstrength = float(state[2])
            sec_excited_state.x_gaussian_excited_spin_squared = float(state[3])
            sec_excited_state.x_gaussian_excited_transition = ' '.join(state[4:])

        # casscf
        casscf_energy = section.get('casscf_energy', [])
        for energy in casscf_energy:
            sec_casscf = sec_scc.m_create(x_gaussian_section_casscf)
            sec_casscf.x_gaussian_casscf_energy = energy

        # orbital symmetries
        orbital_symmetries = section.get('population_analysis', {}).get('orbital_symmetries')
        if orbital_symmetries is not None:
            sec_orbital_symmetries = sec_run.m_create(x_gaussian_section_orbital_symmetries)
            if orbital_symmetries[:2]:
                sec_orbital_symmetries.x_gaussian_alpha_symmetries = np.concatenate(orbital_symmetries[:2])
            if orbital_symmetries[2:]:
                sec_orbital_symmetries.x_gaussian_beta_symmetries = np.concatenate(orbital_symmetries[2:])

        # electronic symmetries
        elstate_symmetry = section.get('population_analysis', {}).get('x_gaussian_elstate_symmetry')
        if elstate_symmetry is not None:
            sec_symmetry = sec_run.m_create(x_gaussian_section_symmetry)
            sec_symmetry.x_gaussian_elstate_symmetry = elstate_symmetry

        # eigenvalues
        values, occupation = [[], []], [[], []]
        eigenvalues = section.get('population_analysis', {}).get('eigenvalues')
        if eigenvalues is not None:
            for eigs_occs in eigenvalues:
                for spin in range(2):
                    values[spin].extend(eigs_occs[0][spin])
                    occupation[spin].extend(eigs_occs[1][spin])
            if not values[1]:
                values = values[0:1]
                occupation = np.array(occupation[0:1]) * 2
            try:
                values = np.array(values, dtype=np.dtype(np.float64))
                values = np.reshape(values, (len(values), 1, len(values[0])))
                occupation = np.reshape(occupation, (len(occupation), 1, len(occupation[0])))
                sec_eigenvalues = sec_scc.m_create(BandEnergies)
                sec_eigenvalues.energies = values * ureg.hartree
                sec_eigenvalues.occupations = occupation
            except Exception:
                self.logger.error('Error setting eigenvalues.')

        # optimization
        optimization_completed = section.get('optimization_completed')
        if optimization_completed is not None:
            sec_optimization_info = sec_run.m_create(x_gaussian_section_geometry_optimization_info)
            sec_optimization_info.x_gaussian_geometry_optimization_converged = optimization_completed

        # multipoles
        multipoles = []
        keys = ['charge', 'dipole', 'quadrupole', 'octapole', 'hexadecapole']
        for n, key in enumerate(keys):
            val = section.get(key)
            if val is not None:
                val = val.to('coulomb * meter**%d' % n).magnitude
                val = [val] if isinstance(val, float) else val
                # TODO why quadrupole moments are not sorted, adapted from old parser
                if key == 'quadrupole':
                    val = [val[0], val[3], val[1], val[4], val[5], val[2]]
                multipoles.extend(val)
        if multipoles:
            sec_molecular_multipoles = sec_scc.m_create(x_gaussian_section_molecular_multipoles)
            sec_molecular_multipoles.x_gaussian_molecular_multipole_values = multipoles
            sec_molecular_multipoles.x_gaussian_molecular_multipole_m_kind = 'polynomial'

        # forces
        forces = section.get('forces')
        if forces is not None:
            sec_scc.forces = Forces(total=ForcesEntry(value_raw=forces))

        # force constants
        force_constants = section.get('force_constants')
        if force_constants is not None:
            sec_force_constant = sec_run.m_create(x_gaussian_section_force_constant_matrix)
            force_constants = force_constants * ureg.hartree / ureg.bohr ** 2
            sec_force_constant.x_gaussian_force_constant_values = force_constants.to(
                'J/(m**2)').magnitude

        # vibrational frequencies
        frequencies = section.get('frequencies')
        if frequencies is not None:
            # frequencies in old parsers are in J, not consistent with metainfo
            sec_frequencies = sec_run.m_create(x_gaussian_section_frequencies)
            sec_frequencies.x_gaussian_frequencies = np.hstack(frequencies)
            reduced_masses = section.get('reduced_masses')
            if reduced_masses is not None:
                reduced_masses = np.array(np.hstack(reduced_masses), dtype=np.float64) * ureg.amu
                sec_frequencies.x_gaussian_red_masses = reduced_masses.to('kg').magnitude
            normal_modes = section.get('normal_modes')
            if normal_modes is not None:
                normal_modes = np.hstack(normal_modes)
                normal_modes = np.reshape(normal_modes, (len(normal_modes), len(normal_modes[0]) // 3, 3))
                sec_frequencies.x_gaussian_normal_mode_values = np.transpose(normal_modes, axes=(1, 0, 2))

        # thermochemistry
        temperature_pressure = section.get('temperature_pressure')
        if temperature_pressure is not None:
            sec_thermo = sec_scc.m_create(Thermodynamics)
            # TODO extend Thermodynamics instead
            sec_thermochem = sec_run.m_create(x_gaussian_section_thermochem)
            sec_thermo.temperature = temperature_pressure[0]
            sec_thermo.pressure = (temperature_pressure[1] * ureg.atm).to('N/m**2')
            sec_scc.temperature = temperature_pressure[0]
            sec_scc.pressure = (temperature_pressure[1] * ureg.atm).to('N/m**2')
            moments = section.get('moments')
            if moments is not None:
                sec_thermochem.x_gaussian_moments = moments.to('kg*m**2').magnitude
            if section.get('zero_point_energy') is not None:
                sec_scc.energy.zero_point = EnergyEntry(value=section.get('zero_point_energy'))
            if section.get('thermal_correction_enthalpy') is not None:
                sec_thermo.enthalpy = section.get('thermal_correction_enthalpy')
            keys = [
                'zero_point_energy', 'thermal_correction_energy',
                'thermal_correction_enthalpy', 'thermal_correction_free_energy']
            for key in keys:
                val = section.get(key)
                if val is not None:
                    setattr(sec_thermochem, 'x_gaussian_%s' % key, val.to('joule').magnitude)

        # scf_iteration
        for iteration in section.get('scf_iteration', []):
            sec_scf_iteration = sec_scc.m_create(ScfIteration)
            energy = iteration.get('energy_total_scf_iteration')
            sec_scf_energy = sec_scf_iteration.m_create(Energy)
            if energy is not None:
                sec_scf_energy.total = EnergyEntry(value=energy)
            energy = iteration.get('x_gaussian_delta_energy_total_scf_iteration')
            if energy is not None:
                sec_scf_energy.change = energy

        iteration = section.get('scf_iteration_final')
        if iteration is not None:
            sec_scf_iteration = sec_scc.scf_iteration
            sec_scf_iteration = sec_scf_iteration[-1] if sec_scf_iteration else sec_scc.m_create(ScfIteration)
            sec_scf_energy = sec_scf_iteration.m_create(Energy)
            keys = [
                'x_gaussian_single_configuration_calculation_converged',
                'x_gaussian_hf_detect', 'energy_total', 'x_gaussian_energy_error',
                'energy_kinetic_electronic',
                'spin_S2', 'x_gaussian_after_annihilation_spin_S2',
                'x_gaussian_perturbation_energy']
            for key in keys:
                val = iteration.get(key)
                if val is not None:
                    if key.startswith('energy_'):
                        sec_scf_energy.m_add_sub_section(getattr(
                            Energy, key.replace('energy_', '')), EnergyEntry(value=val))
                    else:
                        setattr(sec_scf_iteration, key, val)
            if iteration.get('x_gaussian_single_configuration_calculation_converged') is not None:
                energy_scf = iteration.get('energy_total')
                electronic_ke = iteration.get(' energy_kinetic_electronic')
                if energy_scf is not None and electronic_ke is not None:
                    sec_scf_energy.electrostatic = EnergyEntry(value=energy_scf - electronic_ke)
                if energy_scf is not None:
                    sec_energy.total = EnergyEntry(value=energy_scf)
                sec_scc.calculation_converged = True

        return sec_scc

    def parse_system(self, n_run, section):
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)
        sec_atoms = sec_system.m_create(Atoms)
        lattice_vector = self.out_parser.get('run')[n_run].get('lattice_vector')
        if lattice_vector is not None:
            sec_atoms.lattice_vectors = lattice_vector * ureg.angstrom
            pbc = [len(lattice_vector) >= n for n in [1, 2, 3]]
            sec_atoms.periodic = [pbc]
        else:
            sec_atoms.lattice_vectors = np.zeros((3, 3))
            sec_atoms.periodic = [False] * 3

        orientation = section.get('standard_orientation')
        if orientation is None:
            orientation = section.get('input_orientation')
        if orientation is None:
            orientation = section.get('z_matrix_orientation')
        if orientation is not None:
            sec_atoms.labels = [
                ase.data.chemical_symbols[int(n)] for n in [o[1] for o in orientation]]
            sec_atoms.positions = [o[-3:] for o in orientation] * ureg.angstrom
            sec_system.x_gaussian_number_of_atoms = len(sec_system.atoms.labels)

        return sec_system

    def parse_configurations(self, n_run):
        systems = self.out_parser.get('run')[n_run].get('system', [])
        for system in systems:
            sec_system = self.parse_system(n_run, system)
            for calculation in system.get('calculation', [system]):
                sec_scc = self.parse_scc(calculation)
                if sec_scc is not None:
                    if sec_system is not None:
                        sec_scc.system_ref = sec_system
                    sec_method = self.archive.run[-1].method
                    if sec_method:
                        sec_scc.method_ref = sec_method[-1]

        iterations = self.out_parser.get('run')[n_run].get('iteration', [])
        sec_system = self.archive.run[0].system
        sec_method = self.archive.run[0].method
        for iteration in iterations:
            sec_scc = self.parse_scc(iteration)
            if sec_scc is not None:
                if sec_system:
                    sec_scc.system_ref = sec_system[-1]
                if sec_method:
                    sec_scc.method_ref = sec_method[-1]

    def parse_method(self, n_run):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        run = self.out_parser.get('run')[n_run]

        for key in ['x_gaussian_settings_corrected']:
            val = run.get(key)
            if val is None:
                continue
            setattr(sec_method, key, val)

        def resolve_method(parameter):
            def get_method(name):
                method = self._method_map.get(parameter, None)
                if method is not None:
                    return parameter

                method = self._xc_functional_map.get(parameter, None)
                return 'DFT' if method is not None else method

            method = get_method(parameter)
            if method is None:
                # TODO This is inefficient. Adapted from old parser
                for n in range(9, 1, -1):
                    method = get_method(parameter[0:n])
                    if method is not None:
                        break

            return method

        def resolve_prefix(name):
            name = name.split('=')[0].split('-')[0].strip()
            prefix = ''
            if name not in ['RHF', 'ROHF', 'UHF', 'UFF']:
                res = re.match(r'([RU]{1}O?)(.*)', name)
                if res is not None:
                    prefix = res[1] if res[1] else ''
                    name = res[2]
            return prefix, name

        def resolve_basis_set(parameter):
            basis_set = self._basis_set_map.get(parameter, None)
            if basis_set is not None:
                return (parameter, parameter)

            res = self._basis_set_pattern.match(parameter)
            if res is not None:
                basis_keys = [key for key in res.groups() if key is not None]
                if len(basis_keys) != 1:
                    self.logger.warning('Cannot resolve basis set', data=dict(key=parameter))
                return (basis_keys[0], parameter)

        def resolve_xc_functional(parameter):
            xc_functional = self._xc_functional_map.get(parameter, None)
            if xc_functional is not None:
                return parameter

            res = self._xc_functional_pattern.match(parameter)
            if res is not None:
                xc_keys = [key for key in res.groups() if key is not None]
                if len(xc_keys) != 2:
                    self.logger.warning('Cannot resolve xc functional', data=dict(key=name))
                    return

                x_name = 'LC-' if xc_keys[0] == 'LC-' else self._xc_functional_map.get(
                    xc_keys[0], [{}])[0].get('name', '')
                c_index = -1 if xc_keys[0] == 'LC-' else 0
                c_name = self._xc_functional_map.get(xc_keys[1], [{}])[c_index].get('name', '')

                if x_name and c_name:
                    return '%s%s' % (x_name, c_name)

        settings = run.get('x_gaussian_settings_corrected', '').upper()
        settings = re.sub(r'(?:#[Pp]? |# *)', '', settings)
        xc_functionals = set()
        basis_sets = set()
        methods = set()
        prefix = ''
        for setting in settings.split():
            parameter = setting.split('/')
            prefix, name = resolve_prefix(parameter[0])

            method = resolve_method(name)
            if method is not None:
                methods.add(method)

            xc_functional = resolve_xc_functional(name)
            if xc_functional is not None:
                xc_functionals.add(xc_functional)

            basis_set_parameter = parameter[0] if not parameter[1:] else parameter[1]
            basis_set = resolve_basis_set(basis_set_parameter.strip())
            if basis_set is not None:
                basis_sets.add(basis_set)

        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)
        if len(methods) != 1:
            self.logger.error('Found mutiple or no method', data=dict(
                n_parsed=len(methods)))
        for method in methods:
            sec_method.x_gaussian_method = method
            sec_electronic.method = method
            for entry in self._method_map.get(method, []):
                sec_elstruc_method = sec_method.m_create(x_gaussian_section_elstruc_method)
                sec_elstruc_method.x_gaussian_electronic_structure_method = '%s%s' % (
                    prefix, entry['name'])

        if len(basis_sets) != 1:
            self.logger.error('Found multiple or no basis set', data=dict(
                n_parsed=len(basis_sets)))
        for basis_set in basis_sets:
            sec_basis = sec_method.m_create(BasisSet)
            sec_basis.type = 'gaussians'
            sec_basis.name = basis_set[0]
            for _ in self._basis_set_map.get(basis_set[0], []):
                # TODO need to adjust basis_set atom centered to take multiple entries
                sec_basis_set_atom_centered = sec_basis.m_create(BasisSetAtomCentered)
                # old parser writes the full name of basis set here not the name on map
                sec_basis_set_atom_centered.name = basis_set[1]

        if len(xc_functionals) != 1:
            self.logger.error('Found multiple or no xc functional', data=dict(
                n_parsed=len(xc_functionals)))
        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for xc_functional in xc_functionals:
            sec_method.x_gaussian_xc = xc_functional
            for entry in self._xc_functional_map.get(xc_functional, []):
                if '_X_' in entry['name'] or entry['name'].endswith('_X'):
                    sec_xc_functional.exchange.append(Functional(name=entry['name']))
                elif '_C_' in entry['name'] or entry['name'].endswith('_C'):
                    sec_xc_functional.correlation.append(Functional(name=entry['name']))
                elif 'HYB' in entry['name'] or entry['name'].endswith('_C'):
                    sec_xc_functional.hybrid.append(Functional(name=entry['name']))
                else:
                    sec_xc_functional.contributions.append(Functional(name=entry['name']))

        for key in ['charge', 'spin_target']:
            val = self.out_parser.get('run')[n_run].get(key)
            if val is not None:
                setattr(sec_electronic, key, val)

    def init_parser(self, filepath, logger):
        self.out_parser.mainfile = filepath
        self.out_parser.logger = logger

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.init_parser(filepath, logger)

        runs = self.out_parser.get('run', [])
        for n in range(len(runs)):
            program = self.out_parser.get('program')
            sec_run = self.archive.m_create(Run)
            sec_run.program = Program(name='Gaussian', version=program[0])
            sec_run.x_gaussian_program_implementation = program[1]
            sec_run.x_gaussian_program_release_date = program[2]
            sec_run.x_gaussian_program_execution_date = program[3]

            for key in ['x_gaussian_chk_file', 'x_gaussian_memory', 'x_gaussian_number_of_processors']:
                val = self.out_parser.get(key)
                if val is not None:
                    setattr(sec_run, key, val)

            self.parse_method(n)

            self.parse_configurations(n)

            sec_times = sec_run.m_create(x_gaussian_section_times)
            for key in ['program_cpu_time', 'program_termination_date']:
                val = runs[n].get(key)
                if val is not None:
                    setattr(sec_times, 'x_gaussian_%s' % key, val.strip())
