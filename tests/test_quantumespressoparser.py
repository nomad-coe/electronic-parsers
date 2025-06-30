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

from electronicparsers.quantumespresso.parser import EFGParser, EPRGtensorParser, EPRHyperfineParser
from electronicparsers.utils.utils import (
    convert_system_to_model_system,
    convert_xcfunctional
)
from nomad.datamodel import EntryArchive
from nomad.units import ureg
from electronicparsers.quantumespresso import QuantumEspressoParser, NMRParser
from nomad_simulations.schema_packages.model_system import Cell
from devtools import debug

MODEL_SYSTEM_EXPECTED = {
    "positions": np.array([
        [ 1.15464835e-10, -1.99991799e-10,  1.80119567e-10],
        [ 1.15464835e-10,  1.99991799e-10,  3.60239158e-10],
        [-2.30929670e-10,  0.00000000e+00,  0.00000000e+00],
        [ 1.67339273e-10, -6.23246070e-11,  1.15852911e-10],
        [-2.96951681e-11,  1.76082964e-10,  2.95972478e-10],
        [-1.37644104e-10, -1.13758357e-10,  4.76092069e-10],
        [ 1.67339273e-10,  6.23246070e-11, -1.15852911e-10],
        [-2.96951681e-11, -1.76082964e-10,  2.44386248e-10],
        [-1.37644104e-10,  1.13758357e-10,  6.42666562e-11],
    ]) * ureg.meter,

    "cell_lactice_vectors": np.array([
        [ 2.45617602e-10, -4.25423933e-10,  0.00000000e+00],
        [ 2.45617602e-10,  4.25423933e-10,  0.00000000e+00],
        [ 0.00000000e+00,  0.00000000e+00,  5.40358725e-10]
    ]) * ureg.meter,

    "cell_periodic_boundary_conditions": [True, True, True],

    "particle_state_labels": ['Si', 'Si', 'Si', 'O', 'O', 'O', 'O', 'O', 'O'],
}

