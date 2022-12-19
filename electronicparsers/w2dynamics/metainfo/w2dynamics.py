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
import numpy as np

from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, Package, Quantity, Section, SubSection, JSON
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_w2dynamics_axes(MSection):
    '''
    Section containing data in .axes of the hdf5 mainfile.
    '''

    m_def = Section(validate=False)

    x_w2dynamics_iw = Quantity(
        type=np.float64,
        shape=['Niw'],
        description='''
        Matsubara frequencies.
        ''')

    x_w2dynamics_iwb_g4 = Quantity(
        type=np.float64,
        shape=['N4iwb'],
        description='''
        Number of bosonic Matsubaras for 4-point GF.
        ''')

    x_w2dynamics_iwb_p2 = Quantity(
        type=np.float64,
        shape=[],
        description='''
        ''')

    x_w2dynamics_iwb_p3 = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_iwf_g2 = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_iwf_g4 = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_iwf_p3 = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_iwb_g4 = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_iwb_p3 = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_pos_iw = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_tau = Quantity(
        type=np.float64,
        shape=['Ntau'],
        description='''
        Tau times.
        ''')

    x_w2dynamics_tau_g4 = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_taubin = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_tauf = Quantity(
        type=np.float64,
        shape=['Nftau'],
        description='''
        ''')

    x_w2dynamics_tausus = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        ''')

    x_w2dynamics_w_dos = Quantity(
        type=np.float64,
        shape=['0..*'],
        description='''
        Energies for the DOS.
        ''')


class x_w2dynamics_quantities(MSection):
    '''
    Section containing data in .quantities of the hdf5 mainfile.
    '''

    m_def = Section(validate=False)

    x_w2dynamics_accept_flavourchange = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for flavourchange moves
        ''')

    x_w2dynamics_accept_glob = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for global symmetry moves
        ''')

    x_w2dynamics_accept_ins = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for insertions into local trace
        ''')

    x_w2dynamics_accept_ins4 = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for insertions of 4 operators into local trace
        ''')

    x_w2dynamics_accept_pair_tau = Quantity(
        type=np.float64,
        description='''
        Total number of accepted pair insertions and removals in tau bins
        ''')

    x_w2dynamics_accept_rem = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for removals of local trace operators
        ''')

    x_w2dynamics_accept_rem4 = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for removal of 4 operators in the local trace
        ''')

    x_w2dynamics_accept_shift = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for tau-shift moves
        ''')

    x_w2dynamics_accept_worm_ins = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for worm insertions into local trace
        ''')

    x_w2dynamics_accept_worm_rem = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for worm removals from local trace
        ''')

    x_w2dynamics_accept_worm_rep = Quantity(
        type=np.float64,
        description='''
        Acceptance rate for worm replacement moves
        ''')

    x_w2dynamics_at2neq = Quantity(
        type=np.float64,
        description='''
        corresponding inequivalent index to atom index
        ''')

    x_w2dynamics_contrib_sst = Quantity(
        type=np.float64,
        description='''
        Trace contribution per outer superstate
        ''')

    x_w2dynamics_contrib_state = Quantity(
        type=np.float64,
        description='''
        Trace contribution per outer state
        ''')

    x_w2dynamics_dc = Quantity(
        type=np.float64,
        description='''
        double counting correction
        ''')

    x_w2dynamics_dc_latt = Quantity(
        type=np.float64,
        description='''
        double counting correction on the lattice
        ''')

    x_w2dynamics_densitymatrix = Quantity(
        type=np.float64,
        description='''
        Density matrix in occupation number basis measured at beta/2
        ''')

    x_w2dynamics_double_occ = Quantity(
        type=np.float64,
        description='''
        Double occupancies <n_i n_j>
        ''')

    x_w2dynamics_energies_eigenstates = Quantity(
        type=np.float64,
        description='''
        Energies of eigenstates by state index
        ''')

    x_w2dynamics_expresdensitymatrix = Quantity(
        type=np.float64,
        description='''
        density matrix resolved by expansion order
        ''')

    x_w2dynamics_fiw = Quantity(
        type=np.complex128,
        description='''
        hybridisation function in Matsubara frequencies
        ''')

    x_w2dynamics_fmom = Quantity(
        type=np.complex128,
        description='''
        moments of the Hybridisation function in iw
        ''')

    x_w2dynamics_ftau = Quantity(
        type=np.complex128,
        description='''
        hybridisation function in imaginary time
        ''')

    x_w2dynamics_ftau_full = Quantity(
        type=np.complex128,
        description='''
        hybridisation function in imaginary time
        ''')

    x_w2dynamics_g0iw = Quantity(
        type=np.complex128,
        description='''
        Weiss field
        ''')

    x_w2dynamics_g0iw_full = Quantity(
        type=np.complex128,
        description='''
        Weiss field including spin/orbital off-diagonal terms
        ''')

    x_w2dynamics_g2iw = Quantity(
        type=np.complex128,
        description='''
        Two-particle Green's function in Matsubara basis
        ''')

    x_w2dynamics_g4iw = Quantity(
        type=np.complex128,
        description='''
        Two-particle Green's function in Matsubara basis (particle-hole channel)
        ''')

    x_w2dynamics_g4iw_pp = Quantity(
        type=np.complex128,
        description='''
        Two-particle Green's function in Matsubara basis (particle-particle channel)
        ''')

    x_w2dynamics_g4iw_worm = Quantity(
        type=np.complex128,
        description='''
        Two-particle Green's function in particle-hole Matsubara frequencies from worm sampling
        There are two conventions:
        0: (v+w) tau_1 - v tau_2 + v' tau_3 - (v'+w) tau_4
        1: v tau_1 - (v-w) tau_2 + (v'-w) tau_3 - v' tau_4
        ''')

    x_w2dynamics_g4iwpp_worm = Quantity(
        type=np.complex128,
        description='''
        Two-particle Green's function in particle-particle Matsubara frequencies from worm sampling
        Convention: v tau_1 - (w-v') tau_2 + (w-v) tau_3 - v' tau_4
        ''')

    x_w2dynamics_g4leg = Quantity(
        type=np.complex128,
        description='''
        Two-particle Green's function in Legendre/Matsubara basis
        ''')

    x_w2dynamics_g4tau = Quantity(
        type=np.complex128,
        description='''
        Two-particle Green's function in tau12, tau34, tau14
        ''')

    x_w2dynamics_gdensnew = Quantity(
        type=np.complex128,
        description='''
        densities with new self-energy after adjustment of mu
        ''')

    x_w2dynamics_gdensold = Quantity(
        type=np.complex128,
        description='''
        densities with old self-energy before adjustment of mu
        ''')

    x_w2dynamics_giw = Quantity(
        type=np.complex128,
        description='''
        impurity Green's function used as input for Dyson equation
        ''')

    x_w2dynamics_giw_cov = Quantity(
        type=np.complex128,
        description='''
        covariance of diagonal impurity Green's function
        ''')

    x_w2dynamics_giw_full = Quantity(
        type=np.complex128,
        description='''
        impurity Green's function used as input for Dyson equation
        ''')

    x_w2dynamics_giw_meas = Quantity(
        type=np.complex128,
        description='''
        Impurity Green's function in Matsubara
        ''')

    x_w2dynamics_giw_worm = Quantity(
        type=np.complex128,
        description='''
        Impurity Green's function in Matsubara from worm sampling
        ''')

    x_w2dynamics_gleg = Quantity(
        type=np.complex128,
        description='''
        impurity Green's function in Legendre expansion
        ''')

    x_w2dynamics_gleg_full = Quantity(
        type=np.complex128,
        description='''
        full impurity Green's function in Legendre expansion
        ''')

    x_w2dynamics_glocnew = Quantity(
        type=np.complex128,
        description='''
        local Green's function in Matsubara (new self-energy)
        ''')

    x_w2dynamics_glocnew_lattice = Quantity(
        type=np.complex128,
        description='''
        local Green's function in Matsubara (old self-energy), diagonal part for all lda-bands
        ''')

    x_w2dynamics_glocold = Quantity(
        type=np.complex128,
        description='''
        local Green's function in Matsubara (old self-energy)
        ''')

    x_w2dynamics_glocold_lattice = Quantity(
        type=np.complex128,
        description='''
        local Green's function in Matsubara (old self-energy), diagonal part for all lda-bands
        ''')

    x_w2dynamics_gsigmaiw = Quantity(
        type=np.complex128,
        description='''
        Improved estimators in Matsubara basis
        ''')

    x_w2dynamics_gsigmaiw_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Improved estimators in Matsubara basis
        ''')

    x_w2dynamics_gtau = Quantity(
        type=np.float64,
        description='''
        impurity Green's function on the imaginary time axis
        ''')

    x_w2dynamics_gtau_blocks = Quantity(
        type=np.float64,
        description='''
        blocking analysis for the impurity Green's function
        ''')

    x_w2dynamics_gtau_full = Quantity(
        type=np.float64,
        description='''
        impurity Green's function on the imaginary time axis, full offdiagonal
        ''')

    x_w2dynamics_gtau_mean_step = Quantity(
        type=np.float64,
        description='''
        impurity Green's function averaged over tau, resolved in time (= Monte carlo steps)
        ''')

    x_w2dynamics_gtau_mid_step = Quantity(
        type=np.float64,
        description='''
        impurity Green's function averaged over tau between 0.4 * beta and 0.6 * beta, resolved in time (= Monte carlo steps)
        ''')

    x_w2dynamics_gtau_worm = Quantity(
        type=np.float64,
        description='''
        Impurity Green's function in imaginary time from worm sampling
        ''')

    x_w2dynamics_h_mean = Quantity(
        type=np.complex128,
        description='''
        Mean over k-points of Hamiltonian H(k)
        ''')

    x_w2dynamics_h_mom2 = Quantity(
        type=np.float64,
        description='''
        Second moment of the density of states
        ''')

    x_w2dynamics_h4iw_worm = Quantity(
        type=np.float64,
        description='''
        Two-particle improved estimator in Matsubara basis from worm sampling
        ''')

    x_w2dynamics_hist = Quantity(
        type=np.float64,
        description='''
        Histogram for expansion orders
        ''')

    x_w2dynamics_hist_seg = Quantity(
        type=np.float64,
        description='''
        number of empty flavours in trace
        ''')

    x_w2dynamics_hist_sst = Quantity(
        type=np.float64,
        description='''
        Histogram for outer superstates
        ''')

    x_w2dynamics_hist_state = Quantity(
        type=np.float64,
        description='''
        Histogram for outer states
        ''')

    x_w2dynamics_hk = Quantity(
        type=np.complex128,
        description='''
        Full Hamiltonian H(k)
        ''')

    x_w2dynamics_hk_mean = Quantity(
        type=np.complex128,
        description='''
        Mean of diagonals of Hamiltonian H(k)
        ''')

    x_w2dynamics_jbar = Quantity(
        type=np.float64,
        description='''
        shell-averaged J values
        ''')

    x_w2dynamics_lda_dens = Quantity(
        type=np.float64,
        description='''
        LDA orbital-resolved densities
        ''')

    x_w2dynamics_lda_dos = Quantity(
        type=np.float64,
        description='''
        LDA density of states
        ''')

    x_w2dynamics_lda_mu = Quantity(
        type=np.float64,
        description='''
        chemical potential (non-interacting)
        ''')

    x_w2dynamics_leadsiw_full = Quantity(
        type=np.float64,
        description='''
        Weiss field including spin/orbital off-diagonal terms
        ''')

    x_w2dynamics_lhist = Quantity(
        type=np.float64,
        description='''
        Histogram for Lanczos steps in the time evolution
        ''')

    x_w2dynamics_mu = Quantity(
        type=np.float64,
        description='''
        chemical potential (lattice model)
        ''')

    x_w2dynamics_muimp = Quantity(
        type=np.complex128,
        description='''
        impurity chemical potential
        ''')

    x_w2dynamics_muimp_full = Quantity(
        type=np.complex128,
        description='''
        impurity chemical potential
        ''')

    x_w2dynamics_neq2at = Quantity(
        type=np.float64,
        description='''
        atom index first occurrence of inequivalent atom
        ''')

    x_w2dynamics_nneq = Quantity(
        type=np.float64,
        description='''
        number of non-equivalent atoms in unit cell
        ''')

    x_w2dynamics_nqqdag_worm = Quantity(
        type=np.float64,
        description='''
        Part of Symmetric Improved 2P estimator in Matsubara frequencies
        ''')

    x_w2dynamics_ntau_n0 = Quantity(
        type=np.float64,
        description='''
        density-density correlation function in tau bins
        ''')

    x_w2dynamics_occ = Quantity(
        type=np.float64,
        description='''
        Occupancies
        ''')

    x_w2dynamics_occbasis_mapping = Quantity(
        type=np.float64,
        description='''
        Occupation number eigenvalues by state index as used in densitymatrix
        ''')

    x_w2dynamics_p2iw_worm = Quantity(
        type=np.complex128,
        description='''
        Two legged two-particle Green's function ph-convention (1 bosonic)
        ''')

    x_w2dynamics_p2iwpp_worm = Quantity(
        type=np.complex128,
        description='''
        Two legged two-particle Green's function pp-convention (1 bosonic)
        ''')

    x_w2dynamics_p2tau_worm = Quantity(
        type=np.complex128,
        description='''
        Two legged two-particle Green's function in imaginary time
        ''')

    x_w2dynamics_p2taupp_worm = Quantity(
        type=np.complex128,
        description='''
        Two legged two-particle Green's function pp in imaginary time
        ''')

    x_w2dynamics_p3iw_worm = Quantity(
        type=np.complex128,
        description='''
        Three legged two-particle Green's function ph-convention (1 fermionic, 1 bosonic)
        ''')

    x_w2dynamics_p3iwpp_worm = Quantity(
        type=np.complex128,
        description='''
        Three legged two-particle Green's function pp-convention (1 fermionic, 1 bosonic)
        ''')

    x_w2dynamics_qqdd_worm = Quantity(
        type=np.complex128,
        description='''
        Part of Symmetric Improved 2P estimator in Matsubara frequencies
        ''')

    x_w2dynamics_qqiw_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Symmetric Improved 1P estimator in Matsubara basis
        ''')

    x_w2dynamics_qqqq_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Symmetric Improved 2P estimators in Matsubara basis
        ''')

    x_w2dynamics_qqtau_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Symmetric Improved 1P estimator in imaginary time
        ''')

    x_w2dynamics_quddag_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Improved estimators in Matsubara basis
        ''')

    x_w2dynamics_rhist = Quantity(
        type=np.float64,
        description='''
        Histogram for additional Lanczos steps needed for reversible trace
        ''')

    x_w2dynamics_rho1 = Quantity(
        type=np.float64,
        description='''
        < c^+ c >
        ''')

    x_w2dynamics_rho2 = Quantity(
        type=np.float64,
        description='''
        < c^+ c^+ c c >
        ''')

    x_w2dynamics_sigma_hartree = Quantity(
        type=np.complex128,
        description='''
        Hartree self-energy
        ''')

    x_w2dynamics_sign = Quantity(
        type=np.float64,
        description='''
        Mean sign
        ''')

    x_w2dynamics_sign_sst = Quantity(
        type=np.float64,
        description='''
        Summed total sign per outer superstate
        ''')

    x_w2dynamics_sign_state = Quantity(
        type=np.float64,
        description='''
        Summed total sign per outer state
        ''')

    x_w2dynamics_sign_step = Quantity(
        type=np.float64,
        description='''
        Sign of a configuration's total weight, resolved in time (= Monte carlo steps)
        ''')

    x_w2dynamics_single_occ = Quantity(
        type=np.float64,
        description='''
        Single occupancies <n_i>
        ''')

    x_w2dynamics_siw = Quantity(
        type=np.complex128,
        description='''
        Band-spin-diagonal self-energy in matsubara expansion
        ''')

    x_w2dynamics_siw_cov = Quantity(
        type=np.complex128,
        description='''
        covariance of diagonal self-energy in matsubara expansion
        ''')

    x_w2dynamics_siw_full = Quantity(
        type=np.complex128,
        description='''
        Full self-energy in matsubara expansion (with jackknife error)
        ''')

    x_w2dynamics_siw_trial = Quantity(
        type=np.complex128,
        description='''
        Full trial self-energy in matsubara expansion
        ''')

    x_w2dynamics_smom = Quantity(
        type=np.float64,
        description='''
        Moments of the self-energy (in Matsubara)
        ''')

    x_w2dynamics_smom_full = Quantity(
        type=np.float64,
        description='''
        Moments of the self-energy including all terms
        ''')

    x_w2dynamics_ssts_states = Quantity(
        type=np.float64,
        description='''
        Assignment of states to superstates by state index
        ''')

    x_w2dynamics_steps_worm_partition = Quantity(
        type=np.float64,
        description='''
        Time spent in worm space and partition space
        ''')

    x_w2dynamics_time = Quantity(
        type=np.float64,
        description='''
        Total elapsed walltime of the run
        ''')

    x_w2dynamics_time_g4iw_add = Quantity(
        type=np.float64,
        description='''
        Time spent on constructing and adding G4(iw,iw,iW)
        ''')

    x_w2dynamics_time_g4iw_ft = Quantity(
        type=np.float64,
        description='''
        Time spent on fourier-transforming G4(iw,iw,iW)
        ''')

    x_w2dynamics_time_giw = Quantity(
        type=np.float64,
        description='''
        Time spent on measuring G(iw)
        ''')

    x_w2dynamics_time_qmc = Quantity(
        type=np.float64,
        description='''
        Mean CPU seconds spent in CT-QMC per process
        ''')

    x_w2dynamics_time_sampling = Quantity(
        type=np.float64,
        description='''
        CPU time used for the QMC simulation excluding measurements
        ''')

    x_w2dynamics_time_simulation = Quantity(
        type=np.float64,
        description='''
        CPU time used for the QMC simulation
        ''')

    x_w2dynamics_time_warmup = Quantity(
        type=np.float64,
        description='''
        CPU time used for the QMC warmup
        ''')

    x_w2dynamics_ubar = Quantity(
        type=np.float64,
        description='''
        shell-averaged U values
        ''')

    x_w2dynamics_ucaca_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Symmetric Improved 2P estimators in Matsubara basis
        ''')

    x_w2dynamics_ucacatau_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Symmetric Improved 2P estimators in Matsubara basis
        ''')

    x_w2dynamics_uccaa_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Symmetric Improved 2P estimators in Matsubara basis
        ''')

    x_w2dynamics_uccaatau_worm = Quantity(
        type=np.complex128,
        description='''
        Worm Symmetric Improved 2P estimators in Matsubara basis
        ''')

    x_w2dynamics_worm_eta = Quantity(
        type=np.complex128,
        description='''
        Worm balancing factor
        ''')


