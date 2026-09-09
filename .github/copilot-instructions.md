# GitHub Copilot Instructions for NOMAD Parser Development

## Overview

This document provides guidance for GitHub Copilot when working with NOMAD electronic structure parsers. Each parser extracts computational results from simulation output files and maps them to NOMAD's unified runschema.

**IMPORTANT**: Before merging any parser changes (especially new features), ensure the parser's `MAPPING_REPORT.md` file is updated to reflect the current mapping coverage, and that these changes are reviewed. The exact `MAPPING_REPORT.md` requirements to be enforced are stated below.

## Parser Mapping Report

Each parser has a `MAPPING_REPORT.md` file in its directory that documents, per output file,
exactly which of the parser's declarative file-parser quantities are mapped into the normalized
runschema. This mirrors the programmatic report produced for the new-schema simulation parsers
(`FAIRmat-NFDI/nomad-parser-plugins-simulation`, `nomad-sim-parser mapping-report`); here the
legacy imperative parsers carry no declarative archive-mapper annotation, so the report is
produced by reading the parser code rather than auto-generated. The files serve as a reference for:
- Which file-parser quantities each parser exposes
- Which of them are actually written to the runschema archive (coverage), and where
- Where the gaps are (unmapped quantities), to prioritise future work

### File Location

Parser mapping reports are located at:
```
electronicparsers/{parser_name}/MAPPING_REPORT.md
```

A combined, repo-wide report at `docs/reference/parser_mapping_report.md` is the concatenation of
all per-parser fragments. It is maintained by hand (no build tooling): whenever you add or edit a
fragment, regenerate the combined file by concatenating the fragments in alphabetical order of
parser directory, e.g.

```bash
{ echo "# Electronic parser mapping report"; echo;
  for f in $(ls electronicparsers/*/MAPPING_REPORT.md | sort); do
    tail -n +2 "$f"; echo;   # drop each fragment's generated-by comment line
  done; } > docs/reference/parser_mapping_report.md
```

Treat the combined file as generated output: never hand-edit it — edit the fragment and rebuild it.

### Editing Guidelines

**IMPORTANT**: When editing `MAPPING_REPORT.md` files:
- Record model attribution in a single HTML comment at the top of the file:
  ```markdown
  <!-- generated-by: Claude Sonnet 4.5 | last_updated: 2026-09-09 -->
  ```
  Use YYYY-MM-DD for the date and the exact model name that made the edits (e.g.,
  "GitHub Copilot", "Claude Sonnet 4.5", "GPT-4"). Retain it so the assisting model is tracked.
  Do NOT annotate every row with the model name.
- Update the timestamp each time the file is modified.
- Every quantity name and every mapped target you write MUST be verifiable against the parser
  source (see the anti-hallucination rule below); do not invent entries.

## NOMAD Runschema Terminology

The runschema is NOMAD's unified data model for computational materials science. It consists of hierarchical sections:

### 1. Run Section (`runschema.run`)

Top-level container for a complete calculation run.

**Key components:**
- `Program` - Software metadata
  - `name` - Code name (e.g., "VASP", "CP2K")
  - `version` - Software version
  - `compilation_host` - Where compiled
- `TimeRun` - Execution timing
  - `date_start`, `date_end` - Timestamps
  - `cpu1_start`, `cpu1_end` - CPU time
  - `wall_start`, `wall_end` - Wall clock time

### 2. Method Section (`runschema.method`)

Describes the computational methodology used.

**Key components:**

#### Electronic Structure Method
- `Method.electronic` - Electronic structure approach
  - Values: "DFT", "HF", "GW", "MP2", "CCSD", "DMFT", etc.
  - `n_spin_channels` - 1 (unpolarized) or 2 (spin-polarized)
  - `smearing` - Electron occupation smearing method
  - `relativity_method` - Relativistic treatment
  - `van_der_waals_method` - Dispersion corrections

#### DFT Specifics
- `DFT` with `XCFunctional` - Exchange-correlation functional
  - `exchange` - Exchange functional(s)
    - Examples: "GGA_X_PBE", "HYB_GGA_XC_HSE06"
  - `correlation` - Correlation functional(s)
    - Examples: "GGA_C_PBE", "LDA_C_PW"
  - `hybrid` - Hybrid functional components
  - Common functionals: LDA, PBE, PBE0, HSE06, B3LYP

