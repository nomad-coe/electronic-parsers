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


class x_soliddmft_general_parameters(MSection):
    '''
    Section containing the general parameters of solid_dmft.
    '''

    m_def = Section(validate=False)

    x_soliddmft_J = Quantity(
        type=np.float64,
        description='''
        J values for impurities if only one value is given, the same J is assumed for all impurities.
        ''')

    x_soliddmft_U = Quantity(
        type=np.float64,
        description='''
        U values for impurities if only one value is given, the same U is assumed for all impurities.
        ''')

    x_soliddmft_afm_mapping = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_soliddmft_afm_order = Quantity(
        type=np.bool_,
        description='''
        Copy self energies instead of solving explicitly for afm order.
        ''')

    x_soliddmft_beta = Quantity(
        type=np.float64,
        description='''
        Inverse temperature for Greens function etc.
        ''')

    x_soliddmft_block_suppress_orbital_symm = Quantity(
        type=np.bool_,
        description='''
        Should blocks be checked if symmetry-equiv. between orbitals? Does not affect spin symmetries.
        ''')

    x_soliddmft_block_threshold = Quantity(
        type=np.float64,
        description='''
        Threshold for finding block structures in the input data (off-diag yes or no).
        ''')

    x_soliddmft_calc_energies = Quantity(
        type=np.bool_,
        description='''
        Calc energies explicitly within the dmft loop.
        ''')

    x_soliddmft_config_file = Quantity(
        type=str,
        description='''
        Config file name.
        ''')

    x_soliddmft_csc = Quantity(
        type=np.bool_,
        description='''
        Are we doing a CSC calculation?
        ''')

    x_soliddmft_cthyb_delta_interface = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_soliddmft_dc = Quantity(
        type=np.bool_,
        description='''
        dc correction on yes or no?
        ''')

    x_soliddmft_dc_dmft = Quantity(
        type=np.bool_,
        description='''
        Whether to use DMFT or DFT occupations:
            DC with DMFT occupation in each iteration -> True
            DC with DFT occupations after each DFT cycle -> False
        ''')

    x_soliddmft_dc_type = Quantity(
        type=np.int64,
        description='''
        Type of double counting correction considered: * 0: FLL * 1: held formula,
        needs to be used with slater-kanamori h_int_type=2 * 2: AMF * 3: FLL for eg orbitals
        only with U,J for Kanamori.
        ''')

    x_soliddmft_dft_mu = Quantity(
        type=str,
        description='''
        DFT mu file.
        ''')

    x_soliddmft_diag_delta = Quantity(
        type=np.bool_,
        description='''
        Option to remove off-diagonal terms in the hybridization function.
        ''')

    x_soliddmft_energy_shift_orbitals = Quantity(
        type=np.float64,
        description='''
        Orbitals will be shifted by this energy. The entries can be python code, to be
        combined with configparser's interpolation.
        ''')

    x_soliddmft_enforce_off_diag = Quantity(
        type=np.bool_,
        description='''
        Enforce off diagonal elements in block structure finder.
        ''')

    x_soliddmft_fixed_mu_value = Quantity(
        type=np.float64,
        description='''
        If given, the chemical potential remains fixed in calculations.
        ''')

    x_soliddmft_g0_conv_crit = Quantity(
        type=np.int64,
        description='''
        Stop the calculation if sum_w 1/(w^0.6) ||G0-G0_prev|| is smaller than threshold.
        ''')

    x_soliddmft_g0_mix = Quantity(
        type=np.float64,
        description='''
        Mixing the Weiss field G0 with previous iteration G0 for better convergency. 1.0 means no mixing.
        ''')

    x_soliddmft_g0_mix_type = Quantity(
        type=str,
        description='''
        Which type of mixing is used. Possible values are: linear, linear mixing broyden, broyden mixing.
        ''')

    x_soliddmft_gimp_conv_crit = Quantity(
        type=np.int64,
        description='''
        Stop the calculation if sum_w 1/(w^0.6) ||Gimp-Gloc|| is smaller than threshold.
        ''')

    x_soliddmft_h5_save_freq = Quantity(
        type=np.int64,
        description='''
        How often is the output saved to the h5 archive.
        ''')

    x_soliddmft_h_field = Quantity(
        type=np.float64,
        description='''
        Magnetic field.
        ''')

    x_soliddmft_h_field_it = Quantity(
        type=np.int64,
        description='''
        ''')

    x_soliddmft_h_int_basis = Quantity(
        type=str,
        description='''
        ''')

    x_soliddmft_h_int_type = Quantity(
        type=np.str_,
        description='''
        Interaction type:
            density_density: used for full d-shell or eg- or t2g-subset
            kanamori: only physical for the t2g or the eg subset
            full_slater: used for full d-shell or eg- or t2g-subset
            crpa: use the cRPA matrix as interaction Hamiltonian
            crpa_density_density: use the density-density terms of the cRPA matrix
            dynamic: use dynamic U from h5 archive. Needs to be stored as Matsubara Gf under dynamic_U/U_iw in the input h5
        ''')

    x_soliddmft_jobname = Quantity(
        type=str,
        description='''
        One or multiple jobnames specifying the output directories.
        ''')

    x_soliddmft_legendre_fit = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_soliddmft_load_sigma = Quantity(
        type=np.bool_,
        description='''
        Load a old sigma from h5 file.
        ''')

    x_soliddmft_magmom = Quantity(
        type=np.float64,
        description='''
        Initialize magnetic moments if magnetic is on. length must be #imps. This will be
        used as factor for each imp in the initial self energy, with up (or ud for
        spin-orbit coupling) (1+fac)*sigma, and with down (1-fac)*sigma.
        ''')

    x_soliddmft_magnetic = Quantity(
        type=np.bool_,
        description='''
        Are we doing a magnetic calculations? If yes put magnetic to True. Not implemented for CSC calculations
        ''')

    x_soliddmft_measure_chi_SzSz = Quantity(
        type=np.bool_,
        description='''
        Measure the dynamic spin suszeptibility chi(sz,sz(tau))
        triqs.github.io/cthyb/unstable/guide/dynamic_susceptibility_notebook.html.
        ''')

    x_soliddmft_measure_chi_insertions = Quantity(
        type=np.int64,
        description='''
        Number of insertation for measurement of chi.
        ''')

    x_soliddmft_mu_gap_gb2_threshold = Quantity(
        type=np.float64,
        description='''
        Threshold of the absolute of the lattice GF at tau=beta/2 for use of MaxEnt’s
        lattice spectral function to put the chemical potential into the middle of the gap.
        Does not work if system completely full or empty, mu mixing is not applied to it.
        Recommended value 0.01.
        ''')

    x_soliddmft_mu_initial_guess = Quantity(
        type=np.float64,
        description='''
        ''')

    x_soliddmft_mu_mix_const = Quantity(
        type=np.float64,
        description='''
        Constant term of the mixing of the chemical potential. See mu_mix_per_occupation_offset.
        ''')

    x_soliddmft_mu_mix_per_occupation_offset = Quantity(
        type=np.float64,
        description='''
        Mu mixing proportional to the occupation offset. Mixing between the dichotomy result
        and the previous mui,

        mu_next = factor * mu_dichotomy + (1-factor) * mu_previous, with factor = mu_mix_per_occupation_offset * abs(n - n_target) + mu_mix_const.

        The program ensures that 0 <= factor <= 1. mu_mix_const = 1.0 and
        mu_mix_per_occupation_offset = 0.0 means no mixing.
        ''')

    x_soliddmft_mu_update_freq = Quantity(
        type=np.int64,
        description='''
        The chemical potential will be updated every # iteration.
        ''')

    x_soliddmft_n_iter_dmft = Quantity(
        type=np.int64,
        description='''
        Number of iterations per dmft cycle after first cycle.
        ''')

    x_soliddmft_n_iw = Quantity(
        type=np.int64,
        description='''
        Number of Matsubara frequencies; default = 1025.
        ''')

    x_soliddmft_n_tau = Quantity(
        type=np.int64,
        description='''
        Number of imaginary time points; default = 10001.
        ''')

    x_soliddmft_noise_level_initial_sigma = Quantity(
        type=np.float64,
        description='''
        Spread of Gaussian noise applied to the initial Sigma.
        ''')

    x_soliddmft_occ_conv_crit = Quantity(
        type=np.int64,
        description='''
        Stop the calculation if a certain threshold for the imp occ change is reached.
        ''')

    x_soliddmft_oneshot_postproc_gamma_file = Quantity(
        type=np.bool_,
        description='''
        Write the GAMMA file for vasp after completed one-shot calculations.
        ''')

    x_soliddmft_prec_mu = Quantity(
        type=np.float64,
        description='''
        General precision for determining the chemical potential at any time calc_mu is called.
        ''')

    x_soliddmft_previous_file = Quantity(
        type=str,
        description='''
        ''')

    x_soliddmft_ratio_F4_F2 = Quantity(
        type=np.float64,
        description='''
        Ratio between the Slater integrals F_4 and F_2. Only used for the interaction
        Hamiltonians 'density_density' and 'full_slater' and only for d-shell impurities,
        where the default is 0.63.
        ''')

    x_soliddmft_seedname = Quantity(
        type=str,
        description='''
        Seedname for h5 archive or for multiple if calculations should be connected.
        ''')

    x_soliddmft_set_rot = Quantity(
        type=str,
        description='''
        Use density_mat_dft to diagonalize occupations = 'den' or use hloc_dft to diagonalize
        occupations = 'hloc'.
        ''')

    x_soliddmft_sigma_conv_crit = Quantity(
        type=np.int64,
        description='''
        Stop the calculation if sum_w 1/(w^0.6) ||Sigma-Sigma_prev|| is smaller than threshold.
        ''')

    x_soliddmft_sigma_mix = Quantity(
        type=np.float64,
        description='''
        Sigma mixing can break orbital symmetries, use G0 mixing mixing sigma with previous
        iteration sigma for better convergency. 1.0 means no mixing.
        ''')

    x_soliddmft_solver_type = Quantity(
        type=str,
        description='''
        type of solver chosen for the calculation, currently supports: 'cthyb', 'ctint',
        'ftps', 'hubbardI', 'ctseg'.
        ''')

    x_soliddmft_store_solver = Quantity(
        type=np.bool_,
        description='''
        ''')


