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
import os
import logging
import re
from scipy import optimize

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, DataTextParser
from nomad.datamodel import EntryArchive

from runschema.run import Run, Program
from runschema.system import System, Atoms
from runschema.method import (
    Method,
    HubbardKanamoriModel,
    FrequencyMesh,
    DMFT,
    AtomParameters,
)
from runschema.calculation import (
    Calculation,
    ScfIteration,
    Energy,
    EnergyEntry,
    Charges,
    GreensFunctions,
    Dos,
    DosValues,
)
from simulationworkflowschema import SinglePoint
from nomad.parsing.file_parser import DataTextParser
from .metainfo.edmft import x_edmft_method_parameters
from ..utils import get_files, BeyondDFTWorkflowsParser
from ..wien2k.parser import (
    StructParser,
)  # Wien2k is imported to parse the system information


class OutParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = []


class IndmflParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_orbitals_list(val_in):
            return val_in.replace("'", '').split(' ')[:-1]

        self._quantities = [
            Quantity(
                'hybridization_window',
                r'(\d+) *(\d+) *(\d+) *(\d+) *\# hybridization band index nemin and nemax\, renormalize for interstitials\, projection type',
            ),
            Quantity(
                'real_or_imaginary_axis',
                r'(\d+) *([\d\.]+) *([\d\.]+) *(\d+) *([\d\-\.]+) *([\d\-\.]+) *\# matsubara\, broadening\-corr\, broadening\-noncorr\, nomega\, omega\_min\, omega\_max \(in eV\)',
            ),
            Quantity('n_corr_atoms', r'(\d+)\s*\# number of correlated atoms'),
            Quantity(
                'i_atom_corr',
                r'(\d+)\s*(\d+)\s*(\d+)\s*\# iatom\, nL\, locrot',
                repeats=True,
            ),
            Quantity(
                'l_atom_corr',
                r'\s*(\d+)\s*(\d+)\s*(\d+)\s*\# L\, qsplit\, cix',
                repeats=True,
            ),
            Quantity(
                'siginds_corr',
                r'(\# Siginds and crystal\-field transformations for correlated orbitals \=*[\s\S]+)(?:\# Sigind follows)',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'indep_cix_blocks',
                            r'(\d+) *(\d+) *(\d+) *\# Number of independent kcix blocks\, max dimension\, max num\-independent-components',
                        ),
                        Quantity(
                            'cix',
                            r'(\d+) *(\d+) *(\d+) *\# cix\-num\, dimension\, num\-independent\-components',
                            repeats=True,
                        ),
                        Quantity(
                            'orbitals',
                            r'\# Independent components are \-*[\s\S]([\'\^\-\+a-zA-Z\s\d]+)',
                            str_operation=str_to_orbitals_list,
                        ),
                    ]
                ),
            ),
        ]


class ParamsParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'general_parameters',
                r'([\s\S]+)(?:\# Impurity problem number 0)',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'params',
                            r'([a-zA-Z\_]+)\s*\=\s*\'*([a-zA-Z\d\.\-]+)\'*',
                            repeats=True,
                        )
                    ]
                ),
            ),
            Quantity(
                'impurity_parameters',
                r'iparams0\=([\s\S]+)(?:\s*\})',
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            'params',
                            r'\s*\"(.+)\"\s*\:\s*\[[\"\'\s]*([a-zA-Z\d\.\-]+)[\"\'\s]*\,',
                            repeats=True,
                        )
                    ]
                ),
            ),
        ]


class ImpurityGfOutParser(DataTextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'parameters',
                r'\# *nf\=([\d\.]+) *mu\=([\d\.\-]+) *T\=([\d\.]+) *TrSigmaG\=([\d\.\-]+) *Epot\=([\d\.\-]+) *Ekin\=([\d\.\-]+) *mom\=([\[\]\,\d\.\-]+)',
                repeats=False,
            )
        ]


class MaxentParamsParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_multiply_to_float(val_in):
            val = val_in.split('*')
            return float(val[0]) * float(val[1])

        self._quantities = [
            Quantity(
                'parameters',
                r'\'([a-zA-Z\d\_]+)\' *\: *\ ([\d\.\*a-zA-Z]+)\'*\, *\#',
                repeats=True,
            ),
            Quantity(
                'smearing',
                r'\'gwidth\' *\: *([\d\*\.]+)\, *\#',
                str_operation=str_multiply_to_float,
            ),
        ]


class MaxEntSigOutParser(DataTextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        def str_to_array(val_in):
            val = [float(v) for v in val_in.split(', ')]
            return val

        self._quantities = [
            Quantity(
                'aux_sigma',
                r'\# *s\_oo\= *\[([\d\.\,\-\s]+)\]',
                repeats=False,
                str_operation=str_to_array,
            )
        ]


class EDMFTParser(BeyondDFTWorkflowsParser):
    """Parser for inputs / outputs of the eDMFT code. This parses generates (if the calculation
    files are present) 3 archives:
        1- `self.archive` -> the DMFT SinglePoint calculations. It contains DMFT methodology
        and GFs quantities in Matsubara frequencies.
        2- `maxent_archive` -> the analytically continuated, MaxEnt, SinglePoint calculation. It
        contains MaxEnt methodology and the self-energy in real space frequencies.
        3- `dmft_maxent_archive` -> combines both archives (DMFT and MaxEnt SinglePoints) into
        a workflow archive containing all the information. It also contains the Green's function
        in real space frequencies and the DOS. Useful to then use to define the DFT+DMFT
        workflow archive.
    """

    def __init__(self):
        self._re_namesafe = re.compile(r'[^\w]')
        self._calculation_type = 'dmft'
        self._child_archives = {}

        self.out_parser = OutParser()
        self.struct_parser = StructParser()
        self.indmfl_parser = IndmflParser()
        self.params_parser = ParamsParser()
        self.iterate_parser = DataTextParser()
        self.imp_gf_parser = ImpurityGfOutParser()
        self.lattice_parser = DataTextParser()

        self._solver_map = {'CTQMC': 'CT-HYB', 'OCA': 'OCA', 'NCA': 'NCA'}

        self._angular_momentum = ['s', 'p', 'd', 'f']

        self._gf_files_map = {
            'imp.0/Gf.out.*': 'greens_function_iw',
            'imp.0/Sig.out.*': 'self_energy_iw',
            'imp.0/Delta.inp.*': 'hybridization_function_iw',
        }

        self._gf_lattice = ['greens_function_iw', 'self_energy_iw']

        self._gf_lattice_maxent = [
            'greens_function_freq',
            'hybridization_function_freq',
        ]

        self.maxent_params_parser = MaxentParamsParser()
        self.maxent_sigout_parser = MaxEntSigOutParser()

    def parse_system(self, sec_run: Run):
        """Parses the system from the Wien2k *.struct file using Wien2k parsing class `StructParser`.

        Args:
            sec_run (Run): Specific Run section to be populated with System.
        """
        struct_files = get_files('*.struct', self.filepath, self.mainfile)
        if not struct_files:
            return
        if len(struct_files) > 1:
            self.logger.warning(
                'Multiple *struct files found; we will parse the last one.',
                data={'files': struct_files},
            )
        self.struct_parser.mainfile = struct_files[-1]
        atoms = self.struct_parser.get_atoms()
        if atoms is None:
            return

        sec_system = System()
        sec_run.system.append(sec_system)
        sec_atoms = Atoms()
        sec_system.atoms = sec_atoms
        sec_atoms.lattice_vectors = np.array(atoms.get_cell()) * ureg.angstrom
        sec_atoms.positions = atoms.get_positions() * ureg.angstrom
        sec_atoms.labels = atoms.get_chemical_symbols()
        sec_atoms.periodic = atoms.get_pbc()

    def parse_initial_model(self):
        """Parses the initial model for running DMFT SinglePoint. It is composed of the
        projection matrix plus the Hubbard-Kanamori parameters.
        """
        sec_run = self.archive.run[-1]
        sec_method = Method()
        sec_run.method.append(sec_method)

        # TODO ask @LucianPascut what projectorw.dat means to parse as initial model.

        # HubbardKanamori part
        for n in range(self.indmfl_parser.get('n_corr_atoms', 1)):
            sec_atom_params = AtomParameters()
            sec_method.atom_parameters.append(sec_atom_params)
            if sec_run.m_xpath('system[-1].atoms.labels'):
                labels = sec_run.system[-1].atoms.labels
                if self.indmfl_parser.get('i_atom_corr') is not None:
                    atom_corr = self.indmfl_parser.get('i_atom_corr')[n]
                    label = labels[atom_corr[0] - 1]
                    sec_atom_params.label = label
                if self.indmfl_parser.get('l_atom_corr') is not None:
                    angular_momentum = self._angular_momentum[
                        self.indmfl_parser.get('l_atom_corr')[n][0]
                    ]
                if self.indmfl_parser.get('siginds_corr', {}).get('cix') is not None:
                    n_orbitals = self.indmfl_parser.get('siginds_corr', {}).get('cix')[
                        n
                    ][-1]
                    sec_atom_params.n_orbitals = n_orbitals
                if (
                    self.indmfl_parser.get('siginds_corr', {}).get('orbitals')
                    is not None
                ):
                    sec_atom_params.orbitals = [
                        f'{angular_momentum}{orb}'
                        for orb in self.indmfl_parser.get('siginds_corr', {}).get(
                            'orbitals'
                        )
                    ]
            sec_hubbard_kanamori = HubbardKanamoriModel()
            sec_atom_params.hubbard_kanamori_model = sec_hubbard_kanamori
            sec_hubbard_kanamori.double_counting_correction = (
                self.general_parameters.get('DCs', '')
            )
            sec_hubbard_kanamori.u = self.impurity_parameters.get('U', 0.0) * ureg.eV
            sec_hubbard_kanamori.jh = self.impurity_parameters.get('J', 0.0) * ureg.eV
            if self.impurity_parameters.get('CoulombF', 'Full') == 'Ising':
                sec_hubbard_kanamori.j = 0.0
            else:
                sec_hubbard_kanamori.up = (
                    sec_hubbard_kanamori.u - 2 * sec_hubbard_kanamori.jh
                )
                sec_hubbard_kanamori.j = sec_hubbard_kanamori.jh

    def parse_method(self):
        """Parses DMFT SinglePoint method parameters."""
        sec_run = self.archive.run[-1]

        sec_method = Method()
        sec_run.method.append(sec_method)
        sec_method.starting_method_ref = sec_run.method[
            0
        ]  # ref to the Non- and InteractionHamiltonian

        # Code-specific parameters
        sec_edmft_params = x_edmft_method_parameters()
        sec_method.x_edmft_method = sec_edmft_params
        sec_edmft_params.x_edmft_general = self.general_parameters
        sec_edmft_params.x_edmft_impurity_solver = self.impurity_parameters

        # DMFT method
        sec_dmft = DMFT()
        sec_method.dmft = sec_dmft
        n_corr_atoms = self.indmfl_parser.get('n_corr_atoms', 1)
        sec_dmft.n_impurities = n_corr_atoms
        if self.indmfl_parser.get('siginds_corr', {}).get('cix'):
            n_orbitals = [
                orb[-1] for orb in self.indmfl_parser.get('siginds_corr', {}).get('cix')
            ]
            sec_dmft.n_correlated_orbitals = n_orbitals
        if self.impurity_parameters.get('nf0'):
            n_corr_elect = self.impurity_parameters.get('nf0', 1.0) / n_corr_atoms
            corr_elect = [
                n_corr_elect
            ] * n_corr_atoms  # TODO ask Lucian if this makes sense
            sec_dmft.n_electrons = corr_elect
        sec_dmft.inverse_temperature = (
            self.impurity_parameters.get('beta', 0.0) / ureg.eV
        )
        sec_dmft.magnetic_state = 'paramagnetic'  # TODO ask Lucian if this is correct
        sec_dmft.impurity_solver = self._solver_map.get(
            self.general_parameters.get('solver', '')
        )

    def extract_greens_functions_data(
        self,
        sec_scc: Calculation,
        sec_gfs: GreensFunctions,
        n_orbitals: np.int32,
        gf_data: np.ndarray,
        mesh_type: str,
        create_freq_mesh: bool = True,
    ):
        """Extracts GF data from gf_data as read from the data output files, and populates
        sec_gfs with it.

        Args:
            sec_scc (Calculation): Calculation section for updating the method_ref.
            sec_gfs (GreensFunctions): GreensFunctions section to be populated with gf_data
            n_orbitals (np.int32): Number of correlated orbitals.
            gf_data (np.ndarray): Data extracted from the data output files.
            mesh_type(str): Specifies if the FreqMesh is imaginary (Matsubara) or real frequencies.
            create_freq_mesh (bool, optional): Creates a FrequencyMesh section and the
                calculation.method_ref if true. Defaults to True.
        """
        # Adding FreqMesh
        if gf_data is None:
            return
        freq = gf_data[:, 0]
        if mesh_type == 'imaginary':
            sec_gfs.matsubara_freq = freq
            freq = freq * 1j
        elif mesh_type == 'real':
            sec_gfs.frequencies = freq

        if create_freq_mesh:
            freq = freq.reshape((len(freq), 1))
            sec_freq_mesh = FrequencyMesh(
                dimensionality=1, n_points=len(freq), points=freq * ureg.eV
            )
            try:
                method_ref = sec_scc.method_ref
                method_ref.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
            except Exception:
                pass

        # Defining the full Gf in the basis n_atoms x 2 x n_orbitals x n_freq
        gf_orb_data = np.array(
            [
                gf_data[:, 2 * n + 1] + gf_data[:, 2 * n + 2] * 1j
                for n in range(n_orbitals)
            ]
        )
        return np.array([[gf_orb_data, gf_orb_data]])

    def parse_scc(self):
        """Parses output calculation from a DMFT SinglePoint calculation. Each DMFT calculation
        step is composed of a scf convergence, as explained in the documentation workflow
        graphs: http://hauleweb.rutgers.edu/tutorials/Overview.html

        Each calculation section is then composed of:
            a) Iteration energy and charge quantities inside scf_iteration.
            b) Impurity GF quantities in Matsubara frequency space. The last
            calculation contains the last output quantities to be compared with the lattice GF
            quantities.
            c) The final calculation also contains the lattice GF quantities.
        """
        # TODO: (1) ask about extensions when more than one impurity: iparams0, iparams1,
        # info.iterate n_latt and n_imp columns? imp.X subfolders?
        # (2) how to check convergence (Gimp - Glatt < criteria)?
        sec_run = self.archive.run[-1]

        def create_calculation_section():
            """Creates a calculation section and includes system_ref and method_ref."""
            sec_scc = Calculation()
            sec_run.calculation.append(sec_scc)
            if sec_run.system is not None:
                sec_scc.system_ref = sec_run.system[-1]
            if sec_run.method is not None:
                sec_scc.method_ref = sec_run.method[-1]  # ref DMFT
            return sec_scc

        if sec_run.m_xpath('method[-1].dmft.n_correlated_orbitals') is not None:
            n_orbitals = sec_run.method[-1].dmft.n_correlated_orbitals[0]
        else:
            self.logger.warning(
                'Number of orbitals could not be extracted. We cannot parse '
                'the output calculation information.'
            )
            return

        # Parsing iteration steps for each of the calculation steps
        iterate_files = get_files('info.iterate', self.filepath, self.mainfile)
        if iterate_files:
            if len(iterate_files) > 1:
                self.logger.warning(
                    'Multiple info.iterate files found; we will parse the last one.',
                    data={'files': iterate_files},
                )
            self.iterate_parser.mainfile = iterate_files[-1]
            data_scf = (
                [] if self.iterate_parser.data is None else self.iterate_parser.data
            )
            calculations = sec_run.calculation
            for i_dmft, data in enumerate(data_scf):
                iter_dmft = np.int32(data[1])
                sec_scc = (
                    create_calculation_section()
                    if len(calculations) <= iter_dmft
                    else calculations[iter_dmft]
                )

                sec_scf_iteration = ScfIteration()
                sec_scc.scf_iteration.append(sec_scf_iteration)
                # Energies
                sec_energy = Energy()
                sec_scf_iteration.energy = sec_energy
                sec_energy.chemical_potential = data[3] * ureg.eV
                sec_energy.double_counting = EnergyEntry(value=data[4] * ureg.eV)
                sec_energy.total = EnergyEntry(value=data[5] * ureg.rydberg)
                sec_energy.free = EnergyEntry(value=data[7] * ureg.rydberg)
                # Lattice and impurity occupations
                sec_charges_latt = Charges()
                sec_scf_iteration.charges.append(sec_charges_latt)
                sec_charges_latt.kind = 'lattice'
                sec_charges_latt.n_atoms = sec_scc.method_ref.dmft.n_impurities
                sec_charges_latt.n_orbitals = n_orbitals
                sec_charges_latt.n_electrons = [data[8]]
                sec_charges_imp = Charges()
                sec_scf_iteration.charges.append(sec_charges_imp)
                sec_charges_imp.kind = 'impurity'
                sec_charges_imp.n_atoms = sec_scc.method_ref.dmft.n_impurities
                sec_charges_imp.n_orbitals = n_orbitals
                sec_charges_imp.n_electrons = [data[9]]

        # Impurity Green's function, self-energy, hybridization function parsing for each calculation step
        for imp_path in self._gf_files_map.keys():
            impurity_files = get_files(imp_path, self.filepath, self.mainfile)
            if impurity_files:
                impurity_files.sort()
                for i_scc, f in enumerate(impurity_files):
                    # Calculation and GreensFunction sections
                    if sec_run.calculation:
                        sec_scc = sec_run.calculation[i_scc]
                    else:
                        sec_scc = Calculation()
                        sec_run.calculation.append(sec_scc)
                    if sec_scc.greens_functions:
                        sec_gfs = sec_scc.greens_functions[-1]
                    else:
                        sec_gfs = GreensFunctions()
                        sec_scc.greens_functions.append(sec_gfs)
                        sec_gfs.type = 'impurity'
                    # Parsing data
                    self.imp_gf_parser.mainfile = f
                    imp_gf_data = self.imp_gf_parser.data
                    impurity_data = (
                        self.extract_greens_functions_data(
                            sec_scc, sec_gfs, n_orbitals, imp_gf_data, 'imaginary'
                        )
                        if imp_gf_data is not None
                        else None
                    )
                    if impurity_data is not None:
                        sec_gfs.m_set(
                            sec_gfs.m_get_quantity_definition(
                                self._gf_files_map[imp_path]
                            ),
                            impurity_data,
                        )
                    if self.imp_gf_parser.get('parameters'):
                        sec_gfs.chemical_potential = (
                            self.imp_gf_parser.get('parameters')[1] * ureg.eV
                        )

        # Parse lattice GFs quantities in the last calculation
        if sec_run.calculation is not None:
            sec_scc = sec_run.calculation[-1]
            lattice_gf_files = get_files('*.gc1', self.filepath, self.mainfile)
            lattice_sigma_files = get_files('sig.inp1', self.filepath, self.mainfile)
            for i_files, lattice_files in enumerate(
                [lattice_gf_files, lattice_sigma_files]
            ):
                if lattice_files:
                    if len(lattice_files) > 1:
                        self.logger.warning(
                            'Multiple lattice files (*.gc* or sig.inp1) found; we will parse the last one.',
                            data={'files': lattice_files},
                        )
                    self.lattice_parser.mainfile = lattice_files[-1]
                    sec_gfs = GreensFunctions()
                    sec_scc.greens_functions.append(sec_gfs)
                    sec_gfs.type = 'lattice'
                    lattice_data = self.lattice_parser.data
                    # Extracting Matsubara freqs and GF data without storing FrequencyMesh -> this
                    # is because impurity and lattice GFs can have different size in Matsubara frequencies.
                    extracted_lattice_data = (
                        self.extract_greens_functions_data(
                            sec_scc,
                            sec_gfs,
                            n_orbitals,
                            lattice_data,
                            'imaginary',
                            False,
                        )
                        if lattice_data is not None
                        else None
                    )
                    sec_gfs.m_set(
                        sec_gfs.m_get_quantity_definition(self._gf_lattice[i_files]),
                        extracted_lattice_data,
                    )

    def init_parser(self):
        self.out_parser.mainfile = self.mainfile
        self.out_parser.logger = self.logger
        self.struct_parser.mainfile = None
        self.struct_parser.logger = self.logger
        self.indmfl_parser.mainfile = None
        self.indmfl_parser.logger = self.logger
        self.params_parser.mainfile = None
        self.params_parser.logger = self.logger
        self.iterate_parser.mainfile = None
        self.iterate_parser.logger = self.logger
        self.imp_gf_parser.mainfile = None
        self.imp_gf_parser.logger = self.logger
        self.lattice_parser.mainfile = None
        self.lattice_parser.logger = self.logger
        self.maxent_params_parser.mainfile = None
        self.maxent_params_parser.logger = self.logger
        self.maxent_sigout_parser.mainfile = None
        self.maxent_sigout_parser.logger = self.logger

    def get_mainfile_keys(self, **kwargs):
        filepath = kwargs.get('filename')
        mainfile = os.path.basename(filepath)
        maxent_files = get_files('maxent_params.dat', filepath, mainfile)
        if maxent_files is not None:
            return ['MaxEnt', 'MaxEnt_workflow']
        return True

    def parse_maxent_archive(self, archive: EntryArchive):
        """Populates the MaxEnt SinglePoint archive. This will contain:
        1- The analytical continuation method parameters.
        2- The self-energy in real frequencies.
        """
        self.init_parser()
        sec_run = Run()
        archive.run.append(sec_run)
        sec_run.program = Program(name='eDMFT')

        def _freq_tan_points(x0: float, l0: float, n_w: int):
            """Defines the frequency mesh points in a 'Tan' mesh. Following script by @LucianPascut."""

            def opt_function(x: np.ndarray, x0: float, l0: float, n_w: int):
                d = x[0]
                w = x[1]
                return np.array(
                    [l0 - w / np.tan(d), x0 - w * np.tan(np.pi / (2 * n_w) - d / n_w)]
                )

            xi = x0 / l0
            d0 = (
                0.5
                * n_w
                * (
                    np.tan(np.pi / (2 * n_w))
                    - np.sqrt(np.tan(np.pi / (2 * n_w)) ** 2 - 4 * xi / n_w)
                )
            )
            w0 = l0 * d0

            sol = optimize.root(opt_function, [d0, w0], args=(x0, l0, n_w))
            (d, w) = sol.x
            return w * np.tan(
                np.linspace(0, 1, 2 * n_w + 1) * (np.pi - 2 * d) - np.pi / 2 + d
            )

        def parse_maxent_method():
            """Populates method section with MaxEnt parameters and the real space FrequencyMesh."""
            sec_method = Method()
            sec_run.method.append(sec_method)
            params = dict(self.maxent_params_parser.get('parameters'))
            sec_maxent_params = x_edmft_method_parameters()
            sec_method.x_edmft_method = sec_maxent_params
            sec_maxent_params.x_edmft_maxent = params
            sec_freq_mesh = FrequencyMesh(
                dimensionality=1, sampling_method='Tan', n_points=params.get('Nw', 1)
            )
            try:
                freqs = _freq_tan_points(
                    params.get('x0'), params.get('L'), params.get('Nw')
                )
                freqs = freqs.reshape((len(freqs), 1))
                sec_freq_mesh.points = freqs * ureg.eV
            except Exception:
                self.logger.warning('Real frequency mesh could not be extracted.')
            sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)

        def parse_maxent_scc():
            """Populates the calculation section with the analytically continuated self-energies
            in real space frequencies. This contains the info of the auxiliary function Sigma(infinity),
            which is also stored in the archive.
            """
            data = self.maxent_sigout_parser.data
            if data is None:
                return
            sec_scc = Calculation()
            sec_run.calculation.append(sec_scc)
            sec_scc.system_ref = sec_run.system[-1]
            sec_scc.method_ref = sec_run.method[-1]
            sec_gfs = GreensFunctions()
            sec_scc.greens_functions.append(sec_gfs)
            sec_gfs.frequencies = data[:, 0]
            try:
                n_orbitals = (
                    self.archive.run[-1].method[-1].dmft.n_correlated_orbitals[0]
                )  # getting them from DMFT SinglePoint
                sigout_orb_data = np.array(
                    [
                        data[:, 2 * n + 1] + data[:, 2 * n + 2] * 1j
                        for n in range(n_orbitals)
                    ]
                )
                sec_gfs.self_energy_freq = np.array(
                    [[sigout_orb_data, sigout_orb_data]]
                )
            except Exception:
                self.logger.warning(
                    'Could not extract self-energy in real frequencies data.'
                )
            aux_sigma = self.maxent_sigout_parser.get('aux_sigma', [])
            if aux_sigma is not None:
                sec_gfs.x_edmft_self_energy_infinity = aux_sigma

        # System
        self.parse_system(sec_run)

        # Method and MaxEnt calculation
        maxent_params_files = get_files(
            'maxent_params.dat', self.filepath, self.mainfile
        )
        if maxent_params_files:
            if len(maxent_params_files) > 1:
                self.logger.warning(
                    'Multiple maxent_params.dat files found; we will parse the last one.',
                    data={'files': maxent_params_files},
                )
            maxent_file = maxent_params_files[-1]
            self.maxent_params_parser.mainfile = maxent_file
            parse_maxent_method()
            sigout_files = get_files(
                'Sig.out', maxent_file, os.path.basename(maxent_file)
            )
            if sigout_files:
                if len(sigout_files) > 1:
                    self.logger.warning(
                        'Multiple Sig.out files found; we will parse the last one.',
                        data={'files': sigout_files},
                    )
                self.maxent_sigout_parser.mainfile = sigout_files[-1]
                parse_maxent_scc()

        # Workflow
        workflow = SinglePoint()
        workflow.name = 'MaxEnt Sigma'
        archive.workflow2 = workflow

    def parse_maxent_workflow(
        self, maxent_archive: EntryArchive, workflow_archive: EntryArchive
    ):
        """Populates the DMFT+MaxEnt workflow archive. This will contain:
        1- The Green's function in real frequencies and the Spectral density function (to be compared with the DOS).
        2- Tasks pointing to the DMFT SinglePoint and MaxEnt SinglePoint entries.
        """
        self.init_parser()
        sec_run = Run()
        workflow_archive.run.append(sec_run)
        sec_run.program = Program(name='eDMFT')

        def parse_gfs_real_freqs():
            sec_scc = Calculation()
            sec_run.calculation.append(sec_scc)
            if sec_run.system is not None:
                sec_scc.system_ref = sec_run.system[-1]
            maxent_indmfl_files = get_files('**/*.indmfl', self.filepath, self.mainfile)
            if not maxent_indmfl_files:
                return
            for file in maxent_indmfl_files:
                self.indmfl_parser.mainfile = file
                if self.indmfl_parser.get('real_or_imaginary_axis') is not None:
                    axis_flag = int(self.indmfl_parser.get('real_or_imaginary_axis')[0])
                    if axis_flag == 0:  # real frequencies flaghybridization_function
                        if not self.indmfl_parser.get('siginds_corr', {}).get('cix'):
                            self.logger.warning(
                                'Could not locate the number of correlated orbital in the impurity.'
                            )
                            return
                        n_orbitals = self.indmfl_parser.get('siginds_corr', {}).get(
                            'cix'
                        )[0][-1]
                        # Parsing Green's function and hybridization function
                        lattice_gf_files = get_files(
                            '*.gc1', file, os.path.basename(file)
                        )
                        lattice_delta_files = get_files(
                            '*.dlt1', file, os.path.basename(file)
                        )
                        for i_files, lattice_files in enumerate(
                            [lattice_gf_files, lattice_delta_files]
                        ):
                            if lattice_files:
                                if len(lattice_files) > 1:
                                    self.logger.warning(
                                        'Multiple lattice files (*.gc1 or *.dlt1) found; we will parse the last one.',
                                        data={'files': lattice_files},
                                    )
                                self.lattice_parser.mainfile = lattice_files[-1]
                                sec_gfs = GreensFunctions()
                                sec_scc.greens_functions.append(sec_gfs)
                                sec_gfs.type = 'lattice'
                                lattice_data = self.lattice_parser.data
                                extracted_lattice_data = (
                                    self.extract_greens_functions_data(
                                        sec_scc,
                                        sec_gfs,
                                        n_orbitals,
                                        lattice_data,
                                        'real',
                                        False,
                                    )
                                    if lattice_data is not None
                                    else None
                                )
                                sec_gfs.m_set(
                                    sec_gfs.m_get_quantity_definition(
                                        self._gf_lattice_maxent[i_files]
                                    ),
                                    extracted_lattice_data,
                                )
                                # Parsing DOS as - Im G / np.pi
                                if lattice_files == lattice_gf_files:
                                    sec_dos = Dos()
                                    sec_scc.dos_electronic.append(sec_dos)
                                    sec_dos.kind = 'spectral'
                                    sec_dos.energy_fermi = 0.0 * ureg.eV
                                    sec_dos.n_energies = len(lattice_data[:, 0])
                                    sec_dos.energies = lattice_data[:, 0] * ureg.eV
                                    sec_dos_values = DosValues()
                                    sec_dos.total.append(sec_dos_values)
                                    value = (
                                        -np.sum(extracted_lattice_data[0][0].imag, (0))
                                        / np.pi
                                    )
                                    sec_dos_values.value = value / ureg.eV

        # System
        self.parse_system(sec_run)

        # G(w) and DOS calculation
        parse_gfs_real_freqs()

        # Workflow
        self.parse_dmft_maxent_workflow(maxent_archive, workflow_archive)

    def parse(self, filepath: str, archive: EntryArchive, logger):
        self.filepath = filepath
        self.archive = archive
        self.maindir = os.path.dirname(self.filepath)
        self.mainfile = os.path.basename(self.filepath)
        self.logger = logging.getLogger(__name__) if logger is None else logger

        self.init_parser()

        params_files = get_files('*params.dat', self.filepath, self.mainfile)
        if params_files:
            if len(params_files) > 1:
                self.logger.warning(
                    f'Multiple *params.dat files found: we will parse the last one.',
                )
            self.params_parser.mainfile = params_files[-1]

            if self.params_parser.get('general_parameters'):
                self.general_parameters = dict(
                    self.params_parser.get('general_parameters').get('params', [])
                )
            if self.params_parser.get('impurity_parameters'):
                self.impurity_parameters = dict(
                    self.params_parser.get('impurity_parameters').get('params', [])
                )

        # Program section
        sec_run = Run()
        self.archive.run.append(sec_run)
        sec_run.program = Program(name='eDMFT')

        # System section
        self.parse_system(sec_run)

        # Method.DMFT section
        indmfl_files = get_files('*.indmfl', self.filepath, self.mainfile)
        if indmfl_files:
            if len(indmfl_files) > 1:
                self.logger.warning(
                    f'Multiple *.indmfl files found we will parse the last one.',
                )
            self.indmfl_parser.mainfile = indmfl_files[-1]
            if self.general_parameters and self.impurity_parameters:
                self.parse_initial_model()
                self.parse_method()

        # Calculation section
        self.parse_scc()

        # Workflow section
        workflow = SinglePoint()
        self.archive.workflow2 = workflow

        # DMFT+MaxEnt workflow
        maxent_archive = self._child_archives.get('MaxEnt')
        if maxent_archive:
            # Parse first the MaxEnt SinglePoint archive.
            # MaxEnt contains the analytical continuation of the imaginary axis Self-energy
            # into the real frequencies space.
            self.parse_maxent_archive(maxent_archive)

            # Then parse the DMFT with MaxEnt continuation workflow archive.
            # DMFT+MaxEnt contains the DMFT SinglePoint, the MaxEnt point, as well as the
            # calculation of the Green's function and DOS in the real frequency axis.
            dmft_maxent_archive = self._child_archives.get('MaxEnt_workflow')
            try:
                self.parse_maxent_workflow(maxent_archive, dmft_maxent_archive)
            except Exception:
                self.logger.error(
                    'Error parsing the automatic DMFT with MaxEnt continuation workflow.'
                )
