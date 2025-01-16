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
from nomad.units import ureg
from electronicparsers.quantumespresso import QuantumEspressoParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return QuantumEspressoParser()


def RyB_to_N(value):
    return (value * ureg.rydberg / ureg.bohr).to_base_units().magnitude


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/quantumespresso/HO_scf/benchmark2.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '5.2.1 (svn rev. 11920)'
    assert sec_run.x_qe_input_filename == 'uspp1.in'
    assert sec_run.time_run.date_start.magnitude == 1451140876.0
    assert sec_run.x_qe_section_compile_options[0].x_qe_lmaxx == 3
    assert sec_run.x_qe_section_parallel[0].x_qe_nproc == 4
    assert archive.workflow2 is not None
    assert 'rdiaghg' in sec_run.x_qe_profile_function
    assert sec_run.time_run.date_end.magnitude == 1451140881.0
    assert sec_run.clean_end

    sec_method = sec_run.method[0]
    assert len(sec_method.k_mesh.points) == 1
    # basis set
    sec_em = sec_method.electrons_representation
    assert sec_em[0].scope[0] == 'wavefunction'
    assert sec_em[0].basis_set[0].cutoff.to('Ry').magnitude == approx(25.0)
    assert sec_em[1].scope[0] == 'density'
    assert sec_em[1].basis_set[0].cutoff.to('Ry').magnitude == approx(100.0)
    assert sec_method.x_qe_sticks_sum_G_smooth == 135043

    assert 'NL pseudopotentials' in sec_method.x_qe_allocated_array_name
    assert sec_method.x_qe_allocated_array_size[2] == 33554432.0
    assert sec_method.x_qe_temporary_array_dimensions[3] == '262144,    8'
    assert sec_method.x_qe_per_process_mem == approx(2.84373811e08)
    assert sec_method.x_qe_potential_mixing_scheme == 'plain'
    assert sec_method.x_qe_starting_charge == 7.99998
    assert len(sec_method.dft.xc_functional.exchange) == 1
    assert sec_method.x_qe_xc_igcc_name == 'pbc'
    assert sec_method.dft.xc_functional.exchange[0].name == 'GGA_X_PBE'
    assert sec_method.electronic.n_electrons == 8
    assert sec_method.electronic.n_spin_channels == 1
    sec_atoms = sec_method.atom_parameters
    assert len(sec_atoms) == 2
    assert sec_atoms[1].label == 'H'
    assert sec_atoms[0].x_qe_pp_md5sum == '7e325307d184e51bd80757047dcf04f9'
    assert sec_atoms[1].x_qe_pp_ncoefficients == 8
    assert sec_atoms[0].x_qe_kind_mass == 16.0

    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels == ['O', 'H', 'H']
    assert sec_system.atoms.positions[2][0].magnitude == approx(5.12015994e-10)
    assert False not in sec_system.atoms.periodic
    assert sec_system.x_qe_reciprocal_cell[2][2].magnitude == approx(5.93674971e09)
    assert len(sec_system.x_qe_k_info_vec) == 1
    assert sec_system.x_qe_cell_volume == approx(1.18547769e-27)
    assert sec_system.x_qe_nsymm == 4
    assert sec_system.x_qe_dense_FFT_grid[1] == 64

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-7.49748432e-17)
    assert 'ewald contribution' in sec_scc.x_qe_energy_decomposition_name
    assert sec_scc.x_qe_energy_decomposition_value[1] == approx(7.42289975e-17)
    assert sec_scc.forces.total.value_raw[1][1].magnitude == approx(-3.57815176e-10)
    assert sec_scc.stress.total.value[2][2].magnitude == approx(-1.68e08)
    assert np.shape(sec_scc.eigenvalues[0].kpoints) == (1, 3)
    assert np.shape(sec_scc.eigenvalues[0].energies[0][0]) == (4,)
    assert sec_scc.eigenvalues[0].energies[0][0][2].magnitude == approx(-1.42427094e-18)
    assert sec_scc.energy.highest_occupied.magnitude == approx(-1.15444837e-18)
    assert sec_scc.x_qe_output_datafile == 'pwscf.save'
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 8
    assert sec_scfs[4].energy.total.value.magnitude == approx(-7.49748038e-17)
    assert sec_scfs[1].x_qe_energy_total_accuracy_estimate_iteration == approx(
        1.15623477e-18
    )
    assert sec_scfs[6].x_qe_iteration_ecutwfc == approx(5.4496809027589626e-17)
    # uncomment this when time_physical def is updated
    # assert sec_scfs[0].time_calculation.magnitude == 1.2
    assert sec_scfs[3].x_qe_iteration_charge_negative_up == 0.06614


