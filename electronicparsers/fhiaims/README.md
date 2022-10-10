This is a NOMAD parser for [FHI-aims](https://aimsclub.fhi-berlin.mpg.de/). It will read FHI-aims input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For FHI-aims please provide at least the files from this table if applicable to your
calculations (remember that you can provide more files if you want):

|Input Filename| Description|
|--- | --- |
|`<text_file>` | **Mainfile**, plain text file w/arbitrary name, e.g.,  `<output,control, aims,...>.out` |
|`control.in` | Runtime information |
|`geometry.in` | Material's atomic-structure information,  |
|AUX FILES| Description|
|`<atoml_label>_l_proj_dos.out`|  Angular-momentum-resolved DOS @ Fermi Energy|
|`<atoml_label>_l_proj_dos_raw.out`|  Angular-momentum-resolved DOS @ vacuum|
|`KS_DOS_total.dat`| Kohn-Sham total DOS @ Fermi Energy |
|`KS_DOS_total_raw.dat`| Kohn-Sham total DOS @ vacuum |
|`Mulliken.out` **WARNING-->**|Mulliken charge analysis on all atoms. **WARNING** not yet read by NOMAD's parser|
|`atom_proj_dos_<atom_name><index>_raw.dat`  | Atom-projected DOS @ vacuum|
|`atom_projected_dos_<atom_name><index>.dat`  | Atom-projected DOS @ Fermi Energy|
|`band<spin><segment>.out` | bandstructure file |
|`GW_band<spin><segment>.out` | GW bandstructure file |
