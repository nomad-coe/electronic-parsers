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
from nomad.datamodel.metainfo.workflow import Workflow, Task as Taskold, GW as GWold
from nomad.datamodel.metainfo.workflow2 import Link, TaskReference
from nomad.datamodel.metainfo.simulation.workflow import (
    GW, GWMethod, GWResults, ParticleHoleExcitations,
    ParticleHoleExcitationsMethod, ParticleHoleExcitationsResults,
    PhotonPolarization, PhotonPolarizationMethod, PhotonPolarizationResults
)


def extract_section(source: EntryArchive, path: str):
    '''
    Extracts the (last) section from source given by path. Examples:
        sec_system = extract_section(archive, 'run/system')
        spectra = extract_section(archive, 'run/calculation/spectra')
    '''
    section_segments = path.split('/')
    for section in section_segments:
        try:
            value = getattr(source, section)
            source = value[-1] if isinstance(value, list) else value
        except Exception:
            return
    return source


def get_files(pattern: str, filepath: str, stripname: str = '', deep: bool = True):
    '''
    Get files up to / down from the filepath (deep=`**` going up, and deep=`..` down,) to
    find the file `pattern` with respect to the file `stripname` (normally being the
    mainfile of the parser).
    '''
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
    Generates automatic GW, BSE, etc, workflows for all electronic codes that can handle
    these calculations.
    '''
    def __init__(self, archive: EntryArchive, _child_archives: dict, _xs_spectra_types: list):
        self.archive = archive
        self._child_archives = _child_archives
        self._xs_spectra_types = _xs_spectra_types

    def run_workflow_archive(self, workflow_archive: EntryArchive):
        '''
        Initializes the workflow archive by checking if Run exists or not, as well as copying
        Program and System into it.
        '''
        if workflow_archive.run:
            sec_run = workflow_archive.run[-1]
        else:
            sec_run = workflow_archive.m_create(Run)
        sec_run.program = self.archive.run[-1].program
        sec_run.system = self.archive.run[-1].system

    def parse_gw_workflow(self, gw_archive: EntryArchive, gw_workflow_archive: EntryArchive):
        '''
            self.archive = DFT archive
            gw_archive = GW archive
            gw_workflow_archive = DFT+GW workflow archive
        '''
        self.run_workflow_archive(gw_workflow_archive)

        # Extracting DFT and GW results
        dos_dft = extract_section(self.archive, 'run/calculation/dos_electronic')
        dos_gw = extract_section(gw_archive, 'run/calculation/dos_electronic')
        bs_dft = extract_section(self.archive, 'run/calculation/band_structure_electronic')
        bs_gw = extract_section(gw_archive, 'run/calculation/band_structure_electronic')

        # Old workflow
        workflow_old = gw_workflow_archive.m_create(Workflow)
        workflow_old.type = 'GW'
        workflow_old.workflows_ref = [self.archive.workflow[-1], gw_archive.workflow[-1]]
        workflow_old.task = [
            Taskold(
                input_workflow=workflow_old, output_workflow=self.archive.workflow[-1],
                description='DFT calculation performed in an input structure.'),
            Taskold(
                input_workflow=self.archive.workflow[0], output_workflow=gw_archive.workflow[-1],
                description='GW calculation performed from input DFT calculation.'),
            Taskold(
                input_workflow=gw_archive.workflow[0], output_workflow=workflow_old,
                description='Comparison between DFT and GW.')
        ]
        gw_old = workflow_old.m_create(GWold)
        gw_old.dos_dft = dos_dft
        gw_old.dos_gw = dos_gw
        gw_old.band_structure_dft = bs_dft
        gw_old.band_structure_gw = bs_gw

        # -- New workflow --
        workflow = GW(method=GWMethod(), results=GWResults())
        workflow.name = 'GW'

        # Method
        method_gw = extract_section(gw_archive, 'run/method/gw')
        method_xcfunctional = extract_section(self.archive, 'run/method/dft/xc_functional')
        method_basisset = extract_section(self.archive, 'run/method/basis_set')
        workflow.method.gw_method_ref = method_gw
        workflow.method.starting_point = method_xcfunctional
        workflow.method.basis_set = method_basisset

        # Results
        workflow.results.dos_dft = dos_dft
        workflow.results.dos_gw = dos_gw
        workflow.results.band_structure_dft = bs_dft
        workflow.results.band_structure_gw = bs_gw

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
        '''
            self.archive = archive for the workflow
            self._child_archives = archives for SinglePoint photons
        '''
        workflow = PhotonPolarization(method=PhotonPolarizationMethod(), results=PhotonPolarizationResults())
        workflow.name = 'Spectra'

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
        '''
            self.archive = DFT archive
            xs_archives = archives for all Spectra workflows
            xs_workflow_archive = DFT+Spectra workflow archive
        '''
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
            task.name = f'Spectra {index + 1}'
            if dft_calculation:
                xs_archive.workflow2.m_add_sub_section(
                    PhotonPolarization.inputs, Link(name='Output DFT calculation', section=dft_calculation))
                for photon_task in xs_archive.workflow2.tasks:
                    photon_task.m_add_sub_section(
                        TaskReference.inputs, Link(name='Output DFT calculation', section=dft_calculation))
            workflow.m_add_sub_section(ParticleHoleExcitations.tasks, task)

        xs_workflow_archive.workflow2 = workflow
