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
from electronicparsers.vasp import VASPParser
from tests.dos_integrator import integrate_dos


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return VASPParser()


@pytest.fixture(scope='module')
def silicon_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Si_dos_band/dos_si.xml', archive, None)
    return archive


@pytest.fixture(scope='module')
def silicon_band(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Si_dos_band/band_si.xml', archive, None)
    return archive


@pytest.fixture(scope='module')
def silicon_gw(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Si_GW/vasprun.xml', archive, None)
    return archive


def test_vasprunxml_static(parser):
    """Test Mg1 system, computed in VASP 4.6.35"""
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Mg_bands/vasprun.xml.static', archive, None)

    assert len(archive.run) == 1

    sec_run = archive.run[0]

    assert sec_run.program.compilation_datetime.magnitude == 1366564273.0

    sec_method = sec_run.method[0]
    assert len(sec_method.x_vasp_incar_in) == 27
    assert len(sec_method.x_vasp_incar_out) == 112
    assert sec_method.x_vasp_incar_in['LCHARG']
    assert len(sec_method.dft.xc_functional.exchange) == 1

    # basis set
    sec_representation = sec_method.electrons_representation[0]
    sec_basis_set = sec_representation.basis_set
    assert sec_representation.native_tier == 'high'
    assert sec_basis_set[0].type == 'plane waves'
    assert sec_basis_set[0].scope == ['valence']
    assert sec_basis_set[0].cutoff.to('eV').magnitude == approx(512.2418)
    assert sec_basis_set[1].type == 'plane waves'
    assert sec_basis_set[1].scope == ['augmentation']
    assert sec_basis_set[1].cutoff.to('eV').magnitude == approx(429)

    sec_system = sec_run.system[-1]
    assert len(sec_system.atoms.labels) == 1
    assert sec_system.atoms.lattice_vectors[0][0].magnitude == approx(-1.78559323e-10)

    sec_scc = sec_run.calculation[-1]
    assert sec_scc.energy.total.value.magnitude == approx(-2.3264377e-19)
    assert np.shape(sec_scc.forces.total.value) == (1, 3)
    assert sec_scc.stress.total.value[2][2].magnitude == approx(-2.78384438e08)
    assert np.shape(sec_scc.eigenvalues[0].energies[0][887]) == (37,)
    assert sec_scc.scf_iteration[2].energy.total_t0.value.magnitude == approx(
        -2.27580485e-19,
    )

    # Check the k-point sampling
    k_mesh = sec_method.k_mesh
    assert list(k_mesh.grid) == [32] * 3
    assert k_mesh.sampling_method == 'Monkhorst-Pack'
    assert len(k_mesh.points) == 888
    assert k_mesh.points[-1][2] == approx(0.48437500)
    assert k_mesh.weights[100] == approx(0.00073242)
    assert (k_mesh.x_vasp_tetrahedrons_list[0] == [4, 1, 2, 2, 18]).all()

    # test DOS values
    sec_dos = sec_scc.dos_electronic
    assert len(sec_dos) == 1
    assert len(sec_dos[0].energies) == 5000
    assert sec_dos[0].total[0].value[1838].magnitude == approx(
        (0.1369 / ureg.eV).to(1 / ureg.joule).magnitude
    )
    assert len(sec_dos[0].orbital_projected) == 9
    orbital_labels = [
        [0, 0],
        [1, 1],
        [1, 2],
        [1, 0],
        [2, 1],
        [2, 4],
        [2, 5],
        [2, 2],
        [2, 0],
    ]
    sec_orbital_labels = [
        list(orbital_dos.lm) for orbital_dos in sec_dos[0].orbital_projected
    ]
    assert sec_orbital_labels == orbital_labels
    assert sec_dos[0].orbital_projected[0].value[-1].magnitude == approx(3.40162245e17)
    # test DOS integrated
    dos_integrated = integrate_dos(sec_dos, sec_scc.energy.fermi)
    assert (
        pytest.approx(dos_integrated, abs=1e-2) == 8.0 - 6.0
    )  # dos starts from 6 electrons already


def test_vasprunxml_relax(parser):
    """Test Ac1Ag1 system, computed by VASP 5.3.2"""
    archive = EntryArchive()
    parser.parse('tests/data/vasp/AgAc_relax/vasprun.xml.relax', archive, None)

    assert len(archive.run[0].method) == 1

    sec_run = archive.run[0]
    sec_systems = archive.run[0].system
    assert len(sec_systems) == 3
    assert sec_systems[1].atoms.positions[1][0].magnitude == approx(3.2771907e-10)

    # Check the k-point sampling
    k_mesh = sec_run.method[-1].k_mesh
    assert list(k_mesh.grid) == [16] * 3
    assert k_mesh.sampling_method == 'Gamma-centered'

    # Check the basis set
    sec_method = sec_run.method[0]
    sec_representation = sec_method.electrons_representation[0]
    sec_basis_set = sec_representation.basis_set
    assert sec_representation.native_tier == 'accurate'
    assert sec_basis_set[0].type == 'plane waves'
    assert sec_basis_set[0].scope == ['valence']
    assert sec_basis_set[0].cutoff.to('eV').magnitude == approx(249.8)
    assert sec_basis_set[1].type == 'plane waves'
    assert sec_basis_set[1].scope == ['augmentation']
    assert sec_basis_set[1].cutoff.to('eV').magnitude == approx(543.281)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 3
    assert [len(scc.scf_iteration) for scc in sec_sccs] == [12, 10, 6]
    assert sec_sccs[0].energy.free.value.magnitude == approx(-1.14352735e-18)
    assert np.mean(sec_sccs[1].forces.total.value.magnitude) == 0.0
    assert sec_sccs[2].stress.total.value[2][2].magnitude == approx(-2.02429105e08)
    assert sec_sccs[2].energy.lowest_unoccupied.magnitude == approx(7.93718304e-19)
    assert sec_sccs[2].energy.highest_occupied.magnitude == approx(7.93702283e-19)
    assert [len(scc.eigenvalues) for scc in sec_sccs] == [0, 0, 1]
    assert [len(scc.dos_electronic) for scc in sec_sccs] == [0, 0, 2]
    sec_dos = sec_sccs[-1].dos_electronic
    assert sec_dos[0].spin_channel == 0 and sec_dos[1].spin_channel == 1
    dos_integrated = integrate_dos(sec_dos, sec_sccs[-1].energy.fermi)
    assert pytest.approx(dos_integrated, abs=1) == 22.0
    assert sec_sccs[1].time_calculation.magnitude == approx(438.32)
    assert sec_sccs[2].time_physical.magnitude == approx(1235.66)
    assert sec_sccs[0].scf_iteration[2].time_calculation.magnitude == approx(43.00)
    assert sec_sccs[1].scf_iteration[1].time_physical.magnitude == approx(612.72)


def test_vasprunxml_bands(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Mg_bands/vasprun.xml.bands', archive, None)

    sec_run = archive.run[0]
    k_mesh = sec_run.method[0].k_mesh
    assert len(k_mesh.points) == 128 * 6
    assert k_mesh.sampling_method == 'Line-path'

    sec_k_band = sec_run.calculation[0].band_structure_electronic[0]
    assert len(sec_k_band.segment) == 6
    assert np.shape(sec_k_band.segment[0].energies[0][127].magnitude) == (37,)
    assert sec_k_band.segment[1].energies[0][1][1].magnitude == approx(-6.27128785e-18)
    assert sec_k_band.segment[5].occupations[0][127][5] == 0.0


def test_band_silicon(silicon_band):
    """Tests that the band structure of silicon is parsed correctly."""
    scc = silicon_band.run[-1].calculation[0]
    band = scc.band_structure_electronic[-1]
    segments = band.segment
    energies = np.array([s.energies.to(ureg.electron_volt).magnitude for s in segments])

    # Check that an energy reference is reported
    energy_reference = scc.energy.fermi
    if energy_reference is None:
        energy_reference = scc.energy.highest_occupied
    assert energy_reference is not None
    energy_reference = energy_reference.to(ureg.electron_volt).magnitude

    # Check that an approporiately sized band gap is found at the given
    # reference energy
    energies = energies.flatten()
    energies.sort()
    lowest_unoccupied_index = np.searchsorted(energies, energy_reference, 'right')
    highest_occupied_index = lowest_unoccupied_index - 1
    gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
    assert gap == approx(0.5091)


def test_dos_silicon(silicon_dos):
    """Tests that the DOS of Si2 is parsed correctly.
    Computed using VASP 5.2.2
    """

    scc = silicon_dos.run[-1].calculation[0]
    k_mesh = silicon_dos.run[-1].method[-1].k_mesh
    dos = scc.dos_electronic
    assert len(dos) == 1
    energies = dos[-1].energies.to(ureg.electron_volt).magnitude
    values = np.array([d.value.magnitude for d in dos[-1].total])

    # Check the k-point sampling
    assert list(k_mesh.grid) == [15] * 3
    assert k_mesh.sampling_method == 'Monkhorst-Pack'

    # Check that an energy reference is reported
    energy_reference = scc.energy.fermi
    if energy_reference is None:
        energy_reference = scc.energy.highest_occupied
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
    assert gap == approx(0.83140)

    # Check that the no. valence electrons is recovered
    dos_integrated = integrate_dos(dos, scc.energy.fermi)
    assert pytest.approx(dos_integrated, abs=1e-2) == 8.0


def test_outcar(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/AgAc_relax/OUTCAR', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '5.3.2 13Sep12 complex serial LinuxIFC'

    sec_method = sec_run.method[0]
    # basis set
    sec_representation = sec_method.electrons_representation[0]
    sec_basis_set = sec_representation.basis_set
    assert sec_representation.native_tier == 'medium'
    assert sec_basis_set[0].type == 'plane waves'
    assert sec_basis_set[0].scope == ['valence']
    assert sec_basis_set[0].cutoff.to('eV').magnitude == approx(520)
    assert sec_basis_set[1].type == 'plane waves'
    assert sec_basis_set[1].scope == ['augmentation']
    assert sec_basis_set[1].cutoff.to('eV').magnitude == approx(543.3)
    # DFT
    assert sec_method.dft.xc_functional.exchange[0].name == 'GGA_X_PBE'
    assert len(sec_method.atom_parameters) == 2

    k_mesh = sec_method.k_mesh
    assert len(k_mesh.points) == 145

    sec_atom_param = sec_method.atom_parameters[0]
    assert sec_atom_param.n_valence_electrons == approx(11.0)
    assert sec_atom_param.mass.to('amu').magnitude == approx(227.028)

    sec_pseudo = sec_atom_param.pseudopotential
    assert sec_pseudo.name == 'PAW_PBE Ac 06Sep2000'
    assert sec_pseudo.xc_functional_name == ['GGA_X_PBE', 'GGA_C_PBE']
    assert sec_pseudo.cutoff.to('eV').magnitude == approx(172.237)

    sec_system = sec_run.system[0]
    assert sec_system.atoms.lattice_vectors[1][0].magnitude == approx(3.141538e-10)
    assert sec_system.atoms.positions[1][0].magnitude == approx(3.14154e-10)

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-1.11695443e-18)
    assert sec_scc.forces.total.value[0][0].magnitude == 0.0
    assert sec_scc.stress.total.value[0][0].magnitude == approx(7.060258e09)
    assert sec_scc.energy.lowest_unoccupied.magnitude == approx(9.40461662e-19)
    assert sec_scc.energy.highest_occupied.magnitude == approx(9.51212268e-19)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 11
    assert sec_scfs[4].energy.total.value.magnitude == approx(-1.20437432e-18)
    assert sec_scfs[7].energy.sum_eigenvalues.value.magnitude == approx(-1.61008452e-17)
    sec_eigs = sec_scc.eigenvalues[0]
    assert np.shape(sec_eigs.energies[0][144]) == (15,)
    assert sec_eigs.energies[0][9][14].magnitude == approx(1.41810256e-18)
    assert sec_eigs.occupations[0][49][9] == 2.0
    assert sec_eigs.kpoints_multiplicities[1] == 8
    assert sec_scc.time_calculation.magnitude == approx(391.97)
    assert sec_scfs[1].time_physical.magnitude == approx(53.39)
    assert sec_scfs[2].time_calculation.magnitude == approx(33.36)

    # check DOS
    assert len(sec_scc.dos_electronic) == 1
    sec_dos = sec_scc.dos_electronic[0]
    assert len(sec_dos.energies) == 301
    assert sec_dos.total[0].value[282].magnitude == approx(
        (0.2545e01 / ureg.eV).to(1 / ureg.joule).magnitude
    )
    assert len(sec_dos.orbital_projected) == 32
    assert sec_dos.orbital_projected[10].value[-15].magnitude == approx(1.51481425e17)
    assert sec_dos.orbital_projected[5].value[-16].magnitude == approx(1.71267009e16)
    assert (
        sec_dos.total[0].value_integrated[-1] == 30.0
    )  # This runs up to the conduction band


#    BUG EMIN is stored in the fermi energy!!
#    dos_integrated = integrate_dos(sec_dos, False, sec_scc.energy.fermi)
#    try:
#        assert pytest.approx(dos_integrated, abs=1) == 22.
#    except AssertionError:
#        raise AssertionError(sec_scc.energy.fermi)


@pytest.mark.parametrize(
    'filename, name, cutoff',
    [
        (
            'tests/data/vasp/alternative_pseudopotentials/AlN/vasprun.xml',
            'PAW_PBE Al 04Jan2001',
            240.3,
        ),
        (
            'tests/data/vasp/alternative_pseudopotentials/F_GW/OUTCAR',
            '^PAW_PBE F_h_GW 20May2014',
            848.358,
        ),
    ],
)
def test_potcar(parser, filename, name, cutoff):
    archive = EntryArchive()
    parser.parse(filename, archive, None)

    sec_method = archive.run[0].method[0]
    sec_pseudo = sec_method.atom_parameters[-1].pseudopotential
    assert sec_pseudo.name == name
    assert sec_pseudo.type == 'PAW'
    assert sec_pseudo.xc_functional_name == ['GGA_X_PBE', 'GGA_C_PBE']
    assert sec_pseudo.cutoff.to('eV').magnitude == approx(cutoff)


def test_broken_xml(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/vasprun.xml.broken', archive, None)


def test_hybrid(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/hybrid_vasprun.xml.gz', archive, None)

    sec_run = archive.run[-1]
    sec_method = sec_run.method[-1]
    k_mesh = sec_method.k_mesh

    # Check the k-point sampling
    assert list(k_mesh.grid) == [1] * 3
    assert k_mesh.sampling_method == 'Gamma-centered'

    sec_xc_functional = sec_method.dft.xc_functional
    assert (
        sec_xc_functional.hybrid[0].parameters['exact_exchange_mixing_factor'] == 0.25
    )
    assert sec_xc_functional.hybrid[0].name == 'HYB_GGA_XC_HSE06'


def test_metagga(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/hle17_vasprun.xml.gz', archive, None)

    sec_run = archive.run[-1]
    sec_method = sec_run.method[-1]
    k_mesh = sec_method.k_mesh

    # Check the k-point sampling
    assert list(k_mesh.grid) == [1] * 3
    assert k_mesh.sampling_method == 'Gamma-centered'

    sec_xc_functional = sec_method.dft.xc_functional
    assert sec_xc_functional.contributions[0].name == 'MGGA_XC_HLE17'


@pytest.mark.parametrize(
    'dir, slice, uref, jref',
    [
        ('multi_parameter/', 1, 3.25, 0.0),
        ('multi_parameter_no_incar/', 1, 3.2, 0.0),
        ('multi_parameter/', 2, 2.0, 1.0),
        ('single_parameter/', 0, 7.5, 0.0),
    ],
)
def test_dftu_static(parser, dir, slice, uref, jref):
    """Static calculation using PBE+U.
    Geometry taken from NOMAD Archive and Repository site.
    `multi_parameter` generated by N. Daelman on JENA cluster using VASP 6.1.0
    `single_parameter` taken from NOMAD Archive, `entry_id = URIGyi36nFOR8KTVGpotZhG4n28`
    """

    archive = EntryArchive()
    # test the values in vasprun.xml and INCAR (selected in place of OUTCAR)
    prefix = 'tests/data/vasp/dftu/'
    for mainfile in ['vasprun.xml', 'OUTCAR']:
        filename = os.path.join(prefix, dir, mainfile)
        if not os.path.isfile(filename):
            continue
        parser.parse(filename, archive, None)
        param = archive.run[-1].method[-1].atom_parameters[slice]
        if hubb := param.hubbard_kanamori_model:
            assert hubb.double_counting_correction == 'Dudarev'
            assert hubb.orbital == 'd'
            assert approx(hubb.u.to('eV').magnitude) == uref
            assert approx(hubb.j.to('eV').magnitude) == jref


def test_gw(silicon_gw):
    """Tests that the GW metainfo has been parsed correctly."""
    sec_run = silicon_gw.run[-1]
    sec_method = sec_run.method[-1]
    assert sec_method.m_xpath('gw') and sec_method.m_xpath('k_mesh')
    assert not sec_method.m_xpath('dft')
    assert (sec_method.k_mesh.grid == np.array([6, 6, 6])).all()
    assert sec_method.gw.type == 'G0W0'
    assert sec_method.gw.analytical_continuation == 'pade'
    assert sec_method.gw.n_states == 72
    assert (sec_method.gw.q_mesh.grid == np.array([6, 6, 6])).all()
    assert sec_method.gw.q_mesh.sampling_method == 'Gamma-centered'
    assert len(sec_method.frequency_mesh) == 1
    assert sec_method.frequency_mesh[0].n_points == 50
    sec_scc = sec_run.calculation
    assert len(sec_scc) == 1
    homo = sec_scc[-1].energy.highest_occupied.to('eV').magnitude
    lumo = sec_scc[-1].energy.lowest_unoccupied.to('eV').magnitude
    assert homo == approx(2.132)
    assert lumo == approx(3.8526)
    bandgap = lumo - homo
    assert bandgap == approx(1.7206)


@pytest.mark.parametrize(
    'filename',
    [
        'dotted',
        'single_char',
        'mixed_case',
        'lowercase',
    ],
)
def test_booleans(filename, parser):
    """Tests that booleans are parse correctly no matter which format is used."""
    archive = EntryArchive()
    parser.parse(f'tests/data/vasp/booleans/{filename}/OUTCAR', archive, None)
    lnbo = parser._outcar_parser._incar['incar']['LNBO']
    assert lnbo is True
