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
    Reference,
    JSON,
)

from . import abinit_autogenerated
import runschema.run  # pylint: disable=unused-import
import runschema.calculation  # pylint: disable=unused-import
import runschema.method  # pylint: disable=unused-import
import runschema.system  # pylint: disable=unused-import


m_package = Package()


class x_abinit_section_stress_tensor(MSection):
    """
    Section describing the stress tensor
    """

    m_def = Section(validate=False)

    x_abinit_stress_tensor_xx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        xx component of the stress tensor
        """,
    )

    x_abinit_stress_tensor_yy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        yy component of the stress tensor
        """,
    )

    x_abinit_stress_tensor_zz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        zz component of the stress tensor
        """,
    )

    x_abinit_stress_tensor_zy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        zy component of the stress tensor
        """,
    )

    x_abinit_stress_tensor_zx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        zx component of the stress tensor
        """,
    )

    x_abinit_stress_tensor_yx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        yx component of the stress tensor
        """,
    )


class x_abinit_section_dataset_header(MSection):
    """
    -
    """

    m_def = Section(validate=False)

    x_abinit_dataset_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Dataset number
        """,
    )

    x_abinit_vprim_1 = Quantity(
        type=str,
        shape=[],
        description="""
        Primitive axis 1
        """,
    )

    x_abinit_vprim_2 = Quantity(
        type=str,
        shape=[],
        description="""
        Primitive axis 2
        """,
    )

    x_abinit_vprim_3 = Quantity(
        type=str,
        shape=[],
        description="""
        Primitive axis 3
        """,
    )


class x_abinit_section_var(MSection):
    """
    -
    """

    m_def = Section(validate=False)

    x_abinit_vardtset = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        Variable dataset number
        """,
    )

    x_abinit_varname = Quantity(
        type=str,
        shape=[],
        description="""
        Variable name
        """,
    )

    x_abinit_varvalue = Quantity(
        type=str,
        shape=[],
        description="""
        Variable value
        """,
    )

    x_abinit_vartruncation = Quantity(
        type=str,
        shape=[],
        description="""
        Variable truncation length
        """,
    )


class Run(runschema.run.Run):
    m_def = Section(validate=False, extends_base_section=True)

    x_abinit_parallel_compilation = Quantity(
        type=str,
        shape=[],
        description="""
        Parallel or sequential compilation
        """,
    )

    x_abinit_start_date = Quantity(
        type=str,
        shape=[],
        description="""
        Start date as string
        """,
    )

    x_abinit_start_time = Quantity(
        type=str,
        shape=[],
        description="""
        Start time as string
        """,
    )

    x_abinit_input_file = Quantity(
        type=str,
        shape=[],
        description="""
        Input file name
        """,
    )

    x_abinit_output_file = Quantity(
        type=str,
        shape=[],
        description="""
        Output file name
        """,
    )

    x_abinit_input_files_root = Quantity(
        type=str,
        shape=[],
        description="""
        Root for input files
        """,
    )

    x_abinit_output_files_root = Quantity(
        type=str,
        shape=[],
        description="""
        Root for output files
        """,
    )

    x_abinit_total_cpu_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Total CPU time
        """,
    )

    x_abinit_total_wallclock_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Total wallclock time
        """,
    )

    x_abinit_completed = Quantity(
        type=str,
        shape=[],
        description="""
        Message that the calculation was completed
        """,
    )

    x_abinit_section_var = SubSection(
        sub_section=x_abinit_section_var.m_def, repeats=True
    )


