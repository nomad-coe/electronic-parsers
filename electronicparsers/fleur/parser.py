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
import re

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import (
    Run, Program, TimeRun
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.method import (
    Method, BasisSet, DFT, XCFunctional, Functional, Electronic, Smearing
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, ScfIteration, Energy, EnergyEntry, Forces, ForcesEntry, BandEnergies
)
from .metainfo.fleur import x_fleur_header


re_n = r'[\n\r]'
re_f = r'[-+]?\d*\.\d*(?:[DdEe][-+]\d+)?'


def _eval(exp, variables=dict()):
    # TODO implementation can be improved
    operators = {
        '**': lambda x, y: x ** y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x + y
    }
    exp = exp.replace(' ', '')
    if not exp:
        return 0

    for key, operation in operators.items():
        if key not in exp:
            continue

        segments = exp.rsplit(key, 1)
        if len(segments) == 2:
            return operation(_eval(segments[0], variables), _eval(segments[1], variables))

    value = variables.get(exp)
    if value:
        return value

    try:
        return float(exp)
    except Exception as e:
        raise e


class XMLParser(TextParser):

    def init_quantities(self):
        re_bulk_lattice = re.compile(r'bulkLattice scale="(.+?)"(?: latnam="(.+?)")*')
        re_lattice_constant = re.compile(r'<(.+?) scale="(.+?)"\>(.+?)\<\/')
        re_lattice_vector = re.compile(rf'\<row\-(\d)\>(\S+ +\S+ +\S+)\<')

        def to_cell(val_in):
            bulk = re_bulk_lattice.findall(val_in)
            lattice_constant = re_lattice_constant.findall(val_in)

            if re_bulk_lattice:
                scale, lattice = bulk[0]
                if lattice == 'squ':
                    if not lattice_constant:
                        return
                    # TODO why is c specified for squ lattice
                    a = float(lattice_constant[0][1]) * float(lattice_constant[0][2])
                    return np.diag((a, a, a)) * float(scale) * ureg.bohr

                else:
                    lattice_vector = re_lattice_vector.findall(val_in)
                    if not lattice_vector:
                        return

                    cell = np.zeros((3, 3))
                    for vector in lattice_vector:
                        cell[int(vector[0]) - 1][:] = vector[1].split()
                    return cell * ureg.bohr

        self._quantities = [
            Quantity(
                'header',
                r'\<programVersion([\s\S]+?)\<\/programVersion\>',
                sub_parser=TextParser(quantities=[
                    Quantity('program_version', r'version=\"(fleur \S+)\"', dtype=str, flatten=False),
                    Quantity('x_fleur_precision', r'precision type=\"(\S+)\"', dtype=str),
                    Quantity('x_fleur_structure_class', r'\<targetStructureClass\>(.+?)\<', dtype=str),
                    Quantity('x_fleur_additional_flags', r'\<additionalCompilerFlags\>(.+?)\<', dtype=str)
                ])
            ),
            Quantity('start_time', r'date="(.+?)" time="(.+?)" zone="(.+?)"', flatten=False, dtype=str),
            Quantity(
                'input',
                r'\<inputData\>([\s\S]+?)\<\/inputData\>',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters', r'\<calculationSetup\>([\s\S]+?)\<\/calculationSetup\>',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'key_val', r' (\S+=)\"(.+?)\"',
                                str_operation=lambda x: x.split('='), repeats=True
                            )
                        ])
                    ),
                    Quantity(
                        'cell',
                        r'\<cell\>([\s\S]+?)\<\/cell\>',
                        str_operation=to_cell
                    ),
                    Quantity(
                        'xc_functional',
                        r'<xcFunctional name="(.+?)" relativisticCorrections="(.)"',
                        dtype=str
                    ),
                    Quantity(
                        'atom',
                        r'\<atomGroup([\s\S]+?)\<\/atomGroup\>', repeats=True,
                        # TODO parse more quantities
                        sub_parser=TextParser(quantities=[
                            Quantity('species', r'species="([A-Z][a-z]*)', dtype=str),
                            Quantity(
                                'position', r'\<relPos.*?\>(.+?)\<\/relPos\>',
                                str_operation=lambda x: [_eval(v) for v in x.strip().split()]
                            )
                        ])
                    ),
                    Quantity(
                        'output_parameters',
                        r'\<output([\s\S]+?)\<\/output\>',
                        sub_parser=TextParser(quantities=[
                            Quantity(
                                'key_val', r' (\S+=)\"(.+?)\"',
                                str_operation=lambda x: x.split('='), repeats=True
                            )
                        ])
                    )
                ])
            ),
            Quantity(
                'numerical_parameters',
                r'\<numericalParameters\>([\s\S]+?)\<\/numericalParameters\>',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'key_val', r' (\S+=)\"(.+?)\"',
                        str_operation=lambda x: x.split('='), repeats=True
                    )
                ])
            ),
            Quantity(
                'scf_iteration',
                r'\<iteration([\s\S]+?)\<\/iteration\>', repeats=True,
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_total',
                        rf'totalEnergy +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_sum_eigenvalues',
                        rf'sumOfEigenvalues +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_x_fleur_density_coulomb_potential',
                        rf'densityCoulombPotentialIntegral +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_x_fleur_density_effective_potential',
                        rf'densityEffectivePotentialIntegral +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_x_fleur_charge_density_xc',
                        rf'chargeDenXCDenIntegral +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_free',
                        rf'freeEnergy +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_total_t0',
                        rf'extrapolationTo0K +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'fermi',
                        rf'FermiEnergy +value=" *({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'eigenvalues_kpts',
                        r'\<eigenvaluesAt([\s\S]+?\<)\/eigenvaluesAt\>',
                        repeats=True, sub_parser=TextParser(quantities=[
                            Quantity(
                                'kpt',
                                rf'spin="1" ikpt="\d+" k_x="({re_f})" k_y="({re_f})" k_z="({re_f})"',
                                dtype=np.dtype(np.float64)
                            ),
                            Quantity('energies', rf'\>([\s\S]+?)\<', dtype=np.dtype(np.float64))
                        ])
                    )
                    # TODO parse other quantities
                ])
            )
        ]

    def get_xc_functional(self):
        xc_functional = self.get('input', {}).get('xc_functional')
        if xc_functional is not None:
            return f'{xc_functional[0]} {"non-" if xc_functional[1] == "F" else ""}relativistic correction'

    def get_system(self):
        input = self.input
        if not input:
            return None, None, None

        cell = input.cell
        atoms = input.get('atom', [])
        labels = [atom.species for atom in atoms]
        positions = np.dot([atom.position for atom in atoms], cell)
        return labels, positions, cell


