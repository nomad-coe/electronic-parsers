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
from nomad.units import ureg


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return Wannier90Parser()


def test_lco(parser):
    archive = EntryArchive()
    parser.parse('tests/data/wannier90/lco_mlwf/lco.wout', archive, None)

    sec_program = archive.run[0].program
    assert sec_program.name == 'Wannier90'
    assert sec_program.version == '3.1.0'

    sec_system = archive.run[0].system
    assert len(sec_system) == 1
    assert sec_system[0].atoms.labels[-1] == 'O'
    assert (sec_system[0].atoms.positions[2].magnitude == np.array([0., 0., 0.])).all()
    assert sec_system[0].atoms.lattice_vectors[0][0].magnitude == approx(-1.909145e-10)
    assert sec_system[0].atoms.periodic == [True, True, True]

    sec_projection = archive.run[0].method[0].projection
    assert sec_projection.n_projected_orbitals == 1
    assert sec_projection.n_bands == 5
    assert sec_projection.is_maximally_localise is True
    assert sec_projection.k_mesh.n_points == 343

    # Band tests
    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 1
    assert len(sec_scc[0].band_structure_electronic[0].segment) == 4
    assert sec_scc[0].band_structure_electronic[0].segment[0].n_kpoints == 100
    assert sec_scc[0].band_structure_electronic[0].segment[0].n_kpoints == \
        len(sec_scc[0].band_structure_electronic[0].segment[0].energies[0])
    assert sec_scc[0].energy.fermi == sec_scc[0].band_structure_electronic[0].energy_fermi
    assert sec_scc[0].band_structure_electronic[0].energy_fermi.to('eV').magnitude == approx(11.375)
    # DOS tests
    sec_dos = sec_scc[0].dos_electronic
    assert len(sec_dos) == 1
    assert sec_dos[0].n_energies == 692
    assert sec_dos[0].n_energies == len(sec_dos[0].energies)
    assert sec_dos[0].energy_shift == sec_dos[0].energy_fermi
    assert len(sec_dos[0].total[0].value) == sec_dos[0].n_energies
    # x_wannier90 tests
    sec_hoppings = sec_scc[0].x_wannier90_hoppings
    assert sec_hoppings.nrpts == 397
    assert sec_hoppings.nrpts == len(sec_hoppings.degeneracy_factors)
    assert sec_hoppings.hopping_matrix.shape[0] == sec_hoppings.nrpts
    assert sec_hoppings.hopping_matrix.shape[1] == 7