MS_EXPECTED_VALUES = {
    "text": np.array([
        [[ 4.325142e-04,  5.825000e-07,  6.176400e-06],
         [ 5.819000e-07,  4.318332e-04,  3.559900e-06],
         [-1.130830e-05, -6.529500e-06,  4.295852e-04]],

        [[ 4.325142e-04, -5.825000e-07, -6.176400e-06],
         [-5.819000e-07,  4.318332e-04,  3.559900e-06],
         [ 1.130830e-05, -6.529500e-06,  4.295852e-04]],

        [[ 4.314911e-04,  0.000000e+00,  0.000000e+00],
         [ 0.000000e+00,  4.328567e-04, -7.129500e-06],
         [ 0.000000e+00,  1.306330e-05,  4.295880e-04]],

        [[ 2.113641e-04,  2.251230e-05, -2.008190e-05],
         [ 2.158540e-05,  2.335098e-04, -2.789930e-05],
         [-2.096140e-05, -2.718030e-05,  2.249562e-04]],

        [[ 2.470986e-04, -9.521000e-07,  3.419190e-05],
         [-1.879900e-06,  1.977630e-04, -3.471100e-06],
         [ 3.398330e-05, -4.590500e-06,  2.249352e-04]],

        [[ 2.089116e-04, -2.017010e-05, -1.410880e-05],
         [-2.109170e-05,  2.359424e-04,  3.132410e-05],
         [-1.304160e-05,  3.171420e-05,  2.249453e-04]],

        [[ 2.113641e-04, -2.251230e-05,  2.008190e-05],
         [-2.158540e-05,  2.335098e-04, -2.789930e-05],
         [ 2.096140e-05, -2.718030e-05,  2.249562e-04]],

        [[ 2.470986e-04,  9.521000e-07, -3.419190e-05],
         [ 1.879900e-06,  1.977630e-04, -3.471100e-06],
         [-3.398330e-05, -4.590500e-06,  2.249352e-04]],

        [[2.089116e-04, 2.017010e-05, 1.410880e-05],
         [2.109170e-05, 2.359424e-04, 3.132410e-05],
         [1.304160e-05, 3.171420e-05, 2.249453e-04]],
    ]),

    "xml": np.array([
        [[ 4.41563539e-04,  7.39057663e-07,  6.31690773e-06],
         [ 6.26376541e-07,  4.40604944e-04,  3.56587984e-06],
         [-1.14783591e-05, -6.62512101e-06,  4.38388924e-04]],
        
        [[ 4.41563539e-04, -7.39057663e-07, -6.31690773e-06],
         [-6.26376541e-07,  4.40604944e-04,  3.56587984e-06],
         [ 1.14783591e-05, -6.62512101e-06,  4.38388924e-04]],

        [[ 4.40310991e-04,  5.80716167e-22, -9.24422859e-23],
         [-2.76820504e-20,  4.42180289e-04, -7.24753948e-06],
         [ 7.89501593e-23,  1.33063891e-05,  4.38546713e-04]],

        [[ 2.12248892e-04,  2.17201148e-05, -1.92951632e-05],
         [ 2.09382548e-05,  2.33142256e-04, -2.72806345e-05],
         [-2.04661901e-05, -2.67712434e-05,  2.25241935e-04]],

        [[ 2.46993992e-04, -8.60713658e-07,  3.31460618e-05],
         [-1.75607782e-06,  1.98580619e-04, -3.51434621e-06],
         [ 3.28081306e-05, -4.68602317e-06,  2.24946526e-04]],

        [[ 2.10056139e-04, -1.97009764e-05, -1.37998736e-05],
         [-2.04954639e-05,  2.35244330e-04,  3.00495401e-05],
         [-1.26765796e-05,  3.05365331e-05,  2.25168117e-04]],

        [[ 2.12248892e-04, -2.17201148e-05,  1.92951632e-05],
         [-2.09382548e-05,  2.33142256e-04, -2.72806345e-05],
         [ 2.04661901e-05, -2.67712434e-05,  2.25241935e-04]],

        [[ 2.46993992e-04,  8.60713658e-07, -3.31460618e-05],
         [ 1.75607782e-06,  1.98580619e-04, -3.51434621e-06],
         [-3.28081306e-05, -4.68602317e-06,  2.24946526e-04]],

        [[2.10056139e-04, 1.97009764e-05, 1.37998736e-05],
         [2.04954639e-05, 2.35244330e-04, 3.00495401e-05],
         [1.26765796e-05, 3.05365331e-05, 2.25168117e-04]],
    ])
}

SUS_EXPECTED_VALUES = {
        "text": {
            "value": np.array([
                [-6.372115e-11,  0.000000e+00,  0.000000e+00],
                [ 0.000000e+00, -6.375900e-11, -2.180000e-14],
                [ 0.000000e+00,  3.085000e-14, -6.403545e-11]
            ]) * ureg('meter**3 / mole'),

            "value_vgv_approx": np.array([
                [-6.26047e-11,  0.00000e+00,  0.00000e+00],
                [ 0.00000e+00, -6.26340e-11,  5.90000e-15],
                [ 0.00000e+00,  5.70000e-15, -6.29139e-11]
            ]) * ureg('meter**3 / mole'),

            "value_pgv_approx": np.array([
                [-6.48376e-11,  0.00000e+00,  0.00000e+00],
                [ 0.00000e+00, -6.48840e-11, -4.95000e-14],
                [ 0.00000e+00,  5.60000e-14, -6.51570e-11]
            ]) * ureg('meter**3 / mole')
        },

        "xml": {
            "value": np.array([
                [-6.66333614e+01,  0.00000000e+00,  0.00000000e+00],
                [ 0.00000000e+00, -6.66955489e+01, -7.12042136e-02],
                [ 0.00000000e+00, -3.54456212e-02, -6.65337517e+01]
            ]) * ureg('meter ** 3 / mole'),

            "value_vgv_approx": np.array([
                [-6.84937768e+01,  0.00000000e+00,  0.00000000e+00],
                [ 0.00000000e+00, -6.85853665e+01, -1.09507752e-01],
                [ 0.00000000e+00, -3.80460314e-02, -6.83273167e+01]
            ]) * ureg('meter ** 3 / mole'),

            "value_pgv_approx": np.array([
                [-6.47729461e+01,  0.00000000e+00,  0.00000000e+00],
                [ 0.00000000e+00, -6.48057312e+01, -3.29006750e-02],
                [ 0.00000000e+00, -3.28452110e-02, -6.47401867e+01]
            ]) * ureg('meter ** 3 / mole')
        }

    }

