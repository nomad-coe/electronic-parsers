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


class x_cpmd_section_input_ATOMS_ATOMIC_CHARGES(MSection):
    '''
    Changes the default charge (0) of the atoms for the initial guess to the values read
    from the next line. One value per atomic species has to be given.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_ATOMIC_CHARGES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ATOMIC_CHARGES.
        ''')

    x_cpmd_input_ATOMS_ATOMIC_CHARGES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ATOMIC_CHARGES.
        ''')


class x_cpmd_section_input_ATOMS_CHANGE_BONDS(MSection):
    '''
    The buildup of the empirical Hessian can be affected. You can either add or delete
    bonds. The number of changed bonds is read from the next line. This line is followed
    by the description of the bonds. The format is  {\\sl \\{ ATOM1 \\ \\ ATOM2 \\ \\ FLAG\\} }.
    \\hfill  {\\sl ATOM1} and {\\sl ATOM2} are the numbers of the atoms involved in the bond.
    A {\\sl FLAG} of $-1$ causes a bond to be deleted and a {\\sl FLAG} of $1$ a bond to be
    added. \\hfill Example:  {\\tt \\begin{tabular}{ccc} \\multicolumn{3}{l}{\\bf CHANGE BONDS}
    2 &   &          1 & 2 & +1       6 & 8 & -1 \\end{tabular} }
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_CHANGE_BONDS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CHANGE_BONDS.
        ''')

    x_cpmd_input_ATOMS_CHANGE_BONDS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CHANGE_BONDS.
        ''')


class x_cpmd_section_input_ATOMS_CONFINEMENT_POTENTIAL(MSection):
    '''
    The use of this label activates a spherical gaussian confinement potential in the
    calculation of the form factor of pseudopotentials. In the next line(s) two parameters
    for each atomic species must be supplied: the amplitude $\\alpha$ and the cut off
    radius $r_c$. The gaussian spherical amplitude is computed as $A=\\pi ^{3/2}r_c^3\\cdot
    \\alpha$ and the gaussian confinement potential reads \\begin{equation*} V({\\bf G}) =
    \\sum_{\\bf G} A \\cdot |{\\bf G}|\\cdot e^{-G^2r_c^2/4} \\label{pconf} \\end{equation*}
    being {\\bf G} the G-vectors, although in practice the loop runs only on the G-shells
    $G=|{\\bf G}|$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_CONFINEMENT_POTENTIAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CONFINEMENT_POTENTIAL.
        ''')

    x_cpmd_input_ATOMS_CONFINEMENT_POTENTIAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CONFINEMENT_POTENTIAL.
        ''')


class x_cpmd_section_input_ATOMS_DUMMY_ATOMS(MSection):
    '''
    The definition of dummy atoms follows this keyword. Three different kinds of dummy
    atoms are implemented. Type 1 is fixed in space, type 2 lies at the arithmetic mean,
    type 3 at the center of mass of the coordinates of real atoms.  % For types 2, 3 and 4
    you can also have a %      negative weight (NOTE: works only for restraints). The
    first line contains the total number of dummy atoms. The following lines start with
    the type label {\\bf TYPE1, TYPE2, TYPE3, TYPE4}. For type 1 dummy atoms the label is
    followed by the Cartesian coordinates.  For type 2 and type 3 dummy atoms the first
    number specifies the total number of atoms involved in the definition of the dummy
    atom. Then the number of these atoms has to be specified on the same line. A negative
    number of atoms stands for all atoms. For type 4, the dummy atom is defined as a
    weigthed average of coordinates of real atoms with user-supplied weights. This feature
    is useful e.~g. in constrained dynamics, because allows to modify positions and
    weights of dummy atoms according to some relevant quantity such as forces on selected
    atoms. % A negative atom index means that a negative weight is assigned % to this atom
    (works only with restraints)  Example:   {\\tt \\begin{tabular}{llll}
    \\multicolumn{4}{l}{\\bf DUMMY ATOMS } 3           &     &     &           {\\bf TYPE1} &
    0.0 & 0.0 & 0.0       {\\bf TYPE2} & 2   & 1   & 4         {\\bf TYPE3} & -1
    \\end{tabular} }  Note: Indices of dummy atoms always start with total-number-of-atoms
    plus 1. In the case of a Gromos-QM/MM interface simulations with dummy hydrogen atoms
    for capping, it is total-number-of-atoms plus number-of-dummy-hydrogens plus 1
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_DUMMY_ATOMS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DUMMY_ATOMS.
        ''')

    x_cpmd_input_ATOMS_DUMMY_ATOMS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DUMMY_ATOMS.
        ''')


class x_cpmd_section_input_ATOMS_GENERATE_COORDINATES(MSection):
    '''
    The number of generator atoms for each species are read from the next line.  These
    atoms are used together with the point group information to generate all other atomic
    positions. The input still has to have entries for all atoms but their coordinates are
    overwritten. Also the total number of atoms per species has to be correct.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_GENERATE_COORDINATES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword GENERATE_COORDINATES.
        ''')

    x_cpmd_input_ATOMS_GENERATE_COORDINATES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword GENERATE_COORDINATES.
        ''')


class x_cpmd_section_input_ATOMS_ISOTOPE(MSection):
    '''
    Changes the default masses of the atoms.

    This keyword has to be followed by {\\sl NSP} lines (number of atom types). In each
    line the new mass (in a.m.u.) of the respective species has to be specified (in order
    of their definition).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_ISOTOPE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ISOTOPE.
        ''')

    x_cpmd_input_ATOMS_ISOTOPE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ISOTOPE.
        ''')


class x_cpmd_section_input_ATOMS_MOVIE_TYPE(MSection):
    '''
    Assign special movie atom types to the species. The types are read from the next line.
    Values from 0 to 5 were allowed in the original MOVIE format.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_MOVIE_TYPE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MOVIE_TYPE.
        ''')

    x_cpmd_input_ATOMS_MOVIE_TYPE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MOVIE_TYPE.
        ''')


class x_cpmd_section_input_ATOMS(MSection):
    '''
    Atoms and pseudopotentials and related parameters (\\textbf{required}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_ATOMS_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section ATOMS even without a keyword.
        ''')

    x_cpmd_section_input_ATOMS_ATOMIC_CHARGES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS_ATOMIC_CHARGES'),
        repeats=True)

    x_cpmd_section_input_ATOMS_CHANGE_BONDS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS_CHANGE_BONDS'),
        repeats=True)

    x_cpmd_section_input_ATOMS_CONFINEMENT_POTENTIAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS_CONFINEMENT_POTENTIAL'),
        repeats=True)

    x_cpmd_section_input_ATOMS_DUMMY_ATOMS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS_DUMMY_ATOMS'),
        repeats=True)

    x_cpmd_section_input_ATOMS_GENERATE_COORDINATES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS_GENERATE_COORDINATES'),
        repeats=True)

    x_cpmd_section_input_ATOMS_ISOTOPE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS_ISOTOPE'),
        repeats=True)

    x_cpmd_section_input_ATOMS_MOVIE_TYPE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS_MOVIE_TYPE'),
        repeats=True)


class x_cpmd_section_input_BASIS(MSection):
    '''
    Atomic basis sets for properties or initial guess
    '''

    m_def = Section(validate=False)

    x_cpmd_input_BASIS_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section BASIS even without a keyword.
        ''')


class x_cpmd_section_input_CLASSIC_FREEZE_QUANTUM(MSection):
    '''
    Freeze the quantum atoms and performs a classical MD on the others (in QMMM mode only
    !).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CLASSIC_FREEZE_QUANTUM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FREEZE_QUANTUM.
        ''')

    x_cpmd_input_CLASSIC_FREEZE_QUANTUM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FREEZE_QUANTUM.
        ''')


class x_cpmd_section_input_CLASSIC_FULL_TRAJECTORY(MSection):
    '''
    Not documented
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CLASSIC_FULL_TRAJECTORY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FULL_TRAJECTORY.
        ''')

    x_cpmd_input_CLASSIC_FULL_TRAJECTORY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FULL_TRAJECTORY.
        ''')


class x_cpmd_section_input_CLASSIC_PRINT_COORDINATES(MSection):
    '''
    Not documented
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CLASSIC_PRINT_COORDINATES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRINT_COORDINATES.
        ''')

    x_cpmd_input_CLASSIC_PRINT_COORDINATES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRINT_COORDINATES.
        ''')


class x_cpmd_section_input_CLASSIC_PRINT_FF(MSection):
    '''
    Not documented
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CLASSIC_PRINT_FF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRINT_FF.
        ''')

    x_cpmd_input_CLASSIC_PRINT_FF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRINT_FF.
        ''')


class x_cpmd_section_input_CLASSIC(MSection):
    '''
    Simple classical code interface
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CLASSIC_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section CLASSIC even without a keyword.
        ''')

    x_cpmd_section_input_CLASSIC_FREEZE_QUANTUM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CLASSIC_FREEZE_QUANTUM'),
        repeats=True)

    x_cpmd_section_input_CLASSIC_FULL_TRAJECTORY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CLASSIC_FULL_TRAJECTORY'),
        repeats=True)

    x_cpmd_section_input_CLASSIC_PRINT_COORDINATES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CLASSIC_PRINT_COORDINATES'),
        repeats=True)

    x_cpmd_section_input_CLASSIC_PRINT_FF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CLASSIC_PRINT_FF'),
        repeats=True)


class x_cpmd_section_input_CPMD_ALEXANDER_MIXING(MSection):
    '''
    Mixing used during optimization of geometry or molecular dynamics. Parameter read in
    the next line.

    \\textbf{Default} value is \\defaultvalue{0.9}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ALEXANDER_MIXING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ALEXANDER_MIXING.
        ''')

    x_cpmd_input_CPMD_ALEXANDER_MIXING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ALEXANDER_MIXING.
        ''')


class x_cpmd_section_input_CPMD_ALLTOALL(MSection):
    '''
    Perform the matrix transpose (AllToAll communication) in the 3D FFT using
    single/double precision numbers. Default is to use double precision numbers.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ALLTOALL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ALLTOALL.
        ''')

    x_cpmd_input_CPMD_ALLTOALL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ALLTOALL.
        ''')


class x_cpmd_section_input_CPMD_ANDERSON_MIXING(MSection):
    '''
    Anderson mixing for the electronic density during self-consistent iterations. In the
    next line the parameter (between 0 and 1) for the Anderson mixing is read.

    \\textbf{Default} is \\defaultvalue{0.2}.

    With the additional option $N=n$ a mixing parameter can be specified for different
    threshold densities. $n$ different thresholds can be set. The program reads $n$ lines,
    each with a threshold density and an Anderson mixing parameter.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ANDERSON_MIXING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ANDERSON_MIXING.
        ''')

    x_cpmd_input_CPMD_ANDERSON_MIXING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ANDERSON_MIXING.
        ''')


class x_cpmd_section_input_CPMD_ANNEALING(MSection):
    '''
    Scale the ionic, electronic, or cell velocities every time step. The scaling factor is
    read from the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ANNEALING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ANNEALING.
        ''')

    x_cpmd_input_CPMD_ANNEALING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ANNEALING.
        ''')


class x_cpmd_section_input_CPMD_BENCHMARK(MSection):
    '''
    This keyword is used to control some special features related to benchmarks. If you
    want to know more, have a look in the source code.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_BENCHMARK_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BENCHMARK.
        ''')

    x_cpmd_input_CPMD_BENCHMARK_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BENCHMARK.
        ''')


class x_cpmd_section_input_CPMD_BERENDSEN(MSection):
    '''
    Use a simple Berendsen-type thermostat\\cite{Berendsen84} to control the respective
    temperature of ions, electrons, or cell. The target temperature and time constant
    $\\tau$ (in a.u.) are read from the next line.  These thermostats are a gentler
    alternative to the \\refkeyword{TEMPCONTROL} mechanism to thermalize a system. For
    production runs, please use the corresponding \\refkeyword{NOSE} or
    \\refkeyword{LANGEVIN} thermostats, as the Berendsen scheme does not represent any
    defined statistical mechanical ensemble.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_BERENDSEN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BERENDSEN.
        ''')

    x_cpmd_input_CPMD_BERENDSEN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BERENDSEN.
        ''')


class x_cpmd_section_input_CPMD_BFGS(MSection):
    '''
    Use a quasi-Newton method for optimization of the ionic positions. The approximated
    Hessian is updated using the Broyden-Fletcher-Goldfarb-Shano
    procedure~\\cite{Fletcher80}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_BFGS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BFGS.
        ''')

    x_cpmd_input_CPMD_BFGS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BFGS.
        ''')


class x_cpmd_section_input_CPMD_BLOCKSIZE_STATES(MSection):
    '''
    Parameter read in from next line. {\\sl NSTBLK}  Defines the minimal number of states
    used per processor in the distributed linear algebra calculations. {\\bf Default} is to
    equally distribute states over all processors.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_BLOCKSIZE_STATES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BLOCKSIZE_STATES.
        ''')

    x_cpmd_input_CPMD_BLOCKSIZE_STATES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BLOCKSIZE_STATES.
        ''')


class x_cpmd_section_input_CPMD_BOGOLIUBOV_CORRECTION(MSection):
    '''
    Computes the Bogoliubov correction for the energy of the Trotter approximation or not.

    {\\bf Default} is {\\bf no Bogoliubov correction}.

    The keyword has to appear after \\refkeyword{FREE ENERGY FUNCTIONAL}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_BOGOLIUBOV_CORRECTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BOGOLIUBOV_CORRECTION.
        ''')

    x_cpmd_input_CPMD_BOGOLIUBOV_CORRECTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BOGOLIUBOV_CORRECTION.
        ''')


class x_cpmd_section_input_CPMD_BOX_WALLS(MSection):
    '''
    The thickness parameter for soft, reflecting QM-box walls is read from the next line.
    This keyword allows to reverse the momentum of the particles (${\\bf p}_I \\rightarrow
    -{\\bf p}_I$) when they reach the walls of the simulation supercell in the case in
    which no periodic boundary conditions are applied. Specifically, in the unidimensional
    surface-like case, molecules departing from the surface are reflected back along the
    direction orthogonal to the surface, whereas in the bidimensional polymer-like case,
    they are reflected back in the two dimensons orthogonal to the "polymer" axis.
    Warning: This procedure, although keeping your particles inside the cell, affect the
    momentum conservation.  This feature is {\\bf disabled by default}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_BOX_WALLS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BOX_WALLS.
        ''')

    x_cpmd_input_CPMD_BOX_WALLS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BOX_WALLS.
        ''')


class x_cpmd_section_input_CPMD_BROYDEN_MIXING(MSection):
    '''
    Parameters read in from next line. {\\sl BROYMIX, ECUTBROY, W02BROY, NFRBROY, IBRESET,
    KERMIX}  These mean: \\hfill\\smallskip {\\sl BROYMIX}: \\hfill\\begin{minipage}[t]{10cm}
    Initial mixing, e.g. $0.1$; \\textbf{default} value is \\defaultvalue{0.5}
    \\end{minipage}  {\\sl ECUTBROY:} \\hfill\\begin{minipage}[t]{10cm} Cutoff for Broyden
    mixing. \\defaultvalue{DUAL*ECUT} is the best choice and the \\textbf{default}
    \\end{minipage}  {\\sl W02BROY:} \\hfill\\begin{minipage}[t]{10cm} $w_0^2$ parameter of
    Johnson~\\cite{Johnson88}. \\textbf{Default} \\defaultvalue{0.01} \\end{minipage}  {\\sl
    NFRBROY:} \\hfill\\begin{minipage}[t]{10cm} Number of Anderson mixing steps done before
    Broyden mixing. \\textbf{Default} is \\defaultvalue{0} \\end{minipage}  {\\sl IBRESET:}
    \\hfill\\begin{minipage}[t]{10cm} Number of Broyden vectors. $5$ is usually a good value
    and the default. \\end{minipage}  {\\sl KERMIX:} \\hfill\\begin{minipage}[t]{10cm} Kerker
    mixing according to the original deinition of Ref.~\\cite{Kerker}. By default the
    mixing parameter is set to 0. \\end{minipage}  You can also specify some parameters
    with the following syntax: \\textbf{[BROYMIX=}\\textsl{BROYMIX}\\textbf{]}
    \\textbf{[ECUTBROY=}\\textsl{ECUTBROY}\\textbf{]}
    \\textbf{[W02BROY=}\\textsl{W02BROY}\\textbf{]}
    \\textbf{[NFRBROY=}\\textsl{NFRBROY}\\textbf{]}
    \\textbf{[IBRESET=}\\textsl{IBRESET}\\textbf{]}
    \\textbf{[KERMIX=}\\textsl{KERMIX}\\textbf{]} Finally, you can use the keyword {\\bf
    DEFAULT} to use the default values.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_BROYDEN_MIXING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BROYDEN_MIXING.
        ''')

    x_cpmd_input_CPMD_BROYDEN_MIXING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BROYDEN_MIXING.
        ''')


class x_cpmd_section_input_CPMD_CAYLEY(MSection):
    '''
    Used to propagate the Kohn-Sham orbitals in \\refkeyword{MOLECULAR DYNAMICS} EH and
    \\refkeyword{PROPAGATION SPECTRA}. At present is the only propagation scheme availabe.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CAYLEY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CAYLEY.
        ''')

    x_cpmd_input_CPMD_CAYLEY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CAYLEY.
        ''')


class x_cpmd_section_input_CPMD_CDFT(MSection):
    '''
    The main switch for constrained DFT. Parameters $N_\\text{c}$, $V_\\text{init}$, and
    MAXSTEP are read from the next line. {\\bf NEWTON}, {\\bf DEKKER} (\\defaultvalue{off})
    are switches to enable either the Newton or the Dekker optimisation scheme for the
    constraint. If neither of those are set a simple gradient scheme is used. {\\bf SPIN}
    (\\defaultvalue{off}) if activated the constraint will act on the spin density instead
    of the charge density. This may help against excessive spin contamination. {\\bf ALL}
    (\\defaultvalue{off}) activates dual spin and charge constraint, all inputs for
    $N_\\text{c}$ and $V_\\text{init}$ have to be given twice (first for charge then for
    spin) {\\bf PCGFI} (\\defaultvalue{off}) instructs CPMD to do PCG for the first V
    optimisation cycle regardles of the choice of optimiser. {\\bf RESWF}
    (\\defaultvalue{off}) if activated this switch re-initialises the wavefunction after
    each $V$ optimisation step. This is useful if the wavefunction convergence between the
    optimisation steps is slow. Usage in conjunction with \\refkeyword{INITIALIZE
    WAVEFUNCTION} RANDOM may help. {\\bf NOCCOR} (\\defaultvalue{off}) if activated this
    switch turns off cutoff correction for the forces. {\\bf HDA} (\\defaultvalue{off}) if
    activated this switch turns on the calculation of the transition matrix element
    between the constrained states given by $N_\\text{c}$ and $\\hat{N}_\\text{c}$ which is
    then read from the second line. For this keyword to take effect the
    \\refkeyword{OPTIMIZE WAVEFUNCTION} option has to be activated. Sub-options of {\\bf
    HDA} {\\bf AUTO} (\\defaultvalue{off}) if activated this switch lets CPMD choose the
    constraint values for the transition matrix calculation. $N_\\text{c}$ is chosen from
    the initial charge distribution and $\\hat{N}_\\text{c}=-N_\\text{c}$. It might be a good
    idea to use \\refkeyword{INITIALIZE WAVEFUNCTION} ATOMS and \\refkeyword{ATOMIC CHARGES}
    (\\&ATOM section) so that CPMD initialises the wavefunction with the desired pseudo
    wavefunction. {\\bf PHIOUT} (\\defaultvalue{off}) if activated this switch tells CPMD to
    write out the overlap matrices $\\Phi_\\text{AA},\\Phi_\\text{BB},\\Phi_\\text{AB},$ and
    $\\Phi_\\text{BA}$ to the file PHI\\_MAT. {\\bf PROJECT} (\\defaultvalue{off}) if activated
    this switch lets CPMD read in two reference states from RESTART.REF1 and RESTART.REF2
    after the actual HDA calculation in order to project the two constrained states on
    them and thus calculate the diabatic transition matrix element in an orthogonalised
    ``dressed'' basis. If CDFT is activated the program writes the current $V$ value to
    CDFT\\_RESTART everytime the RESTART file is written.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CDFT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CDFT.
        ''')

    x_cpmd_input_CPMD_CDFT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CDFT.
        ''')


class x_cpmd_section_input_CPMD_CENTER_MOLECULE(MSection):
    '''
    The center of mass is moved/not moved to the center of the computational box in a
    calculation with the cluster option. This is only done when the coordinates are read
    from the input file.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CENTER_MOLECULE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CENTER_MOLECULE.
        ''')

    x_cpmd_input_CPMD_CENTER_MOLECULE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CENTER_MOLECULE.
        ''')


class x_cpmd_section_input_CPMD_CHECK_MEMORY(MSection):
    '''
    Check sanity of all dynamically allocated arrays whenever a change in the allocation
    is done. By default memory is checked only at break points.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CHECK_MEMORY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CHECK_MEMORY.
        ''')

    x_cpmd_input_CPMD_CHECK_MEMORY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CHECK_MEMORY.
        ''')


class x_cpmd_section_input_CPMD_CLASSTRESS(MSection):
    '''
    Not documented.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CLASSTRESS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CLASSTRESS.
        ''')

    x_cpmd_input_CPMD_CLASSTRESS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CLASSTRESS.
        ''')


class x_cpmd_section_input_CPMD_CMASS(MSection):
    '''
    The fictitious mass of the cell in atomic units is read from the next line.
    \\textbf{Default} value is \\defaultvalue{200}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CMASS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CMASS.
        ''')

    x_cpmd_input_CPMD_CMASS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CMASS.
        ''')


class x_cpmd_section_input_CPMD_COMBINE_SYSTEMS(MSection):
    '''
    Read in two wavefunctions from RESTART.R1 and RESTART.R2 and combine them into
    RESTART.1 which can then be used in an FODFT calculations. The option NONORTH disables
    orthogonalisation of the combined WF's. Parameters NTOT1, NTOT2, NSUP1, NSUP2 are read
    from the next line. NTOT1/NTOT2 total number of electrons in state 1/2 (mandatory).
    NSUP1/NSUP2 number of alpha electrons in state 1/2 (only LSD). If the option REFLECT
    is given a fifth parameter (CM\\_DIR) is read and the WF given in RESTART.R2 will be
    either mirrored through the centre of the box (CM\\_DIR=0), mirrored through the
    central yz-plane of the box (CM\\_DIR=1) or if CM\\_DIR=4 mirrored through the central
    yz-plane and translated in x direction by CM\\_DR (sixth parameter to be read). If the
    option SAB is set, write out the overlap matrix element between orbitals K and L.
    Parameters K and L are read from the next line. After combining the wavefunctions CPMD
    will exit. For this option to work the RESTART option and \\refkeyword{OPTIMIZE
    WAVEFUNCTION} have to be activated.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_COMBINE_SYSTEMS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword COMBINE_SYSTEMS.
        ''')

    x_cpmd_input_CPMD_COMBINE_SYSTEMS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword COMBINE_SYSTEMS.
        ''')


class x_cpmd_section_input_CPMD_COMPRESS(MSection):
    '''
    Write the wavefunctions with nn bytes precision to the restart file.  Possible choices
    are \\texttt{WRITE32}, \\texttt{WRITE16}, \\texttt{WRITE8} and \\texttt{WRITEAO}.
    \\texttt{WRITE32} corresponds to the compress option in older versions.
    \\texttt{WRITEAO} stores the wavefunction as a projection on atomic basis sets. The
    atomic basis set can be specified in the section \\&BASIS \\ldots \\&END. If this input
    section is missing a default basis from Slater type orbitals is constructed. See
    section~\\ref{input:basis} for more details.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_COMPRESS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword COMPRESS.
        ''')

    x_cpmd_input_CPMD_COMPRESS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword COMPRESS.
        ''')


class x_cpmd_section_input_CPMD_CONJUGATE_GRADIENTS(MSection):
    '''
    For the electrons, the keyword is equivalent to \\refkeyword{PCG}. The
    \\texttt{NOPRECONDITIONING} parameter only applies for electrons. For the ions the
    conjugate gradients scheme is used to relax the atomic positions.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CONJUGATE_GRADIENTS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CONJUGATE_GRADIENTS.
        ''')

    x_cpmd_input_CPMD_CONJUGATE_GRADIENTS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CONJUGATE_GRADIENTS.
        ''')


class x_cpmd_section_input_CPMD_CONVERGENCE(MSection):
    '''
    The adaptive convergence criteria for the wavefunction during a geometry optimization
    are specified. For more informations, see~\\cite{LSCAL}. The ratio {\\sl TOLAD} between
    the smallest maximum component of the nuclear gradient reached so far and the maximum
    allowed component of the electronic {\\bf gradient} is specified with {\\bf CONVERGENCE
    ADAPT}. This criterion is switched off once the value {\\sl TOLOG} given with {\\bf
    CONVERGENCE ORBITALS} is reached. By default, the adaptive gradient criterion is not
    active. A reasonable value for the parameter {\\sl TOLAD} is 0.02.

    If the parameter {\\sl TOLENE} is given with {\\bf CONVERGENCE ENERGY}, in addition to
    the gradient criterion for the wavefunction, the energy change between two
    wavefunction optimization cycles must be smaller than the energy change of the last
    accepted geometry change multiplied by {\\sl TOLENE} for the wavefunction to be
    considered converged. By default, the adaptive energy criterion is not active. It is
    particularly useful for {\\bf transition state search} with P-RFO, where the trust
    radius is based on the quality of energy prediction. A reasonable value for {\\sl
    TOLENE} is 0.05.

    To save CPU time, the gradient on the ions is only calculated if the wavefunction is
    almost converged. The parameter {\\sl TOLFOR} given with {\\bf CONVERGENCE CALFOR} is
    the ratio between the convergence criteria for the wavefunction and the criteria
    whether the gradient on the ions is to be calculated. \\textbf{Default} value for {\\sl
    TOLFOR} is \\defaultvalue{3.0}.

    If the wavefunction is very slowly converging during a geometry optimization, a small
    nuclear displacement can help. The parameter {\\sl NSTCNV} is given with {\\bf
    CONVERGENCE RELAX}. Every {\\sl NSTCNV} wavefunction optimization cycles, the
    convergence criteria for the wavefunction are relaxed by a factor of two. A geometry
    optimization step resets the criteria to the unrelaxed values. By default, the
    criteria for wavefunction convergence are never relaxed.

    When starting a geometry optimization from an unconverged wavefunction, the nuclear
    gradient and therefore the adaptive tolerance of the electronic gradient is not known.
    To avoid the {\\bf full convergence} criterion to be applied at the beginning, a
    convergence criterion for the wavefunction of the initial geometry can be supplied
    with {\\bf CONVERGENCE INITIAL}. By default, the initial convergence criterion is equal
    to the full convergence criterion.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CONVERGENCE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CONVERGENCE.
        ''')

    x_cpmd_input_CPMD_CONVERGENCE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CONVERGENCE.
        ''')


class x_cpmd_section_input_CPMD_CZONES(MSection):
    '''
    Activates convergence zones for the wavefunction during the \\refkeyword{CDFT}
    constraint minimisation. If SET is set the parameters CZONE1, CZONE2, and CZONE3 are
    read from the next line and CZLIMIT1 and CZLIMIT2 from the line after. CZONE1
    \\defaultvalue{$10^{-3}$},CZONE2 \\defaultvalue{$10^{-4}$},CZONE3
    \\defaultvalue{$10^{-5}$} $\\in \\mathbb{R}_+$ are the orbital convergences in zones 1-3,
    respectively. CZLIMIT1 \\defaultvalue{0.3}, CZLIMIT2 \\defaultvalue{0.1} $\\in
    \\mathbb{R}_+$ define the boundaries between zone 1-2 and 2-3, respectively.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_CZONES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CZONES.
        ''')

    x_cpmd_input_CPMD_CZONES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CZONES.
        ''')


class x_cpmd_section_input_CPMD_DAMPING(MSection):
    '''
    Add a damping factor $f_{damp}(x) = - \\gamma \\cdot v(x)$ to the ionic, electronic, or
    cell forces in every time step. The scaling factor $\\gamma$ is read from the next
    line. Useful values depend on the employed masses are generally in the range $5.0 \\to
    50.0$.  Damping can be used as a more efficient alternative to \\refkeyword{ANNEALING}
    for wavefunction, geometry or cell optimization (and particularly combinations
    thereof) of systems where the faster methods (e.g. \\refkeyword{ODIIS},
    \\refkeyword{PCG}, \\refkeyword{LBFGS}, \\refkeyword{GDIIS}) fail to converge or may
    converge to the wrong state.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DAMPING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DAMPING.
        ''')

    x_cpmd_input_CPMD_DAMPING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DAMPING.
        ''')


class x_cpmd_section_input_CPMD_DAVIDSON_DIAGONALIZATION(MSection):
    '''
    Use Davidson diagonalization scheme.\\cite{davidson75}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DAVIDSON_DIAGONALIZATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DAVIDSON_DIAGONALIZATION.
        ''')

    x_cpmd_input_CPMD_DAVIDSON_DIAGONALIZATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DAVIDSON_DIAGONALIZATION.
        ''')


class x_cpmd_section_input_CPMD_DAVIDSON_PARAMETER(MSection):
    '''
    This keyword controls the Davidson diagonalization routine used to determine the Kohn-
    Sham energies.

    The maximum number of additional vectors to construct the Davidson matrix, the
    convergence criterion and the maximum number of steps are read from the next line.

    \\textbf{Defaults} are \\defaultvalue{10$^{-5}$} and the same number as states to be
    optimized. If the system has 20 occupied states and you ask for 5 unoccupied states,
    the default number of additional vectors is 25. By using less than 25 some memory can
    be saved but convergence might be somewhat slower.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DAVIDSON_PARAMETER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DAVIDSON_PARAMETER.
        ''')

    x_cpmd_input_CPMD_DAVIDSON_PARAMETER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DAVIDSON_PARAMETER.
        ''')


class x_cpmd_section_input_CPMD_DEBUG_CODE(MSection):
    '''
    Very verbose output concerning subroutine calls for debugging purpose.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DEBUG_CODE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DEBUG_CODE.
        ''')

    x_cpmd_input_CPMD_DEBUG_CODE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DEBUG_CODE.
        ''')


class x_cpmd_section_input_CPMD_DEBUG_FILEOPEN(MSection):
    '''
    Very verbose output concerning opening files for debugging purpose.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DEBUG_FILEOPEN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DEBUG_FILEOPEN.
        ''')

    x_cpmd_input_CPMD_DEBUG_FILEOPEN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DEBUG_FILEOPEN.
        ''')


class x_cpmd_section_input_CPMD_DEBUG_FORCES(MSection):
    '''
    Very verbose output concerning the calculation of each contribution to the forces for
    debugging purpose.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DEBUG_FORCES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DEBUG_FORCES.
        ''')

    x_cpmd_input_CPMD_DEBUG_FORCES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DEBUG_FORCES.
        ''')


class x_cpmd_section_input_CPMD_DEBUG_MEMORY(MSection):
    '''
    Very verbose output concerning memory for debugging purpose.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DEBUG_MEMORY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DEBUG_MEMORY.
        ''')

    x_cpmd_input_CPMD_DEBUG_MEMORY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DEBUG_MEMORY.
        ''')


class x_cpmd_section_input_CPMD_DEBUG_NOACC(MSection):
    '''
    Do not read/write accumulator information from/to the \\refkeyword{RESTART} file. This
    avoids putting timing information to the restart and makes restart files identical for
    otherwise identical runs.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DEBUG_NOACC_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DEBUG_NOACC.
        ''')

    x_cpmd_input_CPMD_DEBUG_NOACC_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DEBUG_NOACC.
        ''')


