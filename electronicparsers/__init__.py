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
from nomad.config.models.plugins import ParserEntryPoint


class EntryPoint(ParserEntryPoint):
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

        return MatchingParserInterface(self.parser_class_name)


abacus_parser_entry_point = EntryPoint(
    name='parsers/abacus',
    description='NOMAD parser for ABACUS.',
    parser_class_name='electronicparsers.abacus.ABACUSParser',
)

abinit_parser_entry_point = EntryPoint(
    name='parsers/abinit',
    description='NOMAD parser for ABINIT.',
    parser_class_name='electronicparsers.abinit.AbinitParser',
)

ams_parser_entry_point = EntryPoint(
    name='parsers/ams',
    description='NOMAD parser for AMS.',
    parser_class_name='electronicparsers.ams.AMSParser',
)

atk_parser_entry_point = EntryPoint(
    name='parsers/atk',
    description='NOMAD parser for ATK.',
    parser_class_name='electronicparsers.atk.ATKParser',
)

bigdft_parser_entry_point = EntryPoint(
    name='parsers/bigdft',
    description='NOMAD parser for BIGDFT.',
    parser_class_name='electronicparsers.bigdft.BigDFTParser',
)

castep_parser_entry_point = EntryPoint(
    name='parsers/castep',
    description='NOMAD parser for CASTEP.',
    parser_class_name='electronicparsers.castep.CastepParser',
)

charmm_parser_entry_point = EntryPoint(
    name='parsers/charmm',
    description='NOMAD parser for CHARMM.',
    parser_class_name='electronicparsers.charmm.CharmmParser',
)

cp2k_parser_entry_point = EntryPoint(
    name='parsers/cp2k',
    description='NOMAD parser for CP2K.',
    parser_class_name='electronicparsers.cp2k.CP2KParser',
)

cpmd_parser_entry_point = EntryPoint(
    name='parsers/cpmd',
    description='NOMAD parser for CPMD.',
    parser_class_name='electronicparsers.cpmd.CPMDParser',
)

crystal_parser_entry_point = EntryPoint(
    name='parsers/crystal',
    description='NOMAD parser for CRYSTAL.',
    parser_class_name='electronicparsers.crystal.CrystalParser',
)

dmol3_parser_entry_point = EntryPoint(
    name='parsers/dmol3',
    description='NOMAD parser for DMOL3.',
    parser_class_name='electronicparsers.dmol3.Dmol3Parser',
)

edmft_parser_entry_point = EntryPoint(
    name='parsers/edmft',
    description='NOMAD parser for EDMFT.',
    parser_class_name='electronicparsers.edmft.EDMFTParser',
)

elk_parser_entry_point = EntryPoint(
    name='parsers/elk',
    description='NOMAD parser for ELK.',
    parser_class_name='electronicparsers.elk.ElkParser',
)

exciting_parser_entry_point = EntryPoint(
    name='parsers/exciting',
    description='NOMAD parser for EXCITING.',
    parser_class_name='electronicparsers.exciting.ExcitingParser',
)

fhiaims_parser_entry_point = EntryPoint(
    name='parsers/fhi-aims',
    description='NOMAD parser for FHIAIMS.',
    parser_class_name='electronicparsers.fhiaims.FHIAimsParser',
)

fleur_parser_entry_point = EntryPoint(
    name='parsers/fleur',
    description='NOMAD parser for FLEUR.',
    parser_class_name='electronicparsers.fleur.FleurParser',
)

fplo_parser_entry_point = EntryPoint(
    name='parsers/fplo',
    description='NOMAD parser for FPLO.',
    parser_class_name='electronicparsers.fplo.FploParser',
)

gamess_parser_entry_point = EntryPoint(
    name='parsers/gamess',
    description='NOMAD parser for GAMESS.',
    parser_class_name='electronicparsers.gamess.GamessParser',
)

gaussian_parser_entry_point = EntryPoint(
    name='parsers/gaussian',
    description='NOMAD parser for GAUSSIAN.',
    parser_class_name='electronicparsers.gaussian.GaussianParser',
)

gpaw_parser_entry_point = EntryPoint(
    name='parsers/gpaw',
    description='NOMAD parser for GPAW.',
    parser_class_name='electronicparsers.gpaw.GPAWParser',
)

magres_parser_entry_point = EntryPoint(
    name='parsers/magres',
    description='NOMAD parser for MAGRES.',
    parser_class_name='electronicparsers.magres.MagresParser',
)

