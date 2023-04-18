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
from electronicparsers.fhiaims import FHIAimsParser
from tests.dos_integrator import integrate_dos


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return FHIAimsParser()


@pytest.fixture(scope='module')
def silicon_versions():
    return ('v071914_7', 'v171221_1')


@pytest.fixture(scope='module')
def silicon(parser, silicon_versions):
    silicon = {}
    for version in silicon_versions:
        archive = EntryArchive()
        parser.parse('tests/data/fhiaims/Si_band_dos_' + version + '/aims_CC.out',
                     archive, None)
        silicon[version] = archive
    return silicon


@pytest.fixture(scope='module')
def silicon_normalization_factors(silicon_versions):
    normalization_factors = [.5, 1]
    return dict(zip(silicon_versions, normalization_factors))


def test_scf_spinpol(parser):
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/Fe_scf_spinpol/out.out', archive, None)

    assert archive.run[0].program.version == '151211'
    assert archive.run[0].time_run.wall_start.magnitude == approx(2.23485023e+08)

    assert len(archive.run[0].method) == 1
    sec_method = archive.run[0].method[0]
    assert list(sec_method.k_mesh.grid) == [16] * 3
    assert sec_method.electronic.n_spin_channels == 2
    assert sec_method.electronic.relativity_method == 'scalar_relativistic_atomic_ZORA'
    assert sec_method.dft.xc_functional.correlation[0].name == 'LDA_C_PW'
    sec_basis_func = sec_method.x_fhi_aims_section_controlIn_basis_set[0].x_fhi_aims_section_controlIn_basis_func
    assert len(sec_basis_func) == 10
    assert sec_basis_func[2].x_fhi_aims_controlIn_basis_func_radius == 6.0
    assert sec_basis_func[6].x_fhi_aims_controlIn_basis_func_type == 'hydro'
    sec_atom_type = archive.run[0].method[0].atom_parameters[0]
    assert sec_atom_type.mass.magnitude == approx(9.27328042e-26)
    assert sec_atom_type.x_fhi_aims_section_controlInOut_atom_species[0].x_fhi_aims_controlInOut_species_cut_pot.magnitude == approx(3.5e-10)

    assert len(archive.run[0].system) == 1
    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.lattice_vectors[1][1].magnitude == approx(-1.4e-10)
    assert sec_system.atoms.periodic == [True, True, True]
    assert sec_system.atoms.labels == ['Fe']

    assert len(archive.run[0].calculation) == 1
    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.xc.value.magnitude == approx(-2.3433685e-16)
    assert sec_scc.calculation_converged
    assert sec_scc.energy.fermi.magnitude == approx(-1.50351795e-18)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 15
    assert sec_scfs[12].energy.total_t0.value.magnitude == approx(-5.56048676e-15)
    assert sec_scfs[7].energy.change.magnitude == approx(9.43361602e-22)
    sec_eig = sec_scc.eigenvalues[0]
    assert np.shape(sec_eig.kpoints) == (4, 3)
    assert np.shape(sec_eig.occupations[1][3]) == (19,)
    assert sec_eig.energies[1][2][4].magnitude == approx(-1.1221523e-16)
    assert sec_eig.occupations[0][3][9] == 1.0


def test_geomopt(parser):
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/Si_geomopt/out.out', archive, None)

    sec_methods = archive.run[0].method
    assert len(sec_methods) == 1
    assert list(sec_methods[0].k_mesh.grid) == [8] * 3

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 6

    assert np.shape(sec_sccs[1].eigenvalues[0].energies[0][0]) == (20,)
    assert sec_sccs[2].energy.correlation.value.magnitude == approx(-9.34966824e-18)
    assert len(sec_sccs[3].scf_iteration) == 6
    assert np.max(sec_sccs[3].forces.free.value_raw.magnitude) == approx(2.4933233e-11)
    assert np.max(sec_sccs[4].forces.free.value.magnitude) == 0.


