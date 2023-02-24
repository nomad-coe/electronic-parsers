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


def extract_section(source, path):
    '''
    Extracts the section from source given by path. Examples:
        sec_system = extract_section(archive, 'run/system')
        spectra = extract_section(archive, 'run/calculation/spectra')
    '''
    path_segments = path.split('/', 1)
    try:
        value = getattr(source, path_segments[0])
        value = value[-1] if isinstance(value, list) else value
    except Exception:
        return

    if len(path_segments) == 1:
        return value
    else:
        return extract_section(value, path_segments[1])


def get_files(pattern, filepath, stripname: str = '', deep: bool = True):
    '''
    Get files in a recursive way (up ** or down ..) from the folder of the mainfile.
    '''
    # TODO do recursion until files are found
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
