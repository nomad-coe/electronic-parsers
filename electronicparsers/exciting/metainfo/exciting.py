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


class x_exciting_section_geometry_optimization(MSection):
    '''
    section for geometry optimization
    '''

    m_def = Section(validate=False)


class x_exciting_section_atoms_group(MSection):
    '''
    a group of atoms of the same type
    '''

    m_def = Section(validate=False)

    x_exciting_geometry_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        labels of atom
        ''')

    x_exciting_geometry_atom_number = Quantity(
        type=str,
        shape=[],
        description='''
        number to identify the atoms of a species
        ''')

    x_exciting_atom_number = Quantity(
        type=str,
        shape=[],
        description='''
        number to identify the atoms of a species in the geometry optimization
        ''')

    x_exciting_atom_label = Quantity(
        type=str,
        shape=[],
        description='''
        labels of atoms in geometry optimization
        ''')

    x_exciting_MT_external_magnetic_field_atom_number = Quantity(
        type=str,
        shape=[],
        description='''
        number to identify the atoms of a species on which a magnetic field is applied
        ''')

    x_exciting_geometry_atom_positions = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        atomic positions
        ''')

    x_exciting_geometry_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x component of atomic position
        ''')

    x_exciting_geometry_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        y component of atomic position
        ''')

    x_exciting_geometry_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        z component of atomic position
        ''')

    x_exciting_MT_external_magnetic_field_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x component of the magnetic field
        ''')

    x_exciting_MT_external_magnetic_field_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        y component of the magnetic field
        ''')

    x_exciting_MT_external_magnetic_field_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        z component of the magnetic field
        ''')

    x_exciting_muffin_tin_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        muffin-tin points
        ''')

    x_exciting_muffin_tin_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        muffin-tin radius
        ''')

    x_exciting_atom_position_format = Quantity(
        type=str,
        shape=[],
        description='''
        whether the atomic positions are given in cartesian or vector coordinates
        ''')

    x_exciting_magnetic_field_format = Quantity(
        type=str,
        shape=[],
        description='''
        whether the magnetic field is given in cartesian or vector coordinates
        ''')


class x_exciting_section_bandstructure(MSection):
    '''
    bandstructure values
    '''

    m_def = Section(validate=False)

    x_exciting_band_number_of_vertices = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of vertices along the kpoint path used for the bandstructure plot
        ''')

    x_exciting_band_number_of_kpoints = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of points along the kpoint path used for the bandstructure plot
        ''')

    x_exciting_band_vertex_labels = Quantity(
        type=str,
        shape=['x_exciting_band_number_of_vertices'],
        description='''
        labels of the vertices along the kpoint path used for the bandstructure plot
        ''')

    x_exciting_band_vertex_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_band_number_of_vertices', 3],
        description='''
        coordinates of the vertices along the kpoint path used for the bandstructure plot
        ''')

    x_exciting_band_structure_kind = Quantity(
        type=str,
        shape=[],
        description='''
        String to specify the kind of band structure (either electronic or vibrational).
        ''')

    x_exciting_band_number_of_eigenvalues = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of eigenvalues per k-point
        ''')

    x_exciting_band_k_points = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_band_number_of_kpoints'],
        description='''
        Fractional coordinates of the k points (in the basis of the reciprocal-lattice
        vectors) for which the electronic energy are given.
        ''')

    x_exciting_band_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_spin_channels', 'x_exciting_band_number_of_kpoints', 'x_exciting_band_number_of_eigenvalues'],
        unit='joule',
        description='''
        $k$-dependent energies of the electronic band structure.
        ''')

    x_exciting_band_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Bandstructure energy values
        ''')


class x_exciting_section_dos(MSection):
    '''
    dos values
    '''

    m_def = Section(validate=False)

    x_exciting_dos_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        energy value for a dos point
        ''')

    x_exciting_dos_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / joule',
        description='''
        Density of states values
        ''')


class x_exciting_section_fermi_surface(MSection):
    '''
    Fermi surface values
    '''

    m_def = Section(validate=False)

    x_exciting_fermi_energy_fermi_surface = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Fermi energy for Fermi surface
        ''')

    x_exciting_grid_fermi_surface = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        number of points in the mesh to calculate the Fermi surface
        ''')

    x_exciting_number_of_bands_fermi_surface = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of bands for fermi surface
        ''')

    x_exciting_number_of_mesh_points_fermi_surface = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of mesh points for fermi surface
        ''')

    x_exciting_origin_fermi_surface = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Origin (in lattice coordinate) of the region where the Fermi surface is calculated
        ''')

    x_exciting_values_fermi_surface = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_number_of_bands_fermi_surface', 'x_exciting_number_of_mesh_points_fermi_surface'],
        unit='joule',
        description='''
        Fermi surface values
        ''')

    x_exciting_vectors_fermi_surface = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        Vectors (in lattice coordinate) defining the region where the Fermi surface is
        calculated
        ''')


class x_exciting_section_lattice_vectors(MSection):
    '''
    lattice vectors
    '''

    m_def = Section(validate=False)

    x_exciting_geometry_lattice_vector_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of lattice vector
        ''')

    x_exciting_geometry_lattice_vector_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of lattice vector
        ''')

    x_exciting_geometry_lattice_vector_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of lattice vector
        ''')


class x_exciting_section_reciprocal_lattice_vectors(MSection):
    '''
    reciprocal lattice vectors
    '''

    m_def = Section(validate=False)

    x_exciting_geometry_reciprocal_lattice_vector_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        x component of reciprocal lattice vector
        ''')

    x_exciting_geometry_reciprocal_lattice_vector_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        y component of reciprocal lattice vector
        ''')

    x_exciting_geometry_reciprocal_lattice_vector_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        z component of reciprocal lattice vector
        ''')


class x_exciting_section_spin(MSection):
    '''
    section for exciting spin treatment
    '''

    m_def = Section(validate=False)

    x_exciting_spin_treatment = Quantity(
        type=str,
        shape=[],
        description='''
        Spin treatment
        ''')


class x_exciting_section_xc(MSection):
    '''
    index for exciting functional
    '''

    m_def = Section(validate=False)

    x_exciting_xc_functional = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        index for exciting functional
        ''')


