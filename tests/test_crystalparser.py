#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
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
import numpy as np
import pytest
from electronicparsers.crystal import CrystalParser
from nomad.datamodel import EntryArchive


parser = CrystalParser()


def approx(value, abs=0, rel=1e-6):
    return pytest.approx(value, abs=abs, rel=rel)


def parse(filepath):
    """Used to parse a file in the fiven filepath with the Crystal parser."""
    archive = EntryArchive()
    logger = None
    parser.parse(filepath, archive, logger)
    return archive


def test_misc():
    """Generic tests for exceptional cases that the parser needs to take into
    consideration.
    """
    # The atomic number is given in the NAT convention
    filepath = 'tests/data/crystal/misc/nat/HfS2_PBE0D3_ZD_fc3_supercell-00497.o'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    system = archive.run[0].system[0]
    assert set(system.atoms.species) == set((16, 72))

    # Tests that ghost atoms are ignored in the system. Maybe they need their
    # own metainfo?
    filepath = 'tests/data/crystal/misc/ghosts/fevo46_sngt_ti_zero.cryst.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    system = archive.run[0].system[0]
    assert set(system.atoms.species) == set((8, 26, 22, 38))

    # Tests that substitutions are handled correctly
    filepath = 'tests/data/crystal/misc/substitution/neutral.cryst.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    system = archive.run[0].system[0]
    assert set(system.atoms.species) == set((8, 26, 22, 38))

    # Geometry optimization with constraints
    filepath = 'tests/data/crystal/misc/constraints/ionic1_fullspin_spinfx_2.cryst.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)

    # Displacement of atoms
    filepath = 'tests/data/crystal/misc/displacement/fe50_x8_l0_re.cryst.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)


def test_xc_functionals():
    """Tests that different kinds of XC functionals are correctly identified."""
    # PBE
    filepath = 'tests/data/crystal/xc_functionals/pbe_1/supercell-00138.o'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.run[0].method[0]
    assert method.dft.xc_functional.name == '1.0*GGA_C_PBE+1.0*GGA_X_PBE'

    # PW91 Hybrid
    filepath = 'tests/data/crystal/xc_functionals/pw91_hybrid/f075_l3_ph.o'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.run[0].method[0]
    assert method.dft.xc_functional.name == '1.0*GGA_C_PW91+0.9*GGA_X_PW91+0.1*HF_X'

    # WC1LYP
    filepath = 'tests/data/crystal/xc_functionals/wc1lyp/albite_freq_intens.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.run[0].method[0]
    assert method.dft.xc_functional.name == '1.0*GGA_C_LYP+0.84*GGA_X_WC+0.16*HF_X'

    # PBE0
    filepath = 'tests/data/crystal/xc_functionals/pbe0/ZrS2_band_structure_dos.prop.o'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.run[0].method[0]
    assert method.dft.xc_functional.name == '1.0*HYB_GGA_XC_PBEH'


def test_molecule():
    """Tests that molecular calculations are parsed correctly."""
    filepath = 'tests/data/crystal/molecule/w.out'
    archive = parse(filepath)
    asserts_basic(archive, system_type='0D')
    asserts_basic_code_specific(archive, system_type='0D')
    method = archive.run[0].method[0]
    assert method.dft.xc_functional.name == '1.0*HYB_GGA_XC_PBEH'


def test_surface():
    """Tests that surface calculations are parsed correctly."""
    filepath = 'tests/data/crystal/surface/w221_sr_pbe0.cryst.out'
    archive = parse(filepath)
    asserts_basic(archive, system_type='2D')
    asserts_basic_code_specific(archive, system_type='2D')


def test_nanotube():
    """Tests that nanotube calculations are parsed correctly."""
    # Nanotube SCF
    filepath = 'tests/data/crystal/nanotube/scf/test_nano07_3.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)

    # Nanotube geo opt
    filepath = 'tests/data/crystal/nanotube/geo_opt/test_nano05.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)


