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
import os

from nomad.units import ureg
from nomad.datamodel import EntryArchive
from electronicparsers.exciting import ExcitingParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return ExcitingParser()


@pytest.fixture(scope='module')
def silicon_gw(parser):
    archive = EntryArchive()
    parser.parse('tests/data/exciting/Si_gw/GW_INFO.OUT', archive, None)
    return archive


def test_gs(parser):
    archive = EntryArchive()
    parser.parse('tests/data/exciting/C_gs/INFO.OUT', archive, None)

    assert len(archive.run) == 1

    sec_run = archive.run[0]
    assert sec_run.program.version == 'CARBON'

    sec_method = sec_run.method[0]
    assert list(sec_method.k_mesh.grid) == [6] * 3
    assert list(sec_method.k_mesh.offset) == [0.0] * 3
    assert sec_method.electronic.n_spin_channels == 1
    assert sec_method.electronic.smearing.width == approx(4.35974472e-22)
    assert sec_method.dft.xc_functional.exchange[0].name == 'GGA_X_PBE_SOL'
    assert sec_method.x_exciting_scf_threshold_force_change.magnitude == approx(
        4.11936175e-12
    )

    sec_system = sec_run.system[0]
    assert sec_system.atoms.lattice_vectors[0][0].magnitude == approx(1.72297146e-10)
    assert sec_system.atoms.positions[1][0].magnitude == approx(8.61485729e-11)
    assert len(sec_system.atoms.labels) == 2
    assert (
        sec_system.x_exciting_section_spin[0].x_exciting_spin_treatment
        == 'spin-unpolarised'
    )
    assert sec_system.x_exciting_section_atoms_group[
        0
    ].x_exciting_muffin_tin_radius.magnitude == approx(6.87930374e-11)

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-3.30863556e-16)
    assert np.mean(sec_scc.forces.total.value) == 0.0
    assert sec_scc.charges[0].total.magnitude == approx(1.92261196e-18)
    assert sec_scc.energy.fermi.magnitude == approx(2.4422694e-18)
    assert len(sec_scc.scf_iteration) == 12
    assert sec_scc.scf_iteration[5].x_exciting_valence_charge.magnitude == approx(
        1.28174131e-18
    )
    assert sec_scc.scf_iteration[8].x_exciting_exchange_energy.magnitude == approx(
        -4.39756926e-17
    )
    assert sec_scc.scf_iteration[
        11
    ].energy.kinetic_electronic.value.magnitude == approx(3.30404896e-16)
    sec_eig = sec_scc.eigenvalues[0]
    assert np.shape(sec_eig.kpoints) == (30, 3)
    assert sec_eig.energies[0][9][4].magnitude == approx(2.74680139e-18)


