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


class Method(simulation.run.Method):
    '''
    Contains the specifications of the method.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_soliddmft_dft_input = Quantity(
        type=JSON,
        description='''
        DFT input parameters.
        ''')

    x_soliddmft_dft_misc_input = Quantity(
        type=JSON,
        description='''
        Miscellaneous DFT input parameters.
        ''')

    x_soliddmft_dft_symmcorr_input = Quantity(
        type=JSON,
        description='''
        Symmetry of correlated orbitals DFT input parameters.
        ''')

    x_soliddmft_general_params = Quantity(
        type=JSON,
        description='''
        General DMFT input parameters.
        ''')

    x_soliddmft_solver_params = Quantity(
        type=JSON,
        description='''
        DMFT solver parameters.
        ''')

    x_soliddmft_advanced_params = Quantity(
        type=JSON,
        description='''
        Advanced DMFT input parameters.
        ''')


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
