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
from electronicparsers.alf import ALFParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return ALFParser()


def test_qmc(parser):
    archive = EntryArchive()
    parser.parse('tests/data/alf/1/data.h5', archive, None)

    # program tests
    sec_program = archive.run[0].program
    assert sec_program.name == 'ALF'
    assert sec_program.x_alf_commit_hash == '8cdcc2d7'
    assert sec_program.x_alf_commit_branch == '196-write-parameters-to-hdf5-file'
    # system tests
    sec_system = archive.run[0].system
    assert len(sec_system) == 1
    assert sec_system[0].name == 'Square'
    assert sec_system[0].type == '2D'
    assert sec_system[0].is_representative
    assert len(sec_system[0].atoms.labels) == 16
    assert len(sec_system[0].atoms.labels) == len(sec_system[0].atoms.positions)
    assert (sec_system[0].atoms.lattice_vectors.to('angstrom').magnitude[0] == np.array([1., 0., 0.])).all()
    # method tests
    sec_method = archive.run[0].method
    assert len(sec_method) == 1
    assert sec_method[0].qmc.model_name == 'Square Hubbard'
    assert sec_method[0].qmc.U == 4.0
    assert sec_method[0].qmc.chemical_potential == 0.0
    assert sec_method[0].qmc.n_bins == 213
    # calculation tests
    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 2
    assert sec_scc[0].system_ref == sec_scc[1].system_ref
    assert sec_scc[0].method_ref == sec_scc[1].method_ref
    assert sec_scc[0].hopping_matrix[0].n_orbitals == 2
    assert sec_scc[1].calculations_ref[0] == sec_scc[0]
    assert sec_scc[1].x_alf_ener_scal.x_alf_obser.shape == (213, 1, 2)
    assert sec_scc[1].x_alf_green_eq.x_alf_obser[0][0][0][0][0][0] == approx(0.99999999999)
    assert sec_scc[1].x_alf_green_eq.x_alf_obser[0][0][0][0][0][1] == approx(2.07957262521e-12)
