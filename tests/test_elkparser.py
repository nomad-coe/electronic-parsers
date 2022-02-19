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

from nomad.datamodel import EntryArchive
from electronicparsers.elk import ElkParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return ElkParser()


def test_basic(parser):
    archive = EntryArchive()

    parser.parse('tests/data/elk/Al/INFO.OUT', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '4.0.15'

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.lattice_vectors[1][0].magnitude == approx(2.02500243e-10)
    assert sec_system.atoms.labels == ['Al']
    assert sec_system.atoms.positions[0][1].magnitude == 0.

    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 19
    assert sec_sccs[2].energy.total.value.magnitude == approx(-1.05555622e-15)
    assert sec_sccs[7].energy.fermi.magnitude == approx(1.13675091e-18)
    assert sec_sccs[12].energy.exchange.value.magnitude == approx(-7.28319203e-17)


def test_2(parser):
    archive = EntryArchive()

    parser.parse('tests/data/elk/GaAs/INFO.OUT', archive, None)

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels == ['Ga', 'As']
    assert sec_system.atoms.positions[1][2].magnitude == approx(1.41382921e-10)
