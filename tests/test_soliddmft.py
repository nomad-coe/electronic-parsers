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
from electronicparsers.soliddmft import SolidDMFTParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return SolidDMFTParser()


@pytest.mark.skip('Disabled as the data is too big for the repo. Please contact Jose Pizarro if you would like to obtain the data')
def test_srvo3_highstat(parser):
    archive = EntryArchive()
    parser.parse('tests/data/w2dynamics/srvo3/SrVO3_beta60_high-stat-2022-09-29-Thu-15-29-40.hdf5', archive, None)

    # Run tests
    assert len(archive.run) == 1
    sec_run = archive.run[-1]
    assert len(sec_run.x_w2dynamics_axes) == 14
    assert sec_run.x_w2dynamics_axes.x_w2dynamics_iw.shape[0] == 2400
    assert sec_run.x_w2dynamics_axes.x_w2dynamics_tau.shape[0] == 1000
    assert sec_run.x_w2dynamics_axes.x_w2dynamics_w_dos.shape[0] == 2794

    # Program tests
    assert sec_run.program.name == 'w2dynamics'

    # System tests (SrVO3 crystal)
    assert sec_run.system[-1].atoms.labels == ['Sr', 'V', 'O', 'O', 'O']
    assert sec_run.system[-1].atoms.periodic == [True, True, True]

    # Method tests
    assert len(sec_run.method) == 2  # 2 methods: [0] input Hamiltonian, [1] input DMFT parameters
    sec_lattice_model = sec_run.method[0].lattice_model_hamiltonian[0]
    assert hasattr(sec_lattice_model, 'hopping_matrix')
    assert hasattr(sec_lattice_model, 'hubbard_kanamori_model')
    assert sec_lattice_model.hubbard_kanamori_model.orbital == 'd'
    u = sec_lattice_model.hubbard_kanamori_model.u.to('eV').magnitude
    jh = sec_lattice_model.hubbard_kanamori_model.jh.to('eV').magnitude
    assert u == approx(4.0)
    assert jh == approx(0.6)
    up = sec_lattice_model.hubbard_kanamori_model.up.to('eV').magnitude
    j = sec_lattice_model.hubbard_kanamori_model.j.to('eV').magnitude
    # testing rotational invariance
    assert up == approx(u - 2 * jh)
    assert j == approx(jh)
    assert len(sec_run.method[1].x_w2dynamics_config.x_w2dynamics_config_general) == 58
    assert sec_run.method[1].x_w2dynamics_config.x_w2dynamics_config_general.x_w2dynamics_beta == 60.0
    assert sec_run.method[1].starting_method_ref == sec_run.method[0]
    sec_dmft = sec_run.method[1].dmft
    assert sec_dmft.n_correlated_bands == 3
    assert sec_dmft.n_correlated_electrons == approx(1.0)
    assert sec_dmft.inverse_temperature == approx(sec_run.method[1].x_w2dynamics_config.x_w2dynamics_config_general.x_w2dynamics_beta)
    assert sec_run.x_w2dynamics_axes.x_w2dynamics_iw.shape[0] == approx(2 * sec_dmft.n_matsubara_freq)
    assert sec_run.x_w2dynamics_axes.x_w2dynamics_tau.shape[0] == approx(sec_dmft.n_tau)
    assert sec_dmft.impurity_solver == 'CT-HYB'

    # Calculation tests
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    assert sec_scc.system_ref == sec_run.system[0]
    assert sec_scc.method_ref == sec_run.method[1]
    sec_gfs = sec_scc.greens_functions[0]
    assert sec_gfs.matsubara_freq[0] == approx(-125.61134626603189)
    assert sec_gfs.matsubara_freq[-1] == approx(125.61134626603189)
    assert sec_gfs.self_energy_iw.dtype == 'complex128'
    assert sec_gfs.self_energy_iw.shape == (3, 2, 2400)
    assert sec_gfs.greens_function_iw[2][0][1450] == approx(-0.0019482734893255288 - 0.03783597807548039j)
    assert sec_gfs.chemical_potential == approx(7.877904086990344)
    # SCF tests
    sec_scf = sec_scc.scf_iteration
    assert len(sec_scf) == 11
    assert sec_scf[0].energy.fermi.to('eV').magnitude == approx(7.877920164769436)
    assert sec_scf[-1].energy.fermi.to('eV').magnitude == approx(7.877904086990344)
    assert sec_scf[1].x_w2dynamics_ineq[0].x_w2dynamics_fiw.dtype == 'complex128'
    assert sec_scf[1].x_w2dynamics_ineq[0].x_w2dynamics_fiw.shape == (3, 2, 2400)
    assert sec_scf[10].x_w2dynamics_ineq[0].x_w2dynamics_fiw[1][1][100] == approx(-2.4387509114487393e-05 - 0.0026711105507501998j)
