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


m_package = Package()


class x_gaussian_configuration_core(MCategory):
    '''
    Properties defining the current configuration.
    '''

    m_def = Category()


class x_gaussian_atom_forces_type(MCategory):
    '''
    Some forces on the atoms (i.e. minus derivatives of some energy with respect to the
    atom position).
    '''

    m_def = Category()


class x_gaussian_scf_info(MCategory):
    '''
    Information on the self-consistent field (SCF) procedure.
    '''

    m_def = Category()


class x_gaussian_section_geometry(MSection):
    '''
    section that contains Cartesian coordinates of the system for a given geometry
    '''

    m_def = Section(validate=False,)

    x_gaussian_atomic_number = Quantity(
        type=str,
        shape=[],
        description='''
        atomic number for atoms
        ''',)

    x_gaussian_atom_x_coord = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x coordinate for the atoms
        ''',)

    x_gaussian_atom_y_coord = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y coordinate for the atoms
        ''',)

    x_gaussian_atom_z_coord = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z coordinate for the atoms
        ''',)


class x_gaussian_section_hybrid_coeffs(MSection):
    '''
    section that contains coefficients for the hybrid DFT functionals
    '''

    m_def = Section(validate=False,)

    hybrid_xc_coeff1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Coefficient for Hartree-Fock exchange in hybrid DFT functionals
        ''',)

    hybrid_xc_coeff2 = Quantity(
        type=str,
        shape=[],
        description='''
        Coefficients for Slater exchange, non-local exchange, local correlation, and non-
        local correlation, respectively, in hybrid DFT functionals
        ''',)

    x_gaussian_hybrid_xc_hfx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Hartree-Fock exchange
        ''',)

    x_gaussian_hybrid_xc_slater = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Slater exchange
        ''',)

    x_gaussian_hybrid_xc_nonlocalex = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Slater exchange
        ''',)

    x_gaussian_hybrid_xc_localcorr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Slater exchange
        ''',)

    x_gaussian_hybrid_xc_nonlocalcorr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Slater exchange
        ''',)


class x_gaussian_section_total_scf_one_geometry(MSection):
    '''
    Check for SCF convergence and writes the total energy value to backend
    '''

    m_def = Section(validate=False,)


class x_gaussian_section_times(MSection):
    '''
    section that contains the execution times of the run
    '''

    m_def = Section(validate=False,)

    x_gaussian_program_termination_date = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_gaussian_program_cpu_time = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)


class x_gaussian_section_atom_forces(MSection):
    '''
    section that contains Cartesian coordinates of the system for a given geometry
    '''

    m_def = Section(validate=False,)

    x_gaussian_atom_x_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''',)

    x_gaussian_atom_y_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''',)

    x_gaussian_atom_z_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        -
        ''',)


class x_gaussian_section_molecular_multipoles(MSection):
    '''
    Section describing multipoles (charges, dipoles,...).
    '''

    m_def = Section(validate=False,)

    charge = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the total charge of the system (in electronic units).
        ''',)

    dipole_moment_x = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the x component of the dipole moment (Debye).
        ''',)

    dipole_moment_y = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the y component of the dipole moment (Debye).
        ''',)

    dipole_moment_z = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the z component of the dipole moment (Debye).
        ''',)

    quadrupole_moment_xx = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xx component of the quadrupole moment (Debye-Ang).
        ''',)

    quadrupole_moment_yy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yy component of the quadrupole moment (Debye-Ang).
        ''',)

    quadrupole_moment_zz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the zz component of the quadrupole moment (Debye-Ang).
        ''',)

    quadrupole_moment_xy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xy component of the quadrupole moment (Debye-Ang).
        ''',)

    quadrupole_moment_xz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xz component of the quadrupole moment (Debye-Ang).
        ''',)

    quadrupole_moment_yz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yz component of the quadrupole moment (Debye-Ang).
        ''',)

    octapole_moment_xxx = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxx component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_yyy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yyy component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_zzz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the zzz component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_xyy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xyy component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_xxy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxy component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_xxz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxz component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_xzz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xzz component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_yzz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yzz component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_yyz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yyz component of the octapole moment (Debye-Ang**2).
        ''',)

    octapole_moment_xyz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xyz component of the octapole moment (Debye-Ang**2).
        ''',)

    hexadecapole_moment_xxxx = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxxx component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_yyyy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yyyy component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_zzzz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the zzzz component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_xxxy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxxy component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_xxxz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxxz component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_yyyx = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yyyx component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_yyyz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yyyz component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_zzzx = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the zzzx component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_zzzy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the zzzy component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_xxyy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxyy component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_xxzz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxzz component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_yyzz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yyzz component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_xxyz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the xxyz component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_yyxz = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the yyxz component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    hexadecapole_moment_zzxy = Quantity(
        type=str,
        shape=[],
        description='''
        Value of the zzxy component of the hexadecapole moment (Debye-Ang**3).
        ''',)

    x_gaussian_molecular_multipole_lm = Quantity(
        type=np.dtype(np.int32),
        shape=['x_gaussian_number_of_lm_molecular_multipoles', 2],
        description='''
        Tuples of $l$ and $m$ values for which the molecular multipoles (including the
        electric charge, dipole, etc.) are given. The meaning of the integer number $l$ is
        monopole/charge for $l=0$, dipole for $l=1$, quadrupole for $l=2$, etc. The
        meaning of the integer numbers $m$ is specified by molecular_multipole_m_kind.
        ''',)

    x_gaussian_molecular_multipole_m_kind = Quantity(
        type=str,
        shape=[],
        description='''
        String describing what the integer numbers $m$ in molecular_multipole_lm mean.
        Allowed values (for atomic multipoles) are listed in the [m\\_kind wiki
        page](https://gitlab.rzg.mpg.de/nomad-lab/nomad-meta-info/wikis/metainfo/m-kind).
        ''',)

    x_gaussian_molecular_multipole_values = Quantity(
        type=np.dtype(np.float64),
        shape=['x_gaussian_number_of_lm_molecular_multipoles'],
        description='''
        Value of the multipoles (including the monopole/charge for $l$ = 0, the dipole for
        $l$ = 1, etc.).
        ''',)

    x_gaussian_number_of_lm_molecular_multipoles = Quantity(
        type=int,
        shape=[],
        description='''
        Number of $l,m$ combinations for which molecular multipoles are given.
        ''',)


class x_gaussian_section_geometry_optimization_info(MSection):
    '''
    Specifies whether a geometry optimization is converged.
    '''

    m_def = Section(validate=False,)

    x_gaussian_geometry_optimization_converged = Quantity(
        type=str,
        shape=[],
        description='''
        Specifies whether a geometry optimization is converged.
        ''',)


class x_gaussian_section_frequencies(MSection):
    '''
    section for the values of the frequencies, reduced masses and normal mode vectors
    '''

    m_def = Section(validate=False,)

    x_gaussian_frequency_values = Quantity(
        type=str,
        shape=['number_of_frequency_rows'],
        description='''
        values of frequencies, in cm-1
        ''',)

    x_gaussian_frequencies = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_frequencies'],
        description='''
        values of frequencies, in cm-1
        ''',)

    x_gaussian_reduced_masses = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_reduced_masses_rows'],
        description='''
        values of normal mode reduced masses
        ''',)

    x_gaussian_red_masses = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_frequencies'],
        description='''
        values of normal mode reduced masses
        ''',)

    x_gaussian_normal_modes = Quantity(
        type=str,
        shape=['number_of_normal_modes_rows'],
        description='''
        normal mode vectors
        ''',)

    x_gaussian_normal_mode_values = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_frequencies', 'number_of_atoms', 3],
        description='''
        normal mode vectors
        ''',)


class x_gaussian_section_thermochem(MSection):
    '''
    section for thermochemical quantities
    '''

    m_def = Section(validate=False,)

    x_gaussian_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of temperature for thermochemical values
        ''',)

    x_gaussian_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of pressure for thermochemical values
        ''',)

    x_gaussian_moment_of_inertia_X = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        X component of moment of inertia
        ''',)

    x_gaussian_moment_of_inertia_Y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Y component of moment of inertia
        ''',)

    x_gaussian_moment_of_inertia_Z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Z component of moment of inertia
        ''',)

    x_gaussian_moments = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Values of moments of inertia
        ''',)

    x_gaussian_zero_point_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of zero-point energy
        ''',)

    x_gaussian_thermal_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of thermal correction to total energy
        ''',)

    x_gaussian_thermal_correction_enthalpy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of thermal correction to enthalpy
        ''',)

    x_gaussian_thermal_correction_free_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of thermal correction to Gibbs free energy
        ''',)


