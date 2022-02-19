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
from electronicparsers.dmol3 import Dmol3Parser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return Dmol3Parser()


def test_basic(parser):
    archive = EntryArchive()

    parser.parse('tests/data/dmol3/h2o.outmol', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == 'version 3.0'

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 11
    assert sec_systems[0].atoms.labels[2] == 'H'
    assert sec_systems[2].atoms.positions[1][2].magnitude == approx(-8.84266338e-10,)

    sec_sccs = sec_run.calculation
    assert sec_sccs[7].energy.total.value.magnitude == approx(-3.33238073e-16)