class x_cpmd_section_input_CPMD_DIIS_MIXING(MSection):
    '''
    Use the direct inversion iterative scheme to mix density.

    Read in the next line the number of previous densities (NRDIIS) for the mixing
    (however not useful).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DIIS_MIXING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DIIS_MIXING.
        ''')

    x_cpmd_input_CPMD_DIIS_MIXING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DIIS_MIXING.
        ''')


class x_cpmd_section_input_CPMD_DIPOLE_DYNAMICS(MSection):
    '''
    Calculate the dipole moment~\\cite{vdb_berry,resta} every {\\sl NSTEP} iteration in MD.

    {\\sl NSTEP} is read from the next line if the keyword SAMPLE is present.

    {\\bf Default} is {\\bf every} time step.

    The keyword {\\bf Wannier} allows the calculation of optimally localized Wannier
    functions\\cite{Marzari97,PSil99,berghold}. The procedure used is equivalent (for
    single k-point) to Boys localization.  The produced output is IONS+CENTERS.xyz,
    IONS+CENTERS, DIPOLE, WANNIER\\_CENTER and WANNIER\\_DOS. The localization procedure is
    controlled by the following keywords.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DIPOLE_DYNAMICS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DIPOLE_DYNAMICS.
        ''')

    x_cpmd_input_CPMD_DIPOLE_DYNAMICS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DIPOLE_DYNAMICS.
        ''')


class x_cpmd_section_input_CPMD_DISTRIBUTE_FNL(MSection):
    '''
    The array \\texttt{FNL} is distributed in parallel runs.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DISTRIBUTE_FNL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DISTRIBUTE_FNL.
        ''')

    x_cpmd_input_CPMD_DISTRIBUTE_FNL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DISTRIBUTE_FNL.
        ''')


class x_cpmd_section_input_CPMD_DISTRIBUTED_LINALG(MSection):
    '''
    Perform linear algebra calculations using distributed memory algorithms. Setting this
    option ON will also enable (distributed) initialization from atomic wavefunctions
    using a parallel Lanczos algorithm \\cite{distrib.lanczos.07}. Note that distributed
    initialization is not available with {\\bf KPOINTS} calculations. In this case,
    initialization from atomic wavefunctions will involve replicated calculations.  When
    setting {\\bf LINALG ON} the keyword  \\refkeyword{BLOCKSIZE STATES} becomes relevant
    (see entry). The number of \\refkeyword{BLOCKSIZE STATES} must be an {\\bf exact
    divisor} of the number of  \\refkeyword{STATES}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_DISTRIBUTED_LINALG_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DISTRIBUTED_LINALG.
        ''')

    x_cpmd_input_CPMD_DISTRIBUTED_LINALG_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DISTRIBUTED_LINALG.
        ''')


class x_cpmd_section_input_CPMD_ELECTRONIC_SPECTRA(MSection):
    '''
    Perform a TDDFT calculation~\\cite{tddft_all,tddft_pw} to determine the electronic
    spectra. See below under \\referto{sec:ElectronicSpectra}{Electronic Spectra} and under
    the other keywords for the input sections \\referto{inputkw:linres}{\\&LINRES} and
    \\referto{inputkw:tddft}{\\&TDDFT} for further options.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ELECTRONIC_SPECTRA_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ELECTRONIC_SPECTRA.
        ''')

    x_cpmd_input_CPMD_ELECTRONIC_SPECTRA_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ELECTRONIC_SPECTRA.
        ''')


class x_cpmd_section_input_CPMD_ELECTROSTATIC_POTENTIAL(MSection):
    '''
    Store the electrostatic potential on file. The resulting file is written in platform
    specific binary format. You can use the cpmd2cube tool to convert it into a Gaussian
    cube file for visualization. Note that this flag automatically activates the
    \\refkeyword{RHOOUT} flag as well.  With the optional keyword {\\bf SAMPLE} the file
    will be written every {\\em nrhoout} steps during an MD trajectory. The corresponding
    time step number will be appended to the filename.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ELECTROSTATIC_POTENTIAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ELECTROSTATIC_POTENTIAL.
        ''')

    x_cpmd_input_CPMD_ELECTROSTATIC_POTENTIAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ELECTROSTATIC_POTENTIAL.
        ''')


class x_cpmd_section_input_CPMD_ELF(MSection):
    '''
    Store the total valence density and the valence electron localization function
    ELF~\\cite{Becke90,silsav,marx-savin-97,homeofelf} on files. The default smoothing
    parameters for ELF can be changed optionally when specifying in addition the PARAMETER
    keyword. Then the two parameters ``elfcut'' and ``elfeps'' are read from the next
    line. The particular form of ELF that is implemented is defined in the header of the
    subroutine elf.F.  Note 1: it is a {\\em very} good idea to increase the planewave
    cutoff and then specify ``elfcut''~$=0.0$ and ``elfeps''~$=0.0$ if you want to obtain
    a smooth ELF for a given nuclear configuration. In the case of a spin--polarized (i.e.
    spin unrestricted) DFT calculation (see keyword \\refkeyword{LSD}) in addition the spin
    --polarized average of ELF as well as the separate $\\alpha$-- and $\\beta$--orbital
    parts are written to the files LSD\\_ELF, ELF\\_ALPHA and ELF\\_BETA, respectively; see
    Ref.~\\cite{Kohut96} for definitions and further infos.  Note 2: ELF does not make much
    sense when using Vanderbilt's ultra-soft pseudopotentials!
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ELF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ELF.
        ''')

    x_cpmd_input_CPMD_ELF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ELF.
        ''')


class x_cpmd_section_input_CPMD_EMASS(MSection):
    '''
    The fictitious electron mass in atomic units is read from the next line.  {\\bf
    Default} is {\\bf 400 a.u.}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_EMASS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EMASS.
        ''')

    x_cpmd_input_CPMD_EMASS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EMASS.
        ''')


class x_cpmd_section_input_CPMD_ENERGYBANDS(MSection):
    '''
    Write the band energies (eigenvalues) for k points in the file ENERGYBANDS.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ENERGYBANDS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ENERGYBANDS.
        ''')

    x_cpmd_input_CPMD_ENERGYBANDS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ENERGYBANDS.
        ''')


class x_cpmd_section_input_CPMD_EXTERNAL_POTENTIAL(MSection):
    '''
    Read an external potential from file. With ADD specified, its effects is added to the
    forces acting on the ions.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_EXTERNAL_POTENTIAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXTERNAL_POTENTIAL.
        ''')

    x_cpmd_input_CPMD_EXTERNAL_POTENTIAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXTERNAL_POTENTIAL.
        ''')


class x_cpmd_section_input_CPMD_EXTRAPOLATE_CONSTRAINT(MSection):
    '''
    In a CDFT MD run extrapolate the next value for $V$ using a Lagrange polynomial. The
    order $k$ of the polynomial is read from the next line. { \\bf Default} is
    \\defaultvalue{k=5}, but it pays off to use the orderfinder.py python script on the
    ENERGIES file of a former run to estimate the optimal extrapolation order
    $k_\\text{opt}$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_EXTRAPOLATE_CONSTRAINT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXTRAPOLATE_CONSTRAINT.
        ''')

    x_cpmd_input_CPMD_EXTRAPOLATE_CONSTRAINT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXTRAPOLATE_CONSTRAINT.
        ''')


class x_cpmd_section_input_CPMD_EXTRAPOLATE_WFN(MSection):
    '''
    Read the number of wavefunctions to retain from the next line.  These wavefunctions
    are used to extrapolate the initial guess wavefunction in Born-Oppenheimer MD. This
    can help to speed up BO-MD runs significantly by reducing the number of wavefunction
    optimization steps needed through two effects: the initial guess wavefunction is much
    improved and also you do not need to converge as tightly to conserve energy. BO-MD
    without needs CONVERGENCE ORBITALS to be set to 1.0e-7 or smaller to maintain good
    energy conservation. With the additional keyword {\\bf STORE} the wavefunction history
    is also written to restart files. See \\refkeyword{RESTART} for how to read it back.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_EXTRAPOLATE_WFN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXTRAPOLATE_WFN.
        ''')

    x_cpmd_input_CPMD_EXTRAPOLATE_WFN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXTRAPOLATE_WFN.
        ''')


class x_cpmd_section_input_CPMD_FFTW_WISDOM(MSection):
    '''
    Controls the use of the ``wisdom'' facility when using FFTW or compatible libraries.
    When enabled, CPMD will switch to using the ``measure'' mode, which enables searching
    for additional runtime optimizations of the FFT. The resulting parameters will be
    written to a file called {\\sl FFTW\\_WISDOM} and re-read on subsequent runs. The
    parameters in the file are machine specific and when moving a job to a different
    machine, the file should be deleted.  The use of fftw wisdom incurs additional
    overhead and thus may lead to slower execution. It is recommended to stick with the
    default settings unless you know what you are doing.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_FFTW_WISDOM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FFTW_WISDOM.
        ''')

    x_cpmd_input_CPMD_FFTW_WISDOM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FFTW_WISDOM.
        ''')


class x_cpmd_section_input_CPMD_FILE_FUSION(MSection):
    '''
    Reads in two separate \\refkeyword{RESTART} files for ground state and
    \\refkeyword{ROKS} excited state and writes them into a single restart file. Required
    to start \\refkeyword{SURFACE HOPPING} calculations.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_FILE_FUSION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FILE_FUSION.
        ''')

    x_cpmd_input_CPMD_FILE_FUSION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FILE_FUSION.
        ''')


class x_cpmd_section_input_CPMD_FILEPATH(MSection):
    '''
    The path to the files written by CPMD (RESTART.x, MOVIE, ENERGIES, DENSITY.x etc.) is
    read from the next line. This overwrites the value given in the environment variable
    {\\bf CPMD\\_FILEPATH}. {\\bf Default} is the {\\bf current directory}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_FILEPATH_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FILEPATH.
        ''')

    x_cpmd_input_CPMD_FILEPATH_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FILEPATH.
        ''')


class x_cpmd_section_input_CPMD_FINITE_DIFFERENCES(MSection):
    '''
    The step length in a finite difference run for vibrational frequencies ({VIBRATIONAL
    ANALYSIS} keywords) is read from the next line. With the keywords {\\bf COORD=}{\\sl
    coord\\_fdiff(1..3)} and {\\bf RADIUS=}{\\sl radius} put in the same line as the step
    length, you can specify a sphere in order to calculate the finite differences only for
    the atoms inside it. The sphere is centered on the position {\\sl coord\\_fdiff(1..3)}
    with a radius {\\sl radius} (useful for a point defect).  \\textbf{NOTE:} The the step
    length for the finite difference is \\textbf{always} in Bohr (default is 1.0d-2 a.u.).
    The (optional) coordinates of the center and the radius are read in either Angstrom or
    Bohr, depending on whether the \\refkeyword{ANGSTROM} keyword is specified or not.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_FINITE_DIFFERENCES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FINITE_DIFFERENCES.
        ''')

    x_cpmd_input_CPMD_FINITE_DIFFERENCES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FINITE_DIFFERENCES.
        ''')


class x_cpmd_section_input_CPMD_FIXRHO_UPWFN(MSection):
    '''
    Wavefunctions optimization with the method of direct inversion of the iterative
    subspace (DIIS), performed without updating the charge density at each step. When the
    orbital energy gradients are below the given tolerance or when the maximum number of
    iterations is reached, the KS energies and the occupation numbers are calculated, the
    density is updated, and a new wavefunction optimization is started. The variations of
    the density coefficients are used as convergence criterium. The default electron
    temperature is 1000 K and 4 unoccupied states are added. Implemented also for
    k-points. Only one sub-option is allowed per line and the respective parameter is read
    from the next line. The parameters mean: \\hfill\\smallskip{\\sl VECT}:
    \\hfill\\begin{minipage}[t]{10cm} The number of DIIS vectors is read from the next line.
    (ODIIS with 4 vectors is the default). \\end{minipage}\\hfill  {\\sl LOOP:}
    \\hfill\\begin{minipage}[t]{10cm} the minimum and maximum number of DIIS iterations per
    each wfn optimization is read from the following line. Default values are 4 and 20.
    \\end{minipage}\\hfill  {\\sl WFTOL:} \\hfill\\begin{minipage}[t]{10cm} The convergence
    tolerance for the wfn optimization during the ODIIS is read from the following line.
    The default value is $10^{-7}$. The program adjusts this criterion automatically,
    depending on the convergence status of the density. As the density improves (when the
    density updates become smaller), also the wavefunction convergence criterion is set to
    its final value. \\end{minipage}\\hfill
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_FIXRHO_UPWFN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FIXRHO_UPWFN.
        ''')

    x_cpmd_input_CPMD_FIXRHO_UPWFN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FIXRHO_UPWFN.
        ''')


class x_cpmd_section_input_CPMD_FORCEMATCH(MSection):
    '''
    Activates the QM/MM force matching procedure. This keywords requires the presence of a
    \\&QMMM ... \\&END section with a correspoding \\refkeyword{FORCEMATCH ... END
    FORCEMATCH} block. See sections~\\ref{sec:qmmm} and~\\ref{sec:forcematch-desc} for more
    details.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_FORCEMATCH_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FORCEMATCH.
        ''')

    x_cpmd_input_CPMD_FORCEMATCH_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FORCEMATCH.
        ''')


class x_cpmd_section_input_CPMD_FREE_ENERGY_FUNCTIONAL(MSection):
    '''
    Calculates the electronic free energy using free energy density
    functional~\\cite{Alavi94,PSil,mbaops} from DFT at finite temperature. This option
    needs additional keywords (free energy keywords). By {\\bf default} we use {\\bf Lanczos
    diagonalization} with {\\bf Trotter factorization} and {\\bf Bogoliubov correction}. If
    the number of states is not specified, use $N_{electrons}/2+4$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_FREE_ENERGY_FUNCTIONAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FREE_ENERGY_FUNCTIONAL.
        ''')

    x_cpmd_input_CPMD_FREE_ENERGY_FUNCTIONAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FREE_ENERGY_FUNCTIONAL.
        ''')


class x_cpmd_section_input_CPMD_GDIIS(MSection):
    '''
    Use the method of direct inversion in the iterative subspace combined with a quasi-
    Newton method (using BFGS) for optimization of the ionic
    positions~\\cite{Csaszar84}.%\\cite{Fischer} The number of DIIS vectors is read from the
    next line. GDIIS with {\\bf 5 vectors} is the {\\bf default} method in optimization
    runs.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_GDIIS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword GDIIS.
        ''')

    x_cpmd_input_CPMD_GDIIS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword GDIIS.
        ''')


class x_cpmd_section_input_CPMD_GSHELL(MSection):
    '''
    Write a file {\\bf GSHELL} with the information on the plane waves for further use in
    S(q) calculations.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_GSHELL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword GSHELL.
        ''')

    x_cpmd_input_CPMD_GSHELL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword GSHELL.
        ''')


class x_cpmd_section_input_CPMD_HAMILTONIAN_CUTOFF(MSection):
    '''
    The lower cutoff for the diagonal approximation to the Kohn-Sham
    matrix~\\cite{Tuckerman94} is read from the next line. {\\bf Default} is {\\bf 0.5}
    atomic units. For variable cell dynamics only the kinetic energy as calculated for the
    reference cell is used.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_HAMILTONIAN_CUTOFF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HAMILTONIAN_CUTOFF.
        ''')

    x_cpmd_input_CPMD_HAMILTONIAN_CUTOFF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HAMILTONIAN_CUTOFF.
        ''')


class x_cpmd_section_input_CPMD_HARMONIC_REFERENCE_SYSTEM(MSection):
    '''
    Switches harmonic reference system integration~\\cite{Tuckerman94} on/off.  The number
    of shells included in the analytic integration is controlled with the keyword
    \\refkeyword{HAMILTONIAN CUTOFF}.  By {\\bf default} this option is switched {\\bf off}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_HARMONIC_REFERENCE_SYSTEM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HARMONIC_REFERENCE_SYSTEM.
        ''')

    x_cpmd_input_CPMD_HARMONIC_REFERENCE_SYSTEM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HARMONIC_REFERENCE_SYSTEM.
        ''')


class x_cpmd_section_input_CPMD_HESSCORE(MSection):
    '''
    Calculates the partial Hessian after relaxation of the enviroment, equivalent to {\\sl
    NSMAXP=0} ({\\bf PRFO NSMAXP}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_HESSCORE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HESSCORE.
        ''')

    x_cpmd_input_CPMD_HESSCORE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HESSCORE.
        ''')


class x_cpmd_section_input_CPMD_HESSIAN(MSection):
    '''
    The initial approximate {\\bf Hessian} for a {\\bf geometry optimization} is constructed
    using empirical rules with the DISCO~\\cite{Fischer92} or Schlegel's~\\cite{Schlegel84}
    parametrization or simply a unit matrix is used.  If the option {\\bf PARTIAL} is used
    the initial approximate Hessian for a geometry optimization is constructed from a
    block matrix formed of the parametrized Hessian and the partial Hessian (of the
    reaction core). If the reaction core spans the entire system, its Hessian is simply
    copied.  The keywords \\refkeyword{RESTART} PHESS are required.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_HESSIAN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HESSIAN.
        ''')

    x_cpmd_input_CPMD_HESSIAN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HESSIAN.
        ''')


class x_cpmd_section_input_CPMD_INITIALIZE_WAVEFUNCTION(MSection):
    '''
    The initial guess for wavefunction optimization are either random functions or
    functions derived from the atomic pseudo-wavefunctions. For INITIALIZE WAVEFUNCTION
    ATOMS PRIMITIVE, CPMD will use the occupation information given in the \\&BASIS section
    in order to construct a minimum spin multiplicity (i.e. doublet or singlet) initial
    wavefunction from the pseudo atomic orbitals. This option may be helpful to avoid
    excessive spin contamination in CDFT calculations (together with an already good
    initial guess for $V$) as it allows a strict initial localisation of excess spins on
    any atom species.

    {\\bf Default} is to use the {\\bf atomic pseudo-wavefunctions}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_INITIALIZE_WAVEFUNCTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword INITIALIZE_WAVEFUNCTION.
        ''')

    x_cpmd_input_CPMD_INITIALIZE_WAVEFUNCTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword INITIALIZE_WAVEFUNCTION.
        ''')


class x_cpmd_section_input_CPMD_INTERFACE(MSection):
    '''
    Use CPMD together with a classical molecular dynamics code. CPMD and the classical MD
    code are run simultaneously and communicate via a file based protocol. See the file
    egointer.F for more details. This needs a specially adapted version of the respective
    classical MD code. So far, there is an interface\\cite{egoqmmm,gmxqmmm} to the MD
    programs ego\\cite{ego1,ego2} and Gromacs\\cite{gmx3}.  When using the suboption
    PCGFIRST the code will use \\refkeyword{PCG}~MINIMIZE on the very first wavefunction
    optimization and then switch back to DIIS.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_INTERFACE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword INTERFACE.
        ''')

    x_cpmd_input_CPMD_INTERFACE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword INTERFACE.
        ''')


class x_cpmd_section_input_CPMD_INTFILE(MSection):
    '''
    This keyword means {\\it Interface File} and allows to select a special file name in
    the reading and writing stages. The file name (max 40 characters) must be supplied in
    the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_INTFILE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword INTFILE.
        ''')

    x_cpmd_input_CPMD_INTFILE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword INTFILE.
        ''')


class x_cpmd_section_input_CPMD_ISOLATED_MOLECULE(MSection):
    '''
    Calculate the ionic temperature assuming that the system consists of an isolated
    molecule or cluster.

    Note:

    This keyword affects exclusively the determination of the number of dynamical degrees
    of freedom.

    This keyword does \\textbf{not} activate the 'cluster option' \\refkeyword{SYMMETRY} 0,
    but it is activated if SYMMETRY 0 is used \\textbf{unless} the keyword
    \\refkeyword{QMMM} is set as well.

    It allows studying an isolated molecule or cluster within periodic boundary
    conditions.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ISOLATED_MOLECULE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ISOLATED_MOLECULE.
        ''')

    x_cpmd_input_CPMD_ISOLATED_MOLECULE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ISOLATED_MOLECULE.
        ''')


class x_cpmd_section_input_CPMD_KSHAM(MSection):
    '''
    Write out the Kohn-Sham Hamiltonian Matrix in the orbital basis given in the RESTART
    file to KS\\_HAM. For this option to work the \\refkeyword{RESTART} option and
    \\refkeyword{OPTIMIZE WAVEFUNCTION} have to be activated. This option is useful for
    fragment orbital DFT (FODFT) calculations. Orbitals for the output of the FO-DFT
    matrix element can be given with the option {\\bf STATE}, then indics of the two
    orbitals are read from the next line. {\\bf ROUT} controls printing of involved
    orbitals.\\\\ {\\bf MATRIX} instructs CPMD to read a transformation matrix from the file
    LOWDIN\\_A to transform the KS-Hamiltonian to the non-orthogonal orbital basis
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_KSHAM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword KSHAM.
        ''')

    x_cpmd_input_CPMD_KSHAM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword KSHAM.
        ''')


class x_cpmd_section_input_CPMD_LANCZOS_DIAGONALIZATION(MSection):
    '''
    Use {\\bf Lanczos diagonalization} scheme.  \\textbf{Default} with \\textbf{free energy
    functional}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_LANCZOS_DIAGONALIZATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LANCZOS_DIAGONALIZATION.
        ''')

    x_cpmd_input_CPMD_LANCZOS_DIAGONALIZATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LANCZOS_DIAGONALIZATION.
        ''')


class x_cpmd_section_input_CPMD_LANCZOS_PARAMETER(MSection):
    '''
    Give four parameters for Lanczos diagonalization in the next line: \\begin{itemize}
    \\item Maximal number of Lanczos iterations (50 is enough), \\item Maximal number for
    the Krylov sub-space (8 best value), \\item Blocking dimension ( $\\leq NSTATE$, best in
    range 20-100) If you put a negative or zero number, this parameter is fixed by the
    program in function of the number of states ($(n+1)/(int(n/100+1))$). \\item Tolerance
    for the accuracy of wavefunctions ($10^{-8}$ otherwise $10^{-12}$ with Trotter
    approximation) \\end{itemize} If n is specified, read $n-1$ lines after the first one,
    containing a threshold density and a tolerance. See the hints section
    \\ref{hints:lanczos} for more information.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_LANCZOS_PARAMETER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LANCZOS_PARAMETER.
        ''')

    x_cpmd_input_CPMD_LANCZOS_PARAMETER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LANCZOS_PARAMETER.
        ''')


class x_cpmd_section_input_CPMD_LANGEVIN(MSection):
    '''
    Use a (generalized) Langevin equation to thermostat the simulation\\cite{Ceriotti10}.
    By default, the component of the noise parallel to the center of mass velocity is
    removed at each step of the thermostat. Removal can be disabled by the option {\\sl
    MOVECM}. \\\\\\smallskip {\\sl CUSTOM:} \\hfill\\begin{minipage}[t]{10cm} The {\\bf number of
    additional momenta} of the generalized Langevin equation {\\sl NS} is read from the
    next line. The drift matrix (dimension $(NS+1)\\times(NS+1)$) is read from the file
    \\texttt{GLE-A}, which must be in the same directory in which the program is run.
    Optionally, the static covariance for the GLE dynamics can be provided in the file
    \\texttt{GLE-C}, so as to generate {\\bf non-canonical sampling}. A library of GLE
    parameters can be downloaded from
    \\htref{http://gle4md.berlios.de/}{http://gle4md.berlios.de/} \\end{minipage}
    \\smallskip\\\\ A few {\\bf presets} are provided, and are activated by the keywords: {\\sl
    WHITE:} \\hfill\\begin{minipage}[t]{10cm} A simple {\\bf white-noise} Langevin dynamics
    is used. The optimally-sampled frequency {\\sl W0} (in cm$^{-1}$) is read from the next
    line. Note that use of {\\sl LANGEVIN WHITE} in conjunction with {\\sl MOLECULAR
    DYNAMICS CPMD} will most likely cause a large drift of the electronic temperature.
    \\end{minipage} {\\sl OPTIMAL:} \\hfill\\begin{minipage}[t]{10cm} An {\\bf optimal-
    sampling} generalized Langevin dynamics is used. The frequencies in the range from
    $10^{-4}${\\sl W0} up to {\\sl W0} will be sampled efficiently. Note that use of {\\sl
    LANGEVIN OPTIMAL} in conjunction with {\\sl MOLECULAR DYNAMICS CPMD} will cause a large
    drift of the electronic temperature. This option is suggested for use in Born-
    Oppenheimer MD. \\end{minipage} {\\sl CPMD:} \\hfill\\begin{minipage}[t]{10cm} A
    generalized Langevin dynamics is used which is designed to work in conjunction with
    Car-Parrinello MD. The highest ionic frequency {\\sl W0} (in cm$^{-1}$) is read from
    the next line. Ionic frequencies down to $10^{-4}${\\sl W0} will be sampled
    efficiently, but not as much as for the {\\sl OPTIMAL} keyword. \\end{minipage}  {\\sl
    SMART:} \\hfill\\begin{minipage}[t]{10cm} A generalized Langevin dynamics that aims to
    be as efficient as possible on the slowest time scale accessible to a typical ab
    initio simulation. In practice, vibrations with a time scale which is about 10000 time
    steps will be sampled optimally, and faster modes will be sampled as efficiently as
    possible without disturbing slower modes. The highest ionic frequency {\\sl W0} (in
    cm$^{-1}$) is read from the next line. Will be about 50\\%{} more efficient than {\\sl
    OPTIMAL} for slow modes, but less efficient for fast vibrations. Use only with Born-
    Oppenheimer dynamics. \\end{minipage}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_LANGEVIN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LANGEVIN.
        ''')

    x_cpmd_input_CPMD_LANGEVIN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LANGEVIN.
        ''')


class x_cpmd_section_input_CPMD_LBFGS(MSection):
    '''
    Use the limited-memory BFGS method (L-BFGS) for linear scaling {\\bf optimization} of
    the {\\bf ionic positions}. For more informations, see~\\cite{LSCAL}. The information
    about the Hessian for the quasi-Newton method employed is derived from the history of
    the optimization~\\cite{LSCAL,Liu89}. Only one sub-option is allowed per line and the
    respective parameter is read from the next line. The parameters mean: \\hfill\\smallskip
    {\\sl NREM}: \\hfill\\begin{minipage}[t]{10cm} {\\bf Number} of {\\bf ionic gradients} and
    {\\bf displacements remembered} to approximate the Hessian. The default is either 40 or
    the number of ionic degrees of freedom, whichever is smaller. Values greater the
    number of degrees of freedom are not advisable. \\end{minipage} {\\sl NTRUST:}
    \\hfill\\begin{minipage}[t]{10cm} {\\sl NTRUST=1} switches from a trust radius algorithm
    to a {\\bf line search} algorithm. The default value of 0 ({\\bf trust radius}) is
    recommended. \\end{minipage} {\\sl NRESTT:} \\hfill\\begin{minipage}[t]{10cm} {\\sl
    NRESTT$>$0} demands a {\\bf periodic reset} of the optimizer every {\\sl NRESTT} steps.
    Default is 0 (no periodic reset). This option makes only sense if the ionic gradient
    is not accurate. \\end{minipage} {\\sl TRUSTR:} \\hfill\\begin{minipage}[t]{10cm} Maximum
    and initial {\\bf trust radius}. Default is 0.5 atomic units. \\end{minipage} It can be
    useful to combine these keywords with the keywords \\refkeyword{PRFO},
    \\refkeyword{CONVERGENCE} ADAPT, \\refkeyword{RESTART} LSSTAT, \\refkeyword{PRINT} LSCAL
    ON and others.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_LBFGS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LBFGS.
        ''')

    x_cpmd_input_CPMD_LBFGS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LBFGS.
        ''')


class x_cpmd_section_input_CPMD_LINEAR_RESPONSE(MSection):
    '''
    A perturbation theory calculation is done, according to the (required) further input
    in the \\&RESP section. In the latter, one of the possible perturbation types (PHONONS,
    LANCZOS, RAMAN, FUKUI, KPERT, NMR, EPR, see section \\ref{sec:resp-section}) can be
    chosen, accompanied by further options.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_LINEAR_RESPONSE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LINEAR_RESPONSE.
        ''')

    x_cpmd_input_CPMD_LINEAR_RESPONSE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LINEAR_RESPONSE.
        ''')


class x_cpmd_section_input_CPMD_LOCAL_SPIN_DENSITY(MSection):
    '''
    Use the local spin density approximation. {\\bf Warning:} Not all functionals are
    implemented for this option.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_LOCAL_SPIN_DENSITY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LOCAL_SPIN_DENSITY.
        ''')

    x_cpmd_input_CPMD_LOCAL_SPIN_DENSITY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LOCAL_SPIN_DENSITY.
        ''')


class x_cpmd_section_input_CPMD_LSD(MSection):
    '''
    Use the local spin density approximation. {\\bf Warning:} Not all functionals are
    implemented for this option.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_LSD_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LSD.
        ''')

    x_cpmd_input_CPMD_LSD_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LSD.
        ''')


class x_cpmd_section_input_CPMD_MAXITER(MSection):
    '''
    The maximum number of iteration steps for the self-consistency of wavefunctions.
    Recommended use instead of \\refkeyword{MAXSTEP} for pure wavefunction optimisation.
    The value is read from the next line.  {\\bf Default} is {\\bf 10000} steps.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MAXITER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MAXITER.
        ''')

    x_cpmd_input_CPMD_MAXITER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MAXITER.
        ''')


class x_cpmd_section_input_CPMD_MAXRUNTIME(MSection):
    '''
    The maximum RUN TIME (ELAPSED TIME) in seconds to be used is read from the next line.
    The calculation will stop after the given amount of time. {\\bf Default} is no limit.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MAXRUNTIME_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MAXRUNTIME.
        ''')

    x_cpmd_input_CPMD_MAXRUNTIME_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MAXRUNTIME.
        ''')


class x_cpmd_section_input_CPMD_MAXSTEP(MSection):
    '''
    The maximum number of steps for geometry optimization or molecular dynamics to be
    performed. In the case of pure wavefunction optimisation, this keyword may be used
    instead of \\refkeyword{MAXITER}. The value is read from the next line.  {\\bf Default}
    is {\\bf 10000} steps.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MAXSTEP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MAXSTEP.
        ''')

    x_cpmd_input_CPMD_MAXSTEP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MAXSTEP.
        ''')


class x_cpmd_section_input_CPMD_MEMORY(MSection):
    '''
    Using {\\bf BIG}, the structure factors for the density cutoff are only calculated once
    and stored for reuse.  This option allows for considerable time savings in connection
    with Vanderbilt pseudopotentials. {\\bf Default} is ({\\bf SMALL}) to {\\bf recalculate}
    them whenever needed.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MEMORY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MEMORY.
        ''')

    x_cpmd_input_CPMD_MEMORY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MEMORY.
        ''')


class x_cpmd_section_input_CPMD_MIRROR(MSection):
    '''
    Write the input file to the output.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MIRROR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MIRROR.
        ''')

    x_cpmd_input_CPMD_MIRROR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MIRROR.
        ''')


class x_cpmd_section_input_CPMD_MIXDIIS(MSection):
    '''
    Not documented
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MIXDIIS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MIXDIIS.
        ''')

    x_cpmd_input_CPMD_MIXDIIS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MIXDIIS.
        ''')


class x_cpmd_section_input_CPMD_MIXSD(MSection):
    '''
    Not documented
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MIXSD_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MIXSD.
        ''')

    x_cpmd_input_CPMD_MIXSD_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MIXSD.
        ''')


