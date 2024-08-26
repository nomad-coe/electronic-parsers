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

from nomad.config.models.plugins import ParserEntryPoint


class EntryPoint(ParserEntryPoint):
    parser_class_name: str = Field(
        description="""
        The fully qualified name of the Python class that implements the parser.
        This class must have a function `def parse(self, mainfile, archive, logger)`.
    """
    )

    def load(self):
        from nomad.parsing import MatchingParserInterface
        from . import (
            abacus,
            abinit,
            ams,
            atk,
            bigdft,
            castep,
            charmm,
            cp2k,
            cpmd,
            crystal,
            dmol3,
            edmft,
            elk,
            exciting,
            fhiaims,
            fleur,
            fplo,
            gamess,
            gaussian,
            gpaw,
            magres,
            molcas,
            mopac,
            nwchem,
            ocean,
            octopus,
            onetep,
            openmx,
            orca,
            psi4,
            qball,
            qbox,
            quantumespresso,
            siesta,
            soliddmft,
            tbstudio,
            turbomole,
            vasp,
            w2dynamics,
            wannier90,
            wien2k,
            yambo,
            utils,
        )

        return MatchingParserInterface(**self.dict())


abacus_parser_entry_point = EntryPoint(
    name='parsers/abacus',
    description='NOMAD parser for ABACUS.',
    mainfile_contents_re=r'\s*\n\s*WELCOME TO ABACUS',
    python_package='electronicparsers.abacus',
    parser_class_name='electronicparsers.abacus.ABACUSParser',
)

abinit_parser_entry_point = EntryPoint(
    name='parsers/abinit',
    description='NOMAD parser for ABINIT.',
    mainfile_contents_re=r'^\n*\.Version\s*[0-9.]*\s*of ABINIT\s*',
    python_package='electronicparsers.abinit',
    parser_class_name='electronicparsers.abinit.AbinitParser',
)

ams_parser_entry_point = EntryPoint(
    name='parsers/ams',
    description='NOMAD parser for AMS.',
    python_package='electronicparsers.ams',
    mainfile_contents_re=r'\* +\| +A M S +\| +\*',
    parser_class_name='electronicparsers.ams.AMSParser',
)

atk_parser_entry_point = EntryPoint(
    name='parsers/atk',
    description='NOMAD parser for ATK.',
    python_package='electronicparsers.atk',
    mainfile_mime_re='application/octet-stream',
    mainfile_name_re=r'^.*\.nc',
    parser_class_name='electronicparsers.atk.ATKParser',
)

bigdft_parser_entry_point = EntryPoint(
    name='parsers/bigdft',
    description='NOMAD parser for BIGDFT.',
    python_package='electronicparsers.bigdft',
    mainfile_contents_re=r'\|_____\|__:__\|__:__\|_____\|_____\|___ BBBBB          i     g         g\s*',
    parser_class_name='electronicparsers.bigdft.BigDFTParser',
)

castep_parser_entry_point = EntryPoint(
    name='parsers/castep',
    description='NOMAD parser for CASTEP.',
    python_package='electronicparsers.castep',
    mainfile_contents_re=r'\s\|\s*CCC\s*AA\s*SSS\s*TTTTT\s*EEEEE\s*PPPP\s*\|\s*',
    parser_class_name='electronicparsers.castep.CastepParser',
)

charmm_parser_entry_point = EntryPoint(
    name='parsers/charmm',
    description='NOMAD parser for CHARMM.',
    python_package='electronicparsers.charmm',
    mainfile_contents_re=r'\s*Chemistry\s*at\s*HARvard\s*Macromolecular\s*Mechanics\s*',
    mainfile_mime_re='text/.*',
    parser_class_name='electronicparsers.charmm.CharmmParser',
)

cp2k_parser_entry_point = EntryPoint(
    name='parsers/cp2k',
    description='NOMAD parser for CP2K.',
    python_package='electronicparsers.cp2k',
    mainfile_contents_re=(r'\*\*\*\* \*\*\*\* \*\*\*\*\*\*  \*\*  PROGRAM STARTED '
        r'AT\s.*\n \*\*\*\*\* \*\* \*\*\*  \*\*\* \*\*   PROGRAM STARTED ON\s*.*\n \*\*    \*\*\*\*   \*\*\*\*\*\*    '
        r'PROGRAM STARTED BY .*\n \*\*\*\*\* \*\*    \*\* \*\* \*\*   PROGRAM PROCESS ID .*\n  \*\*\*\* '
        r'\*\*  \*\*\*\*\*\*\*  \*\*  PROGRAM STARTED IN .*\n'),
    parser_class_name='electronicparsers.cp2k.CP2KParser',
)

