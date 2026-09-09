<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## CASTEP / CellParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `block` | Mapped | `runschema.calculation.Calculation.band_structure_electronic.segment.endpoints_labels`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.kpoints` |
| `value` | Mapped | `runschema.calculation.Calculation.band_structure_electronic.segment.endpoints_labels`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.kpoints` |

## CASTEP / BandsParser

**Summary:** 2 mapped, 4 unmapped quantities (33.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `n_kpoints` | Unmapped | — |
| `n_spins` | Mapped | `runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |
| `n_electrons` | Unmapped | — |
| `n_eigenvalues` | Unmapped | — |
| `fermi_energies` | Unmapped | — |
| `kpt_energies` | Mapped | `runschema.calculation.Calculation.eigenvalues.kpoints`<br>`runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.kpoints`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |

## CASTEP / OutParser

**Summary:** 43 mapped, 23 unmapped quantities (65.15% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `unit_cell` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `unit_cell.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `unit_cell.lattice_parameters` | Unmapped | — |
| `unit_cell.cell_volume` | Unmapped | — |
| `cell_contents` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.velocities` |
| `cell_contents.positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `cell_contents.velocities` | Mapped | `runschema.system.Atoms.velocities` |
| `species` | Mapped | `runschema.method.Method.atom_parameters.label`<br>`runschema.method.Method.atom_parameters.mass` |
| `species.mass` | Mapped | `runschema.method.Method.atom_parameters.label`<br>`runschema.method.Method.atom_parameters.mass` |
| `dft_d` | Unmapped | — |
| `dft_d.method` | Unmapped | — |
| `dft_d.parameter` | Unmapped | — |
| `scf` | Mapped | `runschema.calculation.Calculation.scf_iteration.energy.total`<br>`runschema.calculation.Calculation.scf_iteration.energy.fermi`<br>`runschema.calculation.Calculation.scf_iteration.energy.change`<br>`runschema.calculation.Calculation.scf_iteration.time_physical`<br>`runschema.calculation.Calculation.scf_iteration.time_calculation` |
| `energy` | Mapped | `runschema.calculation.Calculation.energy.free`<br>`runschema.calculation.Calculation.energy.total_t0`<br>`runschema.calculation.Calculation.energy.contributions` |
| `energy_total` | Mapped | `runschema.calculation.Calculation.energy.total` |
| `enthalpy` | Mapped | `runschema.calculation.Calculation.thermodynamics.enthalpy` |
| `frequency` | Unmapped | — |
| `forces` | Mapped | `runschema.calculation.Calculation.forces.total` |
| `stress_tensor` | Mapped | `runschema.calculation.Calculation.stress.total`<br>`runschema.calculation.Calculation.thermodynamics.pressure` |
| `stress_tensor.stress_tensor` | Mapped | `runschema.calculation.Calculation.stress.total` |
| `stress_tensor.pressure` | Mapped | `runschema.calculation.Calculation.thermodynamics.pressure` |
| `mulliken` | Mapped | `runschema.calculation.Calculation.charges.value`<br>`runschema.calculation.Calculation.charges.orbital_projected` |
| `tddft` | Unmapped | — |
| `tddft.iteration` | Unmapped | — |
| `tddft.energies` | Unmapped | — |
| `tddft.time` | Unmapped | — |
| `interaction_energy` | Unmapped | — |
| `interaction_energy.energy` | Unmapped | — |
| `interaction_energy.shell` | Unmapped | — |
| `fermi_energy` (spin up/down) | Unmapped | — |
| `fermi_energy` (spin-degenerate) | Unmapped | — |
| `kpt_energies` | Mapped | `runschema.calculation.Calculation.eigenvalues.kpoints`<br>`runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |
| `iteration` (basis_set_correction) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration.cutoff` | Unmapped | — |
| `md_data` | Unmapped | — |
| `iteration` (md) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (dmd) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (di) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (tss) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (cg_refinement) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `spin_density` | Unmapped | — |
| `iteration` (bfgs) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration.iteration` (bfgs) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `program_version` | Mapped | `runschema.run.Program.name`<br>`runschema.run.Program.version` |
| `program_compilation` | Mapped | `runschema.run.Program.compilation_host` |
| `compiler` | Unmapped | — |
| `maths_library` | Unmapped | — |
| `fft_library` | Unmapped | — |
| `constants_reference` | Unmapped | — |
| `run_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `title` | Mapped | `runschema.method.Method.electrons_representation`<br>`runschema.method.DFT.xc_functional`<br>`runschema.method.Electronic.smearing`<br>`runschema.method.Electronic.relativity_method`<br>`runschema.method.Electronic.van_der_waals_method` |
| `dft_u` | Mapped | `runschema.method.Electronic.method` |
| `calculation` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.vibrational_frequencies` | Mapped | `runschema.calculation.Calculation.vibrational_frequencies.value`<br>`runschema.calculation.Calculation.vibrational_frequencies.infrared`<br>`runschema.calculation.Calculation.vibrational_frequencies.raman` |
| `calculation.raman_tensor` | Unmapped | — |
| `calculation.bandstructure` | Mapped | `runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |
| `calculation.basis_set_correction` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.tss` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.cg_refinement` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.md` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.dmd` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.di` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.bfgs` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.final` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `time` | Mapped | `runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `nmr_flag` | Mapped | `runschema.method.Method.label` |

## CASTEP / CastepParser

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.
