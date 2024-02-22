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
    assert (
        sec_run.program.x_soliddmft_hash == 'ae0794c4e3678d367ad340b25e1a64a5c0f23a9f'
    )

    # System tests (SrVO3 crystal)
    # unknown: we need this info from the devs

    # Method tests
    assert (
        len(sec_run.method) == 2
    )  # 2 methods: [0] input Hamiltonian, [1] input DMFT parameters

    # input Hamiltonian
    sec_input_model = sec_run.method[0]
    assert (
        sec_input_model.atom_parameters
        and sec_input_model.x_soliddmft_projection_matrix is not None
    )
    assert sec_input_model.x_soliddmft_projection_matrix.shape == (729, 1, 3, 5)
    assert len(sec_input_model.atom_parameters) == 1
    assert sec_input_model.atom_parameters[0].atom_index == 2
    assert sec_input_model.atom_parameters[0].n_orbitals == 3
    assert sec_input_model.atom_parameters[0].orbitals == ['d0', 'd1', 'd2']
    hubbard_model = sec_input_model.atom_parameters[0].hubbard_kanamori_model
    assert hubbard_model.double_counting_correction == 'held_formula'
    u_int = hubbard_model.u.to('eV').magnitude
    jh_int = hubbard_model.jh.to('eV').magnitude
    up_int = hubbard_model.up.to('eV').magnitude
    j_int = hubbard_model.j.to('eV').magnitude
    assert u_int == approx(8.0)
    assert jh_int == approx(0.65)
    # testing rotational invariance
    assert up_int == approx(u_int - 2 * jh_int)
    assert j_int == jh_int

    # input DMFT
    assert (
        isinstance(sec_run.method[1].x_soliddmft_general_params, dict)
        and len(sec_run.method[1].x_soliddmft_general_params) == 48
    )
    assert len(sec_run.method[1].x_soliddmft_solver_params) == 15
    assert len(sec_run.method[1].x_soliddmft_advanced_params) == 6
    assert sec_run.method[1].starting_method_ref == sec_run.method[0]
    sec_dmft = sec_run.method[1].dmft
    assert sec_dmft.n_impurities == 1
    assert sec_dmft.n_correlated_orbitals[0] == 3
    assert sec_dmft.n_electrons[0] == approx(1.0000225214138097)
    assert sec_dmft.inverse_temperature.to('1/eV').magnitude == approx(10.0)
    assert sec_dmft.impurity_solver == 'CT-HYB'
    sec_k_mesh = sec_run.method[1].k_mesh
    assert sec_k_mesh.n_points == 729
    assert (
        len(sec_run.method[1].frequency_mesh) == 1
        and len(sec_run.method[1].time_mesh) == 1
    )
    sec_freq_mesh = sec_run.method[1].frequency_mesh[0]
    assert sec_freq_mesh.n_points == 501
    assert sec_freq_mesh.points[15][0].to('eV').magnitude == approx(-97.10000000000001j)
    sec_time_mesh = sec_run.method[1].time_mesh[0]
    assert sec_time_mesh.n_points == 10001
    assert sec_time_mesh.points[76][0] == approx(0.076j)

    # Calculation tests
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    # assert sec_scc.system_ref == sec_run.system[0]
    assert sec_scc.method_ref == sec_run.method[1]
    assert sec_scc.energy.chemical_potential.to('eV').magnitude == approx(
        0.050287075199847694
    )
    assert len(sec_scc.energy.double_counting.values_per_atom.to('eV').magnitude) == 1
    assert sec_scc.energy.double_counting.values_per_atom.to('eV').magnitude[
        0
    ] == approx(7.544843542949807e-05)
    # Greens functions tests
    sec_gfs = sec_scc.greens_functions[0]
    assert sec_gfs.matsubara_freq[0] == approx(-100.1)
    assert sec_gfs.matsubara_freq[-1] == approx(100.1)
    assert sec_gfs.tau.shape[0] == sec_time_mesh.n_points
    assert sec_gfs.self_energy_iw.dtype == 'complex128'
    assert sec_gfs.self_energy_iw.shape == (1, 2, 3, 1002)
    assert sec_gfs.greens_function_tau[0][1][1][1025] == approx(
        0.14109113749664728 + 0j
    )
    assert sec_gfs.chemical_potential.to('eV').magnitude == approx(0.050287075199847694)
    assert np.sum(sec_gfs.orbital_occupations) == approx(1.008321846227956)
    assert sec_gfs.quasiparticle_weights.shape == (1, 2, 3)
    assert sec_gfs.quasiparticle_weights[0][0][0] == approx(0.16195076915540912)


def test_lacu2o4_real_freq(parser):
    archive = EntryArchive()
    parser.parse('tests/data/soliddmft/lacu2o4/lco.h5', archive, None)

    # Run tests
    assert len(archive.run) == 1
    sec_run = archive.run[-1]
    # Program tests
    assert sec_run.program.name == 'solid_dmft'
    assert sec_run.program.version == '3.2.0'
    assert (
        sec_run.program.x_soliddmft_hash == '707c012359758d3aca1ce46e3446312df86ca5d6'
    )

    # Real frequency and MPS solver test
    sec_freq_mesh = sec_run.method[1].frequency_mesh
    assert len(sec_freq_mesh) == 1
    assert sec_freq_mesh[0].n_points == 3001
    assert np.isreal(sec_freq_mesh[0].points.to('eV').magnitude).all()
    sec_dmft = sec_run.method[1].dmft
    assert sec_dmft.impurity_solver == 'MPS'

    # SCF and Calculation tests
    sec_scc = sec_run.calculation[-1]
    assert sec_scc.dos_electronic
    assert sec_scc.dos_electronic[0].kind == 'spectral'
    assert sec_scc.dos_electronic[0].n_energies == 3001
    assert sec_scc.m_xpath('greens_functions[0].frequencies') is not None
    assert sec_scc.m_xpath('greens_functions[0].greens_function_freq') is not None
    # NOTE: scf steps are not parsed because they require archive.m_context, so we cannot
    # test it here.