def test_band_spinpol(parser):
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/Fe_band_spinpol/Fe_band_structure_dos_spin.out', archive, None)

    assert len(archive.run[0].calculation) == 1
    sec_scc = archive.run[0].calculation[0]

    sec_method = archive.run[0].method[0]
    assert list(sec_method.k_mesh.grid) == [16] * 3

    sec_k_band = sec_scc.band_structure_electronic[0]
    assert len(sec_k_band.segment) == 3
    assert np.shape(sec_k_band.segment[0].energies[1][14]) == (19,)
    assert np.shape(sec_k_band.segment[1].kpoints) == (15, 3)
    assert np.shape(sec_k_band.segment[2].occupations[1][14]) == (19,)
    assert sec_k_band.segment[0].occupations[1][9][2] == approx(1.0)
    assert sec_k_band.segment[1].energies[0][3][5].magnitude == approx(-1.54722007e-17)
    assert sec_k_band.segment[2].kpoints[14][2] == approx(0.5)

    # test DOS
    sec_dos = sec_scc.dos_electronic[0]
    assert np.shape(sec_dos.energies) == (50,)
    assert np.shape(sec_dos.total[1].value) == (50,)
    assert sec_dos.energies[46].magnitude == approx(-1.1999976e-18)
    assert sec_dos.total[0].value[46].to('1 / eV').magnitude == approx(.18127036)
    assert sec_dos.total[1].value[15].to('1 / eV').magnitude == approx(.57150097)
    dos_integrated = integrate_dos(sec_dos, True, sec_scc.energy.fermi)
    assert pytest.approx(dos_integrated, abs=1) == 8.

    # v151211 test for the Fermi level
    assert sec_scc.energy.fermi.to('eV').magnitude == approx(-9.3842209)
    assert sec_k_band.energy_fermi == sec_scc.energy.fermi


@pytest.mark.parametrize("version", silicon_versions())
def test_band_silicon(silicon, version):
    """Tests that the band structure of silicon is parsed correctly.
    """
    scc = silicon[version].run[-1].calculation[0]
    band = scc.band_structure_electronic[0]
    segments = band.segment
    energies = np.array([s.energies.to('eV').magnitude for s in segments])

    # Check that an energy reference is reported
    energy_reference = scc.energy.fermi.to('eV').magnitude
    assert energy_reference == approx(-5.7308573, abs=1e-5)
    assert band.energy_fermi.to('eV').magnitude == energy_reference

    # Check that an approporiately sized band gap is found at the given
    # reference energy
    energies = energies.flatten()
    energies.sort()
    lowest_unoccupied_index = np.searchsorted(energies, energy_reference, "right")
    highest_occupied_index = lowest_unoccupied_index - 1
    gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
    assert gap == approx(0.60684)


@pytest.mark.parametrize("version", silicon_versions())
def test_dos_silicon(silicon, version, silicon_normalization_factors):
    """Tests that the DOS of silicon is parsed correctly.
    """
    scc = silicon[version].run[-1].calculation[0]
    dos = scc.dos_electronic[0]
    energy_reference = scc.energy.fermi.to('eV').magnitude
    energies = dos.energies.to('eV').magnitude
    values = np.array([d.value.magnitude for d in dos.total])
    dos_integrated = integrate_dos(dos, False, scc.energy.fermi)

    assert pytest.approx(dos_integrated, abs=5e-2) == 8
    assert dos.total[0].x_fhi_aims_normalization_factor_raw_data == silicon_normalization_factors[version]

    # Check that an approporiately sized band gap is found at the given
    # reference energy
    nonzero = np.unique(values.nonzero())
    energies = energies[nonzero]
    energies.sort()
    lowest_unoccupied_index = np.searchsorted(energies, energy_reference, "right")
    highest_occupied_index = lowest_unoccupied_index - 1
    gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
    assert gap == approx(0.54054054, abs=.04)  # TODO increase accuracy


