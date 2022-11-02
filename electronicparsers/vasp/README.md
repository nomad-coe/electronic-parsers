This is a NOMAD parser for [VASP](https://www.vasp.at/). It will read VASP input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For VASP please provide at least the files from this table, if applicable
(remember that you always can provide additional files if you want):

|Input Filename| Description|
|--- | --- |
|`vasprun.xml` | **Mainfile** in plain-text (structured) XML format |
|`OUTCAR` | plain-text (semi-structured) file, VAPS's detailed output. Read by NOMAD only as fallback to parse `outcar` data |
