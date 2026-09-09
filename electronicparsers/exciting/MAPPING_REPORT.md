<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
# exciting parser mapping report

The exciting parser is an imperative NOMAD parser built around several declarative
file-parser classes (subclasses of `TextParser`/`XMLParser`). Each `##` section below
lists every `Quantity(...)` declared in one such class, marks whether the imperative
`ExcitingParser` code writes it into the normalized runschema, and names the runschema
target for the mapped ones. Quantities that only ever populate code-specific
`x_exciting_*` metainfo are reported as `Unmapped`.

## Exciting / INFO.OUT

Parsed by `ExcitingInfoParser`. Consumed by `parse_method`, `parse_system`, `parse_scc`,
`parse_configurations` and their helpers.

`ExcitingInfoParser` also appends quantities in loops with a variable `name` argument
sourced from the `_system_keys_mapping`, `_method_keys_mapping`,
`_miscellaneous_keys_mapping` and `_convergence_keys_mapping` dictionaries; these are listed
below as individual rows at their declaration position (the system/method keys inside
`initialization`, the miscellaneous/convergence keys inside `groundstate.scf_iteration`).

**Summary:** 37 mapped, 43 unmapped quantities (46.25% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `program.version` |
| `hash_id` | Mapped | `program.version_internal` |
| `initialization.lattice_vectors` | Mapped | `system.atoms.lattice_vectors` |
| `initialization.lattice_vectors_reciprocal` | Mapped | `system.atoms.lattice_vectors_reciprocal` |
| `initialization.x_exciting_unit_cell_volume` | Unmapped | — |
| `initialization.x_exciting_brillouin_zone_volume` | Unmapped | — |
| `initialization.x_exciting_number_of_atoms` | Unmapped | — |
| `initialization.x_exciting_spin_treatment` | Mapped | `method.electronic.n_spin_channels` |
| `initialization.x_exciting_number_of_bravais_lattice_symmetries` | Unmapped | — |
| `initialization.x_exciting_number_of_crystal_symmetries` | Unmapped | — |
| `initialization.kpoint_grid` | Mapped | `method.k_mesh.grid` |
| `initialization.kpoint_offset` | Mapped | `method.k_mesh.offset` |
| `initialization.x_exciting_number_kpoints` | Unmapped | — |
| `initialization.x_exciting_rgkmax` | Unmapped | — |
| `initialization.x_exciting_species_rtmin` | Unmapped | — |
| `initialization.x_exciting_gkmax` | Unmapped | — |
| `initialization.x_exciting_gmaxvr` | Unmapped | — |
| `initialization.x_exciting_gvector_size` | Unmapped | — |
| `initialization.x_exciting_gvector_total` | Unmapped | — |
| `initialization.x_exciting_lmaxapw` | Unmapped | — |
| `initialization.x_exciting_nuclear_charge` | Unmapped | — |
| `initialization.x_exciting_electronic_charge` | Unmapped | — |
| `initialization.x_exciting_core_charge_initial` | Unmapped | — |
| `initialization.x_exciting_valence_charge_initial` | Unmapped | — |
| `initialization.x_exciting_wigner_radius` | Unmapped | — |
| `initialization.x_exciting_empty_states` | Unmapped | — |
| `initialization.x_exciting_valence_states` | Unmapped | — |
| `initialization.x_exciting_hamiltonian_size` | Unmapped | — |
| `initialization.x_exciting_pw` | Unmapped | — |
| `initialization.x_exciting_lo` | Unmapped | — |
| `initialization.smearing_kind` | Mapped | `method.electronic.smearing.kind` |
| `initialization.smearing_width` | Mapped | `method.electronic.smearing.width` |
| `initialization.species.number` | Unmapped | — |
| `initialization.species.symbol` | Mapped | `system.atoms.labels` |
| `initialization.species.file` | Unmapped | — |
| `initialization.species.name` | Unmapped | — |
| `initialization.species.nuclear_charge` | Unmapped | — |
| `initialization.species.electronic_charge` | Unmapped | — |
| `initialization.species.atomic_mass` | Unmapped | — |
| `initialization.species.muffin_tin_radius` | Unmapped | — |
| `initialization.species.radial_points` | Unmapped | — |
| `initialization.species.positions_format` | Unmapped | — |
| `initialization.species.positions` | Mapped | `system.atoms.positions` |
| `initialization.potential_mixing` | Unmapped | — |
| `initialization.xc_functional.type` | Mapped | `method.dft.xc_functional` |
| `initialization.xc_functional.name_reference` | Mapped | `method.dft.xc_functional.name`<br>`method.dft.xc_functional.reference` |
| `initialization.xc_functional.parameters` | Unmapped | — |
| `groundstate.scf_iteration.energy_total` | Mapped | `calculation.scf_iteration.energy.total` |
| `groundstate.scf_iteration.energy_contributions` | Mapped | `calculation.scf_iteration.energy` |
| `groundstate.scf_iteration.x_exciting_dos_fermi` | Unmapped | — |
| `groundstate.scf_iteration.charge_contributions` | Mapped | `calculation.scf_iteration.charges` |
| `groundstate.scf_iteration.moment_contributions` | Unmapped | — |
| `groundstate.scf_iteration.x_exciting_gap` | Unmapped | — |
| `groundstate.scf_iteration.time_physical` | Mapped | `calculation.scf_iteration.time_physical` |
| `groundstate.scf_iteration.x_exciting_effective_potential_convergence` | Unmapped | — |
| `groundstate.scf_iteration.x_exciting_energy_convergence` | Mapped | `method.scf.threshold_energy_change` |
| `groundstate.scf_iteration.x_exciting_charge_convergence` | Unmapped | — |
| `groundstate.scf_iteration.x_exciting_IBS_force_convergence` | Unmapped | — |
| `groundstate.final` | Mapped | `calculation.energy.total` |
| `groundstate.atomic_positions.positions_format` | Mapped | `system.atoms.positions` |
| `groundstate.atomic_positions.symbols` | Mapped | `system.atoms.labels` |
| `groundstate.atomic_positions.positions` | Mapped | `system.atoms.positions` |
| `groundstate.forces` | Mapped | `calculation.forces.total` |
| `structure_optimization.optimization_step.atomic_positions.positions_format` | Mapped | `system.atoms.positions` |
| `structure_optimization.optimization_step.atomic_positions.symbols` | Mapped | `system.atoms.labels` |
| `structure_optimization.optimization_step.atomic_positions.positions` | Mapped | `system.atoms.positions` |
| `structure_optimization.optimization_step.forces` | Mapped | `calculation.forces.total` |
| `structure_optimization.optimization_step.step` | Unmapped | — |
| `structure_optimization.optimization_step.method` | Unmapped | — |
| `structure_optimization.optimization_step.n_scf_iterations` | Unmapped | — |
| `structure_optimization.optimization_step.force_convergence` | Mapped | `workflow2.method.convergence_tolerance_force_maximum` |
| `structure_optimization.optimization_step.energy_total` | Mapped | `calculation.energy.total` |
| `structure_optimization.optimization_step.time_calculation` | Mapped | `calculation.time_calculation` |
| `structure_optimization.final` | Mapped | `calculation.energy.total` |
| `structure_optimization.atomic_positions.positions_format` | Mapped | `system.atoms.positions` |
| `structure_optimization.atomic_positions.symbols` | Mapped | `system.atoms.labels` |
| `structure_optimization.atomic_positions.positions` | Mapped | `system.atoms.positions` |
| `structure_optimization.forces` | Mapped | `calculation.forces.total` |
| `hybrids` | Mapped | `calculation.energy.total` |
| `total_time` | Mapped | `calculation.time_physical` |

## Exciting / bandstructure.xml

Parsed by `BandstructureXMLParser` (an `XMLParser`). It declares no `Quantity(...)`
objects; band energies, k-points and segment labels are read directly from XML attributes
through its `parse(key)` method and written to `calculation.band_structure_electronic` in
`_parse_bandstructure`.

**Summary:** 0 mapped, 0 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |

## Exciting / dos.xml

Parsed by `DOSXMLParser` (an `XMLParser`). It declares no `Quantity(...)` objects; total
and partial DOS are read directly from XML attributes through its `parse(key)` method and
written to `calculation.dos_electronic` in `_parse_dos`.

**Summary:** 0 mapped, 0 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |

## Exciting / EIGVAL.OUT

Parsed by `ExcitingEigenvalueParser`. Consumed by `_parse_eigenvalues`.

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `k_points` | Mapped | `calculation.eigenvalues.kpoints` |
| `eigenvalues_occupancies` | Mapped | `calculation.eigenvalues.energies`<br>`calculation.eigenvalues.occupations` |

## Exciting / EVALQP.DAT

Parsed by `ExcitingEvalqpParser`. Consumed by `_parse_evalqp`.

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `kpoints_eigenvalues` | Mapped | `calculation.eigenvalues.energies`<br>`calculation.eigenvalues.kpoints`<br>`calculation.eigenvalues.value_exchange`<br>`calculation.eigenvalues.value_correlation`<br>`calculation.eigenvalues.value_xc_potential`<br>`calculation.eigenvalues.qp_linearization_prefactor` |

## Exciting / GW_INFO.OUT

Parsed by `GWInfoParser`. Consumed by `parse_gw`.

**Summary:** 3 mapped, 2 unmapped quantities (60.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `frequency_data` | Unmapped | — |
| `fermi_energy` | Mapped | `calculation.energy.fermi` |
| `direct_band_gap` | Mapped | `calculation.band_gap.value` |
| `fundamental_band_gap` | Mapped | `calculation.band_gap.value` |
| `optical_band_gap` | Unmapped | — |

## Exciting / FERMISURF.bxsf

Parsed by `ExcitingFermiSurfaceBxsfParser`. Consumed by `_parse_fermisurface`, which
writes only into the code-specific `x_exciting_section_fermi_surface`.

**Summary:** 0 mapped, 3 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `fermi_energy` | Unmapped | — |
| `band_parameters` | Unmapped | — |
| `fermi_surface` | Unmapped | — |

## Exciting / LINENGY.OUT

Parsed by `LinengyParser`. This parser is instantiated but its results are not consumed by
any imperative `parse_*` method, so none of its quantities reach the runschema.

**Summary:** 0 mapped, 12 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `species_block` | Unmapped | — |
| `species_block.element` | Unmapped | — |
| `species_block.apw_line` | Unmapped | — |
| `species_block.apw_line.lo_index` | Unmapped | — |
| `species_block.apw_line.l` | Unmapped | — |
| `species_block.apw_line.order` | Unmapped | — |
| `species_block.apw_line.e_param` | Unmapped | — |
| `species_block.lo_line` | Unmapped | — |
| `species_block.lo_line.lo_index` | Unmapped | — |
| `species_block.lo_line.l` | Unmapped | — |
| `species_block.lo_line.order` | Unmapped | — |
| `species_block.lo_line.e_param` | Unmapped | — |

## Exciting / species file (Si.xml)

Parsed by `SpeciesParser`. Consumed by `_parse_species`, which builds
`method.atom_parameters` and `method.electrons_representation` basis-set sections. The
block-matching quantities carry a nested `key_val` quantity whose name is the dynamic
attribute `self.flag` (`'key_val'`); `to_dict`/`_supplant` folds its attribute key/value
pairs into the parent block dict that `_parse_species` reads. Each `key_val` is listed at
its declaration position with the same status as its parent block.

**Summary:** 12 mapped, 6 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `sp` | Mapped | `method.atom_parameters.atom_number`<br>`method.atom_parameters.label`<br>`method.atom_parameters.mass` |
| `sp.key_val` | Mapped | `method.atom_parameters.atom_number`<br>`method.atom_parameters.label`<br>`method.atom_parameters.mass` |
| `muffinTin` | Mapped | `method.electrons_representation.basis_set.radius`<br>`method.electrons_representation.basis_set.radius_lin_spacing` |
| `muffinTin.key_val` | Mapped | `method.electrons_representation.basis_set.radius`<br>`method.electrons_representation.basis_set.radius_lin_spacing` |
| `atomicState` | Unmapped | — |
| `atomicState.key_val` | Unmapped | — |
| `default` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `default.wf` | Unmapped | — |
| `default.wf.key_val` | Unmapped | — |
| `default.key_val` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `custom` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `custom.wf` | Unmapped | — |
| `custom.wf.key_val` | Unmapped | — |
| `custom.key_val` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo.wf` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo.wf.key_val` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo.l` | Mapped | `method.electrons_representation.basis_set.orbital` |

## Exciting / GW output (ExcitingGWOutParser)

Parsed by `ExcitingGWOutParser`. This class declares an empty quantity list
(`self._quantities = []`) and is not wired into `ExcitingParser`; GW output properties are
read via `GWInfoParser` instead.

**Summary:** 0 mapped, 0 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
