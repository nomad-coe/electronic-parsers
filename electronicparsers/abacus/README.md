This is a NOMAD parser for [ABACUS](http://abacus.ustc.edu.cn/). It will read ABACUS input and
output files and provide all information in NOMAD's unified Metainfo based Archive format.

For ABACUS please provide at least the files from this table if applicable to your
calculations (remember that you can provide more files if you want):

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

Clone the parser project and install it in development mode:

```
git clone https://github.com/nomad-coe/nomad-parser-abacus.git nomad-parser-abacus
pip install -e nomad-parser-abacus
```

Running the parser now, will use the parser's Python code from the clone project.