class x_cpmd_section_input_CPMD_MODIFIED_GOEDECKER(MSection):
    '''
    To be used in combination with \\refkeyword{LOW SPIN EXCITATION}~\\textbf{ROKS}.
    Calculation of the off-diagonal Kohn-Sham matrix elements $F_{AB}$ and $F_{BA}$ (with
    A, B: ROKS-SOMOs) is performed according to a modified Goedecker-Umrigar scheme (
    $F_{AB} := (1-\\lambda _{AB})F_{AB} + \\lambda _{AB} F_{BA}$ and $F_{BA} := (1-\\lambda
    _{BA})F_{BA} + \\lambda _{BA} F_{AB}$ ). Default values are $\\lambda _{AB}=-0.5$ and
    $\\lambda _{BA}=0.5$. see Ref.~\\cite{GrimmJCP2003}.  With the optional keyword
    \\textbf{PARAMETERS}: $\\lambda _{AB}$ and $\\lambda _{BA}$ are read from the next line.
    Can be used to avoid unphysical rotation of the SOMOs. Always check the orbitals!  See
    also \\ref{hints:roks}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MODIFIED_GOEDECKER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MODIFIED_GOEDECKER.
        ''')

    x_cpmd_input_CPMD_MODIFIED_GOEDECKER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MODIFIED_GOEDECKER.
        ''')


class x_cpmd_section_input_CPMD_MOLECULAR_DYNAMICS(MSection):
    '''
    Perform a molecular dynamics (MD) run. {\\bf CP} stands for a Car-Parrinello type MD.
    With the option {\\bf BO} a Born-Oppenheimer MD is performed where the wavefunction is
    reconverged after each MD-step. {\\bf EH} specifies Ehrenfest type dynamics according
    to which the Kohn-Sham orbitals are propagated in time (real electronic dynamics
    coupled to the nuclear dynamics). In this case the time step has to be decreased
    accordingly due to the small mass of the electrons (typical values between 0.01 and
    0.1 au). If you use EH dynamics and additional input section {\\&PTDDFT} need to be
    specified. You need to start the dynamics with well converged KS orbitals from the
    RESTART file (before starting the EH dynamics do an optimization of the wavefunction
    with a convergence of {1.D-8} or {1.D-9}, if possibe. An additional file called
    "wavefunctions" is produced, which containes the complex KS orbitals needed for the
    restart of the EH dynamics (see restart options in {\\&PTDDFT}). Typical (minimal)
    input \\&CPMD and \\&PTDDFT sections to be used with EH dynmiacs \\&CPMD  MOLECULAR
    DYNAMICS EH  RESTART WAVEFUNCTION COORDINATES LATEST  CAYLEY  RUNGE-KUTTA  TIMESTEP
    0.01  MAXSTEP  10000  \\&END  \\&PTDDFT  ACCURACY  1.0D-8  RESTART  2  \\&END  The
    keywords CAYLEY and RUNGE-KUTTA specifies the algorithms used for the propagation of
    the KS orbitals (are the default and recommended options). {\\bf CLASSICAL } means that
    a MD that includes classical atoms is performed.  If {\\bf FILE} is set, then the
    trajectory is reread from a file instead of being calculated. This is useful for
    performing analysis on a previous trajectory. Can be used in conjonction with the
    standard MD options like DIPOLE DYNAMICS and WANNIER; some other features like LINEAR
    RESPONSE are also enabled. The trajectory is read from a file named TRAJSAVED (usually
    a copy of a previous TRAJECTORY file), or TRAJSAVED.xyz if {\\bf XYZ} is set. {\\bf
    NSKIP} and {\\bf NSAMPLE} control the selection of frames read: the frame read at step
    ISTEP is NSKIP+ISTEP*NSAMPLE.  {\\bf Default} is {\\bf CP}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MOLECULAR_DYNAMICS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MOLECULAR_DYNAMICS.
        ''')

    x_cpmd_input_CPMD_MOLECULAR_DYNAMICS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MOLECULAR_DYNAMICS.
        ''')


class x_cpmd_section_input_CPMD_MOVERHO(MSection):
    '''
    Mixing used during optimization of geometry or molecular dynamics. Use atomic or
    pseudowavefunctions to project wavefunctions in order to calculate the new ones with
    movement of atoms. Read in the next line the parameter (typically 0.2).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MOVERHO_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MOVERHO.
        ''')

    x_cpmd_input_CPMD_MOVERHO_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MOVERHO.
        ''')


class x_cpmd_section_input_CPMD_MOVIE(MSection):
    '''
    Write the atomic coordinates without applying periodic boundary conditions in MOVIE
    format every {\\sl IMOVIE} time steps on file {\\em MOVIE}. {\\sl  IMOVIE} is read from
    the next line.  {\\bf Default} is {\\bf not} to write a movie file.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_MOVIE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MOVIE.
        ''')

    x_cpmd_input_CPMD_MOVIE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MOVIE.
        ''')


class x_cpmd_section_input_CPMD_NOGEOCHECK(MSection):
    '''
    Default is to check all atomic distances and stop the program if the smallest
    disctance is below 0.5 Bohr. This keyword requests not to perform the check.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_NOGEOCHECK_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NOGEOCHECK.
        ''')

    x_cpmd_input_CPMD_NOGEOCHECK_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NOGEOCHECK.
        ''')


class x_cpmd_section_input_CPMD_NONORTHOGONAL_ORBITALS(MSection):
    '''
    Use the norm constraint method~\\cite{HutterIP} for molecular dynamics or
    non\\-orthogonal orbitals in an optimization run. On the next line the limit of the off
    diagonal elements of the overlap matrix is defined. {\\bf Warning:} Adding or deleting
    this option during a MD run needs special care.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_NONORTHOGONAL_ORBITALS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NONORTHOGONAL_ORBITALS.
        ''')

    x_cpmd_input_CPMD_NONORTHOGONAL_ORBITALS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NONORTHOGONAL_ORBITALS.
        ''')


class x_cpmd_section_input_CPMD_NOSE_PARAMETERS(MSection):
    '''
    The {\\bf parameters} controlling the {\\bf Nos\\'e thermostats}~\\cite{Nose84,Hoover85}
    are read in the following order from the next line: The {\\bf length} of the
    Nos\\'e-Hoover chain for the {\\bf ions}, the {\\bf length} of the Nos\\'e-Hoover chain
    for the {\\bf electrons}, the {\\bf length} of the Nos\\'e-Hoover chain for the {\\bf cell
    parameters}. (The respective {\\bf default} values are {\\bf 4}.) The {\\bf
    multiplication factor} (NEDOF0, a real number) for the number of {\\bf electronic}
    degrees of freedom. The used degrees of freedom (NEDOF) are defined as
    $NEDOF=NEDOF0*X$ If NEDOF0 is a negative number X is the true number of DOFs, if it's
    a positive number, X is the number of electronic states ({\\bf default} for NEDOF0 is
    {\\bf 6}).  The order of the {\\bf Suzuki/Yoshida integrator} ({\\bf default} is {\\bf 7},
    choices are 3, 5, 7, 9, 15, 25, 125 and 625), and the {\\bf decomposition ratio} of the
    time step ({\\bf default} is {\\bf 1}). If this keyword is omitted, the defaults are
    used.  {\\bf If the keyword is used \\underline{all} parameters have to be specified.}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_NOSE_PARAMETERS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NOSE_PARAMETERS.
        ''')

    x_cpmd_input_CPMD_NOSE_PARAMETERS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NOSE_PARAMETERS.
        ''')


class x_cpmd_section_input_CPMD_NOSE(MSection):
    '''
    {\\bf Nos\\'e-Hoover chains}~\\cite{Nose84,Hoover85} for the {\\bf ions}, {\\bf electrons},
    or {\\bf cell parameters} are used. The {\\bf target temperature} in Kelvin and the {\\bf
    thermostat frequency} in $cm^{-1}$, respectively the {\\bf fictitious kinetic energy}
    in atomic units and the {\\bf thermostat frequency} in $cm^{-1}$ are read from the next
    line. Two files NOSE\\_ENERGY and NOSE\\_TRAJEC are written at each step containing the
    Nos\\'e-Hoover kinetic, potential and total energies along the dynamics (NOSE\\_ENERGY)
    and the Nos\\'e-Hoover variables and their velocities (NOSE\\_TRAJEC); these are useful
    in a wealth of post-processing calculations such as, e.~g. heat transfer
    problems\\cite{heat1,heat2}. For the ionic case the additional keyword {\\bf ULTRA}
    selects a thermostat for each species, the keyword {\\bf MASSIVE} selects a thermostat
    for each degree of freedom, and the keyword {\\bf CAFES} can be used to give different
    temperatures to different groups of atoms\\cite{cafes02}. The syntax in the {\\bf CAFES}
    case is:\\\\[2ex] \\texttt{NOSE IONS CAFES} ~~~~\\textsl{ncafesgrp}
    ~~\\textsl{cpnumber\\_a\\_1}~~\\textsl{cpnumber\\_a\\_2}~~Temperature Frequency \\dots
    ~~\\textsl{cpnumber\\_n\\_1}~~\\textsl{cpnumber\\_n\\_2}~~Temperature Frequency\\\\[2ex] There
    are \\textsl{ncafesgrp} groups, specified by giving their first CPMD atom number
    (\\textsl{cpnumber\\_X\\_1}) and last CPMD atom number (\\textsl{cpnumber\\_X\\_2}). In the
    case of hybrid QM/MM simulations, you have to consult the QMMM\\_ORDER file to find
    those numbers. The temperature and frequency can be different for each group. All
    atoms of the system have to be in a CAFES group. A new file, \\texttt{CAFES} is created
    containing the temperature of each group (cols. 2 \\dots \\textsl{ncafesgrp+1}) and the
    energy of the Nose-Hoover chains of that group (last columns). Using CAFES with
    different temperatures only makes sense if the different groups are decoupled from
    each other by increasing the masses of the involved atoms. The mass can be specified
    in the topology / or with the \\refkeyword{ISOTOPE} keyword. However, you can only
    change the mass of a complete CPMD species at a time. Hence, the topology and/or the
    input should be such that atoms of different CAFES group are in different species.
    {\\bf NOTE:} CAFES is currently not restartable.\\\\[2ex] The keyword {\\bf LOCAL}
    collects groups of atoms to seperate thermostats, each having its own Nos\\'e-Hoover
    chain. Specify the local thermostats as follows:\\\\[1ex] \\begin{tabular}{lll}
    \\multicolumn{3}{l}{\\tt NOSE IONS LOCAL} \\multicolumn{3}{l}{$n_l$ \\em (number of local
    thermostats)} \\em temperature 1 & \\em frequency 1& \\vdots \\em temperature $n_l$ & \\em
    frequency $n_l$ &\\\\[1ex] \\multicolumn{3}{l}{$n_r$ \\em (number of atom ranges)} \\em
    thermostat number & \\em start atom & \\em end atom \\vdots &\\em ($n_r$ entries)&
    \\end{tabular}  The parser for the atom ranges uses either the CPMD ordering or the
    GROMOS ordering in case of classical or QM/MM runs. Multiple ranges may be specified
    for the same thermostat. Atoms belonging to the same CPMD constraint or the same
    solvent molecule in QM/MM runs must belong to the same local thermostat.  If {\\bf T0}
    option is present, the initial temperature for the Nos{\\'e}-Hoover chains are read
    soon after the thermostat frequencies in the same line (also for the LOCAL
    thermostat). By default it is same as the target temperature of the thermostat. Note:
    This is not implemented for the CAFES thermostat.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_NOSE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NOSE.
        ''')

    x_cpmd_input_CPMD_NOSE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NOSE.
        ''')


class x_cpmd_section_input_CPMD_ODIIS(MSection):
    '''
    Use the method of {\\bf direct inversion} in the iterative subspace for {\\bf
    optimization} of the {\\bf wavefunction}~\\cite{Hutter94a}. The number of DIIS vectors
    is read from the next line.  (ODIIS with {\\bf 10 vectors} is the {\\bf default} method
    in optimization runs.) The preconditioning is controlled by the keyword
    \\refkeyword{HAMILTONIAN CUTOFF}. Optionally preconditioning can be disabled. By
    default, the number of wavefunction optimization cycles until DIIS is {\\bf reset} on
    poor progress, is the number of DIIS vectors. With {\\bf ODIIS NO\\_RESET}, this number
    can be changed, or DIIS resets can be {\\bf disabled} altogether with a value of -1.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ODIIS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ODIIS.
        ''')

    x_cpmd_input_CPMD_ODIIS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ODIIS.
        ''')


class x_cpmd_section_input_CPMD_OPTIMIZE_GEOMETRY(MSection):
    '''
    This option causes the program to optimize the geometry of the system through a
    sequence of wavefunction optimizations and position updates. The additional keyword
    XYZ requests writing the ``trajectory'' of the geometry additionally in xmol/xyz-
    format in a file {\\em GEO\\_OPT.xyz}. If the keyword SAMPLE is given, {\\em NGXYZ} is
    read from the next line, and then only every {\\em NGXTZ} step is written to the
    xmol/xyz file. The {\\bf default} is to write every step ({\\em NGXYZ} = $1$). By
    default the a BFGS/DIIS algorithm is used (see \\refkeyword{GDIIS}) to updated the
    ionic positions. Other options are: \\refkeyword{LBFGS}, \\refkeyword{PRFO}, and
    \\refkeLMAXyword{STEEPEST DESCENT} IONS. See \\refkeyword{OPTIMIZE WAVEFUNCTION} for
    details on the corresponding options for wavefunction optimizations.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_OPTIMIZE_GEOMETRY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OPTIMIZE_GEOMETRY.
        ''')

    x_cpmd_input_CPMD_OPTIMIZE_GEOMETRY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OPTIMIZE_GEOMETRY.
        ''')


class x_cpmd_section_input_CPMD_OPTIMIZE_WAVEFUNCTION(MSection):
    '''
    Request a single point energy calculation through a wavefunction optimization. The
    resulting total energy is printed (for more output options see, e.g.,:
    \\refkeyword{PRINT}, \\refkeyword{RHOOUT}, \\refkeyword{ELF}) and a \\refkeyword{RESTART}
    file is written. This restart file is a prerequisite for many other subsequent
    calculation types in CPMD, e.g. \\refkeyword{MOLECULAR DYNAMICS} CP or
    \\refkeyword{PROPERTIES}. By default a DIIS optimizer is used (see \\refkeyword{ODIIS}),
    but other options are: \\refkeyword{PCG} (optionally with MINIMIZE),
    \\refkeyword{LANCZOS DIAGONALIZATION}, \\refkeyword{DAVIDSON DIAGONALIZATION}, and
    \\refkeyword{STEEPEST DESCENT} ELECTRONS.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_OPTIMIZE_WAVEFUNCTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OPTIMIZE_WAVEFUNCTION.
        ''')

    x_cpmd_input_CPMD_OPTIMIZE_WAVEFUNCTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OPTIMIZE_WAVEFUNCTION.
        ''')


class x_cpmd_section_input_CPMD_ORBITAL_HARDNESS(MSection):
    '''
    Perform an orbital hardness calculation. See section \\&Hardness for further input
    options.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ORBITAL_HARDNESS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ORBITAL_HARDNESS.
        ''')

    x_cpmd_input_CPMD_ORBITAL_HARDNESS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ORBITAL_HARDNESS.
        ''')


class x_cpmd_section_input_CPMD_ORTHOGONALIZATION(MSection):
    '''
    Orthogonalization in optimization runs is done either by a L\\"owdin (symmetric) or
    Gram-Schmidt procedure. {\\bf Default} is Gram-Schmidt except for parallel runs where
    L\\"owdin orthogonalization is used with the conjugate-gradient scheme. With the
    additional keyword {\\bf MATRIX} the L\\"owdin transformation matrix is written to a
    file named LOWDIN\\_A.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ORTHOGONALIZATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ORTHOGONALIZATION.
        ''')

    x_cpmd_input_CPMD_ORTHOGONALIZATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ORTHOGONALIZATION.
        ''')


class x_cpmd_section_input_CPMD_PATH_INTEGRAL(MSection):
    '''
    Perform a {\\bf path integral molecular dynamics} calculation~\\cite{Marx94,Marx96}.
    This keyword requires further input in the section \\&PIMD ... \\&END.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PATH_INTEGRAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PATH_INTEGRAL.
        ''')

    x_cpmd_input_CPMD_PATH_INTEGRAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PATH_INTEGRAL.
        ''')


class x_cpmd_section_input_CPMD_PATH_MINIMIZATION(MSection):
    '''
    Perform a {\\bf mean free energy path} search~\\cite{Eijnden06}. This keyword requires
    further input in the section \\&PATH ... \\&END.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PATH_MINIMIZATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PATH_MINIMIZATION.
        ''')

    x_cpmd_input_CPMD_PATH_MINIMIZATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PATH_MINIMIZATION.
        ''')


class x_cpmd_section_input_CPMD_PATH_SAMPLING(MSection):
    '''
    Use CPMD together with a reaction path sampling~\\cite{tps} program. This needs special
    software. Note: this keyword has {\\em nothing} to do with path integral MD as
    activated by the keyword PATH INTEGRAL and as specified in the section \\&PIMD ...
    \\&END.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PATH_SAMPLING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PATH_SAMPLING.
        ''')

    x_cpmd_input_CPMD_PATH_SAMPLING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PATH_SAMPLING.
        ''')


class x_cpmd_section_input_CPMD_PCG(MSection):
    '''
    Use the method of {\\bf preconditioned conjugate gradients} for {\\bf optimization} of
    the {\\bf wavefunction}. The fixed step length is controlled by the keywords
    \\refkeyword{TIMESTEP ELECTRONS} and \\refkeyword{EMASS}. If the additional option {\\bf
    MINIMIZE} is chosen, then additionally line searches are performed to improve the
    preconditioning. The preconditioning is controlled by the keyword
    \\refkeyword{HAMILTONIAN CUTOFF}. Optionally preconditioning can be disabled.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PCG_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PCG.
        ''')

    x_cpmd_input_CPMD_PCG_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PCG.
        ''')


class x_cpmd_section_input_CPMD_PRFO_NSVIB(MSection):
    '''
    Perform a {\\bf vibrational analysis} every NSVIB P-RFO steps {\\bf on the fly}. This
    option only works with the P-RFO and microiterative transition state search
    algorithms. In case of microiterative TS search, only the reaction core is analyzed.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PRFO_NSVIB_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRFO_NSVIB.
        ''')

    x_cpmd_input_CPMD_PRFO_NSVIB_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRFO_NSVIB.
        ''')


class x_cpmd_section_input_CPMD_PRFO(MSection):
    '''
    Use the partitioned rational function optimizer (P-RFO) with a quasi-Newton method
    for {\\bf optimization} of the {\\bf ionic positions}. For more informations,
    see~\\cite{LSCAL}. The approximated Hessian is updated using the Powell
    method~\\cite{Powell71}. This method is used to find {\\bf transition states} by {\\bf
    following eigenmodes} of the approximated Hessian~\\cite{Banerjee85,LSCAL}. Only one
    suboption is allowed per line and the respective parameter is read from the next line.
    The suboption {\\bf PRJHES} does not take any parameter. If it is present, the
    translational and rotational modes are removed from the Hessian. This is only
    meaningful for conventional (not microiterative) transition state search. The
    parameters mean: \\hfill\\smallskip {\\sl MODE}: \\hfill\\begin{minipage}[t]{9.6cm} Number
    of the initial Hessian {\\bf eigenmode} to be followed. Default is 1 (lowest
    eigenvalue). \\end{minipage} {\\sl MDLOCK:} \\hfill\\begin{minipage}[t]{9.6cm} {\\sl
    MDLOCK=1} switches from a mode following algorithm to a {\\bf fixed eigenvector} to be
    maximized. The default value of 0 ({\\bf mode following}) is recommended.
    \\end{minipage} {\\sl TRUSTP:} \\hfill\\begin{minipage}[t]{9.6cm} Maximum and initial {\\bf
    trust radius}. Default is 0.2 atomic units. \\end{minipage} {\\sl OMIN:}
    \\hfill\\begin{minipage}[t]{9.6cm} This parameter is the minimum {\\bf overlap} between
    the maximized mode of the previous step and the most overlapping eigenvector of the
    current Hessian. The trust radius is reduced until this requirement is fulfilled. The
    default is 0.5. \\end{minipage} {\\sl DISPLACEMENT:} \\hfill\\begin{minipage}[t]{9.6cm}
    Finite-difference {\\bf displacement} for initial partial Hessian. The default is 0.02.
    \\end{minipage} {\\sl HESSTYPE:} \\hfill\\begin{minipage}[t]{9.6cm} {\\bf Type} of initial
    partial Hessian. 0: Finite-difference. 1: Taken from the full Hessian assuming a
    block-diagonal form. See keyword \\refkeyword{HESSIAN}. The default is 0.
    \\end{minipage} It can be useful to combine these keywords with the keywords
    \\refkeyword{CONVERGENCE} ENERGY, \\refkeyword{RESTART} LSSTAT, \\refkeyword{RESTART}
    PHESS, \\refkeyword{PRFO} NSVIB, \\refkeyword{PRINT} LSCAL ON and others.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PRFO_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRFO.
        ''')

    x_cpmd_input_CPMD_PRFO_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRFO.
        ''')


class x_cpmd_section_input_CPMD_PRINT(MSection):
    '''
    A {\\bf detailed output} is printed every {\\sl IPRINT} iterations. Either only
    different contribution to the energy or in addition the atomic coordinates and the
    forces are printed. {\\sl IPRINT} is read from the next line if the keywords {\\bf ON}
    or {\\bf OFF} are not specified.  {\\bf Default} is {\\bf only energies} after the first
    step and at the end of the run. OFF switches the output off.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PRINT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRINT.
        ''')

    x_cpmd_input_CPMD_PRINT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRINT.
        ''')


class x_cpmd_section_input_CPMD_PRNGSEED(MSection):
    '''
    The seed for the random number generator is read as an integer number from the next
    line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PRNGSEED_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRNGSEED.
        ''')

    x_cpmd_input_CPMD_PRNGSEED_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRNGSEED.
        ''')


class x_cpmd_section_input_CPMD_PROJECT(MSection):
    '''
    This keyword is controlling the calculation of the constraint force in optimization
    runs.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PROJECT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PROJECT.
        ''')

    x_cpmd_input_CPMD_PROJECT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PROJECT.
        ''')


class x_cpmd_section_input_CPMD_PROPAGATION_SPECTRA(MSection):
    '''
    Calculates the electronic absorption spectra using the TDDFT propagation of the Kohn-
    Sham orbitals. Use the section \\&PTDDFT to define the parameters. Use this principal
    keyword always with CAYLEY (in \\&CPMD). The program produces a file "dipole.dat" with
    the time series of the variation of the dipole in x, y, and z directions. After
    Fourier transform of this file one gets the desired absorption spectra. Typical
    (minimal) input file (for the sections \\&CPMD and \\&PTDDFT) \\&CPMD  PROPAGATION
    SPECTRA RESTART WAVEFUNCTION COORDINATES LATEST CAYLEY \\&END  \\&PTDDFT  ACCURACY
    1.0D-8  N\\_CYCLES  100000  PROP\\_TSTEP  0.01  EXT\\_PULSE  1.D-5  PERT\\_DIRECTION  1
    RESTART  2  \\&END  The time step is specified by setting \\refkeyword{PROP-TSTEP}. The
    total number of iteration is controlled by \\refkeyword{N-CYCLES}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PROPAGATION_SPECTRA_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PROPAGATION_SPECTRA.
        ''')

    x_cpmd_input_CPMD_PROPAGATION_SPECTRA_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PROPAGATION_SPECTRA.
        ''')


class x_cpmd_section_input_CPMD_PROPERTIES(MSection):
    '''
    Calculate some properties. This keyword requires further input in the section \\&PROP
    \\dots \\&END.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_PROPERTIES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PROPERTIES.
        ''')

    x_cpmd_input_CPMD_PROPERTIES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PROPERTIES.
        ''')


class x_cpmd_section_input_CPMD_QMMM(MSection):
    '''
    Activate the hybrid QM/MM code. This keyword requires further input in the section
    \\&QMMM \\dots \\&END.  The QM driver is the standard CPMD. An interface program ({\\bf
    MM\\_Interface}) and a classic force field
    (Gromos\\cite{gromos96}/Amber\\cite{amber7}-like) are needed to run the code in hybdrid
    mode\\cite{qmmm02,qmmm03,qmmm04,qmmm05,qmmm06}. This code requires a {\\it special
    licence} and is {\\bf not} included in the standard CPMD code. % FIXME: AK 2005/07/10 %
    we should put a contact address or web page here. (see section~\\ref{sec:qmmm} for more
    information on the available options and the input format).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_QMMM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword QMMM.
        ''')

    x_cpmd_input_CPMD_QMMM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword QMMM.
        ''')


class x_cpmd_section_input_CPMD_QUENCH(MSection):
    '''
    The {\\bf velocities} of the {\\bf ions}, {\\bf wavefunctions} or the {\\bf cell} are set
    to zero at the beginning of a run. With the option {\\bf BO} the wavefunctions are
    converged at the beginning of the MD run.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_QUENCH_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword QUENCH.
        ''')

    x_cpmd_input_CPMD_QUENCH_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword QUENCH.
        ''')


class x_cpmd_section_input_CPMD_RANDOMIZE(MSection):
    '''
    The {\\bf ionic positions} or the {\\bf wavefunction} or the {\\bf cell parameters} are
    {\\bf randomly displaced} at the beginning of a run. The maximal amplitude of the
    displacement is read from the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_RANDOMIZE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RANDOMIZE.
        ''')

    x_cpmd_input_CPMD_RANDOMIZE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RANDOMIZE.
        ''')


class x_cpmd_section_input_CPMD_RATTLE(MSection):
    '''
    This option can be used to set the maximum number of iterations and the tolerance for
    the {\\bf iterative orthogonalization}. These two numbers are read from the next line.
    {\\bf Defaults} are 30 and $10^{-6}$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_RATTLE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RATTLE.
        ''')

    x_cpmd_input_CPMD_RATTLE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RATTLE.
        ''')


class x_cpmd_section_input_CPMD_REAL_SPACE_WFN_KEEP(MSection):
    '''
    The real space wavefunctions are kept in memory for later reuse. This minimizes the
    number of Fourier transforms and can result in a significant speedup at the expense of
    a larger memory use. With the option {\\bf SIZE} the maximum available memory for the
    storage of wavefunctions is read from the next line (in MBytes). The program stores as
    many wavefunctions as possible within the given memory allocation.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_REAL_SPACE_WFN_KEEP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REAL_SPACE_WFN_KEEP.
        ''')

    x_cpmd_input_CPMD_REAL_SPACE_WFN_KEEP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REAL_SPACE_WFN_KEEP.
        ''')


class x_cpmd_section_input_CPMD_RESCALE_OLD_VELOCITIES(MSection):
    '''
    Rescale {\\bf ionic} velocities after \\refkeyword{RESTART} to the temperature specified
    by either \\refkeyword{TEMPERATURE}, \\refkeyword{TEMPCONTROL} {\\bf IONS}, or
    \\refkeyword{NOSE} {\\bf IONS}. Useful if the type of ionic thermostatting is changed,
    (do not use RESTART NOSEP in this case).  Note only for path integral runs: the
    scaling is only applied to the first (centroid) replica.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_RESCALE_OLD_VELOCITIES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RESCALE_OLD_VELOCITIES.
        ''')

    x_cpmd_input_CPMD_RESCALE_OLD_VELOCITIES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RESCALE_OLD_VELOCITIES.
        ''')


class x_cpmd_section_input_CPMD_RESTART(MSection):
    '''
    This keyword controls what data is read (at the beginning) from the file RESTART.x.
    {\\bf Warning:} You can only read data that has been previously written into the
    RESTART-file. A list of different {\\it OPTIONS}\\ can be specified. List of valid
    options:
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_RESTART_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RESTART.
        ''')

    x_cpmd_input_CPMD_RESTART_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RESTART.
        ''')


class x_cpmd_section_input_CPMD_RESTFILE(MSection):
    '''
    The number of distinct \\refkeyword{RESTART} files generated during CPMD runs is read
    from the next line. The restart files are written in turn. {\\bf Default is 1}. If you
    specify e.g.~3, then the files RESTART.1, RESTART.2, RESTART.3 are used in rotation.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_RESTFILE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RESTFILE.
        ''')

    x_cpmd_input_CPMD_RESTFILE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RESTFILE.
        ''')


class x_cpmd_section_input_CPMD_REVERSE_VELOCITIES(MSection):
    '''
    Reverse the ionic and electronic (if applicable) velocities after the initial setup of
    an MD run. This way one can, e.g., go ``backwards'' from a given \\refkeyword{RESTART}
    to improve sampling of a given MD ``path''.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_REVERSE_VELOCITIES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REVERSE_VELOCITIES.
        ''')

    x_cpmd_input_CPMD_REVERSE_VELOCITIES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REVERSE_VELOCITIES.
        ''')


class x_cpmd_section_input_CPMD_RHOOUT(MSection):
    '''
    {\\bf Store} the {\\bf density} at the end of the run on file {\\em DENSITY}.  If the
    keyword BANDS is defined then on the following lines the number of bands (or orbitals)
    to be plotted and their index (starting from 1) have to be given. If the position
    specification is a negative number, then the wavefunction instead of the density is
    written. Each band is stored on its own file {\\em DENSITY.num}. For spin polarized
    calculations besides the total density also the spin density is stored on the file
    {\\em SPINDEN}. The following example will request output of the orbitals or bands
    number 5, 7, and 8 as wavefunctions:
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_RHOOUT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RHOOUT.
        ''')

    x_cpmd_input_CPMD_RHOOUT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RHOOUT.
        ''')


class x_cpmd_section_input_CPMD_ROKS(MSection):
    '''
    Calculates the first excited state using Restricted Open-shell Kohn-Sham
    theory~\\cite{Frank98}. By default, the singlet state is calculated using the
    delocalized variant of the modified Goedecker-Umrigar scheme, which is supposed to
    work in most cases. That is, for doing a ROKS simulation, it is usually sufficient to
    just include this keyword in the CPMD section (instead of using the
    \\refspekeyword{LSE}{LOW SPIN EXCITATION} input). See \\ref{hints:roks} for further
    information.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_ROKS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ROKS.
        ''')

    x_cpmd_input_CPMD_ROKS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ROKS.
        ''')


class x_cpmd_section_input_CPMD_SCALED_MASSES(MSection):
    '''
    Switches the usage of g-vector dependent masses on/off.  The number of shells included
    in the analytic integration is controlled with the keyword {\\bf HAMILTONIAN CUTOFF}.
    By {\\bf default} this option is switched {\\bf off}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_SCALED_MASSES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SCALED_MASSES.
        ''')

    x_cpmd_input_CPMD_SCALED_MASSES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SCALED_MASSES.
        ''')


class x_cpmd_section_input_CPMD_SHIFT_POTENTIAL(MSection):
    '''
    After this keyword, useful in hamiltonian diagonalization, the shift value $V_{\\rm
    shift}$ must be provided in the next line. This option is used in the Davidson
    diagonalization subroutine and shifts rigidly the total electronic potential as
    $V_{\\rm pot}({\\bf r}) \\to V_{\\rm pot}({\\bf r})+V_{\\rm shift}$ then it is subtracted
    again at the end of the main loop, restoring back the original $V_{\\rm pot}({\\bf r})$
    that remains basically unaffected once that the calculation is completed.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_SHIFT_POTENTIAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SHIFT_POTENTIAL.
        ''')

    x_cpmd_input_CPMD_SHIFT_POTENTIAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SHIFT_POTENTIAL.
        ''')


class x_cpmd_section_input_CPMD_SPLINE(MSection):
    '''
    This option controls the generation of the pseudopotential functions in g-space.  All
    pseudopotential functions are first initialized on a evenly spaced grid in g-space and
    then calculated at the needed positions with a spline interpolation. The number of
    spline points is read from the next line when {\\bf POINTS} is specified.  ( The {\\bf
    default} number is {\\bf 5000}.) For calculations with the small cutoffs typically used
    together with Vanderbilt PP a much smaller value, like 1500 or 2000, is sufficient.
    In addition it is possible to keep the Q-functions of the Vanderbilt pseudopotentials
    on the spline grid during the whole calculation and do the interpolation whenever
    needed. This option may be useful to save time during the initialization phase and
    memory in the case of Vanderbilt pseudopotentials when the number of shells is not
    much smaller than the total number of plane waves, i.e. for all cell symmetries except
    simple cubic and fcc.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_SPLINE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SPLINE.
        ''')

    x_cpmd_input_CPMD_SPLINE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SPLINE.
        ''')


