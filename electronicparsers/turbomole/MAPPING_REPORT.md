<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
# TURBOMOLE legacy parser — mapping report

The TURBOMOLE parser defines three declarative file-parser classes that declare
`Quantity(...)` lists: `EigenvaluesParser`, `ControlParser` and `OutParser`.
`AuxiliaryOutParser` is a `FileParser` subclass with a custom `matrix` reader and
declares no `Quantity`, so it is reported without a table. Nested `sub_parser`
quantities are listed with dotted paths reflecting their container. The
`module_quantities` block is shared by every `module_*` sub-parser (its members
are declared once and reused by list concatenation); it is listed once, followed
by the module-specific extensions under their respective module prefix
(`aoforce.`, `ccsdf12.`, `dscf.`, `escf.`, `freeh.`, `pnoccsd.`, `ricc2.`,
`ridft.`, `rirpa.`, `statpt.`). Status is Mapped only when `parse()` writes the
quantity into the normalized run schema; quantities written solely to
code-specific `x_turbomole_*` targets are Unmapped.

## TURBOMOLE / AuxiliaryOutParser

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## TURBOMOLE / EigenvaluesParser

**Summary:** 2 mapped, 1 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `irrep` | Unmapped | — |
| `eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `occupation` | Mapped | `runschema.calculation.BandEnergies.occupations` |

## TURBOMOLE / ControlParser

**Summary:** 0 mapped, 9 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `operating_system` | Unmapped | — |
| `scf_iter_limit` | Unmapped | — |
| `scf_conv` | Unmapped | — |
| `time_for_integral_calc` | Unmapped | — |
| `pople_kind` | Unmapped | — |
| `damping_parameter` | Unmapped | — |
| `scfint` | Unmapped | — |
| `interconversion_status` | Unmapped | — |
| `drvopt` | Unmapped | — |

## TURBOMOLE / OutParser

**Summary:** 68 mapped, 23 unmapped quantities (74.73% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `scf_quantities.iteration.damping_scf_iteration` | Unmapped | — |
| `scf_quantities.iteration.energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.ScfIteration.x_turbomole_energy_1electron_scf_iteration`<br>`runschema.calculation.ScfIteration.x_turbomole_energy_2electron_scf_iteration` |
| `scf_quantities.iteration.energy_XC` | Mapped | `runschema.calculation.Energy.xc` |
| `scf_quantities.iteration.norm_diis_scf_iteration` | Unmapped | — |
| `scf_quantities.iteration.norm_fia` | Unmapped | — |
| `scf_quantities.iteration.norm_fock` | Unmapped | — |
| `scf_quantities.iteration.delta_eigenvalues` | Unmapped | — |
| `scf_quantities.iteration.fon` | Unmapped | — |
| `self_consistency.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistency.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistency.number_of_scf_iterations` | Mapped | `runschema.calculation.Calculation.n_scf_iterations` |
| `atomic_info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.AtomParameters.label` |
| `atomic_info.info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `atomic_info.center_of_nuclear_mass` | Unmapped | — |
| `atomic_info.center_of_nuclear_charge` | Unmapped | — |
| `basis_set_info` | Mapped | `runschema.method.Method.electrons_representation` |
| `basis_set_info.auxiliary` | Mapped | `runschema.method.BasisSetContainer.scope` |
| `basis_set_info.spherical` | Mapped | `runschema.method.BasisSetAtomCentered.n_basis_functions` |
| `basis_set_info.atom` | Mapped | `runschema.method.BasisSetAtomCentered.name`<br>`runschema.method.BasisSetAtomCentered.atom_number`<br>`runschema.method.BasisSetAtomCentered.n_basis_functions` |
| `basis_set_info.total` | Unmapped | — |
| `mo_occupation` | Unmapped | — |
| `wavefunction_model` | Mapped | `runschema.method.Electronic.method` |
| `dft_functional` | Mapped | `runschema.method.Functional.name` |
| `dft_functional.functional` | Mapped | `runschema.method.Functional.name` |
| `dft_functional.exchange` | Unmapped | — |
| `dft_functional.correlation` | Unmapped | — |
| `embedding_point_charges` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `embedding_point_charges.pceem_max_multipole` | Unmapped | — |
| `embedding_point_charges.pceem_multipole_precision` | Unmapped | — |
| `embedding_point_charges.pceem_min_separation_cells` | Unmapped | — |
| `embedding_point_charges.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `embedding_point_charges.redefined` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `embedding_point_charges.pc_cluster` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `embedding_point_charges.qm_cluster` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `dft_d3` | Mapped | `runschema.method.Electronic.van_der_waals_method`<br>`runschema.calculation.Energy.van_der_waals` |
| `dft_d3.version` | Mapped | `runschema.method.Electronic.van_der_waals_method` |
| `dft_d3.energy_van_der_Waals` | Mapped | `runschema.calculation.Energy.van_der_waals` |
| `uhf` | Mapped | `runschema.method.Electronic.n_spin_channels` |
| `smearing` | Mapped | `runschema.method.Smearing.kind`<br>`runschema.method.Smearing.width` |
| `smearing.kind` | Mapped | `runschema.method.Smearing.kind` |
| `smearing.width` | Mapped | `runschema.method.Smearing.width` |
| `energy_reference_wavefunction` | Unmapped | — |
| `energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.kinetic` |
| `self_consistency` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistency.iteration (CCSD)` | Unmapped | — |
| `self_consistency.convergence` | Unmapped | — |
| `energies_MP2` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `energies_CCSD` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `energies_CCSD(T0)` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `energy_gradient` | Mapped | `runschema.calculation.Forces.total` |
| `eigenvalue_file` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `wall_time` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `aoforce.hessian` | Mapped | `runschema.calculation.Calculation.hessian_matrix` |
| `aoforce.hessian_file` | Mapped | `runschema.calculation.Calculation.hessian_matrix` |
| `aoforce.normal_modes_vibrational_frequencies` | Unmapped | — |
| `aoforce.normal_modes_file` | Unmapped | — |
| `aoforce.vibrational_spectrum_file` | Unmapped | — |
| `aoforce.energy_zero_point` | Mapped | `runschema.calculation.Energy.zero_point` |
| `aoforce.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `aoforce.energy_current` | Mapped | `runschema.calculation.Energy.current` |
| `ccsdf12.energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `dscf.self_consistency` | Mapped | `runschema.calculation.Calculation.scf_iteration`<br>`runschema.calculation.Calculation.n_scf_iterations` |
| `escf.gw` | Mapped | `runschema.calculation.BandEnergies.value_ks`<br>`runschema.method.Electronic.n_spin_channels` |
| `escf.gw.parameters` | Mapped | `runschema.method.Electronic.n_spin_channels` |
| `escf.gw.qp_states` | Mapped | `runschema.calculation.BandEnergies.value_ks`<br>`runschema.calculation.BandEnergies.value_qp`<br>`runschema.calculation.BandEnergies.value_ks_xc` |
| `freeh.thermodynamics` | Mapped | `runschema.calculation.Thermodynamics.temperature`<br>`runschema.calculation.Thermodynamics.pressure`<br>`runschema.calculation.Energy.correction_entropy` |
| `freeh.energy_zero_point` | Mapped | `runschema.calculation.Energy.zero_point` |
| `pnoccsd.methods` | Mapped | `runschema.method.Electronic.method` |
| `pnoccsd.energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `ricc2.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `ridft.self_consistency` | Mapped | `runschema.calculation.Calculation.scf_iteration`<br>`runschema.calculation.Calculation.n_scf_iterations` |
| `rirpa.energies_RPA` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `statpt.atomic_info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `statpt.atomic_info.info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `statpt.options` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum` |
| `statpt.convergence` | Unmapped | — |
| `x_turbomole_nodename` | Unmapped | — |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `time` | Mapped | `runschema.run.TimeRun.date_start`<br>`runschema.run.TimeRun.date_end` |
| `module_aoforce` | Mapped | `runschema.run.Run.calculation` |
| `module_ccsdf12` | Mapped | `runschema.run.Run.calculation` |
| `module_dscf` | Mapped | `runschema.run.Run.calculation` |
| `module_escf` | Mapped | `runschema.run.Run.calculation` |
| `module_freeh` | Mapped | `runschema.run.Run.calculation` |
| `module_grad` | Mapped | `runschema.run.Run.calculation` |
| `module_pnoccsd` | Mapped | `runschema.run.Run.calculation` |
| `module_ricc2` | Mapped | `runschema.run.Run.calculation` |
| `module_ridft` | Mapped | `runschema.run.Run.calculation` |
| `module_rirpa` | Mapped | `runschema.run.Run.calculation` |
| `module_statpt` | Mapped | `runschema.run.Run.calculation` |
| `module_run` | Mapped | `runschema.run.Run.system`<br>`runschema.run.Run.method`<br>`runschema.run.Run.calculation` |
