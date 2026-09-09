<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## Qbox / parser.py

**Summary:** 28 mapped, 20 unmapped quantities (58.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `run.parameter` | Mapped | `runschema.method.Method.dft.xc_functional`<br>`runschema.method.Method.x_qbox_input_parameters` |
| `run.species` | Unmapped | — |
| `run.species.symbol` | Unmapped | — |
| `run.species.atomic_numer` | Unmapped | — |
| `run.species.mass` | Unmapped | — |
| `run.iteration` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `run.iteration.charge` | Unmapped | — |
| `run.iteration.energy_kinetic_electronic` | Mapped | `runschema.calculation.Energy.kinetic_electronic` |
| `run.iteration.energy_x_qbox_conf` | Unmapped | — |
| `run.iteration.energy_x_qbox_ps` | Unmapped | — |
| `run.iteration.energy_x_qbox_nl` | Unmapped | — |
| `run.iteration.energy_coulomb` | Mapped | `runschema.calculation.Energy.coulomb` |
| `run.iteration.energy_xc` | Mapped | `runschema.calculation.Energy.xc` |
| `run.iteration.energy_x_qbox_sr` | Unmapped | — |
| `run.iteration.energy_x_qbox_self` | Unmapped | — |
| `run.iteration.energy_x_qbox_ts` | Unmapped | — |
| `run.iteration.energy_x_qbox_exf` | Unmapped | — |
| `run.iteration.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `run.iteration.energy_x_qbox_pv` | Unmapped | — |
| `run.iteration.energy_x_qbox_efield` | Unmapped | — |
| `run.iteration.energy_x_qbox_enthalpy` | Unmapped | — |
| `run.iteration.stress_tensor` | Mapped | `runschema.calculation.Stress` |
| `run.iteration.stress_tensor.contribution` | Mapped | `runschema.calculation.Stress.total`<br>`runschema.calculation.Stress.contributions` |
| `run.iteration.stress_tensor.contribution.kind` | Mapped | `runschema.calculation.StressEntry.kind` |
| `run.iteration.stress_tensor.contribution.value` | Mapped | `runschema.calculation.StressEntry.value` |
| `run.iteration.multipole` | Mapped | `runschema.calculation.Multipoles` |
| `run.iteration.multipole.dipole` | Mapped | `runschema.calculation.Multipoles.dipole` |
| `run.iteration.multipole.quadrupole` | Mapped | `runschema.calculation.Multipoles.quadrupole` |
| `run.iteration.mlwf` | Unmapped | — |
| `run.iteration.mlwf.center` | Unmapped | — |
| `run.iteration.scf` | Mapped | `runschema.calculation.ScfIteration` |
| `run.iteration.scf.charge` | Unmapped | — |
| `run.iteration.scf.energy_sum_eigenvalues` | Mapped | `runschema.calculation.Energy.sum_eigenvalues` |
| `run.iteration.scf.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `run.iteration.atomset` | Mapped | `runschema.system.Atoms` |
| `run.iteration.atomset.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `run.iteration.atomset.atom` | Mapped | `runschema.system.Atoms` |
| `run.iteration.atomset.atom.label` | Mapped | `runschema.system.Atoms.labels` |
| `run.iteration.atomset.atom.position` | Mapped | `runschema.system.Atoms.positions` |
| `run.iteration.atomset.atom.velocity` | Mapped | `runschema.system.Atoms.velocities` |
| `run.iteration.atomset.atom.force` | Mapped | `runschema.calculation.Forces.total` |
| `run.iteration.time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `start_time` | Mapped | `runschema.run.TimeRun.date_start` |
| `end_time` | Mapped | `runschema.run.TimeRun.date_end` |
| `x_qbox_nodename` | Unmapped | — |
| `x_qbox_loading_xml_file` | Unmapped | — |
| `run` | Mapped | `runschema.run.Run` |
