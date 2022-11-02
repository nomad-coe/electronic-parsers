This is a NOMAD parser for [ABACUS](http://abacus.ustc.edu.cn/). It will read ABACUS input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For ABACUS please provide at least the files from this table, if applicable
(remember that you always can provide additional files if you want):

|Input Filename| Description|
|--- | --- |
|`<text_file>` | **Mainfile**, plain text file w/arbitrary name, e.g.,  `running_<scf, nscf, relax, ...md>.log` |
|`INPUT` | Runtime information |
|AUX FILES| Description|
|`STRU` | Material's atomic-structure information |
|`KPT` | K-points information |
|`<text_file>` |  pseudopotental files |
|`<text_file>`| optimized atomic basis sets |
|`TDOS`| Kohn-Sham total DOS |
|`PDOS`  | Projected DOS |
|`BANDS_<nspin>.dat` | bandstructure file |
