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
from electronicparsers.onetep import OnetepParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return OnetepParser()


def test_scf(parser):
    archive = EntryArchive()

    parser.parse('tests/data/onetep/fluor/12-difluoroethane.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '4.5.3.32'
    assert sec_run.time_run.date_end.magnitude == approx(1474976160.0)

    sec_system = sec_run.system
    assert sec_system[0].atoms.lattice_vectors[2][2].magnitude == approx(
        1.29648417e-09,
    )
    assert sec_system[0].atoms.positions[3][2].magnitude == approx(5.7072299e-10)
    assert sec_system[0].atoms.labels[7] == 'H'

    sec_scc = sec_run.calculation
    assert len(sec_scc) == 1
    assert sec_scc[0].energy.total.value.magnitude == approx(-2.72023829e-16)
    assert sec_scc[0].energy.kinetic_electronic.value.magnitude == approx(
        1.89937757e-16
    )
    assert sec_scc[0].energy.correction_hartree.value.magnitude == approx(
        3.87263469e-16
    )
    assert sec_scc[0].energy.x_onetep_pseudopotential_local.value.magnitude == approx(
        -9.80296609e-16
    )
    assert sec_scc[0].energy.xc.value.magnitude == approx(-6.21292141e-17)
    assert len(sec_scc[0].scf_iteration) == 4

    sec_method = sec_run.method[0]
    assert sec_method.electrons_representation[0].basis_set[0].cutoff.to(
        'Ha'
    ).magnitude == approx(30.38533)


def test_relax(parser):
    archive = EntryArchive()

    parser.parse('tests/data/onetep/test08/ethene_relax.out', archive, None)

    sec_method = archive.run[0].method
    assert sec_method[0].dft.xc_functional.exchange[0].name == 'LDA_X_PZ'
    assert sec_method[0].x_onetep_input_parameters['ngwf_threshold_orig'] == approx(
        1e-5
    )
    assert sec_method[0].electrons_representation[0].basis_set[0].cutoff.to(
        'Ha'
    ).magnitude == approx(20.05907)

    sec_system = archive.run[0].system
    assert len(sec_system) == 3
    assert sec_system[0].atoms.labels == ['C', 'H', 'H', 'C', 'H', 'H']
    assert sec_system[0].atoms.positions[3][1].magnitude == approx(1.06563278e-09)
    assert sec_system[1].atoms.positions[5][0].magnitude == approx(9.36407121e-10)
    assert sec_system[2].atoms.lattice_vectors[1][1].magnitude == approx(2.11670884e-09)

    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 3
    assert sec_scc[2].system_ref == sec_system[2]
    assert sec_scc[0].energy.total.value.magnitude == approx(-5.95750082e-17)
    assert sec_scc[0].energy.correction_hartree.value.magnitude == approx(
        1.08846112e-16
    )
    assert len(sec_scc[1].scf_iteration) == 9
    assert sec_scc[1].scf_iteration[7].energy.total.value.magnitude == approx(
        -5.96007361e-17
    )


def test_tddft(parser):
    archive = EntryArchive()

    parser.parse('tests/data/onetep/ethene/ethene_tddft.out', archive, None)

    sec_method = archive.run[0].method
    assert sec_method[0].electrons_representation[0].basis_set[0].cutoff.to(
        'Ha'
    ).magnitude == approx(14.88881)

    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 1
    assert sec_scc[0].energy.total.value.magnitude == approx(2.60907575e-18)
    assert len(sec_scc[0].scf_iteration) == 15
    assert sec_scc[0].scf_iteration[12].energy.total.value.magnitude == approx(
        2.60907651e-18
    )
    assert sec_scc[0].x_onetep_section_tddft[0].x_onetep_section_tddft_excitations[
        0
    ].x_onetep_tddft_excit_energy.magnitude == approx(1.25314575e-18)
    assert sec_scc[0].x_onetep_section_tddft[0].x_onetep_section_tddft_excitations[
        1
    ].x_onetep_tddft_excit_oscill_str == approx(0.35891e-02)
    assert sec_scc[0].x_onetep_section_tddft[0].x_onetep_section_tddft_excitations[
        1
    ].x_onetep_tddft_excit_lifetime.magnitude == approx(8.9651e-08)


def test_charges(parser):
    archive = EntryArchive()

    parser.parse('tests/data/onetep/test20/test20.out', archive, None)

    sec_method = archive.run[0].method
    assert sec_method[0].electrons_representation[0].basis_set[0].cutoff.to(
        'Ha'
    ).magnitude == approx(31.36667)

    sec_scc = archive.run[0].calculation
    assert len(sec_scc) == 1
    assert sec_scc[0].charges[0].value[3].magnitude == approx(-7.89873081e-20)
