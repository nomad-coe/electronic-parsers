import numpy as np
import logging
import ase
from ase.io.ulm import Reader

from nomad.units import ureg
from nomad.parsing.file_parser import FileParser, TarParser, XMLParser, DataTextParser
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.method import (
    Electronic, Method, DFT, Smearing, XCFunctional, Functional, BasisSet, BasisSetAtomCentered,
    BasisSetCellDependent, Electronic, Scf
)
from nomad.datamodel.metainfo.simulation.system import (
    System, Atoms
)
from nomad.datamodel.metainfo.simulation.calculation import (
    Calculation, Energy, EnergyEntry, Forces, ForcesEntry, BandEnergies, BandStructure,
    Density, Potential, PotentialValue
)
from .metainfo import gpaw  # pylint: disable=unused-import


class GPWParser(TarParser):
    def __init__(self):
        super().__init__()
        self._version_map = {6: '1.1.0', 5: '0.11.0', 3: '0.10.0'}
        self._info_map = {
            'energy_total': 'Epot', 'energy_XC': 'Exc', 'electronic_kinetic_energy': 'Ekin',
            'energy_correction_entropy': 'S', 'atom_forces_free': 'CartesianForce',
            'atom_positions': 'CartesianPositions', 'occupation': 'OccupationNumbers',
            'kpoints': 'IBZKPoints'}

    def init_parameters(self):
        self._info = None

    @property
    def info(self):
        if self._info is None:
            self._info = dict()
            xml_file = self.get('info.xml', None)
            if xml_file is None:
                return
            self.xml_file = xml_file
            xml_parser = XMLParser(xml_file, logger=self.logger)

            def convert(val):
                if isinstance(val, list):
                    return [convert(v) for v in val]
                try:
                    if val in ['True', 'False']:
                        return val == 'True'
                    else:
                        val = float(val)
                        if val % 1.0 == 0.0:
                            val = int(val)
                        return val
                except Exception:
                    return val

            # parameters
            self._info['parameter'] = {
                'lengthunit': 'angstrom', 'energyunit': 'eV', 'timeunit': 'femtosecond'}
            self._info['parameter'].update({p['name'].lower(): convert(
                p['value']) for p in xml_parser.get('parameter/', [])})

            # array shapes, types, dimensions
            self._info['array'] = dict()
            dimension = dict()
            for arr in xml_parser.root.findall('./array'):
                name = arr.attrib.get('name', None)
                dtype = arr.attrib.get('type', None)
                if name is None or dtype is None:
                    continue
                shape = []
                for dim in arr.findall('./dimension'):
                    length = int(dim.attrib.get('length', 0))
                    shape.append(length)
                    dimension[dim.attrib.get('name')] = length
                self._info['array'][name.lower()] = dict(dtype=dtype, shape=shape)
            self._info['array_dimension'] = dimension

            self._info['bytesswap'] = (
                xml_parser.root.attrib['endianness'] == 'little') != np.little_endian
        return self._info

    def get_parameter(self, key, unit=None):
        key = self._info_map.get(key, key)
        return self.info['parameter'].get(key.lower(), None)

    def get_array(self, key, unit=None):
        key = self._info_map.get(key, key)
        file_object = self.get(key)
        if file_object is None:
            return

        key = key.lower()
        shape = self.info['array'].get(key, {}).get('shape', None)
        dtype = self.info['array'].get(key, {}).get('dtype', None)
        dtype = np.dtype({'int': 'int32'}.get(dtype, dtype))
        size = np.prod(shape) * dtype.itemsize

        file_object.seek(0)
        parser = DataTextParser(
            mainfile_contents=file_object.read(size), logger=self.logger, dtype=dtype)
        if parser.data is None:
            return

        array = parser.data
        if self._info['bytesswap']:
            array = array.byteswap()
        if dtype == np.int32:
            array = np.asarray(array, int)
        array.shape = shape
        return array

    def get_array_dimension(self, key):
        if key == 'ngpts':
            val = [self.get_array_dimension('ngpts%s' % n) for n in ['x', 'y', 'z']]
        else:
            val = self.info['array_dimension'].get(key)
        return val

    def get_program_version(self):
        return self._version_map.get(self.get_parameter('version'), '0.9.0')

    def get_smearing_width(self):
        return self.get_parameter('fermiwidth')