class x_cpmd_section_input_CPMD_SSIC(MSection):
    '''
    Apply an {\\it ad hoc} Self Interaction Correction (SIC) to the ordinary DFT
    calculation expressed in terms of total energy as \\begin{equation*} E^{\\rm tot}-a\\cdot
    E_H[m]- b\\cdot E_{xc}[m, 0] \\end{equation*} where $m({\\bf x}) = \\rho_\\alpha({\\bf
    x})-\\rho_\\beta({\\bf x})$. The value of $a$ must be supplied in the next line, while in
    the present implementation $b$ is not required, being the optimal values $a=0.2$ and
    $b=0.0$ according to Ref.~\\cite{SSIC}. These are assumed as default values although it
    is not always the case \\cite{dna_sic}. Note that if you select negative $\\{a, b \\}$
    parameters, the signs in the equation above will be reversed. The Hartree electronic
    potential is changed accordingly as $V_H[\\rho] \\to V_H[\\rho] \\pm a\\cdot V_{\\rm
    SIC}[m]$, being \\begin{equation*} V_{\\rm SIC}[m]=\\frac{\\delta E_H[m]}{\\delta m({\\bf
    x})} \\end{equation*} where the sign is $+$ for $\\alpha$ spin and $-$ for $\\beta$ spin
    components, respectively. Be aware that this keyword should be used together with
    $LSD$ (set by default).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_SSIC_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SSIC.
        ''')

    x_cpmd_input_CPMD_SSIC_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SSIC.
        ''')


class x_cpmd_section_input_CPMD_STEEPEST_DESCENT(MSection):
    '''
    NOPRECONDITIONING works only for electrons and LINE only for ions. Use the method of
    {\\bf steepest descent} for the {\\bf optimization} of wavefunction and/or atomic
    positions and/or cell. If both options are specified in a geometry optimization run, a
    simultaneous optimization is performed.  Preconditioning of electron masses (scaled
    masses) is used by default. The preconditioning is controlled by the keyword {\\bf
    HAMILTONIAN CUTOFF}. Optionally preconditioning can be disabled. For ions
    optimization, the steplength is controlled by the keywords {\\bf TIMESTEP} and {\\bf
    EMASS}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_STEEPEST_DESCENT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword STEEPEST_DESCENT.
        ''')

    x_cpmd_input_CPMD_STEEPEST_DESCENT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword STEEPEST_DESCENT.
        ''')


class x_cpmd_section_input_CPMD_STRUCTURE(MSection):
    '''
    Print {\\bf structure information} at the end of the run.  Bonds, angles and dihedral
    angles can be printed. Dihedral angles are defined between 0 and 180 degrees. This
    might change in the future. If the option {\\bf SELECT} is used the output is
    restricted to a set of atoms. The number of atoms and a list of the selected atoms has
    to be given on the next lines.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_STRUCTURE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword STRUCTURE.
        ''')

    x_cpmd_input_CPMD_STRUCTURE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword STRUCTURE.
        ''')


class x_cpmd_section_input_CPMD_SUBTRACT(MSection):
    '''
    If COMVEL is selected, the total momentum of the system is removed, if ROTVEL is
    selected the global angular momentum of the system is removed. Both options can be
    used separately and simultaneously. The subtraction is done each {\\bf ncomv} or {\\bf
    nrotv} steps, where the value is read in the next line.  If this key is activated but
    no number provided, the {\\bf default} is $10000$ steps.   {\\bf Note}: The use of these
    keywords is strongly recommended for long runs (e.g. $t>10$ ps) and/or low density
    systems (e.g. isolated molecules, gas phase \\& Co.). Otherwise the whole system will
    start to translate and/or rotate toward a (random) direction with increasing speed and
    spinning. The ``relative'' translation within the system slows down correspondingly
    and thus the system effectively cools down. As a consequence dynamic properties, like
    self-diffusion coefficients will be wrong.  This option should not be used for
    systems, where some atoms are kept at fixed positions, e.g. slab configurations. Here
    the center of mass may (or should) move. Due to the interactions with the fixed atoms,
    a drift of the whole system should be much reduced, anyways.  {\\bf Note}: since the
    subtracted kinetic energy is put back into the system by simple rescaling of the ionic
    velocities, these options is not fully compatible with \\refkeyword{NOSE} thermostats.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_SUBTRACT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SUBTRACT.
        ''')

    x_cpmd_input_CPMD_SUBTRACT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SUBTRACT.
        ''')


class x_cpmd_section_input_CPMD_SURFACE_HOPPING(MSection):
    '''
    Nonadiabatic dynamics involving the ground state and a \\refkeyword{ROKS} excited
    state\\cite{surfhop}. Do NOT use this keyword together with \\refkeyword{T-SHTDDFT},
    which invokes the surface hopping MD scheme based on TDDFT~\\cite{TDDFT-SH} (see
    \\refkeyword{T-SHTDDFT}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_SURFACE_HOPPING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SURFACE_HOPPING.
        ''')

    x_cpmd_input_CPMD_SURFACE_HOPPING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SURFACE_HOPPING.
        ''')


class x_cpmd_section_input_CPMD_TDDFT(MSection):
    '''
    Calculate the energy according to TDDFT. This keyword can be used together with
    \\refkeyword{OPTIMIZE GEOMETRY} or \\refkeyword{MOLECULAR DYNAMICS} BO. Use the \\&TDDFT
    section to set parameters for the calculation. This keyword requires
    \\refkeyword{RESTART} LINRES.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TDDFT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TDDFT.
        ''')

    x_cpmd_input_CPMD_TDDFT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TDDFT.
        ''')


class x_cpmd_section_input_CPMD_TEMPCONTROL(MSection):
    '''
    The {\\bf temperature} of the {\\bf ions} in Kelvin or the {\\bf fictitious kinetic
    energy} of the {\\bf electrons} in atomic units or the {\\bf kinetic energy} of the {\\bf
    cell} in atomic units (?) is controlled by scaling.  The {\\bf target} temperature and
    the {\\bf tolerance} for the ions or the target kinetic energy and the tolerance for
    the electrons or the cell are read from the next line.  As a gentler alternative you
    may want to try the \\refkeyword{BERENDSEN} scheme instead.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TEMPCONTROL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TEMPCONTROL.
        ''')

    x_cpmd_input_CPMD_TEMPCONTROL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TEMPCONTROL.
        ''')


class x_cpmd_section_input_CPMD_TEMPERATURE_ELECTRON(MSection):
    '''
    The {\\bf electronic temperature} is read from the next line. {\\bf Default} is $1000$K.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TEMPERATURE_ELECTRON_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TEMPERATURE_ELECTRON.
        ''')

    x_cpmd_input_CPMD_TEMPERATURE_ELECTRON_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TEMPERATURE_ELECTRON.
        ''')


class x_cpmd_section_input_CPMD_TEMPERATURE(MSection):
    '''
    The {\\bf initial temperature} in Kelvin of the {\\bf system} is read from the next
    line. With the additional keyword {\\bf RAMP} the temperature can be linearly ramped to
    a target value and two more numbers are read, the ramping target temperature in Kelvin
    and the ramping speed in Kelvin per atomic time unit (to get the change per timestep
    you have to multiply it with the value of \\refkeyword{TIMESTEP}). Note that this
    ramping affects the target temperatures for \\refkeyword{TEMPCONTROL},
    \\refkeyword{BERENDSEN} and the global \\refkeyword{NOSE} thermostats.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TEMPERATURE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TEMPERATURE.
        ''')

    x_cpmd_input_CPMD_TEMPERATURE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TEMPERATURE.
        ''')


class x_cpmd_section_input_CPMD_TIMESTEP_ELECTRONS(MSection):
    '''
    The time step for electron dynamics in atomic units is read from the next line. This
    is can be used to tweak the convergence behavior of the wavefunction optimization in
    Born-Oppenheimer dynamics, where the default time step may be too large. see, e.g.
    \\refkeyword{PCG}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TIMESTEP_ELECTRONS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TIMESTEP_ELECTRONS.
        ''')

    x_cpmd_input_CPMD_TIMESTEP_ELECTRONS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TIMESTEP_ELECTRONS.
        ''')


class x_cpmd_section_input_CPMD_TIMESTEP_IONS(MSection):
    '''
    The time step in atomic units is read from the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TIMESTEP_IONS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TIMESTEP_IONS.
        ''')

    x_cpmd_input_CPMD_TIMESTEP_IONS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TIMESTEP_IONS.
        ''')


class x_cpmd_section_input_CPMD_TIMESTEP(MSection):
    '''
    The time step in atomic units is read from the next line.  {\\bf Default} is a time
    step of {\\bf 5 a.u.} ($1\\, a.u. = 0.0241888428$ fs).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TIMESTEP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TIMESTEP.
        ''')

    x_cpmd_input_CPMD_TIMESTEP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TIMESTEP.
        ''')


class x_cpmd_section_input_CPMD_TRACE(MSection):
    '''
    Activate the tracing of the procedures. {\\sl ALL} specifies that all the mpi tasks are
    traced. {\\sl ALL} specifies that only the master is traced.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TRACE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TRACE.
        ''')

    x_cpmd_input_CPMD_TRACE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TRACE.
        ''')


class x_cpmd_section_input_CPMD_TRAJECTORY(MSection):
    '''
    Store the atomic positions, velocities and optionally forces at every {\\em NTRAJ} time
    step on file {\\em TRAJECTORY}. This is the {\\bf default for MD runs}. With the
    additional keyword XYZ the trajectory is also writthen in xyz-format on the file {\\em
    TRAJEC.xyz}, similarly with the additional keyword DCD a trajectory in dcd-format
    (binary and single precision, as used by CHARMM, X-PLOR and other programs) is written
    on the file {\\rm TRAJEC.dcd}. If the keyword SAMPLE is given {\\em NTRAJ} is read from
    the next line, otherwise the default value for {\\em NTRAJ} is $1$. A negative value of
    {\\em NTRAJ} will disable output of the {\\em TRAJECTORY} file, but e.g. {TRAJEC.xyz}
    will still be written every {\\em -NTRAJ} steps. A value of 0 for {\\em NTRAJ} will
    disable writing of the trajectory files alltogether.  The TRAJECTORY file is written
    in binary format if the keyword BINARY is present. If FORCES is specified also the
    forces are written together with the positions and velocities into the file
    FTRAJECTORY. It is possible to store the data of a subset of atoms by specifying the
    suboption RANGE, the smallest and largest index of atoms is read from the next line.
    If both, SAMPLE and RANGE are given, the RANGE parameters have to come before the
    SAMPLE parameter.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TRAJECTORY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TRAJECTORY.
        ''')

    x_cpmd_input_CPMD_TRAJECTORY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TRAJECTORY.
        ''')


class x_cpmd_section_input_CPMD_TROTTER_FACTORIZATION_OFF(MSection):
    '''
    Do not use Trotter factorization to calculate free energy functional. Remark: Place
    this keywords only after FREE ENERGY FUNCTIO\\-NAL; before it has no effect. Note: this
    keyword has {\\em nothing} to do with path integral MD as activated by the keyword PATH
    INTEGRAL and as specified in the section \\&PIMD ... \\&END.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TROTTER_FACTORIZATION_OFF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TROTTER_FACTORIZATION_OFF.
        ''')

    x_cpmd_input_CPMD_TROTTER_FACTORIZATION_OFF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TROTTER_FACTORIZATION_OFF.
        ''')


class x_cpmd_section_input_CPMD_TROTTER_FACTOR(MSection):
    '''
    Solve $e^{-H/k_BT}$ directly using {\\bf Trotter approximation} $\\left( e^{-pH} \\simeq
    e^{-pK/2}e^{-pV}e^{-pK/2}\\right)$. The Trotter approximation is twice as fast. The
    Trotter factor is read from the next line (typically 0.001 is very accurate).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_TROTTER_FACTOR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TROTTER_FACTOR.
        ''')

    x_cpmd_input_CPMD_TROTTER_FACTOR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TROTTER_FACTOR.
        ''')


class x_cpmd_section_input_CPMD_VDW_CORRECTION(MSection):
    '''
    An empirical van der Waals correction scheme is applied to pairs of atom types
    specified with this keyword. This activates reading the corresponding parameters from
    the \\&VDW ... \\& END in which you have to specify all the VDW parameters between the
    opening and closing section keywords EMPIRICAL CORRECTION and END EMPIRICAL
    CORRECTION. Note that the two possible vdW options, EMPIRICAL CORRECTION  and WANNIER
    CORRECTION are mutually exclusive. See \\refkeyword{VDW PARAMETERS} for more details.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_VDW_CORRECTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword VDW_CORRECTION.
        ''')

    x_cpmd_input_CPMD_VDW_CORRECTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword VDW_CORRECTION.
        ''')


class x_cpmd_section_input_CPMD_VDW_WANNIER(MSection):
    '''
    A first-principle van der Waals correction scheme \\cite{psil1,psil2} is applied to
    selected groups of atoms on which maximally localized Wannier functions (WF) and
    centers (WFC) have been previously computed. The file WANNIER-CENTER generated upon
    WFC calculation must be present. This activates the reading procedure of the
    corresponding parameters from the \\&VDW ... \\&END section.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_VDW_WANNIER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword VDW_WANNIER.
        ''')

    x_cpmd_input_CPMD_VDW_WANNIER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword VDW_WANNIER.
        ''')


class x_cpmd_section_input_CPMD_VGFACTOR(MSection):
    '''
    For \\refkeyword{CDFT} runs read the inverse of the gradient optimiser step size
    ($1/dx$) from the next line. The standard value of \\defaultvalue{10.0} should be fine
    in most situations.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_VGFACTOR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword VGFACTOR.
        ''')

    x_cpmd_input_CPMD_VGFACTOR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword VGFACTOR.
        ''')


class x_cpmd_section_input_CPMD_VIBRATIONAL_ANALYSIS(MSection):
    '''
    Calculate harmonic frequencies by finite differences of first derivatives {\\bf (FD)}
    (see also keyword \\refkeyword{FINITE DIFFERENCES}), by {\\bf linear response} to ionic
    displacements {\\bf (LR)} or from a {\\bf pre-calculated} Hessian {\\bf (IN)}. K-point
    sampling is currently possible using finite differences. If the option GAUSS is
    specified, additional output is written on the file {\\em VIB1.log} which contains the
    modes in a style similar to GAUSSIAN 98 output. This file can be read in and
    visualized with programs like MOLDEN or MOLEKEL. The option SAMPLE reads an integer
    from the next line. If this number is 2 an additional file {\\em VIB2.log} containing
    the lowest modes is written. The {\\bf default} value is 1. If the option ACLIMAX is
    specified, additional output is written on the file VIB.aclimax which contains the
    modes in a style readable by aClimax (\\htref{http://www.isis.rl.ac.uk/molecularspectro
    scopy/aclimax/}{http://www.isis.rl.ac.uk/molecularspectroscopy/aclimax/}). If a
    section {\\bf \\&PROP} is present with the keyword \\refkeyword{DIPOLE MOMENT}[BERRY] or
    \\refkeyword{DIPOLE MOMENT}[RS], the Born charge tensor is calculated on the fly. See
    also the block \\&LINRES ... \\&END and the keywords \\refkeyword{RESTART} PHESS and
    \\refkeyword{HESSIAN} \\{DISCO,SCHLEGEL,UNIT\\} PARTIAL.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_VIBRATIONAL_ANALYSIS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword VIBRATIONAL_ANALYSIS.
        ''')

    x_cpmd_input_CPMD_VIBRATIONAL_ANALYSIS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword VIBRATIONAL_ANALYSIS.
        ''')


class x_cpmd_section_input_CPMD_VMIRROR(MSection):
    '''
    For \\refkeyword{CDFT} HDA runs initialise $V$ for the second state as the negative
    final $V$ value of the first state. Useful in symmetric systems.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_VMIRROR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword VMIRROR.
        ''')

    x_cpmd_input_CPMD_VMIRROR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword VMIRROR.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_DOS(MSection):
    '''
    Outputs the projected density of states of the Wannier orbitals (file WANNIER\\_DOS)
    and the KS hamiltonian in the Wannier states representation (file WANNIER\\_HAM).  When
    running \\refkeyword{MOLECULAR DYNAMICS} CP the files WANNIER\\_DOS and WANNIER\\_HAM
    solely written at the last step.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_DOS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_DOS.
        ''')

    x_cpmd_input_CPMD_WANNIER_DOS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_DOS.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_MOLECULAR(MSection):
    '''
    Generates effective molecular orbitals from the Wannier representation. It first
    attributes Wannier orbitals to molecules and then diagonalizes by molecular blocks the
    KS Hamiltonian.  Does not work with \\refkeyword{MOLECULAR DYNAMICS} CP.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_MOLECULAR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_MOLECULAR.
        ''')

    x_cpmd_input_CPMD_WANNIER_MOLECULAR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_MOLECULAR.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_NPROC(MSection):
    '''
    Set the number of mpi tasks to be used for localization. Default is to use all the
    tasks avalable. The number of tasks is read from the next line and shall be a divisor
    of the number of tasks in a parallel run.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_NPROC_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_NPROC.
        ''')

    x_cpmd_input_CPMD_WANNIER_NPROC_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_NPROC.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_OPTIMIZATION(MSection):
    '''
    Use steepest descent or Jacobi rotation method for the orbital localization. Default
    are Jacobi rotations.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_OPTIMIZATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_OPTIMIZATION.
        ''')

    x_cpmd_input_CPMD_WANNIER_OPTIMIZATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_OPTIMIZATION.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_PARAMETER(MSection):
    '''
    {\\sl W\\_STEP, W\\_EPS, W\\_RAN, W\\_MAXS} are read from the next line. {\\sl W\\_STEP} is
    the step size of the steepest descent algorithm used in the optimization procedure
    (default value 0.1). {\\sl W\\_EPS} the convergence criteria for the gradient (default
    value $1.e-7$). {\\sl W\\_RAN} the amplitude for the initial random rotation of the
    states (default value 0.0). {\\sl W\\_MAXS} is the maximum steps allowed in the
    optimization (default value 200).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_PARAMETER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_PARAMETER.
        ''')

    x_cpmd_input_CPMD_WANNIER_PARAMETER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_PARAMETER.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_REFERENCE(MSection):
    '''
    The vector {\\sl W\\_REF} is read from the next line, which consists of 3 coordinates
    $x, y, z$. These are assumed as the origin for the WFCs positions and related ionic
    coordinates (i.e. ${\\bf R}_I \\to {\\bf R}_I-(x, y, z)$). The default value is the
    center of the supercell, if \\refkeyword{CENTER MOLECULE} keyword is active (Note, that
    this is implicitely turned on, for calculations with \\refkeyword{SYMMETRY} 0).
    Otherwise it is set to (0,0,0), which is usually not the center of the box. In order
    to get the best results displaying the IONS+CENTERS.xyz file this parameter should be
    set explicitly.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_REFERENCE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_REFERENCE.
        ''')

    x_cpmd_input_CPMD_WANNIER_REFERENCE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_REFERENCE.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_SERIAL(MSection):
    '''
    Requests that the calculation of Wannier functions is performed using the serial code,
    even in parallel runs.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_SERIAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_SERIAL.
        ''')

    x_cpmd_input_CPMD_WANNIER_SERIAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_SERIAL.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_TYPE(MSection):
    '''
    Indicates the type of Wannier functions. Vanderbilt type is the default.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_TYPE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_TYPE.
        ''')

    x_cpmd_input_CPMD_WANNIER_TYPE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_TYPE.
        ''')


class x_cpmd_section_input_CPMD_WANNIER_WFNOUT(MSection):
    '''
    Controls the printing of Wannier functions. Either all or only some of the functions
    can be printed. This will be done at the end of each calculation of Wannier functions.
    For {\\bf PARTIAL} output you have to give the indices of the first and the last
    wannier function to print; the {\\em LIST} directive follows the syntax of
    \\refkeyword{RHOOUT} {\\em BANDS}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WANNIER_WFNOUT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_WFNOUT.
        ''')

    x_cpmd_input_CPMD_WANNIER_WFNOUT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_WFNOUT.
        ''')


class x_cpmd_section_input_CPMD_WOUT(MSection):
    '''
    Controls the printing of the CDFT weight(s). If the keyword FULL is set the full
    weight is written out in the form of a density to WEIGHT-(suff), where (suff) is
    defined by the kind of the CDFT job. (suff)=WFOPT for single point calculations, while
    for geometry optimisations and MD two weights are written, (suff)=INIT at the
    beginning and (suff)=FINAL for the last step. If FULL is not set write out a slice of
    the weight in gnuplot readable form to WEIGHT-(suff).dat. Parameters WSLICE and WSTEP
    are read from the next line. WSLICE \\defaultvalue{0.5} is if larger than zero the z
    coordinate of the x-y weight plane to write out divided by the total box height. If
    WSLICE$<0$ the weight at the z coordinate of the first acceptor atom will be used.
    WSTEP \\defaultvalue{1} is the grid point step size for the output.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_WOUT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WOUT.
        ''')

    x_cpmd_input_CPMD_WOUT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WOUT.
        ''')


class x_cpmd_section_input_CPMD(MSection):
    '''
    General control parameters for calculation (\\textbf{required}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_CPMD_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section CPMD even without a keyword.
        ''')

    x_cpmd_section_input_CPMD_ALEXANDER_MIXING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ALEXANDER_MIXING'),
        repeats=True)

    x_cpmd_section_input_CPMD_ALLTOALL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ALLTOALL'),
        repeats=True)

    x_cpmd_section_input_CPMD_ANDERSON_MIXING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ANDERSON_MIXING'),
        repeats=True)

    x_cpmd_section_input_CPMD_ANNEALING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ANNEALING'),
        repeats=True)

    x_cpmd_section_input_CPMD_BENCHMARK = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_BENCHMARK'),
        repeats=True)

    x_cpmd_section_input_CPMD_BERENDSEN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_BERENDSEN'),
        repeats=True)

    x_cpmd_section_input_CPMD_BFGS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_BFGS'),
        repeats=True)

    x_cpmd_section_input_CPMD_BLOCKSIZE_STATES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_BLOCKSIZE_STATES'),
        repeats=True)

    x_cpmd_section_input_CPMD_BOGOLIUBOV_CORRECTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_BOGOLIUBOV_CORRECTION'),
        repeats=True)

    x_cpmd_section_input_CPMD_BOX_WALLS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_BOX_WALLS'),
        repeats=True)

    x_cpmd_section_input_CPMD_BROYDEN_MIXING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_BROYDEN_MIXING'),
        repeats=True)

    x_cpmd_section_input_CPMD_CAYLEY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CAYLEY'),
        repeats=True)

    x_cpmd_section_input_CPMD_CDFT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CDFT'),
        repeats=True)

    x_cpmd_section_input_CPMD_CENTER_MOLECULE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CENTER_MOLECULE'),
        repeats=True)

    x_cpmd_section_input_CPMD_CHECK_MEMORY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CHECK_MEMORY'),
        repeats=True)

    x_cpmd_section_input_CPMD_CLASSTRESS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CLASSTRESS'),
        repeats=True)

    x_cpmd_section_input_CPMD_CMASS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CMASS'),
        repeats=True)

    x_cpmd_section_input_CPMD_COMBINE_SYSTEMS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_COMBINE_SYSTEMS'),
        repeats=True)

    x_cpmd_section_input_CPMD_COMPRESS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_COMPRESS'),
        repeats=True)

    x_cpmd_section_input_CPMD_CONJUGATE_GRADIENTS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CONJUGATE_GRADIENTS'),
        repeats=True)

    x_cpmd_section_input_CPMD_CONVERGENCE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CONVERGENCE'),
        repeats=True)

    x_cpmd_section_input_CPMD_CZONES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_CZONES'),
        repeats=True)

    x_cpmd_section_input_CPMD_DAMPING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DAMPING'),
        repeats=True)

    x_cpmd_section_input_CPMD_DAVIDSON_DIAGONALIZATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DAVIDSON_DIAGONALIZATION'),
        repeats=True)

    x_cpmd_section_input_CPMD_DAVIDSON_PARAMETER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DAVIDSON_PARAMETER'),
        repeats=True)

    x_cpmd_section_input_CPMD_DEBUG_CODE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DEBUG_CODE'),
        repeats=True)

    x_cpmd_section_input_CPMD_DEBUG_FILEOPEN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DEBUG_FILEOPEN'),
        repeats=True)

    x_cpmd_section_input_CPMD_DEBUG_FORCES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DEBUG_FORCES'),
        repeats=True)

    x_cpmd_section_input_CPMD_DEBUG_MEMORY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DEBUG_MEMORY'),
        repeats=True)

    x_cpmd_section_input_CPMD_DEBUG_NOACC = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DEBUG_NOACC'),
        repeats=True)

    x_cpmd_section_input_CPMD_DIIS_MIXING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DIIS_MIXING'),
        repeats=True)

    x_cpmd_section_input_CPMD_DIPOLE_DYNAMICS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DIPOLE_DYNAMICS'),
        repeats=True)

    x_cpmd_section_input_CPMD_DISTRIBUTE_FNL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DISTRIBUTE_FNL'),
        repeats=True)

    x_cpmd_section_input_CPMD_DISTRIBUTED_LINALG = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_DISTRIBUTED_LINALG'),
        repeats=True)

    x_cpmd_section_input_CPMD_ELECTRONIC_SPECTRA = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ELECTRONIC_SPECTRA'),
        repeats=True)

    x_cpmd_section_input_CPMD_ELECTROSTATIC_POTENTIAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ELECTROSTATIC_POTENTIAL'),
        repeats=True)

    x_cpmd_section_input_CPMD_ELF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ELF'),
        repeats=True)

    x_cpmd_section_input_CPMD_EMASS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_EMASS'),
        repeats=True)

    x_cpmd_section_input_CPMD_ENERGYBANDS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ENERGYBANDS'),
        repeats=True)

    x_cpmd_section_input_CPMD_EXTERNAL_POTENTIAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_EXTERNAL_POTENTIAL'),
        repeats=True)

    x_cpmd_section_input_CPMD_EXTRAPOLATE_CONSTRAINT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_EXTRAPOLATE_CONSTRAINT'),
        repeats=True)

    x_cpmd_section_input_CPMD_EXTRAPOLATE_WFN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_EXTRAPOLATE_WFN'),
        repeats=True)

    x_cpmd_section_input_CPMD_FFTW_WISDOM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_FFTW_WISDOM'),
        repeats=True)

    x_cpmd_section_input_CPMD_FILE_FUSION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_FILE_FUSION'),
        repeats=True)

    x_cpmd_section_input_CPMD_FILEPATH = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_FILEPATH'),
        repeats=True)

    x_cpmd_section_input_CPMD_FINITE_DIFFERENCES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_FINITE_DIFFERENCES'),
        repeats=True)

    x_cpmd_section_input_CPMD_FIXRHO_UPWFN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_FIXRHO_UPWFN'),
        repeats=True)

    x_cpmd_section_input_CPMD_FORCEMATCH = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_FORCEMATCH'),
        repeats=True)

    x_cpmd_section_input_CPMD_FREE_ENERGY_FUNCTIONAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_FREE_ENERGY_FUNCTIONAL'),
        repeats=True)

    x_cpmd_section_input_CPMD_GDIIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_GDIIS'),
        repeats=True)

    x_cpmd_section_input_CPMD_GSHELL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_GSHELL'),
        repeats=True)

    x_cpmd_section_input_CPMD_HAMILTONIAN_CUTOFF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_HAMILTONIAN_CUTOFF'),
        repeats=True)

    x_cpmd_section_input_CPMD_HARMONIC_REFERENCE_SYSTEM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_HARMONIC_REFERENCE_SYSTEM'),
        repeats=True)

    x_cpmd_section_input_CPMD_HESSCORE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_HESSCORE'),
        repeats=True)

    x_cpmd_section_input_CPMD_HESSIAN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_HESSIAN'),
        repeats=True)

    x_cpmd_section_input_CPMD_INITIALIZE_WAVEFUNCTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_INITIALIZE_WAVEFUNCTION'),
        repeats=True)

    x_cpmd_section_input_CPMD_INTERFACE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_INTERFACE'),
        repeats=True)

    x_cpmd_section_input_CPMD_INTFILE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_INTFILE'),
        repeats=True)

    x_cpmd_section_input_CPMD_ISOLATED_MOLECULE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ISOLATED_MOLECULE'),
        repeats=True)

    x_cpmd_section_input_CPMD_KSHAM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_KSHAM'),
        repeats=True)

    x_cpmd_section_input_CPMD_LANCZOS_DIAGONALIZATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_LANCZOS_DIAGONALIZATION'),
        repeats=True)

    x_cpmd_section_input_CPMD_LANCZOS_PARAMETER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_LANCZOS_PARAMETER'),
        repeats=True)

    x_cpmd_section_input_CPMD_LANGEVIN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_LANGEVIN'),
        repeats=True)

    x_cpmd_section_input_CPMD_LBFGS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_LBFGS'),
        repeats=True)

    x_cpmd_section_input_CPMD_LINEAR_RESPONSE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_LINEAR_RESPONSE'),
        repeats=True)

    x_cpmd_section_input_CPMD_LOCAL_SPIN_DENSITY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_LOCAL_SPIN_DENSITY'),
        repeats=True)

    x_cpmd_section_input_CPMD_LSD = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_LSD'),
        repeats=True)

    x_cpmd_section_input_CPMD_MAXITER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MAXITER'),
        repeats=True)

    x_cpmd_section_input_CPMD_MAXRUNTIME = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MAXRUNTIME'),
        repeats=True)

    x_cpmd_section_input_CPMD_MAXSTEP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MAXSTEP'),
        repeats=True)

    x_cpmd_section_input_CPMD_MEMORY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MEMORY'),
        repeats=True)

    x_cpmd_section_input_CPMD_MIRROR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MIRROR'),
        repeats=True)

    x_cpmd_section_input_CPMD_MIXDIIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MIXDIIS'),
        repeats=True)

    x_cpmd_section_input_CPMD_MIXSD = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MIXSD'),
        repeats=True)

    x_cpmd_section_input_CPMD_MODIFIED_GOEDECKER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MODIFIED_GOEDECKER'),
        repeats=True)

    x_cpmd_section_input_CPMD_MOLECULAR_DYNAMICS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MOLECULAR_DYNAMICS'),
        repeats=True)

    x_cpmd_section_input_CPMD_MOVERHO = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MOVERHO'),
        repeats=True)

    x_cpmd_section_input_CPMD_MOVIE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_MOVIE'),
        repeats=True)

    x_cpmd_section_input_CPMD_NOGEOCHECK = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_NOGEOCHECK'),
        repeats=True)

    x_cpmd_section_input_CPMD_NONORTHOGONAL_ORBITALS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_NONORTHOGONAL_ORBITALS'),
        repeats=True)

    x_cpmd_section_input_CPMD_NOSE_PARAMETERS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_NOSE_PARAMETERS'),
        repeats=True)

    x_cpmd_section_input_CPMD_NOSE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_NOSE'),
        repeats=True)

    x_cpmd_section_input_CPMD_ODIIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ODIIS'),
        repeats=True)

    x_cpmd_section_input_CPMD_OPTIMIZE_GEOMETRY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_OPTIMIZE_GEOMETRY'),
        repeats=True)

    x_cpmd_section_input_CPMD_OPTIMIZE_WAVEFUNCTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_OPTIMIZE_WAVEFUNCTION'),
        repeats=True)

    x_cpmd_section_input_CPMD_ORBITAL_HARDNESS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ORBITAL_HARDNESS'),
        repeats=True)

    x_cpmd_section_input_CPMD_ORTHOGONALIZATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ORTHOGONALIZATION'),
        repeats=True)

    x_cpmd_section_input_CPMD_PATH_INTEGRAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PATH_INTEGRAL'),
        repeats=True)

    x_cpmd_section_input_CPMD_PATH_MINIMIZATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PATH_MINIMIZATION'),
        repeats=True)

    x_cpmd_section_input_CPMD_PATH_SAMPLING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PATH_SAMPLING'),
        repeats=True)

    x_cpmd_section_input_CPMD_PCG = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PCG'),
        repeats=True)

    x_cpmd_section_input_CPMD_PRFO_NSVIB = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PRFO_NSVIB'),
        repeats=True)

    x_cpmd_section_input_CPMD_PRFO = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PRFO'),
        repeats=True)

    x_cpmd_section_input_CPMD_PRINT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PRINT'),
        repeats=True)

    x_cpmd_section_input_CPMD_PRNGSEED = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PRNGSEED'),
        repeats=True)

    x_cpmd_section_input_CPMD_PROJECT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PROJECT'),
        repeats=True)

    x_cpmd_section_input_CPMD_PROPAGATION_SPECTRA = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PROPAGATION_SPECTRA'),
        repeats=True)

    x_cpmd_section_input_CPMD_PROPERTIES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_PROPERTIES'),
        repeats=True)

    x_cpmd_section_input_CPMD_QMMM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_QMMM'),
        repeats=True)

    x_cpmd_section_input_CPMD_QUENCH = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_QUENCH'),
        repeats=True)

    x_cpmd_section_input_CPMD_RANDOMIZE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_RANDOMIZE'),
        repeats=True)

    x_cpmd_section_input_CPMD_RATTLE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_RATTLE'),
        repeats=True)

    x_cpmd_section_input_CPMD_REAL_SPACE_WFN_KEEP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_REAL_SPACE_WFN_KEEP'),
        repeats=True)

    x_cpmd_section_input_CPMD_RESCALE_OLD_VELOCITIES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_RESCALE_OLD_VELOCITIES'),
        repeats=True)

    x_cpmd_section_input_CPMD_RESTART = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_RESTART'),
        repeats=True)

    x_cpmd_section_input_CPMD_RESTFILE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_RESTFILE'),
        repeats=True)

    x_cpmd_section_input_CPMD_REVERSE_VELOCITIES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_REVERSE_VELOCITIES'),
        repeats=True)

    x_cpmd_section_input_CPMD_RHOOUT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_RHOOUT'),
        repeats=True)

    x_cpmd_section_input_CPMD_ROKS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_ROKS'),
        repeats=True)

    x_cpmd_section_input_CPMD_SCALED_MASSES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_SCALED_MASSES'),
        repeats=True)

    x_cpmd_section_input_CPMD_SHIFT_POTENTIAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_SHIFT_POTENTIAL'),
        repeats=True)

    x_cpmd_section_input_CPMD_SPLINE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_SPLINE'),
        repeats=True)

    x_cpmd_section_input_CPMD_SSIC = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_SSIC'),
        repeats=True)

    x_cpmd_section_input_CPMD_STEEPEST_DESCENT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_STEEPEST_DESCENT'),
        repeats=True)

    x_cpmd_section_input_CPMD_STRUCTURE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_STRUCTURE'),
        repeats=True)

    x_cpmd_section_input_CPMD_SUBTRACT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_SUBTRACT'),
        repeats=True)

    x_cpmd_section_input_CPMD_SURFACE_HOPPING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_SURFACE_HOPPING'),
        repeats=True)

    x_cpmd_section_input_CPMD_TDDFT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TDDFT'),
        repeats=True)

    x_cpmd_section_input_CPMD_TEMPCONTROL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TEMPCONTROL'),
        repeats=True)

    x_cpmd_section_input_CPMD_TEMPERATURE_ELECTRON = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TEMPERATURE_ELECTRON'),
        repeats=True)

    x_cpmd_section_input_CPMD_TEMPERATURE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TEMPERATURE'),
        repeats=True)

    x_cpmd_section_input_CPMD_TIMESTEP_ELECTRONS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TIMESTEP_ELECTRONS'),
        repeats=True)

    x_cpmd_section_input_CPMD_TIMESTEP_IONS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TIMESTEP_IONS'),
        repeats=True)

    x_cpmd_section_input_CPMD_TIMESTEP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TIMESTEP'),
        repeats=True)

    x_cpmd_section_input_CPMD_TRACE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TRACE'),
        repeats=True)

    x_cpmd_section_input_CPMD_TRAJECTORY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TRAJECTORY'),
        repeats=True)

    x_cpmd_section_input_CPMD_TROTTER_FACTORIZATION_OFF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TROTTER_FACTORIZATION_OFF'),
        repeats=True)

    x_cpmd_section_input_CPMD_TROTTER_FACTOR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_TROTTER_FACTOR'),
        repeats=True)

    x_cpmd_section_input_CPMD_VDW_CORRECTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_VDW_CORRECTION'),
        repeats=True)

    x_cpmd_section_input_CPMD_VDW_WANNIER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_VDW_WANNIER'),
        repeats=True)

    x_cpmd_section_input_CPMD_VGFACTOR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_VGFACTOR'),
        repeats=True)

    x_cpmd_section_input_CPMD_VIBRATIONAL_ANALYSIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_VIBRATIONAL_ANALYSIS'),
        repeats=True)

    x_cpmd_section_input_CPMD_VMIRROR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_VMIRROR'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_DOS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_DOS'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_MOLECULAR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_MOLECULAR'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_NPROC = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_NPROC'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_OPTIMIZATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_OPTIMIZATION'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_PARAMETER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_PARAMETER'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_REFERENCE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_REFERENCE'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_SERIAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_SERIAL'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_TYPE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_TYPE'),
        repeats=True)

    x_cpmd_section_input_CPMD_WANNIER_WFNOUT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WANNIER_WFNOUT'),
        repeats=True)

    x_cpmd_section_input_CPMD_WOUT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD_WOUT'),
        repeats=True)


class x_cpmd_section_input_DFT_ACM0(MSection):
    '''
    Add exact exchange to the specified \\refkeyword{FUNCTIONAL} according to the adiabatic
    connection method 0.~\\cite{acm0,adamo2000} This only works for isolated systems and
    should only be used if an excessive amount of CPU time is available.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_ACM0_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ACM0.
        ''')

    x_cpmd_input_DFT_ACM0_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ACM0.
        ''')


