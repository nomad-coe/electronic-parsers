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
from electronicparsers.cp2k import CP2KParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return CP2KParser()


def test_versioning(parser):
    """
    Test for breaking changes between versions.
    Known breaks:
    - v2023.1:
    -- Change of geometry section header from `MODULE QUICKSTEP: ATOMIC COORDINATES angstrom`
    to `MODULE QUICKSTEP: ATOMIC COORDINATES IN ANGSTROM`
    """

    # v2023.1: try elements and positions
    archive = EntryArchive()
    parser.parse(
        'tests/data/cp2k/version_2023_1/Defect_level_D_mode.548022.out', archive, None
    )

    sec_run = archive.run[0]
    assert sec_run.system[0].atoms.labels == 287 * ['Se'] + 144 * ['W']
    assert list(sec_run.system[0].atoms.positions[0].to('angstrom').magnitude) == [
        11.616523,
        1.916229,
        18.320724,
    ]


def test_single_point(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cp2k/single_point/si_bulk8.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == 'CP2K version 2.6.2'
    assert sec_run.x_cp2k_section_startinformation[0].x_cp2k_start_id == 8212
    assert sec_run.x_cp2k_section_end_information[0].x_cp2k_end_id == 8212
    assert sec_run.x_cp2k_global_settings.get('run_type') == 'ENERGY_FORCE'

    assert (
        sec_run.x_cp2k_section_end_information[0].x_cp2k_end_time
        == '2016-02-08 22:11:17.875'
    )
    assert sec_run.x_cp2k_program_information.get('svn_revision') == 'svn:15893'

    sec_input = sec_run.x_cp2k_section_input[0]
    assert (
        sec_input.x_cp2k_section_input_GLOBAL[0].x_cp2k_input_GLOBAL_PROJECT_NAME
        == 'Si_bulk8'
    )
    sec_force_eval_dft = sec_input.x_cp2k_section_input_FORCE_EVAL[
        0
    ].x_cp2k_section_input_FORCE_EVAL_DFT[0]
    assert (
        sec_force_eval_dft.x_cp2k_section_input_FORCE_EVAL_DFT_SCF[
            0
        ].x_cp2k_input_FORCE_EVAL_DFT_SCF_EPS_SCF
        == '1.0E-7'
    )

    sec_method = sec_run.method[0]
    sec_basis_sets = sec_method.electrons_representation[0].basis_set
    assert sec_basis_sets[0].atom_centered[0].name == 'DZVP-GTH-PADE'
    assert sec_basis_sets[1].cutoff.magnitude == approx(6.53961708e-16)
    assert sec_method.scf.threshold_energy_change.magnitude == approx(
        4.35974472220717e-25
    )
    assert sec_method.dft.xc_functional.contributions[0].name == 'LDA_XC_TETER93'
    sec_qs_settings = sec_method.x_cp2k_section_quickstep_settings[0]
    assert sec_qs_settings.x_cp2k_planewave_cutoff == 150.0
    sec_atom_kind = sec_qs_settings.x_cp2k_section_atomic_kinds[
        0
    ].x_cp2k_section_atomic_kind[0]
    assert sec_atom_kind.x_cp2k_kind_number_of_atoms == '8'
    assert (
        sec_atom_kind.x_cp2k_section_kind_basis_set[0].x_cp2k_basis_set_norm_type == 2
    )
    assert (
        sec_qs_settings.x_cp2k_section_total_numbers[0].x_cp2k_cartesian_basis_functions
        == 112
    )
    assert (
        sec_qs_settings.x_cp2k_section_maximum_angular_momentum[
            0
        ].x_cp2k_orbital_basis_functions
        == 2
    )
    assert sec_method.atom_parameters[0].atom_number == 14

    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-1.36450791e-16)
    assert sec_scc.forces.total.value[4][1].magnitude == approx(-8.2387235e-16)
    assert len(sec_scc.scf_iteration) == 10
    assert sec_scc.scf_iteration[1].energy.total.value.magnitude == approx(
        -1.35770357e-16
    )

    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels == ['Si'] * 8
    assert sec_system.atoms.positions[6][2].magnitude == approx(4.073023e-10)
    assert sec_system.atoms.lattice_vectors[2][2].magnitude == approx(5.431e-10)
    assert False not in sec_system.atoms.periodic

    assert archive.workflow2.m_def.name == 'SinglePoint'


def test_unterminated_section(parser):
    """Test the proper extraction of process ID"""
    archive = EntryArchive()
    parser.parse(
        'tests/data/cp2k/single_point/si_bulk8_unterminated.out', archive, None
    )
    assert archive.run[0].x_cp2k_section_startinformation[0].x_cp2k_start_id == 8212


