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
import numpy as np  # pylint: disable=unused-import
import typing  # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection,
    MCategory,
    Category,
    Package,
    Quantity,
    Section,
    SubSection,
    SectionProxy,
    Reference,
    JSON,
)
import runschema.run  # pylint: disable=unused-import
import runschema.calculation  # pylint: disable=unused-import
import runschema.method  # pylint: disable=unused-import
import runschema.system  # pylint: disable=unused-import
import simulationworkflowschema


m_package = Package()


class Program(runschema.run.Program):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_name = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_engine = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )


class BandEnergies(runschema.calculation.BandEnergies):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_energy_min = Quantity(
        type=np.float64,
        shape=['n_spin_channels', 'n_bands'],
        unit='joule',
        description="""
        """,
    )

    x_ams_energy_max = Quantity(
        type=np.float64,
        shape=['n_spin_channels', 'n_bands'],
        unit='joule',
        description="""
        """,
    )

    x_ams_occupations = Quantity(
        type=np.float64,
        shape=['n_spin_channels', 'n_bands'],
        unit='joule',
        description="""
        """,
    )


class Energy(runschema.calculation.Energy):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_dispersion = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_fit_error_correction = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_v_atomic_def = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_v_def_def = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_orthogonalization = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_orbital_interaction = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_orbital_interaction_a = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_orbital_interaction_efield = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_orbital_interaction_fit_correction = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_orbital_interaction_ts_correction_lda = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_orbital_interaction_ts_correction_nl = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_pauli_coulomb = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_pauli_efield = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_pauli_fit_correction = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_pauli_kinetic = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_pauli_kinetic_coulomb = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_pauli_ts_correction_lda = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_pauli = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_rpa = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_rpa = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_sum_fragments_scf_fit_correction = SubSection(
        sub_section=runschema.calculation.EnergyEntry
    )

    x_ams_bond = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_mp2 = SubSection(sub_section=runschema.calculation.EnergyEntry)

    x_ams_bond_efield = SubSection(sub_section=runschema.calculation.EnergyEntry)


class Forces(runschema.calculation.Forces):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_p_matrix = SubSection(sub_section=runschema.calculation.ForcesEntry)

    x_ams_electronic_kinetic = SubSection(sub_section=runschema.calculation.ForcesEntry)

    x_ams_electronic = SubSection(sub_section=runschema.calculation.ForcesEntry)

    x_ams_xc = SubSection(sub_section=runschema.calculation.ForcesEntry)

    x_ams_electrostatic = SubSection(sub_section=runschema.calculation.ForcesEntry)

    x_ams_pair_interactions = SubSection(sub_section=runschema.calculation.ForcesEntry)

    x_ams_dispersion = SubSection(sub_section=runschema.calculation.ForcesEntry)

    x_ams_nuclear_repulsion = SubSection(sub_section=runschema.calculation.ForcesEntry)


class GeometryOptimization(simulationworkflowschema.GeometryOptimization):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_optimization_coordinates = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_optimize_lattice = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_maximum_rms_gradient = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_maximum_rms_step_allowed = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_maximum_stress_energy_allowed = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_initial_model_hessian = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_hessian_update_method = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_first_gdiis_cycle = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_maximum_gdiis_vectors = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_trust_radius = Quantity(
        type=np.float64,
        shape=[],
        unit='bohr',
        description="""
        """,
    )

    x_ams_trust_radius_varies = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_constraints_converged_at_all_steps = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_symmetrize_steps = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_use_projector = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )


class Method(runschema.method.Method):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_dftb_resources_dir = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_scc_convergence_enabled = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_max_scc_cycles = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_scc_charge_convergence = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_scc_charge_mixing = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_diis_max_dimension = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_diis_max_coeff = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_adaptive_scc_charge_mixing = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_adaptive_scc_mixing_strategy = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_spin_polarization = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_orbital_dependent_scc = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_orbital_fill_strategy = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_fermi_temperature = Quantity(
        type=np.float64,
        unit='kelvin',
        shape=[],
        description="""
        """,
    )

    x_ams_use_symmetry = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_radial_function_extrapolation_method = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_grimme_d3_dispersion_correction = Quantity(
        type=JSON,
        shape=[],
        description="""
        """,
    )

    x_ams_other_parameters = Quantity(
        type=JSON,
        shape=[],
        description="""
        """,
    )

    x_ams_assume_insulator = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_ewald_tolerance = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_ewald_range_factor = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_nuclear_charge_density_model = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_ams_bzstruct_config = Quantity(
        type=JSON,
        shape=[],
        description="""
        """,
    )

    x_ams_run_config = Quantity(
        type=JSON,
        shape=[],
        description="""
        """,
    )


class BasisSetAtomCentered(runschema.method.BasisSetAtomCentered):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_basis_functions_confinement_radius = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_basis_functions_confinement_width = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )


class AtomParameters(runschema.method.AtomParameters):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_radial_points = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_nuclear_charge = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_n_radial_core_functions = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_orbital_energies = Quantity(
        type=np.float64,
        shape=['n_orbitals'],
        unit='joule',
        description="""
        """,
    )

    x_ams_orbital_radii = Quantity(
        type=np.float64,
        shape=['n_orbitals'],
        description="""
        """,
    )

    x_ams_energy_sum_eigenvalues = Quantity(
        type=np.float64,
        shape=[],
        unit='joule',
        description="""
        """,
    )

    x_ams_energy_total_lda = Quantity(
        type=np.float64,
        shape=[],
        unit='joule',
        description="""
        """,
    )

    x_ams_energy_kinetic = Quantity(
        type=np.float64,
        shape=[],
        unit='joule',
        description="""
        """,
    )

    x_ams_energy_classical_electron_electron_repulsion = Quantity(
        type=np.float64,
        shape=[],
        unit='joule',
        description="""
        """,
    )

    x_ams_energy_electron_nucleus_repulsion = Quantity(
        type=np.float64,
        shape=[],
        unit='joule',
        description="""
        """,
    )

    x_ams_n_radial_valence_orbitals = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_n_radial_core_orbitals = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_n_radial_fit_functions = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_cutoff_valence = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_cutoff_core = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_cutoff_valence_kinetic = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_cutoff_core_kinetic = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )


class BandGapDeprecated(runschema.calculation.BandGapDeprecated):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_n_valence_electrons = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_valence_band_index = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_valence_band_spin_index = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_conduction_band_index = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_conduction_band_spin_index = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )


class Scf(runschema.method.Scf):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_diis_settings_dirac = Quantity(
        type=JSON,
        shape=[],
        description="""
        """,
    )

    x_ams_diis_settings_scf = Quantity(
        type=JSON,
        shape=[],
        description="""
        """,
    )

    x_ams_growth_factor = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_shrink_factor = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_mix = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_degenerate = Quantity(
        type=bool,
        shape=[],
        description="""
        """,
    )

    x_ams_edegen = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_scfrtx = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_convrg = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_ncyclx = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_vsplit = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )


class KMesh(runschema.method.KMesh):
    m_def = Section(validate=False, extends_base_section=True)

    x_ams_general_integration_parameter = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_bz_volume_total = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_bz_volume_irreducible = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_bz_volume_numerical_integration = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_ams_n_points_unique = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_n_simplices = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_ams_n_points_per_simplex = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )
