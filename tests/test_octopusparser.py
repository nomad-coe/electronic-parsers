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
from electronicparsers.octopus import OctopusParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return OctopusParser()


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/octopus/Si_scf/stdout.txt', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == 'wolfi'
    assert sec_run.x_octopus_input_Spacing == approx(0.28345892)
    assert sec_run.x_octopus_parserlog_SpeciesProjectorSphereThreshold == 0.001

    sec_method = sec_run.method[0]
    assert list(sec_method.k_mesh.grid) == [4] * 3
    assert sec_method.electronic.smearing.kind == 'empty'
    assert sec_method.electronic.method == 'DFT'
    assert sec_method.dft.xc_functional.correlation[0].name == 'LDA_C_PZ_MOD'

    sec_system = sec_run.system[0]
    assert False not in sec_system.atoms.periodic
    assert sec_system.atoms.labels == ['Si', 'Si', 'Si', 'Si']
    assert sec_system.atoms.positions[1][0].magnitude == approx(1.91979671e-10)

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-6.91625667e-17)
    assert sec_scc.energy.electrostatic.value.magnitude == approx(4.79087203e-18)
    assert np.count_nonzero(sec_scc.forces.free.value_raw) == 0
    sec_eig = sec_scc.eigenvalues[0]
    assert np.shape(sec_eig.energies[0][17]) == (8,)
    assert sec_eig.kpoints[11][2] == 0.25
    assert sec_eig.energies[0][4][6].magnitude == approx(5.26639723e-19)
    assert sec_eig.occupations[0][16][1] == 2.0
    sec_scf = sec_scc.scf_iteration
    assert len(sec_scf) == 8
    assert sec_scf[3].energy.total.value.magnitude == approx(-6.91495422e-17)
    assert sec_scf[7].time_calculation.magnitude == 9.42
    assert sec_scf[2].time_physical.magnitude == approx(127.9)
    assert sec_scc.time_physical.magnitude == approx(298.09)
    assert sec_scc.time_calculation.magnitude == approx(298.09)


def test_spinpol(parser):
    archive = EntryArchive()
    parser.parse('tests/data/octopus/Fe_spinpol/stdout.txt', archive, None)

    sec_run = archive.run[0]
    assert sec_run.x_octopus_parserlog_SpinComponents == '2'
    assert sec_run.x_octopus_input_Units == 'ev_angstrom'
    assert sec_run.x_octopus_parserlog_PreconditionerFilterFactor == 0.6

    sec_method = sec_run.method[0]
    assert list(sec_method.k_mesh.grid) == [4] * 3

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.fermi.magnitude == approx(7.39160185e-19)
    sec_eig = sec_scc.eigenvalues[0]
    assert np.shape(sec_eig.energies[1][9]) == (20,)
    assert sec_eig.energies[1][5][4].magnitude == approx(-7.40576381e-18)
    assert sec_eig.kpoints[9][0] == 0.5
    assert sec_eig.occupations[0][1][17] == 0.972222
    sec_scfs = sec_scc.scf_iteration
    assert sec_scfs[0].energy.total.value.magnitude == approx(-1.02450582e-15)
    assert sec_scfs[5].energy.fermi.magnitude == approx(7.85685151e-19)
    assert sec_scfs[8].time_calculation.magnitude == 15.63


def test_geomopt(parser):
    # cannot find example
    pass


def test_td(parser):
    # cannot find example
    pass