def test_strucopt(parser):
    archive = EntryArchive()
    parser.parse('tests/data/exciting/GaO_strucopt/INFO.OUT', archive, None)

    assert (
        archive.run[0].program.version_internal
        == '1e47a4bd61d2aa73ef68a31c2f3385676bee2c3a'
    )

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 15
    assert sec_systems[0].atoms.labels == [
        'Ga',
        'Ga',
        'Ga',
        'Ga',
        'O',
        'O',
        'O',
        'O',
        'O',
        'O',
    ]
    assert sec_systems[0].x_exciting_gkmax.magnitude == approx(1.13383567e11)
    assert sec_systems[3].atoms.positions[1][1].magnitude == approx(3.07695918e-10)
    assert sec_systems[10].atoms.positions[-1][0].magnitude == approx(3.67156876e-11)
    assert sec_systems[1].atoms.lattice_vectors[2][1].magnitude == approx(
        sec_systems[13].atoms.lattice_vectors[2][1].magnitude
    )

    sec_run = archive.run[0]
    sec_method = sec_run.method[0]
    assert list(sec_method.k_mesh.grid) == [6] * 3
    assert list(sec_method.k_mesh.offset) == [0.0] * 3
    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 15
    assert len(sec_sccs[0].scf_iteration) == 19
    assert sec_sccs[0].time_physical.magnitude == approx(743.16)
    assert sec_sccs[0].time_calculation.magnitude == approx(743.16)
    assert sec_sccs[0].scf_iteration[16].time_calculation.magnitude == approx(38.87)
    assert sec_sccs[7].time_calculation.magnitude == approx(758.49)
    assert sec_sccs[3].time_physical.magnitude == approx(2426.67)
    assert sec_sccs[0].scf_iteration[18].x_exciting_effective_potential_convergence[
        0
    ].magnitude == approx(4.62350928e-26)
    assert sec_sccs[3].x_exciting_maximum_force_magnitude.magnitude == approx(
        1.64771998e-10
    )
    assert sec_sccs[6].energy.total.value.magnitude == approx(-3.58415586e-14)
    assert sec_sccs[9].time_calculation.magnitude == approx(724.33)
    assert len(sec_sccs[-1].x_exciting_section_MT_charge_atom) == 10
    assert sec_sccs[-1].x_exciting_fermi_energy.magnitude == approx(1.03200886e-18)


def test_dos_spinpol(parser):
    archive = EntryArchive()
    parser.parse('tests/data/exciting/CeO_dos/INFO.OUT', archive, None)

    sec_run = archive.run[0]
    sec_method = sec_run.method[0]
    assert list(sec_method.k_mesh.grid) == [8] * 3
    assert list(sec_method.k_mesh.offset) == [0.0] * 3

    sec_scc = sec_run.calculation[0]
    assert len(sec_scc.dos_electronic) == 2
    sec_dos_up = sec_scc.dos_electronic[0]
    sec_dos_down = sec_scc.dos_electronic[1]
    assert sec_dos_up.spin_channel == 0 and sec_dos_down.spin_channel == 1
    assert np.shape(sec_dos_up.total[0].value) == (500,)
    assert (
        sec_dos_up.energies[79].to('Ha') - sec_scc.energy.fermi.to('Ha')
    ).magnitude == approx(-0.684)
    assert (
        sec_dos_up.energies[240].to('Ha') - sec_scc.energy.fermi.to('Ha')
    ).magnitude == approx(-0.4e-01)
    assert sec_dos_up.total[0].value[126].to('1/Ha').magnitude == approx(20.83182629)
    assert sec_dos_down.total[0].value[136].to('1/Ha').magnitude == approx(2.109103733)
    assert sec_dos_up.total[0].value[220].to('1/Ha').magnitude == approx(62.06860954)
    assert sec_dos_down.total[0].value[78].to('1/Ha').magnitude == approx(47.70198869)

    assert (
        len(sec_dos_up.atom_projected) == 75 and len(sec_dos_down.atom_projected) == 75
    )
    assert np.shape(sec_dos_up.atom_projected[73].value) == (500,)
    assert sec_dos_up.atom_projected[11].atom_index == 2
    assert sec_dos_up.atom_projected[11].m_kind == 'spherical'
    assert np.all(sec_dos_up.atom_projected[11].lm == np.array([3, 0]))
    assert sec_dos_up.atom_projected[11].value[85].to('1/Ha').magnitude == approx(
        0.027132587730000005
    )
    assert sec_dos_down.atom_projected[11].value[85].to('1/Ha').magnitude == approx(
        0.0001147139711
    )


