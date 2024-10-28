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
from electronicparsers.psi4 import Psi4Parser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return Psi4Parser()


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/adc1/output.ref', archive, None)

    assert len(archive.run) == 1
    run = archive.run[-1]
    assert run.program.version == '1.1rc3.dev5'
    assert run.x_psi4_process_id == 22664
    assert run.x_psi4_memory == 500

    method = run.method[0]
    assert method.electronic.method == 'RHF'
    sec_basis = method.electrons_representation[0].basis_set
    assert len(sec_basis) == 1
    assert sec_basis[0].atom_centered[0].name == '6-31G**'
    assert sec_basis[0].atom_centered[0].x_psi4_n_shells == 12
    assert method.scf.minimization_algorithm == 'PK'
    assert not method.scf.x_psi4_mom
    assert method.scf.threshold_energy_change.magnitude == approx(4.35974472e-26)
    assert method.scf.x_psi4_integral_threshold == approx(0)

    system = run.system[0]
    assert system.atoms.positions[1][1].magnitude == approx(-4.00873327e-11)
    assert system.atoms.labels[2] == 'H'
    assert system.x_psi4_full_point_group == 'C2v'
    assert system.x_psi4_rotational_constants[2] == approx(9.50429)
    assert system.x_psi4_nbeta == 5

    calc = run.calculation[0]
    assert calc.energy.nuclear_repulsion.value.magnitude == approx(4.00382263e-17)
    assert calc.energy.contributions[0].value.magnitude == approx(-5.36576827e-16)
    assert calc.energy.contributions[3].value.magnitude == approx(0)
    assert calc.energy.total.value.magnitude == approx(-3.31441255e-16)
    assert len(calc.scf_iteration) == 12
    assert calc.scf_iteration[10].energy.total.value.magnitude == approx(
        -3.31441255e-16
    )
    assert calc.scf_iteration[3].energy.change.magnitude == approx(-1.03461102e-18)
    assert calc.multipoles[0].dipole.total[2] == approx(-9.91967374e-31)
    assert calc.multipoles[1].dipole.total[2] == approx(8.28504716e-30)
    assert calc.multipoles[2].dipole.total[2] == approx(7.29392762e-30)
    eigs = calc.eigenvalues[0]
    assert np.shape(eigs.energies) == np.shape(eigs.occupations) == (1, 1, 25)
    assert eigs.orbital_labels[11] == '12A'
    assert eigs.energies[0][0][3].magnitude == approx(-2.47920807e-18)
    assert eigs.occupations[0][0][4] == approx(2)
    assert eigs.occupations[0][0][5] == approx(0)


