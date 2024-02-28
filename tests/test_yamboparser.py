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
from electronicparsers.yambo import YamboParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return YamboParser()


def test_0(parser):
    archive = EntryArchive()
    parser.parse('tests/data/yambo/hBN/r_setup', archive, None)

    run = archive.run[-1]
    assert run.program.version == '5.0.4 Revision 19598'
    assert run.program.x_yambo_hash == '20b2ffa04'
    assert run.x_yambo_threads_per_core == 1
    assert run.x_yambo_fragmented_wfs

    system = run.system[0]
    assert system.atoms.positions[2][1].magnitude == approx(-7.20417507e-11)
    assert system.atoms.labels[3] == 'N'
    assert system.atoms.lattice_vectors[0][1].magnitude == approx(-1.24779986e-10)

    calc = run.calculation[0]
    assert calc.energy.fermi.magnitude == approx(8.18834506e-19)
    assert calc.energy.lowest_unoccupied.magnitude == approx(6.21331789e-19)
    assert calc.x_yambo_electronic_density == approx(0.46037e24)
    assert not calc.x_yambo_finite_temperature_mode
    assert calc.x_yambo_filled_bands[1] == 8
    assert calc.x_yambo_direct_gap.magnitude == approx(6.87318075e-19)
    eigenvalues = calc.eigenvalues[0]
    assert eigenvalues.kpoints[6][1] == approx(-0.49999997)
    assert eigenvalues.energies[0][6][7].magnitude == approx(2.76666665e-20)


def test_1(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/yambo/hBN/r-10b_1Ry_HF_and_locXC_gw0_em1d_ppa', archive, None
    )

    run = archive.run[-1]
    method = run.method
    assert len(method) == 5
    assert (
        method[0]
        .x_yambo_transferred_momenta[0]
        .x_yambo_input[0]
        .x_yambo_parameters['Sigma scattering']
        == 'yes'
    )
    assert (
        method[1].x_yambo_dipoles[0].x_yambo_input[0].x_yambo_file
        == './SAVE//ns.kb_pp_pwscf'
    )
    assert method[1].x_yambo_dipoles[0].x_yambo_input[0].x_yambo_sn == '009327'
    assert (
        method[1]
        .x_yambo_dipoles[0]
        .x_yambo_output[0]
        .x_yambo_parameters['Fragmentation']
        == 'yes'
    )
    assert method[2].x_yambo_dynamic_dielectric_matrix[0].x_yambo_output[
        0
    ].x_yambo_parameters['BZ Q point size factor'] == approx(1.0)
    assert (
        method[3]
        .x_yambo_local_xc_nonlocal_fock[0]
        .x_yambo_output[0]
        .x_yambo_parameters['RL vectors']
        == 1491
    )
    assert method[4].x_yambo_dyson[0].x_yambo_input[0].x_yambo_parameters[
        'X poles'
    ] == approx(100.0)
    assert (
        method[4].x_yambo_dyson[1].x_yambo_output[0].x_yambo_parameters['GW solver']
        == 'Newton'
    )
    ddm = method[2].x_yambo_dynamic_dielectric_matrix[0]
    assert ddm.x_yambo_output[0].x_yambo_file == './10b_1Ry//ndb.pp'
    assert ddm.x_yambo_mesh_size[2] == 27
    assert len(ddm.x_yambo_fragment) == 14
    assert np.shape(ddm.x_yambo_fragment[2].x_yambo_X_Q) == (2, 5, 5, 2)
    assert method[3].x_yambo_local_xc_nonlocal_fock[0].x_yambo_mesh_size[1] == 18
    assert method[3].x_yambo_local_xc_nonlocal_fock[0].x_yambo_plane_waves_vxc == 3187

    calc = run.calculation
    assert calc[0].x_yambo_bosonic_temperature == approx(0.0)
    assert calc[0].energy.fermi.magnitude == approx(8.18834506e-19)
    assert calc[0].energy.lowest_unoccupied.magnitude == approx(6.21331789e-19)
    assert calc[0].x_yambo_filled_bands[1] == 8

    assert calc[1].energy.xc.value.magnitude == approx(-3.16453858e-17)
    assert calc[1].x_yambo_local_xc_nonlocal_fock_bandenergies[0].x_yambo_sx[0][0][
        1
    ].magnitude == approx(-8.87037934e-19)
    assert calc[1].x_yambo_local_xc_nonlocal_fock_bandenergies[0].x_yambo_vxc[0][0][
        0
    ].magnitude == approx(-2.58066631e-18)

    assert calc[2].eigenvalues[0].kpoints[-1][1] == approx(-0.5)
    assert calc[2].eigenvalues[0].qp_linearization_prefactor[0][0][1] == approx(
        0.8320594
    )
    assert calc[2].eigenvalues[0].value_qp[0][0][0].magnitude == approx(-1.56952554e-19)
    assert calc[2].eigenvalues[0].value_ks[0][0][0].magnitude == approx(-6.59862623e-20)


