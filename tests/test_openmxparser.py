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
import logging
import numpy as np
from datetime import datetime

from nomad.datamodel import EntryArchive
from nomad.units import ureg as units

from electronicparsers.openmx import OpenmxParser


@pytest.fixture
def parser():
    return OpenmxParser()


def A_to_m(value):
    return (value * units.angstrom).to_base_units().magnitude


def Ha_to_J(value):
    return (value * units.hartree).to_base_units().magnitude


def K_to_J(value):
    return (value * units.joule * units.k).to_base_units().magnitude


def HaB_to_N(value):
    return (value * units.hartree / units.bohr).to_base_units().magnitude


# default pytest.approx settings are abs=1e-12, rel=1e-6 so it doesn't work for small numbers
# use the default just for comparison with zero
def approx(value):
    return pytest.approx(value, abs=0, rel=1e-6)


def test_HfO2(parser):
    """
    Simple single point calculation monoclinic HfO2 test case.
    """
    archive = EntryArchive()
    parser.parse('tests/data/openmx/HfO2_single_point/m-HfO2.out', archive, logging)

    run = archive.run[0]
    assert run.program.version == '3.9.2'
    assert run.clean_end
    scc = run.calculation
    assert len(scc) == 1
    assert scc[0].energy.total.value.magnitude == approx(Ha_to_J(-346.328738171942))
    scf = scc[0].scf_iteration
    assert scc[0].stress is None
    assert len(scf) == 24
    scf[3].energy.sum_eigenvalues.value.magnitude == approx(-3.916702417016777e-16)

    method = run.method[0]
    assert method.electrons_representation[0].basis_set[0].type == 'numeric AOs'
    assert method.electronic.n_spin_channels == 1
    assert method.electronic.method == 'DFT'
    assert method.electronic.smearing.width == approx(K_to_J(300))
    assert method.dft.xc_functional.correlation[0].name == 'GGA_C_PBE'
    assert method.dft.xc_functional.exchange[0].name == 'GGA_X_PBE'

    system = run.system[0]
    assert system.atoms.periodic == [True, True, True]
    assert system.atoms.lattice_vectors[0][0].magnitude == approx(A_to_m(5.1156000))
    assert system.atoms.lattice_vectors[2][2].magnitude == approx(A_to_m(5.2269843))
    assert len(system.atoms.positions) == 12
    assert system.atoms.positions[5][0].magnitude == approx(A_to_m(-0.3293636))
    assert system.atoms.positions[11][2].magnitude == approx(A_to_m(2.6762159))
    assert len(system.atoms.labels) == 12
    assert system.atoms.labels[9] == 'O'


