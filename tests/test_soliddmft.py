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
from electronicparsers.soliddmft import SolidDMFTParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return SolidDMFTParser()


def test_srvo3(parser):
    archive = EntryArchive()
    parser.parse('tests/data/soliddmft/srvo3/svo_example.h5', archive, None)

    # Run tests
    assert len(archive.run) == 1
    sec_run = archive.run[-1]
    # Program tests
    assert sec_run.program.name == 'solid_dmft'
    assert sec_run.program.version == '3.1.2'
    assert sec_run.program.x_soliddmft_hash == 'ae0794c4e3678d367ad340b25e1a64a5c0f23a9f'

    # System tests (SrVO3 crystal)
    # unknown: we need this info from the devs

    # Method tests
    assert len(sec_run.method) == 2  # 2 methods: [0] input Hamiltonian, [1] input DMFT parameters
    # input Hamiltonian
    assert sec_run.m_xpath('method[0].lattice_model_hamiltonian')
    sec_lattice_model = sec_run.method[0].lattice_model_hamiltonian[0]
    assert hasattr(sec_lattice_model, 'projection_matrix')
    assert sec_lattice_model.projection_matrix.shape == (729, 1, 3, 5)
    assert hasattr(sec_lattice_model, 'hubbard_kanamori_model')
    assert len(sec_lattice_model.hubbard_kanamori_model) == 1
    assert sec_lattice_model.hubbard_kanamori_model[0].orbital == 'd'
    u = sec_lattice_model.hubbard_kanamori_model[0].u.to('eV').magnitude
    jh = sec_lattice_model.hubbard_kanamori_model[0].jh.to('eV').magnitude
    assert u == approx(8.0)
    assert jh == approx(0.65)
    up = sec_lattice_model.hubbard_kanamori_model[0].up.to('eV').magnitude
    j = sec_lattice_model.hubbard_kanamori_model[0].j.to('eV').magnitude
    # testing rotational invariance
    assert up == approx(u - 2 * jh)
    assert j == approx(jh)
    # input DMFT
    assert len(sec_run.method[-1].x_soliddmft_general) == 55
    assert len(sec_run.method[-1].x_soliddmft_solver) == 15
    assert len(sec_run.method[-1].x_soliddmft_advanced) == 8
    assert sec_run.method[-1].starting_method_ref == sec_run.method[0]
    sec_dmft = sec_run.method[-1].dmft
    assert sec_dmft.n_impurities == 1
    assert sec_dmft.n_correlated_orbitals[0] == 3
    assert sec_dmft.n_electrons == approx(1.0000225214138097)
    assert sec_dmft.inverse_temperature.to('1/eV').magnitude == approx(10.0)
    assert sec_dmft.inverse_temperature.to('1/eV').magnitude == approx(sec_run.method[-1].x_soliddmft_general.x_soliddmft_beta)
    assert sec_dmft.impurity_solver == 'CT-HYB'
    sec_k_mesh = sec_run.method[-1].k_mesh
    assert sec_k_mesh.n_points == 729
    assert sec_run.m_xpath('method[-1].frequency_mesh') and sec_run.m_xpath('method[-1].time_mesh')
    sec_freq_mesh = sec_run.method[-1].frequency_mesh
    assert sec_freq_mesh.n_points == 501
    assert sec_freq_mesh.points[15][0].to('eV').magnitude == approx(-97.10000000000001j)
    sec_time_mesh = sec_run.method[-1].time_mesh
    assert sec_time_mesh.n_points == 10001
    assert sec_time_mesh.points[76][0] == approx(0.076j)

    # Calculation tests
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    # assert sec_scc.system_ref == sec_run.system[0]
    assert sec_scc.method_ref == sec_run.method[1]
    sec_gfs = sec_scc.greens_functions[0]
    assert sec_gfs.matsubara_freq[0] == approx(-100.1)
    assert sec_gfs.matsubara_freq[-1] == approx(100.1)
    assert sec_gfs.tau.shape[0] == sec_time_mesh.n_points
    assert sec_gfs.self_energy_iw.dtype == 'complex128'
    assert sec_gfs.self_energy_iw.shape == (1, 2, 3, 1002)
    assert sec_gfs.greens_function_tau[0][1][1][1025] == approx(-0.14109113749664728 + 0j)
    assert sec_gfs.chemical_potential.magnitude == approx(0.0378235342396917)
    assert np.sum(sec_gfs.orbital_occupations) == approx(1.008321846227956)
    assert sec_gfs.quasiparticle_weights.shape == (1, 2, 3)
    assert sec_gfs.quasiparticle_weights[0][0][0] == approx(0.16195076915540912)
    # SCF tests
    sec_scf = sec_scc.scf_iteration
    assert len(sec_scf) == 3
    assert sec_scf[0].energy.fermi.to('eV').magnitude == approx(-0.027041)
    assert sec_scf[-1].energy.fermi.to('eV').magnitude == approx(sec_gfs.chemical_potential.magnitude)
    assert sec_scf[1].x_soliddmft_convergence_obs.x_soliddmft_d_G0[0] == 0.03463529305810029
