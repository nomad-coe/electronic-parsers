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


class x_ocean_core_haydock_parameters(MSection):
    '''
    Input parameters for the Lanczos-Haydock algorithm.
    '''

    m_def = Section(validate=False)

    x_ocean_converge_spacing = Quantity(
        type=np.int32,
        description='''
        ''')

    x_ocean_converge_thresh = Quantity(
        type=np.float64,
        description='''
        ''')

    x_ocean_niter = Quantity(
        type=np.int32,
        description='''
        This sets the number of Haydock iterations. The default is 100.
        ''')


class x_ocean_core_gmres_parameters(MSection):
    '''
    Input parameters for the GMRES algorithm.
    '''

    m_def = Section(validate=False)

    x_ocean_echamp = Quantity(
        type=bool,
        description='''
        ''')

    x_ocean_elist = Quantity(
        type=np.float64,
        shape=['*'],
        description='''
        A list of energies (of arbitrary length) for the code to run the GMRES algorithm.
        ''')

    x_ocean_erange = Quantity(
        type=np.int32,
        shape=[3],
        description='''
        Run the GMRES algorithm on a set of evenly spaced energies specified by starting
        energy, ending energy, and step size (all in eV).
        ''')

    x_ocean_estyle = Quantity(
        type=str,
        description='''
        ''')

    x_ocean_ffff = Quantity(
        type=np.float64,
        description='''
        Sets the convergence criterion for the GMRES
        ''')

    x_ocean_gprc = Quantity(
        type=np.float64,
        description='''
        The version of the GMRES algorithm implemented in ocean uses the one-electron energies
        as a pre-conditioner with a Lorentzian broadening set by GPRC (in Ha.). By default this is
        0.5 Ha.
        ''')

    x_ocean_nloop = Quantity(
        type=np.int32,
        description='''
        The version of the GMRES algorithm implemented in ocean will grow to be a subspace of no
        larger than NLOOP before it is restarted. By default this is set to 80
        ''')


class x_ocean_bse_parameters(MSection):
    '''
    Input parameters for the BSE type of calculation: haydock or gmres
    '''

    m_def = Section(validate=False)

    x_ocean_screen_radius = Quantity(
        type=np.float64,
        description='''
        ''')

    x_ocean_core_haydock = SubSection(sub_section=x_ocean_core_haydock_parameters.m_def, repeats=False)

    x_ocean_core_gmres = SubSection(sub_section=x_ocean_core_gmres_parameters.m_def, repeats=False)

    x_ocean_xmesh = Quantity(
        type=np.int32,
        shape=[3],
        description='''
        When the wave-functions are converted into the NIST BSE format they are condensed onto a
        grid controlled by CNBSE.XMESH. The states are then projected onto a localized basis set,
        using the PAW formalism. By default ocean will attempt to guess a reasonable setting for
        this mesh.
        ''')


class x_ocean_screen_parameters(MSection):
    '''
    Input parameters for the screening
    '''

    m_def = Section(validate=False)

    x_ocean_all_augment = Quantity(
        type=bool,
        description='''
        ''')

    x_ocean_augment = Quantity(
        type=bool,
        description='''
        ''')

    x_ocean_convertstyle = Quantity(
        type=str,
        description='''
        ''')

    x_ocean_core_offset_average = Quantity(
        type=bool,
        description='''
        ''')

    x_ocean_core_offset_enable = Quantity(
        type=bool,
        description='''
        ''')

    x_ocean_core_offset_energy = Quantity(
        type=str,
        description='''
        ''')

    x_ocean_dft_energy_range = Quantity(
        type=np.float64,
        description='''
        ''')

    x_ocean_final_dr = Quantity(
        type=np.float64,
        description='''
        ''')

    x_ocean_final_rmax = Quantity(
        type=np.int32,
        description='''
        ''')

    x_ocean_grid_ang = Quantity(
        type=np.float64,
        shape=['*'],
        description='''
        ''')

    x_ocean_grid_deltar = Quantity(
        type=np.float64,
        shape=['*'],
        description='''
        ''')

    x_ocean_grid_lmax = Quantity(
        type=np.int32,
        description='''
        ''')

    x_ocean_grid_rmax = Quantity(
        type=np.int32,
        description='''
        ''')

    x_ocean_grid_rmode = Quantity(
        type=str,
        shape=['*'],
        description='''
        ''')

    x_ocean_grid_scheme = Quantity(
        type=str,
        description='''
        ''')

    x_ocean_grid_shells = Quantity(
        type=np.int32,
        shape=['*'],
        description='''
        ''')

    x_ocean_inversionstyle = Quantity(
        type=str,
        shape=['*'],
        description='''
        ''')

    x_ocean_kshift = Quantity(
        type=np.float64,
        shape=[3],
        description='''
        ''')

    x_ocean_mimic_exciting_bands = Quantity(
        type=bool,
        description='''
        ''')

    x_ocean_model_flavor = Quantity(
        type=str,
        description='''
        ''')

    x_ocean_shells = Quantity(
        type=np.float64,
        shape=['*'],
        description='''
        ''')


class Method(simulation.run.Method):
    '''
    Contains the specifications of the program.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_ocean_bse = SubSection(sub_section=x_ocean_bse_parameters.m_def, repeats=False)

    x_ocean_screen = SubSection(sub_section=x_ocean_screen_parameters.m_def, repeats=False)


class Program(simulation.run.Program):
    '''
    Contains the specifications of the program.
    '''

    m_def = Section(validate=False, extends_base_section=True)

    x_ocean_commit_hash = Quantity(
        type=str,
        description='''
        Commit hash label from the OCEAN git repository.
        ''')

    x_ocean_original_dft_code = Quantity(
        type=str,
        description='''
        DFT code (QuantumESPRESSO or ABINIT) used in the initial step.
        '''
    )
