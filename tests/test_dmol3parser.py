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
from electronicparsers.dmol3 import Dmol3Parser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return Dmol3Parser()


def test_optimization(parser):
    archive = EntryArchive()

    parser.parse('tests/data/dmol3/h2o.outmol', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '3.0'
    assert sec_run.time_run.date_start > 0.0

    sec_method = archive.run[0].method[0]
    assert sec_method.x_dmol3_calculation_type == 'optimize_frequency'
    assert sec_method.x_dmol3_rcut == approx(6.0)
    assert sec_method.x_dmol3_scf_iterations == 150
    assert sec_method.x_dmol3_occupation_name == 'Fermi'
    assert sec_method.x_dmol3_diis_number == 10
    assert sec_method.x_dmol3_diis_name == 'pulay'
    assert sec_method.x_dmol3_opt_energy_convergence == approx(1.0e-05)

    sec_system = archive.run[0].system
    assert len(sec_system) == 11
    assert sec_system[0].atoms.labels[2] == 'H'
    assert sec_system[2].atoms.positions[1][2].magnitude == approx(
        -8.84266338e-10,
    )

    sec_calc = sec_run.calculation
    assert sec_calc[7].energy.total.value.magnitude == approx(-3.33238073e-16)
    assert sec_calc[2].energy.x_dmol3_binding.value.magnitude == approx(-1.66336861e-18)
    assert len(sec_calc[5].scf_iteration) == 7
    assert sec_calc[1].scf_iteration[2].energy.total.value.magnitude == approx(
        -3.33238086e-16
    )
    assert sec_calc[5].scf_iteration[
        5
    ].energy.x_dmol3_binding.value.magnitude == approx(-1.66332632e-18)
    assert sec_calc[0].eigenvalues[0].energies[0][0][4].magnitude == approx(
        -1.08436443e-18
    )
    assert sec_calc[0].eigenvalues[0].occupations[0][0][2] == approx(2.0)
    assert sec_calc[1].charges[0].value[0].magnitude == approx(-4.82255167e-20)
    assert sec_calc[1].charges[1].value[2].magnitude == approx(3.89328922e-20)
    assert sec_calc[1].multipoles[0].dipole.total == approx(1.9470)
    assert sec_calc[10].vibrational_frequencies[0].value[2].magnitude == approx(-1050.0)
    assert sec_calc[10].vibrational_frequencies[0].x_dmol3_normal_modes[5][2][
        0
    ] == approx(-0.1073)
    assert sec_calc[10].x_dmol3_h_rot == approx(0.889)
    assert sec_calc[10].x_dmol3_c_vib == approx(5.816)
    assert sec_calc[3].time_physical.magnitude == approx(0.150 * 60)
    assert sec_calc[7].time_calculation.magnitude == approx(0.6)

    sec_workflow = archive.workflow2
    # TODO handle multiple workflow sections
    # assert sec_workflow.method.convergence_tolerance_energy_difference.magnitude == approx(4.35974472e-23)
    # assert sec_workflow.method.convergence_tolerance_force_maximum.magnitude == approx(8.2387235e-12)
    # assert sec_workflow.method.convergence_tolerance_displacement_maximum.magnitude == approx(1.58753163e-13)
    assert sec_workflow.results.temperature[22].magnitude == approx(550.00)
    assert sec_workflow.results.entropy[32].magnitude == approx(5.15393944e-22)
    assert sec_workflow.results.heat_capacity_c_p[40].magnitude == approx(
        1.08988499e-22
    )
    # TODO uncomment this after merging workflow changes
    # assert sec_workflow[1].thermodynamics.enthalpy[7].magnitude == approx(1.1136461e-19)
    assert sec_workflow.results.gibbs_free_energy[20].magnitude == approx(
        -9.34881901e-20
    )