#### Basis Sets
- `BasisSetContainer` with `BasisSet` - Basis set description
  - `type` - Basis set type
    - "plane waves" - Plane wave expansion
    - "gaussians" - Gaussian-type orbitals
    - "numeric AOs" - Numerical atomic orbitals
    - "Slater-type orbitals" - Slater orbitals
  - `cutoff` - Energy cutoff (for plane waves)
  - `native_tier` - Quality level (low/medium/high/tight)

#### K-point Sampling
- `KMesh` - Brillouin zone sampling
  - `n_points` - Number of k-points
  - `points` - K-point coordinates
  - `grid` - Monkhorst-Pack grid dimensions

#### Self-Consistent Field
- `Scf` - SCF convergence parameters
  - `threshold_energy_change` - Energy convergence criterion
  - `n_max_iteration` - Maximum SCF iterations

#### Atom-Specific Parameters
- `AtomParameters` - Per-atom settings
  - `mass` - Atomic mass
  - `charge` - Atomic charge
  - Pseudopotential information

- `Pseudopotential` - Pseudopotential details
  - `type` - "norm conserving", "ultrasoft", "PAW"
  - `name` - Pseudopotential identifier

#### Advanced Methods
- `HubbardKanamoriModel` - DFT+U parameters
  - Hubbard U, J values for correlated electrons
- `GW` - GW approximation settings
  - G0W0, scGW, etc.
- `CoreHole` - Core hole spectroscopy

### 3. System Section (`runschema.system`)

Describes the atomic structure and configuration.

**Key components:**

- `System` - Complete atomic configuration
  - `Atoms` - Atomic structure
    - `labels` - Atomic symbols (e.g., ["Si", "Si", "O", "O"])
    - `positions` - Atomic coordinates in Cartesian (Å)
    - `lattice_vectors` - Unit cell vectors (3x3 matrix, Å)
    - `periodic` - Periodicity flags [x, y, z]
    - `velocities` - Atomic velocities (for MD)
  - `AtomsGroup` - Subsets of atoms (molecules, fragments)
  - `Symmetry` - Space group and symmetry operations
  - `Constraint` - Constrained atoms or geometric constraints

### 4. Calculation Section (`runschema.calculation`)

Contains results from a single-point calculation.

**Key components:**

#### Energy
- `Energy` with `EnergyEntry` - Energy values
  - `total` - Total energy (most common)
  - `free` - Free energy (Helmholtz)
  - `kinetic` - Kinetic energy
  - `potential` - Potential energy
  - `xc` - Exchange-correlation energy
  - `electrostatic` - Electrostatic/Coulomb energy
  - `ewald` - Ewald summation energy
  - `nuclear_repulsion` - Nuclear-nuclear repulsion
  - `zero_point` - Zero-point energy
  - `fermi` - Fermi energy
  - `highest_occupied` - HOMO energy
  - `lowest_unoccupied` - LUMO energy
  - Each entry has:
    - `value` - Energy value
    - `contributions` - Breakdown of components

#### Forces and Stress
- `Forces` with `ForcesEntry` - Atomic forces
  - `total` - Total forces on atoms (N_atoms x 3)
  - `value` - Force array
  - `contributions` - Force component breakdown

- `Stress` with `StressEntry` - Stress tensor
  - `total` - Total stress (3x3 matrix)
  - `value` - Stress tensor
  - `contributions` - Stress component breakdown

#### Thermodynamics
- `Thermodynamics` - Thermodynamic properties
  - `pressure` - Pressure
  - `temperature` - Temperature
  - `enthalpy` - Enthalpy
  - `entropy` - Entropy

#### SCF Convergence
- `ScfIteration` - SCF convergence history
  - `energy` - Energy per iteration
  - `time_physical` - Physical time (for MD)
  - `time_calculation` - Computation time

#### Electronic Structure
- `BandEnergies` - Band energies/eigenvalues
  - `energies` - Band energies [spin, kpoint, band]
  - `kpoints` - K-point coordinates
  - `occupations` - Band occupations

- `BandStructure` - Band structure along paths
  - `segment` - High-symmetry path segments
  - Each segment has energy and k-point arrays

- `Dos` with `DosValues` - Density of states
  - `energies` - Energy grid
  - `total` - Total DOS [spin, energy]
  - `atom_projected` - Atom-projected DOS [spin, atom, orbital, energy]
  - `orbital_projected` - Orbital-projected DOS

