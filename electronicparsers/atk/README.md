This is a NOMAD parser for [QuantumATK](https://www.synopsys.com/silicon/quantumatk.html). It will read QuantumATK input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For QuantumATK please provide at least the files from this table, if applicable
(remember that you always can provide additional files if you want):

|Input Filename| Description|
|--- | --- |
|`*.nc` | The NetCDF output is used as the **mainfile** (HDF5 output is currently not yet supported) |
|`*` | Other ATK input and output files act as auxiliary files that can be downloaded, put are not parsed |
