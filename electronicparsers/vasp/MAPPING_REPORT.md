<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## VASP / vasprun.xml

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

The `vasprun.xml` content is read by `RunFileParser`, which subclasses `nomad.parsing.file_parser.FileParser` and drives a custom `xml.sax` handler (`RunXmlContentHandler`). It declares no `Quantity(...)` objects; `RunContentParser` addresses the parsed tree by XPath-like string keys rather than named quantities, so there is no declarative quantity list to report.

## VASP / OUTCAR

**Summary:** 26 mapped, 3 unmapped quantities (89.66% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `calculation` | Mapped | `calculation` |
| `calculation.scf_iteration` | Mapped | `calculation.scf_iteration` |
| `calculation.scf_iteration.energy_total` | Mapped | `calculation.scf_iteration.energy.free` |
| `calculation.scf_iteration.energy_entropy0` | Mapped | `calculation.scf_iteration.energy.total` |
| `calculation.scf_iteration.energy_T0` | Mapped | `calculation.scf_iteration.energy.total_t0` |
| `calculation.scf_iteration.energy_components` | Mapped | `calculation.scf_iteration.energy.correction_hartree`<br>`calculation.scf_iteration.energy.xc`<br>`calculation.scf_iteration.energy.exchange`<br>`calculation.scf_iteration.energy.sum_eigenvalues` |
| `calculation.scf_iteration.time` | Mapped | `calculation.scf_iteration.time_calculation`<br>`calculation.scf_iteration.time_physical` |
| `calculation.energies` | Mapped | `calculation.energy` |
| `calculation.energies.energy_total` | Mapped | `calculation.energy.free` |
| `calculation.energies.energy_entropy0` | Mapped | `calculation.energy.total` |
| `calculation.energies.energy_T0` | Mapped | `calculation.energy.total_t0` |
| `calculation.stress` | Mapped | `calculation.stress.total` |
| `calculation.positions_forces` | Mapped | `calculation.forces.total`<br>`system.atoms.positions` |
| `calculation.lattice_vectors` | Mapped | `system.atoms.lattice_vectors` |
| `calculation.converged` | Unmapped | — |
| `calculation.fermi_energy` | Unmapped | — |
| `calculation.eigenvalues` | Mapped | `calculation.eigenvalues`<br>`calculation.band_structure_electronic` |
| `calculation.convergence` | Mapped | `calculation.single_configuration_calculation_converged` |
| `calculation.time` | Mapped | `calculation.time_calculation`<br>`calculation.time_physical` |
| `header` | Mapped | `run.program.version`<br>`run.program.name`<br>`run.time_run.date_start`<br>`run.program.compilation_datetime` |
| `parameters` | Mapped | `method.electrons_representation.basis_set.cutoff`<br>`method.electrons_representation.native_tier` |
| `ions_per_type` | Mapped | `system.atoms.labels`<br>`method.atom_parameters` |
| `species` | Mapped | `method.atom_parameters.label`<br>`method.atom_parameters.atom_number` |
| `kpoints` | Mapped | `method.k_mesh.points`<br>`method.k_mesh.weights` |
| `nbands` | Unmapped | — |
| `lattice_vectors` | Mapped | `system.atoms.lattice_vectors` |
| `positions` | Mapped | `system.atoms.positions` |
| `response_functions` | Mapped | `method.gw.type`<br>`method.frequency_mesh` |
| `response_functions.input_parameters` | Mapped | `method.gw.type`<br>`method.frequency_mesh` |

## VASP / POTCAR

**Summary:** 4 mapped, 0 unmapped quantities (100.00% coverage).

The `PotParser` (`TextParser`) reads pseudopotential headers from `POTCAR` (or, via `OutcarContentParser`, from `OUTCAR`). Its output is consumed in `parse_method`, populating the `Pseudopotential` and `AtomParameters` sections.

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `pseudopotential` | Mapped | `method.atom_parameters.pseudopotential` |
| `pseudopotential.title` | Mapped | `method.atom_parameters.pseudopotential.name`<br>`method.atom_parameters.pseudopotential.xc_functional_name` |
| `pseudopotential.flag` | Mapped | `method.atom_parameters.pseudopotential.type` |
| `pseudopotential.number` | Mapped | `method.atom_parameters.pseudopotential.cutoff`<br>`method.atom_parameters.mass`<br>`method.atom_parameters.n_valence_electrons` |
