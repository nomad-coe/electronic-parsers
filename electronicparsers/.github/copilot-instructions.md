# GitHub Copilot Instructions for NOMAD Parser Development

## Overview

This document provides guidance for GitHub Copilot when working with NOMAD electronic structure parsers. Each parser extracts computational results from simulation output files and maps them to NOMAD's unified runschema.

## Parser Feature Documentation

Each parser has a `FEATURES.yml` file in its directory that documents its capabilities using standardized runschema terminology. These files serve as a reference for:
- Understanding what data each parser extracts
- Identifying which runschema sections are populated
- Recognizing special features and capabilities
- Maintaining consistency across parser implementations

### File Location

Parser feature files are located at:
```
{parser_name}/FEATURES.yml
```

### Editing Guidelines

**IMPORTANT**: When editing FEATURES.yml files:
- Always add a `metadata` section at the top with:
  - `last_updated`: Current timestamp (YYYY-MM-DD format)
  - `updated_by`: The model that made the edit (e.g., "Claude Sonnet 4.5", "GPT-4", etc.)
- The model name should be retained in the file to track which AI assisted with the documentation
- Do NOT annotate every line with the model name, only include it in the metadata section
- Update the timestamp each time the file is modified

Example metadata section:
```yaml
metadata:
  last_updated: "2025-12-05"
  updated_by: "Claude Sonnet 4.5"

parser:
  name: "VASP"
  ...
```

## NOMAD Runschema Terminology

The runschema is NOMAD's unified data model for computational materials science. It consists of hierarchical sections:

### 1. Run Section (`runschema.run`)

Top-level container for a complete calculation run.

**Key components:**
- `Program` - Software metadata (name, version, compilation_host)
- `TimeRun` - Execution timing (date_start, date_end, cpu/wall times)

### 2. Method Section (`runschema.method`)

Describes the computational methodology used.

**Key components:**

#### Electronic Structure Method
- `Method.electronic` - Electronic structure approach (DFT, HF, GW, MP2, CCSD, DMFT)
- `n_spin_channels` - 1 (unpolarized) or 2 (spin-polarized)
- `smearing` - Electron occupation smearing method
- `relativity_method` - Relativistic treatment
- `van_der_waals_method` - Dispersion corrections

#### DFT Specifics
- `DFT` with `XCFunctional` - Exchange-correlation functional
  - `exchange` - Exchange functional(s) (e.g., "GGA_X_PBE", "HYB_GGA_XC_HSE06")
  - `correlation` - Correlation functional(s) (e.g., "GGA_C_PBE", "LDA_C_PW")
  - `hybrid` - Hybrid functional components
  - Common functionals: LDA, PBE, PBE0, HSE06, B3LYP

#### Basis Sets
- `BasisSetContainer` with `BasisSet` - Basis set description
  - `type` - "plane waves", "gaussians", "numeric AOs", "Slater-type orbitals"
  - `cutoff` - Energy cutoff (for plane waves)
  - `native_tier` - Quality level (low/medium/high/tight)

#### K-point Sampling
- `KMesh` - Brillouin zone sampling (n_points, points, grid)

#### Self-Consistent Field
- `Scf` - SCF convergence parameters (threshold_energy_change, n_max_iteration)

#### Atom-Specific Parameters
- `AtomParameters` - Per-atom settings (mass, charge, pseudopotential info)
- `Pseudopotential` - Pseudopotential details (type: "norm conserving", "ultrasoft", "PAW")

#### Advanced Methods
- `HubbardKanamoriModel` - DFT+U parameters (Hubbard U, J values)
- `GW` - GW approximation settings (G0W0, scGW)
- `CoreHole` - Core hole spectroscopy

### 3. System Section (`runschema.system`)

Describes the atomic structure and configuration.

**Key components:**
- `System` - Complete atomic configuration
  - `Atoms` - Atomic structure (labels, positions, lattice_vectors, periodic, velocities)
  - `AtomsGroup` - Subsets of atoms (molecules, fragments)
  - `Symmetry` - Space group and symmetry operations
  - `Constraint` - Constrained atoms or geometric constraints

### 4. Calculation Section (`runschema.calculation`)

Contains results from a single-point calculation.

**Key components:**

#### Energy
- `Energy` with `EnergyEntry` - Energy values (total, free, kinetic, potential, xc, electrostatic, ewald, nuclear_repulsion, zero_point, fermi, highest_occupied, lowest_unoccupied)