class x_exciting_freqgrid_parameters(MSection):
    '''
    Frequency grid setup used for computing W(q,omega) and Sigma(k,omega).
    '''

    m_def = Section(validate=False)

    x_exciting_eta = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Numerical (complex) smearing parameter used for the real frequency convolution
        and qdepw=sum.
        ''')

    x_exciting_fconv = Quantity(
        type=str,
        shape=[],
        description='''
        Frequency convolution type:
            nofreq - skip frequency dependency (testing option).
            refreq - real frequency formalism (only for response functions).
            imfreq - imaginary frequency formalism.
        ''')

    x_exciting_fgrid = Quantity(
        type=str,
        shape=[],
        description='''
        Grid types (listed only the recommended ones, for more grids see the source
        subroutine mod_frequency.f90):
            eqdist - Equidistant grid from freqmin to freqmax.
            gaulag - Grid for the Gauss-Laguerre quadrature rule from 0 to ∞.
            gauleg - Grid for the Gauss-Lagendre quadrature rule from 0 to ∞.
            gauleg2 - Grid for the double Gauss-Lagendre quadrature rule from 0 to freqmax
                      and freqmax to ∞.
            clencurt2 - Grid for the Clenshaw-Curtis quadrature rule from 0 to ∞. freqmax
                        can be used to rescale the frequencies.
        ''')

    x_exciting_freqmax = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Upper limit for the grid interval.
        ''')

    x_exciting_freqmin = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Lower limit for the grid interval.
        ''')

    x_exciting_nomeg = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Number of grid points.
        ''')


class x_exciting_selfenergy_parameters(MSection):
    '''
    Correlation self-energy setup.
    '''

    m_def = Section(validate=False)

    x_exciting_actype = Quantity(
        type=str,
        shape=[],
        description='''
        Analytical continuation scheme:
            pade - Pade's approximant (by H. J. Vidberg and J. W. Serence, J. Low Temp.
                   Phys. 29, 179 (1977)).
            aaa - Y. Nakatsukasa, O. Sete, L. N. Trefethen, "The AAA algorithm for rational
                  approximation", SIAM J. Sci. Comp. 40 (2018), A1494-A1522.
        ''')

    x_exciting_eqpsolver = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Schemes to solve the quasiparticle (non-linear) equation:
            0 - Perturbative solution.
            1 - Z=1 calculations.
            2 - Iterative solution.
        ''')

    x_exciting_eshift = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Alignment of the chemical potential:
            0 - No alignment.
            1 - Self-consistency at the Fermi level (iteratively).
            2 - Self-consistency at the Fermi level (perturbatively).
        ''')

    x_exciting_method = Quantity(
        type=str,
        shape=[],
        description='''
        Technique to compute the frequency convolution integral:
            ac - Analytical continuation
            cd - Contour deformation
        ''')

    x_exciting_nempty = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Number of empty states to calculate the correlation self energy (different from default).
        ''')

    x_exciting_singularity = Quantity(
        type=str,
        shape=[],
        description='''
        Treatment of the q→0 singularity:
            none': No special treatment (test purpose only).
            mpb': Auxiliary function method by S. Massidda, M. Posternak, and A.
                  Baldereschi, PRB 48, 5058 (1993)
            crg': Auxiliary function method by P. Carrier, S. Rohra, and A. Goerling,
                  PRB 75, 205126 (2007).
        ''')

    x_exciting_swidth = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Smearing parameter for visualizing the spectral function.
        ''')

    x_exciting_tol = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Tolerance factor used for generating support points in AAA-interpolation.
        ''')


class x_exciting_wgrid_parameters(MSection):
    '''
    The real frequency grid (output) setup for computing and visualizing the correlation
    self-energy and the spectral function. For more detailed description see freqgrid.
    '''

    m_def = Section(validate=False)

    x_exciting_size = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Number of grid points.
        ''')

    x_exciting_type = Quantity(
        type=str,
        shape=[],
        description='''
        Grid type.
        ''')

    x_exciting_wmax = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Upper limit for the grid interval.
        ''')

    x_exciting_wmin = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Lower limit for the grid interval.
        ''')


class x_exciting_mixbasis_parameters(MSection):
    '''
    Mixed-product basis setup.
    '''

    m_def = Section(validate=False)

    x_exciting_epsmb = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Linear dependence tolerance factor: controls construction of the radial part of
        the mixed-product basis.
        ''')

    x_exciting_gmb = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Plane-wave energy cutoff (in units of GLAPWmax): controls construction of the
        plane-wave part of the mixed-product basis.
        ''')

    x_exciting_lmaxmb = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Maximal angular momentum: controls construction of the radial part of the
        mixed-product basis.
        ''')


class x_exciting_barecoul_parameters(MSection):
    '''
    The bare Coulomb potential setup.
    '''

    m_def = Section(validate=False)

    x_exciting_barcevtol = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Matrix elements of the polarizability, the screened Coulomb potential, and the
        self-energy are computed in the basis that diagonalize the bare Coulomb potential.
        This tolerance factor is used to reduce the size of the Vc-diagonal product basis
        when computing the screened Coulomb potential and the correlation self-energy.
        ''')

    x_exciting_basis = Quantity(
        type=str,
        shape=[],
        description='''
        Two approaches to compute the bare Coulomb potential:
            mb - The Coulomb potential is computed in the mixed-product basis.
            pw - The Coulomb potential is computed in the plane-wave basis and then
                 converted into the mixed-product basis. This option is used only when
                 the potential truncation technique cutofftype is employed. From practical
                 point, usage of this approach requires to set a higher value of pwm
                 (typically = 4.0)
        ''')

    x_exciting_cutofftype = Quantity(
        type=str,
        shape=[],
        description='''
        Trigger the usage of the Coulomb potential truncation technique (S. Ismail-Beigi,
        "Truncation of Periodic Image Interactions for Confined Systems. Phys. Rev. B 73,
        233103 (2006)).
            none - 3D periodic crystal.
            0d - Isolated atom or molecule.
            1d - 1D chain (periodicity along z-axis)
            2d - 2D surface (vacuum separation along z-direction)
        ''')

    x_exciting_pwm = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Plane-wave energy cutoff (in units of gmaxvr*gmb) for computing the plane-wave
        part of the Coulomb potential.
        ''')

    x_exciting_stctol = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Tolerance factor for computing the structure factor in Ewald summation scheme.
        ''')


