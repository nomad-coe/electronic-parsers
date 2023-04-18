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
import re
import logging

from nomad.units import ureg
from nomad.parsing.file_parser import TextParser, Quantity, XMLParser, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Method, DFT, Electronic, Smearing, XCFunctional, Functional, Scf, BasisSet, KMesh,
    FrequencyMesh, Screening, GW, Photon, BSE, CoreHole
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Dos, DosValues, BandStructure, BandEnergies, Energy, EnergyEntry, Charges,
    Forces, ForcesEntry, ScfIteration, BandGap, Spectra
)
from nomad.datamodel.metainfo.workflow import Workflow, GeometryOptimization
from nomad.datamodel.metainfo.simulation.workflow import (
    SinglePoint as SinglePoint2, GeometryOptimization as GeometryOptimization2,
    GeometryOptimizationMethod
)
from .metainfo.exciting import (
    x_exciting_section_MT_charge_atom, x_exciting_section_MT_moment_atom,
    x_exciting_section_spin, x_exciting_section_fermi_surface,
    x_exciting_section_atoms_group, x_exciting_exciton_calculation,
    x_exciting_epsilon_calculation, x_exciting_sigma_calculation,
    x_exciting_loss_calculation, x_exciting_freqgrid_parameters,
    x_exciting_selfenergy_parameters, x_exciting_wgrid_parameters,
    x_exciting_mixbasis_parameters, x_exciting_barecoul_parameters,
    x_exciting_scrcoul_parameters
)
from ..utils import (
    get_files, BeyondDFTWorkflowsParser
)


re_float = r'[-+]?\d+\.\d*(?:[Ee][-+]\d+)?'


class GWInfoParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = []

        def str_to_frequency(val_in):
            val = [v.split() for v in val_in.split('\n')]
            val = np.transpose(np.array([v for v in val if len(v) == 3], float))
            return dict(
                number=np.array(val[0], dtype=int), values=val[1],
                weights=val[2])

        # TODO Read also input parameters here if input_GW.xml does not exist

        self._quantities.append(
            Quantity(
                'frequency_data', r'frequency list:\s*\<\s*#\s*freqs\s*weight\s*>\s*([\d\.Ee\s\-]+)',
                str_operation=str_to_frequency, repeats=False)
        )

        self._quantities.append(
            Quantity(
                'fermi_energy', r'\-\s*G0W0.+\-\s*\-+\s*[\s\S]*?Fermi [Ee]nergy\s*[:=](\s*-?[\d\.]+)\s',
                unit=ureg.hartree, repeats=False)
        )

        self._quantities.append(
            Quantity(
                'direct_band_gap', r'\-\s*G0W0\s*\-\s*\-+\s*[\s\S]*?Direct BandGap\s*\((?P<__unit>\w+)\)\s*\:(\s*[\d\.]+)\s',
                repeats=False)
        )

        self._quantities.append(
            Quantity(
                'fundamental_band_gap', r'\-\s*G0W0\s*\-\s*\-+\s*[\s\S]*?Fundamental BandGap\s*\((?P<__unit>\w+)\)\s*\:(\s*[\d\.]+)\s',
                repeats=False)
        )

        self._quantities.append(
            Quantity(
                'optical_band_gap', r'\-\s*G0W0\s*\-\s*\-+\s*[\s\S]*?Optical BandGap\s*\((?P<__unit>\w+)\)\s*\:(\s*[\d\.]+)\s',
                repeats=False)
        )


class ExcitingEvalqpParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = []

        def str_to_eigenvalue(val_in):
            val = val_in.strip().split('\n')
            kpts = np.array(val[0].split(), dtype=float)
            keys = val[1].split()
            eigs = np.transpose(np.array([v.split() for v in val[2:]], dtype=float))
            eigs = {keys[i]: eigs[i] for i in range(len(keys))}
            return [kpts, eigs]

        self._quantities.append(
            Quantity(
                'kpoints_eigenvalues', r'\s*k\-point \#\s*\d+:\s*([\d\s\.\-]+)([ \w\(\)]+\n)([\s\d\.\-Ee]+)',
                str_operation=str_to_eigenvalue, repeats=True))


