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
import numpy as np            # pylint: disable=unused-import
import typing                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference
)
from nomad.datamodel.metainfo import simulation
from nomad.datamodel.metainfo import workflow


m_package = Package()


class x_turbomole_section_eigenvalues_GW(MSection):
    '''
    section for the eigenvalues of a GW calculation (at present only pertubative G0W0)
    '''

    m_def = Section(validate=False)

    x_turbomole_eigenvalue_correlation_perturbativeGW = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Correlation energy at a given eigenstate from perturbative GW
        ''')

    x_turbomole_eigenvalue_ExactExchange_perturbativeGW = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Exact exchange energy at given eigenstate from perturbative GW
        ''')

    x_turbomole_eigenvalue_ExchangeCorrelation_perturbativeGW = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Self-energy at a given eigenstate from perturbative GW
        ''')

    x_turbomole_eigenvalue_ks_ExchangeCorrelation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        KS exchange correlation energy at a given eigenstate needed to calculate the
        quasi-particle energy in perturbative GW
        ''')

    x_turbomole_eigenvalue_ks_GroundState = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        KS ground state energy at a given eigenstate needed in perturbative GW
        ''')

    x_turbomole_eigenvalue_quasiParticle_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Quasiparticle energy at a given eigenstate from perturbative GW
        ''')

    x_turbomole_ExchangeCorrelation_perturbativeGW_derivation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TODO:
        ''')

    x_turbomole_Z_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TODO:
        ''')


class x_turbomole_section_functionals(MSection):
    '''
    section for one list of XC functionals
    '''

    m_def = Section(validate=False)

    x_turbomole_controlInOut_grid_integration_cells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The integration cells
        ''')

    x_turbomole_controlInOut_grid_integration = Quantity(
        type=str,
        shape=[],
        description='''
        type of the used grid integration
        ''')

    x_turbomole_controlInOut_grid_partition_func = Quantity(
        type=str,
        shape=[],
        description='''
        Type of the partition function used
        ''')

    x_turbomole_controlInOut_grid_partition_sharpness = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Sharpness of the partition function
        ''')

    x_turbomole_controlInOut_grid_points_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Grid points number
        ''')

    x_turbomole_controlInOut_grid_radial_grid_size = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The size of the radial grid
        ''')

    x_turbomole_controlInOut_grid_radial_integration = Quantity(
        type=str,
        shape=[],
        description='''
        The radial integration type
        ''')

    x_turbomole_controlInOut_grid_size = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The size of the used grid
        ''')

    x_turbomole_XC_functional_type = Quantity(
        type=str,
        shape=[],
        description='''
        XC functional type
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_turbomole_controlIn_atom_label = Quantity(
        type=str,
        shape=[],
        description='''
        The label of the atoms in the system
        ''')

    x_turbomole_controlIn_atom_number = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The number of atoms in the system
        ''')

    x_turbomole_controlIn_basis_status = Quantity(
        type=str,
        shape=[],
        description='''
        Status mean here ON or OFF
        ''')

    x_turbomole_controlIn_cartesian_status = Quantity(
        type=str,
        shape=[],
        description='''
        Status mean here ON or OFF
        ''')

    x_turbomole_controlIn_damping_parameter_min = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_damping_parameter_start = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_damping_parameter_step = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_dipole_status = Quantity(
        type=str,
        shape=[],
        description='''
        Status mean here ON or OFF
        ''')

    x_turbomole_controlIn_global_status = Quantity(
        type=str,
        shape=[],
        description='''
        Status mean here ON or OFF
        ''')

    x_turbomole_controlIn_hessian_status = Quantity(
        type=str,
        shape=[],
        description='''
        Status mean here ON or OFF
        ''')

    x_turbomole_controlIn_interconversion_status = Quantity(
        type=str,
        shape=[],
        description='''
        Status mean here ON or OFF
        ''')

    x_turbomole_controlIn_number_of_integral_stored = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_operating_system = Quantity(
        type=str,
        shape=[],
        description='''
        The kind of operating system
        ''')

    x_turbomole_controlIn_pople_kind = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_scf_conv = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_scf_iter_limit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_scfintunit_file = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_scfintunit_size = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_scfintunit_unit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_controlIn_symmetry = Quantity(
        type=str,
        shape=[],
        description='''
        The given symmetry of the system
        ''')

    x_turbomole_controlIn_time_for_integral_calc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        -
        ''')

    x_turbomole_dft_d3_version = Quantity(
        type=str,
        shape=[],
        description='''
        version of the DFT-D3 van-der-Waals correction that is used
        ''')

    x_turbomole_functional_type_correlation = Quantity(
        type=str,
        shape=[],
        description='''
        type of the used correlation functional
        ''')

    x_turbomole_functional_type_exchange = Quantity(
        type=str,
        shape=[],
        description='''
        type of the used exchange functional
        ''')

    x_turbomole_geometry_optimization_cycle_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        By default Turbomole only keeps the output of the final iteration once the
        geometry has been converged, thus the entire optimization trajectory cannot be
        rebuild in most cases. Instead, this value contains the optimization cycle index
        to indicate how many iterations have preceded this one.
        ''')

    x_turbomole_gw_approximation = Quantity(
        type=str,
        shape=[],
        description='''
        The employed GW approximation.
        ''')

    x_turbomole_gw_eta_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        [TO BE VERIFIED]Infinitesimal complex energy shift. Negative value switches to
        calculating at that value but extrapolating to 0 in linear approximation.
        ''')

    x_turbomole_gw_use_rpa_response = Quantity(
        type=bool,
        shape=[],
        description='''
        If true, the pure RPA response function is calculated. Otherwise, the TDDFT
        response function is calculated and used to screen the coulomb interaction.
        ''')

    x_turbomole_uhfmo_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of UHF molecular orbital
        ''')

    x_turbomole_section_functionals = SubSection(
        sub_section=SectionProxy('x_turbomole_section_functionals'),
        repeats=True)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_turbomole_damping_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Damping of the two-electron contributions to Fock matrix in the present SCF
        iteration
        ''')

    x_turbomole_delta_eigenvalues = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        change of the eigenvalues in the current SCF iteration
        ''')

    x_turbomole_energy_1electron_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Total energy contribution from one-electron integrals
        ''')

    x_turbomole_energy_2electron_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Total energy contribution from two-electron integrals
        ''')

    x_turbomole_norm_diis_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Norm of the DIIS error in an SCF-iteration
        ''')

    x_turbomole_norm_fia_orbital_scf_iteration = Quantity(
        type=str,
        shape=[],
        description='''
        orbital with the largest residual norm for the Fia block in this iteration
        ''')

    x_turbomole_norm_fia_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Maximal resid. norm for Fia-block in an SCF-iteration
        ''')

    x_turbomole_norm_fock_orbital_scf_iteration = Quantity(
        type=str,
        shape=[],
        description='''
        orbital with the largest residual Fock norm in this iteration
        ''')

    x_turbomole_norm_fock_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Maximal resid. fock norm in an SCF-iteration
        ''')