EFG_EXPECTED_VALUES = {
    "text": np.array([
        [[-0.027004, -0.061522,  0.013644],
         [-0.061522,  0.044065,  0.007889],
         [ 0.013644,  0.007889, -0.017062]],

        [[-0.027004,  0.061522, -0.013644],
         [ 0.061522,  0.044065,  0.007889],
         [-0.013644,  0.007889, -0.017062]],

        [[ 0.079563,  0.      ,  0.      ],
         [ 0.      , -0.062482, -0.015764],
         [ 0.      , -0.015764, -0.017081]],

        [[-0.193956,  0.386184, -0.440635],
         [ 0.386184,  0.181931, -0.48823 ],
         [-0.440635, -0.48823 ,  0.012026]],

        [[ 0.422345, -0.030355,  0.643132],
         [-0.030355, -0.434371, -0.137484],
         [ 0.643132, -0.137484,  0.012026]],

        [[-0.246543, -0.35583 , -0.202511],
         [-0.35583 ,  0.234523,  0.625715],
         [-0.202511,  0.625715,  0.012021]],

        [[-0.193956, -0.386184,  0.440635],
         [-0.386184,  0.181931, -0.48823 ],
         [ 0.440635, -0.48823 ,  0.012026]],

        [[ 0.422345,  0.030355, -0.643132],
         [ 0.030355, -0.434371, -0.137484],
         [-0.643132, -0.137484,  0.012026]],
         
        [[-0.246543,  0.35583 ,  0.202511],
         [ 0.35583 ,  0.234523,  0.625715],
         [ 0.202511,  0.625715,  0.012021]],
    ]) * ureg('attounified_atomic_mass_unit'),

    "xml": np.array([
        [[-0.0272077 , -0.06280041,  0.01391215],
         [-0.06280041,  0.04512257,  0.00797996],
         [ 0.01391215,  0.00797996, -0.01791486]],

        [[-0.0272077 ,  0.06280041, -0.01391215],
         [ 0.06280041,  0.04512257,  0.00797996],
         [-0.01391215,  0.00797996, -0.01791486]],

        [[ 0.08153004 , 0.         , 0.        ],
         [ 0.        , -0.06350954, -0.01608141],
         [ 0.        , -0.01608141, -0.01802049]],

        [[-0.18840037,  0.37935967, -0.431783  ],
         [ 0.37935967,  0.1782501 , -0.47938534],
         [-0.431783  , -0.47938534,  0.01015027]],

        [[ 0.41482547, -0.03115247,  0.6311346 ],
         [-0.03115247, -0.4249499 , -0.13439391],
         [ 0.6311346 , -0.13439391,  0.01012443]],

        [[-0.24217828, -0.3482194 , -0.19920104],
         [-0.3482194 ,  0.23206629,  0.61361959],
         [-0.19920104,  0.61361959,  0.01011199]],

        [[-0.18840037, -0.37935967,  0.431783  ],
         [-0.37935967,  0.1782501 , -0.47938534],
         [ 0.431783  , -0.47938534,  0.01015027]],

        [[ 0.41482547,  0.03115247, -0.6311346 ],
         [ 0.03115247, -0.4249499 , -0.13439391],
         [-0.6311346 , -0.13439391,  0.01012443]],

        [[-0.24217828,  0.3482194 ,  0.19920104],
         [ 0.3482194 ,  0.23206629,  0.61361959],
         [ 0.19920104,  0.61361959,  0.01011199]],
    ]) * ureg('attounified_atomic_mass_unit')
}

