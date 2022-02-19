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


class x_gpaw_section_paw_method(MSection):
    '''
    GPAW PAW specific information
    '''

    m_def = Section(validate=False)

    x_gpaw_number_of_packed_ap_elements = Quantity(
        type=int,
        shape=[],
        description='''
        number of PAW projector matrix elements in packed format
        ''')

    x_gpaw_number_of_projectors = Quantity(
        type=int,
        shape=[],
        description='''
        number of PAW projectors
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_gpaw_atomic_density_matrices = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_spin_channels', 'x_gpaw_number_of_packed_ap_elements'],
        description='''
        atomic density matrices in the PAW formalism
        ''')

    x_gpaw_fixed_spin_Sz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Target value (fixed) of the z projection of the spin moment operator $S^z$ for the
        converged calculation with the XC_method.
        ''')

    x_gpaw_magnetic_moments = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Magnetic moments projected onto atoms. The sum gives the total magnetic moment
        ''')

    x_gpaw_projections_imag = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_spin_channels', 'number_of_eigenvalues_kpoints', 'number_of_eigenvalues', 'x_gpaw_number_of_projectors'],
        description='''
        projections in the PAW formalism (imaginary part)
        ''')

    x_gpaw_projections_real = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_spin_channels', 'number_of_eigenvalues_kpoints', 'number_of_eigenvalues', 'x_gpaw_number_of_projectors'],
        description='''
        projections in the PAW formalism (real part)
        ''')

    x_gpaw_spin_Sz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Value of the z projection of the spin moment operator $S^z$ for the converged
        calculation with the XC_method.
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_gpaw_density_convergence_criterion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Density convergence criteria for break the SCF cycle
        ''')

    x_gpaw_fix_density = Quantity(
        type=bool,
        shape=[],
        description='''
        Was it a calculation with a fixed density?
        ''')

    x_gpaw_fix_magnetic_moment = Quantity(
        type=bool,
        shape=[],
        description='''
        Was the magnetic moment fixed? If yes the x_gpaw_fixed_sZ is set
        ''')

    x_gpaw_maximum_angular_momentum = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maxium angular momentum (L) for projectors
        ''')

    x_gpaw_mix_beta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Damping parameter in the density mixer
        ''')

    x_gpaw_mix_class = Quantity(
        type=str,
        shape=[],
        description='''
        The density mixer class name (Mixer, MixerSum, MixerDiff)
        ''')

    x_gpaw_mix_old = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of old densities in the density mixer
        ''')

    x_gpaw_mix_weight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mixing weight in density mixer
        ''')

    x_gpaw_symmetry_time_reversal_switch = Quantity(
        type=bool,
        shape=[],
        description='''
        Was time reserval symmetry used
        ''')

    x_gpaw_xc_functional = Quantity(
        type=str,
        shape=[],
        description='''
        The XC functional name used in gpaw as input
        ''')

    x_gpaw_section_paw_method = SubSection(
        sub_section=SectionProxy('x_gpaw_section_paw_method'),
        repeats=True)
