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
    SectionProxy,
    Reference,
)

from runschema.calculation import (
    MagneticShielding as BaseMagneticShielding,
    ElectricFieldGradient as BaseElectricFieldGradient,
    SpinSpinCoupling as BaseSpinSpinCoupling,
)


m_package = Package()


class MagneticShielding(BaseMagneticShielding):
    """
    Section extensions for the Run.Calculation.MagneticShielding base section.
    """

    # ! These quantities should be implemented in `BaseMagneticShielding` as refs to the specific `AtomsState`

    m_def = Section(extends_base_section=True)

    atoms = Quantity(
        type=np.str_,
        shape=['n_atoms', 2],
        description="""
        Identifier for the atoms involved in the magnetic shielding tensor. This a list of
        `n_atoms` pairs of strings [atom_label, atom_index]. The atom index corresponds to the position
        on the list `System.atoms.labels`.
        """,
    )


class ElectricFieldGradient(BaseElectricFieldGradient):
    """
    Section extensions for the Run.Calculation.ElectricFieldGradient base section.
    """

    # ! These quantities should be implemented in `BaseElectricFieldGradient` as refs to the specific `AtomsState`

    m_def = Section(extends_base_section=True)

    atoms = Quantity(
        type=np.str_,
        shape=['n_atoms', 2],
        description="""
        Identifier for the atoms involved in the electric field gradient tensor. This a list of
        `n_atoms` pairs of strings [atom_label, atom_index]. The atom index corresponds to the position
        on the list `System.atoms.labels`.
        """,
    )


class SpinSpinCoupling(BaseSpinSpinCoupling):
    """
    Section extensions for the Run.Calculation.SpinspinCoupling base section.
    """

    # ! These quantities should be implemented in `BaseSpinSpinCoupling` as refs to the specific `AtomsState`g`

    m_def = Section(extends_base_section=True)

    atoms_1 = Quantity(
        type=np.str_,
        shape=['n_atoms', 2],
        description="""
        Identifier for the atoms involved in the spin-spin coupling J12 for the 1 atoms. This a list of
        `n_atoms` pairs of strings [atom_label, atom_index]. The atom index corresponds to the position
        on the list `System.atoms.labels`.
        """,
    )

    atoms_2 = Quantity(
        type=np.str_,
        shape=['n_atoms', 2],
        description="""
        Identifier for the atoms involved in the spin-spin coupling J12 for the 2 atoms. This a list of
        `n_atoms` pairs of strings [atom_label, atom_index]. The atom index corresponds to the position
        on the list `System.atoms.labels`.
        """,
    )