class x_soliddmft_solver_parameters(MSection):
    '''
    Section containing the solver parameters of solid_dmft.
    '''

    m_def = Section(validate=False)

    x_soliddmft_fit_max_moment = Quantity(
        type=np.int64,
        description='''
        Max moment to be fitted.
        ''')

    x_soliddmft_fit_max_w = Quantity(
        type=np.float64,
        description='''
        Highest matsubara frequency to fit.
        ''')

    x_soliddmft_fit_min_w = Quantity(
        type=np.float64,
        description='''
        Start matsubara frequency to start with.
        ''')

    x_soliddmft_imag_threshold = Quantity(
        type=np.float64,
        description='''
        Threshold for imag part of G0_tau. be warned if symmetries are off in projection
        scheme imag parts can occur in G0_tau.
        ''')

    x_soliddmft_length_cycle = Quantity(
        type=np.int64,
        description='''
        Length of each cycle; number of sweeps before measurement is taken.
        ''')

    x_soliddmft_measure_G_l = Quantity(
        type=np.bool_,
        description='''
        Measure Legendre Greens function.
        ''')

    x_soliddmft_measure_density_matrix = Quantity(
        type=np.bool_,
        description='''
        Measures the impurity density matrix and sets also use_norm_as_weight to true.
        ''')

    x_soliddmft_measure_pert_order = Quantity(
        type=np.bool_,
        description='''
        Measure perturbation order histograms: triqs.github.io/cthyb/latest/guide/perturbation_order_notebook.html

        The result is stored in the h5 archive under 'DMFT_results' at every iteration in
        the subgroups 'pert_order_imp_X' and 'pert_order_total_imp_X'
        ''')

    x_soliddmft_move_double = Quantity(
        type=np.bool_,
        description='''
        Double moves in solver.
        ''')

    x_soliddmft_move_shift = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_soliddmft_n_cycles = Quantity(
        type=np.int64,
        description='''
        Total number of sweeps.
        ''')

    x_soliddmft_n_warmup_cycles = Quantity(
        type=np.int64,
        description='''
        Number of warmup cycles before real measurement sets in.
        ''')

    x_soliddmft_off_diag_threshold = Quantity(
        type=np.float64,
        description='''
        Threshold for off-diag elements in Hloc0.
        ''')

    x_soliddmft_perform_tail_fit = Quantity(
        type=np.bool_,
        description='''
        Tail fitting if legendre is off?
        ''')

    x_soliddmft_use_norm_as_weight = Quantity(
        type=np.bool_,
        description='''
        ''')


