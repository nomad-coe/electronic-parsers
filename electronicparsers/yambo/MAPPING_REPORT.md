<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## YAMBO / parser.py :: MainfileParser

The quantities below are listed in source declaration order. Dotted prefixes reflect
the lexical `sub_parser` nesting. The shared quantity lists `io_quantities`,
`energies_quantities`, `qp_properties_quantity` and `module_quantities` are each
declared once but reused under several parents; they are reported once at their point
of declaration.

**Summary:** 12 mapped, 58 unmapped quantities (17.14% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `io_quantities.key_value` | Unmapped | — |
| `io_quantities.file` | Unmapped | — |
| `io_quantities.sn` | Unmapped | — |
| `energies_quantities.fermi` | Mapped | `runschema.calculation.Calculation.energy.fermi` |
| `energies_quantities.conduction` | Mapped | `runschema.calculation.Calculation.energy.lowest_unoccupied` |
| `energies_quantities.valence` | Mapped | `runschema.calculation.Calculation.energy.highest_occupied` |
| `energies_quantities.valence_conduction` | Mapped | `runschema.calculation.Calculation.energy.highest_occupied`<br>`runschema.calculation.Calculation.energy.lowest_unoccupied` |
| `energies_quantities.x_yambo_filled_bands` | Unmapped | — |
| `energies_quantities.x_yambo_empty_bands` | Unmapped | — |
| `energies_quantities.x_yambo_electronic_temperature` | Unmapped | — |
| `energies_quantities.x_yambo_bosonic_temperature` | Unmapped | — |
| `energies_quantities.x_yambo_finite_temperature_mode` | Unmapped | — |
| `energies_quantities.x_yambo_electronic_density` | Unmapped | — |
| `energies_quantities.states_summary` | Unmapped | — |
| `energies_quantities.x_yambo_indirect_gaps` | Unmapped | — |
| `energies_quantities.x_yambo_direct_gaps` | Unmapped | — |
| `energies_quantities.x_yambo_indirect_gap` | Unmapped | — |
| `energies_quantities.x_yambo_direct_gap` | Unmapped | — |
| `energies_quantities.x_yambo_direct_gap_kpoint` | Unmapped | — |
| `energies_quantities.x_yambo_indirect_gap_kpoints` | Unmapped | — |
| `qp_properties` | Unmapped | — |
| `qp_properties.qp_energy` | Unmapped | — |
| `qp_properties.qp_energy.band` | Mapped | `runschema.calculation.BandEnergies.value_qp`<br>`runschema.calculation.BandEnergies.value_ks`<br>`runschema.calculation.BandEnergies.qp_linearization_prefactor` |
| `qp_properties.qp_energy.kpoint` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `qp_properties.output` | Unmapped | — |
| `module_quantities.dipoles` | Unmapped | — |
| `module_quantities.dipoles.input` | Unmapped | — |
| `module_quantities.dipoles.output` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.output` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.x_yambo_plane_waves_vxc` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.x_yambo_plane_waves_exs` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.x_yambo_mesh_size` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.energy_xc` | Mapped | `runschema.calculation.Calculation.energy.xc.value` |
| `module_quantities.local_xc_nonlocal_fock.corrections` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.corrections.band` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.corrections.band_sp` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.hf_occupations` | Unmapped | — |
| `module_quantities.dynamic_dielectric_matrix` | Unmapped | — |
| `module_quantities.dynamic_dielectric_matrix.output` | Unmapped | — |
| `module_quantities.dynamic_dielectric_matrix.x_yambo_mesh_size` | Unmapped | — |
| `module_quantities.bare_xc` | Unmapped | — |
| `module_quantities.bare_xc.output` | Unmapped | — |
| `module_quantities.bare_xc.xc_hf_dft` | Unmapped | — |
| `module_quantities.bare_xc.xc_hf_dft.band` | Unmapped | — |
| `module_quantities.bare_xc.hf_occupations` | Unmapped | — |
| `module_quantities.dyson` | Unmapped | — |
| `module_quantities.dyson.g0w0` | Unmapped | — |
| `module_quantities.dyson.g0w0.x_yambo_bands_range` | Unmapped | — |
| `module_quantities.dyson.g0w0.x_yambo_g_damping` | Unmapped | — |
| `module_quantities.dyson.g0w0.x_yambo_mesh_size` | Unmapped | — |
| `module_quantities.dyson.g0w0.input` | Unmapped | — |
| `version` | Mapped | `runschema.run.Program.version` |
| `hash` | Unmapped | — |
| `build` | Unmapped | — |
| `date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `cpu_files_io` | Unmapped | — |
| `cpu_files_io.parameters` | Unmapped | — |
| `cpu_files_io.input` | Unmapped | — |
| `core_variables_setup` | Unmapped | — |
| `core_variables_setup.energies_occupations` | Unmapped | — |
| `core_variables_setup.energies_occupations.eigenenergies` | Unmapped | — |
| `core_variables_setup.energies_occupations.eigenenergies.energies` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `core_variables_setup.energies_occupations.eigenenergies.kpoints` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `core_variables_setup.energies_occupations.eigenenergies.kpoints_weights` | Mapped | `runschema.calculation.BandEnergies.kpoints_weights` |
| `transferred_momenta` | Unmapped | — |
| `transferred_momenta.input` | Unmapped | — |
| `transferred_momenta.qpoints` | Unmapped | — |
| `transferred_momenta.module` | Unmapped | — |
| `module` | Unmapped | — |

## YAMBO / parser.py :: InputParser

**Summary:** 0 mapped, 2 unmapped quantities (0.00% coverage).

The `InputParser` is instantiated in `YamboParser.__init__` but never invoked during
`parse()`; none of its quantities are read.

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `key_value` | Unmapped | — |
| `key_block` | Unmapped | — |

## YAMBO / parser.py :: NetCDFParser

Coverage: Not available.

`NetCDFParser` is a custom `FileParser` subclass with no `Quantity` declarations. It
reads all variables directly from the NetCDF file via the `netCDF4.Dataset` handler in
`parse()`, exposing them by their raw NetCDF variable names rather than through
declarative `Quantity` objects.