class BandEnergies(simulation.calculation.BandEnergies):

    m_def = Section(validate=False, extends_base_section=True)

    x_turbomole_eigenvalues_irreducible_representation = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_spin_channels', 'number_of_eigenvalues_kpoints', 'number_of_eigenvalues'],
        description='''
        Irreducible representation the eigenstates belong to.
        ''')

    x_turbomole_section_eigenvalues_GW = SubSection(
        sub_section=SectionProxy('x_turbomole_section_eigenvalues_GW'),
        repeats=True)


class GeometryOptimization(workflow.GeometryOptimization):

    m_def = Section(validate=False, extends_base_section=True)

    x_turbomole_geometry_optimization_geometry_change_rms = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        geometry optimization convergence criterion - Root Mean Square of displacements
        ''')

    x_turbomole_geometry_optimization_threshold_force_rms = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        geometry optimization convergence criterion - Root Mean Square of forces
        ''')

    x_turbomole_geometry_optimization_trustregion_initial = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        geometry optimization trust region - initial radius
        ''')

    x_turbomole_geometry_optimization_trustregion_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        geometry optimization trust region - maximum radius
        ''')

    x_turbomole_geometry_optimization_trustregion_min = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        geometry optimization trust region - minimum radius
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_turbomole_module = Quantity(
        type=str,
        shape=[],
        description='''
        The name of the Turbomole module used for this single configuration calculation.
        ''')

    x_turbomole_potential_energy_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Final potential energy
        ''')

    x_turbomole_vibrations_infrared_activity = Quantity(
        type=bool,
        shape=['x_turbomole_vibrations_num_modes'],
        description='''
        IR activicity for vibration modes
        ''')

    x_turbomole_vibrations_raman_activity = Quantity(
        type=bool,
        shape=['x_turbomole_vibrations_num_modes'],
        description='''
        Raman activicity for vibration modes
        ''')

    x_turbomole_vibrations_intensities = Quantity(
        type=np.dtype(np.float64),
        shape=['x_turbomole_vibrations_num_modes'],
        description='''
        IR Intensity for each vibrational normal mode
        ''')

    x_turbomole_vibrations_mode_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['x_turbomole_vibrations_num_modes'],
        description='''
        Excitation energy associated with the vibrational normal modes.
        ''')

    x_turbomole_vibrations_normal_modes = Quantity(
        type=np.dtype(np.float64),
        shape=['x_turbomole_vibrations_num_modes', 'number_of_atoms', 3],
        description='''
        Nuclear displacements for each vibrational normal mode
        ''')

    x_turbomole_vibrations_num_modes = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of vibrational normal modes
        ''')

    x_turbomole_virial_theorem = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Final value from the virial theorem
        ''')

    x_turbomole_wave_func_norm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Final Wave Function Norm
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_turbomole_nodename = Quantity(
        type=str,
        shape=[],
        description='''
        compute node
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_turbomole_pceem_charges = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Charges of the point charges in the unit cell used by the PCEEM embedding model
        ''')

    x_turbomole_pceem_max_multipole = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum multipole moment used in the PCEEM embedding
        ''')

    x_turbomole_pceem_min_separation_cells = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Minimum separation between cells in PCEEM embedding for periodic fast multipole
        treatment
        ''')

    x_turbomole_pceem_multipole_precision = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Multipole precision parameter for PCEEM embedding
        ''')