class GPW2Parser(FileParser):
    def __init__(self):
        super().__init__(None)

    def init_parameters(self):
        self._info = None

    @property
    def ulm(self):
        if self._file_handler is None:
            try:
                self._file_handler = Reader(self.mainfile)
            except Exception:
                pass
        return self._file_handler

    @property
    def info(self):
        if self._info is None:
            self._info = dict()
            self._info['parameter'] = {
                'mode': 'fd', 'xc': 'LDA', 'occupations': None, 'poissonsolver': None,
                'h': None, 'gpts': None, 'kpts': [(0.0, 0.0, 0.0)], 'nbands': None,
                'charge': 0, 'setups': {}, 'basis': {}, 'spinpol': None, 'fixdensity': False,
                'filter': None, 'mixer': None, 'eigensolver': None, 'background_charge': None,
                'external': None, 'random': False, 'hund': False, 'maxiter': 333,
                'idiotproof': True, 'symmetry': {
                    'point_group': True, 'time_reversal': True, 'symmorphic': True,
                    'tolerance': 1e-7},
                'convergence': {
                    'energy': 0.0005, 'density': 1.0e-4, 'eigenstates': 4.0e-8,
                    'bands': 'occupied', 'forces': np.inf},
                'dtype': None, 'width': None, 'verbose': 0, 'lengthunit': 'angstrom',
                'energyunit': 'eV', 'timeunit': 'femtosecond'}
            if self.ulm is not None:
                self._info['parameter'].update(self.ulm.parameters.asdict())
        return self._info

    def get_parameter(self, key):
        try:
            if key == 'planewavecutoff':
                val = self.get_parameter('mode').get('ecut', None)
            elif key == 'basisset':
                val = self.get_parameter('basis')
            elif key == 'energyerror':
                val = self.get_parameter('convergence').get('energy', None)
            elif key == 'xcfunctional':
                val = self.get_parameter('xc')
            # in gpw format, energies are parameters
            elif key == 'energy_total':
                val = self.ulm.hamiltonian.e_total_extrapolated
            elif key == 'energy_free':
                val = self.ulm.hamiltonian.e_total_free
            elif key == 'energy_XC':
                val = self.ulm.hamiltonian.e_xc
            elif key == 'electronic_kinetic_energy':
                val = self.ulm.hamiltonian.e_kinetic
            elif key == 'energy_correction_entropy':
                val = self.ulm.hamiltonian.e_entropy
            elif key == 'fermilevel':
                val = self.ulm.occupations.fermilevel
            elif key == 'split':
                val = self.ulm.occupations.split
            elif key == 'converged':
                val = self.ulm.scf.converged
            else:
                val = self.info['parameter'].get(key.lower(), None)
        except Exception:
            val = None
        return val

    def get_array(self, key):
        if self.ulm is None:
            return
        try:
            if key == 'unitcell':
                val = self.ulm.atoms.cell
            elif key == 'atomicnumbers':
                val = self.ulm.atoms.numbers
            elif key == 'atom_positions':
                val = self.ulm.atoms.positions
            elif key == 'boundaryconditions':
                val = self.ulm.atoms.pbc
            elif key == 'momenta':
                val = self.ulm.atoms.momenta
            elif key == 'atom_forces_free_raw':
                val = self.ulm.results.forces
            elif key == 'magneticmoments':
                val = self.ulm.results.magmoms
            elif key == 'eigenvalues':
                val = self.ulm.wave_functions.eigenvalues
            elif key == 'occupation':
                val = self.ulm.wave_functions.occupations
            # TODO no koints data in ulm?
            elif key == 'kpoints':
                val = self.ulm.IBZKPoints
            elif key == 'density':
                val = self.ulm.density.density
            elif key == 'potential_effective':
                val = self.ulm.hamiltonian.potential
            elif key == 'band_paths':
                val = self.ulm.wave_functions.band_paths.asdict()
            else:
                val = self.ulm.asdict().get(key, None)
        except Exception:
            val = None
        return val

    def get_array_dimension(self, key):
        if key == 'ngpts':
            val = self.ulm.density.density.shape
        else:
            val = self.ulm.asdict().get(key, None)
        return val

    def get_program_version(self):
        return self.ulm.gpaw_version

    def get_smearing_width(self):
        if self.get_parameter('occupations') is None:
            return 0.0 if tuple(self.get_parameter('kpts')) == (1, 1, 1) else 0.1
        else:
            return self.get_parameter('occupations').get('width')