def test_single_point_dft():
    """Tests that single point DFT calculations are parsed succesfully."""
    filepath = 'tests/data/crystal/single_point/dft/output.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, vdw='DFT-D3', forces=True)


def test_single_point_hf():
    """Tests that single point HF calculations are parsed succesfully."""
    filepath = 'tests/data/crystal/single_point/hf/output.out'
    archive = parse(filepath)
    asserts_basic(archive, method_type='HF')
    asserts_basic_code_specific(archive, method_type='HF')


def test_single_point_forces():
    """Tests that forces are correctly parsed."""
    filepath = (
        'tests/data/crystal/single_point/forces/HfS2_PBE0D3_ZD_fc3_supercell-00001.o'
    )
    archive = parse(filepath)
    asserts_basic(archive, vdw='DFT-D3', forces=True)
    asserts_basic_code_specific(archive)


def test_geo_opt():
    """Tests that geometry optimization is parsed correctly."""
    filepath = 'tests/data/crystal/geo_opt/nio_tzvp_pbe0_opt.o'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, run_type='geo_opt')
    asserts_geo_opt(archive)
    calcs = archive.run[-1].calculation
    assert calcs[1].time_physical.magnitude == approx(1232.5)
    assert calcs[4].time_calculation.magnitude == approx(388.61)
    assert calcs[7].time_physical.magnitude == approx(4531.44)


def test_band_structure():
    """Tests that band structure calculation is parsed correctly."""
    # Regular band structure with .f25 file
    filepath = 'tests/data/crystal/band_structure/nacl_hf/NaCl.out'
    archive = parse(filepath)
    asserts_basic(archive, method_type='HF')
    asserts_basic_code_specific(archive, method_type='HF', run_type='band_structure')
    asserts_band_structure(archive)
    run = archive.run[0]
    method = run.method[0]
    assert method.dft.xc_functional.name == '1.0*HF_X'

    # This band structure is missing the f25 file so no output should be
    # generated for band structure. The functional should still be possible to
    # read.
    filepath = 'tests/data/crystal/band_structure/no_f25_1/test04_dft.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, run_type='band_structure')
    run = archive.run[0]
    method = run.method[0]
    assert method.dft.xc_functional.name == '1.0*HYB_GGA_XC_B3LYP'

    # Another band structure with missing f25 file with different number of
    # spaces used in the output.
    filepath = 'tests/data/crystal/band_structure/no_f25_2/TiS2_band_structure.prop.o'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, run_type='band_structure')
    run = archive.run[0]
    method = run.method[0]
    assert method.dft.xc_functional.name == '1.0*HYB_GGA_XC_PBEH'


def test_dos():
    """Tests that DOS is parsed successfully."""
    filepath = 'tests/data/crystal/dos/nacl_hf/NaCl.out'
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, run_type='dos')
    asserts_dos(archive)


def asserts_basic(archive, method_type='DFT', system_type='3D', vdw=None, forces=False):
    run = archive.run[0]
    systems = run.system
    method = run.method[0]
    sccs = run.calculation
    n_atoms = len(systems[0].atoms.species)

    assert run
    assert sccs
    assert systems
    assert method

    assert run.program.name is not None
    assert run.program.version is not None
    assert run.time_run.date_start is not None
    assert run.time_run.date_end is not None

    if method_type == 'DFT':
        assert method.dft.xc_functional is not None
        assert method.electronic.method == 'DFT'
    if vdw:
        assert method.electronic.van_der_waals_method == vdw

    for system in systems:
        assert system.atoms.positions is not None
        assert system.atoms.species is not None
        assert system.atoms.labels is not None
        if system_type != '0D':
            assert system.atoms.lattice_vectors is not None
            assert system.atoms.lattice_vectors.shape == (3, 3)
            assert system.atoms.periodic == [True] * 3
        else:
            assert system.atoms.lattice_vectors is None
            assert system.atoms.periodic == [False] * 3
        assert system.atoms.positions.shape[0] == n_atoms
        assert system.atoms.species.shape[0] == n_atoms
        assert len(system.atoms.labels) == n_atoms

    # assert method.scf_max_iteration is not None
    # assert method.scf_threshold_energy_change is not None

    for scc in sccs:
        assert scc.system_ref is not None
        assert scc.method_ref is not None
        scf = scc.scf_iteration
        if scf:
            assert scc.calculation_converged is True
            assert scc.n_scf_iterations is not None
            for scf in scc.scf_iteration:
                assert scf.energy.total is not None
                assert scf.energy.change is not None
        if forces:
            assert scc.forces is not None
            assert scc.forces.total.value.shape[0] == n_atoms


