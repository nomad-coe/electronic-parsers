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
from electronicparsers.orca import OrcaParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return OrcaParser()


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/orca/CO_scf/orca3.2985087.out', archive, None)

    assert archive.run[0].program.version == '3.0.3 - RELEASE   -'

    sec_method = archive.run[0].method[0]
    assert sec_method.electronic.method == 'DFT'
    assert sec_method.x_orca_nelectrons == 14.0
    assert sec_method.scf.threshold_energy_change.to('hartree').magnitude == 1.0e-6
    assert sec_method.scf.threshold_density_change == 1.0e-6
    assert sec_method.scf.x_orca_last_max_density_change == 1e-5
    assert sec_method.x_orca_radial_grid_type == 'Gauss-Chebyshev'
    assert len(sec_method.dft.xc_functional.exchange) == 2
    assert sec_method.dft.xc_functional.correlation[0].name == 'GGA_C_LYP'
    sec_basis = sec_method.electrons_representation[0].basis_set
    assert len(sec_basis) == 3
    assert sec_basis[1].x_orca_basis_set == '11s6p2d1f'
    assert sec_basis[2].x_orca_nb_of_primitive_gaussian_functions == 92

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels == ['C', 'O']
    assert sec_system.atoms.positions[1][0].magnitude == approx(1.25e-10)

    assert len(archive.run[0].calculation) == 1
    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-4.94114851e-16)
    assert sec_scc.x_orca_potential_energy == approx(-9.84253575e-16)
    assert sec_scc.x_orca_nb_elect_total == approx(14.000005402207)
    assert len(sec_scc.scf_iteration) == 8
    assert sec_scc.scf_iteration[3].energy.total.value.magnitude == approx(
        -4.94113458e-16
    )
    assert np.shape(sec_scc.eigenvalues[0].energies[0][0]) == (62,)
    assert sec_scc.eigenvalues[0].energies[0][0][28].magnitude == approx(6.53237991e-18)
    assert sec_scc.eigenvalues[0].occupations[0][0][6] == 2.0
    assert len(sec_scc.charges[0].value) == 2
    assert sec_scc.charges[0].value[0].magnitude == 0.131793
    assert sec_scc.charges[0].orbital_projected[27].value.magnitude == 0.027488
    assert sec_scc.x_orca_diis_solution == 0.003


def test_geomopt(parser):
    archive = EntryArchive()
    parser.parse('tests/data/orca/CHO_geomopt/orca3.2985006.out', archive, None)

    sec_run = archive.run[0]
    assert len(sec_run.method) == 6
    assert len(sec_run.system) == 6
    sec_scc = sec_run.calculation
    assert len(sec_scc) == 6

    assert sec_run.method[2].x_orca_nb_grid_pts_after_weights_screening == 34298
    assert sec_run.method[4].x_orca_integr_weight_cutoff == 1e-14
    assert sec_run.system[1].atoms.positions[2][1].magnitude == approx(9.54068e-11)
    assert len(sec_scc[0].scf_iteration) == 13
    assert sec_scc[-1].x_orca_elec_energy == approx(-6.34048432e-16)
    assert sec_scc[0].time_calculation.magnitude == approx(3.373)
    assert sec_scc[2].time_physical.magnitude == approx(7.373)


def test_spinpol(parser):
    archive = EntryArchive()
    parser.parse('tests/data/orca/BO_spinpol/orca3.2984863.out', archive, None)

    assert archive.run[0].method[0].x_orca_multiplicity == 2
    sec_eig = archive.run[0].calculation[0].eigenvalues[0]
    assert np.shape(sec_eig.energies[1][0]) == (28,)
    assert sec_eig.energies[1][0][22].magnitude == approx(7.57745431e-18)
    assert sec_eig.occupations[0][0][2] == 1.0
    sec_charges = archive.run[0].calculation[0].charges[0]
    assert sec_charges.value[0].magnitude == -0.01143
    assert sec_charges.orbital_projected[14].value.magnitude == 1.450488


def test_ci(parser):
    archive = EntryArchive()
    parser.parse('tests/data/orca/FeMgO_ci/orca3.2713636.out', archive, None)

    sec_method = archive.run[0].method[1]
    assert sec_method.electronic.method == 'CCSD'
    assert sec_method.x_orca_single_excitations_on_off == 'ON'
    assert sec_method.x_orca_t1_diagnostic == approx(6.77481921e-20)

    sec_system = archive.run[0].system[0]
    assert sec_system.atoms.labels == ['Fe'] + ['O'] * 6 + ['Mg'] * 18 + ['Q'] * 704
    assert sec_system.atoms.positions[39][1].magnitude == approx(-4.211228e-10)

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.x_orca_ccsd_total_energy == approx(-1.70953359e-14)


def test_tddft(parser):
    archive = EntryArchive()
    parser.parse('tests/data/orca/ClTi_tddft/orca3.2706823.out', archive, None)

    assert archive.run[0].method[1].electronic.method == 'TDDFT'
    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.spectra[0].excitation_energies[8].magnitude == approx(7.85956552e-16)
    assert sec_scc.spectra[0].transition_dipole_moments[21][1].magnitude == approx(
        -2.96742377e-33
    )