def test_2(parser):
    archive = EntryArchive()
    parser.parse('tests/data/yambo/Aluminum/r-01_Lifetimes_em1d_life', archive, None)

    run = archive.run[-1]
    assert run.program.version == '4.4.0 Revision 148'
    assert run.program.x_yambo_build == 'MPI+SLK+OpenMP'
    assert run.x_yambo_threads_tot == 1
    assert run.x_yambo_io_nodes == 1
    assert run.x_yambo_additional_io == '.'
    assert run.x_yambo_job_string == '01_Lifetimes'
    assert run.x_yambo_input.x_yambo_file == './SAVE//ns.db1'
    assert run.x_yambo_input.x_yambo_parameters['Electrons'] == approx(3.0)
    assert run.x_yambo_input.x_yambo_sn == '009108'

    calc = run.calculation
    assert len(calc) == 1
    assert calc[0].energy.fermi.magnitude == approx(1.34005621e-18)
    assert calc[0].energy.highest_occupied.magnitude == approx(1.34005621e-18)
    assert calc[0].x_yambo_electronic_temperature.magnitude == approx(300.1)
    assert calc[0].x_yambo_finite_temperature_mode
    assert calc[0].x_yambo_filled_bands[1] == 1
    assert calc[0].x_yambo_empty_bands[0] == 4
    eigenvalues = calc[0].eigenvalues[0]
    assert eigenvalues.kpoints[24][2] == approx(-0.5)
    assert eigenvalues.kpoints_weights[4] == approx(0.0078)
    assert eigenvalues.energies[0][16][9].magnitude == approx(4.20775484e-18)


def test_3(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/yambo/GaSb/r-02_GW_em1d_ppa_HF_and_locXC_gw0', archive, None
    )

    method = archive.run[-1].method
    assert len(method) == 4
    assert (
        method[0]
        .x_yambo_transferred_momenta[0]
        .x_yambo_input[0]
        .x_yambo_parameters['QP states']
        == '1  29'
    )
    assert method[2].x_yambo_bare_xc[0].x_yambo_output[0].x_yambo_parameters[
        'Bosonic    Temperature'
    ] == approx(0.0)

    calc = archive.run[-1].calculation
    assert len(calc) == 3
    assert calc[0].x_yambo_indirect_gaps[1].magnitude == approx(5.72851847e-19)
    assert calc[0].eigenvalues[0].energies[0][18][5].magnitude == approx(-4.1855743e-19)
    assert calc[1].x_yambo_bare_xc_bandenergies[0].x_yambo_dft[0][0][
        4
    ].magnitude == approx(-1.57994179e-18)
    assert calc[1].x_yambo_bare_xc_bandenergies[0].x_yambo_hf[0][0][
        7
    ].magnitude == approx(-8.34041085e-19)
    assert calc[1].x_yambo_filled_bands[1] == 8
    assert calc[1].x_yambo_direct_gaps[0].magnitude == approx(1.96538367e-19)
    assert calc[2].eigenvalues[0].qp_linearization_prefactor[0][0][2] == approx(0.8)
    assert calc[2].eigenvalues[0].value_qp[0][0][5].magnitude == approx(1.13754541e-19)
    assert calc[2].eigenvalues[0].value_ks[0][0][1].magnitude == approx(0.0)


def test_4(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/yambo/LiF/r-02_QP_PPA_em1d_ppa_HF_and_locXC_gw0', archive, None
    )

    calc = archive.run[-1].calculation
    assert len(calc) == 3
    assert calc[1].x_yambo_bare_xc_bandenergies[0].x_yambo_hf[0][8][
        3
    ].magnitude == approx(-1.02367551e-18)
    assert calc[1].x_yambo_bare_xc_bandenergies[0].x_yambo_dft[0][3][
        1
    ].magnitude == approx(-3.58760674e-18)
    assert calc[2].eigenvalues[0].qp_linearization_prefactor[0][2][2] == approx(0.89)
    assert calc[2].eigenvalues[0].value_qp[0][5][1].magnitude == approx(-5.68772705e-19)
    assert calc[2].eigenvalues[0].value_ks[0][-1][3].magnitude == approx(2.36641489e-18)
