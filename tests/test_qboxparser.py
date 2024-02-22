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
from electronicparsers.qbox import QboxParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return QboxParser()


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/qbox/01_h2ogs.r', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '1.63.2'
    assert sec_run.time_run.date_start > 0
    assert sec_run.time_run.date_end > 0

    sec_method = sec_run.method
    assert sec_method[0].x_qbox_input_parameters['ecut'] == 70

    sec_system = sec_run.system
    assert len(sec_system) == 1
    assert sec_system[0].atoms.labels == ['O', 'H', 'H']
    assert sec_system[0].atoms.positions[1][1].magnitude == approx(7.64131893e-11)
    assert sec_system[0].atoms.lattice_vectors[2][2].magnitude == approx(8.46683537e-10)
    assert sec_system[0].atoms.velocities[1][2].magnitude == approx(0.0)

    sec_scc = sec_run.calculation
    assert len(sec_scc) == 1
    assert sec_scc[0].energy.total.value.magnitude == approx(-7.44295025e-17)
    assert sec_scc[0].energy.xc.value.magnitude == approx(-1.78424213e-17)
    assert sec_scc[0].energy.x_qbox_sr.value.magnitude == approx(6.4166003e-18)
    assert sec_scc[0].forces.total.value[1][2].magnitude == approx(-3.3968257e-12)
    assert sec_scc[0].system_ref == sec_system[0]
    sec_scf = sec_scc[0].scf_iteration
    assert len(sec_scf) == 100
    assert sec_scf[48].energy.total.value.magnitude == approx(-7.23408056e-17)
    assert sec_scf[68].energy.sum_eigenvalues.value.magnitude == approx(-8.94829281e-18)


def test_relax(parser):
    archive = EntryArchive()
    parser.parse('tests/data/qbox/02_h2ocg.r', archive, None)

    sec_run = archive.run[0]

    sec_system = sec_run.system
    assert len(sec_system) == 20
    assert sec_system[4].atoms.positions[0][2].magnitude == approx(-5.87915881e-16)
    assert sec_system[7].atoms.lattice_vectors[1][1].magnitude == approx(8.46683537e-10)

    sec_scc = sec_run.calculation
    assert len(sec_scc) == 20
    assert sec_scc[11].energy.total.value.magnitude == approx(-7.44306125e-17)
    assert sec_scc[18].energy.kinetic_electronic.value.magnitude == approx(
        5.37898452e-17
    )
    assert len(sec_scc[6].scf_iteration) == 10
    assert sec_scc[7].time_calculation.magnitude == approx(1.475)
    assert sec_scc[2].time_physical.magnitude == approx(4.269)


def test_stress(parser):
    archive = EntryArchive()
    parser.parse('tests/data/qbox/03_si2gs.r', archive, None)

    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 30
    assert sec_scc[24].stress.total.value[2][1].magnitude == approx(-20.0)
    assert len(sec_scc[11].stress.contributions) == 7
    assert sec_scc[11].stress.contributions[1].kind == 'conf'
    assert sec_scc[11].stress.contributions[5].value[2][2].magnitude == approx(
        -2680230.0
    )


def test_multipoles(parser):
    archive = EntryArchive()
    parser.parse('tests/data/qbox/10_efield.r', archive, None)

    sec_scc = archive.run[3].calculation
    assert sec_scc[0].multipoles[0].dipole.total[2] == approx(0.0977781797)
    assert sec_scc[0].multipoles[0].quadrupole.total[8] == approx(-32.83786426)
    assert sec_scc[0].x_qbox_section_MLWF[3].x_qbox_geometry_MLWF_atom_positions[
        0
    ].magnitude == approx(-9.20548723e-11)
    assert sec_scc[0].x_qbox_section_MLWF[
        6
    ].x_qbox_geometry_MLWF_atom_spread.magnitude == approx(1.34165266e-10)


def test_dft(parser):
    archive = EntryArchive()
    parser.parse('tests/data/qbox/12_h2o_64_gs.r', archive, None)

    sec_xc = archive.run[0].method[0].dft.xc_functional
    assert sec_xc.exchange[0].name == 'GGA_X_PBE'
    assert sec_xc.correlation[0].name == 'GGA_C_PBE'
