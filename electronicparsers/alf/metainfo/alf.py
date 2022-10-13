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

from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference, JSON
)
from nomad.datamodel.metainfo import simulation


m_package = Package()


class x_alf_parameters_var_hubbard(MSection):
    '''
    Section containing the variables for the specific model.
    Acccess in data['parameters'].
    '''
    m_def = Section(validate=False)

    x_alf_continuous = Quantity(
        type=np.dtype(np.int32),
        description='''
        Uses (1: continuous; 0: discrete) HS transformation.
        ''')

    x_alf_ham_chem = Quantity(
        type=np.dtype(np.float64),
        description='''
        Chemical potential.
        ''')

    x_alf_ham_t = Quantity(
        type=np.dtype(np.float64),
        description='''
        Hopping parameter.
        ''')

    x_alf_ham_t2 = Quantity(
        type=np.dtype(np.float64),
        description='''
        For bilayer systems.
        ''')

    x_alf_ham_tperp = Quantity(
        type=np.dtype(np.float64),
        description='''
        For bilayer systems.
        ''')

    x_alf_ham_u = Quantity(
        type=np.dtype(np.float64),
        description='''
        Hubbard interaction.
        ''')

    x_alf_ham_u2 = Quantity(
        type=np.dtype(np.float64),
        description='''
        For bilayer systems.
        ''')

    x_alf_mz = Quantity(
        type=np.dtype(np.int32),
        description='''
        When true, sets the M_z-Hubbard model: Nf=2, demands that N_sun is even, HS field
        couples to the z-component of magnetization; otherwise, HS field couples to the
        density
        ''')


class x_alf_parameters_var_lattice(MSection):
    '''
    Section containing the variables defining the specific lattice and base model.
    Acccess in data['parameters'].
    '''
    m_def = Section(validate=False)

    x_alf_l1 = Quantity(
        type=np.dtype(np.int32),
        description='''
        Length in direction a1.
        ''')

    x_alf_l2 = Quantity(
        type=np.dtype(np.int32),
        description='''
        Length in direction a2.
        ''')

    x_alf_lattice_type = Quantity(
        type=str,
        description='''
        Type of lattice store in bytes: "Square", "Honeycomb", "Pi_Flux",
        "N_leg_ladder", "Bilayer_square", "Bilayer_honeycomb".
        ''')

    x_alf_model = Quantity(
        type=str,
        description='''
        Sets the interacting model: "Hubbard".
        ''')


class x_alf_parameters_var_model_generic(MSection):
    '''
    Section containing the common model parameters.
    Acccess in data['parameters'].
    '''
    m_def = Section(validate=False)

    x_alf_beta = Quantity(
        type=np.dtype(np.float64),
        description='''
        Inverse temperature.
        ''')

    x_alf_bulk = Quantity(
        type=np.dtype(np.int32),
        description='''
        Twist as a vector potential (1); at the boundary (0).
        ''')

    x_alf_checkerboard = Quantity(
        type=np.dtype(np.int32),
        description='''
        Whether checkerboard decomposition is used (1) or not (0).
        ''')

    x_alf_dtau = Quantity(
        type=np.dtype(np.float64),
        description='''
        Imaginary time step, Ltrot = beta/dtau.
        ''')

    x_alf_n_fl = Quantity(
        type=np.dtype(np.int32),
        description='''
        Number of flavours.
        ''')

    x_alf_n_phi = Quantity(
        type=np.dtype(np.int32),
        description='''
        Total number of flux quanta transversing the lattice.
        ''')

    x_alf_n_sun = Quantity(
        type=np.dtype(np.int32),
        description='''
        Number of colors.
        ''')

    x_alf_phi_x = Quantity(
        type=np.dtype(np.float64),
        description='''
        Twist along the L_1 direction, in units of the flux quanta.
        ''')

    x_alf_phi_y = Quantity(
        type=np.dtype(np.float64),
        description='''
        Twist along the L_2 direction, in units of the flux quanta.
        ''')

    x_alf_projector = Quantity(
        type=np.dtype(np.int32),
        description='''
        Whether the projector algorithm is used (1) or not (0).
        ''')

    x_alf_symm = Quantity(
        type=np.dtype(np.int32),
        description='''
        Whether symmetrization takes place (1) or not (0).
        ''')

    x_alf_theta = Quantity(
        type=np.dtype(np.float64),
        description='''
        Projection parameter.
        ''')