class OutParser(TextParser):
    def init_quantities(self):
        def to_atoms(val_in):
            labels, positions = [], []
            for val in val_in.strip().splitlines():
                val = val.split()
                labels.append(val[1])
                positions.append(val[6:9])
            return labels, np.array(positions, dtype=np.float64) * ureg.bohr

        def to_key_val(val_in):
            val = val_in.strip().replace('D', 'E').split('=')
            key, val = val[0].strip(), val[1].split()
            return [key, val[0] if len(val) == 1 else val]

        key_val_quantity = Quantity(
            'key_val',
            r'([\w \-\/]+\s*=\s*[\d\.\-\+\w ]+)',
            str_operation=to_key_val, repeats=True)

        self._quantities = [
            Quantity(
                'header',
                r'(This output is generated[\s\S]+?Additional flags.+)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'program_version',
                        r'This output is generated by (fleur\S+)',
                        dtype=str
                    ),
                    Quantity('x_fleur_precision', r'(\S+) precision', dtype=str),
                    Quantity('x_fleur_with_inversion', r'(\S+) INVERSION', dtype=lambda x: x == 'with'),
                    Quantity('x_fleur_with_soc', r'(\S+) SOC', dtype=lambda x: x == 'with'),
                    Quantity(
                        'x_fleur_additional_flags',
                        r'Additional flags are: +(.+)',
                        str_operation=lambda x: x.strip(), dtype=str)
                ])
            ),
            Quantity(
                'input',
                r'(Your parameters\:[\s\S]+?fleur)',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'input_parameters',
                        r'dump of inp-file +\-+([\s\S]+?)Local',
                        sub_parser=TextParser(quantities=[key_val_quantity])
                    ),
                    Quantity(
                        'parameters',
                        r'(parameter *\([\s\S]+?)fleur',
                        sub_parser=TextParser(quantities=[key_val_quantity])
                    )
                ])
            ),
            Quantity(
                'system',
                r'([\w ]+\s+lattice=[\s\S]+?)input of',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'parameters',
                        rf'(lattice[\s\S]+?){re_n} *{re_n}',
                        sub_parser=TextParser(quantities=[key_val_quantity])
                    ),
                    Quantity(
                        'x_fleur_unit_cell_volume',
                        rf'the volume of the unit cell omega\-tilda= +({re_f})',
                        dtype=np.float64
                    ),
                    Quantity(
                        'x_fleur_unit_cell_volume_omega',
                        rf'the volume of the unit cell omega= +({re_f})',
                        dtype=np.float64
                    ),
                    Quantity('exchange_correlation', r'exchange\-correlation: (.+)', flatten=False, dtype=str),
                    Quantity('x_fleur_k_max', rf'k_max *= *({re_f})', dtype=np.float64),
                    Quantity('x_fleur_G_max', rf'G_max *= *({re_f})', dtype=np.float64),
                    Quantity('x_fleur_vol_interstitial', rf'volume of interstitial region= +({re_f})', dtype=np.float64),
                    Quantity('x_fleur_nr_of_atom_types', rf'number of atom types= +(\d+)', dtype=np.int32),
                    Quantity(
                        'cell',
                        r'bravais matrices of real and reciprocal lattices\s+'
                        # rf'((?:{re_f} +{re_f} +{re_f} +{re_f} +{re_f} +{re_f}\s+))',
                        rf'({re_f} +{re_f} +{re_f}) +{re_f} +{re_f} +{re_f}\s+'
                        rf'({re_f} +{re_f} +{re_f}) +{re_f} +{re_f} +{re_f}\s+'
                        rf'({re_f} +{re_f} +{re_f}) +{re_f} +{re_f} +{re_f}\s+',
                        dtype=np.dtype(np.float64), shape=(3, 3), unit=ureg.bohr
                    ),
                    Quantity(
                        'atoms',
                        r'no\. +type +int\.\-coord\. +cart\.coord\. +rmt +jri +dx +lmax\s+'
                        rf'((?:\d+ +[A-Z][a-z] +\d+.+\s+)+)',
                        str_operation=to_atoms
                    ),
                ])
            ),
            Quantity(
                'electronic',
                r'(parameters for eigenvalues[\s\S]+?)Local',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'eigenvalues_parameters',
                        rf'parameters for eigenvalues:([\s\S]+?){re_n} *{re_n}',
                        sub_parser=TextParser(quantities=[key_val_quantity])
                    ),
                    Quantity(
                        'smearing',
                        r'gauss\-integration is used += +(\S)',
                        str_operation=lambda x: 'gaussian' if x == 'T' else 'fermi'
                    ),
                    Quantity('width', rf'(?:width|broadening) += +({re_f})', dtype=np.float64),
                    Quantity(
                        'x_fleur_nr_of_valence_electrons',
                        rf'number of valence electrons= +({re_f})',
                        dtype=np.float64
                    )

                ])
            ),
            Quantity(
                'electic_field_parameters',
                rf'parameters for external electric field:([\s\S]+?){re_n} *{re_n}',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'x_fleur_tot_elec_charge',
                        rf'total electronic charge += +({re_f})',
                        dtype=np.float64
                    ),
                    Quantity(
                        'x_fleur_tot_nucl_charge',
                        rf'total nuclear charge += +({re_f})',
                        dtype=np.float64
                    ),
                ])
            ),
            Quantity(
                'scf_iteration',
                r'(it= +\d+[\s\S]+?it= +\d+ +is completed)',
                repeats=True, sub_parser=TextParser(quantities=[
                    Quantity(
                        'energy_sum_eigenvalues',
                        rf'sum of eigenvalues = +({re_f})', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_x_fleur_density_coulomb_potential',
                        rf'density\-coulomb potential int +({re_f}) htr', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_x_fleur_density_effective_potential',
                        rf'density-effective potential i +({re_f}) htr', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_x_fleur_charge_density_xc',
                        rf'charge density\-ex\.\-corr\.energ +({re_f}) htr', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_total',
                        rf'total energy= +({re_f}) htr', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_free',
                        rf'free energy= +({re_f}) htr', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'energy_total_t0',
                        rf'total electron energy= +({re_f}) htr', dtype=np.float64, unit=ureg.hartree
                    ),
                    Quantity(
                        'forces',
                        rf'FX_TOT= *({re_f}) FY_TOT= *({re_f}) FZ_TOT= *({re_f})',
                        repeats=True
                    ),
                    Quantity(
                        'kpoints',
                        rf'k=\( +({re_f} +{re_f} +{re_f})\):',
                        repeats=True, dtype=np.dtype(np.float64)
                    ),
                    Quantity(
                        'eigenvalues',
                        r'the *\d+ eigenvalues are:\s+([\s\d\.\-]+)',
                        repeats=True, dtype=np.dtype(np.float64)
                    ),
                    Quantity(
                        'fermi',
                        rf'new fermi energy +: +({re_f}) htr',
                        unit=ureg.hartree, dtype=np.float64
                    ),
                    Quantity(
                        'x_fleur_n_occupied_states',
                        r'number of occ\. states +: +(\d+)',
                        dtype=np.int32
                    ),
                    Quantity(
                        'x_fleur_valence_charge',
                        rf'valence charge +: +({re_f})',
                        dtype=np.float64
                    ),
                ])
            )
        ]

    def get_xc_functional(self):
        return self.get('system', {}).get('exchange_correlation')

    def get_system(self):
        system = self.get('system')
        if not system:
            return None, None, None

        atoms = system.get('atoms', [None, None])
        return atoms[0], atoms[1], system.cell


