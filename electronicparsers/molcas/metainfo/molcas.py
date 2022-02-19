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


class x_molcas_section_frequency(MSection):
    '''
    Section for Molcas frequency (symmetry, frequency, intensity)
    '''

    m_def = Section(validate=False)

    x_molcas_frequency_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Molcas frequency value
        ''')

    x_molcas_imaginary_frequency_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Molcas imaginary frequency value
        ''')

    x_molcas_frequency_intensity = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Molcas intensity value
        ''')

    x_molcas_frequency_symmetry = Quantity(
        type=str,
        shape=[],
        description='''
        Molcas symmetry for frequencies
        ''')


class x_molcas_section_basis(MSection):
    '''
    Section for Molcas basis sets
    '''

    m_def = Section(validate=False)

    x_molcas_basis_atom_label = Quantity(
        type=str,
        shape=[],
        description='''
        Molcas basis set atom label.
        ''')

    x_molcas_basis_name = Quantity(
        type=str,
        shape=[],
        description='''
        Molcas basis set name.  Repeated strings of '.' are compressed to a single '.'.
        Any leading or trailing '.' are stripped.
        ''')


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_molcas_method_name = Quantity(
        type=str,
        shape=[],
        description='''
        Molcas method name (without UHF; see x_molcas_uhf)
        ''')

    x_molcas_uhf = Quantity(
        type=bool,
        shape=[],
        description='''
        If the Molcas method is UHF.
        ''')

    x_molcas_section_basis = SubSection(
        sub_section=SectionProxy('x_molcas_section_basis'),
        repeats=True)


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_molcas_slapaf_grad_norm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Molcas slapaf (geometry optimization) grad (force) norm
        ''')

    x_molcas_slapaf_grad_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Molcas slapaf (geometry optimization) grad (force) max
        ''')

    x_molcas_section_frequency = SubSection(
        sub_section=SectionProxy('x_molcas_section_frequency'),
        repeats=True)