def test_multirun(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/quantumespresso/Mn_multirun/9064627814752884918776106151027.log',
        archive,
        None,
    )

    sec_runs = archive.run
    sec_method = sec_runs[0].method[0]
    assert len(sec_runs) == 3
    assert len(sec_method.k_mesh.points) == 40
    assert sec_method.electronic.smearing.width == approx(2.3978595972139434e-20)
    assert sec_method.electronic.smearing.kind == 'fermi'
    assert sec_method.electronic.n_spin_channels == 2
    assert len(sec_runs[1].calculation[0].scf_iteration) == 111
    assert (
        sec_runs[2].calculation[0].scf_iteration[45].x_qe_iter_mpersite_magn[6]
        == -0.3325
    )
    assert sec_runs[0].system[0].x_qe_atom_starting_magnetization[1] == 0.133
    assert np.shape(sec_runs[0].calculation[0].eigenvalues[0].energies[1][19]) == (100,)
    assert np.shape(sec_runs[1].calculation[0].eigenvalues[0].energies[1][19]) == (100,)
    assert np.shape(sec_runs[2].calculation[0].eigenvalues[0].energies[1][19]) == (100,)
    assert len(sec_runs[0].calculation[0].eigenvalues[0].kpoints) == 20
    assert len(sec_runs[1].calculation[0].eigenvalues[0].kpoints) == 20
    assert len(sec_runs[2].calculation[0].eigenvalues[0].kpoints) == 20
    assert sec_runs[0].calculation[0].eigenvalues[0].kpoints[10][1] == approx(
        -0.1667096
    )
    assert sec_runs[1].calculation[0].eigenvalues[0].energies[0][3][
        -5
    ].magnitude == approx(1.42385437e-19)
    assert sec_runs[2].calculation[0].eigenvalues[0].energies[1][-10].magnitude[
        35
    ] == approx(-7.25180392e-18)
    assert sec_runs[0].calculation[0].time_calculation.magnitude == approx(9828.2)
    assert sec_runs[0].calculation[0].time_physical.magnitude == approx(9828.2)
    assert sec_runs[1].calculation[0].scf_iteration[
        6
    ].time_calculation.magnitude == approx(68.2)
    assert sec_runs[2].calculation[0].scf_iteration[
        11
    ].time_physical.magnitude == approx(1189.6)


def test_md(parser):
    archive = EntryArchive()
    parser.parse('tests/data/quantumespresso/Si_md/out.out', archive, None)

    assert archive.workflow2 is not None
    sec_run = archive.run[0]
    sec_method = sec_run.method[0]
    assert len(sec_method.k_mesh.points) == 1
    assert sec_method.electronic.n_spin_channels == 1
    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 50
    assert archive.run[0].system[6].atoms.positions[1][2].magnitude == approx(
        6.66987013e-11
    )
    assert sec_sccs[-3].forces.total.value_raw[1][1].magnitude == approx(9.55685747e-10)
    assert len(sec_sccs[22].scf_iteration) == 3
    assert sec_sccs[9].time_physical.magnitude == approx(0.4)
    assert sec_sccs[20].time_calculation.magnitude == approx(0)
    assert sec_sccs[2].scf_iteration[1].time_physical.magnitude == approx(0.1)
    assert sec_sccs[5].scf_iteration[2].time_calculation.magnitude == approx(0)


def test_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/quantumespresso/W_dos/w.dos.out', archive, None)

    sec_run = archive.run[0]
    sec_method = sec_run.method[0]
    assert sec_method.k_mesh.n_points == 413
    assert sec_method.k_mesh.points is None
    assert sec_method.electronic.smearing.kind == 'tetrahedra'
    assert sec_method.electronic.n_spin_channels == 1
    assert len(sec_run.calculation[0].dos_electronic) == 1
    sec_dos = sec_run.calculation[0].dos_electronic[0]
    assert np.shape(sec_dos.total[0].value) == (1801,)
    assert len(sec_dos.energies) == 1801
    assert sec_dos.energies[269].magnitude == approx(1.23207383e-18)
    assert sec_dos.total[0].value[150].magnitude == approx(2.8991809650870246e17)
    assert sec_dos.total[0].value_integrated[1316] == 8.582


def test_vcrelax(parser):
    archive = EntryArchive()
    parser.parse('tests/data/quantumespresso/TiO2_opt/pw.out', archive, None)

    sec_run = archive.run[0]
    sec_sccs = sec_run.calculation
    assert len(sec_sccs) == 6
    assert sec_sccs[0].forces.total.value_raw[3][1].magnitude == approx(
        RyB_to_N(-0.00389184)
    )
    assert sec_sccs[-1].forces.total.value_raw[5][0].magnitude == approx(
        RyB_to_N(0.00001090)
    )
    sec_method = sec_run.method[0]
    assert sec_method.electronic.smearing.kind == 'tetrahedra'
    assert sec_method.electronic.smearing.width is None
    assert sec_method.electronic.n_spin_channels == 1


def test_noncolmag(parser):
    archive = EntryArchive()
    parser.parse('tests/data/quantumespresso/Pt_noncol/pw.out', archive, None)

    sec_run = archive.run[0]
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[0]
    assert sec_scc.forces.total.value_raw[0][2].magnitude == approx(RyB_to_N(0.0))
    assert np.shape(sec_scc.eigenvalues[0].kpoints) == (288, 3)
    assert np.shape(sec_scc.eigenvalues[0].energies) == (1, 288, 26)
    assert len(sec_scc.dos_electronic) == 1
    assert len(sec_scc.dos_electronic[0].total[0].value) == 501
    assert (
        sec_scc.dos_electronic[0].total[0].value[500].magnitude
        == (0.4188 / ureg.eV).to_base_units().magnitude
    )

    sec_method = sec_run.method[0]
    assert sec_method.electronic.smearing.kind == 'gaussian'
    assert (
        sec_method.electronic.smearing.width
        == (0.01 * ureg.rydberg).to_base_units().magnitude
    )
    assert sec_method.electronic.n_spin_channels is None
