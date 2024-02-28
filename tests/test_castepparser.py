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
from electronicparsers.castep import CastepParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return CastepParser()


def test_single_point(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/Si8.castep', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '16.1'
    assert sec_run.x_castep_constants_reference == 'CODATA 2010'
    assert sec_run.time_run.date_start.magnitude == 1455286325.0

    sec_method = sec_run.method[0]
    assert sec_method.electrons_representation[0].basis_set[0].cutoff.to(
        'eV'
    ).magnitude == approx(100)
    assert sec_method.electrons_representation[0].native_tier == 'FINE'
    assert sec_method.electronic.n_spin_channels == 1
    assert sec_method.dft.xc_functional.correlation[0].name == 'GGA_C_PBE'
    assert sec_method.electronic.smearing.kind == 'gaussian'

    assert archive.workflow2.m_def.name == 'SinglePoint'

    sec_scc = sec_run.calculation[0]
    assert np.shape(sec_scc.forces.total.value) == (8, 3)
    assert np.count_nonzero(sec_scc.forces.total.value) == 0
    assert sec_scc.energy.total.value.magnitude == approx(-2.21372403e-16)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 12
    assert sec_scfs[3].energy.total.value.magnitude == approx(-2.21530505e-16)
    assert sec_scfs[8].energy.fermi.magnitude == approx(8.53007633e-19)
    # uncomment one time_physical def is updated
    # assert sec_scfs[6].time_physical.magnitude == 12.70

    sec_system = sec_run.system[0]
    assert sec_system.atoms.positions[2][1].magnitude == approx(2.715e-10)
    assert sec_system.x_castep_section_atom_positions[
        0
    ].x_castep_cell_length_a == approx(5.43e-10)

    assert len(sec_method.atom_parameters) == 1

    sec_mulliken = sec_scc.charges[0]
    assert len(sec_mulliken.value) == 8
    assert sec_mulliken.orbital_projected[17].value.magnitude == 2.66

    assert (
        sec_run.x_castep_section_density_mixing_parameters[
            0
        ].x_castep_density_mixing_length
        == 20
    )
    assert sec_run.x_castep_section_time[0].x_castep_finalisation_time == 0.01


def test_dmd(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/TiO2-geom.castep', archive, None)

    sec_workflow = archive.workflow2
    assert sec_workflow.method.method == 'damped MD'
    assert sec_workflow.method.convergence_tolerance_force_maximum.magnitude == approx(
        8.01088317e-11
    )

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 23
    assert sec_sccs[7].energy.total.value.magnitude == approx(-3.67496146e-16)
    assert len(sec_sccs[20].scf_iteration) == 13
    assert sec_sccs[17].scf_iteration[3].energy.total.value.magnitude == approx(
        -3.67497215e-16
    )
    assert sec_sccs[3].forces.total.value[0][1].magnitude == approx(
        -4.49314415e-10,
    )
    assert sec_sccs[22].energy.total.value.magnitude == approx(-3.67497218e-16)

    sec_systems = archive.run[0].system
    assert sec_systems[12].atoms.positions[3][0].magnitude == approx(9.074282e-11)
    assert sec_systems[0].x_castep_number_of_electrons == 32


def test_md(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/Si8-md-NPT.castep', archive, None)

    sec_workflow = archive.workflow2
    assert sec_workflow.method.thermodynamic_ensemble == 'NPT'
    assert (
        sec_workflow.method.x_castep_thermostat_type == 'Nose-Hoover chain thermostat'
    )
    assert sec_workflow.method.x_castep_frame_energy_tolerance.magnitude == approx(
        1.60217663e-24
    )

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 13
    assert sec_sccs[2].energy.total.value.magnitude == approx(-1.37059981e-16)
    assert sec_sccs[6].stress.total.value[2][1].magnitude == approx(4.06626e09)
    assert sec_sccs[9].thermodynamics[0].pressure.magnitude == approx(1.111e09)
    assert sec_sccs[11].energy.total_t0.value.magnitude == approx(-1.37069057e-16)
    assert len(sec_sccs[12].scf_iteration) == 7
    assert sec_sccs[7].scf_iteration[3].energy.change.magnitude == approx(
        -1.90981043e-21
    )
    assert sec_sccs[0].time_calculation.magnitude == approx(2.83)
    assert sec_sccs[1].scf_iteration[4].time_physical.magnitude == approx(3.91)
    assert sec_sccs[2].scf_iteration[1].time_calculation.magnitude == approx(0.28)
    assert sec_sccs[8].time_physical.magnitude == approx(18.38)
    assert sec_sccs[10].time_calculation.magnitude == approx(2.14)

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 13
    assert sec_systems[0].atoms.positions[7][2].magnitude == approx(1.3575e-10)
    assert sec_systems[1].atoms.velocities[1][1].magnitude == approx(324.536)
    assert sec_systems[12].atoms.lattice_vectors[2][2].magnitude == approx(
        5.5475876e-10
    )


def test_eigenvalues(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/Fe.castep', archive, None)

    sec_eigenvalues = archive.run[0].calculation[0].eigenvalues[0]
    assert np.shape(sec_eigenvalues.energies[1][117]) == (6,)
    assert sec_eigenvalues.energies[1][38][4].magnitude == approx(1.30819997e-18)
    assert sec_eigenvalues.kpoints[22][1] == 0.289474


def test_bandstructure(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/Dispersions/Si2.castep', archive, None)

    sec_band_segment = (
        archive.run[0].calculation[0].band_structure_electronic[0].segment
    )
    assert len(sec_band_segment) == 5
    assert sec_band_segment[3].endpoints_labels == ['X', 'W']
    assert sec_band_segment[1].energies[0][-1][12].magnitude == approx(2.17418526e-18)
    assert sec_band_segment[4].kpoints[2][1] == 0.300000

    sec_method = archive.run[0].method[0]
    assert sec_method.electrons_representation[0].native_tier == 'MEDIUM'


def test_vibration(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/BC2N-Pmm2-Raman.castep', archive, None)

    sec_vibration = archive.run[0].calculation[0].vibrational_frequencies
    assert len(sec_vibration) == 2
    assert sec_vibration[1].value[2].to('1/cm').magnitude == approx(0.461821)
    assert sec_vibration[0].raman.intensity[3] == approx(21.0162567)
    assert sec_vibration[1].infrared.intensity[6] == approx(2.7078705)
    assert sec_vibration[0].raman.activity[10] == 'Y'

    sec_raman = archive.run[0].x_castep_section_raman_tensor
    assert len(sec_raman) == 12
    assert sec_raman[9].x_castep_raman_tensor[2][0].magnitude == approx(0.1834 * 0.5)


def test_tss(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/h2-lst.castep', archive, None)

    assert archive.workflow2.m_def.name == 'GeometryOptimization'

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 27
    assert sec_sccs[20].energy.total.value.magnitude == approx(-4.72809265e-18)


def test_bfgs(parser):
    archive = EntryArchive()
    parser.parse('tests/data/castep/Si2_opt.castep', archive, None)

    assert archive.workflow2.m_def.name == 'GeometryOptimization'

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 9
    sec_sccs[7].thermodynamics[0].pressure.magnitude == approx(400000.0)


def test_di(parser):
    # TODO implement test cannot find an example
    pass
