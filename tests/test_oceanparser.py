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


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return OceanParser()


def test_tio2(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ocean/ms-10734/Spectra-1-1-1/postDefaultsOceanDatafile', archive, None)

    sec_run = archive.run[0]

    # Program
    assert sec_run.program.name == 'OCEAN'
    assert sec_run.program.version == '3.0.1'
    assert sec_run.program.x_ocean_original_dft_code == 'QuantumESPRESSO'
    assert sec_run.program.x_ocean_commit_hash == 'b4307fbb42993e2ddead42d6bce528c0b83a25cb'

    # System
    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels[0] == 'Ti'
    assert sec_system.atoms.labels[4] == 'O'
    assert sec_system.atoms.positions[0][0].magnitude == approx(1.6666840232882102e-10)

    # Method
    sec_method = sec_run.method
    assert len(sec_method) == 1
    assert (sec_method[0].k_mesh.grid == np.array([1, 1, 1])).all()
    sec_bse = sec_method[0].bse
    assert sec_bse.type == 'lanczos-haydock'
    assert sec_bse.mode == 'absorption'
    assert sec_bse.n_empty_states == 119
    assert sec_bse.core_level == 'K'
    assert sec_bse.core_hole_broadening == approx(0.89)
    assert sec_bse.screening_type == 'core'
    assert sec_bse.dielectric_infinity == 1000000
    assert sec_bse.n_empty_states_screening == 472
    assert (sec_bse.k_mesh_screening.grid == np.array([3, 3, 2])).all()
    assert (sec_method[0].x_ocean_edges[0] == np.array([1, 1, 0])).all()
    assert len(sec_method[0].x_ocean_photon) == 3
    assert sec_method[0].x_ocean_photon[0].x_ocean_photon_energy.magnitude == approx(sec_method[0].x_ocean_photon[1].x_ocean_photon_energy.magnitude)
    sec_ocean_screen = sec_method[0].x_ocean_screen
    assert sec_ocean_screen.m_mod_count == 22
    assert sec_ocean_screen.x_ocean_dft_energy_range == approx(150.0)

    # Calculation
    sec_scc = sec_run.calculation
    assert len(sec_scc) == 3
    assert sec_scc[0].m_xpath('spectra')
    sec_spectra = sec_scc[0].spectra[0]
    assert sec_spectra.type == 'XAS'
    assert sec_spectra.n_energies == 1001
    assert sec_spectra.excitation_energies[0].magnitude == approx(-3.204353268e-18)
    assert sec_spectra.intensities[0] == approx(9.99366e-09)
    assert sec_scc[0].m_xpath('x_ocean_lanczos')
    sec_lanczos = sec_scc[0].x_ocean_lanczos[0]
    assert sec_lanczos.x_ocean_n_tridiagonal_matrix == 70
    assert sec_lanczos.x_ocean_scaling_factor == approx(8.99182993377932e-07)
    assert sec_lanczos.x_ocean_tridiagonal_matrix[22][0] == approx(1.1278299324258296)
    assert sec_lanczos.x_ocean_eigenvalues[22][-1] == approx(0.6462608405)
