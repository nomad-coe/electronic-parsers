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
from nomad.datamodel.metainfo.workflow import Workflow, Task, GW as GWold
from nomad.datamodel.metainfo.workflow2 import Link, TaskReference
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint, GW, GWMethod, GWResults, ParticleHoleExcitations,
    ParticleHoleExcitationsMethod, ParticleHoleExcitationsResults
)


def extract_section(source, path):
    '''
    Extracts the section from source given by path. Examples:
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


def get_files(pattern, filepath, stripname: str = '', deep: bool = True):
    '''
    Get files up to / down from the filepath (up ** or down ..).
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

    def parse_gw_workflow(self, gw_archive, gw_workflow_archive):
        sec_run = gw_workflow_archive.m_create(Run)
        sec_run.program = self.archive.run[-1].program
        sec_run.system = self.archive.run[-1].system

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
            Task(
                input_workflow=workflow_old, output_workflow=self.archive.workflow[-1],
                description='DFT calculation performed in an input structure.'),
            Task(
                input_workflow=self.archive.workflow[0], output_workflow=gw_archive.workflow[-1],
                description='GW calculation performed from input DFT calculation.'),
            Task(
                input_workflow=gw_archive.workflow[0], output_workflow=workflow_old,
                description='Comparison between DFT and GW.')
        ]
        gw_old = workflow_old.m_create(GWold)
        gw_old.dos_dft = dos_dft
        gw_old.dos_gw = dos_gw
        gw_old.band_structure_dft = bs_dft
        gw_old.band_structure_gw = bs_gw

        # New workflow
        workflow = GW(method=GWMethod(), results=GWResults())
        workflow.name = 'GW'
        # results
        workflow.results.dos_dft = dos_dft
        workflow.results.dos_gw = dos_gw
        workflow.results.band_structure_dft = bs_dft
        workflow.results.band_structure_gw = bs_gw
        # inputs and outputs
        input_structure = extract_section(self.archive, 'run/system')
        dft_calculation = extract_section(self.archive, 'run/calculation')
        gw_calculation = extract_section(gw_archive, 'run/calculation')
        workflow.inputs.append(Link(name='Workflow parameters', section=workflow.method))
        if input_structure:
            workflow.inputs.append(Link(name='Input structure', section=input_structure))
        if gw_calculation:
            workflow.outputs.append(Link(name='Output GW calculation', section=gw_calculation))
        # DFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            if input_structure:
                task.inputs = [Link(name='Input structure', section=input_structure)]
            if dft_calculation:
                task.outputs = [Link(name='Output DFT calculation', section=dft_calculation)]
            workflow.tasks.append(task)
        # GW task
        if gw_archive.workflow2:
            task = TaskReference(task=gw_archive.workflow2)
            if dft_calculation:
                task.inputs = [Link(name='Input DFT calculation', section=dft_calculation)]
            if gw_calculation:
                task.outputs = [Link(name='Output GW calculation', section=gw_calculation)]
            workflow.tasks.append(task)

        gw_workflow_archive.workflow2 = workflow

    def parse_xs_workflow(self, xs_archives, xs_workflow_archive):
        sec_run = xs_workflow_archive.m_create(Run)
        sec_run.program = self.archive.run[-1].program
        sec_run.system = self.archive.run[-1].system

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
        # results
        bs_dft = extract_section(self.archive, 'run/calculation/band_structure_electronic')
        dos_dft = extract_section(self.archive, 'run/calculation/dos_electronic')
        workflow.results.dos_dft = dos_dft
        workflow.results.band_structure_dft = bs_dft
        workflow.results.spectra = [xs_archive.workflow2.results for xs_archive in xs_archives]
        # inputs and outputs
        input_structure = extract_section(self.archive, 'run/system')
        workflow.inputs.append(Link(name='Workflow parameters', section=workflow.method))
        if input_structure:
            workflow.inputs.append(Link(name='Input structure', section=input_structure))
        workflow.outputs = extract_polarization_outputs()
        dft_calculation = extract_section(self.archive, 'run/calculation')
        output_dft_name = 'Output DFT calculation'
        if dft_calculation:  # include DFT calculation to each single point task
            for archive in self._child_archives.values():
                if isinstance(archive.workflow2, SinglePoint):
                    archive.workflow2.inputs.append(Link(name=output_dft_name, section=dft_calculation))
                    archive.workflow2.tasks[0].inputs.append(Link(name=output_dft_name, section=dft_calculation))
        # DFT task
        if self.archive.workflow2:
            task = TaskReference(task=self.archive.workflow2)
            self.archive.workflow2.outputs = []
            if input_structure:
                self.archive.workflow2.inputs = [Link(name='Input structure', section=input_structure)]
            if dft_calculation:
                self.archive.workflow2.outputs.append(Link(name=output_dft_name, section=dft_calculation))
            workflow.tasks.append(task)
        # PhotonPolarization task
        for xs_archive in xs_archives:
            if xs_archive.workflow2:
                task = TaskReference(task=xs_archive.workflow2)
                if dft_calculation:
                    xs_archive.workflow2.inputs.append(Link(name=output_dft_name, section=dft_calculation))
                workflow.tasks.append(task)

        xs_workflow_archive.workflow2 = workflow
