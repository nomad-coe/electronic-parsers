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
from electronicparsers.edmft import EDMFTParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return EDMFTParser()


def test_lanio2_u7_singlepoint(parser):
    archive = EntryArchive()
    parser.parse('tests/data/edmft/LaNiO2_u7_singlepoint/dmft_info.out', archive, None)

    # Run tests
    assert len(archive.run) == 1
    sec_run = archive.run[-1]
    assert sec_run.program.name == 'eDMFT'
    # System tests
    assert len(sec_run.system) == 1
    sec_system = sec_run.system[-1]
    assert sec_system.atoms.labels == ['La', 'Ni', 'O', 'O']
    assert sec_system.atoms.periodic == [True, True, True]
    assert sec_system.atoms.positions[0][0].magnitude == approx(1.97950000708e-10)
    # Method tests
    assert len(sec_run.method) == 2
    #   Initial model
    sec_init_model = sec_run.method[0]
    assert len(sec_init_model.atom_parameters) == 1
    assert sec_init_model.atom_parameters[0].label == 'Ni'
    assert sec_init_model.atom_parameters[0].n_orbitals == 5
    assert sec_init_model.atom_parameters[0].orbitals == [
        'dz^2',
        'dx^2-y^2',
        'dxz',
        'dyz',
        'dxy',
    ]
    sec_hubbard = sec_init_model.atom_parameters[0].hubbard_kanamori_model
    assert sec_hubbard.double_counting_correction == 'exactd'
    assert sec_hubbard.u.to('eV').magnitude == approx(7.0)
    assert sec_hubbard.jh.to('eV').magnitude == approx(1.0)
    up_interaction = (
        sec_hubbard.u.to('eV').magnitude - 2 * sec_hubbard.jh.to('eV').magnitude
    )
    j_interaction = sec_hubbard.jh.to('eV').magnitude
    assert sec_hubbard.up.to('eV').magnitude == approx(up_interaction)
    assert sec_hubbard.j.to('eV').magnitude == approx(j_interaction)
    #   DMFT
    sec_dmft = sec_run.method[1]
    assert sec_dmft.starting_method_ref == sec_init_model
    assert sec_dmft.dmft.impurity_solver == 'CT-HYB'
    assert sec_dmft.dmft.n_impurities == 1
    assert sec_dmft.dmft.n_correlated_orbitals == [
        sec_init_model.atom_parameters[0].n_orbitals
    ]
    assert sec_dmft.dmft.n_electrons == [8.0]
    assert sec_dmft.dmft.magnetic_state == 'paramagnetic'
    assert sec_dmft.dmft.inverse_temperature.to('1/eV').magnitude == approx(23.2)
    # Calculation tests (testing last one)
    assert len(sec_run.calculation) == 7
    sec_scc_last = sec_run.calculation[-1]
    assert sec_scc_last.system_ref == sec_system
    assert sec_scc_last.method_ref == sec_dmft
    assert len(sec_scc_last.scf_iteration) == 2
    assert len(sec_scc_last.scf_iteration[1].charges) == 2
    assert sec_scc_last.scf_iteration[1].charges[0].kind == 'lattice'
    assert sec_scc_last.scf_iteration[1].charges[0].n_atoms == 1
    assert sec_scc_last.scf_iteration[1].charges[0].n_orbitals == 5
    assert sec_scc_last.scf_iteration[1].charges[0].n_electrons[0] == approx(8.476712)
    assert sec_scc_last.scf_iteration[1].charges[1].kind == 'impurity'
    assert sec_scc_last.scf_iteration[1].charges[1].n_electrons[0] == approx(8.475371)
    sec_gfs = sec_scc_last.greens_functions
    assert len(sec_gfs) == 3
    assert sec_gfs[0].type == 'impurity'
    assert sec_gfs[1].type == 'lattice'
    assert sec_gfs[2].type == sec_gfs[1].type
    assert sec_gfs[1].greens_function_iw.shape == (1, 2, 5, 397)
    assert sec_gfs[1].greens_function_iw[0][0][0][2] == approx(
        0.25737472001 - 0.253983463147j
    )
