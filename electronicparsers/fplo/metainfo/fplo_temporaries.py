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


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_t_program_version_main = Quantity(
        type=str,
        shape=[],
        description='''
        temporary: FPLO main version
        ''')

    x_fplo_t_program_version_release = Quantity(
        type=str,
        shape=[],
        description='''
        temporary: FPLO release number
        ''')

    x_fplo_t_run_hosts = Quantity(
        type=str,
        shape=[],
        description='''
        temporary: FPLO run hosts
        ''')


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_t_vec_a_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for direct lattice vectors, x-component
        ''')

    x_fplo_t_vec_a_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for direct lattice vectors, y-component
        ''')

    x_fplo_t_vec_a_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for direct lattice vectors, z-component
        ''')

    x_fplo_t_vec_b_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for reciprocal lattice vectors, x-component
        ''')

    x_fplo_t_vec_b_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for reciprocal lattice vectors, y-component
        ''')

    x_fplo_t_vec_b_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for reciprocal lattice vectors, z-component
        ''')

    x_fplo_t_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for atom positions, x-component
        ''')

    x_fplo_t_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for atom positions, y-component
        ''')

    x_fplo_t_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for atom positions, z-component
        ''')

    x_fplo_t_atom_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO atom index
        ''')

    x_fplo_t_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for FPLO atom labels
        ''')

    x_fplo_t_atom_wyckoff_idx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO Wyckoff position index of each atom
        ''')

    x_fplo_t_atom_cpa_block = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO CPA block of each atom
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_t_relativity_method = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for FPLO relativistic method
        ''')

    x_fplo_t_dft_plus_u_species_subshell_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U species
        ''')

    x_fplo_t_dft_plus_u_species_subshell_element = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U element
        ''')

    x_fplo_t_dft_plus_u_species_subshell_subshell = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U (n,l)subshell
        ''')

    x_fplo_t_dft_plus_u_species_subshell_F0 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U F0
        ''')

    x_fplo_t_dft_plus_u_species_subshell_F2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U F2
        ''')

    x_fplo_t_dft_plus_u_species_subshell_F4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U F4
        ''')

    x_fplo_t_dft_plus_u_species_subshell_F6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U F6
        ''')

    x_fplo_t_dft_plus_u_species_subshell_U = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U U
        ''')

    x_fplo_t_dft_plus_u_species_subshell_J = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for FPLO per species/(n,l)subshell DFT+U J
        ''')

    x_fplo_t_dft_plus_u_site_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO per site DFT+U index
        ''')

    x_fplo_t_dft_plus_u_site_element = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for FPLO per site DFT+U element
        ''')

    x_fplo_t_dft_plus_u_site_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO per site DFT+U species
        ''')

    x_fplo_t_dft_plus_u_site_subshell = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for FPLO per site DFT+U (n,l)subshell
        ''')

    x_fplo_t_dft_plus_u_site_ubi1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO per site DFT+U ubi1
        ''')

    x_fplo_t_dft_plus_u_site_ubi2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage for FPLO per site DFT+U ubi2
        ''')


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_fplo_t_energy_reference_fermi_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Temporary storage for FPLO Fermi energy in iteration
        ''')