class Method(runschema.method.Method):
    m_def = Section(validate=False, extends_base_section=True)

    x_abinit_tolvrs = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        `TOLerance on the potential V(r) ReSidual`:
        Sets a tolerance for potential residual that, when reached, will cause
        one SCF cycle to stop (and ions to be moved). If set to zero, this
        stopping condition is ignored. Instead, refer to other tolerances, such
        as toldfe, tolwfr.
        """,
    )

    x_abinit_tolwfr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        TOLerance on WaveFunction squared Residual:
        Specifies the threshold on WaveFunction squared Residuals;
        it gives a convergence tolerance for the largest squared residual
        for any given band.
        """,
    )

    x_abinit_istwfk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
         Integer for choice of STorage of WaveFunction at each k point;
        Controls the way the wavefunction for each k-point is stored inside ABINIT,
        in reciprocal space, according to time-reversal symmetry properties.
        """,
    )

    x_abinit_iscf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description="""
        ABINIT variable Integer for Self-Consistent-Field cycles
        """,
    )


class System(runschema.system.System):
    m_def = Section(validate=False, extends_base_section=True)

    x_abinit_atom_xcart_final = Quantity(
        type=str,
        shape=[],
        description="""
        Cartesian coordinates of an atom at the end of the dataset
        """,
    )

    x_abinit_atom_xcart = Quantity(
        type=str,
        shape=[],
        description="""
        Cartesian coordinates of an atom at the end of a single configuration calculation
        """,
    )


class x_abinit_mesh(MSection):
    """
    Section containing the parameters for a mesh.
    """

    m_def = Section(validate=False)

    x_abinit_type = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_abinit_n_mesh = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_mesh = Quantity(
        type=np.float64,
        shape=['x_abinit_n_mesh', 3],
        description="""
        """,
    )


class x_abinit_chi_q_data(MSection):
    """
    Section containing the parameters for chi_q.
    """

    m_def = Section(validate=False)

    x_abinit_q_point = Quantity(
        type=np.float64,
        shape=['x_abinit_n_mesh', 3],
        description="""
        """,
    )

    x_abinit_av_fulfillment = Quantity(
        type=np.float64,
        shape=['x_abinit_n_mesh'],
        description="""
        """,
    )


class x_abinit_screening_dataset(MSection):
    """
    Section containing the outputs of the screening dataset.
    """

    m_def = Section(validate=False)

    x_abinit_precision_algorithm = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_kqmesh = SubSection(sub_section=x_abinit_mesh.m_def, repeats=True)

    x_abinit_n_fftmesh = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_fftmesh = Quantity(
        type=np.int32,
        shape=[3],
        description="""
        """,
    )

    x_abinit_symm_screening = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_abinit_n_bands_per_proc = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_n_bands_per_node = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_n_electrons = Quantity(
        type=np.float64,
        shape=[3],
        description="""
        """,
    )

    x_abinit_wigner_seitz_radius = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_omega_plasma = Quantity(
        type=np.float64,
        shape=[],
        unit='electron_volt',
        description="""
        """,
    )

    x_abinit_static_diel_const = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_static_diel_const_nofields = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_static_max_band_occ = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_chi_q = SubSection(sub_section=x_abinit_chi_q_data.m_def, repeats=False)

    x_abinit_frequencies = Quantity(
        type=np.float64,
        shape=['*', 2],
        description="""
        """,
    )


class x_abinit_ks_band_gaps_params(MSection):
    """
    Section containing the parameters for the KS band gaps.
    """

    m_def = Section(validate=False)

    x_abinit_min_direct_gap = Quantity(
        type=np.float64,
        shape=[4],
        description="""
        """,
    )

    x_abinit_fundamental_gap = Quantity(
        type=np.float64,
        shape=[],
        unit='electron_volt',
        description="""
        """,
    )

    x_abinit_k_top_valence_band = Quantity(
        type=np.float64,
        shape=[3],
        description="""
        """,
    )

    x_abinit_k_bottom_conduction_band = Quantity(
        type=np.float64,
        shape=[3],
        description="""
        """,
    )


class x_abinit_qp_band_gaps_params(MSection):
    """
    Section containing the parameters for the QP band gaps.
    """

    m_def = Section(validate=False)

    x_abinit_value = Quantity(
        type=np.float64,
        shape=[],
        unit='electron_volt',
        description="""
        The Kohn-Sham gap
        """,
    )

    x_abinit_value_fundamental = Quantity(
        type=np.float64,
        shape=[],
        unit='electron_volt',
        description="""
        The Quasi-Particle gap
        """,
    )


class BandEnergies(runschema.calculation.BandEnergies):
    """
    Section exting the band energies to contain QP band gaps.
    Could be depricated later on, since it runs counter to the regular way of working.
    """

    m_def = Section(validate=False, extends_base_section=True)

    x_abinit_qp_band_gaps_params = SubSection(
        sub_section=x_abinit_qp_band_gaps_params.m_def, repeats=False
    )


class x_abinit_sigma_params(MSection):
    """
    Section containing the parameters for the SIGMA.
    """

    m_def = Section(validate=False)

    x_abinit_model = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_abinit_params = Quantity(
        type=JSON,
        description="""
        """,
    )

    x_abinit_freq_step = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_max_omega_sigma = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_zcut_avoid = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )


class x_abinit_epsilon_inv_params(MSection):
    """
    Section containing the parameters for the EPSILON^-1.
    """

    m_def = Section(validate=False)

    x_abinit_dimensions = Quantity(
        type=JSON,
        description="""
        """,
    )

    x_abinit_params = Quantity(
        type=JSON,
        description="""
        """,
    )


class x_abinit_gw_dataset(MSection):
    """
    Section containing the outputs of the gw dataset.
    """

    m_def = Section(validate=False)

    x_abinit_precision_algorithm = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_kqmesh = SubSection(sub_section=x_abinit_mesh.m_def, repeats=True)

    x_abinit_n_fftmesh = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_fftmesh = Quantity(
        type=np.int32,
        shape=[3],
        description="""
        """,
    )

    x_abinit_symm_screening = Quantity(
        type=str,
        shape=[],
        description="""
        """,
    )

    x_abinit_n_bands_per_proc = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_n_bands_per_node = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_n_electrons = Quantity(
        type=np.float64,
        shape=[3],
        description="""
        """,
    )

    x_abinit_wigner_seitz_radius = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_omega_plasma = Quantity(
        type=np.float64,
        shape=[],
        unit='electron_volt',
        description="""
        """,
    )

    x_abinit_static_diel_const = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_static_diel_const_nofields = Quantity(
        type=np.float64,
        shape=[],
        description="""
        """,
    )

    x_abinit_static_max_band_occ = Quantity(
        type=np.int32,
        shape=[],
        description="""
        """,
    )

    x_abinit_ks_band_gaps = SubSection(
        sub_section=x_abinit_ks_band_gaps_params.m_def, repeats=True
    )

    x_abinit_sigma = SubSection(sub_section=x_abinit_sigma_params.m_def, repeats=True)

    x_abinit_epsilon_inv = SubSection(
        sub_section=x_abinit_epsilon_inv_params.m_def, repeats=True
    )


class Calculation(runschema.calculation.Calculation):
    m_def = Section(validate=False, extends_base_section=True)

    x_abinit_magnetisation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Total magnetisation.
        """,
    )

    x_abinit_fermi_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Fermi energy.
        """,
    )

    x_abinit_single_configuration_calculation_converged = Quantity(
        type=str,
        shape=[],
        description="""
        Determines whether a single configuration calculation is converged.
        """,
    )

    x_abinit_atom_force = Quantity(
        type=str,
        shape=[],
        description="""
        Force acting on an atom at the end of a single configuration calculation
        """,
    )

    x_abinit_atom_force_final = Quantity(
        type=np.dtype(np.float64),
        unit='newton',
        shape=[],
        description="""
        Force acting on an atom at the end of the dataset
        """,
    )

    x_abinit_energy_ewald = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Ewald energy
        """,
    )

    x_abinit_energy_psp_core = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Pseudopotential core energy
        """,
    )

    x_abinit_energy_psp_local = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Local pseudopotential energy
        """,
    )

    x_abinit_energy_psp_nonlocal = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Non-local pseudopotential energy
        """,
    )

    x_abinit_energy_internal = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Internal energy
        """,
    )

    x_abinit_energy_ktentropy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        -kT*entropy
        """,
    )

    x_abinit_energy_band = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description="""
        Band energy
        """,
    )

    x_abinit_section_stress_tensor = SubSection(
        sub_section=x_abinit_section_stress_tensor.m_def, repeats=True
    )

    x_abinit_unit_cell_volume = Quantity(
        type=np.dtype(np.float64),
        unit='meter**3',
        shape=[],
        description="""
        Unit cell volume
        """,
    )

    x_abinit_screening = SubSection(
        sub_section=x_abinit_screening_dataset.m_def, repeats=True
    )

    x_abinit_gw = SubSection(sub_section=x_abinit_gw_dataset.m_def, repeats=True)


class x_abinit_section_dataset(abinit_autogenerated.x_abinit_section_dataset):
    m_def = Section(validate=False, extends_base_section=True)

    x_abinit_geometry_optimization_converged = Quantity(
        type=str,
        shape=[],
        description="""
        Determines whether a geometry optimization is converged.
        """,
    )

    x_abinit_eig_filename = Quantity(
        type=str,
        shape=[],
        description="""
        Name of file where the eigenvalues were written to.
        """,
    )

    x_abinit_section_dataset_header = SubSection(
        sub_section=x_abinit_section_dataset_header.m_def, repeats=True
    )