class x_soliddmft_advanced_parameters(MSection):
    '''
    Section containing the advanced parameters of solid_dmft.
    '''

    m_def = Section(validate=False)

    x_soliddmft_dc_J = Quantity(
        type=np.float64,
        description='''
        J values for DC determination if only one value is given, the same J is assumed for
        all impurities.
        ''')

    x_soliddmft_dc_U = Quantity(
        type=np.float64,
        description='''
        U values for DC determination if only one value is given, the same U is assumed for
        all impurities.
        ''')

    x_soliddmft_dc_factor = Quantity(
        type=np.float64,
        description='''
        If given, scales the dc energy by multiplying with this factor, usually < 1.
        ''')

    x_soliddmft_dc_fixed_occ = Quantity(
        type=np.float64,
        description='''
        If given, the occupation for the DC for each impurity is set to the provided value.
        Still uses the same kind of DC!
        ''')

    x_soliddmft_dc_fixed_value = Quantity(
        type=np.float64,
        description='''
        If given, it sets the DC (energy/imp) to this fixed value. Overwrites EVERY other
        DC configuration parameter if DC is turned on.
        ''')

    x_soliddmft_dc_nominal = Quantity(
        type=np.bool_,
        description='''
        ''')

    x_soliddmft_map_solver_struct = Quantity(
        type=str,
        description='''
        Additional manual mapping of the solver block structure, applied after the block
        structure finder for each impurity. Give exactly one dict per ineq impurity. see
        also triqs.github.io/dft_tools/latest/_python_api/triqs_dft_tools.block_structure.BlockStructure.map_gf_struct_solver.html
        ''')

    x_soliddmft_pick_solver_struct = Quantity(
        type=str,
        description='''
        ''')