class x_w2dynamics_config_atoms_parameters(MSection):
    '''
    Input quantities contained in .config:atom.{x}.{name} of the hdf5 mainfile.
    '''

    m_def = Section(validate=False)

    x_w2dynamics_hamiltonian = Quantity(
        type=str,
        description='''
        Type of interacting hamiltonian.
        ''')

    x_w2dynamics_jdd = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        Hunds coupling.
        ''')

    x_w2dynamics_jdp = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        J interaction between d-p orbitals.
        ''')

    x_w2dynamics_jpp = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        J interaction between p-p orbitals.
        ''')

    x_w2dynamics_jppod = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        ''')

    x_w2dynamics_nd = Quantity(
        type=np.int32,
        description='''
        Number of d bands.
        ''')

    x_w2dynamics_nlig = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_np = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nsymmove = Quantity(
        type=np.int32,
        description='''
        Number of symmetry moves.
        ''')

    x_w2dynamics_phonon = Quantity(
        type=np.int32,
        description='''
        Switch for phonon interaction.
        ''')

    x_w2dynamics_quantumnumbers = Quantity(
        type=str,
        description='''
        Good quantum numbers. Separated entries: "Nt" for total occupation, "Szt" for
        spin component, "Qzt" for singly-occupiedness per orbital, "Azt" for occupation
        per spin-orbital, "Lzt" for orbital angular momentum component assuming uniformly
        spaced ascending values symmetric around zero for the impurity orbitals, "Jzt"
        for total angular momentum component, and "All" for automatic partitioning of the
        Hamiltonian into blocks.
        ''')

    x_w2dynamics_screening = Quantity(
        type=np.int32,
        description='''
        Switch for dynamical screening.
        ''')

    x_w2dynamics_se_shift = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_udd = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        Hubbard intra-orbital interaction.
        ''')

    x_w2dynamics_udp = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        U\' interaction between d-p orbitals.
        ''')

    x_w2dynamics_umatrix = Quantity(
        type=str,
        description='''
        String containing the .dat file with the U-interactions matrix.
        ''')

    x_w2dynamics_upp = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        U interaction between p-p orbitals.
        ''')

    x_w2dynamics_uppod = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        ''')

    x_w2dynamics_vdd = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        Hubbard inter-orbital interaction.
        ''')

    x_w2dynamics_vpp = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        U\' interaction between p-p orbitals.
        ''')