molcas_parser_entry_point = EntryPoint(
    name='parsers/molcas',
    description='NOMAD parser for MOLCAS.',
    parser_class_name='electronicparsers.molcas.MolcasParser',
)

mopac_parser_entry_point = EntryPoint(
    name='parsers/mopac',
    description='NOMAD parser for MOPAC.',
    parser_class_name='electronicparsers.mopac.MopacParser',
)

nwchem_parser_entry_point = EntryPoint(
    name='parsers/nwchem',
    description='NOMAD parser for NWCHEM.',
    parser_class_name='electronicparsers.nwchem.NWChemParser',
)

ocean_parser_entry_point = EntryPoint(
    name='parsers/ocean',
    description='NOMAD parser for OCEAN.',
    parser_class_name='electronicparsers.ocean.OceanParser',
)

octopus_parser_entry_point = EntryPoint(
    name='parsers/octopus',
    description='NOMAD parser for OCTOPUS.',
    parser_class_name='electronicparsers.octopus.OctopusParser',
)

onetep_parser_entry_point = EntryPoint(
    name='parsers/onetep',
    description='NOMAD parser for ONETEP.',
    parser_class_name='electronicparsers.onetep.OnetepParser',
)

openmx_parser_entry_point = EntryPoint(
    name='parsers/openmx',
    description='NOMAD parser for OPENMX.',
    parser_class_name='electronicparsers.openmx.OpenmxParser',
)

orca_parser_entry_point = EntryPoint(
    name='parsers/orca',
    description='NOMAD parser for ORCA.',
    parser_class_name='electronicparsers.orca.OrcaParser',
)

psi4_parser_entry_point = EntryPoint(
    name='parsers/psi4',
    description='NOMAD parser for PSI4.',
    parser_class_name='electronicparsers.psi4.Psi4Parser',
)

qball_parser_entry_point = EntryPoint(
    name='parsers/qball',
    description='NOMAD parser for QBALL.',
    parser_class_name='electronicparsers.qball.QBallParser',
)

qbox_parser_entry_point = EntryPoint(
    name='parsers/qbox',
    description='NOMAD parser for QBOX.',
    parser_class_name='electronicparsers.qbox.QboxParser',
)

quantumespresso_parser_entry_point = EntryPoint(
    name='parsers/quantumespresso',
    description='NOMAD parser for QUANTUMESPRESSO.',
    parser_class_name='electronicparsers.quantumespresso.QuantumEspressoParser',
)

siesta_parser_entry_point = EntryPoint(
    name='parsers/siesta',
    description='NOMAD parser for SIESTA.',
    parser_class_name='electronicparsers.siesta.SiestaParser',
)

soliddmft_parser_entry_point = EntryPoint(
    name='parsers/soliddmft',
    description='NOMAD parser for SOLIDDMFT.',
    parser_class_name='electronicparsers.soliddmft.SolidDMFTParser',
)

tbstudio_parser_entry_point = EntryPoint(
    name='parsers/tbstudio',
    description='NOMAD parser for TBSTUDIO.',
    parser_class_name='electronicparsers.tbstudio.TBStudioParser',
)

turbomole_parser_entry_point = EntryPoint(
    name='parsers/turbomole',
    description='NOMAD parser for TURBOMOLE.',
    parser_class_name='electronicparsers.turbomole.TurbomoleParser',
)

vasp_parser_entry_point = EntryPoint(
    name='parsers/vasp',
    description='NOMAD parser for VASP.',
    parser_class_name='electronicparsers.vasp.VASPParser',
)

w2dynamics_parser_entry_point = EntryPoint(
    name='parsers/w2dynamics',
    description='NOMAD parser for W2DYNAMICS.',
    parser_class_name='electronicparsers.w2dynamics.W2DynamicsParser',
)

wannier90_parser_entry_point = EntryPoint(
    name='parsers/wannier90',
    description='NOMAD parser for WANNIER90.',
    parser_class_name='electronicparsers.wannier90.Wannier90Parser',
)

wien2k_parser_entry_point = EntryPoint(
    name='parsers/wien2k',
    description='NOMAD parser for WIEN2K.',
    parser_class_name='electronicparsers.wien2k.Wien2kParser',
)

yambo_parser_entry_point = EntryPoint(
    name='parsers/yambo',
    description='NOMAD parser for YAMBO.',
    parser_class_name='electronicparsers.yambo.YamboParser',
)
