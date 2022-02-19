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
from electronicparsers.cpmd import CPMDParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return CPMDParser()


def test_single_point(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cpmd/single_point/output.out', archive, None)

    assert archive.run[0].program.version == '4.1-rUnversioned directory'

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels == ['H', 'H']
    assert sec_system.atoms.positions[1][2].magnitude == approx(3.99999974e-10)
    assert sec_system.atoms.lattice_vectors[2][2].magnitude == approx(7.99999524e-10)

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-4.78219396e-18)
    assert sec_scc.energy.xc.value.magnitude == approx(-2.50324989e-18)


def test_geometry_optimization(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cpmd/geo_opt/output.out', archive, None)

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 8
    assert sec_systems[2].atoms.positions[0][1].magnitude == approx(3.99999762e-10)

    sec_sccs = archive.run[0].calculation
    assert sec_sccs[2].energy.total.value.magnitude == approx(-4.93913736e-18)
    assert sec_sccs[1].energy.electrostatic.value.magnitude == approx(-2.14706759e-18)


def test_molecular_dynamics(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cpmd/md/output.out', archive, None)

    assert archive.run[0].system[1].atoms.positions[1][0].magnitude == approx(-3.70999792e-11)
