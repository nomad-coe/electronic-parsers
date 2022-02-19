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


class x_wien2k_header(MSection):
    '''
    header (labels) of wien2k.
    '''

    m_def = Section(validate=False)

    x_wien2k_release_date = Quantity(
        type=str,
        shape=[],
        description='''
        Release date of wien2k.
        ''')

    x_wien2k_version = Quantity(
        type=str,
        shape=[],
        description='''
        Version of WIEN2k.
        ''')


class x_wien2k_section_XC(MSection):
    '''
    exchange-correlation potential, in in0
    '''

    m_def = Section(validate=False)

    x_wien2k_indxc = Quantity(
        type=str,
        shape=[],
        description='''
        exchange-correlation potential, in in0
        ''')


class x_wien2k_section_equiv_atoms(MSection):
    '''
    section containing a class of equivalent atoms
    '''

    m_def = Section(validate=False)

    x_wien2k_atom_pos_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        position of atom x in internal units
        ''')

    x_wien2k_atom_pos_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        position of atom y in internal units
        ''')

    x_wien2k_atom_pos_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        position of atom z  in internal units
        ''')

    x_wien2k_atom_name = Quantity(
        type=str,
        shape=[],
        description='''
        name of atom, labelling non-equvalent atoms
        ''')

    x_wien2k_NPT = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of radial mesh points
        ''')

    x_wien2k_RMT = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        atomic sphere radius (muffin-tin radius)
        ''')

    x_wien2k_R0 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        first radial mesh point
        ''')

    x_wien2k_atomic_number_Z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        atomic number Z
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_wien2k_header = SubSection(
        sub_section=SectionProxy('x_wien2k_header'),
        repeats=True)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_wien2k_iteration_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        scf iteration number
        ''')

    x_wien2k_nr_of_independent_atoms = Quantity(
        type=int,
        description='''
        number of independent atoms in the cell
        ''')

    x_wien2k_potential_option = Quantity(
        type=str,
        shape=[],
        description='''
        exchange correlation potential option
        ''')

    x_wien2k_system_name = Quantity(
        type=str,
        shape=[],
        description='''
        user given name for this system
        ''')

    x_wien2k_total_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        total number of atoms in the cell
        ''')

    x_wien2k_lattice_const_a = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        lattice parameter a in this calculation
        ''')

    x_wien2k_lattice_const_b = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        lattice parameter b in this calculation
        ''')

    x_wien2k_lattice_const_c = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        lattice parameter c in this calculation
        ''')

    x_wien2k_unit_cell_volume_bohr3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr ** 3',
        description='''
        unit cell volume
        ''')

    x_wien2k_spinpolarization = Quantity(
        type=str,
        description='''
        spinpolarization treatment
        ''')

    x_wien2k_noe = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        number of electrons
        ''')

    x_wien2k_nr_kpts = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        number of k-points
        ''')

    x_wien2k_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Potential and charge cut-off, Ry**.5
        ''')

    x_wien2k_ene_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        energy gap in Ry
        ''')

    x_wien2k_ene_gap_eV = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='electron_volt',
        description='''
        energy gap in eV
        ''')

    x_wien2k_matrix_size = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        matrix size
        ''')

    x_wien2k_rkm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        rkm
        ''')

    x_wien2k_LOs = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LOs
        ''')

    x_wien2k_mmtot = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        total magnetic moment in cell
        ''')

    x_wien2k_mmint = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        magnetic moment in the interstital region
        ''')

    x_wien2k_mmi = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        magnetic moment inside the sphere
        ''')

    x_wien2k_mmi001 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        magnetic moment inside the sphere
        ''')

    x_wien2k_charge_distance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        charge distance between last 2 iterations
        ''')

    x_wien2k_for_abs = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        force on atom xx in mRy/bohr (in the local (for each atom) cartesian coordinate
        system): |F|
        ''')

    x_wien2k_for = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms', 3],
        description='''
        forces on inequivalent atoms in mRy/bohr (in the local (for each atom) cartesian coordinate
        system)
        ''')

    x_wien2k_for_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        force on atom xx in mRy/bohr (in the local (for each atom) cartesian coordinate
        system): Fx
        ''')

    x_wien2k_for_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        force on atom xx in mRy/bohr (in the local (for each atom) cartesian coordinate
        system): Fy
        ''')

    x_wien2k_for_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        force on atom xx in mRy/bohr (in the local (for each atom) cartesian coordinate
        system): Fz
        ''')

    x_wien2k_for_gl = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms', 3],
        description='''
        force on inequivalent atoms (in the global coordinate system of the unit cell (in
        the same way as the atomic positions are specified))
        ''')

    x_wien2k_for_x_gl = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        force on inequivalent atom xx (in the global coordinate system of the unit cell (in
        the same way as the atomic positions are specified)): Fx
        ''')

    x_wien2k_for_y_gl = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        force on inequivalent atom xx in (in the global coordinate system of the unit cell (in
        the same way as the atomic positions are specified)): Fy
        ''')

    x_wien2k_for_z_gl = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        force on inequivalent atom xx in (in the global coordinate system of the unit cell (in
        the same way as the atomic positions are specified)): Fz
        ''')

    x_wien2k_atom_nr = Quantity(
        type=str,
        shape=[],
        description='''
        number of atom, labelling atoms
        ''')

    x_wien2k_atom_mult = Quantity(
        type=np.dtype(np.int32),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        atom multiplicity
        ''')

    x_wien2k_sphere_nr = Quantity(
        type=str,
        shape=[],
        description='''
        number of sphere, labelling spheres
        ''')

    x_wien2k_tot_diff_charge = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        total difference charge density for atom xx between last 2 iterations
        ''')

    x_wien2k_tot_int_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        total interstitial charge (mixed after MIXER)
        ''')

    x_wien2k_tot_charge_in_sphere = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        total charge in sphere xx (mixed after MIXER)
        ''')

    x_wien2k_tot_int_charge_nm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        total interstitial charge (new (not mixed) from LAPW2+LCORE
        ''')

    x_wien2k_tot_charge_in_sphere_nm = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        total charge in sphere xx (new (not mixed) from LAPW2+LCORE
        ''')

    x_wien2k_tot_val_charge_cell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        total valence charge inside unit cell
        ''')

    x_wien2k_tot_val_charge_sphere = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        total valence charge in sphere xx
        ''')

    x_wien2k_density_at_nucleus_valence = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        density for atom xx at the nucleus (first radial mesh point); valence
        ''')

    x_wien2k_density_at_nucleus_semicore = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        density for atom xx at the nucleus (first radial mesh point); semi-core
        ''')

    x_wien2k_density_at_nucleus_core = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        density for atom xx at the nucleus (first radial mesh point); core
        ''')

    x_wien2k_density_at_nucleus_tot = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        density for atom xx at the nucleus (first radial mesh point); total
        ''')

    x_wien2k_nuclear_charge = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        nuclear and electronic charge; normalization check of electronic charge densities.
        If a significant amount of electrons is missing, one might have core states, whose
        charge density is not completely confined within the respective atomic sphere. In
        such a case the corresponding states should be treated as band states (using LOs).
        ''')

    x_wien2k_electronic_charge = Quantity(
        type=np.dtype(np.float64),
        shape=['x_wien2k_nr_of_independent_atoms'],
        description='''
        nuclear and electronic charge; normalization check of electronic charge densities.
        If a significant amount of electrons is missing, one might have core states, whose
        charge density is not completely confined within the respective atomic sphere. In
        such a case the corresponding states should be treated as band states (using LOs).
        ''')

    x_wien2k_necnr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of the nec test, labelling nec
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_wien2k_nonequiv_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of inequivalent atoms in the unit cell
        ''')

    x_wien2k_system_nameIn = Quantity(
        type=str,
        shape=[],
        description='''
        user given name for this system given in the struct file
        ''')

    x_wien2k_calc_mode = Quantity(
        type=str,
        shape=[],
        description='''
        relativistic or nonrelativistic calculation mode
        ''')

    x_wien2k_unit_cell_param_a = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        unit cell parameters - a
        ''')

    x_wien2k_unit_cell_param_b = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        unit cell parameters - b
        ''')

    x_wien2k_unit_cell_param_c = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        unit cell parameters - c
        ''')

    x_wien2k_angle_between_unit_axis_alfa = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        unit cell parameters - alfa
        ''')

    x_wien2k_angle_between_unit_axis_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        unit cell parameters - beta
        ''')

    x_wien2k_angle_between_unit_axis_gamma = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        unit cell parameters - gamma
        ''')

    x_wien2k_section_equiv_atoms = SubSection(
        sub_section=SectionProxy('x_wien2k_section_equiv_atoms'),
        repeats=True)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_wien2k_switch = Quantity(
        type=str,
        shape=[],
        description='''
        switch in in0 between TOT, KXC, POT, MULT, COUL, EXCH
        ''')

    x_wien2k_ifft = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        FFT-mesh parameters in x direction for the calculation of the XC-potential in the
        interstitial region, in in0
        ''')

    x_wien2k_ifft_x = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FFT-mesh parameters in x direction for the calculation of the XC-potential in the
        interstitial region, in in0
        ''')

    x_wien2k_ifft_y = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FFT-mesh parameters in y direction for the calculation of the XC-potential in the
        interstitial region, in in0
        ''')

    x_wien2k_ifft_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FFT-mesh parameters in z direction for the calculation of the XC-potential in the
        interstitial region, in in0
        ''')

    x_wien2k_ifft_factor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Multiplicative factor to the IFFT grid, in in0
        ''')

    x_wien2k_iprint = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        optional print switch, in in0
        ''')

    x_wien2k_wf_switch = Quantity(
        type=str,
        shape=[],
        description='''
        wave function switch between WFFIL, SUPWF, WPPRI
        ''')

    x_wien2k_rkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        RmtKmax - determines matrix size (convergence), where Kmax is the plane wave cut-
        off, Rmt is the smallest of all atomic sphere radii
        ''')

    x_wien2k_in2_switch = Quantity(
        type=str,
        shape=[],
        description='''
        switch, in in2 between (TOT,FOR,QTL,EFG,ALM,CLM,FERMI)
        ''')

    x_wien2k_in2_emin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        lower energy cut-off for defining the range of occupied states; in in2
        ''')

    x_wien2k_in2_ne = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        number of electrons (per unit cell) in given energy range in in2
        ''')

    x_wien2k_in2_espermin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        LAPW2 tries to find the .mean. energies for each l channel, for both the valence
        and the semicore states. To define .valence. and .semicore. it starts at (EF -
        .esepermin.) and searches for a .gap. with a width of at least .eseper0. and
        defines this as separation energy of valence and semicore; in in2
        ''')

    x_wien2k_in2_esper0 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        minimum gap width; in in2
        ''')

    x_wien2k_smearing_kind = Quantity(
        type=str,
        shape=[],
        description='''
        determines how EF is determined; in in2
        ''')

    x_wien2k_in2_gmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        max. G (magnitude of largest vector) in charge density Fourier expansion; in in2
        ''')

    x_wien2k_section_XC = SubSection(
        sub_section=SectionProxy('x_wien2k_section_XC'),
        repeats=True)
