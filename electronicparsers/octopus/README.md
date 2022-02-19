This is a NOMAD parser for [Octopus](https://octopus-code.org/). It will read Octopus input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For Octopus please provide at least the files from this table if applicable to your
calculations (remember that you can provide more files if you want):

|Input Filename| Description|
|--- | --- |
|`<text_file>` | **Mainfile:** a plain text file w/arbitrary name|
|`exec/` | Subdir for runtime information |
|`exec/parser.log` | Input variables (user-defined & default values) |
|`inp`| input file|
|`parse.log`| **Warining** : probably obsolete|
|`restart/`| Data to restart a calculation, e.g., `restart/gs/` is for ground-state|
|`static/` | Subdir to report static part of a calculation|
|`static/eigenvalues`| |
|`static/info` | General info on static part|


