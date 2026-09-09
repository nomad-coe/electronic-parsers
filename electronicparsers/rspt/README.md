This is a very basic NOMAD parser for [RSPt](https://www.uu.se/en/department/physics-and-astronomy/research/materials-theory/code-development) with the following features:

- identifies RSPt calculation as a file ending with `out_last` and with the header `MPI RSPT`,
- reads the version number from the line `RSPt version number: <version>`
- reads the method (DFT or DMFT) from the line `Initialization of the <method> code`
- reads the temperature from the line `Readin: Setting the temperature to <temperature>` (needed for proper normalization of the DMFT method class)
- reads the structure information from a cif file found in the same directory as the `out_last` file