@pytest.mark.skip('To be updated: TDDFT currently not supported by FAIRmat')
def test_xs_tddft(parser):
    archive = EntryArchive()
    parser.parse('tests/data/exciting/CSi_tddft/INFO_QMT001.OUT', archive, None)

    sec_run = archive.run[0]
    sec_method = sec_run.method[0]
    assert list(sec_method.k_mesh.grid) == [12] * 3
    assert list(sec_method.k_mesh.offset) == [0.097, 0.273, 0.493]

    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 2

    assert len(sec_sccs[1].x_exciting_xs_tddft_epsilon_energies) == 10001
    assert np.shape(
        sec_sccs[1].x_exciting_xs_tddft_dielectric_function_local_field
    ) == (2, 1, 3, 10001)
    assert np.shape(
        sec_sccs[1].x_exciting_xs_tddft_dielectric_function_no_local_field
    ) == (2, 1, 3, 10001)
    assert np.shape(sec_sccs[1].x_exciting_xs_tddft_loss_function_local_field) == (
        1,
        3,
        10001,
    )
    assert np.shape(sec_sccs[1].x_exciting_xs_tddft_loss_function_no_local_field) == (
        1,
        3,
        10001,
    )
    assert np.shape(sec_sccs[1].x_exciting_xs_tddft_loss_function_no_local_field) == (
        1,
        3,
        10001,
    )
    assert np.shape(sec_sccs[1].x_exciting_xs_tddft_sigma_local_field) == (
        2,
        1,
        3,
        10001,
    )
    assert np.shape(sec_sccs[1].x_exciting_xs_tddft_sigma_no_local_field) == (
        2,
        1,
        3,
        10001,
    )


def test_xs_mainfile_keys(parser):
    # This test will not show the BSE archive. We use it instead to test the mainfile_keys
    filepath = 'tests/data/exciting/CHN_bse/INFO.OUT'
    dirname = os.path.dirname(filepath)
    mainfile_keys = parser.get_mainfile_keys(filename=filepath)
    assert mainfile_keys[0] == 'XS_workflow'
    assert mainfile_keys[1] == f'{dirname}/INFOXS.OUT'
    for i in range(2):
        assert f'{dirname}/EPSILON_BSEIP_SCRfull_OC{i + 1}{i + 1}.OUT' in mainfile_keys
        assert (
            f'{dirname}/EPSILON_BSEsinglet_SCRfull_OC{i + 1}{i + 1}.OUT'
            in mainfile_keys
        )
        assert (
            f'{dirname}/EPSILON_BSEtriplet_SCRfull_OC{i + 1}{i + 1}.OUT'
            in mainfile_keys
        )


def test_gw(silicon_gw):
    """Basic tests for a GW calculation."""
    sec_methods = silicon_gw.run[0].method
    assert len(sec_methods) == 1
    sec_gw = sec_methods[-1].gw
    assert sec_gw.x_exciting_coreflag == 'all'
    assert sec_gw.x_exciting_barecoul.x_exciting_barcevtol == approx(0.1)
    assert sec_gw.type == 'G0W0'
    assert sec_gw.analytical_continuation == 'pade'
    assert sec_gw.n_empty_states == 100
    assert sec_gw.screening.type == 'rpa'
    assert sec_gw.screening.n_empty_states == sec_gw.n_empty_states
    assert (sec_gw.screening.k_mesh.grid == np.array([2, 2, 2])).all()
    assert (sec_gw.q_mesh.grid == np.array([2, 2, 2])).all()
    assert len(sec_methods[-1].frequency_mesh) == 1
    sec_freq_mesh = sec_methods[-1].frequency_mesh[0]
    assert sec_freq_mesh.sampling_method == 'Gauss-Legendre'
    assert sec_freq_mesh.n_points == 32
    assert sec_freq_mesh.points[0][4].to('hartree').magnitude == approx(0.125 + 0j)

    sec_sccs = silicon_gw.run[0].calculation
    assert len(sec_sccs) == 1

    # Check GW properties
    # TODO these fail
    # assert sec_sccs[0].energy.fermi.magnitude == approx(1.09865567e-19)
    # assert sec_sccs[0].band_gap[0].value.magnitude == approx(3.42913865e-19)
    assert sec_sccs[0].band_gap[0].provenance.label == 'parser'
    assert np.shape(sec_sccs[0].eigenvalues[0].energies[0][2]) == (20,)
    assert sec_sccs[0].eigenvalues[0].kpoints[-3][1] == 0.0
    assert sec_sccs[0].eigenvalues[0].energies[0][2][9].magnitude == approx(
        1.769533187849446e-18, abs=1e-20
    )
    assert sec_sccs[0].eigenvalues[0].qp_linearization_prefactor[0][2][9] == approx(
        0.79935
    )
    assert sec_sccs[0].eigenvalues[0].value_exchange[0][2][0].magnitude == approx(
        -2.855981572623473e-18, abs=1e-20
    )
    assert sec_sccs[0].eigenvalues[0].value_correlation[0][2][14].magnitude == approx(
        -1.0879742954267992e-18, abs=1e-20
    )
    assert sec_sccs[0].eigenvalues[0].value_xc_potential[0][2][6].magnitude == approx(
        -2.1691473890869554e-18, abs=1e-20
    )


