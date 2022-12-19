This is a NOMAD parser for [w2dynamics](https://github.com/w2dynamics/w2dynamics). It will read w2dynamics input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For w2dynamics please provide at least the files from this table, if applicable
(remember that you always can provide additional files if you want):

| Input Filename | Description |
| --- | --- |
| `*.hdf5` | **Mainfile:** hdf5 file containing all i/o parameters w/ arbitrary name |
| `*.in` | input text file containing [general], [atoms], and [QMC] input parameters |
| `epsk` | plain text, discrete bath levels |
| `Vk` | plain text, hybridizations |
| `w2d.log` | output log error file |