class x_w2dynamics_config_general_parameters(MSection):
    '''
    Input quantities contained in .config:general.{name} of the hdf5 mainfile.
    '''

    m_def = Section(validate=False)

    x_w2dynamics_beta = Quantity(
        type=np.float64,
        description='''
        Inverse temperature.
        ''')

    x_w2dynamics_computedeltan = Quantity(
        type=np.int32,
        description='''
        0 (false) or 1 (true).
        ''')

    x_w2dynamics_curvefit_maxhistory = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_curvefit_minhistory = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_curvefit_startat = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_curvefit_termdiffminlen = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_curvefit_termdiffthresh = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_curvefit_termminhist = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_curvefit_termntoterrfact = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_curvefit_termntotminlen = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_dc = Quantity(
        type=str,
        description='''
        Double counting mixing type: 'anisimov', 'fll', 'amf', 'trace', 'siginfbar',
        'sigzerobar'. Default = 'anisimov'.
        ''')

    x_w2dynamics_dc_dp = Quantity(
        type=np.int32,
        description='''
        Fixint of energetic distance between d and p orbitals.
        ''')

    x_w2dynamics_dc_mixing = Quantity(
        type=np.float64,
        description='''
        Mixing between old and new SE.
        ''')

    x_w2dynamics_dmftsteps = Quantity(
        type=np.int32,
        description='''
        Number of DMFT iterations.
        ''')

    x_w2dynamics_dos = Quantity(
        type=str,
        description='''
        DOS input information: 'flat', 'semicirc', 'ReadIn', 'ReadInSO', 'Bethe',
        'Bethe_in_tau', 'EDcheck', 'nano', 'CoulvsKan', 'readDelta'. Default = 'Bethe'.
        ''')

    x_w2dynamics_dos_deltino = Quantity(
        type=np.float64,
        description='''
        Deltino for the LDA DOS calculation
        ''')

    x_w2dynamics_dump_mixer = Quantity(
        type=str,
        description='''
        ''')

    x_w2dynamics_epseq = Quantity(
        type=np.float64,
        description='''
        Epsilon for identical atom in unit cell.
        ''')

    x_w2dynamics_epsldan = Quantity(
        type=np.float64,
        description='''
        Eps between lda dens and totdens readjust mu.
        ''')

    x_w2dynamics_epsmatsn = Quantity(
        type=np.float64,
        description='''
        Rps between model and num tail to trunc.
        ''')

    x_w2dynamics_epsn = Quantity(
        type=np.float64,
        description='''
        eps between mats sum and totdens readjust mu.
        ''')

    x_w2dynamics_epsoffdiag = Quantity(
        type=np.float64,
        description='''
        Epsilon for checking off-diagonal Hybridisation elements.
        ''')

    x_w2dynamics_eqmaxfreq = Quantity(
        type=np.float64,
        description='''
        Frequency cut-off for equivalence detection.
        ''')

    x_w2dynamics_filenameprefix = Quantity(
        type=str,
        description='''
        Prefix for output file.
        ''')

    x_w2dynamics_fileold = Quantity(
        type=str,
        description='''
        ''')

    x_w2dynamics_fttype = Quantity(
        type=str,
        description='''
        FFT type: 'none', 'plain', 'legendre', 'none_worm'. Default = 'legendre'.
        ''')

    x_w2dynamics_gw = Quantity(
        type=np.int32,
        description='''
        Switch to GW self-energy calculation: 0 = False, 1 = True.
        ''')

    x_w2dynamics_gw_kaverage = Quantity(
        type=np.int32,
        description='''
        Calculation of local GW contribution - K-average or model.
        ''')

    x_w2dynamics_half_bandwidth = Quantity(
        type=np.float64,
        description='''
        Half-bandwidth of the DOS.
        ''')

    x_w2dynamics_hkfile = Quantity(
        type=str,
        description='''
        Filename of the H_k file.
        ''')

    x_w2dynamics_magnetism = Quantity(
        type=str,
        description='''
        Magnetic state for DMFT calculation: 'para', 'ferro', 'antiferro'. Default = 'para'.
        ''')

    x_w2dynamics_mixing = Quantity(
        type=np.float64,
        description='''
        Mixing between old and new SE.
        ''')

    x_w2dynamics_mixing_diis_history = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_mixing_diis_period = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_mixing_strategy = Quantity(
        type=str,
        description='''
        Mixing strategy: 'linear', 'diis'. Default = 'linear'.
        ''')

    x_w2dynamics_mu = Quantity(
        type=np.float64,
        units='electron_volt',
        description='''
        Chemical potential.
        ''')

    x_w2dynamics_mu_mixing = Quantity(
        type=np.float64,
        description='''
        Mix in old chemical potential.
        ''')

    x_w2dynamics_mu_n_load_old = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_w2dynamics_mu_search = Quantity(
        type=str,
        description='''
        Mu search: 'nloc', 'kappa', 'mixer'. Default = 'nloc'.
        ''')

    x_w2dynamics_nat = Quantity(
        type=np.int32,
        description='''
        Number of atoms for the LDA+DMFT calculation.
        ''')

    x_w2dynamics_neps = Quantity(
        type=np.int32,
        description='''
        Numerical integration of DOS.
        ''')

    x_w2dynamics_read_mixer = Quantity(
        type=str,
        description='''
        ''')

    x_w2dynamics_readleads = Quantity(
        type=np.int32,
        description='''
        Read leads from leads-file.
        ''')

    x_w2dynamics_readold = Quantity(
        type=np.int32,
        description='''
        Start again from nth iteration.
        ''')

    x_w2dynamics_readold_mapsiw = Quantity(
        type=str,
        description='''
        ''')

    x_w2dynamics_readold_mu = Quantity(
        type=str,
        description='''
        Default: uses General.mu as mu if General.EPSN == 0; always: when reading old
        output, uses mu from last iteration as mu even if General.EPSN == 0.
        ''')

    x_w2dynamics_readold_preload_mixer = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_selfenergy = Quantity(
        type=str,
        description='''
        Options to calculate the DMFT self-energy: 'dyson', 'improved',
        'improved_worm', 'symmetric_improved_worm'. Default = 'dyson'.
        ''')

    x_w2dynamics_sgwnlfile = Quantity(
        type=str,
        description='''
        File that contains the NON-LOCAL GW self-energy.
        ''')

    x_w2dynamics_siw_moments = Quantity(
        type=str,
        description='''
        SIW moments: 'estimate', 'extract'. Default = 'estimate'.
        ''')

    x_w2dynamics_slurmonlycontinueiftime = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_slurmstopfile = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_w2dynamics_statisticsteps = Quantity(
        type=np.int32,
        description='''
        Number of static steps.
        ''')

    x_w2dynamics_totdens = Quantity(
        type=np.float64,
        description='''
        Number of valence electrons in the correlated subspace per atom.
        ''')

    x_w2dynamics_uw = Quantity(
        type=np.int32,
        description='''
        Include dynamical U(w).
        ''')

    x_w2dynamics_uw_mat = Quantity(
        type=np.int32,
        description='''
        Reading real or Matsubara frequencies from Uw files.
        ''')

    x_w2dynamics_wormsteps = Quantity(
        type=np.int32,
        description='''
        Number of worm steps.
        ''')

    x_w2dynamics_write = Quantity(
        type=str,
        description='''
        Write options: 'full', 'normal', 'minimal'. Default = 'normal'.
        ''')


