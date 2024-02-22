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
from electronicparsers.mopac import MopacParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return MopacParser()


def test_spin_pol(parser):
    archive = EntryArchive()

    parser.parse('tests/data/mopac/O2.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '15.347L'
    assert sec_run.time_run.date_start > 0

    sec_method = sec_run.method[0]
    sec_method.x_mopac_method == 'PM7'
    assert 'TRIPLET' in sec_method.x_mopac_calculation_parameters

    sec_system = sec_run.system[0]
    assert sec_system.atoms.positions[0][1].magnitude == approx(3e-10)
    assert sec_system.atoms.labels == ['O', 'O']

    sec_calc = sec_run.calculation[0]
    assert sec_calc.energy.total.value.magnitude == approx(-9.40492697e-17)
    assert sec_calc.forces.total.value[1][2].magnitude == approx(
        -1.0555523514531733e-08
    )
    assert sec_calc.x_mopac_fhof.magnitude == approx(2.98139507e-21)
    assert sec_calc.energy.electronic.value.magnitude == approx(-1.48484844e-16)
    assert sec_calc.eigenvalues[0].energies[0][0][2].magnitude == approx(
        -2.92861066e-18
    )
    assert sec_calc.eigenvalues[0].energies[1][0][5].magnitude == approx(
        -3.26395424e-20
    )
    assert sec_calc.eigenvalues[0].occupations[0][0][7] == 0.0
    assert sec_calc.eigenvalues[0].occupations[1][0][4] == 1.0
    assert sec_calc.multipoles[0].dipole.total == 0.0
    assert sec_calc.charges[0].value[1].magnitude == approx(9.6130598e-19)
    assert sec_calc.charges[0].orbital_projected[3].value.magnitude == approx(
        1.64698951e-19
    )
    assert sec_calc.charges[0].orbital_projected[2].atom_index == 0
    assert sec_calc.charges[0].orbital_projected[5].atom_label == 'O'
    assert sec_calc.charges[0].orbital_projected[6].orbital == 'py'
    assert sec_calc.spin_S2 == approx(2.002364)
    assert sec_calc.time_calculation.magnitude == approx(0.008)
    assert sec_calc.time_physical.magnitude == approx(0.016)


def test_non_spin_pol(parser):
    archive = EntryArchive()

    parser.parse('tests/data/mopac/C6H6.out', archive, None)

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels[6] == 'H'

    sec_calc = archive.run[0].calculation[0]
    assert sec_calc.energy.total.value.magnitude == approx(-1.30987804e-16)
    assert sec_calc.eigenvalues[0].energies[0][0][4].magnitude == approx(
        -3.35031637e-18
    )
    assert sec_calc.eigenvalues[0].occupations[0][0][14] == 2.0
    assert sec_calc.charges[0].orbital_projected[24].orbital == 's'
    assert sec_calc.charges[0].orbital_projected[6].value.magnitude == approx(
        1.61840668e-19
    )
