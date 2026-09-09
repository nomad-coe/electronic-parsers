<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## CPMD / MainfileParser

**Summary:** 22 mapped, 26 unmapped quantities (45.83% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom_coordinates_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` (`ForcesEntry.value`) |
| `scf` | Mapped | `runschema.calculation.ScfIteration.time_calculation`<br>`runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.ScfIteration.energy` (`Energy.total.value`, `Energy.change`) |
| `energies` | Mapped | `runschema.calculation.Calculation.energy` |
| `energies.total` | Mapped | `runschema.calculation.Energy.total` (`EnergyEntry.value`) |
| `energies.kinetic` | Mapped | `runschema.calculation.Energy.kinetic` (`EnergyEntry.value`)<br>`runschema.calculation.Energy.total.kinetic` |
| `energies.electrostatic` | Mapped | `runschema.calculation.Energy.electrostatic` (`EnergyEntry.value`) |
| `energies.x_cpmd_eself` | Unmapped | — |
| `energies.x_cpmd_esr` | Unmapped | — |
| `energies.x_cpmd_local_pseudopotential` | Unmapped | — |
| `energies.x_cpmd_nl_pseudopotential` | Unmapped | — |
| `energies.xc` | Mapped | `runschema.calculation.Energy.xc` (`EnergyEntry.value`) |
| `x_cpmd_restart_file` | Unmapped | — |
| `x_cpmd_total_number_of_scf_steps` | Unmapped | — |
| `x_cpmd_gnmax` | Unmapped | — |
| `x_cpmd_gnorm` | Unmapped | — |
| `x_cpmd_cnstr` | Unmapped | — |
| `time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `header` | Mapped | `runschema.run.Program.version`<br>`runschema.run.TimeRun.date_start` |
| `header.date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_cpmd_compilation_date` | Unmapped | — |
| `header.x_cpmd_input_filename` | Unmapped | — |
| `header.x_cpmd_run_host_name` | Unmapped | — |
| `header.x_cpmd_process_id` | Unmapped | — |
| `header.x_cpmd_run_user_name` | Unmapped | — |
| `info` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method` |
| `info.simulation_type` | Unmapped | — |
| `info.simulation_parameters` | Unmapped | — |
| `info.geometry_optimization_method` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method` |
| `atoms` | Mapped | `runschema.system.Atoms.labels` |
| `supercell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `supercell.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `supercell.lattice_vectors_reciprocal` | Unmapped | — |
| `supercell.x_cpmd_cell_symmetry` | Unmapped | — |
| `supercell.x_cpmd_cell_lattice_constant` | Unmapped | — |
| `supercell.x_cpmd_cell_dimension` | Unmapped | — |
| `supercell.x_cpmd_cell_volume` | Unmapped | — |
| `supercell.x_cpmd_cell_real_space_mesh` | Unmapped | — |
| `supercell.x_cpmd_wave_function_cutoff` | Mapped | `runschema.method.BasisSet.cutoff` |
| `supercell.x_cpmd_density_cutoff` | Unmapped | — |
| `supercell.x_cpmd_number_of_planewaves_wave_function` | Unmapped | — |
| `supercell.x_cpmd_number_of_planewaves_density` | Unmapped | — |
| `geometry_optimization` | Mapped | routes `step` (see `step_quantities` above) |
| `geometry_optimization.step` | Mapped | routes `step_quantities` (see above) |
| `single_point` | Mapped | routes `step_quantities` (see above) |
| `molecular_dynamics` | Mapped | routes `frame` (see below) |
| `molecular_dynamics.frame` | Mapped | `runschema.calculation.Energy.total` (`value`, `potential`, `kinetic`)<br>`runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.temperature` |
| `molecular_dynamics.averaged` | Unmapped | — |

## CPMD / XYZParser

**Summary:** 2 mapped, 2 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `step` | Mapped | routes `step.positions` (see below) |
| `step.step` | Unmapped | — |
| `step.labels` | Unmapped | — |
| `step.positions` | Mapped | `runschema.system.Atoms.positions` |