class x_gaussian_section_force_constant_matrix(MSection):
    '''
    section for force constant matrix in Cartesians. Units are mdyne.Angstrom
    '''

    m_def = Section(validate=False,)

    x_gaussian_force_constants = Quantity(
        type=str,
        shape=[],
        description='''
        Force constant matrix elements
        ''',)

    x_gaussian_force_constant_values = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_degrees_of_freedom', 'number_of_degrees_of_freedom'],
        description='''
        Force constant matrix element values
        ''',)


class x_gaussian_section_orbital_symmetries(MSection):
    '''
    section for the symmetry of the MOs
    '''

    m_def = Section(validate=False,)

    x_gaussian_alpha_occ_symmetry_values = Quantity(
        type=str,
        shape=['number_of_alpha_occ_rows'],
        description='''
        symmetry of the alpha occupied MOs
        ''',)

    x_gaussian_alpha_vir_symmetry_values = Quantity(
        type=str,
        shape=['number_of_alpha_vir_rows'],
        description='''
        symmetry of the alpha virtual MOs
        ''',)

    x_gaussian_beta_occ_symmetry_values = Quantity(
        type=str,
        shape=['number_of_beta_occ_rows'],
        description='''
        symmetry of the beta occupied MOs
        ''',)

    x_gaussian_beta_vir_symmetry_values = Quantity(
        type=str,
        shape=['number_of_beta_vir_rows'],
        description='''
        symmetry of the beta virtual MOs
        ''',)

    x_gaussian_alpha_symmetries = Quantity(
        type=str,
        shape=['number_of_alpha_mos'],
        description='''
        symmetry of the alpha MOs
        ''',)

    x_gaussian_beta_symmetries = Quantity(
        type=str,
        shape=['number_of_beta_mos'],
        description='''
        symmetry of the beta MOs
        ''',)


class x_gaussian_section_symmetry(MSection):
    '''
    section for the symmetry of the electronic state
    '''

    m_def = Section(validate=False,)

    x_gaussian_elstate_symmetry = Quantity(
        type=str,
        shape=[],
        description='''
        symmetry group of the electronic state
        ''',)


class x_gaussian_section_elstruc_method(MSection):
    '''
    Section containing electronic structure method.
    '''

    m_def = Section(validate=False,)

    x_gaussian_electronic_structure_method = Quantity(
        type=str,
        shape=[],
        description='''
        Name of electronic structure method.
        ''',)


class x_gaussian_section_energy_components(MSection):
    '''
    Section containing total energy components
    '''

    m_def = Section(validate=False,)


class x_gaussian_section_moller_plesset(MSection):
    '''
    Perturbative Moller-Plesset energies.
    '''

    m_def = Section(validate=False,)

    x_gaussian_mp2_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and MP2 energies.
        ''',)

    x_gaussian_mp3_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and MP3 energies.
        ''',)

    x_gaussian_mp4dq_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and MP4(DQ) energies.
        ''',)

    x_gaussian_mp4sdq_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and MP4(SDQ) energies.
        ''',)

    x_gaussian_mp4sdtq_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and MP4(SDTQ) energies.
        ''',)

    x_gaussian_mp5_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and MP5 energies.
        ''',)


class x_gaussian_section_coupled_cluster(MSection):
    '''
    Coupled cluster energies.
    '''

    m_def = Section(validate=False,)

    x_gaussian_ccsd_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and CCSD energies.
        ''',)


class x_gaussian_section_quadratic_ci(MSection):
    '''
    Quadratic CI energies.
    '''

    m_def = Section(validate=False,)

    x_gaussian_qcisd_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and QCISD energies.
        ''',)

    x_gaussian_qcisdtq_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and QCISD(TQ) energies.
        ''',)


class x_gaussian_section_ci(MSection):
    '''
    CI energies.
    '''

    m_def = Section(validate=False,)

    x_gaussian_ci_correction_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Difference between SCF and CI energies.
        ''',)


