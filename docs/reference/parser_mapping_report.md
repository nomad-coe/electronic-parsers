# Electronic parser mapping report

This report is the concatenation of the per-parser `MAPPING_REPORT.md` fragments. Do not edit by hand — edit the fragment and rebuild.

## Abacus / INPUT

**Summary:** 11 mapped, 21 unmapped quantities (34.38% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `stru_filename` | Unmapped | — |
| `kpt_filename` | Unmapped | — |
| `basis_type` | Unmapped | — |
| `x_abacus_init_velocities` | Unmapped | — |
| `xc` | Mapped | `method.dft.xc_functional` |
| `kpar` | Unmapped | — |
| `bndpar` | Unmapped | — |
| `diago_proc` | Unmapped | — |
| `scf_max_iteration` | Mapped | `method.scf.n_max_iteration` |
| `nelec` | Mapped | `system.number_of_electrons_out` |
| `md_type` | Mapped | `workflow2.method.thermodynamic_ensemble` |
| `md_nstep` | Unmapped | — |
| `occupations` | Mapped | `method.electronic.smearing.kind` |
| `smearing_method` | Mapped | `method.electronic.smearing.kind` |
| `smearing_width` | Mapped | `method.electronic.smearing.width` |
| `dft_plus_u` | Mapped | `method.electronic.method` |
| `x_abacus_mixing_method` | Unmapped | — |
| `x_abacus_mixing_beta` | Unmapped | — |
| `x_abacus_diagonalization_algorithm` | Unmapped | — |
| `x_abacus_dispersion_correction_method` | Mapped | `method.electronic.van_der_waals_method` |
| `x_abacus_gamma_algorithms` | Unmapped | — |
| `x_abacus_scf_threshold_density` | Unmapped | — |
| `x_abacus_initial_magnetization_total` | Unmapped | — |
| `x_abacus_hse_omega` | Mapped | `method.dft.xc_functional.hybrid.parameters` |
| `x_abacus_hybrid_xc_coeff` | Mapped | `method.dft.xc_functional.hybrid.weight`<br>`method.dft.xc_functional.hybrid.parameters` |
| `x_abacus_exx_ccp_rmesh_times` | Unmapped | — |
| `x_abacus_exx_dm_threshold` | Unmapped | — |
| `x_abacus_exx_cauchy_threshold` | Unmapped | — |
| `x_abacus_exx_schwarz_threshold` | Unmapped | — |
| `x_abacus_exx_c_threshold` | Unmapped | — |
| `x_abacus_exx_v_threshold` | Unmapped | — |
| `x_abacus_exx_pca_threshold` | Unmapped | — |

## Abacus / running_*.log

**Summary:** 71 mapped, 248 unmapped quantities (22.26% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `program.version` |
| `nproc` | Unmapped | — |
| `start_date_time` | Mapped | `time_run.date_start` |
| `input_filename` | Unmapped | — |
| `pseudopotential_dirname` | Unmapped | — |
| `basis_set_dirname` | Unmapped | — |
| `drank` | Unmapped | — |
| `dsize` | Unmapped | — |
| `dcolor` | Unmapped | — |
| `grank` | Unmapped | — |
| `gsize` | Unmapped | — |
| `header` | Unmapped | — |
| `header.number_of_species` | Unmapped | — |
| `header.alat` | Mapped | `system.atoms.lattice_vectors`<br>`system.atoms.positions` |
| `header.atom_labels` | Unmapped | — |
| `header.number_of_atoms_for_labels` | Unmapped | — |
| `header.atom_data` | Unmapped | — |
| `header.atom_data.label` | Mapped | `method.atom_parameters.label` |
| `header.atom_data.orbital` | Unmapped | — |
| `header.atom_data.natoms` | Unmapped | — |
| `header.atom_data.start_magnetization` | Unmapped | — |
| `header.atom_data.noncollinear_magnetization` | Unmapped | — |
| `header.number_of_atoms` | Mapped | `system.atoms.n_atoms` |
| `header.positions` | Unmapped | — |
| `header.positions.sites` | Mapped | `system.atoms.positions`<br>`system.atoms.labels`<br>`system.atoms.velocities` |
| `header.positions.sites` | Mapped | `system.atoms.positions`<br>`system.atoms.labels` |
| `header.positions.units` | Mapped | `system.atoms.positions` |
| `header.positions.coord_class` | Mapped | `system.atoms.positions` |
| `header.orbital_files` | Unmapped | — |
| `header.cell_volume` | Unmapped | — |
| `header.units` | Unmapped | — |
| `header.lattice_vectors` | Mapped | `system.atoms.lattice_vectors` |
| `header.reciprocal_units` | Unmapped | — |
| `header.reciprocal_vectors` | Mapped | `calculation.eigenvalues.kpoints`<br>`calculation.band_structure_electronic.segment.kpoints` |
| `header.pseudopotential` | Unmapped | — |
| `header.pseudopotential.filename` | Mapped | `method.atom_parameters.pseudopotential_name` |
| `header.pseudopotential.type` | Unmapped | — |
| `header.pseudopotential.xc` | Mapped | `method.dft.xc_functional` |
| `header.pseudopotential.valence` | Mapped | `method.atom_parameters.n_valence_electrons` |
| `header.pseudopotential.lmax` | Unmapped | — |
| `header.pseudopotential.nzeta` | Unmapped | — |
| `header.pseudopotential.nprojectors` | Unmapped | — |
| `header.fermi_energy_in` | Mapped | `calculation.band_structure_electronic.energy_fermi` |
| `header.x_abacus_pao_radial_cutoff` | Unmapped | — |
| `header.number_of_electrons_out` | Unmapped | — |
| `header.occupied_bands` | Unmapped | — |
| `header.nlocal` | Unmapped | — |
| `header.nbands` | Mapped | `calculation.eigenvalues.energies` |
| `header.symmetry` | Unmapped | — |
| `header.symmetry.lattice_vectors` | Unmapped | — |
| `header.symmetry.right_hand_lattice` | Unmapped | — |
| `header.symmetry.norm_a` | Unmapped | — |
| `header.symmetry.norm_b` | Unmapped | — |
| `header.symmetry.norm_c` | Unmapped | — |
| `header.symmetry.alpha` | Unmapped | — |
| `header.symmetry.beta` | Unmapped | — |
| `header.symmetry.gamma` | Unmapped | — |
| `header.symmetry.bravais_name` | Mapped | `system.symmetry.crystal_system`<br>`system.symmetry.bravais_lattice` |
| `header.symmetry.ibrav` | Mapped | `system.symmetry.bravais_lattice` |
| `header.symmetry.number_of_rotation_matrices` | Unmapped | — |
| `header.symmetry.number_of_point_group_operations` | Unmapped | — |
| `header.symmetry.number_of_space_group_operations` | Unmapped | — |
| `header.symmetry.point_group` | Unmapped | — |
| `header.number_of_spin_channels` | Mapped | `method.electronic.n_spin_channels` |
| `header.ksampling_method` | Mapped | `method.k_mesh.generation_method` |
| `header.nkstot` | Mapped | `method.k_mesh.n_points` |
| `header.nkstot_ibz` | Mapped | `method.k_mesh.n_points` |
| `header.k_points` | Mapped | `method.k_mesh.points`<br>`method.k_mesh.weights` |
| `header.density_cutoff` | Mapped | `method.electrons_representation.basis_set.cutoff` |
| `header.density_fft_grid` | Unmapped | — |
| `header.fft_grid_division` | Unmapped | — |
| `header.nbxx` | Unmapped | — |
| `header.nrxx` | Unmapped | — |
| `header.number_of_pw_for_density` | Unmapped | — |
| `header.number_of_sticks_for_density` | Unmapped | — |
| `header.parallel_pw_for_density` | Unmapped | — |
| `header.number_of_g` | Unmapped | — |
| `header.max_g` | Unmapped | — |
| `header.min_g` | Unmapped | — |
| `header.wavefunction_cutoff` | Mapped | `method.electrons_representation.basis_set.cutoff` |
| `header.wavefunction_fft_grid` | Unmapped | — |
| `header.number_of_pw_for_wavefunction` | Unmapped | — |
| `header.number_of_sticks_for_wavefunction` | Unmapped | — |
| `header.parallel_pw_for_wavefunction` | Unmapped | — |
| `header.number_of_total_pw` | Unmapped | — |
| `header.total_number_of_nlocal_projectors` | Unmapped | — |
| `header.init_chg` | Unmapped | — |
| `header.max_mesh_in_pp` | Unmapped | — |
| `header.dq` | Unmapped | — |
| `header.max_q` | Unmapped | — |
| `header.number_of_pseudo_ao` | Unmapped | — |
| `header.orbital_settings` | Unmapped | — |
| `header.orbital_settings.delta_k` | Unmapped | — |
| `header.orbital_settings.delta_r` | Unmapped | — |
| `header.orbital_settings.dr_uniform` | Unmapped | — |
| `header.orbital_settings.rmax` | Unmapped | — |
| `header.orbital_settings.kmesh` | Unmapped | — |
| `header.orbital_settings.orbital_information` | Mapped | `method.electrons_representation.basis_set.type` |
| `header.allocation_method` | Unmapped | — |
| `header.allocation_method.method` | Unmapped | — |
| `header.allocation_method.nb2d` | Unmapped | — |
| `header.allocation_method.trace_loc_row` | Unmapped | — |
| `header.allocation_method.trace_loc_col` | Unmapped | — |
| `header.allocation_method.nloc` | Unmapped | — |
| `full_scf` | Unmapped | — |
| `full_scf.self_consistent` | Unmapped | — |
| `full_scf.self_consistent.iteration` | Unmapped | — |
| `full_scf.self_consistent.iteration.elec_step` | Unmapped | — |
| `full_scf.self_consistent.iteration.density_error` | Unmapped | — |
| `full_scf.self_consistent.iteration.energy_total_scf_iteration` | Mapped | `calculation.scf_iteration.energy.total` |
| `full_scf.self_consistent.iteration.x_abacus_energy_total_harris_foulkes_estimate` | Unmapped | — |
| `full_scf.self_consistent.iteration.e_fermi` | Mapped | `calculation.scf_iteration.energy.fermi` |
| `full_scf.self_consistent.iteration.e_band` | Unmapped | — |
| `full_scf.self_consistent.iteration.e_one_elec` | Unmapped | — |
| `full_scf.self_consistent.iteration.correction_hartree` | Mapped | `calculation.energy.electrostatic.correction` |
| `full_scf.self_consistent.iteration.XC_functional` | Mapped | `calculation.energy.xc` |
| `full_scf.self_consistent.iteration.e_ewald` | Unmapped | — |
| `full_scf.self_consistent.iteration.e_demet` | Unmapped | — |
| `full_scf.self_consistent.iteration.e_descf` | Unmapped | — |
| `full_scf.self_consistent.iteration.e_efield` | Unmapped | — |
| `full_scf.self_consistent.iteration.hartree_fock_X_scaled` | Mapped | `calculation.energy.hartree_fock_x_scaled` |
| `full_scf.self_consistent.iteration.e_vdw` | Mapped | `calculation.energy.van_der_waals` |
| `full_scf.self_consistent.iteration.magnetization_total` | Unmapped | — |
| `full_scf.self_consistent.iteration.magnetization_absolute` | Unmapped | — |
| `full_scf.self_consistent.energy_occupation` | Mapped | `calculation.eigenvalues.energies`<br>`calculation.eigenvalues.occupations`<br>`calculation.eigenvalues.kpoints` |
| `full_scf.self_consistent.reference_fermi` | Mapped | `calculation.energy.fermi` |
| `full_scf.self_consistent.total` | Mapped | `calculation.energy.total` |
| `full_scf.self_consistent.forces` | Mapped | `calculation.forces.total.value` |
| `full_scf.self_consistent.stress` | Mapped | `calculation.stress.total.value` |
| `full_scf.self_consistent.pressure` | Mapped | `calculation.pressure` |
| `full_scf.self_consistent.positions` | Unmapped | — |
| `full_scf.self_consistent.positions.sites` | Unmapped | — |
| `full_scf.self_consistent.positions.sites` | Unmapped | — |
| `full_scf.self_consistent.positions.units` | Unmapped | — |
| `full_scf.self_consistent.positions.coord_class` | Unmapped | — |
| `full_scf.self_consistent.cell_volume` | Unmapped | — |
| `full_scf.self_consistent.units` | Unmapped | — |
| `full_scf.self_consistent.lattice_vectors` | Unmapped | — |
| `full_scf.self_consistent.reciprocal_units` | Unmapped | — |
| `full_scf.self_consistent.reciprocal_vectors` | Unmapped | — |
| `full_scf.self_consistent.k_points` | Unmapped | — |
| `full_scf.self_consistent.search_adjacent_atoms` | Unmapped | — |
| `full_scf.self_consistent.search_adjacent_atoms.longest_orb_rcut` | Unmapped | — |
| `full_scf.self_consistent.search_adjacent_atoms.longest_nonlocal_projector_rcut` | Unmapped | — |
| `full_scf.self_consistent.search_adjacent_atoms.searching_radius` | Unmapped | — |
| `full_scf.self_consistent.search_adjacent_atoms.searching_radius_unit` | Unmapped | — |
| `full_scf.self_consistent.grid_integration` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.read_space_grid` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.big_cell_numbers_in_grid` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.meshcell_numbers_in_big_cell` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.extended_fft_grid` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.extended_fft_grid_dim` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.atom_number` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.local_orbitals_number` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.nnr` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.nnrg` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.nnrg_last` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.nnrg_now` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.lgd_last` | Unmapped | — |
| `full_scf.self_consistent.grid_integration.lgd_now` | Unmapped | — |
| `non_scf` | Unmapped | — |
| `non_scf.nonself_consistent` | Unmapped | — |
| `non_scf.nonself_consistent.band_structure` | Mapped | `calculation.band_structure_electronic.segment.energies`<br>`calculation.band_structure_electronic.segment.kpoints` |
| `non_scf.nonself_consistent.min_state_energy` | Unmapped | — |
| `non_scf.nonself_consistent.max_state_energy` | Unmapped | — |
| `non_scf.nonself_consistent.delta_energy` | Unmapped | — |
| `non_scf.nonself_consistent.nbands` | Unmapped | — |
| `non_scf.nonself_consistent.sum_bands` | Unmapped | — |
| `non_scf.nonself_consistent.fermi_energy_dos` | Mapped | `calculation.band_structure_electronic.energy_fermi` |
| `non_scf.nonself_consistent.ionic_phase` | Unmapped | — |
| `non_scf.nonself_consistent.electronic_phase` | Unmapped | — |
| `non_scf.nonself_consistent.polarization` | Unmapped | — |
| `non_scf.nonself_consistent.polarization.direction` | Unmapped | — |
| `non_scf.nonself_consistent.polarization.P` | Unmapped | — |
| `non_scf.nonself_consistent.search_adjacent_atoms` | Unmapped | — |
| `non_scf.nonself_consistent.search_adjacent_atoms.longest_orb_rcut` | Unmapped | — |
| `non_scf.nonself_consistent.search_adjacent_atoms.longest_nonlocal_projector_rcut` | Unmapped | — |
| `non_scf.nonself_consistent.search_adjacent_atoms.searching_radius` | Unmapped | — |
| `non_scf.nonself_consistent.search_adjacent_atoms.searching_radius_unit` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.read_space_grid` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.big_cell_numbers_in_grid` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.meshcell_numbers_in_big_cell` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.extended_fft_grid` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.extended_fft_grid_dim` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.atom_number` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.local_orbitals_number` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.nnr` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.nnrg` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.nnrg_last` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.nnrg_now` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.lgd_last` | Unmapped | — |
| `non_scf.nonself_consistent.grid_integration.lgd_now` | Unmapped | — |
| `geometry_optimization` | Unmapped | — |
| `geometry_optimization.ion_step` | Unmapped | — |
| `geometry_optimization.self_consistent` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.elec_step` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.density_error` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.energy_total_scf_iteration` | Mapped | `calculation.scf_iteration.energy.total` |
| `geometry_optimization.self_consistent.iteration.x_abacus_energy_total_harris_foulkes_estimate` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.e_fermi` | Mapped | `calculation.scf_iteration.energy.fermi` |
| `geometry_optimization.self_consistent.iteration.e_band` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.e_one_elec` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.correction_hartree` | Mapped | `calculation.energy.electrostatic.correction` |
| `geometry_optimization.self_consistent.iteration.XC_functional` | Mapped | `calculation.energy.xc` |
| `geometry_optimization.self_consistent.iteration.e_ewald` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.e_demet` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.e_descf` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.e_efield` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.hartree_fock_X_scaled` | Mapped | `calculation.energy.hartree_fock_x_scaled` |
| `geometry_optimization.self_consistent.iteration.e_vdw` | Mapped | `calculation.energy.van_der_waals` |
| `geometry_optimization.self_consistent.iteration.magnetization_total` | Unmapped | — |
| `geometry_optimization.self_consistent.iteration.magnetization_absolute` | Unmapped | — |
| `geometry_optimization.self_consistent.energy_occupation` | Mapped | `calculation.eigenvalues.energies`<br>`calculation.eigenvalues.occupations`<br>`calculation.eigenvalues.kpoints` |
| `geometry_optimization.self_consistent.reference_fermi` | Mapped | `calculation.energy.fermi` |
| `geometry_optimization.self_consistent.total` | Mapped | `calculation.energy.total` |
| `geometry_optimization.self_consistent.forces` | Mapped | `calculation.forces.total.value` |
| `geometry_optimization.self_consistent.stress` | Mapped | `calculation.stress.total.value` |
| `geometry_optimization.self_consistent.pressure` | Mapped | `calculation.pressure` |
| `geometry_optimization.self_consistent.positions` | Unmapped | — |
| `geometry_optimization.self_consistent.positions.sites` | Unmapped | — |
| `geometry_optimization.self_consistent.positions.sites` | Unmapped | — |
| `geometry_optimization.self_consistent.positions.units` | Unmapped | — |
| `geometry_optimization.self_consistent.positions.coord_class` | Unmapped | — |
| `geometry_optimization.self_consistent.cell_volume` | Unmapped | — |
| `geometry_optimization.self_consistent.units` | Unmapped | — |
| `geometry_optimization.self_consistent.lattice_vectors` | Unmapped | — |
| `geometry_optimization.self_consistent.reciprocal_units` | Unmapped | — |
| `geometry_optimization.self_consistent.reciprocal_vectors` | Unmapped | — |
| `geometry_optimization.self_consistent.k_points` | Unmapped | — |
| `geometry_optimization.self_consistent.search_adjacent_atoms` | Unmapped | — |
| `geometry_optimization.self_consistent.search_adjacent_atoms.longest_orb_rcut` | Unmapped | — |
| `geometry_optimization.self_consistent.search_adjacent_atoms.longest_nonlocal_projector_rcut` | Unmapped | — |
| `geometry_optimization.self_consistent.search_adjacent_atoms.searching_radius` | Unmapped | — |
| `geometry_optimization.self_consistent.search_adjacent_atoms.searching_radius_unit` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.read_space_grid` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.big_cell_numbers_in_grid` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.meshcell_numbers_in_big_cell` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.extended_fft_grid` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.extended_fft_grid_dim` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.atom_number` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.local_orbitals_number` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.nnr` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.nnrg` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.nnrg_last` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.nnrg_now` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.lgd_last` | Unmapped | — |
| `geometry_optimization.self_consistent.grid_integration.lgd_now` | Unmapped | — |
| `ion_converged` | Unmapped | — |
| `force_threshold` | Mapped | `workflow2.method.convergence_tolerance_force_maximum` |
| `lattice_converged` | Unmapped | — |
| `stress_threshold` | Mapped | `workflow2.method.convergence_tolerance_stress_maximum` |
| `molecular_dynamics` | Unmapped | — |
| `molecular_dynamics.md_step` | Unmapped | — |
| `molecular_dynamics.self_consistent` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.elec_step` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.density_error` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.energy_total_scf_iteration` | Mapped | `calculation.scf_iteration.energy.total` |
| `molecular_dynamics.self_consistent.iteration.x_abacus_energy_total_harris_foulkes_estimate` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.e_fermi` | Mapped | `calculation.scf_iteration.energy.fermi` |
| `molecular_dynamics.self_consistent.iteration.e_band` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.e_one_elec` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.correction_hartree` | Mapped | `calculation.energy.electrostatic.correction` |
| `molecular_dynamics.self_consistent.iteration.XC_functional` | Mapped | `calculation.energy.xc` |
| `molecular_dynamics.self_consistent.iteration.e_ewald` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.e_demet` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.e_descf` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.e_efield` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.hartree_fock_X_scaled` | Mapped | `calculation.energy.hartree_fock_x_scaled` |
| `molecular_dynamics.self_consistent.iteration.e_vdw` | Mapped | `calculation.energy.van_der_waals` |
| `molecular_dynamics.self_consistent.iteration.magnetization_total` | Unmapped | — |
| `molecular_dynamics.self_consistent.iteration.magnetization_absolute` | Unmapped | — |
| `molecular_dynamics.self_consistent.energy_occupation` | Mapped | `calculation.eigenvalues.energies`<br>`calculation.eigenvalues.occupations`<br>`calculation.eigenvalues.kpoints` |
| `molecular_dynamics.self_consistent.reference_fermi` | Mapped | `calculation.energy.fermi` |
| `molecular_dynamics.self_consistent.total` | Mapped | `calculation.energy.total` |
| `molecular_dynamics.self_consistent.forces` | Mapped | `calculation.forces.total.value` |
| `molecular_dynamics.self_consistent.stress` | Mapped | `calculation.stress.total.value` |
| `molecular_dynamics.self_consistent.pressure` | Mapped | `calculation.pressure` |
| `molecular_dynamics.self_consistent.positions` | Unmapped | — |
| `molecular_dynamics.self_consistent.positions.sites` | Unmapped | — |
| `molecular_dynamics.self_consistent.positions.sites` | Unmapped | — |
| `molecular_dynamics.self_consistent.positions.units` | Unmapped | — |
| `molecular_dynamics.self_consistent.positions.coord_class` | Unmapped | — |
| `molecular_dynamics.self_consistent.cell_volume` | Unmapped | — |
| `molecular_dynamics.self_consistent.units` | Unmapped | — |
| `molecular_dynamics.self_consistent.lattice_vectors` | Unmapped | — |
| `molecular_dynamics.self_consistent.reciprocal_units` | Unmapped | — |
| `molecular_dynamics.self_consistent.reciprocal_vectors` | Unmapped | — |
| `molecular_dynamics.self_consistent.k_points` | Unmapped | — |
| `molecular_dynamics.self_consistent.search_adjacent_atoms` | Unmapped | — |
| `molecular_dynamics.self_consistent.search_adjacent_atoms.longest_orb_rcut` | Unmapped | — |
| `molecular_dynamics.self_consistent.search_adjacent_atoms.longest_nonlocal_projector_rcut` | Unmapped | — |
| `molecular_dynamics.self_consistent.search_adjacent_atoms.searching_radius` | Unmapped | — |
| `molecular_dynamics.self_consistent.search_adjacent_atoms.searching_radius_unit` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.read_space_grid` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.big_cell_numbers_in_grid` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.meshcell_numbers_in_big_cell` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.extended_fft_grid` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.extended_fft_grid_dim` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.atom_number` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.local_orbitals_number` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.nnr` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.nnrg` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.nnrg_last` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.nnrg_now` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.lgd_last` | Unmapped | — |
| `molecular_dynamics.self_consistent.grid_integration.lgd_now` | Unmapped | — |
| `molecular_dynamics.energy` | Mapped | `calculation.energy.total` |
| `molecular_dynamics.potential` | Unmapped | — |
| `molecular_dynamics.electronic_kinetic_energy` | Mapped | `calculation.energy.electronic.kinetic` |
| `molecular_dynamics.temperature` | Mapped | `calculation.temperature` |
| `molecular_dynamics.pressure` | Mapped | `calculation.pressure` |
| `final_energy` | Unmapped | — |
| `finish_date_time` | Mapped | `time_run.date_end`<br>`clean_end` |
| `total_time` | Unmapped | — |

## Abinit / OUT

**Summary:** 36 mapped, 73 unmapped quantities (33.03% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `program.version` |
| `x_abinit_parallel_compilation` | Unmapped | — |
| `program_compilation_host` | Mapped | `program.compilation_host` |
| `x_abinit_start_date` | Mapped | `time_run.date_start` |
| `x_abinit_start_time` | Mapped | `time_run.date_start` |
| `x_abinit_input_file` | Unmapped | — |
| `x_abinit_output_file` | Unmapped | — |
| `x_abinit_input_files_root` | Unmapped | — |
| `x_abinit_output_files_root` | Unmapped | — |
| `x_abinit_total_cpu_time` | Unmapped | — |
| `x_abinit_total_wallclock_time` | Unmapped | — |
| `run_clean_end` | Mapped | `clean_end` |
| `input_variables` | Unmapped | — |
| `input_variables.key_value` | Mapped | `method.electronic`<br>`method.scf`<br>`method.dft.xc_functional`<br>`method.k_mesh`<br>`system.atoms.labels`<br>`system.atoms.positions` |
| `dataset` | Unmapped | — |
| `dataset.x_abinit_dataset_number` | Unmapped | — |
| `dataset.x_abinit_var_ixc` | Unmapped | — |
| `dataset.x_abinit_vprim` | Mapped | `system.atoms.lattice_vectors` |
| `dataset.x_abinit_unit_cell_volume` | Unmapped | — |
| `dataset.self_consistent` | Unmapped | — |
| `dataset.self_consistent.energy_total_scf_iteration` | Mapped | `calculation.scf_iteration.energy.total` |
| `dataset.self_consistent.convergence` | Mapped | `calculation.calculation_converged` |
| `dataset.relaxation` | Unmapped | — |
| `dataset.relaxation.stress_tensor` | Mapped | `calculation.stress.total.value` |
| `dataset.relaxation.self_consistent` | Unmapped | — |
| `dataset.relaxation.self_consistent.energy_total_scf_iteration` | Mapped | `calculation.scf_iteration.energy.total` |
| `dataset.relaxation.self_consistent.convergence` | Mapped | `calculation.calculation_converged` |
| `dataset.relaxation.cartesian_coordinates` | Mapped | `system.atoms.positions` |
| `dataset.relaxation.cartesian_forces` | Mapped | `calculation.forces.total.value_raw` |
| `dataset.relaxation.energy_total` | Mapped | `calculation.energy.total` |
| `dataset.results` | Unmapped | — |
| `dataset.results.cartesian_coordinates` | Unmapped | — |
| `dataset.results.cartesian_forces` | Mapped | `calculation.forces.total.value_raw` |
| `dataset.results.x_abinit_eig_filename` | Unmapped | — |
| `dataset.results.fermi_energy` | Mapped | `calculation.energy.fermi` |
| `dataset.results.x_abinit_magnetisation` | Unmapped | — |
| `dataset.results.eigenvalues` | Mapped | `calculation.band_structure_electronic.segment.energies` |
| `dataset.results.occupation_numbers` | Mapped | `calculation.band_structure_electronic.segment.occupations` |
| `dataset.results.energy_total` | Mapped | `calculation.energy.total` |
| `dataset.results.stress_tensor` | Mapped | `calculation.stress.total.value` |
| `dataset.results.energy_kinetic_electronic` | Mapped | `calculation.energy.kinetic_electronic` |
| `dataset.results.energy_electronstatic` | Mapped | `calculation.energy.contributions` |
| `dataset.results.energy_XC` | Mapped | `calculation.energy.contributions` |
| `dataset.results.ewald` | Mapped | `calculation.energy.contributions` |
| `dataset.results.psp_core` | Mapped | `calculation.energy.contributions` |
| `dataset.results.psp_local` | Mapped | `calculation.energy.contributions` |
| `dataset.results.psp_nonlocal` | Mapped | `calculation.energy.contributions` |
| `dataset.results.internal` | Mapped | `calculation.energy.internal` |
| `dataset.results.energy_correction_entropy` | Mapped | `calculation.energy.correction_entropy` |
| `dataset.results.energy_sum_eigenvalues` | Mapped | `calculation.energy.sum_eigenvalues` |
| `screening_dataset` | Unmapped | — |
| `screening_dataset.precision_algorithm` | Unmapped | — |
| `screening_dataset.kmesh` | Unmapped | — |
| `screening_dataset.kmesh.n_mesh` | Unmapped | — |
| `screening_dataset.kmesh.mesh` | Unmapped | — |
| `screening_dataset.qmesh` | Unmapped | — |
| `screening_dataset.qmesh.n_mesh` | Unmapped | — |
| `screening_dataset.qmesh.mesh` | Unmapped | — |
| `screening_dataset.fftmesh` | Unmapped | — |
| `screening_dataset.n_fftmesh` | Unmapped | — |
| `screening_dataset.symm_screening` | Unmapped | — |
| `screening_dataset.max_band_occ` | Unmapped | — |
| `screening_dataset.n_bands_per_proc` | Unmapped | — |
| `screening_dataset.n_bands_per_node` | Unmapped | — |
| `screening_dataset.n_electrons` | Unmapped | — |
| `screening_dataset.wigner_seitz_radius` | Unmapped | — |
| `screening_dataset.omega_plasma` | Unmapped | — |
| `screening_dataset.frequencies` | Unmapped | — |
| `screening_dataset.frequencies.values` | Mapped | `method.frequency_mesh.points` |
| `screening_dataset.static_diel_const` | Unmapped | — |
| `screening_dataset.static_diel_const_nofields` | Unmapped | — |
| `screening_dataset.chi_q` | Unmapped | — |
| `screening_dataset.chi_q.q_point` | Unmapped | — |
| `screening_dataset.chi_q.av_fulfillment` | Unmapped | — |
| `gw_dataset` | Unmapped | — |
| `gw_dataset.precision_algorithm` | Unmapped | — |
| `gw_dataset.kmesh` | Unmapped | — |
| `gw_dataset.kmesh.n_mesh` | Unmapped | — |
| `gw_dataset.kmesh.mesh` | Unmapped | — |
| `gw_dataset.qmesh` | Unmapped | — |
| `gw_dataset.qmesh.n_mesh` | Unmapped | — |
| `gw_dataset.qmesh.mesh` | Unmapped | — |
| `gw_dataset.fftmesh` | Unmapped | — |
| `gw_dataset.n_fftmesh` | Unmapped | — |
| `gw_dataset.symm_screening` | Unmapped | — |
| `gw_dataset.max_band_occ` | Unmapped | — |
| `gw_dataset.n_bands_per_proc` | Unmapped | — |
| `gw_dataset.n_bands_per_node` | Unmapped | — |
| `gw_dataset.n_electrons` | Unmapped | — |
| `gw_dataset.wigner_seitz_radius` | Unmapped | — |
| `gw_dataset.omega_plasma` | Mapped | `method.frequency_mesh.points` |
| `gw_dataset.ks_band_gaps` | Unmapped | — |
| `gw_dataset.ks_band_gaps.min_direct_gap` | Unmapped | — |
| `gw_dataset.ks_band_gaps.fundamental_gap` | Unmapped | — |
| `gw_dataset.ks_band_gaps.k_top_valence_band` | Unmapped | — |
| `gw_dataset.ks_band_gaps.k_bottom_conduction_band` | Unmapped | — |
| `gw_dataset.sigma_parameters` | Unmapped | — |
| `gw_dataset.sigma_parameters.model` | Unmapped | — |
| `gw_dataset.sigma_parameters.params` | Unmapped | — |
| `gw_dataset.sigma_parameters.freq_step` | Unmapped | — |
| `gw_dataset.sigma_parameters.max_omega_sigma` | Unmapped | — |
| `gw_dataset.sigma_parameters.zcut_avoid` | Unmapped | — |
| `gw_dataset.epsilon_inv` | Unmapped | — |
| `gw_dataset.epsilon_inv.dimensions` | Unmapped | — |
| `gw_dataset.epsilon_inv.params` | Unmapped | — |
| `gw_dataset.self_energy_ee` | Unmapped | — |
| `gw_dataset.self_energy_ee.kpoint` | Mapped | `calculation.eigenvalues.kpoints` |
| `gw_dataset.self_energy_ee.params` | Mapped | `calculation.eigenvalues.n_spin_channels` |
| `gw_dataset.self_energy_ee.data` | Mapped | `calculation.eigenvalues.value_qp`<br>`calculation.eigenvalues.value_ks`<br>`calculation.eigenvalues.value_exchange`<br>`calculation.eigenvalues.value_correlation`<br>`calculation.eigenvalues.qp_linearization_factor` |

## AMS / ams.out

**Summary:** 49 mapped, 115 unmapped quantities (29.88% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `labels_positions` | Mapped | `run.system.atoms.labels`<br>`run.system.atoms.positions` |
| `lattice_vectors` | Mapped | `run.system.atoms.lattice_vectors`<br>`run.system.atoms.periodic` |
| `band_engine_input` | Unmapped | — |
| `band_engine_input.basis` | Unmapped | — |
| `model_parameters` | Unmapped | — |
| `model_parameters.dft_potential` | Unmapped | — |
| `model_parameters.dft_potential.LDA` | Mapped | `run.method.dft.xc_functional.exchange.name`<br>`run.method.dft.xc_functional.correlation.name`<br>`run.method.dft.xc_functional.contributions.name` |
| `model_parameters.dft_potential.GGA` | Mapped | `run.method.dft.xc_functional.exchange.name`<br>`run.method.dft.xc_functional.correlation.name`<br>`run.method.dft.xc_functional.contributions.name` |
| `model_parameters.dft_potential.MGGA` | Mapped | `run.method.dft.xc_functional.exchange.name`<br>`run.method.dft.xc_functional.correlation.name`<br>`run.method.dft.xc_functional.contributions.name` |
| `model_parameters.spin` | Mapped | `run.method.electronic.n_spin_channels` |
| `model_parameters.relativistic_corrections` | Mapped | `run.method.electronic.relativity_method` |
| `model_parameters.x_ams_nuclear_charge_density_model` | Unmapped | — |
| `confinement` | Unmapped | — |
| `confinement.x_ams_basis_functions_confinement_radius` | Unmapped | — |
| `confinement.x_ams_basis_functions_confinement_width` | Unmapped | — |
| `radial_functions` | Unmapped | — |
| `radial_functions.x_ams_radial_points` | Unmapped | — |
| `radial_functions.label` | Mapped | `run.method.atom_parameters.label` |
| `radial_functions.x_ams_nuclear_charge` | Unmapped | — |
| `radial_functions.n_valence_electrons` | Mapped | `run.method.atom_parameters.n_valence_electrons` |
| `radial_functions.charge` | Mapped | `run.method.atom_parameters.charge` |
| `radial_functions.orbital_parameters` | Mapped | `run.method.atom_parameters.orbitals`<br>`run.method.atom_parameters.charges` |
| `radial_functions.x_ams_energy_sum_eigenvalues` | Unmapped | — |
| `radial_functions.x_ams_energy_total_lda` | Unmapped | — |
| `radial_functions.x_ams_energy_kinetic` | Unmapped | — |
| `radial_functions.x_ams_energy_classical_electron_electron_repulsion` | Unmapped | — |
| `radial_functions.x_ams_energy_electron_nucleus_repulsion` | Unmapped | — |
| `radial_functions.x_ams_n_radial_valence_orbitals` | Unmapped | — |
| `radial_functions.x_ams_n_radial_core_orbitals` | Unmapped | — |
| `radial_functions.x_ams_n_radial_fit_functions` | Unmapped | — |
| `ranges_atomic_orbitals` | Unmapped | — |
| `ranges_atomic_orbitals.type` | Unmapped | — |
| `ranges_atomic_orbitals.cutoff` | Unmapped | — |
| `x_ams_run_config` | Unmapped | — |
| `k_space_sampling` | Unmapped | — |
| `k_space_sampling.x_ams_general_integration_parameter` | Unmapped | — |
| `k_space_sampling.x_ams_bz_volume_total` | Unmapped | — |
| `k_space_sampling.x_ams_bz_volume_irreducible` | Unmapped | — |
| `k_space_sampling.x_ams_bz_volume_numerical_integration` | Unmapped | — |
| `k_space_sampling.n_points` | Mapped | `run.method.k_mesh.n_points` |
| `k_space_sampling.x_ams_n_points_unique` | Unmapped | — |
| `k_space_sampling.x_ams_n_simplices` | Unmapped | — |
| `k_space_sampling.x_ams_n_points_per_simplex` | Unmapped | — |
| `k_space_sampling.points` | Mapped | `run.method.k_mesh.points` |
| `scf_options` | Unmapped | — |
| `scf_options.x_ams_diis_settings_dirac` | Unmapped | — |
| `scf_options.x_ams_diis_settings_scf` | Unmapped | — |
| `scf_options.x_ams_growth_factor` | Unmapped | — |
| `scf_options.x_ams_shrink_factor` | Unmapped | — |
| `scf_options.x_ams_mix` | Unmapped | — |
| `scf_options.x_ams_degenerate` | Unmapped | — |
| `scf_options.x_ams_edegen` | Unmapped | — |
| `scf_options.x_ams_scfrtx` | Unmapped | — |
| `scf_options.x_ams_convrg` | Unmapped | — |
| `scf_options.x_ams_ncyclx` | Unmapped | — |
| `scf_options.x_ams_vsplit` | Unmapped | — |
| `x_ams_dftb_resources_dir` | Unmapped | — |
| `x_ams_scc_convergence_enabled` | Unmapped | — |
| `x_ams_max_scc_cycles` | Unmapped | — |
| `x_ams_scc_charge_convergence` | Unmapped | — |
| `x_ams_scc_charge_mixing` | Unmapped | — |
| `x_ams_diis_max_dimension` | Unmapped | — |
| `x_ams_diis_max_coeff` | Unmapped | — |
| `x_ams_adaptive_scc_charge_mixing` | Unmapped | — |
| `x_ams_adaptive_scc_mixing_strategy` | Unmapped | — |
| `x_ams_spin_polarization` | Mapped | `run.method.electronic.n_spin_channels` |
| `x_ams_orbital_dependent_scc` | Unmapped | — |
| `x_ams_orbital_fill_strategy` | Unmapped | — |
| `x_ams_fermi_temperature` | Unmapped | — |
| `x_ams_use_symmetry` | Unmapped | — |
| `x_ams_radial_function_extrapolation_method` | Unmapped | — |
| `x_ams_grimme_d3_dispersion_correction` | Unmapped | — |
| `x_ams_other_parameters` | Unmapped | — |
| `x_ams_assume_insulator` | Unmapped | — |
| `x_ams_ewald_tolerance` | Unmapped | — |
| `x_ams_ewald_range_factor` | Unmapped | — |
| `x_ams_bzstruct_config` | Unmapped | — |
| `total_charge` | Mapped | `run.method.electronic.charge` |
| `atomic_charges` | Mapped | `run.calculation.charges.value` |
| `fermi_energy` | Mapped | `run.calculation.energy.fermi` |
| `energies` | Unmapped | — |
| `energies.electronic_kinetic` | Mapped | `run.calculation.energy.electronic.kinetic` |
| `energies.xc` | Mapped | `run.calculation.energy.xc.value` |
| `energies.electrostatic` | Mapped | `run.calculation.energy.electrostatic.value` |
| `energies.x_ams_v_atomic_def` | Unmapped | — |
| `energies.x_ams_v_def_def` | Unmapped | — |
| `energies.x_ams_dispersion` | Unmapped | — |
| `energies.total` | Mapped | `run.calculation.energy.total.value` |
| `energies.x_ams_fit_error_correction` | Unmapped | — |
| `energies` | Unmapped | — |
| `energies.total` | Mapped | `run.calculation.energy.total.value` |
| `energies.electronic` | Mapped | `run.calculation.energy.electronic.value` |
| `energies.electrostatic` | Mapped | `run.calculation.energy.electrostatic.value` |
| `energies.nuclear_repulsion` | Mapped | `run.calculation.energy.nuclear_repulsion.value` |
| `energies.x_ams_dispersion` | Unmapped | — |
| `forces` | Unmapped | — |
| `forces.p_matrix` | Unmapped | — |
| `forces.electronic_kinetic` | Unmapped | — |
| `forces.xc` | Unmapped | — |
| `forces.electrostatic` | Unmapped | — |
| `forces.pair_interactions` | Unmapped | — |
| `forces.dispersion` | Unmapped | — |
| `forces.total` | Mapped | `run.calculation.forces.total.value` |
| `forces` | Unmapped | — |
| `forces.total` | Mapped | `run.calculation.forces.total.value` |
| `forces.electronic` | Unmapped | — |
| `forces.electrostatic` | Unmapped | — |
| `forces.nuclear_repulsion` | Unmapped | — |
| `forces.dispersion` | Unmapped | — |
| `energy_total` | Mapped | `run.calculation.energy.total.value` |
| `energy_total` | Mapped | `run.calculation.energy.total.value` |
| `forces_total` | Mapped | `run.calculation.forces.total.value` |
| `self_consistency` | Unmapped | — |
| `self_consistency.energy_change` | Mapped | `run.calculation.scf_iteration.energy.change` |
| `total_dos` | Unmapped | — |
| `total_dos.nspin_ne` | Unmapped | — |
| `total_dos.dos` | Mapped | `run.calculation.dos_electronic.energies`<br>`run.calculation.dos_electronic.total.value` |
| `mulliken_populations` | Unmapped | — |
| `mulliken_populations.orbital` | Mapped | `run.calculation.charges.orbital_projected` |
| `mulliken_populations.atom` | Mapped | `run.calculation.charges.value`<br>`run.calculation.charges.spin_projected` |
| `mulliken_populations` | Unmapped | — |
| `mulliken_populations.atom` | Mapped | `run.calculation.charges.value`<br>`run.calculation.charges.spin_projected` |
| `mulliken_populations.total` | Mapped | `run.calculation.charges.total` |
| `atom_charge_analysis` | Unmapped | — |
| `atom_charge_analysis.spin` | Unmapped | — |
| `atom_charge_analysis.methods` | Mapped | `run.calculation.charges.analysis_method` |
| `atom_charge_analysis.atom_charges` | Mapped | `run.calculation.charges.value`<br>`run.calculation.charges.spins` |
| `atom_charge_analysis.total` | Mapped | `run.calculation.charges.total` |
| `dipole_moment` | Mapped | `run.calculation.multipoles.dipole.total` |
| `band_energy_ranges` | Mapped | `run.calculation.eigenvalues.occupations` |
| `band_gap_info` | Unmapped | — |
| `band_gap_info.x_ams_n_valence_electrons` | Unmapped | — |
| `band_gap_info.x_ams_valence_band_index` | Unmapped | — |
| `band_gap_info.x_ams_valence_band_spin_index` | Unmapped | — |
| `band_gap_info.x_ams_conduction_band_index` | Unmapped | — |
| `band_gap_info.x_ams_conduction_band_spin_index` | Unmapped | — |
| `band_gap_info.energy_highest_occupied` | Mapped | `run.calculation.eigenvalues.band_gap.energy_highest_occupied` |
| `band_gap_info.energy_lowest_unoccupied` | Mapped | `run.calculation.eigenvalues.band_gap.energy_lowest_unoccupied` |
| `band_gap_info.value` | Mapped | `run.calculation.eigenvalues.band_gap.value` |
| `program_version` | Mapped | `run.program.version` |
| `time_start` | Mapped | `run.time_run.date_start` |
| `single_point` | Unmapped | — |
| `geometry_optimization` | Unmapped | — |
| `geometry_optimization.step` | Unmapped | — |
| `geometry_optimization.method` | Unmapped | — |
| `geometry_optimization.x_ams_optimization_coordinates` | Unmapped | — |
| `geometry_optimization.x_ams_optimize_lattice` | Unmapped | — |
| `geometry_optimization.convergence_tolerance_force_maximum` | Mapped | `workflow2.method.convergence_tolerance_force_maximum` |
| `geometry_optimization.x_ams_maximum_rms_gradient` | Unmapped | — |
| `geometry_optimization.convergence_tolerance_energy_difference` | Mapped | `workflow2.method.convergence_tolerance_energy_difference` |
| `geometry_optimization.convergence_tolerance_displacement_maximum` | Mapped | `workflow2.method.convergence_tolerance_displacement_maximum` |
| `geometry_optimization.x_ams_maximum_rms_step_allowed` | Unmapped | — |
| `geometry_optimization.x_ams_maximum_stress_energy_allowed` | Unmapped | — |
| `geometry_optimization.x_ams_initial_model_hessian` | Unmapped | — |
| `geometry_optimization.x_ams_hessian_update_method` | Unmapped | — |
| `geometry_optimization.optimization_steps_maximum` | Unmapped | — |
| `geometry_optimization.x_ams_first_gdiis_cycle` | Unmapped | — |
| `geometry_optimization.x_ams_maximum_gdiis_vectors` | Unmapped | — |
| `geometry_optimization.x_ams_trust_radius` | Unmapped | — |
| `geometry_optimization.x_ams_trust_radius_varies` | Unmapped | — |
| `geometry_optimization.x_ams_constraints_converged_at_all_steps` | Unmapped | — |
| `geometry_optimization.x_ams_use_projector` | Unmapped | — |
| `geometry_optimization.x_ams_symmetrize_steps` | Unmapped | — |
| `calculation_results` | Unmapped | — |

## AMS / ams.rkf

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## ATK / .nc

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## ATK / calculator

**Summary:** 3 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `smearing_width` | Mapped | `runschema.method.Electronic.smearing.width` |
| `charge` | Mapped | `runschema.method.Electronic.charge` |
| `xc_functional` | Mapped | `runschema.method.XCFunctional.exchange.name`<br>`runschema.method.XCFunctional.correlation.name`<br>`runschema.method.XCFunctional.contributions.name` |

## BigDFT

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## CASTEP / CellParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `block` | Mapped | `runschema.calculation.Calculation.band_structure_electronic.segment.endpoints_labels`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.kpoints` |
| `value` | Mapped | `runschema.calculation.Calculation.band_structure_electronic.segment.endpoints_labels`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.kpoints` |

## CASTEP / BandsParser

**Summary:** 2 mapped, 4 unmapped quantities (33.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `n_kpoints` | Unmapped | — |
| `n_spins` | Mapped | `runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |
| `n_electrons` | Unmapped | — |
| `n_eigenvalues` | Unmapped | — |
| `fermi_energies` | Unmapped | — |
| `kpt_energies` | Mapped | `runschema.calculation.Calculation.eigenvalues.kpoints`<br>`runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.kpoints`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |

## CASTEP / OutParser

**Summary:** 43 mapped, 23 unmapped quantities (65.15% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `unit_cell` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `unit_cell.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `unit_cell.lattice_parameters` | Unmapped | — |
| `unit_cell.cell_volume` | Unmapped | — |
| `cell_contents` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.velocities` |
| `cell_contents.positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `cell_contents.velocities` | Mapped | `runschema.system.Atoms.velocities` |
| `species` | Mapped | `runschema.method.Method.atom_parameters.label`<br>`runschema.method.Method.atom_parameters.mass` |
| `species.mass` | Mapped | `runschema.method.Method.atom_parameters.label`<br>`runschema.method.Method.atom_parameters.mass` |
| `dft_d` | Unmapped | — |
| `dft_d.method` | Unmapped | — |
| `dft_d.parameter` | Unmapped | — |
| `scf` | Mapped | `runschema.calculation.Calculation.scf_iteration.energy.total`<br>`runschema.calculation.Calculation.scf_iteration.energy.fermi`<br>`runschema.calculation.Calculation.scf_iteration.energy.change`<br>`runschema.calculation.Calculation.scf_iteration.time_physical`<br>`runschema.calculation.Calculation.scf_iteration.time_calculation` |
| `energy` | Mapped | `runschema.calculation.Calculation.energy.free`<br>`runschema.calculation.Calculation.energy.total_t0`<br>`runschema.calculation.Calculation.energy.contributions` |
| `energy_total` | Mapped | `runschema.calculation.Calculation.energy.total` |
| `enthalpy` | Mapped | `runschema.calculation.Calculation.thermodynamics.enthalpy` |
| `frequency` | Unmapped | — |
| `forces` | Mapped | `runschema.calculation.Calculation.forces.total` |
| `stress_tensor` | Mapped | `runschema.calculation.Calculation.stress.total`<br>`runschema.calculation.Calculation.thermodynamics.pressure` |
| `stress_tensor.stress_tensor` | Mapped | `runschema.calculation.Calculation.stress.total` |
| `stress_tensor.pressure` | Mapped | `runschema.calculation.Calculation.thermodynamics.pressure` |
| `mulliken` | Mapped | `runschema.calculation.Calculation.charges.value`<br>`runschema.calculation.Calculation.charges.orbital_projected` |
| `tddft` | Unmapped | — |
| `tddft.iteration` | Unmapped | — |
| `tddft.energies` | Unmapped | — |
| `tddft.time` | Unmapped | — |
| `interaction_energy` | Unmapped | — |
| `interaction_energy.energy` | Unmapped | — |
| `interaction_energy.shell` | Unmapped | — |
| `fermi_energy` (spin up/down) | Unmapped | — |
| `fermi_energy` (spin-degenerate) | Unmapped | — |
| `kpt_energies` | Mapped | `runschema.calculation.Calculation.eigenvalues.kpoints`<br>`runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |
| `iteration` (basis_set_correction) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration.cutoff` | Unmapped | — |
| `md_data` | Unmapped | — |
| `iteration` (md) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (dmd) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (di) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (tss) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration` (cg_refinement) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `spin_density` | Unmapped | — |
| `iteration` (bfgs) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `iteration.iteration` (bfgs) | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `program_version` | Mapped | `runschema.run.Program.name`<br>`runschema.run.Program.version` |
| `program_compilation` | Mapped | `runschema.run.Program.compilation_host` |
| `compiler` | Unmapped | — |
| `maths_library` | Unmapped | — |
| `fft_library` | Unmapped | — |
| `constants_reference` | Unmapped | — |
| `run_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `title` | Mapped | `runschema.method.Method.electrons_representation`<br>`runschema.method.DFT.xc_functional`<br>`runschema.method.Electronic.smearing`<br>`runschema.method.Electronic.relativity_method`<br>`runschema.method.Electronic.van_der_waals_method` |
| `dft_u` | Mapped | `runschema.method.Electronic.method` |
| `calculation` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.vibrational_frequencies` | Mapped | `runschema.calculation.Calculation.vibrational_frequencies.value`<br>`runschema.calculation.Calculation.vibrational_frequencies.infrared`<br>`runschema.calculation.Calculation.vibrational_frequencies.raman` |
| `calculation.raman_tensor` | Unmapped | — |
| `calculation.bandstructure` | Mapped | `runschema.calculation.Calculation.eigenvalues.energies`<br>`runschema.calculation.Calculation.band_structure_electronic.segment.energies` |
| `calculation.basis_set_correction` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.tss` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.cg_refinement` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.md` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.dmd` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.di` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.bfgs` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `calculation.final` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `time` | Mapped | `runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `nmr_flag` | Mapped | `runschema.method.Method.label` |

## CASTEP / CastepParser

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## CHARMM

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## CP2K / trajectory files (XYZ)

Parser class `XYZTrajParser` (`TextParser`). Reads CP2K `*-pos-1.xyz` / trajectory files via the custom XYZ reader wrapped by `TrajParser`.

**Summary:** 1 mapped, 2 unmapped quantities (33.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `trajectory` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `energy` | Unmapped | — |
| `iter` | Unmapped | — |

## CP2K / forces file

Parser class `ForceParser` (`TextParser`). Reads the `*-1_<frame>.xyz` atomic-forces print file resolved by `get_forces`.

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom_forces` | Mapped | `runschema.calculation.Forces.total` |

## CP2K / main .out

Parser class `CP2KOutParser` (`TextParser`). Parses the main CP2K text output. Nested `sub_parser` quantities are shown with dotted paths. The `scf_wavefunction_optimization_quantities` and `quickstep_quantities` blocks are single `Quantity` object lists reused across several sub-parsers (`single_point`, `geometry_optimization`, `molecular_dynamics`, `qs_dftb`); each such quantity is listed once at its canonical location.

**Summary:** 43 mapped, 46 unmapped quantities (48.31% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `dbcsr` | Unmapped | — |
| `program` | Unmapped | — |
| `cp2k` | Mapped | `runschema.run.Program.version`<br>`runschema.run.Program.compilation_host` |
| `global` | Unmapped | — |
| `restart` | Unmapped | — |
| `restart.filename` | Unmapped | — |
| `restart.quantities` | Unmapped | — |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `quickstep` | Mapped | drives `runschema.system.System`, `runschema.method.Method`, `runschema.calculation.Calculation` |
| `quickstep.dft` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.dft_u` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.mp2` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.rpa` | Mapped | `runschema.method.Electronic.method` |
| `quickstep.functional` | Unmapped | — |
| `quickstep.vdw` | Mapped | `runschema.method.Method.van_der_waals_method` |
| `quickstep.qs` | Mapped | `runschema.method.BasisSet.cutoff` |
| `quickstep.atomic_kind_information` | Mapped | drives `runschema.method.AtomParameters`, `runschema.method.BasisSetAtomCentered` |
| `quickstep.atomic_kind_information.atom` | Mapped | drives `runschema.method.AtomParameters`, `runschema.method.BasisSetAtomCentered` |
| `quickstep.atomic_kind_information.atom.kind_label` | Mapped | `runschema.method.AtomParameters.label` |
| `quickstep.atomic_kind_information.atom.kind_number_of_atoms` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.kind_basis_set_name` | Mapped | `runschema.method.BasisSetAtomCentered.name` |
| `quickstep.atomic_kind_information.atom.basis_set_norm_type` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_orbital_shell_sets` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_orbital_shells` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_primitive_cartesian_functions` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_cartesian_basis_functions` | Unmapped | — |
| `quickstep.atomic_kind_information.atom.basis_set_number_of_spherical_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers` | Unmapped | — |
| `quickstep.total_maximum_numbers.atomic_kinds` | Unmapped | — |
| `quickstep.total_maximum_numbers.atoms` | Unmapped | — |
| `quickstep.total_maximum_numbers.shell_sets` | Unmapped | — |
| `quickstep.total_maximum_numbers.shells` | Unmapped | — |
| `quickstep.total_maximum_numbers.primitive_cartesian_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.cartesian_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.spherical_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.orbital_basis_functions` | Unmapped | — |
| `quickstep.total_maximum_numbers.local_part_of_gth_pseudopotential` | Unmapped | — |
| `quickstep.total_maximum_numbers.non_local_part_of_gth_pseudopotential` | Unmapped | — |
| `quickstep.atomic_coordinates` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `quickstep.scf_parameters` | Mapped | drives `runschema.method.Scf` |
| `quickstep.scf_parameters.n_max_iteration` | Mapped | `runschema.method.Scf.n_max_iteration` |
| `quickstep.scf_parameters.threshold_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `quickstep.scf_parameters.md` | Unmapped | — |
| `quickstep.single_point` | Mapped | drives `runschema.calculation.Calculation` (via `scf_wavefunction_optimization_quantities`) |
| `quickstep.single_point.iteration` | Mapped | `runschema.calculation.ScfIteration`<br>`runschema.calculation.Energy.change` |
| `quickstep.single_point.converged` | Unmapped | — |
| `quickstep.single_point.cube_file` | Unmapped | — |
| `quickstep.single_point.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `quickstep.single_point.atom_forces` | Mapped | `runschema.calculation.Forces.total` |
| `quickstep.single_point.stress_tensor` | Mapped | `runschema.calculation.Stress.total` |
| `quickstep.single_point.stress_tensor_one_third_of_trace` | Unmapped | — |
| `quickstep.single_point.stress_tensor_determinant` | Unmapped | — |
| `quickstep.single_point.stress_eigenvalues_eigenvectors` | Unmapped | — |
| `quickstep.single_point.hartree_energy` | Unmapped | — |
| `quickstep.single_point.exchange_correlation_energy` | Mapped | `runschema.calculation.Energy.xc` |
| `quickstep.single_point.electronic_kinetic_energy` | Mapped | `runschema.calculation.Energy.kinetic_electronic` |
| `quickstep.single_point.total_energy` | Unmapped | — |
| `quickstep.single_point.fermi_energy` | Mapped | `runschema.calculation.Energy.fermi`<br>`runschema.calculation.Energy.highest_occupied` |
| `quickstep.geometry_optimization` | Mapped | drives `simulationworkflowschema.GeometryOptimization` |
| `quickstep.geometry_optimization.method` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method` |
| `quickstep.geometry_optimization.self_consistent` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.geometry_optimization.optimization_step` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.geometry_optimization.optimization_step.step` | Mapped | `runschema.calculation.Calculation.step` (frame index) |
| `quickstep.geometry_optimization.optimization_step.information` | Unmapped | — |
| `quickstep.geometry_optimization.optimization_step.self_consistent` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.molecular_dynamics` | Mapped | drives `runschema.calculation.Calculation`, `simulationworkflowschema.MolecularDynamics` |
| `quickstep.molecular_dynamics.initial` | Unmapped | — |
| `quickstep.molecular_dynamics.md_par` | Unmapped | — |
| `quickstep.molecular_dynamics.md_ini` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step` | Mapped | drives `runschema.calculation.Calculation` |
| `quickstep.molecular_dynamics.md_step.ensemble_type` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.step` | Mapped | `runschema.calculation.Calculation.step` |
| `quickstep.molecular_dynamics.md_step.time` | Mapped | `runschema.calculation.Calculation.time` |
| `quickstep.molecular_dynamics.md_step.conserved_quantity` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cpu_time` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.energy_drift` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.potential_energy` | Mapped | `runschema.calculation.Energy.potential`<br>`runschema.calculation.Energy.total` |
| `quickstep.molecular_dynamics.md_step.kinetic_energy` | Mapped | `runschema.calculation.Energy.kinetic`<br>`runschema.calculation.Energy.total` |
| `quickstep.molecular_dynamics.md_step.temperature` | Mapped | `runschema.calculation.Calculation.temperature` |
| `quickstep.molecular_dynamics.md_step.pressure` | Mapped | `runschema.calculation.Calculation.pressure` |
| `quickstep.molecular_dynamics.md_step.barostat_temperature` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.volume` | Mapped | `runschema.calculation.Calculation.volume` |
| `quickstep.molecular_dynamics.md_step.cell_length_instantaneous` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cell_length_average` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cell_angle_instantaneous` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.cell_angle_average` | Unmapped | — |
| `quickstep.molecular_dynamics.md_step.self_consistent` | Mapped | drives `runschema.calculation.Calculation` |
| `spin_polarized` | Mapped | `runschema.calculation.Dos.spin_channel` (spin-channel count of `dos_electronic`) |
| `qs_dftb` | Mapped | drives `runschema.system.System`, `runschema.method.Method`, `runschema.calculation.Calculation` (reuses `quickstep_quantities`) |

## CP2K / PDOS files

Parser class `CP2KPDOSParser` (`DataTextParser`). Reads `*.pdos` projected-DOS files, whose histograms are Gaussian-convoluted in `parse_dos`.

**Summary:** 2 mapped, 1 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom_kind` | Mapped | `runschema.calculation.DosValues.atom_label`<br>`runschema.calculation.DosValues.atom_index` |
| `orbitals` | Mapped | `runschema.calculation.DosValues.orbital` |
| `iter` | Unmapped | — |

## CP2K / input file (.inp / .restart)

Parser class `InpParser` (`FileParser`).

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## CP2K / trajectory / cell / velocities loader

Parser class `TrajParser` (`FileParser`). Wraps `XYZTrajParser`, ASE and MDAnalysis readers to load positions/velocities frames.

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## CPMD / MainfileParser

**Summary:** 22 mapped, 26 unmapped quantities (45.83% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom_coordinates_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` (`ForcesEntry.value`) |
| `scf` | Mapped | `runschema.calculation.ScfIteration.time_calculation`<br>`runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.ScfIteration.energy` (`Energy.total.value`, `Energy.change`) |
| `energies` | Mapped | `runschema.calculation.Calculation.energy` |
| `energies.total` | Mapped | `runschema.calculation.Energy.total` (`EnergyEntry.value`) |
| `energies.kinetic` | Mapped | `runschema.calculation.Energy.kinetic` (`EnergyEntry.value`)<br>`runschema.calculation.Energy.total.kinetic` |
| `energies.electrostatic` | Mapped | `runschema.calculation.Energy.electrostatic` (`EnergyEntry.value`) |
| `energies.x_cpmd_eself` | Unmapped | — |
| `energies.x_cpmd_esr` | Unmapped | — |
| `energies.x_cpmd_local_pseudopotential` | Unmapped | — |
| `energies.x_cpmd_nl_pseudopotential` | Unmapped | — |
| `energies.xc` | Mapped | `runschema.calculation.Energy.xc` (`EnergyEntry.value`) |
| `x_cpmd_restart_file` | Unmapped | — |
| `x_cpmd_total_number_of_scf_steps` | Unmapped | — |
| `x_cpmd_gnmax` | Unmapped | — |
| `x_cpmd_gnorm` | Unmapped | — |
| `x_cpmd_cnstr` | Unmapped | — |
| `time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `header` | Mapped | `runschema.run.Program.version`<br>`runschema.run.TimeRun.date_start` |
| `header.date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_cpmd_compilation_date` | Unmapped | — |
| `header.x_cpmd_input_filename` | Unmapped | — |
| `header.x_cpmd_run_host_name` | Unmapped | — |
| `header.x_cpmd_process_id` | Unmapped | — |
| `header.x_cpmd_run_user_name` | Unmapped | — |
| `info` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method` |
| `info.simulation_type` | Unmapped | — |
| `info.simulation_parameters` | Unmapped | — |
| `info.geometry_optimization_method` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method` |
| `atoms` | Mapped | `runschema.system.Atoms.labels` |
| `supercell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `supercell.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `supercell.lattice_vectors_reciprocal` | Unmapped | — |
| `supercell.x_cpmd_cell_symmetry` | Unmapped | — |
| `supercell.x_cpmd_cell_lattice_constant` | Unmapped | — |
| `supercell.x_cpmd_cell_dimension` | Unmapped | — |
| `supercell.x_cpmd_cell_volume` | Unmapped | — |
| `supercell.x_cpmd_cell_real_space_mesh` | Unmapped | — |
| `supercell.x_cpmd_wave_function_cutoff` | Mapped | `runschema.method.BasisSet.cutoff` |
| `supercell.x_cpmd_density_cutoff` | Unmapped | — |
| `supercell.x_cpmd_number_of_planewaves_wave_function` | Unmapped | — |
| `supercell.x_cpmd_number_of_planewaves_density` | Unmapped | — |
| `geometry_optimization` | Mapped | routes `step` (see `step_quantities` above) |
| `geometry_optimization.step` | Mapped | routes `step_quantities` (see above) |
| `single_point` | Mapped | routes `step_quantities` (see above) |
| `molecular_dynamics` | Mapped | routes `frame` (see below) |
| `molecular_dynamics.frame` | Mapped | `runschema.calculation.Energy.total` (`value`, `potential`, `kinetic`)<br>`runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.temperature` |
| `molecular_dynamics.averaged` | Unmapped | — |

## CPMD / XYZParser

**Summary:** 2 mapped, 2 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `step` | Mapped | routes `step.positions` (see below) |
| `step.step` | Unmapped | — |
| `step.labels` | Unmapped | — |
| `step.positions` | Mapped | `runschema.system.Atoms.positions` |

## Crystal / output

**Summary:** 54 mapped, 71 unmapped quantities (43.20% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `datetime` | Unmapped | — |
| `hostname` | Unmapped | — |
| `os` | Unmapped | — |
| `user` | Unmapped | — |
| `input_path` | Unmapped | — |
| `output_path` | Unmapped | — |
| `executable_path` | Unmapped | — |
| `tmpdir` | Unmapped | — |
| `system_type` | Unmapped | — |
| `calculation_type` | Unmapped | — |
| `dftd3` | Mapped | `runschema.method.Electronic.van_der_waals_method` |
| `dftd3.version` | Mapped | `runschema.method.Electronic.van_der_waals_method` |
| `grimme` | Mapped | `runschema.method.Electronic.van_der_waals_method` |
| `dft` | Mapped | `runschema.method.DFT.xc_functional` |
| `dft.exchange` | Mapped | `runschema.method.XCFunctional.exchange` |
| `dft.correlation` | Mapped | `runschema.method.XCFunctional.correlation` |
| `dft.exchange_correlation` | Mapped | `runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `distribution` | Unmapped | — |
| `start_timestamp` | Mapped | `runschema.run.TimeRun.date_start` |
| `title` | Unmapped | — |
| `hamiltonian_type` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.name` |
| `xc_out` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation` |
| `hybrid_out` | Mapped | `runschema.method.XCFunctional.exchange` |
| `initial_trust_radius` | Unmapped | — |
| `maximum_trust_radius` | Unmapped | — |
| `maximum_gradient_component` | Unmapped | — |
| `rms_gradient_component` | Unmapped | — |
| `rms_displacement_component` | Unmapped | — |
| `geometry_change` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum` |
| `energy_change` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference` |
| `extrapolating_polynomial_order` | Unmapped | — |
| `max_steps` | Unmapped | — |
| `sorting_of_energy_points` | Unmapped | — |
| `material_type` | Unmapped | — |
| `crystal_family` | Unmapped | — |
| `crystal_class` | Unmapped | — |
| `space_group` | Unmapped | — |
| `dimensionality` | Mapped | `runschema.system.Atoms.periodic` |
| `lattice_parameters` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `labels_positions` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.species`<br>`runschema.system.Atoms.labels` |
| `labels_positions_raw` | Unmapped | — |
| `system_edited` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.lattice_vectors` |
| `system_edited.lattice_parameters` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `system_edited.labels_positions` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.species`<br>`runschema.system.Atoms.labels` |
| `system_edited.labels_positions_nanotube` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.species`<br>`runschema.system.Atoms.labels` |
| `lattice_vectors_restart` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `labels_positions_restart` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.species`<br>`runschema.system.Atoms.labels` |
| `symmops` | Unmapped | — |
| `basis_set` | Mapped | `runschema.method.BasisSetAtomCentered.atom_number` |
| `basis_set.basis_sets` | Mapped | `runschema.method.BasisSetAtomCentered.atom_number` |
| `basis_set.basis_sets.species` | Mapped | `runschema.method.BasisSetAtomCentered.atom_number` |
| `basis_set.basis_sets.shells` | Unmapped | — |
| `basis_set.basis_sets.shells.shell_range` | Unmapped | — |
| `basis_set.basis_sets.shells.shell_type` | Unmapped | — |
| `basis_set.basis_sets.shells.shell_coefficients` | Unmapped | — |
| `fock_ks_matrix_mixing` | Unmapped | — |
| `coulomb_bipolar_buffer` | Unmapped | — |
| `exchange_bipolar_buffer` | Unmapped | — |
| `toldee` | Unmapped | — |
| `n_atoms_per_cell` | Unmapped | — |
| `n_shells` | Unmapped | — |
| `n_ao` | Unmapped | — |
| `n_electrons` | Unmapped | — |
| `n_core_electrons` | Unmapped | — |
| `n_symmops` | Unmapped | — |
| `tol_coulomb_overlap` | Unmapped | — |
| `tol_coulomb_penetration` | Unmapped | — |
| `tol_exchange_overlap` | Unmapped | — |
| `tol_pseudo_overlap_f` | Unmapped | — |
| `tol_pseudo_overlap_p` | Unmapped | — |
| `pole_order` | Unmapped | — |
| `calculation_type` | Unmapped | — |
| `xc_functional` | Unmapped | — |
| `cappa` | Unmapped | — |
| `scf_max_iteration` | Mapped | `runschema.method.Scf.n_max_iteration` |
| `convergenge_deltap` | Unmapped | — |
| `weight_f` | Unmapped | — |
| `scf_threshold_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `shrink` | Unmapped | — |
| `n_k_points_ibz` | Unmapped | — |
| `shrink_gilat` | Unmapped | — |
| `n_k_points_gilat` | Unmapped | — |
| `scf_block` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_block.scf_iterations` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_block.scf_iterations.charge_normalization_factor` | Unmapped | — |
| `scf_block.scf_iterations.total_atomic_charges` | Unmapped | — |
| `scf_block.scf_iterations.QGAM` | Unmapped | — |
| `scf_block.scf_iterations.BIEL2` | Unmapped | — |
| `scf_block.scf_iterations.energy_kinetic` | Mapped | `runschema.calculation.Energy.electronic_kinetic` |
| `scf_block.scf_iterations.energy_ee` | Unmapped | — |
| `scf_block.scf_iterations.energy_en_ne` | Unmapped | — |
| `scf_block.scf_iterations.energy_nn` | Unmapped | — |
| `scf_block.scf_iterations.virial_coefficient` | Unmapped | — |
| `scf_block.scf_iterations.TOTENY` | Unmapped | — |
| `scf_block.scf_iterations.integrated_density` | Unmapped | — |
| `scf_block.scf_iterations.NUMDFT` | Unmapped | — |
| `scf_block.scf_iterations.energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.change` |
| `scf_block.scf_iterations.FDIK` | Unmapped | — |
| `number_of_scf_iterations` | Mapped | `runschema.calculation.Calculation.calculation_converged` |
| `energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `geo_opt` | Mapped | `simulationworkflowschema.GeometryOptimization` |
| `geo_opt.geo_opt_step` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.system.Atoms` |
| `geo_opt.geo_opt_step.lattice_parameters` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `geo_opt.geo_opt_step.labels_positions` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.species`<br>`runschema.system.Atoms.labels` |
| `geo_opt.geo_opt_step.labels_positions_nanotube` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.species`<br>`runschema.system.Atoms.labels` |
| `geo_opt.geo_opt_step.energy` | Mapped | `runschema.calculation.Energy.total` |
| `geo_opt.geo_opt_step.time_physical` | Mapped | `runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `geo_opt.converged` | Mapped | `simulationworkflowschema.GeometryOptimizationResults.is_converged_geometry` |
| `band_structure` | Mapped | `runschema.calculation.BandStructure` |
| `band_structure.segments` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `band_structure.segments.start_end` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `band_structure.segments.n_steps` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `band_structure.segments.shrinking_factor` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `band_structure.fermi_energy` | Unmapped | — |
| `dos` | Mapped | `runschema.calculation.Dos` |
| `dos.k_points` | Unmapped | — |
| `dos.highest_occupied` | Unmapped | — |
| `dos.lowest_unoccupied` | Unmapped | — |
| `end_timestamp` | Mapped | `runschema.run.TimeRun.date_end` |
| `forces` | Mapped | `runschema.calculation.Forces.total` |
| `end_timestamp` | Mapped | `runschema.run.TimeRun.date_end` |
| `time_end` | Mapped | `runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `f25_filepath1` | Mapped | `runschema.calculation.BandStructure`<br>`runschema.calculation.Dos` |
| `f25_filepath2` | Mapped | `runschema.calculation.BandStructure`<br>`runschema.calculation.Dos` |

## Crystal / f25

**Summary:** 7 mapped, 1 unmapped quantities (87.50% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `segments` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `segments.first_row` | Mapped | `runschema.calculation.Energy.fermi`<br>`runschema.calculation.BandEnergies.energies` |
| `segments.second_row` | Unmapped | — |
| `segments.energies` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `dos` | Mapped | `runschema.calculation.Dos` |
| `dos.first_row` | Mapped | `runschema.calculation.Dos.energies`<br>`runschema.calculation.Energy.fermi` |
| `dos.second_row` | Mapped | `runschema.calculation.Dos.energies` |
| `dos.values` | Mapped | `runschema.calculation.DosValues.value` |

## DMol3 / MAINFILE

**Summary:** 26 mapped, 62 unmapped quantities (29.55% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `scf` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `scf.iteration` | Mapped | `runschema.calculation.ScfIteration.energy.total`<br>`runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.ScfIteration.time_calculation` |
| `scf.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `scf.n_electrons` | Unmapped | — |
| `scf.coordinates` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `scf.final` | Mapped | `runschema.calculation.Calculation.energy.total`<br>`runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `scf.energy_binding` | Unmapped | — |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `x_dmol3_program_compilation_date` | Unmapped | — |
| `date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `coordinates` | Unmapped | — |
| `simulation_parameters` | Unmapped | — |
| `simulation_parameters.calculation_type` | Unmapped | — |
| `simulation_parameters.functional_name` | Unmapped | — |
| `simulation_parameters.pseudopotential_name` | Unmapped | — |
| `simulation_parameters.basis_name` | Unmapped | — |
| `simulation_parameters.spin_polarization` | Unmapped | — |
| `simulation_parameters.spin` | Unmapped | — |
| `simulation_parameters.rcut` | Unmapped | — |
| `simulation_parameters.integration_grid` | Unmapped | — |
| `simulation_parameters.aux_partition` | Unmapped | — |
| `simulation_parameters.aux_density` | Unmapped | — |
| `simulation_parameters.charge` | Unmapped | — |
| `simulation_parameters.symmetry` | Unmapped | — |
| `simulation_parameters.mulliken_analysis` | Unmapped | — |
| `simulation_parameters.hirshfeld_analysis` | Unmapped | — |
| `simulation_parameters.partial_dos` | Unmapped | — |
| `simulation_parameters.electrostatic_moments` | Unmapped | — |
| `simulation_parameters.nuclear_efg` | Unmapped | — |
| `simulation_parameters.optical_absorption` | Unmapped | — |
| `simulation_parameters.kpoints` | Unmapped | — |
| `simulation_parameters.scf_density_convergence` | Unmapped | — |
| `simulation_parameters.scf_spin_mixing` | Unmapped | — |
| `simulation_parameters.scf_charge_mixing` | Unmapped | — |
| `simulation_parameters.scf_diis` | Unmapped | — |
| `simulation_parameters.scf_iterations` | Unmapped | — |
| `simulation_parameters.scf_number_bad_steps` | Unmapped | — |
| `simulation_parameters.scf_direct` | Unmapped | — |
| `simulation_parameters.scf_restart` | Unmapped | — |
| `simulation_parameters.occupation` | Unmapped | — |
| `simulation_parameters.opt_energy_convergence` | Unmapped | — |
| `simulation_parameters.opt_gradient_convergence` | Unmapped | — |
| `simulation_parameters.opt_displacement_convergence` | Unmapped | — |
| `simulation_parameters.opt_iterations` | Unmapped | — |
| `simulation_parameters.opt_coordinate_system` | Unmapped | — |
| `simulation_parameters.opt_gdiis` | Unmapped | — |
| `simulation_parameters.opt_max_displacement` | Unmapped | — |
| `simulation_parameters.opt_steep_tol` | Unmapped | — |
| `simulation_parameters.opt_hessian_project` | Unmapped | — |
| `optimization` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System`<br>`simulationworkflowschema.GeometryOptimization` |
| `optimization.geometry` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum` |
| `optimization.geometry.coordinates` | Unmapped | — |
| `optimization.geometry.tolerance` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum` |
| `optimization.geometry.energy_gradient` | Unmapped | — |
| `properties` | Mapped | `runschema.calculation.Calculation` |
| `properties.hirschfeld` | Mapped | `runschema.calculation.Charges.analysis_method`<br>`runschema.calculation.Charges.value` |
| `properties.hirschfeld.label` | Unmapped | — |
| `properties.hirschfeld.charge` | Mapped | `runschema.calculation.Charges.value` |
| `properties.dipole_moment` | Mapped | `runschema.calculation.Multipoles.dipole.total` |
| `properties.mulliken` | Mapped | `runschema.calculation.Charges.analysis_method`<br>`runschema.calculation.Charges.value`<br>`runschema.calculation.Charges.spins` |
| `properties.mulliken.charge` | Mapped | `runschema.calculation.Charges.value` |
| `properties.mulliken.spin` | Mapped | `runschema.calculation.Charges.spins` |
| `vibrations` | Mapped | `runschema.calculation.Calculation`<br>`simulationworkflowschema.Thermodynamics` |
| `vibrations.dipole_moment` | Mapped | `runschema.calculation.Multipoles.dipole.total` |
| `vibrations.vibrational_frequencies` | Mapped | `runschema.calculation.VibrationalFrequencies.value` |
| `vibrations.normal_modes` | Unmapped | — |
| `vibrations.normal_modes.label` | Unmapped | — |
| `vibrations.normal_modes.value` | Unmapped | — |
| `vibrations.thermodynamic_quantities` | Mapped | `runschema.calculation.Calculation.temperature`<br>`runschema.calculation.Calculation.pressure`<br>`runschema.calculation.Calculation.energy.zero_point` |
| `vibrations.thermodynamic_quantities.temperature` | Mapped | `runschema.calculation.Calculation.temperature` |
| `vibrations.thermodynamic_quantities.pressure` | Mapped | `runschema.calculation.Calculation.pressure` |
| `vibrations.thermodynamic_quantities.energy_zero_point` | Mapped | `runschema.calculation.Calculation.energy.zero_point` |
| `vibrations.thermodynamic_quantities.x_dmol3_h_trans` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_h_rot` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_h_pv` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_h_vib_minus_zpve` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_s_trans` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_s_rot` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_s_vib` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_c_trans` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_c_rot` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_c_vib` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_h_total_minus_zpve` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_s_total` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_c_total` | Unmapped | — |
| `vibrations.thermodynamic_quantities.x_dmol3_g_total` | Unmapped | — |
| `vibrations.thermodynamic_quantities_steps` | Mapped | `simulationworkflowschema.ThermodynamicsResults.temperature`<br>`simulationworkflowschema.ThermodynamicsResults.entropy`<br>`simulationworkflowschema.ThermodynamicsResults.heat_capacity_c_p`<br>`simulationworkflowschema.ThermodynamicsResults.enthalpy`<br>`simulationworkflowschema.ThermodynamicsResults.gibbs_free_energy` |

## eDMFT / IndmflParser

**Summary:** 6 mapped, 3 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `hybridization_window` | Unmapped | — |
| `real_or_imaginary_axis` | Unmapped | — |
| `n_corr_atoms` | Mapped | `runschema.method.DMFT.n_impurities` |
| `i_atom_corr` | Mapped | `runschema.method.AtomParameters.label` |
| `l_atom_corr` | Mapped | `runschema.method.AtomParameters.orbitals` |
| `siginds_corr` | Mapped | `runschema.method.AtomParameters.n_orbitals`<br>`runschema.method.AtomParameters.orbitals`<br>`runschema.method.DMFT.n_correlated_orbitals` |
| `siginds_corr.indep_cix_blocks` | Unmapped | — |
| `siginds_corr.cix` | Mapped | `runschema.method.AtomParameters.n_orbitals`<br>`runschema.method.DMFT.n_correlated_orbitals` |
| `siginds_corr.orbitals` | Mapped | `runschema.method.AtomParameters.orbitals` |

## eDMFT / ParamsParser

**Summary:** 4 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `general_parameters` | Mapped | `runschema.method.HubbardKanamoriModel.double_counting_correction`<br>`runschema.method.DMFT.impurity_solver` |
| `general_parameters.params` | Mapped | `runschema.method.HubbardKanamoriModel.double_counting_correction`<br>`runschema.method.DMFT.impurity_solver` |
| `impurity_parameters` | Mapped | `runschema.method.HubbardKanamoriModel.u`<br>`runschema.method.HubbardKanamoriModel.jh`<br>`runschema.method.HubbardKanamoriModel.j`<br>`runschema.method.HubbardKanamoriModel.up`<br>`runschema.method.DMFT.n_electrons`<br>`runschema.method.DMFT.inverse_temperature` |
| `impurity_parameters.params` | Mapped | `runschema.method.HubbardKanamoriModel.u`<br>`runschema.method.HubbardKanamoriModel.jh`<br>`runschema.method.HubbardKanamoriModel.j`<br>`runschema.method.HubbardKanamoriModel.up`<br>`runschema.method.DMFT.n_electrons`<br>`runschema.method.DMFT.inverse_temperature` |

## eDMFT / ImpurityGfOutParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameters` | Mapped | `runschema.calculation.GreensFunctions.chemical_potential` |

## eDMFT / MaxentParamsParser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameters` | Mapped | `runschema.method.FrequencyMesh.n_points`<br>`runschema.method.FrequencyMesh.points` |
| `smearing` | Unmapped | — |

## eDMFT / MaxEntSigOutParser

**Summary:** 0 mapped, 1 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `aux_sigma` | Unmapped | — |

## Elk / EigenvalParser

**Summary:** 2 mapped, 2 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `n_kpoints` | Unmapped | — |
| `n_states` | Unmapped | — |
| `kpoint` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `eigenvalue_occupancy` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupancies` |

## Elk / MainfileParser

**Summary:** 16 mapped, 22 unmapped quantities (42.11% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.positions` |
| `species` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `species.atom_label` | Mapped | `runschema.system.Atoms.labels` |
| `species.x_elk_muffin_tin_radius` | Unmapped | — |
| `species.x_elk_muffin_tin_points` | Unmapped | — |
| `species.atom_positions` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `spin_treatment` | Unmapped | — |
| `x_elk_kpoints_grid` | Unmapped | — |
| `x_elk_rgkmax` | Unmapped | — |
| `x_elk_gkmax` | Unmapped | — |
| `x_elk_gmaxvr` | Unmapped | — |
| `x_elk_gvector_size` | Unmapped | — |
| `x_elk_gvector_total` | Unmapped | — |
| `x_elk_lmaxapw` | Unmapped | — |
| `x_elk_nuclear_charge` | Unmapped | — |
| `x_elk_core_charge` | Unmapped | — |
| `x_elk_valence_charge` | Unmapped | — |
| `x_elk_excess_charge` | Unmapped | — |
| `x_elk_electronic_charge` | Unmapped | — |
| `x_elk_wigner_radius` | Unmapped | — |
| `x_elk_empty_states` | Unmapped | — |
| `x_elk_valence_states` | Unmapped | — |
| `x_elk_core_states` | Unmapped | — |
| `x_elk_lo` | Unmapped | — |
| `smearing_type` | Mapped | `runschema.method.Smearing.kind` |
| `smearing_width` | Mapped | `runschema.method.Smearing.width` |
| `electronic_temperature` | Unmapped | — |
| `xc_functional` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation` |
| `scf` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `scf.loop` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `scf.loop.energies` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf.loop.energies.key_val` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.fermi`<br>`runschema.calculation.EnergyEntry.kinetic`<br>`runschema.calculation.EnergyEntry.potential` |
| `scf.loop.charges` | Mapped | `runschema.calculation.ScfIteration.charges` |
| `scf.loop.charges.key_val` | Mapped | `runschema.calculation.Charges.total` |
| `scf.loop.charges.muffin_tin` | Mapped | `runschema.calculation.Charges.value` |
| `scf.loop.energy_chage` | Unmapped | — |
| `scf.loop.time` | Mapped | `runschema.calculation.ScfIteration.time_calculation` |

# exciting parser mapping report

The exciting parser is an imperative NOMAD parser built around several declarative
file-parser classes (subclasses of `TextParser`/`XMLParser`). Each `##` section below
lists every `Quantity(...)` declared in one such class, marks whether the imperative
`ExcitingParser` code writes it into the normalized runschema, and names the runschema
target for the mapped ones. Quantities that only ever populate code-specific
`x_exciting_*` metainfo are reported as `Unmapped`.

## Exciting / INFO.OUT

Parsed by `ExcitingInfoParser`. Consumed by `parse_method`, `parse_system`, `parse_scc`,
`parse_configurations` and their helpers.

`ExcitingInfoParser` also appends quantities in loops with a variable `name` argument
sourced from the `_system_keys_mapping`, `_method_keys_mapping`,
`_miscellaneous_keys_mapping` and `_convergence_keys_mapping` dictionaries; these are listed
below as individual rows at their declaration position (the system/method keys inside
`initialization`, the miscellaneous/convergence keys inside `groundstate.scf_iteration`).

**Summary:** 37 mapped, 43 unmapped quantities (46.25% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `program.version` |
| `hash_id` | Mapped | `program.version_internal` |
| `initialization.lattice_vectors` | Mapped | `system.atoms.lattice_vectors` |
| `initialization.lattice_vectors_reciprocal` | Mapped | `system.atoms.lattice_vectors_reciprocal` |
| `initialization.x_exciting_unit_cell_volume` | Unmapped | — |
| `initialization.x_exciting_brillouin_zone_volume` | Unmapped | — |
| `initialization.x_exciting_number_of_atoms` | Unmapped | — |
| `initialization.x_exciting_spin_treatment` | Mapped | `method.electronic.n_spin_channels` |
| `initialization.x_exciting_number_of_bravais_lattice_symmetries` | Unmapped | — |
| `initialization.x_exciting_number_of_crystal_symmetries` | Unmapped | — |
| `initialization.kpoint_grid` | Mapped | `method.k_mesh.grid` |
| `initialization.kpoint_offset` | Mapped | `method.k_mesh.offset` |
| `initialization.x_exciting_number_kpoints` | Unmapped | — |
| `initialization.x_exciting_rgkmax` | Unmapped | — |
| `initialization.x_exciting_species_rtmin` | Unmapped | — |
| `initialization.x_exciting_gkmax` | Unmapped | — |
| `initialization.x_exciting_gmaxvr` | Unmapped | — |
| `initialization.x_exciting_gvector_size` | Unmapped | — |
| `initialization.x_exciting_gvector_total` | Unmapped | — |
| `initialization.x_exciting_lmaxapw` | Unmapped | — |
| `initialization.x_exciting_nuclear_charge` | Unmapped | — |
| `initialization.x_exciting_electronic_charge` | Unmapped | — |
| `initialization.x_exciting_core_charge_initial` | Unmapped | — |
| `initialization.x_exciting_valence_charge_initial` | Unmapped | — |
| `initialization.x_exciting_wigner_radius` | Unmapped | — |
| `initialization.x_exciting_empty_states` | Unmapped | — |
| `initialization.x_exciting_valence_states` | Unmapped | — |
| `initialization.x_exciting_hamiltonian_size` | Unmapped | — |
| `initialization.x_exciting_pw` | Unmapped | — |
| `initialization.x_exciting_lo` | Unmapped | — |
| `initialization.smearing_kind` | Mapped | `method.electronic.smearing.kind` |
| `initialization.smearing_width` | Mapped | `method.electronic.smearing.width` |
| `initialization.species.number` | Unmapped | — |
| `initialization.species.symbol` | Mapped | `system.atoms.labels` |
| `initialization.species.file` | Unmapped | — |
| `initialization.species.name` | Unmapped | — |
| `initialization.species.nuclear_charge` | Unmapped | — |
| `initialization.species.electronic_charge` | Unmapped | — |
| `initialization.species.atomic_mass` | Unmapped | — |
| `initialization.species.muffin_tin_radius` | Unmapped | — |
| `initialization.species.radial_points` | Unmapped | — |
| `initialization.species.positions_format` | Unmapped | — |
| `initialization.species.positions` | Mapped | `system.atoms.positions` |
| `initialization.potential_mixing` | Unmapped | — |
| `initialization.xc_functional.type` | Mapped | `method.dft.xc_functional` |
| `initialization.xc_functional.name_reference` | Mapped | `method.dft.xc_functional.name`<br>`method.dft.xc_functional.reference` |
| `initialization.xc_functional.parameters` | Unmapped | — |
| `groundstate.scf_iteration.energy_total` | Mapped | `calculation.scf_iteration.energy.total` |
| `groundstate.scf_iteration.energy_contributions` | Mapped | `calculation.scf_iteration.energy` |
| `groundstate.scf_iteration.x_exciting_dos_fermi` | Unmapped | — |
| `groundstate.scf_iteration.charge_contributions` | Mapped | `calculation.scf_iteration.charges` |
| `groundstate.scf_iteration.moment_contributions` | Unmapped | — |
| `groundstate.scf_iteration.x_exciting_gap` | Unmapped | — |
| `groundstate.scf_iteration.time_physical` | Mapped | `calculation.scf_iteration.time_physical` |
| `groundstate.scf_iteration.x_exciting_effective_potential_convergence` | Unmapped | — |
| `groundstate.scf_iteration.x_exciting_energy_convergence` | Mapped | `method.scf.threshold_energy_change` |
| `groundstate.scf_iteration.x_exciting_charge_convergence` | Unmapped | — |
| `groundstate.scf_iteration.x_exciting_IBS_force_convergence` | Unmapped | — |
| `groundstate.final` | Mapped | `calculation.energy.total` |
| `groundstate.atomic_positions.positions_format` | Mapped | `system.atoms.positions` |
| `groundstate.atomic_positions.symbols` | Mapped | `system.atoms.labels` |
| `groundstate.atomic_positions.positions` | Mapped | `system.atoms.positions` |
| `groundstate.forces` | Mapped | `calculation.forces.total` |
| `structure_optimization.optimization_step.atomic_positions.positions_format` | Mapped | `system.atoms.positions` |
| `structure_optimization.optimization_step.atomic_positions.symbols` | Mapped | `system.atoms.labels` |
| `structure_optimization.optimization_step.atomic_positions.positions` | Mapped | `system.atoms.positions` |
| `structure_optimization.optimization_step.forces` | Mapped | `calculation.forces.total` |
| `structure_optimization.optimization_step.step` | Unmapped | — |
| `structure_optimization.optimization_step.method` | Unmapped | — |
| `structure_optimization.optimization_step.n_scf_iterations` | Unmapped | — |
| `structure_optimization.optimization_step.force_convergence` | Mapped | `workflow2.method.convergence_tolerance_force_maximum` |
| `structure_optimization.optimization_step.energy_total` | Mapped | `calculation.energy.total` |
| `structure_optimization.optimization_step.time_calculation` | Mapped | `calculation.time_calculation` |
| `structure_optimization.final` | Mapped | `calculation.energy.total` |
| `structure_optimization.atomic_positions.positions_format` | Mapped | `system.atoms.positions` |
| `structure_optimization.atomic_positions.symbols` | Mapped | `system.atoms.labels` |
| `structure_optimization.atomic_positions.positions` | Mapped | `system.atoms.positions` |
| `structure_optimization.forces` | Mapped | `calculation.forces.total` |
| `hybrids` | Mapped | `calculation.energy.total` |
| `total_time` | Mapped | `calculation.time_physical` |

## Exciting / bandstructure.xml

Parsed by `BandstructureXMLParser` (an `XMLParser`). It declares no `Quantity(...)`
objects; band energies, k-points and segment labels are read directly from XML attributes
through its `parse(key)` method and written to `calculation.band_structure_electronic` in
`_parse_bandstructure`.

**Summary:** 0 mapped, 0 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |

## Exciting / dos.xml

Parsed by `DOSXMLParser` (an `XMLParser`). It declares no `Quantity(...)` objects; total
and partial DOS are read directly from XML attributes through its `parse(key)` method and
written to `calculation.dos_electronic` in `_parse_dos`.

**Summary:** 0 mapped, 0 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |

## Exciting / EIGVAL.OUT

Parsed by `ExcitingEigenvalueParser`. Consumed by `_parse_eigenvalues`.

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `k_points` | Mapped | `calculation.eigenvalues.kpoints` |
| `eigenvalues_occupancies` | Mapped | `calculation.eigenvalues.energies`<br>`calculation.eigenvalues.occupations` |

## Exciting / EVALQP.DAT

Parsed by `ExcitingEvalqpParser`. Consumed by `_parse_evalqp`.

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `kpoints_eigenvalues` | Mapped | `calculation.eigenvalues.energies`<br>`calculation.eigenvalues.kpoints`<br>`calculation.eigenvalues.value_exchange`<br>`calculation.eigenvalues.value_correlation`<br>`calculation.eigenvalues.value_xc_potential`<br>`calculation.eigenvalues.qp_linearization_prefactor` |

## Exciting / GW_INFO.OUT

Parsed by `GWInfoParser`. Consumed by `parse_gw`.

**Summary:** 3 mapped, 2 unmapped quantities (60.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `frequency_data` | Unmapped | — |
| `fermi_energy` | Mapped | `calculation.energy.fermi` |
| `direct_band_gap` | Mapped | `calculation.band_gap.value` |
| `fundamental_band_gap` | Mapped | `calculation.band_gap.value` |
| `optical_band_gap` | Unmapped | — |

## Exciting / FERMISURF.bxsf

Parsed by `ExcitingFermiSurfaceBxsfParser`. Consumed by `_parse_fermisurface`, which
writes only into the code-specific `x_exciting_section_fermi_surface`.

**Summary:** 0 mapped, 3 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `fermi_energy` | Unmapped | — |
| `band_parameters` | Unmapped | — |
| `fermi_surface` | Unmapped | — |

## Exciting / LINENGY.OUT

Parsed by `LinengyParser`. This parser is instantiated but its results are not consumed by
any imperative `parse_*` method, so none of its quantities reach the runschema.

**Summary:** 0 mapped, 12 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `species_block` | Unmapped | — |
| `species_block.element` | Unmapped | — |
| `species_block.apw_line` | Unmapped | — |
| `species_block.apw_line.lo_index` | Unmapped | — |
| `species_block.apw_line.l` | Unmapped | — |
| `species_block.apw_line.order` | Unmapped | — |
| `species_block.apw_line.e_param` | Unmapped | — |
| `species_block.lo_line` | Unmapped | — |
| `species_block.lo_line.lo_index` | Unmapped | — |
| `species_block.lo_line.l` | Unmapped | — |
| `species_block.lo_line.order` | Unmapped | — |
| `species_block.lo_line.e_param` | Unmapped | — |

## Exciting / species file (Si.xml)

Parsed by `SpeciesParser`. Consumed by `_parse_species`, which builds
`method.atom_parameters` and `method.electrons_representation` basis-set sections. The
block-matching quantities carry a nested `key_val` quantity whose name is the dynamic
attribute `self.flag` (`'key_val'`); `to_dict`/`_supplant` folds its attribute key/value
pairs into the parent block dict that `_parse_species` reads. Each `key_val` is listed at
its declaration position with the same status as its parent block.

**Summary:** 12 mapped, 6 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `sp` | Mapped | `method.atom_parameters.atom_number`<br>`method.atom_parameters.label`<br>`method.atom_parameters.mass` |
| `sp.key_val` | Mapped | `method.atom_parameters.atom_number`<br>`method.atom_parameters.label`<br>`method.atom_parameters.mass` |
| `muffinTin` | Mapped | `method.electrons_representation.basis_set.radius`<br>`method.electrons_representation.basis_set.radius_lin_spacing` |
| `muffinTin.key_val` | Mapped | `method.electrons_representation.basis_set.radius`<br>`method.electrons_representation.basis_set.radius_lin_spacing` |
| `atomicState` | Unmapped | — |
| `atomicState.key_val` | Unmapped | — |
| `default` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `default.wf` | Unmapped | — |
| `default.wf.key_val` | Unmapped | — |
| `default.key_val` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `custom` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `custom.wf` | Unmapped | — |
| `custom.wf.key_val` | Unmapped | — |
| `custom.key_val` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo.wf` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo.wf.key_val` | Mapped | `method.electrons_representation.basis_set.orbital` |
| `lo.l` | Mapped | `method.electrons_representation.basis_set.orbital` |

## Exciting / GW output (ExcitingGWOutParser)

Parsed by `ExcitingGWOutParser`. This class declares an empty quantity list
(`self._quantities = []`) and is not wired into `ExcitingParser`; GW output properties are
read via `GWInfoParser` instead.

**Summary:** 0 mapped, 0 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |

## FHI-aims / FHIAimsControlParser

**Summary:** 3 mapped, 16 unmapped quantities (15.79% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `x_fhi_aims_controlIn_charge` | Unmapped | — |
| `x_fhi_aims_controlIn_hse_unit` | Unmapped | — |
| `x_fhi_aims_controlIn_hybrid_xc_coeff` | Unmapped | — |
| `x_fhi_aims_controlIn_MD_time_step` | Unmapped | — |
| `k_grid` | Unmapped | — |
| `k_offset` | Unmapped | — |
| `occupation_type` | Mapped | `runschema.method.Smearing.kind`<br>`runschema.method.Smearing.width` |
| `x_fhi_aims_controlIn_override_relativity` | Unmapped | — |
| `relativistic` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_accuracy_rho` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_accuracy_eev` | Unmapped | — |
| `threshold_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `x_fhi_aims_controlIn_sc_accuracy_forces` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_accuracy_stress` | Unmapped | — |
| `x_fhi_aims_controlIn_sc_iter_limit` | Unmapped | — |
| `x_fhi_aims_controlIn_spin` | Unmapped | — |
| `x_fhi_aims_controlIn_verbatim_writeout` | Unmapped | — |
| `xc` | Unmapped | — |
| `species` | Mapped | `runschema.method.BasisSetContainer.native_tier` |

## FHI-aims / FHIAimsOutParser

**Summary:** 75 mapped, 20 unmapped quantities (78.95% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `structure.labels` | Mapped | `runschema.system.Atoms.labels` |
| `structure.positions` | Mapped | `runschema.system.Atoms.positions` |
| `structure.positions` | Mapped | `runschema.system.Atoms.positions` |
| `structure.velocities` | Mapped | `runschema.system.Atoms.velocities` |
| `eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.occupations` |
| `eigenvalues.kpoints` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `eigenvalues.occupation_eigenvalue` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `date_time` | Mapped | `runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.Calculation.time_physical` |
| `self_consistency.energy_components` | Mapped | `runschema.calculation.Energy` |
| `self_consistency.forces` | Unmapped | — |
| `self_consistency.stress_tensor` | Mapped | `runschema.calculation.Stress.total` |
| `self_consistency.pressure` | Mapped | `runschema.calculation.Thermodynamics.pressure` |
| `self_consistency.scf_convergence` | Mapped | `runschema.calculation.Energy.change` |
| `self_consistency.humo` | Unmapped | — |
| `self_consistency.lumo` | Unmapped | — |
| `self_consistency.fermi_level` | Mapped | `runschema.calculation.Energy.fermi` |
| `self_consistency.fermi_level` | Mapped | `runschema.calculation.Energy.fermi` |
| `self_consistency.time_calculation` | Mapped | `runschema.calculation.ScfIteration.time_calculation` |
| `self_consistency` | Mapped | `runschema.calculation.ScfIteration` |
| `self_consistency` | Mapped | `runschema.calculation.ScfIteration` |
| `self_consistency.scf_convergence` | Mapped | `runschema.calculation.Energy.change` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `energy` | Mapped | `runschema.calculation.Energy` |
| `energy_components` | Mapped | `runschema.calculation.Energy` |
| `energy_xc` | Mapped | `runschema.calculation.Energy.xc` |
| `forces` | Mapped | `runschema.calculation.Forces.free` |
| `forces_raw` | Mapped | `runschema.calculation.ForcesEntry.value_raw` |
| `time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation` |
| `total_dos_files` | Mapped | `runschema.calculation.Dos.total` |
| `atom_projected_dos_files` | Mapped | `runschema.calculation.Dos.atom_projected`<br>`runschema.calculation.Dos.orbital_projected` |
| `species_projected_dos_files` | Mapped | `runschema.calculation.Dos.species_projected`<br>`runschema.calculation.Dos.orbital_projected` |
| `vdW_TS` | Mapped | `runschema.method.Electronic.van_der_waals_method` |
| `vdW_TS.kind` | Mapped | `runschema.calculation.EnergyEntry.kind` |
| `vdW_TS.atom_hirshfeld` | Unmapped | — |
| `converged` | Mapped | `runschema.calculation.Calculation.calculation_converged` |
| `md_run` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.thermodynamic_ensemble`<br>`simulationworkflowschema.molecular_dynamics.ThermostatParameters.thermostat_type` |
| `md_timestep` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.integration_timestep` |
| `md_simulation_time` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.n_steps` |
| `md_temperature` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters.reference_temperature` |
| `md_thermostat_mass` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters.coupling_constant`<br>`simulationworkflowschema.molecular_dynamics.ThermostatParameters.effective_mass` |
| `md_thermostat_units` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters.coupling_constant` |
| `md_calculation_info` | Mapped | `runschema.calculation.Calculation.step`<br>`runschema.calculation.Calculation.time`<br>`runschema.calculation.Calculation.temperature`<br>`runschema.calculation.Energy` |
| `md_system_info` | Mapped | `runschema.system.Atoms.velocities` |
| `md_system_info.positions` | Unmapped | — |
| `md_system_info.velocities` | Mapped | `runschema.system.Atoms.velocities` |
| `version` | Mapped | `runschema.run.Program.version` |
| `x_fhi_aims_program_compilation_date` | Unmapped | — |
| `x_fhi_aims_program_compilation_time` | Unmapped | — |
| `compilation_host` | Mapped | `runschema.run.Program.compilation_host` |
| `cpu1_start` | Mapped | `runschema.run.TimeRun.cpu1_start` |
| `wall_start` | Mapped | `runschema.run.TimeRun.wall_start` |
| `raw_id` | Mapped | `runschema.run.Run.raw_id` |
| `x_fhi_aims_number_of_tasks` | Unmapped | — |
| `x_fhi_aims_parallel_task_nr` | Unmapped | — |
| `x_fhi_aims_parallel_task_host` | Unmapped | — |
| `fhi_aims_files` | Unmapped | — |
| `array_size_parameters` | Mapped | `runschema.method.Electronic.n_spin_channels` |
| `x_fhi_aims_controlInOut_hse_unit` | Unmapped | — |
| `x_fhi_aims_controlInOut_hybrid_xc_coeff` | Mapped | `runschema.method.Functional.parameters`<br>`runschema.method.Functional.weight` |
| `k_grid` | Mapped | `runschema.method.KMesh.grid` |
| `x_fhi_aims_controlInOut_MD_time_step` | Unmapped | — |
| `x_fhi_aims_controlInOut_relativistic` | Mapped | `runschema.method.Electronic.relativity_method` |
| `x_fhi_aims_controlInOut_relativistic` | Mapped | `runschema.method.Electronic.relativity_method` |
| `x_fhi_aims_controlInOut_relativistic_threshold` | Unmapped | — |
| `x_fhi_aims_controlInOut_xc` | Mapped | `runschema.method.XCFunctional`<br>`runschema.method.Functional.name` |
| `petukhov` | Unmapped | — |
| `x_fhi_aims_controlInOut_xc` | Mapped | `runschema.method.XCFunctional`<br>`runschema.method.Functional.name` |
| `x_fhi_aims_controlInOut_xc` | Mapped | `runschema.method.XCFunctional`<br>`runschema.method.Functional.name` |
| `band_segment_points` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.occupations` |
| `species` | Unmapped | — |
| `control_inout` | Mapped | `runschema.method.AtomParameters` |
| `control_inout.species` | Mapped | `runschema.method.AtomParameters.charge`<br>`runschema.method.AtomParameters.mass`<br>`runschema.method.AtomParameters.label`<br>`runschema.method.HubbardKanamoriModel.orbital`<br>`runschema.method.HubbardKanamoriModel.u_effective`<br>`runschema.method.HubbardKanamoriModel.double_counting_correction` |
| `control_in_verbatim` | Unmapped | — |
| `control_in_verbatim.md_controlin` | Unmapped | — |
| `gw_flag` | Mapped | `runschema.method.GW.type` |
| `anacon_type` | Mapped | `runschema.method.GW.analytical_continuation` |
| `gw_analytical_continuation` | Unmapped | — |
| `k_grid` | Mapped | `runschema.method.KMesh.grid` |
| `freq_grid_type` | Mapped | `runschema.method.FrequencyMesh.sampling_method` |
| `n_freq` | Mapped | `runschema.method.FrequencyMesh.n_points` |
| `frequency_data` | Mapped | `runschema.method.FrequencyMesh.points` |
| `frozen_core` | Unmapped | — |
| `n_states_gw` | Mapped | `runschema.method.GW.n_states` |
| `gw_self_consistency` | Mapped | `runschema.calculation.ScfIteration` |
| `gw_eigenvalues` | Mapped | `runschema.calculation.BandEnergies.value_ks`<br>`runschema.calculation.BandEnergies.value_qp`<br>`runschema.calculation.BandEnergies.value_exchange`<br>`runschema.calculation.BandEnergies.value_correlation`<br>`runschema.calculation.BandEnergies.value_ks_xc`<br>`runschema.calculation.BandEnergies.occupations` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `lattice_vectors_reciprocal` | Mapped | `runschema.system.Atoms.lattice_vectors_reciprocal` |
| `full_scf` | Mapped | `runschema.calculation.Calculation` |
| `geometry_optimization` | Mapped | `runschema.calculation.Calculation` |
| `molecular_dynamics` | Mapped | `runschema.calculation.Calculation` |
| `timing` | Mapped | `runschema.calculation.Calculation.time_physical` |
| `timing.total_time` | Mapped | `runschema.calculation.Calculation.time_physical` |

## FLEUR / XMLParser

**Summary:** 22 mapped, 10 unmapped quantities (68.75% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_fleur_precision` | Unmapped | — |
| `header.x_fleur_structure_class` | Unmapped | — |
| `header.x_fleur_additional_flags` | Unmapped | — |
| `start_time` | Mapped | `runschema.run.TimeRun.date_start` |
| `input` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.method.DFT.xc_functional` |
| `input.parameters` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.parameters.key_val` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.cell` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.positions` |
| `input.xc_functional` | Mapped | `runschema.method.DFT.xc_functional` |
| `input.species` | Mapped | `runschema.method.BasisSet.radius`<br>`runschema.method.BasisSet.spherical_harmonics_cutoff`<br>`runschema.method.BasisSet.radius_log_spacing`<br>`runschema.method.BasisSet.n_grid_points` |
| `input.species.key_val` | Mapped | `runschema.method.BasisSet.radius`<br>`runschema.method.BasisSet.spherical_harmonics_cutoff`<br>`runschema.method.BasisSet.radius_log_spacing`<br>`runschema.method.BasisSet.n_grid_points` |
| `input.atom` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `input.atom.species` | Mapped | `runschema.system.Atoms.labels` |
| `input.atom.position` | Mapped | `runschema.system.Atoms.positions` |
| `input.output_parameters` | Unmapped | — |
| `input.output_parameters.key_val` | Unmapped | — |
| `numerical_parameters` | Unmapped | — |
| `numerical_parameters.key_val` | Unmapped | — |
| `scf_iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_iteration.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `scf_iteration.energy_sum_eigenvalues` | Mapped | `runschema.calculation.Energy.sum_eigenvalues` |
| `scf_iteration.energy_x_fleur_density_coulomb_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_density_effective_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_charge_density_xc` | Unmapped | — |
| `scf_iteration.energy_free` | Mapped | `runschema.calculation.Energy.free` |
| `scf_iteration.energy_total_t0` | Mapped | `runschema.calculation.Energy.total_t0` |
| `scf_iteration.fermi` | Mapped | `runschema.calculation.Energy.fermi` |
| `scf_iteration.eigenvalues_kpts` | Mapped | `runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.energies` |
| `scf_iteration.eigenvalues_kpts.kpt` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `scf_iteration.eigenvalues_kpts.energies` | Mapped | `runschema.calculation.BandEnergies.energies` |

## FLEUR / OutParser

**Summary:** 21 mapped, 25 unmapped quantities (45.65% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_fleur_precision` | Unmapped | — |
| `header.x_fleur_with_inversion` | Unmapped | — |
| `header.x_fleur_with_soc` | Unmapped | — |
| `header.x_fleur_additional_flags` | Unmapped | — |
| `input` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.input_parameters` | Unmapped | — |
| `input.input_parameters.key_val` | Unmapped | — |
| `input.parameters` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `input.parameters.key_val` | Mapped | `runschema.method.BasisSet.cutoff`<br>`runschema.method.BasisSet.frozen_core` |
| `system` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.lattice_vectors`<br>`runschema.method.DFT.xc_functional` |
| `system.parameters` | Unmapped | — |
| `system.parameters.key_val` | Unmapped | — |
| `system.x_fleur_unit_cell_volume` | Unmapped | — |
| `system.x_fleur_unit_cell_volume_omega` | Unmapped | — |
| `system.exchange_correlation` | Mapped | `runschema.method.DFT.xc_functional` |
| `system.x_fleur_k_max` | Unmapped | — |
| `system.x_fleur_G_max` | Unmapped | — |
| `system.x_fleur_vol_interstitial` | Unmapped | — |
| `system.x_fleur_nr_of_atom_types` | Unmapped | — |
| `system.cell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `system.atoms` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `electronic` | Mapped | `runschema.method.Smearing.kind`<br>`runschema.method.Smearing.width` |
| `electronic.eigenvalues_parameters` | Unmapped | — |
| `electronic.eigenvalues_parameters.key_val` | Unmapped | — |
| `electronic.smearing` | Mapped | `runschema.method.Smearing.kind` |
| `electronic.width` | Mapped | `runschema.method.Smearing.width` |
| `electronic.x_fleur_nr_of_valence_electrons` | Unmapped | — |
| `electic_field_parameters` | Unmapped | — |
| `electic_field_parameters.x_fleur_tot_elec_charge` | Unmapped | — |
| `electic_field_parameters.x_fleur_tot_nucl_charge` | Unmapped | — |
| `scf_iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_iteration.energy_sum_eigenvalues` | Mapped | `runschema.calculation.Energy.sum_eigenvalues` |
| `scf_iteration.energy_x_fleur_density_coulomb_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_density_effective_potential` | Unmapped | — |
| `scf_iteration.energy_x_fleur_charge_density_xc` | Unmapped | — |
| `scf_iteration.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `scf_iteration.energy_free` | Mapped | `runschema.calculation.Energy.free` |
| `scf_iteration.energy_total_t0` | Mapped | `runschema.calculation.Energy.total_t0` |
| `scf_iteration.forces` | Mapped | `runschema.calculation.Forces.total` |
| `scf_iteration.kpoints` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `scf_iteration.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `scf_iteration.fermi` | Mapped | `runschema.calculation.Energy.fermi` |
| `scf_iteration.x_fleur_n_occupied_states` | Unmapped | — |
| `scf_iteration.x_fleur_valence_charge` | Unmapped | — |

## FPLO

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## GAMESS / OutParser

**Summary:** 28 mapped, 6 unmapped quantities (82.35% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `key_val` | Mapped | `runschema.method.Method.electrons_representation.basis_set.atom_centered.name`<br>`runschema.method.Method.electronic.method`<br>`runschema.method.Method.dft.xc_functional` |
| `scf` | Mapped | `runschema.calculation.Calculation.energy.total.value` |
| `scf.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration.energy.total.value` |
| `scf.iteration.iter` | Mapped | `runschema.calculation.ScfIteration.energy.total.value`<br>`runschema.calculation.ScfIteration.energy.change` |
| `scf.energy_total` | Mapped | `runschema.calculation.Calculation.energy.total.value` |
| `scf.converged` | Mapped | `runschema.calculation.Calculation.calculation_converged` |
| `scf.eigenvectors` | Mapped | `runschema.calculation.Calculation.eigenvalues.energies` |
| `scf.eigenvectors.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `time_physical` | Mapped | `runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `coordinates` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `coordinates.unit` | Mapped | `runschema.system.Atoms.positions` |
| `coordinates.label_charge` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.method.AtomParameters.label`<br>`runschema.method.AtomParameters.charge` |
| `coordinates.position` | Mapped | `runschema.system.Atoms.positions` |
| `gradient` | Mapped | `runschema.calculation.Calculation.forces.total.value` |
| `properties` | Mapped | `runschema.calculation.Calculation.energy` |
| `properties.energy_components` | Mapped | `runschema.calculation.Energy.contributions`<br>`runschema.calculation.EnergyEntry.value` |
| `properties.population_analysis` | Mapped | `runschema.calculation.Calculation.charges` |
| `properties.population_analysis.atomic` | Mapped | `runschema.calculation.Charges.value` |
| `properties.population_analysis.spherical_harmonics` | Mapped | `runschema.calculation.Charges.orbital_projected.value` |
| `properties.population_analysis.atomic_orbitals` | Mapped | `runschema.calculation.Charges.orbital_projected.value` |
| `properties.population_analysis.spins` | Mapped | `runschema.calculation.Charges.spins` |
| `properties.electrostatic_moments` | Mapped | `runschema.calculation.Calculation.multipoles` |
| `properties.electrostatic_moments.dipole` | Mapped | `runschema.calculation.Multipoles.dipole` |
| `properties.electrostatic_moments.dipole.origin` | Unmapped | — |
| `properties.electrostatic_moments.dipole.value` | Mapped | `runschema.calculation.MultipolesEntry.value` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `x_gamess_program_implementation` | Unmapped | — |
| `x_gamess_program_execution_date` | Unmapped | — |
| `x_gamess_memory` | Unmapped | — |
| `basis_options` | Mapped | `runschema.method.Method.electrons_representation.basis_set.atom_centered.name`<br>`runschema.method.BasisSetAtomCentered.formula` |
| `control_options` | Mapped | `runschema.method.Method.electronic.method`<br>`runschema.method.Method.electronic.relativity_method`<br>`runschema.method.Method.dft.xc_functional` |
| `system_options` | Unmapped | — |
| `parameters` | Unmapped | — |
| `geometry_opt` | Mapped | `runschema.system.Atoms`<br>`runschema.calculation.Calculation` |

## Gaussian / parser.py

**Summary:** 36 mapped, 49 unmapped quantities (42.35% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `standard_orientation` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `input_orientation` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `z_matrix_orientation` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `hybrid_xc_coeff1` | Unmapped | — |
| `hybrid_xc_coeff2` | Unmapped | — |
| `mp` | Mapped | `runschema.calculation.Energy.total` |
| `energy_total_mp` | Mapped | `runschema.calculation.Energy.total` |
| `mp2_correction_energy` | Unmapped | — |
| `mp3_correction_energy` | Unmapped | — |
| `mp4dq_correction_energy` | Unmapped | — |
| `mp4sdq_correction_energy` | Unmapped | — |
| `mp4sdtq_correction_energy` | Unmapped | — |
| `mp5_correction_energy` | Unmapped | — |
| `cc` | Mapped | `runschema.calculation.Energy.total` |
| `energy_total_cc` | Mapped | `runschema.calculation.Energy.total` |
| `ccsd_correction_energy` | Unmapped | — |
| `qci` | Mapped | `runschema.calculation.Energy.total` |
| `energy_total_qci` | Mapped | `runschema.calculation.Energy.total` |
| `qcisd_correction_energy` | Unmapped | — |
| `qcisdtq_correction_energy` | Unmapped | — |
| `ci` | Mapped | `runschema.calculation.Energy.total` |
| `energy_total_ci` | Mapped | `runschema.calculation.Energy.total` |
| `ci_correction_energy` | Unmapped | — |
| `semiempirical_method` | Unmapped | — |
| `semiempirical_energy` | Unmapped | — |
| `molmech_method` | Unmapped | — |
| `excited_state` | Unmapped | — |
| `casscf_energy` | Unmapped | — |
| `optimization_completed` | Unmapped | — |
| `population_analysis` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `population_analysis.orbital_symmetries` | Unmapped | — |
| `population_analysis.x_gaussian_elstate_symmetry` | Unmapped | — |
| `population_analysis.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `charge` | Unmapped | — |
| `dipole` | Unmapped | — |
| `quadrupole` | Unmapped | — |
| `octapole` | Unmapped | — |
| `hexadecapole` | Unmapped | — |
| `frequency_unit` | Unmapped | — |
| `reduced_mass_unit` | Unmapped | — |
| `harmonic_force_constant_unit` | Unmapped | — |
| `ir_intensity_unit` | Unmapped | — |
| `frequencies` | Unmapped | — |
| `reduced_masses` | Unmapped | — |
| `harmonic_force_constants` | Unmapped | — |
| `ir_intensities` | Unmapped | — |
| `normal_modes` | Unmapped | — |
| `temperature_pressure` | Mapped | `runschema.calculation.Thermodynamics.temperature`<br>`runschema.calculation.Thermodynamics.pressure`<br>`runschema.calculation.Calculation.temperature`<br>`runschema.calculation.Calculation.pressure` |
| `moments` | Unmapped | — |
| `zero_point_energy` | Mapped | `runschema.calculation.Energy.zero_point` |
| `thermal_correction_energy` | Unmapped | — |
| `thermal_correction_enthalpy` | Mapped | `runschema.calculation.Thermodynamics.enthalpy` |
| `thermal_correction_free_energy` | Unmapped | — |
| `forces` | Mapped | `runschema.calculation.Forces.total` |
| `force_constants` | Unmapped | — |
| `scf_iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_iteration.number` | Unmapped | — |
| `scf_iteration.energy_total_scf_iteration` | Mapped | `runschema.calculation.Energy.total` |
| `scf_iteration.x_gaussian_delta_energy_total_scf_iteration` | Mapped | `runschema.calculation.Energy.change` |
| `scf_iteration_final` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf_iteration_final.x_gaussian_single_configuration_calculation_converged` | Mapped | `runschema.calculation.Calculation.calculation_converged` |
| `scf_iteration_final.x_gaussian_hf_detect` | Unmapped | — |
| `scf_iteration_final.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `scf_iteration_final.x_gaussian_energy_error` | Unmapped | — |
| `scf_iteration_final. energy_kinetic_electronic` | Mapped | `runschema.calculation.Energy.electrostatic` |
| `scf_iteration_final.spin_S2` | Mapped | `runschema.calculation.ScfIteration.spin_S2` |
| `scf_iteration_final.x_gaussian_after_annihilation_spin_S2` | Unmapped | — |
| `scf_iteration_final.x_gaussian_perturbation_energy` | Unmapped | — |
| `x_gaussian_settings_corrected` | Mapped | `runschema.method.Electronic.method`<br>`runschema.method.XCFunctional`<br>`runschema.method.BasisSetContainer` |
| `charge` | Mapped | `runschema.method.Electronic.charge` |
| `spin_target` | Mapped | `runschema.method.Electronic.spin_target` |
| `lattice_vector` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `x_gaussian_atomic_masses` | Unmapped | — |
| `system` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |
| `system.calculation` | Mapped | `runschema.calculation.Calculation` |
| `iteration` | Mapped | `runschema.calculation.Calculation` |
| `program_cpu_time` | Unmapped | — |
| `program_termination_date` | Unmapped | — |
| `program` | Mapped | `runschema.run.Program.name`<br>`runschema.run.Program.version` |
| `x_gaussian_chk_file` | Unmapped | — |
| `x_gaussian_memory` | Unmapped | — |
| `x_gaussian_number_of_processors` | Unmapped | — |
| `calc_type` | Mapped | `runschema.run.Run.workflow` |
| `run` | Mapped | `runschema.run.Run` |

## GPAW

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

The GPAW parser reads `.gpw` restart files, which are binary containers rather than text. `GPWParser` subclasses `TarParser` and reads the tar members `info.xml` plus raw numpy arrays via `get_parameter`/`get_array`, driven at runtime by an XML-declared parameter/array map and an `_info_map` dictionary. `GPW2Parser` subclasses `FileParser` and reads the newer ULM format through `ase.io.ulm.Reader`, exposing values through hand-coded `get_parameter`/`get_array` branches. `GPAWParser` is a plain orchestrator (not a `FileParser` subclass) that dispatches to whichever of the two applies and writes the runschema archive in `parse_method`/`parse_system`/`parse_scc`.

None of these classes declare any `Quantity(...)`. All extraction is performed by imperative accessor methods over binary/XML data, so there are no declarative file-parser quantities to report. (The 18 `Quantity(type=...)` definitions in `metainfo/gpaw.py` are metainfo schema quantities and are out of scope for this report.)

## Magres / MagresFileParser

**Summary:** 22 mapped, 18 unmapped quantities (55.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `lattice_units` | Unmapped | — |
| `atom_units` | Unmapped | — |
| `ms_units` | Unmapped | — |
| `efg_units` | Unmapped | — |
| `efg_local_units` | Unmapped | — |
| `efg_nonlocal_units` | Unmapped | — |
| `isc_units` | Unmapped | — |
| `isc_fc_units` | Unmapped | — |
| `isc_spin_units` | Unmapped | — |
| `isc_orbital_p_units` | Unmapped | — |
| `isc_orbital_d_units` | Unmapped | — |
| `sus_units` | Unmapped | — |
| `cutoffenergy_units` | Mapped | `runschema.method.BasisSet.cutoff` |
| `calculation` | Mapped | `runschema.run.Program.name`<br>`runschema.run.Program.version`<br>`runschema.method.Functional.name`<br>`runschema.method.BasisSet.cutoff`<br>`runschema.method.KMesh.grid`<br>`runschema.method.KMesh.offset` |
| `calculation.code` | Mapped | `runschema.run.Program.name` |
| `calculation.code_version` | Mapped | `runschema.run.Program.version` |
| `calculation.code_hgversion` | Unmapped | — |
| `calculation.code_platform` | Unmapped | — |
| `calculation.name` | Unmapped | — |
| `calculation.comment` | Unmapped | — |
| `calculation.xcfunctional` | Mapped | `runschema.method.Functional.name` |
| `calculation.cutoffenergy` | Mapped | `runschema.method.BasisSet.cutoff` |
| `calculation.pspot` | Unmapped | — |
| `calculation.kpoint_mp_grid` | Mapped | `runschema.method.KMesh.grid` |
| `calculation.kpoint_mp_offset` | Mapped | `runschema.method.KMesh.offset` |
| `atoms` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic`<br>`runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `atoms.lattice` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `atoms.symmetry` | Unmapped | — |
| `atoms.atom` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `magres` | Mapped | `runschema.calculation.MagneticShielding.value`<br>`runschema.calculation.ElectricFieldGradient.value`<br>`runschema.calculation.SpinSpinCoupling.reduced_value`<br>`runschema.calculation.MagneticSusceptibility.value` |
| `magres.ms` | Mapped | `runschema.calculation.MagneticShielding.atoms`<br>`runschema.calculation.MagneticShielding.value`<br>`runschema.calculation.MagneticShielding.isotropic_value` |
| `magres.efg` | Mapped | `runschema.calculation.ElectricFieldGradient.atoms`<br>`runschema.calculation.ElectricFieldGradient.contribution`<br>`runschema.calculation.ElectricFieldGradient.value` |
| `magres.efg_local` | Mapped | `runschema.calculation.ElectricFieldGradient.atoms`<br>`runschema.calculation.ElectricFieldGradient.contribution`<br>`runschema.calculation.ElectricFieldGradient.value` |
| `magres.efg_nonlocal` | Mapped | `runschema.calculation.ElectricFieldGradient.atoms`<br>`runschema.calculation.ElectricFieldGradient.contribution`<br>`runschema.calculation.ElectricFieldGradient.value` |
| `magres.isc` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_fc` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_orbital_p` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_orbital_d` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.isc_spin` | Mapped | `runschema.calculation.SpinSpinCoupling.atoms_1`<br>`runschema.calculation.SpinSpinCoupling.atoms_2`<br>`runschema.calculation.SpinSpinCoupling.contribution`<br>`runschema.calculation.SpinSpinCoupling.reduced_value` |
| `magres.sus` | Mapped | `runschema.calculation.MagneticSusceptibility.scale_dimension`<br>`runschema.calculation.MagneticSusceptibility.value` |

## Molcas

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## MOPAC / MainfileParser

**Summary:** 17 mapped, 4 unmapped quantities (80.95% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `calculation` | Unmapped | — |
| `calculation.parameters` | Unmapped | — |
| `calculation.date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `coordinates` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `x_mopac_fhof` | Unmapped | — |
| `energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `energy_electronic` | Mapped | `runschema.calculation.Energy.electronic` |
| `energy_nuclear_repulsion` | Mapped | `runschema.calculation.Energy.nuclear_repulsion` |
| `n_filled_levels` | Unmapped | — |
| `n_alpha_electrons` | Mapped | `runschema.calculation.BandEnergies.occupations` |
| `n_beta_electrons` | Mapped | `runschema.calculation.BandEnergies.occupations` |
| `eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `forces` | Mapped | `runschema.calculation.Forces.total` |
| `dipole` | Mapped | `runschema.calculation.Multipoles.dipole` |
| `atomic_population` | Mapped | `runschema.calculation.Charges.value` |
| `orbital_population` | Mapped | `runschema.calculation.Charges.orbital_projected` |
| `spin_S2` | Mapped | `runschema.calculation.Calculation.spin_S2` |
| `time_physical` | Mapped | `runschema.calculation.Calculation.time_physical` |
| `time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation` |

## NWChem / OutParser

**Summary:** 64 mapped, 39 unmapped quantities (62.14% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `version` | Mapped | `runschema.run.Program.version` |
| `job_info` | Unmapped | — |
| `job_info.info` | Unmapped | — |
| `input` | Unmapped | — |
| `input.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `input.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `single_point` | Unmapped | — |
| `single_point.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `single_point.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `single_point.dft` | Unmapped | — |
| `single_point.dft.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `single_point.dft.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `single_point.dft.general_info` | Unmapped | — |
| `single_point.dft.general_info.info` | Mapped | `runschema.method.Scf.threshold_energy_change`<br>`runschema.method.Scf.n_max_iteration`<br>`runschema.method.Method.*` |
| `single_point.dft.xc_info` | Unmapped | — |
| `single_point.dft.xc_info.functional` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `single_point.dft.energy` | Mapped | `runschema.calculation.Energy.*`<br>`runschema.calculation.Calculation.x_nwchem_energy_one_electron` |
| `single_point.dft.labels_positions_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` |
| `single_point.dft.qmd_info` | Unmapped | — |
| `single_point.dft.self_consistency` | Unmapped | — |
| `single_point.dft.self_consistency.iteration` | Mapped | `runschema.calculation.ScfIteration.energy`<br>`runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.ScfIteration.time_calculation` |
| `single_point.dft.time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `single_point.dft_gradient` | Unmapped | — |
| `single_point.dft_gradient.labels_positions_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` |
| `single_point.dft_gradient.energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `single_point.pw` | Unmapped | — |
| `single_point.pw.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `single_point.pw.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `single_point.pw.energy` | Mapped | `runschema.calculation.Energy.*` |
| `single_point.pw.spin_S2` | Mapped | `runschema.calculation.Calculation.spin_S2` |
| `single_point.pw.parameters` | Unmapped | — |
| `single_point.pw.self_consistency` | Unmapped | — |
| `single_point.pw.self_consistency.iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `single_point.pw.total_charge` | Mapped | `runschema.method.Electronic.charge` |
| `geometry_optimization` | Unmapped | — |
| `geometry_optimization.parameters` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference` |
| `geometry_optimization.iteration` | Unmapped | — |
| `geometry_optimization.iteration.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `geometry_optimization.iteration.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `geometry_optimization.iteration.dft` | Unmapped | — |
| `geometry_optimization.iteration.dft.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `geometry_optimization.iteration.dft.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `geometry_optimization.iteration.dft.general_info` | Unmapped | — |
| `geometry_optimization.iteration.dft.general_info.info` | Mapped | `runschema.method.Scf.threshold_energy_change`<br>`runschema.method.Scf.n_max_iteration`<br>`runschema.method.Method.*` |
| `geometry_optimization.iteration.dft.xc_info` | Unmapped | — |
| `geometry_optimization.iteration.dft.xc_info.functional` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `geometry_optimization.iteration.dft.energy` | Mapped | `runschema.calculation.Energy.*`<br>`runschema.calculation.Calculation.x_nwchem_energy_one_electron` |
| `geometry_optimization.iteration.dft.labels_positions_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` |
| `geometry_optimization.iteration.dft.qmd_info` | Unmapped | — |
| `geometry_optimization.iteration.dft.self_consistency` | Unmapped | — |
| `geometry_optimization.iteration.dft.self_consistency.iteration` | Mapped | `runschema.calculation.ScfIteration.energy`<br>`runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.ScfIteration.time_calculation` |
| `geometry_optimization.iteration.dft.time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `geometry_optimization.iteration.dft_gradient` | Unmapped | — |
| `geometry_optimization.iteration.dft_gradient.labels_positions_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` |
| `geometry_optimization.iteration.dft_gradient.energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `geometry_optimization.iteration.pw` | Unmapped | — |
| `geometry_optimization.iteration.pw.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `geometry_optimization.iteration.pw.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `geometry_optimization.iteration.pw.energy` | Mapped | `runschema.calculation.Energy.*` |
| `geometry_optimization.iteration.pw.spin_S2` | Mapped | `runschema.calculation.Calculation.spin_S2` |
| `geometry_optimization.iteration.pw.parameters` | Unmapped | — |
| `geometry_optimization.iteration.pw.self_consistency` | Unmapped | — |
| `geometry_optimization.iteration.pw.self_consistency.iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `geometry_optimization.iteration.pw.total_charge` | Mapped | `runschema.method.Electronic.charge` |
| `molecular_dynamics` | Unmapped | — |
| `molecular_dynamics.parameters` | Unmapped | — |
| `molecular_dynamics.iteration` | Unmapped | — |
| `molecular_dynamics.iteration.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `molecular_dynamics.iteration.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `molecular_dynamics.iteration.dft` | Unmapped | — |
| `molecular_dynamics.iteration.dft.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `molecular_dynamics.iteration.dft.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `molecular_dynamics.iteration.dft.general_info` | Unmapped | — |
| `molecular_dynamics.iteration.dft.general_info.info` | Mapped | `runschema.method.Scf.threshold_energy_change`<br>`runschema.method.Scf.n_max_iteration`<br>`runschema.method.Method.*` |
| `molecular_dynamics.iteration.dft.xc_info` | Unmapped | — |
| `molecular_dynamics.iteration.dft.xc_info.functional` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `molecular_dynamics.iteration.dft.energy` | Mapped | `runschema.calculation.Energy.*`<br>`runschema.calculation.Calculation.x_nwchem_energy_one_electron` |
| `molecular_dynamics.iteration.dft.labels_positions_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` |
| `molecular_dynamics.iteration.dft.qmd_info` | Unmapped | — |
| `molecular_dynamics.iteration.dft.self_consistency` | Unmapped | — |
| `molecular_dynamics.iteration.dft.self_consistency.iteration` | Mapped | `runschema.calculation.ScfIteration.energy`<br>`runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.ScfIteration.time_calculation` |
| `molecular_dynamics.iteration.dft.time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `molecular_dynamics.iteration.dft_gradient` | Unmapped | — |
| `molecular_dynamics.iteration.dft_gradient.labels_positions_forces` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.calculation.Forces.total` |
| `molecular_dynamics.iteration.dft_gradient.energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `molecular_dynamics.iteration.pw` | Unmapped | — |
| `molecular_dynamics.iteration.pw.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `molecular_dynamics.iteration.pw.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `molecular_dynamics.iteration.pw.energy` | Mapped | `runschema.calculation.Energy.*` |
| `molecular_dynamics.iteration.pw.spin_S2` | Mapped | `runschema.calculation.Calculation.spin_S2` |
| `molecular_dynamics.iteration.pw.parameters` | Unmapped | — |
| `molecular_dynamics.iteration.pw.self_consistency` | Unmapped | — |
| `molecular_dynamics.iteration.pw.self_consistency.iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `molecular_dynamics.iteration.pw.total_charge` | Mapped | `runschema.method.Electronic.charge` |
| `pw` | Unmapped | — |
| `pw.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `pw.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `pw.energy` | Mapped | `runschema.calculation.Energy.*` |
| `pw.spin_S2` | Mapped | `runschema.calculation.Calculation.spin_S2` |
| `pw.parameters` | Unmapped | — |
| `pw.self_consistency` | Unmapped | — |
| `pw.self_consistency.iteration` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `pw.total_charge` | Mapped | `runschema.method.Electronic.charge` |

## OCEAN / parser.py — PhotonParser

**Summary:** 3 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `operator` | Mapped | `runschema.method.Photon.multipole_type` |
| `vectors` | Mapped | `runschema.method.Photon.polarization`<br>`runschema.method.Photon.momentum_transfer` |
| `photon_energy` | Mapped | `runschema.method.Photon.energy` |

## OCEAN / parser.py — LanczosParser

**Summary:** 0 mapped, 1 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `data` | Unmapped | — |

## Octopus / EigenvalueParser

**Summary:** 3 mapped, 1 unmapped quantities (75.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `eigenvalues` | Mapped | `runschema.calculation.Calculation.eigenvalues` |
| `eigenvalues.eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.kpoints`<br>`runschema.calculation.BandEnergies.occupations` |
| `eigenvalues.unit` | Unmapped | — |
| `eigenvalues.fermi_energy` | Mapped | `runschema.calculation.Energy.fermi` |

## Octopus / InfoParser

**Summary:** 4 mapped, 6 unmapped quantities (40.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `brillouin_zone_sampling` | Mapped | `runschema.method.KMesh.grid` |
| `brillouin_zone_sampling.kgrid` | Mapped | `runschema.method.KMesh.grid` |
| `brillouin_zone_sampling.n_kpoints` | Unmapped | — |
| `brillouin_zone_sampling.n_kpoints_reduced` | Unmapped | — |
| `brillouin_zone_sampling.kpoints` | Unmapped | — |
| `energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.free`<br>`runschema.calculation.Energy.nuclear_repulsion`<br>`runschema.calculation.Energy.sum_eigenvalues`<br>`runschema.calculation.Energy.electrostatic`<br>`runschema.calculation.Energy.exchange`<br>`runschema.calculation.Energy.correlation`<br>`runschema.calculation.Energy.van_der_waals`<br>`runschema.calculation.Energy.correction_entropy`<br>`runschema.calculation.Energy.kinetic_electronic` |
| `total_magnetic_moment` | Unmapped | — |
| `local_magnetic_moments` | Unmapped | — |
| `dipole` | Unmapped | — |
| `forces` | Mapped | `runschema.calculation.Forces.free` |

## Octopus / ControlParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `line` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.Electronic.smearing`<br>`runschema.method.Electronic.method`<br>`runschema.method.DFT.xc_functional` |

## Octopus / InpParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `block` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.DFT.xc_functional` |

## Octopus / LogParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `block` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.DFT.xc_functional` |

## Octopus / OutParser

**Summary:** 18 mapped, 4 unmapped quantities (81.82% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.options` | Mapped | `runschema.run.Program.version` |
| `grid` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.periodic` |
| `grid.boxshape` | Unmapped | — |
| `grid.npbc` | Mapped | `runschema.system.Atoms.periodic` |
| `grid.cell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `grid.spacing` | Unmapped | — |
| `theory_level` | Mapped | `runschema.method.DFT.xc_functional` |
| `theory_level.theory_level` | Unmapped | — |
| `theory_level.exchange` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `theory_level.correlation` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions` |
| `self_consistent` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistent.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistent.iteration.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy` (`Energy.total`) |
| `self_consistent.iteration.fermi_level` | Mapped | `runschema.calculation.ScfIteration.energy` (`Energy.fermi`) |
| `self_consistent.iteration.time` | Mapped | `runschema.calculation.ScfIteration.time_calculation`<br>`runschema.calculation.ScfIteration.time_physical` |
| `time_dependent` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`) |
| `time_dependent.iteration` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`) |
| `x_octopus_info_scf_converged_iterations` | Unmapped | — |
| `minimization` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`)<br>`runschema.system.System.atoms` |
| `minimization.energy_total` | Mapped | `runschema.calculation.Calculation.energy` (`Energy.total`) |
| `minimization.number` | Mapped | `runschema.system.System.atoms` |

## ONETEP / InputParser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameter` | Unmapped | — |
| `block` | Mapped | `runschema.system.Atoms.lattice_vectors`<br>`runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |

## ONETEP / OutParser

**Summary:** 26 mapped, 16 unmapped quantities (61.90% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `iteration.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy`<br>`runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry.value` |
| `iteration.band_gap` | Unmapped | — |
| `iteration.x_onetep_rms_occupancy_error` | Unmapped | — |
| `iteration.x_onetep_commutator` | Unmapped | — |
| `iteration.rms_gradient` | Unmapped | — |
| `energy_components` | Mapped | `runschema.calculation.Calculation.energy` |
| `energy_components.contribution` | Mapped | `runschema.calculation.Energy.kinetic_electronic`<br>`runschema.calculation.Energy.correction_hartree`<br>`runschema.calculation.Energy.xc`<br>`runschema.calculation.Energy.ewald`<br>`runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry.value` |
| `energy_components.integrated_density` | Unmapped | — |
| `forces` | Mapped | `runschema.calculation.Calculation.forces` |
| `forces.value` | Mapped | `runschema.calculation.Forces.total`<br>`runschema.calculation.ForcesEntry.value` |
| `convergence_tolerance_energy_difference` | Unmapped | — |
| `convergence_tolerance_force_maximum` | Unmapped | — |
| `convergence_tolerance_displacement_maximum` | Unmapped | — |
| `cell` | Mapped | `runschema.system.System.atoms` |
| `cell.positions` | Mapped | `runschema.system.Atoms.positions` |
| `cell.labels` | Mapped | `runschema.system.Atoms.labels` |
| `mulliken` | Mapped | `runschema.calculation.Calculation.charges`<br>`runschema.calculation.Charges.analysis_method`<br>`runschema.calculation.Charges.value` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `program_name` | Mapped | `runschema.run.Program.name` |
| `x_onetep_number_of_processors` | Unmapped | — |
| `input_file` | Unmapped | — |
| `input` | Mapped | `runschema.method.DFT.xc_functional` |
| `input.parameter` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid`<br>`runschema.method.XCFunctional.contributions`<br>`runschema.method.Functional.name` |
| `date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `date_end` | Mapped | `runschema.run.TimeRun.date_end` |
| `psinc` | Mapped | `runschema.method.Method.electrons_representation`<br>`runschema.method.BasisSetContainer.basis_set` |
| `psinc.cutoff` | Mapped | `runschema.method.BasisSet.cutoff` |
| `geometry_optimization` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.single_point` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.iteration` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.iteration.improve` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.converged` | Unmapped | — |
| `geometry_optimization.final_configuration` | Unmapped | — |
| `single_point` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `tddft` | Mapped | `runschema.system.System.atoms`<br>`runschema.calculation.Calculation` |
| `tddft.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `tddft.iteration.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy`<br>`runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry.value` |
| `tddft.iteration.x_onetep_tddft_omega_change` | Unmapped | — |
| `tddft.iteration.rms_gradient` | Unmapped | — |
| `tddft.iteration.x_onetep_tddft_number_conv_states` | Unmapped | — |
| `tddft.excitation` | Unmapped | — |

## OpenMX / scf_step_parser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `NormRD` | Unmapped | — |
| `Uele` | Mapped | `runschema.calculation.scf_iteration.energy.sum_eigenvalues.value` |

## OpenMX / md_step_parser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `SCF` | Mapped | `runschema.calculation.scf_iteration` |
| `Utot` | Mapped | `runschema.calculation.energy.total.value` |

## OpenMX / species_and_coordinates_parser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom` | Mapped | `runschema.system.atoms.positions`<br>`runschema.system.atoms.labels` |

## OpenMX / species_definition_parser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `species` | Mapped | `runschema.method.atom_parameters.label`<br>`runschema.method.atom_parameters.atom_number`<br>`runschema.method.atom_parameters.pseudopotential`<br>`runschema.method.atom_parameters.core_hole` |

## OpenMX / core_hole_parser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `core_hole` | Mapped | `runschema.method.atom_parameters.core_hole.ms_quantum_bool`<br>`runschema.method.atom_parameters.core_hole.j_quantum_number`<br>`runschema.method.atom_parameters.core_hole.mj_quantum_number` |

## OpenMX / eigenvalues_parser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `kpoints` | Mapped | `runschema.calculation.eigenvalues.kpoints`<br>`runschema.calculation.eigenvalues.n_kpoints`<br>`runschema.calculation.eigenvalues.kpoints_multiplicities`<br>`runschema.method.k_mesh.points`<br>`runschema.method.k_mesh.multiplicities` |
| `eigenvalues` | Mapped | `runschema.calculation.eigenvalues.energies` |

## OpenMX / mainfile_parser

**Summary:** 26 mapped, 2 unmapped quantities (92.86% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `date_start` | Mapped | `runschema.run.time_run.date_start` |
| `elapsed_time` | Mapped | `runschema.run.time_run.date_end` |
| `program_version` | Mapped | `runschema.run.program.version` |
| `md_step` | Mapped | `runschema.calculation.energy.total.value`<br>`runschema.calculation.scf_iteration.energy.sum_eigenvalues.value` |
| `atoms` | Mapped | `runschema.system.atoms.positions`<br>`runschema.system.atoms.labels`<br>`runschema.system.atoms.lattice_vectors` |
| `species` | Mapped | `runschema.method.atom_parameters` |
| `core_hole` | Mapped | `runschema.method.atom_parameters.core_hole.ms_quantum_bool`<br>`runschema.method.atom_parameters.core_hole.mj_quantum_number` |
| `input_lattice_vectors` | Mapped | `runschema.system.atoms.lattice_vectors` |
| `scf.XcType` | Mapped | `runschema.method.dft.xc_functional.exchange`<br>`runschema.method.dft.xc_functional.correlation` |
| `scf.SpinPolarization` | Mapped | `runschema.method.electronic.n_spin_channels` |
| `scf.stress.tensor` | Unmapped | — |
| `Atoms.SpeciesAndCoordinates.Unit` | Mapped | `runschema.system.atoms.positions` |
| `Atoms.UnitVectors.Unit` | Mapped | `runschema.system.atoms.lattice_vectors` |
| `scf.Hubbard.U` | Mapped | `runschema.method.electronic.method` |
| `MD.maxIter` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.optimization_steps_maximum`<br>`simulationworkflowschema.MolecularDynamicsMethod.n_steps` |
| `MD.Type` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.method`<br>`simulationworkflowschema.MolecularDynamicsMethod.thermodynamic_ensemble` |
| `MD.TimeStep` | Mapped | `simulationworkflowschema.MolecularDynamicsMethod.integration_timestep` |
| `MD.Opt.criterion` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum` |
| `MD.TempControl` | Mapped | `simulationworkflowschema.molecular_dynamics.ThermostatParameters` |
| `scf.maxIter` | Mapped | `runschema.method.scf.n_max_iteration` |
| `scf.criterion` | Mapped | `runschema.method.scf.threshold_energy_change` |
| `scf.ElectronicTemperature` | Mapped | `runschema.method.electronic.smearing.width` |
| `scf.Kgrid` | Mapped | `runschema.method.k_mesh.grid` |
| `scf.dftD` | Mapped | `runschema.method.electronic.van_der_waals_method` |
| `version.dftD` | Mapped | `runschema.method.electronic.van_der_waals_method` |
| `have_timing` | Mapped | `runschema.run.clean_end` |
| `eigenvalues` | Mapped | `runschema.calculation.eigenvalues.energies`<br>`runschema.calculation.eigenvalues.kpoints` |
| `elapsed.time` | Unmapped | — |

## OpenMX / stdout_parser

**Summary:** 1 mapped, 2 unmapped quantities (33.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `scf.stress.tensor` | Mapped | `runschema.calculation.stress.total.value` |
| `Uele` | Unmapped | — |
| `elapsed.time` | Unmapped | — |

## ORCA / parser.py — `OutParser`

**Summary:** 37 mapped, 125 unmapped quantities (22.84% coverage).

Quantities are listed in source declaration order. Nested `sub_parser` quantities are shown with dotted paths relative to their containing quantity. Reusable quantity lists (`basis_set_quantities`, `grid_quantities`, `calculation_quantities`, `geometry_optimization_quantities`, etc.) are defined once and referenced from multiple parents; the dotted path shows a representative container.

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `basis_set.basis_set_atom_labels` | Unmapped | — |
| `basis_set.basis_set` | Unmapped | — |
| `basis_set.basis_set_contracted` | Unmapped | — |
| `basis_set_statistics.nb_of_primitive_gaussian_shells` | Unmapped | — |
| `basis_set_statistics.nb_of_primitive_gaussian_functions` | Unmapped | — |
| `basis_set_statistics.nb_of_contracted_shells` | Unmapped | — |
| `basis_set_statistics.nb_of_contracted_basis_functions` | Unmapped | — |
| `basis_set_statistics.highest_angular_moment` | Unmapped | — |
| `basis_set_statistics.maximum_contraction_depth` | Unmapped | — |
| `self_consistent.dft_grid_generation.gral_integ_accuracy` | Unmapped | — |
| `self_consistent.dft_grid_generation.radial_grid_type` | Unmapped | — |
| `self_consistent.dft_grid_generation.angular_grid` | Unmapped | — |
| `self_consistent.dft_grid_generation.grid_pruning_method` | Unmapped | — |
| `self_consistent.dft_grid_generation.weight_gener_scheme` | Unmapped | — |
| `self_consistent.dft_grid_generation.basis_fn_cutoff` | Unmapped | — |
| `self_consistent.dft_grid_generation.integr_weight_cutoff` | Unmapped | — |
| `self_consistent.dft_grid_generation.nb_grid_pts_after_initial_pruning` | Unmapped | — |
| `self_consistent.dft_grid_generation.nb_grid_pts_after_weights_screening` | Unmapped | — |
| `self_consistent.dft_grid_generation.total_nb_grid_pts` | Unmapped | — |
| `self_consistent.dft_grid_generation.total_nb_batches` | Unmapped | — |
| `self_consistent.dft_grid_generation.avg_nb_points_per_batch` | Unmapped | — |
| `self_consistent.dft_grid_generation.avg_nb_grid_pts_per_atom` | Unmapped | — |
| `self_consistent.scf_convergence.last_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `self_consistent.scf_convergence.last_max_density_change` | Unmapped | — |
| `self_consistent.scf_convergence.last_rms_density_change` | Mapped | `runschema.method.Scf.threshold_density_change` |
| `self_consistent.mulliken.atomic_charges` | Mapped | `runschema.calculation.Charges.value`<br>`runschema.calculation.Charges.total`<br>`runschema.calculation.Charges.n_charges_atoms` |
| `self_consistent.mulliken.atomic_charges.species` | Unmapped | — |
| `self_consistent.mulliken.atomic_charges.charge` | Mapped | `runschema.calculation.Charges.value` |
| `self_consistent.mulliken.atomic_charges.total_charge` | Mapped | `runschema.calculation.Charges.total` |
| `self_consistent.mulliken.orbital_charges` | Mapped | `runschema.calculation.Charges.orbital_projected` |
| `self_consistent.mulliken.orbital_charges.atom` | Mapped | `runschema.calculation.ChargesValue.atom_label`<br>`runschema.calculation.ChargesValue.atom_index` |
| `self_consistent.mulliken.orbital_charges.atom.species` | Mapped | `runschema.calculation.ChargesValue.atom_label` |
| `self_consistent.mulliken.orbital_charges.atom.charge` | Mapped | `runschema.calculation.ChargesValue.orbital`<br>`runschema.calculation.ChargesValue.value` |
| `self_consistent.scf_settings.XC_functional_type` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation` |
| `self_consistent.scf_settings.XC_functional_type` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation` |
| `self_consistent.scf_settings.exchange_functional` | Mapped | `runschema.method.XCFunctional.exchange` |
| `self_consistent.scf_settings.xalpha_param` | Mapped | `runschema.method.XCFunctional.exchange` |
| `self_consistent.scf_settings.beckes_beta_param` | Unmapped | — |
| `self_consistent.scf_settings.correl_functional` | Mapped | `runschema.method.XCFunctional.correlation` |
| `self_consistent.scf_settings.lda_part_of_gga_corr` | Mapped | `runschema.method.XCFunctional.correlation` |
| `self_consistent.scf_settings.scalar_relativistic_method` | Unmapped | — |
| `self_consistent.scf_settings.speed_of_light_used` | Unmapped | — |
| `self_consistent.scf_settings.hf_type` | Unmapped | — |
| `self_consistent.scf_settings.total_charge` | Unmapped | — |
| `self_consistent.scf_settings.multiplicity` | Unmapped | — |
| `self_consistent.scf_settings.nelectrons` | Unmapped | — |
| `self_consistent.scf_settings.nuclear_repulsion` | Unmapped | — |
| `self_consistent.scf_settings.convergence_check_mode` | Unmapped | — |
| `self_consistent.scf_settings.energy_change_tolerance` | Unmapped | — |
| `self_consistent.scf_settings.1_elect_energy_change` | Unmapped | — |
| `self_consistent.scf_iterations.energy` | Mapped | `runschema.calculation.ScfIteration.energy.total` |
| `self_consistent.total_scf_energy.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `self_consistent.total_scf_energy.energy_nuclear_repulsion` | Mapped | `runschema.calculation.Energy.nuclear_repulsion` |
| `self_consistent.total_scf_energy.elec_energy` | Unmapped | — |
| `self_consistent.total_scf_energy.one_elec_energy` | Unmapped | — |
| `self_consistent.total_scf_energy.two_elec_energy` | Unmapped | — |
| `self_consistent.total_scf_energy.potential_energy` | Unmapped | — |
| `self_consistent.total_scf_energy.energy_kinetic_electronic` | Mapped | `runschema.calculation.Energy.kinetic_electronic` |
| `self_consistent.total_scf_energy.energy_exchange` | Mapped | `runschema.calculation.Energy.exchange` |
| `self_consistent.total_scf_energy.energy_correlation` | Mapped | `runschema.calculation.Energy.correlation` |
| `self_consistent.total_scf_energy.energy_XC` | Mapped | `runschema.calculation.Energy.xc` |
| `self_consistent.total_scf_energy.virial_ratio` | Unmapped | — |
| `self_consistent.total_scf_energy.nb_elect_alpha_channel` | Unmapped | — |
| `self_consistent.total_scf_energy.nb_elect_beta_channel` | Unmapped | — |
| `self_consistent.total_scf_energy.nb_elect_total` | Unmapped | — |
| `self_consistent.timings.final_time` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `self_consistent.timings.sum_individual_times` | Unmapped | — |
| `self_consistent.timings.fock_matrix_formation` | Unmapped | — |
| `self_consistent.timings.coulomb_formation` | Unmapped | — |
| `self_consistent.timings.split_rj` | Unmapped | — |
| `self_consistent.timings.xc_integration` | Unmapped | — |
| `self_consistent.timings.basis_fn_evaluation` | Unmapped | — |
| `self_consistent.timings.density_evaluation` | Unmapped | — |
| `self_consistent.timings.xc_functional_evaluation` | Unmapped | — |
| `self_consistent.timings.potential_evaluation` | Unmapped | — |
| `self_consistent.timings.diagonalization` | Unmapped | — |
| `self_consistent.timings.density_matrix_formation` | Unmapped | — |
| `self_consistent.timings.population_analysis` | Unmapped | — |
| `self_consistent.timings.initial_guess` | Unmapped | — |
| `self_consistent.timings.orbital_transformation` | Unmapped | — |
| `self_consistent.timings.orbital_orthonormalization` | Unmapped | — |
| `self_consistent.timings.diis_solution` | Unmapped | — |
| `self_consistent.timings.grid_generation` | Unmapped | — |
| `self_consistent.timings.scf_gradient` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `self_consistent.orbital_energies` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `self_consistent.time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `tddft.absorption_spectrum_electric` | Mapped | `runschema.calculation.Spectra.excitation_energies`<br>`runschema.calculation.Spectra.oscillator_strengths`<br>`runschema.calculation.Spectra.transition_dipole_moments` |
| `mp2.mp2_basis_dimension` | Unmapped | — |
| `mp2.scaling_mp2_energy` | Unmapped | — |
| `mp2.mp2_aux_basis_dimension` | Unmapped | — |
| `mp2.energy_method_current` | Unmapped | — |
| `mp2.energy_total` | Unmapped | — |
| `ci.electronic_structure_method` | Mapped | `runschema.method.Electronic.method` |
| `ci.single_excitations_on_off` | Unmapped | — |
| `ci.orbital_opt_on_off` | Unmapped | — |
| `ci.z_vector_calc_on_off` | Unmapped | — |
| `ci.Brueckner_orbitals_calc_on_off` | Unmapped | — |
| `ci.perturbative_triple_excitations_on_off` | Unmapped | — |
| `ci.f12_correction_on_off` | Unmapped | — |
| `ci.frozen_core_treatment` | Unmapped | — |
| `ci.reference_wave_function` | Unmapped | — |
| `ci.nb_of_atomic_orbitals` | Unmapped | — |
| `ci.nb_of_electrons` | Unmapped | — |
| `ci.nb_of_correlated_electrons` | Unmapped | — |
| `ci.integral_transformation` | Unmapped | — |
| `ci.level_shift_amplitude_update` | Unmapped | — |
| `ci.coulomb_transformation_type` | Unmapped | — |
| `ci.coulomb_transformation_dimension_basis` | Unmapped | — |
| `ci.nb_internal_alpha_mol_orbitals` | Unmapped | — |
| `ci.nb_internal_beta_mol_orbitals` | Unmapped | — |
| `ci.pair_cutoff` | Unmapped | — |
| `ci.atomic_orbital_integral_source` | Unmapped | — |
| `ci.integral_package_used` | Unmapped | — |
| `ci.nb_alpha_pairs_included` | Unmapped | — |
| `ci.nb_beta_pairs_included` | Unmapped | — |
| `ci.mp2_energy_spin_aa` | Unmapped | — |
| `ci.mp2_energy_spin_bb` | Unmapped | — |
| `ci.mp2_energy_spin_ab` | Unmapped | — |
| `ci.mp2_initial_guess` | Unmapped | — |
| `ci.mp2_energy` | Unmapped | — |
| `ci.mp2_total_energy` | Unmapped | — |
| `ci.T_and_T_energy` | Unmapped | — |
| `ci.total_nb_pairs_included` | Unmapped | — |
| `ci.iteration_energy` | Unmapped | — |
| `ci.ccsd_correlation_energy` | Unmapped | — |
| `ci.ccsd_total_energy` | Unmapped | — |
| `ci.single_norm_half_ss` | Unmapped | — |
| `ci.t1_diagnostic` | Unmapped | — |
| `ci.ccsdt_total_triples_correction` | Unmapped | — |
| `ci.ccsdt_aaa_triples_contribution` | Unmapped | — |
| `ci.ccsdt_aab_triples_contribution` | Unmapped | — |
| `ci.ccsdt_aba_triples_contribution` | Unmapped | — |
| `ci.ccsdt_bbb_triples_contribution` | Unmapped | — |
| `ci.ccsdt_final_corr_energy` | Unmapped | — |
| `ci.ccsd_final_energy` | Unmapped | — |
| `ci.energy_total` | Unmapped | — |
| `single_point.cartesian_coordinates` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `single_point.basis_set` | Unmapped | — |
| `single_point.auxiliary_basis_set` | Unmapped | — |
| `single_point.basis_set_statistics` | Unmapped | — |
| `single_point.self_consistent` | Unmapped | — |
| `single_point.tddft` | Unmapped | — |
| `single_point.mp2` | Unmapped | — |
| `single_point.ci` | Unmapped | — |
| `geometry_optimization.energy_change_tol` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference` |
| `geometry_optimization.max_gradient_tol` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum` |
| `geometry_optimization.rms_gradient_tol` | Unmapped | — |
| `geometry_optimization.max_displacement_tol` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum` |
| `geometry_optimization.rms_displacement_tol` | Unmapped | — |
| `geometry_optimization.update_method` | Unmapped | — |
| `geometry_optimization.coords_choice` | Unmapped | — |
| `geometry_optimization.initial_hessian` | Unmapped | — |
| `geometry_optimization.cycle` | Unmapped | — |
| `geometry_optimization.final_energy_evaluation` | Unmapped | — |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `program_svn` | Mapped | `runschema.run.Program.version` |
| `program_compilation_date` | Mapped | `runschema.run.Program.version`<br>`runschema.run.Program.compilation_date` |
| `input_file` | Unmapped | — |
| `input_file.xc_functional` | Mapped | `runschema.method.XCFunctional.exchange`<br>`runschema.method.XCFunctional.correlation`<br>`runschema.method.XCFunctional.hybrid` |
| `input_file.tier` | Mapped | `runschema.method.Scf.native_tier` |
| `single_point` | Unmapped | — |
| `geometry_optimization` | Unmapped | — |

## Psi4 / parser.py

**Summary:** 89 mapped, 41 unmapped quantities (68.46% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atom` | Mapped | `runschema.calculation.Charges.value`<br>`runschema.calculation.Charges.spins`<br>`runschema.calculation.ChargesValue.value` |
| `total` | Mapped | `runschema.calculation.Charges.total` |
| `multipole_moments` | Mapped | `runschema.calculation.Multipoles` |
| `multipole_moments.dipole` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `multipole_moments.quadrupole` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `multipole_moments.octupole` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `multipole_moments.hexadecapole` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `multipole_moments.npole` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `nuclear_dipole_moment` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `electronic_dipole_moment` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `total_dipole_moment` | Mapped | `runschema.calculation.MultipolesEntry.total` |
| `mulliken_charges` | Mapped | `runschema.calculation.Charges` |
| `lowdin_charges` | Mapped | `runschema.calculation.Charges` |
| `geometry` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `geometry.atoms` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `geometry.molecular_point_group` | Unmapped | — |
| `geometry.full_point_group` | Unmapped | — |
| `geometry.symmetry` | Unmapped | — |
| `geometry.rotational_constants` | Unmapped | — |
| `geometry.nuclear_repulsion` | Unmapped | — |
| `geometry.charge` | Unmapped | — |
| `geometry.multiplicity` | Unmapped | — |
| `geometry.electrons` | Unmapped | — |
| `geometry.nalpha` | Unmapped | — |
| `geometry.nbeta` | Unmapped | — |
| `algorithm` | Mapped | `runschema.method.Scf` |
| `algorithm.minimization_algorithm` | Mapped | `runschema.method.Scf.minimization_algorithm` |
| `algorithm.x_psi4_diis` | Unmapped | — |
| `algorithm.x_psi4_mom` | Unmapped | — |
| `algorithm.x_psi4_fractional_occupation` | Unmapped | — |
| `algorithm.x_psi4_guess_type` | Unmapped | — |
| `algorithm.threshold_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `algorithm.threshold_densDFT Potential <==ty_change` | Unmapped | — |
| `algorithm.x_psi4_integral_threshold` | Unmapped | — |
| `basis` | Mapped | `runschema.method.BasisSet`<br>`runschema.method.BasisSetAtomCentered` |
| `basis.basis_set` | Mapped | `runschema.method.BasisSetAtomCentered.name`<br>`runschema.method.BasisSetAtomCentered.n_basis_functions` |
| `jk_matrices` | Unmapped | — |
| `jk_matrices.parameters` | Unmapped | — |
| `auxiliary_basis` | Mapped | `runschema.method.BasisSet`<br>`runschema.method.BasisSetAtomCentered` |
| `auxiliary_basis.basis_set` | Mapped | `runschema.method.BasisSetAtomCentered.name`<br>`runschema.method.BasisSetAtomCentered.n_basis_functions` |
| `dft_potential` | Mapped | `runschema.method.DFT.xc_functional` |
| `dft_potential.composite` | Mapped | `runschema.method.Functional.name`<br>`runschema.method.Functional.parameters` |
| `dft_potential.exact_exchange` | Mapped | `runschema.method.Functional.name`<br>`runschema.method.Functional.weight` |
| `dft_potential.exchange` | Mapped | `runschema.method.Functional.name`<br>`runschema.method.Functional.weight` |
| `dft_potential.correlation` | Mapped | `runschema.method.Functional.name`<br>`runschema.method.Functional.weight` |
| `dft_potential.hybrid` | Mapped | `runschema.method.Functional.name`<br>`runschema.method.Functional.weight` |
| `dft_potential.molecular_quadrature` | Unmapped | — |
| `method` | Mapped | `runschema.method.Electronic.method` |
| `iterations` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `iterations.iteration` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.change` |
| `spin_contamination_metric` | Unmapped | — |
| `s2_expected` | Unmapped | — |
| `s2_observed` | Mapped | `runschema.calculation.Calculation.spin_S2` |
| `s_expected` | Unmapped | — |
| `s_observed` | Unmapped | — |
| `orbital_energies` | Mapped | `runschema.calculation.BandEnergies.orbital_labels`<br>`runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `properties` | Mapped | `runschema.calculation.Multipoles`<br>`runschema.calculation.Charges` |
| `total_gradient` | Mapped | `runschema.calculation.Forces.total` |
| `method` | Mapped | `runschema.method.Electronic.method` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `parameters` | Unmapped | — |
| `parameters.key_value` | Unmapped | — |
| `iterations` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `iterations.iteration` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.change` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `root_info` | Unmapped | — |
| `root_info.root_energy` | Unmapped | — |
| `properties` | Mapped | `runschema.calculation.Multipoles`<br>`runschema.calculation.Charges` |
| `iterations` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `iterations.iteration` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.change` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `orbital_energies` | Mapped | `runschema.calculation.BandEnergies.orbital_labels`<br>`runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `parameters` | Unmapped | — |
| `parameters.key_value` | Unmapped | — |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `parameters` | Unmapped | — |
| `parameters.key_value` | Unmapped | — |
| `iterations` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `iterations.iteration` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.change` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `parameters` | Unmapped | — |
| `parameters.key_value` | Unmapped | — |
| `iterations` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `iterations.iteration` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.change` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `parameters` | Unmapped | — |
| `parameters.key_value` | Unmapped | — |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.key_value` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.EnergyEntry` |
| `properties` | Mapped | `runschema.calculation.Multipoles`<br>`runschema.calculation.Charges` |
| `geometry` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `geometry.atoms` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `geometry.forces` | Mapped | `runschema.calculation.Forces.total` |
| `convergence_criteria` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.change` |
| `scf` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `scf_grad` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `mp` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `ci` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `mcscf_detci` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `mcscf` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `cc` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `cc_energy` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `cc_lambda` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `cc_density` | Mapped | `runschema.system.System`<br>`runschema.method.Method`<br>`runschema.calculation.Calculation` |
| `optking` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |
| `options` | Unmapped | — |
| `salc` | Mapped | `runschema.calculation.Forces.total`<br>`runschema.calculation.Forces.contributions` |
| `salc.total_gradient` | Mapped | `runschema.calculation.Forces.total` |
| `salc.contributions_gradient` | Mapped | `runschema.calculation.Forces.contributions` |
| `salc.contributions_gradient.name` | Mapped | `runschema.calculation.ForcesEntry.kind` |
| `salc.contributions_gradient.value` | Mapped | `runschema.calculation.ForcesEntry.value` |
| `module_time` | Mapped | `runschema.calculation.Calculation.time_calculation` |
| `total_time` | Mapped | `runschema.calculation.Calculation.time_physical` |
| `version` | Mapped | `runschema.run.Program.version` |
| `start_time` | Mapped | `runschema.run.TimeRun.date_start` |
| `process_id` | Unmapped | — |
| `psidatadir` | Unmapped | — |
| `memory` | Unmapped | — |
| `threads` | Unmapped | — |
| `input_file` | Unmapped | — |
| `module` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |

## Qball / mainfile_parser

**Summary:** 2 mapped, 1 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `atoms` | Unmapped | — |
| `start_time` | Mapped | `runschema.run.Run.time_run.TimeRun.date_start` |
| `end_time` | Mapped | `runschema.run.Run.time_run.TimeRun.date_end` |

## Qbox / parser.py

**Summary:** 28 mapped, 20 unmapped quantities (58.33% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `run.parameter` | Mapped | `runschema.method.Method.dft.xc_functional`<br>`runschema.method.Method.x_qbox_input_parameters` |
| `run.species` | Unmapped | — |
| `run.species.symbol` | Unmapped | — |
| `run.species.atomic_numer` | Unmapped | — |
| `run.species.mass` | Unmapped | — |
| `run.iteration` | Mapped | `runschema.calculation.Calculation`<br>`runschema.system.System` |
| `run.iteration.charge` | Unmapped | — |
| `run.iteration.energy_kinetic_electronic` | Mapped | `runschema.calculation.Energy.kinetic_electronic` |
| `run.iteration.energy_x_qbox_conf` | Unmapped | — |
| `run.iteration.energy_x_qbox_ps` | Unmapped | — |
| `run.iteration.energy_x_qbox_nl` | Unmapped | — |
| `run.iteration.energy_coulomb` | Mapped | `runschema.calculation.Energy.coulomb` |
| `run.iteration.energy_xc` | Mapped | `runschema.calculation.Energy.xc` |
| `run.iteration.energy_x_qbox_sr` | Unmapped | — |
| `run.iteration.energy_x_qbox_self` | Unmapped | — |
| `run.iteration.energy_x_qbox_ts` | Unmapped | — |
| `run.iteration.energy_x_qbox_exf` | Unmapped | — |
| `run.iteration.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `run.iteration.energy_x_qbox_pv` | Unmapped | — |
| `run.iteration.energy_x_qbox_efield` | Unmapped | — |
| `run.iteration.energy_x_qbox_enthalpy` | Unmapped | — |
| `run.iteration.stress_tensor` | Mapped | `runschema.calculation.Stress` |
| `run.iteration.stress_tensor.contribution` | Mapped | `runschema.calculation.Stress.total`<br>`runschema.calculation.Stress.contributions` |
| `run.iteration.stress_tensor.contribution.kind` | Mapped | `runschema.calculation.StressEntry.kind` |
| `run.iteration.stress_tensor.contribution.value` | Mapped | `runschema.calculation.StressEntry.value` |
| `run.iteration.multipole` | Mapped | `runschema.calculation.Multipoles` |
| `run.iteration.multipole.dipole` | Mapped | `runschema.calculation.Multipoles.dipole` |
| `run.iteration.multipole.quadrupole` | Mapped | `runschema.calculation.Multipoles.quadrupole` |
| `run.iteration.mlwf` | Unmapped | — |
| `run.iteration.mlwf.center` | Unmapped | — |
| `run.iteration.scf` | Mapped | `runschema.calculation.ScfIteration` |
| `run.iteration.scf.charge` | Unmapped | — |
| `run.iteration.scf.energy_sum_eigenvalues` | Mapped | `runschema.calculation.Energy.sum_eigenvalues` |
| `run.iteration.scf.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `run.iteration.atomset` | Mapped | `runschema.system.Atoms` |
| `run.iteration.atomset.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `run.iteration.atomset.atom` | Mapped | `runschema.system.Atoms` |
| `run.iteration.atomset.atom.label` | Mapped | `runschema.system.Atoms.labels` |
| `run.iteration.atomset.atom.position` | Mapped | `runschema.system.Atoms.positions` |
| `run.iteration.atomset.atom.velocity` | Mapped | `runschema.system.Atoms.velocities` |
| `run.iteration.atomset.atom.force` | Mapped | `runschema.calculation.Forces.total` |
| `run.iteration.time_calculation` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `start_time` | Mapped | `runschema.run.TimeRun.date_start` |
| `end_time` | Mapped | `runschema.run.TimeRun.date_end` |
| `x_qbox_nodename` | Unmapped | — |
| `x_qbox_loading_xml_file` | Unmapped | — |
| `run` | Mapped | `runschema.run.Run` |

## Quantum ESPRESSO / QuantumEspressoOutParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `run` | Mapped | `runschema.run.Run` |

## Quantum ESPRESSO / QuantumEspressoRunParser

**Summary:** 53 mapped, 121 unmapped quantities (30.46% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_name_version` | Mapped | `runschema.run.Run.program.version` |
| `start_date_time` | Mapped | `runschema.run.Run.time_run.date_start` |
| `compile_parallel_version` | Unmapped | — |
| `nthreads` | Unmapped | — |
| `nproc` | Unmapped | — |
| `npool` | Unmapped | — |
| `input_filename` | Unmapped | — |
| `ntypx` | Unmapped | — |
| `npk` | Unmapped | — |
| `lmaxx` | Unmapped | — |
| `nchix` | Unmapped | — |
| `ndmx` | Unmapped | — |
| `nbrx` | Unmapped | — |
| `input_positions_cell_dirname` | Unmapped | — |
| `header` | Mapped | `runschema.method.Method`<br>`runschema.system.System` |
| `header.supercell` | Unmapped | — |
| `header.pseudopotential_report` | Unmapped | — |
| `header.pseudopotential_report.species` | Unmapped | — |
| `header.pseudopotential_report.version` | Unmapped | — |
| `header.pseudopotential_report.contents` | Unmapped | — |
| `header.renormalized_wavefunction` | Unmapped | — |
| `header.dispersion` | Unmapped | — |
| `header.atom_radii` | Unmapped | — |
| `header.x_qe_xc_functional_user_enforced` | Unmapped | — |
| `header.x_qe_gamma_algorithms` | Unmapped | — |
| `header.x_qe_diagonalization_algorithm` | Unmapped | — |
| `header.g_vector_sticks` | Unmapped | — |
| `header.x_qe_ibrav` | Unmapped | — |
| `header.alat` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.calculation.BandEnergies.kpoints` |
| `header.x_qe_cell_volume` | Unmapped | — |
| `header.number_of_atoms` | Unmapped | — |
| `header.x_qe_number_of_species` | Unmapped | — |
| `header.number_of_electrons` | Mapped | `runschema.method.Electronic.n_electrons` |
| `header.number_of_electrons.total` | Mapped | `runschema.method.Electronic.n_electrons` |
| `header.number_of_electrons.up` | Mapped | `runschema.method.Electronic.n_electrons` |
| `header.number_of_electrons.down` | Mapped | `runschema.method.Electronic.n_electrons` |
| `header.x_qe_number_of_states` | Unmapped | — |
| `header.wavefunction_cutoff` | Mapped | `runschema.method.BasisSet.cutoff` |
| `header.density_cutoff` | Mapped | `runschema.method.BasisSet.cutoff` |
| `header.fock_cutoff` | Unmapped | — |
| `header.scf_threshold_energy_change` | Mapped | `runschema.method.Scf.threshold_energy_change` |
| `header.x_qe_potential_mixing_beta` | Unmapped | — |
| `header.mixing_scheme` | Unmapped | — |
| `header.xc_functional` | Mapped | `runschema.method.DFT.xc_functional` |
| `header.x_qe_exact_exchange_fraction` | Mapped | `runschema.method.DFT.xc_functional` |
| `header.x_qe_md_max_steps` | Unmapped | — |
| `header.spin_orbit_mode` | Unmapped | — |
| `header.berry_efield` | Unmapped | — |
| `header.berry_efield.direction` | Unmapped | — |
| `header.berry_efield.intensity` | Unmapped | — |
| `header.berry_efield.strings` | Unmapped | — |
| `header.berry_efield.niter` | Unmapped | — |
| `header.assume_isolated` | Unmapped | — |
| `header.x_qe_celldm` | Unmapped | — |
| `header.units` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `header.simulation_cell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `header.reciprocal_cell_units` | Unmapped | — |
| `header.reciprocal_cell` | Unmapped | — |
| `header.pseudopotential` | Mapped | `runschema.method.Method.atom_parameters` |
| `header.pseudopotential.idx` | Unmapped | — |
| `header.pseudopotential.label` | Unmapped | — |
| `header.pseudopotential.filename` | Unmapped | — |
| `header.pseudopotential.md5sum` | Unmapped | — |
| `header.pseudopotential.type` | Unmapped | — |
| `header.pseudopotential.valence` | Unmapped | — |
| `header.pseudopotential.comment` | Unmapped | — |
| `header.pseudopotential.integral_ndirections` | Unmapped | — |
| `header.pseudopotential.integral_lmax_exact` | Unmapped | — |
| `header.pseudopotential.augmentation_shape` | Unmapped | — |
| `header.pseudopotential.ndmx` | Unmapped | — |
| `header.pseudopotential.nbeta` | Unmapped | — |
| `header.pseudopotential.beta` | Unmapped | — |
| `header.pseudopotential.ncoefficients` | Unmapped | — |
| `header.pseudopotential.rinner` | Unmapped | — |
| `header.atom_species_pp` | Mapped | `runschema.method.AtomParameters.label`<br>`runschema.method.AtomParameters.n_valence_electrons` |
| `header.starting_magnetization` | Mapped | `runschema.method.Electronic.n_spin_channels` |
| `header.x_qe_md_cell_mass` | Unmapped | — |
| `header.symmetry` | Unmapped | — |
| `header.symmetry.nsymm` | Unmapped | — |
| `header.symmetry.symm_inversion` | Unmapped | — |
| `header.symmetry.nsymm_with_fractional_translation` | Unmapped | — |
| `header.symmetry.nsymm_ignored` | Unmapped | — |
| `header.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `header.labels_positions.axes` | Unmapped | — |
| `header.labels_positions.units` | Mapped | `runschema.system.Atoms.positions` |
| `header.labels_positions.labels` | Mapped | `runschema.system.Atoms.labels` |
| `header.labels_positions.positions` | Mapped | `runschema.system.Atoms.positions` |
| `header.k_points` | Mapped | `runschema.method.KMesh.n_points`<br>`runschema.method.KMesh.points`<br>`runschema.method.Smearing.kind` |
| `header.k_points.nk` | Mapped | `runschema.method.KMesh.n_points` |
| `header.k_points.smearing` | Mapped | `runschema.method.Smearing.kind` |
| `header.k_points.width` | Mapped | `runschema.method.Smearing.width` |
| `header.k_points.units` | Unmapped | — |
| `header.k_points.ik` | Unmapped | — |
| `header.k_points.points` | Mapped | `runschema.method.KMesh.points` |
| `header.k_points.wk` | Unmapped | — |
| `header.k_points.warning` | Unmapped | — |
| `header.dense_grid` | Unmapped | — |
| `header.smooth_grid` | Unmapped | — |
| `header.x_qe_core_charge_realspace` | Unmapped | — |
| `header.input_occupation` | Unmapped | — |
| `header.allocated_arrays` | Unmapped | — |
| `header.temporary_arrays` | Unmapped | — |
| `header.martyna_tuckerman_parameters` | Unmapped | — |
| `header.core_charge_check` | Unmapped | — |
| `header.x_qe_input_potential_recalculated_file` | Unmapped | — |
| `header.x_qe_starting_density_file` | Unmapped | — |
| `header.x_qe_starting_potential` | Unmapped | — |
| `header.x_qe_starting_charge_negative` | Unmapped | — |
| `header.starting_charge_negative_spin` | Unmapped | — |
| `header.initial_charge` | Unmapped | — |
| `header.x_qe_starting_wfc` | Unmapped | — |
| `header.x_qe_time_setup_cpu1_end` | Unmapped | — |
| `header.x_qe_per_process_mem` | Unmapped | — |
| `self_consistent` | Mapped | `runschema.run.Run.calculation`<br>`runschema.run.Run.system` |
| `self_consistent.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistent.iteration.number` | Unmapped | — |
| `self_consistent.iteration.ecutwfc` | Unmapped | — |
| `self_consistent.iteration.beta` | Unmapped | — |
| `self_consistent.iteration.negative_rho` | Unmapped | — |
| `self_consistent.iteration.magnetic_moments` | Unmapped | — |
| `self_consistent.iteration.energies` | Mapped | `runschema.calculation.ScfIteration.energy.total` |
| `self_consistent.iteration.magnetization_total` | Unmapped | — |
| `self_consistent.iteration.magnetization_absolute` | Unmapped | — |
| `self_consistent.iteration.total_time` | Mapped | `runschema.calculation.ScfIteration.time_physical`<br>`runschema.calculation.ScfIteration.time_calculation` |
| `self_consistent.iteration.diagonalization_algorithm` | Unmapped | — |
| `self_consistent.iteration.diagonalization_ethr` | Unmapped | — |
| `self_consistent.iteration.diagonalization_iteration_avg` | Unmapped | — |
| `self_consistent.iteration.diagonalization_c_bands_n_unconverged_eigenvalues` | Unmapped | — |
| `self_consistent.spin_pol` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `self_consistent.k_points` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `self_consistent.number_of_planewaves` | Unmapped | — |
| `self_consistent.band_energies` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `self_consistent.occupation_numbers` | Mapped | `runschema.calculation.BandEnergies.occupations` |
| `self_consistent.homo_lumo` | Mapped | `runschema.calculation.Energy.highest_occupied`<br>`runschema.calculation.Energy.lowest_unoccupied` |
| `self_consistent.fermi_energy` | Mapped | `runschema.calculation.Energy.fermi` |
| `self_consistent.energies` | Mapped | `runschema.calculation.Energy.total` |
| `self_consistent.energies.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `self_consistent.energies.x_qe_energy_total_harris_foulkes_estimate` | Unmapped | — |
| `self_consistent.energies.x_qe_energy_total_accuracy_estimate` | Unmapped | — |
| `self_consistent.energies.x_qe_energy_total_paw_all_electron` | Unmapped | — |
| `self_consistent.energy_contributions` | Unmapped | — |
| `self_consistent.magnetization_total` | Unmapped | — |
| `self_consistent.magnetization_absolute` | Unmapped | — |
| `self_consistent.convergence_iterations` | Unmapped | — |
| `self_consistent.forces` | Mapped | `runschema.calculation.Calculation.forces` |
| `self_consistent.total_force` | Unmapped | — |
| `self_consistent.forces_dispersion` | Unmapped | — |
| `self_consistent.total_force_dispersion` | Unmapped | — |
| `self_consistent.stress` | Mapped | `runschema.calculation.Calculation.stress`<br>`runschema.calculation.Thermodynamics.pressure` |
| `self_consistent.units` | Mapped | `runschema.system.Atoms.positions` |
| `self_consistent.simulation_cell` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `self_consistent.reciprocal_cell_units` | Unmapped | — |
| `self_consistent.reciprocal_cell` | Unmapped | — |
| `self_consistent.labels_positions` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `self_consistent.starting_magnetization` | Unmapped | — |
| `self_consistent.exx_refine` | Unmapped | — |
| `self_consistent.memory` | Unmapped | — |
| `self_consistent.output_datafile` | Unmapped | — |
| `self_consistent.negative_rho` | Unmapped | — |
| `self_consistent.total_time` | Mapped | `runschema.calculation.Calculation.time_physical`<br>`runschema.calculation.Calculation.time_calculation` |
| `bandstructure` | Mapped | `runschema.run.Run.calculation`<br>`runschema.run.Run.system` |
| `bfgs_geometry_optimization` | Mapped | `runschema.run.Run.calculation`<br>`runschema.run.Run.system` |
| `bfgs_geometry_optimization.final_energy` | Unmapped | — |
| `bfgs_geometry_optimization.convergence` | Unmapped | — |
| `bfgs_geometry_optimization.dynamics` | Unmapped | — |
| `molecular_dynamics` | Mapped | `runschema.run.Run.calculation`<br>`runschema.run.Run.system` |
| `molecular_dynamics.diffusion_coefficients` | Unmapped | — |
| `molecular_dynamics.diffusion_coefficient_mean` | Unmapped | — |
| `damped_dynamics` | Mapped | `runschema.run.Run.calculation`<br>`runschema.run.Run.system` |
| `langevin_dynamics` | Mapped | `runschema.run.Run.calculation`<br>`runschema.run.Run.system` |
| `vcs_wentzcovitch_damped_minimization` | Mapped | `runschema.run.Run.calculation`<br>`runschema.run.Run.system` |
| `profiling` | Unmapped | — |
| `end_date_time` | Mapped | `runschema.run.Run.time_run.date_end` |
| `job_done` | Mapped | `runschema.run.Run.clean_end` |

# SIESTA Parser — Mapping Report

## SIESTA / FDFParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameter` | Mapped | `runschema.method.Method.dft.xc_functional.exchange.name`<br>`runschema.method.Method.dft.xc_functional.correlation.name`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.lattice_vectors` |
| `block` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions`<br>`runschema.system.Atoms.lattice_vectors` |

## SIESTA / OutParser

**Summary:** 32 mapped, 8 unmapped quantities (80.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `coordinates_format` | Mapped | `runschema.system.Atoms.positions` |
| `labels` | Mapped | `runschema.system.Atoms.labels` |
| `species` | Mapped | `runschema.system.Atoms.labels` |
| `positions` | Mapped | `runschema.system.Atoms.positions` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `atoms` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `atoms` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.free`<br>`runschema.calculation.Energy.xc`<br>`runschema.calculation.Energy.sum_eigenvalues`<br>`runschema.calculation.Energy.electrostatic`<br>`runschema.calculation.Energy.nuclear_repulsion`<br>`runschema.calculation.Energy.contributions` |
| `energy.contribution` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `scf` | Mapped | `runschema.calculation.ScfIteration.energy` |
| `scf.step` | Mapped | `runschema.calculation.ScfIteration.energy.total`<br>`runschema.calculation.ScfIteration.energy.free`<br>`runschema.calculation.ScfIteration.energy.fermi`<br>`runschema.calculation.ScfIteration.energy.types` |
| `energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `energy` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `energy.contribution` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.contributions` |
| `forces` | Mapped | `runschema.calculation.Forces.total` |
| `forces.atomic` | Mapped | `runschema.calculation.Forces.total.value` |
| `stress_tensor` | Mapped | `runschema.calculation.Stress.total.value` |
| `stress_tensor` | Mapped | `runschema.calculation.Stress.total.value` |
| `electric_dipole` | Mapped | `runschema.calculation.Multipoles.dipole.total` |
| `mulliken` | Mapped | `runschema.calculation.Charges.value`<br>`runschema.calculation.Charges.total`<br>`runschema.calculation.Charges.analysis_method` |
| `mulliken.atom` | Mapped | `runschema.calculation.Charges.orbital_projected`<br>`runschema.calculation.Charges.spin_projected` |
| `mulliken.atom.label` | Mapped | `runschema.calculation.ChargesValue.atom_label` |
| `mulliken.atom.orbital` | Mapped | `runschema.calculation.ChargesValue.orbital` |
| `mulliken.atom.values` | Mapped | `runschema.calculation.ChargesValue.value`<br>`runschema.calculation.Charges.value` |
| `mulliken.spin` | Mapped | `runschema.calculation.ChargesValue.spin` |
| `mulliken.q_tot` | Unmapped | — |
| `header` | Mapped | `runschema.run.Program.version` |
| `header.program_version` | Mapped | `runschema.run.Program.version` |
| `header.x_siesta_arch` | Unmapped | — |
| `header.x_siesta_compiler_flags` | Unmapped | — |
| `header.x_siesta_parallel` | Unmapped | — |
| `input_data_file` | Unmapped | — |
| `simulation_parameters` | Unmapped | — |
| `simulation_parameters.redata` | Unmapped | — |
| `x_siesta_n_nodes` | Unmapped | — |
| `run_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `run_end` | Mapped | `runschema.run.TimeRun.date_end` |
| `single_point` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |
| `geometry_optimization` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |
| `geometry_optimization.step` | Mapped | `runschema.system.System`<br>`runschema.calculation.Calculation` |

## solid_dmft

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## TBStudio

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

The `TBStudioParser` class reads a JSON `.tbm` file directly via `json.load` and populates the archive through hand-written `parse_system`, `parse_method`, and `parse_scc` methods. It declares no `TextParser`/`XMLParser`/`FileParser` subclass with `Quantity(...)` definitions, so there are no file-parser quantities to report.

# TURBOMOLE legacy parser — mapping report

The TURBOMOLE parser defines three declarative file-parser classes that declare
`Quantity(...)` lists: `EigenvaluesParser`, `ControlParser` and `OutParser`.
`AuxiliaryOutParser` is a `FileParser` subclass with a custom `matrix` reader and
declares no `Quantity`, so it is reported without a table. Nested `sub_parser`
quantities are listed with dotted paths reflecting their container. The
`module_quantities` block is shared by every `module_*` sub-parser (its members
are declared once and reused by list concatenation); it is listed once, followed
by the module-specific extensions under their respective module prefix
(`aoforce.`, `ccsdf12.`, `dscf.`, `escf.`, `freeh.`, `pnoccsd.`, `ricc2.`,
`ridft.`, `rirpa.`, `statpt.`). Status is Mapped only when `parse()` writes the
quantity into the normalized run schema; quantities written solely to
code-specific `x_turbomole_*` targets are Unmapped.

## TURBOMOLE / AuxiliaryOutParser

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## TURBOMOLE / EigenvaluesParser

**Summary:** 2 mapped, 1 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `irrep` | Unmapped | — |
| `eigenvalues` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `occupation` | Mapped | `runschema.calculation.BandEnergies.occupations` |

## TURBOMOLE / ControlParser

**Summary:** 0 mapped, 9 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `operating_system` | Unmapped | — |
| `scf_iter_limit` | Unmapped | — |
| `scf_conv` | Unmapped | — |
| `time_for_integral_calc` | Unmapped | — |
| `pople_kind` | Unmapped | — |
| `damping_parameter` | Unmapped | — |
| `scfint` | Unmapped | — |
| `interconversion_status` | Unmapped | — |
| `drvopt` | Unmapped | — |

## TURBOMOLE / OutParser

**Summary:** 68 mapped, 23 unmapped quantities (74.73% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `scf_quantities.iteration.damping_scf_iteration` | Unmapped | — |
| `scf_quantities.iteration.energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.ScfIteration.x_turbomole_energy_1electron_scf_iteration`<br>`runschema.calculation.ScfIteration.x_turbomole_energy_2electron_scf_iteration` |
| `scf_quantities.iteration.energy_XC` | Mapped | `runschema.calculation.Energy.xc` |
| `scf_quantities.iteration.norm_diis_scf_iteration` | Unmapped | — |
| `scf_quantities.iteration.norm_fia` | Unmapped | — |
| `scf_quantities.iteration.norm_fock` | Unmapped | — |
| `scf_quantities.iteration.delta_eigenvalues` | Unmapped | — |
| `scf_quantities.iteration.fon` | Unmapped | — |
| `self_consistency.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistency.iteration` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistency.number_of_scf_iterations` | Mapped | `runschema.calculation.Calculation.n_scf_iterations` |
| `atomic_info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels`<br>`runschema.method.AtomParameters.label` |
| `atomic_info.info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `atomic_info.center_of_nuclear_mass` | Unmapped | — |
| `atomic_info.center_of_nuclear_charge` | Unmapped | — |
| `basis_set_info` | Mapped | `runschema.method.Method.electrons_representation` |
| `basis_set_info.auxiliary` | Mapped | `runschema.method.BasisSetContainer.scope` |
| `basis_set_info.spherical` | Mapped | `runschema.method.BasisSetAtomCentered.n_basis_functions` |
| `basis_set_info.atom` | Mapped | `runschema.method.BasisSetAtomCentered.name`<br>`runschema.method.BasisSetAtomCentered.atom_number`<br>`runschema.method.BasisSetAtomCentered.n_basis_functions` |
| `basis_set_info.total` | Unmapped | — |
| `mo_occupation` | Unmapped | — |
| `wavefunction_model` | Mapped | `runschema.method.Electronic.method` |
| `dft_functional` | Mapped | `runschema.method.Functional.name` |
| `dft_functional.functional` | Mapped | `runschema.method.Functional.name` |
| `dft_functional.exchange` | Unmapped | — |
| `dft_functional.correlation` | Unmapped | — |
| `embedding_point_charges` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `embedding_point_charges.pceem_max_multipole` | Unmapped | — |
| `embedding_point_charges.pceem_multipole_precision` | Unmapped | — |
| `embedding_point_charges.pceem_min_separation_cells` | Unmapped | — |
| `embedding_point_charges.lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `embedding_point_charges.redefined` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `embedding_point_charges.pc_cluster` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `embedding_point_charges.qm_cluster` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `dft_d3` | Mapped | `runschema.method.Electronic.van_der_waals_method`<br>`runschema.calculation.Energy.van_der_waals` |
| `dft_d3.version` | Mapped | `runschema.method.Electronic.van_der_waals_method` |
| `dft_d3.energy_van_der_Waals` | Mapped | `runschema.calculation.Energy.van_der_waals` |
| `uhf` | Mapped | `runschema.method.Electronic.n_spin_channels` |
| `smearing` | Mapped | `runschema.method.Smearing.kind`<br>`runschema.method.Smearing.width` |
| `smearing.kind` | Mapped | `runschema.method.Smearing.kind` |
| `smearing.width` | Mapped | `runschema.method.Smearing.width` |
| `energy_reference_wavefunction` | Unmapped | — |
| `energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.kinetic` |
| `self_consistency` | Mapped | `runschema.calculation.Calculation.scf_iteration` |
| `self_consistency.iteration (CCSD)` | Unmapped | — |
| `self_consistency.convergence` | Unmapped | — |
| `energies_MP2` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `energies_CCSD` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `energies_CCSD(T0)` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `energy_gradient` | Mapped | `runschema.calculation.Forces.total` |
| `eigenvalue_file` | Mapped | `runschema.calculation.BandEnergies.energies`<br>`runschema.calculation.BandEnergies.occupations` |
| `wall_time` | Mapped | `runschema.calculation.Calculation.time_calculation`<br>`runschema.calculation.Calculation.time_physical` |
| `aoforce.hessian` | Mapped | `runschema.calculation.Calculation.hessian_matrix` |
| `aoforce.hessian_file` | Mapped | `runschema.calculation.Calculation.hessian_matrix` |
| `aoforce.normal_modes_vibrational_frequencies` | Unmapped | — |
| `aoforce.normal_modes_file` | Unmapped | — |
| `aoforce.vibrational_spectrum_file` | Unmapped | — |
| `aoforce.energy_zero_point` | Mapped | `runschema.calculation.Energy.zero_point` |
| `aoforce.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `aoforce.energy_current` | Mapped | `runschema.calculation.Energy.current` |
| `ccsdf12.energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `dscf.self_consistency` | Mapped | `runschema.calculation.Calculation.scf_iteration`<br>`runschema.calculation.Calculation.n_scf_iterations` |
| `escf.gw` | Mapped | `runschema.calculation.BandEnergies.value_ks`<br>`runschema.method.Electronic.n_spin_channels` |
| `escf.gw.parameters` | Mapped | `runschema.method.Electronic.n_spin_channels` |
| `escf.gw.qp_states` | Mapped | `runschema.calculation.BandEnergies.value_ks`<br>`runschema.calculation.BandEnergies.value_qp`<br>`runschema.calculation.BandEnergies.value_ks_xc` |
| `freeh.thermodynamics` | Mapped | `runschema.calculation.Thermodynamics.temperature`<br>`runschema.calculation.Thermodynamics.pressure`<br>`runschema.calculation.Energy.correction_entropy` |
| `freeh.energy_zero_point` | Mapped | `runschema.calculation.Energy.zero_point` |
| `pnoccsd.methods` | Mapped | `runschema.method.Electronic.method` |
| `pnoccsd.energies` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `ricc2.energy_total` | Mapped | `runschema.calculation.Energy.total` |
| `ridft.self_consistency` | Mapped | `runschema.calculation.Calculation.scf_iteration`<br>`runschema.calculation.Calculation.n_scf_iterations` |
| `rirpa.energies_RPA` | Mapped | `runschema.calculation.Energy.total`<br>`runschema.calculation.Energy.current` |
| `statpt.atomic_info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `statpt.atomic_info.info` | Mapped | `runschema.system.Atoms.positions`<br>`runschema.system.Atoms.labels` |
| `statpt.options` | Mapped | `simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_energy_difference`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_force_maximum`<br>`simulationworkflowschema.GeometryOptimizationMethod.convergence_tolerance_displacement_maximum` |
| `statpt.convergence` | Unmapped | — |
| `x_turbomole_nodename` | Unmapped | — |
| `program_version` | Mapped | `runschema.run.Program.version` |
| `time` | Mapped | `runschema.run.TimeRun.date_start`<br>`runschema.run.TimeRun.date_end` |
| `module_aoforce` | Mapped | `runschema.run.Run.calculation` |
| `module_ccsdf12` | Mapped | `runschema.run.Run.calculation` |
| `module_dscf` | Mapped | `runschema.run.Run.calculation` |
| `module_escf` | Mapped | `runschema.run.Run.calculation` |
| `module_freeh` | Mapped | `runschema.run.Run.calculation` |
| `module_grad` | Mapped | `runschema.run.Run.calculation` |
| `module_pnoccsd` | Mapped | `runschema.run.Run.calculation` |
| `module_ricc2` | Mapped | `runschema.run.Run.calculation` |
| `module_ridft` | Mapped | `runschema.run.Run.calculation` |
| `module_rirpa` | Mapped | `runschema.run.Run.calculation` |
| `module_statpt` | Mapped | `runschema.run.Run.calculation` |
| `module_run` | Mapped | `runschema.run.Run.system`<br>`runschema.run.Run.method`<br>`runschema.run.Run.calculation` |

## VASP / vasprun.xml

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

The `vasprun.xml` content is read by `RunFileParser`, which subclasses `nomad.parsing.file_parser.FileParser` and drives a custom `xml.sax` handler (`RunXmlContentHandler`). It declares no `Quantity(...)` objects; `RunContentParser` addresses the parsed tree by XPath-like string keys rather than named quantities, so there is no declarative quantity list to report.

## VASP / OUTCAR

**Summary:** 26 mapped, 3 unmapped quantities (89.66% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `calculation` | Mapped | `calculation` |
| `calculation.scf_iteration` | Mapped | `calculation.scf_iteration` |
| `calculation.scf_iteration.energy_total` | Mapped | `calculation.scf_iteration.energy.free` |
| `calculation.scf_iteration.energy_entropy0` | Mapped | `calculation.scf_iteration.energy.total` |
| `calculation.scf_iteration.energy_T0` | Mapped | `calculation.scf_iteration.energy.total_t0` |
| `calculation.scf_iteration.energy_components` | Mapped | `calculation.scf_iteration.energy.correction_hartree`<br>`calculation.scf_iteration.energy.xc`<br>`calculation.scf_iteration.energy.exchange`<br>`calculation.scf_iteration.energy.sum_eigenvalues` |
| `calculation.scf_iteration.time` | Mapped | `calculation.scf_iteration.time_calculation`<br>`calculation.scf_iteration.time_physical` |
| `calculation.energies` | Mapped | `calculation.energy` |
| `calculation.energies.energy_total` | Mapped | `calculation.energy.free` |
| `calculation.energies.energy_entropy0` | Mapped | `calculation.energy.total` |
| `calculation.energies.energy_T0` | Mapped | `calculation.energy.total_t0` |
| `calculation.stress` | Mapped | `calculation.stress.total` |
| `calculation.positions_forces` | Mapped | `calculation.forces.total`<br>`system.atoms.positions` |
| `calculation.lattice_vectors` | Mapped | `system.atoms.lattice_vectors` |
| `calculation.converged` | Unmapped | — |
| `calculation.fermi_energy` | Unmapped | — |
| `calculation.eigenvalues` | Mapped | `calculation.eigenvalues`<br>`calculation.band_structure_electronic` |
| `calculation.convergence` | Mapped | `calculation.single_configuration_calculation_converged` |
| `calculation.time` | Mapped | `calculation.time_calculation`<br>`calculation.time_physical` |
| `header` | Mapped | `run.program.version`<br>`run.program.name`<br>`run.time_run.date_start`<br>`run.program.compilation_datetime` |
| `parameters` | Mapped | `method.electrons_representation.basis_set.cutoff`<br>`method.electrons_representation.native_tier` |
| `ions_per_type` | Mapped | `system.atoms.labels`<br>`method.atom_parameters` |
| `species` | Mapped | `method.atom_parameters.label`<br>`method.atom_parameters.atom_number` |
| `kpoints` | Mapped | `method.k_mesh.points`<br>`method.k_mesh.weights` |
| `nbands` | Unmapped | — |
| `lattice_vectors` | Mapped | `system.atoms.lattice_vectors` |
| `positions` | Mapped | `system.atoms.positions` |
| `response_functions` | Mapped | `method.gw.type`<br>`method.frequency_mesh` |
| `response_functions.input_parameters` | Mapped | `method.gw.type`<br>`method.frequency_mesh` |

## VASP / POTCAR

**Summary:** 4 mapped, 0 unmapped quantities (100.00% coverage).

The `PotParser` (`TextParser`) reads pseudopotential headers from `POTCAR` (or, via `OutcarContentParser`, from `OUTCAR`). Its output is consumed in `parse_method`, populating the `Pseudopotential` and `AtomParameters` sections.

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `pseudopotential` | Mapped | `method.atom_parameters.pseudopotential` |
| `pseudopotential.title` | Mapped | `method.atom_parameters.pseudopotential.name`<br>`method.atom_parameters.pseudopotential.xc_functional_name` |
| `pseudopotential.flag` | Mapped | `method.atom_parameters.pseudopotential.type` |
| `pseudopotential.number` | Mapped | `method.atom_parameters.pseudopotential.cutoff`<br>`method.atom_parameters.mass`<br>`method.atom_parameters.n_valence_electrons` |

## w2dynamics / parser.py

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `program_version` | Mapped | `runschema.run.Program.version` |

## Wannier90 / WOutParser

**Summary:** 20 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `version` | Mapped | `runschema.run.Program.version` |
| `lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors` |
| `reciprocal_lattice_vectors` | Mapped | `runschema.system.Atoms.lattice_vectors_reciprocal`<br>`runschema.calculation.BandStructure.reciprocal_cell` |
| `structure` | Mapped | `runschema.system.Atoms.labels`<br>`runschema.system.Atoms.positions` |
| `structure.labels` | Mapped | `runschema.system.Atoms.labels` |
| `structure.positions` | Mapped | `runschema.system.Atoms.positions` |
| `k_mesh` | Mapped | `runschema.method.KMesh.n_points`<br>`runschema.method.KMesh.grid`<br>`runschema.method.KMesh.points` |
| `k_mesh.n_points` | Mapped | `runschema.method.KMesh.n_points` |
| `k_mesh.grid` | Mapped | `runschema.method.KMesh.grid` |
| `k_mesh.k_points` | Mapped | `runschema.method.KMesh.points` |
| `Nwannier` | Mapped | `runschema.method.Wannier.n_projected_orbitals` |
| `Nband` | Mapped | `runschema.method.Wannier.n_bands` |
| `Niter` | Mapped | `runschema.method.Wannier.is_maximally_localized` |
| `conv_tol` | Mapped | `runschema.method.Wannier.convergence_tolerance_max_localization` |
| `energy_windows` | Mapped | `runschema.method.Wannier.energy_window_outer`<br>`runschema.method.Wannier.energy_window_inner` |
| `energy_windows.outer` | Mapped | `runschema.method.Wannier.energy_window_outer` |
| `energy_windows.inner` | Mapped | `runschema.method.Wannier.energy_window_inner` |
| `n_k_segments` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `div_first_k_segment` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `band_segments_points` | Mapped | `runschema.calculation.BandEnergies.kpoints` |

## Wannier90 / WInParser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `energy_fermi` | Unmapped | — |
| `projections` | Mapped | `runschema.system.AtomsGroup.label`<br>`runschema.system.AtomsGroup.atom_indices`<br>`runschema.system.AtomsGroup.n_atoms`<br>`runschema.method.AtomParameters.n_orbitals`<br>`runschema.method.AtomParameters.orbitals` |

## Wannier90 / HrParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `degeneracy_factors` | Mapped | `runschema.calculation.HoppingMatrix.n_wigner_seitz_points`<br>`runschema.calculation.HoppingMatrix.degeneracy_factors` |
| `hoppings` | Mapped | `runschema.calculation.HoppingMatrix.value`<br>`runschema.calculation.Energy.fermi`<br>`runschema.calculation.Energy.highest_occupied` |

## WIEN2k / In0Parser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `xc_functional` | Mapped | `runschema.method.Method.dft.xc_functional.exchange.name`<br>`runschema.method.Method.dft.xc_functional.correlation.name`<br>`runschema.method.Method.dft.xc_functional.hybrid.name`<br>`runschema.method.Method.dft.xc_functional.contributions.name` |
| `fft` | Unmapped | — |

## WIEN2k / In1Parser

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

## WIEN2k / StructParser

**Summary:** 5 mapped, 7 unmapped quantities (41.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `lattice` | Unmapped | — |
| `lattice.nonequiv_atoms` | Unmapped | — |
| `lattice.lattice` | Unmapped | — |
| `lattice.calc_mode` | Unmapped | — |
| `lattice.lattice_constants` | Mapped | `runschema.system.System.atoms.lattice_vectors` |
| `lattice.unit` | Mapped | `runschema.system.System.atoms.lattice_vectors` |
| `atom` | Unmapped | — |
| `atom.positions` | Mapped | `runschema.system.System.atoms.positions` |
| `atom.atom_name` | Mapped | `runschema.calculation.Calculation.dos_electronic.species_projected.atom_label` |
| `atom.NPT` | Unmapped | — |
| `atom.R0` | Unmapped | — |
| `atom.Z` | Mapped | `runschema.system.System.atoms.labels` |

## WIEN2k / IncParser

**Summary:** 0 mapped, 4 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `one_atom` | Unmapped | — |
| `one_atom.occupancies` | Unmapped | — |
| `one_atom.n_quantum_numbers` | Unmapped | — |
| `one_atom.kappas` | Unmapped | — |

## WIEN2k / In2Parser

**Summary:** 1 mapped, 3 unmapped quantities (25.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `switch` | Unmapped | — |
| `emin` | Unmapped | — |
| `smearing` | Mapped | `runschema.method.Method.electronic.smearing.kind`<br>`runschema.method.Method.electronic.smearing.width` |
| `gmax` | Unmapped | — |

## WIEN2k / DosParser

**Summary:** 2 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `labels` | Mapped | `runschema.calculation.Calculation.dos_electronic.total.value`<br>`runschema.calculation.Calculation.dos_electronic.species_projected.value` |
| `data` | Mapped | `runschema.calculation.Calculation.dos_electronic.energies`<br>`runschema.calculation.Calculation.dos_electronic.total.value`<br>`runschema.calculation.Calculation.dos_electronic.species_projected.value` |

## WIEN2k / OutParser

**Summary:** 8 mapped, 51 unmapped quantities (13.56% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `version` | Mapped | `runschema.run.Program.version` |
| `start_date` | Mapped | `runschema.run.Run.time_run.date_start` |
| `iteration` | Mapped | `runschema.run.Run.calculation.scf_iteration` |
| `iteration.NATO` | Unmapped | — |
| `iteration.NATO.nr_of_independent_atoms` | Unmapped | — |
| `iteration.NATO.total_atoms` | Unmapped | — |
| `iteration.NATO.system_name` | Unmapped | — |
| `iteration.POT` | Unmapped | — |
| `iteration.POT.potential_option` | Unmapped | — |
| `iteration.LAT` | Unmapped | — |
| `iteration.LAT.lattice_const` | Unmapped | — |
| `iteration.VOL` | Unmapped | — |
| `iteration.VOL.unit_cell_volume_bohr3` | Unmapped | — |
| `iteration.VOL.spinpolarization` | Mapped | `runschema.method.Method.electronic.n_spin_channels` |
| `iteration.RKM` | Unmapped | — |
| `iteration.RKM.matrix_size` | Unmapped | — |
| `iteration.RKM.LOs` | Unmapped | — |
| `iteration.RKM.rkm` | Unmapped | — |
| `iteration.KPT` | Unmapped | — |
| `iteration.KPT.nr_kpts` | Unmapped | — |
| `iteration.GAP` | Unmapped | — |
| `iteration.GAP.ene_gap` | Unmapped | — |
| `iteration.NOE` | Unmapped | — |
| `iteration.NOE.noe` | Unmapped | — |
| `iteration.FER` | Unmapped | — |
| `iteration.FER.energy_reference_fermi` | Mapped | `runschema.calculation.ScfIteration.energy.fermi`<br>`runschema.calculation.Calculation.energy.fermi` |
| `iteration.GMA` | Unmapped | — |
| `iteration.GMA.cutoff` | Unmapped | — |
| `iteration.POSi` | Unmapped | — |
| `iteration.POSi.atom_mult` | Unmapped | — |
| `iteration.POSi.position` | Unmapped | — |
| `iteration.CHAi` | Unmapped | — |
| `iteration.CHAi.tot_val_charge_cell` | Unmapped | — |
| `iteration.SUM` | Unmapped | — |
| `iteration.SUM.energy_sum_eigenvalues` | Mapped | `runschema.calculation.ScfIteration.energy.sum_eigenvalues.value` |
| `iteration.RTOi` | Unmapped | — |
| `iteration.NTO` | Unmapped | — |
| `iteration.NTO.tot_int_charge_nm` | Unmapped | — |
| `iteration.NTOi` | Unmapped | — |
| `iteration.NTOi.tot_charge_in_sphere_nm` | Unmapped | — |
| `iteration.DTOi` | Unmapped | — |
| `iteration.DTOi.tot_diff_charge` | Unmapped | — |
| `iteration.DIS` | Unmapped | — |
| `iteration.DIS.charge_distance` | Unmapped | — |
| `iteration.CTO` | Unmapped | — |
| `iteration.CTO.tot_int_charge` | Unmapped | — |
| `iteration.CTOi` | Unmapped | — |
| `iteration.CTOi.tot_charge_in_sphere` | Unmapped | — |
| `iteration.NECi` | Unmapped | — |
| `iteration.MMINT` | Unmapped | — |
| `iteration.MMINT.mmint` | Unmapped | — |
| `iteration.MMIi` | Unmapped | — |
| `iteration.MMIi.mmi` | Unmapped | — |
| `iteration.MMTOT` | Unmapped | — |
| `iteration.MMTOT.mmtot` | Unmapped | — |
| `iteration.ENE` | Unmapped | — |
| `iteration.ENE.energy_total` | Mapped | `runschema.calculation.ScfIteration.energy.total.value`<br>`runschema.calculation.Calculation.energy.total.value` |
| `iteration.FORi` | Unmapped | — |
| `iteration.FGLi` | Mapped | `runschema.calculation.Calculation.forces.total.value` |

## YAMBO / parser.py :: MainfileParser

The quantities below are listed in source declaration order. Dotted prefixes reflect
the lexical `sub_parser` nesting. The shared quantity lists `io_quantities`,
`energies_quantities`, `qp_properties_quantity` and `module_quantities` are each
declared once but reused under several parents; they are reported once at their point
of declaration.

**Summary:** 12 mapped, 58 unmapped quantities (17.14% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `io_quantities.key_value` | Unmapped | — |
| `io_quantities.file` | Unmapped | — |
| `io_quantities.sn` | Unmapped | — |
| `energies_quantities.fermi` | Mapped | `runschema.calculation.Calculation.energy.fermi` |
| `energies_quantities.conduction` | Mapped | `runschema.calculation.Calculation.energy.lowest_unoccupied` |
| `energies_quantities.valence` | Mapped | `runschema.calculation.Calculation.energy.highest_occupied` |
| `energies_quantities.valence_conduction` | Mapped | `runschema.calculation.Calculation.energy.highest_occupied`<br>`runschema.calculation.Calculation.energy.lowest_unoccupied` |
| `energies_quantities.x_yambo_filled_bands` | Unmapped | — |
| `energies_quantities.x_yambo_empty_bands` | Unmapped | — |
| `energies_quantities.x_yambo_electronic_temperature` | Unmapped | — |
| `energies_quantities.x_yambo_bosonic_temperature` | Unmapped | — |
| `energies_quantities.x_yambo_finite_temperature_mode` | Unmapped | — |
| `energies_quantities.x_yambo_electronic_density` | Unmapped | — |
| `energies_quantities.states_summary` | Unmapped | — |
| `energies_quantities.x_yambo_indirect_gaps` | Unmapped | — |
| `energies_quantities.x_yambo_direct_gaps` | Unmapped | — |
| `energies_quantities.x_yambo_indirect_gap` | Unmapped | — |
| `energies_quantities.x_yambo_direct_gap` | Unmapped | — |
| `energies_quantities.x_yambo_direct_gap_kpoint` | Unmapped | — |
| `energies_quantities.x_yambo_indirect_gap_kpoints` | Unmapped | — |
| `qp_properties` | Unmapped | — |
| `qp_properties.qp_energy` | Unmapped | — |
| `qp_properties.qp_energy.band` | Mapped | `runschema.calculation.BandEnergies.value_qp`<br>`runschema.calculation.BandEnergies.value_ks`<br>`runschema.calculation.BandEnergies.qp_linearization_prefactor` |
| `qp_properties.qp_energy.kpoint` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `qp_properties.output` | Unmapped | — |
| `module_quantities.dipoles` | Unmapped | — |
| `module_quantities.dipoles.input` | Unmapped | — |
| `module_quantities.dipoles.output` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.output` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.x_yambo_plane_waves_vxc` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.x_yambo_plane_waves_exs` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.x_yambo_mesh_size` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.energy_xc` | Mapped | `runschema.calculation.Calculation.energy.xc.value` |
| `module_quantities.local_xc_nonlocal_fock.corrections` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.corrections.band` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.corrections.band_sp` | Unmapped | — |
| `module_quantities.local_xc_nonlocal_fock.hf_occupations` | Unmapped | — |
| `module_quantities.dynamic_dielectric_matrix` | Unmapped | — |
| `module_quantities.dynamic_dielectric_matrix.output` | Unmapped | — |
| `module_quantities.dynamic_dielectric_matrix.x_yambo_mesh_size` | Unmapped | — |
| `module_quantities.bare_xc` | Unmapped | — |
| `module_quantities.bare_xc.output` | Unmapped | — |
| `module_quantities.bare_xc.xc_hf_dft` | Unmapped | — |
| `module_quantities.bare_xc.xc_hf_dft.band` | Unmapped | — |
| `module_quantities.bare_xc.hf_occupations` | Unmapped | — |
| `module_quantities.dyson` | Unmapped | — |
| `module_quantities.dyson.g0w0` | Unmapped | — |
| `module_quantities.dyson.g0w0.x_yambo_bands_range` | Unmapped | — |
| `module_quantities.dyson.g0w0.x_yambo_g_damping` | Unmapped | — |
| `module_quantities.dyson.g0w0.x_yambo_mesh_size` | Unmapped | — |
| `module_quantities.dyson.g0w0.input` | Unmapped | — |
| `version` | Mapped | `runschema.run.Program.version` |
| `hash` | Unmapped | — |
| `build` | Unmapped | — |
| `date_start` | Mapped | `runschema.run.TimeRun.date_start` |
| `cpu_files_io` | Unmapped | — |
| `cpu_files_io.parameters` | Unmapped | — |
| `cpu_files_io.input` | Unmapped | — |
| `core_variables_setup` | Unmapped | — |
| `core_variables_setup.energies_occupations` | Unmapped | — |
| `core_variables_setup.energies_occupations.eigenenergies` | Unmapped | — |
| `core_variables_setup.energies_occupations.eigenenergies.energies` | Mapped | `runschema.calculation.BandEnergies.energies` |
| `core_variables_setup.energies_occupations.eigenenergies.kpoints` | Mapped | `runschema.calculation.BandEnergies.kpoints` |
| `core_variables_setup.energies_occupations.eigenenergies.kpoints_weights` | Mapped | `runschema.calculation.BandEnergies.kpoints_weights` |
| `transferred_momenta` | Unmapped | — |
| `transferred_momenta.input` | Unmapped | — |
| `transferred_momenta.qpoints` | Unmapped | — |
| `transferred_momenta.module` | Unmapped | — |
| `module` | Unmapped | — |

## YAMBO / parser.py :: InputParser

**Summary:** 0 mapped, 2 unmapped quantities (0.00% coverage).

The `InputParser` is instantiated in `YamboParser.__init__` but never invoked during
`parse()`; none of its quantities are read.

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `key_value` | Unmapped | — |
| `key_block` | Unmapped | — |

## YAMBO / parser.py :: NetCDFParser

Coverage: Not available.

`NetCDFParser` is a custom `FileParser` subclass with no `Quantity` declarations. It
reads all variables directly from the NetCDF file via the `netCDF4.Dataset` handler in
`parse()`, exposing them by their raw NetCDF variable names rather than through
declarative `Quantity` objects.

