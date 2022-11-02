This is a collection of the NOMAD parsers for the following electronic codes:

1. [ABACUS](http://abacus.ustc.edu.cn/)
2. [ABINIT](https://www.abinit.org/)
3. [ALF](https://git.physik.uni-wuerzburg.de/ALF/ALF)
4. [AMS](https://www.scm.com)
5. [QuantumATK](https://www.synopsys.com/silicon/quantumatk.html)
6. [BigDFT](http://bigdft.org/)
7. [CASTEP](http://www.castep.org/)
8. [CHARMM](https://www.charmm.org)
9. [CP2K](https://www.cp2k.org/)
10. [CPMD](https://www.cpmd.org/)
11. [CRYSTAL](https://www.crystal.unito.it/)
12. [DMol3](http://dmol3.web.psi.ch/)
13. [Elk](http://elk.sourceforge.net/)
14. [exciting](http://exciting-code.org/)
15. [FHI-aims](https://aimsclub.fhi-berlin.mpg.de/)
16. [FLEUR](https://www.flapw.de/)
17. [FPLO](https://www.fplo.de/)
18. [GAMESS](https://www.msg.chem.iastate.edu/)
19. [Gaussian](http://gaussian.com)
20. [GPAW](https://wiki.fysik.dtu.dk/gpaw/)
21. [Molcas](http://molcas.org/)
22. [MOPAC](http://openmopac.net/)
23. [NWChem](https://nwchemgit.github.io/)
24. [Octopus](https://octopus-code.org/)
25. [ONETEP](https://www.onetep.org/)
26. [OpenMX](http://www.openmx-square.org/)
27. [ORCA](https://www.faccts.de/orca/)
28. [Psi4](https://psicode.org/)
29. [Qball](https://github.com/LLNL/qball)
30. [Qbox](http://qboxcode.org/)
31. [QuantumESPRESSO](http://www.quantum-espresso.org/)
32. [SIESTA](https://siesta-project.org/siesta)
33. [TURBOMOLE](https://www.turbomole.org/)
34. [VASP](https://www.vasp.at/)
35. [Wannier90](http://www.wannier.org/)
36. [WIEN2k](http://www.wien2k.at/)
37. [YAMBO](https://www.yambo-code.org/)

## Preparing code input and output file for uploading to NOMAD

An *upload* is basically a directory structure with files. If you have all the files locally
you can just upload everything as a `.zip` or `.tar.gz` file in a single step. While the upload is
in the *staging area* (i.e. before it is published) you can also easily add or remove files in the
directory tree via the web interface. NOMAD will automatically try to choose the right parser
for you files.

For each parser there is one type of file that the respective parser can recognize. We call
these files *mainfiles*. For each mainfile that NOMAD discovers it will create an *entry*
in the database, which users can search, view, and download. NOMAD will consider all files
in the same directory as *auxiliary files* that also are associated with that entry. Parsers
might also read information from these auxillary files. This way you can add more files
to an entry, even if the respective parser/code might not use them. However, we strongly
recommend to not have multiple mainfiles in the same directory. For CMS calculations, we
recommend having a separate directory for each code run.

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

Clone the parser project and install it in development mode:

```
git clone https://github.com/nomad-coe/electronic-parsers.git electronic-parsers
pip install -e electronic-parsers
```

Running the parser now, will use the parser's Python code from the clone project.