def test_gw_band_silicon(silicon_gw):
    """Tests that the band structure of silicon is parsed correctly from a GW
    calculation.
    """
    sccs = silicon_gw.run[-1].calculation
    assert len(sccs) == 1
    gaps = [1.2553776]
    for gap_assumed, scc in zip(gaps, sccs):
        band = scc.band_structure_electronic[0]
        segments = band.segment
        energies = [s.energies.to(ureg.electron_volt).magnitude for s in segments]
        energies = np.concatenate(energies, axis=1)

        # Check that an energy reference is reported
        energy_reference = scc.energy.fermi
        if energy_reference is None:
            energy_reference = scc.band_structure.info.energy_highest_occupied
        assert energy_reference is not None
        energy_reference = energy_reference.to(ureg.electron_volt).magnitude

        # Check that an appropriately sized band gap is found at the given
        # reference energy
        energies = energies.flatten()
        energies.sort()
        lowest_unoccupied_index = np.searchsorted(energies, energy_reference, 'right')
        highest_occupied_index = lowest_unoccupied_index - 1
        gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
        assert gap == approx(gap_assumed)


def test_gw_dos_silicon(silicon_gw):
    """Tests that the DOS of silicon is parsed correctly from a GW calculation."""
    sccs = silicon_gw.run[-1].calculation
    assert len(sccs) == 1
    gaps = [1.360569]
    for gap_assumed, scc in zip(gaps, sccs):
        dos = scc.dos_electronic[0]
        energies = dos.energies.to(ureg.electron_volt).magnitude
        values = np.array([d.value.magnitude for d in dos.total])

        # Check that an energy reference is reported
        energy_reference = scc.energy.fermi
        if energy_reference is None:
            energy_reference = scc.energy_reference_highest_occupied
        assert energy_reference is not None
        energy_reference = energy_reference.to(ureg.electron_volt).magnitude

        # Check that an appropriately sized band gap is found at the given
        # reference energy
        nonzero = np.unique(values.nonzero())
        energies = energies[nonzero]
        energies.sort()
        lowest_unoccupied_index = np.searchsorted(energies, energy_reference, 'right')
        highest_occupied_index = lowest_unoccupied_index - 1
        gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
        assert gap == approx(gap_assumed)


def test_hybrids(parser):
    archive = EntryArchive()
    parser.parse('tests/data/exciting/PbI_hybrids/INFO.OUT', archive, None)

    sec_method = archive.run[-1].method[0]
    assert list(sec_method.k_mesh.grid) == [6, 6, 4]
    assert list(sec_method.k_mesh.offset) == [0.0] * 3
    assert sec_method.dft.xc_functional.hybrid[0].name == 'HYB_GGA_XC_HSE03'

    calc = archive.run[-1].calculation[0]
    assert len(calc.scf_iteration) == 4
    assert calc.energy.total.value.magnitude == approx(-1.5345852e-13)