class x_alf_observable_scal_data(MSection):
    '''
    Section containing X_scal datasets.
    '''
    m_def = Section(validate=False)

    x_alf_obser = Quantity(
        type=np.dtype(np.float64),
        shape=['NBins', 'Nobs', 2],
        description='''
        Dataset of shape (Nbins, Nobs, 2).
        ''')

    x_alf_sign = Quantity(
        type=np.dtype(np.float64),
        shape=['Nbins'],
        description='''
        Dataset of shape (Nbins).
        ''')


class x_alf_observable_eqtau_data(MSection):
    '''
    Section containing Y_eq and Y_tau datasets.
    '''
    m_def = Section(validate=False)

    x_alf_obser = Quantity(
        type=np.dtype(np.float64),
        shape=['NBins', 'Norbs', 'Norbs', 'Ntau', 'Nlatt', 2],
        description='''
        Dataset of shape (Nbins, Norbs, Norbs, Ntau, Nlatt, 2).
        ''')

    x_alf_back = Quantity(
        type=np.dtype(np.float64),
        shape=['NBins', 'Nobs', 2],
        description='''
        Dataset of shape (Nbins, Nobs, 2).
        ''')

    x_alf_sign = Quantity(
        type=np.dtype(np.float64),
        shape=['Nbins'],
        description='''
        Dataset of shape (Nbins).
        ''')


class Program(simulation.run.Program):
    '''
    Contains the specifications of the program.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_alf_commit_hash = Quantity(
        type=str,
        description='''
        Commit hash label from the ALF git repository.
        ''')

    x_alf_commit_branch = Quantity(
        type=str,
        description='''
        Commit branch label from the ALF git repository.
        ''')


class System(simulation.run.System):
    '''
    Contains parameters describing a system of atomic configuration. These inclue the
    compound name, atomic positions, lattice vectors, contraints on the atoms, etc.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_alf_l1 = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        Superlattice vector L1.
        ''')

    x_alf_l2 = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        Superlattice vector L2.
        ''')

    x_alf_n_coord = Quantity(
        type=np.dtype(np.int32),
        description='''
        Coordination number.
        ''')

    x_alf_n_dim = Quantity(
        type=np.dtype(np.int32),
        description='''
        Number of orbitals per site.
        ''')

    x_alf_n_orb = Quantity(
        type=np.dtype(np.int32),
        description='''
        Number of orbitals.
        ''')

    x_alf_orbital = Quantity(
        type=np.dtype(np.float64),
        shape=[2, 'x_alf_n_orb'],
        description='''
        Real space center of each orbital.
        ''')

    x_alf_a1 = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        Lattice vector a1.
        ''')

    x_alf_a2 = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        Lattice vector a2.
        ''')

    x_alf_var_lattice = SubSection(sub_section=x_alf_parameters_var_lattice)


class Method(simulation.method.Method):
    '''
    Section containing the various parameters that define the theory and the
    approximations (convergence, thresholds, etc.) behind the calculation.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_alf_var_hubbard = SubSection(sub_section=x_alf_parameters_var_hubbard)

    x_alf_var_model_generic = SubSection(sub_section=x_alf_parameters_var_model_generic)

    x_alf_precision_green = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        Mean and Max Green functions precision.
        ''')

    x_alf_precision_phase = Quantity(
        type=np.dtype(np.float64),
        description='''
        Max phase precision.
        ''')

    x_alf_precision_tau = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        Mean and Max tau precision.
        ''')


class Calculation(simulation.calculation.Calculation):
    '''
    Section containing the operators.

    | X_scal      | Results of equal-time measurements of scalar observables. The          |
    |             | placeholder X stands for the observables Kin, Pot, Part, and Ener.     |
    | Y_eq, Y_tau | Results of equal-time and time-displaced measurements of correlation   |
    |             | functions. The placeholder Y stands for Green, SpinZ, SpinXY, Den, etc |
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_alf_den_eq = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_den_tau = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_ener_scal = SubSection(sub_section=x_alf_observable_scal_data)

    x_alf_green_eq = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_green_tau = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_kin_scal = SubSection(sub_section=x_alf_observable_scal_data)

    x_alf_part_scal = SubSection(sub_section=x_alf_observable_scal_data)

    x_alf_pot_scal = SubSection(sub_section=x_alf_observable_scal_data)

    x_alf_spint_eq = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_spint_tau = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_spinxy_eq = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_spinxy_tau = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_spinz_eq = SubSection(sub_section=x_alf_observable_eqtau_data)

    x_alf_spinz_tau = SubSection(sub_section=x_alf_observable_eqtau_data)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)