class FleurParser:
    def __init__(self):
        self._out_parser = OutParser()
        self._xml_parser = XMLParser()
        self._xc_map = {
            'pbe': ['GGA_X_PBE', 'GGA_C_PBE'],
            'rpbe': ['GGA_X_PBE', 'GGA_C_PBE'],
            'Rpbe': ['GGA_X_RPBE'],
            'pw91': ['GGA_X_PW91', 'GGA_C_PW91'],
            'l91': ['LDA_C_PW', 'LDA_C_PW_RPA', 'LDA_C_PW_MOD', 'LDA_C_OB_PW'],
            'vwn': ['LDA_C_VWN', 'LDA_C_VWN_1', 'LDA_C_VWN_2', 'LDA_C_VWN_3', 'LDA_C_VWN_4', 'LDA_C_VWN_RPA'],
            'bh': ['LDA_C_VBH'],
            'pz': ['LDA_C_PZ'],
            'x-a': [],
            'mjw': [],
            'wign': [],
            'hl': [],
            'xal': [],
            'relativistic': []
        }
        # TODO implement xml parser

    def init_parser(self):
        self.parser = self._xml_parser if self.filepath.endswith('.xml') else self._out_parser
        self.parser.mainfile = self.filepath
        self.parser.logger = self.logger

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.maindir = os.path.dirname(self.filepath)
        self.init_parser()

        header = self.parser.get('header', {})
        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name='fleur', version=header.get('program_version'))
        sec_header = sec_run.m_create(x_fleur_header)
        for key, val in header.items():
            if key.startswith('x_fleur'):
                setattr(sec_header, key, val)

        if self.parser.start_time:
            dt = datetime.strptime(self.parser.start_time, '%Y/%m/%d %H:%M:%S %z')
            sec_run.time_run = TimeRun(date_start=dt.timestamp())

        sec_method = sec_run.m_create(Method)
        sec_method.basis_set.append(BasisSet(type='(L)APW+lo'))
        input = self.parser.get('input')
        if input is not None:
            for key in ['parameters', 'input_parameters']:
                setattr(sec_method, f'x_fleur_{key}', {
                    key: list([float(v) for v in val]) if isinstance(
                        val, np.ndarray) else val for key, val in input.get(key, {}).get('key_val', [])})
        if not sec_method.x_fleur_parameters:
            sec_method.x_fleur_parameters = {}
        sec_method.x_fleur_parameters.update(input.get('output_parameters', {}))
        sec_method.x_fleur_parameters.update(self.parser.get('numerical_parameters', {}))

        electronic = self.parser.electronic
        if electronic is not None:
            sec_method.x_fleur_eigenvalues_parameters = {
                key: val for key, val in electronic.get('eigenvalues_parameters', {}).get('key_val')}
            sec_method.electronic = Electronic(smearing=Smearing(
                kind=electronic.smearing, width=electronic.width))

        exchange_correlation = self.parser.get_xc_functional()
        if exchange_correlation is not None:
            exchange_correlation = [xc.strip() for xc in exchange_correlation.strip().split(' ', 1)]
            sec_method.dft = DFT()
            sec_xc_functional = sec_method.dft.m_create(XCFunctional)
            for xc_functional in self._xc_map.get(exchange_correlation[0], []):
                if '_X_' in xc_functional or xc_functional.endswith('_X'):
                    sec_xc_functional.exchange.append(Functional(name=xc_functional))
                elif '_C_' in xc_functional or xc_functional.endswith('_C'):
                    sec_xc_functional.correlation.append(Functional(name=xc_functional))
                elif 'HYB' in xc_functional:
                    sec_xc_functional.hybrid.append(Functional(name=xc_functional))
                else:
                    sec_xc_functional.contributions.append(Functional(name=xc_functional))

            sec_xc_functional.x_fleur_xc_correction = exchange_correlation[1]

        electric_field = self.parser.electic_field_parameters
        if electric_field is not None:
            for key, val in electric_field.items():
                setattr(sec_method, key, val)

        labels, positions, lattice_vectors = self.parser.get_system()
        sec_system = sec_run.m_create(System)
        sec_system.x_fleur_parameters = dict()
        if labels is not None:
            sec_system.atoms = Atoms(
                lattice_vectors=lattice_vectors, labels=labels, positions=positions)

            system = self.parser.get('system', {})
            sec_system.x_fleur_parameters = {key: val for key, val in system.get('parameters', {}).get('key_val', [])}

            for key, val in system.items():
                if key.startswith('x_fleur'):
                    setattr(sec_system, key, val)

        sec_scc = sec_run.m_create(Calculation)
        sec_scc.system_ref = sec_system

        scf = None
        nspin = sec_method.x_fleur_parameters.get('jspins', sec_system.x_fleur_parameters.get('jspins', 1))
        for scf in self.parser.get('scf_iteration', []):
            sec_scf = sec_scc.m_create(ScfIteration)
            sec_scf_energy = sec_scf.m_create(Energy)
            sec_eigenvalues = sec_scf.m_create(BandEnergies)

            for key, val in scf.items():
                if val is None:
                    continue
                if key.startswith('energy_'):
                    setattr(sec_scf_energy, key.replace('energy_', ''), EnergyEntry(value=val))
                elif key == 'forces':
                    sec_scf.forces = Forces(total=ForcesEntry(value=val * ureg.hartree / ureg.bohr))
                elif key == 'fermi':
                    sec_scf_energy.fermi = val
                elif key == 'kpoints':
                    sec_eigenvalues.kpoints = val
                elif key == 'eigenvalues':
                    sec_eigenvalues.energies = np.reshape(val, (nspin, len(val) // nspin, len(val[0]))) * ureg.hartree
                elif key == 'eigenvalues_kpts':
                    sec_eigenvalues.kpoints = [v.kpt for v in val]
                    # it seems that it only shows the eigenvalues for spin 1
                    energies = [v.energies for v in val]
                    sec_eigenvalues.energies = np.reshape(energies, (1, len(energies), len(energies[0]))) * ureg.hartree
                elif key.startswith('x_fleur'):
                    setattr(sec_scf, key, val)

        if scf is not None:
            sec_scc.energy = sec_scf.energy
            sec_scc.forces = sec_scf.forces
            sec_scc.eigenvalues.append(sec_scf.eigenvalues[0])
