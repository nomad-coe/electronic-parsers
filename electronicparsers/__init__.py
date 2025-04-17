#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from pydantic import Field
from typing import Optional

from nomad.config.models.plugins import ParserEntryPoint


class EntryPoint(ParserEntryPoint):
    parser_class_name: str = Field(
        description="""
        The fully qualified name of the Python class that implements the parser.
        This class must have a function `def parse(self, mainfile, archive, logger)`.
    """
    )
    level: int = Field(
        0,
        description="""
        Order of execution of parser with respect to other parsers.
    """,
    )
    code_name: Optional[str] = None
    code_homepage: Optional[str] = None
    code_category: Optional[str] = None
    metadata: Optional[dict] = Field(
        None,
        description="""
        Metadata passed to the UI. Deprecated. """,
    )

    def load(self):
        from nomad.parsing import MatchingParserInterface

        return MatchingParserInterface(**self.dict())


abacus_parser_entry_point = EntryPoint(
    name='parsers/abacus',
    aliases=['parsers/abacus'],
    description='NOMAD parser for ABACUS.',
    mainfile_contents_re=r'\s*\n\s*WELCOME TO ABACUS',
    python_package='electronicparsers.abacus',
    parser_class_name='electronicparsers.abacus.ABACUSParser',
    code_name='ABACUS',
    code_homepage='http://abacus.ustc.edu.cn/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'ABACUS',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'abacus',
        'codeUrl': 'http://abacus.ustc.edu.cn/',
        'parserDirName': 'dependencies/parsers/abacus/',
        'parserGitUrl': 'https://github.com/nomad-coe/nomad-parser-abacus.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': "|Input Filename| Description|\n|--- | --- |\n|`<text_file>` | **Mainfile**, plain text file w/arbitrary name, e.g.,  `running_<scf, nscf, relax, ...md>.log` |\n|`INPUT` | Runtime information |\n|AUX FILES| Description|\n|`STRU` | Material's atomic-structure information |\n|`KPT` | K-points information |\n|`<text_file>` |  pseudopotental files |\n|`<text_file>`| optimized atomic basis sets |\n|`TDOS`| Kohn-Sham total DOS |\n|`PDOS`  | Projected DOS |\n|`BANDS_<nspin>.dat` | bandstructure file |\n",
    },
)

abinit_parser_entry_point = EntryPoint(
    name='parsers/abinit',
    aliases=['parsers/abinit'],
    description='NOMAD parser for ABINIT.',
    mainfile_contents_re=r'^\n*\.Version\s*[0-9.]*\s*of ABINIT\s*',
    python_package='electronicparsers.abinit',
    parser_class_name='electronicparsers.abinit.AbinitParser',
    code_name='ABINIT',
    code_homepage='https://www.abinit.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'ABINIT',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'abinit',
        'codeUrl': 'https://www.abinit.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/abinit/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`*.*o*` | **Mainfile:** a plain text file w/ **user-defined** name|\n|`*.files`| plain text; user-defined filenames |\n|`*.*i*`| plain text, input parameters|\n|`*_o_DDB`| netcdf binary file, Derivative DataBases of total energy|\n|`*_o_DEN`| netcdf binary file, charge density|\n|`*_o_EIG`| text file, eigenvalues|\n|`*_o_WFK`| netcdf binary file, wavefunction|\n|`*o_SCR`| netcdf binary file, RPA inverse dielectric screening |\n|`*o_SIGRES`| netcdf binary file, GW self-energy correction |\n|`log` | plain text, redirection of screen output (`stdout`)|\n',
    },
)

ams_parser_entry_point = EntryPoint(
    name='parsers/ams',
    aliases=['parsers/ams'],
    description='NOMAD parser for AMS.',
    python_package='electronicparsers.ams',
    mainfile_contents_re=r'\* +\| +A M S +\| +\*',
    parser_class_name='electronicparsers.ams.AMSParser',
    code_name='AMS',
    code_homepage='https://www.scm.com',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'AMS',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'ams',
        'codeUrl': 'https://www.scm.com',
        'parserDirName': 'dependencies/electronic/electronicparsers/ams/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

atk_parser_entry_point = EntryPoint(
    name='parsers/atk',
    aliases=['parsers/atk'],
    description='NOMAD parser for ATK.',
    python_package='electronicparsers.atk',
    mainfile_mime_re='application/octet-stream',
    mainfile_name_re=r'^.*\.nc',
    parser_class_name='electronicparsers.atk.ATKParser',
    code_name='QuantumATK',
    code_homepage='https://www.synopsys.com/silicon/quantumatk.html',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'QuantumATK',
        'codeLabelStyle': 'capitals: Q, A, T, K',
        'codeName': 'atk',
        'codeUrl': 'https://www.synopsys.com/silicon/quantumatk.html',
        'parserDirName': 'dependencies/electronic/electronicparsers/atk/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': 'Currently, NOMAD only supports NetCDF output of AtomistixToolKit (ATK) and not the\nHDF5 based output of QuantumATK.\n',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`*.nc` | The NetCDF output is used as the **mainfile** (HDF5 output is currently not yet supported) |\n|`*` | Other ATK input and output files act as auxiliary files that can be downloaded, put are not parsed |\n',
    },
)