def test_AlN(parser):
    """
    Geometry optimization (atomic positions only) AlN test case.
    """
    archive = EntryArchive()
    parser.parse('tests/data/openmx/AlN_ionic_optimization/AlN.out', archive, logging)

    run = archive.run[0]
    assert run.program.version == '3.9.2'
    assert run.clean_end

    date_start_timestamp = datetime(2021, 4, 17, 18, 14, 52).timestamp()
    assert run.time_run.date_start.magnitude == date_start_timestamp

    date_end_timestamp = datetime(2021, 4, 17, 18, 19, 12, 811000).timestamp()
    assert run.time_run.date_end.magnitude == date_end_timestamp

    scc = run.calculation
    assert len(scc) == 5
    assert scc[0].energy.total.value.magnitude == approx(Ha_to_J(-25.194346653540))
    assert scc[4].energy.total.value.magnitude == approx(Ha_to_J(-25.194358042252))
    assert np.shape(scc[0].forces.total.value) == (4, 3)
    assert scc[0].forces.total.value[0][2].magnitude == approx(HaB_to_N(0.00139))
    assert scc[4].forces.total.value[3][2].magnitude == approx(HaB_to_N(-0.00018))
    scf = scc[0].scf_iteration
    assert len(scf) == 21
    scf[20].energy.sum_eigenvalues.value.magnitude == approx(-3.4038353611878345e-17)
    scf = scc[3].scf_iteration
    assert len(scf) == 6
    scf[5].energy.sum_eigenvalues.value.magnitude == approx(-3.4038520917173614e-17)

    method = run.method[0]
    assert method.electronic.n_spin_channels == 1
    assert method.electronic.method == 'DFT'
    assert method.electronic.smearing.width == approx(K_to_J(300))
    assert method.electronic.van_der_waals_method == ''
    assert method.dft.xc_functional.correlation[0].name == 'GGA_C_PBE'
    assert method.dft.xc_functional.exchange[0].name == 'GGA_X_PBE'
    assert method.scf.n_max_iteration == 100
    assert method.scf.threshold_energy_change.magnitude == approx(Ha_to_J(1e-7))

    workflow = archive.workflow2
    assert workflow.method.method == 'steepest_descent'
    assert workflow.method.optimization_steps_maximum == 50
    assert workflow.method.convergence_tolerance_force_maximum.magnitude == approx(
        (0.0003 * units.hartree / units.bohr).to_base_units().magnitude
    )

    assert len(run.system) == 5
    system = run.system[0]
    assert system.atoms.periodic == [True, True, True]
    assert system.atoms.lattice_vectors[0][0].magnitude == approx(A_to_m(3.10997))
    assert system.atoms.lattice_vectors[1][0].magnitude == approx(A_to_m(-1.55499))
    assert len(system.atoms.positions) == 4
    assert system.atoms.positions[0][0].magnitude == approx(A_to_m(1.55499))
    assert system.atoms.positions[3][2].magnitude == approx(A_to_m(4.39210))
    assert len(system.atoms.labels) == 4
    assert system.atoms.labels[3] == 'N'
    system = run.system[0]
    assert np.shape(system.atoms.velocities) == (4, 3)
    assert system.atoms.velocities[0][0].magnitude == pytest.approx(0.0)
    assert system.atoms.velocities[3][2].magnitude == pytest.approx(0.0)
    system = run.system[3]
    assert system.atoms.lattice_vectors[1][1].magnitude == approx(A_to_m(2.69331))
    assert system.atoms.lattice_vectors[2][2].magnitude == approx(A_to_m(4.98010))
    assert len(system.atoms.positions) == 4
    assert system.atoms.positions[0][1].magnitude == approx(A_to_m(0.89807))
    assert system.atoms.positions[2][2].magnitude == approx(A_to_m(1.90030))
    assert len(system.atoms.labels) == 4
    assert system.atoms.labels[0] == 'Al'
    system = run.system[4]
    assert system.atoms.lattice_vectors[0][0].magnitude == approx(A_to_m(3.10997))
    assert system.atoms.lattice_vectors[2][2].magnitude == approx(A_to_m(4.98010))
    assert len(system.atoms.positions) == 4
    assert system.atoms.positions[0][2].magnitude == approx(A_to_m(0.00253))
    assert system.atoms.positions[3][2].magnitude == approx(A_to_m(4.39015))
    assert len(system.atoms.labels) == 4
    assert system.atoms.labels[1] == 'Al'

    eigenvalues = run.calculation[-1].eigenvalues[0]
    assert eigenvalues.n_kpoints == 74
    assert np.shape(eigenvalues.kpoints) == (74, 3)
    assert eigenvalues.kpoints[0][0] == approx(-0.42857)
    assert eigenvalues.kpoints[0][2] == approx(-0.33333)
    assert eigenvalues.kpoints[73][2] == pytest.approx(0.0)
    assert np.shape(eigenvalues.energies) == (1, 74, 52)
    assert eigenvalues.energies[0, 0, 0].magnitude == approx(Ha_to_J(-0.77128985545768))
    assert eigenvalues.energies[0, 73, 51].magnitude == approx(
        Ha_to_J(4.86822333092339)
    )


