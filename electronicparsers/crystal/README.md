This is a NOMAD parser for [CRYSTAL](https://www.crystal.unito.it/). It will read CRYSTAL input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For CRYSTAL please provide at least the files from this table if applicable to your
calculations (remember that you can provide more files if you want):

|Input Filename| Description|
|--- | --- |
|`<text_file>` | **Mainfile**, plain text file w/arbitrary name. E.g.,  `simulation.out` |
|`<text_file>.d12` | Program input. Plain text file with the same name (different extension) as the mainfile. E.g. `simulation.d12` |
|AUX FILES| Description|
|`<text_file>.f25`| Output of various electronic and electrical properties. Plain text file with the same name (different extension) as the mainfile. **NOTE**: required in order to parse band structures and density of states. E.g. `simulation.f25` |


