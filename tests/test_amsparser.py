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
from electronicparsers.ams import AMSParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return AMSParser()


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ams/scf/phenylrSmall-metagga.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '70630 2018-11-24'
    assert sec_run.time_run.date_start.magnitude == 1550053118.0

    sec_method = archive.run[0].method[0]
    assert sec_method.electronic.n_spin_channels == 2
    assert sec_method.electronic.relativity_method == 'scalar_relativistic_atomic_ZORA'
    assert sec_method.electronic.charge == 0.0
    assert sec_method.scf.x_ams_diis_settings_dirac['Method'] == 'diis'
    assert sec_method.scf.x_ams_diis_settings_scf['Cond'] == approx(1.0e6)
    assert not sec_method.scf.x_ams_degenerate
    assert sec_method.scf.x_ams_growth_factor == approx(1.1)
    assert sec_method.scf.x_ams_convrg == approx(1.0e-6)
    assert sec_method.x_ams_nuclear_charge_density_model == 'Point Charge Nuclei'
    assert sec_method.x_ams_grimme_d3_dispersion_correction['damping'] == 'BJ'
    assert sec_method.x_ams_grimme_d3_dispersion_correction['s8'] == approx(1.944)
    assert sec_method.x_ams_other_parameters['version'] == 4
    assert sec_method.dft.xc_functional.contributions[0].name == 'MGGA_XC_TPSS'
    sec_atom = sec_method.atom_parameters
    assert len(sec_atom) == 2
    assert sec_atom[0].x_ams_radial_points == 3000
    assert sec_atom[1].x_ams_nuclear_charge == approx(1.0)
    assert sec_atom[0].n_valence_electrons == 4
    assert sec_atom[1].charge == approx(0.0)
    assert sec_atom[0].orbitals[1] == '2S'
    assert sec_atom[1].x_ams_orbital_energies[0].magnitude == approx(-1.01788704e-18)
    assert sec_atom[0].x_ams_orbital_radii[2] == approx(1.794)
    assert sec_atom[1].x_ams_energy_sum_eigenvalues.magnitude == approx(-1.01800039e-18)
    assert sec_atom[0].x_ams_energy_kinetic.magnitude == approx(1.62379128e-16)
    assert sec_atom[1].x_ams_n_radial_fit_functions == 0
    assert sec_atom[0].label == 'C'
    assert sec_atom[1].x_ams_cutoff_valence == approx(23.76)
    assert sec_atom[0].x_ams_cutoff_core_kinetic == approx(4.36)
    assert sec_method.x_ams_run_config['Zlm fitting']

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.positions[2][1].magnitude == approx(2.31103866e-10)
    assert sec_system.atoms.lattice_vectors[0][0].magnitude == approx(8.72113987e-10)
    assert sec_system.atoms.periodic == [True, True, False]

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-1.11415974e-17)
    assert sec_scc.energy.electronic.kinetic.magnitude == approx(1.11552116e-17)
    assert sec_scc.energy.xc.value.magnitude == approx(-1.01588269e-17)
    assert sec_scc.energy.electrostatic.value.magnitude == approx(-8.69562185e-18)
    sec_charges = sec_scc.charges
    assert sec_charges[0].analysis_method == 'Hirshfeld'
    assert sec_charges[2].value[3].magnitude == approx(-1.69830723e-20)
    assert sec_charges[1].spins[7] == approx(-0.011)
    assert sec_charges[3].total.magnitude == 0.0
    assert sec_charges[-1].analysis_method == 'Mulliken'
    assert len(sec_charges[-1].spin_projected) == 22
    assert sec_charges[-1].spin_projected[2].atom_index == 1
    assert sec_charges[-1].spin_projected[5].value.magnitude == approx(3.25882727e-19)
    assert len(sec_charges[-1].orbital_projected) == 206
    assert sec_charges[-1].orbital_projected[11].value.magnitude == approx(
        3.25241857e-20
    )
    assert sec_charges[-1].orbital_projected[26].orbital == '2s'
    assert sec_scc.multipoles[0].dipole.total[0] == approx(2.84126561e-30)
    assert sec_scc.eigenvalues[0].x_ams_energy_min[0][3].magnitude == approx(
        -2.51827575e-18
    )
    assert sec_scc.eigenvalues[0].x_ams_energy_max[1][16].magnitude == approx(
        -2.32112809e-19
    )
    assert sec_scc.eigenvalues[0].occupations[1][0][14] == 0.0
    assert sec_scc.eigenvalues[0].band_gap[0].value.magnitude == approx(4.22895238e-19)
    assert sec_scc.eigenvalues[0].band_gap[
        0
    ].energy_highest_occupied.magnitude == approx(-1.07685695e-18)
    assert sec_scc.eigenvalues[0].band_gap[0].x_ams_conduction_band_index == 15

    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 20
    assert sec_scfs[11].energy.change.magnitude == approx(2.1449944e-21)


