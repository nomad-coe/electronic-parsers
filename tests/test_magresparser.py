#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
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

import pytest
import numpy as np

from nomad.datamodel import EntryArchive
from electronicparsers.magres import MagresParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return MagresParser()


def test_single_point_ethanol(parser):
    archive = EntryArchive()
    parser.parse('tests/data/magres/ethanol_nmr.magres', archive, None)
    sec_run = archive.run[-1]

    # Program testing
    assert sec_run.program.name == 'CASTEP'
    assert sec_run.program.version == '24.1'

    # System testing
    assert len(sec_run.system) == 1
    sec_system = sec_run.system[-1]
    assert sec_system.atoms.labels == ['H', 'H', 'H', 'H', 'H', 'H', 'C', 'C', 'O']
    assert sec_system.atoms.positions[0][1].magnitude == approx(4.3583475749937473e-10)

    # Method testing
    assert len(sec_run.method) == 1
    sec_method = sec_run.method[-1]
    assert sec_method.label == 'NMR'
    assert sec_method.dft.xc_functional.exchange[-1].name == 'LDA_X_PZ'
    assert sec_method.dft.xc_functional.correlation[-1].name == 'LDA_C_PZ'
    assert (sec_method.k_mesh.grid == np.array([1, 1, 1])).all()
    assert sec_method.electrons_representation[-1].type == 'plane waves'

    # Calculation testing
    assert len(sec_run.calculation) == 1
    sec_calc = sec_run.calculation[-1]
    assert sec_calc.system_ref == sec_system
    assert sec_calc.method_ref == sec_method
    assert sec_calc.magnetic_shielding and sec_calc.electric_field_gradient
    assert not sec_calc.spin_spin_coupling and not sec_calc.magnetic_susceptibility
    # Magnetic shielding testing
    assert len(sec_calc.magnetic_shielding) == 1
    sec_ms = sec_calc.magnetic_shielding[-1]
    assert sec_ms.atoms.shape == (9, 2)
    assert (sec_ms.atoms[3] == ['H', '4']).all()
    assert sec_ms.value.shape == (9, 3, 3)
    assert sec_ms.value[4][2][1] == approx(-8.661757088509511e-06)
    assert sec_ms.isotropic_value.shape == (9,)
    assert sec_ms.isotropic_value[4] == approx(3.035708828276491e-05)
    # Electric field gradient testing
    assert len(sec_calc.electric_field_gradient) == 1
    sec_efg = sec_calc.electric_field_gradient[-1]
    assert sec_efg.contribution == 'total'
    assert sec_efg.value.shape == sec_ms.value.shape
    assert sec_efg.value[4][2][1].magnitude == approx(-3.0317252106856217e21)