class x_exciting_scrcoul_parameters(MSection):
    '''
    Dynamically screened Coulomb potential setup.
    '''

    m_def = Section(validate=False)

    x_exciting_omegap = Quantity(
        type=np.float64,
        shape=[],
        description='''
        Plasmon-pole frequency (fitting parameter).
        ''')

    x_exciting_scrtype = Quantity(
        type=str,
        shape=[],
        description='''
        Approximation:
            rpa - Full-frequency Random-Phase Approximation.
            ppm - Godby-Needs plasmon-pole model.
        ''')


class GW(simulation.method.GW):

    m_def = Section(validate=False, extends_base_section=True)

    x_exciting_coreflag = Quantity(
        type=str,
        shape=[],
        description='''
        Option for treating core states in GW:
            all - All-electron treatment.
            xal - Both core and valence states are used to compute the exchange self-energy
                  and only valence electrons for computing the correlation self-energy.
            val - Valence-electron treatment.
            vab - Valence-electron treatment where core states are also excluded from the
                  construction of the mixed-product basis.
        ''')

    x_exciting_ibgw = Quantity(
        type=np.int32,
        shape=[],
        description='''
        QP corrections are computed for states in the interval [ibgw, nbgw].
        ''')

    x_exciting_nbgw = Quantity(
        type=np.int32,
        shape=[],
        description='''
        QP corrections are computed for states in the interval [ibgw, nbgw].
        ''')

    x_exciting_mblksiz = Quantity(
        type=np.int32,
        shape=[],
        description='''
        To reduce the memory usage, in summations over unoccupied states, big matrices are
        considered to be in a block form with a size of mblksiz.
        ''')

    x_exciting_nempty = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Number of empty states to compute both the screened Coulomb potential and the self-energy.
        ''')

    x_exciting_ngridq = Quantity(
        type=np.int32,
        shape=[3],
        description='''
        Size of the k/q-point grids.
        ''')

    x_exciting_printSelfC = Quantity(
        type=bool,
        shape=[],
        description='''
        Output the correlation self-energy.
        ''')

    x_exciting_printSpectralFunction = Quantity(
        type=bool,
        shape=[],
        description='''
        Compute and output the spectral function.
        ''')

    x_exciting_nempty = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Method to compute k/q and frequency dependent weights in the expression for
        polarizability:
            tet - Using the tetrahedron method as implemented in LibBZInt library
            sum - Direct summation employing a smearing parameter eta of freqgrid
        ''')

    x_exciting_rpmat = Quantity(
        type=bool,
        shape=[],
        description='''
        Skip calculation of the momentum matrix elements, instead read them from files
        PMATVV.OUT and PMATCV.OUT (restart option).
        ''')

    x_exciting_skipgnd = Quantity(
        type=bool,
        shape=[],
        description='''
        Skip the recalculation of KS eigenvalues and eigenvectors for the specified
        k/q-point grids (restart option).
        ''')

    x_exciting_taskname = Quantity(
        type=str,
        shape=[],
        description='''
        Tasks launcher:
            g0w0 - G0W0 calculations
            g0w0-x - Exchange only G0W0 calculations
            cohsex - Coulomb-hole and screened-exchange (COHSEX) approximation
            band - QP banstructure as obtained by Fourier interpolation
            dos - QP density of states
            emac - Calculate the macroscopic dielectric function
            vxc - Calculate the diagonal matrix elements of the exchange-correlation potential
            pmat - Calculate matrix elements of the momentum operator
            acon - Perform analytic continuation of the correlation self-energy from
                   imaginary to real frequency and calculate QP energies
        ''')

    x_exciting_vqloff = Quantity(
        type=np.float64,
        shape=[3],
        description='''
        The k/q-point offset vector in lattice coordinates.
        ''')

    x_exciting_freqgrid = SubSection(
        sub_section=x_exciting_freqgrid_parameters.m_def, repeats=False)

    x_exciting_selfenergy = SubSection(
        sub_section=x_exciting_selfenergy_parameters.m_def, repeats=False)

    x_exciting_wgrid = SubSection(
        sub_section=x_exciting_wgrid_parameters.m_def, repeats=False)

    x_exciting_mixbasis = SubSection(
        sub_section=x_exciting_mixbasis_parameters.m_def, repeats=False)

    x_exciting_barecoul = SubSection(
        sub_section=x_exciting_barecoul_parameters.m_def, repeats=False)

    x_exciting_scrcoul = SubSection(
        sub_section=x_exciting_scrcoul_parameters.m_def, repeats=False)

    x_exciting_bare_coulomb_gmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        Maximum G for the pw basis for the Coulomb potential.
        ''')

    x_exciting_mixed_basis_gmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        Cut-off parameter for the truncation of the expansion of the plane waves in the
        interstitial region.
        ''')


