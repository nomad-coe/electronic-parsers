<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## Octopus / EigenvalueParser

**Summary:** 3 mapped, 1 unmapped quantities (75.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `eigenvalues` | Mapped | `runschema.calculation.Calculation.eigenvalues` |
| `eigenvalues.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.occupations` |
| `eigenvalues.unit` | Unmapped | — |
| `eigenvalues.fermi_energy` | Mapped | `runschema.calculation.Energy.fermi` |

## Octopus / InfoParser

**Summary:** 4 mapped, 6 unmapped quantities (40.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `brillouin_zone_sampling` | Mapped | `runschema.method.KMesh.grid` |
| `brillouin_zone_sampling.kgrid` | Mapped | `runschema.method.KMesh.grid` |
| `brillouin_zone_sampling.n_kpoints` | Unmapped | — |
| `brillouin_zone_sampling.n_kpoints_reduced` | Unmapped | — |
| `brillouin_zone_sampling.kpoints` | Unmapped | — |
| `energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.free`<br>`runschema.calculation.Energy.nuclear_repulsion`<br>`runschema.calculation.Energy.sum_eigenvalues`<br>`runschema.calculation.Energy.electrostatic`<br>`runschema.calculation.Energy.exchange`<br>`runschema.calculation.Energy.correlation`<br>`runschema.calculation.Energy.van_der_waals`<br>`runschema.calculation.Energy.correction_entropy`<br>`runschema.calculation.Energy.kinetic_electronic` |
| `total_magnetic_moment` | Unmapped | — |
| `local_magnetic_moments` | Unmapped | — |
| `dipole` | Unmapped | — |
| `forces` | Mapped | `runschema.calculation.Forces.free` |

## Octopus / ControlParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `line` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.Electronic.smearing`<br>`runschema.method.Electronic.method`<br>`runschema.method.DFT.xc_functional` |

## Octopus / InpParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `block` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.DFT.xc_functional` |

## Octopus / LogParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `block` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.DFT.xc_functional` |

## Octopus / OutParser

**Summary:** 18 mapped, 4 unmapped quantities (81.82% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.options` | Mapped | `runschema.run.Program.version` |
| `grid` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `grid.boxshape` | Unmapped | — |
| `grid.npbc` | Mapped | `runschema.system.Atoms.periodic` |
| `grid.cell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `grid.spacing` | Unmapped | — |
| `theory_level` | Mapped | `runschema.method.DFT.xc_functional` |
| `theory_level.theory_level` | Unmapped | — |
| `theory_level.exchange` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `theory_level.correlation` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `self_consistent` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistent.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistent.iteration.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy` (`Energy.total`) |
| `self_consistent.iteration.fermi_level` | Mapped | `runschema.calculation.ScfIteration.energy` (`Energy.fermi`) |
| `self_consistent.iteration.time` | Mapped | `runschema.calculation.ScfIteration.time_calculation`<br>`runschema.calculation.ScfIteration.time_physical` |
| `time_dependent` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`) |
| `time_dependent.iteration` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`) |
| `x_octopus_info_scf_converged_iterations` | Unmapped | — |
| `minimization` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`)<br>`runschema.system.System.atoms` |
| `minimization.energy_total` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`) |
| `minimization.number` | Mapped | `runschema.system.System.atoms` |