def test_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/ClNa_dos/ClNa_dos.out', archive, None)

    sec_method = archive.run[0].method[0]
    assert list(sec_method.k_mesh.grid) == [10] * 3

    sec_scc = archive.run[0].calculation[0]
    sec_dos = sec_scc.dos_electronic[0]
    assert np.shape(sec_dos.energies) == (50,)
    assert np.shape(sec_dos.total[0].value) == (50,)
    assert sec_dos.total[0].value[0].to('1 / eV').magnitude == approx(0.00233484)
    assert sec_dos.total[0].value[-1].to('1 / eV').magnitude == approx(0.49471595)

    dos_integrated = integrate_dos(sec_dos, False, sec_scc.energy.fermi)
    assert pytest.approx(dos_integrated, abs=1) == 3.  # 3rd valence shell

    sec_species_dos = sec_dos.species_projected
    assert np.shape(sec_species_dos[7].value) == (50,)
    assert sec_species_dos[0].value[44].to('1 / eV').magnitude == approx(0.62432797)  # Na total
    assert sec_species_dos[1].value[37].to('1 / eV').magnitude == approx(0.12585650)  # Cl total
    assert sec_species_dos[4].value[3].to('1 / eV').magnitude == approx(0.07198767)  # Na l=1
    assert sec_species_dos[7].value[5].to('1 / eV').magnitude == approx(0.00394778)  # Cl l=2


def test_md(parser):
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/HO_md/H2O_periodic_MD.out', archive, None)

    sec_method = archive.run[0].method[0]
    assert list(sec_method.k_mesh.grid) == [2] * 3

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 6
    assert len(sec_sccs[1].scf_iteration) == 14
    assert sec_sccs[4].energy.sum_eigenvalues.value.magnitude == approx(-1.82257271e-16)

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 6
    assert sec_systems[2].atoms.velocities[1][2].magnitude == approx(-1195.746888)
    assert sec_systems[4].atoms.positions[2][0].magnitude == approx(2.00130424e-10)

    sec_calculation = archive.run[0].calculation
    assert len(sec_calculation) == 6
    assert sec_calculation[4].step == 3
    assert sec_calculation[4].time.magnitude == approx(0.003)
    assert sec_calculation[4].temperature.magnitude == approx(339.815893902375)
    assert sec_calculation[4].energy.kinetic.value.magnitude == approx(2.111251998587359e-20)
    assert sec_calculation[4].energy.potential.value.magnitude == approx(-3.3301149258970176e-16)

    sec_workflow = archive.workflow2
    assert sec_workflow.method.thermodynamic_ensemble == 'NVT'
    assert sec_workflow.method.integration_timestep.magnitude == approx(1e-15)
    assert sec_workflow.method.n_steps == 5
    sec_thermostat = sec_workflow.method.thermostat_parameters
    assert sec_thermostat.thermostat_type == 'nose_hoover'
    assert sec_thermostat.reference_temperature.magnitude == approx(300.0)
    assert sec_thermostat.coupling_constant.magnitude == approx(3.706267724423911e-14)


def test_hybrid(parser):
    """"Taken from the official test files in FHI-aims v210716_3"""
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/GaAs_HSE06+SOC/aims.out', archive, None)

    sec_method = archive.run[0].method[0]
    assert list(sec_method.k_mesh.grid) == [12] * 3

    sec_xc_functional = sec_method.dft.xc_functional
    assert sec_xc_functional.hybrid[0].parameters['exact_exchange_mixing_factor'] == .25
    assert sec_xc_functional.hybrid[0].name == 'HYB_GGA_XC_HSE06'


def test_dftu(parser):
    """Test generated by Nathan Daelman on DUNE3 cluster"""

    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/CeO2_dftu/aims_CC.out', archive, None)

    sec_method = archive.run[0].method[0]
    assert list(sec_method.k_mesh.grid) == [1] * 3

    sec_hubb = sec_method.atom_parameters[0].hubbard_kanamori_model
    assert sec_hubb.orbital == '4f'
    assert approx(sec_hubb.u_effective.to('eV').magnitude) == 4.5
    assert sec_hubb.double_counting_correction == 'Dudarev'


