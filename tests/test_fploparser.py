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
from electronicparsers.fplo import FploParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return FploParser()


def test_basic(parser):
    archive = EntryArchive()

    parser.parse('tests/data/fplo/hcp_ti/out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '14.00 M-CPA 47'

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.lattice_vectors[0][1].magnitude == approx(-1.475e-10)
    assert sec_system.atoms.labels == ['Ti', 'Ti']
    assert sec_system.atoms.positions[1][2].magnitude == approx(-1.17e-10)

    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 14
    assert sec_sccs[5].energy.total.value.magnitude == approx(-2.73593178e-16)
    assert sec_sccs[8].energy.fermi.magnitude == approx(-2.47707723e-20)


def test_1(parser):
    archive = EntryArchive()

    parser.parse('tests/data/fplo/dhcp_gd/out', archive, None)

    assert len(archive.run[0].system[0].atoms.positions) == 4