def test_geometry_optimization(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ams/go/phenylrSmall-geoopt.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 22
    assert sec_sccs[17].energy.total.value.magnitude == approx(-1.10701399e-17)
    assert sec_sccs[3].energy.xc.value.magnitude == approx(-1.00379617e-17)
    assert sec_sccs[2].energy.electrostatic.value.magnitude == approx(-8.83926829e-18)
    assert sec_sccs[14].energy.electronic.kinetic.magnitude == approx(1.07350325e-17)
    assert sec_sccs[19].energy.x_ams_fit_error_correction.value.magnitude == approx(
        -8.0916862e-23
    )
    assert sec_sccs[0].energy.x_ams_v_atomic_def.value.magnitude == approx(
        -3.6046467e-18
    )
    assert sec_sccs[2].energy.x_ams_dispersion.value.magnitude == approx(-4.7877583e-20)
    assert len(sec_sccs[6].scf_iteration) == 11
    assert sec_sccs[10].forces.total.value[5][1].magnitude == approx(3.11423748e-11)
    assert sec_sccs[20].forces.x_ams_dispersion.value[9][0].magnitude == approx(
        -6.5909788e-12
    )
    assert sec_sccs[10].forces.x_ams_pair_interactions.value[1][2].magnitude == approx(
        8.9338246e-09
    )
    assert sec_sccs[8].forces.x_ams_electrostatic.value[6][1].magnitude == approx(
        -4.2076891e-08
    )
    assert sec_sccs[9].forces.x_ams_xc.value[3][2].magnitude == approx(3.04008897e-11)
    assert sec_sccs[5].forces.x_ams_electronic_kinetic.value[8][2].magnitude == approx(
        -3.4639301e-08
    )
    assert sec_sccs[1].forces.x_ams_p_matrix.value[4][0].magnitude == approx(
        -8.88908833e-09
    )
    assert sec_sccs[4].eigenvalues[0].x_ams_energy_min[0][15].magnitude == approx(
        -2.84386148e-19
    )

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 22
    assert sec_systems[3].atoms.positions[10][1].magnitude == approx(5.81904209e-10)
    assert sec_systems[9].atoms.lattice_vectors[1][1].magnitude == approx(
        7.56032016e-10
    )

    sec_methods = archive.run[0].method
    assert len(sec_methods) == 1
    assert not sec_methods[0].x_ams_run_config['Store original Bloch functions']
    assert sec_methods[0].atom_parameters[1].x_ams_cutoff_valence_kinetic == approx(
        24.05
    )
    assert (
        sec_methods[0].electronic.relativity_method == 'scalar_relativistic_atomic_ZORA'
    )


def test_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ams/dos/NiO-dos.out', archive, None)
    sec_scc = archive.run[0].calculation[0]
    assert len(sec_scc.dos_electronic) == 2
    sec_dos_up = sec_scc.dos_electronic[0]
    sec_dos_down = sec_scc.dos_electronic[1]
    assert sec_dos_up.spin_channel == 0 and sec_dos_down.spin_channel == 1
    assert sec_dos_up.energies[78].magnitude == approx(-8.6717613e-20)
    assert sec_dos_down.total[0].value.shape == (158,)
    assert sec_dos_down.total[0].value[19].magnitude == approx(4.66493971e14)

    archive = EntryArchive()
    parser.parse('tests/data/ams/dos/NiO-dos-restricted.out', archive, None)
    sec_scc = archive.run[0].calculation[0]
    len(sec_scc.dos_electronic) == 1
    sec_dos = sec_scc.dos_electronic[0]
    assert sec_dos.total[0].value.shape == (154,)


def test_geometry_optimization_new(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ams/go/EDUSIF.out', archive, None)

    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 14
    assert sec_scc[10].energy.total.value.magnitude == approx(-4.25064334e-15)
    assert sec_scc[-1].energy.electronic.value.magnitude == approx(-4.31446337e-15)
    assert sec_scc[-1].energy.electrostatic.value.magnitude == approx(2.31028918e-17)
    assert sec_scc[-1].energy.nuclear_repulsion.value.magnitude == approx(
        4.26346154e-17
    )
    assert sec_scc[-1].energy.x_ams_dispersion.value.magnitude == approx(
        -1.92033353e-18
    )
    assert sec_scc[-1].forces.total.value[163][0].magnitude == approx(-1.43919212e-11)
    assert sec_scc[-1].forces.x_ams_electronic.value[7][2].magnitude == approx(
        -2.99480631e-09
    )
    assert sec_scc[-1].forces.x_ams_electrostatic.value[291][1].magnitude == approx(
        9.48766784e-11
    )
    assert sec_scc[-1].forces.x_ams_nuclear_repulsion.value[3][2].magnitude == approx(
        -4.79941725e-09
    )
    assert sec_scc[-1].forces.x_ams_dispersion.value[423][1].magnitude == approx(
        -1.1331013e-11
    )
    assert sec_scc[-1].charges[0].value[21].magnitude == approx(-3.10822267e-21)
    assert sec_scc[-1].charges[1].analysis_method == 'Mulliken'
    assert sec_scc[-1].charges[1].value[29].magnitude == approx(-8.62902976e-20)
    assert sec_scc[-1].eigenvalues[0].x_ams_energy_min[0][11].magnitude == approx(
        -3.34244189e-18
    )
    assert sec_scc[-1].eigenvalues[0].occupations[0][0][775] == approx(2.0)

    sec_system = archive.run[0].system
    assert len(sec_system) == 14
    assert sec_system[4].atoms.positions[10][2].magnitude == approx(2.45975365e-09)
    assert sec_system[7].atoms.lattice_vectors[1][1].magnitude == approx(2.5832e-09)


def test_adf_sp(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ams/adf_SP/adf_SP.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '98925 2021-11-25'
    assert sec_run.program.x_ams_engine == 'adf'

    assert len(sec_run.method) == 1
    sec_method = sec_run.method[0]
    assert sec_method.dft.xc_functional.contributions[0].name == 'LDA_XC_VWN'
    assert sec_method.electronic.n_spin_channels == 1

    assert len(sec_run.system) == 1
    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels[0] == 'O'
    assert sec_system.atoms.positions.to('bohr')[1][0].magnitude == approx(
        -3.1867335262123166
    )

    assert len(sec_run.calculation) == 1
    sec_calc = sec_run.calculation[0]
    assert sec_calc.band_gap[0].energy_highest_occupied.to(
        'hartree'
    ).magnitude == approx(-0.2576927526332149)
    assert sec_calc.band_gap[0].energy_lowest_unoccupied.to(
        'hartree'
    ).magnitude == approx(-0.3054616645218846)
    assert sec_calc.energy.fermi.to('hartree').magnitude == approx(-0.28159925821297915)
    assert sec_calc.energy.x_ams_orthogonalization.value.to(
        'hartree'
    ).magnitude == approx(5.416521358379486e-06)
    assert sec_calc.energy.x_ams_orbital_interaction.value.to(
        'hartree'
    ).magnitude == approx(-0.921823054134502)
    assert sec_calc.energy.x_ams_pauli_coulomb.value.to('hartree').magnitude == approx(
        -2.492069688604461
    )
    assert sec_calc.energy.x_ams_bond.value.to('hartree').magnitude == approx(
        -0.25256548879865254
    )
    assert sec_calc.energy.total.value.to('hartree').magnitude == approx(
        -0.25256548879865254
    )
    assert sec_calc.energy.xc.value.to('hartree').magnitude == approx(
        -0.25252261177051805
    )
    assert sec_calc.charges[0].value.to('elementary_charge').magnitude[1] == approx(
        -1.2850914998807639e-08
    )


def test_band_go(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ams/band_pbe_GF/band_GF.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '98925 2021-11-25'
    assert sec_run.program.x_ams_engine == 'band'

    assert len(sec_run.system) == 1
    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels == ['Cs', 'Cl']
    assert sec_system.atoms.positions.to('bohr').magnitude[1][2] == approx(
        -3.892835816729087
    )
    assert sec_system.atoms.lattice_vectors.to('bohr').magnitude[1][1] == approx(
        7.785671633458174
    )
    assert np.all(sec_system.atoms.periodic)

    assert len(sec_run.calculation) == 1
    sec_calc = sec_run.calculation[0]
    assert sec_calc.energy.total.value.to('hartree').magnitude == approx(
        -0.23505514020774143
    )
    assert sec_calc.forces.total.value.to('hartree / bohr').magnitude[0][0] == approx(
        3.132257252867465e-22
    )
    assert sec_calc.band_gap[0].value.to('hartree').magnitude == approx(
        0.19174663326676872
    )
    assert sec_calc.band_gap[0].energy_highest_occupied.to(
        'hartree'
    ).magnitude == approx(-0.31612650570712414)
    assert sec_calc.band_gap[0].energy_lowest_unoccupied.to(
        'hartree'
    ).magnitude == approx(-0.12437987244035544)
    assert sec_calc.eigenvalues[0].energies.to('hartree').magnitude[0][2][18] == approx(
        0.7009522244059739
    )
    assert sec_calc.eigenvalues[0].occupations[0][0][3] == approx(1.9999999999999984)
    assert sec_calc.dos_electronic[0].energies.to('hartree').magnitude[78] == approx(
        0.04238290440428649
    )
    assert sec_calc.dos_electronic[0].total[0].value.to('1 / hartree').magnitude[
        24
    ] == approx(0.5740645825775643)
    assert sec_calc.charges[0].value.to('elementary_charge').magnitude[1] == approx(
        -0.2880699228617729
    )
    assert sec_calc.charges[1].value.to('elementary_charge').magnitude[0] == approx(
        0.6258874446060609
    )


def test_dftb_md(parser):
    archive = EntryArchive()
    parser.parse('tests/data/ams/dftb_MD/dftb_MD.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.x_ams_engine == 'dftb'

    sec_system = sec_run.system
    assert len(sec_system) == 1001
    assert sec_system[772].atoms.positions.to('bohr').magnitude[10][1] == approx(
        -3.28424033
    )
    assert sec_system[47].atoms.labels[8] == 'H'
    assert sec_system[144].atoms.velocities.to('bohr / fs').magnitude[9][2] == approx(
        -0.0024493607814810845
    )

    sec_calc = sec_run.calculation
    assert len(sec_calc) == 1001
    assert sec_calc[20].charges[0].value.to('elementary_charge').magnitude[6] == approx(
        0.35322952840842603
    )
    assert sec_calc[94].energy.total.potential.to('hartree').magnitude == approx(
        -23.066413874869223
    )
    assert sec_calc[502].energy.total.kinetic.to('hartree').magnitude == approx(
        0.04109780793407973
    )
    assert sec_calc[687].time.to('fs').magnitude == approx(171.75)
    assert sec_calc[341].temperature.magnitude == approx(740.3622235664087)
