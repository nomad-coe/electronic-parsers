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
from electronicparsers.wannier90 import Wannier90Parser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return Wannier90Parser()


def test_lco(parser):
    archive = EntryArchive()
    parser.parse('tests/data/wannier90/lco_mlwf/lco.wout', archive, None)

    sec_run = archive.run[-1]
    sec_program = sec_run.program
    assert sec_program.name == 'Wannier90'
    assert sec_program.version == '3.1.0'

    assert len(sec_run.system) == 1
    sec_system = sec_run.system[-1]
    assert sec_system.atoms.labels[-1] == 'O'
    assert (sec_system.atoms.positions[2].magnitude == np.array([0.0, 0.0, 0.0])).all()
    assert sec_system.atoms.lattice_vectors[0][0].magnitude == approx(-1.909145e-10)
    assert sec_system.atoms.periodic == [True, True, True]
    assert sec_system.m_xpath('atoms_group')
    assert len(sec_system.atoms_group) == 1
    assert sec_system.atoms_group[-1].label == 'projection'
    assert sec_system.atoms_group[-1].type == 'active_orbitals'
    assert sec_system.atoms_group[-1].index == 0
    assert sec_system.atoms_group[-1].atom_indices[0] == 2

    assert len(sec_run.method) == 1
    sec_method = sec_run.method[-1]
    assert sec_method.k_mesh.n_points == 343
    assert (
        sec_method.k_mesh.points[303] == np.array([0.85714, 0.14286, 0.28571])
    ).all()
    assert (sec_method.k_mesh.grid == np.array([7, 7, 7])).all()
    sec_wannier = sec_method.tb.wannier
    assert sec_wannier.n_projected_orbitals == 1
    assert sec_wannier.n_bands == 5
    assert sec_wannier.is_maximally_localized is True
    assert sec_method.atom_parameters[-1].n_orbitals == 1
    assert sec_method.atom_parameters[-1].orbitals[0] == 'dx2-y2'

    # Band tests
    assert len(sec_run.calculation) == 1
    sec_scc = sec_run.calculation[-1]
    assert len(sec_scc.band_structure_electronic[0].segment) == 4
    assert sec_scc.band_structure_electronic[0].segment[0].n_kpoints == 100
    assert sec_scc.band_structure_electronic[0].segment[0].n_kpoints == len(
        sec_scc.band_structure_electronic[0].segment[0].energies[0]
    )
    assert sec_scc.energy.fermi == sec_scc.band_structure_electronic[0].energy_fermi
    assert sec_scc.band_structure_electronic[0].energy_fermi.to(
        'eV'
    ).magnitude == approx(12.895622)
    # DOS tests
    sec_dos = sec_scc.dos_electronic
    assert len(sec_dos) == 1
    assert sec_dos[0].n_energies == 692
    assert sec_dos[0].n_energies == len(sec_dos[0].energies)
    assert len(sec_dos[0].total[0].value) == sec_dos[0].n_energies
    # x_wannier90 tests
    sec_hoppings = sec_scc.hopping_matrix[0]
    assert sec_hoppings.n_wigner_seitz_points == 397
    assert sec_hoppings.n_wigner_seitz_points == len(sec_hoppings.degeneracy_factors)
    assert sec_hoppings.n_orbitals == sec_wannier.n_projected_orbitals
    assert sec_hoppings.value.shape[0] == sec_hoppings.n_wigner_seitz_points
    assert sec_hoppings.value.shape[1] == sec_hoppings.n_orbitals
    assert sec_hoppings.value.shape[2] == 7
