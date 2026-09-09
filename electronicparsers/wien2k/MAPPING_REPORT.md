<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## WIEN2k / In0Parser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `xc_functional` | Mapped | `runschema.method.Method.dft.xc_functional.exchange.name`<br>`runschema.method.Method.dft.xc_functional.correlation.name`<br>`runschema.method.Method.dft.xc_functional.hybrid.name`<br>`runschema.method.Method.dft.xc_functional.contributions.name` |
| `fft` | Unmapped | — |

## WIEN2k / In1Parser

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## WIEN2k / StructParser

**Summary:** 5 mapped, 7 unmapped quantities (41.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `lattice` | Unmapped | — |
| `lattice.nonequiv_atoms` | Unmapped | — |
| `lattice.lattice` | Unmapped | — |
| `lattice.calc_mode` | Unmapped | — |
| `lattice.lattice_constants` | Mapped | `runschema.system.System.atoms.lattice_vectors` |
| `lattice.unit` | Mapped | `runschema.system.System.atoms.lattice_vectors` |
| `atom` | Unmapped | — |
| `atom.positions` | Mapped | `runschema.system.System.atoms.positions` |
| `atom.atom_name` | Mapped | `runschema.calculation.Calculation.dos_electronic.species_projected.atom_label` |
| `atom.NPT` | Unmapped | — |
| `atom.R0` | Unmapped | — |
| `atom.Z` | Mapped | `runschema.system.System.atoms.labels` |

## WIEN2k / IncParser

**Summary:** 0 mapped, 4 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `one_atom` | Unmapped | — |
| `one_atom.occupancies` | Unmapped | — |
| `one_atom.n_quantum_numbers` | Unmapped | — |
| `one_atom.kappas` | Unmapped | — |

## WIEN2k / In2Parser

**Summary:** 1 mapped, 3 unmapped quantities (25.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `switch` | Unmapped | — |
| `emin` | Unmapped | — |
| `smearing` | Mapped | `runschema.method.Method.electronic.smearing.kind`<br>`runschema.method.Method.electronic.smearing.width` |
| `gmax` | Unmapped | — |

## WIEN2k / DosParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `labels` | Mapped | `runschema.calculation.Calculation.dos_electronic.total.value`<br>`runschema.calculation.Calculation.dos_electronic.species_projected.value` |
| `data` | Mapped | `runschema.calculation.Calculation.dos_electronic.energies`<br>`runschema.calculation.Calculation.dos_electronic.total.value`<br>`runschema.calculation.Calculation.dos_electronic.species_projected.value` |

## WIEN2k / OutParser

**Summary:** 8 mapped, 51 unmapped quantities (13.56% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `version` | Mapped | `runschema.run.Program.version` |
| `start_date` | Mapped | `runschema.run.Run.time_run.date_start` |
| `iteration` | Mapped | `runschema.run.Run.calculation.scf_iteration` |
| `iteration.NATO` | Unmapped | — |
| `iteration.NATO.nr_of_independent_atoms` | Unmapped | — |
| `iteration.NATO.total_atoms` | Unmapped | — |
| `iteration.NATO.system_name` | Unmapped | — |
| `iteration.POT` | Unmapped | — |
| `iteration.POT.potential_option` | Unmapped | — |
| `iteration.LAT` | Unmapped | — |
| `iteration.LAT.lattice_const` | Unmapped | — |
| `iteration.VOL` | Unmapped | — |
| `iteration.VOL.unit_cell_volume_bohr3` | Unmapped | — |
| `iteration.VOL.spinpolarization` | Mapped | `runschema.method.Method.electronic.n_spin_channels` |
| `iteration.RKM` | Unmapped | — |
| `iteration.RKM.matrix_size` | Unmapped | — |
| `iteration.RKM.LOs` | Unmapped | — |
| `iteration.RKM.rkm` | Unmapped | — |
| `iteration.KPT` | Unmapped | — |
| `iteration.KPT.nr_kpts` | Unmapped | — |
| `iteration.GAP` | Unmapped | — |
| `iteration.GAP.ene_gap` | Unmapped | — |
| `iteration.NOE` | Unmapped | — |
| `iteration.NOE.noe` | Unmapped | — |
| `iteration.FER` | Unmapped | — |
| `iteration.FER.energy_reference_fermi` | Mapped | `runschema.calculation.ScfIteration.energy.fermi`<br>`runschema.calculation.Calculation.energy.fermi` |
| `iteration.GMA` | Unmapped | — |
| `iteration.GMA.cutoff` | Unmapped | — |
| `iteration.POSi` | Unmapped | — |
| `iteration.POSi.atom_mult` | Unmapped | — |
| `iteration.POSi.position` | Unmapped | — |
| `iteration.CHAi` | Unmapped | — |
| `iteration.CHAi.tot_val_charge_cell` | Unmapped | — |
| `iteration.SUM` | Unmapped | — |
| `iteration.SUM.energy_sum_eigenvalues` | Mapped | `runschema.calculation.ScfIteration.energy.sum_eigenvalues.value` |
| `iteration.RTOi` | Unmapped | — |
| `iteration.NTO` | Unmapped | — |
| `iteration.NTO.tot_int_charge_nm` | Unmapped | — |
| `iteration.NTOi` | Unmapped | — |
| `iteration.NTOi.tot_charge_in_sphere_nm` | Unmapped | — |
| `iteration.DTOi` | Unmapped | — |
| `iteration.DTOi.tot_diff_charge` | Unmapped | — |
| `iteration.DIS` | Unmapped | — |
| `iteration.DIS.charge_distance` | Unmapped | — |
| `iteration.CTO` | Unmapped | — |
| `iteration.CTO.tot_int_charge` | Unmapped | — |
| `iteration.CTOi` | Unmapped | — |
| `iteration.CTOi.tot_charge_in_sphere` | Unmapped | — |
| `iteration.NECi` | Unmapped | — |
| `iteration.MMINT` | Unmapped | — |
| `iteration.MMINT.mmint` | Unmapped | — |
| `iteration.MMIi` | Unmapped | — |
| `iteration.MMIi.mmi` | Unmapped | — |
| `iteration.MMTOT` | Unmapped | — |
| `iteration.MMTOT.mmtot` | Unmapped | — |
| `iteration.ENE` | Unmapped | — |
| `iteration.ENE.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy.total.value`<br>`runschema.calculation.Calculation.energy.total.value` |
| `iteration.FORi` | Unmapped | — |
| `iteration.FGLi` | Mapped | `runschema.calculation.Calculation.forces.total.value` |
