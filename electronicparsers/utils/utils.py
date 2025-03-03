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
import os
from glob import glob

from typing import Optional, Union
from nomad.utils import extract_section
from nomad.datamodel import EntryArchive
from runschema.run import Run
from nomad.datamodel.metainfo.workflow import Link, TaskReference
from simulationworkflowschema import (
    DFTPlusGW,
    DFTPlusGWMethod,
    DFTPlusTBPlusDMFT,
    DFTPlusTBPlusDMFTMethod,
    XS,
    XSMethod,
    FirstPrinciplesPlusTB,
    FirstPrinciplesPlusTBMethod,
    DMFTPlusMaxEnt,
    DMFTPlusMaxEntMethod,
    PhotonPolarization,
    PhotonPolarizationMethod,
    PhotonPolarizationResults,
)

# Special file-format workflow definition
from .magres_workflow import (
    NMRMagRes,
    NMRMagResMethod,
    NMRMagResResults,
)


def get_files(pattern: str, filepath: str, stripname: str = '', deep: bool = True):
    """Get files following the `pattern` with respect to the file `stripname` (usually this
    being the mainfile of the given parser) up to / down from the `filepath` (`deep=True` going
    down, `deep=False` up)

    Args:
        pattern (str): targeted pattern to be found
        filepath (str): filepath to start the search
        stripname (str, optional): name with respect to which do the search. Defaults to ''.
        deep (bool, optional): boolean setting the path in the folders to scan (down or up). Defaults to down=True.

    Returns:
        list: List of found files.
    """
    for _ in range(10):
        filenames = glob(f'{os.path.dirname(filepath)}/{pattern}')
        pattern = os.path.join('**' if deep else '..', pattern)
        if filenames:
            break

    if len(filenames) > 1:
        # filter files that match
        suffix = os.path.basename(filepath).strip(stripname)
        matches = [f for f in filenames if suffix in f]
        filenames = matches if matches else filenames

    filenames = [f for f in filenames if os.access(f, os.F_OK)]
    return filenames


# ! Consider implementation of `JSONEncoder` class for direct conversion during dump
def numpy_type_to_json_serializable(quantity) -> Optional[Union[bool, int, float]]:
    """Converts numpy data types to native Python types suitable for JSON serialization.

    Args:
        quantity (Union[np.bool_, np.int32, np.int64, np.float64]): The numpy data type
            value to be converted.

    Returns:
        Union[bool, int, float]: The converted native Python type.
    """
    if isinstance(quantity, np.bool_):
        return bool(quantity)
    if isinstance(quantity, np.integer):
        return int(quantity)
    if isinstance(quantity, np.floating):
        return float(quantity)
    return None


