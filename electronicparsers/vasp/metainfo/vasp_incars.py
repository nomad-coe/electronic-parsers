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


class x_vasp_incar_param(MCategory):
    '''
    Incar parameters. Value stored in incar.
    '''

    m_def = Category()


class Method(simulation.method.Method):

    m_def = Section(validate=False, extends_base_section=True)

    x_vasp_incar_ADDGRID = Quantity(
        type=bool,
        shape=[],
        description='''
        ADDGRID determines whether an additional support grid is used for the evaluation
        of the augmentation charges.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_AEXX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AEXX specifies the fraction of exact exchange in a Hartree-Fock/DFT hybrid
        functional type calculation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_AGGAC = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AGGAC specifies the fraction of gradient corrections to the correlation in a
        Hartree-Fock/DFT hybrid functional type calculation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_AGGAX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AGGAX specifies the fraction of gradient corrections to the exchange in a Hartree-
        Fock/DFT hybrid functional type calculation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ALDAC = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ALDAC specifies the fraction of LDA correlation in a Hartree-Fock/DFT hybrid
        functional type calculation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ALGO = Quantity(
        type=str,
        shape=[],
        description='''
        Option to specify the electronic minimisation algorithm (as of VASP.4.5) and/or to
        select the type of GW calculations.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_AMIN = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AMIN specifies the minimal mixing parameter in Kerker's initial approximation to
        the charge dielectric function used in the Broyden / Pulay mixing scheme (IMIX=4,
        INIMIX=1).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_AMIX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AMIX specifies the linear mixing parameter.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_AMIX_MAG = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AMIX_MAG linear mixing parameter for the magnetization density.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ANDERSEN_PROB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ANDERSEN_PROB sets the collision probability for the Anderson thermostat (in case
        VASP was compiled with the flag -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ANTIRES = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The flag ANTIRES determines whether the Tamm-Dancoff approximation is used or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_APACO = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        APACO sets the maximum distance in the evaluation of the pair-correlation function
        (in Angstroms).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_BMIX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        BMIX sets the cutoff wave vector for Kerker mixing scheme (IMIX = 1 and / or
        INIMIX = 1).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_BMIX_MAG = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        BMIX_MAG sets the cutoff wave vector for Kerker mixing scheme (IMIX=1 and/or
        INIMIX=1) for the magnetization density.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CH_LSPEC = Quantity(
        type=bool,
        shape=[],
        description='''
        This flag controls whether the imaginary part of the dielectric function for a
        selected core electron is calculated and written to the OUTCAR file or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CH_NEDOS = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies the number of frequency (energy) grid points on the x-axis in
        the calculation of the dielectric function for XAS spectra.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CH_SIGMA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag specifies the broadening in eV of the imaginary dielectric function for a
        core electron.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CLL = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CLL selects the angular (l) quantum number of the excited electron when using
        ICORELEVEL=2.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CLN = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CLN selects the main quantum number of the excited electron when using
        ICORELEVEL=2.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CLNT = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CLNT selects for which species the core levels are calculated using the tag
        ICORELEVEL.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CLZ = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CLZ selects the electron count of the excited electron when using ICORELEVEL=2.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CMBJ = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        defines the _c_ parameter in the modified Becke-Johnson meta-GGA potential. NOTE:
        Either specify a single value, or one value per atomic type (FIXME)
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CMBJA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        sets the $\\alpha$ parameter in the modified Becke-Johnson meta-GGA potential.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CMBJB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        sets the $\\eta$ parameter in the modified Becke-Johnson meta-GGA potential.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_CSHIFT = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CSHIFT sets the (small) complex shift $\\eta$ in the Kramers-Kronig transformation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_DEPER = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        DEPER specifies a relative stopping criterion for the optimization of an
        eigenvalue.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_DIMER_DIST = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag DIMER_DIST defines the step size for the numerical differentiation (in
        Angstrongs) for the Improved Dimer Method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_DIPOL = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Specifies the center of the cell in direct lattice coordinates with respect to
        which the total dipole-moment in the cell is calculated.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_DQ = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Step size for the finite difference _k_-space derivative in the linear response
        calculation of chemical shifts. Typical values for DQ are in the range [0.001 -
        0.003]. The default is often sufficient
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EBREAK = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EBREAK specifies an absolute stopping criterion for the optimization of an
        eigenvalue.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EDIFF = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EDIFF specifies the global break condition for the electronic SC-loop.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EDIFFG = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EDIFFG defines the break condition for the ionic relaxation loop.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EFIELD = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EFIELD controls the magnitude of the applied electric force field.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EFIELD_PEAD = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        EFIELD_PEAD specifies the homogeneous electric field in the electric enthalpy
        functional used to compute the  self-consistent response to finite electric
        fields.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EINT = Quantity(
        type=np.dtype(np.float64),
        shape=[2],
        description='''
        Specifies the energy range of the bands that are used for the evaluation of the
        partial charge density needed in Band decomposed charge densities. Check also
        NBMOD and IBAND.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EMAX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EMAX specifies the  upper boundary of the energy range for the evaluation of the
        DOS.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EMIN = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        specifies the lower boundary of the energy range for the evaluation of the DOS.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ENAUG = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENAUG specifies the cut-off energy of the plane wave representation of the
        augmentation charges in eV.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ENCUT = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENCUT specifies the cutoff energy for the planewave basis set in eV.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ENCUTFOCK = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The ENCUTFOCK tag sets the energy cutoff that determines the FFT grids used by the
        Hartree-Fock routines. WARNING: The flag ENCUTFOCK is no longer supported in
        VASP.5.2.4 and newer versions. Please use PRECFOCK instead.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ENCUTGW = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The tag ENCUTGW sets the energy cutoff for response function. It controls the
        basis set for the response functions  in exactly the same manner as ENCUT does for
        the orbitals.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ENCUTGWSOFT = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag ENCUTGWSOFT sets the energy cutoff for response function, such that it
        allows to truncate the Coulomb kernel slowly between the energy specified by
        ENCUTGWSOFT and ENCUTGW.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ENINI = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENINI controls the cutoff during the initial (steepest descent) phase for
        IALGO=48.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EPSILON = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EPSILON sets the dielectric constant of the medium.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EVENONLY = Quantity(
        type=bool,
        shape=[],
        description='''
        EVENONLY=.TRUE. selects a subset of k-points for the representation of the Fock
        exchange potential, with $C_1=C_2=C_3=1$, and $n_1+n_2+n_3$ even.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_EVENONLYGW = Quantity(
        type=bool,
        shape=[],
        description='''
        EVENONLYGW allows to restrict the k-points in the evaluation of response functions
        (in GW calculations) to even values.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_FERDO = Quantity(
        type=np.dtype(np.float64),
        shape=['x_vasp_incar_NBANDS * x_vasp_number_of_k_points'],
        description='''
        FERDO sets the occupancies of the states in the down-spin channel for ISMEAR=-2
        and ISPIN=2.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_FERWE = Quantity(
        type=np.dtype(np.float64),
        shape=['x_vasp_incar_NBANDS  *  x_vasp_number_of_k_points'],
        description='''
        FERWE sets the occupancies of the states for  ISMEAR=-2.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_FINDIFF = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The flag DIMER_DIST defines whether a forward (FINDIFF=1) or a central (FINDIFF=2)
        difference formula for the numerical differentiation to compute the curvature
        along the dimer direction is used in the Improved Dimer Method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_GGA = Quantity(
        type=str,
        shape=[],
        description='''
        GGA specifies the type of generalized-gradient-approximation one wishes to use.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_GGA_COMPAT = Quantity(
        type=bool,
        shape=[],
        description='''
        This flag restores the full lattice symmetry for gradient corrected functionals.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_HFLMAX = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        To be compatible w.r.t. old releases, VASP also reads the flag HFLMAX to the same
        effect as LMAXFOCK.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_HFRCUT = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        HFRCUT specifies the spherical cutoff radius for the potential kernel in hybrid
        functionals.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_HFSCREEN = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        HFSCREEN specifies the range-separation parameter in range separated hybrid
        functionals.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_HILLS_BIN = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        HILLS_BIN sets the number of steps after which the bias potential is updated in a
        metadynamics run (in case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_HILLS_H = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        HILLS_H specifies the height of the Gaussian hill (in eV) used in metadynamics (in
        case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_HILLS_W = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        HILLS_W specifies the width of the Gaussian hill (in units of the corresponding
        collective variable) used in metadynamics (in case VASP was compiled with
        -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_HITOLER = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        HITOLER specifies the convergence parameter for iterative Hirschfeld partitioning
        (DFT-TS/HI).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_I_CONSTRAINED_M = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        I_CONSTRAINED_M switches on the constrained local moments approach.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IALGO = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IALGO selects the algorithm used to optimize the orbitals. WARNING
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IBAND = Quantity(
        type=np.dtype(np.uint32),
        shape=['1..x_vasp_incar_NBANDS'],
        description='''
        Controls which bands are used in the calculation of Band decomposed charge
        densities. Check also NBMOD and EINT.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IBRION = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IBRION determines how the ions are updated and moved.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ICHARG = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ICHARG determines how VASP constructs the <i>initial</i> charge density.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ICHIBARE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        determines the order of the finite difference stencil used to calculate the
        magnetic susceptibility.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ICORELEVEL = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ICORELEVEL controls whether the core energies are explicitely calculated or not
        and how they are calculated.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IDIPOL = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IDIPOL switches on monopole/dipole and quadrupole corrections to the total energy.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IEPSILON = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The flag IEPSILON determines along which Cartesien the E field is applied.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IGPAR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies the socalled parallel or  $G_{||}$ direction in the integration
        over the reciprocal space unit cell needed for LCALCPOL.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IMAGES = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IMAGES defines the number of interpolated geometries between the initial and final
        state in Elastic Band calculations
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IMIX = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IMIX specifies the type of mixing.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_INCREM = Quantity(
        type=np.dtype(np.float64),
        shape=['x'],
        description='''
        INCREM controls the transformation velocity in the slow-growth approach (in case
        VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_INIMIX = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        INIMIX determines the functional form of the initial mixing matrix in the Broyden
        scheme (IMIX=4).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_INIWAV = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        INIWAV specifies how to set up the initial orbitals in case ISTART=0.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IPEAD = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IPEAD specifies the order of the finite difference stencil used to compute the
        derivative of the cell-periodic part of the orbitals w.r.t. **k** (LPEAD=.TRUE.),
        and the derivative of the polarization w.r.t. the orbitals,  for (LCALCEPS=.TRUE.,
        or EFIELD_PEAD$\\not=$0).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ISIF = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ISIF determines whether the stress tensor is calculated and which principal
        degrees-of-freedom are allowed to change in relaxation and molecular dynamics
        runs.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ISMEAR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ISMEAR determines how the partial occupancies $f_{n\\mathbf{k}}$  are set for each
        orbital. SIGMA  determines the width of the smearing in eV.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ISPIN = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ISPIN specifies spin polarization.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ISTART = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ISTART determines whether or not to read the WAVECAR file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ISYM = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ISYM determines the way VASP treats symmetry.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IVDW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag controls whether vdW corrections are calculated or not. If they are
        calculated IVDW controls how they are calculated.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_IWAVPR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IWAVPR determines how orbitals and/or charge densities are extrapolated from one
        ionic configuration to the next configuration.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_KBLOCK = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        After KBLOCK*NBLOCK ionic steps the averaged pair correlation function and DOS are
        written to the files PCDAT and DOSCAR. More details can be found on the page
        describing the tag NBLOCK.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_KGAMMA = Quantity(
        type=bool,
        shape=[],
        description='''
        Determines whether the _k_-points (determined by the tag KSPACING if KPOINTS file
        is not present) are center around (KGAMMA=.TRUE.), or shifted away
        (KGAMMA=.FALSE.) from the $\\Gamma$ point.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_KPAR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        KPAR determines the number of **k**-points that are to be treated in parallel
        (available as of VASP.5.3.2).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_KPOINT_BSE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The flag KPOINT_BSE allows to calculate the dielectric matrix at one of the
        kpoints used to sample the Brillouin zone. NOTE: Either specify one or three
        integers (FIXME)
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_KPUSE = Quantity(
        type=np.dtype(np.int32),
        shape=['1..x_vasp_number_of_k_points'],
        description='''
        Specifies which k-points are used in the evaluation of the partial dos (Band
        decomposed charge densities).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_KSPACING = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The tag KSPACING determines the number of k-points if the KPOINTS file is not
        present.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LADDER = Quantity(
        type=bool,
        shape=[],
        description='''
        Controls whether the ladder diagrams are included in the BSE calculation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LAECHG = Quantity(
        type=bool,
        shape=[],
        description='''
        When LAECHG=.TRUE. the all-electron charge density will be reconstructed
        explicitly and written out to file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LAMBDA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        LAMBDA sets the weight with which the penalty terms of the constrained local
        moment approach enter into the total energy expression and the Hamiltonian.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LANGEVIN_GAMMA = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        LANGEVIN_GAMMA specifies the friction coefficients (in ps$^{-1}$) for atomic
        degrees-of-freedom when using a Langevin thermostat (in case VASP was compiled
        with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LANGEVIN_GAMMA_L = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        LANGEVIN_GAMMA_L specifies the friction coefficient (in ps$^{-1}$) for lattice
        degrees-of-freedom in case of Parrinello-Rahman dynamics (in case VASP was
        compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LASPH = Quantity(
        type=bool,
        shape=[],
        description='''
        include non-spherical contributions related to the gradient of the density in the
        PAW spheres.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LASYNC = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag controls the overlap in communication.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LATTICE_CONSTRAINTS = Quantity(
        type=bool,
        shape=[3],
        description='''
        The tag LATTICE_CONSTRAINTS determines whether the lattice dynamics are released
        (LATTICE_CONSTRAINTS=.TRUE.) in the given directions or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LBERRY = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag is used in the the evaluation of the Berry phase expression for the
        electronic polarization of an insulating system.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LBLUEOUT = Quantity(
        type=bool,
        shape=[],
        description='''
        for LBLUEOUT=.TRUE., VASP writes output for the free-energy gradient calculation
        to the REPORT-file (in case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LBONE = Quantity(
        type=bool,
        shape=[],
        description='''
        LBONE adds the small B-component to the chemical shift tensor.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LCALCEPS = Quantity(
        type=bool,
        shape=[],
        description='''
        for LCALCEPS=.TRUE. the macroscopic ion-clamped static dielectric tensor, Born
        effective charge tensors, and the ion-clamped piezoelectric tensor of the system
        are determined from the response to finite electric fields.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LCALCPOL = Quantity(
        type=bool,
        shape=[],
        description='''
        LCALCPOL=.TRUE. switches on the evaluation of the Berry phase expressions for the
        macroscopic electronic polarization in accordance with the so-called Modern Theory
        of Polarization.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LCHARG = Quantity(
        type=bool,
        shape=[],
        description='''
        LCHARG determines whether the charge densities (files CHGCAR and CHG) are written.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LCHIMAG = Quantity(
        type=bool,
        shape=[],
        description='''
        calculate the chemical shifts by means of linear response.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LCORR = Quantity(
        type=bool,
        shape=[],
        description='''
        Controls whether Harris corrections are calculated or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDAU = Quantity(
        type=bool,
        shape=[],
        description='''
        LDAU=.TRUE. switches on the L(S)DA+U.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDAUJ = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        LDAUJ specifies the strength of the effective on-site exchange interactions.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDAUL = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atomic_species'],
        description='''
        LDAUL specifies the _l_-quantum number for which the on-site interaction is added.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDAUPRINT = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LDAUPRINT controls the verbosity of the L(S)DA+U routines.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDAUTYPE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LDAUTYPE specifies which type of L(S)DA+U approach will be used.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDAUU = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        LDAUU specifies the strength of the effective on-site Coulomb interactions.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDIAG = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag determines whether a subspace diagonalization is performed or not within
        the main algorithm selected by IALGO.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LDIPOL = Quantity(
        type=bool,
        shape=[],
        description='''
        LDIPOL switches on corrections to the potential and forces in VASP. Can be applied
        for charged molecules and  molecules and slabs with a net dipole moment.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LEFG = Quantity(
        type=bool,
        shape=[],
        description='''
        The LEFG Computes the Electric Field Gradient at positions of the atomic nuclei.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LELF = Quantity(
        type=bool,
        shape=[],
        description='''
        LELF determines whether to create an ELFCAR file or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LEPSILON = Quantity(
        type=bool,
        shape=[],
        description='''
        LEPSILON=.TRUE. determines the static dielectric matrix, ion-clamped piezoelectric
        tensor and the Born effective charges using density functional perturbation
        theory.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LFOCKAEDFT = Quantity(
        type=bool,
        shape=[],
        description='''
        LFOCKAEDFT forces VASP to use the same charge augmentation for the Hartree and DFT
        exchange correlation part as is used in the Fock exchange and the many body beyond
        DFT methods, such as RPA, MP2 etc.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LHARTREE = Quantity(
        type=bool,
        shape=[],
        description='''
        Controls whether the bubble diagrams are included in the BSE calculation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LHFCALC = Quantity(
        type=bool,
        shape=[],
        description='''
        LHFCALC specifies whether Hartree-Fock/DFT hybrid functional type calculations are
        performed.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LHYPERFINE = Quantity(
        type=bool,
        shape=[],
        description='''
        compute the hyperfine tensors at the atomic sites (available as of vasp.5.3.2).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LKPROJ = Quantity(
        type=bool,
        shape=[],
        description='''
        switches on the **k**-point projection scheme.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LLRAUG = Quantity(
        type=bool,
        shape=[],
        description='''
        LLRAUG calculates the two-center contributions to the chemical shift tensor.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LMAXFOCK = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LMAXFOCK sets the maximum angular momentum quantum number _L_ for the augmentation
        of charge densities in Hartree-Fock type routines.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LMAXFOCKAE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NMAXFOCKAE and LMAXFOCKAE determine whether the overlap densities in the Fock
        exchange and correlated wave function methods are accurately reconstructed on the
        plane wave grid. This flag generally only applies to the Fock-exchange part as
        well as many-body post DFT methods (GW, RPA, MP2, etc.).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LMAXMIX = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LMAXMIX controls up to which l-quantum number the one-center PAW charge densities
        are passed through the charge density mixer and written to the CHGCAR file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LMAXPAW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LMAXPAW sets the maximum _l_-quantum number for the evaluation of the one-center
        terms on the radial support grids in the PAW method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LMAXTAU = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LMAXTAU is the maximum _l_-quantum number included in the PAW one-center expansion
        of the kinetic energy density.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LMIXTAU = Quantity(
        type=bool,
        shape=[],
        description='''
        send the kinetic energy density through the density mixer as well.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LMONO = Quantity(
        type=bool,
        shape=[],
        description='''
        LMONO switches on monopole-monopole corrections for the total energy.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LNABLA = Quantity(
        type=bool,
        shape=[],
        description='''
        LNABLA=.TRUE. evaluates the transversal expression for the frequency dependent
        dielectric matrix.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LNMR_SYM_RED = Quantity(
        type=bool,
        shape=[],
        description='''
        discard symmetry operations that are not consistent with the way _k_-space
        derivative are calculated in the linear response calculations of chemical shifts.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LNONCOLLINEAR = Quantity(
        type=bool,
        shape=[],
        description='''
        LNONCOLLINEAR specifies whether fully non-collinear magnetic calculations are
        performed.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LOCPROJ = Quantity(
        type=str,
        shape=[],
        description='''
        by means of the LOCPROJ-tag one may specify a (set of) local function(s) on which
        the orbitals are to be projected. These projections are written to the PROJCAR,
        LOCPROJ, and vasprun.xml files.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LOPTICS = Quantity(
        type=bool,
        shape=[],
        description='''
        LOPTICS=.TRUE. calculates the frequency dependent dielectric matrix after the
        electronic ground state has been determined.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LORBIT = Quantity(
        type=str,
        shape=[],
        description='''
        LORBIT, together with an appropriate RWIGS, determines whether the PROCAR or
        PROOUT files are written.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LORBMOM = Quantity(
        type=bool,
        shape=[],
        description='''
        LORBMOM specifies whether the orbital moments are written out or not (in a
        calculation using LSORBIT=.TRUE.).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LPARD = Quantity(
        type=bool,
        shape=[],
        description='''
        Determines whether partial (band or k-point decomposed) charge densities are
        evaluated. See also 'Band-decomposed charge densities' .
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LPEAD = Quantity(
        type=bool,
        shape=[],
        description='''
        for LPEAD=.TRUE., the derivative of the cell-periodic part of the orbitals w.r.t.
        **k**  is calculated using finite differences.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LPLANE = Quantity(
        type=bool,
        shape=[],
        description='''
        LPLANE switches on the plane-wise data distribution in real space.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LREAL = Quantity(
        type=bool,
        shape=[],
        description='''
        LREAL determines whether the projection operators are evaluated in real-space or
        in reciprocal space.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LRPA = Quantity(
        type=bool,
        shape=[],
        description='''
        LRPA=.TRUE. includes local field effect on the Hartree level only.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSCAAWARE = Quantity(
        type=bool,
        shape=[],
        description='''
        LSCAAWARE controls the distribution of the Hamilton matrix.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSCALAPACK = Quantity(
        type=bool,
        shape=[],
        description='''
        LSCALAPACK controls the use of scaLAPACK.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSCALU = Quantity(
        type=bool,
        shape=[],
        description='''
        LSCALU switches on the parallel LU decomposition (using scaLAPACK) in the
        orthonormalization of the wave functions.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSCSGRAD = Quantity(
        type=bool,
        shape=[],
        description='''
        LSCSGRAD decides whether to compute gradients in the calculation of the MBD
        dispersion energy.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSELFENERGY = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag controls whether the frequency dependent self-energy is calculated or
        not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSEPB = Quantity(
        type=bool,
        shape=[],
        description='''
        Specifies whether the charge density is calculated for every band separately and
        written to a file PARCHG.nb.* (LSEPB=.TRUE.) or whether charge density is merged
        for all selected bands and written to the files PARCHG.ALLB.* or PARCHG.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSEPK = Quantity(
        type=bool,
        shape=[],
        description='''
        Specifies whether the charge density of every k-point is write to the files
        PARCHG.*.nk (LSEPK=.TRUE.) or whether it is merged to a single file. If the merged
        file is written, then the weight of each k-point is determined from the KPOINTS
        file, otherwise the k-point weights of one are chosen.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSORBIT = Quantity(
        type=bool,
        shape=[],
        description='''
        LSORBIT specifies whether spin-orbit coupling is taken into account.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSPECTRAL = Quantity(
        type=bool,
        shape=[],
        description='''
        LSPECTRAL specifies to use the spectral method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSPECTRALGW = Quantity(
        type=bool,
        shape=[],
        description='''
        LSPECTRALGW specifies to use the spectral method for calculating the self-energy.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSPIRAL = Quantity(
        type=bool,
        shape=[],
        description='''
        set LSPIRAL=.TRUE. to represent spin spirals by means of a generalized Bloch
        condition.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LSUBROT = Quantity(
        type=bool,
        shape=[],
        description='''
        LSUBROT determines whether an optimal rotation matrix between the occupied and
        unoccupied block is sought, when a direct optimization of the energy functional is
        performed (i.e. ALGO = All | Damped).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LTHOMAS = Quantity(
        type=bool,
        shape=[],
        description='''
        LTHOMAS selects a decomposition of the exchange functional based on Thomas-Fermi
        screening.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LUSE_VDW = Quantity(
        type=bool,
        shape=[],
        description='''
        The flag LUSE_VDW determines whether the VdW-DF functional of Langreth and
        Lundqvist et al. is used or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LVDW_EWALD = Quantity(
        type=bool,
        shape=[],
        description='''
        LVDW_EWALD decides whether lattice summation in $E_{disp}$ expression by means of
        Ewald's summation is computed in the DFT-D2 method (available in VASP.5.3.4 and
        later).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LVDW_ONECELL = Quantity(
        type=bool,
        shape=[3],
        description='''
        LVDW_ONECELL  can be used to disable vdW interaction with mirror image in X Y Z
        direction. This is advisable for molecular calculations in the gas phase. In all
        other cases, use the default.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LVDWEXPANSION = Quantity(
        type=bool,
        shape=[],
        description='''
        LVDWEXPANSION  decides whether to write the two- to six- body contributions to MBD
        dispersion energy in the OUTCAR file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LVHAR = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag determines whether the total local potential (saved in the file LOCPOT)
        contains the entire local potential (ionic + Hartree + exchange correlation) or
        the electrostatic contributions only (ionic + Hartree).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LVTOT = Quantity(
        type=bool,
        shape=[],
        description='''
        LVTOT determines whether the total local potential is written to the LOCPOT file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LWANNIER90 = Quantity(
        type=bool,
        shape=[],
        description='''
        LWANNIER90=.TRUE. switches on the interface between VASP and WANNIER90.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LWANNIER90_RUN = Quantity(
        type=bool,
        shape=[],
        description='''
        LWANNIER90_RUN executes wannier_setup (see LWANNIER90=.TRUE.) and subsequently
        runs WANNIER90 in library mode (wannier_run).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LWAVE = Quantity(
        type=bool,
        shape=[],
        description='''
        LWAVE determines whether the wavefunctions are written to the WAVECAR file at the
        end of a run.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LWRITE_MMN_AMN = Quantity(
        type=bool,
        shape=[],
        description='''
        LWRITE_MMN_AMN=.TRUE. tells the VASP2WANNIER90 interface to write the
        wannier90.mmn and wannier90.amn files.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LWRITE_UNK = Quantity(
        type=bool,
        shape=[],
        description='''
        LWRITE_UNK decides whether the cell-periodic part of the relevant Bloch functions
        is written.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LWRITE_WANPROJ = Quantity(
        type=bool,
        shape=[],
        description='''
        LWRITE_WANPROJ determines whether the Wannier projection fille WANPROJ is written.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_LZEROZ = Quantity(
        type=bool,
        shape=[],
        description='''
        for LZEROZ=.TRUE. the _z_-component of the spin-spiral magnetisation density will
        be forced to be and to remain zero.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_M_CONSTR = Quantity(
        type=np.dtype(np.float64),
        shape=['3*number_of_atoms'],
        description='''
        M_CONSTR specifies the desired local magnetic moment (size and/or direction) for
        the constrained local moments approach.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_MAGMOM = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        MAGMOM Specifies the initial magnetic moment for each atom, if and only if
        ICHARG=2, or if ICHARG=1 and the CHGCAR file contains no magnetisation density
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_MAXMEM = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAXMEM specifies the maximum memory one MPI rank will attempt to allocate (in
        MByte).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_MAXMIX = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAXMIX specifies the maximum number steps stored in Broyden mixer IMIX=4).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_MDALGO = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MDALGO specifies the molecular dynamics simulation protocol (in case IBRION=0 and
        VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_METAGGA = Quantity(
        type=str,
        shape=[],
        description='''
        selects one of various meta-GGA functionals.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_MINROT = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag MINROT defines the value for which the dimer is rotated only if the
        predicted rotation angle is greater than MINROT (rad.) in the Improved Dimer
        Method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_MIXPRE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MIXPRE specifies the metric in the Broyden mixing scheme(IMIX=4).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_AFILT2_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag sets the filtering parameter for the angular filtering for
        ML_FF_IAFILT2_MB in the machine learning force-field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_CDOUB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag controls the necessity of DFT calculations in the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_CSF = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag sets the threshold for the spilling factor in the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_CSIG = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Parameter used in the automatic determination of threshold for Bayesian error
        estimation in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_CSLOPE = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Parameter used in the automatic determination of threshold for Bayesian error
        estimation in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_CTIFOR = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag sets the threshold for the Bayesian error estimation on the force in the
        machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_EATOM = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atoms'],
        description='''
        Reference total energies of isolated atoms used in the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_IAFILT2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies the type of angular filtering used in the machine learning
        force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_IBROAD1_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag determines how the atomic distribution is broadened for the radial
        descriptor within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_IBROAD2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag determines how the atomic distribution is broadened for the angular
        descriptor within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ICOUPLE_MB = Quantity(
        type=np.dtype(np.int32),
        shape=['number_of_atoms'],
        description='''
        This tag specifies the atoms where the coupling parameter is introduced to
        calculate the chemical potential within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ICUT1_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies the type of cutoff function used for the radial descriptor in
        the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ICUT2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies the type of cutoff function used for the angular descriptor in
        the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_IERR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag selects the error estimation method used in the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_IREG_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies whether the regularization parameters are kept constant or not
        in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ISAMPLE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag controls the sampling in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ISCALE_TOTEN_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies how to scale the energy data for the many-body term in the
        machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ISOAP1_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag defines the type of the SOAP kernel for the radial descriptor in the
        machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ISOAP2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag defines the type of the SOAP kernel for the angular descriptor in the
        machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_ISTART = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag decides if and how calculations are continued from existing data in
        machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_IWEIGHT = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Flag to control the weighting of training data in the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LAFILT2_MB = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag specifies whether angular filtering is applied or not within the machine
        learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LBASIS_DISCARD = Quantity(
        type=bool,
        shape=[],
        description='''
        This variable specifies whether the basis sets are thrown away when its number
        exceeds ML_FF_MB_MB in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LCONF_DISCARD = Quantity(
        type=bool,
        shape=[],
        description='''
        This flag decides whether configurations that do not provide local reference
        configurations are discarded or not in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LCOUPLE_MB = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag specifies whether coupling parameters are used for the calculation of
        chemical potentials is used or not within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LCRITERIA = Quantity(
        type=bool,
        shape=[],
        description='''
        Decides whether the threshold in the learning decision step for the Bayesian error
        estimation is renewed or not in the machine learning force field methods.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LEATOM_MB = Quantity(
        type=bool,
        shape=[],
        description='''
        This term specifies whether the total atomic energy is written out or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LHEAT_MB = Quantity(
        type=bool,
        shape=[],
        description='''
        This flag specifies whether the heat flux is calculated or not in the machine
        learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LMAX2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies the maximum angular momentum quantum number of spherical
        harmonics used to expand atomic distributions within the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LMLFF = Quantity(
        type=bool,
        shape=[],
        description='''
        Main control tag whether to use machine learned force fields or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LMLMB = Quantity(
        type=bool,
        shape=[],
        description='''
        This controls whether the many-body interaction term is included in the machine
        learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LNORM1_MB = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag specifies whether the radial descriptor is normalized (by dividing
        through it's norm) or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_LNORM2_MB = Quantity(
        type=bool,
        shape=[],
        description='''
        This tag specifies whether the angular descriptor is normalized (by dividing
        through it's norm) or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MB_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag sets the maximum number of basis sets describing the many-body
        interactions in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MCONF = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag sets the maximum number of configurations used for training in the
        machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MCONF_NEW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag sets the number of configurations that are stored temporally as
        candidates for the training data in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MHIS = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag sets the number of estimated errors stored in memory to determine the
        threshold for the Bayesian error in the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MRB1_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag sets the number of radial basis sets used to expand the atomic
        distribution for the radial descriptor within the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MRB2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag sets the number of radial basis sets used to expand the atomic
        distribution for the angular descriptor withtin the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MSPL1_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag sets the number of points for the radial grid used in the spline
        interpolation for the radial descriptor within the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_MSPL2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag sets the number of points for the radial grid used in the spline
        interpolation of the angular descriptor within the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NATOM_COUPLED_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag specifies the number of atoms for which a coupling parameter is
        introduced to calculate the chemical potential within the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NDIM_SCALAPACK = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag sets the dimension of the ScaLAPACK grids used in the machine learning
        force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NHYP1_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Polynomial power of the radial kernel.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NHYP2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Polynomial parameter (power) of the SOAP kernel.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NMDINT = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Tag to control the minimum interval to get training samples in the machine
        learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NR1_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag determines the number of grid points used to execute radial integrations
        to compute the radial descriptor within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NR2_MB = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag determines the number of grid points used to execute radial integrations
        to compute the angular descriptor within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_NWRITE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This tag controls part of the output within the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_RCOUPLE_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag specifies the value of the coupling parameter for the calculation of the
        chemical potential within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_RCUT1_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag sets the cutoff radius for the radial descriptor in the machine learning
        force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_RCUT2_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag sets the cutoff radius for the angular descriptor in the machine
        learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_SIGV0_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag sets the initial noise parameter in the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_SIGW0_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag sets the initial precision parameter in the machine learning force field
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_SION1_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag specifies the width of the Gaussian functions used for broadening the
        atomic distributions for the radial descriptor within the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_SION2_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag specifies the width of the Gaussian functions used for broadening the
        atomic distributions of the angular descriptor within the machine learning force
        field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_W1_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag defines the weight for the radial descriptor within the machine learning
        force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_W2_MB = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag defines the weight for the angular descriptor within the machine learning
        force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_WTIFOR = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag sets the weight for the scaling of the forces in the training data within
        the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_WTOTEN = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag sets the weight for the scaling of the total energy in the training data
        within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ML_FF_WTSIF = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This tag sets the weight for the scaling of the total energy in the training data
        within the machine learning force field method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBANDS = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NBANDS determines the actual number of bands in the calculation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBANDSGW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        The flag determines how many QP energies are calculated and updated in GW type
        calculations.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBANDSO = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NBANDSO determines how many occupied orbitals are included in the Casida/BSE
        calculations or time-propagation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBANDSV = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NBANDSV determines how many unoccupied orbitals are included in the Casida/BSE
        calculations or timepropagation.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBLK = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NBLK determines the blocking factor in many BLAS level 3 routines.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBLOCK = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        After NBLOCK ionic steps the pair correlation function and the DOS are calculated
        and the ionic configuration is written to the XDATCAR-file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBMOD = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Controls which bands are used in the calculation of Band decomposed charge
        densities. Check also IBAND and EINT.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NBSEEIG = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NBSEEIG sets the number number of BSE eigenvectors written to the BSEFATBAND
        output file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NCORE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NCORE determines the number of compute cores that work on an individual orbital
        (available as of VASP.5.2.13).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NCRPA_BANDS = Quantity(
        type=np.dtype(np.int32),
        shape=['1..x_vasp_incar_NBANDS'],
        description='''
        Controls which bands are excluded in CRPA. Check also NTARGET_STATES.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NDAV = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NDAV sets the maximum number of iterative steps per bands per RMM-DIIS step
        (IALGO=4X).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NEDOS = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NEDOS specifies number of gridpoints on which the DOS is evaluated
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NELECT = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        NELECT sets the number of electrons.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NELM = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NELM sets the maximum number of electronic SC (selfconsistency) steps which may be
        performed.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NELMDL = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NELMDL specifies the number of non-selfconsistent steps at the beginning.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NELMIN = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NELMIN specifies the minimum number of electronic SCF steps.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NFREE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        depending on IBRION, NFREE specifies the number of remembered steps in the history
        of ionic convergence runs, or the number of ionic displacements in frozen phonon
        calculations.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NGX = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NGX sets the number of grid points in the FFT-grid along the first lattice vector.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NGXF = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NGXF sets the number of grid points in the fine FFT-grid along the first lattice
        vector.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NGY = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NGY sets the number of grid points in the FFT-grid along the second lattice
        vector.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NGYF = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NGYF sets the number of grid points in the fine FFT-grid along the second lattice
        vector.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NGYROMAG = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        NGYROMAG specifies the nuclear gyromagnetic ratios (in MHz, for H<sub>0</sub> = 1
        T) for the atomic types on the POTCAR file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NGZ = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NGZ sets the number of grid points in the FFT-grid along the third lattice vector.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NGZF = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NGZF sets the number of grid points in the fine  FFT-grid along the first lattice
        vector.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NKRED = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NKRED specifies an uniform reduction factor for the **q**-point grid
        representation of the exact exchange potential and the correlation part in GW
        calculations.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NKREDX = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NKREDX specifies a reduction factor for the **q**-point grid representation of the
        exact exchange potential along reciprocal space direction **b**<sub>1</sub>.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NKREDY = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NKREDY specifies a reduction factor for the **q**-point grid representation of the
        exact exchange potential along reciprocal space direction **b**<sub>2</sub>.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NKREDZ = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NKREDZ specifies a reduction factor for the **q**-point grid representation of the
        exact exchange potential along reciprocal space direction **b**<sub>3</sub>.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NLSPLINE = Quantity(
        type=bool,
        shape=[],
        description='''
        construct the PAW projectors in reciprocal space using spline interpolation so
        that they are _k_-differentiable.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NMAXFOCKAE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NMAXFOCKAE and LMAXFOCKAE determine whether the overlap densities in the Fock
        exchange and correlated wave function methods are accurately reconstructed on the
        plane wave grid. This flag generally only applies to the Fock-exchange part as
        well as many-body post DFT methods (GW, RPA, MP2, etc.).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NOMEGA = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NOMEGA specifies the number of (imaginary) frequency and imaginary time grid
        points.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NOMEGAPAR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NOMEGAPAR available as of VASP.6, specifies the number of processor groups sharing
        the same imaginary frequency grid points..
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NOMEGAR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NOMEGAR specifies the number of frequency grid points along the real axis.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NPACO = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NPACO sets the number of slots in the pair-correlation function written to PCDAT.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NPAR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NPAR determines the number of bands that are treated in parallel.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NPPSTR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NPPSTR specifies the number of k-points on the strings in the IGPAR direction.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NSIM = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NSIM sets the number of bands that are optimized simultaneously by the RMM-DIIS
        algorithm.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NSUBSYS = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NSUBSYS defines the atomic subsystems in calculations with multiple Anderson
        thermostats (in case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NSW = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NSW sets the maximum number of ionic steps.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NTARGET_STATES = Quantity(
        type=np.dtype(np.int32),
        shape=['x_vasp_incar_NBANDS'],
        description='''
        Controls which Wannier states are excluded in CRPA. Check also NCRPA_BANDS.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NTAUPAR = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NTAUPAR available as of VASP.6, specifies the number of MPI groups sharing same
        imaginary time grid points. The default value of NTAUPAR is set automatically and
        depends on MAXMEM, the available memory for each rank on one node.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NUPDOWN = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Sets the difference between the number of electrons in the up and down spin
        components.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_NWRITE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag determines how much will be written to the file OUTCAR ('verbosity
        flag').
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ODDONLY = Quantity(
        type=bool,
        shape=[],
        description='''
        ODDONLY=.TRUE. selects a subset of **k**-points for the representation of the Fock
        exchange potential, with _C_<sub>1</sub>=_C_<sub>2</sub>=_C_<sub>3</sub>=1, and
        _n_<sub>1</sub>+_n_<sub>2</sub>+_n_<sub>3</sub> odd.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ODDONLYGW = Quantity(
        type=bool,
        shape=[],
        description='''
        ODDONLYGW allows to avoid the inclusion of the  point in the evaluation of
        response functions (in GW calculations).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_OFIELD_A = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag OFIELD_A sets the desired order parameter *Q*<sub>6</sub> in the
        Interface pinning method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_OFIELD_KAPPA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag OFIELD_KAPPA sets the strength of bias potential in units of 'eV/(unit of
        Q)$^2$' in the Interface pinning method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_OFIELD_Q6_FAR = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag OFIELD_Q6_FAR sets the far fading distance (in Angstroms) for the
        computation of a continuous to *Q*<sub>6</sub> parameter in the Interface pinning
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_OFIELD_Q6_NEAR = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag OFIELD_Q6_NEAR sets the near fading distance (in Angstroms) for the
        computation of a continuous *Q*<sub>6</sub> parameter in the Interface pinning
        method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_OMEGAMAX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OMEGAMAX specifies the maximum frequency for dense part of the frequency grid. For
        CRPA calculations, OMEGAMAX is the frequency point of the interaction.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_OMEGAMIN = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        minimum frequency in the frequency grid.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_OMEGATL = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OMEGATL specifies the maximum frequency for coarse part of the frequency grid.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PARAM1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag PARAM1 determines the first parameter used in the enhancement factor of
        the optPBE-vdW and optB88-vdW functional.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PARAM2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag PARAM2 determines the second parameter used in the enhancement factor of
        the optPBE-vdW and optB88-vdW functional.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PFLAT = Quantity(
        type=bool,
        shape=[],
        description='''
        Control flag for the output of the profiling routines.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PHON_LBOSE = Quantity(
        type=bool,
        shape=[],
        description='''
        This flag determines whether random structures in the Monte-Carlo (MC) sampling
        are created according to Bose-Einstein or Maxwell-Boltzmann statistics.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PHON_LMC = Quantity(
        type=bool,
        shape=[],
        description='''
        This flag controls whether electron-phonon interactions from Monte-Carlo sampling
        are calculated or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PHON_NSTRUCT = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag sets the number of structures for electron-phonon interactions from
        Monte-Carlo (MC) sampling.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PHON_NTLIST = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        This flag sets the number temperatures for that the electron-phonon interactions
        using the ZG configuration is evaluated.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PHON_TLIST = Quantity(
        type=np.dtype(np.int32),
        shape=['x_vasp_incar_PHON_NTLIST'],
        description='''
        This flag provides the list of temperatures for that the electron-phonon
        interactions using the ZG configuration is evaluated.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PLEVEL = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Control flag for the output of the profiling routines.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PMASS = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        PMASS assigns a fictitious mass (in amu) to the lattice degrees-of-freedom in case
        of Parrinello-Rahman dynamics (in case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_POMASS = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        POMASS describes the mass of each atomic sphere in atomic units.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_POTIM = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        POTIM sets the time step (MD) or step width scaling (ionic relaxations).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PREC = Quantity(
        type=str,
        shape=[],
        description='''
        PREC specifies the precision  mode.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PRECFOCK = Quantity(
        type=str,
        shape=[],
        description='''
        PRECFOCK controls the FFT grids used in the exact exchange routines (Hartree-Fock
        and hybrid functionals).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PROUTINE = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Control flag for the output of the profiling routines.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PSTRESS = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        This flag controls whether Pulay corrections are added to the stress tensor or
        not. In molecular dynamics calculations it controls the pressure. The unit of
        PSTRESS is in kB.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PSUBSYS = Quantity(
        type=np.dtype(np.float64),
        shape=['1..3'],
        description='''
        PSUBSYS sets the collision probabilities for the atoms in each atomic subsystem in
        calculations with multiple Anderson thermostats (in case VASP was compiled with
        -Dtbdyn). Note: 0 ≤ PSUBSYS ≤ 1
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_PTHRESHOLD = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Control flag for the output of the profiling routines.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_QMAXFOCKAE = Quantity(
        type=np.dtype(np.float64),
        shape=['1..x_vasp_number_of_k_points'],
        description='''
        The parameter QMAXFOCKAE controls at which wave vectors the local augmentation
        charges are fitted to obtain an accurate charge augmentation on the plane wave
        grid.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_QSPIRAL = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        the QSPIRAL-tag specifies the spin spiral propagation vector.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_QUAD_EFG = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        nuclear quadrupole moment (in millbarn) for the atomic types on the POTCAR file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_RANDOM_SEED = Quantity(
        type=np.dtype(np.int32),
        shape=['x'],
        description='''
        RANDOM_SEED specifies the seed of the random-number-generator (in case VASP was
        compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ROPT = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        ROPT determines how precise the projectors are represented in real space.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_RWIGS = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        RWIGS specifies the Wigner-Seitz radius for each atom type.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SAXIS = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        SAXIS specifies the quantisation axis for noncollinear spins.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SCSRAD = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SCSRAD defines the cutoff radius (in Angs ) used in the calculation of
        $\\tau_{ij}$ within the Tkatchenko-Scheffler method. Self-consistent screening in
        Tkatchenko-Scheffler method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SHAKEMAXITER = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        SHAKEMAXITER specifies the maximum number of iterations in the SHAKE algorithm (in
        case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SHAKETOL = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SHAKETOL specifies the tolerance for the SHAKE algorithm (in case VASP was
        compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SIGMA = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SIGMA specifies the width of the smearing in eV.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SMASS = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SMASS controls the velocities during an ab-initio molecular dynamics run.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SMEARINGS = Quantity(
        type=np.dtype(np.int32),
        shape=['x_vasp_incar_NSW'],
        description='''
        SMEARINGS defines the smearing parameters for ISMEAR=-3 in the calculation of the
        partial occupancies.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SPRING = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        SPRING gives the <i>spring constant</i> between the images as used in the elastic
        band method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_STEP_MAX = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag STEP_MAX defines the trust radius (upper limit) for the optimization step
        (in Angs ) in the Improved Dimer Method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_STEP_SIZE = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The flag STEP_SIZE defines the trial step size for the optimization step (in Angs
        ) in the Improved Dimer Method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SYMPREC = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SYMPREC determines to which accuracy the positions in the POSCAR file must be
        specified (as of VASP.4.4.4).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_SYSTEM = Quantity(
        type=str,
        shape=[],
        description='''
        The 'title string' defined by SYSTEM is for the user only and should help the user
        to identify what he wants to do with this specific input file.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_TEBEG = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TEBEG sets the start temperature for an ab-initio molecular dynamics run
        (IBRION=0) and other routines (e.g. Electron-phonon interactions from Monte-Carlo
        sampling).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_TEEND = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TEEND sets the final temperature for an ab-initio molecular dynamics run
        (IBRION=0; SMASS=−1).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_TIME = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TIME controls the time step for IALGO=5X and for the initial (steepest descent)
        phase of IALGO=4X.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_TSUBSYS = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        TSUBSYS sets the temperatures for the atomic subsystems in calculations with
        multiple Anderson thermostats (in case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VALUE_MAX = Quantity(
        type=np.dtype(np.float64),
        shape=['x'],
        description='''
        VALUE_MAX sets the upper limits for the monitoring of geometric parameters (in
        case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VALUE_MIN = Quantity(
        type=np.dtype(np.float64),
        shape=['x'],
        description='''
        VALUE_MIN sets the lower limits for the monitoring of geometric parameters (in
        case VASP was compiled with -Dtbdyn).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VCUTOFF = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        The parameter VCUTOFF sets the energy cutoff for bare Coulomb matrix elements and
        controls the basis set for the bare Coulomb interaction.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_A1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_A1 defines the damping function parameter  in the DFT-D3 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_A2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_A2 defines the damping function parameter  in the DFT-D3 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_C6 = Quantity(
        type=np.dtype(np.float64),
        shape=['x'],
        description='''
        VDW_C6 defines the  $C_6$ parameters (units: J.nm$^6$mol$^{-1}$ ) for each species
        defined in the POSCAR file within the DFT-D2 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_CNRADIUS = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_CNRADIUS defines the cutoff radius (in Angs ) for the calculation of the
        coordination numbers used in the DFT-D3 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_D = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_D defines the damping parameter _d_ in the DFT-D2method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_R0 = Quantity(
        type=np.dtype(np.float64),
        shape=['number_of_atomic_species'],
        description='''
        VDW_R0 defines the $R_0$ parameters (units: Angs ) for each species defined in the
        POSCAR file within the DFT-D2 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_RADIUS = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_RADIUS defines the cutoff radius (in Angs) for the pair interactions used in
        the DFT-D2 and DFT-D3 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_S6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_S6 defines the global scaling factor _S_6_ in the DFT-D2 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_S8 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_S8 defines the damping function parameter $s_8$ in the DFT-D3 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VDW_SR = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VDW_SR defines the damping function parameter $S_R$ (or scaling factor) in the
        DFT-D2 and DFT-D3 method.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_VOSKOWN = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Determines whether Vosko-Wilk-Nusair interpolation is used or not.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_WC = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WC specifies the weight factor for each step in Broyden mixing scheme (IMIX=4).
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_WEIMIN = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WEIMIN specifies the maximum weight for a band to be considered empty.
        ''',
        categories=[x_vasp_incar_param])

    x_vasp_incar_ZVAL = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZVAL describes the valency of each atomic sphere.
        ''',
        categories=[x_vasp_incar_param])
