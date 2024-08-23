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
    MSection,
    Package,
    Quantity,
    Section,
    SubSection,
    JSON,
)
from nomad.datamodel.hdf5 import HDF5Reference
import runschema.run  # pylint: disable=unused-import
import runschema.calculation  # pylint: disable=unused-import
import runschema.method  # pylint: disable=unused-import
import runschema.system  # pylint: disable=unused-import


m_package = Package()


class Method(runschema.run.Method):
    """
    Contains the specifications of the method.
    """

    m_def = Section(validate=False, extends_base_section=True)

    x_soliddmft_dft_input = Quantity(
        type=JSON,
        description="""
        DFT input parameters.
        """,
    )

    x_soliddmft_dft_misc_input = Quantity(
        type=JSON,
        description="""
        Miscellaneous DFT input parameters.
        """,
    )

    x_soliddmft_dft_symmcorr_input = Quantity(
        type=JSON,
        description="""
        Symmetry of correlated orbitals DFT input parameters.
        """,
    )

    x_soliddmft_general_params = Quantity(
        type=JSON,
        description="""
        General DMFT input parameters.
        """,
    )

    x_soliddmft_solver_params = Quantity(
        type=JSON,
        description="""
        DMFT solver parameters.
        """,
    )

    x_soliddmft_advanced_params = Quantity(
        type=JSON,
        description="""
        Advanced DMFT input parameters.
        """,
    )

    # TODO determine standard dimensions for projection_matrix:
    #   KMesh.n_points x n_atoms_per_unit_cell x n_orbitals? x n_bands?
    x_soliddmft_projection_matrix = Quantity(
        type=np.complex128,
        shape=['*', '*', '*', '*'],
        description="""
        Projection matrices from Bloch bands to virtual projected orbitals.
        """,
    )


class Program(runschema.run.Program):
    """
    Contains the specifications of the program.
    """

    m_def = Section(validate=False, extends_base_section=True)

    x_soliddmft_hash = Quantity(
        type=str,
        description="""
        Hash label for the solid_dmft repository branch used.
        """,
    )

    x_soliddmft_solver_hash = Quantity(
        type=str,
        description="""
        Hash label for the solver repository branch used.
        """,
    )

    x_soliddmft_triqs_hash = Quantity(
        type=str,
        description="""
        Hash label for the TRIQS repository branch used.
        """,
    )

    x_soliddmft_solver_version = Quantity(
        type=str,
        description="""
        Version tag of solver.
        """,
    )

    x_soliddmft_triqs_version = Quantity(
        type=str,
        description="""
        Version tag of TRIQS.
        """,
    )


class x_soliddmft_observables_parameters(MSection):
    """
    Section containing the post-processed observables of solid_dmft.
    """

    m_def = Section(validate=False)

    x_soliddmft_Delta_time = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Imaginary or real frequency hybridization function.
            dim n_inequiv_shells x corr_shells.dim x n_tau x 2 (real+imag)
        """,
    )

    x_soliddmft_Delta_freq = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Imaginary time hybridization function.
            dim n_inequiv_shells x corr_shells.dim x n_tau x 2 (real+imag)
        """,
    )

    x_soliddmft_G0_freq = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Imaginary or real frequency Weiss field.
            dim n_inequiv_shells x corr_shells.dim x 2*n_iw x 2 (real+imag)
        """,
    )

    x_soliddmft_Gimp_freq = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Imaginary or real frequency impurity green function.
            dim n_inequiv_shells x corr_shells.dim x 2*n_iw x 2 (real+imag)
        """,
    )

    x_soliddmft_Gimp_time = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Imaginary time representation of the impurity green function.
            dim n_inequiv_shells x corr_shells.dim x n_tau x 2 (real+imag)
        """,
    )

    x_soliddmft_Sigma_freq = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Imaginary frequency self-energy obtained from the Dyson equation.
            dim n_inequiv_shells x corr_shells.dim x 2*n_iw x 2 (real+imag)
        """,
    )

    x_soliddmft_imp_gb2 = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Site G(beta/2), proxy for total density of states at the Fermi level. Low values
        correlate with the presence of a gap.
        """,
    )

    x_soliddmft_imp_occ = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Total mean site occupation.
        """,
    )

    x_soliddmft_orb_Z = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Orbital resolved quasiparticle weight (eff_mass / renormalized_mass). As obtained
        by linearizing the self-energy around w=0:
            Z = inv(1.0 - d [Re Sigma] / dw at w=0)
        """,
    )

    x_soliddmft_orb_gb2 = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Orbital resolved G(beta/2), proxy for projected density of states at the Fermi
        level. Low value of orb_gb2 correlated with the presence of a gap.
        """,
    )

    x_soliddmft_orb_occ = Quantity(
        type=HDF5Reference,
        shape=['*'],
        description="""
        Orbital mean site occupation.
        """,
    )


class ScfIteration(runschema.calculation.ScfIteration):
    """
    Every scf_iteration section represents a self-consistent field (SCF) iteration,
    and gives detailed information on the SCF procedure of the specified quantities.
    """

    m_def = Section(validate=False, extends_base_section=True)

    x_soliddmft_convergence_obs = Quantity(
        type=JSON,
        description="""
        Convergence of the observable parameters per impurity: Etot, G0, Gimp, Sigma,
        imp_occ, mu.
        """,
    )

    x_soliddmft_convergence_orb_occ = Quantity(
        type=np.float64,
        shape=['n_orbitals'],
        description="""
        Convergence of the orbital occupations in the impurity.
        """,
    )

    x_soliddmft_observables = SubSection(
        sub_section=x_soliddmft_observables_parameters.m_def, repeats=True
    )