def test_C2N2(parser):
    """
    Molecular dynamics using the Nose-Hover thermostat for simple N2H2 molecule
    """
    archive = EntryArchive()
    parser.parse('tests/data/openmx/C2H2_molecular_dynamics/C2H2.out', archive, logging)

    run = archive.run[0]
    assert run.program.version == '3.9.2'
    assert run.clean_end

    date_start_timestamp = datetime(2021, 5, 27, 9, 7, 27).timestamp()
    assert run.time_run.date_start.magnitude == date_start_timestamp

    date_end_timestamp = datetime(2021, 5, 27, 9, 13, 7, 525000).timestamp()
    assert run.time_run.date_end.magnitude == date_end_timestamp

    scc = run.calculation
    assert len(scc) == 100
    assert scc[0].temperature.magnitude == approx(300.0)
    assert scc[0].time == approx(0.0)
    assert scc[99].temperature.magnitude == approx(46.053)
    assert scc[99].time.magnitude == approx(49.5e-15)
    assert np.shape(scc[0].forces.total.value) == (4, 3)
    assert scc[0].forces.total.value[0][0].magnitude == approx(HaB_to_N(0.10002))
    assert scc[99].forces.total.value[2][2].magnitude == approx(HaB_to_N(-0.00989))

    assert len(run.system) == 100

    method = run.method[0]
    assert method.electronic.n_spin_channels == 1
    assert method.electronic.method == 'DFT'
    assert method.electronic.smearing.width == approx(K_to_J(500))
    assert method.dft.xc_functional.exchange[0].name == 'LDA_X'
    assert method.dft.xc_functional.correlation[0].name == 'LDA_C_PZ'

    workflow = archive.workflow2
    assert workflow.method.thermodynamic_ensemble == 'NVT'
    assert len(workflow.method.thermostat_parameters) == 2
    thermostat = workflow.method.thermostat_parameters[0]
    assert thermostat.thermostat_type == 'nose_hoover'
    assert thermostat.temperature_profile == 'constant'
    assert thermostat.temperature_update_frame_start == 1
    assert thermostat.temperature_update_frame_end == 50
    assert thermostat.reference_temperature_start.magnitude == approx(300.0)
    assert thermostat.reference_temperature_end.magnitude == approx(300.0)
    thermostat = workflow.method.thermostat_parameters[1]
    assert thermostat.thermostat_type == 'nose_hoover'
    assert thermostat.temperature_profile == 'linear'
    assert thermostat.temperature_update_frame_start == 50
    assert thermostat.temperature_update_frame_end == 100
    assert thermostat.reference_temperature_start.magnitude == approx(300.0)
    assert thermostat.reference_temperature_end.magnitude == approx(1000.0)
    assert workflow.method.coordinate_save_frequency == 1
    assert workflow.method.velocity_save_frequency == 1
    assert workflow.method.force_save_frequency == 1
    assert workflow.method.thermodynamics_save_frequency == 1
    assert workflow.method.integration_timestep.magnitude == approx(0.5e-15)
    assert workflow.method.n_steps == 100

    system = run.system[0]
    assert np.shape(system.atoms.velocities) == (4, 3)
    assert system.atoms.velocities[0][0].magnitude == approx(396.15464)
    assert system.atoms.velocities[3][2].magnitude == approx(2359.24208)
    system = run.system[99]
    assert system.atoms.velocities[0][1].magnitude == approx(-353.94304)
    assert system.atoms.velocities[3][0].magnitude == approx(-315.74184)

    eigenvalues = run.calculation[-1].eigenvalues[0]
    assert eigenvalues.n_kpoints == 1
    assert np.shape(eigenvalues.kpoints) == (1, 3)
    assert (eigenvalues.kpoints[0] == [0, 0, 0]).all()
    assert np.shape(eigenvalues.energies) == (1, 1, 64)
    assert eigenvalues.energies[0, 0, 0].magnitude == approx(Ha_to_J(-0.67352892393426))
    assert eigenvalues.energies[0, 0, 63].magnitude == approx(Ha_to_J(7.29352095903235))


