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
from electronicparsers.nwchem import NWChemParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return NWChemParser()


def test_single_point(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/single_point.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '6.6'
    assert sec_run.x_nwchem_section_start_information[0].x_nwchem_ga_revision == '10594'

    sec_method = archive.run[0].method[0]
    assert sec_method.electrons_representation[0].basis_set[0].type == 'gaussians'
    assert sec_method.scf.n_max_iteration == 50
    assert len(sec_method.dft.xc_functional.correlation) == 1
    assert sec_method.dft.xc_functional.correlation[0].name == 'MGGA_C_TPSS'
    assert sec_method.dft.xc_functional.exchange[0].weight == 1.0

    assert archive.workflow2.m_def.name == 'SinglePoint'

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-3.332424186333889e-16)
    assert sec_scc.x_nwchem_energy_one_electron == approx(-5.35955587575652e-16)
    assert sec_scc.forces.total.value[2][0].magnitude == approx(-4.9432341e-13)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 6
    assert sec_scfs[2].energy.total.value.magnitude == approx(-3.33233301e-16)
    # uncomment this when time_physical def is updated
    # assert sec_scfs[5].time_physical.magnitude == 0.3
    assert sec_scfs[4].energy.change.magnitude == approx(-7.45516347e-23)

    sec_system = archive.run[0].system[0]
    assert len(sec_system.atoms.labels) == 3
    assert sec_system.atoms.positions[0][2].magnitude == approx(-1.1817375e-11)


def test_geometry_optimization(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/geometry_optimization.out', archive, None)

    sec_methods = archive.run[0].method
    assert len(sec_methods) == 4
    assert sec_methods[1].scf.threshold_energy_change.magnitude == approx(
        4.35974472e-24
    )

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 4
    assert sec_sccs[0].energy.correlation.value.magnitude == approx(-1.42869721e-18)
    assert sec_sccs[1].forces.total.value[2][2].magnitude == approx(-2.20633015e-10)
    assert len(sec_sccs[2].scf_iteration) == 4
    assert sec_sccs[0].time_physical.magnitude == approx(0.4)
    assert sec_sccs[1].scf_iteration[1].time_calculation.magnitude == approx(0.1)
    assert sec_sccs[2].scf_iteration[3].time_physical.magnitude == approx(1.6)
    assert sec_sccs[3].time_calculation.magnitude == approx(0.3)

    sec_systems = archive.run[0].system
    assert sec_systems[0].atoms.positions[1][2].magnitude == approx(5.6568542e-11)
    assert sec_systems[3].atoms.periodic == [False, False, False]


def test_molecular_dynamics(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/molecular_dynamics.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 6
    assert sec_sccs[2].energy.xc.value.magnitude == approx(-4.04565658e-17)
    assert sec_sccs[5].x_nwchem_section_qmd_step[
        0
    ].x_nwchem_qmd_step_total_energy.magnitude == approx(-3.32745352e-16)
    assert sec_sccs[2].x_nwchem_section_qmd_step[0].x_nwchem_qmd_step_dipole[
        1
    ] == approx(1.141435e-01)
    assert sec_sccs[2].time_calculation.magnitude == approx(0.4)
    assert sec_sccs[4].time_physical.magnitude == approx(1.8)


def test_pw(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/pw.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert sec_sccs[1].energy.total.value.magnitude == approx(-8.89979631e-17)
    assert sec_sccs[1].spin_S2 == approx(2.0029484134705502)
    sec_scfs = sec_sccs[0].scf_iteration
    assert len(sec_scfs) == 5
    assert sec_scfs[3].energy.total.value.magnitude == approx(-8.86651108e-17)