cpmd_parser_entry_point = EntryPoint(
    name='parsers/cpmd',
    description='NOMAD parser for CPMD.',
    python_package='electronicparsers.cpmd',
    mainfile_contents_re=r'\*\*\*       \*\*   \*\*\*  \*\* \*\*\*\* \*\*  \*\*   \*\*\*',
    parser_class_name='electronicparsers.cpmd.CPMDParser',
)

crystal_parser_entry_point = EntryPoint(
    name='parsers/crystal',
    description='NOMAD parser for CRYSTAL.',
    python_package='electronicparsers.crystal',
    mainfile_contents_re=r'(\r?\n \*\s+CRYSTAL[\d]+\s+\*\r?\n \*\s*[a-zA-Z]+ : \d+[\.\d+]*)',
    parser_class_name='electronicparsers.crystal.CrystalParser',
)

dmol3_parser_entry_point = EntryPoint(
    name='parsers/dmol3',
    description='NOMAD parser for DMOL3.',
    python_package='electronicparsers.dmol3',
    mainfile_contents_re=r'Materials Studio DMol\^3',
    mainfile_name_re=r'.*\.outmol',
    parser_class_name='electronicparsers.dmol3.Dmol3Parser',
)

edmft_parser_entry_point = EntryPoint(
    name='parsers/edmft',
    description='NOMAD parser for EDMFT.',
    python_package='electronicparsers.edmft',
    mainfile_contents_re=r'\-\-\-\s*Preparing GF calculation\s*\-\-\-',
    mainfile_name_re=r'^.*\.(out)$',
    parser_class_name='electronicparsers.edmft.EDMFTParser',
)

elk_parser_entry_point = EntryPoint(
    name='parsers/elk',
    description='NOMAD parser for ELK.',
    python_package='electronicparsers.elk',
    mainfile_contents_re=r'\| Elk version [0-9.a-zA-Z]+ started \|',
    parser_class_name='electronicparsers.elk.ElkParser',
)

exciting_parser_entry_point = EntryPoint(
    name='parsers/exciting',
    description='NOMAD parser for EXCITING.',
    python_package='electronicparsers.exciting',
    mainfile_contents_re=r'EXCITING.*started[\s\S]+?All units are atomic ',
    mainfile_name_re=r'^.*.OUT(\.[^/]*)?$',
    parser_class_name='electronicparsers.exciting.ExcitingParser',
)

fhiaims_parser_entry_point = EntryPoint(
    name='parsers/fhi-aims',
    description='NOMAD parser for FHIAIMS.',
    python_package='electronicparsers.fhiaims',
    mainfile_contents_re=r'^(.*\n)*?\s*Invoking FHI-aims \.\.\.',
    parser_class_name='electronicparsers.fhiaims.FHIAimsParser',
)

fleur_parser_entry_point = EntryPoint(
    name='parsers/fleur',
    description='NOMAD parser for FLEUR.',
    python_package='electronicparsers.fleur',
    mainfile_alternative=True,
    mainfile_contents_re=r'This output is generated by fleur.|\<fleurOutput',
    mainfile_mime_re='(application/.*)|(text/.*)',
    mainfile_name_re=r'.*[^/]*\.xml[^/]*',
    parser_class_name='electronicparsers.fleur.FleurParser',
)

fplo_parser_entry_point = EntryPoint(
    name='parsers/fplo',
    description='NOMAD parser for FPLO.',
    python_package='electronicparsers.fplo',
    mainfile_contents_re=(r'\s*\|\s*FULL-POTENTIAL LOCAL-ORBITAL MINIMUM BASIS BANDSTRUCTURE '
        r'CODE\s*\|\s*'),
    mainfile_mime_re='text/.*',
    parser_class_name='electronicparsers.fplo.FploParser',
)

gamess_parser_entry_point = EntryPoint(
    name='parsers/gamess',
    description='NOMAD parser for GAMESS.',
    python_package='electronicparsers.gamess',
    mainfile_contents_re=(r'\s*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\s*\s*\*\s*GAMESS '
        r'VERSION =\s*(.*)\*\s*\s*\*\s*FROM IOWA STATE UNIVERSITY\s*\*\s*'),
    parser_class_name='electronicparsers.gamess.GamessParser',
)

gaussian_parser_entry_point = EntryPoint(
    name='parsers/gaussian',
    description='NOMAD parser for GAUSSIAN.',
    python_package='electronicparsers.gaussian',
    mainfile_contents_re=r'\s*Cite this work as:\s*Gaussian [0-9]+, Revision [A-Za-z0-9\.]*,',
    mainfile_mime_re='.*',
    parser_class_name='electronicparsers.gaussian.GaussianParser',
)

gpaw_parser_entry_point = EntryPoint(
    name='parsers/gpaw',
    description='NOMAD parser for GPAW.',
    python_package='electronicparsers.gpaw',
    mainfile_mime_re='application/(x-tar|octet-stream)',
    mainfile_name_re=r'^.*\.(gpw2|gpw)$',
    parser_class_name='electronicparsers.gpaw.GPAWParser',
)

