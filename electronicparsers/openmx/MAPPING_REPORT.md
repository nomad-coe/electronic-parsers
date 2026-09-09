<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## OpenMX / scf_step_parser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `NormRD` | Unmapped | — |
| `Uele` | Mapped | `runschema.calculation.scf_iteration.energy.sum_eigenvalues.value` |

## OpenMX / md_step_parser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `SCF` | Mapped | `runschema.calculation.scf_iteration` |
| `Utot` | Mapped | `runschema.calculation.energy.total.value` |

## OpenMX / species_and_coordinates_parser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom` | Mapped | `runschema.system.atoms.positions`<br>`runschema.system.atoms.labels` |

## OpenMX / species_definition_parser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `species` | Mapped | `runschema.method.atom_parameters.label`<br>`runschema.method.atom_parameters.atom_number`<br>`runschema.method.atom_parameters.pseudopotential`<br>`runschema.method.atom_parameters.core_hole` |

## OpenMX / core_hole_parser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `core_hole` | Mapped | `runschema.method.atom_parameters.core_hole.ms_quantum_bool`<br>`runschema.method.atom_parameters.core_hole.j_quantum_number`<br>`runschema.method.atom_parameters.core_hole.mj_quantum_number` |

## OpenMX / eigenvalues_parser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `kpoints` | Mapped | `runschema.calculation.eigenvalues.kpoints`<br>`runschema.calculation.eigenvalues.n_kpoints`<br>`runschema.calculation.eigenvalues.kpoints_multiplicities`<br>`runschema.method.k_mesh.points`<br>`runschema.method.k_mesh.multiplicities` |
| `eigenvalues` | Mapped | `runschema.calculation.eigenvalues.energies` |

## OpenMX / mainfile_parser

**Summary:** 26 mapped, 2 unmapped quantities (92.86% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `date_start` | Mapped | `runschema.run.time_run.date_start` |
| `elapsed_time` | Mapped | `runschema.run.time_run.date_end` |
| `program_version` | Mapped | `runschema.run.program.version` |
| `md_step` | Mapped | `runschema.calculation.energy.total.value`<br>`runschema.calculation.scf_iteration.energy.sum_eigenvalues.value` |
| `atoms` | Mapped | `runschema.system.atoms.positions`<br>`runschema.system.atoms.labels`<br>`runschema.system.atoms.lattice_vectors` |
| `species` | Mapped | `runschema.method.atom_parameters` |
| `core_hole` | Mapped | `runschema.method.atom_parameters.core_hole.ms_quantum_bool`<br>`runschema.method.atom_parameters.core_hole.mj_quantum_number` |
| `input_lattice_vectors` | Mapped | `runschema.system.atoms.lattice_vectors` |
| `scf.XcType` | Mapped | `runschema.method.dft.xc_functional.exchange`<br>`runschema.method.dft.xc_functional.correlation` |
| `scf.SpinPolarization` | Mapped | `runschema.method.electronic.n_spin_channels` |
| `scf.stress.tensor` | Unmapped | — |
| `Atoms.SpeciesAndCoordinates.Unit` | Mapped | `runschema.system.atoms.positions` |
| `Atoms.UnitVectors.Unit` | Mapped | `runschema.system.atoms.lattice_vectors` |
| `scf.Hubbard.U` | Mapped | `runschema.method.electronic.method` |
| `MD.maxIter` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.optimization_steps_maximum`<br>`simulationworkflowschema.MolecularDynamicsMethod.n_steps` |
| `MD.Type` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method`<br>`simulationworkflowschema.MolecularDynamicsMethod.thermodynamic_ensemble` |
| `MD.TimeStep` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.integration_timestep` |
| `MD.Opt.criterion` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum` |
| `MD.TempControl` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters` |
| `scf.maxIter` | Mapped | `runschema.method.scf.n_max_iteration` |
| `scf.criterion` | Mapped | `runschema.method.scf.threshold_energy_change` |
| `scf.ElectronicTemperature` | Mapped | `runschema.method.electronic.smearing.width` |
| `scf.Kgrid` | Mapped | `runschema.method.k_mesh.grid` |
| `scf.dftD` | Mapped | `runschema.method.electronic.van_der_waals_method` |
| `version.dftD` | Mapped | `runschema.method.electronic.van_der_waals_method` |
| `have_timing` | Mapped | `runschema.run.clean_end` |
| `eigenvalues` | Mapped | `runschema.calculation.eigenvalues.energies`<br>`runschema.calculation.eigenvalues.kpoints` |
| `elapsed.time` | Unmapped | — |

## OpenMX / stdout_parser

**Summary:** 1 mapped, 2 unmapped quantities (33.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `scf.stress.tensor` | Mapped | `runschema.calculation.stress.total.value` |
| `Uele` | Unmapped | — |
| `elapsed.time` | Unmapped | — |