class x_soliddmft_impurity_parameters(MSection):
    '''
    Section containing the impurity parameters.
    '''

    m_def = Section(validate=False)

    x_soliddmft_SO = Quantity(
        type=np.float64,
        description='''
        1 if spin-orbit interaction is included, 0 otherwise.
        ''')

    x_soliddmft_atom = Quantity(
        type=np.float64,
        description='''
        Atom index.
        ''')

    x_soliddmft_dim = Quantity(
        type=np.float64,
        description='''
        Number of orbitals in the atom.
        ''')

    x_soliddmft_irep = Quantity(
        type=np.float64,
        description='''
        Dummy integer 0.
        ''')

    x_soliddmft_l = Quantity(
        type=np.float64,
        description='''
        Angular quantum number.
        ''')

    x_soliddmft_sort = Quantity(
        type=np.float64,
        description='''
        Defines the equivalency of the atoms.
        ''')


class x_soliddmft_dft_input_parameters(MSection):
    '''
    Section containing the DFT input parameters of solid_dmft (as coming from DFFTools).
    '''

    m_def = Section(validate=False)

    x_soliddmft_SO = Quantity(
        type=np.int64,
        description='''
        1 if spin-orbit interaction is included, 0 otherwise.
        ''')

    x_soliddmft_SP = Quantity(
        type=np.int64,
        description='''
        1 for spin-polarised Hamiltonian, 0 for paramagnetic Hamiltonian.
        ''')

    x_soliddmft_T = Quantity(
        type=np.complex128,
        description='''
        Transformation matrix from the spherical harmonics to impurity problem basis
        normally the real cubic harmonics). This matrix can be used to calculate the
        4-index U matrix, not automatically done.
            dim n_inequiv_corr_shell x [max(corr_shell[‘dim’]),max(corr_shell[‘dim’])]
        ''')

    x_soliddmft_bz_weights = Quantity(
        type=np.float64,
        description='''
        Weights of the k-points for the k summation. Soon be replaced by kpt_weights.
            dim n_k
        ''')

    x_soliddmft_charge_below = Quantity(
        type=np.float64,
        description='''
        Number of electrons in the crystal below the correlated orbitals. Note that this
        is for compatibility with dmftproj, otherwise set to 0.
        ''')

    x_soliddmft_corr_to_inequiv = Quantity(
        type=np.int64,
        description='''
        Mapping from correlated shells to inequivalent correlated shells. A list of
        length n_corr_shells containing integers, where same numbers mark equivalent
        sites.
        ''')

    x_soliddmft_density_required = Quantity(
        type=np.float64,
        description='''
        Required total electron density. Needed to determine the chemical potential. The
        density in the projection window is then density_required-charge_below.
        ''')

    x_soliddmft_energy_unit = Quantity(
        type=np.float64,
        description='''
        Unit of energy used for the calculation.
        ''')

    x_soliddmft_hopping = Quantity(
        type=np.complex128,
        shape=['*', '*', '*', '*', '*'],
        description='''
        Non-interacting Hamiltonian matrix for each k point. As for proj_mat, all matrices
        have to be of the same size.
            dim [n_k,SP+1-SO,max(n_orbitals),max(n_orbitals)]
        ''')

    x_soliddmft_inequiv_to_corr = Quantity(
        type=np.int64,
        description='''
        A list of length n_inequiv_shells containing list indices as integers pointing
        to the corresponding sites in corr_to_inequiv.
        ''')

    x_soliddmft_k_dep_projection = Quantity(
        type=np.int64,
        description='''
        1 if the dimension of the projection operators depend on the k-point, 0 otherwise.
        ''')

    x_soliddmft_kpt_basis = Quantity(
        type=np.float64,
        description='''
        Basis for the k-point mesh, reciprocal lattice vectors.
            dim [3, 3]
        ''')

    x_soliddmft_kpt_weights = Quantity(
        type=np.float64,
        description='''
        Weights of the k-points for the k summation.
            dim [n_k]
        ''')

    x_soliddmft_kpts = Quantity(
        type=np.float64,
        description='''
        k-points given in reciprocal coordinates.
            dim [n_k, 3]
        ''')

    x_soliddmft_n_corr_shells = Quantity(
        type=np.int64,
        description='''
        Number of correlated atomic shells. If there are two correlated equivalent atoms
        in the unit cell, n_corr_shells is 2.
        ''')

    x_soliddmft_n_inequiv_shells = Quantity(
        type=np.int64,
        description='''
        Number of inequivalent atomic shells. Needs to be smaller than n_corr_shells. The
        up / downfolding routines mediate between all correlated shells and the actual
        inequivalent shells, by using the self-energy etc. for all equal shells belonging
        to the same class of inequivalent shells. The mapping is performed with information
        stored in corr_to_inequiv and inequiv_to_corr.
        ''')

    x_soliddmft_n_k = Quantity(
        type=np.int64,
        description='''
        Number of k-points used for the BZ integration.
        ''')

    x_soliddmft_n_orbitals = Quantity(
        type=np.int64,
        description='''
        Number of Bloch bands included in the projection window for each k-point. If
        SP+1-SO=2, the number of included bands may depend on the spin projection up/down.
            dim [n_k,SP+1-SO]
        ''')

    x_soliddmft_n_reps = Quantity(
        type=np.int64,
        description='''
        Number of irreducible representations of the correlated shell. e.g. 2 if eg/t2g
        splitting is used.
        ''')

    x_soliddmft_n_shells = Quantity(
        type=np.int64,
        description='''
        Number of atomic shells for which post-processing is possible. Note: this is not
        the number of correlated orbitals! If there are two equivalent atoms in the unit
        cell, n_shells is 2.
        ''')

    x_soliddmft_proj_mat = Quantity(
        type=np.complex128,
        shape=[],
        description='''
        Projection matrices from Bloch bands to Wannier orbitals. For efficient storage
        reasons, all matrices must be of the same size (given by last two indices). For
        k-points with fewer bands, only the first entries are used, the rest are zero. e.g.
        if number of Bloch bands ranges from 4-6, all matrices are of size 6.
            dim [n_k,SP+1-SO,n_corr_shells,max(corr_shell[‘dim’]),max(n_orbitals)]
        ''')

    x_soliddmft_proj_or_hk = Quantity(
        type=str,
        description='''
        Switch determining whether the Vasp converter is running in projection mode proj,
        or in Hamiltonian mode hk. In Hamiltonian mode, the hopping matrix is written in
        orbital basis, whereas in projection mode hopping is written in band basis.
        ''')

    x_soliddmft_rot_mat = Quantity(
        type=np.float64,
        description='''
        Rotation matrices for correlated shells, if use_rotations. These rotations are
        automatically applied for up / downfolding. Set to the unity matrix if no rotations
        are used.
            dim n_corr_shells x [corr_shells[‘dim’],corr_shells[‘dim’]]
        ''')

    x_soliddmft_rot_mat_time_inv = Quantity(
        type=np.int64,
        description='''
        If SP is 1, 1 if the coordinate transformation contains inversion, 0 otherwise.
        If use_rotations or SP is 0, give a list of zeros.
        ''')

    x_soliddmft_symm_op = Quantity(
        type=np.int64,
        description='''
        1 if symmetry operations are used for the BZ sums, 0 if all k-points are directly
        included in the input.
        ''')

    x_soliddmft_use_rotations = Quantity(
        type=np.int64,
        description='''
        1 if local and global coordinate systems are used, 0 otherwise.
        ''')

    x_soliddmft_band_window = Quantity(
        type=np.int64,
        description='''
        Band windows as KS band indices in Vasp for each spin channel, and k-point. Needed
        for writing out the GAMMA file.
            dim [n_k, 2]
        ''')

    x_soliddmft_dft_fermi_weights = Quantity(
        type=np.float64,
        description='''
        DFT fermi weights (occupations) of KS eigenstates for each k-point for calculation
        of density matrix correction.
            dim [n_k, SP+1-SO, max(n_orbitals)]
        ''')

    x_soliddmft_kpts_cart = Quantity(
        type=np.float64,
        description='''
        ''')

    x_soliddmft_shells = SubSection(sub_section=x_soliddmft_impurity_parameters.m_def, repeats=True)

    x_soliddmft_corr_shells = SubSection(sub_section=x_soliddmft_impurity_parameters.m_def, repeats=True)

    x_soliddmft_dim_reps = SubSection(sub_section=x_soliddmft_impurity_parameters.m_def, repeats=True)


