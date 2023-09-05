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

from nomad.parsing.file_parser import TextParser
from nomad.datamodel import EntryArchive
from nomad.datamodel.metainfo.simulation.run import Run
from nomad.datamodel.metainfo.workflow import Link, TaskReference
from nomad.datamodel.metainfo.simulation.workflow import (
    GW, GWMethod, DMFT, DMFTMethod, XS, XSMethod, MaxEnt, MaxEntMethod,
    PhotonPolarization, PhotonPolarizationMethod, PhotonPolarizationResults
)


def extract_section(source: EntryArchive, path: str):
    """Extract the (last) section from `source` given by `path`. Separators in path are done
    using `/`. Examples:

    section_system = extract_section(archive, 'run/system)
    spectra = extract_section(archive, 'run/calculation/spectra')

    Args:
        source (EntryArchive): targeted archive
        path (str): path to the desired section to be extracted

    Returns:
        MSection: extracted section
    """
    section_segments = path.split('/')
    for section in section_segments:
        try:
            value = getattr(source, section)
            source = value[-1] if isinstance(value, list) else value
        except Exception:
            return
    return source


def get_files(pattern: str, filepath: str, stripname: str = '', deep: bool = True):
    """Get files following the `pattern` with respect to the file `stripname` (usually this
    being the mainfile of the given parser) up to / down from the `filepath` (`deep=True` going
    down, `deep=False` up)

    Args:
        pattern (str): targeted pattern to be found
        filepath (str): filepath to start the search
        stripname (str, optional): name with respect to which do the search. Defaults to ''.
        deep (bool, optional): boolean setting the path in the folders to scan (up or down). Defaults to True.

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


class BeyondDFTWorkflowsParser:
    '''
    Generates automatic beyondDFT (GW, BSE, DMFT) workflows. Main classes for parsers will
    inherit from here if some automatic workflow parsing has been implemented.
    '''
    def __init__(self, archive: EntryArchive, _child_archives: dict, _xs_spectra_types: list, logger):
        self.archive = archive
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
            sec_run = workflow_archive.m_create(Run)
        sec_run.program = self.archive.run[-1].program

    def parse_gw_workflow(self, gw_archive: EntryArchive, gw_workflow_archive: EntryArchive):
        """Automatically parses the GW workflow. Here, `self.archive` is the DFT archive.

        Args:
            gw_archive (EntryArchive): the GW archive
            gw_workflow_archive (EntryArchive): the GW workflow archive
        """
        self.run_workflow_archive(gw_workflow_archive)
        gw_workflow_archive.run[-1].m_add_sub_section(Run.system, self.archive.run[-1].system[-1])

        workflow = GW(method=GWMethod())
        workflow.name = 'GW'

        # Method
        method_gw = extract_section(gw_archive, 'run/method/gw')
        method_xcfunctional = extract_section(self.archive, 'run/method/dft/xc_functional')
        method_basisset = extract_section(self.archive, 'run/method/electrons_representation')
        workflow.method.gw_method_ref = method_gw
        workflow.method.starting_point = method_xcfunctional
        workflow.method.electrons_representation = method_basisset

        # Inputs and Outputs
        input_structure = extract_section(self.archive, 'run/system')
        dft_calculation = extract_section(self.archive, 'run/calculation')
        gw_calculation = extract_section(gw_archive, 'run/calculation')
        if input_structure:
            workflow.m_add_sub_section(
                GW.inputs, Link(name='Input structure', section=input_structure))
        if gw_calculation:
            workflow.m_add_sub_section(
                GW.outputs, Link(name='Output GW calculation', section=gw_calculation))

        # DFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DFT'
            # TODO check why this re-writting is necessary to not repeat sections inside tasks
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dft_calculation:
                task.outputs = [Link(name='Output DFT calculation', section=dft_calculation)]
            workflow.m_add_sub_section(GW.tasks, task)

        # GW task
        if gw_archive.workflow2:
            task = TaskReference(task=gw_archive.workflow2)
            task.name = 'GW'
            if dft_calculation:
                task.inputs = [Link(name='Output DFT calculation', section=dft_calculation)]
            if gw_calculation:
                task.outputs = [Link(name='Output GW calculation', section=gw_calculation)]
            workflow.m_add_sub_section(GW.tasks, task)

        gw_workflow_archive.workflow2 = workflow

    def parse_photon_workflow(self):
        """Automatically parses the PhotonPolarization workflow. Here, `self.archive` is
        the photon_workflow archive, and `self._child_archives` the archives for SinglePoint
        photons.
        """
        workflow = PhotonPolarization(method=PhotonPolarizationMethod(), results=PhotonPolarizationResults())
        workflow.name = 'BSE'  # this entry contains the full BSE calculation for all photon polarizations

        # Method
        method_bse = extract_section(self.archive, 'run/method/bse')
        workflow.method.bse_method_ref = method_bse

        # Inputs
        input_structure = extract_section(self.archive, 'run/system')
        workflow.m_add_sub_section(
            PhotonPolarization.inputs, Link(name='Input structure', section=input_structure))
        input_method = extract_section(self.archive, 'run/method')
        workflow.m_add_sub_section(
            PhotonPolarization.inputs, Link(name='Input BSE methodology', section=input_method))

        # Outputs
        spectra = []
        for index, path in enumerate(self._child_archives.keys()):
            archive = self._child_archives.get(path)

            output_polarization = extract_section(archive, 'run/calculation')
            if output_polarization:
                workflow.m_add_sub_section(
                    PhotonPolarization.outputs,
                    Link(name=f'Output polarization {index + 1}', section=output_polarization))
                spectra.append(output_polarization.spectra[0])

            # Tasks
            if archive.workflow2:
                task = TaskReference(task=archive.workflow2)
                task.name = f'Photon {index + 1}'
                input_photon_method = archive.run[-1].method[0]
                if input_photon_method and input_structure:
                    task.inputs = [
                        Link(name='Input structure', section=input_structure),
                        Link(name='Input photon parameters', section=input_photon_method)]
                if output_polarization:
                    task.outputs = [
                        Link(name=f'Output polarization {index + 1}', section=output_polarization)]
                workflow.m_add_sub_section(PhotonPolarization.tasks, task)

        # Results
        workflow.results.n_polarizations = len(spectra)
        workflow.results.spectrum_polarization = spectra

        self.archive.workflow2 = workflow

    def parse_xs_workflow(self, xs_archives: EntryArchive, xs_workflow_archive: EntryArchive):
        """Automatically parses the XS workflow. Here, `self.archive` is the DFT archive.

        Args:
            xs_archives (EntryArchive): the XS archive
            xs_workflow_archive (EntryArchive): the XS workflow archive
        """
        self.run_workflow_archive(xs_workflow_archive)
        xs_workflow_archive.run[-1].m_add_sub_section(Run.system, self.archive.run[-1].system[-1])

        def extract_polarization_outputs():
            output = []
            index = 0
            for path, archive in self._child_archives.items():
                if os.path.basename(path).split('_')[0] in self._xs_spectra_types:
                    output_polarization = archive.run[-1].calculation[-1]
                    output.append(Link(name=f'Output polarization {index + 1}', section=output_polarization))
                    index += 1
            return output

        workflow = XS(method=XSMethod())
        workflow.name = 'XS'

        # Inputs and Outputs
        input_structure = extract_section(self.archive, 'run/system')
        dft_calculation = extract_section(self.archive, 'run/calculation')
        polarization_calculations = extract_polarization_outputs()
        if input_structure:
            workflow.m_add_sub_section(
                XS.inputs, Link(name='Input structure', section=input_structure))
        for index, polarizations in enumerate(polarization_calculations):
            workflow.m_add_sub_section(
                XS.outputs, Link(name=f'Polarization {index + 1}', section=polarizations))

        # DFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DFT'
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dft_calculation:
                task.outputs = [Link(name='Output DFT calculation', section=dft_calculation)]
            workflow.m_add_sub_section(XS.tasks, task)

        # Spectra task
        for index, xs_archive in enumerate(xs_archives):
            if not xs_archive.workflow2:
                continue
            task = TaskReference(task=xs_archive.workflow2)
            task.name = f'BSE {index + 1}'
            if dft_calculation:
                xs_archive.workflow2.m_add_sub_section(
                    PhotonPolarization.inputs, Link(name='Output DFT calculation', section=dft_calculation))
                task.inputs = [Link(name='Output DFT calculation', section=dft_calculation)]
                for i_photon, photon_task in enumerate(xs_archive.workflow2.tasks):
                    photon_task.m_add_sub_section(
                        TaskReference.inputs, Link(name='Output DFT calculation', section=dft_calculation))
                    if photon_task.m_xpath('outputs[-1].section'):
                        task.m_add_sub_section(TaskReference.outputs, Link(name=f'Polarization {i_photon + 1}', section=photon_task.outputs[-1].section))
            workflow.m_add_sub_section(XS.tasks, task)

        xs_workflow_archive.workflow2 = workflow

    def parse_dmft_maxent_workflow(self, maxent_archive: EntryArchive, workflow_archive: EntryArchive):
        """Automatically parses the DMFT+MaxEnt workflow. Here, `self.archive` is the DMFT archive.

        Args:
            maxent_archive (EntryArchive): the MaxEnt archive
            workflow_archive (EntryArchive): the DMFT+MaxEnt workflow archive
        """

        workflow = MaxEnt(method=MaxEntMethod())

        # Method
        method_dmft = extract_section(self.archive, 'run/method/dmft')
        method_maxent = extract_section(maxent_archive, 'run/method')
        workflow.method.dmft_method_ref = method_dmft
        workflow.method.maxent_method_ref = method_maxent

        # Inputs and Outputs
        input_structure = extract_section(self.archive, 'run/system')
        dmft_calculation = extract_section(self.archive, 'run/calculation')
        maxent_calculation = extract_section(maxent_archive, 'run/calculation')
        workflow_maxent_calculation = extract_section(workflow_archive, 'run/calculation')
        if input_structure:
            workflow.m_add_sub_section(
                MaxEnt.inputs, Link(name='Input structure', section=input_structure))
        if maxent_calculation and workflow_maxent_calculation:
            outputs = [
                Link(name='Output MaxEnt Sigma calculation', section=maxent_calculation),
                Link(name='Output MaxEnt GF and DOS calculation', section=workflow_maxent_calculation)]
            workflow.outputs = outputs

        # DMFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DMFT'
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dmft_calculation:
                task.outputs = [Link(name='Output DMFT calculation', section=dmft_calculation)]
            workflow.m_add_sub_section(MaxEnt.tasks, task)

        # MaxEnt task
        if maxent_archive.workflow2:
            task = TaskReference(task=maxent_archive.workflow2)
            task.name = 'MaxEnt'
            if dmft_calculation:
                task.inputs = [Link(name='Output DMFT calculation', section=dmft_calculation)]
            if maxent_calculation:
                task.outputs = [Link(name='Output MaxEnt Sigma calculation', section=maxent_calculation)]
            workflow.m_add_sub_section(GW.tasks, task)

        workflow_archive.workflow2 = workflow

    def parse_dmft_workflow(self, wannier_archive: EntryArchive, dmft_workflow_archive: EntryArchive):
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

        workflow = DMFT(method=DMFTMethod())
        workflow.name = 'DMFT'

        # Method
        method_proj = extract_section(wannier_archive, 'run/method/projection')
        method_dmft = extract_section(self.archive, 'run/method/dmft')
        workflow.method.projection_method_ref = method_proj
        workflow.method.dmft_method_ref = method_dmft

        # Inputs and Outputs
        input_structure = extract_section(wannier_archive, 'run/system')
        wannier_calculation = extract_section(wannier_archive, 'run/calculation')
        dmft_calculation = extract_section(self.archive, 'run/calculation')
        if input_structure:
            workflow.m_add_sub_section(
                DMFT.inputs, Link(name='Input structure', section=input_structure))
        if dmft_calculation:
            workflow.m_add_sub_section(
                DMFT.outputs, Link(name='Output DMFT calculation', section=dmft_calculation))

        # Wannier90 task
        if wannier_archive.workflow2:
            task = TaskReference(task=wannier_archive.workflow2)
            task.name = 'Projection'
            # TODO check why this re-writting is necessary to not repeat sections inside tasks
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if wannier_calculation:
                task.outputs = [Link(name='Output Projection calculation', section=wannier_calculation)]
            workflow.m_add_sub_section(DMFT.tasks, task)

        # DMFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DMFT'
            if wannier_calculation:
                task.inputs = [Link(name='Output Projection calculation', section=wannier_calculation)]
            if dmft_calculation:
                task.outputs = [Link(name='Output DMFT calculation', section=dmft_calculation)]
            workflow.m_add_sub_section(DMFT.tasks, task)

        dmft_workflow_archive.workflow2 = workflow


class DataANDTextParser(TextParser):  # TODO rename to 'DataTextParser' after changes are done in NOMAD
    """Parser for structured data text files with a few lines containing unstructured text.

    Args:
        mainfile: the file to be parsed.
    """
    def __init__(self):
        super().__init__()

    def init_quantities(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = np.loadtxt(self.mainfile)
        return self._data
