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
from electronicparsers.ocean import OceanParser
from electronicparsers.ocean.metainfo.ocean import x_ocean_screen_parameters


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return OceanParser()


def test_tio2(parser):
    # Testing the photon_workflow_archive, from empty photon_archives, hence no sections program nor system.
    archive = EntryArchive()
    parser.parse(
        'tests/data/ocean/ms-10734/Spectra-1-1-1/postDefaultsOceanDatafile',
        archive,
        None,
    )

    sec_run = archive.run[-1]

    # Method
    sec_method = sec_run.method
    assert len(sec_method) == 1
    assert sec_method[-1].m_xpath('bse')
    sec_bse = sec_method[-1].bse
    assert sec_bse.type == 'Singlet'
    assert sec_bse.solver == 'Lanczos-Haydock'
    assert sec_bse.n_states == 119
    assert sec_bse.broadening.to('eV').magnitude == approx(0.1)
    assert (sec_bse.q_mesh.grid == np.array([1, 1, 1])).all()
    assert sec_bse.screening.type == 'core'
    assert sec_bse.screening.n_states == 472
    assert sec_bse.screening.dielectric_infinity == 1000000
    assert (sec_bse.screening.k_mesh.grid == np.array([3, 3, 2])).all()
    assert (sec_method[-1].x_ocean_edges[0] == np.array([1, 1, 0])).all()
    assert sec_bse.core_hole.solver == 'Lanczos-Haydock'
    assert sec_bse.core_hole.mode == 'absorption'
    assert sec_bse.core_hole.broadening.to('eV').magnitude == approx(0.89)

    sec_ocean_screen = sec_method[-1].x_ocean_screen
    for screen_param in x_ocean_screen_parameters.m_def.quantities:
        assert sec_ocean_screen.m_is_set(screen_param)
    assert sec_ocean_screen.x_ocean_dft_energy_range == approx(150.0)

    # Calculation
    sec_scc = sec_run.calculation
    assert len(sec_scc) == 0  # Calculation not populated in workflow2\
