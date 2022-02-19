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
import numpy as np            # pylint: disable=unused-import
import typing                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_siesta_input(MCategory):
    '''
    siesta input variables
    '''

    m_def = Category()


class x_siesta_section_input(MSection):
    '''
    input section
    '''

    m_def = Section(validate=False)

    x_siesta_input_endblock = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "%endblock"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Atom_Setup_Only = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Atom-Setup-Only"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Atom_Debug_KB_Generation = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Atom.Debug.KB.Generation"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_AtomCoorFormatOut = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "AtomCoorFormatOut"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_AtomLeftVcte = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "AtomLeftVcte"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_AtomRightVcte = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "AtomRightVcte"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_AtomicCoordinatesFormat = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "AtomicCoordinatesFormat"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BasisPressure = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BasisPressure"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BornCharge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BornCharge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BuildSuperCell = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BuildSuperCell"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BulkLead = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BulkLead"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BulkTransport = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BulkTransport"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BulkTransvCellSize = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BulkTransvCellSize"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BulkTransvCellSizeX = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BulkTransvCellSizeX"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BulkTransvCellSizeY = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BulkTransvCellSizeY"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_BulkTransvCellSizeZ = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "BulkTransvCellSizeZ"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_CB_MaxKappa = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "CB.MaxKappa"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_CB_WriteComplexBands = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "CB.WriteComplexBands"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_CDFT = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "CDFT"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_CDFT_MaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "CDFT.MaxIter"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_COOP_Write = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "COOP.Write"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_CalcIETS = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "CalcIETS"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_CalcMPSH = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "CalcMPSH"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ChangeKgridInMD = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ChangeKgridInMD"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Compat_pre_v4_DM_H = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Compat-pre-v4-DM-H"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_AllowExtrapolation = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.AllowExtrapolation"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_AllowReuse = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.AllowReuse"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_EnergyTolerance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.EnergyTolerance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_FIRE_Mixing = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.FIRE.Mixing"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_FormattedFiles = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.FormattedFiles"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_FormattedInput = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.FormattedInput"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_FormattedOutput = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.FormattedOutput"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_HarrisTolerance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.HarrisTolerance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_KickMixingWeight = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.KickMixingWeight"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_MixSCF1 = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.MixSCF1"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_MixingWeight = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.MixingWeight"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_NormalizationTolerance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.NormalizationTolerance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_NormalizeDuringSCF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.NormalizeDuringSCF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_NumberBroyden = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.NumberBroyden"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_NumberKick = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.NumberKick"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_NumberPulay = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.NumberPulay"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_OccupancyTolerance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.OccupancyTolerance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_Pulay_Avoid_First_After_Kick = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.Pulay.Avoid.First.After.Kick"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_PulayOnFile = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.PulayOnFile"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_RequireEnergyConvergence = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.RequireEnergyConvergence"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_RequireHarrisConvergence = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.RequireHarrisConvergence"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_Tolerance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.Tolerance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DM_UseSaveDM = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DM.UseSaveDM"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Delta = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Delta"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DeltaWorkfunction = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DeltaWorkfunction"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Diag_AllInOne = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Diag.AllInOne"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Diag_DivideAndConquer = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Diag.DivideAndConquer"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Diag_Memory = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Diag.Memory"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Diag_NoExpert = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Diag.NoExpert"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Diag_ParallelOverK = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Diag.ParallelOverK"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Diag_PreRotate = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Diag.PreRotate"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Diag_Use2D = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Diag.Use2D"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DiagMemory = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DiagMemory"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DiagScale = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DiagScale"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DirectPhi = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DirectPhi"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_DivideAndConquer = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "DivideAndConquer"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_AddRhoGate = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.AddRhoGate"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_AddVgIsolatedLocalCharges = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.AddVgIsolatedLocalCharges"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_COOPCalculate = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.COOPCalculate"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_COOPNumberOfBonds = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.COOPNumberOfBonds"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_DebugRhoGate = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.DebugRhoGate"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_NetRhoGateCharge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.NetRhoGateCharge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_PrintLimits = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.PrintLimits"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_RhoGateLxMax = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.RhoGateLxMax"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_RhoGateLxMin = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.RhoGateLxMin"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_RhoGateLyMax = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.RhoGateLyMax"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_RhoGateLyMin = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.RhoGateLyMin"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_RhoGateLzMax = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.RhoGateLzMax"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_RhoGateLzMin = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.RhoGateLzMin"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_TRCAddVCDFT = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.TRCAddVCDFT"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_TimeReversal = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.TimeReversal"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_Timings = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.Timings"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EM_addV = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EM.addV"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EMPDOSKSO = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EMPDOSKSO"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EMTransport = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EMTransport"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ElectronicTemperature = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ElectronicTemperature"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_EnergLowestBound = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "EnergLowestBound"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_FilterCutoff = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "FilterCutoff"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_FilterTol = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "FilterTol"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_FinalTransmRange = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "FinalTransmRange"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_FixAuxiliaryCell = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "FixAuxiliaryCell"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_FixAuxillaryCell = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "FixAuxillaryCell"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_FixSpin = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "FixSpin"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ForceAuxCell = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ForceAuxCell"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_FullRamp = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "FullRamp"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_HSetupOnly = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "HSetupOnly"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Harris_functional = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Harris_functional"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_HartreeLeadsBottom = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "HartreeLeadsBottom"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_HartreeLeadsLeft = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "HartreeLeadsLeft"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_HartreeLeadsRight = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "HartreeLeadsRight"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Ik_Select = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Ik_Select"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_InitTransmRange = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "InitTransmRange"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_InitTransport = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "InitTransport"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_KB_New_Reference_Orbitals = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "KB.New.Reference.Orbitals"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_KB_Rmax = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "KB.Rmax"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_LDAU_units = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "LDAU.units"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_LDAUForces = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "LDAUForces"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_LDAU_METHOD = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "LDAU_METHOD"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_LatticeConstant = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "LatticeConstant"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_LongOutput = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "LongOutput"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_AnnealOption = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.AnnealOption"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_BulkModulus = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.BulkModulus"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCAcousticSumRule = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCAcousticSumRule"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCAtomRestart = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCAtomRestart"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCAxisRestart = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCAxisRestart"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCDispl = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCDispl"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCEigenVectors = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCEigenVectors"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCIR = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCIR"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCRead = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCRead"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FCfirst = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FCfirst"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FClast = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FClast"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FinalTimeStep = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FinalTimeStep"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_FireQuench = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.FireQuench"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_InitialTemperature = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.InitialTemperature"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_InitialTimeStep = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.InitialTimeStep"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_LengthTimeStep = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.LengthTimeStep"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_MaxCGDispl = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.MaxCGDispl"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_MaxForceTol = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.MaxForceTol"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_MaxStressTol = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.MaxStressTol"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_NoseMass = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.NoseMass"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_NumCGsteps = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.NumCGsteps"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_NumNEBsteps = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.NumNEBsteps"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_ParrinelloRahmanMass = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.ParrinelloRahmanMass"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_Quench = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.Quench"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_RelaxCellOnly = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.RelaxCellOnly"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_RemoveIntraMolecularPressure = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.RemoveIntraMolecularPressure"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_TRCSampling = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.TRCSampling"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_TRCSkip = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.TRCSkip"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_TargetPressure = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.TargetPressure"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_TargetTemperature = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.TargetTemperature"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_TauRelax = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.TauRelax"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_Timing = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.Timing"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_TypeOfRun = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.TypeOfRun"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_UseSaveCG = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.UseSaveCG"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_UseSaveNEB = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.UseSaveNEB"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_UseSaveXV = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.UseSaveXV"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_UseSaveZM = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.UseSaveZM"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_UseStructFile = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.UseStructFile"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MD_VariableCell = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MD.VariableCell"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MM_Cutoff = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MM.Cutoff"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MM_UnitsDistance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MM.UnitsDistance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MM_UnitsEnergy = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MM.UnitsEnergy"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MPSHAtomFirst = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MPSHAtomFirst"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MPSHAtomLast = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MPSHAtomLast"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MPSHOrbFirst = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MPSHOrbFirst"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MPSHOrbLast = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MPSHOrbLast"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MaxBondDistance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MaxBondDistance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MaxSCFIterations = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MaxSCFIterations"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MeshCutoff = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MeshCutoff"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MeshSubDivisions = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MeshSubDivisions"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MinSCFIterations = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MinSCFIterations"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MixCharge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MixCharge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MixHamiltonian = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MixHamiltonian"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MixedParallel = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MixedParallel"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MonitorForcesInSCF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MonitorForcesInSCF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_MullikenInSCF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "MullikenInSCF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NC_OrbitalRotationEnd = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NC.OrbitalRotationEnd"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NC_OrbitalRotationStart = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NC.OrbitalRotationStart"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NEB_SkipEdge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NEB.SkipEdge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NEnergReal = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NEnergReal"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NIVPoints = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NIVPoints"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NPoles = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NPoles"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NSlices = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NSlices"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NTransmPoints = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NTransmPoints"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NaiveAuxiliaryCell = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NaiveAuxiliaryCell"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NeglNonOverlapInt = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NeglNonOverlapInt"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NenergImCircle = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NenergImCircle"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NenergImLine = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NenergImLine"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NetCharge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NetCharge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NonCollinearSpin = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NonCollinearSpin"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NumSkipWriteDM = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NumSkipWriteDM"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NumberLinearMix = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NumberLinearMix"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NumberOfAtoms = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NumberOfAtoms"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NumberOfEigenStates = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NumberOfEigenStates"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_NumberOfSpecies = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "NumberOfSpecies"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Number_of_species = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Number_of_species"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_ChemicalPotential = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.ChemicalPotential"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_ChemicalPotentialOrder = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.ChemicalPotentialOrder"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_ChemicalPotentialRc = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.ChemicalPotentialRc"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_ChemicalPotentialTemperature = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.ChemicalPotentialTemperature"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_ChemicalPotentialUse = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.ChemicalPotentialUse"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_MaxNumIter = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.MaxNumIter"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_UseSaveLWF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.UseSaveLWF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_eta = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.eta"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_eta_alpha = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.eta_alpha"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_eta_beta = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.eta_beta"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_etol = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.etol"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ON_functional = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ON.functional"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_OccupationFunction = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "OccupationFunction"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_On_RcLWF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "On.RcLWF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_OpticalCalculation = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "OpticalCalculation"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Optim_Broyden = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Optim.Broyden"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Output_Structure_Only = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Output-Structure-Only"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_BasisSize = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.BasisSize"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_BasisType = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.BasisType"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_EnergyShift = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.EnergyShift"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_Filter = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.Filter"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_FixSplitTable = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.FixSplitTable"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_Keep_Findp_Bug = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.Keep.Findp.Bug"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_NewSplitCode = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.NewSplitCode"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_OldStylePolorbs = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.OldStylePolorbs"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_SoftDefault = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.SoftDefault"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_SoftInnerRadius = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.SoftInnerRadius"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_SoftPotential = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.SoftPotential"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_SplitNorm = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.SplitNorm"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_SplitNormH = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.SplitNormH"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PAO_SplitTailNorm = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PAO.SplitTailNorm"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PS_SIC = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PS.SIC"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ParallelOverK = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ParallelOverK"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PartialChargesAtEveryGeometry = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PartialChargesAtEveryGeometry"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PartialChargesAtEveryScfStep = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PartialChargesAtEveryScfStep"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_PoissonMultigrid = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "PoissonMultigrid"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Print_ldau = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Print_ldau"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ProcessorGridX = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ProcessorGridX"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ProcessorGridY = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ProcessorGridY"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ProcessorGridZ = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ProcessorGridZ"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ProjectionInSCF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ProjectionInSCF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ProjectionMethod = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ProjectionMethod"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_RcSpatial = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "RcSpatial"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ReInitialiseDM = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ReInitialiseDM"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ReadHamiltonian = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ReadHamiltonian"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ReadKPIN = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ReadKPIN"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ReparametrizePseudos = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ReparametrizePseudos"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Restricted_Radial_Grid = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Restricted.Radial.Grid"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Rmax_Radial_Grid = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Rmax.Radial.Grid"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_RotateSpin_Phi = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "RotateSpin.Phi"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_RotateSpin_Theta = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "RotateSpin.Theta"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_LinearMixingAfterPulay = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.LinearMixingAfterPulay"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_MixAfterConvergence = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.MixAfterConvergence"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_MixingWeightAfterPulay = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.MixingWeightAfterPulay"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Pulay_Damping = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Pulay.Damping"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Pulay_DebugSVD = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Pulay.DebugSVD"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Pulay_RcondSVD = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Pulay.RcondSVD"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Pulay_UseSVD = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Pulay.UseSVD"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_PulayDmaxRegion = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.PulayDmaxRegion"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_PulayMinimumHistory = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.PulayMinimumHistory"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Read_Charge_NetCDF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Read.Charge.NetCDF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Read_Deformation_Charge_NetCDF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Read.Deformation.Charge.NetCDF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Recompute_H_After_Scf = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Recompute-H-After-Scf"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCF_Want_Variational_EKS = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCF.Want.Variational.EKS"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SCFMustConverge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SCFMustConverge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_Flavour = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.Flavour"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_Lambda = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.Lambda"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_NoRelaxation = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.NoRelaxation"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_Npop = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.Npop"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_PopDMConv = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.PopDMConv"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_PopKgridFactor = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.PopKgridFactor"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_PopSmatSparsity = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.PopSmatSparsity"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_ProjectionMode = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.ProjectionMode"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_ProjectionType = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.ProjectionType"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SIC_Rot_Inv = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SIC.Rot_Inv"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_STT_Calculation = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "STT.Calculation"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_STT_LinearResponse = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "STT.LinearResponse"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveBaderCharge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveBaderCharge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveDeltaRho = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveDeltaRho"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveElectrostaticPotential = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveElectrostaticPotential"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveHS = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveHS"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveInitialChargeDensity = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveInitialChargeDensity"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveIonicCharge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveIonicCharge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveNeutralAtomPotential = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveNeutralAtomPotential"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveRho = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveRho"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveRhoXC = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveRhoXC"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveTotalCharge = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveTotalCharge"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SaveTotalPotential = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SaveTotalPotential"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Scissor_Operator = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Scissor.Operator"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SetBulkTransvCell = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SetBulkTransvCell"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Siesta2Wannier90_NumberOfBands = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Siesta2Wannier90.NumberOfBands"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Siesta2Wannier90_NumberOfBandsDown = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Siesta2Wannier90.NumberOfBandsDown"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Siesta2Wannier90_NumberOfBandsUp = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Siesta2Wannier90.NumberOfBandsUp"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Siesta2Wannier90_WriteAmn = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Siesta2Wannier90.WriteAmn"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Siesta2Wannier90_WriteEig = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Siesta2Wannier90.WriteEig"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Siesta2Wannier90_WriteMmn = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Siesta2Wannier90.WriteMmn"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Siesta2Wannier90_WriteUnk = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Siesta2Wannier90.WriteUnk"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Sigma_DSigmaDE = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Sigma.DSigmaDE"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SignatureRecords = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SignatureRecords"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SimulateDoping = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SimulateDoping"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SingleExcitation = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SingleExcitation"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SkipLastIter = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SkipLastIter"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SlabDipoleCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SlabDipoleCorrection"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SolutionMethod = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SolutionMethod"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SpinConfLeads = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SpinConfLeads"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SpinOrbit = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SpinOrbit"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SpinPolarized = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SpinPolarized"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SystemLabel = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SystemLabel"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_SystemName = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "SystemName"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_TS_MixH = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "TS.MixH"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_TimeReversal = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "TimeReversal"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_TimeReversalSymmetryForKpoints = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "TimeReversalSymmetryForKpoints"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_TrCoefficients = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "TrCoefficients"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_TryMemoryIncrease = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "TryMemoryIncrease"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_UseDomainDecomposition = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "UseDomainDecomposition"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_UseNewDiagk = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "UseNewDiagk"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_UseSaveData = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "UseSaveData"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_UseSpatialDecomposition = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "UseSpatialDecomposition"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_UseStructFile = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "UseStructFile"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_UseTreeTimer = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "UseTreeTimer"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_VFinal = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "VFinal"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_VGate = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "VGate"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_VInitial = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "VInitial"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_Vna_Filter = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "Vna.Filter"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WarningMinimumAtomicDistance = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WarningMinimumAtomicDistance"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteBands = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteBands"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteCoorCerius = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteCoorCerius"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteCoorInitial = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteCoorInitial"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteCoorStep = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteCoorStep"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteCoorXmol = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteCoorXmol"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDM = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDM"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDM_History_NetCDF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDM.History.NetCDF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDM_NetCDF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDM.NetCDF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDMHS_History_NetCDF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDMHS.History.NetCDF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDMHS_NetCDF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDMHS.NetCDF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDMT = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDMT"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDenchar = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDenchar"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteDiagdS = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteDiagdS"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteEDM = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteEDM"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteEigenvalues = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteEigenvalues"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteForces = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteForces"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteHSDeriv = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteHSDeriv"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteHamiltonPop = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteHamiltonPop"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteHirshfeldPop = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteHirshfeldPop"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteIonPlotFiles = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteIonPlotFiles"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteKbands = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteKbands"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteKpoints = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteKpoints"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteMDXmol = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteMDXmol"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteMDhistory = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteMDhistory"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteMullikenPop = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteMullikenPop"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteProjections = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteProjections"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteSpinMulliken = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteSpinMulliken"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteSpinSCF = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteSpinSCF"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteVNA = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteVNA"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteVoronoiPop = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteVoronoiPop"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_WriteWaveFunctions = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "WriteWaveFunctions"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_XML_AbortOnErrors = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "XML.AbortOnErrors"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_XML_AbortOnWarnings = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "XML.AbortOnWarnings"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_XML_Write = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "XML.Write"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZBroadeningG = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZBroadeningG"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZLeftVcte = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZLeftVcte"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZM_CalcAllForces = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZM.CalcAllForces"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZM_ForceTolAngle = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZM.ForceTolAngle"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZM_ForceTolLength = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZM.ForceTolLength"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZM_MaxDisplAngle = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZM.MaxDisplAngle"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZM_MaxDisplLength = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZM.MaxDisplLength"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZM_UnitsAngle = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZM.UnitsAngle"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZM_UnitsLength = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZM.UnitsLength"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZRightVcte = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZRightVcte"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZVGateL = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZVGateL"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZVGateR = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZVGateR"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZeemanTermBx = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZeemanTermBx"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZeemanTermBy = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZeemanTermBy"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_ZeemanTermBz = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "ZeemanTermBz"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_alloc_report_level = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "alloc_report_level"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_alloc_report_threshold = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "alloc_report_threshold"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_blocksize = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "blocksize"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_compat_pre_v4_dynamics = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "compat-pre-v4-dynamics"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_fdf_debug = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "fdf-debug"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_kgrid_cutoff = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "kgrid_cutoff"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_processorY = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "processorY"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_timer_report_threshold = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "timer_report_threshold"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_user_basis = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "user-basis"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_user_basis_netcdf = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "user-basis-netcdf"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_xc_authors = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "xc.authors"
        ''',
        categories=[x_siesta_input])

    x_siesta_input_xc_functional = Quantity(
        type=str,
        shape=[],
        description='''
        siesta input variable "xc.functional"
        ''',
        categories=[x_siesta_input])


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_siesta_section_input = SubSection(
        sub_section=SectionProxy('x_siesta_section_input'),
        repeats=True)
