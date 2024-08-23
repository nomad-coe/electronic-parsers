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
from electronicparsers.tbstudio import TBStudioParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return TBStudioParser()


def test_parser(parser):
    archive = EntryArchive()
    parser.parse('tests/data/tbstudio/graphenePz.tbm', archive, None)

    sec_run = archive.run[-1]
    sec_program = sec_run.program
    assert sec_program.name == 'TBStudio'
    assert sec_program.version == '2.0'

    assert len(sec_run.system) == 1
    sec_system = sec_run.system[-1]
    assert sec_system.atoms.labels == ['C', 'C']

    a = [1.23435, 2.14452, 0.0]
    b = [1.23435, -2.14452, 0.0]
    c = [0.0, 0.0, 20.0]
    positions = [[0.00414, -0.004863, 10.0], [1.238611, -0.72006, 10.0]]
    # TODO not sure why this is problematic
    # assert sec_system.atoms.lattice_vectors.to('angstrom').magnitude == approx(
    #     np.array([a, b, c])
    # )
    # assert sec_system.atoms.positions.to('angstrom').magnitude == approx(
    #     np.array(positions)
    # )
    assert sec_system.atoms.periodic == [True, True, False]

    assert len(sec_run.method) == 1
    sec_method = sec_run.method[-1]

    assert sec_method.tb.slater_koster is not None
    sk = sec_method.tb.slater_koster
    assert len(sk.orbitals) == 2
    assert len(sk.bonds) == 3

    assert sk.orbitals[0].orbital_name == 'p_z'
    assert sk.orbitals[1].orbital_name == 'p_z'
    assert sk.orbitals[0].shell == 0
    assert sk.orbitals[1].shell == 0
    assert sk.orbitals[0].onsite_energy == -0.15789243
    assert sk.orbitals[1].onsite_energy == -0.15789243
    assert sk.orbitals[0].atom_index == 0
    assert sk.orbitals[1].atom_index == 1

    for i in [0, 1, 2]:
        assert sk.bonds[i].bond_label == 'Bond 1'
        assert sk.bonds[i].center1.shell == 1
        assert sk.bonds[i].pps == 0.0
        assert sk.bonds[i].ppp == -2.34157934
        assert (sk.bonds[i].center1.cell_index == [0, 0, 0]).all()

    assert sk.bonds[0].center1.atom_index == 1
    assert sk.bonds[1].center1.atom_index == 2
    assert sk.bonds[2].center1.atom_index == 2
    assert sk.bonds[0].center2.atom_index == 2
    assert sk.bonds[1].center2.atom_index == 1
    assert sk.bonds[2].center2.atom_index == 1
    assert (sk.bonds[0].center2.cell_index == [0, 0, 0]).all()
    assert (sk.bonds[1].center2.cell_index == [0, 1, 0]).all()
    assert (sk.bonds[2].center2.cell_index == [1, 1, 0]).all()

    # Band tests
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[-1]
    assert len(sec_scc.band_structure_electronic[0].segment) == 3
    assert len(sec_scc.band_structure_electronic[0].segment[0].kpoints) == 100
    assert len(sec_scc.band_structure_electronic[0].segment[0].kpoints) == len(
        sec_scc.band_structure_electronic[0].segment[0].energies[0]
    )
    assert sec_scc.energy.fermi == sec_scc.band_structure_electronic[0].energy_fermi
    assert sec_scc.band_structure_electronic[0].energy_fermi.to(
        'eV'
    ).magnitude == approx(-4.25178)
