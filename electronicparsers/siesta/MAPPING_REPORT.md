<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
# SIESTA Parser — Mapping Report

## SIESTA / FDFParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameter` | Mapped | `runschema.method.Method.dft.xc_functional.exchange.name`<br>`runschema.method.Method.dft.xc_functional.correlation.name`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.lattice_vectors` |
| `block` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.lattice_vectors` |

## SIESTA / OutParser

**Summary:** 32 mapped, 8 unmapped quantities (80.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `coordinates_format` | Mapped | `runschema.system.Atoms.positions` |
| `labels` | Mapped | `runschema.system.Atoms.labels` |
| `species` | Mapped | `runschema.system.Atoms.labels` |
| `positions` | Mapped | `runschema.system.Atoms.positions` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `atoms` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `atoms` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.free`<br>`runschema.calculation.Energy.xc`<br>`runschema.calculation.Energy.sum_eigenvalues`<br>`runschema.calculation.Energy.electrostatic`<br>`runschema.calculation.Energy.nuclear_repulsion`<br>`runschema.calculation.Energy.contributions` |
| `energy.contribution` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `scf` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf.step` | Mapped | `runschema.calculation.ScfIteration.energy.total`<br>`runschema.calculation.ScfIteration.energy.free`<br>`runschema.calculation.ScfIteration.energy.fermi`<br>`runschema.calculation.ScfIteration.energy.types` |
| `energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.contribution` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `forces` | Mapped | `runschema.calculation.Forces.total` |
| `forces.atomic` | Mapped | `runschema.calculation.Forces.total.value` |
| `stress_tensor` | Mapped | `runschema.calculation.Stress.total.value` |
| `stress_tensor` | Mapped | `runschema.calculation.Stress.total.value` |
| `electric_dipole` | Mapped | `runschema.calculation.Multipoles.dipole.total` |
| `mulliken` | Mapped | `runschema.calculation.Charges.value`<br>`runschema.calculation.Charges.total`<br>`runschema.calculation.Charges.analysis_method` |
| `mulliken.atom` | Mapped | `runschema.calculation.Charges.orbital_projected`<br>`runschema.calculation.Charges.spin_projected` |
| `mulliken.atom.label` | Mapped | `runschema.calculation.ChargesValue.atom_label` |
| `mulliken.atom.orbital` | Mapped | `runschema.calculation.ChargesValue.orbital` |
| `mulliken.atom.values` | Mapped | `runschema.calculation.ChargesValue.value`<br>`runschema.calculation.Charges.value` |
| `mulliken.spin` | Mapped | `runschema.calculation.ChargesValue.spin` |
| `mulliken.q_tot` | Unmapped | — |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_siesta_arch` | Unmapped | — |
| `header.x_siesta_compiler_flags` | Unmapped | — |
| `header.x_siesta_parallel` | Unmapped | — |
| `input_data_file` | Unmapped | — |
| `simulation_parameters` | Unmapped | — |
| `simulation_parameters.redata` | Unmapped | — |
| `x_siesta_n_nodes` | Unmapped | — |
| `run_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `run_end` | Mapped | `runschema.run.TimeRun.date_end` |
| `single_point` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |
| `geometry_optimization` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.step` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |
