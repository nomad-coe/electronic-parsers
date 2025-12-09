This is a NOMAD parser for [CP2K](https://www.cp2k.org/). It will read CP2K input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For CP2K please provide at least the files from this table if applicable to your
calculations (remember that you can provide more files if you want):

---

# CP2K Molecular Dynamics Output Format Documentation

## Overview

CP2K changed its molecular dynamics (MD) output format between versions 7.1 and 8.1. This document explains the semantics of the different output prefixes and provides examples from actual test files.

## Format Changes by Version

- **Old Format (CP2K ≤ 7.1)**: Uses `INITIAL|` prefix for MD parameters and initialization
- **New Format (CP2K ≥ 8.1)**: Uses `MD_PAR|`, `MD_INI|`, and `MD|` prefixes for different types of MD output

## Output Prefix Semantics

### MD_PAR| - MD Parameters (CP2K ≥ 8.1)

**Meaning:** Molecular dynamics protocol and input parameters

**Pattern:** `" MD_PAR| <property_name> [unit]  <value>"`

**Contains:**
- Ensemble type (NVE, NVT, NPT_F, etc.)
- Number of time steps
- Time step size
- Target temperature and pressure
- Print frequencies
- Output file names and formats

### MD_INI| - MD Initialization (CP2K ≥ 8.1)

**Meaning:** Initial state values at MD simulation start

**Pattern:** `" MD_INI| <property_name> [unit]  <value>"`

**Contains:**
- Initial potential and kinetic energy
- Initial temperature
- Initial cell volume, lengths, and angles
- Starting configuration properties

### MD| - MD Step Output (CP2K ≥ 8.1)

**Meaning:** Per-step molecular dynamics output

**Pattern:** `" MD| <property_name> [unit]  <instantaneous_value> <average_value>"`

**Contains:**
- Step number and time
- Conserved quantity
- CPU time per step
- Energy drift per atom
- Potential and kinetic energies (instantaneous and average)
- Temperature and pressure (instantaneous and average)
- Cell volume, lengths, and angles

## Regex Parsing

The parser uses the `md_extract` function (parser.py:442) with the following regex pattern:

```python
r' ?(?:MD|MD_PAR|MD_INI)\| (?P<key>.+?)(?: \[(?P<unit>.+)\])? {2,}(?P<value>.+)'
```

**Pattern breakdown:**
- `' ?'` - optional leading space
- `'(?:MD|MD_PAR|MD_INI)\|'` - prefix: MD|, MD_PAR|, or MD_INI|
- `' (?P<key>.+?)'` - property name (captured as 'key')
- `'(?: \[(?P<unit>.+)\])?'` - optional unit in brackets (captured as 'unit')
- `' {2,}'` - two or more spaces (separator)
- `'(?P<value>.+)'` - value (captured as 'value')

**Example:** `" MD_PAR| Time step [fs]  0.5"` → key='Time step', unit='fs', value='0.5'

## Examples from Test Files

### Old Format: CP2K Version 2.6.2 (2015)

**Test file:** `tests/data/cp2k/molecular_dynamics/H2O-32.out`

**Lines 726-731:**
```
INITIAL POTENTIAL ENERGY[hartree]     =                     -0.343303964710E+02
INITIAL KINETIC ENERGY[hartree]       =                      0.712533452240E-02
INITIAL TEMPERATURE[K]                =                                 300.000
INITIAL VOLUME[bohr^3]                =                      0.645469325907E+04
INITIAL CELL LNTHS[bohr]   =      0.1861909E+02   0.1861909E+02   0.1861909E+02
INITIAL CELL ANGLS[deg]    =      0.9000000E+02   0.9000000E+02   0.9000000E+02
```

### New Format: CP2K Version 2023.1

**Test file:** `tests/data/cp2k/molecular_dynamics/H2O-32-2023.1.out`

#### MD_PAR| Output (Lines 454-465)
```
MD_PAR| Molecular dynamics protocol (MD input parameters)
MD_PAR| Ensemble type                                                       NVE
MD_PAR| Number of time steps                                                 10
MD_PAR| Time step [fs]                                                 0.500000
MD_PAR| Temperature [K]                                              300.000000
MD_PAR| Temperature tolerance [K]                                      0.000000
MD_PAR| Print MD information every                                    1 step(s)
MD_PAR| File type   Print frequency [steps]                          File names
MD_PAR| Coordinates          1                                 H2O-32-pos-1.xyz
MD_PAR| Velocities           1                                 H2O-32-vel-1.xyz
MD_PAR| Energies             1                                    H2O-32-1.ener
MD_PAR| Dump                20                                 H2O-32-1.restart
```

#### MD_INI| Output (Lines 649-657)
```
MD_INI| MD initialization
MD_INI| Potential energy [hartree]                          -0.343303968832E+02
MD_INI| Kinetic energy [hartree]                             0.712533452240E-02
MD_INI| Temperature [K]                                              300.000000
MD_INI| Cell volume [bohr^3]                                 6.454693259067E+03
MD_INI| Cell volume [ang^3]                                  9.564868456940E+02
MD_INI| Cell lengths [bohr]      1.86190936E+01  1.86190936E+01  1.86190936E+01
MD_INI| Cell lengths [ang]       9.85280000E+00  9.85280000E+00  9.85280000E+00
MD_INI| Cell angles [deg]        9.00000000E+01  9.00000000E+01  9.00000000E+01
```

#### MD| Output (Lines 732-740)
```
MD| ***************************************************************************
MD| Step number                                                               1
MD| Time [fs]                                                          0.500000
MD| Conserved quantity [hartree]                            -0.343232465525E+02
MD| ---------------------------------------------------------------------------
MD|                                          Instantaneous             Averages
MD| CPU time per MD step [s]                     21.680633            21.680633
MD| Energy drift per atom [K]           0.131552476993E+01   0.000000000000E+00
MD| Potential energy [hartree]         -0.343297798065E+02  -0.343297798065E+02
```

## Parser Implementation

The parser handles both formats (parser.py:1201-1218):

```python
# Combine MD settings from old format (scf_parameters/md) and
# new format (molecular_dynamics/md_par+md_ini)
md_settings_old = to_dict(
    self.out_parser.get(self._calculation_type, {})
    .get('scf_parameters', {})
    .get('md', [])
)
md_settings_new_par = to_dict(
    self.out_parser.get(self._calculation_type, {})
    .get('molecular_dynamics', {})
    .get('md_par', [])
)
md_settings_new_ini = to_dict(
    self.out_parser.get(self._calculation_type, {})
    .get('molecular_dynamics', {})
    .get('md_ini', [])
)
# Merge settings, with old format taking precedence if both exist
self._settings['md'] = {**md_settings_new_par, **md_settings_new_ini, **md_settings_old}
```

## Test Files

Reference test files in this repository:

- **Old format (CP2K 2.6.2):**
  - `tests/data/cp2k/molecular_dynamics/H2O-32.out`

- **New format (CP2K 2023.1):**
  - `tests/data/cp2k/molecular_dynamics/H2O-32-2023.1.out`

## References

- CP2K Official Documentation: https://manual.cp2k.org/
- CP2K GitHub Repository: https://github.com/cp2k/cp2k
- This parser implementation: `electronicparsers/cp2k/parser.py`