def test_properties(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/scf-property/output.ref', archive, None)

    calc = archive.run[-1].calculation
    assert calc[0].spin_S2 == approx(2.011483171)
    assert calc[0].x_psi4_s_expected == approx(1)
    assert len(calc[0].scf_iteration) == 10
    assert np.shape(calc[0].eigenvalues[0].energies) == (2, 1, 25)
    assert calc[0].eigenvalues[0].occupations[0][0][4] == approx(1)
    assert calc[0].eigenvalues[0].occupations[1][0][3] == approx(0)
    assert calc[0].energy.total.value.magnitude == approx(-1.69663469e-16)
    assert calc[0].charges[0].value[0].magnitude == approx(-4.12095852e-20)
    assert calc[0].charges[1].spin_projected[5].value.magnitude == approx(
        7.31970417e-20
    )
    assert calc[0].charges[1].total.magnitude == approx(0)
    assert calc[1].eigenvalues[0].energies[1][0][4].magnitude == approx(-1.77537525e-19)
    assert calc[1].energy.nuclear_repulsion.value.magnitude == approx(2.89854093e-17)
    assert calc[1].multipoles[0].dipole.total[2] == approx(-4.14390216e-30)
    assert calc[1].multipoles[1].dipole.total[2] == approx(6.28452197e-30)
    assert calc[1].multipoles[2].dipole.total[2] == approx(2.14062066e-30)
    assert calc[1].multipoles[0].quadrupole.total[0] == approx(-2.54058558e-39)
    assert calc[1].multipoles[1].quadrupole.total[3] == approx(2.52114741e-39)
    assert calc[1].multipoles[2].quadrupole.total[3] == approx(-2.00335127e-39)
    assert calc[1].multipoles[0].octupole.total[2] == approx(-1.28485205e-51)
    assert calc[1].multipoles[1].octupole.total[7] == approx(9.96716959e-50)
    assert calc[1].multipoles[2].octupole.total[9] == approx(-1.56865451e-51)
    assert calc[1].multipoles[0].higher_order[0].kind == 'hexadecapole'
    assert calc[1].multipoles[0].higher_order[0].total[0] == approx(-2.64081324e-59)
    assert calc[1].multipoles[1].higher_order[0].total[10] == approx(1.98360911e-59)
    assert calc[1].multipoles[2].higher_order[0].total[3] == approx(-1.19284477e-59)
    assert calc[1].multipoles[0].higher_order[1].total[2] == approx(6.1606188e-71)
    assert calc[1].multipoles[1].higher_order[1].total[16] == approx(7.84205161e-70)
    assert calc[1].multipoles[2].higher_order[1].total[7] == approx(-1.41403902e-70)


def test_ecp_basis(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/basis-ecp/output.ref', archive, None)

    method = archive.run[0].method
    assert len(method) == 6
    assert len(method[1].electrons_representation[0].basis_set) == 2
    sec_basis = method[2].electrons_representation[0].basis_set
    assert sec_basis[0].atom_centered[0].name == 'DEF2-SV_P_'
    assert sec_basis[0].atom_centered[1].x_psi4_n_shells == 4
    assert sec_basis[1].atom_centered[0].name == 'DEF2-SV_P_ AUX'
    assert method[3].x_psi4_jk_matrices_parameters['Schwarz Cutoff'] == approx(1e-12)
    sec_basis = method[4].electrons_representation[0].basis_set
    assert sec_basis[1].atom_centered[0].n_basis_functions == 309
    assert method[5].electronic.method == 'RHF'

    calc = archive.run[0].calculation
    assert len(calc) in (5, 6)
    assert calc[3].energy.total.value.magnitude == approx(-1.29372859e-15)
    assert calc[4].scf_iteration[1].energy.total.value.magnitude == approx(
        -3.00651252e-14
    )
    if len(calc) == 6:  # cover failed calculation step
        assert calc[-1].calculations_ref is None
        assert calc[-1].method_ref == archive.run[0].method[5]
        assert calc[-1].system_ref == archive.run[0].system[5]
        # TODO: add check for basis set to really identify the failed step


def test_dft(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/dft-b3lyp/output.ref', archive, None)

    dft = archive.run[-1].method[0].dft
    assert dft.xc_functional.contributions[0].name == 'HYB_GGA_XC_B3LYP'
    assert dft.xc_functional.contributions[0].parameters['X_Alpha'] == approx(0.2)

    archive = EntryArchive()
    parser.parse('tests/data/psi4/dft-custom-hybrid/output.ref', archive, None)

    dft = archive.run[-1].method[1].dft
    assert len(dft.xc_functional.exchange) == 2
    assert dft.xc_functional.exchange[0].name == 'LDA_X'
    assert dft.xc_functional.exchange[1].weight == approx(0.7500)
    assert len(dft.xc_functional.correlation) == 1
    assert dft.xc_functional.correlation[0].name == 'GGA_C_PBE'
    assert dft.x_psi4_molecular_quadrature is not None


def test_dft_grad(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/dft-grad-disk/output.ref', archive, None)

    assert archive.run[-1].system[1].atoms.positions[0][2].magnitude == approx(
        -1.88056612e-11
    )
    assert (
        archive.run[-1]
        .method[1]
        .electrons_representation[0]
        .basis_set[0]
        .atom_centered[0]
        .name
        == 'AUG-CC-PVQZ'
    )
    assert (
        archive.run[-1]
        .method[0]
        .electrons_representation[0]
        .basis_set[1]
        .atom_centered[0]
        .name
        == 'AUG-CC-PVQZ AUX'
    )
    assert archive.run[-1].calculation[1].forces.total.value[1][2].magnitude == approx(
        -8.16191049e-09
    )


def test_mp2p5(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/mp2p5-grad1/output.ref', archive, None)

    assert len(archive.run[-1].method) == 2
    assert archive.run[-1].method[1].electronic.method == 'MP2.5'
    assert archive.run[-1].method[1].core_method_ref == archive.run[-1].method[0]
    options = archive.run[-1].method[-1].x_psi4_options
    assert options['E_CONVERGENCE'] == approx(1e-8)
    assert not options['EP_IP_POLES']

    calc = archive.run[-1].calculation
    assert len(calc) == 3
    assert calc[0].energy.total.value.magnitude == approx(-3.3145727e-16)
    assert calc[0].energy.contributions[2].kind == 'Empirical Dispersion'
    assert calc[0].energy.contributions[2].value.magnitude == approx(0)
    assert calc[1].energy.nuclear_repulsion.value.magnitude == approx(4.00546595e-17)
    assert calc[1].energy.contributions[5].kind == '0.5 Correction'
    assert calc[1].energy.contributions[5].value.magnitude == approx(-1.47957903e-20)
    assert calc[1].energy.contributions[3].kind == 'Alpha-Beta'
    assert calc[1].energy.contributions[3].value.magnitude == approx(-6.87879256e-19)
    assert calc[1].energy.total.value.magnitude == approx(-3.32361538e-16)
    assert calc[2].energy.contributions[8].value.magnitude == approx(-3.32321529e-16)
    assert calc[2].energy.contributions[12].value.magnitude == approx(-8.89471802e-19)
    assert calc[2].energy.contributions[0].value.magnitude == approx(-3.3145727e-16)
    assert calc[2].energy.contributions[5].value.magnitude == approx(-7.4885929e-20)


def test_ci(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/ci-property/output.ref', archive, None)

    assert len(archive.run[-1].system) == 3
    method = archive.run[-1].method
    assert len(method) == 6
    assert method[1].x_psi4_parameters['OPENTYPE'] == 'HIGHSPIN'
    assert method[3].x_psi4_parameters['E CONV'] == approx(1.00e-10)

    calc = archive.run[-1].calculation
    assert len(calc) == 17
    assert calc[3].starting_calculation_ref == calc[1]
    assert calc[5].energy.contributions[1].value.magnitude == approx(9.92653295e-16)
    assert calc[6].energy.total.value.magnitude == approx(-1.21540239e-15)
    assert calc[11].energy.nuclear_repulsion.value.magnitude == approx(5.03566352e-16)
    assert calc[1].energy.total.value.magnitude == approx(-1.21546394e-15)

    assert calc[3].multipoles[2].quadrupole.total[3] == approx(-9.62457097e-39)
    assert calc[7].charges[0].value[3].magnitude == approx(-9.74716199e-20)


def test_mcscf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/mcscf1/output.ref', archive, None)

    calc = archive.run[-1].calculation[0]
    assert len(calc.scf_iteration) == 17
    assert calc.scf_iteration[8].energy.total.value.magnitude == approx(-1.69643637e-16)
    assert calc.scf_iteration[2].energy.change.magnitude == approx(-3.92706531e-18)
    assert calc.eigenvalues[0].energies[0][0][6].magnitude == approx(1.56016953e-18)
    assert calc.eigenvalues[0].occupations[0][0][4] == approx(2)


def test_gradient(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/cbs-xtpl-gradient/output.ref', archive, None)

    calc = archive.run[-1].calculation
    assert len(calc) == 35
    assert calc[18].forces.total.value[1][2].magnitude == approx(-9.9316642e-10)
    assert calc[20].forces.contributions[1].kind == 'One-electron'
    assert calc[20].forces.contributions[2].value[1][2].magnitude == approx(
        1.43696057e-09
    )
    assert calc[3].time_calculation.magnitude == approx(0.28)
    assert calc[10].time_physical.magnitude == approx(3.24)


def test_cc(parser):
    archive = EntryArchive()
    parser.parse('tests/data/psi4/cc1/output.ref', archive, None)

    method = archive.run[-1].method
    assert len(method) == 15

    calc = archive.run[-1].calculation
    assert len(calc) == 30
    assert calc[1].energy.nuclear_repulsion.value.magnitude == approx(3.95744411e-17)
    assert len(calc[2].scf_iteration) == 13
    assert calc[2].scf_iteration[2].energy.total.value.magnitude == approx(
        -9.08810332e-19
    )
    assert calc[2].energy.contributions[3].value.magnitude == approx(-2.19424304e-19)
    assert calc[3].scf_iteration[9].energy.total.value.magnitude == approx(
        -8.98015443e-19
    )
    assert calc[4].energy.total.value.magnitude == approx(-3.32347651e-16)
    assert calc[5].energy.contributions[5].value.magnitude == approx(-8.87549814e-22)
    assert calc[6].energy.contributions[0].value.magnitude == approx(3.30311948e-16)
    assert calc[9].forces.total.value[1][1].magnitude == approx(-5.32388792e-10)
    assert calc[1].time_calculation.magnitude == approx(0.02)
    assert calc[3].time_physical.magnitude == approx(0.54)

    geo_opt = archive.workflow2
    assert geo_opt.method.convergence_tolerance_energy_difference.magnitude == approx(
        4.35974472e-24
    )
    assert geo_opt.method.convergence_tolerance_force_maximum.magnitude == approx(
        2.47161705e-11
    )
    assert (
        geo_opt.method.convergence_tolerance_displacement_maximum.magnitude
        == approx(6.35012653e-14)
    )