class x_exciting_exciton_calculation(MSection):
    '''
    Calculation of EXCITON
    '''

    m_def = Section(validate=False)

    x_exciting_xs_bse_number_of_excitons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of excitons
        ''')

    x_exciting_xs_bse_exciton_amplitude_im = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_excitons'],
        description='''
        Imaginary part of the transition amplitude
        ''')

    x_exciting_xs_bse_exciton_amplitude_re = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_excitons'],
        description='''
        Real part of the transition amplitude
        ''')

    x_exciting_xs_bse_exciton_binding_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_excitons'],
        unit='joule',
        description='''
        Exciton binding energies
        ''')

    x_exciting_xs_bse_exciton_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_excitons'],
        unit='joule',
        description='''
        Exciton energies
        ''')

    x_exciting_xs_bse_exciton_oscillator_strength = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_excitons'],
        description='''
        Exciton oscillator strength
        ''')


class x_exciting_epsilon_calculation(MSection):
    '''
    Calculation of EPSILON
    '''

    m_def = Section(validate=False)

    x_exciting_xs_bse_epsilon_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        unit='joule',
        description='''
        Energies of the dielectric function epsilon
        ''')

    x_exciting_xs_bse_epsilon_im = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        description='''
        Imaginary part of the dielectric function epsilon
        ''')

    x_exciting_xs_bse_epsilon_re = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        description='''
        Real part of the dielectric function epsilon
        ''')


class x_exciting_sigma_calculation(MSection):
    '''
    Calculation of SIGMA
    '''

    m_def = Section(validate=False)

    x_exciting_xs_bse_sigma_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        unit='joule',
        description='''
        Energies of the conductivity function sigma
        ''')

    x_exciting_xs_bse_sigma_im = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        description='''
        Imaginary part of the conductivity function sigma
        ''')

    x_exciting_xs_bse_sigma_re = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        description='''
        Real part of the conductivity function sigma
        ''')


class x_exciting_loss_calculation(MSection):
    '''
    Calculation of LOSS
    '''

    m_def = Section(validate=False)

    x_exciting_xs_bse_loss = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        description='''
        Loss function
        ''')

    x_exciting_xs_bse_loss_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_bse_number_of_components', 'x_exciting_xs_bse_number_of_energy_points'],
        unit='joule',
        description='''
        Energies of the loss function
        ''')


class Calculation(simulation.calculation.Calculation):

    m_def = Section(validate=False, extends_base_section=True)

    x_exciting_atom_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_number_of_atoms', 3],
        unit='newton',
        description='''
        Forces acting on the atoms.
        ''')

    x_exciting_atom_IBS_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_number_of_atoms', 3],
        unit='newton',
        description='''
        IBS correction to the Force acting on the atoms.
        ''')

    x_exciting_geometry_optimization_method = Quantity(
        type=str,
        shape=[],
        description='''
        Geometry optimization method
        ''')

    x_exciting_geometry_optimization_step = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Geometry optimization step
        ''')

    x_exciting_atom_core_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_number_of_atoms', 3],
        unit='newton',
        description='''
        core correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_HF_forces = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_number_of_atoms', 3],
        unit='newton',
        description='''
        HF correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_IBS_forces_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x-component of the IBS correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_IBS_forces_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        y-component of the IBS correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_IBS_forces_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        z-component of the IBS correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_core_forces_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x-component of the core correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_core_forces_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        y-component of the core correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_core_forces_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        z-component of the core correction to the Force acting on the atoms.
        ''')

    x_exciting_atom_HF_forces_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x-component of the HF Force acting on the atoms.
        ''')

    x_exciting_atom_HF_forces_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        y-component of the HF Force acting on the atoms.
        ''')

    x_exciting_atom_HF_forces_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        z-component of the HF Force acting on the atoms.
        ''')

    x_exciting_atom_forces_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        x-component of the Force acting on the atoms.
        ''')

    x_exciting_atom_forces_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        y-component of the Force acting on the atoms.
        ''')

    x_exciting_atom_forces_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        z-component of the Force acting on the atoms.
        ''')

    x_exciting_core_electron_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Core-electron kinetic energy final
        ''')

    x_exciting_core_leakage = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Core leakage
        ''')

    x_exciting_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Correlation energy final
        ''')

    x_exciting_coulomb_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb energy final
        ''')

    x_exciting_coulomb_potential_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb potential energy final
        ''')

    x_exciting_dos_fermi = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / joule',
        description='''
        DOS at Fermi energy
        ''')

    x_exciting_effective_potential_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Effective potential energy final
        ''')

    x_exciting_electron_nuclear_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Electron-nuclear energy final
        ''')

    x_exciting_exchange_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Exchange energy final
        ''')

    x_exciting_fermi_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Fermi energy final
        ''')

    x_exciting_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Estimated fundamental gap
        ''')

    x_exciting_geometry_atom_forces_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        x component of the force acting on the atom
        ''')

    x_exciting_geometry_atom_forces_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        y component of the force acting on the atom
        ''')

    x_exciting_geometry_atom_forces_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        z component of the force acting on the atom
        ''')

    x_exciting_geometry_dummy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        time for scf in geometry optimization
        ''')

    x_exciting_maximum_force_magnitude = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        Maximum force magnitude in geometry optimization
        ''')

    x_exciting_geometry_optimization_threshold_force = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        Value of threshold for the force modulus as convergence criterion of the
        geometry_optimization_method used in exciting
        ''')

    x_exciting_hartree_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Hartree energy final
        ''')

    x_exciting_interstitial_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Interstitial charge
        ''')

    x_exciting_madelung_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Madelung energy final
        ''')

    x_exciting_nuclear_nuclear_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Nuclear-nuclear energy final
        ''')

    x_exciting_store_total_forces = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storing converged atom forces cartesian
        ''')

    x_exciting_total_MT_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Total charge in muffin-tins
        ''')

    x_exciting_XC_potential = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        XC potential final
        ''')

    x_exciting_xs_bse_number_of_components = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of independent components in the dielectric tensor
        ''')

    x_exciting_xs_bse_number_of_energy_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Energy mesh for the dielectric function, conductivity and loss function
        ''')

    x_exciting_xs_tddft_dielectric_function_local_field = Quantity(
        type=np.dtype(np.float64),
        shape=[2, 'x_exciting_xs_tddft_number_of_q_points', 'x_exciting_xs_tddft_number_of_components', 'x_exciting_xs_tddft_number_of_epsilon_values'],
        description='''
        Dielectric function epsilon including local-field effects
        ''')

    x_exciting_xs_tddft_dielectric_function_no_local_field = Quantity(
        type=np.dtype(np.float64),
        shape=[2, 'x_exciting_xs_tddft_number_of_q_points', 'x_exciting_xs_tddft_number_of_components', 'x_exciting_xs_tddft_number_of_epsilon_values'],
        description='''
        Dielectric function epsilon without local-field effects
        ''')

    x_exciting_xs_tddft_dielectric_tensor_no_sym = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_tddft_number_of_q_points', 2, 3, 3],
        description='''
        No-symmetrized static dielectric tensor
        ''')

    x_exciting_xs_tddft_dielectric_tensor_sym = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_tddft_number_of_q_points', 2, 3, 3],
        description='''
        Symmetrized static dielectric tensor
        ''')

    x_exciting_xs_tddft_epsilon_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_tddft_number_of_epsilon_values'],
        unit='joule',
        description='''
        Array containing the set of discrete energy values for the dielectric function
        epsilon.
        ''')

    x_exciting_xs_tddft_loss_function_local_field = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_tddft_number_of_q_points', 'x_exciting_xs_tddft_number_of_components', 'x_exciting_xs_tddft_number_of_epsilon_values'],
        description='''
        Loss function including local-field effects
        ''')

    x_exciting_xs_tddft_loss_function_no_local_field = Quantity(
        type=np.dtype(np.float64),
        shape=['x_exciting_xs_tddft_number_of_q_points', 'x_exciting_xs_tddft_number_of_components', 'x_exciting_xs_tddft_number_of_epsilon_values'],
        description='''
        Loss function without local-field effects
        ''')

    x_exciting_xs_tddft_number_of_epsilon_values = Quantity(
        type=int,
        shape=[],
        description='''
        Gives the number of energy values for the dielectric function epsilon.
        ''')

    x_exciting_xs_tddft_number_of_optical_components = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of independent components in the dielectric function epsilon
        ''')

    x_exciting_xs_tddft_number_of_q_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of Q points
        ''')

    x_exciting_xs_tddft_optical_component = Quantity(
        type=str,
        shape=['x_exciting_xs_tddft_number_of_optical_components'],
        description='''
        Value of the independent optical components in the dielectric function epsilon
        ''')

    x_exciting_xs_tddft_sigma_local_field = Quantity(
        type=np.dtype(np.float64),
        shape=[2, 'x_exciting_xs_tddft_number_of_q_points', 'x_exciting_xs_tddft_number_of_components', 'x_exciting_xs_tddft_number_of_epsilon_values'],
        description='''
        Sigma including local-field effects
        ''')

    x_exciting_xs_tddft_sigma_no_local_field = Quantity(
        type=np.dtype(np.float64),
        shape=[2, 'x_exciting_xs_tddft_number_of_q_points', 'x_exciting_xs_tddft_number_of_components', 'x_exciting_xs_tddft_number_of_epsilon_values'],
        description='''
        Sigma without local-field effects
        ''')

    x_exciting_xs_qpointset_qpoint = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        A q-point is given in reciprocal space coordinates
        ''')

    x_exciting_section_bandstructure = SubSection(
        sub_section=SectionProxy('x_exciting_section_bandstructure'),
        repeats=True)

    x_exciting_section_dos = SubSection(
        sub_section=SectionProxy('x_exciting_section_dos'),
        repeats=True)

    x_exciting_section_fermi_surface = SubSection(
        sub_section=SectionProxy('x_exciting_section_fermi_surface'),
        repeats=True)

    x_exciting_section_MT_charge_atom = SubSection(
        sub_section=SectionProxy('x_exciting_section_MT_charge_atom'),
        repeats=True
    )

    x_exciting_section_MT_moment_atom = SubSection(
        sub_section=SectionProxy('x_exciting_section_MT_moment_atom'),
        repeats=True
    )

    x_exciting_exciton = SubSection(sub_section=x_exciting_exciton_calculation.m_def, repeats=False)

    x_exciting_epsilon = SubSection(sub_section=x_exciting_epsilon_calculation.m_def, repeats=False)

    x_exciting_sigma = SubSection(sub_section=x_exciting_sigma_calculation.m_def, repeats=False)

    x_exciting_loss = SubSection(sub_section=x_exciting_loss_calculation.m_def, repeats=False)


class System(simulation.system.System):

    m_def = Section(validate=False, extends_base_section=True)

    x_exciting_brillouin_zone_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter ** 3',
        description='''
        Brillouin zone volume
        ''')

    x_exciting_core_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Core charge
        ''')

    x_exciting_core_charge_initial = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Core charge
        ''')

    x_exciting_electronic_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Electronic charge
        ''')

    x_exciting_empty_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of empty states
        ''')

    x_exciting_clathrates_atom_labels = Quantity(
        type=str,
        shape=['number_of_atoms'],
        description='''
        Labels of the atoms in the clathrates.
        ''')

    x_exciting_clathrates_atom_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms', 3],
        description='''
        Ordered list of the atoms coordinates in the clathrates.
        ''')

    x_exciting_clathrates = Quantity(
        type=bool,
        shape=[],
        description='''
        It indicates whether the system is a clathrate.
        ''')

    x_exciting_gkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        Maximum length of |G+k| for APW functions
        ''')

    x_exciting_gmaxvr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        Maximum length of |G|
        ''')

    x_exciting_gvector_size_x = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector grid size x
        ''')

    x_exciting_gvector_size_y = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector grid size y
        ''')

    x_exciting_gvector_size_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector grid size z
        ''')

    x_exciting_gvector_size = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        G-vector grid size
        ''')

    x_exciting_gvector_total = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        G-vector total
        ''')

    x_exciting_hamiltonian_size = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum Hamiltonian size
        ''')

    x_exciting_kpoint_offset_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        K-points offset y component
        ''')

    x_exciting_kpoint_offset_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        K-points offset z component
        ''')

    x_exciting_kpoint_offset = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        K-points offset
        ''')

    x_exciting_lmaxapw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Angular momentum cut-off for the APW functions
        ''')

    x_exciting_lo = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of local-orbitals
        ''')

    x_exciting_nuclear_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Nuclear charge
        ''')

    x_exciting_number_kpoint_x = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points x
        ''')

    x_exciting_number_kpoint_y = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points y
        ''')

    x_exciting_number_kpoint_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points z
        ''')

    x_exciting_number_kpoints = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number k-points
        ''')

    x_exciting_number_of_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The number of atoms in the unit cell
        ''')

    x_exciting_potential_mixing = Quantity(
        type=str,
        shape=[],
        description='''
        Mixing type for potential
        ''')

    x_exciting_pw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Maximum number of plane-waves
        ''')

    x_exciting_rgkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        Radius MT * Gmax
        ''')

    x_exciting_species_rtmin = Quantity(
        type=str,
        shape=[],
        description='''
        Chemical species with radius RT * Gmax
        ''')

    x_exciting_simulation_reciprocal_cell = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        unit='meter',
        description='''
        Reciprocal lattice vectors (in Cartesian coordinates) of the simulation cell. The
        first index runs over the $x,y,z$ Cartesian coordinates, and the second index runs
        over the 3 lattice vectors.
        ''')

    x_exciting_smearing_type = Quantity(
        type=str,
        shape=[],
        description='''
        Smearing scheme for KS occupancies
        ''')

    x_exciting_smearing_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smearing width for KS occupancies
        ''')

    x_exciting_unit_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter ** 3',
        description='''
        unit cell volume
        ''')

    x_exciting_valence_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Valence charge
        ''')

    x_exciting_valence_charge_initial = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Valence charge
        ''')

    x_exciting_valence_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Total number of valence states
        ''')

    x_exciting_wigner_radius = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        Effective Wigner radius
        ''')

    x_exciting_number_of_bravais_lattice_symmetries = Quantity(
        type=int,
        shape=[],
        description='''
        Number of Bravais lattice symmetries
        ''')

    x_exciting_number_of_crystal_symmetries = Quantity(
        type=int,
        shape=[],
        description='''
        Number of crystal symmetries
        ''')

    x_exciting_section_atoms_group = SubSection(
        sub_section=SectionProxy('x_exciting_section_atoms_group'),
        repeats=True)

    x_exciting_section_lattice_vectors = SubSection(
        sub_section=SectionProxy('x_exciting_section_lattice_vectors'),
        repeats=True)

    x_exciting_section_reciprocal_lattice_vectors = SubSection(
        sub_section=SectionProxy('x_exciting_section_reciprocal_lattice_vectors'),
        repeats=True)

    x_exciting_section_spin = SubSection(
        sub_section=SectionProxy('x_exciting_section_spin'),
        repeats=True)

    x_exciting_section_xc = SubSection(
        sub_section=SectionProxy('x_exciting_section_xc'),
        repeats=True)


class x_exciting_section_MT_charge_atom(MSection):
    '''
    atom-resolved charges in muffin tins
    '''

    m_def = Section(validate=False)

    x_exciting_MT_charge_atom_index = Quantity(
        type=int,
        shape=[],
        description='''
        index of the atom with muffin-tin charge
        ''')

    x_exciting_MT_charge_atom_symbol = Quantity(
        type=str,
        shape=[],
        description='''
        chemical symbol of the atom with muffin-tin charge
        ''')

    x_exciting_MT_charge_atom_value = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        value of the muffin-tin charge on atom
        ''')


