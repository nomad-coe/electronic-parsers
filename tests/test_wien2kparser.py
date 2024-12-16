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
from electronicparsers.wien2k import Wien2kParser
from runschema.method import (
    AtomParameters,
    CoreHole,
)


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return Wien2kParser()


def test_single_point(parser, caplog):
    archive = EntryArchive()
    parser.parse('tests/data/wien2k/basic/ok.scf', archive, None)

    assert len(caplog.records) == 0

    sec_run = archive.run[0]
    assert sec_run.program.version == '12.1 22/7/2012'
    assert sec_run.time_run.date_start.magnitude == 1397313280.0

    sec_method = archive.run[0].method[0]
    assert sec_method.dft.xc_functional.correlation[0].name == 'GGA_C_PBE_SOL'
    assert sec_method.x_wien2k_ifft[1] == 120
    assert sec_method.electrons_representation[0].basis_set[0].cutoff_fractional == 7.0
    assert sec_method.electronic.smearing.kind == 'tetrahedra'
    assert sec_method.x_wien2k_in2_espermin == 0.50

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-8.09654094e-15)
    assert np.shape(sec_scc.forces.total.value) == (49, 3)
    assert sec_scc.forces.total.value[19][1].magnitude == approx(-2.76650574e-10)
    assert sec_scc.energy.fermi.magnitude == approx(-4.46784636e-19)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 40
    assert sec_scfs[21].energy.total.value.magnitude == approx(-8.09654095e-15)
    assert sec_scfs[6].x_wien2k_noe == 196.000
    assert sec_scfs[17].x_wien2k_tot_diff_charge[9] == approx(0.0001539)

    sec_system = archive.run[0].system[0]
    assert np.shape(sec_system.atoms.positions) == (49, 3)
    assert sec_system.atoms.positions[18][1].magnitude == approx(9.94126646e-10)
    assert sec_system.atoms.lattice_vectors[1][1].magnitude == approx(1.06500038e-09)
    assert sec_system.atoms.labels == ['C'] * 49


def test_eigenvalues(parser, caplog):
    archive = EntryArchive()
    parser.parse('tests/data/wien2k/eigenvalues/64k_8Rk_mBJkol.scf', archive, None)

    assert len(caplog.records) == 2
    assert 'Different number of eigenvalues' in caplog.records[1].msg

    sec_eigenvalues = archive.run[0].calculation[0].eigenvalues[0]
    assert np.shape(sec_eigenvalues.energies[0][7]) == (314,)
    assert np.shape(sec_eigenvalues.kpoints) == (8, 3)
    assert sec_eigenvalues.energies[0][2][31].magnitude == approx(-2.98121062e-18)
    assert sec_eigenvalues.kpoints[7][0] == 0.375
    assert sec_eigenvalues.kpoints_multiplicities[6] == 8

    sec_dos = archive.run[0].calculation[0].dos_electronic[0]
    assert np.shape(sec_dos.total[0].value) == (1251,)
    assert len(sec_dos.energies) == 1251
    assert sec_dos.total[0].value[1178].magnitude == approx(5.93635529e19)
    assert sec_dos.energies[285].magnitude == approx(-9.37345115e-19)


def test_dos(parser, caplog):
    archive = EntryArchive()
    parser.parse('tests/data/wien2k/dos/CrO2-sp.scf', archive, None)

    assert len(caplog.records) == 2
    assert 'Different number of eigenvalues' in caplog.records[1].msg

    sec_scc = archive.run[0].calculation[0]

    sec_eigenvalues = sec_scc.eigenvalues[0]
    assert np.shape(sec_eigenvalues.energies) == (2, 70, 43)
    assert sec_eigenvalues.energies[0][2][42].magnitude == approx(3.88893e-18)
    assert sec_eigenvalues.energies[0][52][11].magnitude == approx(-1.81337e-18)
    assert sec_eigenvalues.energies[0][69][42].magnitude == approx(3.88971e-18)
    assert sec_eigenvalues.energies[1][68][41].magnitude == approx(3.695777e-18)

    assert len(sec_scc.dos_electronic) == 2
    sec_dos_up = sec_scc.dos_electronic[0]
    sec_dos_down = sec_scc.dos_electronic[1]
    assert sec_dos_up.spin_channel == 0 and sec_dos_down.spin_channel == 1
    assert sec_dos_up.energies[26].magnitude == approx(-9.76582818e-19)
    assert np.shape(sec_dos_down.total[0].value) == (1000,)
    assert sec_dos_down.total[0].value[334].magnitude == approx(1.32586595e19)

    assert len(sec_dos_up.species_projected) == 2 and len(
        sec_dos_up.species_projected
    ) == len(sec_dos_down.species_projected)
    assert sec_dos_up.species_projected[0].atom_label == 'Cr'
    assert sec_dos_up.species_projected[1].atom_label == 'O'
    assert np.shape(sec_dos_up.species_projected[0].value) == (1000,)
    assert sec_dos_up.species_projected[1].value[926].magnitude == approx(
        2.7395685667470246e17
    )


def test_core_hole(parser, caplog):
    archive = EntryArchive()
    parser.parse('tests/data/wien2k/TiN-corehole/TiN-corehole.scf', archive, None)

    sec_method = archive.run[0].method[0]
    atom_par = sec_method.atom_parameters[0]
    assert atom_par.atom_index == 2
    assert atom_par.core_hole.n_electrons_excited == 1.0
    assert atom_par.core_hole.l_quantum_number == 1
    assert atom_par.core_hole.j_quantum_number == 1.5
    assert atom_par.core_hole.n_quantum_number == 2
    assert atom_par.core_hole.occupation == 3
    assert atom_par.core_hole.dscf_state == 'final'