class BeyondDFTWorkflowsParser:
    """
    Generates automatic beyondDFT (GW, BSE, DMFT) workflows. Main classes for parsers will
    inherit from here if some automatic workflow parsing has been implemented.
    """

    def __init__(
        self,
        archive: EntryArchive,
        _child_archives: dict,
        _xs_spectra_types: list,
        logger,
    ):
        self.archive = archive
        self.logger = logger
        self._child_archives = _child_archives
        self._xs_spectra_types = _xs_spectra_types

    def run_workflow_archive(self, workflow_archive: EntryArchive):
        """Initializes the workflow archive by checking if Run exists or not, as well as
        copying Program and System into it.

        Args:
            workflow_archive (EntryArchive): the workflow archive targeted for initialization
        """
        if workflow_archive.run:
            sec_run = workflow_archive.run[-1]
        else:
            sec_run = Run()
            workflow_archive.run.append(sec_run)
        sec_run.program = self.archive.run[-1].program

    def parse_gw_workflow(
        self, gw_archive: EntryArchive, gw_workflow_archive: EntryArchive
    ):
        """Automatically parses the GW workflow. Here, `self.archive` is the DFT archive.

        Args:
            gw_archive (EntryArchive): the GW archive
            gw_workflow_archive (EntryArchive): the GW workflow archive
        """
        self.run_workflow_archive(gw_workflow_archive)
        gw_workflow_archive.run[-1].m_add_sub_section(
            Run.system, self.archive.run[-1].system[-1]
        )

        workflow = DFTPlusGW(method=DFTPlusGWMethod())

        # Method
        method_gw = extract_section(gw_archive, ['run', 'method', 'gw'])
        method_xcfunctional = extract_section(
            self.archive, ['run', 'method', 'dft', 'xc_functional']
        )
        method_basisset = extract_section(
            self.archive, ['run', 'method', 'electrons_representation']
        )
        workflow.method.gw_method_ref = method_gw
        workflow.method.starting_point = method_xcfunctional
        workflow.method.electrons_representation = method_basisset

        # Inputs and Outputs
        input_structure = extract_section(self.archive, ['run', 'system'])
        dft_calculation = extract_section(self.archive, ['run', 'calculation'])
        gw_calculation = extract_section(gw_archive, ['run', 'calculation'])
        if input_structure:
            workflow.m_add_sub_section(
                DFTPlusGW.inputs, Link(name='Input structure', section=input_structure)
            )
        if gw_calculation:
            workflow.m_add_sub_section(
                DFTPlusGW.outputs,
                Link(name='Output GW calculation', section=gw_calculation),
            )

        # DFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DFT'
            # TODO check why this re-writting is necessary to not repeat sections inside tasks
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dft_calculation:
                task.outputs = [
                    Link(name='Output DFT calculation', section=dft_calculation)
                ]
            workflow.m_add_sub_section(DFTPlusGW.tasks, task)

        # GW task
        if gw_archive.workflow2:
            task = TaskReference(task=gw_archive.workflow2)
            task.name = 'GW'
            if dft_calculation:
                task.inputs = [
                    Link(name='Output DFT calculation', section=dft_calculation)
                ]
            if gw_calculation:
                task.outputs = [
                    Link(name='Output GW calculation', section=gw_calculation)
                ]
            workflow.m_add_sub_section(DFTPlusGW.tasks, task)

        gw_workflow_archive.workflow2 = workflow

    def parse_tb_workflow(
        self,
        tb_archive: EntryArchive,
        first_principles_calculation_archive: EntryArchive,
        tb_workflow_archive: EntryArchive,
    ):
        """Automatically parses the TB workflow. Here, `self.archive` is the DFT archive.

        Args:
            tb_archive (EntryArchive): the Tight-Binding archive
            first_principles_calculation_archive (EntryArchive): the first-principles-calculation archive
            tb_workflow_archive (EntryArchive): the Tight-Binding workflow archive
        """
        self.run_workflow_archive(tb_workflow_archive)
        tb_workflow_archive.run[-1].m_add_sub_section(
            Run.system, first_principles_calculation_archive.run[-1].system[-1]
        )
        workflow = FirstPrinciplesPlusTB(method=FirstPrinciplesPlusTBMethod())

        # Method
        method_first_principles = extract_section(
            first_principles_calculation_archive, ['run', 'method']
        )
        method_tb = extract_section(tb_archive, ['run', 'method', 'tb'])
        workflow.method.first_principles_method_ref = method_first_principles
        workflow.method.tb_method_ref = method_tb

        # Inputs and Outputs
        input_structure = extract_section(
            first_principles_calculation_archive, ['run', 'system']
        )
        first_principles_calculation = extract_section(
            first_principles_calculation_archive, ['run', 'calculation']
        )
        tb_calculation = extract_section(tb_archive, ['run', 'calculation'])
        if input_structure:
            workflow.m_add_sub_section(
                FirstPrinciplesPlusTB.inputs,
                Link(name='Input Structure', section=input_structure),
            )
        if tb_calculation:
            workflow.m_add_sub_section(
                FirstPrinciplesPlusTB.outputs,
                Link(name='Output TB Model', section=tb_calculation),
            )

        # First Principles Calculation task
        if self.archive.workflow2:
            first_principles_task = TaskReference(
                task=first_principles_calculation_archive.workflow2
            )
            first_principles_task.name = 'FirstPrinciples'
            if input_structure:
                first_principles_task.inputs = [
                    Link(name='Input Structure', section=input_structure)
                ]
            if first_principles_calculation:
                first_principles_task.outputs = [
                    Link(
                        name='Output FirstPrinciples Calculation',
                        section=first_principles_calculation,
                    )
                ]
            workflow.m_add_sub_section(
                FirstPrinciplesPlusTB.tasks, first_principles_task
            )

        # TB task
        if tb_archive.workflow2:
            tb_task = TaskReference(task=tb_archive.workflow2)
            tb_task.name = 'TB'
            if first_principles_calculation:
                tb_task.inputs = [
                    Link(
                        name='Input FirstPrinciples Calculation',
                        section=first_principles_calculation,
                    )
                ]
            if tb_calculation:
                tb_task.outputs = [Link(name='Output TB Model', section=tb_calculation)]
            workflow.m_add_sub_section(FirstPrinciplesPlusTB.tasks, tb_task)

        tb_workflow_archive.workflow2 = workflow

    def parse_photon_workflow(self):
        """Automatically parses the PhotonPolarization workflow. Here, `self.archive` is
        the photon_workflow archive, and `self._child_archives` the archives for SinglePoint
        photons.
        """
        workflow = PhotonPolarization(
            method=PhotonPolarizationMethod(), results=PhotonPolarizationResults()
        )
        workflow.name = 'BSE'  # this entry contains the full BSE calculation for all photon polarizations

        # Method
        method_bse = extract_section(self.archive, ['run', 'method', 'bse'])
        workflow.method.bse_method_ref = method_bse

        # Inputs
        input_structure = extract_section(self.archive, ['run', 'system'])
        workflow.m_add_sub_section(
            PhotonPolarization.inputs,
            Link(name='Input structure', section=input_structure),
        )
        input_method = extract_section(self.archive, ['run', 'method'])
        workflow.m_add_sub_section(
            PhotonPolarization.inputs,
            Link(name='Input BSE methodology', section=input_method),
        )

        # Outputs
        spectra = []
        for index, path in enumerate(self._child_archives.keys()):
            archive = self._child_archives.get(path)

            output_polarization = extract_section(archive, ['run', 'calculation'])
            if output_polarization:
                workflow.m_add_sub_section(
                    PhotonPolarization.outputs,
                    Link(
                        name=f'Output polarization {index + 1}',
                        section=output_polarization,
                    ),
                )
                spectra.append(output_polarization.spectra[0])

            # Tasks
            if archive.workflow2:
                task = TaskReference(task=archive.workflow2)
                task.name = f'Photon {index + 1}'
                input_photon_method = archive.run[-1].method[0]
                if input_photon_method and input_structure:
                    task.inputs = [
                        Link(name='Input structure', section=input_structure),
                        Link(
                            name='Input photon parameters', section=input_photon_method
                        ),
                    ]
                if output_polarization:
                    task.outputs = [
                        Link(
                            name=f'Output polarization {index + 1}',
                            section=output_polarization,
                        )
                    ]
                workflow.m_add_sub_section(PhotonPolarization.tasks, task)

        # Results
        workflow.results.n_polarizations = len(spectra)
        workflow.results.spectrum_polarization = spectra

        self.archive.workflow2 = workflow

    def parse_xs_workflow(
        self, xs_archives: EntryArchive, xs_workflow_archive: EntryArchive
    ):
        """Automatically parses the XS workflow. Here, `self.archive` is the DFT archive.

        Args:
            xs_archives (EntryArchive): the XS archive
            xs_workflow_archive (EntryArchive): the XS workflow archive
        """
        self.run_workflow_archive(xs_workflow_archive)
        xs_workflow_archive.run[-1].m_add_sub_section(
            Run.system, self.archive.run[-1].system[-1]
        )

        def extract_polarization_outputs():
            output = []
            index = 0
            for path, archive in self._child_archives.items():
                if os.path.basename(path).split('_')[0] in self._xs_spectra_types:
                    output_polarization = archive.run[-1].calculation[-1]
                    output.append(
                        Link(
                            name=f'Output polarization {index + 1}',
                            section=output_polarization,
                        )
                    )
                    index += 1
            return output

        workflow = XS(method=XSMethod())
        workflow.name = 'XS'

        # Inputs and Outputs
        input_structure = extract_section(self.archive, ['run', 'system'])
        dft_calculation = extract_section(self.archive, ['run', 'calculation'])
        polarization_calculations = extract_polarization_outputs()
        if input_structure:
            workflow.m_add_sub_section(
                XS.inputs, Link(name='Input structure', section=input_structure)
            )
        for index, polarizations in enumerate(polarization_calculations):
            workflow.m_add_sub_section(
                XS.outputs,
                Link(name=f'Polarization {index + 1}', section=polarizations),
            )

        # DFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DFT'
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dft_calculation:
                task.outputs = [
                    Link(name='Output DFT calculation', section=dft_calculation)
                ]
            workflow.m_add_sub_section(XS.tasks, task)

        # Spectra task
        for index, xs_archive in enumerate(xs_archives):
            if not xs_archive.workflow2:
                continue
            task = TaskReference(task=xs_archive.workflow2)
            task.name = f'BSE {index + 1}'
            if dft_calculation:
                xs_archive.workflow2.m_add_sub_section(
                    PhotonPolarization.inputs,
                    Link(name='Output DFT calculation', section=dft_calculation),
                )
                task.inputs = [
                    Link(name='Output DFT calculation', section=dft_calculation)
                ]
                for i_photon, photon_task in enumerate(xs_archive.workflow2.tasks):
                    photon_task.m_add_sub_section(
                        TaskReference.inputs,
                        Link(name='Output DFT calculation', section=dft_calculation),
                    )
                    if photon_task.m_xpath('outputs[-1].section'):
                        task.m_add_sub_section(
                            TaskReference.outputs,
                            Link(
                                name=f'Polarization {i_photon + 1}',
                                section=photon_task.outputs[-1].section,
                            ),
                        )
            workflow.m_add_sub_section(XS.tasks, task)

        xs_workflow_archive.workflow2 = workflow

    def parse_dmft_maxent_workflow(
        self, maxent_archive: EntryArchive, workflow_archive: EntryArchive
    ):
        """Automatically parses the DMFT+MaxEnt workflow. Here, `self.archive` is the DMFT archive.

        Args:
            maxent_archive (EntryArchive): the MaxEnt archive
            workflow_archive (EntryArchive): the DMFT+MaxEnt workflow archive
        """

        workflow = DMFTPlusMaxEnt(method=DMFTPlusMaxEntMethod())

        # Method
        method_dmft = extract_section(self.archive, ['run', 'method', 'dmft'])
        method_maxent = extract_section(maxent_archive, ['run', 'method'])
        workflow.method.dmft_method_ref = method_dmft
        workflow.method.maxent_method_ref = method_maxent

        # Inputs and Outputs
        input_structure = extract_section(self.archive, ['run', 'system'])
        dmft_calculation = extract_section(self.archive, ['run', 'calculation'])
        maxent_calculation = extract_section(maxent_archive, ['run', 'calculation'])
        workflow_maxent_calculation = extract_section(
            workflow_archive, ['run', 'calculation']
        )
        if input_structure:
            workflow.m_add_sub_section(
                DMFTPlusMaxEnt.inputs,
                Link(name='Input structure', section=input_structure),
            )
        if maxent_calculation and workflow_maxent_calculation:
            outputs = [
                Link(
                    name='Output MaxEnt Sigma calculation', section=maxent_calculation
                ),
                Link(
                    name='Output MaxEnt GF and DOS calculation',
                    section=workflow_maxent_calculation,
                ),
            ]
            workflow.outputs = outputs

        # DMFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DMFT'
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dmft_calculation:
                task.outputs = [
                    Link(name='Output DMFT calculation', section=dmft_calculation)
                ]
            workflow.m_add_sub_section(DMFTPlusMaxEnt.tasks, task)

        # MaxEnt task
        if maxent_archive.workflow2:
            task = TaskReference(task=maxent_archive.workflow2)
            task.name = 'MaxEnt'
            if dmft_calculation:
                task.inputs = [
                    Link(name='Output DMFT calculation', section=dmft_calculation)
                ]
            if maxent_calculation:
                task.outputs = [
                    Link(
                        name='Output MaxEnt Sigma calculation',
                        section=maxent_calculation,
                    )
                ]
            workflow.m_add_sub_section(DMFTPlusMaxEnt.tasks, task)

        workflow_archive.workflow2 = workflow

    def parse_dmft_workflow(
        self, wannier_archive: EntryArchive, dmft_workflow_archive: EntryArchive
    ):
        # TODO extend for DFT tasks
        self.run_workflow_archive(dmft_workflow_archive)
        # Check if system exists in the DMFT archive or not, and whether it exists on the
        # Wannier90 archive or not, and then add it.
        try:
            sec_system = self.archive.run[-1].system[-1]
            dmft_workflow_archive.run[-1].m_add_sub_section(Run.system, sec_system)
        except Exception:
            if wannier_archive.run[-1].system[-1]:
                sec_system = wannier_archive.run[-1].system[-1]
                self.archive.run[-1].m_add_sub_section(Run.system, sec_system)
                dmft_workflow_archive.run[-1].m_add_sub_section(Run.system, sec_system)

        workflow = DFTPlusTBPlusDMFT(method=DFTPlusTBPlusDMFTMethod())

        # Method
        method_proj = extract_section(wannier_archive, ['run', 'method', 'tb'])
        method_dmft = extract_section(self.archive, ['run', 'method', 'dmft'])
        workflow.method.tb_method_ref = method_proj
        workflow.method.dmft_method_ref = method_dmft

        # Inputs and Outputs
        input_structure = extract_section(wannier_archive, ['run', 'system'])
        wannier_calculation = extract_section(wannier_archive, ['run', 'calculation'])
        dmft_calculation = extract_section(self.archive, ['run', 'calculation'])
        if input_structure:
            workflow.m_add_sub_section(
                DFTPlusTBPlusDMFT.inputs,
                Link(name='Input structure', section=input_structure),
            )
        if dmft_calculation:
            workflow.m_add_sub_section(
                DFTPlusTBPlusDMFT.outputs,
                Link(name='Output DMFT calculation', section=dmft_calculation),
            )

        # Wannier90 task
        if wannier_archive.workflow2:
            task = TaskReference(task=wannier_archive.workflow2)
            task.name = 'TB'
            # TODO check why this re-writting is necessary to not repeat sections inside tasks
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if wannier_calculation:
                task.outputs = [
                    Link(name='Output TB calculation', section=wannier_calculation)
                ]
            workflow.m_add_sub_section(DFTPlusTBPlusDMFT.tasks, task)

        # DMFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DMFT'
            if wannier_calculation:
                task.inputs = [
                    Link(name='Output TB calculation', section=wannier_calculation)
                ]
            if dmft_calculation:
                task.outputs = [
                    Link(name='Output DMFT calculation', section=dmft_calculation)
                ]
            workflow.m_add_sub_section(DFTPlusTBPlusDMFT.tasks, task)

        dmft_workflow_archive.workflow2 = workflow

    def parse_nmr_magres_file_format(self, nmr_first_principles_archive: EntryArchive):
        """
        Automatically parses the NMR Magres workflow. Here, `self.archive` is the
        NMR magres archive in which we will link the original NMR first principles (CASTEP
        or QuantumEspresso-GIPAW)

        Args:
            nmr_first_principles_archive (EntryArchive): the NMR (first principles)
            SinglePoint archive
        """
        workflow = NMRMagRes(method=NMRMagResMethod(), results=NMRMagResResults())
        workflow.name = 'NMR MagRes'

        # Method
        method_nmr = extract_section(nmr_first_principles_archive, ['run', 'method'])
        workflow.method.nmr_method_ref = method_nmr

        # Inputs and Outputs
        input_structure = extract_section(
            nmr_first_principles_archive, ['run', 'system']
        )
        nmr_magres_calculation = extract_section(self.archive, ['run', 'calculation'])
        if input_structure:
            workflow.m_add_sub_section(
                NMRMagRes.inputs, Link(name='Input structure', section=input_structure)
            )
        if nmr_magres_calculation:
            workflow.m_add_sub_section(
                NMRMagRes.outputs,
                Link(name='Output NMR calculation', section=nmr_magres_calculation),
            )

        # NMR (first principles) task
        if nmr_first_principles_archive.workflow2:
            task = TaskReference(task=nmr_first_principles_archive.workflow2)
            task.name = 'NMR FirstPrinciples'
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if nmr_magres_calculation:
                task.outputs = [
                    Link(
                        name='Output NMR calculation',
                        section=nmr_magres_calculation,
                    )
                ]
            workflow.m_add_sub_section(NMRMagRes.tasks, task)

        self.archive.workflow2 = workflow