class x_cpmd_section_input_DFT_ACM1(MSection):
    '''
    Add exact exchange to the specified \\refkeyword{FUNCTIONAL} according to the adiabatic
    connection method 1.~\\cite{adamo2000,acm1} The parameter is read from the next line.
    This only works for isolated systems and should only be used if an excessive amount of
    CPU time is available.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_ACM1_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ACM1.
        ''')

    x_cpmd_input_DFT_ACM1_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ACM1.
        ''')


class x_cpmd_section_input_DFT_ACM3(MSection):
    '''
    Add exact exchange to the specified \\refkeyword{FUNCTIONAL} according to the adiabatic
    connection method 3.~\\cite{adamo2000,acm3} The three needed parameters are read from
    the next line. This only works for isolated systems and should only be used if an
    excessive amount of CPU time is available.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_ACM3_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ACM3.
        ''')

    x_cpmd_input_DFT_ACM3_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ACM3.
        ''')


class x_cpmd_section_input_DFT_BECKE_BETA(MSection):
    '''
    Change the $\\beta$ parameter in Becke's exchange functional~\\cite{Becke88} to the
    value given on the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_BECKE_BETA_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BECKE_BETA.
        ''')

    x_cpmd_input_DFT_BECKE_BETA_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BECKE_BETA.
        ''')


class x_cpmd_section_input_DFT_EXCHANGE_CORRELATION_TABLE(MSection):
    '''
    Specifies the range and the  granularity of the lookup table for the local exchange-
    correlation energy and potential. The number of table entries and the maximum density
    have to be given on the next line.  Note that this keyword is only relevant when using
    \\refkeyword{OLDCODE} and even then it is set to \\textbf{NO} be default. Previous
    default values were 30000 and 2.0.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_EXCHANGE_CORRELATION_TABLE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXCHANGE_CORRELATION_TABLE.
        ''')

    x_cpmd_input_DFT_EXCHANGE_CORRELATION_TABLE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXCHANGE_CORRELATION_TABLE.
        ''')


class x_cpmd_section_input_DFT_FUNCTIONAL(MSection):
    '''
    Single keyword for setting up XC-functionals. Available functionals are NONE, SONLY,
    LDA (in PADE form), \\goodbreak BONLY, BP, BLYP, XLYP, GGA (=PW91), PBE, PBES, REVPBE,
    \\goodbreak HCTH, OPTX, OLYP, TPSS, PBE0, B1LYP, B3LYP, X3LYP,PBES, \\goodbreak HSE06
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_FUNCTIONAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FUNCTIONAL.
        ''')

    x_cpmd_input_DFT_FUNCTIONAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FUNCTIONAL.
        ''')


class x_cpmd_section_input_DFT_GRADIENT_CORRECTION(MSection):
    '''
    Individual components of gradient corrected functionals can be selected. Rarely needed
    anymore, use the \\refkeyword{FUNCTIONAL} keyword instead.  Functionals implemented are
    for the exchange energy: {\\bf BECKE88}~\\cite{Becke88}, {\\bf GGAX}~\\cite{Perdew92} {\\bf
    PBEX}~\\cite{Perdew96}, {\\bf REVPBEX}~\\cite{Zhang98}, \\goodbreak{\\bf
    HCTH}~\\cite{Handy98}, {\\bf OPTX}~\\cite{Optx},{\\bf PBESX}~\\cite{Perdew07}  and for the
    correlation part: {\\bf PERDEW86}~\\cite{Perdew86}, {\\bf LYP}~\\cite{Lee88}, {\\bf
    GGAC}~\\cite{Perdew92}, {\\bf PBEC} \\cite{Perdew96}, {\\bf REVPBEC} \\cite{Zhang98}, {\\bf
    HCTH} \\cite{Handy98} {\\bf OLYP}~\\cite{Optx},{\\bf PBESC}~\\cite{Perdew07}.  Note that
    for HCTH, exchange and correlation are treated as a unique functional. The keywords
    {\\bf EXCHANGE} and {\\bf CORRELATION} can be used for the default functionals
    (currently BECKE88 and PERDEW86). If no functionals are specified the default
    functionals for exchange and correlation are used.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_GRADIENT_CORRECTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword GRADIENT_CORRECTION.
        ''')

    x_cpmd_input_DFT_GRADIENT_CORRECTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword GRADIENT_CORRECTION.
        ''')


class x_cpmd_section_input_DFT_HARTREE(MSection):
    '''
    Do a Hartree calculation. Only of use for testing purposes.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_HARTREE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HARTREE.
        ''')

    x_cpmd_input_DFT_HARTREE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HARTREE.
        ''')


class x_cpmd_section_input_DFT_HFX_SCREENING(MSection):
    '''
    Read value from the next line.  Perform the calculation of exact exchange using
    Wannier functions. Orbital pairs are screened according to the distance of the Wannier
    centers {\\sl WFC}, the value of the integrals {\\sl EPS\\_INT}, or only the diagonal
    terms are included ({\\sl DIAG}). {\\sl RECOMPUTE\\_TWO\\_INT\\_LIST\\_EVERY} allows to set
    how often the integral list is recomputed.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_HFX_SCREENING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HFX_SCREENING.
        ''')

    x_cpmd_input_DFT_HFX_SCREENING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HFX_SCREENING.
        ''')


class x_cpmd_section_input_DFT_LDA_CORRELATION(MSection):
    '''
    The LDA correlation functional is specified.  Possible functionals are {\\bf NO} (no
    correlation functional), {\\bf PZ}~\\cite{Perdew81}, \\penalty 1000 {\\bf
    VWN}~\\cite{Vosko80}, {\\bf LYP}~\\cite{Lee88} and {\\bf PW}~\\cite{Perdew91}.  Default is
    the {\\bf PZ}, the Perdew and Zunger fit to the data of Ceperley and
    Alder~\\cite{Ceperley80}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_LDA_CORRELATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LDA_CORRELATION.
        ''')

    x_cpmd_input_DFT_LDA_CORRELATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LDA_CORRELATION.
        ''')


class x_cpmd_section_input_DFT_LR_KERNEL(MSection):
    '''
    Use another functional for the linear response kernel.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_LR_KERNEL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LR_KERNEL.
        ''')

    x_cpmd_input_DFT_LR_KERNEL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LR_KERNEL.
        ''')


class x_cpmd_section_input_DFT_NEWCODE(MSection):
    '''
    Switch to select one out of two versions of code to calculate exchange-correlation
    functionals.  NEWCODE is the default, but not all functionals are available with
    NEWCODE, if you select one of these, \\refkeyword{OLDCODE} is used automatically.
    NEWCODE is highly recommended for all new projects and especially for vector
    computers, also some of the newer functionality is untested or non-functional with
    OLDCODE.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_NEWCODE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NEWCODE.
        ''')

    x_cpmd_input_DFT_NEWCODE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NEWCODE.
        ''')


class x_cpmd_section_input_DFT_OLDCODE(MSection):
    '''
    see \\refkeyword{NEWCODE}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_OLDCODE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OLDCODE.
        ''')

    x_cpmd_input_DFT_OLDCODE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OLDCODE.
        ''')


class x_cpmd_section_input_DFT_REFUNCT(MSection):
    '''
    Use a special reference functional in a calculation. This option is not active.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_REFUNCT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REFUNCT.
        ''')

    x_cpmd_input_DFT_REFUNCT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REFUNCT.
        ''')


class x_cpmd_section_input_DFT_SLATER(MSection):
    '''
    The $\\alpha$ value for the Slater exchange functional~\\cite{Slater51} is read from the
    next line. With NO the exchange functional is switched off. Default is a value of 2/3.
    This option together with no correlation functional, allows for $X\\alpha$ theory.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_SLATER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SLATER.
        ''')

    x_cpmd_input_DFT_SLATER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SLATER.
        ''')


class x_cpmd_section_input_DFT_SMOOTH(MSection):
    '''
    A smoothening function is applied to the density~\\cite{Laasonen93}. The function is of
    the Fermi type. \\[  f(G) = \\frac{1}{% \\displaystyle{1 + e^{\\frac{\\scriptstyle{G -
    G_{\\scriptstyle cut}}} {\\scriptstyle\\Delta}}}} \\] G is the wavevector, $G_{cut} =
    \\alpha\\,G_{max}$ and $\\Delta = \\beta\\,G_{max}$. Values for $\\alpha$ and $\\beta$ have
    to be given on the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_SMOOTH_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SMOOTH.
        ''')

    x_cpmd_input_DFT_SMOOTH_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SMOOTH.
        ''')


class x_cpmd_section_input_DFT(MSection):
    '''
    Exchange and correlation functional and related parameters.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_DFT_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section DFT even without a keyword.
        ''')

    x_cpmd_section_input_DFT_ACM0 = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_ACM0'),
        repeats=True)

    x_cpmd_section_input_DFT_ACM1 = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_ACM1'),
        repeats=True)

    x_cpmd_section_input_DFT_ACM3 = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_ACM3'),
        repeats=True)

    x_cpmd_section_input_DFT_BECKE_BETA = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_BECKE_BETA'),
        repeats=True)

    x_cpmd_section_input_DFT_EXCHANGE_CORRELATION_TABLE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_EXCHANGE_CORRELATION_TABLE'),
        repeats=True)

    x_cpmd_section_input_DFT_FUNCTIONAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_FUNCTIONAL'),
        repeats=True)

    x_cpmd_section_input_DFT_GRADIENT_CORRECTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_GRADIENT_CORRECTION'),
        repeats=True)

    x_cpmd_section_input_DFT_HARTREE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_HARTREE'),
        repeats=True)

    x_cpmd_section_input_DFT_HFX_SCREENING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_HFX_SCREENING'),
        repeats=True)

    x_cpmd_section_input_DFT_LDA_CORRELATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_LDA_CORRELATION'),
        repeats=True)

    x_cpmd_section_input_DFT_LR_KERNEL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_LR_KERNEL'),
        repeats=True)

    x_cpmd_section_input_DFT_NEWCODE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_NEWCODE'),
        repeats=True)

    x_cpmd_section_input_DFT_OLDCODE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_OLDCODE'),
        repeats=True)

    x_cpmd_section_input_DFT_REFUNCT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_REFUNCT'),
        repeats=True)

    x_cpmd_section_input_DFT_SLATER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_SLATER'),
        repeats=True)

    x_cpmd_section_input_DFT_SMOOTH = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT_SMOOTH'),
        repeats=True)


class x_cpmd_section_input_EXTE(MSection):
    '''
    External field definition for EGO QM/MM interface
    '''

    m_def = Section(validate=False)

    x_cpmd_input_EXTE_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section EXTE even without a keyword.
        ''')


class x_cpmd_section_input_HARDNESS_DIAGONAL(MSection):
    '''
    Not documented
    '''

    m_def = Section(validate=False)

    x_cpmd_input_HARDNESS_DIAGONAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DIAGONAL.
        ''')

    x_cpmd_input_HARDNESS_DIAGONAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DIAGONAL.
        ''')


class x_cpmd_section_input_HARDNESS_ORBITALS(MSection):
    '''
    Specify the number of orbitals to be used in a hardness calculation on the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_HARDNESS_ORBITALS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ORBITALS.
        ''')

    x_cpmd_input_HARDNESS_ORBITALS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ORBITALS.
        ''')


class x_cpmd_section_input_HARDNESS_REFATOM(MSection):
    '''
    Specify the reference atom to be used in a hardness calculation on the next line. This
    option is to be used together with the \\refkeyword{ORBITALS} and
    \\refkeyword{LOCALIZE}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_HARDNESS_REFATOM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REFATOM.
        ''')

    x_cpmd_input_HARDNESS_REFATOM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REFATOM.
        ''')


class x_cpmd_section_input_HARDNESS(MSection):
    '''
    Input for HARDNESS calculations
    '''

    m_def = Section(validate=False)

    x_cpmd_input_HARDNESS_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section HARDNESS even without a keyword.
        ''')

    x_cpmd_section_input_HARDNESS_DIAGONAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_HARDNESS_DIAGONAL'),
        repeats=True)

    x_cpmd_section_input_HARDNESS_ORBITALS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_HARDNESS_ORBITALS'),
        repeats=True)

    x_cpmd_section_input_HARDNESS_REFATOM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_HARDNESS_REFATOM'),
        repeats=True)


class x_cpmd_section_input_INFO(MSection):
    '''
    A place to put comments about the job.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_INFO_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section INFO even without a keyword.
        ''')


class x_cpmd_section_input_LINRES_DIFF_FORMULA(MSection):
    '''
    Number of points used in finite difference formula for second derivatives of exchange
    --correlation functionals. Default is two point central differences.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_DIFF_FORMULA_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DIFF_FORMULA.
        ''')

    x_cpmd_input_LINRES_DIFF_FORMULA_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DIFF_FORMULA.
        ''')


class x_cpmd_section_input_LINRES_GAUGE(MSection):
    '''
    Gauge of the linear-response wavefunctions. Default is the parallel-transport gauge
    (PARA) for closed-shell calculations and a sensible combination of the parallel-
    transport gauge and the full-rotation gauge (GEN) for all other cases. The full-
    rotation gauge can be enforced for all states by selecting ALL. See \\cite{lsets}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_GAUGE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword GAUGE.
        ''')

    x_cpmd_input_LINRES_GAUGE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword GAUGE.
        ''')


class x_cpmd_section_input_LINRES_HTHRS(MSection):
    '''
    Threshold for Hessian in preconditioner for linear response optimizations. Default is
    0.5.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_HTHRS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HTHRS.
        ''')

    x_cpmd_input_LINRES_HTHRS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HTHRS.
        ''')


class x_cpmd_section_input_LINRES_OPTIMIZER(MSection):
    '''
    Optimizer to be used for linear response equations. Default is ``AUTO'' which will
    first use PCG, then switch to DIIS and finally switch to DIIS with full storage and
    state dependent preconditioner. \\refkeyword{THAUTO} sets the two tolerances for when
    to do the switch.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_OPTIMIZER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OPTIMIZER.
        ''')

    x_cpmd_input_LINRES_OPTIMIZER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OPTIMIZER.
        ''')


class x_cpmd_section_input_LINRES_STEPLENGTH(MSection):
    '''
    Step length for steepest descent and preconditioned conjugate gradient methods used in
    linear response calculations. Default is 0.1.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_STEPLENGTH_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword STEPLENGTH.
        ''')

    x_cpmd_input_LINRES_STEPLENGTH_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword STEPLENGTH.
        ''')


class x_cpmd_section_input_LINRES_THAUTO(MSection):
    '''
    The two values read from the next line control the switch to different optimizers for
    an automatic selection of optimizers during a linear response calculation. This also
    applies to the Z-vector optimization for TDDFT forces. The first value is the
    threshold for switching from conjugate gradients to DIIS (with compressed storage and
    averged preconditioner, subspace size defined with \\refkeyword{ODIIS}). The second
    value is the threshold for switching to DIIS with full storage and state dependent
    preconditioner. See also \\refkeyword{ZDIIS} for specification of the subspace size.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_THAUTO_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword THAUTO.
        ''')

    x_cpmd_input_LINRES_THAUTO_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword THAUTO.
        ''')


class x_cpmd_section_input_LINRES_ZDIIS(MSection):
    '''
    The subspace size for the optimizer is read from the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_ZDIIS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ZDIIS.
        ''')

    x_cpmd_input_LINRES_ZDIIS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ZDIIS.
        ''')


class x_cpmd_section_input_LINRES(MSection):
    '''
    General input for HARDNESS and TDDFT calculations
    '''

    m_def = Section(validate=False)

    x_cpmd_input_LINRES_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section LINRES even without a keyword.
        ''')

    x_cpmd_section_input_LINRES_DIFF_FORMULA = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES_DIFF_FORMULA'),
        repeats=True)

    x_cpmd_section_input_LINRES_GAUGE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES_GAUGE'),
        repeats=True)

    x_cpmd_section_input_LINRES_HTHRS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES_HTHRS'),
        repeats=True)

    x_cpmd_section_input_LINRES_OPTIMIZER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES_OPTIMIZER'),
        repeats=True)

    x_cpmd_section_input_LINRES_STEPLENGTH = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES_STEPLENGTH'),
        repeats=True)

    x_cpmd_section_input_LINRES_THAUTO = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES_THAUTO'),
        repeats=True)

    x_cpmd_section_input_LINRES_ZDIIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES_ZDIIS'),
        repeats=True)


class x_cpmd_section_input_PATH_ALPHA(MSection):
    '''
    Smoothing parameter for iterating the string (see \\cite{Eijnden06}). \\textbf{Default}
    value is \\defaultvalue{0.2}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PATH_ALPHA_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ALPHA.
        ''')

    x_cpmd_input_PATH_ALPHA_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ALPHA.
        ''')


class x_cpmd_section_input_PATH_FACTOR(MSection):
    '''
    Step for propagating string (see \\cite{Eijnden06}). \\textbf{Default} value is
    \\defaultvalue{1.0}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PATH_FACTOR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FACTOR.
        ''')

    x_cpmd_input_PATH_FACTOR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FACTOR.
        ''')


class x_cpmd_section_input_PATH_NEQUI(MSection):
    '''
    Number of equilibration steps discarded to calculate the mean force.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PATH_NEQUI_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NEQUI.
        ''')

    x_cpmd_input_PATH_NEQUI_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NEQUI.
        ''')


class x_cpmd_section_input_PATH_NLOOP(MSection):
    '''
    Maximum number of string searches for Mean Free Energy Path searches.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PATH_NLOOP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NLOOP.
        ''')

    x_cpmd_input_PATH_NLOOP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NLOOP.
        ''')


class x_cpmd_section_input_PATH_NPREVIOUS(MSection):
    '''
    String index to restart from. Note that this is just for numbering files, the initial
    path in collective variables for the search is always {\\em string.inp}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PATH_NPREVIOUS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NPREVIOUS.
        ''')

    x_cpmd_input_PATH_NPREVIOUS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NPREVIOUS.
        ''')


class x_cpmd_section_input_PATH_REPLICA_NUMBER(MSection):
    '''
    Number of replicas along the string.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PATH_REPLICA_NUMBER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REPLICA_NUMBER.
        ''')

    x_cpmd_input_PATH_REPLICA_NUMBER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REPLICA_NUMBER.
        ''')


class x_cpmd_section_input_PATH(MSection):
    '''
    Mean free energy path calculation (MFEP)
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PATH_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section PATH even without a keyword.
        ''')

    x_cpmd_section_input_PATH_ALPHA = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PATH_ALPHA'),
        repeats=True)

    x_cpmd_section_input_PATH_FACTOR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PATH_FACTOR'),
        repeats=True)

    x_cpmd_section_input_PATH_NEQUI = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PATH_NEQUI'),
        repeats=True)

    x_cpmd_section_input_PATH_NLOOP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PATH_NLOOP'),
        repeats=True)

    x_cpmd_section_input_PATH_NPREVIOUS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PATH_NPREVIOUS'),
        repeats=True)

    x_cpmd_section_input_PATH_REPLICA_NUMBER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PATH_REPLICA_NUMBER'),
        repeats=True)


class x_cpmd_section_input_PIMD_CENTROID_DYNAMICS(MSection):
    '''
    Adiabatic centroid molecular dynamics, see Ref.~\\cite{Cao93,Martyna96,aicmd} for
    theory and details of our implementation, which yields quasiclassical dynamics of the
    nuclear centroids at a specified temperature of the non--centroid modes. This keyword
    makes only sense if used in conjunction with the normal mode propagator via the
    keyword NORMAL MODES {\\em and} FACSTAGE~$>1.0$ {\\em and} WMASS~$=1.0$. The centroid
    adiabaticity control parameter FACSTAGE, which makes the non-centroid modes
    artificially fast in order to sample adiabatically the quantum fluctuations, has to be
    chosen carefully; note that FACSTAGE~$= 1/\\gamma$ as introduced in Ref.~\\cite{aicmd}
    in eq.~(2.51).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_CENTROID_DYNAMICS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CENTROID_DYNAMICS.
        ''')

    x_cpmd_input_PIMD_CENTROID_DYNAMICS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CENTROID_DYNAMICS.
        ''')


class x_cpmd_section_input_PIMD_CLASSICAL_TEST(MSection):
    '''
    Test option to reduce the path integral branch to the classical code for the special
    case $P=1$ in order to allow for a one-to-one comparison to a run using the standard
    branch of CPMD. It works only with primitive propagator, i.e.\\ not together with
    NORMAL MODES, STAGING and/or \\refkeyword{DEBROGLIE} CENTROID.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_CLASSICAL_TEST_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CLASSICAL_TEST.
        ''')

    x_cpmd_input_PIMD_CLASSICAL_TEST_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CLASSICAL_TEST.
        ''')


class x_cpmd_section_input_PIMD_DEBROGLIE(MSection):
    '''
    An initial configuration assuming quantum free particle behavior is generated for each
    individual atom according to its physical mass at the temperature given in Kelvin on
    the following input line.

    Using DEBROGLIE each nuclear position obtained from the \\&ATOMS \\ldots\\ \\&END section
    serves as the starting point for a Gaussian L\\'evy walk of length $P$ in three
    dimensions, see e.g.\\ Ref.~\\cite{Fosdick66}.

    Using DEBROGLIE CENTROID each nuclear position obtained from the \\&ATOMS \\ldots\\ \\&END
    section serves as the centroid (center of geometry) for obtaining the centroid (center
    of geometry) for obtaining the $P$ normal modes in three dimensions, see e.g.\\
    Ref.~\\cite{Tuckerman96}.

    This option does only specify the generation of the initial configuration if
    INITIALIZATION and GENERATE REPLICAS are active.

    Default is DEBROGLIE CENTROID and 500~Kelvin.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_DEBROGLIE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DEBROGLIE.
        ''')

    x_cpmd_input_PIMD_DEBROGLIE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DEBROGLIE.
        ''')


class x_cpmd_section_input_PIMD_FACMASS(MSection):
    '''
    Obtain the fictitious nuclear masses $M_I^\\prime$ within path integral molecular
    dynamics from the real physical atomic masses $M_I$ (as tabulated in the DATA ATWT /
    \\ldots /  statement in atoms.F) by {\\em multiplying} them with the dimensionless
    factor WMASS that is read from the following line; if the NORMAL MODES or STAGING
    propagator is used obtain $M_I^{\\prime (s)}= \\mbox{WMASS} \\cdot M_I^{(s)}$ for {\\em
    all} replicas $s=1, \\dots , P$; see e.g. Ref.~\\cite{aicmd} eq.~(2.37) for
    nomenclature.  \\textbf{Default} value of WMASS is \\defaultvalue{1.0}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_FACMASS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FACMASS.
        ''')

    x_cpmd_input_PIMD_FACMASS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FACMASS.
        ''')


class x_cpmd_section_input_PIMD_GENERATE_REPLICAS(MSection):
    '''
    Generate quantum free particle replicas from scratch given a classical input
    configuration according to the keyword \\refkeyword{DEBROGLIE} specification.

    This is the default if \\refkeyword{INITIALIZATION} is active.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_GENERATE_REPLICAS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword GENERATE_REPLICAS.
        ''')

    x_cpmd_input_PIMD_GENERATE_REPLICAS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword GENERATE_REPLICAS.
        ''')


class x_cpmd_section_input_PIMD_INITIALIZATION(MSection):
    '''
    Provide an initial configuration for all replicas as specified either by
    \\refkeyword{GENERATE REPLICAS} or by \\refkeyword{READ REPLICAS}.

    This option is automatically activated if \\refkeyword{RESTART} COORDINATES is not
    specified.

    It is defaulted to GENERATE REPLICAS together with \\refkeyword{DEBROGLIE} CENTROID and
    a temperature of 500~Kelvin.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_INITIALIZATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword INITIALIZATION.
        ''')

    x_cpmd_input_PIMD_INITIALIZATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword INITIALIZATION.
        ''')


class x_cpmd_section_input_PIMD_NORMAL_MODES(MSection):
    '''
    Use the normal mode representation~\\cite{Tuckerman96} of the path integral propagator.
    It is possible to impose a mass disparity between centroid and non--centroid
    coordinates by dividing the fictitious masses of only the {\\em non}--centroid $s=2,
    \\dots ,P$ replicas by the adiabaticity control factor FACSTAGE. This dimensionless
    factor {\\em must always} be specified in the following line. Note: the eigen--{\\em
    frequencies} of the $s>1$ replicas are changed by only $\\sqrt{\\mbox{FACSTAGE}}$, see
    Ref.~\\cite{Martyna96}(b). Using FACSTAGE~$\\not= 1.0$ makes only sense in conjunction
    with CENTROID DYNAMICS where WMASS=1.0 has to be used as well.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_NORMAL_MODES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NORMAL_MODES.
        ''')

    x_cpmd_input_PIMD_NORMAL_MODES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NORMAL_MODES.
        ''')


