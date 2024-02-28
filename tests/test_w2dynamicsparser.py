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
from electronicparsers.w2dynamics import W2DynamicsParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return W2DynamicsParser()


def test_srvo3(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/w2dynamics/SrVO3_beta60-2021-12-03-Fri-13-38-46.hdf5', archive, None
    )

    # Run tests
    assert len(archive.run) == 1
    sec_run = archive.run[-1]
    assert len(sec_run.x_w2dynamics_axes) == 12
    assert len(sec_run.x_w2dynamics_axes.x_w2dynamics_w_dos) == 2788

    # Program tests
    assert sec_run.program.name == 'w2dynamics'

    # System tests (SrVO3 crystal)
    assert sec_run.system[-1].atoms.labels == ['Sr', 'V', 'O', 'O', 'O']
    assert sec_run.system[-1].atoms.periodic == [True, True, True]

    # Method tests
    assert (
        len(sec_run.method) == 2
    )  # 2 methods: [0] input Hamiltonian, [1] input DMFT parameters
    assert sec_run.m_xpath('method[0].lattice_model_hamiltonian')
    sec_lattice_model = sec_run.method[0].lattice_model_hamiltonian[0]
    assert hasattr(sec_lattice_model, 'hopping_matrix')
    assert hasattr(sec_lattice_model, 'hubbard_kanamori_model')
    assert sec_lattice_model.hubbard_kanamori_model[0].orbital == 'd'
    assert (
        sec_lattice_model.hubbard_kanamori_model[0].double_counting_correction
        == 'anisimov'
    )
    u = sec_lattice_model.hubbard_kanamori_model[0].u.to('eV').magnitude
    jh = sec_lattice_model.hubbard_kanamori_model[0].jh.to('eV').magnitude
    assert u == approx(4.0)
    assert jh == approx(0.6)
    up = sec_lattice_model.hubbard_kanamori_model[0].up.to('eV').magnitude
    j = sec_lattice_model.hubbard_kanamori_model[0].j.to('eV').magnitude
    # testing rotational invariance
    assert up == approx(u - 2 * jh)
    assert j == approx(jh)
    assert len(sec_run.method[1].x_w2dynamics_config.x_w2dynamics_config_general) == 58
    assert (
        sec_run.method[1].x_w2dynamics_config.x_w2dynamics_config_general.get('beta')
        == 60.0
    )
    assert sec_run.method[1].starting_method_ref == sec_run.method[0]
    sec_dmft = sec_run.method[1].dmft
    assert sec_dmft.n_correlated_orbitals.shape == (1,)
    assert sec_dmft.n_correlated_orbitals[0] == 3
    assert sec_dmft.n_electrons[0] == approx(1.0)
    assert sec_dmft.inverse_temperature.to('1/eV').magnitude == approx(
        sec_run.method[1].x_w2dynamics_config.x_w2dynamics_config_general.get('beta')
    )
    assert sec_dmft.impurity_solver == 'CT-HYB'
    # Frequency and Time meshes
    assert sec_run.m_xpath('method[-1].frequency_mesh') and sec_run.m_xpath(
        'method[-1].time_mesh'
    )
    assert (
        len(sec_run.method[-1].frequency_mesh) == 1
        and len(sec_run.method[-1].time_mesh) == 1
    )
    sec_freq_mesh = sec_run.method[-1].frequency_mesh[0]
    assert sec_freq_mesh.points[22][0].to('eV').magnitude == approx(
        -123.30751165339937j
    )
    sec_time_mesh = sec_run.method[-1].time_mesh[0]
    assert sec_time_mesh.points[40][0] == approx(2.4024024024024024j)

    # Calculation tests
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    assert sec_scc.system_ref == sec_run.system[0]
    assert sec_scc.method_ref == sec_run.method[1]
    sec_gfs = sec_scc.greens_functions[0]
    assert sec_gfs.matsubara_freq[0] == approx(-125.61134626603189)
    assert sec_gfs.matsubara_freq[-1] == approx(125.61134626603189)
    assert sec_gfs.self_energy_iw.dtype == 'complex128'
    assert sec_gfs.self_energy_iw.shape == (1, 2, 3, 2400)
    assert sec_gfs.greens_function_iw[0][0][2][1450] == approx(
        -0.0019060478736177338 - 0.037816153432527574j
    )
    assert sec_gfs.chemical_potential.to('eV').magnitude == approx(14.159227949307798)
    # SCF tests
    sec_scf = sec_scc.scf_iteration
    assert len(sec_scf) == 4
