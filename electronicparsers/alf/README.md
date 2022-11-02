This is a NOMAD parser for [ALF](https://git.physik.uni-wuerzburg.de/ALF/ALF). It will read ALF input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For ALF please provide at least the files from this table, if applicable
(remember that you always can provide additional files if you want):

| Input Filename  | Description |
| --- | --- |
| `data.h5` | **Mainfile**: output hdf5 file  |
| `confout.h5`  | output hdf5 with HS and bosonic configurations |
| `info`  | output text with model parameters and simulation info |
| `parameters`  | input text file |
