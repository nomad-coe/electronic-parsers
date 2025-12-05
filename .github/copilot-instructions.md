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

```yaml
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
    - program  # name, version
    - time_run  # timing information

  method:
    - electronic.method  # DFT, HF, GW, etc.
    - dft.xc_functional  # XC functional for DFT codes
    - basis_set  # type, cutoff
    - k_mesh  # k-point sampling
    - scf  # SCF parameters
    - smearing  # occupation smearing
    - pseudopotential  # pseudopotential info
    # Add other method components as applicable

  system:
    - atoms  # positions, species, lattice_vectors, periodic
    - symmetry  # optional: space group

  calculation:
    # Energy components (list what the parser extracts)
    - energy.total
    - energy.free
    - energy.kinetic
    # Add other energy components as applicable

    # Forces and stress
    - forces.total  # if parser extracts forces
    - stress.total  # if parser extracts stress

    # Convergence
    - scf_iteration  # if parser tracks SCF

    # Electronic structure
    - band_structure_electronic  # if parser extracts band structure
    - dos_electronic  # if parser extracts DOS
    - eigenvalues  # band energies

    # Other properties
    - charges  # if charge analysis available
    - vibrational_frequencies  # if phonons/vibrations
    - thermodynamics  # temperature, pressure

  workflow:
    - single_point  # all parsers
    - geometry_optimization  # if supported
    - molecular_dynamics  # if supported
    - phonon  # if supported
    # Add other workflow types as applicable

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
2. Analyze the parser implementation to identify:
   - Which runschema sections are populated
   - What properties are extracted
   - Special capabilities or unique features
3. Use the YAML schema above as a template
4. Focus on runschema terminology, not code-specific names

### When Updating Existing Parsers

1. If a parser gains new capabilities, update its `FEATURES.yml`
2. Add new runschema sections to `runschema_capabilities`
3. Document new special features
4. Keep descriptions concise and standardized

### Best Practices

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