class x_cpmd_section_input_PIMD_OUTPUT(MSection):
    '''
    Output files for each processor, processor group, or only grandparent.

    Default is PARENT to standard output file (Note: some information such as messages for
    correct reading~/ writing of restart files is lost); GROUPS and ALL write to the files
    OUTPUT\\_$n$ where $n$ is the group and bead number, respectively.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_OUTPUT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OUTPUT.
        ''')

    x_cpmd_input_PIMD_OUTPUT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OUTPUT.
        ''')


class x_cpmd_section_input_PIMD_PRINT_LEVEL(MSection):
    '''
    The detail of printing information is read as an integer number from the next line.

    Currently there is only minimal output for $<5$ and maximal output for $\\geq 5$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_PRINT_LEVEL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRINT_LEVEL.
        ''')

    x_cpmd_input_PIMD_PRINT_LEVEL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRINT_LEVEL.
        ''')


class x_cpmd_section_input_PIMD_PROCESSOR_GROUPS(MSection):
    '''
    % This is only needed for {\\em fine}--tuning load balancing in case of path integral
    runs {\\em iff} two level parallelization is used. The default optimizes the combined
    load balancing of the parallelization over replicas and g--vectors. The default load
    distribution is usually optimal. Separate the total number of processors into a
    certain number of processor groups that is read from the following line; only 2$^N$ =
    2, 4, 8, 16, $\\dots$ groups are allowed and the maximum number of groups is the number
    of replicas. Every processor group is headed by one PARENT and has several CHILDREN
    that work together on a single replica at one time; the processor groups work
    sequentially on replicas if there is more than one replica assigned to one processor
    group.

    Note: if the resulting number of processor groups is much smaller than the number of
    replicas (which occurs in ``odd'' cases) specifying the number of processor groups to
    be equal to the number of replicas might be more efficient.

    This keyword is only active in parallel mode.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_PROCESSOR_GROUPS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PROCESSOR_GROUPS.
        ''')

    x_cpmd_input_PIMD_PROCESSOR_GROUPS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PROCESSOR_GROUPS.
        ''')


class x_cpmd_section_input_PIMD_READ_REPLICAS(MSection):
    '''
    Read all $P$ replicas from a file with a name to be specified in the following line,
    for the input format see subroutine rreadf.F.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_READ_REPLICAS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword READ_REPLICAS.
        ''')

    x_cpmd_input_PIMD_READ_REPLICAS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword READ_REPLICAS.
        ''')


class x_cpmd_section_input_PIMD_STAGING(MSection):
    '''
    Use the staging representation~\\cite{Tuckerman96} of the path integral propagator. It
    is possible to impose a mass disparity between centroid and non--centroid coordinates
    by dividing the fictitous masses of only the {\\em non}--centroid $s=2, \\dots ,P$
    replicas by the adiabaticity control factor FACSTAGE. This dimensionless factor {\\em
    must always} be specified in the following line. Note: the eigen--{\\em frequencies} of
    the $s>1$ replicas are changed by only $\\sqrt{\\mbox{FACSTAGE}}$, see
    Ref.~\\cite{Martyna96}(b). Note: using FACSTAGE~$\\not= 1.0$ essentially makes no sense
    within the STAGING scheme, but see its use within CENTROID DYNAMICS and NORMAL MODES.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_STAGING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword STAGING.
        ''')

    x_cpmd_input_PIMD_STAGING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword STAGING.
        ''')


class x_cpmd_section_input_PIMD_TROTTER_DIMENSION(MSection):
    '''
    The Trotter number $P$, i.e. the number of ``replicas'', ``beads'', or ``imaginary
    time slices'' which are used in order to discretize the Feynman--Kac path integral of
    the nuclei, is read from the next line. If NORMAL MODES or STAGING is not activated
    the path integral is discretized in cartesian coordinates in real space (so--called
    ``primitive coordinates''). A discussion about controlling discretization errors and
    on estimating $P$ in advance is given in Ref.~\\cite{knoll-marx-00}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_TROTTER_DIMENSION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TROTTER_DIMENSION.
        ''')

    x_cpmd_input_PIMD_TROTTER_DIMENSION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TROTTER_DIMENSION.
        ''')


class x_cpmd_section_input_PIMD(MSection):
    '''
    Path integral molecular dynamics (PIMD)
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PIMD_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section PIMD even without a keyword.
        ''')

    x_cpmd_section_input_PIMD_CENTROID_DYNAMICS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_CENTROID_DYNAMICS'),
        repeats=True)

    x_cpmd_section_input_PIMD_CLASSICAL_TEST = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_CLASSICAL_TEST'),
        repeats=True)

    x_cpmd_section_input_PIMD_DEBROGLIE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_DEBROGLIE'),
        repeats=True)

    x_cpmd_section_input_PIMD_FACMASS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_FACMASS'),
        repeats=True)

    x_cpmd_section_input_PIMD_GENERATE_REPLICAS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_GENERATE_REPLICAS'),
        repeats=True)

    x_cpmd_section_input_PIMD_INITIALIZATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_INITIALIZATION'),
        repeats=True)

    x_cpmd_section_input_PIMD_NORMAL_MODES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_NORMAL_MODES'),
        repeats=True)

    x_cpmd_section_input_PIMD_OUTPUT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_OUTPUT'),
        repeats=True)

    x_cpmd_section_input_PIMD_PRINT_LEVEL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_PRINT_LEVEL'),
        repeats=True)

    x_cpmd_section_input_PIMD_PROCESSOR_GROUPS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_PROCESSOR_GROUPS'),
        repeats=True)

    x_cpmd_section_input_PIMD_READ_REPLICAS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_READ_REPLICAS'),
        repeats=True)

    x_cpmd_section_input_PIMD_STAGING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_STAGING'),
        repeats=True)

    x_cpmd_section_input_PIMD_TROTTER_DIMENSION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD_TROTTER_DIMENSION'),
        repeats=True)


class x_cpmd_section_input_PROP_AVERAGED_POTENTIAL(MSection):
    '''
    Calculate averaged electrostatic potential in spheres of radius Rcut around the atomic
    positions.   Parameter Rcut is read in from next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_AVERAGED_POTENTIAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword AVERAGED_POTENTIAL.
        ''')

    x_cpmd_input_PROP_AVERAGED_POTENTIAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword AVERAGED_POTENTIAL.
        ''')


class x_cpmd_section_input_PROP_CHARGES(MSection):
    '''
    Calculate atomic charges. Charges are calculated according to the method of
    Hirshfeld~\\cite{Hirshfeld77} and charges derived from the electrostatic
    potential~\\cite{Cox84}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_CHARGES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CHARGES.
        ''')

    x_cpmd_input_PROP_CHARGES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CHARGES.
        ''')


class x_cpmd_section_input_PROP_CONDUCTIVITY(MSection):
    '''
    Computes the optical conductivity according to the Kubo-Greenwod formula
    \\begin{equation*} \\sigma(\\omega) = \\frac{2 \\pi e^2}{3m^2 V_{\\rm cell}} \\frac{1}{\\omega
    } \\sum_{i,j} (f_i-f_j) |\\langle \\psi _i| \\hat{\\bf p} |\\psi _j \\rangle |^2
    \\delta(\\epsilon _i -\\epsilon_j - \\hbar \\omega) \\label{condu} \\end{equation*} where
    $\\psi _i$ are the Kohn-Sham eigenstates, $\\epsilon _i$ their corresponding
    eigenvalues, $f_i$ the occupation number and the difference $f_i-f_j$ takes care of
    the fermionic occupancy. This calculation is executed when the keyword PROPERTIES is
    used in the section \\&CPMD ... \\&END. In the section \\&PROP ... \\&END the keyword
    CONDUCTIVITY must be present and the interval interval $\\Delta \\omega$ for the
    calculation of the spectrum is read from the next line. Note that, since this is a
    "PROPERTIES" calculation, {\\it you must have previously computed the electronic
    structure of your system and have a consistent \\refkeyword{RESTART} file ready to
    use}. Further keyword: \\texttt{STEP=0.14}, where (e.g.) 0.14 is the bin width in eV of
    the $\\sigma(\\omega)$ histogram if you want it to be different from $\\Delta \\omega$. A
    file MATRIX.DAT is written in your working directory, where all the non-zero
    transition amplitudes and related informations are reported (see the header of
    MATRIX.DAT). An example of application is given in Refs.~\\cite{solve,solve2}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_CONDUCTIVITY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CONDUCTIVITY.
        ''')

    x_cpmd_input_PROP_CONDUCTIVITY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CONDUCTIVITY.
        ''')


class x_cpmd_section_input_PROP_CORE_SPECTRA(MSection):
    '''
    Computes the X-ray adsorption spectrum and related transition matrix elements
    according to Ref.~\\cite{xray}. This calculation is executed when the keyword
    PROPERTIES is used in the section \\&CPMD ... \\&END. In the section \\&PROP ... \\&END
    the keyword CORE SPECTRA must be present and the core atom number (e.g. 10 if it is
    the 10$th$ atom in your list) and core level energy (in au) are read from the next
    line, while in the following line the $n$ and $l$ quantum numbers of the selected core
    level, along with the exponential factor $a$ of the STO orbital for the core level
    must be provided. In the case of $1s$ states, the core orbital is reconstructed as
    \\begin{equation*} \\psi _{1s}(r) = 2 a^{\\frac{3}{2}} r \\cdot \\exp (-a\\cdot r)
    \\label{1s} \\end{equation*} and it is this $a$ value in au that must be supplied in
    input. As a general rule, first-row elements in the neutral case have the following
    $a$ values: B (4.64), C (5.63), N (6.62), O (7.62). For an excited atom these values
    would be of course a bit larger; e.g. for O it is 7.74453, i.e. 1.6 \\% larger. Since
    this is a "PROPERTIES" calculation, {\\it you must have previously computed the
    electronic structure of your system and have a consistent \\refkeyword{RESTART} file
    ready to use}. A file XRAYSPEC.DAT is written in your working directory, containing
    all the square transition amplitudes and related informations, part of which are also
    written in the standard output. Waring: in order to use this keyword you need special
    pseudopotentials. These are provided, at least for some elements, in the PP library of
    CPMD and are named as *\\_HOLE.psp
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_CORE_SPECTRA_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CORE_SPECTRA.
        ''')

    x_cpmd_input_PROP_CORE_SPECTRA_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CORE_SPECTRA.
        ''')


class x_cpmd_section_input_PROP_CUBECENTER(MSection):
    '''
    Sets the center of the cubefiles produced by the \\refkeyword{CUBEFILE} flag. The next
    line has to contain the coordinates of the center in Bohr or Angstrom, depending on
    whether the \\refkeyword{ANGSTROM} keyword was given. \\textbf{Default} is the geometric
    center of the system.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_CUBECENTER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CUBECENTER.
        ''')

    x_cpmd_input_PROP_CUBECENTER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CUBECENTER.
        ''')


class x_cpmd_section_input_PROP_CUBEFILE(MSection):
    '''
    Plots the requested objects in .CUBE file format. If ORBITALS are demanded, the total
    number as well as the indices have to be given on the next and second next line.
    HALFMESH reduces the number of grid points per direction by 2, thus reducing the file
    size by a factor of 8.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_CUBEFILE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CUBEFILE.
        ''')

    x_cpmd_input_PROP_CUBEFILE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CUBEFILE.
        ''')


class x_cpmd_section_input_PROP_DIPOLE_MOMENT(MSection):
    '''
    Calculate the dipole moment.

    Without the additional keywords {\\bf BERRY} or {\\bf RS} this is only implemented for
    simple cubic and fcc supercells. The keyword {\\bf RS} requests the use of the real-
    space algorithm. The keyword {\\bf BERRY} requests the use of the Berry phase
    algorithm.

    {\\bf Default} is to use the real-space algorithm.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_DIPOLE_MOMENT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DIPOLE_MOMENT.
        ''')

    x_cpmd_input_PROP_DIPOLE_MOMENT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DIPOLE_MOMENT.
        ''')


class x_cpmd_section_input_PROP_EXCITED_DIPOLE(MSection):
    '''
    Calculate the difference of dipole moments between the ground state density and a
    density generated by differently occupied Kohn-Sham orbitals.  On the next line the
    number of dipole moments to calculate and the total number orbitals has to be given.
    On the following lines the occupation of the states for each calculation has to be
    given. By default the dipoles are calculated by the method used for the {\\bf DIPOLE
    MOMENT} option and the same restrictions apply. If the {\\bf LOCAL DIPOLE} option is
    specified the dipole moment differences are calculated within the same boxes.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_EXCITED_DIPOLE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXCITED_DIPOLE.
        ''')

    x_cpmd_input_PROP_EXCITED_DIPOLE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXCITED_DIPOLE.
        ''')


class x_cpmd_section_input_PROP_LDOS(MSection):
    '''
    Calculate the layer projected density of states. The number of layers is read from the
    next line.  To use the LDOS keyword, the user must first have performed a wavefunction
    optimization and then restart with with the \\refkeyword{PROPERTIES} and
    \\refkeyword{LANCZOS DIAGONALIZATION} keywords in the \\&CPMD section (and LDOS in the
    \\&PROP section).  \\textbf{Warning:} If you use special k-points for a special
    structure you need to symmetrize charge density for which you must specify the
    \\refkeyword{POINT GROUP}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_LDOS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LDOS.
        ''')

    x_cpmd_input_PROP_LDOS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LDOS.
        ''')


class x_cpmd_section_input_PROP_LOCAL_DIPOLE(MSection):
    '''
    Calculate $numloc$ local dipole moments.  $numloc$ is read from the next line followed
    by two numloc lines with the format: \\\\  $xmin$ $ymin$ $zmin$ \\\\  $xmax$ $ymax$ $zmax$
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_LOCAL_DIPOLE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LOCAL_DIPOLE.
        ''')

    x_cpmd_input_PROP_LOCAL_DIPOLE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LOCAL_DIPOLE.
        ''')


class x_cpmd_section_input_PROP_LOCALIZE(MSection):
    '''
    Localize the molecular orbitals \\cite{Hutter94b} as defined through the atomic basis
    set.  The same localization transformation is then applied also to the wavefunctions
    in the plane wave basis. These wavefunction can be printed with the keyword {\\bf
    RHOOUT} specified in the section \\&CPMD section.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_LOCALIZE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LOCALIZE.
        ''')

    x_cpmd_input_PROP_LOCALIZE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LOCALIZE.
        ''')


class x_cpmd_section_input_PROP_NOPRINT_ORBITALS(MSection):
    '''
    Do not print the wavefunctions in the atomic basis set.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_NOPRINT_ORBITALS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NOPRINT_ORBITALS.
        ''')

    x_cpmd_input_PROP_NOPRINT_ORBITALS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NOPRINT_ORBITALS.
        ''')


class x_cpmd_section_input_PROP_OPTIMIZE_SLATER_EXPONENTS(MSection):
    '''
    Not documented
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_OPTIMIZE_SLATER_EXPONENTS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OPTIMIZE_SLATER_EXPONENTS.
        ''')

    x_cpmd_input_PROP_OPTIMIZE_SLATER_EXPONENTS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OPTIMIZE_SLATER_EXPONENTS.
        ''')


class x_cpmd_section_input_PROP_POLARISABILITY(MSection):
    '''
    Computes the polarisability of a system, intended as dipole moment per unit volume.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_POLARISABILITY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword POLARISABILITY.
        ''')

    x_cpmd_input_PROP_POLARISABILITY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword POLARISABILITY.
        ''')


class x_cpmd_section_input_PROP_POPULATION_ANALYSIS(MSection):
    '''
    The type of population analysis that is performed with the projected wavefunctions.
    L\\"owdin charges are given with both options. For the Davidson
    analysis~\\cite{Davidson67} the maximum complexity can be specified with the keyword
    {\\bf n-CENTER}. Default for n is 2, terms up to 4 are programmed. For the Davidson
    option one has to specify the number of atomic orbitals that are used in the analysis.
    For each species one has to give this number in a separate line. An input example for
    a water molecule is given in the hints section \\ref{hints:pop}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_POPULATION_ANALYSIS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword POPULATION_ANALYSIS.
        ''')

    x_cpmd_input_PROP_POPULATION_ANALYSIS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword POPULATION_ANALYSIS.
        ''')


class x_cpmd_section_input_PROP_PROJECT_WAVEFUNCTION(MSection):
    '''
    The wavefunctions are projected on atomic orbitals.  The projected wavefunctions are
    then used to calculate atomic populations and bond orders. The atomic orbitals to
    project on are taken from the \\&BASIS section. If there is no \\&BASIS section in the
    input a minimal Slater basis is used. See section~\\ref{input:basis} for more details.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_PROJECT_WAVEFUNCTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PROJECT_WAVEFUNCTION.
        ''')

    x_cpmd_input_PROP_PROJECT_WAVEFUNCTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PROJECT_WAVEFUNCTION.
        ''')


class x_cpmd_section_input_PROP_TRANSITION_MOMENT(MSection):
    '''
    Calculate the dipole transition matrix element.

    On the following lines, the number of transitions and the involved orbitals are given.
    Example:  {\\tt \\begin{tabular}{ccc} \\multicolumn{2}{l}{\\bf TRANSITION MOMENT} 2 &   6
    & 7 6 & 8 \\end{tabular} }

    This calculates the dipole transition matrix elements between KS states 6 and 7, and
    between 6 and 8.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_TRANSITION_MOMENT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TRANSITION_MOMENT.
        ''')

    x_cpmd_input_PROP_TRANSITION_MOMENT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TRANSITION_MOMENT.
        ''')


class x_cpmd_section_input_PROP(MSection):
    '''
    Calculation of properties
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PROP_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section PROP even without a keyword.
        ''')

    x_cpmd_section_input_PROP_AVERAGED_POTENTIAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_AVERAGED_POTENTIAL'),
        repeats=True)

    x_cpmd_section_input_PROP_CHARGES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_CHARGES'),
        repeats=True)

    x_cpmd_section_input_PROP_CONDUCTIVITY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_CONDUCTIVITY'),
        repeats=True)

    x_cpmd_section_input_PROP_CORE_SPECTRA = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_CORE_SPECTRA'),
        repeats=True)

    x_cpmd_section_input_PROP_CUBECENTER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_CUBECENTER'),
        repeats=True)

    x_cpmd_section_input_PROP_CUBEFILE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_CUBEFILE'),
        repeats=True)

    x_cpmd_section_input_PROP_DIPOLE_MOMENT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_DIPOLE_MOMENT'),
        repeats=True)

    x_cpmd_section_input_PROP_EXCITED_DIPOLE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_EXCITED_DIPOLE'),
        repeats=True)

    x_cpmd_section_input_PROP_LDOS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_LDOS'),
        repeats=True)

    x_cpmd_section_input_PROP_LOCAL_DIPOLE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_LOCAL_DIPOLE'),
        repeats=True)

    x_cpmd_section_input_PROP_LOCALIZE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_LOCALIZE'),
        repeats=True)

    x_cpmd_section_input_PROP_NOPRINT_ORBITALS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_NOPRINT_ORBITALS'),
        repeats=True)

    x_cpmd_section_input_PROP_OPTIMIZE_SLATER_EXPONENTS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_OPTIMIZE_SLATER_EXPONENTS'),
        repeats=True)

    x_cpmd_section_input_PROP_POLARISABILITY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_POLARISABILITY'),
        repeats=True)

    x_cpmd_section_input_PROP_POPULATION_ANALYSIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_POPULATION_ANALYSIS'),
        repeats=True)

    x_cpmd_section_input_PROP_PROJECT_WAVEFUNCTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_PROJECT_WAVEFUNCTION'),
        repeats=True)

    x_cpmd_section_input_PROP_TRANSITION_MOMENT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP_TRANSITION_MOMENT'),
        repeats=True)


class x_cpmd_section_input_PTDDFT_ACCURACY(MSection):
    '''
    Specifies the accuracy to be reached in the Cayley propagation scheme used in
    Ehrenfest type of dynamics and spectra calculation.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PTDDFT_ACCURACY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ACCURACY.
        ''')

    x_cpmd_input_PTDDFT_ACCURACY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ACCURACY.
        ''')


class x_cpmd_section_input_PTDDFT_PIPULSE(MSection):
    '''
    Specifies a time dependent pi-pulse to be used with MOLECULAR DYNAMICS EH. Use PIPULSE
    together with TD\\_POTENTIAL. The pulse strength is read from the next line (see
    subroutine gaugepot\\_laser in td\\_util.F for further details).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PTDDFT_PIPULSE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PIPULSE.
        ''')

    x_cpmd_input_PTDDFT_PIPULSE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PIPULSE.
        ''')


class x_cpmd_section_input_PTDDFT_RESTFILE(MSection):
    '''
    Defines a restart code for the restart of the Ehrenfest dynamics
    (\\refkeyword{MOLECULAR DYNAMICS} EH) and the propagation spectra
    (\\refkeyword{PROPAGATION SPECTRA}). The restart option is read from the next line:
    0(=default) restart from the (complex)wavefunctions in the file wavefunctions. This
    option is used in case of a continuation run; 1. restart from the the orbital files
    WAVEFUNCTION.n, where $n$ is the index of the KS orbital and runs from $1$ to the
    number of s tates (This states a prepare in a previuos run using the KOHN-SHAM
    ENERGIES principal keyward), 2; restart from the orbitals stored in RESTART (obtained
    from a optimization run with tight convergence (at least 1.D-7)).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PTDDFT_RESTFILE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RESTFILE.
        ''')

    x_cpmd_input_PTDDFT_RESTFILE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RESTFILE.
        ''')


class x_cpmd_section_input_PTDDFT(MSection):
    '''
    Propagation TDDFT for Ehrenfest dynamics and spectra calculation
    '''

    m_def = Section(validate=False)

    x_cpmd_input_PTDDFT_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section PTDDFT even without a keyword.
        ''')

    x_cpmd_section_input_PTDDFT_ACCURACY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PTDDFT_ACCURACY'),
        repeats=True)

    x_cpmd_section_input_PTDDFT_PIPULSE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PTDDFT_PIPULSE'),
        repeats=True)

    x_cpmd_section_input_PTDDFT_RESTFILE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PTDDFT_RESTFILE'),
        repeats=True)


class x_cpmd_section_input_QMMM_AMBER(MSection):
    '''
    An Amber functional form for the classical force field is used. In this case
    coordinates and topology files as obtained by Amber have to be converted in Gromos
    format just for input/read consistency. This is done with the tool amber2gromos
    availabe with the CPMD/QMMM package. This keyword is mutually exclusive with the
    \\refkeyword{GROMOS} keyword (which is used by default).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_AMBER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword AMBER.
        ''')

    x_cpmd_input_QMMM_AMBER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword AMBER.
        ''')


class x_cpmd_section_input_QMMM_BOX_TOLERANCE(MSection):
    '''
    The value for the box tolerance is read from the next line. In a QM/MM calculation the
    size of the QM-box is fixed and the QM-atoms must not come to close to the walls of
    this box. On top of always recentering the QM-box around the center of the
    distribution of the atoms, CPMD prints a warning message to the output when the
    distribution extends too much to fit into the QM-box properly anymore. This value may
    need to be adjusted to the requirements of the Poisson solver used (see section
    \\ref{hints:symm0}). {\\bf Default} value is 8~a.u.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_BOX_TOLERANCE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BOX_TOLERANCE.
        ''')

    x_cpmd_input_QMMM_BOX_TOLERANCE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BOX_TOLERANCE.
        ''')


class x_cpmd_section_input_QMMM_BOX_WALLS(MSection):
    '''
    The thickness parameter for soft, reflecting QM-box walls is read from the next line.
    This keyword allows to reverse the momentum of the particles (${\\bf p}_I \\rightarrow
    -{\\bf p}_I$) when they reach the walls of the simulation supercell similar to the full
    quantum case, but acting along all the three directions $x,y,z$. In the case this
    keyword is used in the \\&QMMM section,QM  particles are reflected back in the QM box.
    Contrary to the normal procedure of re-centering the QM-box, a soft, reflecting
    confinement potential is applied if atoms come too close to the border of the QM
    box~\\cite{box-walls}. It is highly recommended to also use \\refkeyword{SUBTRACT}
    COMVEL in combination with this feature. {\\bf NOTE:} to have your QM-box properly
    centered, it is best to run a short MD with this feature turned off and then start
    from the resulting restart with the soft walls turned on. Since the reflecting walls
    reverse the sign of the velocities, ${\\bf p}_I \\to -{\\bf p}_I$ ($I$ = QM atom index),
    be aware that this options affects the momentum conservation in your QM subsystem.
    This feature is {\\bf disabled by default}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_BOX_WALLS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword BOX_WALLS.
        ''')

    x_cpmd_input_QMMM_BOX_WALLS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword BOX_WALLS.
        ''')


class x_cpmd_section_input_QMMM_CAPPING(MSection):
    '''
    Add (dummy) hydrogen atoms to the QM-system to saturate dangling bonds when cutting
    between MM- and QM-system. This needs a special pseudopotential entry in the \\&ATOMS
    section (see section \\ref{sec:qmmm-cut-bonds} for more details).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_CAPPING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CAPPING.
        ''')

    x_cpmd_input_QMMM_CAPPING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CAPPING.
        ''')


class x_cpmd_section_input_QMMM_COORDINATES(MSection):
    '''
    On the next line the name of a Gromos96 format coordinate file has to be given. Note,
    that this file must match the corresponding input and topology files. Note, that in
    case of hydrogen capping, this file has to be modified to also contain the respective
    dummy hydrogen atoms.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_COORDINATES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword COORDINATES.
        ''')

    x_cpmd_input_QMMM_COORDINATES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword COORDINATES.
        ''')


class x_cpmd_section_input_QMMM_ELECTROSTATIC_COUPLING(MSection):
    '''
    The electrostatic interaction of the quantum system with the classical system is
    explicitly kept into account for all classical atoms  at a  distance $r \\leq
    $~\\refspekeyword{RCUT\\_NN}{RCUT-NN} from any quantum atom and for all the MM  atoms at
    a distance of \\refspekeyword{RCUT\\_NN}{RCUT-NN}~$< r
    \\leq$~\\refspekeyword{RCUT\\_MIX}{RCUT-MIX} and a charge larger than $0.1 e_0$ (NN
    atoms).  MM-atoms with a charge smaller than $0.1 e_0$ and a distance of
    \\refspekeyword{RCUT\\_NN}{RCUT-NN}~$< r \\leq$~\\refspekeyword{RCUT\\_MIX}{RCUT-MIX} and
    all MM-atoms with \\refspekeyword{RCUT\\_MIX}{RCUT-MIX}~$< r
    \\leq$~\\refspekeyword{RCUT\\_ESP}{RCUT-ESP} are coupled  to the QM system by a ESP
    coupling Hamiltonian (EC atoms).  If the additional \\texttt{LONG RANGE} keyword is
    specified, the interaction of the QM-system with the rest of the classical atoms is
    explicitly kept into account via interacting with a multipole expansion for the QM-
    system up to quadrupolar order. A file named \\texttt{MULTIPOLE} is produced.  If
    \\texttt{LONG RANGE} is omitted the quantum system is coupled to the classical atoms
    not in the NN-area and in the EC-area list via the force-field charges.  If the
    keyword \\texttt{ELECTROSTATIC COUPLING} is omitted, all classical atoms are coupled to
    the quantum system by the force-field charges (mechanical coupling).  The files
    INTERACTING.pdb, TRAJECTORY\\_INTERACTING, MOVIE\\_INTERACTING, TRAJ\\_INT.dcd, and ESP
    (or some of them) are created. The list of NN and EC atoms is updated every 100 MD
    steps. This can be changed using the keyword \\refkeyword{UPDATE LIST}.  The default
    values for the cut-offs are RCUT\\_NN=RCUT\\_MIX=RCUT\\_ESP=10 a.u.. These values can be
    changed by the keywords \\refspekeyword{RCUT\\_NN}{RCUT-NN},
    \\refspekeyword{RCUT\\_MIX}{RCUT-MIX}, and \\refspekeyword{RCUT\\_ESP}{RCUT-ESP} with
    $r_{nn} \\leq r_{mix} \\leq r_{esp}$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_ELECTROSTATIC_COUPLING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ELECTROSTATIC_COUPLING.
        ''')

    x_cpmd_input_QMMM_ELECTROSTATIC_COUPLING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ELECTROSTATIC_COUPLING.
        ''')


class x_cpmd_section_input_QMMM_ESPWEIGHT(MSection):
    '''
    The ESP-charg fit weighting parameter is read from the next line. {\\bf Default} value
    is $0.1 e_0$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_ESPWEIGHT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ESPWEIGHT.
        ''')

    x_cpmd_input_QMMM_ESPWEIGHT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ESPWEIGHT.
        ''')


class x_cpmd_section_input_QMMM_EXCLUSION(MSection):
    '''
    Specify charge interactions that should be excluded from the QM/MM hamiltonian. With
    the additional flag GROMOS, the exclusions from the Gromos topology are used. With the
    additional flag LIST, an explicit list is read from following lines. The format of
    that list has the number of exclusions in the first line and then the exclusions
    listed in pairs of numbers of the QM atom and the MM atom in Gromos ordering; the
    optional flag NORESP in this case requests usage of MM point charges for the QM atoms
    instead of the D-RESP charges (default).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_EXCLUSION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXCLUSION.
        ''')

    x_cpmd_input_QMMM_EXCLUSION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXCLUSION.
        ''')


class x_cpmd_section_input_QMMM_FLEXIBLE_WATER(MSection):
    '''
    Convert some solven water molecules into solute molecules and thus using a flexible
    potential. With the BONDTYPE flag, the three bond potentials (OH1, OH2, and H1H2) can
    be given as index in the BONDTYPE section of the Gromos topology file. Note that the
    {\\bf non-bonded} parameters are taken from the SOLVENATOM section of the
    \\refkeyword{TOPOLOGY} file. {\\bf Default} is to use the values: 35, 35, 41. With the
    additional flag ALL this applies to all solvent water molecules, otherwise on the next
    line the number of flexible water molecules has to be given with the Gromos index
    numbers of their respective Oxygen atoms on the following line(s). On successful
    conversion a new, adapted topology file, MM\\_TOPOLOGY, is written that has to be used
    with the \\refkeyword{TOPOLOGY} keyword for subsequent restarts. Also the
    \\refkeyword{INPUT} file has to be adapted: in the SYSTEM section the number of solvent
    molecules has to be reduced by the number of converted molecules, and in the
    SUBMOLECULES section the new solute atoms have to be added accordingly.\\\\ Example:
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_FLEXIBLE_WATER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FLEXIBLE_WATER.
        ''')

    x_cpmd_input_QMMM_FLEXIBLE_WATER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FLEXIBLE_WATER.
        ''')


class x_cpmd_section_input_QMMM_GROMOS(MSection):
    '''
    A Gromos functional form for the classical force field is used (this is the default).
    This keyword is mutually exclusive with the \\refkeyword{AMBER} keyword.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_GROMOS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword GROMOS.
        ''')

    x_cpmd_input_QMMM_GROMOS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword GROMOS.
        ''')


class x_cpmd_section_input_QMMM_HIRSHFELD(MSection):
    '''
    With this option, restraints to Hirshfeld charges~\\cite{Hirshfeld77} can be turned on
    or off {\\bf Default} value is ON.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_HIRSHFELD_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HIRSHFELD.
        ''')

    x_cpmd_input_QMMM_HIRSHFELD_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HIRSHFELD.
        ''')


