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

import sys
import pytest

from nomad.datamodel import EntryArchive
from electronicparsers.cpmd import CPMDParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return CPMDParser()


def test_single_point(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cpmd/single_point/output.out', archive, None)

    run = archive.run[0]
    assert run.program.version == '4.1-rUnversioned directory'
    assert run.time_run.date_start > 0.
    sec_info = run.x_cpmd_section_start_information[0]
    assert sec_info.x_cpmd_compilation_date == 'Jun 22 2016 -- 12:41:05'
    assert sec_info.x_cpmd_process_id == 32589
    assert sec_info.x_cpmd_input_filename == 'input.inp'

    sec_system = run.system
    assert sec_system[0].atoms.labels == ['H', 'H']
    assert sec_system[0].atoms.positions[1][2].magnitude == approx(3.99999974e-10)
    assert sec_system[0].atoms.lattice_vectors[2][2].magnitude == approx(7.99999524e-10)

    sec_calc = run.calculation
    assert sec_calc[0].energy.total.value.magnitude == approx(-4.78219396e-18)
    assert sec_calc[0].energy.xc.value.magnitude == approx(-2.50324989e-18)

    sec_method = run.method
    assert sec_method[0].basis_set[0].cell_dependent[0].name == 'PW_70.0'
    assert sec_method[0].x_cpmd_simulation_parameters['TIME STEP FOR ELECTRONS'] == 5.0
    assert sec_method[0].x_cpmd_simulation_parameters['MAXIMUM NUMBER OF ITERATIONS FOR SC'] == 10000


def test_geometry_optimization(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cpmd/geo_opt/output.out', archive, None)

    sec_system = archive.run[0].system
    assert len(sec_system) == 5
    assert sec_system[2].atoms.positions[0][1].magnitude == approx(3.99999762e-10)

    sec_calc = archive.run[0].calculation
    assert sec_calc[2].energy.total.value.magnitude == approx(-4.93913736e-18)
    assert sec_calc[4].energy.electrostatic.value.magnitude == approx(-2.14706759e-18)
    assert sec_calc[4].forces.total.value[1][2].magnitude == approx(1.09986959e-23)
    assert sec_calc[2].scf_iteration[0].energy.total.value.magnitude == approx(-4.93903272e-18)
    assert sec_calc[3].scf_iteration[4].energy.change.magnitude == approx(-6.80556151e-30)


def test_molecular_dynamics(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cpmd/md/output.out', archive, None)

    system = archive.run[0].system
    assert len(system) == 50
    assert system[1].atoms.positions[1][0].magnitude == approx(-3.72683727e-11)
    assert system[28].atoms.positions[1][1].magnitude == approx(-1.42764129e-12)
    assert system[34].atoms.velocities[1][2].magnitude == approx(-549.239774)
    assert system[5].atoms.labels == ['H', 'H']
    assert system[40].atoms.lattice_vectors[2][2].magnitude == approx(7.99999524e-10)

    calc = archive.run[0].calculation
    assert len(calc) == 50
    assert calc[14].energy.total.value.magnitude == approx(-4.78447105e-18)
    assert calc[39].energy.total.potential.magnitude == approx(-4.86144243e-18)
    assert calc[41].energy.total.kinetic.magnitude == approx(6.61026239e-20)
    assert calc[8].temperature.magnitude == approx(71.351)

    md = archive.workflow[0].molecular_dynamics
    assert md.ensemble_type == 'NVE'
    assert md.x_cpmd_section_md_averaged_quantities[0].x_cpmd_density_functional_energy_mean == approx(-1.115075)
    assert md.x_cpmd_section_md_averaged_quantities[0].x_cpmd_ion_displacement_std == approx(.193303E-02)