bigdft_parser_entry_point = EntryPoint(
    name='parsers/bigdft',
    aliases=['parsers/bigdft'],
    description='NOMAD parser for BIGDFT.',
    python_package='electronicparsers.bigdft',
    mainfile_contents_re=r'\|_____\|__:__\|__:__\|_____\|_____\|___ BBBBB          i     g         g\s*',
    parser_class_name='electronicparsers.bigdft.BigDFTParser',
    code_name='BigDFT',
    code_homepage='http://bigdft.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'BigDFT',
        'codeLabelStyle': 'Capitals: B,D,F,T,',
        'codeName': 'bigdft',
        'codeUrl': 'http://bigdft.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/bigdft/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

castep_parser_entry_point = EntryPoint(
    name='parsers/castep',
    aliases=['parsers/castep'],
    description='NOMAD parser for CASTEP.',
    python_package='electronicparsers.castep',
    mainfile_contents_re=r'\s\|\s*CCC\s*AA\s*SSS\s*TTTTT\s*EEEEE\s*PPPP\s*\|\s*',
    parser_class_name='electronicparsers.castep.CastepParser',
    code_name='CASTEP',
    code_homepage='http://www.castep.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'CASTEP',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'castep',
        'codeUrl': 'http://www.castep.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/castep/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '### CASTEP output examples\n[Note: The list below is much shorter than the existing examples]\nA few output files to test the parser are provided in the directory `castep/test/examples/*/`.\n\n        FILE NAME     |              FILE DESCRIPTION\n    __________________|___________________________________________________\n    "Si2.castep_v_1" --> Single Point Calculation (minimum verbosity)\n    "Si2.castep_v_2" --> Single Point Calculation (medium verbosity)\n    "Si2.castep_v_3" --> Single Point Calculation (maximum verbosity)\n\n    "Si2.castep_b_v_1" --> Band Structure Calculation (minimum verbosity)\n    "Si2.castep_b_v_2" --> Band Structure Calculation (medium verbosity)\n    "Si2.castep_b_v_3" --> Band Structure Calculation (maximum verbosity)\n',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

charmm_parser_entry_point = EntryPoint(
    name='parsers/charmm',
    aliases=['parsers/charmm'],
    description='NOMAD parser for CHARMM.',
    python_package='electronicparsers.charmm',
    mainfile_contents_re=r'\s*Chemistry\s*at\s*HARvard\s*Macromolecular\s*Mechanics\s*',
    mainfile_mime_re='text/.*',
    parser_class_name='electronicparsers.charmm.CharmmParser',
    code_name='CHARMM',
    code_homepage='https://www.charmm.org',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'CHARMM',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'charmm',
        'codeUrl': 'https://www.charmm.org',
        'parserDirName': 'dependencies/electronic/electronicparsers/charmm/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

cp2k_parser_entry_point = EntryPoint(
    name='parsers/cp2k',
    aliases=['parsers/cp2k'],
    description='NOMAD parser for CP2K.',
    python_package='electronicparsers.cp2k',
    mainfile_contents_re=(
        r'\*\*\*\* \*\*\*\* \*\*\*\*\*\*  \*\*  PROGRAM STARTED '
        r'AT\s.*\n \*\*\*\*\* \*\* \*\*\*  \*\*\* \*\*   PROGRAM STARTED ON\s*.*\n \*\*    \*\*\*\*   \*\*\*\*\*\*    '
        r'PROGRAM STARTED BY .*\n \*\*\*\*\* \*\*    \*\* \*\* \*\*   PROGRAM PROCESS ID .*\n  \*\*\*\* '
        r'\*\*  \*\*\*\*\*\*\*  \*\*  PROGRAM STARTED IN .*\n'
    ),
    parser_class_name='electronicparsers.cp2k.CP2KParser',
    code_name='CP2K',
    code_homepage='https://www.cp2k.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'CP2K',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'cp2k',
        'codeUrl': 'https://www.cp2k.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/cp2k/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': "## Usage notes\nThe parser is based on CP2K 2.6.2.\n\nThe CP2K input setting\n[PRINT_LEVEL](https://manual.cp2k.org/trunk/CP2K_INPUT/GLOBAL.html#PRINT_LEVEL)\ncontrols the amount of details that are outputted during the calculation. The\nhigher this setting is, the more can be parsed from the upload.\n\nThe parser will try to find the paths to all the input and output files, but if\nthey are located very deep inside some folder structure or outside the folder\nwhere the output file is, the parser will not be able to locate them. For this\nreason it is recommended to keep the upload structure as flat as possible.\n\nHere is a list of features/fixes that would make the parsing of CP2K results\neasier:\n- The pdb trajectory output doesn't seem to conform to the actual standard as\n  the different configurations are separated by the END keyword which is\n  supposed to be written only once in the file. The [format\n  specification](http://www.wwpdb.org/documentation/file-format) states that\n  different configurations should start with MODEL and end with ENDMDL tags.\n- The output file should contain the paths/filenames of different input and\n  output files that are accessed during the program run. This data is already\n  available for some files (input file, most files produced by MD), but many\n  are not mentioned.\n",
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '| Input Filename | Description |\n| --- | --- |\n| `*.out` | **Mainfile**: output text file w/ arbitrary name |\n| `*.in` or `*.restart` | input text file; defined in the first lines of `*.out` |\n| `*.pdos` | (projected) dos output file |\n| `*.xyz` | trajectories output file |\n| `*.ener` | MD energies output file |\n',
    },
)

cpmd_parser_entry_point = EntryPoint(
    name='parsers/cpmd',
    aliases=['parsers/cpmd'],
    description='NOMAD parser for CPMD.',
    python_package='electronicparsers.cpmd',
    mainfile_contents_re=r'\*\*\*       \*\*   \*\*\*  \*\* \*\*\*\* \*\*  \*\*   \*\*\*',
    parser_class_name='electronicparsers.cpmd.CPMDParser',
    code_name='CPMD',
    code_homepage='https://www.cpmd.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'CPMD',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'cpmd',
        'codeUrl': 'https://www.cpmd.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/cpmd/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

crystal_parser_entry_point = EntryPoint(
    name='parsers/crystal',
    aliases=['parsers/crystal'],
    description='NOMAD parser for CRYSTAL.',
    python_package='electronicparsers.crystal',
    mainfile_contents_re=r'(\r?\n \*\s+CRYSTAL[\d]+\s+\*\r?\n \*\s*[a-zA-Z]+ : \d+[\.\d+]*)',
    parser_class_name='electronicparsers.crystal.CrystalParser',
    code_name='CRYSTAL',
    code_homepage='https://www.crystal.unito.it/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'CRYSTAL',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'crystal',
        'codeUrl': 'https://www.crystal.unito.it/',
        'parserDirName': 'dependencies/electronic/electronicparsers/crystal/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`<text_file>` | **Mainfile**, plain text file w/arbitrary name. E.g.,  `simulation.out` |\n|`<text_file>.d12` | Program input. Plain text file with the same name (different extension) as the mainfile. E.g. `simulation.d12` |\n|AUX FILES| Description|\n|`<text_file>.f25`| Output of various electronic and electrical properties. Plain text file with the same name (different extension) as the mainfile. **NOTE**: required in order to parse band structures and density of states. E.g. `simulation.f25` |\n',
    },
)

dmol3_parser_entry_point = EntryPoint(
    name='parsers/dmol',
    aliases=['parsers/dmol'],
    description='NOMAD parser for DMOL3.',
    python_package='electronicparsers.dmol3',
    mainfile_contents_re=r'Materials Studio DMol\^3',
    mainfile_name_re=r'.*\.outmol',
    parser_class_name='electronicparsers.dmol3.Dmol3Parser',
    code_name='DMol3',
    code_homepage='http://dmol3.web.psi.ch/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'DMol3',
        'codeLabelStyle': 'Capitals: D, M',
        'codeName': 'dmol',
        'codeUrl': 'http://dmol3.web.psi.ch/',
        'parserDirName': 'dependencies/electronic/electronicparsers/dmol3/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

edmft_parser_entry_point = EntryPoint(
    name='parsers/edmft',
    aliases=['parsers/edmft'],
    description='NOMAD parser for EDMFT.',
    python_package='electronicparsers.edmft',
    mainfile_contents_re=r'\-\-\-\s*Preparing GF calculation\s*\-\-\-',
    mainfile_name_re=r'^.*\.(out)$',
    parser_class_name='electronicparsers.edmft.EDMFTParser',
    level=2,
    code_name='eDMFT',
    code_homepage='http://hauleweb.rutgers.edu/tutorials/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'eDMFT',
        'codeLabelStyle': 'e in lower case, DMFT in capitals',
        'codeName': 'eDMFT',
        'codeUrl': 'http://hauleweb.rutgers.edu/tutorials/',
        'parserDirName': 'dependencies/parsers/electronic/electronicparsers/edmft/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '| Input Filename | Description |\n| --- | --- |\n| `dmft_info.out` | **Mainfile:** output full DMFT loop text file |\n| `dmft1_info.out` | output DMFT1 loop text file |\n| `dmft2_info.out` | output DMFT2 loop text file |\n| `*.indmfl` | input basis parameters text file |\n| `*params.dat` | input DMFT parameters text file |\n| `*.struct` | output text file with data for the structure (specific to WIEN2k) |\n| `*projectorw.dat` | output data file with projectors |\n| `*.dayfile` | output sfc charge information for DMFT2->DFT |\n| `info.iterate` | output sfc information; use second Ftot+T*Simp column for the free energy |\n| `*.gcJ` | output Greens function lattice data per DMFT loop J |\n| `imp.X/Gf.out.I.J` | output Greens function data for impurity X per DFT+DMFT loop I and DMFT loop J |\n| `sig.inpJ` | output self-energy lattice data per DMFT loop J |\n| `imp.X/Sig.out.I.J` | output self-energy data for impurity X data per DFT+DMFT loop I and DMFT loop J |\n| `*.dltJ` | output hybridization function data per DMFT loop J |\n| `imp.X/Delta.inp.I.J` | output hybridization function data for impurity X data DFT+DMFT loop I and DMFT loop J |\n',
    },
)

elk_parser_entry_point = EntryPoint(
    name='parsers/elk',
    aliases=['parsers/elk'],
    description='NOMAD parser for ELK.',
    python_package='electronicparsers.elk',
    mainfile_contents_re=r'\| Elk version [0-9.a-zA-Z]+ started \|',
    parser_class_name='electronicparsers.elk.ElkParser',
    code_name='Elk',
    code_homepage='http://elk.sourceforge.net/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Elk',
        'codeLabelStyle': 'Only E in capitals',
        'codeName': 'elk',
        'codeUrl': 'http://elk.sourceforge.net/',
        'parserDirName': 'dependencies/electronic/electronicparsers/elk/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

exciting_parser_entry_point = EntryPoint(
    name='parsers/exciting',
    aliases=['parsers/exciting'],
    description='NOMAD parser for EXCITING.',
    python_package='electronicparsers.exciting',
    mainfile_contents_re=r'EXCITING.*started[\s\S]+?All units are atomic ',
    mainfile_name_re=r'^.*.OUT(\.[^/]*)?$',
    parser_class_name='electronicparsers.exciting.ExcitingParser',
    code_name='exciting',
    code_homepage='http://exciting-code.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'exciting',
        'codeLabelStyle': 'All in LOWER case',
        'codeName': 'exciting',
        'codeUrl': 'http://exciting-code.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/exciting/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`INFO.OUT`| mainfile|\n|`BAND-QP.OUT`| |\n|`BANDLINES.OUT`| |\n|`DIELTENS0*.OUT`| |\n|`DIELTENS0_NOSYM*.OUT`| |\n|`EIGVAL.OUT`| |\n|`EPSILON_*FXC*_OC*.OUT `| |\n|`EPSILON_*NLF_FXC*_OC*.OUT`| |\n|`EPSILON_BSE*_SCR*_OC*.OUT`| |\n|`EVALQP.DAT or EVALQP.TXT`| |\n|`EXCITON_BSE*_SCR*_OC*.OUT`| |\n|`FERMISURF.bxsf`| |\n|`GQPOINTS*.OUT`| |\n|`GW_INFO.OUT`| |\n|`INFO_VOL       `| |\n|`LOSS_*FXC*_OC*.OUT`| |\n|`LOSS_*NLF_*FXC*_OC*.OUT`| |\n|`QPOINTS.OUT`| |\n|`SIGMA_*FXC*_OC*.OUT`| |\n|`SIGMA_*NLF_FXC*_OC*.OUT `| |\n|`SIGMA_BSE*_SCR*_OC*.OUT `| |\n|`TDOS-QP.OUT` | time dependent DOS|\n|`bandstructure-qp.dat`| |\n|`bandstructure.xml`| (vertexLabGWFile)|\n|`bandstructure.xml`| |\n|`dos.xml`| |\n|`input-gw.xml `| |\n|`input.xml`|(GSFile) |\n|`input.xml`| (XSFile)|\n|`str.out`| |\n',
    },
)

fhiaims_parser_entry_point = EntryPoint(
    name='parsers/fhi-aims',
    aliases=['parsers/fhi-aims'],
    description='NOMAD parser for FHIAIMS.',
    python_package='electronicparsers.fhiaims',
    mainfile_contents_re=r'^(.*\n)*?\s*Invoking FHI-aims \.\.\.',
    parser_class_name='electronicparsers.fhiaims.FHIAimsParser',
    code_name='FHI-aims',
    code_homepage='https://aimsclub.fhi-berlin.mpg.de/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'FHI-aims',
        'codeLabelStyle': 'Capitals: FHI, the rest in lowercase; use dash.',
        'codeName': 'fhi-aims',
        'codeUrl': 'https://aimsclub.fhi-berlin.mpg.de/',
        'parserDirName': 'dependencies/electronic/electronicparsers/fhi-aims/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserLastUpdate': '18.10.2022',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': "|Input Filename| Description|\n|--- | --- |\n|`<text_file>` | **Mainfile**, plain text file w/arbitrary name, e.g.,  `<output,control, aims,...>.out` |\n|`control.in` | Runtime information |\n|`geometry.in` | Material's atomic-structure information,  |\n|AUX FILES| Description|\n|`<atoml_label>_l_proj_dos.out`|  Angular-momentum-resolved DOS @ Fermi Energy|\n|`<atoml_label>_l_proj_dos_raw.out`|  Angular-momentum-resolved DOS @ vacuum|\n|`KS_DOS_total.dat`| Kohn-Sham total DOS @ Fermi Energy |\n|`KS_DOS_total_raw.dat`| Kohn-Sham total DOS @ vacuum |\n|`Mulliken.out` **WARNING-->**|Mulliken charge analysis on all atoms. **WARNING** not yet read by NOMAD's parser|\n|`atom_proj_dos_<atom_name><index>_raw.dat`  | Atom-projected DOS @ vacuum|\n|`atom_projected_dos_<atom_name><index>.dat`  | Atom-projected DOS @ Fermi Energy|\n|`band<spin><segment>.out` | bandstructure file |\n|`GW_band<spin><segment>` | GW bandstructure file |\n",
    },
)

fleur_parser_entry_point = EntryPoint(
    name='parsers/fleur',
    aliases=['parsers/fleur'],
    description='NOMAD parser for FLEUR.',
    python_package='electronicparsers.fleur',
    mainfile_alternative=True,
    mainfile_contents_re=r'This output is generated by fleur.|\<fleurOutput',
    mainfile_mime_re='(application/.*)|(text/.*)',
    mainfile_name_re=r'.*[^/]*\.xml[^/]*',
    parser_class_name='electronicparsers.fleur.FleurParser',
    code_name='FLEUR',
    code_homepage='https://www.flapw.de/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'FLEUR',
        'codeLabelStyle': 'Found: 1) only F in capitals, 2) all in capitals.',
        'codeName': 'fleur',
        'codeUrl': 'https://www.flapw.de/',
        'parserDirName': 'dependencies/electronic/electronicparsers/fleur/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

fplo_parser_entry_point = EntryPoint(
    name='parsers/fplo',
    aliases=['parsers/fplo'],
    description='NOMAD parser for FPLO.',
    python_package='electronicparsers.fplo',
    mainfile_contents_re=(
        r'\s*\|\s*FULL-POTENTIAL LOCAL-ORBITAL MINIMUM BASIS BANDSTRUCTURE '
        r'CODE\s*\|\s*'
    ),
    mainfile_mime_re='text/.*',
    parser_class_name='electronicparsers.fplo.FploParser',
    code_name='FPLO',
    code_homepage='https://www.fplo.de/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'FPLO',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'fplo',
        'codeUrl': 'https://www.fplo.de/',
        'parserDirName': 'dependencies/electronic/electronicparsers/fplo/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

gamess_parser_entry_point = EntryPoint(
    name='parsers/gamess',
    aliases=['parsers/gamess'],
    description='NOMAD parser for GAMESS.',
    python_package='electronicparsers.gamess',
    mainfile_contents_re=(
        r'\s*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\s*\s*\*\s*GAMESS '
        r'VERSION =\s*(.*)\*\s*\s*\*\s*FROM IOWA STATE UNIVERSITY\s*\*\s*'
    ),
    parser_class_name='electronicparsers.gamess.GamessParser',
    code_name='GAMESS',
    code_homepage='https://www.msg.chem.iastate.edu/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'GAMESS',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'gamess',
        'codeUrl': 'https://www.msg.chem.iastate.edu/',
        'parserDirName': 'dependencies/electronic/electronicparsers/gamess/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

gaussian_parser_entry_point = EntryPoint(
    name='parsers/gaussian',
    aliases=['parsers/gaussian'],
    description='NOMAD parser for GAUSSIAN.',
    python_package='electronicparsers.gaussian',
    mainfile_contents_re=r'\s*Cite this work as:\s*Gaussian [0-9]+, Revision [A-Za-z0-9\.]*,',
    mainfile_mime_re='.*',
    parser_class_name='electronicparsers.gaussian.GaussianParser',
    code_name='Gaussian',
    code_homepage='http://gaussian.com',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Gaussian',
        'codeLabelStyle': 'Capitals: G',
        'codeName': 'gaussian',
        'codeUrl': 'http://gaussian.com',
        'parserDirName': 'dependencies/electronic/electronicparsers/gaussian/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

gpaw_parser_entry_point = EntryPoint(
    name='parsers/gpaw',
    aliases=['parsers/gpaw'],
    description='NOMAD parser for GPAW.',
    python_package='electronicparsers.gpaw',
    mainfile_mime_re='application/(x-tar|octet-stream)',
    mainfile_name_re=r'^.*\.(gpw2|gpw)$',
    parser_class_name='electronicparsers.gpaw.GPAWParser',
    code_name='GPAW',
    code_homepage='https://wiki.fysik.dtu.dk/gpaw/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'GPAW',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'gpaw',
        'codeUrl': 'https://wiki.fysik.dtu.dk/gpaw/',
        'parserDirName': 'dependencies/electronic/electronicparsers/gpaw/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

magres_parser_entry_point = EntryPoint(
    name='parsers/magres',
    aliases=['parsers/magres'],
    description='NOMAD parser for MAGRES.',
    python_package='electronicparsers.magres',
    mainfile_contents_re=r'\$magres-abinitio-v(\d\.)+',
    mainfile_name_re=r'^.*\.magres',
    parser_class_name='electronicparsers.magres.MagresParser',
    level=1,
    code_name='magres',
    code_homepage='https://www.ccpnc.ac.uk/docs/magres',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'magres',
        'codeLabelStyle': 'all in lower case',
        'codeName': 'magres',
        'codeUrl': 'https://www.ccpnc.ac.uk/docs/magres',
        'parserDirName': 'dependencies/electronic/electronicparsers/magres/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

molcas_parser_entry_point = EntryPoint(
    name='parsers/molcas',
    aliases=['parsers/molcas'],
    description='NOMAD parser for MOLCAS.',
    python_package='electronicparsers.molcas',
    mainfile_contents_re=r'M O L C A S',
    parser_class_name='electronicparsers.molcas.MolcasParser',
    code_name='Molcas',
    code_homepage='http://molcas.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Molcas',
        'codeLabelStyle': 'Capitals: M; also seen all in capitals',
        'codeName': 'molcas',
        'codeUrl': 'http://molcas.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/molcas/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

mopac_parser_entry_point = EntryPoint(
    name='parsers/mopac',
    aliases=['parsers/mopac'],
    description='NOMAD parser for MOPAC.',
    python_package='electronicparsers.mopac',
    mainfile_contents_re=r'\s*\*\*\s*MOPAC\s*([0-9a-zA-Z\.]*)\s*\*\*\s*',
    mainfile_mime_re='text/.*',
    parser_class_name='electronicparsers.mopac.MopacParser',
    code_name='MOPAC',
    code_homepage='http://openmopac.net/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'MOPAC',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'mopac',
        'codeUrl': 'http://openmopac.net/',
        'parserDirName': 'dependencies/parsers/atomistic/atomisticparsers/mopac/',
        'parserGitUrl': 'https://github.com/nomad-coe/atomistic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

nwchem_parser_entry_point = EntryPoint(
    name='parsers/nwchem',
    aliases=['parsers/nwchem'],
    description='NOMAD parser for NWCHEM.',
    python_package='electronicparsers.nwchem',
    mainfile_contents_re=r'Northwest Computational Chemistry Package \(NWChem\) (\d+\.)+\d+',
    parser_class_name='electronicparsers.nwchem.NWChemParser',
    code_name='NWChem',
    code_homepage='https://nwchemgit.github.io/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'NWChem',
        'codeLabelStyle': 'Capitals: N, W, C',
        'codeName': 'nwchem',
        'codeUrl': 'https://nwchemgit.github.io/',
        'parserDirName': 'dependencies/electronic/electronicparsers/nwchem/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

ocean_parser_entry_point = EntryPoint(
    name='parsers/ocean',
    aliases=['parsers/ocean'],
    description='NOMAD parser for OCEAN.',
    python_package='electronicparsers.ocean',
    mainfile_contents_dict={'__has_all_keys': ['bse', 'structure', 'screen', 'calc']},
    mainfile_mime_re='(application/.*)|(text/.*)',
    parser_class_name='electronicparsers.ocean.OceanParser',
    code_name='OCEAN',
    code_homepage='https://feff.phys.washington.edu/OCEAN/index.html',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'OCEAN',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'ocean',
        'codeUrl': 'https://feff.phys.washington.edu/OCEAN/index.html',
        'parserDirName': 'dependencies/electronic/electronicparsers/ocean/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '| Input Filename | Description |\n| --- | --- |\n| `*` | **Mainfile:** text output file (in JSON format) |\n| `*.in` | input file with all parameters |\n| `absspct*` | output data file with the Absorption Spectra |\n| `abslanc*` | output data file with (Lanzcos algorithm) Absorption spectra |\n| `xesspct*` | output data file with the Emission Spectra |\n| `rxsspct*` | output data file with the RIXS |\n| `photon*` | electron-photon operator |\n',
    },
)

octopus_parser_entry_point = EntryPoint(
    name='parsers/octopus',
    aliases=['parsers/octopus'],
    description='NOMAD parser for OCTOPUS.',
    python_package='electronicparsers.octopus',
    mainfile_contents_re=r'\|0\) ~ \(0\) \|',
    parser_class_name='electronicparsers.octopus.OctopusParser',
    code_name='Octopus',
    code_homepage='https://octopus-code.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Octopus',
        'codeLabelStyle': 'Capitals: O',
        'codeName': 'octopus',
        'codeUrl': 'https://octopus-code.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/octopus/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`<text_file>` | **Mainfile:** a plain text file w/arbitrary name|\n|`exec/` | Subdir for runtime information |\n|`exec/parser.log` | Input variables (user-defined & default values) |\n|`inp`| input file|\n|`parse.log`| **Warining** : probably obsolete|\n|`restart/`| Data to restart a calculation, e.g., `restart/gs/` is for ground-state|\n|`static/` | Subdir to report static part of a calculation|\n|`static/eigenvalues`| |\n|`static/info` | General info on static part|\n',
    },
)

onetep_parser_entry_point = EntryPoint(
    name='parsers/onetep',
    aliases=['parsers/onetep'],
    description='NOMAD parser for ONETEP.',
    python_package='electronicparsers.onetep',
    mainfile_contents_re=r'####### #     # ####### ####### ####### ######',
    parser_class_name='electronicparsers.onetep.OnetepParser',
    code_name='ONETEP',
    code_homepage='https://www.onetep.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'ONETEP',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'onetep',
        'codeUrl': 'https://www.onetep.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/onetep/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

openmx_parser_entry_point = EntryPoint(
    name='parsers/openmx',
    aliases=['parsers/openmx'],
    description='NOMAD parser for OPENMX.',
    python_package='electronicparsers.openmx',
    mainfile_contents_re=r'^\*{59}\s+\*{59}\s+This calculation was performed by OpenMX',
    mainfile_mime_re='(text/.*)',
    mainfile_name_re=r'.*\.out$',
    parser_class_name='electronicparsers.openmx.OpenmxParser',
    code_name='OpenMX',
    code_homepage='http://www.openmx-square.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'OpenMX',
        'codeLabelStyle': 'First and last two characters in capitals',
        'codeName': 'openmx',
        'codeUrl': 'http://www.openmx-square.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/openmx/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`<systemname>.out` | **Mainfile** in OpenMX specific plain-text |\n',
    },
)

orca_parser_entry_point = EntryPoint(
    name='parsers/orca',
    aliases=['parsers/orca'],
    description='NOMAD parser for ORCA.',
    python_package='electronicparsers.orca',
    mainfile_contents_re=(
        r'\s+\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\s*\s+\* O   R   C   A '
        r'\*\s*\s+\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\s*\s*'
    ),
    parser_class_name='electronicparsers.orca.OrcaParser',
    code_name='ORCA',
    code_homepage='https://www.faccts.de/orca/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'ORCA',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'orca',
        'codeUrl': 'https://www.faccts.de/orca/',
        'parserDirName': 'dependencies/electronic/electronicparsers/orca/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

psi4_parser_entry_point = EntryPoint(
    name='parsers/psi4',
    aliases=['parsers/psi4'],
    description='NOMAD parser for PSI4.',
    python_package='electronicparsers.psi4',
    mainfile_contents_re=r'Psi4: An Open-Source Ab Initio Electronic Structure Package',
    parser_class_name='electronicparsers.psi4.Psi4Parser',
    code_name='Psi4',
    code_homepage='https://psicode.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Psi4',
        'codeLabelStyle': 'Capitals: P',
        'codeName': 'psi4',
        'codeUrl': 'https://psicode.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/psi4/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`*.out` | **Mainfile:** a plain text file w/ **user-defined** name|\n|`*.dat` |plain text input file|\n',
    },
)

qball_parser_entry_point = EntryPoint(
    name='parsers/qball',
    aliases=['parsers/qball'],
    description='NOMAD parser for QBALL.',
    python_package='electronicparsers.qball',
    mainfile_contents_re=r'qball',
    supported_compressions=['gz', 'bz2', 'xz'],
    parser_class_name='electronicparsers.qball.QBallParser',
    code_name='Qball',
    code_homepage='https://github.com/LLNL/qball',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Qball',
        'codeLabelStyle': 'Capitals: Q',
        'codeName': 'qball',
        'codeUrl': 'https://github.com/LLNL/qball',
        'parserDirName': 'dependencies/electronic/electronicparsers/qball/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`*.out` | **Mainfile:** a plain text file w/ **user-defined** name|\n',
    },
)

qbox_parser_entry_point = EntryPoint(
    name='parsers/qbox',
    aliases=['parsers/qbox'],
    description='NOMAD parser for QBOX.',
    python_package='electronicparsers.qbox',
    mainfile_contents_re=r'http://qboxcode.org',
    mainfile_mime_re='(application/xml)|(text/.*)',
    parser_class_name='electronicparsers.qbox.QboxParser',
    code_name='Qbox',
    code_homepage='http://qboxcode.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Qbox',
        'codeLabelStyle': 'Capitals: Q',
        'codeName': 'qbox',
        'codeUrl': 'http://qboxcode.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/qbox/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

quantumespresso_parser_entry_point = EntryPoint(
    name='parsers/quantumespresso',
    aliases=['parsers/quantumespresso'],
    description='NOMAD parser for QUANTUMESPRESSO.',
    python_package='electronicparsers.quantumespresso',
    mainfile_contents_re=(
        r'(Program PWSCF.*starts)|(Current dimensions of program ' r'PWSCF are)'
    ),
    supported_compressions=['gz', 'bz2', 'xz'],
    parser_class_name='electronicparsers.quantumespresso.QuantumEspressoParser',
    code_name='QuantumESPRESSO',
    code_homepage='http://www.quantum-espresso.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'QuantumESPRESSO',
        'codeLabelStyle': 'Capitals Q, E, S, P, R, E, S, S, O',
        'codeName': 'quantumespresso',
        'codeUrl': 'http://www.quantum-espresso.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/quantum-espresso/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': "|Filename| Description|\n|---|---|\n|`<text_file>`|**Mainfile:** a plain text file w/arbitrary name. \\\nOne of the top lines must contain '`Program PWSCF.*starts`', \\\nwhere '`.*`' means an arbitrary number '`*`' of arbitrary \\\ncharacters '`.`'|\"\n",
    },
)

siesta_parser_entry_point = EntryPoint(
    name='parsers/siesta',
    aliases=['parsers/siesta'],
    description='NOMAD parser for SIESTA.',
    python_package='electronicparsers.siesta',
    mainfile_contents_re=(
        r'(Siesta Version: siesta-|SIESTA [0-9]\.[0-9]\.[0-9])|(\*\s*WELCOME '
        r'TO SIESTA\s*\*)'
    ),
    parser_class_name='electronicparsers.siesta.SiestaParser',
    code_name='SIESTA',
    code_homepage='https://siesta-project.org/siesta',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'SIESTA',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'siesta',
        'codeUrl': 'https://siesta-project.org/siesta',
        'parserDirName': 'dependencies/electronic/electronicparsers/siesta/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

soliddmft_parser_entry_point = EntryPoint(
    name='parsers/soliddmft',
    aliases=['parsers/soliddmft'],
    description='NOMAD parser for SOLIDDMFT.',
    python_package='electronicparsers.soliddmft',
    mainfile_binary_header_re=b'^\\x89HDF',
    mainfile_contents_dict={
        '__has_all_keys': ['dft_input', 'DMFT_input', 'DMFT_results']
    },
    mainfile_mime_re='(application/x-hdf)',
    mainfile_name_re=r'^.*\.(h5|hdf5)$',
    parser_class_name='electronicparsers.soliddmft.SolidDMFTParser',
    code_name='solid_dmft',
    code_homepage='https://github.com/TRIQS/solid_dmft',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'solid_dmft',
        'codeLabelStyle': 'All in lowercase',
        'codeName': 'solid_dmft',
        'codeUrl': 'https://github.com/TRIQS/solid_dmft',
        'codeVersion': '',
        'parserDirName': 'dependencies/parsers/electronic/electronicparsers/soliddmft/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '| Input Filename | Description |\n| --- | --- |\n| `*.h5` | **Mainfile:** h5 file containing all i/o parameters w/ arbitrary name |\n',
    },
)

tbstudio_parser_entry_point = EntryPoint(
    name='parsers/tbstudio',
    aliases=['parsers/tbstudio'],
    description='NOMAD parser for TBSTUDIO.',
    python_package='electronicparsers.tbstudio',
    mainfile_contents_re=r'"ApplicationFullName": "Tight Binding Studio"',
    mainfile_mime_re='(application/json)|(text/.*)',
    mainfile_name_re=r'.*\.tbm',
    parser_class_name='electronicparsers.tbstudio.TBStudioParser',
    level=1,
    code_name='TBStudio',
    code_homepage='https://tight-binding.com/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'TBStudio',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'tbstudio',
        'codeUrl': 'https://tight-binding.com/',
        'parserDirName': 'dependencies/electronic/electronicparsers/tbstudio/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '| Input Filename | Description |\n| --- | --- |\n| `*.tbm` | **Mainfile**: output binary file |\n',
    },
)

turbomole_parser_entry_point = EntryPoint(
    name='parsers/turbomole',
    aliases=['parsers/turbomole'],
    description='NOMAD parser for TURBOMOLE.',
    python_package='electronicparsers.turbomole',
    mainfile_contents_re=r'Copyright \(C\) [0-9]+ TURBOMOLE GmbH, Karlsruhe',
    parser_class_name='electronicparsers.turbomole.TurbomoleParser',
    code_name='TURBOMOLE',
    code_homepage='https://www.turbomole.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'TURBOMOLE',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'turbomole',
        'codeUrl': 'https://www.turbomole.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/turbomole/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

vasp_parser_entry_point = EntryPoint(
    name='parsers/vasp',
    aliases=['parsers/vasp'],
    description='NOMAD parser for VASP.',
    python_package='electronicparsers.vasp',
    mainfile_contents_re=(
        r'^\s*<\?xml version="1\.0" encoding="ISO-8859-1"\?>\s*?\s*<modeling>?\s*<generator>?\s*<i '
        r'name="program" type="string">\s*vasp\s*</i>?|^\svasp[\.\d]+.+?(?:\(build|complex)[\s\S]+?executed '
        r'on'
    ),
    mainfile_mime_re='(application/.*)|(text/.*)',
    mainfile_name_re='.*[^/]*xml[^/]*',
    mainfile_alternative=True,
    supported_compressions=['gz', 'bz2', 'xz'],
    parser_class_name='electronicparsers.vasp.VASPParser',
    code_name='VASP',
    code_homepage='https://www.vasp.at/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'VASP',
        'codeLabelStyle': 'All in capitals',
        'codeName': 'vasp',
        'codeUrl': 'https://www.vasp.at/',
        'parserDirName': 'dependencies/electronic/electronicparsers/vasp/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': "|Input Filename| Description|\n|--- | --- |\n|`vasprun.xml` | **Mainfile** in plain-text (structured) XML format |\n|`OUTCAR` | plain-text (semi-structured) file, VAPS's detailed output. Read by NOMAD only as fallback to parse `outcar` data |\n",
    },
)

w2dynamics_parser_entry_point = EntryPoint(
    name='parsers/w2dynamics',
    aliases=['parsers/w2dynamics'],
    description='NOMAD parser for W2DYNAMICS.',
    python_package='electronicparsers.w2dynamics',
    mainfile_binary_header_re=b'^\\x89HDF',
    mainfile_contents_dict={'__has_all_keys': ['.axes', '.config', '.quantities']},
    mainfile_mime_re='(application/x-hdf)',
    mainfile_name_re=r'^.*\.(h5|hdf5)$',
    parser_class_name='electronicparsers.w2dynamics.W2DynamicsParser',
    level=2,
    code_name='w2dynamics',
    code_homepage='https://github.com/w2dynamics/w2dynamics',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'w2dynamics',
        'codeLabelStyle': 'All in lowercase',
        'codeName': 'w2dynamics',
        'codeUrl': 'https://github.com/w2dynamics/w2dynamics',
        'codeVersion': '',
        'parserDirName': 'dependencies/parsers/electronic/electronicparsers/w2dynamics/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '| Input Filename | Description |\n| --- | --- |\n| `*.hdf5` | **Mainfile:** hdf5 file containing all i/o parameters w/ arbitrary name |\n| `*.in` | input text file containing [general], [atoms], and [QMC] input parameters |\n| `epsk` | plain text, discrete bath levels |\n| `Vk` | plain text, hybridizations |\n| `w2d.log` | output log error file |\n',
    },
)

wannier90_parser_entry_point = EntryPoint(
    name='parsers/wannier90',
    aliases=['parsers/wannier90'],
    description='NOMAD parser for WANNIER90.',
    python_package='electronicparsers.wannier90',
    mainfile_contents_re=r'\|\s*WANNIER90\s*\|',
    parser_class_name='electronicparsers.wannier90.Wannier90Parser',
    level=1,
    code_name='Wannier90',
    code_homepage='http://www.wannier.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'Wannier90',
        'codeLabelStyle': 'First letter in capitals, rest in lower case',
        'codeName': 'wannier90',
        'codeUrl': 'http://www.wannier.org/',
        'codeVersions': '3.1.0',
        'parserDirName': 'dependencies/electronic/electronicparsers/wannier90/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '| Input Filename | Description |\n| --- | --- |\n| `*.wout` | **Mainfile**: output text file w/ arbitrary name |\n| `*.win` | input text file |\n| `*band.dat` | band structure output file |\n| `*dos.dat` | dos output file |\n| `*hr.dat` | hopping matrices (written if write_hr *.win is true) |\n',
    },
)

wien2k_parser_entry_point = EntryPoint(
    name='parsers/wien2k',
    aliases=['parsers/wien2k'],
    description='NOMAD parser for WIEN2K.',
    python_package='electronicparsers.wien2k',
    mainfile_contents_re=r'\s*---------\s*:ITE[0-9]+:\s*[0-9]+\.\s*ITERATION\s*---------',
    mainfile_name_re=r'.*\.scf$',
    mainfile_alternative=True,
    parser_class_name='electronicparsers.wien2k.Wien2kParser',
    code_name='WIEN2k',
    code_homepage='http://www.wien2k.at/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'WIEN2k',
        'codeLabelStyle': 'All in capitals, except k',
        'codeName': 'wien2k',
        'codeUrl': 'http://www.wien2k.at/',
        'parserDirName': 'dependencies/electronic/electronicparsers/wien2k/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'status': 'production',
        'tableOfFiles': '',
    },
)

yambo_parser_entry_point = EntryPoint(
    name='parsers/yambo',
    aliases=['parsers/yambo'],
    description='NOMAD parser for YAMBO.',
    python_package='electronicparsers.yambo',
    mainfile_contents_re=r'Build.+\s+http://www\.yambo-code\.org',
    parser_class_name='electronicparsers.yambo.YamboParser',
    code_name='YAMBO',
    code_homepage='https://www.yambo-code.org/',
    code_category='Atomistic code',
    metadata={
        'codeCategory': 'Atomistic code',
        'codeLabel': 'YAMBO',
        'codeLabelStyle': 'all in capitals',
        'codeName': 'yambo',
        'codeUrl': 'https://www.yambo-code.org/',
        'parserDirName': 'dependencies/electronic/electronicparsers/yambo/',
        'parserGitUrl': 'https://github.com/nomad-coe/electronic-parsers.git',
        'parserSpecific': '',
        'preamble': '',
        'status': 'production',
        'tableOfFiles': '|Input Filename| Description|\n|--- | --- |\n|`r-*` | **Mainfile:** a plain text file w/ **user-defined** name|\n|`o-*` | plain text auxiliary output files w/ user-defined filenames |\n|`*.in`| plain text input file w/ **user-defined** name|\n|`n.*`| netcdf file with **user-defined** name|\n',
    },
)