def asserts_basic_code_specific(
    archive, method_type='DFT', system_type='3D', run_type='scf', vdw=None, forces=False
):
    run = archive.run[0]
    method = run.method[0]

    assert run.program.name == 'Crystal'
    assert method.electrons_representation[0].basis_set[0].type == 'gaussians'

    assert method.x_crystal_n_atoms is not None
    assert method.x_crystal_n_shells is not None
    assert method.x_crystal_n_orbitals is not None
    assert method.x_crystal_n_electrons is not None
    assert method.x_crystal_n_core_electrons is not None
    assert method.x_crystal_n_symmops is not None
    assert method.x_crystal_tol_coulomb_overlap is not None
    assert method.x_crystal_tol_coulomb_penetration is not None
    assert method.x_crystal_tol_exchange_overlap is not None
    assert method.x_crystal_tol_pseudo_overlap_f is not None
    assert method.x_crystal_tol_pseudo_overlap_p is not None
    assert method.x_crystal_pole_order is not None
    assert method.x_crystal_type_of_calculation is not None
    if system_type == '3D':
        assert method.x_crystal_is1 is not None
        assert method.x_crystal_is2 is not None
        assert method.x_crystal_is3 is not None
        assert method.x_crystal_k_pts_monk_net is not None
        assert method.x_crystal_symmops_k is not None
        assert method.x_crystal_symmops_g is not None
        assert method.x_crystal_shrink_gilat is not None
        assert method.x_crystal_n_k_points_ibz is not None
        assert method.x_crystal_shrink is not None
    assert method.x_crystal_weight_f is not None

    bases = method.electrons_representation[0].basis_set[0].atom_centered
    for basis in bases:
        assert isinstance(basis.atom_number, np.int32)
        for shell in basis.x_crystal_section_shell:
            assert shell.x_crystal_shell_type is not None
            assert shell.x_crystal_shell_range is not None
            assert shell.x_crystal_shell_coefficients.shape[1] == 4


def asserts_geo_opt(
    archive, method_type='DFT', system_type='3D', vdw=None, forces=False
):
    workflow = archive.workflow2
    assert workflow.method.convergence_tolerance_energy_difference is not None
    assert workflow.method.convergence_tolerance_displacement_maximum is not None
    assert workflow.results.is_converged_geometry is True


def asserts_band_structure(
    archive, method_type='DFT', system_type='3D', vdw=None, forces=False
):
    run = archive.run[0]
    scc = run.calculation[0]
    bands = scc.band_structure_electronic[0]
    assert scc.energy.fermi is not None
    assert bands.reciprocal_cell.shape == (3, 3)
    for segment in bands.segment:
        assert segment.kpoints.shape[1] == 3
        assert segment.energies is not None
        assert segment.energies.shape[1] == segment.kpoints.shape[0]
        assert segment.n_kpoints is not None


def asserts_dos(archive, method_type='DFT', system_type='3D', vdw=None, forces=False):
    run = archive.run[0]
    dos_found = False
    for scc in run.calculation:
        dos = scc.dos_electronic
        if dos:
            dos = dos[0]
            dos_found = True
            assert (
                scc.energy.fermi is not None or scc.energy.highest_occupied is not None
            )
            assert dos.energies.shape == dos.total[0].value.shape
    assert dos_found
