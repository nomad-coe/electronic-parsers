# GitHub Copilot Instructions for NOMAD Parser Development

## Overview

This document provides guidance for GitHub Copilot when working with NOMAD electronic structure parsers. Each parser extracts computational results from simulation output files and maps them to NOMAD's unified runschema.

**IMPORTANT**: Before merging any parser changes (especially new features), ensure the parser's `FEATURES.yml` file is updated to reflect new capabilities and that these changes are reviewed. The exact `FEATURES.yml` requirements to be enforced are stated below.

## Parser Feature Documentation

Each parser has a `FEATURES.yml` file in its directory that documents its capabilities using standardized runschema terminology. These files serve as a reference for:
- Understanding what data each parser extracts
- Identifying which runschema sections are populated
- Recognizing special features and capabilities
- Maintaining consistency across parser implementations

### File Location

Parser feature files are located at:
```
electronicparsers/{parser_name}/FEATURES.yml
```

### Editing Guidelines

**IMPORTANT**: When editing FEATURES.yml files:
- Always add a `metadata` section at the top with:
  - `last_updated`: Current timestamp (YYYY-MM-DD format)
  - `updated_by`: The model (i.e. YOU) that made the edits (e.g., "GitHub Copilot", "Claude Sonnet 4.5", "GPT-4", etc.)
- The model name should be retained in the file to track which AI assisted with the documentation
- Do NOT annotate every line with the model name, only include it in the metadata section
- Update the timestamp each time the file is modified
- Place string type values in duoble quotation marks

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

## YAML Schema for FEATURES.yml

### Supported File Formats

**IMPORTANT**: The `supported_file_formats` section lists ALL possible file formats the simulation code MAY produce, not necessarily all formats that are currently supported by the parser.

Each format MUST include:
- `name`: The file format name
- `supported`: true/false (whether the parser can handle this format)
- `source`: filepath:class.method pointing to the implementation (filepath from project root, specify the lowest level: method if possible)
- `notes`: Optional brief explanation (e.g., "Fully supported", "Format exists but not parsed")

**Why source is required:**
1. **Traceability**: Easy verification of documented capabilities
2. **Catching hallucinations**: Prevents documenting non-existent features

### Runschema Capabilities

**IMPORTANT**: Every claimed capability MUST include a source reference pointing to the implementation: filepath:class.method (from project root, lowest level possible).

Each capability entry includes:
- `capability`: The runschema section/property name
- `source`: filepath:class.method pointing to the implementation

**Why source is required:**
1. **Traceability**: Easy verification of documented capabilities
2. **Catching hallucinations**: Prevents documenting non-existent features

### YAML Template

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
    - name: "vasprun.xml"
      supported: true
      notes: "Fully supported"
      source: "electronicparsers/vasp/parser.py:VASPParser.init_parser"
    - name: "OUTCAR"
      supported: true
      notes: "Fully supported"
      source: "electronicparsers/vasp/parser.py:VASPParser.init_parser"

runschema_capabilities:
  run:
    - capability: program  # name, version
      source: "electronicparsers/vasp/parser.py:VASPParser.parse"
    - capability: time_run  # timing information
      source: "electronicparsers/vasp/parser.py:VASPParser.parse"

  method:
    - capability: electronic.method  # DFT, HF, GW, etc.
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_method"
    - capability: dft.xc_functional  # XC functional for DFT codes
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_method"
    - capability: basis_set  # type, cutoff
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_method"
    - capability: k_mesh  # k-point sampling
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_kpoints"
    - capability: gw  # GW approximation
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_gw"
    # Add other method components as applicable with sources

  system:
    - capability: atoms  # positions, species, lattice_vectors, periodic
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_configurations"

  calculation:
    # Energy components (list what the parser extracts)
    - capability: energy.total
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_configurations"
    - capability: energy.free
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_configurations"

    # Electronic structure
    - capability: eigenvalues
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_configurations"
    - capability: dos_electronic
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_configurations"

  workflow:
    - capability: single_point
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_workflow"
    - capability: geometry_optimization
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_workflow"
    - capability: molecular_dynamics
      source: "electronicparsers/vasp/parser.py:VASPParser.parse_workflow"
    # Add other workflow types as applicable with sources

special_features:
  # List parser-specific advanced capabilities
  - "Feature description 1"
  - "Feature description 2"

notes:
  # Optional: Additional implementation notes
  - "Note 1"
  - "Note 2"
```

## Guidelines for Maintaining Feature Files

### When Adding New Parsers

1. Create `FEATURES.yml` in the parser directory
2. Add metadata section with current date and your model name
3. Analyze the parser implementation to identify:
   - Which runschema sections are populated
   - What properties are extracted
   - Special capabilities or unique features
4. Use the YAML schema above as a template
5. Focus on runschema terminology, not code-specific names

### When Updating Existing Parsers

1. Update the `metadata` section with current date and your model name
2. Add new runschema sections to `runschema_capabilities`
3. Document new special features
4. Keep descriptions concise and standardized

### Best Practices

- Always update metadata when editing
- Use runschema terminology consistently across all feature files
- List only capabilities that are actually implemented
- Group related capabilities logically
- Include parser-specific features in `special_features`
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