class x_cpmd_section_input_QMMM_INPUT(MSection):
    '''
    On the next line the name of a Gromos input file has to be given. A short summary of
    the input file syntax and some keywords are in section \\ref{sec:qmmm-gromos-inp}.
    Note, that it has to be a correct input file, even though many options do not apply
    for QM/MM runs.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_INPUT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword INPUT.
        ''')

    x_cpmd_input_QMMM_INPUT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword INPUT.
        ''')


class x_cpmd_section_input_QMMM_MAXNN(MSection):
    '''
    Then maximum number of NN atoms, i.e. the number of atoms coupled to the QM system via
    \\refkeyword{ELECTROSTATIC COUPLING} is read from the next line. (Note: This keyword
    was renamed from MAXNAT in older versions of the QM/MM interface code to avoid
    confusion with the MAXNAT keyword in the \\refkeyword{ARRAYSIZES ... END ARRAYSIZES}
    block.) {\\bf Default} value is 5000.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_MAXNN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MAXNN.
        ''')

    x_cpmd_input_QMMM_MAXNN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MAXNN.
        ''')


class x_cpmd_section_input_QMMM_NOSPLIT(MSection):
    '''
    If the program is run on more than one node, the MM forces calculation is performed on
    all nodes. Since the MM part is not parallelized, this is mostly useful for systems
    with a small MM-part and for runs using only very few nodes. Usually the QM part of
    the calculation needs the bulk of the cpu-time in the QM/MM. This setting is the
    default. See also under \\refkeyword{SPLIT}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_NOSPLIT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NOSPLIT.
        ''')

    x_cpmd_input_QMMM_NOSPLIT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NOSPLIT.
        ''')


class x_cpmd_section_input_QMMM_RESTART_TRAJECTORY(MSection):
    '''
    Restart the MD with coordinates and velocities from a previous run. With the
    additional flag FRAME followed by the frame number the trajectory frame can be
    selected. With the flag FILE followed by the name of the trajectory file, the filename
    can be set (Default is TRAJECTORY). Finally the flag REVERSE will reverse the sign of
    the velocities, so the system will move backwards from the selected point in the
    trajecory.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_RESTART_TRAJECTORY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RESTART_TRAJECTORY.
        ''')

    x_cpmd_input_QMMM_RESTART_TRAJECTORY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RESTART_TRAJECTORY.
        ''')


class x_cpmd_section_input_QMMM_SAMPLE_INTERACTING(MSection):
    '''
    The sampling rate for writing a trajectory of the interacting subsystem is read from
    the next line. With the additional keyword OFF or a sampling rate of 0, those
    trajectories are not written. The coordinates of the atoms atoms contained in the file
    INTERACTING.pdb are written, in the same order, on the file TRAJECTORY\\_INTERACTING
    every.  If the \\refkeyword{MOVIE} output is turned on, a file MOVIE\\_INTERACTING is
    written as well.  With the additional keyword DCD the file TRAJ\\_INT.dcd is also
    written to. if the sampling rate is negative, then \\textbf{only} the TRAJ\\_INT.dcd is
    written.  {\\bf Default} value is 5 for MD calculations and OFF for others.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_SAMPLE_INTERACTING_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SAMPLE_INTERACTING.
        ''')

    x_cpmd_input_QMMM_SAMPLE_INTERACTING_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SAMPLE_INTERACTING.
        ''')


class x_cpmd_section_input_QMMM_SPLIT(MSection):
    '''
    If the program is run on more than one node, the MM forces calculation is performed on
    a separate node. This is mostly useful for systems with a large MM-part and runs with
    many nodes where the accumulated time used for the classical part has a larger impact
    on the performace than losing one node for the (in total) much more time consuming QM-
    part. {\\bf Default} is \\refkeyword{NOSPLIT}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_SPLIT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SPLIT.
        ''')

    x_cpmd_input_QMMM_SPLIT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SPLIT.
        ''')


class x_cpmd_section_input_QMMM_TIMINGS(MSection):
    '''
    Display timing information about the various parts of the QM/MM interface code in the
    output file. Also a file \\texttt{TIMINGS} with even more details is written. This
    option is off by {\\bf default}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_TIMINGS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TIMINGS.
        ''')

    x_cpmd_input_QMMM_TIMINGS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TIMINGS.
        ''')


class x_cpmd_section_input_QMMM_TOPOLOGY(MSection):
    '''
    On the next line the name of a Gromos topology file has to be given. Regardless of the
    force field, this topology file has to be in Gromos format\\cite{gromos96}. Topologies
    created with Amber % or Gromacs (Gromos/OPLS-forcefield) can be converted using the
    respective conversion tools shipped with the interface code. A short summary of the
    topology file syntax and some keywords are in section \\ref{sec:qmmm-gromos-inp}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_TOPOLOGY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TOPOLOGY.
        ''')

    x_cpmd_input_QMMM_TOPOLOGY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TOPOLOGY.
        ''')


class x_cpmd_section_input_QMMM_UPDATE_LIST(MSection):
    '''
    On the next line the number of MD steps between updates of the various lists of atoms
    for \\refkeyword{ELECTROSTATIC COUPLING} is given. At every list update a file
    INTERACTING\\_NEW.pdb is created (and overwritten).  {\\bf Default} value is 100.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_UPDATE_LIST_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword UPDATE_LIST.
        ''')

    x_cpmd_input_QMMM_UPDATE_LIST_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword UPDATE_LIST.
        ''')


class x_cpmd_section_input_QMMM_VERBOSE(MSection):
    '''
    The progress of the QM/MM simulation is reported more verbosely in the output. This
    option is off by {\\bf default}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_VERBOSE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword VERBOSE.
        ''')

    x_cpmd_input_QMMM_VERBOSE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword VERBOSE.
        ''')


class x_cpmd_section_input_QMMM_WRITE_LOCALTEMP(MSection):
    '''
    The Temperatures of the QM subsystem, the MM solute (without the QM atoms) and the
    solvent (if present) are calculated separately and writen to the standard output and a
    file \\texttt{QM\\_TEMP}. The file has 5 columns containing the QM temperature, the MM
    temperature, the solvent temperature (or 0.0 if the solvent is part of the solute),
    and the total temperature in that order. With the optional parameters STEP followed by
    an integer, this is done only every \\texttt{nfi\\_lt} timesteps.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_WRITE_LOCALTEMP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WRITE_LOCALTEMP.
        ''')

    x_cpmd_input_QMMM_WRITE_LOCALTEMP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WRITE_LOCALTEMP.
        ''')


class x_cpmd_section_input_QMMM(MSection):
    '''
    Input for Gromos QM/MM interface (see section \\ref{sec:qmmm}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_QMMM_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section QMMM even without a keyword.
        ''')

    x_cpmd_section_input_QMMM_AMBER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_AMBER'),
        repeats=True)

    x_cpmd_section_input_QMMM_BOX_TOLERANCE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_BOX_TOLERANCE'),
        repeats=True)

    x_cpmd_section_input_QMMM_BOX_WALLS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_BOX_WALLS'),
        repeats=True)

    x_cpmd_section_input_QMMM_CAPPING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_CAPPING'),
        repeats=True)

    x_cpmd_section_input_QMMM_COORDINATES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_COORDINATES'),
        repeats=True)

    x_cpmd_section_input_QMMM_ELECTROSTATIC_COUPLING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_ELECTROSTATIC_COUPLING'),
        repeats=True)

    x_cpmd_section_input_QMMM_ESPWEIGHT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_ESPWEIGHT'),
        repeats=True)

    x_cpmd_section_input_QMMM_EXCLUSION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_EXCLUSION'),
        repeats=True)

    x_cpmd_section_input_QMMM_FLEXIBLE_WATER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_FLEXIBLE_WATER'),
        repeats=True)

    x_cpmd_section_input_QMMM_GROMOS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_GROMOS'),
        repeats=True)

    x_cpmd_section_input_QMMM_HIRSHFELD = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_HIRSHFELD'),
        repeats=True)

    x_cpmd_section_input_QMMM_INPUT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_INPUT'),
        repeats=True)

    x_cpmd_section_input_QMMM_MAXNN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_MAXNN'),
        repeats=True)

    x_cpmd_section_input_QMMM_NOSPLIT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_NOSPLIT'),
        repeats=True)

    x_cpmd_section_input_QMMM_RESTART_TRAJECTORY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_RESTART_TRAJECTORY'),
        repeats=True)

    x_cpmd_section_input_QMMM_SAMPLE_INTERACTING = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_SAMPLE_INTERACTING'),
        repeats=True)

    x_cpmd_section_input_QMMM_SPLIT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_SPLIT'),
        repeats=True)

    x_cpmd_section_input_QMMM_TIMINGS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_TIMINGS'),
        repeats=True)

    x_cpmd_section_input_QMMM_TOPOLOGY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_TOPOLOGY'),
        repeats=True)

    x_cpmd_section_input_QMMM_UPDATE_LIST = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_UPDATE_LIST'),
        repeats=True)

    x_cpmd_section_input_QMMM_VERBOSE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_VERBOSE'),
        repeats=True)

    x_cpmd_section_input_QMMM_WRITE_LOCALTEMP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM_WRITE_LOCALTEMP'),
        repeats=True)


class x_cpmd_section_input_RESP_DISCARD(MSection):
    '''
    Request to discard trivial modes in vibrational analysis from linear response (both
    \\refkeyword{PHONON} and \\refkeyword{LANCZOS}).  {\\bf OFF} = argument for performing no
    projection. {\\bf PARTIAL} = argument for projecting out only translations (this is the
    default). {\\bf TOTAL} = argument for projecting both rotations and translations. {\\bf
    LINEAR} = argument for projecting rotations around the $C - \\infty$ axis in a linear
    molecule (not implemented yet).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_DISCARD_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DISCARD.
        ''')

    x_cpmd_input_RESP_DISCARD_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DISCARD.
        ''')


class x_cpmd_section_input_RESP_EIGENSYSTEM(MSection):
    '''
    Not documented.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_EIGENSYSTEM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EIGENSYSTEM.
        ''')

    x_cpmd_input_RESP_EIGENSYSTEM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EIGENSYSTEM.
        ''')


class x_cpmd_section_input_RESP_EPR(MSection):
    '''
    Calculate the EPR $g$ tensor for the system. This routine accepts most, if not all, of
    the options available in the NMR routine (RESTART, NOSMOOTH, NOVIRTUAL, PSI0, RHO0,
    OVERLAP and FULL). Most important new options are:  {\\bf FULL SMART}: does a
    calculation with improved accuracy. A threshold value (between 0 and 1) must be
    present on the next line. The higher the threshold value, the lower the computational
    cost, but this will also reduce the accuracy (a bit). Typically, a value of 0.05
    should be fine. {\\bf OWNOPT}: for the calculation of the $g$ tensor, an effective
    potential is needed. By default, the EPR routine uses the local potential ($V_{LOC} =
    V_{PP,LOC} + V_{HARTREE} + V_{XC}$). This works well with Goedecker pseudopotentials,
    but rather poor with Troullier-Martins pseudopotentials. When using this option, the
    following potential is used instead: $$ V_{EFF} = -\\frac{Z}{r}\\mathrm{erf}(r/r_c) +
    V_{HARTREE} + V_{XC} $$ and $r_c$ (greater than 0) is read on the next line. {\\bf
    HYP}: calculates the hyperfine tensors. See epr\\_hyp.F for details.  Contact
    Reinout.Declerck@UGent.be should you require further information.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_EPR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EPR.
        ''')

    x_cpmd_input_RESP_EPR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EPR.
        ''')


class x_cpmd_section_input_RESP_FUKUI(MSection):
    '''
    Calculates the response to a change of occupation number of chosen orbitals. The
    indices of these orbitals are read from the following nf lines ({\\bf default nf=1}).
    The orbitals themselves are not read from any \\refkeyword{RESTART} file but from
    WAVEFUNCTION.* files generated with \\refkeyword{RHOOUT} in the \\&CPMD section; to
    recall this the orbital numbers have to be negative, just like for the
    \\refkeyword{RHOOUT} keyword.  A weight can be associated with each orbital if given
    just after the orbital number, on the same line. It corresponds to saying how many
    electrons are put in or taken from the orbital. For example;
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_FUKUI_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FUKUI.
        ''')

    x_cpmd_input_RESP_FUKUI_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FUKUI.
        ''')


class x_cpmd_section_input_RESP_HARDNESS(MSection):
    '''
    Not documented.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_HARDNESS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HARDNESS.
        ''')

    x_cpmd_input_RESP_HARDNESS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HARDNESS.
        ''')


class x_cpmd_section_input_RESP_INTERACTION(MSection):
    '''
    Not documented.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_INTERACTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword INTERACTION.
        ''')

    x_cpmd_input_RESP_INTERACTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword INTERACTION.
        ''')


class x_cpmd_section_input_RESP_KEEPREALSPACE(MSection):
    '''
    Like the standard CPMD option, this keeps the C0 ground state wavefunctions in the
    direct space representation during the calculation. Can save a lot of time, but is
    incredibly memory intensive.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_KEEPREALSPACE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword KEEPREALSPACE.
        ''')

    x_cpmd_input_RESP_KEEPREALSPACE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword KEEPREALSPACE.
        ''')


class x_cpmd_section_input_RESP_KPERT(MSection):
    '''
    \\label{sec:kpert
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_KPERT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword KPERT.
        ''')

    x_cpmd_input_RESP_KPERT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword KPERT.
        ''')


class x_cpmd_section_input_RESP_LANCZOS(MSection):
    '''
    lanczos\\_dim  iterations   conv\\_threshold lanczos\\_dim= dimension of the vibrational
    d.o.f. iterations = no. of iterations desired for this run conv\\_threshold = threshold
    for convergence on eigenvectors CONTINUE = argument for continuing Lanczos
    diagonalization from a previous run (reads file LANCZOS\\_CONTINUE) DETAILS  = argument
    for verbosity. prints a lot of stuff
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_LANCZOS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LANCZOS.
        ''')

    x_cpmd_input_RESP_LANCZOS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LANCZOS.
        ''')


class x_cpmd_section_input_RESP_NMR(MSection):
    '''
    Calculate the NMR chemical shielding tensors for the system. Most important option:
    FULL, does a calculation with improved accuracy for periodic systems but takes a lot
    of time. Isolated systems: Use OVERLAP and 0.1 (on next line) for the same effect.
    \\textit{Be careful for non-hydrogen nuclei.} The shielding is calculated without
    contribution from the core electrons. Contact sebastia@mpip-mainz.mpg.de for further
    details.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_NMR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NMR.
        ''')

    x_cpmd_input_RESP_NMR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NMR.
        ''')


class x_cpmd_section_input_RESP_NOOPT(MSection):
    '''
    Do not perform a ground state wfn optimization. Be sure the restarted wfn is at the
    BO-surface.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_NOOPT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NOOPT.
        ''')

    x_cpmd_input_RESP_NOOPT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NOOPT.
        ''')


class x_cpmd_section_input_RESP_OACP(MSection):
    '''
    Not documented.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_OACP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OACP.
        ''')

    x_cpmd_input_RESP_OACP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OACP.
        ''')


class x_cpmd_section_input_RESP_PHONON(MSection):
    '''
    Calculate the harmonic frequencies from perturbation theory.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_PHONON_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PHONON.
        ''')

    x_cpmd_input_RESP_PHONON_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PHONON.
        ''')


class x_cpmd_section_input_RESP_POLAK(MSection):
    '''
    Uses the Polak-Ribiere formula for the conjugate gradient algorithm. Can be safer in
    the convergence.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_POLAK_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword POLAK.
        ''')

    x_cpmd_input_RESP_POLAK_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword POLAK.
        ''')


class x_cpmd_section_input_RESP_RAMAN(MSection):
    '''
    Calculate the polarizability (also in periodic systems) as well as Born-charges and
    dipole moment.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_RAMAN_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword RAMAN.
        ''')

    x_cpmd_input_RESP_RAMAN_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword RAMAN.
        ''')


class x_cpmd_section_input_RESP_TIGHTPREC(MSection):
    '''
    Uses a harder preconditioner. For experts: The Hamiltonian is approximated by the
    kinetic energy, the G-diagonal Coulomb potential and the KS-energies. The number
    obtained this way must not be close to zero. This is achieved by smoothing it with
    This is achieved by smoothing it with $$x \\to f(x) = \\sqrt{x^2 + \\epsilon^2} \\; \\;
    [{\\rm default}] $$ or $$x \\to f(x) = (x^2 + \\epsilon ^2)/x \\; \\; [{\\rm this \\;
    option}] $$ The HARD option conserves the sign of the approximate Hamiltonian whereas
    the default formula does never diverge.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_TIGHTPREC_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TIGHTPREC.
        ''')

    x_cpmd_input_RESP_TIGHTPREC_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TIGHTPREC.
        ''')


class x_cpmd_section_input_RESP(MSection):
    '''
    Response calculations
    '''

    m_def = Section(validate=False)

    x_cpmd_input_RESP_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section RESP even without a keyword.
        ''')

    x_cpmd_section_input_RESP_DISCARD = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_DISCARD'),
        repeats=True)

    x_cpmd_section_input_RESP_EIGENSYSTEM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_EIGENSYSTEM'),
        repeats=True)

    x_cpmd_section_input_RESP_EPR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_EPR'),
        repeats=True)

    x_cpmd_section_input_RESP_FUKUI = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_FUKUI'),
        repeats=True)

    x_cpmd_section_input_RESP_HARDNESS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_HARDNESS'),
        repeats=True)

    x_cpmd_section_input_RESP_INTERACTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_INTERACTION'),
        repeats=True)

    x_cpmd_section_input_RESP_KEEPREALSPACE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_KEEPREALSPACE'),
        repeats=True)

    x_cpmd_section_input_RESP_KPERT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_KPERT'),
        repeats=True)

    x_cpmd_section_input_RESP_LANCZOS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_LANCZOS'),
        repeats=True)

    x_cpmd_section_input_RESP_NMR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_NMR'),
        repeats=True)

    x_cpmd_section_input_RESP_NOOPT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_NOOPT'),
        repeats=True)

    x_cpmd_section_input_RESP_OACP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_OACP'),
        repeats=True)

    x_cpmd_section_input_RESP_PHONON = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_PHONON'),
        repeats=True)

    x_cpmd_section_input_RESP_POLAK = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_POLAK'),
        repeats=True)

    x_cpmd_section_input_RESP_RAMAN = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_RAMAN'),
        repeats=True)

    x_cpmd_section_input_RESP_TIGHTPREC = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP_TIGHTPREC'),
        repeats=True)


class x_cpmd_section_input_SYSTEM_ACCEPTOR(MSection):
    '''
    Set the \\refkeyword{CDFT} acceptor atoms. Parameter NACCR must be specified next to
    the keyword. NACCR $\\in [1,2,...,N]$ is the number of acceptor Atoms ($N$ being the
    total number of atoms). The indices of NACCR atoms separated by whitespaces are read
    from the next line. {\\bf HDASINGLE} \\defaultvalue{off} if set together with CDFT HDA,
    CPMD performs a constrained HDA calculation with only an ACCEPTOR group weight but
    different constraint values $N_\\text{c}$. {\\bf WMULT} \\defaultvalue{off} if set
    together with CDFT HDA, CPMD performs a constrained HDA calculation with two different
    an ACCEPTOR group weights for the two states. {\\bf HDASINGLE} and {\\bf WMULT} are
    mutually exclusive.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_ACCEPTOR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ACCEPTOR.
        ''')

    x_cpmd_input_SYSTEM_ACCEPTOR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ACCEPTOR.
        ''')


class x_cpmd_section_input_SYSTEM_ANGSTROM(MSection):
    '''
    The atomic coordinates and the supercell parameters and several other parameters are
    read in {\\AA}ngs\\-troms.

    {\\bf Default} is {\\bf atomic units} which are always used internally. Not supported
    for \\refkeyword{QMMM} calculations.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_ANGSTROM_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ANGSTROM.
        ''')

    x_cpmd_input_SYSTEM_ANGSTROM_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ANGSTROM.
        ''')


class x_cpmd_section_input_SYSTEM_CELL(MSection):
    '''
    The parameters specifying the super cell are read from the next line. Six numbers in
    the following order have to be provided: $a$, $b/a$, $c/a$, $\\cos \\alpha$, $\\cos
    \\beta$, $\\cos \\gamma$. For cubic phases, $a$ is the lattice parameter. CPMD will check
    those values, unless you turn off the test via \\refkeyword{CHECK SYMMETRY}. With the
    keyword {\\bf ABSOLUTE}, you give $a$, $b$ and $c$. With the keyword {\\bf DEGREE}, you
    provide $\\alpha$, $\\beta$ and $\\gamma$ in degrees instead of their cosine. With the
    keyword {\\bf VECTORS}, the lattice vectors $a1$, $a2$, $a3$ are read from the next
    line instead of the 6 numbers. In this case the {\\bf SYMMETRY} keyword is not used.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_CELL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CELL.
        ''')

    x_cpmd_input_SYSTEM_CELL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CELL.
        ''')


class x_cpmd_section_input_SYSTEM_CHARGE(MSection):
    '''
    The total charge of the system is read from the next line. \\textbf{Default} is
    \\defaultvalue{0}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_CHARGE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CHARGE.
        ''')

    x_cpmd_input_SYSTEM_CHARGE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CHARGE.
        ''')


class x_cpmd_section_input_SYSTEM_CHECK_SYMMETRY(MSection):
    '''
    The precision with which the conformance of the \\refkeyword{CELL} parameters are
    checked against the (supercell) \\refkeyword{SYMMETRY} is read from the next line. With
    older versions of CPMD, redundant variables could be set to arbitrary values; now
    \\textbf{all} values have to conform. If you want the old behavior back, you can turn
    the check off by adding the keyword {\\bf OFF} or by providing a negative precision.
    \\textbf{Default} value is: \\defaultvalue{1.0e-4}
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_CHECK_SYMMETRY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CHECK_SYMMETRY.
        ''')

    x_cpmd_input_SYSTEM_CHECK_SYMMETRY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CHECK_SYMMETRY.
        ''')


class x_cpmd_section_input_SYSTEM_CLASSICAL_CELL(MSection):
    '''
    Not documented.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_CLASSICAL_CELL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CLASSICAL_CELL.
        ''')

    x_cpmd_input_SYSTEM_CLASSICAL_CELL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CLASSICAL_CELL.
        ''')


class x_cpmd_section_input_SYSTEM_CLUSTER(MSection):
    '''
    Isolated system such as a molecule or a cluster. Same effect as \\refkeyword{SYMMETRY}
    0, but allows a non-orthorhombic cell. Only rarely useful.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_CLUSTER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CLUSTER.
        ''')

    x_cpmd_input_SYSTEM_CLUSTER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CLUSTER.
        ''')


class x_cpmd_section_input_SYSTEM_CONSTANT_CUTOFF(MSection):
    '''
    Apply a cutoff function to the kinetic energy term~\\cite{bernasconi95} in order to
    simulate constant cutoff dynamics. The parameters $A$, $\\sigma$ and $E_o$ are read
    from the next line (all quantities have to be given in Rydbergs). $$ G^2 \\to G^2 + A
    \\left[ 1 + \\mbox{erf} \\left( {\\frac{1}{2} G^2 -  \\frac{E_o}{\\sigma}} \\right) \\right]
    $$
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_CONSTANT_CUTOFF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CONSTANT_CUTOFF.
        ''')

    x_cpmd_input_SYSTEM_CONSTANT_CUTOFF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CONSTANT_CUTOFF.
        ''')


class x_cpmd_section_input_SYSTEM_COUPLINGS_LINRES(MSection):
    '''
    Calculate non-adiabatic couplings~\\cite{nonadiabatic} using linear-response theory.
    With BRUTE FORCE, the linear response to the nuclear displacements along all Cartesian
    coordinates is calculated. With NVECT=$n$, at most $n$ cycles of the iterative scheme
    in \\cite{nonadiabatic} are performed. However, the iterative calculation is also
    stopped earlier if its contribution to the non-adiabatic coupling vector is smaller a
    given tolerance (TOL=$C_{\\mathrm{tol}}$). In the case of the iterative scheme, also
    the option THR can be given, followed by three lines each containing a pair of a
    threshold contribution to the non-adiabatic coupling vector and a tolerance for the
    linear-response wavefunction (see \\cite{nonadiabatic}). Do not forget to include a
    \\&LINRES section in the input, even if the defaults are used. See
    \\refkeyword{COUPLINGS NSURF}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_COUPLINGS_LINRES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword COUPLINGS_LINRES.
        ''')

    x_cpmd_input_SYSTEM_COUPLINGS_LINRES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword COUPLINGS_LINRES.
        ''')


class x_cpmd_section_input_SYSTEM_COUPLINGS_NSURF(MSection):
    '''
    Required for non-adiabatic couplings: the Kohn-Sham states involved in the transition.
    For the moment, only one pair of states makes sense, NSURF=1. On the following line,
    the orbital numbers of the two Kohn-Sham states and a weight of 1.0 are expected. For
    singlet-singlet transitions, the ROKS-based Slater transition-state density
    (\\refkeyword{LOW SPIN EXCITATION LSETS}) should be used. For doublet-doublet
    transitions, the local spin-density approximation (\\refkeyword{LSD}) with the
    occupation numbers (\\refkeyword{OCCUPATION}, \\refkeyword{NSUP}, \\refkeyword{STATES})
    of the corresponding Slater transition-state density should be used.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_COUPLINGS_NSURF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword COUPLINGS_NSURF.
        ''')

    x_cpmd_input_SYSTEM_COUPLINGS_NSURF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword COUPLINGS_NSURF.
        ''')


class x_cpmd_section_input_SYSTEM_COUPLINGS(MSection):
    '''
    Calculate non-adiabatic couplings~\\cite{nonadiabatic} using finite differences (FD and
    PROD are two different finite-difference approximations). The displacement $\\epsilon$
    is expected in atomic units. If NAT=$n$ is given, the coupling vector acting on only a
    subset of $n$ atoms is calculated. In this case, a line containing $n$ atom sequence
    numbers is expected. See \\refkeyword{COUPLINGS NSURF}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_COUPLINGS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword COUPLINGS.
        ''')

    x_cpmd_input_SYSTEM_COUPLINGS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword COUPLINGS.
        ''')


class x_cpmd_section_input_SYSTEM_CUTOFF(MSection):
    '''
    The {\\bf cutoff} for the plane wave basis in {\\bf Rydberg} is read from the next line.
    The keyword {\\bf SPHERICAL} is used with k points in order to have $|g + k|^2 <
    E_{cut}$ instead of $|g|^2 < E_{cut}$. This is the default.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_CUTOFF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword CUTOFF.
        ''')

    x_cpmd_input_SYSTEM_CUTOFF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword CUTOFF.
        ''')


class x_cpmd_section_input_SYSTEM_DENSITY_CUTOFF(MSection):
    '''
    Set the plane wave energy cutoff for the density. The value is read from the next
    line. The density cutoff is usally automatically determined from the wavefunction
    \\refkeyword{CUTOFF} via the \\refkeyword{DUAL} factor. With the additional flag {\\bf
    NUMBER} the number of plane waves can be specified directly. This is useful to
    calculate bulk modulus or properties depending on the volume. The given energy cutoff
    has to be bigger than the one to have the required plane wave density number.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_DENSITY_CUTOFF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DENSITY_CUTOFF.
        ''')

    x_cpmd_input_SYSTEM_DENSITY_CUTOFF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DENSITY_CUTOFF.
        ''')


class x_cpmd_section_input_SYSTEM_DONOR(MSection):
    '''
    Set the \\refkeyword{CDFT} donor atoms. Parameter NACCR must be specified next to the
    keyword. NDON $\\in \\mathbb{R}_+$ is the number of Donor Atoms ($N$ being the total
    number of atoms).  If NDON$>0$ the indices of NDON atoms separated by whitespaces are
    read from the next line else only use an Acceptor group in the CDFT weight.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_DONOR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DONOR.
        ''')

    x_cpmd_input_SYSTEM_DONOR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DONOR.
        ''')


class x_cpmd_section_input_SYSTEM_DUAL(MSection):
    '''
    The ratio between the wavefunction energy \\refkeyword{CUTOFF} and the
    \\refkeyword{DENSITY CUTOFF} is read from the next line.

    {\\bf Default} is {\\bf 4}.

    There is little need to change this parameter, except when using ultra-soft
    pseudopotentials, where the wavefunction cutoff is very low and the corresponding
    density cutoff is too low to represent the augmentation charges accurately. In order
    to maintain good energy conservation and have good convergens of wavefunctions and
    related parameters, {\\bf DUAL} needs to be increased to values of 6--10.  Warning: You
    can have some trouble if you use the {\\bf DUAL} option with the symmetrization of the
    electronic density.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_DUAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DUAL.
        ''')

    x_cpmd_input_SYSTEM_DUAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DUAL.
        ''')


class x_cpmd_section_input_SYSTEM_ENERGY_PROFILE(MSection):
    '''
    Perform an energy profile calculation at the end of a wavefunction optimization using
    the ROKS or ROSS methods.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_ENERGY_PROFILE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ENERGY_PROFILE.
        ''')

    x_cpmd_input_SYSTEM_ENERGY_PROFILE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ENERGY_PROFILE.
        ''')


class x_cpmd_section_input_SYSTEM_EXTERNAL_FIELD(MSection):
    '''
    Applies an external electric field to the system using the Berry phase. The electric
    field vector in AU is read from the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_EXTERNAL_FIELD_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXTERNAL_FIELD.
        ''')

    x_cpmd_input_SYSTEM_EXTERNAL_FIELD_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXTERNAL_FIELD.
        ''')


class x_cpmd_section_input_SYSTEM_HFX_CUTOFF(MSection):
    '''
    Set an additional cutoff for wavefunctionand density to be used in the calculation of
    exact exchange. Cutoffs for wavefunctions and densities are read from the next line in
    Rydberg units. Defaults are the same cutoffs as for the normal calculation. Only lower
    cutoffs than the defaults can be specified.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_HFX_CUTOFF_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword HFX_CUTOFF.
        ''')

    x_cpmd_input_SYSTEM_HFX_CUTOFF_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword HFX_CUTOFF.
        ''')


class x_cpmd_section_input_SYSTEM_ISOTROPIC_CELL(MSection):
    '''
    Specifies a constraint on the super cell in constant pressure dynamics or geometry
    optimization. The shape of the cell is held fixed, only the volume changes.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_ISOTROPIC_CELL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ISOTROPIC_CELL.
        ''')

    x_cpmd_input_SYSTEM_ISOTROPIC_CELL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ISOTROPIC_CELL.
        ''')


class x_cpmd_section_input_SYSTEM_KPOINTS(MSection):
    '''
    With no option, read in the next line with the number of k-points and for each
    k-point, read the components in the Cartesian coordinates (units~$2\\pi/a$) and the
    weight.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_KPOINTS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword KPOINTS.
        ''')

    x_cpmd_input_SYSTEM_KPOINTS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword KPOINTS.
        ''')


class x_cpmd_section_input_SYSTEM_LOW_SPIN_EXCITATION_LSETS(MSection):
    '''
    Slater transition-state density with restricted open-shell Kohn-Sham (low spin excited
    state). Currently works only with ROKS but not with ROSS, ROOTHAAN, or CAS22. See
    Ref.~\\cite{lsets}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_LOW_SPIN_EXCITATION_LSETS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LOW_SPIN_EXCITATION_LSETS.
        ''')

    x_cpmd_input_SYSTEM_LOW_SPIN_EXCITATION_LSETS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LOW_SPIN_EXCITATION_LSETS.
        ''')


class x_cpmd_section_input_SYSTEM_LOW_SPIN_EXCITATION(MSection):
    '''
    Use the low spin excited state functional~\\cite{Frank98}. For ROKS calculations, see
    also the \\refkeyword{ROKS} keyword in the \\&CPMD-section.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_LOW_SPIN_EXCITATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LOW_SPIN_EXCITATION.
        ''')

    x_cpmd_input_SYSTEM_LOW_SPIN_EXCITATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LOW_SPIN_EXCITATION.
        ''')