magres_parser_entry_point = EntryPoint(
    name='parsers/magres',
    description='NOMAD parser for MAGRES.',
    python_package='electronicparsers.magres',
    mainfile_contents_re=r'\$magres-abinitio-v(\d\.)+',
    mainfile_name_re=r'^.*\.magres',
    parser_class_name='electronicparsers.magres.MagresParser',
)

molcas_parser_entry_point = EntryPoint(
    name='parsers/molcas',
    description='NOMAD parser for MOLCAS.',
    python_package='electronicparsers.molcas',
    mainfile_contents_re=r'M O L C A S',
    parser_class_name='electronicparsers.molcas.MolcasParser',
)

mopac_parser_entry_point = EntryPoint(
    name='parsers/mopac',
    description='NOMAD parser for MOPAC.',
    python_package='electronicparsers.mopac',
    mainfile_contents_re=r'\s*\*\*\s*MOPAC\s*([0-9a-zA-Z\.]*)\s*\*\*\s*',
    mainfile_mime_re='text/.*',
    parser_class_name='electronicparsers.mopac.MopacParser',
)

nwchem_parser_entry_point = EntryPoint(
    name='parsers/nwchem',
    description='NOMAD parser for NWCHEM.',
    python_package='electronicparsers.nwchem',
    mainfile_contents_re=r'Northwest Computational Chemistry Package \(NWChem\) (\d+\.)+\d+',
    parser_class_name='electronicparsers.nwchem.NWChemParser',
)

ocean_parser_entry_point = EntryPoint(
    name='parsers/ocean',
    description='NOMAD parser for OCEAN.',
    python_package='electronicparsers.ocean',
    mainfile_contents_dict={'__has_all_keys': ['bse', 'structure', 'screen', 'calc']},
    mainfile_mime_re='(application/.*)|(text/.*)',
    parser_class_name='electronicparsers.ocean.OceanParser',
)

octopus_parser_entry_point = EntryPoint(
    name='parsers/octopus',
    description='NOMAD parser for OCTOPUS.',
    python_package='electronicparsers.octopus',
    mainfile_contents_re=r'\|0\) ~ \(0\) \|',
    parser_class_name='electronicparsers.octopus.OctopusParser',
)

onetep_parser_entry_point = EntryPoint(
    name='parsers/onetep',
    description='NOMAD parser for ONETEP.',
    python_package='electronicparsers.onetep',
    mainfile_contents_re=r'####### #     # ####### ####### ####### ######',
    parser_class_name='electronicparsers.onetep.OnetepParser',
)

openmx_parser_entry_point = EntryPoint(
    name='parsers/openmx',
    description='NOMAD parser for OPENMX.',
    python_package='electronicparsers.openmx',
    mainfile_contents_re=r'^\*{59}\s+\*{59}\s+This calculation was performed by OpenMX',
    mainfile_mime_re='(text/.*)',
    mainfile_name_re=r'.*\.out$',
    parser_class_name='electronicparsers.openmx.OpenmxParser',
)

orca_parser_entry_point = EntryPoint(
    name='parsers/orca',
    description='NOMAD parser for ORCA.',
    python_package='electronicparsers.orca',
    mainfile_contents_re=(r'\s+\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\s*\s+\* O   R   C   A '
        r'\*\s*\s+\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**\s*\s*'),
    parser_class_name='electronicparsers.orca.OrcaParser',
)

psi4_parser_entry_point = EntryPoint(
    name='parsers/psi4',
    description='NOMAD parser for PSI4.',
    python_package='electronicparsers.psi4',
    mainfile_contents_re=r'Psi4: An Open-Source Ab Initio Electronic Structure Package',
    parser_class_name='electronicparsers.psi4.Psi4Parser',
)

qball_parser_entry_point = EntryPoint(
    name='parsers/qball',
    description='NOMAD parser for QBALL.',
    python_package='electronicparsers.qball',
    mainfile_contents_re=r'qball',
    supported_compressions=['gz', 'bz2', 'xz'],
    parser_class_name='electronicparsers.qball.QBallParser',
)

qbox_parser_entry_point = EntryPoint(
    name='parsers/qbox',
    description='NOMAD parser for QBOX.',
    python_package='electronicparsers.qbox',
    mainfile_contents_re=r'http://qboxcode.org',
    mainfile_mime_re='(application/xml)|(text/.*)',
    parser_class_name='electronicparsers.qbox.QboxParser',
)