class x_gaussian_section_semiempirical(MSection):
    '''
    semiempirical convergence cycles and energies.
    '''

    m_def = Section(validate=False,)

    x_gaussian_semiempirical_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        semiempirical energies.
        ''',)

    x_gaussian_semiempirical_method = Quantity(
        type=str,
        shape=[],
        description='''
        semiempirical method.
        ''',)


class x_gaussian_section_molmech(MSection):
    '''
    molecular mechanics method and energies.
    '''

    m_def = Section(validate=False,)

    x_gaussian_molmech_method = Quantity(
        type=str,
        shape=[],
        description='''
        molecular mechanics method.
        ''',)


class x_gaussian_section_models(MSection):
    '''
    composite model chemistries.
    '''

    m_def = Section(validate=False,)


class x_gaussian_section_excited_initial(MSection):
    '''
    Excited state energies and properties
    '''

    m_def = Section(validate=False,)


class x_gaussian_section_excited(MSection):
    '''
    CI singles, TDDFT/TDHF, ZINDO or EOMCCSD excited state energies and properties
    '''

    m_def = Section(validate=False,)

    x_gaussian_excited_state_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CIS, TDDFT/TDHF, ZINDO or EOMCCSD excited state number
        ''',)

    x_gaussian_excited_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        CIS, TDDFT/TDHF, ZINDO or EOMCCSD excited state energy
        ''',)

    x_gaussian_excited_oscstrength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CIS, TDDFT/TDHF, ZINDO or EOMCCSD excited state oscillator strength
        ''',)

    x_gaussian_excited_spin_squared = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CIS, TDDFT/TDHF, ZINDO or EOMCCSD excited state spin squared value
        ''',)

    x_gaussian_excited_transition = Quantity(
        type=str,
        shape=[],
        description='''
        CIS, TDDFT/TDHF, ZINDO or EOMCCSD excited state MOs involved in transitions and
        their coefficients
        ''',)


class x_gaussian_section_casscf(MSection):
    '''
    CASSCF energies and properties
    '''

    m_def = Section(validate=False,)

    x_gaussian_casscf_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        CASSCF energy
        ''',)

    x_gaussian_casscf_determinant = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CASSCF determinant number
        ''',)

    x_gaussian_casscf_coefficient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CASSCF determinant coefficient
        ''',)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True,)

    x_gaussian_number_of_atoms = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        number of atoms of the system
        ''',)

    x_gaussian_atomic_masses = Quantity(
        type=str,
        shape=[],
        description='''
        atomic masses for atoms
        ''',)

    x_gaussian_total_charge = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total charge of the system.
        ''',)

    x_gaussian_spin_target_multiplicity = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Target (user-imposed) value of the spin multiplicity $M=2S+1$, where $S$ is the
        total spin. It is an integer value. This value is not necessarly the value
        obtained at the end of the calculation. See spin_S2 for the converged value of the
        spin moment.
        ''',)

    x_gaussian_geometry_lattice_vector_x = Quantity(
        type=str,
        shape=[],
        description='''
        x component of lattice vector
        ''',)

    x_gaussian_geometry_lattice_vector_y = Quantity(
        type=str,
        shape=[],
        description='''
        y component of lattice vector
        ''',)

    x_gaussian_geometry_lattice_vector_z = Quantity(
        type=str,
        shape=[],
        description='''
        z component of lattice vector
        ''',)

    x_gaussian_masses = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        values of atomic masses
        ''',)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True,)

    x_gaussian_atom_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        unit='newton',
        description='''
        Forces acting on the atoms, calculated as minus gradient of energy_total.
        ''',
        categories=[x_gaussian_atom_forces_type],)

    x_gaussian_energy_total_scf_converged = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        SCF total energy converged for a given geometry.
        ''',)

    x_gaussian_number_of_scf_iterations = Quantity(
        type=int,
        shape=[],
        description='''
        Number of performed self-consistent field (SCF) iterations at DFT level.
        ''',
        categories=[x_gaussian_scf_info],)

    x_gaussian_section_hybrid_coeffs = SubSection(
        sub_section=SectionProxy('x_gaussian_section_hybrid_coeffs'),
        repeats=True,)

    x_gaussian_section_total_scf_one_geometry = SubSection(
        sub_section=SectionProxy('x_gaussian_section_total_scf_one_geometry'),
        repeats=True,)

    x_gaussian_section_atom_forces = SubSection(
        sub_section=SectionProxy('x_gaussian_section_atom_forces'),
        repeats=True,)

    x_gaussian_section_molecular_multipoles = SubSection(
        sub_section=SectionProxy('x_gaussian_section_molecular_multipoles'),
        repeats=True,)

    x_gaussian_section_energy_components = SubSection(
        sub_section=SectionProxy('x_gaussian_section_energy_components'),
        repeats=True,)

    x_gaussian_section_moller_plesset = SubSection(
        sub_section=SectionProxy('x_gaussian_section_moller_plesset'),
        repeats=True,)

    x_gaussian_section_coupled_cluster = SubSection(
        sub_section=SectionProxy('x_gaussian_section_coupled_cluster'),
        repeats=True,)

    x_gaussian_section_quadratic_ci = SubSection(
        sub_section=SectionProxy('x_gaussian_section_quadratic_ci'),
        repeats=True,)

    x_gaussian_section_ci = SubSection(
        sub_section=SectionProxy('x_gaussian_section_ci'),
        repeats=True,)

    x_gaussian_section_semiempirical = SubSection(
        sub_section=SectionProxy('x_gaussian_section_semiempirical'),
        repeats=True,)

    x_gaussian_section_molmech = SubSection(
        sub_section=SectionProxy('x_gaussian_section_molmech'),
        repeats=True,)

    x_gaussian_section_models = SubSection(
        sub_section=SectionProxy('x_gaussian_section_models'),
        repeats=True,)

    x_gaussian_section_excited_initial = SubSection(
        sub_section=SectionProxy('x_gaussian_section_excited_initial'),
        repeats=True,)

    x_gaussian_section_excited = SubSection(
        sub_section=SectionProxy('x_gaussian_section_excited'),
        repeats=True,)

    x_gaussian_section_casscf = SubSection(
        sub_section=SectionProxy('x_gaussian_section_casscf'),
        repeats=True,)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True,)

    x_gaussian_chk_file = Quantity(
        type=str,
        shape=[],
        description='''
        binary file with detailed output information
        ''',)

    x_gaussian_memory = Quantity(
        type=str,
        shape=[],
        description='''
        total memory for the run
        ''')

    x_gaussian_number_of_processors = Quantity(
        type=str,
        shape=[],
        description='''
        number of processors used
        ''')

    x_gaussian_program_execution_date = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_gaussian_program_release_date = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_gaussian_program_implementation = Quantity(
        type=str,
        shape=[],
        description='''
        -
        ''',)

    x_gaussian_atom_positions = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        unit='meter',
        description='''
        Positions of all the atoms, in Cartesian coordinates. This metadata defines a
        configuration and is therefore required.
        ''',
        categories=[x_gaussian_configuration_core],)

    x_gaussian_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        Labels of the atoms. These strings identify the atom kind and conventionally start
        with the symbol of the atomic species, possibly followed by a number. The same
        atomic species can be labelled with more than one atom_labels in order to
        distinguish, e.g., atoms of the same species assigned to different atom-centered
        basis sets or pseudopotentials, or simply atoms in different locations in the
        structure (e.g., bulk and surface). These labels can also be used for *particles*
        that do not correspond to physical atoms (e.g., ghost atoms in some codes using
        atom-centered basis sets). This metadata defines a configuration and is therefore
        required.
        ''',
        categories=[x_gaussian_configuration_core],)

    x_gaussian_section_geometry = SubSection(
        sub_section=SectionProxy('x_gaussian_section_geometry'),
        repeats=True,)

    x_gaussian_section_times = SubSection(
        sub_section=SectionProxy('x_gaussian_section_times'),
        repeats=True,)

    x_gaussian_section_geometry_optimization_info = SubSection(
        sub_section=SectionProxy('x_gaussian_section_geometry_optimization_info'),
        repeats=True,)

    x_gaussian_section_frequencies = SubSection(
        sub_section=SectionProxy('x_gaussian_section_frequencies'),
        repeats=True,)

    x_gaussian_section_thermochem = SubSection(
        sub_section=SectionProxy('x_gaussian_section_thermochem'),
        repeats=True,)

    x_gaussian_section_force_constant_matrix = SubSection(
        sub_section=SectionProxy('x_gaussian_section_force_constant_matrix'),
        repeats=True,)

    x_gaussian_section_orbital_symmetries = SubSection(
        sub_section=SectionProxy('x_gaussian_section_orbital_symmetries'),
        repeats=True,)

    x_gaussian_section_symmetry = SubSection(
        sub_section=SectionProxy('x_gaussian_section_symmetry'),
        repeats=True,)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True,)

    x_gaussian_energy_total_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Total energy calculated with a given method during the self-consistent field (SCF)
        iterations.
        ''',)

    x_gaussian_delta_energy_total_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Total energy increment calculated with a given method during the self-consistent
        field (SCF) iterations.
        ''',)

    x_gaussian_single_configuration_calculation_converged = Quantity(
        type=str,
        shape=[],
        description='''
        Determines whether a single configuration calculation is converged.
        ''',)

    x_gaussian_spin_S2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Real value of spin squared.
        ''',)

    x_gaussian_after_annihilation_spin_S2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Real value of spin squared resulting from the annihilation of the first spin
        contaminant.
        ''',)

    x_gaussian_energy_scf = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Value of the SCF total energy, either HF or DFT.
        ''')

    x_gaussian_perturbation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Value of the perturbation energy for double hybrids
        ''')

    x_gaussian_hf_detect = Quantity(
        type=str,
        shape=[],
        description='''
        Determine if the SCF method is one of RHF, UHF, or ROHF
        ''',)

    x_gaussian_energy_electrostatic = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Total electrostatic energy (nuclei + electrons), defined consistently with
        calculation_method.
        ''')

    x_gaussian_energy_error = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Error in the total energy. Defined consistently with XC_method.
        ''')

    x_gaussian_electronic_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Self-consistent electronic kinetic energy as defined in XC_method.
        ''')


class BandEnergies(simulation.calculation.BandEnergies):

    m_def = Section(validate=False, extends_base_section=True,)

    x_gaussian_alpha_occ_eigenvalues_values = Quantity(
        type=str,
        shape=[],
        description='''
        values of eigenenergies for occupied alpha MOs
        ''',)

    x_gaussian_alpha_vir_eigenvalues_values = Quantity(
        type=str,
        shape=[],
        description='''
        values of eigenenergies for virtual alpha MOs
        ''',)

    x_gaussian_beta_occ_eigenvalues_values = Quantity(
        type=str,
        shape=[],
        description='''
        values of eigenenergies for occupied beta MOs
        ''',)

    x_gaussian_beta_vir_eigenvalues_values = Quantity(
        type=str,
        shape=[],
        description='''
        values of eigenenergies for virtual beta MOs
        ''',)

    x_gaussian_alpha_eigenvalues = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_alpha_mos'],
        description='''
        values of eigenenergies, alpha occ
        ''',)

    x_gaussian_beta_eigenvalues = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_beta_mos'],
        description='''
        values of eigenenergies, beta occ
        ''',)

    x_gaussian_alpha_occupations = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_alpha_mos'],
        description='''
        values of eigenenergies, alpha occ
        ''',)

    x_gaussian_beta_occupations = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_beta_mos'],
        description='''
        values of eigenenergies, beta occ
        ''',)

    x_gaussian_eigenvalues_occupation = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_spin_channels', 'number_of_eigenvalues_kpoints', 'number_of_eigenvalues'],
        description='''
        Occupation of the eigenstates whose (energy) eigenvalues are given in
        eigenvalues_values.
        ''',)

    x_gaussian_eigenvalues_values = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_spin_channels', 'number_of_eigenvalues_kpoints', 'number_of_eigenvalues'],
        unit='joule',
        description='''
        Values of the (electronic-energy) eigenvalues. Their occupations are given in
        eigenvalues_occupation.
        ''',)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True,)

    x_gaussian_settings = Quantity(
        type=str,
        shape=[],
        description='''
        electronic structure method, basis set, etc.
        ''',)

    x_gaussian_settings_corrected = Quantity(
        type=str,
        shape=[],
        description='''
        electronic structure method, basis set, etc.
        ''',)

    x_gaussian_method = Quantity(
        type=str,
        shape=[],
        description='''
        String identifying in an unique way the electronic structure method used for the
        final wavefunctions.
        ''',)

    x_gaussian_xc = Quantity(
        type=str,
        shape=[],
        description='''
        String identifying in an unique way the XC method used for the final
        wavefunctions.
        ''',)

    x_gaussian_section_elstruc_method = SubSection(
        sub_section=SectionProxy('x_gaussian_section_elstruc_method'),
        repeats=True,)
