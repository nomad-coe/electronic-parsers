<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## MOPAC / MainfileParser

**Summary:** 17 mapped, 4 unmapped quantities (80.95% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `calculation` | Unmapped | — |
| `calculation.parameters` | Unmapped | — |
| `calculation.date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `coordinates` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `x_mopac_fhof` | Unmapped | — |
| `energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `energy_electronic` | Mapped | `runschema.calculation.Energy.electronic` |
| `energy_nuclear_repulsion` | Mapped | `runschema.calculation.Energy.nuclear_repulsion` |
| `n_filled_levels` | Unmapped | — |
| `n_alpha_electrons` | Mapped | `runschema.calculation.BandEnergies.occupations` |
| `n_beta_electrons` | Mapped | `runschema.calculation.BandEnergies.occupations` |
| `eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `forces` | Mapped | `runschema.calculation.Forces.total` |
| `dipole` | Mapped | `runschema.calculation.Multipoles.dipole` |
| `atomic_population` | Mapped | `runschema.calculation.Charges.value` |
| `orbital_population` | Mapped | `runschema.calculation.Charges.orbital_projected` |
| `spin_S2` | Mapped | `runschema.calculation.Calculation.spin_S2` |
| `time_physical` | Mapped | `runschema.calculation.Calculation.time_physical` |
| `time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation` |