#### Forces and Stress
- `Forces` with `ForcesEntry` - Atomic forces (total forces on N_atoms x 3)
- `Stress` with `StressEntry` - Stress tensor (3x3 matrix)

#### Thermodynamics
- `Thermodynamics` - Thermodynamic properties (pressure, temperature, enthalpy, entropy)

#### SCF Convergence
- `ScfIteration` - SCF convergence history (energy, time_physical, time_calculation)

#### Electronic Structure
- `BandEnergies` - Band energies/eigenvalues (energies [spin, kpoint, band], kpoints, occupations)
- `BandStructure` - Band structure along paths (segment)
- `Dos` with `DosValues` - Density of states (energies, total, atom_projected, orbital_projected)
- `BandGap` - Electronic band gap (value, type: "direct" or "indirect")

#### Charge Analysis
- `Charges` - Atomic charge analysis (value, analysis_method: "Mulliken", "Hirshfeld", "Bader")

#### Vibrational Properties
- `VibrationalFrequencies` - Phonon frequencies (value, intensities, raman_intensities)

#### Volumetric Data
- `Density` - Electron density on grid
- `Potential` - Potential on grid

### 5. Workflow Section (`simulationworkflowschema`)

Describes the type of calculation workflow.

**Workflow types:**

- **SinglePoint** - Basic single-point energy calculation
- **GeometryOptimization** - Structure relaxation to minimize forces
  - `GeometryOptimizationMethod` - method (BFGS, CG, FIRE, damped MD), convergence tolerances
- **MolecularDynamics** - Time-dependent simulation
  - `MolecularDynamicsMethod` - ensemble_type (NVE, NVT, NPT), timestep, ThermostatParameters, BarostatParameters
- **Phonon** - Vibrational/phonon calculation (DFPT or finite displacement)
- **GW** - Beyond-DFT GW calculation
- **BSE** - Bethe-Salpeter equation for excitations
- **DMFT** - Dynamical mean-field theory

## YAML Schema for FEATURES.yml

```yaml
metadata:
  last_updated: "YYYY-MM-DD"
  updated_by: "Model Name (e.g., Claude Sonnet 4.5)"

parser:
  name: "Parser Name"
  description: "Brief description"
  homepage: "https://..."
  mainfile_patterns:
    - "pattern1"
    - "pattern2"
  supported_file_formats:
    - "format1"
    - "format2"

runschema_capabilities:
  run:
    - program
    - time_run

  method:
    - electronic.method
    - dft.xc_functional
    - basis_set
    - k_mesh
    - scf
    - smearing
    - pseudopotential

  system:
    - atoms
    - symmetry

  calculation:
    - energy.total
    - energy.free
    - energy.kinetic
    - forces.total
    - stress.total
    - scf_iteration
    - band_structure_electronic
    - dos_electronic
    - eigenvalues
    - charges
    - vibrational_frequencies
    - thermodynamics

  workflow:
    - single_point
    - geometry_optimization
    - molecular_dynamics
    - phonon

special_features:
  - "Feature description 1"
  - "Feature description 2"

notes:
  - "Note 1"
  - "Note 2"
```

## Guidelines for Maintaining Feature Files

### When Adding New Parsers

1. Create `FEATURES.yml` in the parser directory
2. Add metadata section with current date and your model name
3. Analyze the parser implementation to identify capabilities
4. Use the YAML schema above as a template
5. Focus on runschema terminology, not code-specific names

### When Updating Existing Parsers

1. Update the `metadata` section with current date and your model name
2. Add new runschema sections to `runschema_capabilities`
3. Document new special features
4. Keep descriptions concise and standardized

### Best Practices

- Always update metadata when editing
- Use runschema terminology consistently
- List only capabilities that are actually implemented
- Group related capabilities logically
- Keep descriptions focused on "what" not "how"
- Reference official schema documentation for ambiguous cases

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

When working on parser code, Copilot can reference these feature files to:
- Suggest appropriate runschema sections for extracted data
- Recommend common patterns for similar properties
- Identify missing capabilities that should be implemented
- Ensure consistency with other parsers

To help Copilot understand your intent:
- Mention the parser name in comments
- Reference runschema sections explicitly
- Use standard property names from the schema
- Comment on what data you're extracting in runschema terms
