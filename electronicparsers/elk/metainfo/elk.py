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


class x_elk_section_lattice_vectors(MSection):
    '''
    lattice vectors
    '''

    m_def = Section(validate=False)

    x_elk_geometry_lattice_vector_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of lattice vector
        ''')

    x_elk_geometry_lattice_vector_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of lattice vector
        ''')

    x_elk_geometry_lattice_vector_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of lattice vector
        ''')


class x_elk_section_reciprocal_lattice_vectors(MSection):
    '''
    reciprocal lattice vectors
    '''

    m_def = Section(validate=False)

    x_elk_geometry_reciprocal_lattice_vector_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        x component of reciprocal lattice vector
        ''')

    x_elk_geometry_reciprocal_lattice_vector_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        y component of reciprocal lattice vector
        ''')

    x_elk_geometry_reciprocal_lattice_vector_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        z component of reciprocal lattice vector
        ''')


class x_elk_section_atoms_group(MSection):
    '''
    a group of atoms of the same type
    '''

    m_def = Section(validate=False)

    x_elk_geometry_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        labels of atom
        ''')

    x_elk_geometry_atom_number = Quantity(
        type=str,
        shape=[],
        description='''
        number to identify the atoms of a species
        ''')

    x_elk_geometry_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of atomic position
        ''')

    x_elk_geometry_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of atomic position
        ''')

    x_elk_geometry_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of atomic position
        ''')


class x_elk_section_spin(MSection):
    '''
    section for exciting spin treatment
    '''

    m_def = Section(validate=False)

    x_elk_spin_treatment = Quantity(
        type=str,
        shape=[],
        description='''
        Spin treatment
        ''')


class x_elk_section_xc(MSection):
    '''
    index for elk functional
    '''

    m_def = Section(validate=False)

    x_elk_xc_functional = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        index for elk functional
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_elk_brillouin_zone_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter ** 3',
        description='''
        Brillouin zone volume
        ''')

    x_elk_simulation_reciprocal_cell = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        unit='meter',
        description='''
        Reciprocal lattice vectors of the simulation cell.
        ''')

    x_elk_unit_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter ** 3',
        description='''
        unit cell volume
        ''')

    x_elk_muffin_tin_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        muffin-tin radius
        ''')

    x_elk_muffin_tin_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        muffin-tin points
        ''')

    x_elk_number_kpoint_x = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points x
        ''')

    x_elk_number_kpoint_y = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points y
        ''')

    x_elk_number_kpoint_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points z
        ''')

    x_elk_number_kpoints = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points
        ''')

    x_elk_kpoint_offset_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        K-points offset x component
        ''')

    x_elk_kpoint_offset_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        K-points offset y component
        ''')

    x_elk_kpoint_offset_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        K-points offset z component
        ''')

    x_elk_rgkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        Radius MT * Gmax
        ''')

    x_elk_gvector_size_x = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector grid size x
        ''')

    x_elk_gvector_size_y = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector grid size y
        ''')

    x_elk_gvector_size_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector grid size z
        ''')

    x_elk_gvector_total = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector total
        ''')

    x_elk_lmaxapw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Angular momentum cut-off for the APW functions
        ''')

    x_elk_gkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        Maximum length of |G+k| for APW functions
        ''')

    x_elk_smearing_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smearing width for KS occupancies
        ''')

    x_elk_lo = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of local-orbitals
        ''')

    x_elk_gmaxvr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        Maximum length of |G|
        ''')

    x_elk_valence_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of valence states
        ''')

    x_elk_core_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of core states
        ''')

    x_elk_empty_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of empty states
        ''')

    x_elk_wigner_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        Effective Wigner radius
        ''')

    x_elk_electronic_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Electronic charge
        ''')

    x_elk_valence_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Valence charge
        ''')

    x_elk_nuclear_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Nuclear charge
        ''')

    x_elk_core_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Core charge
        ''')

    x_elk_section_lattice_vectors = SubSection(
        sub_section=SectionProxy('x_elk_section_lattice_vectors'),
        repeats=True)

    x_elk_section_reciprocal_lattice_vectors = SubSection(
        sub_section=SectionProxy('x_elk_section_reciprocal_lattice_vectors'),
        repeats=True)

    x_elk_section_atoms_group = SubSection(
        sub_section=SectionProxy('x_elk_section_atoms_group'),
        repeats=True)

    x_elk_section_spin = SubSection(
        sub_section=SectionProxy('x_elk_section_spin'),
        repeats=True)

    x_elk_section_xc = SubSection(
        sub_section=SectionProxy('x_elk_section_xc'),
        repeats=True)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_elk_core_charge_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Core charge scf iteration
        ''')

    x_elk_valence_charge_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Valence charge scf iteration
        ''')

    x_elk_interstitial_charge_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Interstitial charge scf iteration
        ''')

    x_elk_fermi_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Fermi energy
        ''')

    x_elk_core_electron_kinetic_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Core-electron kinetic energy
        ''')

    x_elk_coulomb_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb energy
        ''')

    x_elk_coulomb_potential_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb potential energy
        ''')

    x_elk_nuclear_nuclear_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Nuclear-nuclear energy
        ''')

    x_elk_electron_nuclear_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Electron-nuclear energy
        ''')

    x_elk_hartree_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Hartree energy
        ''')

    x_elk_madelung_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Madelung energy
        ''')

    x_elk_exchange_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Exchange energy
        ''')

    x_elk_correlation_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Correlation energy
        ''')

    x_elk_electron_entropic_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Electron entropic energy
        ''')

    x_elk_dos_fermi_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / joule',
        description='''
        DOS at Fermi energy
        ''')

    x_elk_direct_gap_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Estimated fundamental direct gap
        ''')

    x_elk_indirect_gap_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Estimated fundamental indirect gap
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_elk_core_charge_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Core charge final
        ''')

    x_elk_valence_charge_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Valence charge final
        ''')

    x_elk_interstitial_charge_final = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Interstitial charge final
        ''')

    x_elk_fermi_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Fermi energy final
        ''')

    x_elk_core_electron_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Core-electron kinetic energy final
        ''')

    x_elk_coulomb_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb energy final
        ''')

    x_elk_coulomb_potential_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb potential energy final
        ''')

    x_elk_nuclear_nuclear_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Nuclear-nuclear energy final
        ''')

    x_elk_electron_nuclear_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Electron-nuclear energy final
        ''')

    x_elk_hartree_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Hartree energy final
        ''')

    x_elk_madelung_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Madelung energy final
        ''')

    x_elk_exchange_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Exchange energy final
        ''')

    x_elk_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Correlation energy final
        ''')

    x_elk_electron_entropic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Electron entropic energy final
        ''')

    x_elk_dos_fermi = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / joule',
        description='''
        DOS at Fermi energy
        ''')

    x_elk_direct_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Estimated fundamental direct gap final
        ''')

    x_elk_indirect_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Estimated fundamental indirect gap final
        ''')