def test_CrO2(parser):
    """
    Single run of feromagnetic CrO2 using LDA+U
    """
    archive = EntryArchive()
    parser.parse('tests/data/openmx/CrO2_single_point/CrO2.out', archive, logging)

    run = archive.run[0]

    date_start_timestamp = datetime(2021, 7, 16, 11, 49, 7).timestamp()
    assert run.time_run.date_start.magnitude == date_start_timestamp

    date_end_timestamp = datetime(2021, 7, 16, 11, 50, 11, 133000).timestamp()
    assert run.time_run.date_end.magnitude == date_end_timestamp

    method = run.method[0]
    assert method.electronic.n_spin_channels == 2
    assert method.electronic.method == 'DFT+U'
    assert method.electronic.smearing.width == approx(K_to_J(500))
    assert method.electronic.van_der_waals_method == ''
    assert method.dft.xc_functional.exchange[0].name == 'LDA_X'
    assert method.dft.xc_functional.correlation[0].name == 'LDA_C_PW'
    assert method.scf.n_max_iteration == 40
    assert method.scf.threshold_energy_change.magnitude == approx(Ha_to_J(1e-7))

    eigenvalues = run.calculation[-1].eigenvalues[0]
    assert eigenvalues.n_kpoints == 100
    assert np.shape(eigenvalues.kpoints) == (100, 3)
    assert eigenvalues.kpoints[39, 2] == approx(0.43750)
    assert np.shape(eigenvalues.energies) == (2, 100, 90)
    assert eigenvalues.energies[0, 42, 8].magnitude == approx(
        Ha_to_J(-0.92962144255459)
    )
    assert eigenvalues.energies[1, 99, 89].magnitude == approx(
        Ha_to_J(13.66867939417960)
    )


def test_graphite(parser):
    """
    Variable cell optimization of graphite with PBE and DFT-D3
    """
    archive = EntryArchive()
    parser.parse(
        'tests/data/openmx/graphite_cell_optimization/graphite.out', archive, logging
    )

    run = archive.run[0]

    method = run.method[0]
    assert method.electronic.n_spin_channels == 1
    assert method.electronic.method == 'DFT'
    assert method.electronic.smearing.width == approx(K_to_J(1000))
    assert method.electronic.van_der_waals_method == 'G10'
    assert method.scf.n_max_iteration == 100
    assert method.scf.threshold_energy_change.magnitude == approx(Ha_to_J(1e-8))

    calculation_first = run.calculation[0]
    stress_tensor_first = calculation_first.stress.total.value
    stress_tensor_expected_first = (
        np.array(
            [
                [-0.00001778, -0.00000244, -0.00000000],
                [-0.00000244, -0.00001879, 0.00000000],
                [-0.00000000, 0.00000000, -0.00002298],
            ]
        )
        * units.hartree
        / units.bohr**3
    )
    assert np.allclose(stress_tensor_first, stress_tensor_expected_first, 0.0)

    calculation_last = run.calculation[-1]
    stress_tensor_last = calculation_last.stress.total.value
    stress_tensor_expected_last = (
        np.array(
            [
                [-0.00000003, -0.00000001, 0.00000000],
                [-0.00000001, -0.00000004, -0.00000000],
                [0.00000000, -0.00000000, -0.00001568],
            ]
        )
        * units.hartree
        / units.bohr**3
    )
    assert np.allclose(stress_tensor_last, stress_tensor_expected_last, 0.0)


def test_graphite_no_stdout(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/openmx/graphite_cell_optimization_outonly/graphite.out',
        archive,
        logging,
    )
    run = archive.run[0]
    calculation = run.calculation[0]
    calc_stress = calculation.stress
    assert calc_stress is None
