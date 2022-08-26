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
from ast import Sub
import numpy as np            # pylint: disable=unused-import
import typing                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference, JSON
)
from nomad.datamodel.metainfo import simulation
from nomad.datamodel.metainfo import workflow


m_package = Package()


class BandEnergies(simulation.calculation.BandEnergies):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_energy_min = Quantity(
        type=np.dtype(np.float64),
        shape=['n_spin_channels', 'n_bands'],
        unit='joule',
        description='''
        ''')

    x_band_energy_max = Quantity(
        type=np.dtype(np.float64),
        shape=['n_spin_channels', 'n_bands'],
        unit='joule',
        description='''
        ''')

    x_band_occupancies = Quantity(
        type=np.dtype(np.float64),
        shape=['n_spin_channels', 'n_bands'],
        unit='joule',
        description='''
        ''')


class Energy(simulation.calculation.Energy):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_dispersion = SubSection(sub_section=simulation.calculation.EnergyEntry)

    x_band_fit_error_correction = SubSection(sub_section=simulation.calculation.EnergyEntry)

    x_band_v_atomic_def = SubSection(sub_section=simulation.calculation.EnergyEntry)

    x_band_v_def_def = SubSection(sub_section=simulation.calculation.EnergyEntry)


class Forces(simulation.calculation.Forces):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_p_matrix = SubSection(sub_section=simulation.calculation.ForcesEntry)

    x_band_electronic_kinetic = SubSection(sub_section=simulation.calculation.ForcesEntry)

    x_band_xc = SubSection(sub_section=simulation.calculation.ForcesEntry)

    x_band_electrostatic = SubSection(sub_section=simulation.calculation.ForcesEntry)

    x_band_pair_interactions = SubSection(sub_section=simulation.calculation.ForcesEntry)

    x_band_dispersion = SubSection(sub_section=simulation.calculation.ForcesEntry)

    x_band_nuclear_repulsion = SubSection(sub_section=simulation.calculation.ForcesEntry)


class GeometryOptimization(workflow.GeometryOptimization):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_optimization_coordinates = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_band_optimize_lattice = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_maximum_rms_gradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_maximum_rms_step_allowed = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_maximum_stress_energy_allowed = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_initial_model_hessian = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_band_hessian_update_method = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_band_first_gdiis_cycle = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_maximum_gdiis_vectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_trust_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ''')

    x_band_trust_radius_varies = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_constraints_converged_at_all_steps = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_symmetrize_steps = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_use_projector = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_dftb_resources_dir = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_band_scc_convergence_enabled = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_max_scc_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_scc_charge_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_scc_charge_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_diis_max_dimension = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_diis_max_coeff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_adaptive_scc_charge_mixing = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_adaptive_scc_mixing_strategy = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_spin_polarization = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_orbital_dependent_scc = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_orbital_fill_strategy = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_band_fermi_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_use_symmetry = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_radial_function_extrapolation_method = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_band_grimme_d3_dispersion_correction = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_band_other_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_band_assume_insulator = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_ewald_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_ewald_range_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_nuclear_charge_density_model = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_band_bzstruct_config = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_band_run_config = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')


class BasisSet(simulation.method.BasisSet):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_basis_functions_confinement_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_basis_functions_confinement_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')


class AtomParameters(simulation.method.AtomParameters):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_radial_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_nuclear_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_n_radial_core_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_orbital_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['n_orbitals'],
        unit='joule',
        description='''
        ''')

    x_band_orbital_radii = Quantity(
        type=np.dtype(np.float64),
        shape=['n_orbitals'],
        description='''
        ''')

    x_band_energy_sum_eigenvalues = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_band_energy_total_lda = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_band_energy_kinetic = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_band_energy_classical_electron_electron_repulsion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_band_energy_electron_nucleus_repulsion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_band_n_radial_valence_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_n_radial_core_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_n_radial_fit_functions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_cutoff_valence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_cutoff_core = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_cutoff_valence_kinetic = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_cutoff_core_kinetic = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')


class Scf(simulation.method.Scf):

    m_def = Section(validate=False, extends_base_section=True)

    x_band_diis_settings_dirac = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_band_diis_settings_scf = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_band_growth_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_shrink_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_mix = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_degenerate = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_band_edegen = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_scfrtx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_convrg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_band_ncyclx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_band_vsplit = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')
