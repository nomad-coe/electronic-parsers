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
from electronicparsers.turbomole import TurbomoleParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return TurbomoleParser()


def test_aoforce(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/aoforce/vib.out', archive, None)

    assert archive.run[0].program.version == '7.2 ( 21285 )'
    assert archive.run[0].time_run.date_start.magnitude == 1532973127.689

    sec_method = archive.run[0].method[0]
    assert sec_method.electronic.method == 'DFT'
    assert sec_method.dft.xc_functional.correlation[0].name == 'GGA_C_P86'
    assert len(sec_method.atom_parameters) == 4
    assert len(sec_method.electrons_representation[0].basis_set[0].atom_centered) == 4
    assert sec_method.electronic.van_der_waals_method == 'DFT-D3'
    assert sec_method.x_turbomole_controlIn_scf_conv == 8

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-3.58404386e-15)
    assert sec_scc.energy.zero_point.value.magnitude == approx(1.02171533e-18)
    assert sec_scc.energy.current.value.magnitude == approx(-3.58302215e-15)
    assert np.shape(sec_scc.hessian_matrix) == (31, 31, 3, 3)
    assert sec_scc.hessian_matrix[3][2][2][0] == approx(-38.1728237)
    assert np.shape(sec_scc.x_turbomole_vibrations_normal_modes) == (93, 31, 3)
    assert sec_scc.x_turbomole_vibrations_normal_modes[0][4][1] == approx(-0.02383)
    assert sec_scc.x_turbomole_vibrations_mode_energies[46] == approx(1005.73)
    assert sec_scc.x_turbomole_vibrations_intensities[72] == approx(41.61)
    assert sec_scc.x_turbomole_vibrations_infrared_activity[49]
    assert not sec_scc.x_turbomole_vibrations_raman_activity[5]

    sec_system = archive.run[0].system[0]
    assert len(sec_system.atoms.positions) == 31
    assert sec_system.atoms.positions[7][1].magnitude == approx(-9.34235013e-11)
    assert sec_system.atoms.labels[21] == 'O'


