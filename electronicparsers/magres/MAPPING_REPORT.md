<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## Magres / MagresFileParser

**Summary:** 22 mapped, 18 unmapped quantities (55.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `lattice_units` | Unmapped | — |
| `atom_units` | Unmapped | — |
| `ms_units` | Unmapped | — |
| `efg_units` | Unmapped | — |
| `efg_local_units` | Unmapped | — |
| `efg_nonlocal_units` | Unmapped | — |
| `isc_units` | Unmapped | — |
| `isc_fc_units` | Unmapped | — |
| `isc_spin_units` | Unmapped | — |
| `isc_orbital_p_units` | Unmapped | — |
| `isc_orbital_d_units` | Unmapped | — |
| `sus_units` | Unmapped | — |
| `cutoffenergy_units` | Mapped | `runschema.method.BasisSet.cutoff` |
| `calculation` | Mapped | `runschema.run.Program.name`<br>`runschema.run.Program.version`<br>`runschema.method.Functional.name`<br>`runschema.method.BasisSet.cutoff`<br>`runschema.method.KMesh.grid`<br>`runschema.method.KMesh.offset` |
| `calculation.code` | Mapped | `runschema.run.Program.name` |
| `calculation.code_version` | Mapped | `runschema.run.Program.version` |
| `calculation.code_hgversion` | Unmapped | — |
| `calculation.code_platform` | Unmapped | — |
| `calculation.name` | Unmapped | — |
| `calculation.comment` | Unmapped | — |
| `calculation.xcfunctional` | Mapped | `runschema.method.Functional.name` |
| `calculation.cutoffenergy` | Mapped | `runschema.method.BasisSet.cutoff` |
| `calculation.pspot` | Unmapped | — |
| `calculation.kpoint_mp_grid` | Mapped | `runschema.method.KMesh.grid` |
| `calculation.kpoint_mp_offset` | Mapped | `runschema.method.KMesh.offset` |
| `atoms` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic`<br>`runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `atoms.lattice` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `atoms.symmetry` | Unmapped | — |
| `atoms.atom` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `magres` | Mapped | `runschema.calculation.MagneticShielding.value`<br>`runschema.calculation.ElectricFieldGradient.value`<br>`runschema.calculation.SpinSpinCoupling.reduced_value`<br>`runschema.calculation.MagneticSusceptibility.value` |
| `magres.ms` | Mapped | `runschema.calculation.MagneticShielding.atoms`<br>`runschema.calculation.MagneticShielding.value`<br>`runschema.calculation.MagneticShielding.isotropic_value` |
| `magres.efg` | Mapped | `runschema.calculation.ElectricFieldGradient.atoms`<br>`runschema.calculation.ElectricFieldGradient.contribution`<br>`runschema.calculation.ElectricFieldGradient.value` |
| `magres.efg_local` | Mapped | `runschema.calculation.ElectricFieldGradient.atoms`<br>`runschema.calculation.ElectricFieldGradient.contribution`<br>`runschema.calculation.ElectricFieldGradient.value` |
| `magres.efg_nonlocal` | Mapped | `runschema.calculation.ElectricFieldGradient.atoms`<br>`runschema.calculation.ElectricFieldGradient.contribution`<br>`runschema.calculation.ElectricFieldGradient.value` |
| `magres.isc` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_fc` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_orbital_p` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_orbital_d` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_spin` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.sus` | Mapped | `runschema.calculation.MagneticSusceptibility.scale_dimension`<br>`runschema.calculation.MagneticSusceptibility.value` |
