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
from electronicparsers.gpaw import GPAWParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return GPAWParser()


def test_gpw(parser):
    archive = EntryArchive()
    parser.parse('tests/data/gpaw/H2.gpw', archive, None)

    assert archive.run[0].program.version == '1.1.0'

    sec_method = archive.run[0].method[0]
    sec_basis = sec_method.electrons_representation[0].basis_set[0]
    assert sec_basis.type == 'real-space grid'
    assert sec_method.scf.threshold_energy_change.magnitude == approx(1.42196374e-24)
    assert sec_method.electronic.smearing.width == 0.0
    assert sec_method.electronic.charge == 0.0
    assert sec_method.dft.xc_functional.correlation[0].name == 'LDA_C_PW'
    assert sec_method.x_gpaw_symmetry_time_reversal_switch

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels == ['H', 'H']
    assert sec_system.atoms.lattice_vectors[2][2].magnitude == approx(4.73716558e-10)
    assert True not in sec_system.atoms.periodic
    assert sec_system.atoms.positions[0][2].magnitude == approx(2.73716576e-10)

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-1.51414975e-18)
    assert sec_scc.x_gpaw_fixed_spin_Sz == 0.0
    assert sec_scc.energy.fermi.magnitude == approx(-4.99922789e-19)
    # there is supposed to be magnetic but read eigenvalues are not spinpol
    assert np.shape(sec_scc.eigenvalues[0].energies[0][0]) == (2,)
    assert np.shape(sec_scc.eigenvalues[0].kpoints) == (1, 3)
    assert sec_scc.eigenvalues[0].energies[0][0][1].magnitude == approx(5.54481608e-19)
    assert sec_scc.eigenvalues[0].occupations[0][0][0] == approx(2.0)
    assert sec_scc.calculation_converged


def test_gpw2(parser):
    archive = EntryArchive()
    parser.parse('tests/data/gpaw/Si_pw.gpw2', archive, None)

    assert archive.run[0].program.version == '1.1.1b1'

    sec_method = archive.run[0].method[0]
    sec_basis = sec_method.electrons_representation[0].basis_set[0]
    assert sec_basis.type == 'plane waves'
    assert sec_basis.cutoff.magnitude == approx(4.8065299e-17)
    assert sec_method.scf.threshold_energy_change.magnitude == approx(8.01088317e-23)
    assert sec_method.electronic.smearing.width == approx(1.60217663e-20)
    assert not sec_method.x_gpaw_fix_density
    assert sec_method.dft.xc_functional.exchange[0].name == 'LDA_X'

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels == ['Si', 'Si']
    assert sec_system.atoms.lattice_vectors[0][1].magnitude == approx(2.715e-10)
    assert False not in sec_system.atoms.periodic
    assert sec_system.atoms.positions[1][0].magnitude == approx(1.3575e-10)

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.xc.value.magnitude == approx(-2.19623851e-18)
    assert sec_scc.energy.fermi.magnitude == approx(8.60653138e-19)
    assert np.shape(sec_scc.eigenvalues[0].energies[0][9]) == (8,)
    assert sec_scc.eigenvalues[0].energies[0][7][4].magnitude == approx(9.50790908e-19)
    assert sec_scc.eigenvalues[0].occupations[0][0][0] == 1.0
    assert sec_scc.calculation_converged


def test_spinpol(parser):
    archive = EntryArchive()
    parser.parse('tests/data/gpaw/Hspinpol.gpw', archive, None)

    sec_eig = archive.run[0].calculation[0].eigenvalues[0]
    assert np.shape(sec_eig.kpoints) == (1, 3)
    assert np.shape(sec_eig.occupations[1][0]) == (1,)
    assert np.shape(sec_eig.energies[1][0]) == (1,)
    assert sec_eig.energies[0][0][0].magnitude == approx(-1.20983278e-18)
    assert archive.run[0].calculation[0].x_gpaw_magnetic_moments[0] == 1.0


def test_lcao(parser):
    archive = EntryArchive()
    parser.parse('tests/data/gpaw/Si_lcao.gpw2', archive, None)

    assert archive.run[0].program.version == '1.1.1b1'

    sec_method = archive.run[0].method[0]
    sec_basis = sec_method.electrons_representation[0].basis_set[0]
    assert sec_basis.type == 'numeric AOs'

    sec_density = archive.run[0].calculation[0].density_charge[0]
    sec_potential = archive.run[0].calculation[0].potential[0].effective[0]
    assert sec_density.value[0][13][2][8].magnitude == approx(8.70353098415676e28)
    assert sec_potential.value[0][5][14][1].magnitude == approx(-1235219198924.2632)
