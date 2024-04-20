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
from electronicparsers.gamess import GamessParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return GamessParser()


def test_dft(parser):
    archive = EntryArchive()

    parser.parse('tests/data/gamess/dft/exam12.out', archive, None)

    sec_method = archive.run[0].method
    assert sec_method[0].dft.xc_functional.correlation[0].name == 'LDA_C_VWN_5'
    sec_basis_ac = (
        sec_method[0].electrons_representation[0].basis_set[0].atom_centered[0]
    )
    assert sec_basis_ac.formula == '6-31G(d)'
    assert sec_basis_ac.name == 'N31'

    sec_system = archive.run[0].system
    assert sec_system[2].atoms.labels == ['C', 'C', 'H', 'H']
    assert sec_system[-1].atoms.positions[2][2].magnitude == approx(-1.68393902e-10)

    sec_calc = archive.run[0].calculation
    assert len(sec_calc) == 6
    assert sec_calc[0].eigenvalues[0].energies[0][0][16].magnitude == approx(
        2.4780789e-18
    )
    assert sec_calc[5].charges[0].analysis_method == 'Mulliken'
    assert sec_calc[5].charges[1].value[1].magnitude == approx(-3.41098599e-20)
    assert sec_calc[5].energy.total.value.magnitude == approx(-3.33887277e-16)
    assert sec_calc[5].energy.total.potential.magnitude == approx(-6.65370978e-16)
    # assert sec_calc[5].energy.total.kinetic.magnitude == approx(3.31483701e-16)
    assert sec_calc[5].energy.x_gamess_two_electron.value.magnitude == approx(
        2.19797148e-16
    )
    assert sec_calc[5].energy.x_gamess_virial_ratio == approx(2.0072509638)
    assert len(sec_calc[5].energy.contributions) == 5
    assert sec_calc[5].energy.contributions[1].kind == 'nucleus-electron_potential'
    # assert sec_calc[5].multipoles[0].dipole.origin[1].magnitude == 0
    assert sec_calc[5].multipoles[0].dipole.value[2][0] == 0


def test_gamess_geometry_opt(parser):
    archive = EntryArchive()

    parser.parse('tests/data/gamess/gamessus/exam01.out', archive, None)

    sec_run = archive.run
    assert sec_run[0].program.version == '1 MAY 2013 (R1)'
    assert sec_run[0].x_gamess_program_implementation == '64 BIT INTEL VERSION'

    sec_method = sec_run[0].method
    assert len(sec_method) == 1
    assert sec_method[0].x_gamess_basis_set_polar == 'NONE'
    assert sec_method[0].atom_parameters[0].charge.magnitude == approx(9.6130598e-19)

    sec_calc = sec_run[0].calculation
    assert len(sec_calc) == 7
    sec_scf = sec_calc[0].scf_iteration
    assert len(sec_scf) == 8
    assert sec_scf[2].energy.total.value.magnitude == approx(-1.62320848e-16)
    assert sec_scf[6].energy.change.magnitude == approx(-2.61584683e-27)
    assert sec_calc[0].energy.total.value.magnitude == approx(-1.62323183e-16)
    assert sec_calc[0].calculation_converged
    sec_eigs = sec_calc[0].eigenvalues[0]
    assert sec_eigs.energies[0][0][2].magnitude == approx(-2.24483256e-18)
    assert sec_eigs.occupations[0][0][4] == 0
    assert sec_calc[2].forces.total.value[1][2].magnitude == approx(-1.04055078e-10)
    assert sec_calc[2].time_physical.magnitude == approx(0.2)
    assert sec_calc[6].time_calculation.magnitude == approx(0.0)

    sec_system = sec_run[0].system
    assert len(sec_system) == 7
    assert sec_system[0].atoms.labels[1] == 'H'
    assert sec_system[0].atoms.positions[0][2].magnitude == approx(-8.99124183e-12)


def test_firefly(parser):
    archive = EntryArchive()

    parser.parse('tests/data/gamess/firefly/bench01.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == 'Firefly version 8.2.0'

    sec_system = archive.run[0].system
    assert sec_system[0].atoms.labels[5] == 'H'
    assert sec_system[0].atoms.positions[7][2].magnitude == approx(-1.219788e-10)

    sec_scc = sec_run.calculation
    assert sec_scc[0].charges[0].value[4].magnitude == approx(-1.47147106e-20)
    assert sec_scc[0].charges[1].orbital_projected[14].value.magnitude == approx(
        2.18424741e-20
    )
