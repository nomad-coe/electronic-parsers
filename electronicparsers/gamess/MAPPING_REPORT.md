<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## GAMESS / OutParser

**Summary:** 28 mapped, 6 unmapped quantities (82.35% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `key_val` | Mapped | `runschema.method.Method.electrons_representation.basis_set.atom_centered.name`<br>`runschema.method.Method.electronic.method`<br>`runschema.method.Method.dft.xc_functional` |
| `scf` | Mapped | `runschema.calculation.Calculation.energy.total.value` |
| `scf.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration.energy.total.value` |
| `scf.iteration.iter` | Mapped | `runschema.calculation.ScfIteration.energy.total.value`<br>`runschema.calculation.ScfIteration.energy.change` |
| `scf.energy_total` | Mapped | `runschema.calculation.Calculation.energy.total.value` |
| `scf.converged` | Mapped | `runschema.calculation.Calculation.calculation_converged` |
| `scf.eigenvectors` | Mapped | `runschema.calculation.Calculation.eigenvalues.energies` |
| `scf.eigenvectors.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `time_physical` | Mapped | `runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `coordinates` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `coordinates.unit` | Mapped | `runschema.system.Atoms.positions` |
| `coordinates.label_charge` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.method.AtomParameters.label`<br>`runschema.method.AtomParameters.charge` |
| `coordinates.position` | Mapped | `runschema.system.Atoms.positions` |
| `gradient` | Mapped | `runschema.calculation.Calculation.forces.total.value` |
| `properties` | Mapped | `runschema.calculation.Calculation.energy` |
| `properties.energy_components` | Mapped | `runschema.calculation.Energy.contributions`<br>`runschema.calculation.EnergyEntry.value` |
| `properties.population_analysis` | Mapped | `runschema.calculation.Calculation.charges` |
| `properties.population_analysis.atomic` | Mapped | `runschema.calculation.Charges.value` |
| `properties.population_analysis.spherical_harmonics` | Mapped | `runschema.calculation.Charges.orbital_projected.value` |
| `properties.population_analysis.atomic_orbitals` | Mapped | `runschema.calculation.Charges.orbital_projected.value` |
| `properties.population_analysis.spins` | Mapped | `runschema.calculation.Charges.spins` |
| `properties.electrostatic_moments` | Mapped | `runschema.calculation.Calculation.multipoles` |
| `properties.electrostatic_moments.dipole` | Mapped | `runschema.calculation.Multipoles.dipole` |
| `properties.electrostatic_moments.dipole.origin` | Unmapped | — |
| `properties.electrostatic_moments.dipole.value` | Mapped | `runschema.calculation.MultipolesEntry.value` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `x_gamess_program_implementation` | Unmapped | — |
| `x_gamess_program_execution_date` | Unmapped | — |
| `x_gamess_memory` | Unmapped | — |
| `basis_options` | Mapped | `runschema.method.Method.electrons_representation.basis_set.atom_centered.name`<br>`runschema.method.BasisSetAtomCentered.formula` |
| `control_options` | Mapped | `runschema.method.Method.electronic.method`<br>`runschema.method.Method.electronic.relativity_method`<br>`runschema.method.Method.dft.xc_functional` |
| `system_options` | Unmapped | — |
| `parameters` | Unmapped | — |
| `geometry_opt` | Mapped | `runschema.system.Atoms`<br>`runschema.calculation.Calculation` |
