import logging
import os
import numpy as np
import re
from ase.io import read
from ase import units as ase_units

from .metainfo import m_env
from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Functional, Smearing, Method, DFT, BasisSet, BasisSetCellDependent,
    XCFunctional, KMesh
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, EnergyEntry, Forces, ForcesEntry, BandEnergies
)
from nomad.datamodel.metainfo.workflow import Workflow


re_float = r'[\d\.\-\+Ee]+'


class EigenvalueParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_eigenvalues(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            kpoint = [0., 0., 0.] if val[0][0] == '#st' else [float(v.rstrip(',')) for v in val[0]]
            if len(val) == 1:
                return
            eigenvalues = np.array([[v[0], v[2], v[3]] for v in val[1:]], dtype=float)
            eigenvalues = np.transpose(eigenvalues)
            nspin = 2 if eigenvalues[0][1] == 1.0 else 1
            nbands = int(max(eigenvalues[0]))
            eigenvalues = eigenvalues[1:]
            eigenvalues.shape = (2, nbands, nspin)
            return kpoint, eigenvalues[0], eigenvalues[1]

        def str_to_fermi_energy(val_in):
            val = val_in.split()
            unit = ureg.eV if val[1].startswith('e') else ureg.hartree
            return float(val[0]) * unit

        self._quantities = [Quantity(
            'eigenvalues',
            r'(Eigenvalues \[[\s\S]+?)(?:\n\n|\Z)', sub_parser=TextParser(quantities=[
                Quantity(
                    'eigenvalues',
                    r'(?:(#st)\s*Spin\s*Eigenvalue\s*Occupation|#k =\s*\d+, k = \(([\-\d\.,\s]+)\))([\d\s\.\-updn]+)',
                    str_operation=str_to_eigenvalues, repeats=True, convert=False),
                Quantity(
                    'unit',
                    r'Eigenvalues \[(.*)\]', convert=False,
                    str_operation=lambda x: 'eV' if x == 'eV' else 'hartree'),
                Quantity(
                    'fermi_energy',
                    rf'Fermi energy =\s*({re_float} .*)',
                    convert=False, str_operation=str_to_fermi_energy)]))]


class InfoParser(EigenvalueParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):

        def str_to_energies(val_in):
            val = [v.split('=') for v in val_in.strip().split('\n')]
            unit = ureg.eV if '[eV]:' in val[0] else ureg.hartree
            return {v[0].strip(): float(v[1]) * unit for v in val if len(v) == 2}

        def str_to_forces(val_in):
            val = [v.split() for v in val_in.strip().split('\n')]
            unit = ureg.eV / ureg.angstrom if '[eV/A]' in val[0] else ureg.hartree / ureg.bohr
            return np.array([v[2:5] for v in val if len(v) == 5], dtype=float) * unit

        super().init_quantities()
        self._quantities += [
            Quantity(
                'brillouin_zone_sampling',
                r'Brillouin zone sampling([\s\S]+?)\*+\n\n', sub_parser=TextParser(quantities=[
                    Quantity(
                        'kgrid',
                        r'Dimensions of the k\-point grid\s*=(.*)', dtype=int),
                    Quantity(
                        'n_kpoints', r'Total number of k\-points\s*=(.*)', dtype=int),
                    Quantity(
                        'n_kpoints_reduced',
                        r'Number of symmetry-reduced k\-points\s*=(.*)', dtype=int),
                    Quantity(
                        'kpoints',
                        rf'\d+\s*({re_float})\s*({re_float})\s*({re_float})\s*({re_float})',
                        dtype=float, repeats=True)])),
            Quantity(
                'energies',
                r'Energy (\[[\s\S]+?)\n\n', str_operation=str_to_energies),
            Quantity(
                'total_magnetic_moment',
                rf'Total Magnetic Moment:\s*mz\s*=\s*({re_float})'),
            Quantity(
                'local_magnetic_moments',
                r'Ion\s*mz\s*([\w\s\.\-]+?)\n\n', convert=False,
                str_operation=lambda x: np.array(
                    [v.split()[2] for v in x.strip().split('\n')], dtype=float)),
            Quantity(
                'dipole',
                rf'Dipole:.*\[Debye\]\s*<x> =\s*\S+\s*({re_float})\s*'
                rf'<y> =\s*\S+\s*({re_float})\s*<z> =\s*\S+\s*({re_float})', dtype=float),
            Quantity(
                'forces',
                r'Forces on the ions (\[.*\]\s*)Ion\s*x\s*y\s*z\s*([\s\S]*)',
                str_operation=str_to_forces, convert=False)]


class ControlParser(TextParser):
    def __init__(self):
        super().__init__()
        self._constants = {
            'pi': np.pi, 'angstrom': 1. / ase_units.Bohr, 'ev': 1. / ase_units.Hartree,
            'yes': True, 'no': False, 't': True, 'f': False, 'true': True, 'false': False,
            'i': 1j}
        self._re_sqrt = re.compile(r'sqrt([\w\. ]+\Z)')
        self._info = None

    def init_quantities(self):
        def str_to_line(val_in):
            val = val_in.replace('"', '').replace("'", '').split('=', 1)
            return [v.strip().split('#')[0] for v in val]

        self._quantities = [
            Quantity(
                'line', r'(\w.*\s*=\s*.*)#?', str_operation=str_to_line, repeats=True)]

    @property
    def mainfile(self):
        return super().mainfile

    @mainfile.setter
    def mainfile(self, val):
        # TODO pylint complains when inheriting property
        self._results = None
        self._file_handler = None
        self._mainfile = os.path.abspath(val) if val is not None else val
        self._info = None
        self._keys_mapping = dict()

    def evaluate_value(self, value):
        # evaluate octopus parameterized variables, e.g. 2*angstrom
        # TODO implement all operations and parameters supported by Octopus

        if isinstance(value, list):
            return [self.evaluate_value(v) for v in value]

        if not isinstance(value, str):
            return value

        try:
            return float(value)
        except Exception:
            pass

        value = value.strip()
        if value == '':
            return 1

        val = self._constants.get(value.lower(), None)
        if val is not None:
            return val

        val = self._info.get(self._keys_mapping.get(value.lower(), None), None)
        if val is not None:
            return val

        open_p = value.rfind('(')
        if open_p > -1:
            n_groups = value.count('(')
            if n_groups != value.count(')'):
                return value
            for _ in range(n_groups):
                part = value[open_p + 1:]
                part = part[:part.find(')')]
                value = value.replace('(%s)' % part, str(self.evaluate_value(part)))
                open_p = value.rfind('(')
            return self.evaluate_value(value)

        sqrt = self._re_sqrt.match(value)
        if sqrt:
            val = self.evaluate_value(sqrt.group(1))
            return np.sqrt(val)

        vals = value.split('**')
        if len(vals) > 1:
            vals = [self.evaluate_value(v) for v in vals]
            val = vals[0]
            for v in reversed(vals[1:]):
                val = val ** v
            return val

        vals = value.split('*')
        if len(vals) > 1:
            vals = [self.evaluate_value(v) for v in vals]
            return np.product(vals)

        vals = value.split('/')
        if len(vals) > 1:
            vals = [self.evaluate_value(v) for v in vals]
            val = vals[0]
            for v in vals[1:]:
                val /= v
            return val

        if '+' in value:
            vals = value.split('+')
            vals = [self.evaluate_value(v) for v in vals]
            val = 0.0
            for v in vals:
                val += v
            return val

        if '-' in value:
            vals = value.split('-')
            vals = [self.evaluate_value(v) for v in vals]
            val = 0.0
            for v in vals:
                val -= v
            return val

        return value

    @property
    def info(self):
        if self._info is None:
            self._info = {v[0].strip(): v[1] for v in self.get('line', [])}
            self._info.update({v[0].strip(): v[1:] for v in self.get('block', [])})
            self._keys_mapping = {k.lower(): k for k in self._info.keys()}
            for key, val in self._info.items():
                try:
                    val = self.evaluate_value(val)
                except Exception:
                    continue
                self._info[key] = val
                self._keys_mapping[key.lower()] = key
        return self._info


class InpParser(ControlParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_block(val_in):
            val = [v.split('#')[0] for v in val_in.strip().split('\n')]
            val = [
                v.replace('"', '').replace("'", '').split('|')
                for v in val if v]
            val[0] = val[0][0]
            return val

        super().init_quantities()
        self._quantities += [
            Quantity(
                'block', r'%([\s\S]+?)%', repeats=True, str_operation=str_to_block)]

    def get_coordinates(self):
        val = self.info.get('Coordinates', self.info.get('ReducedCoordinates', []))

        symbols = []
        coordinates = []
        for v in val:
            symbols.append(v[0].strip())
            coordinates.append(v[1:])

        coordinates = np.array(coordinates, dtype=float)
        coordinates.shape = (len(symbols), 3)
        return symbols, coordinates


class LogParser(ControlParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_block(val_in):
            val = val_in.strip().split('\n')
            name = val[0].strip().replace('"', '').replace("'", '')
            val = [v.split('#')[0].split('=')[1].replace('"', '').replace("'", '').strip() for v in val[1:]]
            return [name, val]

        super().init_quantities()
        self._quantities += [
            Quantity(
                'block',
                r'Opened block([\s\S]+?)Closed block',
                repeats=True, str_operation=str_to_block)]

    def get_coordinates(self):
        symbols = []
        coordinates = []

        val = self.info.get('Coordinates', self.info.get('ReducedCoordinates', [[]]))[0]

        for v in val:
            if isinstance(v, str):
                symbols.append(v.strip())
            else:
                coordinates.append(v)

        coordinates = np.array(coordinates, dtype=float)
        coordinates.shape = (len(symbols), 3)

        return symbols, coordinates


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_option(val_in):
            val = val_in.strip().split(':')
            return [val[0].strip(), ''.join(val[1:]).strip()]

        def str_to_cell(val_in):
            unit = ureg.angstrom if val_in.lower().startswith('a') else ureg.bohr
            val = [v.split() for v in val_in.strip().split('\n')[1:]]
            return np.array(val, dtype=float) * unit

        def str_to_spacing(val_in):
            unit = ureg.angstrom if val_in.startswith('A') else ureg.bohr
            return np.array(val_in.split()[1:4], dtype=float) * unit

        def str_to_energy(val_in):
            val = val_in.split()
            unit = ureg.eV if val[1].startswith('e') else ureg.hartree
            return float(val[0]) * unit

        def str_to_td_iteration(val_in):
            val = val_in.strip().split()
            return dict(
                iter=int(val[0]), time=float(val[1]), energy=float(val[2]),
                scfsteps=int(val[3]), elapsed_time=float(val[4]))

        iteration_quantities = [
            Quantity('energy_total', rf'etot\s*=\s*({re_float})'),
            # TODO scf_iteration eigenvalues are sometimes truncated and unusable
            Quantity(
                'fermi_level', rf'Fermi energy\s*=\s*({re_float} .*)',
                str_operation=str_to_energy, convert=False),
            Quantity(
                'time',
                r'Elapsed time for SCF step\s*\d+:\s*([\d\.]+)', unit='s', dtype=float)]

        self._quantities = [
            Quantity(
                'header',
                r'Running octopus([\s\S]+?)\*{10}', sub_parser=TextParser(quantities=[
                    Quantity(
                        'options',
                        r'\n *([\w ]+?\s*:\s*.*)', str_operation=str_to_option, repeats=True),
                ])),
            Quantity(
                'grid',
                r'\*\s*Grid\s*\*+\s*([\s\S]+?)\*{10}', sub_parser=TextParser(quantities=[
                    Quantity('boxshape', r'Type\s*=\s*(.*)'),
                    Quantity(
                        'npbc',
                        r'Octopus will treat the system as periodic in (\S+) dim', dtype=int),
                    Quantity(
                        'cell',
                        r'Lattice Vectors \[(.*)\]([-\d\s\.]+)',
                        str_operation=str_to_cell, convert=False),
                    Quantity(
                        'spacing',
                        r'Spacing \[(.*)\] = \(\s*(\S+), (\S+), (\S+)\s*\)',
                        str_operation=str_to_spacing, convert=False)])),
            Quantity(
                'theory_level',
                r'\*\s*Theory Level\s*\*+\s*([\s\S]+?)\*{10}', sub_parser=TextParser(quantities=[
                    Quantity('theory_level', r'\[TheoryLevel = (.+)\]', flatten=False),
                    Quantity('exchange', r'Exchange\s+(.*) \(', flatten=False),
                    Quantity('correlation', r'Correlation\s+(.*) \(', flatten=False)
                ])
            ),
            Quantity(
                'self_consistent',
                r'Info: Starting SCF iteration\.\s*([\s\S]+?)Info: SCF', repeats=True,
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        r'SCF CYCLE ITER #\s*(\d+\s*\*+[\s\S]+?)\*{10}', repeats=True,
                        sub_parser=TextParser(quantities=iteration_quantities))])),
            Quantity(
                'time_dependent',
                r'Time\-Dependent Simulation \*+([\s\S]+?)Info: Finished writing information',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'iteration',
                        rf'\n *(\d+\s*{re_float}\s*{re_float}\s*\d+\s*{re_float}) *\n',
                        str_operation=str_to_td_iteration, repeats=True, convert=False)])
            ),
            Quantity(
                'x_octopus_info_scf_converged_iterations',
                r'SCF converged in\s*(\d+) iterations', dtype=int),
            Quantity(
                'minimization',
                r'(MINIMIZATION ITER #:\s*\d+\s*\++\s*Energy[\s\S]+?\+{10})',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_total', rf'Energy\s*=\s*({re_float} .*)',
                        str_operation=str_to_energy, convert=False),
                    Quantity(
                        'number', r'ITER #:\s*(\d+)', dtype=int)]))
            # calculation results are not printed in outfile but in info
        ]

        self._header = None

    @property
    def header(self):
        return {k: v for k, v in self.get('header', {}).get('options', [])}