class x_cpmd_section_input_SYSTEM_LSE_PARAMETERS(MSection):
    '''
    Determines the energy expression used in LSE calculations. The two parameters LSEA and
    LSEB are read from the next line. \\[E = \\mbox{LSEA} \\cdot E(Mixed) + \\mbox{LSEB} \\cdot
    E(Triplet)\\] The default (LSEA $= 2$ and LSEB $= 1$) corresponds to singlet symmetry.
    For the lowest triplet state, the \\refkeyword{LSE PARAMETERS} must be set to 0 and 1
    (zero times mixed state plus triplet). See ref \\cite{Frank98} for a description of the
    method.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_LSE_PARAMETERS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LSE_PARAMETERS.
        ''')

    x_cpmd_input_SYSTEM_LSE_PARAMETERS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LSE_PARAMETERS.
        ''')


class x_cpmd_section_input_SYSTEM_MESH(MSection):
    '''
    The number of {\\bf real space mesh} points in $x-$, $y-$ and $z-$direction is read
    from the next line.  If the values provided by the user are not compatible with the
    plane-wave cutoff or the requirements of the FFT routines the program chooses the next
    bigger valid numbers.  {\\bf Default} are the {\\bf minimal values} compatible with the
    energy cutoff and the {\\bf FFT} requirements.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_MESH_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MESH.
        ''')

    x_cpmd_input_SYSTEM_MESH_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MESH.
        ''')


class x_cpmd_section_input_SYSTEM_MULTIPLICITY(MSection):
    '''
    This keyword only applies to LSD calculations. The multiplicity (2$S$+1) is read from
    the next line. {\\bf Default} is the {\\bf smallest possible} multiplicity.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_MULTIPLICITY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MULTIPLICITY.
        ''')

    x_cpmd_input_SYSTEM_MULTIPLICITY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MULTIPLICITY.
        ''')


class x_cpmd_section_input_SYSTEM_NSUP(MSection):
    '''
    The number of states of the same spin as the first state is read from the next line.
    This keyword makes only sense in spin-polarized calculations (keyword
    \\refkeyword{LSD}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_NSUP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword NSUP.
        ''')

    x_cpmd_input_SYSTEM_NSUP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword NSUP.
        ''')


class x_cpmd_section_input_SYSTEM_OCCUPATION(MSection):
    '''
    The occupation numbers are read from the next line. This keyword must be preceeded by
    \\refkeyword{STATES}. The FIXED option fixes the occupation numbers for the
    diagonalization scheme, otherwise this option is meaningless.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_OCCUPATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword OCCUPATION.
        ''')

    x_cpmd_input_SYSTEM_OCCUPATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword OCCUPATION.
        ''')


class x_cpmd_section_input_SYSTEM_POINT_GROUP(MSection):
    '''
    The point group symmetry of the system can be specified in the next line. With the
    keyword {\\sl AUTO} in the next line, the space group is determined automatically. This
    affects the calculation of nuclear forces and ionic positions. The electronic density
    and nuclear forces are symmetrized in function of point group symmetry. The group
    number is read from the next line. Crystal symmetry groups:
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_POINT_GROUP_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword POINT_GROUP.
        ''')

    x_cpmd_input_SYSTEM_POINT_GROUP_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword POINT_GROUP.
        ''')


class x_cpmd_section_input_SYSTEM_POISSON_SOLVER(MSection):
    '''
    This keyword determines the method for the solution of the Poisson equation for
    isolated systems. Either Hockney's method~\\cite{Hockney70} or Martyna and Tuckerman's
    method~\\cite{Martyna99} is used. The smoothing parameter (for Hockney's method) or $L
    \\times \\alpha$ for Tuckerman's method can be read from the next line using the {\\bf
    PARAMETER} keyword.  For more information about the usage of this parameter see also
    section \\ref{hints:symm0}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_POISSON_SOLVER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword POISSON_SOLVER.
        ''')

    x_cpmd_input_SYSTEM_POISSON_SOLVER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword POISSON_SOLVER.
        ''')


class x_cpmd_section_input_SYSTEM_POLYMER(MSection):
    '''
    Assume {\\bf periodic boundary} condition in {\\bf $x$-direction}. %       You also need
    to set the 'cluster option' (i.e. \\refkeyword{SYMMETRY} 0).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_POLYMER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword POLYMER.
        ''')

    x_cpmd_input_SYSTEM_POLYMER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword POLYMER.
        ''')


class x_cpmd_section_input_SYSTEM_PRESSURE(MSection):
    '''
    The {\\bf external pressure} on the system is read from the next line (in {\\bf kbar}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_PRESSURE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PRESSURE.
        ''')

    x_cpmd_input_SYSTEM_PRESSURE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PRESSURE.
        ''')


class x_cpmd_section_input_SYSTEM_REFERENCE_CELL(MSection):
    '''
    This cell is used to calculate the Miller indices in a constant pressure simulation.
    This keyword is only active together with the option {\\bf PARRINELLO-RAHMAN}. The
    parameters specifying the reference (super) cell are read from the next line.  Six
    numbers in the following order have to be provided: $a$, $b/a$, $c/a$, $\\cos \\alpha$,
    $\\cos \\beta$, $\\cos \\gamma$. The keywords {\\bf ABSOLUTE} and {\\bf DEGREE } are
    described in {\\bf CELL} option.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_REFERENCE_CELL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REFERENCE_CELL.
        ''')

    x_cpmd_input_SYSTEM_REFERENCE_CELL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REFERENCE_CELL.
        ''')


class x_cpmd_section_input_SYSTEM_SCALE(MSection):
    '''
    {\\bf Scale atomic coordinates} of the system with the lattice constants (see {\\bf
    CELL}). You can indicate an additional scale for each axis with the options {\\bf SX},
    {\\bf SY} and {\\bf SZ}. For instance, if you indicate SX=sxscale, you give your
    x-coordinates between $0.$ and sxscale (by default $1.$). This is useful when you use
    many primitive cells. With the keyword {\\bf CARTESIAN}, you specify that the given
    coordinates are in Cartesian basis, otherwise the default with the {\\bf SCALE} option
    is in direct lattice basis. In all cases, the coordinates are multiplied by the
    lattice constants. If this keyword is present an output file GEOMETRY.scale is
    written. This file contains the lattice vectors in \\AA and atomic units together with
    the atomic coordinates in the direct lattice basis.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_SCALE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SCALE.
        ''')

    x_cpmd_input_SYSTEM_SCALE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SCALE.
        ''')


class x_cpmd_section_input_SYSTEM_STATES(MSection):
    '''
    The number of states used in the calculation is read from the next line.  This keyword
    has to preceed the keyword {\\bf OCCUPATION}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_STATES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword STATES.
        ''')

    x_cpmd_input_SYSTEM_STATES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword STATES.
        ''')


class x_cpmd_section_input_SYSTEM_SURFACE(MSection):
    '''
    By default, if nothing is specified, assume {\\bf periodic boundary} condition in {\\bf
    $x$- and $y$-direction}. With the extra keywords {\\sl XY}, {\\sl YZ} or {\\sl ZX}, the
    periodicity of the systems is assumed to be along $(x,y)$, $(y,z)$ or $(z,x)$,
    respectively. %        You also need to set the 'cluster option' (i.e.
    \\refkeyword{SYMMETRY} 0).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_SURFACE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SURFACE.
        ''')

    x_cpmd_input_SYSTEM_SURFACE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SURFACE.
        ''')


class x_cpmd_section_input_SYSTEM_SYMMETRIZE_COORDINATES(MSection):
    '''
    {\\bf Input coordinates} are {\\bf symmetrized} according to the {\\bf point group}
    specified.  This only makes sense when the structure already is close to the symmetric
    one.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_SYMMETRIZE_COORDINATES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SYMMETRIZE_COORDINATES.
        ''')

    x_cpmd_input_SYSTEM_SYMMETRIZE_COORDINATES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SYMMETRIZE_COORDINATES.
        ''')


class x_cpmd_section_input_SYSTEM_SYMMETRY(MSection):
    '''
    The {\\bf supercell symmetry type} is read from the next line. You can put a number or
    a keyword. {\\small \\begin{description} \\renewcommand{\\makelabel}[1]{\\hbox to 2em
    {\\hfill#1}} \\item[0]  {\\bf ISOLATED} system in a cubic/orthorhombic
    box~\\cite{Hockney70,Landman} with ISOLATED MOLECULE option activated. By default the
    Hockney method (see \\refkeyword{POISSON SOLVER}) is used for solving the Poisson
    equations. You can use this option in combination with \\refkeyword{POLYMER} or
    \\refkeyword{SURFACE} for systems that are periodic in only 1 or 2 dimensions. The
    default Poisson solver is MORTENSEN in this case. See the Hints and Tricks section for
    some additional requirements when calculating isolated system. \\item[1]  Simple {\\bf
    CUBIC} \\item[2]  {\\bf FACE CENTERED CUBIC} ({\\bf FCC}) \\item[3]  {\\bf BODY CENTERED
    CUBIC} ({\\bf BCC}) \\item[4]  {\\bf HEXAGONAL} \\item[5]  {\\bf TRIGONAL} or {\\bf
    RHOMBOHEDRAL} \\item[6]  {\\bf TETRAGONAL} \\item[7]  {\\bf BODY CENTRED TETRAGONAL} ({\\bf
    BCT}) \\item[8]  {\\bf ORTHORHOMBIC} \\item[12] {\\bf MONOCLINIC} \\item[14] {\\bf
    TRICLINIC} \\end{description} } Warning: This keyword should not be used with the
    keyword {\\bf CELL VECTORS}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_SYMMETRY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword SYMMETRY.
        ''')

    x_cpmd_input_SYSTEM_SYMMETRY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword SYMMETRY.
        ''')


class x_cpmd_section_input_SYSTEM_TESR(MSection):
    '''
    The number of additional supercells included in the real space sum for the Ewald term
    is read from the next line. Default is 0, for small unit cells larger values (up to 8)
    have to be used.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_TESR_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword TESR.
        ''')

    x_cpmd_input_SYSTEM_TESR_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword TESR.
        ''')


class x_cpmd_section_input_SYSTEM_WCUT(MSection):
    '''
    Set the radial \\refkeyword{CDFT} weight cutoff for all atom species to CUT, which is
    specified next to the keyword. Default is a species specific cutoff at the distance
    where the magnitude of the respective promolecular density is smaller than $10^{-6}$.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_WCUT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WCUT.
        ''')

    x_cpmd_input_SYSTEM_WCUT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WCUT.
        ''')


class x_cpmd_section_input_SYSTEM_WGAUSS(MSection):
    '''
    Use Gaussian weight functions instead of Hirshfeld promolecular orbitals in the
    \\refkeyword{CDFT} weight. Parameter NWG is specified next to the keyword and has to be
    equal to the number of different atom species in the calculation. The Gaussian widths
    $\\sigma_i$ of the species $i$ are read from subsequent lines.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_WGAUSS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WGAUSS.
        ''')

    x_cpmd_input_SYSTEM_WGAUSS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WGAUSS.
        ''')


class x_cpmd_section_input_SYSTEM_ZFLEXIBLE_CELL(MSection):
    '''
    Specifies a constraint on the super cell in constant pressure dynamics or geometry
    optimizations. The supercell may only shrink or grow in z-direction. Should be very
    useful for ``dense slab'' configurations, e.g. a water layer between solid slabs.
    \\textbf{Please note:} this is by no means intended to give a statistically meaningful
    ensemble, but merely to provide a tool for efficient equilibration of a specific class
    of system.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_ZFLEXIBLE_CELL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ZFLEXIBLE_CELL.
        ''')

    x_cpmd_input_SYSTEM_ZFLEXIBLE_CELL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ZFLEXIBLE_CELL.
        ''')


class x_cpmd_section_input_SYSTEM(MSection):
    '''
    Simulation cell and plane wave parameters (\\textbf{required}).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_SYSTEM_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section SYSTEM even without a keyword.
        ''')

    x_cpmd_section_input_SYSTEM_ACCEPTOR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_ACCEPTOR'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_ANGSTROM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_ANGSTROM'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_CELL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_CELL'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_CHARGE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_CHARGE'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_CHECK_SYMMETRY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_CHECK_SYMMETRY'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_CLASSICAL_CELL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_CLASSICAL_CELL'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_CLUSTER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_CLUSTER'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_CONSTANT_CUTOFF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_CONSTANT_CUTOFF'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_COUPLINGS_LINRES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_COUPLINGS_LINRES'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_COUPLINGS_NSURF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_COUPLINGS_NSURF'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_COUPLINGS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_COUPLINGS'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_CUTOFF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_CUTOFF'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_DENSITY_CUTOFF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_DENSITY_CUTOFF'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_DONOR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_DONOR'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_DUAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_DUAL'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_ENERGY_PROFILE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_ENERGY_PROFILE'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_EXTERNAL_FIELD = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_EXTERNAL_FIELD'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_HFX_CUTOFF = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_HFX_CUTOFF'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_ISOTROPIC_CELL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_ISOTROPIC_CELL'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_KPOINTS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_KPOINTS'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_LOW_SPIN_EXCITATION_LSETS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_LOW_SPIN_EXCITATION_LSETS'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_LOW_SPIN_EXCITATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_LOW_SPIN_EXCITATION'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_LSE_PARAMETERS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_LSE_PARAMETERS'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_MESH = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_MESH'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_MULTIPLICITY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_MULTIPLICITY'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_NSUP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_NSUP'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_OCCUPATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_OCCUPATION'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_POINT_GROUP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_POINT_GROUP'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_POISSON_SOLVER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_POISSON_SOLVER'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_POLYMER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_POLYMER'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_PRESSURE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_PRESSURE'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_REFERENCE_CELL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_REFERENCE_CELL'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_SCALE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_SCALE'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_STATES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_STATES'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_SURFACE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_SURFACE'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_SYMMETRIZE_COORDINATES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_SYMMETRIZE_COORDINATES'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_SYMMETRY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_SYMMETRY'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_TESR = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_TESR'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_WCUT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_WCUT'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_WGAUSS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_WGAUSS'),
        repeats=True)

    x_cpmd_section_input_SYSTEM_ZFLEXIBLE_CELL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM_ZFLEXIBLE_CELL'),
        repeats=True)


class x_cpmd_section_input_TDDFT_DAVIDSON_RDIIS(MSection):
    '''
    This keyword controls the residual DIIS method for TDDFT diagonalization. This method
    is used at the end of a DAVIDSON diagonalization for roots that are not yet converged.
    The first number gives the maxium iterations, the second the maximum allowed restarts,
    and the third the maximum residual allowed when the method is invoked.

    \\textbf{Default} values are \\defaultvalue{20}, \\defaultvalue{3} and
    \\defaultvalue{$10^{-3}$}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_DAVIDSON_RDIIS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DAVIDSON_RDIIS.
        ''')

    x_cpmd_input_TDDFT_DAVIDSON_RDIIS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DAVIDSON_RDIIS.
        ''')


class x_cpmd_section_input_TDDFT_DIAGONALIZER(MSection):
    '''
    Specify the iterative diagonalizer to be used.

    \\textbf{Defaults} are {\\sl DAVIDSON} for the Tamm--Dancoff method, {\\sl NONHERMIT} (a
    non-hermitian Davidson method) for TDDFT LR and {\\sl PCG} (Conjugate gradients) for
    the optimized subspace method. The additional keyword {\\sl MINIMIZE} applies to the
    PCG method only. It forces a line minimization with quadratic search.

    \\textbf{Default} is \\defaultvalue{not to use line minimization}.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_DIAGONALIZER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword DIAGONALIZER.
        ''')

    x_cpmd_input_TDDFT_DIAGONALIZER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword DIAGONALIZER.
        ''')


class x_cpmd_section_input_TDDFT_EXTPOT(MSection):
    '''
    Non adiabatic (nonadiabatic, non-adiabatic) Tully's trajectory surface hopping
    dynamics using TDDFT energies and forces, coupled with an external
    field~\\cite{tavernelli2010}. To be used together with the keywords
    \\refkeyword{MOLECULAR DYNAMICS} BO, \\refkeyword{TDDFT} in the \\&CPMD section, and
    \\refkeyword{T-SHTDDFT} in the \\&TDDFT section. Do NOT use the keyword
    \\refkeyword{T-SHTDDFT} together with the keyword \\refkeyword{SURFACE HOPPING} in
    \\&CPMD, which invokes the SH scheme based on \\refkeyword{ROKS}~\\cite{surfhop} (see
    \\refkeyword{SURFACE HOPPING}). This keyword follow the same principle as described for
    the keyword \\refkeyword{T-SHTDDFT}, except that, in the present dynamics, the
    trajectory starts on the ground state and is coupled with an external field through
    the equations of motion for the amplitudes of Tully's trajectory surface hopping.
    According to the evolution of the amplitudes of the different excited states, the
    running trajectory can jump on an excited state. From there, deactivation through
    nonradiative processes is possible, within the normal trajectory surface hopping
    scheme. Parameter \\textit{aampl}, \\textit{adir}, \\textit{afreq}, and \\textit{apara1}
    are read from the next line. The amplitude of the vector potential is provided in
    \\textit{aampl} and its polarization is given in \\textit{adir} (1 = x-polarized, 2 =
    y-polarized, 3 = z-polarized, 4 = all components). The keyword \\textit{afreq} gives
    the frequency of the field and \\textit{apara1} is a free parameter for a specific
    user-specified pulse. Important points: the applied electromagnetic field needs to be
    hard coded in the subroutine sh\\_tddft.F, in the subroutine SH\\_EXTPOT. The vector
    potential is used for the coupling with the amplitudes equations. Be careful to use a
    time step small enough for a correct description of the pulse. The pulse is printed in
    the file SH\\_EXTPT.dat (step, A(t), E(t)).
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_EXTPOT_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword EXTPOT.
        ''')

    x_cpmd_input_TDDFT_EXTPOT_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword EXTPOT.
        ''')


class x_cpmd_section_input_TDDFT_FORCE_STATE(MSection):
    '''
    The state for which the forces are calculated is read from the next line. Default is
    for state 1.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_FORCE_STATE_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword FORCE_STATE.
        ''')

    x_cpmd_input_TDDFT_FORCE_STATE_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword FORCE_STATE.
        ''')


class x_cpmd_section_input_TDDFT_LOCALIZATION(MSection):
    '''
    Use localized orbitals in the TDDFT calculation. Default is to use canonical orbitals.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_LOCALIZATION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword LOCALIZATION.
        ''')

    x_cpmd_input_TDDFT_LOCALIZATION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword LOCALIZATION.
        ''')


class x_cpmd_section_input_TDDFT_MOLECULAR_STATES(MSection):
    '''
    Calculate and group Kohn--Sham orbitals into molecular states for a TDDFT calculation.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_MOLECULAR_STATES_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword MOLECULAR_STATES.
        ''')

    x_cpmd_input_TDDFT_MOLECULAR_STATES_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword MOLECULAR_STATES.
        ''')


class x_cpmd_section_input_TDDFT_PCG_PARAMETER(MSection):
    '''
    The parameters for the PCG diagonalization are read from the next line. If {\\sl
    MINIMIZE} was used in the \\refkeyword{DIAGONALIZER} then the total number of steps
    (default 100) and the convergence criteria (default $10^{-8}$) are read from the next
    line. Without minimization in addition the step length (default 0.5) has also to be
    given.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_PCG_PARAMETER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PCG_PARAMETER.
        ''')

    x_cpmd_input_TDDFT_PCG_PARAMETER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PCG_PARAMETER.
        ''')


class x_cpmd_section_input_TDDFT_PROPERTY(MSection):
    '''
    Calculate properties of excited states at the end of an \\refkeyword{ELECTRONIC
    SPECTRA} calculations. default is to calculate properties for all states. Adding the
    keyword {\\bf STATE} allows to restrict the calculation to only one state. The number
    of the state is read from the next line.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_PROPERTY_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword PROPERTY.
        ''')

    x_cpmd_input_TDDFT_PROPERTY_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword PROPERTY.
        ''')


class x_cpmd_section_input_TDDFT_REORDER_LOCAL(MSection):
    '''
    Reorder the localized states according to a distance criteria. The number of reference
    atoms is read from the next line. On the following line the position of the reference
    atoms within the set of all atoms has to be given. The keyword \\refkeyword{LOCALIZE}
    is automatically set. The minimum distance of the center of charge of each state to
    the reference atoms is calculated and the states are ordered with respect to
    decreasing distance. Together with the {\\sl SUBSPACE} option in a \\refkeyword{TAMM-
    DANCOFF} calculation this can be used to select specific states for a calculation.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_REORDER_LOCAL_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REORDER_LOCAL.
        ''')

    x_cpmd_input_TDDFT_REORDER_LOCAL_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REORDER_LOCAL.
        ''')


class x_cpmd_section_input_TDDFT_REORDER(MSection):
    '''
    Reorder the canonical Kohn--Sham orbitals prior to a TDDFT calculation. The number of
    states to be reordered is read from the next line. On the following line the final
    rank of each states has to be given. The first number given corresponds to the HOMO,
    the next to the HOMO - 1 and so on. All states down to the last one changed have to be
    specified, no holes are allowed. This keyword can be used together with the {\\sl
    SUBSPACE} option in a \\refkeyword{TAMM-DANCOFF} calculation to select arbitrary
    states. Default is to use the ordering of states according to the Kohn--Sham
    eigenvalues.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_REORDER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword REORDER.
        ''')

    x_cpmd_input_TDDFT_REORDER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword REORDER.
        ''')


class x_cpmd_section_input_TDDFT_ROTATION_PARAMETER(MSection):
    '''
    The parameters for the orbital rotations in an optimized subspace calculation (see
    \\refkeyword{TAMM-DANCOFF}) are read from the next line. The total number of iterations
    (default 50), the convergence criteria (default $10^{-6}$) and the step size (default
    0.5) have to be given.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_ROTATION_PARAMETER_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword ROTATION_PARAMETER.
        ''')

    x_cpmd_input_TDDFT_ROTATION_PARAMETER_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword ROTATION_PARAMETER.
        ''')


class x_cpmd_section_input_TDDFT(MSection):
    '''
    Input for TDDFT calculations
    '''

    m_def = Section(validate=False)

    x_cpmd_input_TDDFT_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section TDDFT even without a keyword.
        ''')

    x_cpmd_section_input_TDDFT_DAVIDSON_RDIIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_DAVIDSON_RDIIS'),
        repeats=True)

    x_cpmd_section_input_TDDFT_DIAGONALIZER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_DIAGONALIZER'),
        repeats=True)

    x_cpmd_section_input_TDDFT_EXTPOT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_EXTPOT'),
        repeats=True)

    x_cpmd_section_input_TDDFT_FORCE_STATE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_FORCE_STATE'),
        repeats=True)

    x_cpmd_section_input_TDDFT_LOCALIZATION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_LOCALIZATION'),
        repeats=True)

    x_cpmd_section_input_TDDFT_MOLECULAR_STATES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_MOLECULAR_STATES'),
        repeats=True)

    x_cpmd_section_input_TDDFT_PCG_PARAMETER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_PCG_PARAMETER'),
        repeats=True)

    x_cpmd_section_input_TDDFT_PROPERTY = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_PROPERTY'),
        repeats=True)

    x_cpmd_section_input_TDDFT_REORDER_LOCAL = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_REORDER_LOCAL'),
        repeats=True)

    x_cpmd_section_input_TDDFT_REORDER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_REORDER'),
        repeats=True)

    x_cpmd_section_input_TDDFT_ROTATION_PARAMETER = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT_ROTATION_PARAMETER'),
        repeats=True)


class x_cpmd_section_input_VDW_VDW_PARAMETERS(MSection):
    '''
    Parameters for empirical van der Waals correction schemes are set with the keyword.
    This requires the \\refkeyword{VDW CORRECTION} keyword to be set in the \\&CPMD section.
    For Grimme's {\\bf DFT-D2} type (see below) an automatic assignment of the parameters
    can be requested by putting {\\bf ALL DFT-D2} on the next line. Otherwise the number of
    pairs {\\itshape NVDW} is read from the next line and followed by {\\itshape NVDW} lines
    of parameters: {\\itshape TYPE}, $\\alpha$, $\\beta$, $C_6^{\\alpha\\beta}$,
    $R_0^{\\alpha\\beta}$, and $d$ for each pair of atom types $\\alpha$ and $\\beta$, where
    $\\alpha$ and $\\beta$ are the indexes of pseudopotentials (and their associated groups
    of atoms) in the order they are listed in the \\&ATOMS section. For type {\\bf DFT-D2}
    only $\\alpha$ and $\\beta$ are required. If the other parameters are ommited the
    internal table of parameters is used. % Note:  References to two papers by R. LeSar
    have % been removed from this entry because Elstner's % damping function is quite
    different from LeSars, % Elstner does not reference LeSar's work, % and LeSar's
    damping function was adopted from % earlier work (ie., LeSar was not the first to %
    use such corrections.)  It does appear that % LeSar's function may be in the CPMD
    source code, % but it is commented out.  A presently implemented damped dispersion
    model, described by M. Elstner {\\itshape et al.}\\cite{Elstner}, having the same form
    as that constructed by Mooij {\\itshape et al.}\\cite{mooij:99}, is activated by
    specifying {\\bf C6} as {\\itshape TYPE}.  This model is expressed as % Elstner's
    Damping function: \\begin{equation} \\label{elstner-damping-function} %\\ref{elstner-
    damping-function} E_{vdW} = \\sum_{ij}
    \\frac{C_6^{\\alpha\\beta}}{{R^{\\alpha\\beta}_{ij}}^6} \\left(1 - \\exp{ \\left[-d
    \\left(\\frac{R^{\\alpha\\beta}_{ij}}{R^{\\alpha\\beta}_0} \\right)^7 \\right]} \\right)^4.
    \\end{equation} A table of parameters appropriate for this particular model, using the
    PBE and BLYP functionals, is available \\cite{williams-vdw:06}.  Alternatively Van der
    Waals correction according to Grimme can be used \\cite{Grimme06} by selecting
    {\\itshape TYPE} {\\bf DFT-D2}. \\begin{equation} E_{disp} = - s_6 \\sum_{i=1}^{N_{at} -1}
    \\sum_{j=i+1}^{N_{at}} \\frac{C_6^{ij}}{R_{ij}^6} f_{dmp} (R_{ij}) \\end{equation} The
    values of $C_6$ and $R_0$ are not specific that are used by this method are taken from
    \\cite{Grimme06} and stored internally (see above for details). Namely, all elements
    from H ($Z=1$) to Rn ($Z=86$) are available, whereas elements beyond Rn give by
    default a zero contribution. Note that the parameter $s_6$ depends on the functional
    used and has to be provided consistently with the DFT one chosen for the calculation.
    The following line has to be added {S6GRIMME} and the type of functional is read from
    the next line. One of the following labels has to be provided: {BP86, BLYP, B3LYP,
    PBE, TPSS, REVPBE, PBE0}. Note that Grimme vdW does not support other functionals.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_VDW_VDW_PARAMETERS_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword VDW_PARAMETERS.
        ''')

    x_cpmd_input_VDW_VDW_PARAMETERS_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword VDW_PARAMETERS.
        ''')


class x_cpmd_section_input_VDW_WANNIER_CORRECTION(MSection):
    '''
    Between these opening and ending keywords, the partitioning of the system and the
    calculation procedure must be selected. Three implementatons are available for
    partitioning the system: (1) choosing a {\\it zlevel}, namely a z coordinate separating
    the first fragment form the second (this is appropriate for cases where there are only
    two fragments such as, for instance two graphene layers or adsorption of molecules on
    surfaces); in this case the keyword FRAGMENT ZLEVEL must be used. (2) give reference
    ion and a cut-off radius around which WFCs  are supposed to belong to the given atom
    or fragment; in this case the keyword FRAGMENT RADIUS must be used. (3) the system is
    subdivided into fragments automatically detected by using predefined covalent bond
    radii. in this case the keyword FRAGMENT BOND must be used. This is also the default
    in case no specification is done.  The syntax for the different options is:  VERSION
    iswitchvdw (method 1 \\cite{psil1} or 2 \\cite{psil2})  FRAGMENT ZLEVEL  zlevel (in
    a.u.)  FRAGMENT RADIUS  multifrag  i radius(i)  ...  FRAGMENT BOND  tollength
    DAMPING  a6  RESTART WANNIER  ENERGY MONOMER  enmonomer  TOLERANCE WANNIER  tolwann
    TOLERANCE REFERENCE  tolref  CHANGE BONDS  nboadwf  i  j $\\pm$ 1   CELL  nxvdw nyvdw
    nzvdw  PRINT $[$INFO,FRAGMENT,C6,FORCES$]$  Note that the total number of WFCs in your
    system depends on the spin description you use (1 for LSD, 2 for LDA). The coefficient
    a6 is the smoothing parameter and the reference total energy intended as a sum of all
    the total energies of your fragments (e.g. the ETOT you get by a standard calculation
    not including vdW corrections). For a6 the suggested parameter is 20.0 \\cite{molphy}.
    Note that the two possible vdW options, EMPIRICAL CORRECTION  and WANNIER CORRECTION
    are mutually exclusive.
    '''

    m_def = Section(validate=False)

    x_cpmd_input_VDW_WANNIER_CORRECTION_options = Quantity(
        type=str,
        shape=[],
        description='''
        The options given for keyword WANNIER_CORRECTION.
        ''')

    x_cpmd_input_VDW_WANNIER_CORRECTION_parameters = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters for keyword WANNIER_CORRECTION.
        ''')


class x_cpmd_section_input_VDW(MSection):
    '''
    Empirical van der Waals correction or van der Waals interaction based on Wannier
    functions
    '''

    m_def = Section(validate=False)

    x_cpmd_input_VDW_default_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        The parameters that are present in the section VDW even without a keyword.
        ''')

    x_cpmd_section_input_VDW_VDW_PARAMETERS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_VDW_VDW_PARAMETERS'),
        repeats=True)

    x_cpmd_section_input_VDW_WANNIER_CORRECTION = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_VDW_WANNIER_CORRECTION'),
        repeats=True)


class x_cpmd_section_input(MSection):
    '''
    Contains the CPMD input file contents.
    '''

    m_def = Section(validate=False)

    x_cpmd_section_input_ATOMS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_ATOMS'),
        repeats=True)

    x_cpmd_section_input_BASIS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_BASIS'),
        repeats=True)

    x_cpmd_section_input_CLASSIC = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CLASSIC'),
        repeats=True)

    x_cpmd_section_input_CPMD = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_CPMD'),
        repeats=True)

    x_cpmd_section_input_DFT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_DFT'),
        repeats=True)

    x_cpmd_section_input_EXTE = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_EXTE'),
        repeats=True)

    x_cpmd_section_input_HARDNESS = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_HARDNESS'),
        repeats=True)

    x_cpmd_section_input_INFO = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_INFO'),
        repeats=True)

    x_cpmd_section_input_LINRES = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_LINRES'),
        repeats=True)

    x_cpmd_section_input_PATH = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PATH'),
        repeats=True)

    x_cpmd_section_input_PIMD = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PIMD'),
        repeats=True)

    x_cpmd_section_input_PROP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PROP'),
        repeats=True)

    x_cpmd_section_input_PTDDFT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_PTDDFT'),
        repeats=True)

    x_cpmd_section_input_QMMM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_QMMM'),
        repeats=True)

    x_cpmd_section_input_RESP = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_RESP'),
        repeats=True)

    x_cpmd_section_input_SYSTEM = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_SYSTEM'),
        repeats=True)

    x_cpmd_section_input_TDDFT = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_TDDFT'),
        repeats=True)

    x_cpmd_section_input_VDW = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input_VDW'),
        repeats=True)


class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_cpmd_section_input = SubSection(
        sub_section=SectionProxy('x_cpmd_section_input'),
        repeats=True)
