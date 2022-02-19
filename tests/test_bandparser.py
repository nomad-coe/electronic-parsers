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
from electronicparsers.band import BandParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return BandParser()


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/band/phenylrSmall-metagga.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '70630 2018-11-24'
    assert sec_run.time_run.date_start.magnitude == 1550053118.0

    sec_method = archive.run[0].method[0]
    assert sec_method.electronic.n_spin_channels == 2
    assert sec_method.dft.xc_functional.contributions[0].name == 'MGGA_XC_TPSS'

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.positions[2][1].magnitude == approx(2.31103866e-10)
    assert sec_system.atoms.lattice_vectors[0][0].magnitude == approx(8.72113987e-10)
    assert sec_system.atoms.periodic == [True, True, False]

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-1.11415974e-17)
    assert sec_scc.energy.kinetic_electronic.value.magnitude == approx(1.11552116e-17)
    assert sec_scc.energy.xc.value.magnitude == approx(-1.01588269e-17)
    assert sec_scc.energy.electrostatic.value.magnitude == approx(-8.69562185e-18)

    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 20
    assert sec_scfs[11].energy.change.magnitude == approx(2.1449944e-21)


def test_geometry_optimization(parser):
    archive = EntryArchive()
    parser.parse('tests/data/band/phenylrSmall-geoopt.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 22
    assert sec_sccs[17].energy.total.value.magnitude == approx(-1.10701399e-17)
    assert len(sec_sccs[6].scf_iteration) == 11
    assert sec_sccs[10].forces.total.value[5][1].magnitude == approx(3.11423748e-11)

    sec_systems = archive.run[0].system
    assert sec_systems[3].atoms.positions[10][1].magnitude == approx(5.81904209e-10)
    assert sec_systems[9].atoms.lattice_vectors[1][1].magnitude == approx(7.56032016e-10)


def test_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/band/NiO-dos.out', archive, None)

    sec_dos = archive.run[0].calculation[0].dos_electronic[0]
    assert np.shape(sec_dos.total[1].value) == (158,)
    assert sec_dos.energies[78].magnitude == approx(-8.6717613e-20)
    assert sec_dos.total[1].value[19].magnitude == approx(4.66493971e+14)

    archive = EntryArchive()
    parser.parse('tests/data/band/NiO-dos-restricted.out', archive, None)
    sec_dos = archive.run[0].calculation[0].dos_electronic[0]
    assert np.shape(sec_dos.total[0].value) == (154,)