class x_w2dynamics_config_qmc_parameters(MSection):
    '''
    Input quantities contained in .config:general.{name} of the hdf5 mainfile.
    '''

    m_def = Section(validate=False)

    x_w2dynamics_accumgtau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_eigenbasis = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_enableoutertruncation = Quantity(
        type=str,
        description='''
        ''')

    x_w2dynamics_epsevec = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_epslanc = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_epssandwich = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_epstracevec = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_flavourchange_moves = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_fourpnt = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_full_offdiag = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_g4ph = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_g4pp = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_gtau_mean_step = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_gtau_mid_step = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_maxhisto = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_meas_dm_old = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measdensitymatrix = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measexpresdensitymatrix = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measg2iw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measg4iwpp = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measgiw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measgsigmaiw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measgtaudetrat = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_meassusz = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_measurementtiming = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_n2iwb = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_n3iwb = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_n3iwf = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_n4iwb = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_n4iwf = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_n4leg = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_n4tau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nbatchsize_nfft_worm = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nbin = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_ncorr = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nfft_mode_g4iw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nftau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nice_selfenergy = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_niw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nlegmax = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nlegorder = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nlookup_nfft = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nmeas = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nseed = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_ntau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nwarmups = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_nwarmups2plus = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_offd_strength = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_offdiag = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_percentage4operatormove = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_percentageglobalmove = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_percentageoutermove = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_percentagetaushiftmove = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_percentageworminsert = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_percentagewormoutermove = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_percentagewormreplace = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_printdensitymatrixbasis = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_reusemcconfig = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_segment = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_sign_step = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_statesampling = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_taudiffmax = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_truncation = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_update_trace = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormcombinegiw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormeta = Quantity(
        type=np.float64,
        description='''
        ''')

    x_w2dynamics_wormmeasg4iw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasgiw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasgsigmaiw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasgtau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeash4iw = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasnqqdag = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasp2iwph = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasp2iwpp = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasp2tauph = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasp2taupp = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasp3iwph = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasp3iwpp = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasqq = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasqqdd = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasqqqq = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasqqtau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasquddag = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasucaca = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasucacatau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasuccaa = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormmeasuccaatau = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormphconvention = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormsearcheta = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormsearchetamaxiter = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_wormzmeasg = Quantity(
        type=np.int32,
        description='''
        ''')

    x_w2dynamics_writecovmeangiw = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_w2dynamics_writecovmeansigmaiw = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_w2dynamics_writemcconfig = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_w2dynamics_zphconvention = Quantity(
        type=np.int32,
        description='''
        ''')