quantumespresso_parser_entry_point = EntryPoint(
    name='parsers/quantumespresso',
    description='NOMAD parser for QUANTUMESPRESSO.',
    python_package='electronicparsers.quantumespresso',
    mainfile_contents_re=(r'(Program PWSCF.*starts)|(Current dimensions of program '
        r'PWSCF are)'),
    supported_compressions=['gz', 'bz2', 'xz'],
    parser_class_name='electronicparsers.quantumespresso.QuantumEspressoParser',
)

siesta_parser_entry_point = EntryPoint(
    name='parsers/siesta',
    description='NOMAD parser for SIESTA.',
    python_package='electronicparsers.siesta',
    mainfile_contents_re=(r'(Siesta Version: siesta-|SIESTA [0-9]\.[0-9]\.[0-9])|(\*\s*WELCOME '
        r'TO SIESTA\s*\*)'),
    parser_class_name='electronicparsers.siesta.SiestaParser',
)

soliddmft_parser_entry_point = EntryPoint(
    name='parsers/soliddmft',
    description='NOMAD parser for SOLIDDMFT.',
    python_package='electronicparsers.soliddmft',
    mainfile_binary_header_re=b'^\\x89HDF',
    mainfile_contents_dict={'__has_all_keys': ['dft_input', 'DMFT_input', 'DMFT_results']},
    mainfile_mime_re='(application/x-hdf)',
    mainfile_name_re=r'^.*\.(h5|hdf5)$',
    parser_class_name='electronicparsers.soliddmft.SolidDMFTParser',
)

tbstudio_parser_entry_point = EntryPoint(
    name='parsers/tbstudio',
    description='NOMAD parser for TBSTUDIO.',
    python_package='electronicparsers.tbstudio',
    mainfile_contents_re=r'"ApplicationFullName": "Tight Binding Studio"',
    mainfile_mime_re='(application/json)|(text/.*)',
    mainfile_name_re=r'.*\.tbm',
    parser_class_name='electronicparsers.tbstudio.TBStudioParser',
)

turbomole_parser_entry_point = EntryPoint(
    name='parsers/turbomole',
    description='NOMAD parser for TURBOMOLE.',
    python_package='electronicparsers.turbomole',
    mainfile_contents_re=r'Copyright \(C\) [0-9]+ TURBOMOLE GmbH, Karlsruhe',
    parser_class_name='electronicparsers.turbomole.TurbomoleParser',
)

vasp_parser_entry_point = EntryPoint(
    name='parsers/vasp',
    description='NOMAD parser for VASP.',
    python_package='electronicparsers.vasp',
    mainfile_contents_re=(r'^\s*<\?xml version="1\.0" encoding="ISO-8859-1"\?>\s*?\s*<modeling>?\s*<generator>?\s*<i '
        r'name="program" type="string">\s*vasp\s*</i>?|^\svasp[\.\d]+.+?(?:\(build|complex)[\s\S]+?executed '
        r'on'),
    mainfile_mime_re='(application/.*)|(text/.*)',
    mainfile_name_re='.*[^/]*xml[^/]*',
    mainfile_alternative=True,
    supported_compressions=['gz', 'bz2', 'xz'],
    parser_class_name='electronicparsers.vasp.VASPParser',
)

w2dynamics_parser_entry_point = EntryPoint(
    name='parsers/w2dynamics',
    description='NOMAD parser for W2DYNAMICS.',
    python_package='electronicparsers.w2dynamics',
    mainfile_binary_header_re=b'^\\x89HDF',
    mainfile_contents_dict={'__has_all_keys': ['.axes', '.config', '.quantities']},
    mainfile_mime_re='(application/x-hdf)',
    mainfile_name_re=r'^.*\.(h5|hdf5)$',
    parser_class_name='electronicparsers.w2dynamics.W2DynamicsParser',
)

wannier90_parser_entry_point = EntryPoint(
    name='parsers/wannier90',
    description='NOMAD parser for WANNIER90.',
    python_package='electronicparsers.wannier90',
    mainfile_contents_re=r'\|\s*WANNIER90\s*\|',
    parser_class_name='electronicparsers.wannier90.Wannier90Parser',
)

wien2k_parser_entry_point = EntryPoint(
    name='parsers/wien2k',
    description='NOMAD parser for WIEN2K.',
    python_package='electronicparsers.wien2k',
    mainfile_contents_re=r'\s*---------\s*:ITE[0-9]+:\s*[0-9]+\.\s*ITERATION\s*---------',
    mainfile_name_re=r'.*\.scf$',
    mainfile_alternative=True,
    parser_class_name='electronicparsers.wien2k.Wien2kParser',
)

yambo_parser_entry_point = EntryPoint(
    name='parsers/yambo',
    description='NOMAD parser for YAMBO.',
    python_package='electronicparsers.yambo',
    mainfile_contents_re=r'Build.+\s+http://www\.yambo-code\.org',
    parser_class_name='electronicparsers.yambo.YamboParser',
)
