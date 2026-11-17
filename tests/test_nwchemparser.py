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
from electronicparsers.nwchem import NWChemParser


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


@pytest.fixture(scope='module')
def parser():
    return NWChemParser()


def test_single_point(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/single_point.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.program.version == '6.6'
    assert sec_run.x_nwchem_section_start_information[0].x_nwchem_ga_revision == '10594'

    sec_method = archive.run[0].method[0]
    assert sec_method.electrons_representation[0].basis_set[0].type == 'gaussians'
    assert sec_method.scf.n_max_iteration == 50
    assert len(sec_method.dft.xc_functional.correlation) == 1
    assert sec_method.dft.xc_functional.correlation[0].name == 'MGGA_C_TPSS'
    assert sec_method.dft.xc_functional.exchange[0].weight == approx(1.0)

    assert archive.workflow2.m_def.name == 'SinglePoint'

    sec_scc = archive.run[0].calculation[0]
    assert sec_scc.energy.total.value.magnitude == approx(-3.332424186333889e-16)
    assert sec_scc.x_nwchem_energy_one_electron == approx(-5.35955587575652e-16)
    assert sec_scc.forces.total.value[2][0].magnitude == approx(-4.9432341e-13)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 6
    assert sec_scfs[2].energy.total.value.magnitude == approx(-3.33233301e-16)
    # uncomment this when time_physical def is updated
    # assert sec_scfs[5].time_physical.magnitude == approx(0.3)
    assert sec_scfs[4].energy.change.magnitude == approx(-7.45516347e-23)

    sec_system = archive.run[0].system[0]
    assert len(sec_system.atoms.labels) == 3
    assert sec_system.atoms.positions[0][2].magnitude == approx(-1.1817375e-11)


def test_geometry_optimization(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/geometry_optimization.out', archive, None)

    sec_methods = archive.run[0].method
    assert len(sec_methods) == 4
    assert sec_methods[1].scf.threshold_energy_change.magnitude == approx(
        4.35974472e-24
    )

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 4
    assert sec_sccs[0].energy.correlation.value.magnitude == approx(-1.42869721e-18)
    assert sec_sccs[1].forces.total.value[2][2].magnitude == approx(-2.20633015e-10)
    assert len(sec_sccs[2].scf_iteration) == 4
    assert sec_sccs[0].time_physical.magnitude == approx(0.4)
    assert sec_sccs[1].scf_iteration[1].time_calculation.magnitude == approx(0.1)
    assert sec_sccs[2].scf_iteration[3].time_physical.magnitude == approx(1.6)
    assert sec_sccs[3].time_calculation.magnitude == approx(0.3)

    sec_systems = archive.run[0].system
    assert sec_systems[0].atoms.positions[1][2].magnitude == approx(5.6568542e-11)
    assert sec_systems[3].atoms.periodic == [False, False, False]


def test_molecular_dynamics(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/molecular_dynamics.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert len(sec_sccs) == 6
    assert sec_sccs[2].energy.xc.value.magnitude == approx(-4.04565658e-17)
    assert sec_sccs[5].x_nwchem_section_qmd_step[
        0
    ].x_nwchem_qmd_step_total_energy.magnitude == approx(-3.32745352e-16)
    assert sec_sccs[2].x_nwchem_section_qmd_step[0].x_nwchem_qmd_step_dipole[
        1
    ] == approx(1.141435e-01)
    assert sec_sccs[2].time_calculation.magnitude == approx(0.4)
    assert sec_sccs[4].time_physical.magnitude == approx(1.8)


def test_pw(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/pw.out', archive, None)

    sec_sccs = archive.run[0].calculation
    assert sec_sccs[1].energy.total.value.magnitude == approx(-8.89979631e-17)
    assert sec_sccs[1].spin_S2 == approx(2.0029484134705502)
    sec_scfs = sec_sccs[0].scf_iteration
    assert len(sec_scfs) == 5
    assert sec_scfs[3].energy.total.value.magnitude == approx(-8.86651108e-17)


# settings block of the UHF carbon output, and its variants for the other HF references
UHF_ELECTRONS = '  alpha electrons =     4\n  beta  electrons =     2\n'
BASIS_SUMMARY = (
    '  symmetry adapt  = F\n\n\n'
    ' Summary of "ao basis" -> "ao basis" (spherical)\n'
    ' ------------------------------------------------------------------------------\n'
    '       Tag                 Description            Shells   Functions and Types\n'
    ' ---------------- ------------------------------  ------  ---------------------\n'
    ' C                          cc-pVTZ                 10       30   4s3p2d1f\n'
)


@pytest.mark.parametrize(
    'edits, method, spin_restriction, spin_target, n_spin_channels',
    [
        ([], 'HF', 'unrestricted', 3, 2),
        (
            [
                (
                    UHF_ELECTRONS,
                    '  closed shells   =     2\n  open shells     =     2\n',
                ),
                ('wavefunction    = UHF', 'wavefunction    = ROHF'),
            ],
            'HF',
            'restricted',
            3,
            None,
        ),
        (
            [
                (
                    UHF_ELECTRONS,
                    '  closed shells   =     3\n  open shells     =     0\n',
                ),
                ('wavefunction    = UHF', 'wavefunction    = RHF'),
            ],
            'HF',
            'restricted',
            1,
            1,
        ),
        (
            [('wavefunction    = UHF', 'wavefunction    = MCSCF')],
            None,
            None,
            3,
            None,
        ),
        (
            [(BASIS_SUMMARY, '  symmetry adapt  = F\n\n')],
            'HF',
            'unrestricted',
            3,
            2,
        ),
    ],
    ids=[
        'uhf',
        'rohf-triplet',
        'rhf-singlet',
        'unknown-wavefunction',
        'no-basis-summary',
    ],
)
def test_hf_method(
    parser, tmp_path, edits, method, spin_restriction, spin_target, n_spin_channels
):
    with open('tests/data/nwchem/scf_uhf/output.out') as f:
        text = f.read()
    for old, new in edits:
        assert text.count(old) == 1
        text = text.replace(old, new)
    mainfile = tmp_path / 'output.out'
    mainfile.write_text(text)

    archive = EntryArchive()
    parser.parse(str(mainfile), archive, None)

    sec_method = archive.run[0].method[-1]
    assert sec_method.electronic.method == method
    assert sec_method.x_nwchem_electron_spin_restriction == spin_restriction
    assert sec_method.electronic.spin_target == spin_target
    assert sec_method.electronic.n_spin_channels == n_spin_channels
    assert sec_method.dft is None


def test_hf_calculation(parser):
    archive = EntryArchive()
    parser.parse('tests/data/nwchem/scf_uhf/output.out', archive, None)

    sec_run = archive.run[0]
    assert sec_run.system[0].atoms.labels == ['C']
    assert sec_run.method[-1].scf.n_max_iteration == 30
    assert sec_run.method[-1].electronic.charge.magnitude == approx(0.0)

    sec_scc = sec_run.calculation[-1]
    assert sec_scc.energy.total.value.to('hartree').magnitude == approx(
        -37.691569172750
    )
    assert sec_scc.energy.nuclear_repulsion.value.to('hartree').magnitude == approx(0.0)
    assert sec_scc.time_calculation.magnitude == approx(0.1)
    sec_scfs = sec_scc.scf_iteration
    assert len(sec_scfs) == 5
    assert sec_scfs[0].energy.total.value.to('hartree').magnitude == approx(
        -37.6520514049
    )
    assert sec_scfs[-1].time_physical.magnitude == approx(0.2)


@pytest.mark.parametrize(
    'edits, charge, spin_target',
    [
        ([], 0.0, 3),
        (
            [
                (
                    UHF_ELECTRONS,
                    '  alpha electrons =     3\n  beta  electrons =     2\n',
                ),
                ('  charge          =   0.00', '  charge          =   1.00'),
            ],
            1.0,
            2,
        ),
    ],
    ids=['neutral', 'cation'],
)
def test_hf_charge(parser, tmp_path, edits, charge, spin_target):
    with open('tests/data/nwchem/scf_uhf/output.out') as f:
        text = f.read()
    for old, new in edits:
        assert text.count(old) == 1
        text = text.replace(old, new)
    mainfile = tmp_path / 'output.out'
    mainfile.write_text(text)

    archive = EntryArchive()
    parser.parse(str(mainfile), archive, None)

    sec_electronic = archive.run[0].method[-1].electronic
    assert sec_electronic.charge.to('elementary_charge').magnitude == approx(charge)
    assert sec_electronic.spin_target == spin_target


def test_hf_consecutive_modules(parser, tmp_path):
    with open('tests/data/nwchem/scf_uhf/output.out') as f:
        text = f.read()
    # repeat the SCF module with another total energy, directly before the MP2 module
    start = text.rindex('\n', 0, text.index('NWChem SCF Module')) + 1
    end = text.rindex('\n', 0, text.index('NWChem MP2 Semi-direct')) + 1
    module = text[start:end]
    assert module.count('Total SCF energy =    -37.691569172750') == 1
    second = module.replace(
        'Total SCF energy =    -37.691569172750',
        'Total SCF energy =    -37.700000000000',
    )
    mainfile = tmp_path / 'output.out'
    mainfile.write_text(text[:end] + second + text[end:])

    archive = EntryArchive()
    parser.parse(str(mainfile), archive, None)

    sec_scc = archive.run[0].calculation[-1]
    assert sec_scc.energy.total.value.to('hartree').magnitude == approx(-37.7)


def test_unsupported_module(parser, tmp_path, caplog):
    # a task module the parser does not know, e.g. TCE: only the input geometry is kept
    with open('tests/data/nwchem/scf_uhf/output.out') as f:
        text = f.read()
    assert text.count('NWChem SCF Module') == 1
    mainfile = tmp_path / 'output.out'
    mainfile.write_text(text.replace('NWChem SCF Module', 'NWChem TCE Module'))

    archive = EntryArchive()
    parser.parse(str(mainfile), archive, None)

    sec_run = archive.run[0]
    assert len(sec_run.system) == 1
    assert sec_run.system[0].atoms.labels == ['C']
    assert sec_run.system[0].atoms.positions.magnitude.tolist() == [[0.0, 0.0, 0.0]]
    assert len(sec_run.method) == 0
    assert len(sec_run.calculation) == 0
    assert 'No supported NWChem task module' in caplog.text
    assert "['TCE', 'MP2 Semi-direct Energy/Gradient']" in caplog.text


def test_task_selection(parser, tmp_path):
    # two tasks: an unsupported module with the atom moved to z = 1 A, then the SCF task;
    # the archive describes the SCF task, with the geometry of its own input echo
    with open('tests/data/nwchem/scf_uhf/output.out') as f:
        text = f.read()
    start = text.rindex('\n', 0, text.index('NWChem Input Module')) + 1
    end = text.index('\n', text.index('Task  times')) + 1
    task = text[start:end]
    # the input echo prints the atom in its geometry table and in an XYZ block; the
    # parser reads the table, so move it there
    origin = (
        '    1 C                    6.0000     0.00000000     0.00000000     0.00000000'
    )
    unsupported = task.replace('NWChem SCF Module', 'NWChem TCE Module').replace(
        origin,
        '    1 C                    6.0000     0.00000000     0.00000000     1.00000000',
        1,
    )
    assert unsupported != task.replace('NWChem SCF Module', 'NWChem TCE Module')
    mainfile = tmp_path / 'output.out'
    mainfile.write_text(text[:start] + unsupported + text[start:])

    archive = EntryArchive()
    parser.parse(str(mainfile), archive, None)

    sec_run = archive.run[0]
    assert len(sec_run.system) == 1
    assert sec_run.system[0].atoms.positions.magnitude.tolist() == [[0.0, 0.0, 0.0]]
    assert sec_run.method[-1].electronic.method == 'HF'
    assert sec_run.calculation[-1].energy.total.value.to('hartree').magnitude == approx(
        -37.691569172750
    )
    assert archive.workflow2.m_def.name == 'SinglePoint'
