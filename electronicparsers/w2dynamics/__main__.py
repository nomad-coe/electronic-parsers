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
import sys
import json
import logging

from nomad.utils import configure_logging
from nomad.datamodel import EntryArchive
from electronicparsers.w2dynamics import W2DynamicsParser

if __name__ == "__main__":
    configure_logging(console_log_level=logging.DEBUG)
    archive = EntryArchive()
    W2DynamicsParser().parse(sys.argv[1], archive, logging)
    json.dump(archive.m_to_dict(), sys.stdout, indent=2)
