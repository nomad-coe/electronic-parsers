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
    Reference, JSON
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_gamess_section_atom_forces(MSection):
    '''
    section that contains Cartesian forces of the system for a given geometry
    '''

    m_def = Section(validate=False)

    x_gamess_atom_x_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''')

    x_gamess_atom_y_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''')

    x_gamess_atom_z_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''')


class x_gamess_section_cis(MSection):
    '''
    Configuration interaction singles excitation energies and oscillator strengths.
    '''

    m_def = Section(validate=False)

    x_gamess_cis_excitation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Value of the excitation energies for configuration interaction singles excited
        states.
        ''')

    x_gamess_cis_oscillator_strength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of the oscillator strengths for configuration interaction singles excited
        states.
        ''')


class x_gamess_section_ci(MSection):
    '''
    Configuration interaction energies.
    '''

    m_def = Section(validate=False)


class x_gamess_section_coupled_cluster(MSection):
    '''
    Coupled cluster energies.
    '''

    m_def = Section(validate=False)


class x_gamess_section_elstruc_method(MSection):
    '''
    Section containing electronic structure method.
    '''

    m_def = Section(validate=False)

    x_gamess_electronic_structure_method = Quantity(
        type=str,
        shape=[],
        description='''
        Name of electronic structure method.
        ''')


class x_gamess_section_excited_states(MSection):
    '''
    Time-dependent DFT and configuration interaction singles results.
    '''

    m_def = Section(validate=False)

    x_gamess_section_cis = SubSection(
        sub_section=SectionProxy('x_gamess_section_cis'),
        repeats=True)

    x_gamess_section_tddft = SubSection(
        sub_section=SectionProxy('x_gamess_section_tddft'),
        repeats=True)


class x_gamess_section_frequencies(MSection):
    '''
    section for the values of the frequencies, reduced masses and normal mode vectors
    '''

    m_def = Section(validate=False)

    x_gamess_frequencies = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_frequencies'],
        description='''
        values of frequencies, in cm-1
        ''')

    x_gamess_frequency_values = Quantity(
        type=str,
        shape=[],
        description='''
        values of frequencies, in cm-1
        ''')

    x_gamess_red_masses = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_frequencies'],
        description='''
        values of normal mode reduced masses
        ''')

    x_gamess_reduced_masses = Quantity(
        type=str,
        shape=['number_of_reduced_masses_rows'],
        description='''
        values of normal mode reduced masses
        ''')


class x_gamess_section_geometry_optimization_info(MSection):
    '''
    Specifies whether a geometry optimization is converged.
    '''

    m_def = Section(validate=False)

    x_gamess_geometry_optimization_converged = Quantity(
        type=str,
        shape=[],
        description='''
        Specifies whether a geometry optimization is converged.
        ''')


class x_gamess_section_geometry(MSection):
    '''
    section that contains Cartesian coordinates of the system for a given geometry
    '''

    m_def = Section(validate=False)

    x_gamess_atom_positions = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        unit='meter',
        description='''
        Initial positions of all the atoms, in Cartesian coordinates.
        ''')

    x_gamess_atom_x_coord = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x coordinate for the atoms
        ''')

    x_gamess_atom_y_coord = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y coordinate for the atoms
        ''')

    x_gamess_atom_z_coord = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z coordinate for the atoms
        ''')


class x_gamess_section_mcscf(MSection):
    '''
    Multiconfigurational SCF energies.
    '''

    m_def = Section(validate=False)

    x_gamess_energy_mcscf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Value of the MCSCF total energy, normally CASSCF, during the iterations.
        ''')

    x_gamess_mcscf_active_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of MCSCF active electrons in the calculation.
        ''')

    x_gamess_mcscf_active_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of MCSCF active orbitals in the calculation.
        ''')

    x_gamess_mcscf_inactive_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of MCSCF inactive orbitals in the calculation.
        ''')


class x_gamess_section_moller_plesset(MSection):
    '''
    Perturbative Moller-Plesset energies.
    '''

    m_def = Section(validate=False)


