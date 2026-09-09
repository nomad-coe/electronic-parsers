<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## Wannier90 / WOutParser

**Summary:** 20 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `version` | Mapped | `runschema.run.Program.version` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `reciprocal_lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors_reciprocal`<br>`runschema.calculation.BandStructure.reciprocal_cell` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `structure.labels` | Mapped | `runschema.system.Atoms.labels` |
| `structure.positions` | Mapped | `runschema.system.Atoms.positions` |
| `k_mesh` | Mapped | `runschema.method.KMesh.n_points`<br>`runschema.method.KMesh.grid`<br>`runschema.method.KMesh.points` |
| `k_mesh.n_points` | Mapped | `runschema.method.KMesh.n_points` |
| `k_mesh.grid` | Mapped | `runschema.method.KMesh.grid` |
| `k_mesh.k_points` | Mapped | `runschema.method.KMesh.points` |
| `Nwannier` | Mapped | `runschema.method.Wannier.n_projected_orbitals` |
| `Nband` | Mapped | `runschema.method.Wannier.n_bands` |
| `Niter` | Mapped | `runschema.method.Wannier.is_maximally_localized` |
| `conv_tol` | Mapped | `runschema.method.Wannier.convergence_tolerance_max_localization` |
| `energy_windows` | Mapped | `runschema.method.Wannier.energy_window_outer`<br>`runschema.method.Wannier.energy_window_inner` |
| `energy_windows.outer` | Mapped | `runschema.method.Wannier.energy_window_outer` |
| `energy_windows.inner` | Mapped | `runschema.method.Wannier.energy_window_inner` |
| `n_k_segments` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `div_first_k_segment` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `band_segments_points` | Mapped | `runschema.calculation.BandEnergies.kpoints` |

## Wannier90 / WInParser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `energy_fermi` | Unmapped | — |
| `projections` | Mapped | `runschema.system.AtomsGroup.label`<br>`runschema.system.AtomsGroup.atom_indices`<br>`runschema.system.AtomsGroup.n_atoms`<br>`runschema.method.AtomParameters.n_orbitals`<br>`runschema.method.AtomParameters.orbitals` |

## Wannier90 / HrParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `degeneracy_factors` | Mapped | `runschema.calculation.HoppingMatrix.n_wigner_seitz_points`<br>`runschema.calculation.HoppingMatrix.degeneracy_factors` |
| `hoppings` | Mapped | `runschema.calculation.HoppingMatrix.value`<br>`runschema.calculation.Energy.fermi`<br>`runschema.calculation.Energy.highest_occupied` |
