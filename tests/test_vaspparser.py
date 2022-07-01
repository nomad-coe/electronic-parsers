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

from nomad.units import ureg
from nomad.datamodel import EntryArchive
from electronicparsers.vasp import VASPParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return VASPParser()


@pytest.fixture(scope='module')
def silicon_dos(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Si_dos_band/dos_si.xml', archive, None)
    return archive


@pytest.fixture(scope='module')
def silicon_band(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Si_dos_band/band_si.xml', archive, None)
    return archive


def test_vasprunxml_static(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Mg_bands/vasprun.xml.static', archive, None)

    assert len(archive.run) == 1

    sec_run = archive.run[0]

    assert sec_run.program.compilation_datetime.magnitude == 1366564273.0

    sec_method = sec_run.method[0]
    assert len(sec_method.x_vasp_incar_in) == 27
    assert len(sec_method.x_vasp_incar_out) == 112
    assert sec_method.x_vasp_incar_in['LCHARG']
    assert len(sec_method.k_mesh_points) == 888
    assert sec_method.k_mesh_points[-1][2] == approx(0.48437500)
    assert sec_method.k_mesh_weights[100] == approx(0.00073242)
    assert (sec_method.x_vasp_tetrahedrons_list[0] == [4, 1, 2, 2, 18]).all()
    assert sec_method.atom_parameters[0].mass.magnitude == approx(4.0359402e-26)
    assert len(sec_method.dft.xc_functional.exchange) == 1

    sec_system = sec_run.system[-1]
    assert len(sec_system.atoms.labels) == 1
    assert sec_system.atoms.lattice_vectors[0][0].magnitude == approx(-1.78559323e-10)

    sec_scc = sec_run.calculation[-1]
    assert sec_scc.energy.total.value.magnitude == approx(-2.3264377e-19)
    assert np.shape(sec_scc.forces.total.value) == (1, 3)
    assert sec_scc.stress.total.value[2][2].magnitude == approx(-2.78384438e+08)
    assert len(sec_scc.dos_electronic[0].energies) == 5000
    assert sec_scc.dos_electronic[0].total[0].value[1838].magnitude == approx((.1369 / ureg.eV).to(ureg.joule).magnitude)
    assert len(sec_scc.dos_electronic[0].atom_projected) == 9
    assert sec_scc.dos_electronic[0].atom_projected[0].value[-1].magnitude == approx(3.40162245e+17)
    assert np.shape(sec_scc.eigenvalues[0].energies[0][887]) == (37,)
    assert sec_scc.scf_iteration[2].energy.total_t0.value.magnitude == approx(-2.27580485e-19,)


def test_vasprunxml_relax(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/AgAc_relax/vasprun.xml.relax', archive, None)

    assert len(archive.run[0].method) == 1

    sec_systems = archive.run[0].system
    assert len(sec_systems) == 3
    assert sec_systems[1].atoms.positions[1][0].magnitude == approx(3.2771907e-10)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 3
    assert [len(scc.scf_iteration) for scc in sec_sccs] == [12, 10, 6]
    assert sec_sccs[0].energy.free.value.magnitude == approx(-1.14352735e-18)
    assert np.mean(sec_sccs[1].forces.total.value.magnitude) == 0.0
    assert sec_sccs[2].stress.total.value[2][2].magnitude == approx(-2.02429105e+08)
    assert sec_sccs[2].energy.lowest_unoccupied.magnitude == approx(7.93718304e-19)
    assert sec_sccs[2].energy.highest_occupied.magnitude == approx(7.93702283e-19)
    assert [len(scc.eigenvalues) for scc in sec_sccs] == [0, 0, 1]
    assert [len(scc.dos_electronic) for scc in sec_sccs] == [0, 0, 1]


def test_vasprunxml_bands(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/Mg_bands/vasprun.xml.bands', archive, None)

    sec_k_band = archive.run[0].calculation[0].band_structure_electronic[0]
    assert len(sec_k_band.segment) == 6
    assert np.shape(sec_k_band.segment[0].energies[0][127].magnitude) == (37,)
    assert sec_k_band.segment[1].energies[0][1][1].magnitude == approx(-6.27128785e-18)
    assert sec_k_band.segment[5].occupations[0][127][5] == 0.0


def test_band_silicon(silicon_band):
    """Tests that the band structure of silicon is parsed correctly.
    """
    scc = silicon_band.run[-1].calculation[0]
    band = scc.band_structure_electronic[-1]
    segments = band.segment
    energies = np.array([s.energies.to(ureg.electron_volt).magnitude for s in segments])

    # Check that an energy reference is reported
    energy_reference = scc.energy.fermi
    if energy_reference is None:
        energy_reference = scc.energy.highest_occupied
    assert energy_reference is not None
    energy_reference = energy_reference.to(ureg.electron_volt).magnitude

    # Check that an approporiately sized band gap is found at the given
    # reference energy
    energies = energies.flatten()
    energies.sort()
    lowest_unoccupied_index = np.searchsorted(energies, energy_reference, "right")
    highest_occupied_index = lowest_unoccupied_index - 1
    gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
    assert gap == approx(0.5091)


def test_dos_silicon(silicon_dos):
    """Tests that the DOS of silicon is parsed correctly.
    """
    scc = silicon_dos.run[-1].calculation[0]
    dos = scc.dos_electronic[-1]
    energies = dos.energies.to(ureg.electron_volt).magnitude
    values = np.array([d.value.magnitude for d in dos.total])

    # Check that an energy reference is reported
    energy_reference = scc.energy.fermi
    if energy_reference is None:
        energy_reference = scc.energy.highest_occupied
    assert energy_reference is not None
    energy_reference = energy_reference.to(ureg.electron_volt).magnitude

    # Check that an appropriately sized band gap is found at the given
    # reference energy
    nonzero = np.unique(values.nonzero())
    energies = energies[nonzero]
    energies.sort()
    lowest_unoccupied_index = np.searchsorted(energies, energy_reference, "right")
    highest_occupied_index = lowest_unoccupied_index - 1
    gap = energies[lowest_unoccupied_index] - energies[highest_occupied_index]
    assert gap == approx(0.83140)


def test_outcar(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/AgAc_relax/OUTCAR', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '5.3.2 13Sep12 complex serial LinuxIFC'

    sec_method = sec_run.method[0]
    assert sec_method.basis_set[0].cell_dependent[0].planewave_cutoff.magnitude == approx(8.3313185e-17)
    assert sec_method.dft.xc_functional.exchange[0].name == 'GGA_X_PBE'
    assert len(sec_method.atom_parameters) == 2
    assert sec_method.atom_parameters[1].pseudopotential_name == 'PAW_PBE'

    sec_system = sec_run.system[0]
    assert sec_system.atoms.lattice_vectors[1][0].magnitude == approx(3.141538e-10)
    assert sec_system.atoms.positions[1][0].magnitude == approx(3.14154e-10)

    sec_scc = sec_run.calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-2.23390885e-18)
    assert sec_scc.forces.total.value[0][0].magnitude == 0.0
    assert sec_scc.stress.total.value[0][0].magnitude == approx(7.060258e+09)
    assert sec_scc.energy.lowest_unoccupied.magnitude == approx(9.40461662e-19)
    assert sec_scc.energy.highest_occupied.magnitude == approx(9.51212268e-19)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 11
    assert sec_scfs[4].energy.total.value.magnitude == approx(-1.20437432e-18)
    assert sec_scfs[7].energy.sum_eigenvalues.value.magnitude == approx(-1.61008452e-17)
    sec_eigs = sec_scc.eigenvalues[0]
    assert np.shape(sec_eigs.energies[0][144]) == (15,)
    assert sec_eigs.energies[0][9][14].magnitude == approx(1.41810256e-18)
    assert sec_eigs.occupations[0][49][9] == 2.0
    sec_dos = sec_scc.dos_electronic[0]
    assert len(sec_dos.energies) == 301
    assert sec_dos.total[0].value[282].magnitude == approx((.2545E+01 / ureg.eV).to(ureg.joule).magnitude)
    assert sec_dos.total[0].value_integrated[-1] == 30.0
    assert sec_dos.atom_projected[10].value[-15].magnitude == approx(1.51481425e+17)
    assert sec_dos.atom_projected[5].value[-16].magnitude == approx(1.71267009e+16)


def test_broken_xml(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/vasprun.xml.broken', archive, None)


def test_hybrid(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/hybrid_vasprun.xml.gz', archive, None)

    sec_xc_functional = archive.run[-1].method[-1].dft.xc_functional
    assert sec_xc_functional.hybrid[0].parameters['exact_exchange_mixing_factor'] == .25
    assert sec_xc_functional.hybrid[0].name == 'HYB_GGA_XC_HSE06'


def test_metagga(parser):
    archive = EntryArchive()
    parser.parse('tests/data/vasp/hle17_vasprun.xml.gz', archive, None)

    sec_xc_functional = archive.run[-1].method[-1].dft.xc_functional
    assert sec_xc_functional.contributions[0].name == 'MGGA_XC_HLE17'


def test_dftu_static(parser):
    """Static calculation using PBE+U.
    Geometry taken from NOMAD Archive and Repository site.
    Test generated by N. Daelman on JENA cluster using VASP 6.1.0"""

    archive = EntryArchive()
    # test the values in vasprun.xml and INCAR (selected in place of OUTCAR)
    reference_dir = 'tests/data/vasp/Mg4V2Bi2O12_dftu/'
    for mainfile in ['vasprun.xml', 'OUTCAR']:
        parser.parse(reference_dir + mainfile, archive, None)
        params = archive.run[-1].method[-1].atom_parameters
        references = {'orbital': ('d', 'd'), 'u': (3.25, 2.), 'j': (0., 1.)}
        slice = 0
        for param in params:
            if param.hubbard_model:
                assert param.hubbard_model.method == 'Dudarev'
                assert param.hubbard_model.orbital == references['orbital'][slice]
                assert approx(param.hubbard_model.u.to(ureg.eV).magnitude) == references['u'][slice]
                assert approx(param.hubbard_model.j.to(ureg.eV).magnitude) == references['j'][slice]
                slice += 1

    # check the OUTCAR value when no INCAR is present
    parser.parse('tests/data/vasp/Mg4V2Bi2O12_dftu_no_incar/OUTCAR', archive, None)
    params = archive.run[-1].method[-1].atom_parameters
    assert approx(params[1].hubbard_model.u.to(ureg.eV).magnitude) == 3.2
