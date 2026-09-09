<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## Elk / EigenvalParser

**Summary:** 2 mapped, 2 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `n_kpoints` | Unmapped | — |
| `n_states` | Unmapped | — |
| `kpoint` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `eigenvalue_occupancy` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupancies` |

## Elk / MainfileParser

**Summary:** 16 mapped, 22 unmapped quantities (42.11% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.positions` |
| `species` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `species.atom_label` | Mapped | `runschema.system.Atoms.labels` |
| `species.x_elk_muffin_tin_radius` | Unmapped | — |
| `species.x_elk_muffin_tin_points` | Unmapped | — |
| `species.atom_positions` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `spin_treatment` | Unmapped | — |
| `x_elk_kpoints_grid` | Unmapped | — |
| `x_elk_rgkmax` | Unmapped | — |
| `x_elk_gkmax` | Unmapped | — |
| `x_elk_gmaxvr` | Unmapped | — |
| `x_elk_gvector_size` | Unmapped | — |
| `x_elk_gvector_total` | Unmapped | — |
| `x_elk_lmaxapw` | Unmapped | — |
| `x_elk_nuclear_charge` | Unmapped | — |
| `x_elk_core_charge` | Unmapped | — |
| `x_elk_valence_charge` | Unmapped | — |
| `x_elk_excess_charge` | Unmapped | — |
| `x_elk_electronic_charge` | Unmapped | — |
| `x_elk_wigner_radius` | Unmapped | — |
| `x_elk_empty_states` | Unmapped | — |
| `x_elk_valence_states` | Unmapped | — |
| `x_elk_core_states` | Unmapped | — |
| `x_elk_lo` | Unmapped | — |
| `smearing_type` | Mapped | `runschema.method.Smearing.kind` |
| `smearing_width` | Mapped | `runschema.method.Smearing.width` |
| `electronic_temperature` | Unmapped | — |
| `xc_functional` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation` |
| `scf` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `scf.loop` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `scf.loop.energies` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf.loop.energies.key_val` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.fermi`<br>`runschema.calculation.EnergyEntry.kinetic`<br>`runschema.calculation.EnergyEntry.potential` |
| `scf.loop.charges` | Mapped | `runschema.calculation.ScfIteration.charges` |
| `scf.loop.charges.key_val` | Mapped | `runschema.calculation.Charges.total` |
| `scf.loop.charges.muffin_tin` | Mapped | `runschema.calculation.Charges.value` |
| `scf.loop.energy_chage` | Unmapped | — |
| `scf.loop.time` | Mapped | `runschema.calculation.ScfIteration.time_calculation` |