class OctopusParser:
    def __init__(self):
        self.out_parser = OutParser()
        self.log_parser = LogParser()
        self.info_parser = InfoParser()
        self.inp_parser = InpParser()
        self.eigenvalue_parser = EigenvalueParser()

        self._info = None

        self._metainfo_keys_mapping = {
            'Total': 'energy_total', 'Free': 'energy_free', 'Ion-ion': 'energy_nuclear_repulsion',
            'Eigenvalues': 'energy_sum_eigenvalues', 'Hartree': 'energy_electrostatic',
            'Exchange': 'energy_exchange', 'Correlation': 'energy_correlation', 'vanderWaals': 'energy_van_der_Waals',
            '-TS': 'energy_correction_entropy', 'Kinetic': 'energy_kinetic_electronic',
            'SpinComponents': 'n_spin_channels', 'ExcessCharge': 'charge'}

        # TODO metainfo smearing_kind should be extended to cover all functions,
        # e.g. gaussian and spline are not the same
        self._smearing_functions = {
            1: 'empty', 2: 'fermi', 3: 'marzari-vanderbilt', 4: 'methfessel_paxton',
            5: 'gaussian', 'semiconducting': 'empty', 'spline_smearing': 'gaussian',
            'fermi_dirac': 'fermi', 'cold_smearing': 'marzari-vanderbilt',
            'methfessel_paxton': 'methfessel-paxton'}

        # TODO metainfo electronic_structure_method should be extended to cover all these
        # HF is not DFT but nomad treats it this way
        self._theory_levels = {
            1: 'DFT', 2: None, 3: 'DFT', 4: 'DFT', 5: None, 'hartree': 'DFT',
            'independent_particles': None, 'hartree_fock': 'DFT', 'dft': 'DFT',
            'classical': None}

        # List was generated from https://github.com/qsnake/octopus/blob/master/share/varinfo
        # In parser.log, XCFunctional is an integer given as a sum of exchange
        # and correlation. In stdout.txt, XCFunctional can be read as a string
        # but it is not always consistent with the mapping that we have below (see for
        # example Exchange which is Slater Exchange in stdout.txt). Therefore, in
        # resolving the nomad xc_functional name, we first try to get it from the string
        # output of stdout.txt and if it does not work, we get it from the integer value
        # in parser.log.
        # TODO resolve solely from the integer value
        self._xc_functionals = {
            'Exchange': ('lda_x', 1),
            'Wigner parametrization': ('lda_c_wigner', 2000),
            'Random Phase Approximation': ('lda_c_rpa', 3000),
            'Hedin & Lundqvist': ('lda_c_hl', 4000),
            'Gunnarson & Lundqvist': ('lda_c_gl', 5000),
            'Slater Xalpha': ('lda_c_xalpha', 6000),
            'Vosko, Wilk, & Nussair': ('lda_c_vwn', 7000),
            'Vosko, Wilk, & Nussair (RPA)': ('lda_c_vwn_rpa', 8000),
            'Perdew & Zunger': ('lda_c_pz', 9000),
            'Perdew & Zunger (Modified)': ('lda_c_pz_mod', 10000),
            'Ortiz & Ballone (PZ)': ('lda_c_ob_pz', 11000),
            'Perdew & Wang': ('lda_c_pw', 12000),
            'Perdew & Wang (Modified)': ('lda_c_pw_mod', 13000),
            'Ortiz & Ballone (PW)': ('lda_c_ob_pw', 14000),
            'Attacalite et al': ('lda_c_2d_amgb', 15000),
            'Pittalis, Rasanen & Marques correlation in 2D': ('lda_c_2d_prm', 16000),
            'von Barth & Hedin': ('lda_c_vbh', 17000),
            'Casula, Sorella, and Senatore 1D correlation': ('lda_c_1d_csc', 18000),
            'Exchange in 2D': ('lda_x_2d', 19),
            'Teter 93 parametrization': ('lda_xc_teter93', 20000),
            'Exchange in 1D': ('lda_x_1d', 21),
            'Modified LSD (version 1) of Proynov and Salahub': ('lda_c_ml1', 22000),
            'Modified LSD (version 2) of Proynov and Salahub': ('lda_c_ml2', 23000),
            'Gombas parametrization': ('lda_c_gombas', 24000),
            'Thomas-Fermi kinetic energy functional': ('lda_k_tf', 50),
            'Lee and Parr Gaussian ansatz': ('lda_k_lp', 51),
            'Perdew, Burke & Ernzerhof exchange': ('gga_x_pbe', 101),
            'Perdew, Burke & Ernzerhof exchange (revised)': ('gga_x_pbe_r', 102),
            'Becke 86 Xalfa,beta,gamma': ('gga_x_2d_b86', 128),
            'Herman et al original GGA': ('gga_x_herman', 104),
            'Becke 86 Xalfa,beta,gamma (with mod. grad. correction)': ('gga_x_b86_mgc', 105),
            'Becke 88': ('gga_x_b88', 106),
            'Gill 96': ('gga_x_g96', 107),
            'Perdew & Wang 86': ('gga_x_pw86', 108),
            'Perdew & Wang 91': ('gga_c_pw91', 134000),
            'Handy & Cohen OPTX 01': ('gga_x_optx', 110),
            'dePristo & Kress 87 (version R1)': ('gga_x_dk87_r1', 111),
            'dePristo & Kress 87 (version R2)': ('gga_x_dk87_r2', 112),
            'Lacks & Gordon 93': ('gga_x_lg93', 113),
            'Filatov & Thiel 97 (version A)': ('gga_x_ft97_a', 114),
            'Filatov & Thiel 97 (version B)': ('gga_x_ft97_b', 115),
            'Perdew, Burke & Ernzerhof exchange (solids)': ('gga_x_pbe_sol', 116),
            'Hammer, Hansen & Norskov (PBE-like)': ('gga_x_rpbe', 117),
            'Wu & Cohen': ('gga_x_wc', 118),
            'Modified form of PW91 by Adamo & Barone': ('gga_x_mpw91', 119),
            'Armiento & Mattsson 05 exchange': ('gga_x_am05', 120),
            'Madsen (PBE-like)': ('gga_x_pbea', 121),
            'Adamo & Barone modification to PBE': ('gga_x_mpbe', 122),
            'xPBE reparametrization by Xu & Goddard': ('gga_c_xpbe', 136000),
            'Becke 86 MGC for 2D systems': ('gga_x_2d_b86_mgc', 124),
            'Bayesian best fit for the enhancement factor': ('gga_x_bayesian', 125),
            'JSJR reparametrization by Pedroza, Silva & Capelle': ('gga_x_pbe_jsjr', 126),
            'Becke 88 in 2D': ('gga_x_2d_b88', 127),
            'Perdew, Burke & Ernzerhof exchange in 2D': ('gga_x_2d_pbe', 129),
            'Perdew, Burke & Ernzerhof correlation': ('gga_c_pbe', 130000),
            'Lee, Yang & Parr': ('gga_c_lyp', 131000),
            'Perdew 86': ('gga_c_p86', 132000),
            'Perdew, Burke & Ernzerhof correlation SOL': ('gga_c_pbe_sol', 133000),
            'Armiento & Mattsson 05 correlation': ('gga_c_am05', 135000),
            'Langreth and Mehl correlation': ('gga_c_lm', 137000),
            'JRGX reparametrization by Pedroza, Silva & Capelle': ('gga_c_pbe_jrgx', 138000),
            'Becke 88 reoptimized to be used with vdW functional of Dion et al': ('gga_x_optb88_vdw', 139),
            'PBE reparametrization for vdW': ('gga_x_optpbe_vdw', 141),
            'Regularized PBE': ('gga_c_rge2', 143000),
            'refitted Perdew & Wang 86': ('gga_x_rpw86', 144),
            'Keal and Tozer version 1': ('gga_x_kt1', 145),
            'Keal and Tozer version 2': ('gga_xc_kt2', 146000),
            'Wilson & Levy': ('gga_c_wl', 147000),
            'Wilson & Ivanov': ('gga_c_wi', 148000),
            'van Leeuwen & Baerends': ('gga_x_lb', 160),
            'HCTH functional fitted to 93 molecules': ('gga_xc_hcth_93', 161000),
            'HCTH functional fitted to 120 molecules': ('gga_xc_hcth_120', 162000),
            'HCTH functional fitted to 147 molecules': ('gga_xc_hcth_407', 164000),
            'Empirical functionals from Adamson, Gill, and Pople': ('gga_xc_edf1', 165000),
            'XLYP functional': ('gga_xc_xlyp', 166000),
            'Becke 97': ('hyb_gga_xc_b97', 407000),
            'Becke 97-1': ('hyb_gga_xc_b97_1', 408000),
            'Becke 97-2': ('hyb_gga_xc_b97_2', 410000),
            'Grimme functional to be used with C6 vdW term': ('gga_xc_b97_d', 170000),
            'Boese-Martin for Kinetics': ('hyb_gga_xc_b97_k', 413000),
            'Becke 97-3': ('hyb_gga_xc_b97_3', 414000),
            'Functionals fitted for water': ('gga_xc_pbelyp1w', 175000),
            'Schmider-Becke 98 parameterization 1a': ('hyb_gga_xc_sb98_1a', 420000),
            'Schmider-Becke 98 parameterization 1b': ('hyb_gga_xc_sb98_1b', 421000),
            'Schmider-Becke 98 parameterization 1c': ('hyb_gga_xc_sb98_1c', 422000),
            'Schmider-Becke 98 parameterization 2a': ('hyb_gga_xc_sb98_2a', 423000),
            'Schmider-Becke 98 parameterization 2b': ('hyb_gga_xc_sb98_2b', 424000),
            'Schmider-Becke 98 parameterization 2c': ('hyb_gga_xc_sb98_2c', 425000),
            'van Leeuwen & Baerends modified': ('gga_x_lbm', 182),
            'von Weiszaecker correction to Thomas-Fermi': ('gga_k_vw', 500),
            'Second-order gradient expansion (l = 1/9)': ('gga_k_ge2', 501),
            'TF-lambda-vW form by Golden (l = 13/45)': ('gga_k_golden', 502),
            'TF-lambda-vW form by Yonei and Tomishima (l = 1/5)': ('gga_k_yt65', 503),
            'TF-lambda-vW form by Baltin (l = 5/9)': ('gga_k_baltin', 504),
            'TF-lambda-vW form by Lieb (l = 0.185909191)': ('gga_k_lieb', 505),
            'gamma-TFvW form by Acharya et al [g = 1 - 1.412/N^(1/3)]': ('gga_k_absr1', 506),
            'gamma-TFvW form by Acharya et al [g = 1 - 1.332/N^(1/3)]': ('gga_k_absr2', 507),
            'gamma-TFvW form by Gázquez and Robles': ('gga_k_gr', 508),
            'gamma-TFvW form by Ludeña': ('gga_k_ludena', 509),
            'gamma-TFvW form by Ghosh and Parr': ('gga_k_gp85', 510),
            'Pearson': ('gga_k_pearson', 511),
            'Ou-Yang and Levy v.1': ('gga_k_ol1', 512),
            'Ou-Yang and Levy v.2': ('gga_k_ol2', 513),
            'Fuentealba & Reyes (B88 version)': ('gga_k_fr_b88', 514),
            'Fuentealba & Reyes (PW86 version)': ('gga_k_fr_pw86', 515),
            'The original hybrid proposed by Becke': ('hyb_gga_xc_b3pw91', 401000),
            'The (in)famous B3LYP': ('hyb_gga_xc_b3lyp', 402000),
            'Perdew 86 hybrid similar to B3PW91': ('hyb_gga_xc_b3p86', 403000),
            'hybrid using the optx functional': ('hyb_gga_xc_o3lyp', 404000),
            'mixture of mPW91 and PW91 optimized for kinetics': ('hyb_gga_xc_mpw1k', 405000),
            'aka PBE0 or PBE1PBE': ('hyb_gga_xc_pbeh', 406000),
            'maybe the best hybrid': ('hyb_gga_xc_x3lyp', 411000),
            'Becke 1-parameter mixture of WC and PBE': ('hyb_gga_xc_b1wc', 412000),
            'mixture with the mPW functional': ('hyb_gga_xc_mpw3pw', 415000),
            'Becke 1-parameter mixture of B88 and LYP': ('hyb_gga_xc_b1lyp', 416000),
            'Becke 1-parameter mixture of B88 and PW91': ('hyb_gga_xc_b1pw91', 417000),
            'Becke 1-parameter mixture of mPW91 and PW91': ('hyb_gga_xc_mpw1pw', 418000),
            'mixture of mPW and LYP': ('hyb_gga_xc_mpw3lyp', 419000),
            'Local tau approximation of Ernzerhof & Scuseria': ('mgga_x_lta', 201),
            'Perdew, Tao, Staroverov & Scuseria exchange': ('mgga_x_tpss', 202),
            'Zhao, Truhlar exchange': ('mgga_x_m06l', 203),
            'GVT4 from Van Voorhis and Scuseria (exchange part)': ('mgga_x_gvt4', 204),
            'tau-HCTH from Boese and Handy': ('mgga_x_tau_hcth', 205),
            'Becke-Roussel 89': ('mgga_x_br89', 206),
            'Becke & Johnson correction to Becke-Roussel 89': ('mgga_x_bj06', 207),
            'Tran & Blaha correction to Becke & Johnson': ('mgga_x_tb09', 208),
            'Rasanen, Pittalis, and Proetto correction to Becke & Johnson': ('mgga_x_rpp09', 209),
            'Pittalis, Rasanen, Helbig, Gross Exchange Functional': ('mgga_x_2d_prhg07', 210),
            'PRGH07 with PRP10 correction': ('mgga_x_2d_prhg07_prp10', 211),
            'Perdew, Tao, Staroverov & Scuseria correlation': ('mgga_c_tpss', 231000),
            'VSxc from Van Voorhis and Scuseria (correlation part)': ('mgga_c_vsxc', 232000),
            'Orestes, Marcasso & Capelle': ('lca_omc', 301),
            'Lee, Colwell & Handy': ('lca_lch', 302),
            'OEP: Exact exchange': ('oep_x', 901)}

        self._units_mapping = dict(ev=ureg.eV, hartree=ureg.hartree, angstrom=ureg.angstrom, bohr=ureg.bohr)

    def init_parser(self, filepath, logger):
        self.out_parser.mainfile = filepath
        self.out_parser.logger = logger

        self.info_parser.mainfile = os.path.join(self.maindir, 'static/info')
        self.info_parser.logger = logger
        self.log_parser.mainfile = os.path.join(self.maindir, 'exec/parser.log')
        self.log_parser.logger = logger
        self.inp_parser.mainfile = os.path.join(self.maindir, 'inp')
        self.inp_parser.logger = logger
        self.eigenvalue_parser.mainfile = os.path.join(self.maindir, 'static/eigenvalues')
        self.eigenvalue_parser.logger = logger
        self._info = None

    @property
    def info(self):
        if self._info is None:
            self._info = dict()
            self._info.update(self.inp_parser.info)
            # the variables read from log are more reliable as these are converted
            # to proper octopus values, i.e. we do not worry about compatibility issue
            self._info.update(self.log_parser.info)
            # add units for energy, length
            # TODO not sure what defaults are for units and expected values for units(input)
            # and their meaning
            energyunit = 'hartree'
            lengthunit = 'bohr'
            units = self._info.get('Units', self._info.get('UnitsInput', 0))
            if isinstance(units, str):
                units = units.lower()
                energyunit = 'eV' if 'ev' in units else energyunit
                lengthunit = 'angstrom' if 'angs' in units else lengthunit
            elif isinstance(units, int):
                energyunit = 'eV' if units == 1 else energyunit
                lengthunit = 'angstrom' if units == 1 else lengthunit
            elif units is None:
                cell = self.out_parser.get('grid', {}).get('cell')
                if cell is not None:
                    lengthunit = cell.units
                    energyunit = 'eV' if lengthunit == 'angstrom' else energyunit
            self._info.update(dict(energyunit=energyunit, lengthunit=lengthunit))
        return self._info

    def parse_scc(self):
        sec_run = self.archive.run[-1]

        # self-consistent
        # SCF energies are printed only in output
        for scf in self.out_parser.get('self_consistent', []):
            sec_scc = sec_run.m_create(Calculation)
            for iteration in scf.get('iteration', []):
                sec_scf = sec_scc.m_create(ScfIteration)
                sec_scf_energy = sec_scf.m_create(Energy)
                fermi_level = iteration.get('fermi_level')
                unit = None
                if fermi_level is not None:
                    sec_scf_energy.fermi = fermi_level
                energy_total = iteration.get('energy_total')
                if energy_total is not None:
                    unit = self._units_mapping.get(self.info.get('energyunit', 'hartree').lower()) if unit is None else unit
                    sec_scf_energy.total = EnergyEntry(value=energy_total * unit)
                time = iteration.get('time')
                if time is not None:
                    sec_scf.time_calculation = time

        # time-dependent
        # each td iteration is an scc
        for td in self.out_parser.get('time_dependent', []):
            for iteration in td.get('iteration', []):
                sec_scc = sec_run.m_create(Calculation)
                energy = iteration.get('energy', None)
                if energy is not None:
                    sec_scc.energy = Energy(total=EnergyEntry(
                        value=energy * self._units_mapping.get(self.info.get('energyunit', 'hartree').lower())))

        # TODO add other calculation types

        # TODO bandstructures

        # TODO dipoles

        # TODO add volumetric data

        # TODO test geometry optimizations, cannot find an exaple
        for minimization in self.out_parser.get('minimization', []):
            sec_scc = sec_run.m_create(Calculation)
            energy_total = minimization.get('energy_total')
            if energy_total is not None:
                sec_scc.energy = Energy(total=EnergyEntry(value=energy_total))
            number = minimization.get('number')
            cell = sec_run.system[-1].atoms.lattice_vectors
            pbc = sec_run.system[-1].atoms.periodic
            if number is not None:
                path = os.path.join(self.out_parser.maindir, 'geom/go.%04d.xyz' % number)
                try:
                    atoms = read(path, format='xyz')
                except Exception:
                    continue
                sec_system = sec_run.m_create(System)
                # TODO xyz does not contain cell info right?
                cell = cell if cell is None else atoms.get_cell() * ureg.angstrom
                sec_atoms = sec_system.m_create(Atoms)
                sec_atoms.lattice_vectors = cell
                sec_atoms.periodic = pbc
                sec_atoms.positions = atoms.get_positions() * ureg.angstrom
                sec_atoms.labels = atoms.get_chemical_symbols()
                sec_scc.system_ref = sec_system

        if len(sec_run.calculation) > 0:
            sec_scc = sec_run.calculation[-1]
            # final results are printed only in static/info
            # energies
            energies = self.info_parser.get('energies', {})
            sec_energy = sec_scc.m_create(Energy)
            for key, val in energies.items():
                metainfo_key = self._metainfo_keys_mapping.get(key, None)
                if metainfo_key is None:
                    continue
                if metainfo_key.startswith('energy_'):
                    sec_energy.m_add_sub_section(getattr(
                        Energy, metainfo_key.replace('energy_', '').lower()), EnergyEntry(value=val))
                else:
                    setattr(sec_scc, metainfo_key, val)

            # forces
            forces = self.info_parser.get('forces')
            if forces is not None:
                sec_scc.forces = Forces(free=ForcesEntry(value_raw=forces))

            # eigenvalues
            eigenvalues = self.eigenvalue_parser.get('eigenvalues', self.info_parser.get('eigenvalues'))
            if eigenvalues is not None and eigenvalues.get('eigenvalues') is not None:
                kpts, eigs, occs = list(zip(*[e for e in eigenvalues.eigenvalues if e is not None]))
                eigs = np.transpose(eigs, axes=(2, 0, 1))
                occs = np.transpose(occs, axes=(2, 0, 1))
                sec_eigenvalues = sec_scc.m_create(BandEnergies)
                if len(kpts) > 0:
                    sec_eigenvalues.kpoints = kpts
                eigs = eigs * self._units_mapping.get(self.info.get('energyunit').lower())
                sec_eigenvalues.energies = eigs
                sec_eigenvalues.occupations = occs

                fermi_level = eigenvalues.get('fermi_energy')
                if fermi_level is not None:
                    sec_energy.fermi = fermi_level

            converged = self.out_parser.get('x_octopus_info_scf_converged_iterations')
            if converged is not None:
                sec_run.x_octopus_info_scf_converged_iterations = converged

            sec_scc.method_ref = sec_run.method[-1]
            sec_scc.system_ref = sec_run.system[-1]

    def parse_system(self):
        sec_run = self.archive.run[-1]
        sec_system = sec_run.m_create(System)
        sec_atoms = sec_system.m_create(Atoms)

        cell = self.out_parser.get('grid', {}).get('cell')
        if cell is not None:
            sec_atoms.lattice_vectors = cell
            npbc = self.out_parser.get('grid', {}).get('npbc', 3)
            pbc = [True for _ in range(npbc)]
            sec_atoms.periodic = pbc + [False] * (3 - len(pbc))

        symbols, coordinates = self.log_parser.get_coordinates()
        if len(coordinates) == 0:
            # get if from inp
            symbols, coordinates = self.inp_parser.get_coordinates()
        if len(coordinates) == 0:
            # try to read from file
            atoms = None
            file_types = {
                'PDBCoordinates': 'proteindatabank', 'XYZCoordinates': 'xyz',
                'XSFCoordinates': 'xsf'}
            for ftype, fformat in file_types.items():
                filename = self.info.get(ftype)
                if filename is None:
                    continue
                try:
                    atoms = read(os.path.join(self.maindir, filename), format=fformat)
                except Exception:
                    self.logger.error('Error reading coordinates file', data=dict(filename=filename))
                if atoms is not None:
                    symbols = atoms.get_chemical_symbols()
                    coordinates = atoms.get_positions()
                    break
        if len(coordinates) != 0:
            if self.info.get('ReducedCoordinates', None) is not None and cell is not None:
                coordinates = np.dot(coordinates, cell.magnitude)
                units = cell.units
            elif self.info.get('Coordinates', None) is not None:
                units = self.info.get('lengthunit')
            else:
                # read from ase atoms (in angstroms)
                units = 'angstrom'
            sec_atoms.positions = coordinates * self._units_mapping.get(str(units).lower())
            sec_atoms.labels = symbols
        else:
            self.logger.error('Error parsing atom positions and labels.')

    def parse_method(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        k_mesh = sec_method.m_create(KMesh)
        brillouin_zone_sampling = self.info_parser.get('brillouin_zone_sampling')
        if brillouin_zone_sampling is not None:
            if brillouin_zone_sampling.results is not None:
                k_mesh.grid = brillouin_zone_sampling.results.get('kgrid')

        sec_electronic = sec_method.m_create(Electronic)
        sec_dft = sec_method.m_create(DFT)

        # basis set
        sec_basis = sec_method.m_create(BasisSet)
        sec_basis.type = 'real-space grid'
        sec_basis_set = sec_basis.m_create(BasisSetCellDependent)
        sec_basis_set.kind = 'realspace_grids'

        # smearing
        smearing_function = self._smearing_functions.get(self.info.get('SmearingFunction'), None)
        if smearing_function is not None:
            sec_electronic.smearing = Smearing(kind=smearing_function)
            smearing_width = self.info.get('Smearing', None)
            if smearing_width is not None:
                sec_electronic.smearing.width = (smearing_width * self._units_mapping.get(
                    self.info['energyunit'].lower())).to('joule').magnitude

        # check dft+u
        dft_u = self.info.get('DFTULevel')
        if dft_u is not None:
            sec_electronic.method = 'DFT+U'
        else:
            theory_level = self._theory_levels.get(self.info.get('TheoryLevel', 4), None)
            if theory_level is not None:
                sec_electronic.method = theory_level

        # xc functional
        xc_functionals = []
        xc_int_sum = 0
        xc_functional = self.info.get('XCFunctional', 0)
        if isinstance(xc_functional, str):
            xc_functionals = [xc.strip() for xc in xc_functional.upper().split('+')]
        else:
            # we try to resolve from output string
            for key in ['exchange', 'correlation']:
                val = self.out_parser.get('theory_level', {}).get(key, None)
                name, number = self._xc_functionals.get(val, (None, 0))
                if name is not None:
                    xc_functionals.append(name.upper())
                    xc_int_sum += number
            # get it from log
            diff = xc_functional - xc_int_sum
            if diff > 0:
                names_numbers = list(zip(*self._xc_functionals.values()))
                while diff > 0:
                    index = np.argmin(abs(np.array(names_numbers[1]) - diff))
                    xc_functionals.append(names_numbers[0][index].upper())
                    diff -= names_numbers[1][index]
                if diff < 0:
                    xc_functionals = []
                    self.logger.error(
                        'Error resolving xc functional', data=dict(XCfunctional=xc_functional))
        sec_xc_functional = sec_dft.m_create(XCFunctional)
        for xc_functional in xc_functionals:
            if '_X_' in xc_functional or xc_functional.endswith('_X'):
                sec_xc_functional.exchange.append(Functional(name=xc_functional))
            elif '_C_' in xc_functional or xc_functional.endswith('_C'):
                sec_xc_functional.correlation.append(Functional(name=xc_functional))
            elif 'HYB' in xc_functional:
                sec_xc_functional.hybrid.append(Functional(name=xc_functional))
            else:
                sec_xc_functional.contributions.append(Functional(name=xc_functional))

        method_keys = ['SpinComponents', 'ExcessCharge']
        for key in method_keys:
            val = self.info.get(key)
            metainfo_key = self._metainfo_keys_mapping.get(key, None)
            if val is None or metainfo_key is None:
                continue
            try:
                setattr(sec_electronic, metainfo_key, int(val))
            except Exception:
                self.logger.warning('Error setting metainfo', data=dict(key=metainfo_key))

        # convert parsed values to proper metainfo type
        definitions = dict(m_env.all_definitions_by_name)

        def convert_to_metainfo(prefix, key, val):
            metainfo_name = 'x_octopus_%s_%s' % (prefix, key)
            metainfo_type = definitions.get(metainfo_name, None)
            if metainfo_type is not None:
                metainfo_type = metainfo_type[0].type
                if isinstance(metainfo_type, np.dtype):
                    val = np.array(val, metainfo_type)
                else:
                    val = metainfo_type(val)
            return metainfo_name, val

        # parse keywords from inp and parser.log
        sources = {'input': self.inp_parser, 'parserlog': self.log_parser}
        for prefix, source in sources.items():
            for key, val in source.info.items():
                try:
                    val = source.info.get(key)
                    metainfo_name, val = convert_to_metainfo(prefix, key, val)
                    setattr(sec_run, metainfo_name, val)
                except Exception:
                    self.logger.warning('Error setting metainfo', data=dict(key=key))

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger

        self.maindir = os.path.dirname(os.path.abspath(filepath))
        self.init_parser(filepath, logger)

        sec_run = self.archive.m_create(Run)
        header = self.out_parser.header
        sec_run.program = Program(name='Octopus', version=str(header.get('Version', '')))
        sec_run.x_octopus_log_svn_revision = int(header.get('Revision', 0))

        self.parse_method()

        self.parse_system()

        self.parse_scc()

        sec_workflow = archive.m_create(Workflow)
        sec_workflow.type = 'geometry_optimization'
