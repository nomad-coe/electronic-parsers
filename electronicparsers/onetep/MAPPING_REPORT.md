<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## ONETEP / InputParser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameter` | Unmapped | — |
| `block` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |

## ONETEP / OutParser

**Summary:** 26 mapped, 16 unmapped quantities (61.90% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `iteration.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy`<br>`runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry.value` |
| `iteration.band_gap` | Unmapped | — |
| `iteration.x_onetep_rms_occupancy_error` | Unmapped | — |
| `iteration.x_onetep_commutator` | Unmapped | — |
| `iteration.rms_gradient` | Unmapped | — |
| `energy_components` | Mapped | `runschema.calculation.Calculation.energy` |
| `energy_components.contribution` | Mapped | `runschema.calculation.Energy.kinetic_electronic`<br>`runschema.calculation.Energy.correction_hartree`<br>`runschema.calculation.Energy.xc`<br>`runschema.calculation.Energy.ewald`<br>`runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry.value` |
| `energy_components.integrated_density` | Unmapped | — |
| `forces` | Mapped | `runschema.calculation.Calculation.forces` |
| `forces.value` | Mapped | `runschema.calculation.Forces.total`<br>`runschema.calculation.ForcesEntry.value` |
| `convergence_tolerance_energy_difference` | Unmapped | — |
| `convergence_tolerance_force_maximum` | Unmapped | — |
| `convergence_tolerance_displacement_maximum` | Unmapped | — |
| `cell` | Mapped | `runschema.system.System.atoms` |
| `cell.positions` | Mapped | `runschema.system.Atoms.positions` |
| `cell.labels` | Mapped | `runschema.system.Atoms.labels` |
| `mulliken` | Mapped | `runschema.calculation.Calculation.charges`<br>`runschema.calculation.Charges.analysis_method`<br>`runschema.calculation.Charges.value` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `program_name` | Mapped | `runschema.run.Program.name` |
| `x_onetep_number_of_processors` | Unmapped | — |
| `input_file` | Unmapped | — |
| `input` | Mapped | `runschema.method.DFT.xc_functional` |
| `input.parameter` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions`<br>`runschema.method.Functional.name` |
| `date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `date_end` | Mapped | `runschema.run.TimeRun.date_end` |
| `psinc` | Mapped | `runschema.method.Method.electrons_representation`<br>`runschema.method.BasisSetContainer.basis_set` |
| `psinc.cutoff` | Mapped | `runschema.method.BasisSet.cutoff` |
| `geometry_optimization` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.single_point` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.iteration` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.iteration.improve` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.converged` | Unmapped | — |
| `geometry_optimization.final_configuration` | Unmapped | — |
| `single_point` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `tddft` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `tddft.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `tddft.iteration.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy`<br>`runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry.value` |
| `tddft.iteration.x_onetep_tddft_omega_change` | Unmapped | — |
| `tddft.iteration.rms_gradient` | Unmapped | — |
| `tddft.iteration.x_onetep_tddft_number_conv_states` | Unmapped | — |
| `tddft.excitation` | Unmapped | — |