class Method(simulation.run.Method):
    '''
    Contains the specifications of the method.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_soliddmft_dft_input = SubSection(sub_section=x_soliddmft_dft_input_parameters.m_def, repeats=False)

    x_soliddmft_general = SubSection(sub_section=x_soliddmft_general_parameters.m_def, repeats=False)

    x_soliddmft_solver = SubSection(sub_section=x_soliddmft_solver_parameters.m_def, repeats=False)

    x_soliddmft_advanced = SubSection(sub_section=x_soliddmft_advanced_parameters.m_def, repeats=False)


class Program(simulation.run.Program):
    '''
    Contains the specifications of the program.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_soliddmft_hash = Quantity(
        type=str,
        description='''
        Hash label for the solid_dmft repository branch used.
        ''')

    x_soliddmft_solver_hash = Quantity(
        type=str,
        description='''
        Hash label for the solver repository branch used.
        ''')

    x_soliddmft_triqs_hash = Quantity(
        type=str,
        description='''
        Hash label for the TRIQS repository branch used.
        ''')

    x_soliddmft_solver_version = Quantity(
        type=str,
        description='''
        Version tag of solver.
        ''')

    x_soliddmft_triqs_version = Quantity(
        type=str,
        description='''
        Version tag of TRIQS.
        ''')


