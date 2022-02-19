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
    assert len(sec_dataset[0].x_abinit_section_input[0].x_abinit_var_symrel) == 432
    assert sec_dataset[0].x_abinit_section_input[0].x_abinit_var_znucl[0] == 14.

    sec_method = sec_run.method[0]
    assert sec_method.scf.n_max_iteration == 10.
    assert sec_method.scf.threshold_energy_change.magnitude == approx(4.35974472e-24)
    assert sec_method.basis_set[0].cell_dependent[0].planewave_cutoff.magnitude == approx(3.48779578e-17)
    assert sec_method.basis_set[0].kind == 'wavefunction'
    assert sec_method.dft.xc_functional.contributions[0].name == 'LDA_XC_TETER93'

    sec_system = sec_run.system[0]
    assert sec_system.atoms.labels == ['Si', 'Si']
    assert False not in sec_system.atoms.periodic
    assert sec_system.atoms.positions[1][1].magnitude == approx(1.346756e-10)
    assert sec_system.atoms.lattice_vectors[2][0].magnitude == approx(2.693512e-10)

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-3.86544728e-17)
    assert np.max(sec_scc.forces.total.value_raw.magnitude) == 0.
    assert sec_scc.stress.total.value[2][2].magnitude == approx(-5.60539974e+08)
    assert sec_scc.energy.fermi.magnitude == approx(8.4504932e-19)
    assert sec_scc.energy.kinetic_electronic.value.magnitude == approx(1.3343978e-17)
    assert len(sec_scc.scf_iteration) == 5
    sec_eig = sec_scc.eigenvalues[0]
    assert sec_scc.scf_iteration[1].energy.total.value.magnitude == approx(-3.86541222e-17)
    assert np.shape(sec_eig.energies[0][1]) == (5,)
    assert sec_eig.energies[0][1][2].magnitude == approx(8.4504932e-19)
    assert sec_eig.kpoints[0][0] == -0.25


def test_relax(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abinit/H2/H2.out', archive, None)

    assert len(archive.run[0].x_abinit_section_dataset) == 2
    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 5
    assert len(sec_sccs[2].scf_iteration) == 5
    assert sec_sccs[3].energy.total.value.magnitude == approx(-4.93984603e-18)
    assert sec_sccs[4].scf_iteration[1].energy.total.value.magnitude == approx(-2.13640055e-18)


def test_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/abinit/Fe/Fe.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 2
    assert np.shape(sec_sccs[0].eigenvalues[0].energies[0][5]) == (8,)
    assert np.shape(sec_sccs[1].eigenvalues[0].energies[1][5]) == (8,)
    assert np.shape(sec_sccs[0].dos_electronic[0].total[0].value) == (1601,)
    assert np.shape(sec_sccs[1].dos_electronic[0].total[1].value) == (1601,)
    assert sec_sccs[0].dos_electronic[0].energies[70].magnitude == approx(-3.18261365e-18)
    assert sec_sccs[0].dos_electronic[0].total[0].value[151].magnitude == approx(2.97494483e+14)
    assert sec_sccs[1].dos_electronic[0].total[1].value[180].magnitude == approx(1.27484528e+15)
    assert sec_sccs[0].dos_electronic[0].total[0].value_integrated[457] == approx(4.347007)
    assert sec_sccs[1].dos_electronic[0].total[0].value_integrated[1025] == approx(7.028265)