class x_gamess_section_mrpt2(MSection):
    '''
    Multiference multiconfigurational energies at second order of perturbation theory.
    '''

    m_def = Section(validate=False)

    x_gamess_mrpt2_active_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of active electrons in MRPT2 calculation.
        ''')

    x_gamess_mrpt2_active_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of active orbitals in MRPT2 calculation.
        ''')

    x_gamess_mrpt2_doubly_occupied_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of doubly occupied orbitals in MRPT2 calculation.
        ''')

    x_gamess_mrpt2_external_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of external orbitals in MRPT2 calculation.
        ''')

    x_gamess_mrpt2_frozen_core_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of frozen core orbitals in MRPT2 calculation.
        ''')

    x_gamess_mrpt2_frozen_virtual_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of frozen virtual orbitals in MRPT2 calculation.
        ''')

    x_gamess_mrpt2_method_type = Quantity(
        type=str,
        shape=[],
        description='''
        Determinant (MRPT2) or CSF (MC-QDPT) method for second-order perturbation theory
        calculation
        ''')


class x_gamess_section_scf_hf_method(MSection):
    '''
    Section containing type of SCF method employed (RHF,UHF,ROHF or GVB).
    '''

    m_def = Section(validate=False)

    x_gamess_scf_hf_method = Quantity(
        type=str,
        shape=[],
        description='''
        Type of SCF method employed.
        ''')


class x_gamess_section_tddft(MSection):
    '''
    Time-dependent DFT excitation energies and oscillator strengths.
    '''

    m_def = Section(validate=False)

    x_gamess_tddft_excitation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Value of the excitation energies for time-dependent DFT excited states.
        ''')

    x_gamess_tddft_oscillator_strength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of the oscillator strengths for time-dependent DFT excited states.
        ''')


