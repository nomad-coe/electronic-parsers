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
import numpy as np
import logging

from nomad.units import ureg
from nomad.datamodel import EntryArchive
from nomad.parsing.file_parser import TextParser, Quantity
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Functional,
    Method,
    DFT,
    XCFunctional,
    BasisSetContainer,
    BasisSet,
    KMesh,
)
from nomad.datamodel.metainfo.simulation.system import System, Atoms
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation,
    SpinSpinCoupling,
    ElectricFieldGradient,
    MagneticShielding,
    MagneticSusceptibility,
)

# For the automatic workflow NMR
from nomad.search import search
from nomad.app.v1.models import MetadataRequired
from ..utils import BeyondDFTWorkflowsParser


re_float = r" *[-+]?\d+\.\d*(?:[Ee][-+]\d+)? *"


class MagresFileParser(TextParser):
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._quantities = [
            Quantity("lattice_units", r"units *lattice *([a-zA-Z]+)"),
            Quantity("atom_units", r"units *atom *([a-zA-Z]+)"),
            Quantity("ms_units", r"units *ms *([a-zA-Z]+)"),
            Quantity("efg_units", r"units *efg *([a-zA-Z]+)"),
            Quantity("efg_local_units", r"units *efg_local *([a-zA-Z]+)"),
            Quantity("efg_nonlocal_units", r"units *efg_nonlocal *([a-zA-Z]+)"),
            Quantity("isc_units", r"units *isc *([a-zA-Z\^\d\.\-]+)"),
            Quantity("isc_fc_units", r"units *isc_fc *([a-zA-Z\^\d\.\-]+)"),
            Quantity("isc_spin_units", r"units *isc_spin *([a-zA-Z\^\d\.\-]+)"),
            Quantity(
                "isc_orbital_p_units", r"units *isc_orbital_p *([a-zA-Z\^\d\.\-]+)"
            ),
            Quantity(
                "isc_orbital_d_units", r"units *isc_orbital_d *([a-zA-Z\^\d\.\-]+)"
            ),
            Quantity("sus_units", r"units *sus *([a-zA-Z\^\d\.\-]+)"),
            Quantity("cutoffenergy_units", rf"units *calc\_cutoffenergy *([a-zA-Z]+)"),
            Quantity(
                "calculation",
                r"([\[\<]*calculation[\>\]]*[\s\S]+?)(?:[\[\<]*\/calculation[\>\]]*)",
                sub_parser=TextParser(
                    quantities=[
                        Quantity("code", r"calc\_code *([a-zA-Z]+)"),
                        Quantity(
                            "code_version", r"calc\_code\_version *([a-zA-Z\d\.]+)"
                        ),
                        Quantity(
                            "code_hgversion",
                            r"calc\_code\_hgversion ([a-zA-Z\d\:\+\s]*)\n",
                            flatten=False,
                        ),
                        Quantity(
                            "code_platform", r"calc\_code\_platform *([a-zA-Z\d\_]+)"
                        ),
                        Quantity("name", r"calc\_name *([\w]+)"),
                        Quantity("comment", r"calc\_comment *([\w]+)"),
                        Quantity("xcfunctional", r"calc\_xcfunctional *([\w]+)"),
                        Quantity(
                            "cutoffenergy",
                            rf"calc\_cutoffenergy({re_float})(?P<__unit>\w+)",
                        ),
                        Quantity(
                            "pspot",
                            r"calc\_pspot *([\w]+) *([\w\.\|\(\)\=\:]+)",
                            repeats=True,
                        ),
                        Quantity(
                            "kpoint_mp_grid",
                            r"calc\_kpoint\_mp\_grid *([\w]+) *([\w]+) *([\w]+)",
                        ),
                        Quantity(
                            "kpoint_mp_offset",
                            rf"calc\_kpoint\_mp\_offset({re_float*3})$",
                        ),
                    ]
                ),
            ),
            Quantity(
                "atoms",
                r"([\[\<]*atoms[\>\]]*[\s\S]+?)(?:[\[\<]*\/atoms[\>\]]*)",
                sub_parser=TextParser(
                    quantities=[
                        Quantity("lattice", rf"lattice({re_float*9})"),
                        Quantity("symmetry", r"symmetry *([\w\-\+\,]+)", repeats=True),
                        Quantity(
                            "atom",
                            rf"atom *([a-zA-Z]+) *[a-zA-Z\d]* *([\d]+) *({re_float*3})",
                            repeats=True,
                        ),
                    ]
                ),
            ),
            Quantity(
                "magres",
                r"([\[\<]*magres[\>\]]*[\s\S]+?)(?:[\[\<]*\/magres[\>\]]*)",
                sub_parser=TextParser(
                    quantities=[
                        Quantity(
                            "ms", rf"ms *(\w+) *(\d+)({re_float*9})", repeats=True
                        ),
                        Quantity(
                            "efg", rf"efg *(\w+) *(\d+)({re_float*9})", repeats=True
                        ),
                        Quantity(
                            "efg_local",
                            rf"efg_local *(\w+) *(\d+)({re_float*9})",
                            repeats=True,
                        ),
                        Quantity(
                            "efg_nonlocal",
                            rf"efg_nonlocal *(\w+) *(\d+)({re_float*9})",
                            repeats=True,
                        ),
                        Quantity(
                            "isc",
                            rf"isc *(\w+) *(\d+) *(\w+) *(\d+)({re_float*9})",
                            repeats=True,
                        ),
                        Quantity(
                            "isc_fc",
                            rf"isc_fc *(\w+) *(\d+) *(\w+) *(\d+)({re_float*9})",
                            repeats=True,
                        ),
                        Quantity(
                            "isc_orbital_p",
                            rf"isc_orbital_p *(\w+) *(\d+) *(\w+) *(\d+)({re_float*9})",
                            repeats=True,
                        ),
                        Quantity(
                            "isc_orbital_d",
                            rf"isc_orbital_d *(\w+) *(\d+) *(\w+) *(\d+)({re_float*9})",
                            repeats=True,
                        ),
                        Quantity(
                            "isc_spin",
                            rf"isc_spin *(\w+) *(\d+) *(\w+) *(\d+)({re_float*9})",
                            repeats=True,
                        ),
                        Quantity("sus", rf"sus *({re_float*9})", repeats=True),
                    ]
                ),
            ),
        ]


