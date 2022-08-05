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


def integrate_dos(dos, spin_pol, e_fermi=None):
    """Integrate the DOS value over the spin channels stated in `spin_pol`.
    When the sampling range is wide enough and `e_fermi` is given,
    the integral should yield the number of valence electrons.
    The explicit integral serves to check energy and value units."""
    # Restrain integral to the occupied states
    if e_fermi:
        occ_energy = [e.magnitude for e in dos.energies if e <= e_fermi]
    else:
        occ_energy = [e.magnitude for e in dos.energies]
    # Perofrm the integration
    dos_integrated = 0.
    spins = [0, 1] if spin_pol else [0]
    for spin in spins:
        try:
            spin_channel = dos.total[spin].value[:len(occ_energy)]
        except IndexError:
            raise IndexError('Check the no. spin-channels')
        occ_value = [v.magnitude for v in spin_channel]
        dos_integrated += np.trapz(x=occ_energy, y=occ_value)
    return dos_integrated
