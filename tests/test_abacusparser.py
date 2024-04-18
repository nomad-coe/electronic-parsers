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
from electronicparsers.abacus import ABACUSParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return ABACUSParser()


def test_band(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/Si_band/running_nscf.log', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == 'Parallel, in development'
    assert sec_run.time_run.date_start.magnitude == approx(1657036247.0)
    sec_parallel = sec_run.x_abacus_section_parallel[0]
    assert sec_parallel.x_abacus_nproc == 8
    assert sec_parallel.x_abacus_allocation_method == '2D block'
    assert sec_parallel.x_abacus_allocation_nb2d == 1
    assert sec_parallel.x_abacus_allocation_trace_loc_row == 26
    assert sec_parallel.x_abacus_allocation_trace_loc_col == 26
    assert sec_parallel.x_abacus_allocation_nloc == 91
    assert sec_run.x_abacus_input_filename == 'INPUT'
    assert sec_run.x_abacus_kpt_filename == 'KLINES'
    assert sec_run.time_run.date_end.magnitude == approx(1657036249.0)
    assert sec_run.clean_end

    sec_method = sec_run.method[0]
    sec_basis_set = sec_method.electrons_representation[0].basis_set[0]
    assert sec_basis_set.type == 'numeric AOs'
    assert sec_basis_set.cutoff.to('Ry').magnitude == approx(50)
    sec_basis_set = sec_method.electrons_representation[1].basis_set[0]
    assert sec_basis_set.x_abacus_basis_sets_delta_k.magnitude == approx(0.01)
    assert sec_basis_set.x_abacus_basis_sets_delta_r.magnitude == approx(0.01)
    assert sec_basis_set.x_abacus_basis_sets_dr_uniform.magnitude == approx(0.001)
    assert sec_basis_set.x_abacus_basis_sets_rmax.magnitude == approx(30)
    assert sec_basis_set.x_abacus_basis_sets_kmesh == 711  # Update test to new KMesh
    sec_specie_basis_set = sec_basis_set.x_abacus_section_specie_basis_set
    assert (
        sec_specie_basis_set[0].x_abacus_specie_basis_set_filename
        == 'Si_lda_8.0au_50Ry_2s2p1d'
    )
    assert (
        sec_specie_basis_set[0].x_abacus_specie_basis_set_ln
        == [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
    ).all()
    assert sec_specie_basis_set[0].x_abacus_specie_basis_set_rcutoff.magnitude == 8
    assert sec_specie_basis_set[0].x_abacus_specie_basis_set_rmesh == 801
    assert sec_method.electronic.n_spin_channels == 1
    assert not sec_method.x_abacus_spin_orbit
    assert sec_method.electronic.relativity_method == 'scalar_relativistic'
    sec_atom_parameters = sec_method.atom_parameters
    assert len(sec_atom_parameters) == 1
    assert sec_atom_parameters[0].label == 'Si'
    assert sec_atom_parameters[0].n_valence_electrons == 4
    assert sec_atom_parameters[0].pseudopotential_name == 'Si.pz-vbc.UPF'
    assert sec_atom_parameters[0].x_abacus_pp_type == 'NC'
    assert sec_atom_parameters[0].x_abacus_pp_xc == 'PZ'
    assert sec_atom_parameters[0].x_abacus_pp_lmax == 1
    assert sec_atom_parameters[0].x_abacus_pp_nzeta == 2
    assert sec_atom_parameters[0].x_abacus_pp_nprojectors == 2
    assert sec_method.dft.xc_functional.correlation[0].name == 'LDA_C_PZ'

    sec_system = sec_run.system[0]
    assert sec_system.x_abacus_alat.magnitude == approx(10.2)
    assert sec_system.atoms.lattice_vectors[0][1].magnitude == approx(2.69880378e-10)
    assert sec_system.atoms.labels == ['Si', 'Si']
    assert sec_system.atoms.positions[1][0].magnitude == approx(1.34940189e-10)
    assert sec_system.x_abacus_cell_volume.magnitude == approx(265.302)
    assert sec_system.x_abacus_reciprocal_vectors[2][0].magnitude == approx(
        -1.16406857e10
    )
    assert sec_system.atoms.n_atoms == 2
    assert sec_system.x_abacus_number_of_species == 1
    assert sec_system.x_abacus_number_of_electrons_out[0] == 8

    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    assert sec_scc.x_abacus_longest_orb_rcut.magnitude == approx(8)
    assert sec_scc.x_abacus_longest_nonlocal_projector_rcut.magnitude == approx(5.01)
    assert sec_scc.x_abacus_searching_radius.magnitude == approx(26)
    assert sec_scc.x_abacus_searching_radius_unit.magnitude == approx(10.2)
    assert sec_scc.x_abacus_read_space_grid[0] == 36
    assert sec_scc.x_abacus_big_cell_numbers_in_grid[2] == 18
    assert sec_scc.x_abacus_meshcell_numbers_in_big_cell[1] == 2
    assert sec_scc.x_abacus_extended_fft_grid[0] == 25
    assert sec_scc.x_abacus_extended_fft_grid_dim[2] == 69
    sec_k_band = sec_scc.band_structure_electronic[0]
    assert sec_k_band.energy_fermi.magnitude == approx(1.055136698179135e-18)
    assert sec_k_band.reciprocal_cell[0][0].magnitude == approx(1.16406857e10)
    sec_k_band_segment = sec_k_band.segment[0]
    assert sec_k_band_segment.kpoints.shape == (101, 3)
    assert sec_k_band_segment.kpoints[3][2] == approx(0.425)
    assert sec_k_band_segment.energies.shape == (1, 101, 8)
    assert sec_k_band_segment.energies[0][4][4].magnitude == approx(1.14715847e-18)

    assert archive.workflow2.method.method == 'DFT'


# TODO iteration is None in sub_section
def test_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/Si_dos/running_nscf.log', archive, None)

    sec_run = archive.run[0]
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    sec_k_band = sec_scc.band_structure_electronic[0]
    assert sec_k_band.energy_fermi.magnitude == approx(1.055136698179135e-18)
    energy_reference = sec_k_band.energy_fermi.to('eV').magnitude

    assert len(sec_scc.dos_electronic) == 1
    sec_dos = sec_scc.dos_electronic[0]
    assert not sec_dos.spin_channel
    n_energies = sec_dos.n_energies
    assert n_energies == 2265
    assert sec_dos.energies.shape == (n_energies,)
    assert len(sec_dos.total) == 1
    assert sec_dos.total[0].value.shape == (n_energies,)

    energies = sec_dos.energies.to('eV').magnitude
    values = sec_dos.total[0].value.to('1/eV').magnitude
    nonzero = np.unique(values.nonzero())
    energies = energies[nonzero]
    energies.sort()
    lowest_unoccupied_index = np.searchsorted(energies, [energy_reference], 'right')[0]
    highest_occupied_index = lowest_unoccupied_index - 1
    gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
    assert gap == approx(0.01)


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/Si_scf/running_scf.log', archive, None)

    sec_run = archive.run[0]
    assert sec_run.x_abacus_program_execution_time.magnitude == approx(1.0)

    sec_method = sec_run.method[0]
    assert sec_method.scf.n_max_iteration == 20
    assert sec_method.x_abacus_basis_type == 'pw'

    sec_system = sec_run.system[0]
    sec_system_sym = sec_system.symmetry[0]
    assert sec_system_sym.crystal_system == 'cubic'
    assert sec_system.x_abacus_ibrav == 3
    assert sec_system_sym.bravais_lattice == 'cF'
    assert sec_system_sym.x_abacus_point_group_schoenflies_name == 'T_d'
    assert sec_system.x_abacus_celldm[0] == approx(3.8166849)
    assert sec_system.x_abacus_celldm[-1] == 60
    assert sec_system_sym.x_abacus_number_of_rotation_matrices == 48
    assert sec_system_sym.x_abacus_number_of_point_group_operations == 24
    assert sec_system_sym.x_abacus_number_of_space_group_operations == 24

    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    assert len(sec_scc.scf_iteration) == sec_scc.n_scf_iterations
    assert sec_scc.energy.xc.value.magnitude == approx(-1.0521129713661978e-17)
    assert sec_scc.energy.electrostatic.correction.magnitude == approx(
        2.402022465119184e-18
    )
    assert sec_scc.energy.hartree_fock_x_scaled.value.magnitude == approx(0.0)
    assert sec_scc.energy.total.value.magnitude == approx(-3.452765284822062e-17)
    sec_scf = sec_scc.scf_iteration
    assert sec_scf[5].x_abacus_density_change_scf_iteration == approx(8.46207322367e-10)
    assert sec_scf[5].x_abacus_energy_total_harris_foulkes_estimate.magnitude == approx(
        -3.452765284886149e-17
    )
    assert sec_scf[0].energy.total.value.magnitude == approx(-3.451916016970848e-17)
    assert sec_scf[2].energy.fermi.magnitude == approx(1.0082248524478308e-18)
    sec_eigenvalues = sec_scc.eigenvalues[0]
    assert sec_eigenvalues.energies.shape == (1, 8, 4)
    assert sec_eigenvalues.energies[0][4][1].magnitude == approx(
        -2.3289399769487398e-20
    )
    assert sec_eigenvalues.occupations.shape == (1, 8, 4)
    assert sec_eigenvalues.occupations[0][6][1] == approx(0.0937500)
    assert sec_eigenvalues.kpoints.shape == (8, 3)
    assert sec_eigenvalues.kpoints[4][0] == approx(0.75)
    assert sec_eigenvalues.x_abacus_eigenvalues_number_of_planewaves[3] == 191


def test_geomopt(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/Si_geomopt/running_cell-relax.log', archive, None)

    sec_run = archive.run[0]

    sec_method = sec_run.method[0]
    # TODO smearing is None
    assert sec_method.electronic.smearing.kind == 'gaussian'
    assert sec_method.electronic.smearing.width == approx(2.179872361103585e-20)
    assert sec_method.x_abacus_gamma_algorithms
    assert sec_method.electrons_representation[0].basis_set[0].type == 'numeric AOs'

    sec_workflow = archive.workflow2
    assert sec_workflow.method.convergence_tolerance_force_maximum.magnitude == approx(
        1.6021766339999997e-12
    )
    assert sec_workflow.method.convergence_tolerance_stress_maximum.magnitude == approx(
        1000000.0
    )

    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 50
    # TODO empty sub sections
    assert sec_sccs[20].n_scf_iterations == 10
    assert sec_sccs[20].forces.total.value.shape == (2, 3)
    assert sec_sccs[20].forces.total.value[1][0].magnitude == approx(
        -1.292767486795188e-11
    )
    assert sec_sccs[42].stress.total.value[1][1].magnitude == approx(62419700.0)
    assert sec_sccs[10].pressure.magnitude == approx(-100095500.0)
    assert sec_sccs[48].energy.fermi.magnitude == approx(-6.769734186416427e-19)


def test_md(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/Sn_md/running_md.log', archive, None)

    sec_run = archive.run[0]
    assert sec_run.x_abacus_md_nstep_in == 10
    sec_run.x_abacus_md_nstep_out == 11

    sec_method = sec_run.method[0]
    assert sec_method.x_abacus_scf_threshold_density == approx(1e-5)
    assert sec_method.x_abacus_mixing_beta == approx(0.4)
    assert archive.workflow2.method.thermodynamic_ensemble == 'NVT'

    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 11
    assert sec_sccs[5].energy.electronic.kinetic.magnitude == approx(
        1.748126841263409e-18
    )
    assert sec_sccs[9].temperature.magnitude == approx(1269.5343)
    assert sec_sccs[0].energy.total.value.magnitude == approx(-9.855490687700974e-16)


# TODO no test data
def test_hse(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/GaSb_hse/running_scf.log', archive, None)

    sec_run = archive.run[0]
    assert sec_run.x_abacus_program_execution_time.magnitude == 8837

    sec_method = sec_run.method[0]
    assert sec_method.dft.xc_functional.hybrid[0].name == 'HYB_GGA_XC_HSE06'
    assert sec_method.dft.xc_functional.hybrid[0].parameters[
        '$\\omega$ in m^-1'
    ] == approx(2078698737.084507)
    assert (
        sec_method.dft.xc_functional.hybrid[0].parameters[
            'hybrid coefficient $\\alpha$'
        ]
        == 0.25
    )
    assert sec_method.x_abacus_hse_omega.magnitude == approx(2078698737.084507)
    assert sec_method.x_abacus_hybrid_xc_coeff == approx(0.25)
    assert sec_method.x_abacus_mixing_method == 'pulay'
    assert sec_method.x_abacus_exx_ccp_rmesh_times == approx(1.5)
    assert sec_method.x_abacus_exx_dm_threshold == approx(0.0005)
    assert sec_method.x_abacus_exx_cauchy_threshold == approx(1e-08)
    assert sec_method.x_abacus_exx_schwarz_threshold == approx(5e-05)
    assert sec_method.x_abacus_exx_c_threshold == approx(5e-05)
    assert sec_method.x_abacus_exx_pca_threshold == approx(0.0001)

    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels == ['Sb', 'Ga']
    assert sec_system.atoms.positions[1][2].magnitude == approx(4.571926147831032e-10)

    sec_scc = sec_run.calculation[0]
    assert sec_scc.n_scf_iterations == 55
    assert sec_scc.energy.hartree_fock_x_scaled.value.magnitude == approx(
        -1.2417912255666503e-17
    )


def test_spin2(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/Si_spin2/running_nscf.log', archive, None)
    sec_run = archive.run[0]

    sec_method = sec_run.method[0]
    assert sec_method.electronic.n_spin_channels == 2

    sec_scc = sec_run.calculation[0]
    # TODO fermi energy not set
    sec_k_band = sec_scc.band_structure_electronic[0]
    assert sec_k_band.energy_fermi.magnitude == 0
    sec_k_band_segment = sec_k_band.segment[0]
    assert sec_k_band_segment.energies.shape == (2, 1728, 8)
    assert sec_k_band_segment.energies[0][1][2].magnitude == approx(
        1.0292510870946719e-18
    )

    assert len(sec_scc.dos_electronic) == 2
    sec_dos_up = sec_scc.dos_electronic[0]
    sec_dos_down = sec_scc.dos_electronic[1]
    assert sec_dos_up.spin_channel == 0
    assert sec_dos_up.spin_channel != sec_dos_down.spin_channel
    assert sec_dos_up.energies.shape == (2265,)
    assert len(sec_dos_up.total) == len(sec_dos_down.total)
    assert sec_dos_up.total[0].value.shape == (2265,)


def test_dftu(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abacus/MnBiTe_dftu/running_scf.log', archive, None)

    sec_run = archive.run[0]

    sec_method = sec_run.method[0]
    assert sec_method.electronic.n_spin_channels == 1
    assert sec_method.x_abacus_spin_orbit
    # TODO include  full relativistic
    # assert sec_method.electronic.relativity_method == 'full relativistic'
    assert sec_method.x_abacus_initial_magnetization_total == 0.0
    assert sec_method.x_abacus_diagonalization_algorithm == 'genelpa'
    assert sec_method.electronic.method == 'DFT+U'

    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels == [
        'Mn',
        'Mn',
        'Bi',
        'Bi',
        'Bi',
        'Bi',
        'Te',
        'Te',
        'Te',
        'Te',
        'Te',
        'Te',
        'Te',
        'Te',
    ]
    assert sec_system.x_abacus_number_of_species == 4

    sec_scc = sec_run.calculation[0]
    sec_scf = sec_scc.scf_iteration
    assert sec_scf[9].x_abacus_magnetization_total[2].magnitude == approx(-0.00029174)
    assert sec_scf[16].x_abacus_magnetization_absolute.magnitude == approx(10.04743427)
