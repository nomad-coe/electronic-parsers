This is a collection of the NOMAD parsers for the following electronic structure codes.
1. [ABINIT](https://www.abinit.org/)
2. [BAND](https://www.scm.com/product/band_periodicdft/)
3. [BigDFT](http://bigdft.org/)
4. [CASTEP](http://www.castep.org/)
5. [CHARMM](https://www.charmm.org/charmm/)
6. [CP2K](https://www.cp2k.org/)
7. [CPMD](https://www.cpmd.org/)
8. [CRYSTAL](https://www.crystal.unito.it/)
9. [DMol3 ](http://dmol3.web.psi.ch/)
10. [Elk](http://elk.sourceforge.net/)
11. [exciting](http://exciting-code.org/)
12. [FHI-aims](https://aimsclub.fhi-berlin.mpg.de/)
13. [Fleur](https://www.flapw.de/)
14. [FPLO](https://www.fplo.de/)
15. [GAMESS](https://www.msg.chem.iastate.edu/)
16. [Gaussian](http://gaussian.com)
17. [GPAW](https://wiki.fysik.dtu.dk/gpaw/)
18. [Molcas](http://molcas.org/)
19. [NWChem](https://nwchemgit.github.io/)
20. [Octopus](https://octopus-code.org/)
21. [ONETEP](https://www.onetep.org/)
22. [ORCA](https://www.faccts.de/orca/)
23. [Psi4](https://psicode.org/)
24. [QBALL](https://github.com/LLNL/qball)
25. [Qbox](http://qboxcode.org/)
26. [QUANTUM ESPRESSO](http://www.quantum-espresso.org/)
27. [SIESTA](https://departments.icmab.es/leem/siesta/)
28. [TURBOMOLE](https://www.turbomole.org/)
29. [VASP](https://www.vasp.at/)
30. [WIEN2k](http://www.wien2k.at/)
31. [YAMBO](https://www.yambo-code.org/)
32. [OpenMX](http://www.openmx-square.org/)
33. [ABACUS](http://abacus.ustc.edu.cn/)
34. [Wannier90](http://www.wannier.org/)

Each of the parsers will read the relevant input and output files and provide all information in
NOMAD's unified Metainfo based Archive format.

## Preparing code input and output file for uploading to NOMAD

NOMAD accepts `.zip` and `.tar.gz` archives as uploads. Each upload can contain arbitrary
files and directories. NOMAD will automatically try to choose the right parser for you files.
For each parser (i.e. for each supported code) there is one type of file that the respective
parser can recognize. We call these files `mainfiles` as they typically are the main
output file a code. For each `mainfile` that NOMAD discovers it will create an entry
in the database that users can search, view, and download. NOMAD will associate all files
in the same directory as files that also belong to that entry. Parsers
might also read information from these auxillary files. This way you can add more files
to an entry, even if the respective parser/code might not directly support it.

To create an upload with all calculations in a directory structure:

```
zip -r <upload-file>.zip <directory>/*
```

Go to the [NOMAD upload page](https://nomad-lab.eu/prod/rae/gui/uploads) to upload files
or find instructions about how to upload files from the command line.

## Using the parser

You can use NOMAD's parsers and normalizers locally on your computer. You need to install
NOMAD's pypi package:

```
pip install nomad-lab
```

To parse code input/output from the command line, you can use NOMAD's command line
interface (CLI) and print the processing results output to stdout:

```
nomad parse --show-archive <path-to-file>
```

To parse a file in Python, you can program something like this:
```python
import sys
from nomad.cli.parse import parse, normalize_all

# match and run the parser
archive = parse(sys.argv[1])
# run all normalizers
normalize_all(archive)

# get the 'main section' section_run as a metainfo object
section_run = archive.section_run[0]

# get the same data as JSON serializable Python dict
python_dict = section_run.m_to_dict()
```

## Developing the parser

Create a virtual environment to install the parser in development mode:

```
pip install virtualenv
virtualenv -p `which python3` .pyenv
source .pyenv/bin/activate
```

Install NOMAD's pypi package:

```
pip install nomad-lab
```

Clone the electronic parsers project and install it in development mode:

```
git clone https://github.com/nomad-coe/electronic-parsers.git electronic-parsers
pip install -e electronic-parsers
```