class BandstructureDatParser(DataTextParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._nspin = kwargs.get('nspin', None)
        self._energy_unit = kwargs.get('energy_unit', None)

    def init_parameters(self):
        # TODO make a parent clas for bandstructure dat and xml
        self._nspin = None
        self._nkpts_segment = None
        self._neigs_segment = None
        self._vertices = None
        self._distances = None
        self._band_energies = None
        self._band_k_points = None

    @property
    def band_energies(self):
        if self._band_energies is None:
            if self.data is None:
                return

            data = np.transpose(self.data)
            n_kpoints = int(max(data[1]))
            bands = data[6:]
            bands = np.reshape(bands, (
                self.number_of_spin_channels, self.number_of_band_segment_eigenvalues, n_kpoints))

            self._band_energies = []
            start = 0
            for nkpts_segment in self.number_of_k_points_per_segment:
                end = start + nkpts_segment
                band_energy = np.array([np.transpose(band)[start:end] for band in bands])
                if self._energy_unit:
                    band_energy = band_energy * self._energy_unit
                self._band_energies.append(band_energy)
                start = end

        return self._band_energies

    @property
    def band_k_points(self):
        if self._band_k_points is None:
            data = np.transpose(self.data)
            self._band_k_points = []
            start = 0
            for nkpts_segment in self.number_of_k_points_per_segment:
                end = start + nkpts_segment
                self._band_k_points.append(
                    np.transpose(data[2:5])[start:end])
                start = end

        return self._band_k_points

    @property
    def distances(self):
        if self._distances is None:
            data = np.transpose(self.data)
            self._distances = data[5][:int(max(data[1]))]

        return self._distances

    @property
    def number_of_spin_channels(self):
        if self._nspin is None:
            self._nspin = np.shape(np.transpose(self.data))[0] - 6
        return self._nspin

    @property
    def number_of_k_points_per_segment(self):
        if self._nkpts_segment is None:
            self._nkpts_segment = []
            count = 1
            for i in range(1, len(self.distances)):
                if self.distances[i] == self.distances[i - 1]:
                    self._nkpts_segment.append(count)
                    count = 1
                else:
                    count += 1
            self._nkpts_segment.append(count)

        return self._nkpts_segment

    @property
    def number_of_band_segment_eigenvalues(self):
        if self._neigs_segment is None:
            data = np.transpose(self.data)
            self._neigs_segment = int(max(data[0]))
        return self._neigs_segment


class BandOutParser(DataTextParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._nspin = kwargs.get('nspin', None)
        self._energy_unit = kwargs.get('energy_unit', None)

    def init_parameters(self):
        self._nspin = None
        self._distances = None
        self._band_energies = None
        self._neigs_segment = None
        self._nkpts_segment = None

    @property
    def band_energies(self):
        if self._band_energies is None:
            data = np.transpose(self.data)
            n_kpoints = np.where(data[0] == data[0][0])[0][1]
            bands = data[1:]
            bands = np.reshape(bands, (
                self.number_of_spin_channels, self.number_of_band_segment_eigenvalues, n_kpoints))

            self._band_energies = []
            start = 0
            for nkpts_segment in self.number_of_k_points_per_segment:
                end = start + nkpts_segment
                band_energy = np.array([np.transpose(band)[start:end] for band in bands])
                if self._energy_unit:
                    band_energy = band_energy * self._energy_unit
                self._band_energies.append(band_energy)
                start = end

        return self._band_energies

    @property
    def distances(self):
        if self._distances is None:
            dist = np.transpose(self.data)[0]
            n_k_points = np.where(dist == dist[0])[0][1]
            self._distances = dist[:n_k_points]

        return self._distances

    @property
    def number_of_spin_channels(self):
        if self._nspin is None:
            self._nspin = np.shape(np.transpose(self.data)[1:])[0]
        return self._nspin

    @property
    def number_of_k_points_per_segment(self):
        if self._nkpts_segment is None:
            self._nkpts_segment = []
            count = 1
            for i in range(1, len(self.distances)):
                if self.distances[i] == self.distances[i - 1]:
                    self._nkpts_segment.append(count)
                    count = 1
                else:
                    count += 1
            self._nkpts_segment.append(count)

        return self._nkpts_segment

    @property
    def number_of_band_segment_eigenvalues(self):
        if self._neigs_segment is None:
            data = np.transpose(self.data)[0]
            self._neigs_segment = len(np.where(data == data[0])[0])
        return self._neigs_segment


class BandstructureXMLParser(XMLParser):
    def __init__(self, **kwargs):
        # TODO make a parent class for dos and bandstructure
        super().__init__(None)
        self._distance_key = 'distance'
        self._coord_key = 'coord'
        self._energy_key = 'eval'
        self._vertex_key = 'vertex'
        self._band_key = 'band'
        self._atom_key = 'atom'
        self._nspin = kwargs.get('nspin', None)
        self._energy_unit = kwargs.get('energy_unit', None)

    def init_parameters(self):
        self._nspin = None
        self._nkpts_segment = None
        self._neigs_segment = None
        self._bands = None
        self._vertices = None
        self._distances = None
        self._species = None

    @property
    def distances(self):
        if self._distances is None:
            if not self.bands:
                return

            self._distances = [
                point.attrib.get(self._distance_key) for point in self.bands[0][0]]
            self._distances = np.array(self._distances, dtype=float)

        return self._distances

    @property
    def bands(self):
        if self._bands is None:
            bands = self.root.findall('./%s' % self._band_key)
            self._bands = []
            if bands:
                self._bands.append(bands)
            # add atom-resolved
            bands_atom = self.root.findall('./*/%s' % self._atom_key)
            for band in bands_atom:
                self._bands.append(band.findall('./%s' % self._band_key))
        return self._bands

    @property
    def vertices(self):
        if self._vertices is None:
            self._vertices = self.root.findall('./%s' % self._vertex_key)
        return self._vertices

    @property
    def number_of_spin_channels(self):
        if self._nspin is None:
            self._nspin = 1
        return self._nspin

    @property
    def number_of_k_points_per_segment(self):
        if self._nkpts_segment is None:
            self._nkpts_segment = []
            count = 1
            for i in range(1, len(self.distances)):
                if self.distances[i] == self.distances[i - 1]:
                    self._nkpts_segment .append(count)
                    count = 1
                else:
                    count += 1
            self._nkpts_segment.append(count)

        return self._nkpts_segment

    @property
    def number_of_band_segment_eigenvalues(self):
        if self._neigs_segment is None:
            self._neigs_segment = len(self.bands[0]) // self.number_of_spin_channels
        return self._neigs_segment

    def parse(self, key):
        if self._results is None:
            self._results = dict()

        if not self.bands:
            return

        if key == 'band_energies':
            # TODO I am not certain about the format for the spin polarized case
            # I cannot find an example bandstructure file
            # atom-resolved bandstructure are added as separate section_k_band
            res = []
            for n in range(len(self.bands)):
                res_n = []
                start = 0
                band_energies = np.zeros((
                    self.number_of_spin_channels, self.number_of_band_segment_eigenvalues,
                    len(self.distances)), dtype=float)

                for i in range(len(self.bands[n])):
                    band_energies[i % self.number_of_spin_channels][i] = np.array(
                        [e.attrib.get(self._energy_key) for e in self.bands[n][i]])

                for nkpts_segment in self.number_of_k_points_per_segment:
                    end = start + nkpts_segment
                    band_energy = np.array([
                        np.transpose(energy)[start:end] for energy in band_energies])
                    if self._energy_unit is not None:
                        band_energy = band_energy * self._energy_unit
                    res_n.append(band_energy)
                    start = end
                res.append(res_n)

        elif key == 'band_k_points':
            res = []
            for i in range(len(self.number_of_k_points_per_segment)):
                start = np.array(
                    self.vertices[i].attrib.get(self._coord_key).split(), dtype=float)
                end = np.array(
                    self.vertices[i + 1].attrib.get(self._coord_key).split(), dtype=float)

                res.append(np.linspace(start, end, self.number_of_k_points_per_segment[i]))

        elif key == 'band_segm_labels':
            res = []
            for i in range(len(self.vertices) - 1):
                start = self.vertices[i].attrib.get('label')
                end = self.vertices[i + 1].attrib.get('label')
                res.append([
                    '\u0393' if start.lower() == 'gamma' else start,
                    '\u0393' if end.lower() == 'gamma' else end])

        elif key == 'band_segm_start_end':
            res = []
            for i in range(len(self.number_of_k_points_per_segment)):
                start = self.vertices[i].attrib.get(self._coord_key).split()
                end = self.vertices[i + 1].attrib.get(self._coord_key).split()
                res.append([start, end])

        else:
            res = None

        self._results[key] = res


class DOSXMLParser(XMLParser):
    def __init__(self, **kwargs):
        super().__init__(None)
        self._nspin_key = 'nspin'
        self._totaldos_key = 'totaldos'
        self._partialdos_key = 'partialdos'
        self._diagram_key = 'diagram'
        self._l_key = 'l'
        self._m_key = 'm'
        self._energy_key = 'e'
        self._dos_key = 'dos'
        self._unit_key = 'unit'
        self._energy_unit = kwargs.get('energy_unit', None)
        self._units_mapping = dict(hartree=ureg.hartree)

    def init_parameters(self):
        self._ndos = None
        self._natoms = None
        self._nspin = None
        self._nlm = None
        self._energies = None
        self._total_dos = None
        self._partial_dos = None

    @property
    def energy_unit(self):
        if self._energy_unit is None:
            axis = self.root.find('./axis')
            if axis is None:
                return

            self._energy_unit = self._units_mapping.get(axis.attrib.get(self._unit_key).lower(), 1)

        return self._energy_unit

    @property
    def number_of_spin_channels(self):
        if self._nspin is None:
            if not self.total_dos:
                return
            self._nspin = len(self.total_dos)

        return self._nspin

    @property
    def number_of_atoms(self):
        if self._natoms is None:
            partial_dos = self.root.findall('./%s' % self._partialdos_key)
            self._natoms = len(partial_dos)

        return self._natoms

    @property
    def number_of_dos(self):
        if self._ndos is None:
            total_dos = self.root.find('./%s/%s' % (self._totaldos_key, self._diagram_key))
            self._ndos = len(total_dos)

        return self._ndos

    @property
    def number_of_lm(self):
        if self._nlm is None:
            if self.partial_dos is None:
                return

            self._nlm = 0
            l_list = set([int(e.attrib.get(self._l_key)) for e in self.partial_dos])
            for li in l_list:
                self._nlm += 2 * li + 1

        return self._nlm

    @property
    def total_dos(self):
        if self._total_dos is None:
            self._total_dos = self.root.findall('./%s/%s' % (self._totaldos_key, self._diagram_key))
        return self._total_dos

    @property
    def partial_dos(self):
        if self._partial_dos is None:
            self._partial_dos = self.root.findall('./%s/%s' % (self._partialdos_key, self._diagram_key))
        return self._partial_dos

    @property
    def energies(self):
        if self._energies is None:
            if self.total_dos is None:
                return

            self._energies = np.array(
                [float(point.attrib.get(self._energy_key)) for point in self.total_dos[0]])

            if self.energy_unit is not None:
                self._energies = self._energies * self.energy_unit

        return self._energies

    def _get_dos(self, diagram):
        dos = np.array(
            [point.attrib.get(self._dos_key) for point in diagram], dtype=float)

        return dos

    def parse(self, key):
        if self._results is None:
            self._results = dict()

        if 'total' in key:
            if not self.total_dos:
                return

            res = np.zeros((self.number_of_spin_channels, self.number_of_dos))

            for i in range(len(self.total_dos)):
                spin = self.total_dos[i].attrib.get(self._nspin_key, i)
                res[i] = self._get_dos(self._total_dos[i])

            if self.energy_unit is not None:
                res = res * (1 / self.energy_unit)

        elif 'partial' in key:
            if not self.partial_dos:
                return

            res = np.zeros((
                self.number_of_lm, self.number_of_spin_channels, self.number_of_atoms, self.number_of_dos))

            for i in range(len(self.partial_dos)):
                spin = self.partial_dos[i].attrib.get(self._nspin_key, None)
                if spin is None:
                    spin = (i % (self.number_of_spin_channels * self.number_of_lm)) // self.number_of_lm
                else:
                    spin = int(spin) - 1

                val_l = self.partial_dos[i].attrib.get(self._l_key, None)
                val_m = self.partial_dos[i].attrib.get(self._m_key, None)
                if val_l is None or val_m is None:
                    lm = i % self.number_of_lm
                else:
                    lm = int(val_l) ** 2 + int(val_m) + int(val_l)

                atom = i // (self.number_of_lm * self.number_of_spin_channels)

                res[lm][spin][atom] = self._get_dos(self.partial_dos[i])

            if self.energy_unit is not None:
                res = res * (1 / self.energy_unit)

        elif key == 'energies':
            return self.energies

        else:
            res = None

        self._results[key] = res


class ExcitingFermiSurfaceBxsfParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = []

        self._quantities.append(
            Quantity(
                'fermi_energy', r'Fermi Energy:\s*([\d\.]+)\s*', unit=ureg.hartree, repeats=False))

        def str_to_band_parameters(val_in):
            val = val_in.strip().split('\n')

            nbands = int(val[0])
            mesh = np.array(val[1].split(), dtype=int)
            origin = np.array(val[2].split(), dtype=float)
            vector = np.array([v.split() for v in val[3:6]], dtype=float)

            return [nbands, mesh, origin, vector]

        self._quantities.append(
            Quantity(
                'band_parameters', r'BANDGRID_3D_BANDS\s*([\d\.\-Ee\s]+)',
                str_operation=str_to_band_parameters, repeats=False))

        self._quantities.append(
            Quantity(
                'fermi_surface', r'BAND:\s*\d+\s*([\d\-\+\.Ee\s]+)\n *E*', unit=ureg.hartree,
                repeats=True))


class ExcitingEigenvalueParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = []
        self._quantities.append(
            Quantity(
                'k_points', r'\s*\d+\s*([\d\.Ee\- ]+):\s*k\-point', repeats=True))

        def str_to_eigenvalues(val_in):
            val = val_in[:val_in.rfind('\n \n')].strip()
            val = np.array([v.split() for v in val.split('\n')], dtype=float)
            val = np.transpose(val)
            occs = val[-1]
            eigs = val[-2]

            nspin = 2 if occs[0] == 1. else 1
            data = dict()
            data['occupancies'] = np.reshape(occs, (nspin, len(occs) // nspin))
            data['eigenvalues'] = np.reshape(eigs, (nspin, len(eigs) // nspin))
            return data

        self._quantities.append(
            Quantity(
                'eigenvalues_occupancies', r'\(state\, eigenvalue and occupancy below\)\s*([\d\.Ee\-\s]+?(?:\n *\n))',
                str_operation=str_to_eigenvalues, repeats=True))


class ExcitingGWOutParser(TextParser):
    def __init__(self, mainfile, logger):
        super().__init__(mainfile, logger=logger)

    def init_quantities(self):
        self._quantities = []


class ExcitingInfoParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        re_symbol = re.compile(r'([A-Z][a-z]?)')

        def str_to_array(val_in):
            val = [v.split(':')[-1].split() for v in val_in.strip().split('\n')]
            val = val[0] if len(val) == 1 else val
            return np.array(val, dtype=float)

        def str_to_atom_properties_dict(val_in):
            unit = None
            if 'charge' in val_in:
                unit = ureg.elementary_charge
            elif 'moment' in val_in:
                unit = ureg.elementary_charge * ureg.bohr

            val = val_in.strip().split('\n')

            properties = dict()
            atom_resolved = []
            species = None
            for v in val:
                v = v.strip().split(':')
                if len(v) < 2:
                    continue

                elif v[0].startswith('species'):
                    species = re.search(re_symbol, v[-1]).group(1)

                elif v[0].startswith('atom'):
                    v[0] = v[0].split()
                    v[1] = [float(vi) for vi in v[1].split()]
                    v[1] = v[1][0] if len(v[1]) == 1 else v[1]
                    if species is None:
                        species = v[0][2]
                    atom_resolved.append(((species, v[1] * unit)))

                else:
                    vi = [float(vii) for vii in v[1].split()]
                    vi = vi[0] if len(vi) == 1 else vi
                    properties[v[0].strip()] = vi * unit

            properties['atom_resolved'] = atom_resolved
            return properties

        def str_to_quantity_tolerances(val_in):
            return val_in.strip().replace('(', '').replace(')', '').split()

        def str_to_energy_dict(val_in):
            val = val_in.strip().split('\n')
            energies = dict()
            for v in val:
                v = v.split(':')
                if len(v) < 2:
                    continue
                energies[v[0].strip()] = float(v[1]) * ureg.hartree
            return energies

        self._quantities = [Quantity(
            'program_version', r'\s*EXCITING\s*([\w\-\(\)\. ]+)\s*started', repeats=False,
            dtype=str, flatten=False)]

        initialization_quantities = [
            Quantity(
                'lattice_vectors',
                r'Lattice vectors\s*[\(cartesian\)]*\s*:\s*([\-0-9\.\s]+)\n',
                str_operation=str_to_array, unit=ureg.bohr, repeats=False, convert=False),
            Quantity(
                'lattice_vectors_reciprocal',
                r'Reciprocal lattice vectors\s*[\(cartesian\)]*\s*:\s*([\-0-9\.\s]+)\n',
                str_operation=str_to_array, unit=1 / ureg.bohr, repeats=False, convert=False)
        ]

        self._system_keys_mapping = {
            'x_exciting_unit_cell_volume': ('Unit cell volume', ureg.bohr ** 3),
            'x_exciting_brillouin_zone_volume': ('Brillouin zone volume', 1 / ureg.bohr ** 3),
            'x_exciting_number_of_atoms': ('Total number of atoms per unit cell', None),
            'x_exciting_spin_treatment': ('Spin treatment', None),
            'x_exciting_number_of_bravais_lattice_symmetries': ('Number of Bravais lattice symmetries', None),
            'x_exciting_number_of_crystal_symmetries': ('Number of crystal symmetries', None),
            'kpoint_grid': (r'k\-point grid', None),
            'kpoint_offset': (r'k\-point offset', None),
            'x_exciting_number_kpoints': (r'Total number of k\-points', None),
            'x_exciting_rgkmax': (r'R\^MT\_min \* \|G\+k\|\_max \(rgkmax\)', None),
            'x_exciting_species_rtmin': (r'Species with R\^MT\_min', None),
            'x_exciting_gkmax': (r'Maximum \|G\+k\| for APW functions', 1 / ureg.bohr),
            'x_exciting_gmaxvr': (r'Maximum \|G\| for potential and density', 1 / ureg.bohr),
            'x_exciting_gvector_size': (r'G\-vector grid sizes', None),
            'x_exciting_gvector_total': (r'Total number of G\-vectors', None),
            'x_exciting_lmaxapw': (r'   APW functions', None),
            'x_exciting_nuclear_charge': ('Total nuclear charge', ureg.elementary_charge),
            'x_exciting_electronic_charge': ('Total electronic charge', ureg.elementary_charge),
            'x_exciting_core_charge_initial': ('Total core charge', ureg.elementary_charge),
            'x_exciting_valence_charge_initial': ('Total valence charge', ureg.elementary_charge),
            'x_exciting_wigner_radius': (r'Effective Wigner radius, r\_s', ureg.bohr),
            'x_exciting_empty_states': ('Number of empty states', None),
            'x_exciting_valence_states': ('Total number of valence states', None),
            'x_exciting_hamiltonian_size': ('Maximum Hamiltonian size', None),
            'x_exciting_pw': (r'Maximum number of plane\-waves', None),
            'x_exciting_lo': (r'Total number of local\-orbitals', None)}

        self._method_keys_mapping = {
            'smearing_kind': ('Smearing scheme', None),
            'smearing_width': ('Smearing width', None)}

        for name, key_unit in self._system_keys_mapping.items():
            initialization_quantities.append(
                Quantity(
                    name, r'%s\s*:\s*([\s\S]*?)\n' % key_unit[0], unit=key_unit[1], repeats=False)
            )

        for name, key_unit in self._method_keys_mapping.items():
            initialization_quantities.append(
                Quantity(
                    name, r'%s\s*:\s*([\s\S]*?)\n' % key_unit[0], unit=key_unit[1], repeats=False)
            )

        initialization_quantities.append(Quantity(
            'species',
            rf'(Species : *\d+ *\(\w+\)[\s\S]+?{re_float} *{re_float} *{re_float}\n\s*\n)',
            repeats=True, sub_parser=TextParser(quantities=[
                Quantity('number', r'Species : *(\d+)', dtype=np.int32),
                Quantity('symbol', r'\((\w+)\)'),
                Quantity('file', r'parameters loaded from *: *(.+)'),
                Quantity('name', r'name *: *(.+)'),
                Quantity('nuclear_charge', rf'nuclear charge *: *({re_float})', dtype=np.float64, unit=ureg.elementary_charge),
                Quantity('electronic_charge', rf'electronic charge *: *({re_float})', dtype=np.float64, unit=ureg.elementary_charge),
                Quantity('atomic_mass', rf'atomic mass *: *({re_float})', dtype=np.float64, unit=ureg.electron_mass),
                Quantity('muffin_tin_radius', rf'muffin-tin radius *: *({re_float})', dtype=np.float64, unit=ureg.bohr),
                Quantity('radial_points', rf'radial points in muffin-tin *: *({re_float})', dtype=np.int32),
                Quantity('positions_format', r'atomic positions \((.+?)\)', flatten=False),
                Quantity(
                    'positions',
                    rf'\d+ : *({re_float}) *({re_float}) *({re_float})',
                    repeats=True, dtype=np.dtype(np.float64))])))

        initialization_quantities.append(Quantity(
            'potential_mixing', r'Using ([\w ]+) potential mixing', repeats=False, flatten=False)
        )

        initialization_quantities.append(Quantity(
            'xc_functional', r'(Exchange-correlation type[\s\S]+?\n *\n)',
            sub_parser=TextParser(quantities=[
                Quantity('type', r'Exchange-correlation type +: +(\S+)'),
                Quantity(
                    'name_reference',
                    r'\n *(.+?,.+)',
                    str_operation=lambda x: [v.strip() for v in x.split(':')]),
                Quantity(
                    'parameters',
                    r'\n *(.+?:.+)', repeats=True,
                    str_operation=lambda x: [v.strip() for v in x.split(':')])]))
        )

        self._quantities.append(Quantity(
            'initialization',
            r'(?:All units are atomic|Starting initialization)([\s\S]+?)(?:Using|Ending initialization)', repeats=False,
            sub_parser=TextParser(quantities=initialization_quantities))
        )

        scf_quantities = [
            Quantity(
                'energy_total', r'[Tt]*otal energy\s*:\s*([\-\d\.Ee]+)', repeats=False,
                dtype=float, unit=ureg.hartree),
            Quantity(
                'energy_contributions', r'(?:Energies|_)([\+\-\s\w\.\:]+?)\n *(?:DOS|Density)',
                str_operation=str_to_energy_dict, repeats=False, convert=False),
            Quantity(
                'x_exciting_dos_fermi',
                r'DOS at Fermi energy \(states\/Ha\/cell\)\s*:\s*([\-\d\.Ee]+)',
                repeats=False, dtype=float, unit=1 / ureg.hartree),
            Quantity(
                'charge_contributions',
                r'(?:Charges|Electron charges\s*\:*\s*)([\-\s\w\.\:\(\)]+?)\n *[A-Z\+]',
                str_operation=str_to_atom_properties_dict, repeats=False, convert=False),
            Quantity(
                'moment_contributions',
                r'(?:Moments\s*\:*\s*)([\-\s\w\.\:\(\)]+?)\n *[A-Z\+]',
                str_operation=str_to_atom_properties_dict, repeats=False, convert=False)]

        self._miscellaneous_keys_mapping = {
            'x_exciting_gap': (r'Estimated fundamental gap', ureg.hartree),
            'time': (r'Wall time \(seconds\)', ureg.s)}

        for name, key_unit in self._miscellaneous_keys_mapping.items():
            scf_quantities.append(Quantity(
                name, r'%s\s*\:*\s*([\-\d\.Ee]+)' % key_unit[0], repeats=False,
                unit=key_unit[1]))

        self._convergence_keys_mapping = {
            'x_exciting_effective_potential_convergence': (
                r'RMS change in effective potential \(target\)', ureg.hartree),
            'x_exciting_energy_convergence': (
                r'Absolute change in total energy\s*\(target\)', ureg.hartree),
            'x_exciting_charge_convergence': (
                r'Charge distance\s*\(target\)', ureg.elementary_charge),
            'x_exciting_IBS_force_convergence': (
                r'Abs\. change in max\-nonIBS\-force\s*\(target\)', ureg.hartree / ureg.bohr)}

        for name, key_unit in self._convergence_keys_mapping.items():
            scf_quantities.append(Quantity(
                name, r'%s\s*\:*\s*([\(\)\d\.\-\+Ee ]+)' % key_unit[0],
                str_operation=str_to_quantity_tolerances, unit=key_unit[1], repeats=False))

        module_quantities = [
            Quantity(
                'scf_iteration', r'(?:I| i)teration number :([\s\S]+?)(?:\n *\n\+{10}|\+\-{10})',
                sub_parser=TextParser(quantities=scf_quantities), repeats=True),
            Quantity(
                'final',
                r'(?:Convergence targets achieved\. Performing final SCF iteration|Reached self-consistent loops maximum)([\s\S]+?)(\n *\n\+{10})',
                sub_parser=TextParser(quantities=scf_quantities), repeats=False),
            Quantity(
                'atomic_positions',
                r'(Atomic positions\s*\([\s\S]+?)\n\n',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'positions_format', r'Atomic positions\s*\(([a-z]+)\)'),
                    Quantity(
                        'symbols', r'atom\s*\d+\s*(\w+)', repeats=True, dtype=str),
                    Quantity(
                        'positions', r'\s*:\s*([\d\.\-]+\s*[\d\.\-]+\s*[\d\.\-]+)',
                        repeats=True, dtype=float)])),
            Quantity(
                'forces', r'Total atomic forces including IBS \(\w+\)\s*\:(\s*atom[\-\s\w\.\:]*?)\n *Atomic',
                repeats=False, str_operation=str_to_array, dtype=float, unit=ureg.hartree / ureg.bohr)
        ]

        self._quantities.append(Quantity(
            'groundstate',
            r'(?:Self\-consistent loop started|Groundstate module started)([\s\S]+?)Groundstate module stopped',
            sub_parser=TextParser(quantities=module_quantities), repeats=False))

        optimization_quantities = [
            Quantity(
                'atomic_positions',
                r'(Atomic positions at this step\s*\([\s\S]+?)\n\n',
                sub_parser=TextParser(quantities=[
                    Quantity(
                        'positions_format', r'Atomic positions at this step\s*\(([a-z]+)\)'),
                    Quantity(
                        'symbols', r'atom\s*\d+\s*(\w+)', repeats=True, dtype=str),
                    Quantity(
                        'positions', r'\s*:\s*([\d\.\-]+\s*[\d\.\-]+\s*[\d\.\-]+)',
                        repeats=True, dtype=float)])),
            Quantity(
                'forces',
                r'Total atomic forces including IBS \(\w+\)\s*\:(\s*atom[\-\s\w\.\:]*?)\n *Time',
                repeats=False, str_operation=str_to_array, convert=False, unit=ureg.hartree / ureg.bohr),
            Quantity(
                'step', r'Optimization step\s*(\d+)', repeats=False, dtype=int),
            Quantity(
                'method', r'method\s*=\s*(\w+)', repeats=False, dtype=str),
            Quantity(
                'n_scf_iterations',
                r'Number of (?:total)* scf iterations\s*\:\s*(\d+)', repeats=False, dtype=int),
            Quantity(
                'force_convergence',
                r'Maximum force magnitude\s*\(target\)\s*\:(\s*[\(\)\d\.\-\+Ee ]+)',
                str_operation=str_to_quantity_tolerances, unit=ureg.hartree / ureg.bohr, repeats=False,
                dtype=float),
            Quantity(
                'energy_total', r'Total energy at this optimization step\s*\:\s*([\-\d\.Ee]+)',
                unit=ureg.hartree, repeats=False, dtype=float),
            Quantity(
                'time', r'Time spent in this optimization step\s*\:\s*([\-\d\.Ee]+)\s*seconds',
                unit=ureg.s, repeats=False, dtype=float)
        ]

        self._quantities.append(Quantity(
            'structure_optimization',
            r'Structure\-optimization module started([\s\S]+?)Structure\-optimization module stopped',
            sub_parser=TextParser(quantities=[
                Quantity(
                    'optimization_step',
                    r'(Optimization step\s*\d+[\s\S]+?(?:\n *\n\-{10}|Time spent in this optimization step\s*:\s*[\d\.]+ seconds))',
                    sub_parser=TextParser(quantities=optimization_quantities),
                    repeats=True),
                Quantity(
                    'final',
                    r'Force convergence target achieved([\s\S]+?Opt)',
                    sub_parser=TextParser(quantities=scf_quantities),
                    repeats=False),
                Quantity(
                    'atomic_positions',
                    r'(imized atomic positions\s*\([\s\S]+?)\n\n',
                    sub_parser=TextParser(quantities=[
                        Quantity(
                            'positions_format', r'imized atomic positions\s*\(([a-z]+)\)'),
                        Quantity(
                            'symbols', r'atom\s*\d+\s*(\w+)', repeats=True, dtype=str),
                        Quantity(
                            'positions', r'\s*:\s*([\d\.\-]+\s*[\d\.\-]+\s*[\d\.\-]+)',
                            repeats=True, dtype=float)])),
                Quantity(
                    'forces',
                    r'Total atomic forces including IBS \(\w+\)\s*\:(\s*atom[\-\s\w\.\:]*?)\n *Atomic',
                    repeats=False, str_operation=str_to_array, dtype=float, unit=ureg.hartree / ureg.bohr),
            ]), repeats=False))

        self._quantities.append(Quantity(
            'hybrids',
            r'Hybrids module started([\s\S]+?)Hybrids module stopped',
            sub_parser=TextParser(quantities=module_quantities)
        ))

    def get_atom_labels(self, section):
        labels = section.get('symbols')

        if labels is None:
            # we get it by concatenating species symbols
            species = self.get('initialization', {}).get('species', [])
            labels = []
            for specie in species:
                labels += [specie.get('symbol')] * len(specie.get('positions'))
        return labels

    def get_positions_format(self, section):
        positions_format = section.get('positions_format')

        if positions_format is None:
            species = self.get_initialization_parameter('species', [])
            for specie in species:
                positions_format = specie.get('positions_format', None)
                if positions_format is not None:
                    break

        return positions_format

    def get_atom_positions(self, section={}, positions=None, positions_format=None):
        positions = positions if positions is not None else section.get('positions')

        if positions is None:
            species = self.get_initialization_parameter('species', [])
            if species:
                positions = np.vstack([s.get('positions') for s in species])

        if positions is None:
            return

        positions = np.array(positions)
        positions_format = positions_format if positions_format is not None else self.get_positions_format(section)

        if positions_format == 'lattice':
            cell = self.get_initialization_parameter('lattice_vectors')
            if cell is None:
                return
            positions = np.dot(positions, cell.magnitude)

        return positions * ureg.bohr

    def get_scf_threshold(self, name):
        reference = self.get('groundstate', self.get('hybrids', {}))
        return reference.get('scf_iteration', [{}])[-1].get(
            name, [None, None])[-1]

    def get_scf_quantity(self, name):
        n_scf = len(self.get('energy_total_scf_iteration', []))
        quantity = self.get('%s_scf_iteration' % name)
        if quantity is None:
            return

        # this is really problematic if some scf steps dont have the quantity
        # the only thing that we can do is to assume that the first steps are the
        # ones with the missing quantity
        if len(quantity) < n_scf:
            quantity = [None] * (n_scf - len(quantity)) + quantity

        return quantity

    def get_xc_functional_name(self):
        # TODO expand list to include other xcf
        xc_functional_map = {
            2: ['LDA_C_PZ', 'LDA_X_PZ'],
            3: ['LDA_C_PW', 'LDA_X_PZ'],
            4: ['LDA_C_XALPHA'],
            5: ['LDA_C_VBH'],
            20: ['GGA_C_PBE', 'GGA_X_PBE'],
            21: ['GGA_C_PBE', 'GGA_X_PBE_R'],
            22: ['GGA_C_PBE_SOL', 'GGA_X_PBE_SOL'],
            26: ['GGA_C_PBE', 'GGA_X_WC'],
            30: ['GGA_C_AM05', 'GGA_C_AM05'],
            300: ['GGA_C_BGCP', 'GGA_X_PBE'],
            406: ['HYB_GGA_XC_PBEH'],
            408: ['HYB_GGA_XC_HSE03']}

        xc_functional = self.get('initialization', {}).get('xc_functional', None)
        if xc_functional is None:
            return []

        name = xc_functional_map.get(xc_functional.type, [])

        return name

    @property
    def n_optimization_steps(self):
        return len(self.get('structure_optimization', {}).get('optimization_step', []))

    def get_number_of_spin_channels(self):
        spin_treatment = self.get('initialization', {}).get(
            'x_exciting_spin_treatment', 'spin-unpolarised')
        n_spin = 1 if spin_treatment.lower() == 'spin-unpolarised' else 2
        return n_spin

    def get_unit_cell_volume(self):
        return self.get('initialization', {}).get('x_exciting_unit_cell_volume', 1.0 * ureg.bohr ** 3)

    def get_initialization_parameter(self, key, default=None):
        return self.get('initialization', {}).get(key, default)


class ExcitingParser(BeyondDFTWorkflowsParser):
    def __init__(self):
        self.info_parser = ExcitingInfoParser()
        self.dos_parser = DOSXMLParser(energy_unit=ureg.hartree)
        self.bandstructure_parser = BandstructureXMLParser(energy_unit=ureg.hartree)
        self.eigval_parser = ExcitingEigenvalueParser()
        self.fermisurf_parser = ExcitingFermiSurfaceBxsfParser()
        self.evalqp_parser = ExcitingEvalqpParser()
        self.dos_out_parser = DataTextParser()
        self.bandstructure_dat_parser = BandstructureDatParser(energy_unit=ureg.hartree)
        self.band_out_parser = BandOutParser(energy_unit=ureg.hartree)
        self.info_gw_parser = GWInfoParser()
        self.input_xml_parser = XMLParser()
        self.data_xs_parser = DataTextParser()
        self.data_clathrate_parser = DataTextParser(dtype=str)
        self._child_archives = {}

        # different names for different versions of exciting
        self._energy_keys_mapping = {
            'energy_total': ['Total energy', 'total energy'],
            'x_exciting_fermi_energy': ['Fermi energy', 'Fermi'],
            'energy_kinetic_electronic': ['Kinetic energy', 'electronic kinetic'],
            'energy_coulomb': ['Coulomb energy', 'Coulomb'],
            'x_exciting_coulomb_energy': ['Coulomb energy', 'Coulomb'],
            'energy_exchange': ['Exchange energy', 'exchange'],
            'x_exciting_exchange_energy': ['Exchange energy', 'exchange'],
            'energy_correlation': ['Correlation energy', 'correlation'],
            'x_exciting_correlation_energy': ['Correlation energy', 'correlation'],
            'energy_sum_eigenvalues': ['Sum of eigenvalues', 'sum of eigenvalues'],
            'x_exciting_effective_potential_energy': ['Effective potential energy'],
            'x_exciting_coulomb_potential_energy': ['Coulomb potential energy', 'Coulomb potential'],
            'energy_xc_potential': ['xc potential energy', 'xc potential'],
            'energy_electrostatic': ['Hartree energy', 'Hartree'],
            'x_exciting_hartree_energy': ['Hartree energy', 'Hartree'],
            'x_exciting_electron_nuclear_energy': ['Electron-nuclear energy', 'electron-nuclear '],
            'x_exciting_nuclear_nuclear_energy': ['Nuclear-nuclear energy', 'nuclear-nuclear'],
            'x_exciting_madelung_energy': ['Madelung energy', 'Madelung'],
            'x_exciting_core_electron_kinetic_energy': ['Core-electron kinetic energy', 'core electron kinetic'],
            'x_exciting_dft_d2_dispersion_correction': ['DFT-D2 dispersion correction']
        }

        self._electron_charge_keys_mapping = {
            'x_exciting_core_charge': ['core'],
            'x_exciting_core_leakage': ['core leakage'],
            'x_exciting_valence_charge': ['valence'],
            'x_exciting_interstitial_charge': ['interstitial'],
            'x_exciting_total_MT_charge': ['total charge in muffin-tins', 'total in muffin-tins'],
            'charge_total': ['total charge'],
            'x_exciting_section_MT_charge_atom': ['atom_resolved']
        }

        self._moment_keys_mapping = {
            'x_exciting_interstitial_moment': ['interstitial'],
            'x_exciting_total_MT_moment': ['total moment in muffin-tins'],
            'x_exciting_total_moment': ['total moment'],
            'x_exciting_section_MT_moment_atom': ['atom_resolved']
        }

        self._xs_spectra_types = ['EPSILON', 'EXCITON', 'SIGMA', 'LOSS']

        self._gw_input_default = {
            'coreflag': 'all',
            'ibgw': 1,
            'mblksiz': 0,
            'nbgw': 0,
            'nempty': 0,
            'ngridq': [0, 0, 0],
            'printSelfC': False,
            'printSpectralFunction': False,
            'qdepw': 'tet',
            'rpmat': False,
            'skipgnd': False,
            'taskname': 'g0w0',
            'vqloff': [0.0, 0.0, 0.0]
        }

        self._freqgrid_input_default = {
            'eta': 1.0e-3,
            'fconv': 'imfreq',
            'fgrid': 'gauleg2',
            'freqmax': 1.0,
            'freqmin': 0.0,
            'nomeg': 16
        }

        self._freq_grid_map = {
            'eqdist': 'Equidistant',
            'gaulag': 'Gauss-Laguerre',
            'gauleg': 'Gauss-Legendre',
            'gauleg2': 'Gauss-Legendre',
            'clencurt2': 'Clenshaw-Curtis'
        }

        self._selfenergy_input_default = {
            'actype': 'pade',
            'eqpsolver': 0,
            'eshift': 0,
            'method': 'ac',
            'nempty': 0,
            'singularity': 'mbp',
            'swidth': 1.0e-4,
            'tol': 1.0e-12
        }

        self._wgrid_input_default = {
            'size': 1000,
            'type': 'eqdist',
            'wmax': 1.0,
            'wmin': -1.0
        }

        self._mixbasis_input_default = {
            'epsmb': 1.0e-4,
            'gmb': 1.0,
            'lmaxmb': 3
        }

        self._barecoul_input_default = {
            'barcevtol': 0.1,
            'basis': 'mb',
            'cutofftype': None,
            'pwm': 2.0,
            'stctol': 1.0e-15
        }

        self._scrcoul_input_default = {'omegap': 1.0, 'scrtype': 'rpa'}

    def file_exists(self, filename):
        """Checks if a the given filename exists and is accessible in the same
        folder where the mainfile is stored.
        """
        mainfile = os.path.basename(self.info_parser.mainfile)
        suffix = mainfile.strip('INFO.OUT')
        target = filename.rsplit('.', 1)
        filepath = '%s%s' % (target[0], suffix)
        if target[1:]:
            filepath = '%s.%s' % (filepath, target[1])
        filepath = os.path.join(self.info_parser.maindir, filepath)

        if os.path.isfile(filepath) and os.access(filepath, os.F_OK):
            return True
        return False

    def _parse_dos(self, sec_scc):
        if self.dos_parser.get('totaldos', None) is None:
            return

        # Get fermi energy: it is used to un-shift the DOS to
        # the original scale in which also other energies are reported.
        energy_fermi = sec_scc.energy.fermi
        if energy_fermi is None:
            return
        energy_fermi = (energy_fermi.magnitude * ureg.joule).to('hartree')

        sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
        sec_dos.n_energies = self.dos_parser.number_of_dos
        sec_dos.energies = self.dos_parser.energies + energy_fermi
        totaldos = self.dos_parser.get('totaldos')
        for spin in range(len(totaldos)):
            sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
            sec_dos_values.spin = spin
            sec_dos_values.value = totaldos[spin]

        partialdos = self.dos_parser.get('partialdos')
        if partialdos is None:
            return

        partialdos = partialdos.to('1/joule').magnitude
        lm_values = np.column_stack((np.arange(len(partialdos)), np.zeros(len(partialdos), dtype=np.int32)))
        for lm in range(len(partialdos)):
            for spin in range(len(partialdos[lm])):
                for atom in range(len(partialdos[lm][spin])):
                    sec_dos_values = sec_dos.m_create(DosValues, Dos.atom_projected)
                    sec_dos_values.m_kind = 'spherical'
                    sec_dos_values.lm = lm_values[lm]
                    sec_dos_values.spin = spin
                    sec_dos_values.atom_index = atom
                    sec_dos_values.value = partialdos[lm][spin][atom]

    def _parse_bandstructure(self, sec_scc):
        # we need to set nspin again as this is overwritten when setting mainfile
        self.bandstructure_parser._nspin = self.info_parser.get_number_of_spin_channels()

        band_energies = self.bandstructure_parser.get('band_energies', [])

        for n in range(len(band_energies)):

            # Get fermi energy: it is used to un-shift the band structure to
            # the original scale in which also other energies are reported.
            energy_fermi = sec_scc.energy.fermi
            if energy_fermi is None:
                continue
            energy_fermi = energy_fermi.to("hartree")

            sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
            sec_k_band.energy_fermi = energy_fermi

            band_k_points = self.bandstructure_parser.get('band_k_points')
            nkpts_segment = self.bandstructure_parser.number_of_k_points_per_segment
            band_seg_labels = self.bandstructure_parser.get('band_segm_labels')
            for nb in range(len(band_energies[n])):
                sec_k_band_segment = sec_k_band.m_create(BandEnergies)
                sec_k_band_segment.n_kpoints = nkpts_segment[nb]
                sec_k_band_segment.kpoints = band_k_points[nb]
                sec_k_band_segment.endpoints_labels = band_seg_labels[nb]
                sec_k_band_segment.energies = band_energies[n][nb] + energy_fermi

    def _parse_eigenvalues(self, sec_scc):
        if self.eigval_parser.get('eigenvalues_occupancies', None) is None:
            return

        nspin = self.info_parser.get_number_of_spin_channels()

        def get_data(key):
            data = self.eigval_parser.get('eigenvalues_occupancies')
            # reshaping is not necessary as this is done in parser, however nspin is
            # determined from occupancies which is problematic sometimes
            res = np.hstack([np.reshape(v[key], (nspin, np.size(v[key]) // nspin)) for v in data])
            res = res.reshape((len(res), len(data), len(res[0]) // len(data)))

            if key == 'eigenvalues':
                res = res * ureg.hartree
            return res

        sec_eigenvalues = sec_scc.m_create(BandEnergies)
        sec_eigenvalues.kpoints = self.eigval_parser.get('k_points')
        sec_eigenvalues.occupations = get_data('occupancies')
        sec_eigenvalues.energies = get_data('eigenvalues')

    def _parse_fermisurface(self, sec_scc):
        fermi_surface = self.fermisurf_parser.get('fermi_surface', [None])[0]
        if fermi_surface is None:
            return

        sec_fermisurface = sec_scc.m_create(x_exciting_section_fermi_surface)

        band_parameters = self.fermisurf_parser.get('band_parameters', None)
        if band_parameters is not None:
            sec_fermisurface.x_exciting_number_of_bands_fermi_surface = band_parameters[0]
            sec_fermisurface.x_exciting_number_of_mesh_points_fermi_surface = np.product(band_parameters[1])
            sec_fermisurface.x_exciting_grid_fermi_surface = band_parameters[1]
            sec_fermisurface.x_exciting_origin_fermi_surface = band_parameters[2]
            sec_fermisurface.x_exciting_vectors_fermi_surface = band_parameters[3]

        fermi_energy = self.fermisurf_parser.get('fermi_energy', None)
        if fermi_energy is not None:
            sec_fermisurface.x_exciting_fermi_energy_fermi_surface = fermi_energy

        sec_fermisurface.x_exciting_values_fermi_surface = fermi_surface

    def _parse_evalqp(self, sec_scc):
        data = self.evalqp_parser.get('kpoints_eigenvalues')
        if data is None:
            return

        def get_data(key):
            if key == 'k_points':
                return np.array([d[0][:3] for d in data])
            elif key == 'Znk':
                return np.array([d[1].get(key, None) for d in data])
            else:
                energy = np.array([d[1].get(key, None) for d in data])
                if None in energy:
                    return energy
                return np.array([d[1].get(key) for d in data]) * ureg.hartree

        eigs_gw = get_data('E_GW')
        if eigs_gw[0] is None:
            return

        nspin = self.info_parser.get_number_of_spin_channels()

        def reshape(data):
            if data[0] is None:
                return
            return np.reshape(data, (nspin, len(data) // nspin, len(data[0])))

        sec_gw_eigenvalues = sec_scc.m_create(BandEnergies)
        sec_gw_eigenvalues.qp_linearization_prefactor = reshape(get_data('Znk'))
        sec_gw_eigenvalues.n_bands = len(eigs_gw[0])
        sec_gw_eigenvalues.n_kpoints = len(eigs_gw)
        sec_gw_eigenvalues.kpoints = get_data('k_points')

        sec_gw_eigenvalues.energies = reshape(eigs_gw)
        sec_gw_eigenvalues.value_exchange = reshape(get_data('Sx'))
        eigs_gw_C = reshape(get_data('Sc'))
        if eigs_gw_C is None:
            eigs_gw_C = reshape(get_data('Re(Sc)'))
        sec_gw_eigenvalues.value_correlation = eigs_gw_C
        sec_gw_eigenvalues.value_xc_potential = reshape(get_data('Vxc'))

    def _parse_dos_out(self, sec_scc):
        data = self.dos_out_parser.data
        if data is None:
            return

        # Get fermi energy: it is used to un-shift the DOS to
        # the original scale in which also other energies are reported.
        energy_fermi = sec_scc.energy.fermi
        if energy_fermi is None:
            return
        energy_fermi = (energy_fermi.magnitude * ureg.joule).to('hartree')

        # TODO I am not sure about format for spin-polarized case! I assume it is
        # energy dos_up dos_down
        nspin = self.info_parser.get_number_of_spin_channels()

        sec_dos = sec_scc.m_create(Dos, Calculation.dos_electronic)
        sec_dos.n_energies = len(data) // nspin

        data = np.reshape(data, (nspin, len(data) // nspin, 2))
        data = np.transpose(data, axes=(2, 0, 1))

        sec_dos.energies = data[0][0] * ureg.hartree + energy_fermi
        dos = data[1] * (1 / ureg.hartree)
        for spin in range(len(dos)):
            sec_dos_values = sec_dos.m_create(DosValues, Dos.total)
            sec_dos_values.spin = spin
            sec_dos_values.value = dos[spin]

        # TODO add PDOS

    def _parse_bandstructure_dat(self, sec_scc):
        self.bandstructure_dat_parser._nspin = self.info_parser.get_number_of_spin_channels()

        band_energies = self.bandstructure_dat_parser.band_energies
        if band_energies is None:
            return

        # Get fermi energy: it is used to un-shift the band structure to
        # the original scale in which also other energies are reported.
        energy_fermi = sec_scc.energy.fermi
        if energy_fermi is None:
            return
        energy_fermi = (energy_fermi.magnitude * ureg.joule).to('hartree')

        sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
        sec_k_band.energy_fermi = energy_fermi

        band_k_points = self.bandstructure_dat_parser.band_k_points
        nkpts_segment = self.bandstructure_dat_parser.number_of_k_points_per_segment
        for nb in range(len(band_energies)):
            sec_k_band_segment = sec_k_band.m_create(BandEnergies)
            sec_k_band_segment.n_kpoints = nkpts_segment[nb]
            sec_k_band_segment.kpoints = band_k_points[nb]
            sec_k_band_segment.energies = band_energies[nb] + energy_fermi

    def _parse_band_out(self, sec_scc):
        self.band_out_parser._nspin = self.info_parser.get_number_of_spin_channels()

        band_energies = self.band_out_parser.band_energies
        if band_energies is None:
            return

        # Get fermi energy: it is used to un-shift the band structure to
        # the original scale in which also other energies are reported.
        energy_fermi = 0.0 * ureg.hartree
        if sec_scc.energy is not None:
            energy_fermi = sec_scc.energy.fermi
        energy_fermi = (energy_fermi.magnitude * ureg.joule).to('hartree')
        sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
        sec_k_band.energy_fermi = energy_fermi

        nkpts_segment = self.band_out_parser.number_of_k_points_per_segment
        for nb in range(len(band_energies)):
            sec_k_band_segment = sec_k_band.m_create(BandEnergies)
            sec_k_band_segment.n_kpoints = nkpts_segment[nb]
            sec_k_band_segment.value = band_energies[nb] + energy_fermi

    def parse_file(self, name, section, filepath=None):
        # TODO add support for info.xml, wannier.out
        if name.startswith('dos') and name.endswith('xml'):
            parser = self.dos_parser
            parser_function = self._parse_dos
        elif name.startswith('bandstructure') and name.endswith('xml'):
            parser = self.bandstructure_parser
            parser_function = self._parse_bandstructure
        elif name.startswith('EIGVAL') and name.endswith('OUT'):
            parser = self.eigval_parser
            parser_function = self._parse_eigenvalues
        elif (name.startswith('FERMISURF') or name.startswith('FS')) and name.endswith('bxsf'):
            parser = self.fermisurf_parser
            parser_function = self._parse_fermisurface
        elif name.startswith('EVALQP') and (name.endswith('DAT') or name.endswith('TXT')):
            parser = self.evalqp_parser
            parser_function = self._parse_evalqp
        elif name.startswith('TDOS') and name.endswith('OUT'):
            parser = self.dos_out_parser
            parser_function = self._parse_dos_out
        elif name.startswith('bandstructure') and name.endswith('dat'):
            parser = self.bandstructure_dat_parser
            parser_function = self._parse_bandstructure_dat
        elif name.startswith('BAND') and name.endswith('OUT'):
            parser = self.band_out_parser
            parser_function = self._parse_band_out
        elif name.startswith('input') and name.endswith('xml'):
            parser = self.input_xml_parser
            if self._calculation_type == 'gw':
                parser_function = self._parse_input_gw
            elif self._calculation_type == 'xs':
                parser_function = self._parse_input_xs
            else:
                # TODO implement reading of parameters from input.xml for normal calculations
                # in addition to INFO.OUT
                return
        else:
            return

        filepath = filepath if filepath is not None else self.filepath
        files = get_files(name, filepath, 'INFO.OUT')
        if len(files) > 1:
            self.logger.warning('Found multiple files. Will read all!', data=dict(file=name))

        for n in range(len(files)):
            parser.mainfile = files[n]
            parser_function(section)

        # free up memory
        parser.mainfile = None

    def _parse_input_xs(self, sec_method):
        xstype = self.input_xml_parser.get('xs/xstype', None)
        if xstype is not None:
            sec_method.x_exciting_xs_xstype = xstype
            sec_method.x_exciting_electronic_structure_method = xstype

        sec_method.x_exciting_xs_broadening = self.input_xml_parser.get(
            'xs/broad', 0.01, 'hartree')
        sec_method.x_exciting_xs_gqmax = self.input_xml_parser.get(
            'xs/gqmax', 0.0, '1/bohr')
        sec_method.x_exciting_xs_lmaxapw = self.input_xml_parser.get('xs/lmaxapw', 10)
        sec_method.x_exciting_xs_number_of_empty_states = self.input_xml_parser.get(
            'xs/nempty', 5)
        sec_method.x_exciting_xs_ngridq = self.input_xml_parser.get('xs/ngridq', [1, 1, 1])
        sec_method.x_exciting_xs_ngridk = self.input_xml_parser.get('xs/ngridk', [1, 1, 1])
        rgkmax = self.input_xml_parser.get('xs/rgkmax', None)
        if rgkmax is None:
            rgkmax = self.info_parser.get_initialization_parameter('x_exciting_rgkmax', 0.)
        sec_method.x_exciting_xs_rgkmax = rgkmax
        sec_method.x_exciting_xs_scissor = self.input_xml_parser.get('xs/scissor', 0.0)
        sec_method.x_exciting_xs_vkloff = self.input_xml_parser.get('xs/vkloff', [0., 0., 0.])

        if self.input_xml_parser.get('xs/energywindow') is not None:
            sec_method.x_exciting_xs_energywindow_values = self.input_xml_parser.get(
                'xs/energywindow/intv', np.array([-0.5, 0.5]), 'hartree')
            sec_method.x_exciting_xs_energywindow_points = self.input_xml_parser.get(
                'xs/energywindow/points', 500)

        if self.input_xml_parser.get('xs/screening') is not None:
            sec_method.x_exciting_xs_screening_number_of_empty_states = self.input_xml_parser.get(
                'xs/screening/nempty', 0)
            sec_method.x_exciting_xs_screening_ngridk = self.input_xml_parser.get(
                'xs/screening/ngridk', [0, 0, 0])
            rgkmax = self.input_xml_parser.get('xs/screening/rgkmax', None)
            if rgkmax is None:
                rgkmax = self.info_parser.get_initialization_parameter('x_exciting_rgkmax', 0.)
            sec_method.x_exciting_xs_screening_rgkmax = rgkmax
            sec_method.x_exciting_xs_screening_type = self.input_xml_parser.get(
                'xs/screening/screentype', 'full')

        if self.input_xml_parser.get('xs/BSE') is not None:
            sec_method.x_exciting_xs_bse_type = self.input_xml_parser.get(
                'xs/BSE/bsetype', 'singlet')
            sec_method.x_exciting_xs_bse_antiresonant = self.input_xml_parser.get(
                'xs/BSE/aresbse', True)
            sec_method.x_exciting_xs_bse_angular_momentum_cutoff = self.input_xml_parser.get(
                'xs/BSE/lmaxdielt', 14)
            rgkmax = self.input_xml_parser.get('xs/BSE/rgkmax', None)
            if rgkmax is None:
                rgkmax = self.info_parser.get_initialization_parameter('x_exciting_rgkmax', 0)

            sec_method.x_exciting_xs_bse_rgkmax = rgkmax
            sec_method.x_exciting_xs_bse_sciavbd = self.input_xml_parser.get(
                'xs/BSE/sciavbd', True)
            sec_method.x_exciting_xs_bse_sciavqbd = self.input_xml_parser.get(
                'xs/BSE/sciavqbd', False)
            sec_method.x_exciting_xs_bse_sciavqhd = self.input_xml_parser.get(
                'xs/BSE/sciavqhd', False)
            sec_method.x_exciting_xs_bse_sciavqwg = self.input_xml_parser.get(
                'xs/BSE/sciavqwg', False)
            sec_method.x_exciting_xs_bse_sciavtype = self.input_xml_parser.get(
                'xs/BSE/sciavtype', 'spherical')
            sec_method.x_exciting_xs_bse_xas = self.input_xml_parser.get(
                'xs/BSE/xas', False)
            sec_method.x_exciting_xs_bse_number_of_bands = self.input_xml_parser.get(
                'xs/BSE/nstlbse', [0, 0, 0, 0])
            if sec_method.x_exciting_xs_bse_xas:
                sec_method.x_exciting_xs_bse_xasatom = self.input_xml_parser.get(
                    'xs/BSE/xasatom', 0)
                sec_method.x_exciting_xs_bse_xasedge = self.input_xml_parser.get(
                    'xs/BSE/xasedge', 'K')
                sec_method.x_exciting_xs_bse_xasspecies = self.input_xml_parser.get(
                    'xs/BSE/xasspecies', 0)
                sec_method.x_exciting_xs_bse_xas_number_of_bands = self.input_xml_parser.get(
                    'xs/BSE/nstlxas', [0, 0])

        if self.input_xml_parser.get('xs/tddft') is not None:
            sec_method.x_exciting_xs_tddft_analytic_continuation = self.input_xml_parser.get(
                'xs/tddft/acont', False)
            sec_method.x_exciting_xs_tddft_anomalous_Hall_conductivity = self.input_xml_parser.get(
                'xs/tddft/ahc', False)
            sec_method.x_exciting_xs_tddft_anti_resonant_dielectric = self.input_xml_parser.get(
                'xs/tddft/aresdf', False)
            sec_method.x_exciting_xs_tddft_anti_resonant_xc_kernel = self.input_xml_parser.get(
                'xs/tddft/aresfxc', True)
            sec_method.x_exciting_xs_tddft_drude = self.input_xml_parser.get(
                'xs/tddft/drude', [0., 0.])
            sec_method.x_exciting_xs_tddft_split_parameter = self.input_xml_parser.get(
                'xs/tddft/fxcbsesplit', 0.00001, 'hartree')
            sec_method.x_exciting_xs_tddft_xc_kernel = self.input_xml_parser.get(
                'xs/tddft/fxctype', 'RPA')
            sec_method.x_exciting_xs_tddft_finite_q_intraband_contribution = self.input_xml_parser.get(
                'xs/tddft/intraband', False)
            sec_method.x_exciting_xs_tddft_diagonal_xc_kernel = self.input_xml_parser.get(
                'xs/tddft/kerndiag', False)
            sec_method.x_exciting_xs_tddft_lmax_alda = self.input_xml_parser.get(
                'xs/tddft/lmaxalda', 3)
            sec_method.x_exciting_xs_tddft_macroscopic_dielectric_function_q_treatment = self.input_xml_parser.get(
                'xs/tddft/mdfqtype', 0)
            sec_method.x_exciting_xs_tddft_analytic_continuation_number_of_intervals = self.input_xml_parser.get(
                'xs/tddft/nwacont', 0)
            sec_method.x_exciting_xs_tetra = self.input_xml_parser.get(
                'xs/tetra/tetradf', False)

        if self.input_xml_parser.get('xs/qpointset') is not None:
            sec_method.x_exciting_xs_qpointset_qpoint = self.input_xml_parser.get(
                'xs/qpointset/qpoint')

    def _parse_xs_bse(self, path):
        sec_run = self._child_archives.get(path).run[-1]

        def parse_exciton(data, sec_scc):
            # TODO remove n_components
            n_components = len(data)
            data = np.transpose(np.vstack(data))

            sec_scc.x_exciting_xs_bse_number_of_components = n_components
            n_excitons = len(data[0]) // n_components
            scc_section = sec_scc.m_create(x_exciting_exciton_calculation)
            scc_section.x_exciting_xs_bse_number_of_excitons = n_excitons
            scc_section.x_exciting_xs_bse_exciton_energies = np.reshape(
                data[1], (n_components, n_excitons)) * ureg.hartree
            scc_section.x_exciting_xs_bse_exciton_binding_energies = np.reshape(
                data[2], (n_components, n_excitons)) * ureg.hartree
            scc_section.x_exciting_xs_bse_exciton_oscillator_strength = np.reshape(
                data[3], (n_components, n_excitons))
            scc_section.x_exciting_xs_bse_exciton_amplitude_re = np.reshape(
                data[4], (n_components, n_excitons))
            scc_section.x_exciting_xs_bse_exciton_amplitude_im = np.reshape(
                data[5], (n_components, n_excitons))

        def parse_epsilon(data, sec_scc):
            n_components = len(data)
            data = np.transpose(np.vstack(data))
            n_epsilon = len(data[0]) // n_components

            sec_scc.x_exciting_xs_bse_number_of_energy_points = n_epsilon
            scc_section = sec_scc.m_create(x_exciting_epsilon_calculation)
            scc_section.x_exciting_xs_bse_epsilon_energies = np.reshape(
                data[0], (n_components, n_epsilon)) * ureg.hartree
            scc_section.x_exciting_xs_bse_epsilon_re = np.reshape(
                data[1], (n_components, n_epsilon))
            scc_section.x_exciting_xs_bse_epsilon_im = np.reshape(
                data[2], (n_components, n_epsilon))

            sec_spectra = sec_scc.m_create(Spectra)
            sec_spectra.n_energies = n_epsilon
            sec_spectra.excitation_energies = data[0] * ureg.hartree
            sec_spectra.intensities = data[2]

        def parse_sigma(data, sec_scc):
            n_components = len(data)
            data = np.transpose(np.vstack(data))
            n_sigma = len(data[0]) // n_components

            scc_section = sec_scc.m_create(x_exciting_sigma_calculation)
            scc_section.x_exciting_xs_bse_sigma_energies = np.reshape(
                data[0], (n_components, n_sigma)) * ureg.hartree
            scc_section.x_exciting_xs_bse_sigma_re = np.reshape(
                data[1], (n_components, n_sigma))
            scc_section.x_exciting_xs_bse_sigma_im = np.reshape(
                data[2], (n_components, n_sigma))

        def parse_loss(data, sec_scc):
            n_components = len(data)
            data = np.transpose(np.vstack(data))
            n_loss = len(data[0]) // n_components

            scc_section = sec_scc.m_create(x_exciting_loss_calculation)
            scc_section.x_exciting_xs_bse_loss_energies = np.reshape(
                data[0], (n_components, n_loss)) * ureg.hartree
            scc_section.x_exciting_xs_bse_loss = np.reshape(
                data[1], (n_components, n_loss))

        file_ending = path.split('EPSILON')[-1]  # Identifying files with the same ending but different type of calculation
        polarization_files = [
            f for f in get_files('*BSE*.OUT', self._xs_info_file, 'INFO.OUT') if f.endswith(file_ending)]
        for file in polarization_files:
            if sec_run.m_xpath('calculation'):
                sec_scc = sec_run.calculation[-1]
            else:
                sec_scc = sec_run.m_create(Calculation)
            self.data_xs_parser.mainfile = file
            if self.data_xs_parser.data is None:
                continue

            quantity = os.path.basename(file).split('_')[0]
            if quantity.startswith('EXCITON'):
                parse_function = parse_exciton
            elif quantity.startswith('EPSILON'):
                parse_function = parse_epsilon
            elif quantity.startswith('SIGMA'):
                parse_function = parse_sigma
            elif quantity.startswith('LOSS'):
                parse_function = parse_loss

            try:
                parse_function([self.data_xs_parser.data], sec_scc)
                # Specific tag for the spectra from EPSILON
                if quantity.startswith('EPSILON'):
                    if self.input_xml_parser.get('xs/BSE/xas'):
                        sec_scc.spectra[0].type = 'XAS'
                    elif self.input_xml_parser.get('xs/BSE/xes'):
                        sec_scc.spectra[0].type = 'XES'
            except Exception:
                self.logger.error('Error setting BSE data.')

            # refs
            sec_scc.system_ref = sec_run.system[-1]
            sec_scc.method_ref = sec_run.method[-1]

    def _parse_xs_tddft(self):
        sec_run = self.archive.run[-1]

        def get_data(path):
            # all files related to quantity at all qpoints
            files = get_files(os.path.basename(path).replace('001', '*'), self._xs_info_file, 'INFO.OUT')
            data = [[], [], []]
            data_q = []
            for f in files:
                self.data_xs_parser.mainfile = f
                if self.data_xs_parser.data is None:
                    continue
                data_q.append(self.data_xs_parser.data)
            if data_q:
                data_q = np.transpose(data_q, axes=(2, 0, 1))
                for j in range(len(data)):
                    data[j].append(data_q[j])

            return data

        def get_xs_calculation(path):
            segments = os.path.basename(path).split('_', 1)
            if segments[0] not in self._xs_spectra_types:
                return

            archive = None
            for key in self._child_archives.keys():
                if key.endswith(segments[-1]):
                    archive = self._child_archives[key]
                    break

            if archive is None:
                return

            sec_run = archive.run[0] if archive.run else archive.m_create(Run)
            return sec_run.calculation[0] if sec_run.calculation else sec_run.m_create(Calculation)

        for path in get_files('*_OC*001.OUT', self.filepath, 'INFO.OUT'):
            sec_scc = get_xs_calculation(path)
            if not sec_scc:
                continue

            data = get_data(path)

            if not data[0]:
                continue

            basename = os.path.basename(path)
            quantity = basename.split('_')[0]

            if quantity == 'EPSILON' and '_FXC' in basename:
                sec_scc = sec_run.m_create(Calculation)
                sec_scc.x_exciting_xs_tddft_number_of_epsilon_values = len(data[0][0][0])
                sec_scc.x_exciting_xs_tddft_epsilon_energies = data[0][0][0] * ureg.hartree
                sec_scc.x_exciting_xs_tddft_dielectric_function_local_field = data[1:]

            elif quantity == 'EPSILON' and '_NLF_FXC' in basename:
                sec_scc.x_exciting_xs_tddft_dielectric_function_no_local_field = data[1:3]

            elif quantity == 'LOSS' and '_FXC' in basename:
                sec_scc.x_exciting_xs_tddft_loss_function_local_field = data[1]

            elif quantity == 'LOSS' and '_NLF_FXC' in basename:
                sec_scc.x_exciting_xs_tddft_loss_function_no_local_field = data[1]

            elif quantity == 'SIGMA' and '_FXC' in basename:
                sec_scc.x_exciting_xs_tddft_sigma_local_field = data[1:3]

            elif quantity == 'SIGMA' and '_NLF_FXC' in basename:
                sec_scc.x_exciting_xs_tddft_sigma_no_local_field = data[1:3]

    def parse_polarization(self, path):
        sec_run = self._child_archives.get(path).run[-1]
        sec_photon = sec_run.m_create(Method).m_create(Photon)
        # TODO check with developers if this is correct
        sec_photon.momentum_transfer = sec_run.method[0].get('x_exciting_xs_qpointset_qpoint')

    def parse_xs(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)
        if sec_run.m_xpath('method[0]'):
            sec_method.starting_method_ref = sec_run.method[0]

        # Code-specific
        self.parse_file('input.xml', sec_method, self._xs_info_file)

        # BSE
        sec_bse = sec_method.m_create(BSE)
        sec_bse.type = sec_run.method[-1].x_exciting_xs_bse_type
        sec_bse.n_empty_states = sec_run.method[-1].x_exciting_xs_number_of_empty_states
        sec_bse.broadening = sec_run.method[-1].x_exciting_xs_broadening
        # KMesh
        sec_k_mesh = sec_method.m_create(KMesh)
        sec_k_mesh.grid = sec_run.method[-1].x_exciting_xs_ngridk  # TODO change to output parsing
        # QMesh
        sec_q_mesh = KMesh(grid=sec_run.method[-1].x_exciting_xs_ngridq)
        sec_bse.m_add_sub_section(BSE.q_mesh, sec_q_mesh)
        # FrequencyMesh
        n_freqs = sec_run.method[-1].x_exciting_xs_energywindow_points
        freqs = sec_run.method[-1].x_exciting_xs_energywindow_values
        values = [freqs[0] + i * (freqs[-1] - freqs[0]) / n_freqs for i in range(n_freqs)]
        sec_freq_mesh = FrequencyMesh(dimensionality=1, n_points=n_freqs, points=values)
        sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
        # Screening
        sec_screening = Screening(
            type=sec_run.method[-1].x_exciting_xs_screening_type,
            n_empty_states=sec_run.method[-1].x_exciting_xs_screening_number_of_empty_states)
        sec_k_mesh_screening = KMesh(grid=sec_run.method[-1].x_exciting_xs_screening_ngridk)
        sec_screening.m_add_sub_section(Screening.k_mesh, sec_k_mesh_screening)

        # CoreHole
        if sec_run.method[-1].x_exciting_xs_bse_xas:
            sec_core_hole = CoreHole(
                mode='absorption',
                broadening=sec_run.method[-1].x_exciting_xs_broadening)
            sec_bse.m_add_sub_section(BSE.core_hole, sec_core_hole)
            # TODO wait for new changes in metainfo for CoreHole
            # sec_core.edge = sec_run.method[0].get('x_exciting_xs_bse_xasedge')

    def parse_spectra(self, path):
        input_file = get_files('input.xml', self._xs_info_file, 'INFO.OUT')
        if not input_file:
            return
        self.input_xml_parser.mainfile = input_file[0]
        xstype = self.input_xml_parser.get('xs/xstype', '')
        if xstype.lower() == 'bse':
            self._parse_xs_bse(path)
        elif xstype.lower() == 'tddft':
            self._parse_xs_tddft()

    def parse_photons(self, path):
        sec_run = self._child_archives.get(path).m_create(Run)

        # Program
        sec_run.program = Program(
            name='exciting', version=self.info_parser.get('program_version', '').strip())

        # System
        sec_run.system = self.archive.run[-1].system

        # Photon method
        self.parse_polarization(path)
        # BSE method
        sec_run.method.append(self.archive.run[-1].method[-1])

        # Calculation
        self.parse_spectra(path)

        # Workflow
        workflow = SinglePoint2()
        workflow.name = 'SinglePoint'
        self._child_archives.get(path).workflow2 = workflow

    def _parse_input_gw(self, sec_gw):
        def parse_exciting_gw_inputs(source, path, target):
            for keys in source.keys():
                setattr(
                    target,
                    f'x_exciting_{keys}',
                    self.input_xml_parser.get(f'{path}/{keys}', source[keys]))

        parse_exciting_gw_inputs(self._gw_input_default, 'gw', sec_gw)
        sec_freqgrid = sec_gw.m_create(x_exciting_freqgrid_parameters)
        parse_exciting_gw_inputs(self._freqgrid_input_default, 'gw/freqgrid', sec_freqgrid)
        sec_selfenergy = sec_gw.m_create(x_exciting_selfenergy_parameters)
        parse_exciting_gw_inputs(self._selfenergy_input_default, 'gw/selfenergy', sec_selfenergy)
        sec_wgrid = sec_gw.m_create(x_exciting_wgrid_parameters)
        parse_exciting_gw_inputs(self._wgrid_input_default, 'gw/wgrid', sec_wgrid)
        sec_mixbasis = sec_gw.m_create(x_exciting_mixbasis_parameters)
        parse_exciting_gw_inputs(self._barecoul_input_default, 'gw/mixbasis', sec_mixbasis)
        sec_barecoul = sec_gw.m_create(x_exciting_barecoul_parameters)
        parse_exciting_gw_inputs(self._barecoul_input_default, 'gw/barecoul', sec_barecoul)
        sec_scrcoul = sec_gw.m_create(x_exciting_scrcoul_parameters)
        parse_exciting_gw_inputs(self._scrcoul_input_default, 'gw/scrcoul', sec_scrcoul)

        gmaxvr = self.info_parser.get_initialization_parameter('x_exciting_gmaxvr', 0)
        gmb = self.input_xml_parser.get('gw/mixbasis/gmb', 1.0)
        sec_gw.x_exciting_mixed_basis_gmax = gmb * gmaxvr
        pwm = self.input_xml_parser.get('gw/barecoul/pwm', 2.0)
        sec_gw.x_exciting_bare_coulomb_gmax = pwm * gmb * gmaxvr

    def parse_gw(self):
        sec_run = self.archive.run[-1]

        # GW Method
        sec_method = sec_run.m_create(Method)
        sec_gw = sec_method.m_create(GW)

        # parse input xml files: code-specific metainfo
        for f in ['input_gw.xml', 'input-gw.xml', 'input.xml']:
            self.parse_file(f, sec_gw)

        # GW
        sec_gw.type = 'G0W0'
        # KMesh
        sec_k_mesh = sec_method.m_create(KMesh)
        sec_k_mesh.grid = sec_gw.x_exciting_ngridq
        # QMesh same as KMesh
        sec_gw.m_add_sub_section(GW.q_mesh, sec_k_mesh)
        # Analytical continuation
        if sec_gw.x_exciting_selfenergy.x_exciting_actype == 'pade':
            sec_gw.analytical_continuation = sec_gw.x_exciting_selfenergy.x_exciting_actype
        else:
            if sec_gw.x_exciting_selfenergy.x_exciting_method == 'cd':
                sec_gw.analytical_continuation = 'contour_deformation'
            else:
                if sec_gw.x_exciting_scrcoul.x_exciting_scrtype == 'ppm':
                    sec_gw.analytical_continuation = 'ppm_GodbyNeeds'
                else:
                    self.logger.warning('Could not find the analytical continuation method.')
        # FrequencyMesh
        n_freqs = sec_gw.x_exciting_freqgrid.x_exciting_nomeg
        freqmax = sec_gw.x_exciting_freqgrid.x_exciting_freqmax
        freqmin = sec_gw.x_exciting_freqgrid.x_exciting_freqmin
        freq_points = [freqmin + i * (freqmax - freqmin) / n_freqs for i in range(n_freqs)] * ureg.hartree
        smearing = sec_gw.x_exciting_freqgrid.x_exciting_eta if sec_gw.x_exciting_qdepw == 'sum' else None
        sec_freq_mesh = FrequencyMesh(
            dimensionality=1,
            sampling_method=self._freq_grid_map.get(sec_gw.x_exciting_freqgrid.x_exciting_fgrid),
            n_points=n_freqs,
            points=freq_points,
            smearing=smearing)
        sec_method.m_add_sub_section(Method.frequency_mesh, sec_freq_mesh)
        # Screening
        sec_screening = Screening(
            type=sec_gw.x_exciting_scrcoul.x_exciting_scrtype,
            n_empty_states=sec_gw.x_exciting_nempty,
            k_mesh=sec_k_mesh,
            q_mesh=sec_k_mesh,
            frequency_mesh=sec_freq_mesh)
        sec_gw.m_add_sub_section(GW.screening, sec_screening)
        # Other parameters
        sec_gw.interval_qp_corrections = [sec_gw.x_exciting_ibgw, sec_gw.x_exciting_nbgw]
        if sec_screening.n_empty_states == 0:
            sec_gw.n_empty_states = sec_gw.x_exciting_selfenergy.x_exciting_nempty
        else:
            sec_gw.n_empty_states = sec_screening.n_empty_states

        # GW Calculation
        sec_scc = sec_run.m_create(Calculation)
        # parse properties
        self.info_gw_parser.mainfile = self._gw_info_file

        fermi_energy = self.info_gw_parser.get('fermi_energy', None)
        if fermi_energy is not None:
            sec_scc.energy = Energy(fermi=fermi_energy)

        gw_files = ['EVALQP.DAT', 'EVALQP.TXT', 'TDOS-QP.OUT']

        # Parse GW band structure from one of the files:
        bs_files = ['bandstructure-qp.dat', 'BAND-QP.OUT']
        for fname in bs_files:
            if self.file_exists(fname):
                gw_files.append(fname)
                break

        for f in gw_files:
            self.parse_file(f, sec_scc)

        fundamental_band_gap = self.info_gw_parser.get('direct_band_gap', None)
        if fundamental_band_gap is None:
            fundamental_band_gap = self.info_gw_parser.get('fundamental_band_gap', None)
        sec_gap = sec_scc.eigenvalues[-1].m_create(BandGap)
        if fundamental_band_gap is not None:
            sec_gap.value_fundamental = fundamental_band_gap

        optical_band_gap = self.info_gw_parser.get('optical_band_gap', None)
        if optical_band_gap is not None:
            sec_gap.value_optical = optical_band_gap

        sec_scc.method_ref = sec_method
        self.parse_system(self.info_parser.get('groundstate'))
        sec_scc.system_ref = sec_run.system[-1]

    def parse_workflow(self):
        sec_workflow = self.archive.m_create(Workflow)

        sec_workflow.type = 'single_point'
        workflow = SinglePoint2()
        workflow.name = 'SinglePoint'
        sec_workflow.calculations_ref = self.archive.run[-1].calculation
        structure_optimization = self.info_parser.get('structure_optimization')
        if structure_optimization is not None:
            sec_workflow.type = 'geometry_optimization'
            sec_geometry_opt = sec_workflow.m_create(GeometryOptimization)
            workflow = GeometryOptimization2(method=GeometryOptimizationMethod())
            workflow.name = 'GeometryOptimization'
            threshold_force = structure_optimization.get(
                'optimization_step', [{}])[0].get('force_convergence', [0., 0.])[-1]
            sec_geometry_opt.convergence_tolerance_force_maximum = threshold_force
            workflow.method.convergence_tolerance_force_maximum = threshold_force
        self.archive.workflow2 = workflow

    def parse_method(self):
        sec_run = self.archive.run[-1]
        sec_method = sec_run.m_create(Method)

        if sec_method.k_mesh is None:  # TODO revise need in the future
            k_mesh = sec_method.m_create(KMesh)
            k_mesh.grid = self.info_parser.get_initialization_parameter('kpoint_grid', default=[1] * 3)
            k_mesh.offset = self.info_parser.get_initialization_parameter('kpoint_offset', default=[0.] * 3)

        sec_method.basis_set.append(BasisSet(type='(L)APW+lo'))
        sec_dft = sec_method.m_create(DFT)
        sec_electronic = sec_method.m_create(Electronic)
        sec_electronic.method = 'DFT'

        smearing_kind_map = {
            'Gaussian': 'gaussian', 'Methfessel-Paxton': 'methfessel-paxton',
            'Fermi-Dirac': 'fermi', 'Extended': 'tetrahedra'}

        sec_smearing = sec_electronic.m_create(Smearing)
        smearing_kind = self.info_parser.get_initialization_parameter('smearing_kind')
        if smearing_kind is not None:
            if not isinstance(smearing_kind, str):
                smearing_kind = smearing_kind[0]
            smearing_kind = smearing_kind_map[smearing_kind]
            sec_smearing.kind = smearing_kind
        smearing_width = self.info_parser.get_initialization_parameter('smearing_width')
        if smearing_width is not None:
            smearing_width = (smearing_width * ureg.hartree).to('joule')
            # TODO smearing with should have units of energy
            sec_smearing.width = smearing_width.magnitude

        for name in self.info_parser._convergence_keys_mapping.keys():
            threshold = self.info_parser.get_scf_threshold(name)
            if threshold is None:
                continue

            metainfo_name = 'x_exciting_scf_threshold_%s_change' % name.split('_')[-2]
            setattr(sec_method, metainfo_name, threshold)
            # additionally, set threshold to global metainfo. This is killing me!
            if metainfo_name == 'x_exciting_scf_threshold_energy_change':
                sec_method.scf = Scf(threshold_energy_change=threshold)

        sec_xc_functional = sec_dft.m_create(XCFunctional)
        self.parse_xc_functional(sec_xc_functional)

        sec_electronic.n_spin_channels = self.info_parser.get_number_of_spin_channels()

        if self._calculation_type == 'volume_optimization':
            sec_method.x_exciting_volume_optimization = True

    def parse_xc_functional(self, section):
        xc_functional_names = self.info_parser.get_xc_functional_name()
        if not xc_functional_names:
            # get it from input.xml
            input_file = get_files('input.xml', self.filepath, 'INFO.OUT')
            for f in input_file:
                self.input_xml_parser.mainfile = f
                correlation = self.input_xml_parser.get('libxc/correlation', None)
                xc_functional_names.append(correlation)
                exchange = self.input_xml_parser.get('libxc/exchange', None)
                xc_functional_names.append(exchange)

        for name in xc_functional_names:
            if name is None:
                continue
            if '_X_' in name:
                section.exchange.append(Functional(name=name))
            elif '_C_' in name:
                section.correlation.append(Functional(name=name))
            elif 'HYB' in name:
                section.hybrid.append(Functional(name=name))
            else:
                section.contributions.append(Functional(name=name))

        if not xc_functional_names:
            # simply write parameters
            xc_functional = self.info_parser.get('initialization', {}).get('xc_functional')
            if xc_functional is not None:
                section.name = xc_functional.get('name_reference', [None, None])[0]
                section.reference = xc_functional.get('name_reference', [None, None])[1]

    def parse_scc(self, section):
        sec_run = self.archive.run[-1]

        final = section if section.get('energy_total') is not None else section.get('final')
        if final is None:
            # get it from last scf_iteration or optimization_step
            final = section.get('scf_iteration', [None])[-1]
            final = section.get('optimization_step', [None])[-1] if final is None else final
        if final is None:
            return

        sec_scc = sec_run.m_create(Calculation)
        k_grid = self.info_parser.get('k_grid')
        if k_grid is not None:
            sec_kmesh = sec_scc.m_create(KMesh)
            sec_kmesh.grid = k_grid
            sec_kmesh.offset = self.info_parser.get('k_offset', [0.] * 3)

        def parse_scf(iteration, msection):

            energy_total = iteration.get('energy_total')
            sec_energy = msection.m_create(Energy)
            if energy_total is not None:
                sec_energy.total = EnergyEntry(value=energy_total)

            x_exciting_dos_fermi = iteration.get('x_exciting_dos_fermi')
            if x_exciting_dos_fermi is not None:
                setattr(msection, 'x_exciting_dos_fermi', x_exciting_dos_fermi)

            # energy contributions
            energy_contributions = iteration.get('energy_contributions', {})
            for key, names in self._energy_keys_mapping.items():
                val = None
                for name in names:
                    val = energy_contributions.get(name, None)
                    if val is not None:
                        break
                if val is None:
                    continue
                if key.startswith('energy_'):
                    sec_energy.m_add_sub_section(getattr(
                        Energy, key.replace('energy_', '')), EnergyEntry(value=val))
                else:
                    setattr(msection, key, val)

                if key == 'x_exciting_fermi_energy':
                    sec_energy.fermi = val

            # charge contributions
            charge_contributions = iteration.get('charge_contributions', {})
            for key, names in self._electron_charge_keys_mapping.items():
                val = None
                for name in names:
                    val = charge_contributions.get(name, None)
                    if val is not None:
                        break
                if val is None:
                    continue
                if key == 'x_exciting_section_MT_charge_atom':
                    for n in range(len(val)):
                        sec_mt_charge_atom = msection.m_create(x_exciting_section_MT_charge_atom)
                        sec_mt_charge_atom.x_exciting_MT_charge_atom_index = n + 1
                        sec_mt_charge_atom.x_exciting_MT_charge_atom_symbol = val[n][0]
                        sec_mt_charge_atom.x_exciting_MT_charge_atom_value = val[n][1]
                        sec_charges = msection.m_create(Charges)
                        sec_charges.value = [
                            val[n][1].magnitude for n in range(len(val))] * val[0][1].units
                        sec_charges.total = charge_contributions.get('total charge')
                elif key == 'charge_total':
                    pass
                else:
                    setattr(msection, key, val)

            # moment contributions
            moment_contributions = iteration.get('moment_contributions', {})
            for key, names in self._moment_keys_mapping.items():
                val = None
                for name in names:
                    val = moment_contributions.get(name, None)
                    if val is not None:
                        break
                if val is None:
                    continue
                if key == 'x_exciting_section_MT_moment_atom':
                    for n in range(len(val)):
                        sec_mt_moment_atom = msection.m_create(x_exciting_section_MT_moment_atom)
                        sec_mt_moment_atom.x_exciting_MT_moment_atom_index = n + 1
                        sec_mt_moment_atom.x_exciting_MT_moment_atom_symbol = val[n][0]
                        sec_mt_moment_atom.x_exciting_MT_moment_atom_value = val[n][1]
                else:
                    setattr(msection, key, val)

            # convergence values
            for name in self.info_parser._convergence_keys_mapping.keys():
                val = iteration.get(name)
                if val is None:
                    continue

                setattr(msection, name, val)

            # other metainfo
            for name in self.info_parser._miscellaneous_keys_mapping.keys():
                val = iteration.get(name)
                if val is None:
                    continue

                if name == 'time':
                    msection.time_calculation = val
                else:
                    setattr(msection, name, val)

        # energy, moment, charge contributions
        parse_scf(final, sec_scc)

        # forces
        forces = section.get('forces')
        if forces is not None:
            sec_forces = sec_scc.m_create(Forces)
            sec_forces.total = ForcesEntry(value=np.reshape(forces, (np.size(forces) // 3, 3)))

        # scf iterations
        scf_iterations = section.get('scf_iteration', [])
        for scf_iteration in scf_iterations:
            sec_scf_iteration = sec_scc.m_create(ScfIteration)
            parse_scf(scf_iteration, sec_scf_iteration)

        return sec_scc

    def parse_system(self, section):
        sec_run = self.archive.run[-1]

        positions = self.info_parser.get_atom_positions(section.get('atomic_positions', {}))
        lattice_vectors = self.info_parser.get_initialization_parameter('lattice_vectors')
        atom_labels = self.info_parser.get_atom_labels(section.get('atomic_positions', {}))
        input_file = get_files('input.xml', self.filepath, 'INFO.OUT')

        if positions is None:
            # get it from input.xml
            for f in input_file:
                self.input_xml_parser.mainfile = f
                positions = self.input_xml_parser.get('structure/species/atom/coord')
                lattice_vectors = self.input_xml_parser.get(
                    'structure/crystal/basevect', np.eye(3))
                species = self.input_xml_parser.get('structure/species/speciesfile')

                if positions is None or lattice_vectors is None or species is None:
                    continue
                lattice_vectors = np.array(lattice_vectors, dtype=float)
                lattice_vectors *= self.input_xml_parser.get('structure/crystal/scale', 1.0)
                positions = np.dot(positions, lattice_vectors) * ureg.bohr
                lattice_vectors = lattice_vectors * ureg.bohr

                atoms = self.input_xml_parser.get('structure/species/atom')
                atom_labels = []
                for n in range(len(atoms)):
                    atom_labels.extend([species[n].split('.')[0]] * len(atoms[n]))

        if positions is None or atom_labels is None:
            return

        sec_system = sec_run.m_create(System)

        sec_atoms = sec_system.m_create(Atoms)
        sec_atoms.positions = positions
        sec_atoms.labels = atom_labels
        sec_atoms.periodic = [True] * 3
        # TODO confirm no cell optimization in exciting
        sec_atoms.lattice_vectors = lattice_vectors

        lattice_vectors_reciprocal = self.info_parser.get_initialization_parameter(
            'lattice_vectors_reciprocal')
        sec_atoms.lattice_vectors_reciprocal = lattice_vectors_reciprocal

        if len(sec_run.system) > 1:
            return sec_system

        for name in self.info_parser._system_keys_mapping.keys():
            val = self.info_parser.get_initialization_parameter(name)
            if val is None:
                continue

            if name == 'x_exciting_spin_treatment':
                sub_sec = sec_system.m_create(x_exciting_section_spin)
                sub_sec.x_exciting_spin_treatment = val
            elif name == 'x_exciting_species_rtmin':
                setattr(sec_system, name, ' '.join([str(v) for v in val]))
            else:
                try:
                    setattr(sec_system, name, val)
                except Exception:
                    self.logger.warning('Error setting metainfo.')

        # species
        species = self.info_parser.get_initialization_parameter('species', [])
        for specie in species:
            sec_atoms_group = sec_system.m_create(x_exciting_section_atoms_group)
            sec_atoms_group.x_exciting_geometry_atom_labels = specie.get('symbol')
            sec_atoms_group.x_exciting_geometry_atom_number = str(specie.get('number'))
            sec_atoms_group.x_exciting_muffin_tin_points = specie.get('radial_points')
            sec_atoms_group.x_exciting_muffin_tin_radius = specie.get('muffin_tin_radius')
            positions_format = specie.get('positions_format')
            sec_atoms_group.x_exciting_atom_position_format = positions_format
            positions = specie.get('positions')
            positions = self.info_parser.get_atom_positions(
                positions=positions, positions_format=positions_format).to('m')
            sec_atoms_group.x_exciting_geometry_atom_positions = positions.magnitude

        # clathrate info
        clathrate_file = get_files('str.out', self.filepath, 'INFO.OUT')
        if clathrate_file:
            sec_system.x_exciting_clathrates = True
            self.data_clathrate_parser.mainfile = clathrate_file[0]
            if self.data_clathrate_parser.data:
                data = np.transpose(self.data_clathrate_parser.data)
                sec_system.x_exciting_clathrates_atom_coordinates = np.transpose(
                    np.array(data[:3], dtype=float))
                sec_system.x_exciting_clathrates_atom_labels = list(data[3])
        else:
            sec_system.x_exciting_clathrates = False

        potential_mixing = self.info_parser.get_initialization_parameter('potential_mixing')
        if potential_mixing is not None:
            sec_system.x_exciting_potential_mixing = potential_mixing

        return sec_system

    def parse_configurations(self):
        sec_run = self.archive.run[-1]

        def parse_configuration(section):
            if not section:
                return

            sec_scc = self.parse_scc(section)
            if sec_scc is None:
                return

            sec_system = self.parse_system(section)
            if sec_system is not None:
                sec_scc.system_ref = sec_system

            sec_scc.method_ref = sec_run.method[-1]

            return sec_scc

        # groundstate and hybrids calculation
        for module in ['groundstate', 'hybrids']:
            sec_scc = parse_configuration(self.info_parser.get(module))
            if sec_scc is None:
                continue
            # add data to scc
            # TODO add support for more output files and properties
            exciting_files = ['EIGVAL.OUT', 'FERMISURF.bxsf', 'FS.bxsf']

            # Parse DFT DOS from one of the files
            bs_files = ['dos.xml', 'TDOS.OUT']
            for fname in bs_files:
                if self.file_exists(fname):
                    exciting_files.append(fname)
                    break

            # Parse DFT band structure from one of the files
            bs_files = ['bandstructure.xml', 'BAND.OUT', 'bandstructure.dat']
            for fname in bs_files:
                if self.file_exists(fname):
                    exciting_files.append(fname)
                    break

            for f in exciting_files:
                self.parse_file(f, sec_scc)

        # structure optimization
        structure_optimization = self.info_parser.get('structure_optimization', {})
        for optimization_step in structure_optimization.get('optimization_step', []):
            sec_scc = parse_configuration(optimization_step)

            if optimization_step.get('method') is not None:
                sec_scc.x_exciting_geometry_optimization_method = optimization_step.get('method')

            if optimization_step.get('step') is not None:
                sec_scc.x_exciting_geometry_optimization_step = optimization_step.get('step')

            force_convergence = optimization_step.get('force_convergence')
            if force_convergence is not None:
                sec_scc.x_exciting_maximum_force_magnitude = force_convergence[0]
                sec_scc.x_exciting_geometry_optimization_threshold_force = force_convergence[1]

        sec_scc = parse_configuration(structure_optimization)
        if sec_scc is None:
            return

        # volume optimizations
        volume_index = 1
        while True:
            info_volume = get_files(f"run_dir{str(volume_index).rjust(2, '0')}/INFO.OUT", self.filepath, 'INFO.OUT')
            if not info_volume:
                break
            sec_scc.calculations_path.append(info_volume[0])

    def init_parser(self):
        self.info_parser.mainfile = self.filepath
        self.info_parser.logger = self.logger
        self.dos_parser.logger = self.logger
        self.bandstructure_parser.logger = self.logger
        self.eigval_parser.logger = self.logger
        self.fermisurf_parser.logger = self.logger
        self.evalqp_parser.logger = self.logger
        self.dos_out_parser.logger = self.logger
        self.bandstructure_dat_parser.logger = self.logger
        self.band_out_parser.logger = self.logger
        self.info_gw_parser.logger = self.logger
        self.input_xml_parser.logger = self.logger
        self.data_xs_parser.logger = self.logger
        self.data_clathrate_parser.logger = self.logger
        self._archives_ref = []

    def get_mainfile_keys(self, filepath):
        basename = os.path.basename(filepath)
        dirname = os.path.dirname(filepath)
        if os.path.isfile(os.path.join(dirname, f'GW_{basename}')):
            return ['GW', 'GW_workflow']
        xs_files = get_files(basename.replace('INFO.OUT', 'INFOXS.OUT'), filepath, 'INFO.OUT')
        if xs_files:
            re_xs_mainfile = re.compile(r'.+\d\d\d\.OUT')
            spectra_files = []
            for prefix in self._xs_spectra_types:
                spectra_files = get_files(f'{prefix}_*.OUT', filepath, 'INFO.OUT')
                if spectra_files:
                    # remove files for qpoints other than first
                    files = ['XS_workflow'] + xs_files
                    for f in spectra_files:
                        if re_xs_mainfile.match(f):
                            if '001' in f:
                                files.append(f)
                        else:
                            files.append(f)
                    return files
        return True

    def parse(self, filepath, archive, logger, **kwargs):
        self.filepath = filepath
        self.archive = archive
        self.logger = logger if logger is not None else logging

        self._calculation_type = None
        basename = os.path.basename(filepath)
        dirname = os.path.dirname(filepath)
        if basename.startswith('GW'):
            self._calculation_type = 'gw'
            # read method params from INFO.OUT
            self._gw_info_file = filepath
            self.filepath = os.path.join(dirname, basename.lstrip('GW_'))
        elif basename.startswith('INFOXS'):
            self._calculation_type = 'xs'
            self._xs_info_file = filepath
            info_file = get_files('INFO.OUT', self.filepath, 'INFO.OUT', deep=False)
            if info_file:
                self.filepath = os.path.join(info_file[0])
            # self.filepath = os.path.join(dirname, basename.replace('INFOXS', 'INFO'))

        if not os.path.isfile(self.filepath):
            return

        self.init_parser()

        sec_run = self.archive.m_create(Run)

        sec_run.program = Program(
            name='exciting', version=self.info_parser.get('program_version', '').strip())

        # method goes first since reference needed for sec_scc
        if self._calculation_type == 'gw':
            self.parse_gw()
            self.parse_workflow()
        elif self._calculation_type == 'xs':
            self.parse_system(self.info_parser.get('groundstate'))
            self.parse_xs()

            for child in self._child_archives:
                self.parse_photons(child)
            # putting together all photons in the same xs_archive
            self.parse_photon_workflow()
        else:
            self.parse_method()
            self.parse_configurations()
            self.parse_workflow()

        # GW archives
        gw_archive = self._child_archives.get('GW')
        if gw_archive is not None:
            # parse gw single point
            p = ExcitingParser()
            p.parse(os.path.join(dirname, f'GW_{basename}'), gw_archive, logger)

            # parse gw workflow
            gw_workflow_archive = self._child_archives.get('GW_workflow')
            try:
                self.parse_gw_workflow(gw_archive, gw_workflow_archive)
            except Exception:
                self.logger.error('Error parsing the automatic GW workflow')

        # XS archives
        xs_archives = []
        for xs_info_file, xs_archive in self._child_archives.items():
            if 'INFOXS.OUT' in xs_info_file:
                # parse xs single point
                xs_dirname = os.path.dirname(xs_info_file)
                p = ExcitingParser()
                p._child_archives = {
                    key: archive for key, archive in self._child_archives.items() if key.startswith(
                        xs_dirname) and os.path.basename(key).split('_')[0] in self._xs_spectra_types}

                p.parse(xs_info_file, xs_archive, logger)
                xs_archives.append(xs_archive)

        # parse xs workflow (DFT + all photons)
        # TODO generalize to include GW step
        xs_workflow_archive = self._child_archives.get('XS_workflow')
        if xs_workflow_archive:
            try:
                self.parse_xs_workflow(xs_archives, xs_workflow_archive)
            except Exception:
                self.logger.error('Error parsing the automatic XS workflow')