class MagresParser(BeyondDFTWorkflowsParser):
    level = 1

    def __init__(self):
        self.magres_file_parser = MagresFileParser()

        self._xc_functional_map = {
            "LDA": ["LDA_C_PZ", "LDA_X_PZ"],
            "PW91": ["GGA_C_PW91", "GGA_X_PW91"],
            "PBE": ["GGA_C_PBE", "GGA_X_PBE"],
            "RPBE": ["GGA_X_RPBE"],
            "WC": ["GGA_C_PBE_GGA_X_WC"],
            "PBESOL": ["GGA_X_RPBE"],
            "BLYP": ["GGA_C_LYP", "LDA_X_B88"],
            "B3LYP": ["HYB_GGA_XC_B3LYP5"],
            "HF": ["HF_X"],
            "HF-LDA": ["HF_X_LDA_C_PW"],
            "PBE0": ["HYB_GGA_XC_PBEH"],
            "HSE03": ["HYB_GGA_XC_HSE03"],
            "HSE06": ["HYB_GGA_XC_HSE06"],
            "RSCAN": ["MGGA_X_RSCAN", "MGGA_C_RSCAN"],
        }

    def init_parser(self):
        self.magres_file_parser.mainfile = self.filepath
        self.magres_file_parser.logger = self.logger

    def _check_units_magres(self):
        allowed_units = {
            "lattice": "Angstrom",
            "atom": "Angstrom",
            "ms": "ppm",
            "efg": "au",
            "efg_local": "au",
            "efg_nonlocal": "au",
            "isc": "10^19.T^2.J^-1",
            "isc_fc": "10^19.T^2.J^-1",
            "isc_orbital_p": "10^19.T^2.J^-1",
            "isc_orbital_d": "10^19.T^2.J^-1",
            "isc_spin": "10^19.T^2.J^-1",
            "sus": "10^-6.cm^3.mol^-1",
        }
        for key, value in allowed_units.items():
            data = self.magres_file_parser.get(f"{key}_units", "")
            if data and data != value:
                self.logger.warning(
                    f"The units of {key} are not parsed if they are {data}. "
                    f"We will use the default units, {value}."
                )

    def parse_system(self):
        sec_run = self.archive.run[-1]
        sec_atoms = sec_run.m_create(System).m_create(Atoms)

        # Check if [atoms][/atoms] was correctly parsed
        atoms = self.magres_file_parser.get("atoms")
        if not atoms:
            self.logger.warning("Could not find atomic structure in magres file.")
            return

        # Store lattice_vectors and periodic boundary conditions
        lattice_vectors = np.reshape(np.array(atoms.get("lattice", [])), (3, 3))
        sec_atoms.lattice_vectors = lattice_vectors * ureg.angstrom
        pbc = (
            [True, True, True] if lattice_vectors is not None else [False, False, False]
        )
        sec_atoms.periodic = pbc

        # Storing atom positions and labels
        atoms_list = atoms.get("atom", [])
        if len(atoms_list) == 0:
            self.logger.warning(
                "Could not find atom positions and labels in magres file."
            )
            return
        atom_labels = []
        atom_positions = []
        for atom in atoms_list:
            atom_labels.append(atom[0])
            atom_positions.append(atom[2:])
        sec_atoms.labels = atom_labels
        sec_atoms.positions = atom_positions * ureg.angstrom

    def parse_method(self, calculation_params):
        # Only CASTEP-like method parameters is being supported.
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        sec_method.label = "NMR"
        sec_dft = sec_method.m_create(DFT)

        # XC functional parsing
        xc_functional = calculation_params.get("xcfunctional", "LDA")
        xc_functional_labels = self._xc_functional_map.get(xc_functional)
        if xc_functional_labels:
            sec_xc_functional = sec_dft.m_create(XCFunctional)
            for functional in xc_functional_labels:
                sec_functional = Functional(name=functional)
                if "_X_" in functional or functional.endswith("_X"):
                    sec_xc_functional.m_add_sub_section(
                        XCFunctional.exchange, sec_functional
                    )
                elif "_C_" in functional or functional.endswith("_C"):
                    sec_xc_functional.m_add_sub_section(
                        XCFunctional.correlation, sec_functional
                    )
                elif "HYB" in functional:
                    sec_xc_functional.m_add_sub_section(
                        XCFunctional.hybrid, sec_functional
                    )
                else:
                    sec_xc_functional.m_add_sub_section(
                        XCFunctional.contributions, sec_functional
                    )

        # Basis set parsing (adding cutoff energies units check)
        cutoff = calculation_params.get("cutoffenergy")
        if cutoff.dimensionless:
            cutoff_units = self.magres_file_parser.get("cutoffenergy_units", "eV")
            if cutoff_units == "Hartree":
                cutoff_units = "hartree"
            cutoff = cutoff.magnitude * ureg(cutoff_units)
        sec_basis_set = BasisSetContainer(
            type="plane waves",
            scope=["wavefunction"],
            basis_set=[BasisSet(scope=["valence"], type="plane waves", cutoff=cutoff)],
        )
        sec_method.m_add_sub_section(Method.electrons_representation, sec_basis_set)

        # KMesh parsing
        sec_k_mesh = KMesh(
            grid=calculation_params.get("kpoint_mp_grid", [1, 1, 1]),
            offset=calculation_params.get("kpoint_mp_offset", [0, 0, 0]),
        )
        sec_method.m_add_sub_section(Method.k_mesh, sec_k_mesh)

    def parse_calculation(self):
        sec_run = self.archive.run[-1]

        # Check if [magres][/magres] was correctly parsed
        magres_data = self.magres_file_parser.get("magres")
        if not magres_data:
            self.logger.warning("Could not find [magres] data block in magres file.")
            return

        # Creating Calculation and adding System and Method refs
        sec_scc = sec_run.m_create(Calculation)
        sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]
        atoms = sec_scc.system_ref.atoms.labels
        if not atoms:
            self.logger.warning("Could not find the parsed atomic cell information.")
            return
        n_atoms = len(atoms)

        # Magnetic Shielding Tensor (ms) parsing
        data = magres_data.get("ms", [])
        if len(data) > 0:
            values = np.reshape([d[2:] for d in data], (n_atoms, 3, 3))
            isotropic_value = np.trace(values, axis1=1, axis2=2) / 3.0
            sec_ms = sec_scc.m_create(MagneticShielding)
            sec_ms.value = values * 1e-6 * ureg("dimensionless")
            sec_ms.isotropic_value = isotropic_value * 1e-6 * ureg("dimensionless")

        # Electric Field Gradient (efg) parsing
        efg_contributions = {
            "efg_local": "local",
            "efg_nonlocal": "non_local",
            "efg": "total",
        }
        for tag, contribution in efg_contributions.items():
            data = magres_data.get(tag, [])
            if len(data) == 0:
                continue
            values = np.reshape([d[2:] for d in data], (n_atoms, 3, 3))
            sec_efg = sec_scc.m_create(ElectricFieldGradient)
            sec_efg.contribution = contribution
            sec_efg.value = values * 9.717362e21 * ureg("V/m^2")

        # Indirect Spin-Spin Coupling (isc) parsing
        isc_contributions = {
            "isc_fc": "fermi_contact",
            "isc_orbital_p": "orbital_paramagnetic",
            "isc_orbital_d": "orbital_diamagnetic",
            "isc_spin": "spin_dipolar",
            "isc": "total",
        }
        for tag, contribution in isc_contributions.items():
            # TODO the data is organized weirdly in the file, we need to transform it properly
            data = magres_data.get(tag, [])
            if len(data) == 0:
                continue
            # values = np.array(data)
            # sec_isc = sec_scc.m_create(SpinSpinCoupling)
            # sec_isc.contribution = contribution
            # sec_isc.reduced_value = values * 1e19 * ureg('K^2/J')

            # atom_indices = np.array(magres_data.get(f'isc{contribution}', []))[:, :4]
            # values = np.array(magres_data.get(f'isc{contribution}', []))[:, 4:]

        # Magnetic Susceptibility (sus) parsing
        data = magres_data.get("sus", [])
        if len(data) > 0:
            values = np.reshape(data, (3, 3))
            sec_sus = sec_scc.m_create(MagneticSusceptibility)
            sec_sus.scale_dimension = "macroscopic"
            sec_sus.value = values * 1e-6 * ureg("dimensionless")

    def parse(self, filepath, archive, logger):
        self.filepath = os.path.abspath(filepath)
        self.archive = archive
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        self.init_parser()
        self._check_units_magres()

        sec_run = self.archive.m_create(Run)
        calculation_params = self.magres_file_parser.get("calculation")
        program_name = calculation_params.get("code", "")
        if program_name != "CASTEP":
            self.logger.error(
                "Only CASTEP-based NMR simulations are supported by the "
                "magres parser."
            )
            return
        sec_run.program = Program(
            name=program_name,
            version=calculation_params.get("code_version", ""),
        )

        self.parse_system()

        self.parse_method(calculation_params)

        self.parse_calculation()

        # Checking if other mainfiles are present, if the closest is a CASTEP, tries to
        # link it with the corresponding magres entry
        filepath_stripped = self.filepath.split("raw/")[-1]
        try:
            upload_id = self.archive.metadata.upload_id
            search_ids = search(
                owner="visible",
                user_id=self.archive.metadata.main_author.user_id,
                query={"upload_id": upload_id},
                required=MetadataRequired(include=["entry_id", "mainfile"]),
            ).data
            metadata = [[sid["entry_id"], sid["mainfile"]] for sid in search_ids]
            if len(metadata) > 1:
                for entry_id, mainfile in metadata:
                    if (
                        mainfile == filepath_stripped
                    ):  # we skipped the current parsed mainfile
                        continue
                    entry_archive = archive.m_context.load_archive(
                        entry_id, upload_id, None
                    )
                    method_label = entry_archive.run[-1].method[-1].label
                    if method_label == "NMR":
                        castep_archive = entry_archive
                        # We write the workflow NMRMagRes directly in the magres entry
                        self.parse_nmr_magres_file_format(castep_archive)
                        break
        except Exception:
            self.logger.warning(
                "Could not resolve the automatic workflow for magres "
                "when trying to link with the CASTEP NMR entry. "
                "You can try reorganizing the data in the folders: "
                "CASTEP NMR files in the top-most folder and magres "
                "file in the same folder or one folder below CASTEP."
            )
