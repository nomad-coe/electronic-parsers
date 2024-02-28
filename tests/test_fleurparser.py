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
from electronicparsers.fleur import FleurParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return FleurParser()


def test_scf(parser):
    archive = EntryArchive()

    parser.parse('tests/data/fleur/Si/out', archive, None)

    sec_run = archive.run
    assert sec_run[0].program.version == 'fleur.26b'
    assert sec_run[0].x_fleur_header[0].x_fleur_precision == 'DOUBLE'
    assert not sec_run[0].x_fleur_header[0].x_fleur_with_soc
    assert sec_run[0].x_fleur_header[0].x_fleur_additional_flags == 'CPP_MPI'

    sec_method = sec_run[0].method
    assert sec_method[0].x_fleur_input_parameters['chng'] == approx(-0.100e-11)
    assert sec_method[0].x_fleur_input_parameters['ctail'] == 'T'
    assert sec_method[0].x_fleur_input_parameters['lflip'] == ['F', 1, 1]
    assert sec_method[0].x_fleur_parameters['vM'] == 0
    assert sec_method[0].x_fleur_eigenvalues_parameters['number of energy windows'] == 1
    assert sec_method[0].dft.xc_functional.exchange[0].name == 'GGA_X_PBE'
    assert (
        sec_method[0].dft.xc_functional.x_fleur_xc_correction
        == 'non-relativi correction'
    )
    assert sec_method[0].electronic.smearing.kind == 'fermi'
    assert sec_method[0].electronic.smearing.width == approx(0.001)
    assert sec_method[0].x_fleur_tot_nucl_charge == approx(28.0)

    sec_system = sec_run[0].system
    assert sec_system[0].atoms.lattice_vectors[1][2].magnitude == approx(2.73444651e-10)
    assert sec_system[0].atoms.labels == ['Si', 'Si']
    assert sec_system[0].atoms.positions[1][2].magnitude == approx(-6.97284111e-11)
    assert sec_system[0].x_fleur_parameters['lattice'] == 'any'
    assert sec_system[0].x_fleur_parameters['the vacuum begins at z'] == 0.0
    assert sec_system[0].x_fleur_unit_cell_volume.magnitude == approx(275.952900)
    assert sec_system[0].x_fleur_G_max == approx(11.14815)
    assert sec_system[0].x_fleur_vol_interstitial == approx(192.693364)

    sec_scc = sec_run[0].calculation
    assert len(sec_scc[0].scf_iteration) == 20
    assert sec_scc[0].scf_iteration[18].energy.total.value.magnitude == approx(
        -2.52896385e-15
    )
    assert sec_scc[0].scf_iteration[4].energy.free.value.magnitude == approx(
        -2.52896386e-15
    )
    assert sec_scc[0].scf_iteration[9].forces.total.value[1][1].magnitude == approx(
        7.34976523e-10
    )
    assert sec_scc[0].energy.total_t0.value.magnitude == approx(-2.52896385e-15)
    assert sec_scc[0].energy.fermi.magnitude == approx(9.64676355e-19)
    assert sec_scc[0].eigenvalues[0].kpoints[5][0] == approx(-0.111111)
    assert sec_scc[0].eigenvalues[0].energies[0][15][1].magnitude == approx(
        -2.58602618e-19
    )


def test_xml(parser):
    archive = EntryArchive()

    parser.parse('tests/data/fleur/Si/out.xml', archive, None)

    sec_run = archive.run
    assert sec_run[0].program.version == 'fleur 27'
    assert sec_run[0].x_fleur_header[0].x_fleur_precision == 'DOUBLE'

    sec_method = sec_run[0].method
    assert sec_method[0].x_fleur_parameters['Gmax'] == approx(11.07772533)
    assert sec_method[0].x_fleur_parameters['kcrel'] == 0
    assert sec_method[0].dft.xc_functional.correlation[0].name == 'GGA_C_PBE'
    assert (
        sec_method[0].dft.xc_functional.x_fleur_xc_correction
        == 'non-relativistic correction'
    )

    sec_system = sec_run[0].system
    assert sec_system[0].atoms.lattice_vectors[0][1].to('bohr').magnitude == approx(
        5.167355275190
    )
    assert sec_system[0].atoms.labels == ['Si', 'Si']
    assert sec_system[0].atoms.positions[0][1].to('bohr').magnitude == approx(
        1.29183882
    )

    sec_scc = sec_run[0].calculation
    assert len(sec_scc[0].scf_iteration) == 20
    assert sec_scc[0].scf_iteration[18].energy.total.value.to(
        'hartree'
    ).magnitude == approx(-580.0715443342)
    assert sec_scc[0].scf_iteration[4].energy.free.value.to(
        'hartree'
    ).magnitude == approx(-580.0715457719)
    assert sec_scc[0].energy.total_t0.value.to('hartree').magnitude == approx(
        -580.0715444304
    )
    assert sec_scc[0].energy.fermi.to('hartree').magnitude == approx(0.2212693414)
    assert sec_scc[0].eigenvalues[0].kpoints[5][0] == approx(-0.111111)
    assert sec_scc[0].eigenvalues[0].energies[0][15][1].to(
        'hartree'
    ).magnitude == approx(-0.0593160948)
