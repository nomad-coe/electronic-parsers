This is a NOMAD parser for [OCEAN](https://feff.phys.washington.edu/OCEAN/index.html). It will read OCEAN input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For OCEAN please provide at least the files from this table, if applicable
(remember that you always can provide additional files if you want):

| Input Filename | Description |
| --- | --- |
| `*.out` | **Mainfile:** text output file containing the identifiers for OCEAN |
| `*.in` | input file with all parameters |
| `absspct*` | output data file with the Absorption Spectra |
| `xesspct*` | output data file with the Emission Spectra |
| `rxsspct*` | output data file with the RIXS |
| `photon*` | electron-photon operator |
| `*.fhi*` | pseudopotentials |
| `*fill*` | auxiliary files for targeted element |
| `*opts*` | auxiliary files for targeted element |