def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return QuantumEspressoParser()


@pytest.fixture(scope='module')
def quartz_scf_fixtures(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/quantumespresso/quartz/quartz-scf.out',
        archive,
        None
    )
    model_system = convert_system_to_model_system(
        system=archive.run[-1].system[-1]
    )
    xc_fun_list = convert_xcfunctional(
        archive.run[-1].method[-1].dft.xc_functional
    )
    return model_system, xc_fun_list

@pytest.fixture(scope='module')
def h2o_scf_fixtures(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/quantumespresso/H2O+/H2O+_scf.out',
        archive,
        None
    )
    model_system = convert_system_to_model_system(
        system=archive.run[-1].system[-1]
    )
    xc_fun_list = convert_xcfunctional(
        archive.run[-1].method[-1].dft.xc_functional
    )
    return model_system, xc_fun_list


@pytest.fixture(scope='module')
def quartz_expected_cell():
    expected_cell = Cell()
    expected_cell.lattice_vectors = MODEL_SYSTEM_EXPECTED['cell_lactice_vectors']
    expected_cell.periodic_boundary_conditions = MODEL_SYSTEM_EXPECTED['cell_periodic_boundary_conditions']
    return expected_cell


def RyB_to_N(value):
    return (value * ureg.rydberg / ureg.bohr).to_base_units().magnitude


def test_scf(parser):
    archive = EntryArchive()
    parser.parse(
        'tests/data/quantumespresso/HO_scf/benchmark2.out', 
        archive, 
        None
    )

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


def test_mainfile_keys(parser):
    filepath1 = 'tests/data/quantumespresso/quartz/quartz-scf.out'
    mainfile_keys1 = parser.get_mainfile_keys(filename=filepath1)
    assert mainfile_keys1[0] == 'NMR'
    assert mainfile_keys1[1] == 'EFG'
    assert mainfile_keys1[2] == 'GIPAW_Workflow'

    filepath2 = 'tests/data/quantumespresso/HO_scf/benchmark2.out'
    mainfile_keys2 = parser.get_mainfile_keys(filename=filepath2)
    assert mainfile_keys2

    filepath3 = 'tests/data/quantumespresso/H2O+/H2O+_scf.out'
    mainfile_keys3 = parser.get_mainfile_keys(filename=filepath3)
    assert mainfile_keys3[0] == 'Hyperfine'
    assert mainfile_keys3[1] == 'GIPAW_Workflow'    
    


def test_system_to_model_system_conversion(quartz_scf_fixtures, quartz_expected_cell):
    model_system, _ = quartz_scf_fixtures

    assert model_system.n_particles == 9

    assert np.allclose(
        model_system.positions.to('meter').magnitude,
        MODEL_SYSTEM_EXPECTED["positions"].to('meter').magnitude,
        rtol=1e-8
    )

    assert np.allclose(
        model_system.cell[0].lattice_vectors.to('meter').magnitude,
        quartz_expected_cell.lattice_vectors.to('meter').magnitude,
        rtol=1e-8
    )
    assert model_system.cell[0].periodic_boundary_conditions == quartz_expected_cell.periodic_boundary_conditions

    for index, symbol in enumerate(MODEL_SYSTEM_EXPECTED["particle_state_labels"]):
        assert model_system.particle_states[index].chemical_symbol == symbol


def test_xc_functional_conversion(quartz_scf_fixtures):
    _, xc_functionals = quartz_scf_fixtures

    assert len(xc_functionals) == 2
    assert xc_functionals[0].name == 'exchange'
    assert xc_functionals[0].libxc_name == 'GGA_X_PBE'
    assert xc_functionals[1].libxc_name == 'GGA_C_PBE'
    assert xc_functionals[1].name == 'correlation'


