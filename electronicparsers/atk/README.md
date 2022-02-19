This is a NOMAD parser for [AtomistixToolKit](https://www.synopsys.com/silicon/quantumatk.html). It will read AtomistixToolKit input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For AtomistixToolKit please provide at least the files from this table if applicable to your
calculations (remember that you can provide more files if you want):

|Input Filename| Description|
|--- | --- |
|`*.nc` | The NetCDF output is used as the **mainfile** (HDF5 output is currently not yet supported) |
|`*` | Other ATK input and output files act as auxiliary files that can be downloaded, put are not parsed |