class BandEnergies(simulation.calculation.BandEnergies):

    m_def = Section(validate=False, extends_base_section=True)

    x_gamess_alpha_eigenvalues_values = Quantity(
        type=str,
        shape=[],
        description='''
        values of eigenenergies for alpha MOs
        ''')

    x_gamess_beta_eigenvalues_values = Quantity(
        type=str,
        shape=[],
        description='''
        values of eigenenergies for occupied beta MOs
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_gamess_atom_positions_initial = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        unit='meter',
        description='''
        Initial positions of all the atoms, in Cartesian coordinates.
        ''')

    x_gamess_atom_x_coord_initial = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x coordinate for the atoms of the initial geometry
        ''')

    x_gamess_atom_y_coord_initial = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y coordinate for the atoms of the initial geometry
        ''')

    x_gamess_atom_z_coord_initial = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z coordinate for the atoms of the initial geometry
        ''')

    x_gamess_number_of_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        number of electrons for system
        ''')

    x_gamess_atomic_number = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        atomic number for atoms
        ''')

    x_gamess_memory = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total memory for GAMESS job
        ''')

    x_gamess_spin_target_multiplicity = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Target (user-imposed) value of the spin multiplicity $M=2S+1$, where $S$ is the
        total spin. It is an integer value. This value is not necessarly the value
        obtained at the end of the calculation. See spin_S2 for the converged value of the
        spin moment.
        ''')

    x_gamess_total_charge = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total charge of the system.
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_gamess_basis_set_diffsp = Quantity(
        type=str,
        shape=[],
        description='''
        Include a set of SP diffuse functions on heavy atoms or not
        ''')

    x_gamess_basis_set_diffs = Quantity(
        type=str,
        shape=[],
        description='''
        Incluse a set of S diffuse functions on light atoms or not
        ''')

    x_gamess_basis_set_gbasis = Quantity(
        type=str,
        shape=[],
        description='''
        Gaussian basis set main name
        ''')

    x_gamess_basis_set_igauss = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of main Gaussians
        ''')

    x_gamess_basis_set_ndfunc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of polarization d function sets on heavy atoms
        ''')

    x_gamess_basis_set_nffunc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of polarization f function sets on heavy atoms
        ''')

    x_gamess_basis_set_npfunc = Quantity(
        type=str,
        shape=[],
        description='''
        Number of polarization p function sets on light atoms
        ''')

    x_gamess_basis_set_polar = Quantity(
        type=str,
        shape=[],
        description='''
        Exponents of polarization functions
        ''')

    x_gamess_cctype = Quantity(
        type=str,
        shape=[],
        description='''
        Type of coupled cluster method employed
        ''')

    x_gamess_cistep = Quantity(
        type=str,
        shape=[],
        description='''
        Determinant or CSF method for multiconfigurational SCF calculation
        ''')

    x_gamess_citype = Quantity(
        type=str,
        shape=[],
        description='''
        Type of configuration interaction method employed
        ''')

    x_gamess_comp_method = Quantity(
        type=str,
        shape=[],
        description='''
        Control if the G3MP2 composite method has been defined
        ''')

    x_gamess_mcscf_casscf = Quantity(
        type=str,
        shape=[],
        description='''
        This indicates whether the multiconfigurational SCF calculation is a complete
        active space SCF calculation or not
        ''')

    x_gamess_method = Quantity(
        type=str,
        shape=[],
        description='''
        String identifying in an unique way the WF method used for the final
        wavefunctions.
        ''')

    x_gamess_mplevel = Quantity(
        type=str,
        shape=[],
        description='''
        Level of second-orden Moller-Plesset perturbation theory
        ''')

    x_gamess_pptype = Quantity(
        type=str,
        shape=[],
        description='''
        Name of the pseudopotential employed
        ''')

    x_gamess_relatmethod = Quantity(
        type=str,
        shape=[],
        description='''
        Type of relativistic method employed
        ''')

    x_gamess_scf_method = Quantity(
        type=str,
        shape=[],
        description='''
        String identifying in an unique way the SCF method used in the calculation.
        ''')

    x_gamess_scf_type = Quantity(
        type=str,
        shape=[],
        description='''
        String identifying in an unique way the SCF method used in the calculation.
        ''')

    x_gamess_tddfttype = Quantity(
        type=str,
        shape=[],
        description='''
        Type of time-dependent DFT calculation
        ''')

    x_gamess_vbtype = Quantity(
        type=str,
        shape=[],
        description='''
        Type of valence bond method employed
        ''')

    x_gamess_xc = Quantity(
        type=str,
        shape=[],
        description='''
        String identifying in an unique way the XC method used for the final
        wavefunctions.
        ''')

    x_gamess_control_options = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_gamess_system_options = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_gamess_basis_options = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_gamess_section_elstruc_method = SubSection(
        sub_section=SectionProxy('x_gamess_section_elstruc_method'),
        repeats=True)

    x_gamess_section_scf_hf_method = SubSection(
        sub_section=SectionProxy('x_gamess_section_scf_hf_method'),
        repeats=True)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_gamess_program_execution_date = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_gamess_program_implementation = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''')

    x_gamess_section_geometry_optimization_info = SubSection(
        sub_section=SectionProxy('x_gamess_section_geometry_optimization_info'),
        repeats=True)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_gamess_energy_scf = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Final value of the total electronic energy calculated with the method described in
        XC_method.
        ''')

    x_gamess_energy_total_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Value of the total electronic energy calculated with the method described in
        XC_method during each self-consistent field (SCF) iteration.
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_gamess_section_atom_forces = SubSection(
        sub_section=SectionProxy('x_gamess_section_atom_forces'),
        repeats=True)

    x_gamess_section_ci = SubSection(
        sub_section=SectionProxy('x_gamess_section_ci'),
        repeats=True)

    x_gamess_section_coupled_cluster = SubSection(
        sub_section=SectionProxy('x_gamess_section_coupled_cluster'),
        repeats=True)

    x_gamess_section_excited_states = SubSection(
        sub_section=SectionProxy('x_gamess_section_excited_states'),
        repeats=True)

    x_gamess_section_frequencies = SubSection(
        sub_section=SectionProxy('x_gamess_section_frequencies'),
        repeats=True)

    x_gamess_section_geometry = SubSection(
        sub_section=SectionProxy('x_gamess_section_geometry'),
        repeats=True)

    x_gamess_section_mcscf = SubSection(
        sub_section=SectionProxy('x_gamess_section_mcscf'),
        repeats=True)

    x_gamess_section_moller_plesset = SubSection(
        sub_section=SectionProxy('x_gamess_section_moller_plesset'),
        repeats=True)

    x_gamess_section_mrpt2 = SubSection(
        sub_section=SectionProxy('x_gamess_section_mrpt2'),
        repeats=True)


class Energy(simulation.calculation.Energy):

    m_def = Section(validate=False, extends_base_section=True)

    x_gamess_virial_ratio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')
    x_gamess_wavefunction_normalization = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_gamess_one_electron = SubSection(
        sub_section=simulation.calculation.EnergyEntry.m_def,
        description='''
        ''')

    x_gamess_two_electron = SubSection(
        sub_section=simulation.calculation.EnergyEntry.m_def,
        description='''
        ''')
