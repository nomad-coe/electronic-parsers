<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## FLEUR / XMLParser

**Summary:** 22 mapped, 10 unmapped quantities (68.75% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_fleur_precision` | Unmapped | — |
| `header.x_fleur_structure_class` | Unmapped | — |
| `header.x_fleur_additional_flags` | Unmapped | — |
| `start_time` | Mapped | `runschema.run.TimeRun.date_start` |
| `input` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.method.DFT.xc_functional` |
| `input.parameters` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.parameters.key_val` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.cell` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.positions` |
| `input.xc_functional` | Mapped | `runschema.method.DFT.xc_functional` |
| `input.species` | Mapped | `runschema.method.BasisSet.radius`<br>`runschema.method.BasisSet.spherical_harmonics_cutoff`<br>`runschema.method.BasisSet.radius_log_spacing`<br>`runschema.method.BasisSet.n_grid_points` |
| `input.species.key_val` | Mapped | `runschema.method.BasisSet.radius`<br>`runschema.method.BasisSet.spherical_harmonics_cutoff`<br>`runschema.method.BasisSet.radius_log_spacing`<br>`runschema.method.BasisSet.n_grid_points` |
| `input.atom` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `input.atom.species` | Mapped | `runschema.system.Atoms.labels` |
| `input.atom.position` | Mapped | `runschema.system.Atoms.positions` |
| `input.output_parameters` | Unmapped | — |
| `input.output_parameters.key_val` | Unmapped | — |
| `numerical_parameters` | Unmapped | — |
| `numerical_parameters.key_val` | Unmapped | — |
| `scf_iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_iteration.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `scf_iteration.energy_sum_eigenvalues` | Mapped | `runschema.calculation.Energy.sum_eigenvalues` |
| `scf_iteration.energy_x_fleur_density_coulomb_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_density_effective_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_charge_density_xc` | Unmapped | — |
| `scf_iteration.energy_free` | Mapped | `runschema.calculation.Energy.free` |
| `scf_iteration.energy_total_t0` | Mapped | `runschema.calculation.Energy.total_t0` |
| `scf_iteration.fermi` | Mapped | `runschema.calculation.Energy.fermi` |
| `scf_iteration.eigenvalues_kpts` | Mapped | `runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.energies` |
| `scf_iteration.eigenvalues_kpts.kpt` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `scf_iteration.eigenvalues_kpts.energies` | Mapped | `runschema.calculation.BandEnergies.energies` |

## FLEUR / OutParser

**Summary:** 21 mapped, 25 unmapped quantities (45.65% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_fleur_precision` | Unmapped | — |
| `header.x_fleur_with_inversion` | Unmapped | — |
| `header.x_fleur_with_soc` | Unmapped | — |
| `header.x_fleur_additional_flags` | Unmapped | — |
| `input` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.input_parameters` | Unmapped | — |
| `input.input_parameters.key_val` | Unmapped | — |
| `input.parameters` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.parameters.key_val` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `system` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.lattice_vectors`<br>`runschema.method.DFT.xc_functional` |
| `system.parameters` | Unmapped | — |
| `system.parameters.key_val` | Unmapped | — |
| `system.x_fleur_unit_cell_volume` | Unmapped | — |
| `system.x_fleur_unit_cell_volume_omega` | Unmapped | — |
| `system.exchange_correlation` | Mapped | `runschema.method.DFT.xc_functional` |
| `system.x_fleur_k_max` | Unmapped | — |
| `system.x_fleur_G_max` | Unmapped | — |
| `system.x_fleur_vol_interstitial` | Unmapped | — |
| `system.x_fleur_nr_of_atom_types` | Unmapped | — |
| `system.cell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `system.atoms` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `electronic` | Mapped | `runschema.method.Smearing.kind`<br>`runschema.method.Smearing.width` |
| `electronic.eigenvalues_parameters` | Unmapped | — |
| `electronic.eigenvalues_parameters.key_val` | Unmapped | — |
| `electronic.smearing` | Mapped | `runschema.method.Smearing.kind` |
| `electronic.width` | Mapped | `runschema.method.Smearing.width` |
| `electronic.x_fleur_nr_of_valence_electrons` | Unmapped | — |
| `electic_field_parameters` | Unmapped | — |
| `electic_field_parameters.x_fleur_tot_elec_charge` | Unmapped | — |
| `electic_field_parameters.x_fleur_tot_nucl_charge` | Unmapped | — |
| `scf_iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_iteration.energy_sum_eigenvalues` | Mapped | `runschema.calculation.Energy.sum_eigenvalues` |
| `scf_iteration.energy_x_fleur_density_coulomb_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_density_effective_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_charge_density_xc` | Unmapped | — |
| `scf_iteration.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `scf_iteration.energy_free` | Mapped | `runschema.calculation.Energy.free` |
| `scf_iteration.energy_total_t0` | Mapped | `runschema.calculation.Energy.total_t0` |
| `scf_iteration.forces` | Mapped | `runschema.calculation.Forces.total` |
| `scf_iteration.kpoints` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `scf_iteration.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `scf_iteration.fermi` | Mapped | `runschema.calculation.Energy.fermi` |
| `scf_iteration.x_fleur_n_occupied_states` | Unmapped | — |
| `scf_iteration.x_fleur_valence_charge` | Unmapped | — |