class x_w2dynamics_config_parameters(MSection):
    '''
    Section grouping the different input configuration parameters.
    '''

    m_def = Section(validate=False)

    x_w2dynamics_config_atoms = SubSection(sub_section=x_w2dynamics_config_atoms_parameters.m_def, repeats=True)

    x_w2dynamics_config_general = SubSection(sub_section=x_w2dynamics_config_general_parameters.m_def, repeats=False)

    x_w2dynamics_config_qmc = SubSection(sub_section=x_w2dynamics_config_qmc_parameters.m_def, repeats=False)


class Method(simulation.method.Method):
    '''
    Section containing the various parameters that define the theory and the
    approximations (convergence, thresholds, etc.) behind the calculation.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_w2dynamics_config = SubSection(sub_section=x_w2dynamics_config_parameters.m_def, repeats=False)


class ScfIteration(simulation.calculation.ScfIteration):
    '''
    Every scf_iteration section represents a self-consistent field (SCF) iteration,
    and gives detailed information on the SCF procedure of the specified quantities.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_w2dynamics_dc_latt = Quantity(
        type=np.float64,
        shape=['x_w2dynamics_nd', 2, 'x_w2dynamics_nd', 2],
        description='''
        Double counting correction on the lattice.
        ''')

    x_w2dynamics_gdensnew = Quantity(
        type=np.complex128,
        shape=['x_w2dynamics_nd', 2, 'x_w2dynamics_nd', 2],
        description='''
        Densities with new self-energy after adjustment of mu.
        ''')

    x_w2dynamics_gdensold = Quantity(
        type=np.complex128,
        shape=['x_w2dynamics_nd', 2, 'x_w2dynamics_nd', 2],
        description='''
        Densities with old self-energy before adjustment of mu.
        ''')

    x_w2dynamics_glocnew_lattice = Quantity(
        type=np.complex128,
        shape=['x_w2dynamics_nd', 2, 'Niw'],
        description='''
        Local Green's function in Matsubara (old self-energy), diagonal part for all lda-bands.
        ''')

    x_w2dynamics_glocold_lattice = Quantity(
        type=np.complex128,
        shape=['x_w2dynamics_nd', 2, 'Niw'],
        description='''
        Local Green's function in Matsubara (old self-energy), diagonal part for all lda-bands.
        ''')

    x_w2dynamics_mu = Quantity(
        type=np.float64,
        shape=[],
        units='electron_volt',
        description='''
        Chemical potential (lattice model).
        ''')

    x_w2dynamics_ineq = SubSection(sub_section=x_w2dynamics_quantities.m_def, repeats=True)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_w2dynamics_axes = SubSection(sub_section=x_w2dynamics_axes.m_def, repeats=False)

    # TODO add config, environment variables