class x_soliddmft_convergence_obs_parameters(MSection):
    '''
    Section containing the convergence of each observable of solid_dmft.
    '''

    m_def = Section(validate=False)

    x_soliddmft_d_Etot = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Total energy stepwise difference.
        ''')

    x_soliddmft_d_G0 = Quantity(
        type=np.float64,
        shape=[],
        description='''
        ''')

    x_soliddmft_d_Gimp = Quantity(
        type=np.float64,
        shape=[],
        description='''
        ''')

    x_soliddmft_d_Sigma = Quantity(
        type=np.float64,
        shape=[],
        description='''
        ''')

    x_soliddmft_d_imp_occ = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Impurity occupation stepwise difference
        ''')

    x_soliddmft_d_mu = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Chemical potential stepwise difference.
        ''')

    x_soliddmft_d_orb_occ = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Orbital occupation stepwise difference.
        ''')


class x_soliddmft_observables_parameters(MSection):
    '''
    Section containing the post-processed observables of solid_dmft.
    '''

    m_def = Section(validate=False)

    x_soliddmft_E_DC = Quantity(
        type=np.float64,
        shape=[],
        description='''
        EDC in the total energy expression. Double counting energy contribution.
        ''')

    x_soliddmft_E_bandcorr = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Sum of the E_DC and E_int_imp terms.
        ''')

    x_soliddmft_E_corr_en = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Ecorr in the total energy expression. DMFT correction to the kinetic energy.
        ''')

    x_soliddmft_E_dft = Quantity(
        type=np.float64,
        shape=[],
        description='''
        EDFT in the total energy expression. System energy as computed by the DFT code at
        every csc iteration.
        ''')

    x_soliddmft_E_int = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Eint in the total energy expression. Energy contribution from the electronic
        interactions within the single impurity.
        ''')

    x_soliddmft_E_tot = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Total energy computed as:
            Etot = Edft + Ecorr + Eint - EDC
        ''')

    x_soliddmft_mu = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Chemical potential fed to the solver at the present iteration (pre-dichotomy adjustement).
        ''')

    x_soliddmft_imp_gb2 = Quantity(
        type=np.float64,
        shape=['*'],
        description='''
        Site G(beta/2), proxy for total density of states at the Fermi level. Low values
        correlate with the presence of a gap.
        ''')

    x_soliddmft_imp_occ = Quantity(
        type=np.float64,
        shape=['*'],
        description='''
        Total mean site occupation.
        ''')

    x_soliddmft_orb_Z = Quantity(
        type=np.float64,
        shape=['*', '*'],
        description='''
        Orbital resolved quasiparticle weight (eff_mass / renormalized_mass). As obtained
        by linearizing the self-energy around w=0:
            Z = inv(1.0 - d [Re Sigma] / dw at w=0)
        ''')

    x_soliddmft_orb_gb2 = Quantity(
        type=np.float64,
        shape=['*', '*'],
        description='''
        Orbital resolved G(beta/2), proxy for projected density of states at the Fermi
        level. Low value of orb_gb2 correlated with the presence of a gap.
        ''')

    x_soliddmft_orb_occ = Quantity(
        type=np.float64,
        shape=['*', '*'],
        description='''
        Orbital mean site occupation.
        ''')


class x_soliddmft_iter_parameters(MSection):
    '''
    Section containing the post-processed observables of solid_dmft.
    '''

    m_def = Section(validate=False)

    x_soliddmft_DC_energ = Quantity(
        type=np.float64,
        shape=['*'],
        description='''
        Double counting correction. After parser dim = ['n_inequiv_shells']
        ''')

    x_soliddmft_DC_pot = Quantity(
        type=np.float64,
        shape=['*', '*', '*'],
        description='''
        Double counting potential. After parser dim = ['2 * n_inequiv_shells',
        'n_correlated_orbitals', 'n_correlated_orbitals'].
        ''')

    x_soliddmft_Delta_time = Quantity(
        type=np.float64,
        shape=['*', '*', '*'],
        description='''
        Imaginary time hybridization function.
            dim n_inequiv_shells x corr_shells.dim x n_tau x 2 (real+imag)
        ''')

    x_soliddmft_G0_freq = Quantity(
        type=np.float64,
        shape=['*', '*', '*'],
        description='''
        Imaginary frequency Weiss field.
            dim n_inequiv_shells x corr_shells.dim x 2*n_iw x 2 (real+imag)
        ''')

    x_soliddmft_Gimp_freq = Quantity(
        type=np.float64,
        shape=['*', '*', '*'],
        description='''
        Imaginary frequency impurity green function.
            dim n_inequiv_shells x corr_shells.dim x 2*n_iw x 2 (real+imag)
        ''')

    x_soliddmft_Gimp_time = Quantity(
        type=np.float64,
        shape=['*', '*', '*'],
        description='''
        Imaginary time representation of the impurity green function.
            dim n_inequiv_shells x corr_shells.dim x n_tau x 2 (real+imag)
        ''')

    x_soliddmft_Sigma_freq = Quantity(
        type=np.float64,
        shape=['*', '*', '*'],
        description='''
        Imaginary frequency self-energy obtained from the Dyson equation.
            dim n_inequiv_shells x corr_shells.dim x 2*n_iw x 2 (real+imag)
        ''')

    x_soliddmft_chemical_potential_pre = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Chemical potential before the solver iteration.
        ''')

    x_soliddmft_chemical_potential_post = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Chemical potential after the solver iteration.
        ''')

    x_soliddmft_dens_mat_pre = Quantity(
        type=np.float64,
        shape=['*', '*'],
        description='''
        Density matrix before the solver iteration. After parser dim = ['2 * n_inequiv_shells * n_correlated_orbitals',
        '2'], where the second index goes for real and imaginary
        ''')

    x_soliddmft_dens_mat_post = Quantity(
        type=np.float64,
        shape=['*', '*'],
        description='''
        Density matrix after the solver iteration.
        ''')


class ScfIteration(simulation.calculation.ScfIteration):
    '''
    Every scf_iteration section represents a self-consistent field (SCF) iteration,
    and gives detailed information on the SCF procedure of the specified quantities.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_soliddmft_iter = SubSection(sub_section=x_soliddmft_iter_parameters.m_def, repeats=False)

    x_soliddmft_convergence_obs = SubSection(sub_section=x_soliddmft_convergence_obs_parameters.m_def, repeats=False)

    x_soliddmft_observables = SubSection(sub_section=x_soliddmft_observables_parameters.m_def, repeats=False)
