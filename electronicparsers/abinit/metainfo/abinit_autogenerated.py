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
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, Reference
)

from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_abinit_var(MCategory):
    '''
    section describing the ABINIT variables
    '''

    m_def = Category()


class x_abinit_section_input(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_abinit_var_accuracy = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable ACCURACY
        ''',
        categories=[x_abinit_var])

    x_abinit_var_acell = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        unit='bohr',
        description='''
        ABINIT variable CELL lattice vector scaling
        ''',
        categories=[x_abinit_var])

    x_abinit_var_adpimd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable ADiabatic Path-Integral Molecular Dynamics
        ''',
        categories=[x_abinit_var])

    x_abinit_var_adpimd_gamma = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable ADiabatic Path-Integral Molecular Dynamics: GAMMA factor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_algalch = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_ntypalch'],
        description='''
        ABINIT variable ALGorithm for generating ALCHemical pseudopotentials
        ''',
        categories=[x_abinit_var])

    x_abinit_var_amu = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable Atomic Mass Units
        ''',
        categories=[x_abinit_var])

    x_abinit_var_angdeg = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable ANGles in DEGrees
        ''',
        categories=[x_abinit_var])

    x_abinit_var_asr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Acoustic Sum Rule
        ''',
        categories=[x_abinit_var])

    x_abinit_var_atvshift = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_natom', 'x_abinit_var_nsppol', 'x_abinit_var_natvshift'],
        description='''
        ABINIT variable ATomic potential (V) energy SHIFTs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_autoparal = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable AUTOmatisation of the PARALlelism
        ''',
        categories=[x_abinit_var])

    x_abinit_var_awtr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable evaluate the Adler-Wiser expression of $\\chi^{0}_{KS}$ assuming
        Time-Reversal
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bandpp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable BAND Per Processor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bdberry = Quantity(
        type=np.dtype(np.int32),
        shape=[4],
        description='''
        ABINIT variable BanD limits for BERRY phase
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bdeigrf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable BanD for second-order EIGenvalues from Response-Function
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bdgw = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nsppol', 'x_abinit_var_nkptgw', 2],
        description='''
        ABINIT variable BanDs for GW calculation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_berryopt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable BERRY phase OPTions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_berrysav = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable BERRY SAVe
        ''',
        categories=[x_abinit_var])

    x_abinit_var_berrystep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable BERRY phase : multiple STEP
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bfield = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable finite B FIELD calculation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bmass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Barostat MASS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_boxcenter = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable BOX CENTER
        ''',
        categories=[x_abinit_var])

    x_abinit_var_boxcutmin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable BOX CUT-off MINimum
        ''',
        categories=[x_abinit_var])

    x_abinit_var_brvltt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable BRaVais LaTTice type
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_algorithm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter ALGORITHM
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_calctype = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter CALCulation TYPE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_coulomb_term = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter COULOMB TERM
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_coupling = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter COUPLING
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_eh_cutoff = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable Bethe-Salpeter Electron-Hole CUTOFF
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_exchange_term = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter EXCHANGE TERM
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_freq_mesh = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        unit='hartree',
        description='''
        ABINIT variable Bethe-Salpeter FREQuency MESH
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_hayd_term = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter HAYdock TERMinator
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_haydock_niter = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter HAYDOCK Number of Iterations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_haydock_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        ABINIT variable Bethe-Salpeter HAYDOCK TOLerance
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_interp_kmult = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Bethe-Salpeter INTERPolation K-point MULTiplication factors
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_interp_m3_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter INTERPolation Method3 WIDTH
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_interp_method = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter INTERPolation METHOD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_interp_mode = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter INTERPolation MODE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_interp_prep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter INTERPolation PREParation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_interp_rl_nb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter INTERPolation Rohlfing & Louie NeighBour
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_loband = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nsppol'],
        description='''
        ABINIT variable Bethe-Salpeter Lowest Occupied BAND
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bs_nstates = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Bethe-Salpeter Number of States
        ''',
        categories=[x_abinit_var])

    x_abinit_var_builtintest = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable BUIT-IN TEST number
        ''',
        categories=[x_abinit_var])

    x_abinit_var_bxctmindg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable BoX CuT-off MINimum for the Double Grid (PAW)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cd_customnimfrqs = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Contour Deformation Custom Imaginary Frequencies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cd_frqim_method = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Contour Deformation Imaginary Frequency integration Method
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cd_full_grid = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Contour Deformation Full Grid in complex plane
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cd_halfway_freq = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Contour Deformation tangent grid Halfway Frequency
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cd_imfrqs = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_cd_customnimfrqs'],
        description='''
        ABINIT variable Contour Deformation Imaginary Frequencies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cd_max_freq = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Contour Deformation grid Maximum Frequency
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cd_subset_freq = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable Contour Deformation grid calculate Subset of Frequencies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cgtyphf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Conjugate Gradient TYpe used for Hartree Fock exact exchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable CHARGE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_chkexit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable CHecK whether the user want to EXIT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_chkprim = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable CHecK whether the cell is PRIMitive
        ''',
        categories=[x_abinit_var])

    x_abinit_var_chksymbreak = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable CHecK SYMmetry BREAKing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_chneut = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable CHarge NEUTrality treatment
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cineb_start = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Climbing-Image Nudged Elastic Band: STARTing iteration
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cpuh = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable CPU time limit in Hours
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cpum = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable CPU time limit in Minutes
        ''',
        categories=[x_abinit_var])

    x_abinit_var_cpus = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable CPU time limit in seconds
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert1_atpol = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 1: limits of ATomic
        POLarisations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert1_dir = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 1: DIRections
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert1_elfd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 1: ELectric FielD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert1_phon = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 1: PHONons
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert2_atpol = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 2: limits of ATomic
        POLarisations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert2_dir = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 2: DIRections
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert2_elfd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 2: ELectric FielD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert2_phon = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 2: PHONons
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert3_atpol = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 3: limits of ATomic
        POLarisations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert3_dir = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 3: DIRections
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert3_elfd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 3: ELectric FielD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_d3e_pert3_phon = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable 3rd Derivative of Energy, mixed PERTurbation 3: PHONons
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ddamp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable electric Displacement field DAMPing parameter
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ddb_ngqpt = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Derivative DatabBase: Number of Grid points for Q-PoinTs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_delayperm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable DELAY between trials to PERMUTE atoms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_densfor_pred = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable DENSity and FORces PREDictor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_densty = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable initial DENSity for each TYpe of atom
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dfield = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable Displacement FIELD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dfpt_sciss = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable DFPT SCISSor operator
        ''',
        categories=[x_abinit_var])

    x_abinit_var_diecut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable DIElectric matrix Energy CUToff
        ''',
        categories=[x_abinit_var])

    x_abinit_var_diegap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable DIElectric matrix GAP
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dielam = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable DIElectric matrix LAMbda
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dielng = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable model DIElectric screening LeNGth
        ''',
        categories=[x_abinit_var])

    x_abinit_var_diemac = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable model DIElectric MACroscopic constant
        ''',
        categories=[x_abinit_var])

    x_abinit_var_diemix = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable model DIElectric MIXing factor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_diemixmag = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable model DIElectric MIXing factor for the MAGgnetization
        ''',
        categories=[x_abinit_var])

    x_abinit_var_diismemory = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Direct Inversion in the Iterative Subspace MEMORY
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dilatmx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable DILATation : MaXimal value
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dipdip = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable DIPole-DIPole interaction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmatpawu = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_natpawu', 'max(x_abinit_var_nsppol, x_abinit_var_nspinor)', '2*max(x_abinit_var_lpawu)+1', '2*max(x_abinit_var_lpawu)+1'],
        description='''
        ABINIT variable initial Density MATrix for PAW+U
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmatpuopt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Density MATrix for PAW+U OPTion
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmatudiag = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Density MATrix for paw+U, DIAGonalization
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_dc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Double Counting
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_entropy = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: ENTROPY
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_iter = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: number of ITERation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_mxsf = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: MiXing parameter for the SelF energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_nlambda = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Number of LAMBDA points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_nwli = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Number of frequency omega (W) in the
        LInear mesh
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_nwlo = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Number of frequency omega (W) in the
        log mesh
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_read_occnd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Read Occupations (Non Diagonal)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_rslf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Read SeLF energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_solv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: choice of SOLVer
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_t2g = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: t2g orbitals
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmft_tollc = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Tolerance on Local Charge for
        convergence of the DMFT loop
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftbandf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Field Theory: BAND: Final
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftbandi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Field Theory: BAND: Initial
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftcheck = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: CHECKs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_basis = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        basis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_check = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        check
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_correl = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        CORRelations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_gmove = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        Global MOVEs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_grnns = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        GReeNs NoiSe
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_meas = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        MEASurements
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_mov = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        MOVie
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_mrka = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        MARKov Analysis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftctqmc_order = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Continuous Time Quantum Monte Carlo
        perturbation ORDER
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftqmc_l = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Quantum Monte Carlo time sLices
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftqmc_n = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Quantum Monte Carlo sweeps
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftqmc_seed = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Quantum Monte Carlo seed
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dmftqmc_therm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Dynamical Mean Fied Theory: Quantum Monte Carlo THERMalization
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dosdeltae = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable DOS Delta in Energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dtion = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Delta Time for IONs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_dynimage = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nimage'],
        description='''
        ABINIT variable DYNamics of the IMAGE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ecut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Energy CUToff
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ecuteps = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Energy CUT-off for EPSilon (the dielectric matrix)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ecutsigx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Energy CUT-off for SIGma eXchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ecutsm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Energy CUToff SMearing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ecutwfn = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Energy CUT-off for WaveFunctions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_effmass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable EFFective MASS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efield = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable Electric FIELD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable EFfective MASs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_bands = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nkpt', 2],
        description='''
        ABINIT variable EFfective MASs, BANDS to be treated.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_calc_dirs = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable EFfective MASs, CALCulate along DIRectionS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_deg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable EFfective MASs, activate DEGenerate formalism
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_deg_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable EFfective MASs, DEGeneracy TOLerance
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_dim = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable EFfective MASs, DIMension of the effective mass tensor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_dirs = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_efmas_n_dirs', '3 or 2'],
        description='''
        ABINIT variable EFfective MASs, DIRectionS to be calculated
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_n_dirs = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable EFfective MASs, Number of DIRectionS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_efmas_ntheta = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable EFfective MASs, Number of points for integration w/r to THETA
        ''',
        categories=[x_abinit_var])

    x_abinit_var_elph2_imagden = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable ELectron-PHonon interaction at 2nd order : IMAGina y shoft of the
        DENominator
        ''',
        categories=[x_abinit_var])

    x_abinit_var_enunit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable ENergy UNITs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eph_extrael = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Electron-PHonon: EXTRA ELectrons
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eph_fermie = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Electron-PHonon: Fermi Energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eph_fsewin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Electron-Phonon: Fermi Surface Energy WINdow
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eph_fsmear = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Electron-PHonon: Fermi surface SMEARing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eph_intmeth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Electron-Phonon: INTegration METHod
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eph_mustar = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable MU STAR
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eph_ngqpt_fine = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Number of Grid Q-Points in FINE grid.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_eshift = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Energy SHIFT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_esmear = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Eigenvalue SMEARing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_exchmix = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable EXCHange MIXing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_exchn2n3d = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable EXCHange N2 and N3 Dimensions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_extrapwf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable flag - EXTRAPolation of the Wave-Functions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_f4of2_sla = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable F4 Over F2 ratio of Slater integrals
        ''',
        categories=[x_abinit_var])

    x_abinit_var_f6of2_sla = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable F6 Over F2 ratio of Slater integrals
        ''',
        categories=[x_abinit_var])

    x_abinit_var_fband = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Factor for the number of BANDs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_fermie_nest = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable FERMI Energy for printing the NESTing function
        ''',
        categories=[x_abinit_var])

    x_abinit_var_fftalg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Fast Fourier Transform ALGorithm
        ''',
        categories=[x_abinit_var])

    x_abinit_var_fftcache = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Fast Fourier Transform CACHE size
        ''',
        categories=[x_abinit_var])

    x_abinit_var_fftgw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable FFT for GW calculation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_freqim_alpha = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable FREQuencies along the IMaginary axis ALPHA parameter
        ''',
        categories=[x_abinit_var])

    x_abinit_var_freqremax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable FREQuencies along the Real axis MAXimum
        ''',
        categories=[x_abinit_var])

    x_abinit_var_freqremin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable FREQuencies along the Real axis MINimum
        ''',
        categories=[x_abinit_var])

    x_abinit_var_freqspmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable FREQuencies for the SPectral function MAXimum
        ''',
        categories=[x_abinit_var])

    x_abinit_var_freqspmin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable FREQuencies for the SPectral function MINimum
        ''',
        categories=[x_abinit_var])

    x_abinit_var_friction = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable internal FRICTION coefficient
        ''',
        categories=[x_abinit_var])

    x_abinit_var_frzfermi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable FReeZe FERMI energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_fxcartfactor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Forces to (X) CARTesian coordinates FACTOR
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ga_algor = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Genetic Algorithm selection
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ga_fitness = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Genetic Algorithm FITNESS function selection
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ga_n_rules = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Genetic Algorithm Number of RULES
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ga_opt_percent = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Genetic Algorithm OPTIMAL PERCENT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ga_rules = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Genetic Algorithm RULES
        ''',
        categories=[x_abinit_var])

    x_abinit_var_genafm = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable GENerator of the translation for Anti-FerroMagnetic space group
        ''',
        categories=[x_abinit_var])

    x_abinit_var_get1den = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the first-order density from _DEN file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_get1wf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the first-order wavefunctions from _1WF file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getbscoup = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the Bethe-Salpeter COUPling block from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getbseig = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the Bethe-Salpeter EIGenstates from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getbsreso = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the Bethe-Salpeter RESOnant block from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getcell = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET CELL parameters from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getddb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the DDB from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getddk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the ddk wavefunctions from _1WF file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the DENsity from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getgam_eig2nkq = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the GAMma phonon data EIG2NKQ from dataset
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gethaydock = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the Haydock restart file from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getocc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET OCC parameters from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getqps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET QuasiParticle Structure
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getscr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET SCReening (the inverse dielectric matrix) from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getsuscep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET SUSCEPtibility (the irreducible polarizability) from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getvel = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET VEL from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getwfk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of _1WF files
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getwfkfine = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the fine grid wavefunctions from _WFK file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getwfq = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET the wavefunctions from _WFQ file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getxcart = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET XCART from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_getxred = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GET XRED from ...
        ''',
        categories=[x_abinit_var])

    x_abinit_var_goprecon = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Geometry Optimization PRECONditioner equations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_goprecprm = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable Geometry Optimization PREconditioner PaRaMeters equations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gpu_devices = Quantity(
        type=np.dtype(np.int32),
        shape=[5],
        description='''
        ABINIT variable GPU: choice of DEVICES on one node
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gpu_linalg_limit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GPU (Cuda): LINear ALGebra LIMIT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw1rdm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW 1-Reduced Density Matrix
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_customnfreqsp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW CUSTOM SPectral FREQuencies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_freqsp = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_gw_customnfreqsp'],
        description='''
        ABINIT variable GW SPectral FREQuencies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_frqim_inzgrid = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Contour Deformation Imaginary Frequencies Inverse Z Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_frqre_inzgrid = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Contour Deformation Real Frequencies Inverse Z Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_frqre_tangrid = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Contour Deformation Use Tangent Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_icutcoul = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW CUT-off for COULomb interaction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_invalid_freq = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Invalid Frequency for Hybertsen-Louie PPM
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_nqlwl = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW, Number of Q-points for the Long Wave-Length Limit
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_nstep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW Number of self-consistent STEPS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_qlwl = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_gw_nqlwl', 3],
        description='''
        ABINIT variable GW, Q-points for the Long Wave-Length Limit
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_qprange = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW Policy for K-point and Bands selection
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_sctype = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW, Self-Consistency TYPE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_sigxcore = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW, SIGma (self-energy) for the CORE contribution
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gw_toldfeig = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable GW TOLerance on the DiFference of the EIGenvalues
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwaclowrank = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW Analytic Continuation LOW RANK approximation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwcalctyp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW CALCulation TYPe
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwcomp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW COMPletness
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwencomp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable GW Energy for COMPletness
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwgamma = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW Gamma
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwgmcorr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW Galitskii-Migdal CORRelation energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_band_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS BAND INDEX
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_correlation = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS CORRELATION
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_dielectric_model = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS dielectric model, version old
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_diel_model = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS dielectric model, version new
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_exchange = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS exact EXCHANGE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_first_seed = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS FIRST SEED vector
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_kmax_analytic = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS KMAX for the ANALYTIC term
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_kmax_complement = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS KMAX for the COMPLEMENT space.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_kmax_numeric = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS KMAX for the NUMERIC term
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_kmax_poles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS KMAX for the calculation of the POLES residue
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_list_proj_freq = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_gwls_n_proj_freq'],
        description='''
        ABINIT variable GWLS LIST of the PROJection FREQuencies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_model_parameter = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable GWLS model parameter
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_n_proj_freq = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS Number of PROJection FREQuencies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_npt_gauss_quad = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS Number of PoinTs to use for the GAUSSian QUADrature
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_nseeds = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS Number of SEED vectorS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_print_debug = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS PRINT level for DEBUGging
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_recycle = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS RECYCLE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_second_model_parameter = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable GWLS second model parameter
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_sternheimer_kmax = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS Kmax, version old
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwls_stern_kmax = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GWLS Kmax, version new
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwmem = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW MEMory
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwpara = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW PARAllelization level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_gwrpacorr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable GW RPA CORRelation energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iatcon = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nconeq', 'x_abinit_var_natcon'],
        description='''
        ABINIT variable Indices of AToms in CONstraint equations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iatfix = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_natfix'],
        description='''
        ABINIT variable Indices of AToms that are FIXed
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iatfixx = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_natfixx'],
        description='''
        ABINIT variable Indices of AToms that are FIXed along the X direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iatfixy = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_natfixy'],
        description='''
        ABINIT variable Indices of AToms that are FIXed along the Y direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iatfixz = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_natfixz'],
        description='''
        ABINIT variable Indices of AToms that are FIXed along the Z direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iatsph = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_natsph'],
        description='''
        ABINIT variable Index for the ATomic SPHeres of the atom-projected density-of-
        states
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iboxcut = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer governing the internal use of BOXCUT - not a very good
        choice of variable name
        ''',
        categories=[x_abinit_var])

    x_abinit_var_icoulomb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Coulomb TReaTMenT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_icutcoul = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the CUT-off for COULomb interaction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ieig2rf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for second-order EIGenvalues from Response-Function
        ''',
        categories=[x_abinit_var])

    x_abinit_var_imgmov = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable IMaGe MOVEs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_inclvkb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable INCLude VKB
        ''',
        categories=[x_abinit_var])

    x_abinit_var_intxc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable INTerpolation for eXchange-Correlation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iomode = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable IO MODE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ionmov = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable IONic MOVEs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iprcel = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for PReConditioning of ELectron response
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iprcfc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for PReConditioner of Force Constants
        ''',
        categories=[x_abinit_var])

    x_abinit_var_iqpt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Index for QPoinT generation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irandom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for the choice of the RANDOM number generator
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ird1den = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of 1st-order DEN file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ird1wf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of _1WF files
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdbscoup = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of COUPling block
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdbseig = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of BS_EIG file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdbsreso = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of RESOnant block
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdddb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of DDB file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdddk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of DDK wavefunctions, in _1WF
        files
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of DEN file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdhaydock = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of the HAYDOCK restart file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdqps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of QuasiParticle Structure
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdscr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of the SCReening
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdsuscep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of the SUSCEPtibility
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdvdw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of _VDW files
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdwfk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of _WFK files
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdwfkfine = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of the fine grid _WFK files
        ''',
        categories=[x_abinit_var])

    x_abinit_var_irdwfq = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer that governs the ReaDing of _WFQ files
        ''',
        categories=[x_abinit_var])

    x_abinit_var_isecur = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for level of SECURity choice
        ''',
        categories=[x_abinit_var])

    x_abinit_var_istatimg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer governing the computation of STATic IMaGes
        ''',
        categories=[x_abinit_var])

    x_abinit_var_istatr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for STATus file SHiFT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_istatshft = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for STATus file SHiFT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_istwfk = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nkpt'],
        description='''
        ABINIT variable Integer for choice of STorage of WaveFunction at each k point
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ixc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for eXchange-Correlation choice
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ixc_sigma = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Index of eXchange-Correlation functional used for self-energy calculations (SIGMA)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ixcpositron = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Integer for the eXchange-Correlation applied to the electron-
        POSITRON interaction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_jdtset = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_ndtset'],
        description='''
        ABINIT variable index -J- for DaTaSETs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_jellslab = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable include a JELLium SLAB in the cell
        ''',
        categories=[x_abinit_var])

    x_abinit_var_jfielddir = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable electric/displacement FIELD DIRection
        ''',
        categories=[x_abinit_var])

    x_abinit_var_jpawu = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        unit='hartree',
        description='''
        ABINIT variable value of J for PAW+U
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kberry = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nberry', 3],
        description='''
        ABINIT variable K wavevectors for BERRY phase computation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kpt = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nkpt', 3],
        description='''
        ABINIT variable K - PoinTs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kptbounds = Quantity(
        type=np.dtype(np.float64),
        shape=['abs(x_abinit_var_kptopt)+1)', 3],
        description='''
        ABINIT variable K PoinTs BOUNDarieS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kptgw = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 'x_abinit_var_nkptgw'],
        description='''
        ABINIT variable K-PoinTs for GW calculations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kptnrm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable K - PoinTs NoRMalization
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kptns = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nkpt', 3],
        description='''
        ABINIT variable K-PoinTs re-Normalized and Shifted
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kptopt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable KPoinTs OPTion
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kptrlatt = Quantity(
        type=np.dtype(np.int32),
        shape=[3, 3],
        description='''
        ABINIT variable K - PoinTs grid : Real space LATTice
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kptrlen = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable K - PoinTs grid : Real space LENgth
        ''',
        categories=[x_abinit_var])

    x_abinit_var_kssform = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Kohn Sham Structure file FORMat
        ''',
        categories=[x_abinit_var])

    x_abinit_var_lexexch = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable value of angular momentum L for EXact EXCHange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_localrdwf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable LOCAL ReaD WaveFunctions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_lotf_classic = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable LOTF classic model for Glue model
        ''',
        categories=[x_abinit_var])

    x_abinit_var_lotf_nitex = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable LOTF number of iterations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_lotf_nneigx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable LOTF max number of neighbours
        ''',
        categories=[x_abinit_var])

    x_abinit_var_lotf_version = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable LOTF version of MD algorithm
        ''',
        categories=[x_abinit_var])

    x_abinit_var_lpawu = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable value of angular momentum L for PAW+U
        ''',
        categories=[x_abinit_var])

    x_abinit_var_macro_uj = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Macro variable that activates the determination of the U and J
        parameter (for the PAW+U calculations)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_magcon_lambda = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable MAGnetization CONstraint LAMBDA parameter
        ''',
        categories=[x_abinit_var])

    x_abinit_var_magconon = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable turn MAGnetization CONstraint ON
        ''',
        categories=[x_abinit_var])

    x_abinit_var_max_ncpus = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable MAXimum Number of CPUS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_maxestep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable MAXimum Electric field STEP
        ''',
        categories=[x_abinit_var])

    x_abinit_var_maxnsym = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable MAXimum Number of SYMetries
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mband = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Maximum number of BANDs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mbpt_sciss = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Many Body Perturbation Theory SCISSor operator
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mdf_epsinf = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Model dielectric function, epsilon infinity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mdtemp = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        ABINIT variable Molecular Dynamics Temperatures
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mdwall = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Molecular Dynamics WALL location
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mem_test = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable MEMory TEST
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mep_mxstep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable Minimal Energy Path search: MaXimum allowed STEP size
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mep_solver = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Minimal Energy Path ordinary differential equation SOLVER
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mgfft = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Maximum of nGFFT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mgfftdg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Maximum of nGFFT for the Double Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mixalch = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypalch', 'x_abinit_var_npspalch'],
        description='''
        ABINIT variable MIXing coefficients for ALCHemical potentials
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mpw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Maximum number of Plane Waves
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mqgrid = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Maximum number of Q-space GRID points for pseudopotentials
        ''',
        categories=[x_abinit_var])

    x_abinit_var_mqgriddg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Maximum number of Q-wavevectors for the 1-dimensional GRID  for
        the Double Grid in PAW
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natcon = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nconeq'],
        description='''
        ABINIT variable Number of AToms in CONstraint equations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natfix = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Atoms that are FIXed
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natfixx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Atoms that are FIXed along the X direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natfixy = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Atoms that are FIXed along the Y direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natfixz = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Atoms that are FIXed along the Z direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of ATOMs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natpawu = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of AToms on which PAW+U is applied
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natrd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of AToms ReaD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natsph = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of ATomic SPHeres for the atom-projected density-of-states
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natsph_extra = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of ATomic SPHeres for the l-projected density-of-states in
        EXTRA set
        ''',
        categories=[x_abinit_var])

    x_abinit_var_natvshift = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of ATomic potential (V) energy SHIFTs (per atom)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nband = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nkpt', 'x_abinit_var_nsppol'],
        description='''
        ABINIT variable Number of BANDs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nbandhf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of BANDs for Fock exact exchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nbandkss = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of BANDs in the KSS file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nbdblock = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of BanDs in a BLOCK
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nbdbuf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of BanDs for the BUFfer
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nberry = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of BERRY phase computations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nc_xccc_gspace = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Norm-Conserving, use XC Core-Correction in G-space
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nconeq = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of CONstraint EQuations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nctime = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable NetCdf TIME between output of molecular dynamics informations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ndivk = Quantity(
        type=np.dtype(np.int32),
        shape=['abs(x_abinit_var_kptopt)'],
        description='''
        ABINIT variable Number of DIVisions of K lines
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ndivsm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of DIVisions for the SMallest segment
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ndtset = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of DaTaSETs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ndynimage = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of DYNamical IMAGEs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_neb_algo = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Nudged Elastic Band ALGOrithm
        ''',
        categories=[x_abinit_var])

    x_abinit_var_neb_spring = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        ABINIT variable Nudged Elastic Band: SPRING constant
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nelect = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Number of ELECTrons
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nfft = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of FFT points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nfftdg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of FFT points for the Double Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nfreqim = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of FREQuencies along the IMaginary axis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nfreqmidm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Nth FREQuencey Moment of the Imaginary part of the Dielectric
        Matrix
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nfreqre = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of FREQuencies along the REal axis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nfreqsp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of FREQuencies for the SPectral function
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ngfft = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Number of Grid points for Fast Fourier Transform
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ngfftdg = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Number of Grid points for Fast Fourier Transform : Double Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ngkpt = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Number of Grid points for K PoinTs generation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ngqpt = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Number of Grid pointsfor Q PoinTs generation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nimage = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of IMAGEs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nkpt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of K - Points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nkptgw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of K-PoinTs for GW corrections
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nkpthf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of K - Points for Fock exact exchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nline = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of LINE minimisations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nloc_alg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Non LOCal ALGorithm
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nloc_mem = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Non LOCal MEMOry
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nnos = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of nose masses
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nnsclo = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Non-Self Consistent LOops
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nnsclohf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Non-Self Consistent LOops for Fock exact exchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nobj = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of OBJects
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nomegasf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Number of OMEGA to evaluate the Spectral Function
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nomegasi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of OMEGA(S) along the Imaginary axis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nomegasrd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of OMEGA to evaluate the Sigma Real axis Derivative
        ''',
        categories=[x_abinit_var])

    x_abinit_var_normpawu = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable NORMalize atomic PAW+U projector
        ''',
        categories=[x_abinit_var])

    x_abinit_var_noseinert = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable NOSE thermostat INERTia factor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_np_slk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of mpi Processors used for ScaLapacK calls
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npband = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Processors at the BAND level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npfft = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Processors at the FFT level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nphf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Processors for Fock exact exchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npimage = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Processors at the IMAGE level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npkpt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Processors at the K-Point Level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nppert = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Processors at the PERTurbation level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npsp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of PSeudoPotentials
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npspalch = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of PSeudoPotentials that are "ALCHemical"
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npspinor = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Processors at the SPINOR level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npulayit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of PULAY ITerations for SC mixing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npvel = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Particle VELocities
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npweps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of PlaneWaves for EPSilon (the dielectric matrix)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npwkss = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of PlaneWaves in the KSS file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npwsigx = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of PlaneWaves for SIGma eXchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_npwwfn = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of PlaneWaves for WaveFunctioNs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nqpt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Q - POINTs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nqptdm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of Q-PoinTs for the Dielectric Matrix
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nscforder = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SCaling Function ORDER
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nshiftk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of SHIFTs for K point grids
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nshiftq = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of SHIFTs for Q point grids
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nspden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of SPin-DENsity components
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nspinor = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of SPINORial components of the wavefunctions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nsppol = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of SPin POLarization
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nstep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of (non-)self-consistent field STEPS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nsym = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of SYMmetry operations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ntime = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of TIME steps
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ntimimage = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of TIME steps for IMAGE propagation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ntypalch = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of TYPe of atoms that are "ALCHemical"
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ntypat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of TYPEs of atoms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ntyppure = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of TYPe of atoms that are "PURe"
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nucdipmom = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_natom', 3],
        description='''
        ABINIT variable NUClear DIPole MOMents
        ''',
        categories=[x_abinit_var])

    x_abinit_var_nwfshist = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Number of WaveFunctionS HISTory
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objaat = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_objan'],
        description='''
        ABINIT variable OBJect A : list of AToms, OBJect B : list of AToms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objaax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable OBJect A : AXis, OBJect B : AXis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objan = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OBJect A : Number of atoms, OBJect B : Number of atoms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objarf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OBJect A : Repetition Factors, OBJect B : Repetition Factors
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objaro = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable OBJect A : ROtations, OBJect B : ROtations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objatr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable OBJect A : TRanslations, OBJect B : TRanslations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objbat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OBJect A : list of AToms, OBJect B : list of AToms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objbax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable OBJect A : AXis, OBJect B : AXis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objbn = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OBJect A : Number of atoms, OBJect B : Number of atoms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objbrf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OBJect A : Repetition Factors, OBJect B : Repetition Factors
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objbro = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable OBJect A : ROtations, OBJect B : ROtations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_objbtr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable OBJect A : TRanslations, OBJect B : TRanslations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_occ = Quantity(
        type=np.dtype(np.float64),
        shape=['sum(x_abinit_var_nband)'],
        description='''
        ABINIT variable OCCupation numbers
        ''',
        categories=[x_abinit_var])

    x_abinit_var_occopt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OCCupation OPTion
        ''',
        categories=[x_abinit_var])

    x_abinit_var_omegasimax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable OMEGA to evaluate Sigma along the Imaginary axis D: MAXimal value
        ''',
        categories=[x_abinit_var])

    x_abinit_var_omegasrdmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable OMEGA to evaluate the Sigma Real axis Derivative : MAXimal value
        ''',
        categories=[x_abinit_var])

    x_abinit_var_optcell = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OPTimize the CELL shape and dimensions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_optdriver = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OPTions for the DRIVER
        ''',
        categories=[x_abinit_var])

    x_abinit_var_optforces = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OPTions for the calculation of FORCES
        ''',
        categories=[x_abinit_var])

    x_abinit_var_optnlxccc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OPTion for the calculation of Non-Linear eXchange-Correlation Core
        Correction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_optstress = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable OPTion for the computation of STRess
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ortalg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable ORThogonalisation ALGorithm
        ''',
        categories=[x_abinit_var])

    x_abinit_var_papiopt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAPI OPTion
        ''',
        categories=[x_abinit_var])

    x_abinit_var_paral_atom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable activate PARALelization over (paw) ATOMic sites
        ''',
        categories=[x_abinit_var])

    x_abinit_var_paral_kgb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable activate PARALelization over K-point, G-vectors and Bands
        ''',
        categories=[x_abinit_var])

    x_abinit_var_paral_rf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable activate PARALlelization over Response Function perturbations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawcpxocc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - use ComPleX rhoij OCCupancies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawcross = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - add CROSS term in oscillator strengths
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawecutdg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable PAW - Energy CUToff for the Double Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawfatbnd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW: print band structure in the FAT-BaND representation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawlcutd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - L angular momentum used to CUT the development in moments of
        the Densitites
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawlmix = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - maximum L used in the spherical part MIXing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawmixdg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - MIXing is done (or not) on the (fine) Double Grid
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawnhatxc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - Flag for exact computation of gradients of NHAT density in
        eXchange-Correlation.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawnphi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - Number of PHI angles used to discretize the sphere around
        each atom.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawntheta = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - Number of THETA angles used to discretize the sphere around
        each atom.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawnzlm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - only compute Non-Zero LM-moments of the contributions to the
        density from the spheres
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawoptmix = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - OPTion for the MIXing of the spherical part
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawoptosc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - OPTion for the computation of the OSCillator matrix elements
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawovlp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable PAW - spheres OVerLap allowed (in percentage)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawprt_b = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW print band
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawprt_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW print k-point
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawprtden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW: PRinT total physical electron DENsity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawprtdos = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW: PRinT partial DOS contributions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawprtvol = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW: PRinT VOLume
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawprtwf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW: PRinT WaveFunctions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawspnorb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - option for SPiN-ORBit coupling
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawstgylm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - option for the STorage of G_l(r).YLM(r)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawsushat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - SUSceptibility, inclusion of HAT (compensation charge)
        contribution
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawujat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW+macro_UJ, ATom number
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawujrad = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable PAW+macro_UJ, sphere RADius
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawujv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable PAW+macro_UJ, potential shift (V)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawusecp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - option for the USE of CPrj in memory (cprj=WF projected with
        NL projector)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pawxcdev = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PAW - choice for eXchange-Correlation DEVelopment (spherical part)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_intmeth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PHonon: INTegration METHod
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_ndivsm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PHonon: number of divisions for sampling the smallest segment
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_ngqpt = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable PHonon: Number of Grid points for Q-PoinT mesh.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_nqpath = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PHonon: numer of Q-points defining the PATH
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_nqshift = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PHonons: Number of q-SHIFTs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_qpath = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ph_nqpath', 3],
        description='''
        ABINIT variable Phonon: Q-PATH
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_qshift = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ph_nqshift', 3],
        description='''
        ABINIT variable PHONONS: Q-SHIFTs for mesh.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_smear = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable PHonon: SMEARing factor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ph_wstep = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable PHonons: frequency STEP.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pimass = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable Path Integral fictitious MASSes
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pitransform = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Path Integral coordinate TRANSFORMation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_bandf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions Initial BAND
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_bandi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions Initial BAND
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_compute = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions COMPUTATION
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_iatom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions,  ATOM Index
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_it = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_plowan_nt', 3],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions,  Index of Translation.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_lcalc = Quantity(
        type=np.dtype(np.int32),
        shape=['sum(x_abinit_var_plowan_nbl)'],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions,  L values to use for
        CALCulation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_natom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions, Number of ATOMs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_nbl = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_plowan_natom'],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions,  NumBer of L values
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_nt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions,  Number of Translation
        on which the real space values ofenergy are computed
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_projcalc = Quantity(
        type=np.dtype(np.int32),
        shape=['sum(x_abinit_var_plowan_nbl)'],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions,  PROJectors values to
        use for CALCulation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_plowan_realspace = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Projected Local Orbital WANnier functions,  activate REAL SPACE
        calculation.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_polcen = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable POLarization for Centrosymmetric geometry
        ''',
        categories=[x_abinit_var])

    x_abinit_var_posdoppler = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable POSitron computation of DOPPLER broadening
        ''',
        categories=[x_abinit_var])

    x_abinit_var_positron = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable POSITRON calculation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_posnstep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable POSitron calculation: max. Number of STEPs for the two-component
        DFT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_posocc = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable POSitron calculation: OCCupation number for the positron
        ''',
        categories=[x_abinit_var])

    x_abinit_var_postoldfe = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable POSITRON calculation: TOLerance on the DiFference of total Energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_postoldff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable POSitron calculation: TOLerance on the DiFference of Forces
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ppmfrq = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Plasmon Pole Model FReQuency
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ppmodel = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Plasmon Pole MODEL
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prepanl = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PREPAre Non-Linear response calculation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prepgkk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PREPAre GKK calculation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prepscphon = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PREPare Self-Consistent PHONon calculation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prt1dm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT 1-DiMensional potential and density
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtatlist = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT by ATom LIST of ATom
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtbbb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT Band-By-Band decomposition
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtbltztrp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT output for BoLTZTRaP code
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtcif = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT Crystallographic Information File
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the DENsity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtdensph = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT integral of DENsity inside atomic SPHeres
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtdipole = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT DIPOLE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtdos = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the Density Of States
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtdosm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the Density Of States with M decomposition
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtefg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRint Electric Field Gradient
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prteig = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT EIGenenergies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtelf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT Electron Localization Function (ELF)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtfc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT Fermi Contact term
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtfsurf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT Fermi SURFace file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtgden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the Gradient of electron DENsity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtgeo = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the GEOmetry analysis
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtgkk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the GKK matrix elements file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtgsr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the GSR file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtkden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the Kinetic energy DENsity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtkpt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the K-PoinTs sets
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtlden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the Laplacian of electron DENsity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtnabla = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRint NABLA
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtnest = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT NESTing function
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtposcar = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT POSCAR file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtpot = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT V_XC
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtpsps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRint the PSPS file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtspcur = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the SPin CURrent density
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtstm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the STM density
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtsuscep = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the SUSCEPtibility file (the irreducible polarizability)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvclmb = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT V CouLoMB
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvdw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT Van Der Waals file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvha = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT V_HArtree
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvhxc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT V_HXC
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvol = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT VOLume
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvolimg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT VOLume for IMaGes
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvpsp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT V_PSeudoPotential
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtvxc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT V_XC
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtwant = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT WANT file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtwf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT the WaveFunction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtwf_full = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT Wavefunction file on the FULL mesh
        ''',
        categories=[x_abinit_var])

    x_abinit_var_prtxml = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PRinT an XML output
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ptcharge = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable PoinT CHARGEs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ptgroupma = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable PoinT GROUP number for the MAgnetic space group
        ''',
        categories=[x_abinit_var])

    x_abinit_var_pvelmax = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable Particle VELocity MAXimum
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qmass = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nnos'],
        description='''
        ABINIT variable Q thermostat mass
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qprtrb = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Q-wavevector of the PERTurbation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qpt = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable Q PoinT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qptdm = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nqptdm', 3],
        description='''
        ABINIT variable Q-PoinTs for the Dielectric Matrix
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qptn = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable Q-PoinT re-Normalized
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qptnrm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Q PoinTs NoRMalization
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qptopt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable QPoinTs OPTion
        ''',
        categories=[x_abinit_var])

    x_abinit_var_qptrlatt = Quantity(
        type=np.dtype(np.int32),
        shape=[3, 3],
        description='''
        ABINIT variable Q - PoinTs grid : Real space LATTice
        ''',
        categories=[x_abinit_var])

    x_abinit_var_quadmom = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable QUADrupole MOMents
        ''',
        categories=[x_abinit_var])

    x_abinit_var_random_atpos = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RANDOM ATomic POSitions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ratsph = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable Radii of the ATomic SPHere(s)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ratsph_extra = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable Radii of the ATomic SPHere(s) in the EXTRA set
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Radius of the CUT-off for coulomb interaction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_recefermi = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable RECursion - initial guess  of the FERMI Energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_recgratio = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RECursion - Grid Ratio
        ''',
        categories=[x_abinit_var])

    x_abinit_var_recnpath = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RECursion - Number of point for PATH integral calculations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_recnrec = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RECursion - Number of RECursions
        ''',
        categories=[x_abinit_var])

    x_abinit_var_recptrott = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RECursion - TROTTer P parameter
        ''',
        categories=[x_abinit_var])

    x_abinit_var_recrcut = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RECursion - CUTing Radius
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rectesteg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RECursion - TEST on Electron Gas
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rectolden = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable RECursion - TOLerance on the difference of electronic DENsity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_red_dfield = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable REDuced Displacement FIELD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_red_efield = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable REDuced Electric FIELD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_red_efieldbar = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable REDuced Electric FIELD BAR
        ''',
        categories=[x_abinit_var])

    x_abinit_var_restartxf = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable RESTART from (X,F) history
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rf2_dkdk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function : 2nd Derivative of wavefunctions with respect
        to K
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfasr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function : Acoustic Sum Rule
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfatpol = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable Response Function : Acoustic Sum Rule
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfddk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function with respect to Derivative with respect to K
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfdir = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Response Function : DIRections
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfelfd = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function with respect to the ELectric FielD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfmeth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function METHod
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfphon = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function with respect to PHONons
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfstrs = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function with respect to STRainS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rfuser = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Response Function, USER-defined
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rhoqpmix = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable RHO QuasiParticle MIXing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_sigma_bsum_range = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable SIGMA: Band SUM RANGE
        ''',
        categories=[x_abinit_var])

    x_abinit_var_sigma_ngkpt = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable SIGMA: Number of Grid points for K PoinTs generation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_sigma_nshiftk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SIGMA: Number of SHIFTs for K point grids
        ''',
        categories=[x_abinit_var])

    x_abinit_var_sigma_shiftk = Quantity(
        type=np.dtype(np.int32),
        shape=[3, 'x_abinit_var_sigma_nshiftk'],
        description='''
        ABINIT variable SHIFT for K points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rprim = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        ABINIT variable Real space PRIMitive translations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_rprimd = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        ABINIT variable Real space PRIMitive translations, Dimensional
        ''',
        categories=[x_abinit_var])

    x_abinit_var_scalecart = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable SCALE CARTesian coordinates
        ''',
        categories=[x_abinit_var])

    x_abinit_var_scphon_supercell = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Self Consistent PHONon SUPERCELL
        ''',
        categories=[x_abinit_var])

    x_abinit_var_scphon_temp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Self Consistent PHONon TEMPerature
        ''',
        categories=[x_abinit_var])

    x_abinit_var_shiftk = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nshiftk', 3],
        description='''
        ABINIT variable SHIFT for K points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_shiftq = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nshiftq', 3],
        description='''
        ABINIT variable SHIFT for Q points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_signperm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SIGN of PERMutation potential
        ''',
        categories=[x_abinit_var])

    x_abinit_var_slabwsrad = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable jellium SLAB Wigner-Seitz RADius
        ''',
        categories=[x_abinit_var])

    x_abinit_var_slabzbeg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable jellium SLAB BEGinning edge along the Z direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_slabzend = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable jellium SLAB ENDing edge along the Z direction
        ''',
        categories=[x_abinit_var])

    x_abinit_var_smdelta = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SMeared DELTA function
        ''',
        categories=[x_abinit_var])

    x_abinit_var_so_psp = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_npsp'],
        description='''
        ABINIT variable Spin-Orbit treatment for each PSeudoPotential
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spbroad = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable SPectral BROADening
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spgaxor = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SPace Group : AXes ORientation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spgorig = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SPace Group : ORIGin
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spgroup = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SPace GROUP number
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spgroupma = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SPace GROUP number defining a MAgnetic space group
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spinat = Quantity(
        type=np.dtype(np.float64),
        shape=['min(x_abinit_var_natom,x_abinit_var_natrd)', 3],
        description='''
        ABINIT variable SPIN for AToms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spinmagntarget = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable SPIN-MAGNetization TARGET
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spmeth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SPectral METHod
        ''',
        categories=[x_abinit_var])

    x_abinit_var_spnorbscl = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable SPin-ORBit SCaLing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_stmbias = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Scanning Tunneling Microscopy BIAS voltage
        ''',
        categories=[x_abinit_var])

    x_abinit_var_strfact = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable STRess FACTor
        ''',
        categories=[x_abinit_var])

    x_abinit_var_string_algo = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable STRING method ALGOrithm
        ''',
        categories=[x_abinit_var])

    x_abinit_var_strprecon = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable STRess PRECONditioner
        ''',
        categories=[x_abinit_var])

    x_abinit_var_strtarget = Quantity(
        type=np.dtype(np.float64),
        shape=[6],
        description='''
        ABINIT variable STRess TARGET
        ''',
        categories=[x_abinit_var])

    x_abinit_var_symafm = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nsym'],
        description='''
        ABINIT variable SYMmetries, Anti-FerroMagnetic characteristics
        ''',
        categories=[x_abinit_var])

    x_abinit_var_symchi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SYMmetryze \\chi_o
        ''',
        categories=[x_abinit_var])

    x_abinit_var_symdynmat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SYMmetrize the DYNamical MATrix
        ''',
        categories=[x_abinit_var])

    x_abinit_var_symmorphi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SYMMORPHIc symmetry operations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_symrel = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_nsym', 3, 3],
        description='''
        ABINIT variable SYMmetry in REaL space
        ''',
        categories=[x_abinit_var])

    x_abinit_var_symsigma = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable SYMmetrization of SIGMA matrix elements
        ''',
        categories=[x_abinit_var])

    x_abinit_var_td_maxene = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Time-Dependent dft : MAXimal kohn-sham ENErgy difference
        ''',
        categories=[x_abinit_var])

    x_abinit_var_td_mexcit = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Time-Dependent dft : Maximal number of EXCITations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tfkinfunc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Thomas-Fermi KINetic energy FUNCtional
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tfw_toldfe = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Thomas-Fermi-Weizsacker: TOLerance on the DiFference of total
        Energy, for initialization steps
        ''',
        categories=[x_abinit_var])

    x_abinit_var_timopt = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable TIMing OPTion
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tl_nprccg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable TaiL maximum Number of PReConditionner Conjugate Gradient
        iterations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tl_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable TaiL expansion RADIUS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tnons = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nsym', 3],
        description='''
        ABINIT variable Translation NON-Symmorphic vectors
        ''',
        categories=[x_abinit_var])

    x_abinit_var_toldfe = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable TOLerance on the DiFference of total Energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_toldff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable TOLerance on the DiFference of Forces
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolimg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable TOLerance on the mean total energy for IMaGes
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolmxde = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable TOLerance on the MaXimal Difference in Energy
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolmxf = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable TOLerance on the MaXimal Force
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolrde = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable TOLerance on the Relative Difference of Eigenenergies
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolrff = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable TOLerance on the Relative diFference of Forces
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolsym = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable TOLERANCE for SYMmetries
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolvrs = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable TOLerance on the potential V(r) ReSidual
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tolwfr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable TOLerance on WaveFunction squared Residual
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tphysel = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Temperature (PHYSical) of the ELectrons
        ''',
        categories=[x_abinit_var])

    x_abinit_var_tsmear = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Temperature of SMEARing
        ''',
        categories=[x_abinit_var])

    x_abinit_var_typat = Quantity(
        type=np.dtype(np.int32),
        shape=['min(x_abinit_var_natom,x_abinit_var_natrd)'],
        description='''
        ABINIT variable TYPE of atoms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ucrpa = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable calculation of the screened interaction U with the Constrained RPA
        method
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ucrpa_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable For the calculation of U with the Constrained RPA method, gives
        correlated BANDS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ucrpa_window = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        ABINIT variable For the calculation of U with the Constrained RPA method, gives
        energy WINDOW
        ''',
        categories=[x_abinit_var])

    x_abinit_var_udtset = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable Upper limit on DaTa SETs
        ''',
        categories=[x_abinit_var])

    x_abinit_var_upawu = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        unit='hartree',
        description='''
        ABINIT variable value of U for PAW+U
        ''',
        categories=[x_abinit_var])

    x_abinit_var_use_gemm_nonlop = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE the GEMM routine for the application of the NON-Local OPerator
        ''',
        categories=[x_abinit_var])

    x_abinit_var_use_gpu_cuda = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable activate USE of GPU accelerators with CUDA (nvidia)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_use_nonscf_gkk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE NON-SCF calculation of GKK matrix elements (electron phonon)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_use_oldchi = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE OLD CHI implementation for evaluating \\chi_o with eigenvalues
        taken from a QPS file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_use_slk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE ScaLapacK
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usedmatpu = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE of an initial Density MATrix in Paw+U
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usedmft = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE Dynamical Mean Field Theory
        ''',
        categories=[x_abinit_var])

    x_abinit_var_useexexch = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE of EXact EXCHange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usefock = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE FOCK exact exchange
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usekden = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE Kinetic energy DENsity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usepaw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE Projector Augmented Waves method
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usepawu = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE PAW+U (spherical part)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usepotzero = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE POTential ZERO
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userec = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE RECursion
        ''',
        categories=[x_abinit_var])

    x_abinit_var_useria = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USER Integer variable A
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userib = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USER Integer variable B
        ''',
        categories=[x_abinit_var])

    x_abinit_var_useric = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USER Integer variable C
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userid = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USER Integer variable D
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userie = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USER Integer variable E
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userra = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable USER Real variable A
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userrb = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable USER Real variable B
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userrc = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable USER Real variable C
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userrd = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable USER Real variable D
        ''',
        categories=[x_abinit_var])

    x_abinit_var_userre = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable USER Real variable E
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usewvl = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Use WaVeLet basis set
        ''',
        categories=[x_abinit_var])

    x_abinit_var_usexcnhat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE eXchange-Correlation with NHAT (compensation charge density)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_useylm = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable USE YLM (the spherical harmonics)
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vaclst = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_vacnum'],
        description='''
        ABINIT variable VACancies LiST
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vacnum = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable VACancies NUMber
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vacuum = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable VACUUM identification
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vacwidth = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable VACuum WIDTH
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vcutgeo = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable V (potential) CUT-off GEOmetry
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_acutmin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF MINimum Angular CUT-off
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_aratio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF RATIO between the highest andlowest Angle.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_damax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF MAXimum Angular Delta
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_damin = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF MINimum Angular Delta
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_dcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF D-mesh CUT-off
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_dratio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF RATIO between the highest andlowest D.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_dsoft = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF SOFTening distance.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_gcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF K-space CUT-off
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_ndpts = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable vdW-DF Number of D-mesh PoinTS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_ngpts = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable vdW-DF Number of G-mesh PoinTS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_nqpts = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable vdW-DF Number of Q-mesh PoinTS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_nrpts = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable vdW-DF Number of R-PoinTS
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_nsmooth = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable vdW-DF Number of SMOOTHening iterations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_phisoft = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF SOFTening PHI value.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_qcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF Q-mesh CUT-off
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_qratio = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF RATIO between highest andlowest Q
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_rcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF Real-space CUT-off
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_rsoft = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF SOFTening radius.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_threshold = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF energy calculation threshold
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_tolerance = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF global TOLERANCE.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_tweaks = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable vdW-DF tweaks.
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_df_zab = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable vdW-DF Zab parameter
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_nfrag = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable van der Waals Number of interacting FRAGments
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_supercell = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        ABINIT variable Van Der Waals correction from Wannier functions in SUPERCELL
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable van der Waals TOLerance
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_tol_3bt = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable van der Waals TOLerance for 3-Body Term
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_typfrag = Quantity(
        type=np.dtype(np.int32),
        shape=['x_abinit_var_natom'],
        description='''
        ABINIT variable van der Waals TYPe of FRAGment
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vdw_xc = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable van der Waals eXchange-Correlation functional
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vel = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_natom', 3],
        description='''
        ABINIT variable VELocity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vel_cell = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        ABINIT variable VELocity of the CELL parameters
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vis = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable VIScosity
        ''',
        categories=[x_abinit_var])

    x_abinit_var_vprtrb = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        unit='hartree',
        description='''
        ABINIT variable potential -V- for the PeRTuRBation
        ''',
        categories=[x_abinit_var])

    x_abinit_var_w90iniprj = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Wannier90- INItial PROJections
        ''',
        categories=[x_abinit_var])

    x_abinit_var_w90prtunk = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable Wannier90- PRINT UNKp.s file
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wfoptalg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable WaveFunction OPTimisation ALGorithm
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wtatcon = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nconeq', 'x_abinit_var_natcon', 3],
        description='''
        ABINIT variable WeighTs for AToms in CONstraint equations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wtk = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_nkpt'],
        description='''
        ABINIT variable WeighTs for K points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wtq = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable WeighTs for the current Q-points
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wvl_bigdft_comp = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable WaVeLet BigDFT Comparison
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wvl_crmult = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable WaVeLet Coarse grid Radius MULTiplier
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wvl_frmult = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable WaVeLet Fine grid Radius MULTiplier
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wvl_hgrid = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='bohr',
        description='''
        ABINIT variable WaVeLet H step GRID
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wvl_ngauss = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        ABINIT variable WaVeLet Number of GAUSSians
        ''',
        categories=[x_abinit_var])

    x_abinit_var_wvl_nprccg = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable WaVeLet maximum Number of PReConditionner Conjugate Gradient
        iterations
        ''',
        categories=[x_abinit_var])

    x_abinit_var_x1rdm = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable EXchange-only 1-Reduced Density Matrix
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xangst = Quantity(
        type=np.dtype(np.float64),
        shape=['min(x_abinit_var_natom,x_abinit_var_natrd)', 3],
        description='''
        ABINIT variable vectors (X) of atom positions in cartesian coordinates -length in
        ANGSTrom-
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xc_denpos = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable eXchange-Correlation - DENsity POSitivity value
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xc_tb09_c = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ABINIT variable Value of the c parameter in the eXchange-Correlation TB09
        functional
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xcart = Quantity(
        type=np.dtype(np.float64),
        shape=['min(x_abinit_var_natom,x_abinit_var_natrd)', 3],
        unit='bohr',
        description='''
        ABINIT variable vectors (X) of atom positions in CARTesian coordinates
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xclevel = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ABINIT variable eXchange Correlation functional level
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xred = Quantity(
        type=np.dtype(np.float64),
        shape=['min(x_abinit_var_natom,x_abinit_var_natrd)', 3],
        description='''
        ABINIT variable vectors (X) of atom positions in REDuced coordinates
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xredsph_extra = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_natsph_extra', 3],
        description='''
        ABINIT variable X(position) in REDuced coordinates of the SPHeres for dos
        projection in the EXTRA set
        ''',
        categories=[x_abinit_var])

    x_abinit_var_xyzfile = Quantity(
        type=str,
        shape=[],
        description='''
        ABINIT variable XYZ FILE input for geometry
        ''',
        categories=[x_abinit_var])

    x_abinit_var_zcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='hartree',
        description='''
        ABINIT variable Z-CUT
        ''',
        categories=[x_abinit_var])

    x_abinit_var_zeemanfield = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        ABINIT variable ZEEMAN FIELD
        ''',
        categories=[x_abinit_var])

    x_abinit_var_ziontypat = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_ntypat'],
        description='''
        ABINIT variable Z (charge) of the IONs for the different TYPes of AToms
        ''',
        categories=[x_abinit_var])

    x_abinit_var_znucl = Quantity(
        type=np.dtype(np.float64),
        shape=['x_abinit_var_npsp'],
        description='''
        ABINIT variable charge -Z- of the NUCLeus
        ''',
        categories=[x_abinit_var])


class x_abinit_section_dataset(MSection):
    '''
    -
    '''

    m_def = Section(validate=False)

    x_abinit_section_input = SubSection(
        sub_section=x_abinit_section_input.m_def,
        repeats=False)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_abinit_section_dataset = SubSection(
        sub_section=x_abinit_section_dataset.m_def,
        repeats=True)