def test_nmr_text(quartz_scf_fixtures):
    archive = EntryArchive()
    model_system, _ = quartz_scf_fixtures
    parser = NMRParser(system=model_system, xc_func_list=None)
    parser.parse(
        filepath='tests/data/quantumespresso/quartz/quartz-nmr.out',
        archive=archive,
        logger=None)
    
    simulation = archive.data

    # Program
    assert simulation.program.name == 'GIPAW'
    assert simulation.program.version == '7.4.1'

    # ModelSystem
    assert len(simulation.model_system) == 1
    assert simulation.model_system[0].is_representative
    
    # ModelMethod
    assert len(simulation.model_method) == 1
    assert simulation.model_method[0].name == 'NMR'

    # Outputs
    assert len(simulation.outputs) == 1
    output = simulation.outputs[0]

    assert output.model_system_ref == simulation.model_system[0]
    assert output.model_method_ref == simulation.model_method[0]

    #   MagneticShielding
    ms = output.magnetic_shieldings
    assert len(ms) == 9
    for i in range(9):
        assert ms[i].name == "MagneticShielding"
        if i in [0, 1, 2]:
            assert ms[i].entity_ref.chemical_symbol == "Si"
        else:
            assert ms[i].entity_ref.chemical_symbol == "O"
        assert np.allclose(ms[i].value, MS_EXPECTED_VALUES["text"][i], rtol=1e-10)

    #   MagneticSusceptibility
    sus = output.magnetic_susceptibilities[0]
    assert sus.name == "MagneticSusceptibility"
    assert np.allclose(sus.value, SUS_EXPECTED_VALUES["text"]["value"], rtol=1e-10)
    assert np.allclose(sus.value_vgv_approx, SUS_EXPECTED_VALUES["text"]["value_vgv_approx"], rtol=1e-10)
    assert np.allclose(sus.value_pgv_approx, SUS_EXPECTED_VALUES["text"]["value_pgv_approx"], rtol=1e-10)


def test_nmr_xml(quartz_scf_fixtures):
    archive = EntryArchive()
    model_system, xc_fun_list = quartz_scf_fixtures
    parser = NMRParser(system=model_system, xc_func_list=xc_fun_list)
    parser.parse(
        filepath='tests/data/quantumespresso/quartz/quartz-nmr-gipaw.xml',
        archive=archive,
        logger=None)
    
    simulation = archive.data

    # Program
    assert simulation.program.name == 'GIPAW'
    assert simulation.program.version == ''

    # ModelSystem
    assert len(simulation.model_system) == 1
    model_system = simulation.model_system[0]

    # ModelMethod
    assert len(simulation.model_method) == 1
    assert simulation.model_method[0].name == 'NMR'

    # Outputs
    assert len(simulation.outputs) == 1
    output = simulation.outputs[0]

    assert output.model_system_ref == simulation.model_system[0]
    assert output.model_method_ref == simulation.model_method[0]

    #   MagneticShielding
    ms = output.magnetic_shieldings
    assert len(ms) == 9
    for i in range(9):
        debug(i)
        assert ms[i].name == "MagneticShielding"
        if i in [0, 1, 2]:
            assert ms[i].entity_ref.chemical_symbol == "Si"
        else:
            assert ms[i].entity_ref.chemical_symbol == "O"
        assert np.allclose(ms[i].value, MS_EXPECTED_VALUES["xml"][i], rtol=1e-10)

    #   MagneticSusceptibility
    sus = output.magnetic_susceptibilities[0]
    assert sus.name == "MagneticSusceptibility"
    assert np.allclose(sus.value.magnitude, SUS_EXPECTED_VALUES["xml"]["value"].magnitude, rtol=1e-8)
    assert np.allclose(sus.value_vgv_approx.magnitude, SUS_EXPECTED_VALUES["xml"]["value_vgv_approx"].magnitude, rtol=1e-8)
    assert np.allclose(sus.value_pgv_approx.magnitude, SUS_EXPECTED_VALUES["xml"]["value_pgv_approx"].magnitude, rtol=1e-8)