def test_pdos(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/cp2k/graphene_15x15_pdos/Grafene15x15-alone-smear-cell-opt.out',
        archive,
        None,
    )

    assert len(archive.run) == 1
    sec_run = archive.run[-1]
    assert sec_run.program.version == 'CP2K version 6.1'
    assert sec_run.method[-1].dft.xc_functional.exchange[0].name == 'MGGA_X_TPSS'
    assert sec_run.method[-1].dft.xc_functional.exchange[1].name == 'GGA_X_PBE'
    assert sec_run.method[-1].dft.xc_functional.correlation[0].name == 'MGGA_C_TPSS'
    assert sec_run.method[-1].dft.xc_functional.correlation[1].name == 'GGA_C_PBE'

    sec_scc = sec_run.calculation
    assert len(sec_scc) == 1
    assert sec_scc[0].dos_electronic is not None
    sec_dos = sec_scc[0].dos_electronic
    assert len(sec_dos) == 2
    # Unrestricted spin-polarized calculation
    assert sec_dos[0].spin_channel == 0
    assert sec_dos[1].spin_channel == 1
    assert sec_dos[0].n_energies == 3713
    assert sec_dos[0].orbital_projected is not None
    assert len(sec_dos[0].orbital_projected) == 9
    assert sec_dos[1].n_energies == 3713
    assert len(sec_dos[0].orbital_projected) == len(sec_dos[1].orbital_projected)
    assert sec_dos[0].energy_fermi.to('hartree').magnitude == approx(-0.16863)
    # Storing original histogram
    assert sec_scc[0].x_cp2k_pdos is not None
    assert len(sec_scc[0].x_cp2k_pdos) == 2
    assert sec_scc[0].x_cp2k_pdos[0].x_cp2k_gaussian_width.to('eV').magnitude == approx(
        0.5
    )
    assert sec_scc[0].x_cp2k_pdos[0].x_cp2k_gaussian_delta_energy.to(
        'eV'
    ).magnitude == approx(0.01)
    assert len(sec_scc[0].x_cp2k_pdos[0].x_cp2k_pdos_histogram_orbital) == 9
    assert sec_scc[0].x_cp2k_pdos[0].x_cp2k_pdos_histogram_orbital == [
        's',
        'py',
        'pz',
        'px',
        'd-2',
        'd-1',
        'd0',
        'd+1',
        'd+2',
    ]
    # Testing values
    dos_values = sec_dos[0].orbital_projected[2]
    assert dos_values.atom_label == 'C'
    assert dos_values.orbital == 'pz'
    assert dos_values.value.to('1/eV').magnitude[1050] == approx(1.2619316298909414e-05)
    assert (dos_values.value.to('1/eV').magnitude > 0).all()


def test_geometry_optimization(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cp2k/geometry_optimization/H2O.out', archive, None)

    sec_workflow = archive.workflow2
    assert sec_workflow.method.method == 'conjugate gradient'
    sec_opt = sec_workflow.x_cp2k_section_geometry_optimization[0]
    assert len(sec_opt.x_cp2k_section_geometry_optimization_step) == 11
    assert sec_opt.x_cp2k_section_geometry_optimization_step[
        2
    ].x_cp2k_optimization_rms_gradient == approx(1.0992366882757706e-10)
    assert sec_opt.x_cp2k_section_geometry_optimization_step[
        -1
    ].x_cp2k_optimization_energy_change == approx(-2.306304958047593e-25)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 13
    assert sec_sccs[7].energy.xc.value.to('hartree').magnitude == approx(-4.1274870248)
    assert len(sec_sccs[2].scf_iteration) == 6
    assert sec_sccs[11].scf_iteration[-1].energy.total.value.to(
        'hartree'
    ).magnitude == approx(-17.1646260706)
    assert sec_sccs[1].scf_iteration[1].time_calculation.magnitude == approx(0.5)
    assert sec_sccs[2].time_physical.magnitude == approx(14.4)
    assert sec_sccs[3].scf_iteration[3].time_physical.magnitude == approx(16.3)
    assert sec_sccs[4].time_calculation.magnitude == approx(1.8)

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 13
    assert sec_systems[6].atoms.positions[1][1].to('angstrom').magnitude == approx(
        2.2567157451
    )


def test_molecular_dynamics(parser):
    archive = EntryArchive()
    parser.parse('tests/data/cp2k/molecular_dynamics/H2O-32.out', archive, None)

    sec_workflow = archive.workflow2
    assert sec_workflow.method.thermodynamic_ensemble == 'NVE'
    assert (
        sec_workflow.method.x_cp2k_section_md_settings[0].x_cp2k_md_print_frequency == 1
    )

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 11
    assert len(sec_sccs[6].scf_iteration) == 7
    assert sec_sccs[3].energy.total.value.to('hartree').magnitude == approx(
        -34.32799897809764
    )
    assert sec_sccs[9].energy.kinetic.value.to('hartree').magnitude == approx(
        0.005371243
    )
    assert sec_sccs[7].temperature.magnitude == approx(230.324748558)
    assert sec_sccs[1].time_physical.magnitude == approx(5.2)
    assert sec_sccs[3].time_calculation.magnitude == approx(2.0)

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 11
    assert sec_systems[5].atoms.positions[4][0].to('angstrom').magnitude == approx(
        0.5824842170
    )