class x_exciting_section_MT_moment_atom(MSection):
    '''
    atom-resolved moments in muffin tins
    '''

    m_def = Section(validate=False)

    x_exciting_MT_moment_atom_index = Quantity(
        type=int,
        shape=[],
        description='''
        index of the atom with muffin-tin moment
        ''')

    x_exciting_MT_moment_atom_symbol = Quantity(
        type=str,
        shape=[],
        description='''
        chemical symbol of the atom with muffin-tin moment
        ''')

    x_exciting_MT_moment_atom_value = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        unit='coulomb * meter',
        description='''
        value of the muffin-tin moment on atom
        ''')


class ScfIteration(simulation.calculation.ScfIteration):

    m_def = Section(validate=False, extends_base_section=True)

    x_exciting_charge_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        exciting charge convergence
        ''')

    x_exciting_core_electron_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Core-electron kinetic energy
        ''')

    x_exciting_core_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Core charge
        ''')

    x_exciting_valence_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Valence charge
        ''')

    x_exciting_core_leakage = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Core leakage
        ''')

    x_exciting_correlation_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Correlation energy
        ''')

    x_exciting_coulomb_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb energy
        ''')

    x_exciting_coulomb_potential_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Coulomb potential energy
        ''')

    x_exciting_dos_fermi = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / joule',
        description='''
        DOS at Fermi energy
        ''')

    x_exciting_effective_potential_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        exciting effective potential convergence
        ''')

    x_exciting_force_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        exciting force convergence
        ''')

    x_exciting_effective_potential_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Effective potential energy
        ''')

    x_exciting_electron_nuclear_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Electron-nuclear energy
        ''')

    x_exciting_energy_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        exciting energy convergence
        ''')

    x_exciting_exchange_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Exchange energy
        ''')

    x_exciting_fermi_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Fermi energy
        ''')

    x_exciting_gap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Estimated fundamental gap
        ''')

    x_exciting_hartree_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Hartree energy
        ''')

    x_exciting_IBS_force_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        exciting IBS force convergence
        ''')

    x_exciting_interstitial_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Interstitial charge
        ''')

    x_exciting_madelung_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Madelung energy
        ''')

    x_exciting_nuclear_nuclear_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Nuclear-nuclear energy
        ''')

    x_exciting_time = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='s',
        description='''
        scf iteration time
        ''')

    x_exciting_total_MT_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Total charge in muffin-tins
        ''')

    x_exciting_total_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Total charge
        ''')

    x_exciting_XC_potential = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        XC potential
        ''')

    x_exciting_interstitial_moment = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        unit='coulomb * meter',
        description='''
        Interstitial moment
        ''')

    x_exciting_total_MT_moment = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        unit='coulomb * meter',
        description='''
        Total moment in muffin-tins
        ''')

    x_exciting_total_moment = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        unit='coulomb * meter',
        description='''
        Total moment
        ''')

    x_exciting_section_MT_charge_atom_scf_iteration = SubSection(
        sub_section=SectionProxy('x_exciting_section_MT_charge_atom'),
        repeats=True)

    x_exciting_section_MT_moment_atom_scf_iteration = SubSection(
        sub_section=SectionProxy('x_exciting_section_MT_moment_atom'),
        repeats=True)


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_exciting_dummy = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dummy metadata for debuging purposes
        ''')

    x_exciting_volume_optimization = Quantity(
        type=bool,
        shape=[],
        description='''
        If the volume optimization is performed.
        ''')

    x_exciting_scf_threshold_energy_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Specifies the threshold for the x_exciting_energy_total_scf_iteration change
        between two subsequent self-consistent field (SCF) iterations.
        ''')

    x_exciting_scf_threshold_potential_change_list = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Specifies the threshold for the x_exciting_effective_potential_convergence between
        two subsequent self-consistent field (SCF) iterations.
        ''')

    x_exciting_scf_threshold_potential_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Specifies the threshold for the x_exciting_effective_potential_convergence between
        two subsequent self-consistent field (SCF) iterations.
        ''')

    x_exciting_scf_threshold_charge_change_list = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Specifies the threshold for the x_exciting_effective_potential_convergence between
        two subsequent self-consistent field (SCF) iterations.
        ''')

    x_exciting_scf_threshold_charge_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='coulomb',
        description='''
        Specifies the threshold for the x_exciting_effective_potential_convergence between
        two subsequent self-consistent field (SCF) iterations.
        ''')

    x_exciting_scf_threshold_force_change_list = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence tolerance for forces (not including IBS contribution) during the SCF
        run.
        ''')

    x_exciting_scf_threshold_force_change = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='newton',
        description='''
        Convergence tolerance for forces (not including IBS contribution) during the SCF
        run
        ''')

    x_exciting_electronic_structure_method = Quantity(
        type=str,
        shape=[],
        description='''
        String identifying the used electronic structure method. Allowed values are BSE
        and TDDFT. Temporary metadata to be canceled when BSE and TDDFT will be added to
        public metadata electronic_structure_method
        ''')

    x_exciting_xs_broadening = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Lorentzian broadening applied to the spectra.
        ''')

    x_exciting_xs_bse_angular_momentum_cutoff = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Angular momentum cutoff of the spherical harmonics expansion of the dielectric
        matrix.
        ''')

    x_exciting_xs_bse_antiresonant = Quantity(
        type=bool,
        shape=[],
        description='''
        If the anti-resonant part of the Hamiltonian is used for the BSE spectrum
        ''')

    x_exciting_xs_bse_number_of_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[4],
        description='''
        Range of bands included for the BSE calculation. The first pair of numbers
        corresponds to the band index for local orbitals and valence states (counted from
        the lowest eigenenergy), the second pair corresponds to the band index of the
        conduction states (counted from the Fermi level).
        ''')

    x_exciting_xs_bse_rgkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smallest muffin-tin radius times gkmax.
        ''')

    x_exciting_xs_bse_sciavbd = Quantity(
        type=bool,
        shape=[],
        description='''
        if the body of the screened Coulomb interaction is averaged (q=0).
        ''')

    x_exciting_xs_bse_sciavqbd = Quantity(
        type=bool,
        shape=[],
        description='''
        if the body of the screened Coulomb interaction is averaged (q!=0).
        ''')

    x_exciting_xs_bse_sciavqhd = Quantity(
        type=bool,
        shape=[],
        description='''
        if the head of the screened Coulomb interaction is averaged (q=0).
        ''')

    x_exciting_xs_bse_sciavqwg = Quantity(
        type=bool,
        shape=[],
        description='''
        if the wings of the screened Coulomb interaction is averaged (q=0).
        ''')

    x_exciting_xs_bse_sciavtype = Quantity(
        type=str,
        shape=[],
        description='''
        how the screened Coulomb interaction matrix is averaged
        ''')

    x_exciting_xs_bse_type = Quantity(
        type=str,
        shape=[],
        description='''
        which parts of the BSE Hamiltonian is considered. Possible values are IP, RPA,
        singlet, triplet.
        ''')

    x_exciting_xs_bse_xas = Quantity(
        type=bool,
        shape=[],
        description='''
        X-ray absorption spectrum
        ''')

    x_exciting_xs_bse_xas_number_of_bands = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        Range of bands included for the BSE calculation. The pair corresponds to the band
        index of the conduction states (counted from the Fermi level).
        ''')

    x_exciting_xs_bse_xasatom = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom number for which the XAS is calculated.
        ''')

    x_exciting_xs_bse_xasedge = Quantity(
        type=str,
        shape=[],
        description='''
        Defines the initial states of the XAS calculation.
        ''')

    x_exciting_xs_bse_xasspecies = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Species number for which the XAS is calculated..
        ''')

    x_exciting_xs_gqmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='1 / meter',
        description='''
        G vector cutoff for the plane-waves matrix elements.
        ''')

    x_exciting_xs_lmaxapw = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Angular momentum cut-off for the APW functions.
        ''')

    x_exciting_xs_ngridk = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        k-point mesh for the excited states calculation.
        ''')

    x_exciting_xs_ngridq = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        q-point mesh for the excited states calculation.
        ''')

    x_exciting_xs_number_of_empty_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of empty states used in the calculation of the response function.
        ''')

    x_exciting_xs_rgkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smallest muffin-tin radius times gkmax.
        ''')

    x_exciting_xs_scissor = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Scissor operator
        ''')

    x_exciting_xs_screening_ngridk = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        k-point mesh for the calculation of the screening.
        ''')

    x_exciting_xs_screening_number_of_empty_states = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of empty states used in the calculation of the screening.
        ''')

    x_exciting_xs_screening_rgkmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Smallest muffin-tin radius times gkmax.
        ''')

    x_exciting_xs_screening_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of screening used in the calculations. POssible values are full, diag,
        noinvdiag, longrange.
        ''')

    x_exciting_xs_screening_vkloff = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        k-point set offset for the screening
        ''')

    x_exciting_xs_starting_point = Quantity(
        type=str,
        shape=[],
        description='''
        Exchange-correlation functional of the ground-state calculation. See xc_functional
        list at https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-meta-info/wikis/metainfo/XC-
        functional
        ''')

    x_exciting_xs_tddft_analytic_continuation = Quantity(
        type=bool,
        shape=[],
        description='''
        Analytic continuation for the calculation of the Kohn-Sham response function
        ''')

    x_exciting_xs_tddft_analytic_continuation_number_of_intervals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of energy intervals (on imaginary axis) for analytic continuation.
        ''')

    x_exciting_xs_tddft_anomalous_hall_conductivity = Quantity(
        type=bool,
        shape=[],
        description='''
        If the anomalous Hall conductivity term is included in the calculation of the
        dielectric tensor [see PRB 86, 125139 (2012)].
        ''')

    x_exciting_xs_tddft_anti_resonant_dielectric = Quantity(
        type=bool,
        shape=[],
        description='''
        If the anti-resonant part is considered for the calculation of the dielectric
        function
        ''')

    x_exciting_xs_tddft_anti_resonant_xc_kernel = Quantity(
        type=bool,
        shape=[],
        description='''
        If the anti-resonant part is considered for the calculation of the MBPT-derived
        xc-kernel
        ''')

    x_exciting_xs_tddft_diagonal_xc_kernel = Quantity(
        type=bool,
        shape=[],
        description='''
        If true, only the diagonal part of xc-kernel is used.
        ''')

    x_exciting_xs_tddft_drude = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        unit='1 / second',
        description='''
        Parameters defining the semiclassical Drude approximation to intraband term. The
        first value determines the plasma frequency ωp and the second the inverse
        relaxation time ωτ: χD0=1/ω ωp^2/(ω+iωτ)
        ''')

    x_exciting_xs_tddft_finite_q_intraband_contribution = Quantity(
        type=bool,
        shape=[],
        description='''
        Parameter determining whether the the intraband contribution is included in the
        calculation for the finite q.
        ''')

    x_exciting_xs_tddft_lmax_alda = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Angular momentum cutoff for the Rayleigh expansion of the exponential factor for
        ALDA-kernel
        ''')

    x_exciting_xs_tddft_macroscopic_dielectric_function_q_treatment = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Treatment of macroscopic dielectric function for the Q-point outside the Brillouin
        zone. A value of 0 uses the full Q and the (0,0) component of the microscopic
        dielectric matrix is used. A value of 1 means a decomposition Q=q+Gq and the
        (Qq,Qq) component of the microscopic dielectric matrix is used.
        ''')

    x_exciting_xs_tddft_split_parameter = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Split parameter for degeneracy in energy differences of MBPT derived xc kernels.
        See A. Marini, Phys. Rev. Lett., 91, (2003) 256402.
        ''')

    x_exciting_xs_tddft_xc_kernel = Quantity(
        type=str,
        shape=[],
        description='''
        Defines which xc kernel is to be used. Possible choices are: RPA - Random-phase
        approximation kernel (fxc=0); LRCstatic - Long-range correction kernel (fxc =
        -alpha/q^2) with alpha given by alphalrcdyn see S. Botti et al., Phys. Rev. B 69,
        155112 (2004); LRCdyn - Dynamical long-range correction kernel, with alpha anf
        beta give by alphalrcdyn and betalrcdyn, respectively, see S. Botti et al., Phys.
        Rev. B 72, 125203 (2005); ALDA - Adiabatic LDA kernel, with Vxc given by the spin-
        unpolarised exchange-correlation potential corresponding to the Perdew-Wang
        parameterisation of Ceperley-Alder's Monte-Carlo data, see Phys. Rev. B 45, 13244
        (1992) and Phys. Rev. Lett. 45, 566 (1980); MB1 - BSE derived xc kernel. See L.
        Reining et al., Phys. Rev. Lett. 88, 066404 (2002) and A. Marini et al., Phys.
        Rev. Lett. 91, 256402 (2003); BO - Bootstrap kernel, see S. Sharma et al., Phys.
        Rev. Lett. 107, 186401 (2011); BO_SCALAR - Scalar version of the bootstrap kernel;
        see S. Sharma et al., Phys. Rev. Lett. 107, 186401 (2011); RBO - RPA bootstrap
        kernel; see S. Rigamonti et al., Phys. Rev. Lett. 114, 146402 (2015).
        ''')

    x_exciting_xs_tetra = Quantity(
        type=bool,
        shape=[],
        description='''
        Integration method (tetrahedron) used for the k-space integration in the Kohn-Sham
        response function.
        ''')

    x_exciting_xs_vkloff = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        k-point set offset
        ''')

    x_exciting_xs_xstype = Quantity(
        type=str,
        shape=[],
        description='''
        Type of excited states calculation, BSE or TDDFT
        ''')

    x_exciting_xs_energywindow_values = Quantity(
        type=np.float64,
        shape=[2],
        unit='joule',
        description='''
        Energy interval lower and upper limits. Default is [-0.5d0, 0.5d0] in Hartree.
        ''')

    x_exciting_xs_energywindow_points = Quantity(
        type=np.int32,
        shape=[],
        description='''
        Number of points to be sampled linearly inside the energy interval including the
        lower limit. Default is 500.
        ''')


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_exciting_dummy2 = Quantity(
        type=str,
        shape=[],
        description='''
        dummy metadata for debuging purposes
        ''')

    x_exciting_section_geometry_optimization = SubSection(
        sub_section=SectionProxy('x_exciting_section_geometry_optimization'),
        repeats=True)
