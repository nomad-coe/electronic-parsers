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
from electronicparsers.abinit import AbinitParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return AbinitParser()


def test_scf(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abinit/Si/Si.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '7.8.2'
    assert sec_run.x_abinit_total_cpu_time == 1.4
    assert sec_run.clean_end
    assert sec_run.time_run.date_start.magnitude == 1467132480.0
    sec_dataset = sec_run.x_abinit_section_dataset
    assert len(sec_dataset) == 1
    assert np.size(sec_dataset[0].x_abinit_section_input.x_abinit_var_symrel) == 432
    assert sec_dataset[0].x_abinit_section_input.x_abinit_var_znucl[0] == 14.0

    sec_method = sec_run.method[0]
    assert sec_method.scf.n_max_iteration == 10.0
    assert sec_method.scf.threshold_energy_change.magnitude == approx(4.35974472e-24)
    assert sec_method.electrons_representation[0].basis_set[0].cutoff.to(
        'hartree'
    ).magnitude == approx(8)
    assert sec_method.dft.xc_functional.contributions[0].name == 'LDA_XC_TETER93'

    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels == ['Si', 'Si']
    assert False not in sec_system.atoms.periodic
    assert sec_system.atoms.positions[1][1].magnitude == approx(1.346756e-10)
    assert sec_system.atoms.lattice_vectors[2][0].magnitude == approx(2.693512e-10)

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-3.86544728e-17)
    assert np.max(sec_scc.forces.total.value_raw.magnitude) == 0.0
    assert sec_scc.stress.total.value[2][2].magnitude == approx(-5.60539974e08)
    assert sec_scc.energy.fermi.magnitude == approx(8.4504932e-19)
    assert sec_scc.energy.kinetic_electronic.value.magnitude == approx(1.3343978e-17)
    assert len(sec_scc.scf_iteration) == 5
    assert sec_scc.scf_iteration[1].energy.total.value.magnitude == approx(
        -3.86541222e-17
    )


def test_relax(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abinit/H2/H2.out', archive, None)

    assert archive.workflow2.m_def.name == 'GeometryOptimization'
    assert archive.workflow2.method.method == 'bfgs'
    sec_run = archive.run[0]
    assert len(sec_run.x_abinit_section_dataset) == 2
    assert len(sec_run.system) == 3
    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 4
    for i in range(1, 4):  # sec_scc[0] do not store any scf section
        assert sec_scc[i].m_xpath('scf_iteration')
    assert len(sec_scc[2].scf_iteration) == 5
    assert sec_scc[2].energy.total.value.magnitude == approx(-4.93984603e-18)
    assert sec_scc[2].scf_iteration[4].energy.total.value.magnitude == approx(
        -4.9398460277747174e-18
    )


def test_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abinit/Fe/Fe.out', archive, None)

    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 2
    assert sec_scc[-1].m_xpath('dos_electronic')  # dos always stored after dataset 1
    assert len(sec_scc[-1].dos_electronic) == 2
    sec_dos_up = sec_scc[-1].dos_electronic[0]
    sec_dos_down = sec_scc[-1].dos_electronic[1]
    assert sec_dos_up.spin_channel == 0 and sec_dos_down.spin_channel == 1
    assert sec_dos_up.n_energies == 1601
    assert sec_dos_up.energies[0].magnitude == approx(-3.487795777765736e-18)
    assert sec_dos_up.energies[543].magnitude == approx(-1.1204543936072428e-18)
    assert sec_dos_up.energies[-1].magnitude == approx(
        -sec_dos_up.energies[0].magnitude
    )
    assert len(sec_dos_up.total) == 1
    sec_dos_up_total = sec_dos_up.total[0]
    assert sec_dos_up_total.value[151].magnitude == approx(3.01852536e14)
    assert sec_dos_up_total.value[180].magnitude == approx(5.46018208e15)
    assert sec_dos_up_total.value_integrated[151] == approx(1.3e-5)
    assert sec_dos_up_total.value_integrated[180] == approx(2.39e-4)


def test_gw(parser):
    archive = EntryArchive()
    parser._calculation_type = 'gw'
    parser.parse('tests/data/abinit/ZrO2_GW/A1.abo', archive, None)
    sec_run = archive.run[-1]

    # Method
    sec_method = sec_run.method
    assert len(sec_method) == 1
    assert sec_method[-1].m_xpath('gw') and sec_method[-1].m_xpath('k_mesh')
    assert sec_method[-1].k_mesh.n_points == 3
    sec_gw = sec_method[-1].gw
    assert sec_gw.type == 'G0W0'
    assert sec_gw.analytical_continuation == 'contour_deformation'
    assert sec_gw.interval_qp_corrections[0] == 12
    assert sec_gw.interval_qp_corrections[-1] == 13
    assert sec_gw.n_states == 512
    assert sec_gw.n_empty_states == 500
    assert sec_gw.screening.n_empty_states == sec_gw.n_empty_states
    assert sec_gw.q_mesh.n_points == sec_method[-1].k_mesh.n_points
    assert len(sec_method[-1].frequency_mesh) == 1
    assert sec_method[-1].frequency_mesh[0].n_points == 2
    assert sec_method[-1].frequency_mesh[0].points[-1].to('eV').magnitude == approx(
        31.855950000000004j
    )

    # Calculation
    sec_scc = sec_run.calculation
    assert len(sec_scc) == 1
    assert sec_scc[-1].m_xpath('x_abinit_screening')
    assert sec_scc[-1].m_xpath('x_abinit_gw')
    sec_eigen = sec_scc[-1].eigenvalues
    assert len(sec_eigen) == 3
    assert sec_eigen[0].value_qp.to('eV').magnitude[0][0][2] == approx(7.024)
    assert sec_eigen[0].value_qp.to('eV').magnitude[0][0][3] == approx(12.483)