- `BandGap` - Electronic band gap
  - `value` - Gap value
  - `type` - "direct" or "indirect"

#### Charge Analysis
- `Charges` - Atomic charge analysis
  - `value` - Charges per atom
  - `analysis_method` - "Mulliken", "Hirshfeld", "Bader", etc.

#### Vibrational Properties
- `VibrationalFrequencies` - Phonon frequencies
  - `value` - Frequencies
  - `intensities` - IR intensities
  - `raman_intensities` - Raman intensities

#### Volumetric Data
- `Density` - Electron density on grid
- `Potential` - Potential on grid

### 5. Workflow Section (`simulationworkflowschema`)

Describes the type of calculation workflow.

**Workflow types:**

#### SinglePoint
Basic single-point energy calculation.

#### GeometryOptimization
Structure relaxation to minimize forces.
- `GeometryOptimizationMethod` - Optimization settings
  - `method` - Optimizer algorithm
    - "BFGS", "CG" (conjugate gradient), "FIRE", "damped MD"
  - `convergence_tolerance_force_maximum` - Force convergence
  - `convergence_tolerance_energy_difference` - Energy convergence
  - `convergence_tolerance_displacement_maximum` - Displacement convergence

#### MolecularDynamics
Time-dependent simulation.
- `MolecularDynamicsMethod` - MD settings
  - `ensemble_type` - Statistical ensemble
    - "NVE" (microcanonical), "NVT" (canonical), "NPT" (isothermal-isobaric)
  - `timestep` - Integration timestep
  - `ThermostatParameters` - Temperature control
    - `type` - "Nose-Hoover", "Berendsen", "Langevin", etc.
    - `target_temperature` - Target temperature
  - `BarostatParameters` - Pressure control (NPT only)

#### Phonon
Vibrational/phonon calculation.
- Finite displacement or DFPT methods
- Phonon band structure and DOS

#### GW
Beyond-DFT GW calculation.

#### BSE
Bethe-Salpeter equation for excitations.

#### DMFT
Dynamical mean-field theory.

## Markdown Mapping-Report Format

A `MAPPING_REPORT.md` contains **one section per declarative file-parser class**. Its shape is
identical to the auto-generated report of the new-schema simulation parsers, so the two can be
read side by side.

### Template

```markdown
<!-- generated-by: Claude Sonnet 4.5 | last_updated: 2026-09-09 -->
## <Code> / <FILE>

**Summary:** {mapped} mapped, {unmapped} unmapped quantities ({coverage:.2f}% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `quantity_name` | Mapped | `runschema.target.path` |
| `x_code_specific_quantity` | Unmapped | — |
```

- **Heading** (`## <Code> / <FILE>`): the code name and the output file the class parses, e.g.
  `## Exciting / INFO.OUT`, `## VASP / vasprun.xml`. One heading per file-parser class; a parser
  that reads several files (e.g. exciting `INFO.OUT`, `EIGVAL.OUT`, band-structure XML) gets one
  section each, all in the same `MAPPING_REPORT.md`.
- **Summary line**: exact wording
  `**Summary:** {mapped} mapped, {unmapped} unmapped quantities ({coverage:.2f}% coverage).`,
  where `coverage = mapped / total * 100` with two decimals.
- **Left column (`File-parser quantity`)**: the `name=` of each `Quantity(...)` defined in the
  file-parser class, in declaration order. Use **dotted paths** for nested / sub-parser quantities
  (e.g. `dataset.results.eigenvalues`). Wrap every name in backticks.
- **Status**: `Mapped` if `parse()` (or a `parse_*` helper) writes the quantity into the
  normalized runschema, otherwise `Unmapped`. Code-specific `x_<code>_*` quantities that only land
  in the code-specific metainfo extension (never the normalized runschema) count as `Unmapped`.
- **Archive mapper source**: for a `Mapped` row, the runschema attribute path it feeds (e.g.
  `energy.total`, `atoms.positions`, `dos_electronic`) or the helper that consumes it; for an
  `Unmapped` row, an em dash `—`. Join multiple targets with `<br>`. Wrap paths in backticks.

### Skipped parsers

If a parser writes to the archive purely through custom imperative code and exposes **no**
declarative `Quantity` list to report on, do not fabricate a coverage number. Emit a single
section instead:

```markdown
## <Code>

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no
reportable file-parser quantities.
```

### Anti-hallucination rule (replaces the old `source:` field)

There is no validator; correctness is a review responsibility, so self-check every entry against
the parser source before committing:
1. **Every** left-column quantity name MUST correspond to a real `Quantity(...)` in the parser's
   file-parser class. Confirm with a grep, e.g.
   `grep -nE "Quantity\(" electronicparsers/<code>/*.py`.
2. **Every** `Mapped` target MUST be a real runschema attribute path (cross-check against
   `packages/nomad-schema-plugin-run/runschema/`).
3. Do not omit quantities to inflate coverage: list every declared quantity, mapped or not —
   **including quantities whose `name` is built dynamically** (in a loop or from a dict/mapping,
   e.g. abinit's energy components, exciting's `x_exciting_*_convergence`). Resolve the runtime
   names and list each as its own row; do not skip them just because the name is not a string
   literal.

## Guidelines for Maintaining Mapping Reports

### Generation recipe (adding or regenerating a report)

1. Locate the declarative file-parser classes in the parser:
   `grep -nE "class .*\((TextParser|XMLParser)\)" electronicparsers/<code>/parser.py`.
2. For each class, enumerate every `Quantity(...)` including nested `sub_parser` / repeating
   quantities, and any quantities appended dynamically (loops, dict-driven names) → the left
   column, using dotted paths for nesting.
3. Read `parse()` / `parse_*` to decide, per quantity, whether it is written to the normalized
   runschema and to which target path → Status + Archive mapper source.
4. Compute `coverage = mapped / total * 100`; write the summary line and table.
5. Emit one `##` section per file-parser class; refresh the top-of-file `generated-by` comment.

### Best Practices

- Update the `generated-by` comment (model + date) on every edit.
- List every declared quantity — mapped and unmapped — never a curated subset.
- Prefer normalized runschema attribute paths in the source column; only fall back to a helper
  name when no single attribute path applies.
- Keep quantity names and target paths copy-exact against the source.
- Rebuild `docs/reference/parser_mapping_report.md` by concatenating the fragments (see the
  snippet under *File Location*) after editing any fragment.

## Schema Documentation References

- Main runschema: `packages/nomad-schema-plugin-run/runschema/`
  - `run.py` - Run section
  - `method.py` - Method section
  - `system.py` - System section
  - `calculation.py` - Calculation section
- Workflow schema: `packages/nomad-schema-plugin-simulation-workflow/simulationworkflowschema/`

## Common Patterns in Parser Implementation

### Energy Extraction Pattern
```python
sec_energy = calculation.Energy()
sec_energy.total = EnergyEntry(value=total_energy * ureg.eV)
sec_energy.free = EnergyEntry(value=free_energy * ureg.eV)
sec_calculation.energy = sec_energy
```

### Forces Extraction Pattern
```python
sec_forces = calculation.Forces()
sec_forces.total = ForcesEntry(value=forces_array * ureg.eV / ureg.angstrom)
sec_calculation.forces = sec_forces
```

### Band Structure Pattern
```python
sec_k_band = calculation.BandEnergies()
sec_k_band.energies = eigenvalues * ureg.eV  # [spin, kpoint, band]
sec_k_band.occupations = occupations
sec_k_band.kpoints = kpoint_coords
sec_calculation.band_structure_electronic.append(sec_k_band)
```

### Workflow Detection Pattern
```python
if self.is_geometry_optimization():
    workflow = GeometryOptimization()
    workflow.method = GeometryOptimizationMethod(
        method="BFGS",
        convergence_tolerance_force_maximum=1e-3 * ureg.eV / ureg.angstrom
    )
elif self.is_molecular_dynamics():
    workflow = MolecularDynamics()
    workflow.method = MolecularDynamicsMethod(
        ensemble_type="NVT",
        timestep=1.0 * ureg.fs
    )
```

## Usage with GitHub Copilot

When working on parser code, Copilot can reference these mapping reports to:
- Suggest appropriate runschema sections for extracted data
- Recommend common patterns for similar properties
- Identify unmapped quantities that should be wired into the runschema
- Ensure consistency with other parsers

To help Copilot understand your intent:
- Mention the parser name in comments
- Reference runschema sections explicitly
- Use standard property names from the schema
- Comment on what data you're extracting in runschema terms
