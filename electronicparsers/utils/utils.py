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

import os
from glob import glob

from nomad.datamodel import EntryArchive
from nomad.datamodel.metainfo.simulation.run import Run
from nomad.datamodel.metainfo.workflow import Link, TaskReference
from nomad.datamodel.metainfo.simulation.workflow import (
    GW, GWMethod, ParticleHoleExcitations,
    ParticleHoleExcitationsMethod, ParticleHoleExcitationsResults,
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
    up, `deep=False` down)

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
    def __init__(self, archive: EntryArchive, _child_archives: dict, _xs_spectra_types: list):
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
        sec_run.system = self.archive.run[-1].system

    def parse_gw_workflow(self, gw_archive: EntryArchive, gw_workflow_archive: EntryArchive):
        """Automatically parses the GW workflow. Here, `self.archive` is the DFT archive.

        Args:
            gw_archive (EntryArchive): the GW archive
            gw_workflow_archive (EntryArchive): the GW workflow archive
        """
        self.run_workflow_archive(gw_workflow_archive)

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

        # TODO define Method

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

        def extract_polarization_outputs():
            output = []
            index = 0
            for path, archive in self._child_archives.items():
                if os.path.basename(path).split('_')[0] in self._xs_spectra_types:
                    output_polarization = archive.run[-1].calculation[-1]
                    output.append(Link(name=f'Output polarization {index + 1}', section=output_polarization))
                    index += 1
            return output

        workflow = ParticleHoleExcitations(
            method=ParticleHoleExcitationsMethod(), results=ParticleHoleExcitationsResults())
        workflow.name = 'ParticleHoleExcitations'

        # TODO define Method

        # Results
        bs_dft = extract_section(self.archive, 'run/calculation/band_structure_electronic')
        dos_dft = extract_section(self.archive, 'run/calculation/dos_electronic')
        workflow.results.dos_dft = dos_dft
        workflow.results.band_structure_dft = bs_dft
        workflow.results.spectra = [xs_archive.workflow2.results for xs_archive in xs_archives]

        # Inputs and Outputs
        input_structure = extract_section(self.archive, 'run/system')
        dft_calculation = extract_section(self.archive, 'run/calculation')
        polarization_calculations = extract_polarization_outputs()
        workflow.m_add_sub_section(
            ParticleHoleExcitations.inputs,
            Link(name='Particle-Hole excitations workflow parameters', section=workflow.method))
        if input_structure:
            workflow.m_add_sub_section(
                ParticleHoleExcitations.inputs, Link(name='Input structure', section=input_structure))
        for index, polarizations in enumerate(polarization_calculations):
            workflow.m_add_sub_section(
                ParticleHoleExcitations.outputs, Link(name=f'Polarization {index + 1}', section=polarizations))

        # DFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            task.name = 'DFT'
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dft_calculation:
                task.outputs = [Link(name='Output DFT calculation', section=dft_calculation)]
            workflow.m_add_sub_section(ParticleHoleExcitations.tasks, task)

        # Spectra task
        for index, xs_archive in enumerate(xs_archives):
            if not xs_archive.workflow2:
                continue
            task = TaskReference(task=xs_archive.workflow2)
            task.name = f'BSE {index + 1}'
            if dft_calculation:
                xs_archive.workflow2.m_add_sub_section(
                    PhotonPolarization.inputs, Link(name='Output DFT calculation', section=dft_calculation))
                for photon_task in xs_archive.workflow2.tasks:
                    photon_task.m_add_sub_section(
                        TaskReference.inputs, Link(name='Output DFT calculation', section=dft_calculation))
            workflow.m_add_sub_section(ParticleHoleExcitations.tasks, task)

        xs_workflow_archive.workflow2 = workflow
