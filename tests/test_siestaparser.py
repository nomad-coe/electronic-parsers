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
from electronicparsers.siesta import SiestaParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return SiestaParser()


def test_single_point(parser):
    archive = EntryArchive()

    parser.parse('tests/data/siesta/Fe/out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == 'siesta-4.0--500'
    assert sec_run.x_siesta_compiler_flags == 'mpiifort -O2'
    assert sec_run.x_siesta_parallel
    assert sec_run.x_siesta_n_nodes == 2
    assert sec_run.time_run.date_end > 0.0

    sec_method = sec_run.method
    assert sec_method[0].x_siesta_input_parameters['DM.MixingWeight'] == approx(0.1)
    assert sec_method[0].x_siesta_input_parameters['SpinPolarized']
    assert sec_method[0].x_siesta_input_parameters['PAO.EnergyShift'] == 50
    assert sec_method[0].x_siesta_input_parameters['SystemName'] == 'bcc Fe ferro GGA'
    assert sec_method[0].x_siesta_simulation_parameters[
        'DM (free)Energy tolerance for SCF'
    ] == approx(0.00001)
    assert sec_method[0].dft.xc_functional.exchange[0].name == 'GGA_X_PBE'

    sec_system = archive.run[0].system
    assert sec_system[0].atoms.lattice_vectors[2][2].magnitude == approx(-1.435e-10)
    assert sec_system[0].atoms.labels[0] == 'Fe'

    sec_scc = sec_run.calculation
    assert sec_scc[0].energy.total.value.magnitude == approx(-1.25329082e-16)
    assert len(sec_scc[0].energy.contributions) == 14
    assert sec_scc[0].energy.contributions[2].kind == 'Ena'
    assert sec_scc[0].energy.contributions[4].value.magnitude == approx(-7.51141294e-17)
    sec_scf = sec_scc[0].scf_iteration
    assert len(sec_scf) == 24
    assert sec_scf[7].energy.total.value.magnitude == approx(-1.25327159e-16)
    assert sec_scf[11].energy.types[0].value.magnitude == approx(-1.25328953e-16)
    assert sec_scc[1].energy.sum_eigenvalues.value.magnitude == approx(-1.03934823e-17)
    assert sec_scc[1].energy.contributions[2].kind == 'Ion-electron'
    assert sec_scc[1].energy.total.value.magnitude == approx(-1.25329082e-16)
    assert sec_scc[1].stress.total.value[2][0].magnitude == approx(-5.20547188e08)
    assert sec_scc[1].charges[0].orbital_projected[8].orbital == '3dyz'
    assert sec_scc[1].charges[0].orbital_projected[25].value.magnitude == approx(
        -8.01088317e-21
    )
    assert sec_scc[1].charges[0].spin_projected[1].value.magnitude == approx(
        4.55338599e-19
    )
    assert sec_scc[1].charges[0].value[0].magnitude == approx(1.28174131e-18)


def test_relax(parser):
    archive = EntryArchive()

    parser.parse('tests/data/siesta/H2O-relax/out', archive, None)

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 7
    assert sec_systems[3].atoms.lattice_vectors[1][1].magnitude == approx(5.692925e-10)
    assert sec_systems[6].atoms.positions[2][0].magnitude == approx(-7.6940893e-11)
    assert sec_systems[0].atoms.labels[0] == 'O'

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 8
    assert sec_sccs[5].energy.total.value.magnitude == approx(-7.48200466e-17)
    assert sec_sccs[1].energy.total.value.magnitude == approx(-7.47758426e-17)
    assert sec_sccs[2].forces.total.value[1][1].magnitude == approx(-2.06092787e-10)
    assert sec_sccs[7].multipoles[0].dipole.total[1] == approx(1.362042)