def test_gw(parser):
    """Tests for GW calculations in an atom, He"""
    archive = EntryArchive()
    parser._calculation_type = 'gw'
    parser.parse('tests/data/fhiaims/He_gw/He_scGW_ontop_PBE.out', archive, None)

    sec_run = archive.run[-1]

    # System
    sec_system = sec_run.system
    assert len(sec_system) == 1
    assert sec_system[-1].atoms.labels == ['He']
    assert sec_system[-1].atoms.periodic == [False, False, False]

    # Method
    sec_method = archive.run[-1].method
    assert len(sec_method) == 1
    assert sec_method[-1].gw.type == 'scGW'
    assert sec_method[-1].gw.analytical_continuation == 'pade'
    assert sec_method[-1].gw.n_states == 5
    assert sec_method[-1].frequency_mesh.n_points == len(sec_method[-1].frequency_mesh.points)
    assert sec_method[-1].frequency_mesh.points[-1].to('hartree').magnitude == approx(3571.4288641158605 + 0j)

    # GW energies
    sec_scf = sec_run.calculation[-1].scf_iteration
    assert len(sec_scf) == 5
    assert sec_scf[0].x_fhi_aims_energy_scgw_correlation_energy.to('eV').magnitude == approx(-2.392295)
    assert sec_scf[-1].x_fhi_aims_energy_scgw_correlation_energy.to('eV').magnitude == approx(-1.73791)


def test_gw_eigs(parser):
    """Tests for GW calculations in a molecule, CHN"""
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/CHN_gw/output.out', archive, None)

    sec_run = archive.run[-1]

    # System and Method
    sec_system = sec_run.system
    assert len(sec_system) == 1
    assert sec_system[-1].atoms.labels[0] == 'O'
    sec_method = sec_run.method
    assert len(sec_method) == 1
    assert sec_method[-1].m_xpath('gw')
    assert sec_method[-1].gw.type == 'G0W0'
    assert sec_method[-1].gw.n_states == 1590
    assert sec_method[-1].gw.analytical_continuation == 'pade'

    # GW eigenvalues
    sec_eigs_gw = sec_run.calculation[-1].eigenvalues[0]
    assert sec_eigs_gw.value_qp.shape == (1, 1, 81)
    assert sec_eigs_gw.value_correlation[-1][0][0].to('eV').magnitude == approx(10.4622)
    assert sec_eigs_gw.value_exchange[-1][0][0].to('eV').magnitude == approx(-99.6569)
    assert sec_eigs_gw.value_qp[-1][0][0].to('eV').magnitude == approx(-550.2817)
    assert sec_eigs_gw.value_ks[-1][0][0].to('eV').magnitude == approx(-524.2553)
    assert sec_eigs_gw.value_ks_xc[-1][0][0].to('eV').magnitude == approx(-63.1682)


def test_gw_bands(parser):
    """Tests for GW calculations in a solid, Si2"""
    archive = EntryArchive()
    parser.parse('tests/data/fhiaims/Si_pbe_vs_gw_bands/aims.out', archive, None)

    sec_run = archive.run[-1]

    # System and Method
    assert sec_run.system[-1].atoms.labels == ['Si', 'Si']
    sec_method = sec_run.method[-1]
    assert list(sec_method.k_mesh.grid) == [8] * 3
    assert sec_method.gw.type == 'G0W0'

    sec_scc = sec_run.calculation[-1]
    assert sec_scc.energy.fermi.to('eV').magnitude == approx(-5.73695796)
    assert len(sec_scc.band_structure_electronic[0].segment) == 10
    assert sec_scc.band_structure_electronic[0].segment[0].kpoints.shape == (17, 3)
    assert sec_scc.band_structure_electronic[0].segment[-1].occupations.shape == (1, 6, 24)

# WATCH OUT: reset (if needed) self._calculation_type accordingly after the GW tests!