class GPAWParser:
    def __init__(self):
        self.gpw_parser = GPWParser()
        self.gpw2_parser = GPW2Parser()
        self._xc_map = {
            'LDA': ['LDA_X', 'LDA_C_PW'],
            'PW91': ['GGA_X_PW91', 'GGA_C_PW91'],
            'PBE': ['GGA_X_PBE', 'GGA_C_PBE'],
            'PBEsol': ['GGA_X_PBE_SOL', 'GGA_C_PBE_SOL'],
            'revPBE': ['GGA_X_PBE_R', 'GGA_C_PBE'],
            'RPBE': ['GGA_X_RPBE', 'GGA_C_PBE'],
            'BLYP': ['GGA_X_B88', 'GGA_C_LYP'],
            'HCTH407': ['GGA_XC_HCTH_407'],
            'WC': ['GGA_X_WC', 'GGA_C_PBE'],
            'AM05': ['GGA_X_AM05', 'GGA_C_AM05'],
            'M06-L': ['MGGA_X_M06_L', 'MGGA_C_M06_L'],
            'TPSS': ['MGGA_X_TPSS', 'MGGA_C_TPSS'],
            'revTPSS': ['MGGA_X_REVTPSS', 'MGGA_C_REVTPSS'],
            'mBEEF': ['MGGA_X_MBEEF', 'GGA_C_PBE_SOL']}

    def init_parser(self, filepath, logger):
        self.parser = self.gpw_parser
        self.parser.mainfile = filepath
        if self.parser.mainfile_obj is None:
            self.parser = self.gpw2_parser
            self.parser.mainfile = filepath
        self.parser.logger = logger

    def apply_unit(self, val, unit):
        units_map = {
            'ev': ureg.eV, 'hartree': ureg.hartree, 'angstrom': ureg.angstrom,
            'bohr': ureg.bohr, 'femtosecond': ureg.fs}
        p_unit = self.parser.info['parameter'].get(unit, '').lower()
        unit = units_map.get(p_unit, p_unit) if p_unit else unit
        return val * unit

    def get_basis_set_name(self, basis_set):
        if basis_set == 'plane waves':
            pw_cutoff = self.parser.get_parameter('planewavecutoff')
            pw_cutoff = self.apply_unit(pw_cutoff, 'energyunit')
            return 'PW_%.1f_Ry' % (pw_cutoff.to('rydberg').magnitude)
        elif basis_set == 'real space grid':
            cell = self.parser.get_array('unitcell')
            ngpts = self.parser.get_array_dimension('ngpts')
            if cell is None or ngpts is None:
                return
            h_grid = np.linalg.norm(cell, axis=1) / np.array(ngpts[:3])
            h_grid = self.apply_unit(np.sum(h_grid) / 3.0, 'lengthunit')
            return 'GR_%.1f' % (h_grid.to('fm').magnitude)
        elif basis_set == 'numeric AOs':
            return self.parser.get_parameter('basisset')

    def get_mode(self):
        mode = self.parser.get_parameter('mode')
        if isinstance(mode, dict):
            mode = mode.get('name', None)
        return mode

    def get_nspin(self):
        # TODO another way determine spin?
        magnetic_moments = self.parser.get_array('magneticmoments')
        return 1 if magnetic_moments is None else 2

    def get_fermi_level(self):
        fermi_level = [self.parser.get_parameter('fermilevel')] * self.get_nspin()
        if None in fermi_level:
            return
        split = self.parser.get_parameter('split')
        if split is not None:
            fermi_level = [v + (-i + 0.5) * split for i, v in enumerate(fermi_level)]
        return self.apply_unit(fermi_level, 'energyunit')

    def parse_method(self):
        sec_method = self.archive.run[-1].m_create(Method)
        sec_basis_set = sec_method.m_create(BasisSet)
        mode = self.get_mode()
        if mode == 'pw':
            sec_basis = sec_basis_set.m_create(BasisSetCellDependent)
            pw_cutoff = self.parser.get_parameter('planewavecutoff')
            pw_cutoff = self.apply_unit(pw_cutoff, 'energyunit')
            sec_basis.kind = 'plane waves'
            sec_basis.planewave_cutoff = pw_cutoff
            sec_basis.name = self.get_basis_set_name('plane waves')
        elif mode == 'fd':
            sec_basis = sec_basis_set.m_create(BasisSetCellDependent)
            sec_basis.kind = 'real space grid'
            sec_basis.name = self.get_basis_set_name('real space grid')
        elif mode == 'lcao':
            sec_basis = sec_basis_set.m_create(BasisSetAtomCentered)
            sec_basis.kind = 'numeric AOs'
            sec_basis.name = self.get_basis_set_name('numeric AOs')
        sec_basis_set.type = sec_basis.kind

        sec_electronic = sec_method.m_create(Electronic)
        sec_electronic.relativity_method = 'pseudo_scalar_relativistic'
        sec_electronic.method = 'DFT'
        charge = self.parser.get_parameter('charge')
        if charge is not None:
            sec_electronic.charge = int(charge)

        threshold_energy = self.parser.get_parameter('energyerror')
        sec_scf = sec_method.m_create(Scf)
        sec_scf.threshold_energy_change = self.apply_unit(threshold_energy, 'energyunit')

        smearing_width = self.parser.get_smearing_width()
        if smearing_width is not None:
            sec_electronic.smearing = Smearing(kind='fermi', width=self.apply_unit(
                smearing_width, 'energyunit').to('joule').magnitude)

        sec_dft = sec_method.m_create(DFT)
        sec_xc_functional = sec_dft.m_create(XCFunctional)
        xc_functional = self.parser.get_parameter('xcfunctional')
        for xc in self._xc_map.get(xc_functional, [xc_functional]):
            if '_X_' in xc or xc.endswith('_X'):
                sec_xc_functional.exchange.append(Functional(name=xc))
            elif '_C_' in xc or xc.endswith('_C'):
                sec_xc_functional.correlation.append(Functional(name=xc))
            elif 'HYB' in xc:
                sec_xc_functional.hybrid.append(Functional(name=xc))
            else:
                sec_xc_functional.contributions.append(Functional(name=xc))

        method_keys = [
            'fix_magnetic_moment', 'fix_density', 'density_convergence_criterion',
            'mix_class', 'mix_beta', 'mix_weight', 'mix_old', 'maximum_angular_momentum',
            'symmetry_time_reversal_switch']
        for key in method_keys:
            val = self.parser.get_parameter(key.replace('_', ''))
            if val is None:
                continue
            setattr(sec_method, 'x_gpaw_%s' % key, val)

    def parse_scc(self):
        sec_run = self.archive.run[-1]
        sec_scc = sec_run.m_create(Calculation)

        # energies (in gpw, energies are part of parameters)
        energy_keys = [
            'energy_total', 'energy_free', 'energy_XC', 'energy_kinetic_electronic',
            'energy_correction_entropy']
        sec_energy = sec_scc.m_create(Energy)
        for key in energy_keys:
            val = self.parser.get_parameter(key)
            if val is not None:
                sec_energy.m_add_sub_section(getattr(
                    Energy, key.replace('energy_', '').lower()), EnergyEntry(
                        value=self.apply_unit(val, 'energyunit')))

        # forces
        if self.parser.get_array('atom_forces_free') is not None:
            energyunit = self.apply_unit(1, 'energyunit').units
            lengthunit = self.apply_unit(1, 'lengthunit').units
            value = self.parser.get_array('atom_forces_free') * energyunit / lengthunit
            raw = self.parser.get_array('atom_forces_free_raw') * energyunit / lengthunit
            sec_scc.forces = Forces(free=ForcesEntry(value=value, value_raw=raw))

        # magnetic moments
        magnetic_moments = self.parser.get_array('magneticmoments')
        if magnetic_moments is not None:
            sec_scc.x_gpaw_magnetic_moments = magnetic_moments
            sec_scc.x_gpaw_fixed_spin_Sz = magnetic_moments.sum() / 2.

        # fermi level
        fermi_level = self.get_fermi_level()
        if fermi_level is not None:
            sec_scc.energy.fermi = fermi_level[0]

        # eigenvalues
        eigenvalues = self.parser.get_array('eigenvalues')
        if eigenvalues is not None:
            sec_eigenvalues = sec_scc.m_create(BandEnergies)
            sec_eigenvalues.kpoints = self.parser.get_array('kpoints')
            values = self.apply_unit(eigenvalues, 'energyunit')
            occupations = self.parser.get_array('occupation')
            sec_eigenvalues.energies = values
            if occupations is not None:
                sec_eigenvalues.occupations = occupations

        # band path (TODO only in ulm?)
        band_paths = self.parser.get_array('band_paths')
        if band_paths is not None:
            sec_k_band = sec_scc.m_create(BandStructure, Calculation.band_structure_electronic)
            for band_path in band_paths:
                sec_band_seg = sec_k_band.m_create(BandEnergies)
                if band_path.get('eigenvalues', None) is not None:
                    energies = self.apply_unit(band_path.get('eigenvalues'), 'energyunit')
                    sec_band_seg.energies = energies
                kpoints = band_path.get('kpoints', None)
                if kpoints is not None:
                    sec_band_seg.kpoints = kpoints
                if band_path.get('labels', None) is not None:
                    sec_band_seg.endpoints_labels = band_path.get('labels')

        # volumetric data
        density = self.parser.get_array('density')
        if density is not None:
            cell = self.parser.get_array('unitcell')
            origin = -0.5 * np.array(cell).sum(axis=0)
            pbc = self.parser.get_array('boundaryconditions')
            npoints = np.array(density.shape[1:])
            npoints = [(npt + 1) if not pbc[i] else npt for i, npt in enumerate(npoints)]
            displacements = cell / np.array(npoints)
            lengthunit = self.apply_unit(1, 'lengthunit').units
            energyunit = self.apply_unit(1, 'energyunit').units
            density = self.parser.get_array('density')
            if density is not None:
                sec_density = sec_scc.m_create(Density, Calculation.density_charge)
                sec_density.origin = (origin * lengthunit)
                sec_density.displacements = (displacements * lengthunit)
                sec_density.value = density / lengthunit ** 3

            potential = self.parser.get_array('potential_effective')
            if potential is not None:
                sec_scc.potential.append(Potential(effective=[PotentialValue()]))
                sec_scc.potential[0].effective[0].origin = (origin * lengthunit)
                sec_scc.potential[0].effective[0].displacements = (displacements * lengthunit)
                sec_scc.potential[0].effective[0].value = potential * energyunit / lengthunit ** 3

        converged = self.parser.get_parameter('converged')
        if converged is not None:
            sec_scc.calculation_converged = converged

        sec_scc.system_ref = sec_run.system[-1]
        sec_scc.method_ref = sec_run.method[-1]

    def parse_system(self):
        sec_system = self.archive.run[-1].m_create(System)
        sec_atoms = sec_system.m_create(Atoms)

        cell = self.parser.get_array('unitcell')
        if cell is not None:
            cell = self.apply_unit(cell, 'lengthunit')
            sec_atoms.lattice_vectors = cell

        sec_system.atoms.labels = [
            ase.data.chemical_symbols[z] for z in self.parser.get_array('atomicnumbers')]

        positions = self.parser.get_array('atom_positions')
        sec_atoms.positions = self.apply_unit(positions, 'lengthunit')

        pbc = [True, True, True] if self.get_mode() == 'pw' else np.array(
            self.parser.get_array('boundaryconditions'), bool)
        sec_atoms.periodic = pbc

        momenta = self.parser.get_array('momenta')
        if momenta is not None:
            masses = np.array([ase.data.atomic_masses[self.parser.get_array('atomicnumbers')]])
            velocities = momenta / masses.reshape(-1, 1)
            sec_atoms.velocities = velocities * ase.units.fs / ase.units.Angstrom * ureg.angstrom / ureg.fs

    def parse(self, filepath, archive, logger):
        self.filepath = filepath
        self.archive = archive
        self.logger = logging.getLogger(__name__) if logger is None else logger
        self.init_parser(filepath, logger)

        sec_run = self.archive.m_create(Run)
        sec_run.program = Program(name='GPAW', version=self.parser.get_program_version())

        self.parse_method()

        self.parse_system()

        self.parse_scc()
