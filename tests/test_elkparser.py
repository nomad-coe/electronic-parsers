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


def test_1(parser):
    archive = EntryArchive()

    parser.parse('tests/data/elk/Al/INFO.OUT', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '4.0.15'

    sec_method = sec_run.method[0]
    assert sec_method.dft.xc_functional.exchange[0].name == 'LDA_X_PZ'
    assert sec_method.electronic.smearing.kind == 'fermi'
    assert sec_method.electronic.smearing.width == approx(0.001)
    assert sec_method.x_elk_kpoints_grid[2] == 4
    assert sec_method.x_elk_gkmax.magnitude == approx(6.01276494e10)

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.lattice_vectors[1][0].magnitude == approx(2.02500243e-10)
    assert sec_system.atoms.labels == ['Al']
    assert sec_system.atoms.positions[0][1].magnitude == 0.0

    sec_calc = sec_run.calculation[0]
    assert len(sec_calc.scf_iteration) == 19
    assert sec_calc.scf_iteration[2].energy.total.value.magnitude == approx(
        -1.05555622e-15
    )
    assert sec_calc.scf_iteration[7].energy.fermi.magnitude == approx(1.13675091e-18)
    assert sec_calc.scf_iteration[12].energy.exchange.value.magnitude == approx(
        -7.28319203e-17
    )
    assert sec_calc.scf_iteration[3].energy.electronic.kinetic.magnitude == approx(
        1.05431941e-15
    )
    assert sec_calc.scf_iteration[5].energy.sum_eigenvalues.value.magnitude == approx(
        -5.63620032e-16
    )
    assert sec_calc.scf_iteration[8].energy.xc.potential.magnitude == approx(
        -1.018882e-16
    )
    assert sec_calc.scf_iteration[
        9
    ].energy.x_elk_core_electron_kinetic_energy.magnitude == approx(7.83218672e-16)
    assert sec_calc.scf_iteration[11].energy.electrostatic.value.magnitude == approx(
        -2.03299947e-15
    )
    assert sec_calc.scf_iteration[
        13
    ].energy.electrostatic.potential.magnitude == approx(-1.5165141e-15)
    assert sec_calc.scf_iteration[15].energy.x_elk_hartree_energy.magnitude == approx(
        3.32138956e-16
    )
    assert sec_calc.scf_iteration[17].energy.madelung.value.magnitude == approx(
        -1.27473913e-15
    )
    assert sec_calc.scf_iteration[
        18
    ].energy.x_elk_electron_entropic_energy.magnitude == approx(-1.13486501e-21)
    assert sec_calc.scf_iteration[0].energy.correlation.value.magnitude == approx(
        -4.30831902e-18
    )


def test_2(parser):
    archive = EntryArchive()

    parser.parse('tests/data/elk/GaAs/INFO.OUT', archive, None)

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels == ['Ga', 'As']
    assert sec_system.atoms.positions[1][2].magnitude == approx(1.41382921e-10)

    sec_calc = archive.run[0].calculation[0]
    assert len(sec_calc.scf_iteration) == 20
    assert sec_calc.scf_iteration[6].charges[0].value[1].magnitude == approx(
        5.01086463e-18
    )
    assert sec_calc.scf_iteration[13].charges[0].total.magnitude == approx(
        1.02539305e-17
    )
    assert sec_calc.eigenvalues[0].kpoints[17][2] == approx(0.6250000000)
    assert sec_calc.eigenvalues[0].energies[0][13][5].magnitude == approx(
        -1.6048802e-18
    )
    assert sec_calc.eigenvalues[0].occupancies[0][2][13] == approx(2.0)
    assert sec_calc.dos_electronic[0].energies[87].magnitude == approx(-1.42127678e-18)
    assert sec_calc.dos_electronic[0].total[0].value[49].magnitude == approx(
        1.26640442e19
    )