def test_ccsdf12(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/ccsdf12.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 3
    assert sec_sccs[0].energy.total.value.magnitude == approx(-2.99865659e-15)
    assert sec_sccs[1].energy.total.value.magnitude == approx(-2.99841134e-15)
    assert sec_sccs[2].energy.total.value.magnitude == approx(-2.99844594e-15)
    assert sec_sccs[1].energy.current.value.magnitude == approx(-5.78479974e-18)
    sec_scfs = sec_sccs[0].scf_iteration
    assert len(sec_scfs) == 13
    assert sec_scfs[8].energy.total.value.magnitude == approx(-2.99844594e-15)
    assert sec_sccs[0].time_calculation.magnitude == 40 * 60 + 7
    assert sec_sccs[0].scf_iteration[2].time_physical.magnitude == approx(5.89)
    assert sec_sccs[0].scf_iteration[4].time_calculation.magnitude == approx(1.89)


def test_grad_statpt_dscf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/acrolein_grad_statpt_dscf.out', archive, None)

    sec_methods = archive.run[0].method
    assert (
        sec_methods[0].electrons_representation[0].basis_set[0].atom_centered[0].name
        == 'def2-SVP'
    )
    assert len(sec_methods) == 3
    assert sec_methods[0].dft.xc_functional.hybrid[0].name == 'HYB_GGA_XC_B3LYP'

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 3
    assert sec_systems[1].atoms.positions[5][1].magnitude == approx(
        1.22377337e-10,
    )

    sec_sccs = archive.run[0].calculation
    assert sec_sccs[0].forces.total.value_raw[6][0].magnitude == approx(-4.2984543e-12)
    sec_scfs = sec_sccs[2].scf_iteration
    assert len(sec_scfs) == 3
    assert sec_scfs[1].energy.total.value.magnitude == approx(-8.35592725e-16)
    assert sec_scfs[0].x_turbomole_delta_eigenvalues.magnitude == approx(2.92683961e-22)
    assert sec_sccs[2].energy.kinetic_electronic.value.magnitude == approx(
        8.27834082e-16
    )

    sec_sampling = archive.workflow2
    assert (
        sec_sampling.method.x_turbomole_geometry_optimization_trustregion_min.magnitude
        == approx(5.29177211e-14)
    )
    assert sec_sampling.method.method == 'BFGS'
    assert sec_sampling.method.convergence_tolerance_force_maximum.magnitude == approx(
        8.2387235e-11
    )


def test_escf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/benzene_escf.out', archive, None)

    sec_method = archive.run[0].method[0]
    assert sec_method.electronic.method == 'G0W0'
    assert sec_method.x_turbomole_gw_eta_factor.magnitude == approx(4.35974472e-21)
    assert sec_method.x_turbomole_gw_approximation == 'G0W0'

    sec_scc = archive.run[0].calculation[0]
    sec_eigs_gw = sec_scc.eigenvalues[0]
    assert sec_eigs_gw.value_ks[0][0][9].magnitude == approx(-3.59608546e-18)
    assert sec_eigs_gw.value_exchange[0][0][1].magnitude == approx(-1.55874163e-17)
    assert sec_eigs_gw.qp_linearization_prefactor[0][0][19] == 0.786


def test_freeh(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/freeh.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 2
    assert sec_sccs[0].energy.zero_point.value.magnitude == approx(4.89692971e-19)
    assert sec_sccs[1].energy.correction_entropy.value.magnitude == approx(
        2.00144971e-19
    )
    assert sec_sccs[1].thermodynamics[0].heat_capacity_c_v.magnitude == approx(
        2.27860167e-22
    )
    assert sec_sccs[1].thermodynamics[0].pressure.magnitude == 100000.0


def test_pnoccsd(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/pnoccsd.out', archive, None)

    assert np.shape(archive.run[0].system[0].atoms.positions) == (51, 3)

    sec_methods = archive.run[0].method
    assert len(sec_methods) == 4
    assert sec_methods[0].electronic.method == 'CCSD(T)'
    assert sec_methods[1].electronic.method == 'MP2'
    assert sec_methods[2].electronic.method == 'CCSD'
    assert sec_methods[3].electronic.method == 'CCSD(T0)'

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 4
    assert sec_sccs[0].energy.total.value.magnitude == approx(-5.63810959e-15)
    assert sec_sccs[1].energy.total.value.magnitude == approx(-5.63669838e-15)
    assert sec_sccs[2].energy.current.value.magnitude == approx(-2.19140251e-17)
    assert sec_sccs[3].energy.total.value.magnitude == approx(-5.6380984e-15)

    sec_scfs = sec_sccs[0].scf_iteration
    assert len(sec_scfs) == 13
    assert sec_scfs[6].energy.total.value.magnitude == approx(-5.63708622e-15)


def test_ricc2(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/MgO_embedding_ricc2.out', archive, None)

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 4
    assert sec_systems[0].atoms.positions[4][2].magnitude == approx(6.38760003e-10)
    assert sec_systems[1].atoms.positions[18][0].magnitude == approx(4.25840002e-10)
    assert sec_systems[2].atoms.positions[25][2].magnitude == approx(2.12920001e-10)
    assert sec_systems[3].atoms.positions[-2][1].magnitude == approx(8.51680003e-10)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 3
    assert sec_sccs[1].energy.total.value.magnitude == approx(-8.6955048e-15)


def test_ridft(parser):
    archive = EntryArchive()
    parser.parse('tests/data/turbomole/ridft.out', archive, None)

    sec_method = archive.run[0].method[0]
    assert sec_method.x_turbomole_dft_d3_version == '3.1 Rev 0'

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.van_der_waals.value.magnitude == approx(-1.32811671e-18)
    assert sec_scc.energy.total.value.magnitude == approx(-2.25881721e-14)
    assert sec_scc.x_turbomole_virial_theorem == approx(1.94918952771)

    sec_scf = sec_scc.scf_iteration
    assert len(sec_scf) == 28
    assert sec_scf[3].x_turbomole_energy_2electron_scf_iteration.magnitude == approx(
        1.02566632e-13
    )
    assert sec_scf[23].energy.xc.value.magnitude == approx(-2.28814098e-15)
