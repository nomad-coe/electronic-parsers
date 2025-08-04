#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
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
from importlib.metadata import version

numpy_version = version('numpy')
use_trapz = (
    int(numpy_version.split('.')[0]) < 2
)  # TODO: this can be removed once the numpy < 2 restriction from nomad-lab is gone


def integrate_dos(dos, e_fermi=None):
    """Integrate the DOS value over the spin channels stated in `spin_pol`.
    When the sampling range is wide enough and `e_fermi` is given,
    the integral should yield the number of valence electrons.
    The explicit integral serves to check energy and value units."""
    # Restrain integral to the occupied states
    if e_fermi:
        occ_energy = [
            [e.magnitude for e in dos_spin.energies if e <= e_fermi] for dos_spin in dos
        ]
    else:
        occ_energy = [[e.magnitude for e in dos_spin.energies] for dos_spin in dos]
    # Perofrm the integration
    dos_integrated = 0.0
    for ispin, dos_spin in enumerate(dos):
        try:
            spin_channel = dos_spin.total[0].value[: len(occ_energy[ispin])]
        except IndexError:
            raise IndexError('Check the no. spin-channels')
        occ_value = [v.magnitude for v in spin_channel]
        if use_trapz:
            dos_integrated += np.trapz(y=occ_value, x=occ_energy[ispin])
        else:
            dos_integrated += np.trapezoid(y=occ_value, x=occ_energy[ispin])
    return dos_integrated
