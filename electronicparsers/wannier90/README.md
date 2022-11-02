This is a NOMAD parser for [Wannier90](http://www.wannier.org/). It will read Wannier90 input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For Wannier90 please provide at least the files from this table, if applicable
(remember that you always can provide additional files if you want):

| Input Filename | Description |
| --- | --- |
| `*.wout` | **Mainfile**: output text file w/ arbitrary name |
| `*.win` | input text file |
| `*band.dat` | band structure output file |
| `*dos.dat` | dos output file |
| `*hr.dat` | hopping matrices (written if write_hr *.win is true) |
