<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## FHI-aims / FHIAimsControlParser

**Summary:** 3 mapped, 16 unmapped quantities (15.79% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `x_fhi_aims_controlIn_charge` | Unmapped | — |
| `x_fhi_aims_controlIn_hse_unit` | Unmapped | — |
| `x_fhi_aims_controlIn_hybrid_xc_coeff` | Unmapped | — |
| `x_fhi_aims_controlIn_MD_time_step` | Unmapped | — |
| `k_grid` | Unmapped | — |
| `k_offset` | Unmapped | — |
| `occupation_type` | Mapped | `runschema.method.Smearing.kind`<br>`runschema.method.Smearing.width` |
| `x_fhi_aims_controlIn_override_relativity` | Unmapped | — |
| `relativistic` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_accuracy_rho` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_accuracy_eev` | Unmapped | — |
| `threshold_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `x_fhi_aims_controlIn_sc_accuracy_forces` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_accuracy_stress` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_iter_limit` | Unmapped | — |
| `x_fhi_aims_controlIn_spin` | Unmapped | — |
| `x_fhi_aims_controlIn_verbatim_writeout` | Unmapped | — |
| `xc` | Unmapped | — |
| `species` | Mapped | `runschema.method.BasisSetContainer.native_tier` |

## FHI-aims / FHIAimsOutParser

**Summary:** 75 mapped, 20 unmapped quantities (78.95% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `structure.labels` | Mapped | `runschema.system.Atoms.labels` |
| `structure.positions` | Mapped | `runschema.system.Atoms.positions` |
| `structure.positions` | Mapped | `runschema.system.Atoms.positions` |
| `structure.velocities` | Mapped | `runschema.system.Atoms.velocities` |
| `eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.occupations` |
| `eigenvalues.kpoints` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `eigenvalues.occupation_eigenvalue` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `date_time` | Mapped | `runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.Calculation.time_physical` |
| `self_consistency.energy_components` | Mapped | `runschema.calculation.Energy` |
| `self_consistency.forces` | Unmapped | — |
| `self_consistency.stress_tensor` | Mapped | `runschema.calculation.Stress.total` |
| `self_consistency.pressure` | Mapped | `runschema.calculation.Thermodynamics.pressure` |
| `self_consistency.scf_convergence` | Mapped | `runschema.calculation.Energy.change` |
| `self_consistency.humo` | Unmapped | — |
| `self_consistency.lumo` | Unmapped | — |
| `self_consistency.fermi_level` | Mapped | `runschema.calculation.Energy.fermi` |
| `self_consistency.fermi_level` | Mapped | `runschema.calculation.Energy.fermi` |
| `self_consistency.time_calculation` | Mapped | `runschema.calculation.ScfIteration.time_calculation` |
| `self_consistency` | Mapped | `runschema.calculation.ScfIteration` |
| `self_consistency` | Mapped | `runschema.calculation.ScfIteration` |
| `self_consistency.scf_convergence` | Mapped | `runschema.calculation.Energy.change` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `energy` | Mapped | `runschema.calculation.Energy` |
| `energy_components` | Mapped | `runschema.calculation.Energy` |
| `energy_xc` | Mapped | `runschema.calculation.Energy.xc` |
| `forces` | Mapped | `runschema.calculation.Forces.free` |
| `forces_raw` | Mapped | `runschema.calculation.ForcesEntry.value_raw` |
| `time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation` |
| `total_dos_files` | Mapped | `runschema.calculation.Dos.total` |
| `atom_projected_dos_files` | Mapped | `runschema.calculation.Dos.atom_projected`<br>`runschema.calculation.Dos.orbital_projected` |
| `species_projected_dos_files` | Mapped | `runschema.calculation.Dos.species_projected`<br>`runschema.calculation.Dos.orbital_projected` |
| `vdW_TS` | Mapped | `runschema.method.Electronic.van_der_waals_method` |
| `vdW_TS.kind` | Mapped | `runschema.calculation.EnergyEntry.kind` |
| `vdW_TS.atom_hirshfeld` | Unmapped | — |
| `converged` | Mapped | `runschema.calculation.Calculation.calculation_converged` |
| `md_run` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.thermodynamic_ensemble`<br>`simulationworkflowschema.molecular_dynamics.ThermostatParameters.thermostat_type` |
| `md_timestep` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.integration_timestep` |
| `md_simulation_time` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.n_steps` |
| `md_temperature` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters.reference_temperature` |
| `md_thermostat_mass` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters.coupling_constant`<br>`simulationworkflowschema.molecular_dynamics.ThermostatParameters.effective_mass` |
| `md_thermostat_units` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters.coupling_constant` |
| `md_calculation_info` | Mapped | `runschema.calculation.Calculation.step`<br>`runschema.calculation.Calculation.time`<br>`runschema.calculation.Calculation.temperature`<br>`runschema.calculation.Energy` |
| `md_system_info` | Mapped | `runschema.system.Atoms.velocities` |
| `md_system_info.positions` | Unmapped | — |
| `md_system_info.velocities` | Mapped | `runschema.system.Atoms.velocities` |
| `version` | Mapped | `runschema.run.Program.version` |
| `x_fhi_aims_program_compilation_date` | Unmapped | — |
| `x_fhi_aims_program_compilation_time` | Unmapped | — |
| `compilation_host` | Mapped | `runschema.run.Program.compilation_host` |
| `cpu1_start` | Mapped | `runschema.run.TimeRun.cpu1_start` |
| `wall_start` | Mapped | `runschema.run.TimeRun.wall_start` |
| `raw_id` | Mapped | `runschema.run.Run.raw_id` |
| `x_fhi_aims_number_of_tasks` | Unmapped | — |
| `x_fhi_aims_parallel_task_nr` | Unmapped | — |
| `x_fhi_aims_parallel_task_host` | Unmapped | — |
| `fhi_aims_files` | Unmapped | — |
| `array_size_parameters` | Mapped | `runschema.method.Electronic.n_spin_channels` |
| `x_fhi_aims_controlInOut_hse_unit` | Unmapped | — |
| `x_fhi_aims_controlInOut_hybrid_xc_coeff` | Mapped | `runschema.method.Functional.parameters`<br>`runschema.method.Functional.weight` |
| `k_grid` | Mapped | `runschema.method.KMesh.grid` |
| `x_fhi_aims_controlInOut_MD_time_step` | Unmapped | — |
| `x_fhi_aims_controlInOut_relativistic` | Mapped | `runschema.method.Electronic.relativity_method` |
| `x_fhi_aims_controlInOut_relativistic` | Mapped | `runschema.method.Electronic.relativity_method` |
| `x_fhi_aims_controlInOut_relativistic_threshold` | Unmapped | — |
| `x_fhi_aims_controlInOut_xc` | Mapped | `runschema.method.XCFunctional`<br>`runschema.method.Functional.name` |
| `petukhov` | Unmapped | — |
| `x_fhi_aims_controlInOut_xc` | Mapped | `runschema.method.XCFunctional`<br>`runschema.method.Functional.name` |
| `x_fhi_aims_controlInOut_xc` | Mapped | `runschema.method.XCFunctional`<br>`runschema.method.Functional.name` |
| `band_segment_points` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.occupations` |
| `species` | Unmapped | — |
| `control_inout` | Mapped | `runschema.method.AtomParameters` |
| `control_inout.species` | Mapped | `runschema.method.AtomParameters.charge`<br>`runschema.method.AtomParameters.mass`<br>`runschema.method.AtomParameters.label`<br>`runschema.method.HubbardKanamoriModel.orbital`<br>`runschema.method.HubbardKanamoriModel.u_effective`<br>`runschema.method.HubbardKanamoriModel.double_counting_correction` |
| `control_in_verbatim` | Unmapped | — |
| `control_in_verbatim.md_controlin` | Unmapped | — |
| `gw_flag` | Mapped | `runschema.method.GW.type` |
| `anacon_type` | Mapped | `runschema.method.GW.analytical_continuation` |
| `gw_analytical_continuation` | Unmapped | — |
| `k_grid` | Mapped | `runschema.method.KMesh.grid` |
| `freq_grid_type` | Mapped | `runschema.method.FrequencyMesh.sampling_method` |
| `n_freq` | Mapped | `runschema.method.FrequencyMesh.n_points` |
| `frequency_data` | Mapped | `runschema.method.FrequencyMesh.points` |
| `frozen_core` | Unmapped | — |
| `n_states_gw` | Mapped | `runschema.method.GW.n_states` |
| `gw_self_consistency` | Mapped | `runschema.calculation.ScfIteration` |
| `gw_eigenvalues` | Mapped | `runschema.calculation.BandEnergies.value_ks`<br>`runschema.calculation.BandEnergies.value_qp`<br>`runschema.calculation.BandEnergies.value_exchange`<br>`runschema.calculation.BandEnergies.value_correlation`<br>`runschema.calculation.BandEnergies.value_ks_xc`<br>`runschema.calculation.BandEnergies.occupations` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `lattice_vectors_reciprocal` | Mapped | `runschema.system.Atoms.lattice_vectors_reciprocal` |
| `full_scf` | Mapped | `runschema.calculation.Calculation` |
| `geometry_optimization` | Mapped | `runschema.calculation.Calculation` |
| `molecular_dynamics` | Mapped | `runschema.calculation.Calculation` |
| `timing` | Mapped | `runschema.calculation.Calculation.time_physical` |
| `timing.total_time` | Mapped | `runschema.calculation.Calculation.time_physical` |
