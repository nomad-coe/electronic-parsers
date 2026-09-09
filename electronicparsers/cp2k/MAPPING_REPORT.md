<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## CP2K / trajectory files (XYZ)

Parser class `XYZTrajParser` (`TextParser`). Reads CP2K `*-pos-1.xyz` / trajectory files via the custom XYZ reader wrapped by `TrajParser`.

**Summary:** 1 mapped, 2 unmapped quantities (33.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `trajectory` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `energy` | Unmapped | — |
| `iter` | Unmapped | — |

## CP2K / forces file

Parser class `ForceParser` (`TextParser`). Reads the `*-1_<frame>.xyz` atomic-forces print file resolved by `get_forces`.

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom_forces` | Mapped | `runschema.calculation.Forces.total` |

## CP2K / main .out

Parser class `CP2KOutParser` (`TextParser`). Parses the main CP2K text output. Nested `sub_parser` quantities are shown with dotted paths. The `scf_wavefunction_optimization_quantities` and `quickstep_quantities` blocks are single `Quantity` object lists reused across several sub-parsers (`single_point`, `geometry_optimization`, `molecular_dynamics`, `qs_dftb`); each such quantity is listed once at its canonical location.

**Summary:** 43 mapped, 46 unmapped quantities (48.31% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `dbcsr` | Unmapped | — |
| `program` | Unmapped | — |
| `cp2k` | Mapped | `runschema.run.Program.version`<br>`runschema.run.Program.compilation_host` |
| `global` | Unmapped | — |
| `restart` | Unmapped | — |
| `restart.filename` | Unmapped | — |
| `restart.quantities` | Unmapped | — |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `quickstep` | Mapped | drives `runschema.system.System`, `runschema.method.Method`, `runschema.calculation.Calculation` |
| `quickstep.dft` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.dft_u` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.mp2` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.rpa` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.functional` | Unmapped | — |
| `quickstep.vdw` | Mapped | `runschema.method.Method.van_der_waals_method` |
| `quickstep.qs` | Mapped | `runschema.method.BasisSet.cutoff` |
| `quickstep.atomic_kind_information` | Mapped | drives `runschema.method.AtomParameters`, `runschema.method.BasisSetAtomCentered` |
| `quickstep.atomic_kind_information.atom` | Mapped | drives `runschema.method.AtomParameters`, `runschema.method.BasisSetAtomCentered` |
| `quickstep.atomic_kind_information.atom.kind_label` | Mapped | `runschema.method.AtomParameters.label` |
| `quickstep.atomic_kind_information.atom.kind_number_of_atoms` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.kind_basis_set_name` | Mapped | `runschema.method.BasisSetAtomCentered.name` |
| `quickstep.atomic_kind_information.atom.basis_set_norm_type` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_orbital_shell_sets` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_orbital_shells` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_primitive_cartesian_functions` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_cartesian_basis_functions` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_spherical_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers` | Unmapped | — |
| `quickstep.total_maximum_numbers.atomic_kinds` | Unmapped | — |
| `quickstep.total_maximum_numbers.atoms` | Unmapped | — |
| `quickstep.total_maximum_numbers.shell_sets` | Unmapped | — |
| `quickstep.total_maximum_numbers.shells` | Unmapped | — |
| `quickstep.total_maximum_numbers.primitive_cartesian_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.cartesian_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.spherical_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.orbital_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.local_part_of_gth_pseudopotential` | Unmapped | — |
| `quickstep.total_maximum_numbers.non_local_part_of_gth_pseudopotential` | Unmapped | — |
| `quickstep.atomic_coordinates` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `quickstep.scf_parameters` | Mapped | drives `runschema.method.Scf` |
| `quickstep.scf_parameters.n_max_iteration` | Mapped | `runschema.method.Scf.n_max_iteration` |
| `quickstep.scf_parameters.threshold_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `quickstep.scf_parameters.md` | Unmapped | — |
| `quickstep.single_point` | Mapped | drives `runschema.calculation.Calculation` (via `scf_wavefunction_optimization_quantities`) |
| `quickstep.single_point.iteration` | Mapped | `runschema.calculation.ScfIteration`<br>`runschema.calculation.Energy.change` |
| `quickstep.single_point.converged` | Unmapped | — |
| `quickstep.single_point.cube_file` | Unmapped | — |
| `quickstep.single_point.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `quickstep.single_point.atom_forces` | Mapped | `runschema.calculation.Forces.total` |
| `quickstep.single_point.stress_tensor` | Mapped | `runschema.calculation.Stress.total` |
| `quickstep.single_point.stress_tensor_one_third_of_trace` | Unmapped | — |
| `quickstep.single_point.stress_tensor_determinant` | Unmapped | — |
| `quickstep.single_point.stress_eigenvalues_eigenvectors` | Unmapped | — |
| `quickstep.single_point.hartree_energy` | Unmapped | — |
| `quickstep.single_point.exchange_correlation_energy` | Mapped | `runschema.calculation.Energy.xc` |
| `quickstep.single_point.electronic_kinetic_energy` | Mapped | `runschema.calculation.Energy.kinetic_electronic` |
| `quickstep.single_point.total_energy` | Unmapped | — |
| `quickstep.single_point.fermi_energy` | Mapped | `runschema.calculation.Energy.fermi`<br>`runschema.calculation.Energy.highest_occupied` |
| `quickstep.geometry_optimization` | Mapped | drives `simulationworkflowschema.GeometryOptimization` |
| `quickstep.geometry_optimization.method` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method` |
| `quickstep.geometry_optimization.self_consistent` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.geometry_optimization.optimization_step` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.geometry_optimization.optimization_step.step` | Mapped | `runschema.calculation.Calculation.step` (frame index) |
| `quickstep.geometry_optimization.optimization_step.information` | Unmapped | — |
| `quickstep.geometry_optimization.optimization_step.self_consistent` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.molecular_dynamics` | Mapped | drives `runschema.calculation.Calculation`, `simulationworkflowschema.MolecularDynamics` |
| `quickstep.molecular_dynamics.initial` | Unmapped | — |
| `quickstep.molecular_dynamics.md_par` | Unmapped | — |
| `quickstep.molecular_dynamics.md_ini` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.molecular_dynamics.md_step.ensemble_type` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.step` | Mapped | `runschema.calculation.Calculation.step` |
| `quickstep.molecular_dynamics.md_step.time` | Mapped | `runschema.calculation.Calculation.time` |
| `quickstep.molecular_dynamics.md_step.conserved_quantity` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cpu_time` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.energy_drift` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.potential_energy` | Mapped | `runschema.calculation.Energy.potential`<br>`runschema.calculation.Energy.total` |
| `quickstep.molecular_dynamics.md_step.kinetic_energy` | Mapped | `runschema.calculation.Energy.kinetic`<br>`runschema.calculation.Energy.total` |
| `quickstep.molecular_dynamics.md_step.temperature` | Mapped | `runschema.calculation.Calculation.temperature` |
| `quickstep.molecular_dynamics.md_step.pressure` | Mapped | `runschema.calculation.Calculation.pressure` |
| `quickstep.molecular_dynamics.md_step.barostat_temperature` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.volume` | Mapped | `runschema.calculation.Calculation.volume` |
| `quickstep.molecular_dynamics.md_step.cell_length_instantaneous` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cell_length_average` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cell_angle_instantaneous` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cell_angle_average` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.self_consistent` | Mapped | drives `runschema.calculation.Calculation` |
| `spin_polarized` | Mapped | `runschema.calculation.Dos.spin_channel` (spin-channel count of `dos_electronic`) |
| `qs_dftb` | Mapped | drives `runschema.system.System`, `runschema.method.Method`, `runschema.calculation.Calculation` (reuses `quickstep_quantities`) |

## CP2K / PDOS files

Parser class `CP2KPDOSParser` (`DataTextParser`). Reads `*.pdos` projected-DOS files, whose histograms are Gaussian-convoluted in `parse_dos`.

**Summary:** 2 mapped, 1 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom_kind` | Mapped | `runschema.calculation.DosValues.atom_label`<br>`runschema.calculation.DosValues.atom_index` |
| `orbitals` | Mapped | `runschema.calculation.DosValues.orbital` |
| `iter` | Unmapped | — |

## CP2K / input file (.inp / .restart)

Parser class `InpParser` (`FileParser`).

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## CP2K / trajectory / cell / velocities loader

Parser class `TrajParser` (`FileParser`). Wraps `XYZTrajParser`, ASE and MDAnalysis readers to load positions/velocities frames.

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.
