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
from nomad.datamodel.metainfo.simulation import run                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, Reference, JSON
)

from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_yambo_io(MSection):
    m_def = Section(validate=False)

    x_yambo_parameters = Quantity(
        type=JSON,
        shape=[],
        description='''
        ''')

    x_yambo_file = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_sn = Quantity(
        type=str,
        shape=[],
        description='''
        ''')


class x_yambo_parameters(MSection):
    m_def = Section(validate=False)

    x_yambo_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_k_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_g_vectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_components = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_symmetries = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_spinor_components = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_spin_polarization = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_yambo_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_yambo_wf_g_vectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_max_atoms_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_n_atom_species = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_exact_exchange_fraction_in_xc = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_yambo_exact_exchange_screening_in_xc = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_yambo_magnetic_symmetries = Quantity(
        type=str,
        shape=[],
        description='''
        ''')


class Program(simulation.run.Program):
    m_def = Section(validate=False, extends_base_section=True)

    x_yambo_build = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_hash = Quantity(
        type=str,
        shape=[],
        description='''
        ''')


class Run(simulation.run.Run):
    m_def = Section(validate=False, extends_base_section=True)

    x_yambo_job_string = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_cpu = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_threads = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_threads_tot = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_io_nodes = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_fragmented_io = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_yambo_fragmented_wfs = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_yambo_core_databases = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_additional_io = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_communications = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_input_file = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_report_file = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_verbose_log_report = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_yambo_precision = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_log_files = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_yambo_input = SubSection(sub_section=x_yambo_io.m_def, repeats=False)


class x_yambo_local_xc_nonlocal_fock_bandenergies(simulation.calculation.BandEnergies):
    m_def = Section(validate=False)

    x_yambo_sx = Quantity(
        type=np.dtype(np.float64),
        shape=['n_spin_channels', 'n_kpoints', 'n_bands'],
        unit='joule',
        description='''
        ''')

    x_yambo_vxc = Quantity(
        type=np.dtype(np.float64),
        shape=['n_spin_channels', 'n_kpoints', 'n_bands'],
        unit='joule',
        description='''
        ''')


class x_yambo_bare_xc_bandenergies(simulation.calculation.BandEnergies):
    m_def = Section(validate=False)

    x_yambo_dft = Quantity(
        type=np.dtype(np.float64),
        shape=['n_spin_channels', 'n_kpoints', 'n_bands'],
        unit='joule',
        description='''
        ''')

    x_yambo_hf = Quantity(
        type=np.dtype(np.float64),
        shape=['n_spin_channels', 'n_kpoints', 'n_bands'],
        unit='joule',
        description='''
        ''')


class Calculation(simulation.calculation.Calculation):
    m_def = Section(validate=False, extends_base_section=True)

    x_yambo_electronic_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        ''')

    x_yambo_bosonic_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='kelvin',
        description='''
        ''')

    x_yambo_finite_temperature_mode = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_yambo_electronic_density = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        # unit='1/cm**3',
        description='''
        ''')

    x_yambo_filled_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ''')

    x_yambo_empty_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ''')

    x_yambo_indirect_gaps = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        unit='joule',
        description='''
        ''')

    x_yambo_direct_gaps = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        unit='joule',
        description='''
        ''')

    x_yambo_indirect_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_yambo_direct_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        ''')

    x_yambo_direct_gap_k_point = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_indirect_gap_k_points = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ''')

    x_yambo_local_xc_nonlocal_fock_bandenergies = SubSection(sub_section=x_yambo_local_xc_nonlocal_fock_bandenergies.m_def, repeats=True)

    x_yambo_bare_xc_bandenergies = SubSection(sub_section=x_yambo_bare_xc_bandenergies.m_def, repeats=True)


class x_yambo_dynamic_dielectric_matrix_fragment(MSection):
    m_def = Section(validate=False)

    x_yambo_FREQ_PARS_sec_iq = Quantity(
        type=np.dtype(np.float64),
        shape=[1],
        description='''
        ''')

    x_yambo_FREQ_sec_iq = Quantity(
        type=np.dtype(np.float64),
        shape=[2, 2],
        description='''
        ''')

    x_yambo_matrix_size = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_X_Q = Quantity(
        type=np.dtype(np.float64),
        shape=[2, 'x_yambo_matrix_size', 'x_yambo_matrix_size', 2],
        description='''
        ''')


class x_yambo_module(MSection):
    m_def = Section(validate=False)

    x_yambo_mesh_size = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ''')

    x_yambo_input = SubSection(sub_section=x_yambo_io.m_def, repeats=True)

    x_yambo_output = SubSection(sub_section=x_yambo_io.m_def, repeats=True)


class x_yambo_dynamic_dielectric_matrix(x_yambo_module):
    m_def = Section(validate=False)

    x_yambo_fragment = SubSection(sub_section=x_yambo_dynamic_dielectric_matrix_fragment.m_def, repeats=True)


class x_yambo_local_xc_nonlocal_fock(x_yambo_module):
    m_def = Section(validate=False)

    x_yambo_plane_waves_vxc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_yambo_plane_waves_exs = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')


class x_yambo_bare_xc(x_yambo_module):
    m_def = Section(validate=False)

    x_yambo_plane_waves_exs = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')


class x_yambo_dipoles(x_yambo_module):
    m_def = Section(validate=False)


class x_yambo_dyson(x_yambo_module):
    m_def = Section(validate=False)

    x_yambo_bands_range = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ''')

    x_yambo_g_damping = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')


class x_yambo_transferred_momenta(x_yambo_module):
    m_def = Section(validate=False)


class Method(simulation.method.Method):
    m_def = Section(validate=False, extends_base_section=True)

    x_yambo_transferred_momenta = SubSection(sub_section=x_yambo_transferred_momenta.m_def, repeats=True)

    x_yambo_dynamic_dielectric_matrix = SubSection(sub_section=x_yambo_dynamic_dielectric_matrix.m_def, repeats=True)

    x_yambo_local_xc_nonlocal_fock = SubSection(sub_section=x_yambo_local_xc_nonlocal_fock.m_def, repeats=True)

    x_yambo_bare_xc = SubSection(sub_section=x_yambo_bare_xc.m_def, repeats=True)

    x_yambo_dipoles = SubSection(sub_section=x_yambo_dipoles.m_def, repeats=True)

    x_yambo_dyson = SubSection(sub_section=x_yambo_dyson.m_def, repeats=True)