def test_efg_xml(quartz_scf_fixtures):
    archive = EntryArchive()
    model_system, xc_fun_list = quartz_scf_fixtures
    parser = EFGParser(system=model_system, xc_func_list=xc_fun_list)
    parser.parse(
        filepath='tests/data/quantumespresso/quartz/quartz-efg-gipaw.xml',
        archive=archive,
        logger=None)
    
    simulation = archive.data
    
    # Program
    assert simulation.program.name == 'GIPAW'
    assert simulation.program.version == ''

    # ModelSystem
    assert len(simulation.model_system) == 1
    assert simulation.model_system[0].is_representative
    
    # ModelMethod
    assert len(simulation.model_method) == 1
    assert simulation.model_method[0].name == 'EFG'

    # Outputs
    assert len(simulation.outputs) == 1
    output = simulation.outputs[0]

    assert output.model_system_ref == simulation.model_system[0]
    assert output.model_method_ref == simulation.model_method[0]

    #   ElectricFieldGradient
    efg = output.electric_field_gradients
    assert len(efg) == 9
    for i in range(9):
        assert efg[i].name == "ElectricFieldGradient"
        assert efg[i].type == "total"
        if i in [0, 1, 2]:
            assert efg[i].entity_ref.chemical_symbol == "Si"
        else:
            assert efg[i].entity_ref.chemical_symbol == "O"
        assert np.allclose(efg[i].value, EFG_EXPECTED_VALUES["xml"][i], rtol=1e-10)


def test_efg_text(quartz_scf_fixtures):
    archive = EntryArchive()
    model_system, _ = quartz_scf_fixtures
    parser = EFGParser(system=model_system, xc_func_list=None)
    parser.parse(
        filepath='tests/data/quantumespresso/quartz/quartz-efg.out',
        archive=archive,
        logger=None)
    
    simulation = archive.data
    
    # Program
    assert simulation.program.name == 'GIPAW'
    assert simulation.program.version == '7.4.1'

    # ModelSystem
    assert len(simulation.model_system) == 1
    assert simulation.model_system[0].is_representative
    
    # ModelMethod
    assert len(simulation.model_method) == 1
    assert simulation.model_method[0].name == 'EFG'

    # Outputs
    assert len(simulation.outputs) == 1
    output = simulation.outputs[0]

    assert output.model_system_ref == simulation.model_system[0]
    assert output.model_method_ref == simulation.model_method[0]

    #   ElectricFieldGradient
    efg = output.electric_field_gradients
    assert len(efg) == 9
    for i in range(9):
        assert efg[i].name == "ElectricFieldGradient"
        assert efg[i].type == "total"
        if i in [0, 1, 2]:
            assert efg[i].entity_ref.chemical_symbol == "Si"
        else:
            assert efg[i].entity_ref.chemical_symbol == "O"
        assert np.allclose(efg[i].value, EFG_EXPECTED_VALUES["text"][i], rtol=1e-10)
        


def test_epr_hyperfine_text(h2o_scf_fixtures):
    archive = EntryArchive()
    model_system, _ = h2o_scf_fixtures
    parser = EPRHyperfineParser(system=model_system, xc_func_list=None)
    parser.parse(
        filepath='tests/data/quantumespresso/H2O+/H2O+_hyperfine.out',
        archive=archive,
        logger=None)
    
    simulation = archive.data

    debug(simulation.outputs[0].hyperfine_dipolar)
    debug(simulation.outputs[0].hyperfine_fermi_contact)

    
    # # Program
    # assert simulation.program.name == 'GIPAW'
    # assert simulation.program.version == '7.4.1'





def test_epr_gtensor_text(h2o_scf_fixtures):
    archive = EntryArchive()
    model_system, _ = h2o_scf_fixtures
    parser = EPRGtensorParser(system=model_system, xc_func_list=None)
    parser.parse(
        filepath='tests/data/quantumespresso/H2O+/H2O+_g-tensor.out',
        archive=archive,
        logger=None)
    
    simulation = archive.data

    # debug(simulation.outputs[0].delta_g[0].value)
    # debug(simulation.outputs[0].delta_g_paratec[0].value)

    debug(simulation.outputs)
    debug(simulation.outputs[0])


    
    # # Program
    # assert simulation.program.name == 'GIPAW'
    # assert simulation.program.version == '7.4.1'