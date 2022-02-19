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

from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference, JSON
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_fleur_header(MSection):
    '''
    header (labels) of fleur.
    '''

    m_def = Section(validate=False)

    x_fleur_version = Quantity(
        type=str,
        shape=[],
        description='''
        Version of Fleur
        ''')

    x_fleur_precision = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_fleur_with_inversion = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_fleur_with_soc = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_fleur_additional_flags = Quantity(
        type=str,
        shape=[],
        description='''
        ''')


class x_fleur_section_equiv_atoms(MSection):
    '''
    section containing a class of equivalent atoms
    '''

    m_def = Section(validate=False)

    x_fleur_atom_name = Quantity(
        type=str,
        shape=[],
        description='''
        name of atom, labelling non-equvalent atoms
        ''')

    x_fleur_atom_pos_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        position of atom x
        ''')

    x_fleur_atom_pos_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        position of atom y
        ''')

    x_fleur_atom_pos_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        position of atom z
        ''')

    x_fleur_atom_coord_scale = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        scales coordinates by 1/scale. If film=T, scales only x&y coordinates, if film=F
        also z
        ''')

    x_fleur_atomic_number_Z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        atomic number Z
        ''')

    x_fleur_nr_equiv_atoms_in_this_atom_type = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        number_equiv_atoms_in_this_atom_type
        ''')


class x_fleur_section_XC(MSection):
    '''
    exchange-correlation potential
    '''

    m_def = Section(validate=False)

    x_fleur_exch_pot = Quantity(
        type=str,
        shape=[],
        description='''
        exchange-correlation potential, in out
        ''')

    x_fleur_xc_correction = Quantity(
        type=str,
        shape=[],
        description='''
        informaion on relativistic correction for the exchange-correlation potential, in
        out
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_fleur_header = SubSection(
        sub_section=SectionProxy('x_fleur_header'),
        repeats=True)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_fleur_lattice_vector_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of vector of unit cell
        ''')

    x_fleur_lattice_vector_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of vector of unit cell
        ''')

    x_fleur_lattice_vector_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of vector of unit cell
        ''')

    x_fleur_rec_lattice_vector_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of reciprocal lattice vector
        ''')

    x_fleur_rec_lattice_vector_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of reciprocal lattice vector
        ''')

    x_fleur_rec_lattice_vector_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of reciprocal lattice vector
        ''')

    x_fleur_space_group = Quantity(
        type=str,
        shape=[],
        description='''
        space group
        ''')

    x_fleur_name_of_atom_type = Quantity(
        type=str,
        shape=[],
        description='''
        name of atom type
        ''')

    x_fleur_system_nameIn = Quantity(
        type=str,
        shape=[],
        description='''
        user given name for this system given in the inp file
        ''')

    x_fleur_system_name = Quantity(
        type=str,
        shape=[],
        description='''
        user given name for this system
        ''')

    x_fleur_total_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        total number of atoms
        ''')

    x_fleur_nr_of_atom_types = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of atom types
        ''')

    x_fleur_nuclear_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        nuclear number
        ''')

    x_fleur_number_of_core_levels = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        x_fleur_number_of_core_levels
        ''')

    x_fleur_lexpansion_cutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        l-expansion cutoff
        ''')

    x_fleur_mt_gridpoints = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        muffin-tin gridpoints
        ''')

    x_fleur_mt_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        muffin-tin radius
        ''')

    x_fleur_logarythmic_increment = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        logarythmic increment
        ''')

    x_fleur_k_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Kmax is the plane wave cut-off
        ''')

    x_fleur_G_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gmax
        ''')

    x_fleur_tot_nucl_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        total nuclear charge
        ''')

    x_fleur_tot_elec_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        total electronic charge
        ''')

    x_fleur_unit_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr ** 3',
        description='''
        unit cell volume
        ''')

    x_fleur_unit_cell_volume_omega = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        unit cell volume omega tilda
        ''')

    x_fleur_vol_interstitial = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        volume of interstitial region
        ''')

    x_fleur_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_fleur_section_equiv_atoms = SubSection(
        sub_section=SectionProxy('x_fleur_section_equiv_atoms'),
        repeats=True)


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_fleur_tot_for_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL FORCE FOR ATOM TYPE, X
        ''')

    x_fleur_tot_for_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL FORCE FOR ATOM TYPE, Y
        ''')

    x_fleur_tot_for_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL FORCE FOR ATOM TYPE, Z
        ''')

    x_fleur_tot_for_fx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL FORCE FOR ATOM TYPE, FX_TOT
        ''')

    x_fleur_tot_for_fy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL FORCE FOR ATOM TYPE, FY_TOT
        ''')

    x_fleur_tot_for_fz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL FORCE FOR ATOM TYPE, FZ_TOT
        ''')

    x_fleur_iteration_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        scf iteration number
        ''')

    x_fleur_energy_total = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        energy total
        ''')

    x_fleur_free_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        free energy
        ''')

    x_fleur_entropy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        (tkb*entropy) TS
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_fleur_nkptd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of all the k-points
        ''')

    x_fleur_k_point_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x component of vector of k point
        ''')

    x_fleur_k_point_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        y component of vector of k point
        ''')

    x_fleur_k_point_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        z component of vector of k point
        ''')

    x_fleur_k_point_weight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        weights of k point
        ''')

    x_fleur_smearing_kind = Quantity(
        type=str,
        shape=[],
        description='''
        The Brillouin zone integration mode. It can be one of hist - Use the histogram
        mode, this is the default; gauss - Use Gaussian smearing, tria - Use the
        tetrahedron method
        ''')

    x_fleur_smearing_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        specifies the width of the broadening, smearing for calculation of fermi-energy &
        weights. The Fermi smearing can be parametrized by this energy
        ''')

    x_fleur_nr_of_valence_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The number of electrons to be represented within the valence electron framework
        ''')

    x_fleur_smearing_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        Fermi smearing temperature set in Kelvin
        ''')

    x_fleur_input_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_fleur_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_fleur_eigenvalues_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_fleur_section_XC = SubSection(
        sub_section=SectionProxy('x_fleur_section_XC'),
        repeats=True)


class XCFunctional(simulation.method.XCFunctional):

    m_def = Section(validate=False, extends_base_section=True)

    x_fleur_xc_correction = Quantity(
        type=str,
        shape=[],
        description='''
        ''')


class BaseCalculation(simulation.calculation.BaseCalculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_fleur_n_occupied_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')
