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


class x_octopus_input(MCategory):
    '''
    section describing Octopus input parameters
    '''

    m_def = Category()


class x_octopus_parserlog(MCategory):
    '''
    section describing Octopus inputfile parser log output
    '''

    m_def = Category()


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_octopus_input_ABCapHeight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ABCapHeight" of type "float" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ABShape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ABShape" of type "block" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_AbsorbingBoundaries = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "AbsorbingBoundaries" of type "flag" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ABWidth = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ABWidth" of type "float" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_AlphaFMM = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "AlphaFMM" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_AnimationMultiFiles = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "AnimationMultiFiles" of type "logical" in section
        "Utilities::oct-xyz-anim"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_AnimationSampling = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "AnimationSampling" of type "integer" in section
        "Utilities::oct-xyz-anim"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ArpackInitialTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ArpackInitialTolerance" of type "float" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_AtomsMagnetDirection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "AtomsMagnetDirection" of type "block" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_AxisType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "AxisType" of type "integer" in section "Utilities::oct-
        center-geom"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_CalcDipoleMtxels = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_CalcDipoleMtxels" of type "logical" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_CalcExchange = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_CalcExchange" of type "logical" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_NumberBands = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_NumberBands" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_VmtxelNumCondBands = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_VmtxelNumCondBands" of type "integer" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_VmtxelNumValBands = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_VmtxelNumValBands" of type "integer" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_VmtxelPolarization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_VmtxelPolarization" of type "block" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_Vxc_diag_nmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_Vxc_diag_nmax" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_Vxc_diag_nmin = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_Vxc_diag_nmin" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_Vxc_offdiag_nmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_Vxc_offdiag_nmax" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_Vxc_offdiag_nmin = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_Vxc_offdiag_nmin" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BerkeleyGW_WFN_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BerkeleyGW_WFN_filename" of type "string" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BornChargeSumRuleCorrection = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "BornChargeSumRuleCorrection" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BoxShapeImage = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BoxShapeImage" of type "string" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BoxShapeUsDef = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BoxShapeUsDef" of type "string" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_BoxShape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "BoxShape" of type "integer" in section "Mesh::Simulation
        Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CalcEigenvalues = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CalcEigenvalues" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CalcInfrared = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CalcInfrared" of type "logical" in section "Linear
        Response::Vibrational Modes"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CalcNormalModeWfs = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CalcNormalModeWfs" of type "logical" in section "Linear
        Response::Vibrational Modes"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CalculateSelfInducedMagneticField = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CalculateSelfInducedMagneticField" of type "logical" in
        section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CalculationMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CalculationMode" of type "integer" in section
        "Calculation Modes"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaCalcForcesKernel = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CasidaCalcForcesKernel" of type "logical" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaCalcForcesSCF = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CasidaCalcForcesSCF" of type "logical" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaCalcForces = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CasidaCalcForces" of type "logical" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaCalcTriplet = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CasidaCalcTriplet" of type "logical" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaHermitianConjugate = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "CasidaHermitianConjugate" of type "logical" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaKohnShamStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CasidaKohnShamStates" of type "string" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaKSEnergyWindow = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CasidaKSEnergyWindow" of type "float" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaMomentumTransfer = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CasidaMomentumTransfer" of type "block" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaQuadratureOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CasidaQuadratureOrder" of type "integer" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaSpectrumBroadening = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CasidaSpectrumBroadening" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaSpectrumEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CasidaSpectrumEnergyStep" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaSpectrumMaxEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CasidaSpectrumMaxEnergy" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaSpectrumMinEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CasidaSpectrumMinEnergy" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaSpectrumRotationMatrix = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CasidaSpectrumRotationMatrix" of type "block" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaTheoryLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CasidaTheoryLevel" of type "flag" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CasidaTransitionDensities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CasidaTransitionDensities" of type "string" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ClassicalPotential = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ClassicalPotential" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingAlphaLeft = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingAlphaLeft" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingAlpha" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingLocalizationRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingLocalizationRadius" of type "float" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingLocalizationThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingLocalizationThreshold" of type "float" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingLocalizedStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingLocalizedStates" of type "integer" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingPenalizationFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingPenalizationFactor" of type "float" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingRotateSpectrum = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingRotateSpectrum" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScalingTheta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ComplexScalingTheta" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ComplexScaling = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ComplexScaling" of type "flag" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConductivityFromForces = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ConductivityFromForces" of type "logical" in section
        "Utilities::oct-conductivity_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConductivitySpectrumTimeStepFactor = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConductivitySpectrumTimeStepFactor" of type "integer" in
        section "Utilities::oct-conductivity_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvAbsDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvAbsDens" of type "float" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvAbsEv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvAbsEv" of type "float" in section "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvEigenError = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ConvEigenError" of type "logical" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvEnergy" of type "float" in section "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertEnd = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertEnd" of type "integer" in section "Utilities::oct-
        convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertEnergyMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvertEnergyMax" of type "float" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertEnergyMin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvertEnergyMin" of type "float" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvertEnergyStep" of type "float" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertFilename" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertFolder" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertFTMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertFTMethod" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertHow = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertHow" of type "integer" in section "Utilities::oct-
        convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertIterateFolder = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ConvertIterateFolder" of type "logical" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertOutputFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertOutputFilename" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertOutputFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertOutputFolder" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertReadSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertReadSize" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertScalarOperation = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertScalarOperation" of type "block" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertStart" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertStep = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertStep" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertSubtractFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertSubtractFilename" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertSubtractFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ConvertSubtractFolder" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvertSubtract = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ConvertSubtract" of type "logical" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvForce = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvForce" of type "float" in section "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvRelDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvRelDens" of type "float" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ConvRelEv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ConvRelEv" of type "float" in section "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Coordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Coordinates" of type "block" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurrentDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CurrentDensity" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurrentThroughPlane = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CurrentThroughPlane" of type "block" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvGygiAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CurvGygiAlpha" of type "float" in section
        "Mesh::Curvilinear::Gygi"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvGygiA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CurvGygiA" of type "float" in section
        "Mesh::Curvilinear::Gygi"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvGygiBeta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CurvGygiBeta" of type "float" in section
        "Mesh::Curvilinear::Gygi"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "CurvMethod" of type "integer" in section
        "Mesh::Curvilinear"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvModineJBar = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CurvModineJBar" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvModineJlocal = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CurvModineJlocal" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvModineJrange = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CurvModineJrange" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_CurvModineXBar = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "CurvModineXBar" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Debug = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Debug" of type "flag" in section "Execution::Debug"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DegeneracyThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "DegeneracyThreshold" of type "float" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DeltaEFMM = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "DeltaEFMM" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DensitytoCalc = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "DensitytoCalc" of type "block" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DerivativesOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "DerivativesOrder" of type "integer" in section
        "Mesh::Derivatives"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DerivativesStencil = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "DerivativesStencil" of type "integer" in section
        "Mesh::Derivatives"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DescribeParticlesModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "DescribeParticlesModelmb" of type "block" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Dimensions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Dimensions" of type "integer" in section "System"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DisableOpenCL = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "DisableOpenCL" of type "logical" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Displacement = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Displacement" of type "float" in section "Linear
        Response::Vibrational Modes"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DOSEnergyMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "DOSEnergyMax" of type "float" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DOSEnergyMin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "DOSEnergyMin" of type "float" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DOSEnergyPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "DOSEnergyPoints" of type "integer" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DOSGamma = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "DOSGamma" of type "float" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DoubleFFTParameter = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "DoubleFFTParameter" of type "float" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DoubleGridOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "DoubleGridOrder" of type "integer" in section "Mesh"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_DoubleGrid = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "DoubleGrid" of type "logical" in section "Mesh"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverArnoldiVectors = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EigensolverArnoldiVectors" of type "integer" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverArpackInitialResid = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EigensolverArpackInitialResid" of type "integer" in
        section "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverArpackSort = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EigensolverArpackSort" of type "string" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverImaginaryTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "EigensolverImaginaryTime" of type "float" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EigensolverMaxIter" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverMinimizationIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EigensolverMinimizationIter" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverParpack = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EigensolverParpack" of type "logical" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverSaveMemory = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EigensolverSaveMemory" of type "logical" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EigensolverTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "EigensolverTolerance" of type "float" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Eigensolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Eigensolver" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ELFWithCurrentTerm = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ELFWithCurrentTerm" of type "logical" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMCalcBornCharges = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMCalcBornCharges" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMCalcDiagonalField = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMCalcDiagonalField" of type "logical" in section "Linear
        Response::Static Polarization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMCalcMagnetooptics = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMCalcMagnetooptics" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMCalcRotatoryResponse = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMCalcRotatoryResponse" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMEta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "EMEta" of type "float" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMForceNoKdotP = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMForceNoKdotP" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMFreqsSort = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMFreqsSort" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMFreqs = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EMFreqs" of type "block" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMHyperpol = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EMHyperpol" of type "block" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMMagnetoopticsNoHVar = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMMagnetoopticsNoHVar" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMOccupiedResponse = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMOccupiedResponse" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMPerturbationType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "EMPerturbationType" of type "integer" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMStartDensityIsZeroField = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMStartDensityIsZeroField" of type "logical" in section
        "Linear Response::Static Polarization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMStaticElectricField = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "EMStaticElectricField" of type "float" in section "Linear
        Response::Static Polarization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMVerbose = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMVerbose" of type "logical" in section "Linear
        Response::Static Polarization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMWavefunctionsFromScratch = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMWavefunctionsFromScratch" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EMWriteRestartDensities = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "EMWriteRestartDensities" of type "logical" in section
        "Linear Response::Static Polarization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_EwaldAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "EwaldAlpha" of type "float" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ExcessCharge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ExcessCharge" of type "float" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ExperimentalFeatures = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ExperimentalFeatures" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ExtraStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ExtraStates" of type "integer" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FeastContour = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "FeastContour" of type "block" in section
        "SCF::Eigensolver::FEAST"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FeastMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "FeastMaxIter" of type "integer" in section
        "SCF::Eigensolver::FEAST"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FFTLibrary = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "FFTLibrary" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FFTOptimize = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "FFTOptimize" of type "logical" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FFTPreparePlan = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "FFTPreparePlan" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FilterPotentials = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "FilterPotentials" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FlushMessages = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "FlushMessages" of type "logical" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ForceComplex = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ForceComplex" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ForceTotalEnforce = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ForceTotalEnforce" of type "logical" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FromScratch = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "FromScratch" of type "logical" in section "Execution"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FrozenDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "FrozenDir" of type "string" in section
        "Output::Subsystems"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_FrozenStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "FrozenStates" of type "integer" in section
        "Output::Subsystems"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GaugeFieldDynamics = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "GaugeFieldDynamics" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GaugeVectorField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "GaugeVectorField" of type "block" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOCenter = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "GOCenter" of type "logical" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOFireMass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "GOFireMass" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOLineTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "GOLineTol" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "GOMaxIter" of type "integer" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "GOMethod" of type "integer" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOMinimumMove = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "GOMinimumMove" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOObjective = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "GOObjective" of type "integer" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "GOStep" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GOTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "GOTolerance" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GuessMagnetDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "GuessMagnetDensity" of type "integer" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_GyromagneticRatio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "GyromagneticRatio" of type "float" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_HamiltonianVariation = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "HamiltonianVariation" of type "integer" in section
        "Linear Response::Sternheimer"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_IgnoreExternalIons = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "IgnoreExternalIons" of type "logical" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_InitialSpins = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "InitialSpins" of type "block" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Interaction1DScreening = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Interaction1DScreening" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Interaction1D = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Interaction1D" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_InvertKSConvAbsDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "InvertKSConvAbsDens" of type "float" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_InvertKSMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "InvertKSMaxIter" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_InvertKSmethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "InvertKSmethod" of type "integer" in section "Calculation
        Modes::Invert KS"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_InvertKSTargetDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "InvertKSTargetDensity" of type "string" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_InvertKSVerbosity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "InvertKSVerbosity" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_IonicInteraction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "IonicInteraction" of type "block" in section
        "System::Species"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_IonsConstantVelocity = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "IonsConstantVelocity" of type "logical" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_IonsTimeDependentDisplacements = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "IonsTimeDependentDisplacements" of type "block" in
        section "Time-Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KdotPCalcSecondOrder = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "KdotPCalcSecondOrder" of type "logical" in section
        "Linear Response::KdotP"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KdotPCalculateEffectiveMasses = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "KdotPCalculateEffectiveMasses" of type "logical" in
        section "Linear Response::KdotP"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KdotPEta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "KdotPEta" of type "float" in section "Linear
        Response::KdotP"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KdotPOccupiedSolutionMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "KdotPOccupiedSolutionMethod" of type "integer" in section
        "Linear Response::KdotP"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KdotPUseNonLocalPseudopotential = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "KdotPUseNonLocalPseudopotential" of type "logical" in
        section "Linear Response::KdotP"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KdotPVelMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "KdotPVelMethod" of type "integer" in section "Linear
        Response::KdotP"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KPointsGrid = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "KPointsGrid" of type "block" in section "Mesh::KPoints"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KPointsReduced = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "KPointsReduced" of type "block" in section
        "Mesh::KPoints"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KPointsUseSymmetries = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "KPointsUseSymmetries" of type "logical" in section
        "Mesh::KPoints"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KPointsUseTimeReversal = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "KPointsUseTimeReversal" of type "logical" in section
        "Mesh::KPoints"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "KPoints" of type "block" in section "Mesh::KPoints"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KSInversionAsymptotics = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "KSInversionAsymptotics" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_KSInversionLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "KSInversionLevel" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LatticeParameters = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LatticeParameters" of type "block" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LatticeVectors = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LatticeVectors" of type "block" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LB94_modified = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LB94_modified" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LB94_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LB94_threshold" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAOAlternative = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LCAOAlternative" of type "logical" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAOComplexYlms = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LCAOComplexYlms" of type "logical" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAODiagTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LCAODiagTol" of type "float" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAODimension = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LCAODimension" of type "integer" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAOExtraOrbitals = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LCAOExtraOrbitals" of type "logical" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAOKeepOrbitals = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LCAOKeepOrbitals" of type "logical" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAOMaximumOrbitalRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LCAOMaximumOrbitalRadius" of type "float" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAOScaleFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LCAOScaleFactor" of type "float" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LCAOStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LCAOStart" of type "integer" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDBaderThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LDBaderThreshold" of type "float" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDEnd = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDEnd" of type "integer" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDExtraWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LDExtraWrite" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDFilename" of type "string" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDFolder" of type "string" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDIonicDipole = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LDIonicDipole" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDIterateFolder = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LDIterateFolder" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDMultipoleLmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDMultipoleLmax" of type "integer" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDOutputFormat = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDOutputFormat" of type "flag" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDOutput" of type "flag" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDOverWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LDOverWrite" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDRadiiFile = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDRadiiFile" of type "string" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDRestartFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDRestartFolder" of type "string" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDRestart = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LDRestart" of type "logical" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDStart" of type "integer" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDStep = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LDStep" of type "integer" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDUpdate = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LDUpdate" of type "logical" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LDUseAtomicRadii = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "LDUseAtomicRadii" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_libvdwxcDebug = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "libvdwxcDebug" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_libvdwxcMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "libvdwxcMode" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_libvdwxcVDWFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "libvdwxcVDWFactor" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LinearSolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LinearSolverMaxIter" of type "integer" in section "Linear
        Response::Solver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LinearSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LinearSolver" of type "integer" in section "Linear
        Response::Solver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LocalDomains = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LocalDomains" of type "block" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LocalMagneticMomentsSphereRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LocalMagneticMomentsSphereRadius" of type "float" in
        section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRConvAbsDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LRConvAbsDens" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRConvRelDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LRConvRelDens" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRMaximumIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LRMaximumIter" of type "integer" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRTolAdaptiveFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LRTolAdaptiveFactor" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRTolFinalTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LRTolFinalTol" of type "float" in section "Linear
        Response::Solver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRTolInitTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LRTolInitTol" of type "float" in section "Linear
        Response::Solver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRTolIterWindow = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "LRTolIterWindow" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_LRTolScheme = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "LRTolScheme" of type "integer" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Lsize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Lsize" of type "block" in section "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MagneticGaugeCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MagneticGaugeCorrection" of type "integer" in section
        "Linear Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MainAxis = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MainAxis" of type "block" in section "Utilities::oct-
        center-geom"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MassScaling = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MassScaling" of type "block" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MaximumIterBerry = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MaximumIterBerry" of type "integer" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MaximumIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MaximumIter" of type "integer" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MemoryLimit = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MemoryLimit" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MeshBlockSize" of type "block" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MeshOrder" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshPartitionDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MeshPartitionDir" of type "string" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshPartitionPackage = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MeshPartitionPackage" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshPartitionRead = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "MeshPartitionRead" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshPartitionStencil = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MeshPartitionStencil" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshPartitionVirtualSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MeshPartitionVirtualSize" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshPartitionWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "MeshPartitionWrite" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshPartition = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MeshPartition" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MeshUseTopology = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "MeshUseTopology" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MixField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MixField" of type "integer" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MixingPreconditioner = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "MixingPreconditioner" of type "logical" in section
        "SCF::Mixing"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MixingScheme = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MixingScheme" of type "integer" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Mixing" of type "float" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MixInterval = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MixInterval" of type "integer" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MixNumberSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MixNumberSteps" of type "integer" in section
        "SCF::Mixing"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MomentumTransfer = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MomentumTransfer" of type "block" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MoveIons = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "MoveIons" of type "logical" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MPIDebugHook = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "MPIDebugHook" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MultigridLevels = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MultigridLevels" of type "integer" in section "Mesh"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MultiResolutionArea = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MultiResolutionArea" of type "block" in section "Mesh"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_MultiResolutionInterpolationOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "MultiResolutionInterpolationOrder" of type "integer" in
        section "Mesh"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NDimModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "NDimModelmb" of type "integer" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NFFTCutoff = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "NFFTCutoff" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NFFTGuruInterface = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "NFFTGuruInterface" of type "logical" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NFFTOversampling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "NFFTOversampling" of type "float" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NFFTPrecompute = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "NFFTPrecompute" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NLOperatorCompactBoundaries = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "NLOperatorCompactBoundaries" of type "logical" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NParticleModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "NParticleModelmb" of type "integer" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_NTypeParticleModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "NTypeParticleModelmb" of type "integer" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Occupations = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Occupations" of type "block" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTCheckGradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTCheckGradient" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTClassicalTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTClassicalTarget" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTControlFunctionOmegaMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTControlFunctionOmegaMax" of type "float" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTControlFunctionRepresentation = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTControlFunctionRepresentation" of type "integer" in
        section "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTControlFunctionType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTControlFunctionType" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTCurrentFunctional = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTCurrentFunctional" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTCurrentWeight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTCurrentWeight" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTDelta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTDelta" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTDirectStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTDirectStep" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTDoubleCheck = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OCTDoubleCheck" of type "logical" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTDumpIntermediate = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OCTDumpIntermediate" of type "logical" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTEps = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTEps" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTEta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTEta" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTExcludedStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTExcludedStates" of type "string" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTFilter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTFilter" of type "block" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTFixFluenceTo = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTFixFluenceTo" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTFixInitialFluence = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OCTFixInitialFluence" of type "logical" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTHarmonicWeight = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTHarmonicWeight" of type "string" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTInitialState = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTInitialState" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTInitialTransformStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTInitialTransformStates" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTInitialUserdefined = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTInitialUserdefined" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTLaserEnvelope = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTLaserEnvelope" of type "block" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTLocalTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTLocalTarget" of type "string" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTMaxIter" of type "integer" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTMomentumDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTMomentumDerivatives" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTNumberCheckPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTNumberCheckPoints" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTOptimizeHarmonicSpectrum = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTOptimizeHarmonicSpectrum" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTPenalty = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OCTPenalty" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTPositionDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTPositionDerivatives" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTRandomInitialGuess = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OCTRandomInitialGuess" of type "logical" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTScheme = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTScheme" of type "integer" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTSpatialCurrWeight = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTSpatialCurrWeight" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTStartIterCurrTg = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTStartIterCurrTg" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTTargetDensityFromState = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTTargetDensityFromState" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTTargetDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTTargetDensity" of type "string" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTTargetOperator = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTTargetOperator" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTTargetSpin = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTTargetSpin" of type "block" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTTargetTransformStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTTargetTransformStates" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTTargetUserdefined = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTTargetUserdefined" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTTdTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTTdTarget" of type "block" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTVelocityDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTVelocityDerivatives" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OCTVelocityTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OCTVelocityTarget" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OEPLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OEPLevel" of type "integer" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OEPMixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OEPMixing" of type "float" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OnlyUserDefinedInitialStates = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OnlyUserDefinedInitialStates" of type "logical" in
        section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OpenCLBenchmark = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OpenCLBenchmark" of type "logical" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OpenCLDevice = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OpenCLDevice" of type "integer" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OpenCLPlatform = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OpenCLPlatform" of type "integer" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OpenSCADIsovalue = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "OpenSCADIsovalue" of type "float" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OperateComplexSingle = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OperateComplexSingle" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OperateComplex = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OperateComplex" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OperateDouble = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OperateDouble" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OperateOpenCL = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OperateOpenCL" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OperateSingle = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OperateSingle" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputBandsGnuplotMode = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OutputBandsGnuplotMode" of type "logical" in section
        "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputBandsGraceMode = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OutputBandsGraceMode" of type "logical" in section
        "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputDuringSCF = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "OutputDuringSCF" of type "logical" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputFormat = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OutputFormat" of type "flag" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputInterval = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OutputInterval" of type "integer" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputIterDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OutputIterDir" of type "string" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputMatrixElements = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OutputMatrixElements" of type "flag" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputMEMultipoles = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OutputMEMultipoles" of type "integer" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_OutputWfsNumber = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "OutputWfsNumber" of type "string" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Output = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Output" of type "flag" in section "Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParallelizationNumberSlaves = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ParallelizationNumberSlaves" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParallelizationOfDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ParallelizationOfDerivatives" of type "integer" in
        section "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParallelizationPoissonAllNodes = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ParallelizationPoissonAllNodes" of type "logical" in
        section "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParDomains = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ParDomains" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParKPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ParKPoints" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParOther = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ParOther" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ParStates" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ParticleMass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ParticleMass" of type "float" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PartitionPrint = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PartitionPrint" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMCalcMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PCMCalcMethod" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMCalculation = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PCMCalculation" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMCavity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PCMCavity" of type "string" in section "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMChargeSmearNN = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PCMChargeSmearNN" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMDynamicEpsilon = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PCMDynamicEpsilon" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMGamessBenchmark = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PCMGamessBenchmark" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMQtotTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PCMQtotTol" of type "float" in section "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMRadiusScaling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PCMRadiusScaling" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMRenormCharges = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PCMRenormCharges" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMSmearingFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PCMSmearingFactor" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMSpheresOnH = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PCMSpheresOnH" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMStaticEpsilon = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PCMStaticEpsilon" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMTessSubdivider = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PCMTessSubdivider" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMUpdateIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PCMUpdateIter" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PCMVdWRadii = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PCMVdWRadii" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PDBClassical = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PDBClassical" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PDBCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PDBCoordinates" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PDBVelocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PDBVelocities" of type "string" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PeriodicDimensions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PeriodicDimensions" of type "integer" in section "System"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_ARPES_grid = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_ARPES_grid" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_AvoidAB = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_AvoidAB" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_BZones = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_BZones" of type "block" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_DeltaK = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_DeltaK" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_EnergyGrid = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_EnergyGrid" of type "block" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_Gpoint_Upsample = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_Gpoint_Upsample" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_Kmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_Kmax" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_Lmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_Lmax" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_Lsize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_Lsize" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_Offset = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_Offset" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_Radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_Radius" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_Shape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_Shape" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_StepsPhiK = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_StepsPhiK" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_StepsPhiR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_StepsPhiR" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_StepsThetaK = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_StepsThetaK" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_StepsThetaR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_StepsThetaR" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_Flux_UseMemory = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PES_Flux_UseMemory" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_spm_DeltaOmega = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PES_spm_DeltaOmega" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_spm_OmegaMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PES_spm_OmegaMax" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_spm_points = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_spm_points" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_spm_Radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PES_spm_Radius" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_spm_recipe = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_spm_recipe" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_spm_StepsPhiR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_spm_StepsPhiR" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PES_spm_StepsThetaR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PES_spm_StepsThetaR" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMask2PEnlargeFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PESMask2PEnlargeFactor" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskEnlargeFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PESMaskEnlargeFactor" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskFilterCutOff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PESMaskFilterCutOff" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskIncludePsiA = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PESMaskIncludePsiA" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PESMaskMode" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskPlaneWaveProjection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PESMaskPlaneWaveProjection" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskShape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PESMaskShape" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PESMaskSize" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskSpectEnergyMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PESMaskSpectEnergyMax" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskSpectEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PESMaskSpectEnergyStep" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PESMaskStartTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PESMaskStartTime" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PhotoelectronSpectrumOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PhotoelectronSpectrumOutput" of type "flag" in section
        "Utilities::oct-photoelectron_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PhotoelectronSpectrumResolveStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PhotoelectronSpectrumResolveStates" of type "block" in
        section "Utilities::oct-photoelectron_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PhotoElectronSpectrum = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PhotoElectronSpectrum" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PNFFTCutoff = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PNFFTCutoff" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PNFFTOversampling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PNFFTOversampling" of type "float" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Poisson1DSoftCoulombParam = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Poisson1DSoftCoulombParam" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonCutoffRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PoissonCutoffRadius" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonFFTKernel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonFFTKernel" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverBoundaries = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverBoundaries" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverISFParallelData = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverISFParallelData" of type "logical" in
        section "Hamiltonian::Poisson::ISF"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMaxIter" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMaxMultipole = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMaxMultipole" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMGMaxCycles = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMGMaxCycles" of type "integer" in section
        "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMGPostsmoothingSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMGPostsmoothingSteps" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMGPresmoothingSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMGPresmoothingSteps" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMGRelaxationFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMGRelaxationFactor" of type "float" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMGRelaxationMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMGRelaxationMethod" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverMGRestrictionMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverMGRestrictionMethod" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverNodes = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverNodes" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolverThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PoissonSolverThreshold" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PoissonSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PoissonSolver" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PreconditionerFilterFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PreconditionerFilterFactor" of type "float" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Preconditioner = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Preconditioner" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Preorthogonalization = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "Preorthogonalization" of type "logical" in section
        "Linear Response::Sternheimer"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ProfilingAllNodes = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ProfilingAllNodes" of type "logical" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ProfilingMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ProfilingMode" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumDampFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumDampFactor" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumDampMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumDampMode" of type "integer" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumEndTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumEndTime" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumEnergyStep" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumMaxEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumMaxEnergy" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumSigmaDiagonalization = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumSigmaDiagonalization" of type
        "logical" in section "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumStartTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumStartTime" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumTransform = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumTransform" of type "integer" in
        section "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PropagationSpectrumType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PropagationSpectrumType" of type "integer" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_PseudopotentialSet = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "PseudopotentialSet" of type "integer" in section
        "System::Species"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Radius" of type "float" in section "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RandomVelocityTemp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "RandomVelocityTemp" of type "float" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RashbaSpinOrbitCoupling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "RashbaSpinOrbitCoupling" of type "float" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RDMConvEner = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "RDMConvEner" of type "float" in section "SCF::RDMFT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RDMTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "RDMTolerance" of type "float" in section "SCF::RDMFT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RecalculateGSDuringEvolution = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "RecalculateGSDuringEvolution" of type "logical" in
        section "Time-Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ReducedCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ReducedCoordinates" of type "block" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RelativisticCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "RelativisticCorrection" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ReportMemory = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ReportMemory" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ResponseMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "ResponseMethod" of type "integer" in section "Linear
        Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RestartFixedOccupations = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "RestartFixedOccupations" of type "logical" in section
        "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RestartOptions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "RestartOptions" of type "block" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RestartReorderOccs = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "RestartReorderOccs" of type "logical" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RestartWriteInterval = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "RestartWriteInterval" of type "integer" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RestartWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "RestartWrite" of type "logical" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RootSolverAbsTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "RootSolverAbsTolerance" of type "float" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RootSolverHavePolynomial = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "RootSolverHavePolynomial" of type "logical" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RootSolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "RootSolverMaxIter" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RootSolverRelTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "RootSolverRelTolerance" of type "float" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RootSolverWSRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "RootSolverWSRadius" of type "float" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_RootSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "RootSolver" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ScaLAPACKCompatible = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "ScaLAPACKCompatible" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SCDM_EXX = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SCDM_EXX" of type "logical" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SCDM_verbose = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SCDM_verbose" of type "logical" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SCDMCutoffRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "SCDMCutoffRadius" of type "float" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SCFCalculateDipole = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SCFCalculateDipole" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SCFCalculateForces = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SCFCalculateForces" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SCFCalculatePartialCharges = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SCFCalculatePartialCharges" of type "logical" in section
        "SCF"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SCFinLCAO = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SCFinLCAO" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SICCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SICCorrection" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SmearingFunction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SmearingFunction" of type "integer" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SmearingMPOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SmearingMPOrder" of type "integer" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Smearing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Smearing" of type "float" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SOStrength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "SOStrength" of type "float" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Spacing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Spacing" of type "float" in section "Mesh"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SPARSKITAbsTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "SPARSKITAbsTolerance" of type "float" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SPARSKITIterOut = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SPARSKITIterOut" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SPARSKITKrylovSubspaceSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SPARSKITKrylovSubspaceSize" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SPARSKITMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SPARSKITMaxIter" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SPARSKITRelTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "SPARSKITRelTolerance" of type "float" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SPARSKITSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SPARSKITSolver" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SPARSKITVerboseSolver = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SPARSKITVerboseSolver" of type "logical" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SpeciesProjectorSphereThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "SpeciesProjectorSphereThreshold" of type "float" in
        section "System::Species"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SpeciesTimeDependent = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SpeciesTimeDependent" of type "logical" in section
        "System::Species"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Species = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Species" of type "block" in section "System::Species"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SpectrumMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SpectrumMethod" of type "integer" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SpectrumSignalNoise = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "SpectrumSignalNoise" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SpinComponents = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SpinComponents" of type "integer" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Splines = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Splines" of type "integer" in section "Execution"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_StatesBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "StatesBlockSize" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_StatesCLDeviceMemory = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "StatesCLDeviceMemory" of type "float" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_StatesOrthogonalization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "StatesOrthogonalization" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_StatesPack = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "StatesPack" of type "logical" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_StaticElectricField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "StaticElectricField" of type "block" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_StaticMagneticField2DGauge = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "StaticMagneticField2DGauge" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_StaticMagneticField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "StaticMagneticField" of type "block" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_stderr = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "stderr" of type "string" in section "Execution::IO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_stdout = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "stdout" of type "string" in section "Execution::IO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SubspaceDiagonalization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SubspaceDiagonalization" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SubSystemCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SubSystemCoordinates" of type "block" in section
        "System::Subsystems"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SubSystems = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SubSystems" of type "block" in section
        "System::Subsystems"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SymmetriesCompute = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SymmetriesCompute" of type "logical" in section
        "Execution::Symmetries"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SymmetrizeDensity = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SymmetrizeDensity" of type "logical" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SymmetrizeDynamicalMatrix = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "SymmetrizeDynamicalMatrix" of type "logical" in section
        "Linear Response::Vibrational Modes"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_SymmetryBreakDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "SymmetryBreakDir" of type "block" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDDeltaKickTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDDeltaKickTime" of type "float" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDDeltaStrengthMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDDeltaStrengthMode" of type "integer" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDDeltaStrength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDDeltaStrength" of type "float" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDDeltaUserDefined = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDDeltaUserDefined" of type "string" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDDynamics = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDDynamics" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDEnergyUpdateIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDEnergyUpdateIter" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDExcitedStatesToProject = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDExcitedStatesToProject" of type "block" in section
        "Time-Dependent::TD Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDExponentialMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDExponentialMethod" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDExpOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDExpOrder" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDExternalFields = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDExternalFields" of type "block" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDFloquetDimension = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDFloquetDimension" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDFloquetFrequency = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDFloquetFrequency" of type "float" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDFloquetSample = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDFloquetSample" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDFreezeHXC = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "TDFreezeHXC" of type "logical" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDFreezeOrbitals = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDFreezeOrbitals" of type "integer" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDFunctions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDFunctions" of type "block" in section "Time-Dependent"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDGlobalForce = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDGlobalForce" of type "string" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDIonicTimeScale = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDIonicTimeScale" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDKickFunction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDKickFunction" of type "block" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDLanczosTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDLanczosTol" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDMaxSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDMaxSteps" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDMomentumTransfer = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDMomentumTransfer" of type "block" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDMultipoleLmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDMultipoleLmax" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDOutput" of type "flag" in section "Time-Dependent::TD
        Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDPolarizationDirection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDPolarizationDirection" of type "integer" in section
        "Time-Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDPolarizationEquivAxes = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDPolarizationEquivAxes" of type "integer" in section
        "Time-Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDPolarizationWprime = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDPolarizationWprime" of type "block" in section "Time-
        Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDPolarization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDPolarization" of type "block" in section "Time-
        Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDProjStateStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDProjStateStart" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDPropagationTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDPropagationTime" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDPropagator = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDPropagator" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDSCFThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDSCFThreshold" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDStepsWithSelfConsistency = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TDStepsWithSelfConsistency" of type "integer" in section
        "Time-Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TDTimeStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TDTimeStep" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TemperatureFunction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TemperatureFunction" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TestMaxBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TestMaxBlockSize" of type "integer" in section
        "Utilities::oct-test"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TestMinBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TestMinBlockSize" of type "integer" in section
        "Utilities::oct-test"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TestMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TestMode" of type "integer" in section "Utilities::oct-
        test"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TestRepetitions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TestRepetitions" of type "integer" in section
        "Utilities::oct-test"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TestType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TestType" of type "integer" in section "Utilities::oct-
        test"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TheoryLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TheoryLevel" of type "integer" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_ThermostatMass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "ThermostatMass" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Thermostat = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Thermostat" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TimeZero = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "TimeZero" of type "logical" in section "Hamiltonian"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TnaddFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "TnaddFactor" of type "float" in section
        "Hamiltonian::Subsystems"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TnaddFunctional = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TnaddFunctional" of type "integer" in section
        "Hamiltonian::Subsystems"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TnaddPolarized = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "TnaddPolarized" of type "logical" in section
        "Hamiltonian::Subsystems"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TotalStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TotalStates" of type "integer" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_TransformStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "TransformStates" of type "block" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_UnitsInput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "UnitsInput" of type "integer" in section
        "Execution::Units"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_UnitsOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "UnitsOutput" of type "integer" in section
        "Execution::Units"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_UnitsXYZFiles = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "UnitsXYZFiles" of type "integer" in section
        "Execution::Units"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Units = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Units" of type "integer" in section "Execution::Units"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_UnoccShowOccStates = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "UnoccShowOccStates" of type "logical" in section
        "Calculation Modes::Unoccupied States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_UseFineMesh = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "UseFineMesh" of type "logical" in section "Mesh"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_UserDefinedStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "UserDefinedStates" of type "block" in section "States"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_VDWCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "VDWCorrection" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_vdWNPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "vdWNPoints" of type "integer" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_VDWSelfConsistent = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "VDWSelfConsistent" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Velocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "Velocities" of type "block" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_VibrationalSpectrumTimeStepFactor = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "VibrationalSpectrumTimeStepFactor" of type "integer" in
        section "Utilities::oct-vibrational_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_VibrationalSpectrumTime = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "VibrationalSpectrumTime" of type "integer" in section
        "Utilities::oct-vibrational_spectrum"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_WatterstromODESolverNSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "WatterstromODESolverNSteps" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_WatterstromODESolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "WatterstromODESolver" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_WorkDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "WorkDir" of type "string" in section "Execution::IO"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Xalpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Xalpha" of type "float" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCDensityCorrectionCutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "XCDensityCorrectionCutoff" of type "float" in section
        "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCDensityCorrectionMinimum = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "XCDensityCorrectionMinimum" of type "logical" in section
        "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCDensityCorrectionNormalize = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "XCDensityCorrectionNormalize" of type "logical" in
        section "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCDensityCorrectionOptimize = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "XCDensityCorrectionOptimize" of type "logical" in section
        "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCDensityCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XCDensityCorrection" of type "integer" in section
        "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCFunctional = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XCFunctional" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCKernelLRCAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "XCKernelLRCAlpha" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCKernel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XCKernel" of type "integer" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCParallel = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "XCParallel" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XCUseGaugeIndependentKED = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus input parameter "XCUseGaugeIndependentKED" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_Xlength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus input parameter "Xlength" of type "float" in section "Mesh::Simulation
        Box"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XSFCoordinatesAnimStep = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XSFCoordinatesAnimStep" of type "integer" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XSFCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XSFCoordinates" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XSFVelocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XSFVelocities" of type "string" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XYZCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XYZCoordinates" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_input])

    x_octopus_input_XYZVelocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus input parameter "XYZVelocities" of type "string" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_input])

    x_octopus_parserlog_ABCapHeight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ABCapHeight" of type "float" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ABShape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ABShape" of type "block" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_AbsorbingBoundaries = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "AbsorbingBoundaries" of type "flag" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ABWidth = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ABWidth" of type "float" in section "Time-
        Dependent::Absorbing Boundaries"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_AlphaFMM = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "AlphaFMM" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_AnimationMultiFiles = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "AnimationMultiFiles" of type "logical" in section
        "Utilities::oct-xyz-anim"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_AnimationSampling = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "AnimationSampling" of type "integer" in section
        "Utilities::oct-xyz-anim"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ArpackInitialTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ArpackInitialTolerance" of type "float" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_AtomsMagnetDirection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "AtomsMagnetDirection" of type "block" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_AxisType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "AxisType" of type "integer" in section "Utilities::oct-
        center-geom"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_CalcDipoleMtxels = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_CalcDipoleMtxels" of type "logical" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_CalcExchange = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_CalcExchange" of type "logical" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_NumberBands = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_NumberBands" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_VmtxelNumCondBands = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_VmtxelNumCondBands" of type "integer" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_VmtxelNumValBands = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_VmtxelNumValBands" of type "integer" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_VmtxelPolarization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_VmtxelPolarization" of type "block" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_Vxc_diag_nmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_Vxc_diag_nmax" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_Vxc_diag_nmin = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_Vxc_diag_nmin" of type "integer" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_Vxc_offdiag_nmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_Vxc_offdiag_nmax" of type "integer" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_Vxc_offdiag_nmin = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_Vxc_offdiag_nmin" of type "integer" in
        section "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BerkeleyGW_WFN_filename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BerkeleyGW_WFN_filename" of type "string" in section
        "Output::BerkeleyGW"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BornChargeSumRuleCorrection = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "BornChargeSumRuleCorrection" of type "logical" in
        section "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BoxShapeImage = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BoxShapeImage" of type "string" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BoxShapeUsDef = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BoxShapeUsDef" of type "string" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_BoxShape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "BoxShape" of type "integer" in section "Mesh::Simulation
        Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CalcEigenvalues = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CalcEigenvalues" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CalcInfrared = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CalcInfrared" of type "logical" in section "Linear
        Response::Vibrational Modes"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CalcNormalModeWfs = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CalcNormalModeWfs" of type "logical" in section "Linear
        Response::Vibrational Modes"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CalculateSelfInducedMagneticField = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CalculateSelfInducedMagneticField" of type "logical" in
        section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CalculationMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CalculationMode" of type "integer" in section
        "Calculation Modes"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaCalcForcesKernel = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CasidaCalcForcesKernel" of type "logical" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaCalcForcesSCF = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CasidaCalcForcesSCF" of type "logical" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaCalcForces = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CasidaCalcForces" of type "logical" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaCalcTriplet = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CasidaCalcTriplet" of type "logical" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaHermitianConjugate = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "CasidaHermitianConjugate" of type "logical" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaKohnShamStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CasidaKohnShamStates" of type "string" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaKSEnergyWindow = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CasidaKSEnergyWindow" of type "float" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaMomentumTransfer = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CasidaMomentumTransfer" of type "block" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaQuadratureOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CasidaQuadratureOrder" of type "integer" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaSpectrumBroadening = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CasidaSpectrumBroadening" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaSpectrumEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CasidaSpectrumEnergyStep" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaSpectrumMaxEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CasidaSpectrumMaxEnergy" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaSpectrumMinEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CasidaSpectrumMinEnergy" of type "float" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaSpectrumRotationMatrix = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CasidaSpectrumRotationMatrix" of type "block" in section
        "Utilities::oct-casida_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaTheoryLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CasidaTheoryLevel" of type "flag" in section "Linear
        Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CasidaTransitionDensities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CasidaTransitionDensities" of type "string" in section
        "Linear Response::Casida"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ClassicalPotential = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ClassicalPotential" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingAlphaLeft = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingAlphaLeft" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingAlpha" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingLocalizationRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingLocalizationRadius" of type "float" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingLocalizationThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingLocalizationThreshold" of type "float" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingLocalizedStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingLocalizedStates" of type "integer" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingPenalizationFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingPenalizationFactor" of type "float" in
        section "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingRotateSpectrum = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingRotateSpectrum" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScalingTheta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ComplexScalingTheta" of type "float" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ComplexScaling = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ComplexScaling" of type "flag" in section
        "Hamiltonian::ComplexScaling"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConductivityFromForces = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ConductivityFromForces" of type "logical" in section
        "Utilities::oct-conductivity_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConductivitySpectrumTimeStepFactor = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConductivitySpectrumTimeStepFactor" of type "integer" in
        section "Utilities::oct-conductivity_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvAbsDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvAbsDens" of type "float" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvAbsEv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvAbsEv" of type "float" in section "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvEigenError = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ConvEigenError" of type "logical" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvEnergy" of type "float" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertEnd = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertEnd" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertEnergyMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvertEnergyMax" of type "float" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertEnergyMin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvertEnergyMin" of type "float" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvertEnergyStep" of type "float" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertFilename" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertFolder" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertFTMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertFTMethod" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertHow = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertHow" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertIterateFolder = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ConvertIterateFolder" of type "logical" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertOutputFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertOutputFilename" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertOutputFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertOutputFolder" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertReadSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertReadSize" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertScalarOperation = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertScalarOperation" of type "block" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertStart" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertStep = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertStep" of type "integer" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertSubtractFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertSubtractFilename" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertSubtractFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ConvertSubtractFolder" of type "string" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvertSubtract = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ConvertSubtract" of type "logical" in section
        "Utilities::oct-convert"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvForce = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvForce" of type "float" in section "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvRelDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvRelDens" of type "float" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ConvRelEv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ConvRelEv" of type "float" in section "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Coordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Coordinates" of type "block" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurrentDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CurrentDensity" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurrentThroughPlane = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CurrentThroughPlane" of type "block" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvGygiAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CurvGygiAlpha" of type "float" in section
        "Mesh::Curvilinear::Gygi"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvGygiA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CurvGygiA" of type "float" in section
        "Mesh::Curvilinear::Gygi"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvGygiBeta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CurvGygiBeta" of type "float" in section
        "Mesh::Curvilinear::Gygi"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "CurvMethod" of type "integer" in section
        "Mesh::Curvilinear"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvModineJBar = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CurvModineJBar" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvModineJlocal = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CurvModineJlocal" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvModineJrange = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CurvModineJrange" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_CurvModineXBar = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "CurvModineXBar" of type "float" in section
        "Mesh::Curvilinear::Modine"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Debug = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Debug" of type "flag" in section "Execution::Debug"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DegeneracyThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "DegeneracyThreshold" of type "float" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DeltaEFMM = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "DeltaEFMM" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DensitytoCalc = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "DensitytoCalc" of type "block" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DerivativesOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "DerivativesOrder" of type "integer" in section
        "Mesh::Derivatives"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DerivativesStencil = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "DerivativesStencil" of type "integer" in section
        "Mesh::Derivatives"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DescribeParticlesModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "DescribeParticlesModelmb" of type "block" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Dimensions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Dimensions" of type "integer" in section "System"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DisableOpenCL = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "DisableOpenCL" of type "logical" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Displacement = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Displacement" of type "float" in section "Linear
        Response::Vibrational Modes"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DOSEnergyMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "DOSEnergyMax" of type "float" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DOSEnergyMin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "DOSEnergyMin" of type "float" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DOSEnergyPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "DOSEnergyPoints" of type "integer" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DOSGamma = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "DOSGamma" of type "float" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DoubleFFTParameter = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "DoubleFFTParameter" of type "float" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DoubleGridOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "DoubleGridOrder" of type "integer" in section "Mesh"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_DoubleGrid = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "DoubleGrid" of type "logical" in section "Mesh"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverArnoldiVectors = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EigensolverArnoldiVectors" of type "integer" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverArpackInitialResid = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EigensolverArpackInitialResid" of type "integer" in
        section "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverArpackSort = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EigensolverArpackSort" of type "string" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverImaginaryTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "EigensolverImaginaryTime" of type "float" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EigensolverMaxIter" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverMinimizationIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EigensolverMinimizationIter" of type "integer" in
        section "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverParpack = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EigensolverParpack" of type "logical" in section
        "SCF::Eigensolver::ARPACK"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverSaveMemory = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EigensolverSaveMemory" of type "logical" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EigensolverTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "EigensolverTolerance" of type "float" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Eigensolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Eigensolver" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ELFWithCurrentTerm = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ELFWithCurrentTerm" of type "logical" in section
        "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMCalcBornCharges = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMCalcBornCharges" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMCalcDiagonalField = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMCalcDiagonalField" of type "logical" in section
        "Linear Response::Static Polarization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMCalcMagnetooptics = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMCalcMagnetooptics" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMCalcRotatoryResponse = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMCalcRotatoryResponse" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMEta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "EMEta" of type "float" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMForceNoKdotP = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMForceNoKdotP" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMFreqsSort = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMFreqsSort" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMFreqs = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EMFreqs" of type "block" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMHyperpol = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EMHyperpol" of type "block" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMMagnetoopticsNoHVar = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMMagnetoopticsNoHVar" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMOccupiedResponse = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMOccupiedResponse" of type "logical" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMPerturbationType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "EMPerturbationType" of type "integer" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMStartDensityIsZeroField = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMStartDensityIsZeroField" of type "logical" in section
        "Linear Response::Static Polarization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMStaticElectricField = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "EMStaticElectricField" of type "float" in section
        "Linear Response::Static Polarization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMVerbose = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMVerbose" of type "logical" in section "Linear
        Response::Static Polarization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMWavefunctionsFromScratch = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMWavefunctionsFromScratch" of type "logical" in section
        "Linear Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EMWriteRestartDensities = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "EMWriteRestartDensities" of type "logical" in section
        "Linear Response::Static Polarization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_EwaldAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "EwaldAlpha" of type "float" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ExcessCharge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ExcessCharge" of type "float" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ExperimentalFeatures = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ExperimentalFeatures" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ExtraStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ExtraStates" of type "integer" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FeastContour = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "FeastContour" of type "block" in section
        "SCF::Eigensolver::FEAST"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FeastMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "FeastMaxIter" of type "integer" in section
        "SCF::Eigensolver::FEAST"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FFTLibrary = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "FFTLibrary" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FFTOptimize = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "FFTOptimize" of type "logical" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FFTPreparePlan = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "FFTPreparePlan" of type "integer" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FilterPotentials = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "FilterPotentials" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FlushMessages = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "FlushMessages" of type "logical" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ForceComplex = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ForceComplex" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ForceTotalEnforce = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ForceTotalEnforce" of type "logical" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FromScratch = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "FromScratch" of type "logical" in section "Execution"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FrozenDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "FrozenDir" of type "string" in section
        "Output::Subsystems"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_FrozenStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "FrozenStates" of type "integer" in section
        "Output::Subsystems"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GaugeFieldDynamics = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "GaugeFieldDynamics" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GaugeVectorField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "GaugeVectorField" of type "block" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOCenter = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "GOCenter" of type "logical" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOFireMass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "GOFireMass" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOLineTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "GOLineTol" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "GOMaxIter" of type "integer" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "GOMethod" of type "integer" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOMinimumMove = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "GOMinimumMove" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOObjective = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "GOObjective" of type "integer" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "GOStep" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GOTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "GOTolerance" of type "float" in section "Calculation
        Modes::Geometry Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GuessMagnetDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "GuessMagnetDensity" of type "integer" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_GyromagneticRatio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "GyromagneticRatio" of type "float" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_HamiltonianVariation = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "HamiltonianVariation" of type "integer" in section
        "Linear Response::Sternheimer"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_IgnoreExternalIons = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "IgnoreExternalIons" of type "logical" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_InitialSpins = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "InitialSpins" of type "block" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Interaction1DScreening = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Interaction1DScreening" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Interaction1D = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Interaction1D" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_InvertKSConvAbsDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "InvertKSConvAbsDens" of type "float" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_InvertKSMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "InvertKSMaxIter" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_InvertKSmethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "InvertKSmethod" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_InvertKSTargetDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "InvertKSTargetDensity" of type "string" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_InvertKSVerbosity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "InvertKSVerbosity" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_IonicInteraction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "IonicInteraction" of type "block" in section
        "System::Species"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_IonsConstantVelocity = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "IonsConstantVelocity" of type "logical" in section
        "Time-Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_IonsTimeDependentDisplacements = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "IonsTimeDependentDisplacements" of type "block" in
        section "Time-Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KdotPCalcSecondOrder = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "KdotPCalcSecondOrder" of type "logical" in section
        "Linear Response::KdotP"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KdotPCalculateEffectiveMasses = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "KdotPCalculateEffectiveMasses" of type "logical" in
        section "Linear Response::KdotP"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KdotPEta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "KdotPEta" of type "float" in section "Linear
        Response::KdotP"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KdotPOccupiedSolutionMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "KdotPOccupiedSolutionMethod" of type "integer" in
        section "Linear Response::KdotP"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KdotPUseNonLocalPseudopotential = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "KdotPUseNonLocalPseudopotential" of type "logical" in
        section "Linear Response::KdotP"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KdotPVelMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "KdotPVelMethod" of type "integer" in section "Linear
        Response::KdotP"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KPointsGrid = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "KPointsGrid" of type "block" in section "Mesh::KPoints"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KPointsReduced = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "KPointsReduced" of type "block" in section
        "Mesh::KPoints"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KPointsUseSymmetries = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "KPointsUseSymmetries" of type "logical" in section
        "Mesh::KPoints"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KPointsUseTimeReversal = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "KPointsUseTimeReversal" of type "logical" in section
        "Mesh::KPoints"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "KPoints" of type "block" in section "Mesh::KPoints"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KSInversionAsymptotics = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "KSInversionAsymptotics" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_KSInversionLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "KSInversionLevel" of type "integer" in section
        "Calculation Modes::Invert KS"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LatticeParameters = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LatticeParameters" of type "block" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LatticeVectors = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LatticeVectors" of type "block" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LB94_modified = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LB94_modified" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LB94_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LB94_threshold" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAOAlternative = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LCAOAlternative" of type "logical" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAOComplexYlms = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LCAOComplexYlms" of type "logical" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAODiagTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LCAODiagTol" of type "float" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAODimension = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LCAODimension" of type "integer" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAOExtraOrbitals = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LCAOExtraOrbitals" of type "logical" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAOKeepOrbitals = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LCAOKeepOrbitals" of type "logical" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAOMaximumOrbitalRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LCAOMaximumOrbitalRadius" of type "float" in section
        "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAOScaleFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LCAOScaleFactor" of type "float" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LCAOStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LCAOStart" of type "integer" in section "SCF::LCAO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDBaderThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LDBaderThreshold" of type "float" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDEnd = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDEnd" of type "integer" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDExtraWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LDExtraWrite" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDFilename = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDFilename" of type "string" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDFolder" of type "string" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDIonicDipole = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LDIonicDipole" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDIterateFolder = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LDIterateFolder" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDMultipoleLmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDMultipoleLmax" of type "integer" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDOutputFormat = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDOutputFormat" of type "flag" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDOutput" of type "flag" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDOverWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LDOverWrite" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDRadiiFile = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDRadiiFile" of type "string" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDRestartFolder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDRestartFolder" of type "string" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDRestart = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LDRestart" of type "logical" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDStart" of type "integer" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDStep = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LDStep" of type "integer" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDUpdate = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LDUpdate" of type "logical" in section "Utilities::oct-
        local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LDUseAtomicRadii = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "LDUseAtomicRadii" of type "logical" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_libvdwxcDebug = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "libvdwxcDebug" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_libvdwxcMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "libvdwxcMode" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_libvdwxcVDWFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "libvdwxcVDWFactor" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LinearSolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LinearSolverMaxIter" of type "integer" in section
        "Linear Response::Solver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LinearSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LinearSolver" of type "integer" in section "Linear
        Response::Solver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LocalDomains = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LocalDomains" of type "block" in section
        "Utilities::oct-local_multipoles"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LocalMagneticMomentsSphereRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LocalMagneticMomentsSphereRadius" of type "float" in
        section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRConvAbsDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LRConvAbsDens" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRConvRelDens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LRConvRelDens" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRMaximumIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LRMaximumIter" of type "integer" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRTolAdaptiveFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LRTolAdaptiveFactor" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRTolFinalTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LRTolFinalTol" of type "float" in section "Linear
        Response::Solver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRTolInitTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LRTolInitTol" of type "float" in section "Linear
        Response::Solver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRTolIterWindow = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "LRTolIterWindow" of type "float" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_LRTolScheme = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "LRTolScheme" of type "integer" in section "Linear
        Response::SCF in LR calculations"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Lsize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Lsize" of type "block" in section "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MagneticGaugeCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MagneticGaugeCorrection" of type "integer" in section
        "Linear Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MainAxis = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MainAxis" of type "block" in section "Utilities::oct-
        center-geom"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MassScaling = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MassScaling" of type "block" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MaximumIterBerry = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MaximumIterBerry" of type "integer" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MaximumIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MaximumIter" of type "integer" in section
        "SCF::Convergence"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MemoryLimit = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MemoryLimit" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MeshBlockSize" of type "block" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MeshOrder" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshPartitionDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MeshPartitionDir" of type "string" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshPartitionPackage = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MeshPartitionPackage" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshPartitionRead = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "MeshPartitionRead" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshPartitionStencil = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MeshPartitionStencil" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshPartitionVirtualSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MeshPartitionVirtualSize" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshPartitionWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "MeshPartitionWrite" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshPartition = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MeshPartition" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MeshUseTopology = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "MeshUseTopology" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MixField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MixField" of type "integer" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MixingPreconditioner = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "MixingPreconditioner" of type "logical" in section
        "SCF::Mixing"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MixingScheme = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MixingScheme" of type "integer" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Mixing" of type "float" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MixInterval = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MixInterval" of type "integer" in section "SCF::Mixing"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MixNumberSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MixNumberSteps" of type "integer" in section
        "SCF::Mixing"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MomentumTransfer = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MomentumTransfer" of type "block" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MoveIons = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "MoveIons" of type "logical" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MPIDebugHook = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "MPIDebugHook" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MultigridLevels = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MultigridLevels" of type "integer" in section "Mesh"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MultiResolutionArea = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MultiResolutionArea" of type "block" in section "Mesh"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_MultiResolutionInterpolationOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "MultiResolutionInterpolationOrder" of type "integer" in
        section "Mesh"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NDimModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "NDimModelmb" of type "integer" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NFFTCutoff = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "NFFTCutoff" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NFFTGuruInterface = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "NFFTGuruInterface" of type "logical" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NFFTOversampling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "NFFTOversampling" of type "float" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NFFTPrecompute = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "NFFTPrecompute" of type "integer" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NLOperatorCompactBoundaries = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "NLOperatorCompactBoundaries" of type "logical" in
        section "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NParticleModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "NParticleModelmb" of type "integer" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_NTypeParticleModelmb = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "NTypeParticleModelmb" of type "integer" in section
        "States::ModelMB"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Occupations = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Occupations" of type "block" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTCheckGradient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTCheckGradient" of type "float" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTClassicalTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTClassicalTarget" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTControlFunctionOmegaMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTControlFunctionOmegaMax" of type "float" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTControlFunctionRepresentation = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTControlFunctionRepresentation" of type "integer" in
        section "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTControlFunctionType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTControlFunctionType" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTCurrentFunctional = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTCurrentFunctional" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTCurrentWeight = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTCurrentWeight" of type "float" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTDelta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTDelta" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTDirectStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTDirectStep" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTDoubleCheck = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OCTDoubleCheck" of type "logical" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTDumpIntermediate = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OCTDumpIntermediate" of type "logical" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTEps = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTEps" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTEta = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTEta" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTExcludedStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTExcludedStates" of type "string" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTFilter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTFilter" of type "block" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTFixFluenceTo = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTFixFluenceTo" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTFixInitialFluence = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OCTFixInitialFluence" of type "logical" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTHarmonicWeight = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTHarmonicWeight" of type "string" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTInitialState = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTInitialState" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTInitialTransformStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTInitialTransformStates" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTInitialUserdefined = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTInitialUserdefined" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTLaserEnvelope = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTLaserEnvelope" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTLocalTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTLocalTarget" of type "string" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTMaxIter" of type "integer" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTMomentumDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTMomentumDerivatives" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTNumberCheckPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTNumberCheckPoints" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTOptimizeHarmonicSpectrum = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTOptimizeHarmonicSpectrum" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTPenalty = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OCTPenalty" of type "float" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTPositionDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTPositionDerivatives" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTRandomInitialGuess = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OCTRandomInitialGuess" of type "logical" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTScheme = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTScheme" of type "integer" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTSpatialCurrWeight = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTSpatialCurrWeight" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTStartIterCurrTg = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTStartIterCurrTg" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTTargetDensityFromState = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTTargetDensityFromState" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTTargetDensity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTTargetDensity" of type "string" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTTargetOperator = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTTargetOperator" of type "integer" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTTargetSpin = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTTargetSpin" of type "block" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTTargetTransformStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTTargetTransformStates" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTTargetUserdefined = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTTargetUserdefined" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTTdTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTTdTarget" of type "block" in section "Calculation
        Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTVelocityDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTVelocityDerivatives" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OCTVelocityTarget = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OCTVelocityTarget" of type "block" in section
        "Calculation Modes::Optimal Control"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OEPLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OEPLevel" of type "integer" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OEPMixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OEPMixing" of type "float" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OnlyUserDefinedInitialStates = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OnlyUserDefinedInitialStates" of type "logical" in
        section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OpenCLBenchmark = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OpenCLBenchmark" of type "logical" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OpenCLDevice = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OpenCLDevice" of type "integer" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OpenCLPlatform = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OpenCLPlatform" of type "integer" in section
        "Execution::OpenCL"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OpenSCADIsovalue = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "OpenSCADIsovalue" of type "float" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OperateComplexSingle = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OperateComplexSingle" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OperateComplex = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OperateComplex" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OperateDouble = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OperateDouble" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OperateOpenCL = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OperateOpenCL" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OperateSingle = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OperateSingle" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputBandsGnuplotMode = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OutputBandsGnuplotMode" of type "logical" in section
        "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputBandsGraceMode = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OutputBandsGraceMode" of type "logical" in section
        "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputDuringSCF = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "OutputDuringSCF" of type "logical" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputFormat = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OutputFormat" of type "flag" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputInterval = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OutputInterval" of type "integer" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputIterDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OutputIterDir" of type "string" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputMatrixElements = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OutputMatrixElements" of type "flag" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputMEMultipoles = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OutputMEMultipoles" of type "integer" in section
        "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_OutputWfsNumber = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "OutputWfsNumber" of type "string" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Output = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Output" of type "flag" in section "Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParallelizationNumberSlaves = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ParallelizationNumberSlaves" of type "integer" in
        section "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParallelizationOfDerivatives = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ParallelizationOfDerivatives" of type "integer" in
        section "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParallelizationPoissonAllNodes = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ParallelizationPoissonAllNodes" of type "logical" in
        section "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParDomains = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ParDomains" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParKPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ParKPoints" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParOther = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ParOther" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ParStates" of type "integer" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ParticleMass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ParticleMass" of type "float" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PartitionPrint = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PartitionPrint" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMCalcMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PCMCalcMethod" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMCalculation = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PCMCalculation" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMCavity = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PCMCavity" of type "string" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMChargeSmearNN = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PCMChargeSmearNN" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMDynamicEpsilon = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PCMDynamicEpsilon" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMGamessBenchmark = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PCMGamessBenchmark" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMQtotTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PCMQtotTol" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMRadiusScaling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PCMRadiusScaling" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMRenormCharges = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PCMRenormCharges" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMSmearingFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PCMSmearingFactor" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMSpheresOnH = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PCMSpheresOnH" of type "logical" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMStaticEpsilon = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PCMStaticEpsilon" of type "float" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMTessSubdivider = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PCMTessSubdivider" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMUpdateIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PCMUpdateIter" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PCMVdWRadii = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PCMVdWRadii" of type "integer" in section
        "Hamiltonian::PCM"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PDBClassical = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PDBClassical" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PDBCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PDBCoordinates" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PDBVelocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PDBVelocities" of type "string" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PeriodicDimensions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PeriodicDimensions" of type "integer" in section
        "System"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_ARPES_grid = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_ARPES_grid" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_AvoidAB = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_AvoidAB" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_BZones = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_BZones" of type "block" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_DeltaK = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_DeltaK" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_EnergyGrid = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_EnergyGrid" of type "block" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_Gpoint_Upsample = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_Gpoint_Upsample" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_Kmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_Kmax" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_Lmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_Lmax" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_Lsize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_Lsize" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_Offset = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_Offset" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_Radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_Radius" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_Shape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_Shape" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_StepsPhiK = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_StepsPhiK" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_StepsPhiR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_StepsPhiR" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_StepsThetaK = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_StepsThetaK" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_StepsThetaR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_StepsThetaR" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_Flux_UseMemory = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PES_Flux_UseMemory" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_spm_DeltaOmega = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PES_spm_DeltaOmega" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_spm_OmegaMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PES_spm_OmegaMax" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_spm_points = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_spm_points" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_spm_Radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PES_spm_Radius" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_spm_recipe = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_spm_recipe" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_spm_StepsPhiR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_spm_StepsPhiR" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PES_spm_StepsThetaR = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PES_spm_StepsThetaR" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMask2PEnlargeFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PESMask2PEnlargeFactor" of type "float" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskEnlargeFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PESMaskEnlargeFactor" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskFilterCutOff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PESMaskFilterCutOff" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskIncludePsiA = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PESMaskIncludePsiA" of type "logical" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PESMaskMode" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskPlaneWaveProjection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PESMaskPlaneWaveProjection" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskShape = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PESMaskShape" of type "integer" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PESMaskSize" of type "block" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskSpectEnergyMax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PESMaskSpectEnergyMax" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskSpectEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PESMaskSpectEnergyStep" of type "float" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PESMaskStartTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PESMaskStartTime" of type "float" in section "Time-
        Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PhotoelectronSpectrumOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PhotoelectronSpectrumOutput" of type "flag" in section
        "Utilities::oct-photoelectron_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PhotoelectronSpectrumResolveStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PhotoelectronSpectrumResolveStates" of type "block" in
        section "Utilities::oct-photoelectron_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PhotoElectronSpectrum = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PhotoElectronSpectrum" of type "integer" in section
        "Time-Dependent::PhotoElectronSpectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PNFFTCutoff = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PNFFTCutoff" of type "integer" in section "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PNFFTOversampling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PNFFTOversampling" of type "float" in section
        "Mesh::FFTs"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Poisson1DSoftCoulombParam = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Poisson1DSoftCoulombParam" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonCutoffRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PoissonCutoffRadius" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonFFTKernel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonFFTKernel" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverBoundaries = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverBoundaries" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverISFParallelData = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverISFParallelData" of type "logical" in
        section "Hamiltonian::Poisson::ISF"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMaxIter" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMaxMultipole = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMaxMultipole" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMGMaxCycles = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMGMaxCycles" of type "integer" in section
        "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMGPostsmoothingSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMGPostsmoothingSteps" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMGPresmoothingSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMGPresmoothingSteps" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMGRelaxationFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMGRelaxationFactor" of type "float" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMGRelaxationMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMGRelaxationMethod" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverMGRestrictionMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverMGRestrictionMethod" of type "integer" in
        section "Hamiltonian::Poisson::Multigrid"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverNodes = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverNodes" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolverThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolverThreshold" of type "float" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PoissonSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PoissonSolver" of type "integer" in section
        "Hamiltonian::Poisson"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PreconditionerFilterFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PreconditionerFilterFactor" of type "float" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Preconditioner = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Preconditioner" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Preorthogonalization = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "Preorthogonalization" of type "logical" in section
        "Linear Response::Sternheimer"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ProfilingAllNodes = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ProfilingAllNodes" of type "logical" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ProfilingMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ProfilingMode" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumDampFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumDampFactor" of type "float" in
        section "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumDampMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumDampMode" of type "integer" in
        section "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumEndTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumEndTime" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumEnergyStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumEnergyStep" of type "float" in
        section "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumMaxEnergy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumMaxEnergy" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumSigmaDiagonalization = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumSigmaDiagonalization" of type
        "logical" in section "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumStartTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumStartTime" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumTransform = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumTransform" of type "integer" in
        section "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PropagationSpectrumType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PropagationSpectrumType" of type "integer" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_PseudopotentialSet = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "PseudopotentialSet" of type "integer" in section
        "System::Species"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Radius" of type "float" in section "Mesh::Simulation
        Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RandomVelocityTemp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "RandomVelocityTemp" of type "float" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RashbaSpinOrbitCoupling = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "RashbaSpinOrbitCoupling" of type "float" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RDMConvEner = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "RDMConvEner" of type "float" in section "SCF::RDMFT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RDMTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "RDMTolerance" of type "float" in section "SCF::RDMFT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RecalculateGSDuringEvolution = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "RecalculateGSDuringEvolution" of type "logical" in
        section "Time-Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ReducedCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ReducedCoordinates" of type "block" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RelativisticCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "RelativisticCorrection" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ReportMemory = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ReportMemory" of type "logical" in section
        "Execution::Debug"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ResponseMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "ResponseMethod" of type "integer" in section "Linear
        Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RestartFixedOccupations = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "RestartFixedOccupations" of type "logical" in section
        "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RestartOptions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "RestartOptions" of type "block" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RestartReorderOccs = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "RestartReorderOccs" of type "logical" in section
        "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RestartWriteInterval = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "RestartWriteInterval" of type "integer" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RestartWrite = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "RestartWrite" of type "logical" in section
        "Execution::IO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RootSolverAbsTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "RootSolverAbsTolerance" of type "float" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RootSolverHavePolynomial = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "RootSolverHavePolynomial" of type "logical" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RootSolverMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "RootSolverMaxIter" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RootSolverRelTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "RootSolverRelTolerance" of type "float" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RootSolverWSRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "RootSolverWSRadius" of type "float" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_RootSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "RootSolver" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ScaLAPACKCompatible = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "ScaLAPACKCompatible" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SCDM_EXX = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SCDM_EXX" of type "logical" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SCDM_verbose = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SCDM_verbose" of type "logical" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SCDMCutoffRadius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "SCDMCutoffRadius" of type "float" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SCFCalculateDipole = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SCFCalculateDipole" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SCFCalculateForces = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SCFCalculateForces" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SCFCalculatePartialCharges = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SCFCalculatePartialCharges" of type "logical" in section
        "SCF"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SCFinLCAO = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SCFinLCAO" of type "logical" in section "SCF"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SICCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SICCorrection" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SmearingFunction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SmearingFunction" of type "integer" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SmearingMPOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SmearingMPOrder" of type "integer" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Smearing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Smearing" of type "float" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SOStrength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "SOStrength" of type "float" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Spacing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Spacing" of type "float" in section "Mesh"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SPARSKITAbsTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "SPARSKITAbsTolerance" of type "float" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SPARSKITIterOut = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SPARSKITIterOut" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SPARSKITKrylovSubspaceSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SPARSKITKrylovSubspaceSize" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SPARSKITMaxIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SPARSKITMaxIter" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SPARSKITRelTolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "SPARSKITRelTolerance" of type "float" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SPARSKITSolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SPARSKITSolver" of type "integer" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SPARSKITVerboseSolver = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SPARSKITVerboseSolver" of type "logical" in section
        "Math::SPARSKIT"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SpeciesProjectorSphereThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "SpeciesProjectorSphereThreshold" of type "float" in
        section "System::Species"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SpeciesTimeDependent = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SpeciesTimeDependent" of type "logical" in section
        "System::Species"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Species = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Species" of type "block" in section "System::Species"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SpectrumMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SpectrumMethod" of type "integer" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SpectrumSignalNoise = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "SpectrumSignalNoise" of type "float" in section
        "Utilities::oct-propagation_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SpinComponents = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SpinComponents" of type "integer" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Splines = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Splines" of type "integer" in section "Execution"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_StatesBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "StatesBlockSize" of type "integer" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_StatesCLDeviceMemory = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "StatesCLDeviceMemory" of type "float" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_StatesOrthogonalization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "StatesOrthogonalization" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_StatesPack = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "StatesPack" of type "logical" in section
        "Execution::Optimization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_StaticElectricField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "StaticElectricField" of type "block" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_StaticMagneticField2DGauge = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "StaticMagneticField2DGauge" of type "integer" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_StaticMagneticField = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "StaticMagneticField" of type "block" in section
        "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_stderr = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "stderr" of type "string" in section "Execution::IO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_stdout = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "stdout" of type "string" in section "Execution::IO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SubspaceDiagonalization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SubspaceDiagonalization" of type "integer" in section
        "SCF::Eigensolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SubSystemCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SubSystemCoordinates" of type "block" in section
        "System::Subsystems"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SubSystems = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SubSystems" of type "block" in section
        "System::Subsystems"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SymmetriesCompute = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SymmetriesCompute" of type "logical" in section
        "Execution::Symmetries"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SymmetrizeDensity = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SymmetrizeDensity" of type "logical" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SymmetrizeDynamicalMatrix = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "SymmetrizeDynamicalMatrix" of type "logical" in section
        "Linear Response::Vibrational Modes"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_SymmetryBreakDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "SymmetryBreakDir" of type "block" in section
        "Mesh::Simulation Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDDeltaKickTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDDeltaKickTime" of type "float" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDDeltaStrengthMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDDeltaStrengthMode" of type "integer" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDDeltaStrength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDDeltaStrength" of type "float" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDDeltaUserDefined = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDDeltaUserDefined" of type "string" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDDynamics = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDDynamics" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDEnergyUpdateIter = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDEnergyUpdateIter" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDExcitedStatesToProject = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDExcitedStatesToProject" of type "block" in section
        "Time-Dependent::TD Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDExponentialMethod = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDExponentialMethod" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDExpOrder = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDExpOrder" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDExternalFields = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDExternalFields" of type "block" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDFloquetDimension = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDFloquetDimension" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDFloquetFrequency = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDFloquetFrequency" of type "float" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDFloquetSample = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDFloquetSample" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDFreezeHXC = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "TDFreezeHXC" of type "logical" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDFreezeOrbitals = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDFreezeOrbitals" of type "integer" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDFunctions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDFunctions" of type "block" in section "Time-Dependent"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDGlobalForce = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDGlobalForce" of type "string" in section "Time-
        Dependent"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDIonicTimeScale = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDIonicTimeScale" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDKickFunction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDKickFunction" of type "block" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDLanczosTol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDLanczosTol" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDMaxSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDMaxSteps" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDMomentumTransfer = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDMomentumTransfer" of type "block" in section "Time-
        Dependent::Response"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDMultipoleLmax = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDMultipoleLmax" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDOutput" of type "flag" in section "Time-Dependent::TD
        Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDPolarizationDirection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDPolarizationDirection" of type "integer" in section
        "Time-Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDPolarizationEquivAxes = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDPolarizationEquivAxes" of type "integer" in section
        "Time-Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDPolarizationWprime = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDPolarizationWprime" of type "block" in section "Time-
        Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDPolarization = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDPolarization" of type "block" in section "Time-
        Dependent::Response::Dipole"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDProjStateStart = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDProjStateStart" of type "integer" in section "Time-
        Dependent::TD Output"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDPropagationTime = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDPropagationTime" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDPropagator = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDPropagator" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDSCFThreshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDSCFThreshold" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDStepsWithSelfConsistency = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TDStepsWithSelfConsistency" of type "integer" in section
        "Time-Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TDTimeStep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TDTimeStep" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TemperatureFunction = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TemperatureFunction" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TestMaxBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TestMaxBlockSize" of type "integer" in section
        "Utilities::oct-test"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TestMinBlockSize = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TestMinBlockSize" of type "integer" in section
        "Utilities::oct-test"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TestMode = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TestMode" of type "integer" in section "Utilities::oct-
        test"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TestRepetitions = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TestRepetitions" of type "integer" in section
        "Utilities::oct-test"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TestType = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TestType" of type "integer" in section "Utilities::oct-
        test"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TheoryLevel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TheoryLevel" of type "integer" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_ThermostatMass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "ThermostatMass" of type "float" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Thermostat = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Thermostat" of type "integer" in section "Time-
        Dependent::Propagation"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TimeZero = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "TimeZero" of type "logical" in section "Hamiltonian"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TnaddFactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "TnaddFactor" of type "float" in section
        "Hamiltonian::Subsystems"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TnaddFunctional = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TnaddFunctional" of type "integer" in section
        "Hamiltonian::Subsystems"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TnaddPolarized = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "TnaddPolarized" of type "logical" in section
        "Hamiltonian::Subsystems"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TotalStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TotalStates" of type "integer" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_TransformStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "TransformStates" of type "block" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_UnitsInput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "UnitsInput" of type "integer" in section
        "Execution::Units"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_UnitsOutput = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "UnitsOutput" of type "integer" in section
        "Execution::Units"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_UnitsXYZFiles = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "UnitsXYZFiles" of type "integer" in section
        "Execution::Units"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Units = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Units" of type "integer" in section "Execution::Units"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_UnoccShowOccStates = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "UnoccShowOccStates" of type "logical" in section
        "Calculation Modes::Unoccupied States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_UseFineMesh = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "UseFineMesh" of type "logical" in section "Mesh"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_UserDefinedStates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "UserDefinedStates" of type "block" in section "States"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_VDWCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "VDWCorrection" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_vdWNPoints = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "vdWNPoints" of type "integer" in section "Linear
        Response::Polarizabilities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_VDWSelfConsistent = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "VDWSelfConsistent" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Velocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "Velocities" of type "block" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_VibrationalSpectrumTimeStepFactor = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "VibrationalSpectrumTimeStepFactor" of type "integer" in
        section "Utilities::oct-vibrational_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_VibrationalSpectrumTime = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "VibrationalSpectrumTime" of type "integer" in section
        "Utilities::oct-vibrational_spectrum"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_WatterstromODESolverNSteps = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "WatterstromODESolverNSteps" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_WatterstromODESolver = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "WatterstromODESolver" of type "integer" in section
        "Math::RootSolver"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_WorkDir = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "WorkDir" of type "string" in section "Execution::IO"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Xalpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Xalpha" of type "float" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCDensityCorrectionCutoff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "XCDensityCorrectionCutoff" of type "float" in section
        "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCDensityCorrectionMinimum = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "XCDensityCorrectionMinimum" of type "logical" in section
        "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCDensityCorrectionNormalize = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "XCDensityCorrectionNormalize" of type "logical" in
        section "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCDensityCorrectionOptimize = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "XCDensityCorrectionOptimize" of type "logical" in
        section "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCDensityCorrection = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XCDensityCorrection" of type "integer" in section
        "Hamiltonian::XC::DensityCorrection"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCFunctional = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XCFunctional" of type "integer" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCKernelLRCAlpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "XCKernelLRCAlpha" of type "float" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCKernel = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XCKernel" of type "integer" in section "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCParallel = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "XCParallel" of type "logical" in section
        "Execution::Parallelization"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XCUseGaugeIndependentKED = Quantity(
        type=bool,
        shape=[],
        description='''
        Octopus parser log entry "XCUseGaugeIndependentKED" of type "logical" in section
        "Hamiltonian::XC"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_Xlength = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Octopus parser log entry "Xlength" of type "float" in section "Mesh::Simulation
        Box"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XSFCoordinatesAnimStep = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XSFCoordinatesAnimStep" of type "integer" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XSFCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XSFCoordinates" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XSFVelocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XSFVelocities" of type "string" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XYZCoordinates = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XYZCoordinates" of type "string" in section
        "System::Coordinates"
        ''',
        categories=[x_octopus_parserlog])

    x_octopus_parserlog_XYZVelocities = Quantity(
        type=str,
        shape=[],
        description='''
        Octopus parser log entry "XYZVelocities" of type "string" in section
        "System::Velocities"
        ''',
        categories=[x_octopus_parserlog])
