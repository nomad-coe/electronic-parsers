<?xml version="1.0" encoding="UTF-8"?>
<fpmd:simulation xmlns:fpmd="http://www.quantum-simulation.org/ns/fpmd/fpmd-1.0">

                   ============================
                   I qbox 1.63.2              I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I                          I
                   I http://qboxcode.org      I
                   ============================


<release> 1.63.2 dell </release>
<sysname> Linux </sysname>
<nodename> theobook68 </nodename>
<start_time> 2016-04-06T12:25:00Z </start_time>
<mpi_processes count="4">
<process id="0"> theobook68 </process>
<process id="1"> theobook68 </process>
<process id="2"> theobook68 </process>
<process id="3"> theobook68 </process>
</mpi_processes>
[qbox] <cmd># Si ground state</cmd>
[qbox] <cmd>set cell 5.13 5.13 0 0 5.13 5.13 5.13 0 5.13</cmd>
<unit_cell 
    a="5.13000000   5.13000000   0.00000000  "
    b="0.00000000   5.13000000   5.13000000  "
    c="5.13000000   0.00000000   5.13000000  " />
[qbox] <cmd>set ref_cell 5.5 5.5 0  0 5.5 5.5  5.5 0 5.5</cmd>
  <reference_unit_cell>
<unit_cell 
    a="5.50000000   5.50000000   0.00000000  "
    b="0.00000000   5.50000000   5.50000000  "
    c="5.50000000   0.00000000   5.50000000  " />
  </reference_unit_cell>
[qbox] <cmd>species silicon Si_VBC_LDA-1.0.xml</cmd>
  SpeciesCmd: defining species silicon as Si_VBC_LDA-1.0.xml

 species silicon:
<species name="silicon">
 <description>
Translated from UPF format by upf2qso
Generated using unknown code
Author: Von Barth-Car ( 1984)
Info: automatically converted from PWSCF format
    0        The Pseudo was generated with a Non-Relativistic Calculation
  0.00000000000E+00    Local Potential cutoff radius
nl pn  l   occ               Rcut            Rcut US             E pseu
3S  0  0  2.00      0.00000000000      0.00000000000      0.00000000000
3P  0  1  2.00      0.00000000000      0.00000000000      0.00000000000
SLA PZ NOGX NOGC
 </description>
 <symbol>Si</symbol>
 <atomic_number>14</atomic_number>
 <mass>28.08550000</mass>
 <norm_conserving_pseudopotential>
 <valence_charge>4</valence_charge>
 <lmax>2</lmax>
 <llocal>2</llocal>
 <nquad>0</nquad>
 <rquad>0.00000000</rquad>
 <mesh_spacing>0.01000000</mesh_spacing>
 </norm_conserving_pseudopotential>
</species>
 Kleinman-Bylander potential
 rcps_ =   1.50000000
[qbox] <cmd> atom Si1 silicon 1.2825 1.2825 1.2825</cmd>
[qbox] <cmd> atom Si2 silicon -1.2825 -1.2825 -1.2825</cmd>
[qbox] <cmd># Special point in the FCC Brillouin Zone</cmd>
[qbox] <cmd># A. Baldereschi, Phys. Rev. B7, 5212 (1973)</cmd>
[qbox] <cmd># 12-point set</cmd>
[qbox] <cmd>kpoint delete 0 0 0</cmd>
[qbox] <cmd>kpoint add  0.45880  0.14765  0.31115   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add -0.16350  0.14765 -0.31115   0.0833333333333333 </cmd>
[qbox] <cmd>kpoint add  0.45880  0.31115  0.14765   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add  0.16350  0.31115 -0.14765   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add  0.31115  0.45880  0.14765   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add -0.31115 -0.16350  0.14765   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add  0.14765  0.45880  0.31115   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add -0.14765  0.16350  0.31115   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add  0.14765  0.31115  0.45880   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add  0.14765 -0.31115 -0.16350   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add  0.31115  0.14765  0.45880   0.0833333333333333</cmd>
[qbox] <cmd>kpoint add  0.31115 -0.14765  0.16350   0.0833333333333333</cmd>
[qbox] <cmd>set stress ON</cmd>
[qbox] <cmd>set debug STRESS</cmd>
[qbox] <cmd>set ecut 15 </cmd>
[qbox] <cmd>set ecuts 10</cmd>
[qbox] <cmd>set wf_dyn PSD</cmd>
[qbox] <cmd>set ecutprec 4</cmd>
[qbox] <cmd>randomize_wf</cmd>
[qbox] <cmd>run 30 10</cmd>
  EnergyFunctional: np0v,np1v,np2v: 24 24 24
  EnergyFunctional: vft->np012(): 13824
<wavefunction ecut="7.50000000" nspin="1" nel="8" nempty="0">
<cell a="5.130000 5.130000 0.000000"
      b="0.000000 5.130000 5.130000"
      c="5.130000 0.000000 5.130000"/>
 reciprocal lattice vectors
 0.612396 0.612396 -0.612396
 -0.612396 0.612396 0.612396
 0.612396 -0.612396 0.612396
<refcell a="5.500000 5.500000 0.000000"
         b="0.000000 5.500000 5.500000"
         c="5.500000 0.000000 5.500000"/>
<grid nx="12" ny="12" nz="12"/>
 kpoint: 0.458800 0.147650 0.311150 weight: 0.083333
<slater_determinant kpoint="0.458800 0.147650 0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: -0.163500 0.147650 -0.311150 weight: 0.083333
<slater_determinant kpoint="-0.163500 0.147650 -0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.458800 0.311150 0.147650 weight: 0.083333
<slater_determinant kpoint="0.458800 0.311150 0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.163500 0.311150 -0.147650 weight: 0.083333
<slater_determinant kpoint="0.163500 0.311150 -0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.311150 0.458800 0.147650 weight: 0.083333
<slater_determinant kpoint="0.311150 0.458800 0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: -0.311150 -0.163500 0.147650 weight: 0.083333
<slater_determinant kpoint="-0.311150 -0.163500 0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.147650 0.458800 0.311150 weight: 0.083333
<slater_determinant kpoint="0.147650 0.458800 0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: -0.147650 0.163500 0.311150 weight: 0.083333
<slater_determinant kpoint="-0.147650 0.163500 0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.147650 0.311150 0.458800 weight: 0.083333
<slater_determinant kpoint="0.147650 0.311150 0.458800" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.147650 -0.311150 -0.163500 weight: 0.083333
<slater_determinant kpoint="0.147650 -0.311150 -0.163500" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.311150 0.147650 0.458800 weight: 0.083333
<slater_determinant kpoint="0.311150 0.147650 0.458800" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.311150 -0.147650 0.163500 weight: 0.083333
<slater_determinant kpoint="0.311150 -0.147650 0.163500" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
</wavefunction>
<iteration count="1">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  38.91841090 </eigenvalue_sum>
  <etotal_int>      71.69377918 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  4.79379542 </eigenvalue_sum>
  <etotal_int>       3.48681236 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -1.78794952 </eigenvalue_sum>
  <etotal_int>      -9.70779484 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -3.76707006 </eigenvalue_sum>
  <etotal_int>     -13.71061236 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -4.46161766 </eigenvalue_sum>
  <etotal_int>     -15.14442038 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -4.74233366 </eigenvalue_sum>
  <etotal_int>     -15.74652415 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -4.88006487 </eigenvalue_sum>
  <etotal_int>     -16.05770142 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -4.96788011 </eigenvalue_sum>
  <etotal_int>     -16.26434760 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.04072786 </eigenvalue_sum>
  <etotal_int>     -16.43696777 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.11278777 </eigenvalue_sum>
  <etotal_int>     -16.60455942 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00810926 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00883750 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00816498 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00014727 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00063438 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00011754 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00029930 </sigma_econf_xx>
   <sigma_econf_yy>   0.00029987 </sigma_econf_yy>
   <sigma_econf_zz>   0.00029731 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000944 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000796 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000556 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01068822 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01076595 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01067484 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00002606 </sigma_eps_xy>
   <sigma_eps_yz>  -0.00000273 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00013224 </sigma_eps_xz>

   <sigma_enl_xx>   0.00918365 </sigma_enl_xx>
   <sigma_enl_yy>   0.00921766 </sigma_enl_yy>
   <sigma_enl_zz>   0.00917047 </sigma_enl_zz>
   <sigma_enl_xy>   0.00002287 </sigma_enl_xy>
   <sigma_enl_yz>   0.00003804 </sigma_enl_yz>
   <sigma_enl_xz>   0.00010833 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00399398 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00402341 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00398827 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00004469 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00005836 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00017963 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00261913 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00261913 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00261913 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>   0.00086955 </sigma_eks_xx>
   <sigma_eks_yy>   0.00152520 </sigma_eks_yy>
   <sigma_eks_zz>   0.00092918 </sigma_eks_zz>
   <sigma_eks_xy>   0.00019820 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00053275 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00031552 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         3.39022759 </ekin>
  <econf>        0.02064193 </econf>
  <eps>         -2.59617920 </eps>
  <enl>          2.03190157 </enl>
  <ecoul>       -7.78221072 </ecoul>
  <exc>         -2.32895188 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.26457071 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.26457071 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00513205 -0.01662698 0.00991197 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00825831 0.01605405 -0.00853693 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  25.58333096 </sigma_eks_xx>
   <sigma_eks_yy>  44.87353610 </sigma_eks_yy>
   <sigma_eks_zz>  27.33781575 </sigma_eks_zz>
   <sigma_eks_xy>   5.83141634 </sigma_eks_xy>
   <sigma_eks_yz> -15.67440067 </sigma_eks_yz>
   <sigma_eks_xz>  -9.28293321 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  25.58333096 </sigma_xx>
   <sigma_yy>  44.87353610 </sigma_yy>
   <sigma_zz>  27.33781575 </sigma_zz>
   <sigma_xy>   5.83141634 </sigma_xy>
   <sigma_yz> -15.67440067 </sigma_yz>
   <sigma_xz>  -9.28293321 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.213" max="    0.217"/>
</iteration>
<iteration count="2">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.19007428 </eigenvalue_sum>
  <etotal_int>     -16.77970689 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.27503549 </eigenvalue_sum>
  <etotal_int>     -16.96775162 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.36836443 </eigenvalue_sum>
  <etotal_int>     -17.17042130 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.46977231 </eigenvalue_sum>
  <etotal_int>     -17.38739488 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.57836125 </eigenvalue_sum>
  <etotal_int>     -17.61706930 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.69284561 </eigenvalue_sum>
  <etotal_int>     -17.85702200 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.81171842 </eigenvalue_sum>
  <etotal_int>     -18.10436050 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -5.93339274 </eigenvalue_sum>
  <etotal_int>     -18.35601747 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.05631845 </eigenvalue_sum>
  <etotal_int>     -18.60899255 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.17906710 </eigenvalue_sum>
  <etotal_int>     -18.86052639 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00774186 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00826377 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00815489 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00013855 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00059995 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000486 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00029884 </sigma_econf_xx>
   <sigma_econf_yy>   0.00030315 </sigma_econf_yy>
   <sigma_econf_zz>   0.00030041 </sigma_econf_zz>
   <sigma_econf_xy>   0.00001000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000670 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000645 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01108930 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01126940 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01115190 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00001032 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002034 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00013655 </sigma_eps_xz>

   <sigma_enl_xx>   0.00956372 </sigma_enl_xx>
   <sigma_enl_yy>   0.00970307 </sigma_enl_yy>
   <sigma_enl_zz>   0.00960421 </sigma_enl_zz>
   <sigma_enl_xy>   0.00001533 </sigma_enl_xy>
   <sigma_enl_yz>   0.00000798 </sigma_enl_yz>
   <sigma_enl_xz>   0.00010775 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00380619 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00388703 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00382864 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00001444 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00001752 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00018362 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00267358 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00267358 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00267358 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>   0.00061402 </sigma_eks_xx>
   <sigma_eks_yy>   0.00101864 </sigma_eks_yy>
   <sigma_eks_zz>   0.00098405 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00010910 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00054741 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00020111 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         3.26180813 </ekin>
  <econf>        0.02089875 </econf>
  <eps>         -2.67901963 </eps>
  <enl>          2.07658679 </enl>
  <ecoul>       -7.86189658 </ecoul>
  <exc>         -2.37587955 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.55750209 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.55750209 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00230645 -0.01555862 0.00597835 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00080052 0.01517518 -0.00442616 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  18.06536576 </sigma_eks_xx>
   <sigma_eks_yy>  29.96996873 </sigma_eks_yy>
   <sigma_eks_zz>  28.95209988 </sigma_eks_zz>
   <sigma_eks_xy>  -3.20976756 </sigma_eks_xy>
   <sigma_eks_yz> -16.10570942 </sigma_eks_yz>
   <sigma_eks_xz>  -5.91706627 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  18.06536576 </sigma_xx>
   <sigma_yy>  29.96996873 </sigma_yy>
   <sigma_zz>  28.95209988 </sigma_zz>
   <sigma_xy>  -3.20976756 </sigma_xy>
   <sigma_yz> -16.10570942 </sigma_yz>
   <sigma_xz>  -5.91706627 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.221" max="    0.225"/>
</iteration>
<iteration count="3">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.30038094 </eigenvalue_sum>
  <etotal_int>     -19.10820048 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.41919014 </eigenvalue_sum>
  <etotal_int>     -19.34997150 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.53460791 </eigenvalue_sum>
  <etotal_int>     -19.58416076 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.64591495 </eigenvalue_sum>
  <etotal_int>     -19.80942204 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.75254209 </eigenvalue_sum>
  <etotal_int>     -20.02470583 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.85405597 </eigenvalue_sum>
  <etotal_int>     -20.22922978 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -6.95014868 </eigenvalue_sum>
  <etotal_int>     -20.42245703 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.04062965 </eigenvalue_sum>
  <etotal_int>     -20.60407938 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.12541783 </eigenvalue_sum>
  <etotal_int>     -20.77400103 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.20453219 </eigenvalue_sum>
  <etotal_int>     -20.93231915 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00739348 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00768698 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00783075 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00019404 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00046164 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00016620 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00028124 </sigma_econf_xx>
   <sigma_econf_yy>   0.00028471 </sigma_econf_yy>
   <sigma_econf_zz>   0.00028161 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000659 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000200 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000303 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01108895 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01125513 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01113465 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000063 </sigma_eps_xy>
   <sigma_eps_yz>   0.00006033 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00007481 </sigma_eps_xz>

   <sigma_enl_xx>   0.00958639 </sigma_enl_xx>
   <sigma_enl_yy>   0.00972343 </sigma_enl_yy>
   <sigma_enl_zz>   0.00961105 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000564 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00003199 </sigma_enl_yz>
   <sigma_enl_xz>   0.00004689 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00380641 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00388662 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00381644 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001034 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00004100 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00014481 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268256 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268256 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268256 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>   0.00026186 </sigma_eks_xx>
   <sigma_eks_yy>   0.00044947 </sigma_eks_yy>
   <sigma_eks_zz>   0.00066843 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00019279 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00039030 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000351 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         3.09314428 </ekin>
  <econf>        0.01966664 </econf>
  <eps>         -2.66182030 </eps>
  <enl>          2.05999577 </enl>
  <ecoul>       -7.86351834 </ecoul>
  <exc>         -2.38362178 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.73615373 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.73615373 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00037272 -0.01279418 -0.00264500 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00077563 0.01201452 0.00362928 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>   7.70442667 </sigma_eks_xx>
   <sigma_eks_yy>  13.22422706 </sigma_eks_yy>
   <sigma_eks_zz>  19.66613498 </sigma_eks_zz>
   <sigma_eks_xy>  -5.67207865 </sigma_eks_xy>
   <sigma_eks_yz> -11.48334300 </sigma_eks_yz>
   <sigma_eks_xz>  -0.10324259 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>   7.70442667 </sigma_xx>
   <sigma_yy>  13.22422706 </sigma_yy>
   <sigma_zz>  19.66613498 </sigma_zz>
   <sigma_xy>  -5.67207865 </sigma_xy>
   <sigma_yz> -11.48334300 </sigma_yz>
   <sigma_xz>  -0.10324259 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.215" max="    0.219"/>
</iteration>
<iteration count="4">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.27807984 </eigenvalue_sum>
  <etotal_int>     -21.07930009 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.34624200 </eigenvalue_sum>
  <etotal_int>     -21.21535144 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.40925873 </eigenvalue_sum>
  <etotal_int>     -21.34099172 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.46741335 </eigenvalue_sum>
  <etotal_int>     -21.45681991 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.52101782 </eigenvalue_sum>
  <etotal_int>     -21.56348673 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.57039966 </eigenvalue_sum>
  <etotal_int>     -21.66166919 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.61589097 </eigenvalue_sum>
  <etotal_int>     -21.75204933 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.65781966 </eigenvalue_sum>
  <etotal_int>     -21.83529727 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.69650273 </eigenvalue_sum>
  <etotal_int>     -21.91205844 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.73224156 </eigenvalue_sum>
  <etotal_int>     -21.98294459 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00725030 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00740687 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00760644 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00013678 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00034069 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00025612 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00027128 </sigma_econf_xx>
   <sigma_econf_yy>   0.00027362 </sigma_econf_yy>
   <sigma_econf_zz>   0.00027109 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000342 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000027 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000093 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01105373 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01117499 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01105974 </sigma_eps_zz>
   <sigma_eps_xy>   0.00000584 </sigma_eps_xy>
   <sigma_eps_yz>   0.00007960 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00003950 </sigma_eps_xz>

   <sigma_enl_xx>   0.00955729 </sigma_enl_xx>
   <sigma_enl_yy>   0.00966006 </sigma_enl_yy>
   <sigma_enl_zz>   0.00954973 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00000146 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00004987 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001192 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00383842 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00389993 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00383049 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000810 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00007381 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00011113 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268041 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268041 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268041 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>   0.00008497 </sigma_eks_xx>
   <sigma_eks_yy>   0.00016389 </sigma_eks_yy>
   <sigma_eks_zz>   0.00043530 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00013707 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00023743 </sigma_eks_yz>
   <sigma_eks_xz>   0.00011833 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         3.00571389 </ekin>
  <econf>        0.01895103 </econf>
  <eps>         -2.64002160 </eps>
  <enl>          2.04101912 </enl>
  <ecoul>       -7.85600049 </ecoul>
  <exc>         -2.38177213 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.81211018 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.81211018 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00533941 -0.01148577 -0.00396658 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00444918 0.01101152 0.00439939 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>   2.49993708 </sigma_eks_xx>
   <sigma_eks_yy>   4.82201907 </sigma_eks_yy>
   <sigma_eks_zz>  12.80708363 </sigma_eks_zz>
   <sigma_eks_xy>  -4.03274619 </sigma_eks_xy>
   <sigma_eks_yz>  -6.98552421 </sigma_eks_yz>
   <sigma_eks_xz>   3.48147190 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>   2.49993708 </sigma_xx>
   <sigma_yy>   4.82201907 </sigma_yy>
   <sigma_zz>  12.80708363 </sigma_zz>
   <sigma_xy>  -4.03274619 </sigma_xy>
   <sigma_yz>  -6.98552421 </sigma_yz>
   <sigma_xz>   3.48147190 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.212" max="    0.219"/>
</iteration>
<iteration count="5">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.76531877 </eigenvalue_sum>
  <etotal_int>     -22.04852793 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.79599632 </eigenvalue_sum>
  <etotal_int>     -22.10933773 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.82451468 </eigenvalue_sum>
  <etotal_int>     -22.16585895 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.85109279 </eigenvalue_sum>
  <etotal_int>     -22.21853230 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.87592847 </eigenvalue_sum>
  <etotal_int>     -22.26775541 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.89919931 </eigenvalue_sum>
  <etotal_int>     -22.31388465 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.92106384 </eigenvalue_sum>
  <etotal_int>     -22.35723761 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.94166278 </eigenvalue_sum>
  <etotal_int>     -22.39809577 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.96112050 </eigenvalue_sum>
  <etotal_int>     -22.43670744 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.97954645 </eigenvalue_sum>
  <etotal_int>     -22.47329076 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00720353 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00727403 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00747860 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00007923 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00024137 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00027246 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026620 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026795 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026621 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000180 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000048 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000016 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103347 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01112762 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01102417 </sigma_eps_zz>
   <sigma_eps_xy>   0.00000240 </sigma_eps_xy>
   <sigma_eps_yz>   0.00007353 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00003217 </sigma_eps_xz>

   <sigma_enl_xx>   0.00953844 </sigma_enl_xx>
   <sigma_enl_yy>   0.00962072 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952080 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00000057 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00004921 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000565 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00385550 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00390541 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00384197 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001095 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00006830 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00009091 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00267862 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00267862 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00267862 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>   0.00001924 </sigma_eks_xx>
   <sigma_eks_yy>   0.00002973 </sigma_eks_yy>
   <sigma_eks_zz>   0.00029951 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00008655 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00014923 </sigma_eks_yz>
   <sigma_eks_xz>   0.00015519 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.96420771 </ekin>
  <econf>        0.01859722 </econf>
  <eps>         -2.62900564 </eps>
  <enl>          2.03149277 </enl>
  <ecoul>       -7.85186028 </ecoul>
  <exc>         -2.38023465 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.84680287 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.84680287 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00564159 -0.01077906 -0.00341264 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00450661 0.01079283 0.00350401 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>   0.56599024 </sigma_eks_xx>
   <sigma_eks_yy>   0.87457184 </sigma_eks_yy>
   <sigma_eks_zz>   8.81210204 </sigma_eks_zz>
   <sigma_eks_xy>  -2.54651307 </sigma_eks_xy>
   <sigma_eks_yz>  -4.39058152 </sigma_eks_yz>
   <sigma_eks_xz>   4.56599496 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>   0.56599024 </sigma_xx>
   <sigma_yy>   0.87457184 </sigma_yy>
   <sigma_zz>   8.81210204 </sigma_zz>
   <sigma_xy>  -2.54651307 </sigma_xy>
   <sigma_yz>  -4.39058152 </sigma_yz>
   <sigma_xz>   4.56599496 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.216" max="    0.223"/>
</iteration>
<iteration count="6">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -7.99703663 </eigenvalue_sum>
  <etotal_int>     -22.50803670 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.01367504 </eigenvalue_sum>
  <etotal_int>     -22.54111195 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.02953499 </eigenvalue_sum>
  <etotal_int>     -22.57266170 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.04468041 </eigenvalue_sum>
  <etotal_int>     -22.60281228 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.05916701 </eigenvalue_sum>
  <etotal_int>     -22.63167345 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.07304333 </eigenvalue_sum>
  <etotal_int>     -22.65934062 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.08635164 </eigenvalue_sum>
  <etotal_int>     -22.68589665 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.09912877 </eigenvalue_sum>
  <etotal_int>     -22.71141349 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.11140676 </eigenvalue_sum>
  <etotal_int>     -22.73595357 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.12321345 </eigenvalue_sum>
  <etotal_int>     -22.75957091 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00719392 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00719875 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00738799 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00003362 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00015401 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00024415 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026299 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026427 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026321 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000092 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000021 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000015 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01102240 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01110106 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01101880 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000907 </sigma_eps_xy>
   <sigma_eps_yz>   0.00005675 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00003232 </sigma_eps_xz>

   <sigma_enl_xx>   0.00952564 </sigma_enl_xx>
   <sigma_enl_yy>   0.00959684 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951669 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000712 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00004077 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000975 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00386060 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00390371 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00385199 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00002085 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00004523 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00006897 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00267837 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00267837 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00267837 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000014 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00004461 </sigma_eks_yy>
   <sigma_eks_zz>   0.00019739 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00005550 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00009301 </sigma_eks_yz>
   <sigma_eks_xz>   0.00015246 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.94051292 </ekin>
  <econf>        0.01837600 </econf>
  <eps>         -2.62365584 </eps>
  <enl>          2.02624277 </enl>
  <ecoul>       -7.85038896 </ecoul>
  <exc>         -2.38001526 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.86892836 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.86892836 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00308348 -0.00859395 -0.00274085 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00178388 0.00878673 0.00265972 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00418170 </sigma_eks_xx>
   <sigma_eks_yy>  -1.31246359 </sigma_eks_yy>
   <sigma_eks_zz>   5.80759719 </sigma_eks_zz>
   <sigma_eks_xy>  -1.63280116 </sigma_eks_xy>
   <sigma_eks_yz>  -2.73662046 </sigma_eks_yz>
   <sigma_eks_xz>   4.48551540 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -0.00418170 </sigma_xx>
   <sigma_yy>  -1.31246359 </sigma_yy>
   <sigma_zz>   5.80759719 </sigma_zz>
   <sigma_xy>  -1.63280116 </sigma_xy>
   <sigma_yz>  -2.73662046 </sigma_yz>
   <sigma_xz>   4.48551540 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.213" max="    0.220"/>
</iteration>
<iteration count="7">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.13457293 </eigenvalue_sum>
  <etotal_int>     -22.78231206 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.14550596 </eigenvalue_sum>
  <etotal_int>     -22.80421695 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.15603029 </eigenvalue_sum>
  <etotal_int>     -22.82531950 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.16616097 </eigenvalue_sum>
  <etotal_int>     -22.84564827 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.17591064 </eigenvalue_sum>
  <etotal_int>     -22.86522696 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.18528977 </eigenvalue_sum>
  <etotal_int>     -22.88407502 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.19430697 </eigenvalue_sum>
  <etotal_int>     -22.90220815 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.20296926 </eigenvalue_sum>
  <etotal_int>     -22.91963889 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.21128235 </eigenvalue_sum>
  <etotal_int>     -22.93637719 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.21925094 </eigenvalue_sum>
  <etotal_int>     -22.95243104 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00719226 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00716139 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00731474 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000350 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00009493 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00018422 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026059 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026136 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026084 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000035 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000001 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000034 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01102032 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01107927 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01102583 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00001792 </sigma_eps_xy>
   <sigma_eps_yz>   0.00003886 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002756 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951925 </sigma_enl_xx>
   <sigma_enl_yy>   0.00957410 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952131 </sigma_enl_zz>
   <sigma_enl_xy>   0.00001344 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00002967 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001223 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00386316 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00389598 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00386101 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00002664 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00002449 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00003962 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00267896 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00267896 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00267896 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00001167 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00007867 </sigma_eks_yy>
   <sigma_eks_zz>   0.00010977 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00003427 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00006124 </sigma_eks_yz>
   <sigma_eks_xz>   0.00012893 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.92535693 </ekin>
  <econf>        0.01820602 </econf>
  <eps>         -2.62053645 </eps>
  <enl>          2.02235722 </enl>
  <ecoul>       -7.85005398 </ecoul>
  <exc>         -2.38052521 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.88519547 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.88519547 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00075133 -0.00495943 -0.00194275 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00057528 0.00510639 0.00180677 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.34329591 </sigma_eks_xx>
   <sigma_eks_yy>  -2.31473450 </sigma_eks_yy>
   <sigma_eks_zz>   3.22948363 </sigma_eks_zz>
   <sigma_eks_xy>  -1.00842014 </sigma_eks_xy>
   <sigma_eks_yz>  -1.80164820 </sigma_eks_yz>
   <sigma_eks_xz>   3.79339835 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -0.34329591 </sigma_xx>
   <sigma_yy>  -2.31473450 </sigma_yy>
   <sigma_zz>   3.22948363 </sigma_zz>
   <sigma_xy>  -1.00842014 </sigma_xy>
   <sigma_yz>  -1.80164820 </sigma_yz>
   <sigma_xz>   3.79339835 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.220" max="    0.227"/>
</iteration>
<iteration count="8">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.22687905 </eigenvalue_sum>
  <etotal_int>     -22.96780707 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.23417027 </eigenvalue_sum>
  <etotal_int>     -22.98251116 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.24112808 </eigenvalue_sum>
  <etotal_int>     -22.99654901 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.24775607 </eigenvalue_sum>
  <etotal_int>     -23.00992668 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.25405822 </eigenvalue_sum>
  <etotal_int>     -23.02265103 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.26003901 </eigenvalue_sum>
  <etotal_int>     -23.03473009 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.26570363 </eigenvalue_sum>
  <etotal_int>     -23.04617343 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.27105805 </eigenvalue_sum>
  <etotal_int>     -23.05699226 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.27610908 </eigenvalue_sum>
  <etotal_int>     -23.06719961 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28086438 </eigenvalue_sum>
  <etotal_int>     -23.07681034 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718723 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00715389 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00725866 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000835 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00005933 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00011681 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025881 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025919 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025900 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000003 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000012 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000038 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01102342 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01106003 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103295 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00001775 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002368 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001888 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951740 </sigma_enl_xx>
   <sigma_enl_yy>   0.00955210 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952476 </sigma_enl_zz>
   <sigma_enl_xy>   0.00001320 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001891 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001067 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00386647 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00388694 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00386793 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00002331 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00001046 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00001528 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00267965 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00267965 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00267965 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00002742 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00008278 </sigma_eks_yy>
   <sigma_eks_zz>   0.00004056 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00001947 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00004398 </sigma_eks_yz>
   <sigma_eks_xz>   0.00009294 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.91609328 </ekin>
  <econf>        0.01807860 </econf>
  <eps>         -2.61832326 </eps>
  <enl>          2.01916403 </enl>
  <ecoul>       -7.84995641 </ecoul>
  <exc>         -2.38112122 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.89606498 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.89606498 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00042934 -0.00193789 -0.00120847 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00157988 0.00205222 0.00108697 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.80669432 </sigma_eks_xx>
   <sigma_eks_yy>  -2.43536843 </sigma_eks_yy>
   <sigma_eks_zz>   1.19332188 </sigma_eks_zz>
   <sigma_eks_xy>  -0.57284462 </sigma_eks_xy>
   <sigma_eks_yz>  -1.29384491 </sigma_eks_yz>
   <sigma_eks_xz>   2.73431860 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -0.80669432 </sigma_xx>
   <sigma_yy>  -2.43536843 </sigma_yy>
   <sigma_zz>   1.19332188 </sigma_zz>
   <sigma_xy>  -0.57284462 </sigma_xy>
   <sigma_yz>  -1.29384491 </sigma_yz>
   <sigma_xz>   2.73431860 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="9">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28533242 </eigenvalue_sum>
  <etotal_int>     -23.08584108 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28952246 </eigenvalue_sum>
  <etotal_int>     -23.09431009 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29344445 </eigenvalue_sum>
  <etotal_int>     -23.10223714 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29710892 </eigenvalue_sum>
  <etotal_int>     -23.10964323 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30052687 </eigenvalue_sum>
  <etotal_int>     -23.11655040 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30370965 </eigenvalue_sum>
  <etotal_int>     -23.12298148 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30666886 </eigenvalue_sum>
  <etotal_int>     -23.12895979 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30941618 </eigenvalue_sum>
  <etotal_int>     -23.13450894 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31196333 </eigenvalue_sum>
  <etotal_int>     -23.13965257 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31432190 </eigenvalue_sum>
  <etotal_int>     -23.14441416 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718211 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00715957 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00722238 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000921 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00003678 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00006693 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025770 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025785 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025781 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000007 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000013 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000031 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01102661 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01104665 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103554 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00001297 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001332 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001170 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951672 </sigma_enl_xx>
   <sigma_enl_yy>   0.00953593 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952429 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000957 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001101 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000784 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00386971 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00388091 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387209 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001638 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00000310 </sigma_ehart_yz>
   <sigma_ehart_xz>  -0.00000336 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268005 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268005 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268005 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00004117 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00007558 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000451 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00001064 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00003124 </sigma_eks_yz>
   <sigma_eks_xz>   0.00005940 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.91127164 </ekin>
  <econf>        0.01799884 </econf>
  <eps>         -2.61671755 </eps>
  <enl>          2.01681822 </enl>
  <ecoul>       -7.84979861 </ecoul>
  <exc>         -2.38146662 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90189408 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90189408 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00068223 -0.00047206 -0.00071885 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00154064 0.00058844 0.00063717 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.21131616 </sigma_eks_xx>
   <sigma_eks_yy>  -2.22360902 </sigma_eks_yy>
   <sigma_eks_zz>  -0.13274788 </sigma_eks_zz>
   <sigma_eks_xy>  -0.31295161 </sigma_eks_xy>
   <sigma_eks_yz>  -0.91910040 </sigma_eks_yz>
   <sigma_eks_xz>   1.74753523 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.21131616 </sigma_xx>
   <sigma_yy>  -2.22360902 </sigma_yy>
   <sigma_zz>  -0.13274788 </sigma_zz>
   <sigma_xy>  -0.31295161 </sigma_xy>
   <sigma_yz>  -0.91910040 </sigma_yz>
   <sigma_xz>   1.74753523 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="10">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31650331 </eigenvalue_sum>
  <etotal_int>     -23.14881681 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31851870 </eigenvalue_sum>
  <etotal_int>     -23.15288313 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32037889 </eigenvalue_sum>
  <etotal_int>     -23.15663502 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32209431 </eigenvalue_sum>
  <etotal_int>     -23.16009365 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32367494 </eigenvalue_sum>
  <etotal_int>     -23.16327931 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32513035 </eigenvalue_sum>
  <etotal_int>     -23.16621137 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32646958 </eigenvalue_sum>
  <etotal_int>     -23.16890825 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32770123 </eigenvalue_sum>
  <etotal_int>     -23.17138735 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32883338 </eigenvalue_sum>
  <etotal_int>     -23.17366510 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32987362 </eigenvalue_sum>
  <etotal_int>     -23.17575692 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717939 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00716659 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00720201 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000693 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00002248 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00003777 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025710 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025717 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025717 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000008 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000011 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000021 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01102851 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103902 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103512 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000835 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000733 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000724 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951617 </sigma_enl_xx>
   <sigma_enl_yy>   0.00952631 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952195 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000610 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000624 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000543 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387210 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387795 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387415 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001050 </sigma_ehart_xy>
   <sigma_ehart_yz>   0.00000017 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000047 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00004947 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00006843 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00002966 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000590 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00002111 </sigma_eks_yz>
   <sigma_eks_xz>   0.00003622 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90910119 </ekin>
  <econf>        0.01795684 </econf>
  <eps>         -2.61566735 </eps>
  <enl>          2.01533246 </enl>
  <ecoul>       -7.84961740 </ecoul>
  <exc>         -2.38159637 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90449064 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90449064 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00055542 0.00001323 -0.00043528 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00114226 0.00009808 0.00038826 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.45556245 </sigma_eks_xx>
   <sigma_eks_yy>  -2.01323140 </sigma_eks_yy>
   <sigma_eks_zz>  -0.87269384 </sigma_eks_zz>
   <sigma_eks_xy>  -0.17346369 </sigma_eks_xy>
   <sigma_eks_yz>  -0.62108592 </sigma_eks_yz>
   <sigma_eks_xz>   1.06555382 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.45556245 </sigma_xx>
   <sigma_yy>  -2.01323140 </sigma_yy>
   <sigma_zz>  -0.87269384 </sigma_zz>
   <sigma_xy>  -0.17346369 </sigma_xy>
   <sigma_yz>  -0.62108592 </sigma_yz>
   <sigma_xz>   1.06555382 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.215" max="    0.222"/>
</iteration>
<iteration count="11">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33082907 </eigenvalue_sum>
  <etotal_int>     -23.17767726 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33170637 </eigenvalue_sum>
  <etotal_int>     -23.17943961 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33251172 </eigenvalue_sum>
  <etotal_int>     -23.18105654 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33325088 </eigenvalue_sum>
  <etotal_int>     -23.18253973 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33392917 </eigenvalue_sum>
  <etotal_int>     -23.18390002 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33455156 </eigenvalue_sum>
  <etotal_int>     -23.18514743 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33512260 </eigenvalue_sum>
  <etotal_int>     -23.18629126 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33564653 </eigenvalue_sum>
  <etotal_int>     -23.18734004 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33612723 </eigenvalue_sum>
  <etotal_int>     -23.18830168 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33656829 </eigenvalue_sum>
  <etotal_int>     -23.18918344 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717844 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717157 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00719123 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000467 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00001370 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00002192 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025682 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025684 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025685 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000006 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000007 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000013 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01102949 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103502 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103388 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000516 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000409 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000460 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951573 </sigma_enl_xx>
   <sigma_enl_yy>   0.00952109 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951962 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000373 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000356 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000369 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387362 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387668 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387507 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000655 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000068 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000119 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268023 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268023 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268023 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005369 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00006376 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00004281 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000337 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001378 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002206 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90819138 </ekin>
  <econf>        0.01793652 </econf>
  <eps>         -2.61503715 </eps>
  <enl>          2.01446799 </enl>
  <ecoul>       -7.84947197 </ecoul>
  <exc>         -2.38162826 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90554148 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90554148 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00037240 0.00012176 -0.00027086 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00075796 -0.00002766 0.00024606 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.57956485 </sigma_eks_xx>
   <sigma_eks_yy>  -1.87592535 </sigma_eks_yy>
   <sigma_eks_zz>  -1.25956228 </sigma_eks_zz>
   <sigma_eks_xy>  -0.09906146 </sigma_eks_xy>
   <sigma_eks_yz>  -0.40529211 </sigma_eks_yz>
   <sigma_eks_xz>   0.64910985 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.57956485 </sigma_xx>
   <sigma_yy>  -1.87592535 </sigma_yy>
   <sigma_zz>  -1.25956228 </sigma_zz>
   <sigma_xy>  -0.09906146 </sigma_xy>
   <sigma_yz>  -0.40529211 </sigma_yz>
   <sigma_xz>   0.64910985 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="12">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33697300 </eigenvalue_sum>
  <etotal_int>     -23.18999199 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33734441 </eigenvalue_sum>
  <etotal_int>     -23.19073348 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33768528 </eigenvalue_sum>
  <etotal_int>     -23.19141355 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33799818 </eigenvalue_sum>
  <etotal_int>     -23.19203736 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33828545 </eigenvalue_sum>
  <etotal_int>     -23.19260965 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33854924 </eigenvalue_sum>
  <etotal_int>     -23.19313478 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33879151 </eigenvalue_sum>
  <etotal_int>     -23.19361671 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33901408 </eigenvalue_sum>
  <etotal_int>     -23.19405910 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33921859 </eigenvalue_sum>
  <etotal_int>     -23.19446528 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33940655 </eigenvalue_sum>
  <etotal_int>     -23.19483831 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717828 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717462 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00718557 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000305 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000838 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00001318 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025668 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025669 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025670 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000004 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000005 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000008 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103001 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103296 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103276 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000317 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000234 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000298 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951544 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951831 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951790 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000227 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000207 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000248 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387453 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387615 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387548 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000408 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000077 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000103 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268023 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268023 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268023 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005570 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00006106 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00004964 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000197 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000883 </sigma_eks_yz>
   <sigma_eks_xz>   0.00001362 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90781633 </ekin>
  <econf>        0.01792684 </econf>
  <eps>         -2.61467392 </eps>
  <enl>          2.01398036 </enl>
  <ecoul>       -7.84937342 </ecoul>
  <exc>         -2.38162835 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90595215 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90595215 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00023026 0.00011880 -0.00017149 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00047929 -0.00004582 0.00015922 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.63883094 </sigma_eks_xx>
   <sigma_eks_yy>  -1.79634203 </sigma_eks_yy>
   <sigma_eks_zz>  -1.46038445 </sigma_eks_zz>
   <sigma_eks_xy>  -0.05797454 </sigma_eks_xy>
   <sigma_eks_yz>  -0.25984508 </sigma_eks_yz>
   <sigma_eks_xz>   0.40085039 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.63883094 </sigma_xx>
   <sigma_yy>  -1.79634203 </sigma_yy>
   <sigma_zz>  -1.46038445 </sigma_zz>
   <sigma_xy>  -0.05797454 </sigma_xy>
   <sigma_yz>  -0.25984508 </sigma_yz>
   <sigma_xz>   0.40085039 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.216" max="    0.223"/>
</iteration>
<iteration count="13">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33957935 </eigenvalue_sum>
  <etotal_int>     -23.19518096 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33973826 </eigenvalue_sum>
  <etotal_int>     -23.19549581 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33988443 </eigenvalue_sum>
  <etotal_int>     -23.19578518 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34001892 </eigenvalue_sum>
  <etotal_int>     -23.19605121 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34014270 </eigenvalue_sum>
  <etotal_int>     -23.19629586 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34025667 </eigenvalue_sum>
  <etotal_int>     -23.19652090 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34036163 </eigenvalue_sum>
  <etotal_int>     -23.19672798 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34045833 </eigenvalue_sum>
  <etotal_int>     -23.19691859 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34054744 </eigenvalue_sum>
  <etotal_int>     -23.19709409 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34062959 </eigenvalue_sum>
  <etotal_int>     -23.19725573 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717837 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717640 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00718254 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000197 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000516 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000814 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025661 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025661 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025662 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000003 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000003 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000005 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103028 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103189 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103195 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000195 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000137 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000195 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951527 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951683 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951676 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000139 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000123 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000165 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387506 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387594 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387565 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000255 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000063 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000074 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268023 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268023 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268023 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005666 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005954 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005324 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000117 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000562 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000853 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90766015 </ekin>
  <econf>        0.01792213 </econf>
  <eps>         -2.61446743 </eps>
  <enl>          2.01370690 </enl>
  <ecoul>       -7.84931180 </ecoul>
  <exc>         -2.38162149 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90611153 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90611153 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00013705 0.00009176 -0.00010944 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00029665 -0.00003818 0.00010376 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.66694834 </sigma_eks_xx>
   <sigma_eks_yy>  -1.75171966 </sigma_eks_yy>
   <sigma_eks_zz>  -1.56627185 </sigma_eks_zz>
   <sigma_eks_xy>  -0.03448820 </sigma_eks_xy>
   <sigma_eks_yz>  -0.16528553 </sigma_eks_yz>
   <sigma_eks_xz>   0.25089633 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.66694834 </sigma_xx>
   <sigma_yy>  -1.75171966 </sigma_yy>
   <sigma_zz>  -1.56627185 </sigma_zz>
   <sigma_xy>  -0.03448820 </sigma_xy>
   <sigma_yz>  -0.16528553 </sigma_yz>
   <sigma_xz>   0.25089633 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.226" max="    0.233"/>
</iteration>
<iteration count="14">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34070534 </eigenvalue_sum>
  <etotal_int>     -23.19740466 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34077523 </eigenvalue_sum>
  <etotal_int>     -23.19754192 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34083972 </eigenvalue_sum>
  <etotal_int>     -23.19766847 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34089925 </eigenvalue_sum>
  <etotal_int>     -23.19778519 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34095423 </eigenvalue_sum>
  <etotal_int>     -23.19789287 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34100501 </eigenvalue_sum>
  <etotal_int>     -23.19799225 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34105194 </eigenvalue_sum>
  <etotal_int>     -23.19808400 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34109532 </eigenvalue_sum>
  <etotal_int>     -23.19816873 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34113544 </eigenvalue_sum>
  <etotal_int>     -23.19824702 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34117256 </eigenvalue_sum>
  <etotal_int>     -23.19831937 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717850 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717743 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00718090 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000127 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000320 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000511 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025657 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025658 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025658 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000002 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000002 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000003 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103044 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103132 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103143 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000121 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000082 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000127 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951516 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951602 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951606 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000085 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000074 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000109 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387537 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387585 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387572 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000160 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000046 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000049 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268022 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268022 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268022 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005712 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005869 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005517 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000070 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000356 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000539 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90759371 </ekin>
  <econf>        0.01791977 </econf>
  <eps>         -2.61435040 </eps>
  <enl>          2.01355314 </enl>
  <ecoul>       -7.84927478 </ecoul>
  <exc>         -2.38161504 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90617361 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90617361 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00008006 0.00006531 -0.00007000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00018194 -0.00002736 0.00006763 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.68049543 </sigma_eks_xx>
   <sigma_eks_yy>  -1.72680462 </sigma_eks_yy>
   <sigma_eks_zz>  -1.62324424 </sigma_eks_zz>
   <sigma_eks_xy>  -0.02073462 </sigma_eks_xy>
   <sigma_eks_yz>  -0.10480806 </sigma_eks_yz>
   <sigma_eks_xz>   0.15854364 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.68049543 </sigma_xx>
   <sigma_yy>  -1.72680462 </sigma_yy>
   <sigma_zz>  -1.62324424 </sigma_zz>
   <sigma_xy>  -0.02073462 </sigma_xy>
   <sigma_yz>  -0.10480806 </sigma_yz>
   <sigma_xz>   0.15854364 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.220"/>
</iteration>
<iteration count="15">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34120690 </eigenvalue_sum>
  <etotal_int>     -23.19838626 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34123870 </eigenvalue_sum>
  <etotal_int>     -23.19844812 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34126814 </eigenvalue_sum>
  <etotal_int>     -23.19850536 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34129542 </eigenvalue_sum>
  <etotal_int>     -23.19855833 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34132069 </eigenvalue_sum>
  <etotal_int>     -23.19860737 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34134413 </eigenvalue_sum>
  <etotal_int>     -23.19865280 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34136586 </eigenvalue_sum>
  <etotal_int>     -23.19869488 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34138602 </eigenvalue_sum>
  <etotal_int>     -23.19873388 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34140473 </eigenvalue_sum>
  <etotal_int>     -23.19877004 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34142210 </eigenvalue_sum>
  <etotal_int>     -23.19880358 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717861 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717801 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717999 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000082 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000199 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000325 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025656 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025656 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025656 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000001 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000001 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000002 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103052 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103101 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103111 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000075 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000049 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000083 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951510 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951558 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951563 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000053 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000045 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000072 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387555 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387581 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387576 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000101 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000032 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000032 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005735 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005822 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005623 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000043 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000226 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000343 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90756470 </ekin>
  <econf>        0.01791854 </econf>
  <eps>         -2.61428402 </eps>
  <enl>          2.01346629 </enl>
  <ecoul>       -7.84925301 </ecoul>
  <exc>         -2.38161045 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90619794 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90619794 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00004635 0.00004480 -0.00004477 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00011124 -0.00001856 0.00004396 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.68718163 </sigma_eks_xx>
   <sigma_eks_yy>  -1.71282332 </sigma_eks_yy>
   <sigma_eks_zz>  -1.65445619 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01255532 </sigma_eks_xy>
   <sigma_eks_yz>  -0.06639828 </sigma_eks_yz>
   <sigma_eks_xz>   0.10077560 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.68718163 </sigma_xx>
   <sigma_yy>  -1.71282332 </sigma_yy>
   <sigma_zz>  -1.65445619 </sigma_zz>
   <sigma_xy>  -0.01255532 </sigma_xy>
   <sigma_yz>  -0.06639828 </sigma_yz>
   <sigma_xz>   0.10077560 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="16">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34143823 </eigenvalue_sum>
  <etotal_int>     -23.19883470 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34145321 </eigenvalue_sum>
  <etotal_int>     -23.19886358 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34146714 </eigenvalue_sum>
  <etotal_int>     -23.19889039 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34148008 </eigenvalue_sum>
  <etotal_int>     -23.19891529 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34149212 </eigenvalue_sum>
  <etotal_int>     -23.19893842 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34150332 </eigenvalue_sum>
  <etotal_int>     -23.19895992 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34151374 </eigenvalue_sum>
  <etotal_int>     -23.19897991 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34152343 </eigenvalue_sum>
  <etotal_int>     -23.19899850 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34153247 </eigenvalue_sum>
  <etotal_int>     -23.19901579 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34154088 </eigenvalue_sum>
  <etotal_int>     -23.19903188 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717868 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717835 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717948 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000053 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000125 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000207 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025655 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025655 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025655 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000001 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000001 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000001 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103057 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103084 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103092 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000047 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000030 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000054 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951507 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951534 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951538 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000033 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000028 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000047 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387565 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387579 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387577 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000064 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000021 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000020 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005746 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005795 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005682 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000026 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000143 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000218 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90755170 </ekin>
  <econf>        0.01791789 </econf>
  <eps>         -2.61424630 </eps>
  <enl>          2.01341703 </enl>
  <ecoul>       -7.84924036 </ecoul>
  <exc>         -2.38160750 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90620755 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90620755 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00002673 0.00003013 -0.00002860 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00006801 -0.00001231 0.00002848 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69056824 </sigma_eks_xx>
   <sigma_eks_yy>  -1.70492271 </sigma_eks_yy>
   <sigma_eks_zz>  -1.67179955 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00764224 </sigma_eks_xy>
   <sigma_eks_yz>  -0.04206841 </sigma_eks_yz>
   <sigma_eks_xz>   0.06426931 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69056824 </sigma_xx>
   <sigma_yy>  -1.70492271 </sigma_yy>
   <sigma_zz>  -1.67179955 </sigma_zz>
   <sigma_xy>  -0.00764224 </sigma_xy>
   <sigma_yz>  -0.04206841 </sigma_yz>
   <sigma_xz>   0.06426931 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.229" max="    0.235"/>
</iteration>
<iteration count="17">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34154871 </eigenvalue_sum>
  <etotal_int>     -23.19904686 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34155602 </eigenvalue_sum>
  <etotal_int>     -23.19906081 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34156283 </eigenvalue_sum>
  <etotal_int>     -23.19907380 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34156918 </eigenvalue_sum>
  <etotal_int>     -23.19908591 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34157510 </eigenvalue_sum>
  <etotal_int>     -23.19909719 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34158063 </eigenvalue_sum>
  <etotal_int>     -23.19910771 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34158579 </eigenvalue_sum>
  <etotal_int>     -23.19911752 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34159061 </eigenvalue_sum>
  <etotal_int>     -23.19912668 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34159510 </eigenvalue_sum>
  <etotal_int>     -23.19913522 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34159931 </eigenvalue_sum>
  <etotal_int>     -23.19914319 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717873 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717854 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717919 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000034 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000078 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000133 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000001 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103060 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103075 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103080 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000030 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000019 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000035 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951505 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951520 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951523 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000021 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000017 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000031 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387571 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387579 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000040 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000014 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000013 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005752 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005780 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005715 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000016 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000091 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000140 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754570 </ekin>
  <econf>        0.01791754 </econf>
  <eps>         -2.61422483 </eps>
  <enl>          2.01338899 </enl>
  <ecoul>       -7.84923306 </ecoul>
  <exc>         -2.38160570 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621137 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621137 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00001541 0.00002002 -0.00001825 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00004164 -0.00000807 0.00001839 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69232579 </sigma_eks_xx>
   <sigma_eks_yy>  -1.70042952 </sigma_eks_yy>
   <sigma_eks_zz>  -1.68153845 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00467067 </sigma_eks_xy>
   <sigma_eks_yz>  -0.02666707 </sigma_eks_yz>
   <sigma_eks_xz>   0.04105853 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69232579 </sigma_xx>
   <sigma_yy>  -1.70042952 </sigma_yy>
   <sigma_zz>  -1.68153845 </sigma_zz>
   <sigma_xy>  -0.00467067 </sigma_xy>
   <sigma_yz>  -0.02666707 </sigma_yz>
   <sigma_xz>   0.04105853 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.228" max="    0.235"/>
</iteration>
<iteration count="18">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34160324 </eigenvalue_sum>
  <etotal_int>     -23.19915063 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34160691 </eigenvalue_sum>
  <etotal_int>     -23.19915758 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34161034 </eigenvalue_sum>
  <etotal_int>     -23.19916408 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34161355 </eigenvalue_sum>
  <etotal_int>     -23.19917015 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34161655 </eigenvalue_sum>
  <etotal_int>     -23.19917582 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34161936 </eigenvalue_sum>
  <etotal_int>     -23.19918113 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34162199 </eigenvalue_sum>
  <etotal_int>     -23.19918609 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34162445 </eigenvalue_sum>
  <etotal_int>     -23.19919073 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34162675 </eigenvalue_sum>
  <etotal_int>     -23.19919507 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34162891 </eigenvalue_sum>
  <etotal_int>     -23.19919913 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717876 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717865 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717903 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000022 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000049 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000085 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000001 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103062 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103070 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103073 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000019 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000012 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000023 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951504 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951512 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951514 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000013 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000011 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000020 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387574 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000025 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000009 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000008 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005755 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005771 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005734 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000010 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000057 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000089 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754287 </ekin>
  <econf>        0.01791734 </econf>
  <eps>         -2.61421260 </eps>
  <enl>          2.01337300 </enl>
  <ecoul>       -7.84922887 </ecoul>
  <exc>         -2.38160464 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621289 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621289 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000890 0.00001320 -0.00001163 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00002556 -0.00000527 0.00001184 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69325737 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69786102 </sigma_eks_yy>
   <sigma_eks_zz>  -1.68704873 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00286408 </sigma_eks_xy>
   <sigma_eks_yz>  -0.01691523 </sigma_eks_yz>
   <sigma_eks_xz>   0.02625140 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69325737 </sigma_xx>
   <sigma_yy>  -1.69786102 </sigma_yy>
   <sigma_zz>  -1.68704873 </sigma_zz>
   <sigma_xy>  -0.00286408 </sigma_xy>
   <sigma_yz>  -0.01691523 </sigma_yz>
   <sigma_xz>   0.02625140 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.216" max="    0.223"/>
</iteration>
<iteration count="19">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34163093 </eigenvalue_sum>
  <etotal_int>     -23.19920294 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34163283 </eigenvalue_sum>
  <etotal_int>     -23.19920650 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34163460 </eigenvalue_sum>
  <etotal_int>     -23.19920984 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34163627 </eigenvalue_sum>
  <etotal_int>     -23.19921296 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34163783 </eigenvalue_sum>
  <etotal_int>     -23.19921589 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34163929 </eigenvalue_sum>
  <etotal_int>     -23.19921864 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164066 </eigenvalue_sum>
  <etotal_int>     -23.19922121 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164195 </eigenvalue_sum>
  <etotal_int>     -23.19922362 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164316 </eigenvalue_sum>
  <etotal_int>     -23.19922588 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164430 </eigenvalue_sum>
  <etotal_int>     -23.19922801 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717878 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717872 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717893 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000014 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000031 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000054 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103063 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103067 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103069 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000012 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000007 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000015 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951503 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951508 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951509 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000008 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000007 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000013 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387576 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000016 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000006 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000005 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005757 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005766 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005745 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000006 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000036 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000057 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754149 </ekin>
  <econf>        0.01791723 </econf>
  <eps>         -2.61420561 </eps>
  <enl>          2.01336386 </enl>
  <ecoul>       -7.84922646 </ecoul>
  <exc>         -2.38160402 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621350 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621350 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000515 0.00000866 -0.00000740 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00001572 -0.00000343 0.00000761 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69375983 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69638707 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69018325 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00176122 </sigma_eks_xy>
   <sigma_eks_yz>  -0.01073672 </sigma_eks_yz>
   <sigma_eks_xz>   0.01678911 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69375983 </sigma_xx>
   <sigma_yy>  -1.69638707 </sigma_yy>
   <sigma_zz>  -1.69018325 </sigma_zz>
   <sigma_xy>  -0.00176122 </sigma_xy>
   <sigma_yz>  -0.01073672 </sigma_yz>
   <sigma_xz>   0.01678911 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="20">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164536 </eigenvalue_sum>
  <etotal_int>     -23.19923000 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164636 </eigenvalue_sum>
  <etotal_int>     -23.19923187 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164730 </eigenvalue_sum>
  <etotal_int>     -23.19923362 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164818 </eigenvalue_sum>
  <etotal_int>     -23.19923527 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164901 </eigenvalue_sum>
  <etotal_int>     -23.19923681 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34164979 </eigenvalue_sum>
  <etotal_int>     -23.19923826 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165052 </eigenvalue_sum>
  <etotal_int>     -23.19923963 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165120 </eigenvalue_sum>
  <etotal_int>     -23.19924091 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165185 </eigenvalue_sum>
  <etotal_int>     -23.19924211 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165246 </eigenvalue_sum>
  <etotal_int>     -23.19924324 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717879 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717876 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717888 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000009 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000020 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000035 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103063 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103066 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103067 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000007 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000005 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000010 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951503 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951506 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951506 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000005 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000004 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000008 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387577 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000010 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000004 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000003 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005758 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005763 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005751 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000004 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000023 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000036 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754081 </ekin>
  <econf>        0.01791717 </econf>
  <eps>         -2.61420162 </eps>
  <enl>          2.01335864 </enl>
  <ecoul>       -7.84922508 </ecoul>
  <exc>         -2.38160366 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621375 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621375 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000299 0.00000565 -0.00000471 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000970 -0.00000222 0.00000488 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69403462 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69553887 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69197308 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00108564 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00681930 </sigma_eks_yz>
   <sigma_eks_xz>   0.01073769 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69403462 </sigma_xx>
   <sigma_yy>  -1.69553887 </sigma_yy>
   <sigma_zz>  -1.69197308 </sigma_zz>
   <sigma_xy>  -0.00108564 </sigma_xy>
   <sigma_yz>  -0.00681930 </sigma_yz>
   <sigma_xz>   0.01073769 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.217" max="    0.224"/>
</iteration>
<iteration count="21">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165303 </eigenvalue_sum>
  <etotal_int>     -23.19924430 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165357 </eigenvalue_sum>
  <etotal_int>     -23.19924530 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165407 </eigenvalue_sum>
  <etotal_int>     -23.19924624 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165455 </eigenvalue_sum>
  <etotal_int>     -23.19924713 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165499 </eigenvalue_sum>
  <etotal_int>     -23.19924796 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165541 </eigenvalue_sum>
  <etotal_int>     -23.19924874 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165581 </eigenvalue_sum>
  <etotal_int>     -23.19924947 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165618 </eigenvalue_sum>
  <etotal_int>     -23.19925016 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165653 </eigenvalue_sum>
  <etotal_int>     -23.19925081 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165686 </eigenvalue_sum>
  <etotal_int>     -23.19925143 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717880 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717878 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717885 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000006 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000012 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000022 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103063 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103065 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103066 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000005 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000003 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000006 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951503 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951504 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951505 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000003 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000003 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000005 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387577 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000007 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000003 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000002 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005758 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005761 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005754 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000002 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000015 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000023 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754046 </ekin>
  <econf>        0.01791714 </econf>
  <eps>         -2.61419934 </eps>
  <enl>          2.01335564 </enl>
  <ecoul>       -7.84922430 </ecoul>
  <exc>         -2.38160345 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621385 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621385 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000174 0.00000367 -0.00000300 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000600 -0.00000144 0.00000312 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69418653 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69504981 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69299780 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00067058 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00433367 </sigma_eks_yz>
   <sigma_eks_xz>   0.00686665 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69418653 </sigma_xx>
   <sigma_yy>  -1.69504981 </sigma_yy>
   <sigma_zz>  -1.69299780 </sigma_zz>
   <sigma_xy>  -0.00067058 </sigma_xy>
   <sigma_yz>  -0.00433367 </sigma_yz>
   <sigma_xz>   0.00686665 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.217" max="    0.224"/>
</iteration>
<iteration count="22">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165717 </eigenvalue_sum>
  <etotal_int>     -23.19925200 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165747 </eigenvalue_sum>
  <etotal_int>     -23.19925254 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165774 </eigenvalue_sum>
  <etotal_int>     -23.19925306 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165800 </eigenvalue_sum>
  <etotal_int>     -23.19925354 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165825 </eigenvalue_sum>
  <etotal_int>     -23.19925399 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165848 </eigenvalue_sum>
  <etotal_int>     -23.19925442 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165869 </eigenvalue_sum>
  <etotal_int>     -23.19925482 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165890 </eigenvalue_sum>
  <etotal_int>     -23.19925519 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165909 </eigenvalue_sum>
  <etotal_int>     -23.19925555 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165927 </eigenvalue_sum>
  <etotal_int>     -23.19925589 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717880 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717879 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717883 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000004 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000008 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000014 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103065 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000003 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000002 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000004 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951503 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951503 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951504 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000002 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000002 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000003 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000004 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000002 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000001 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268021 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268021 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268021 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005760 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005756 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000001 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000009 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000015 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754028 </ekin>
  <econf>        0.01791712 </econf>
  <eps>         -2.61419804 </eps>
  <enl>          2.01335393 </enl>
  <ecoul>       -7.84922384 </ecoul>
  <exc>         -2.38160334 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621389 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621389 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000102 0.00000238 -0.00000190 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000372 -0.00000093 0.00000200 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69427119 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69476744 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69358558 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00041493 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00275544 </sigma_eks_yz>
   <sigma_eks_xz>   0.00439041 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69427119 </sigma_xx>
   <sigma_yy>  -1.69476744 </sigma_yy>
   <sigma_zz>  -1.69358558 </sigma_zz>
   <sigma_xy>  -0.00041493 </sigma_xy>
   <sigma_yz>  -0.00275544 </sigma_yz>
   <sigma_xz>   0.00439041 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.223" max="    0.230"/>
</iteration>
<iteration count="23">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165944 </eigenvalue_sum>
  <etotal_int>     -23.19925620 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165960 </eigenvalue_sum>
  <etotal_int>     -23.19925650 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165976 </eigenvalue_sum>
  <etotal_int>     -23.19925678 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34165990 </eigenvalue_sum>
  <etotal_int>     -23.19925705 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166004 </eigenvalue_sum>
  <etotal_int>     -23.19925730 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166016 </eigenvalue_sum>
  <etotal_int>     -23.19925753 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166028 </eigenvalue_sum>
  <etotal_int>     -23.19925775 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166040 </eigenvalue_sum>
  <etotal_int>     -23.19925796 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166050 </eigenvalue_sum>
  <etotal_int>     -23.19925816 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166060 </eigenvalue_sum>
  <etotal_int>     -23.19925835 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717880 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717882 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000002 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000005 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000009 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000002 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000001 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000003 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951503 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951503 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000001 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000001 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000002 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000003 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000001 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000001 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005760 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005757 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000001 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000006 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000010 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754019 </ekin>
  <econf>        0.01791711 </econf>
  <eps>         -2.61419729 </eps>
  <enl>          2.01335295 </enl>
  <ecoul>       -7.84922359 </ecoul>
  <exc>         -2.38160327 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621391 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621391 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000060 0.00000154 -0.00000121 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000231 -0.00000060 0.00000128 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69431867 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69460426 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69392317 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00025713 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00175275 </sigma_eks_yz>
   <sigma_eks_xz>   0.00280663 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69431867 </sigma_xx>
   <sigma_yy>  -1.69460426 </sigma_yy>
   <sigma_zz>  -1.69392317 </sigma_zz>
   <sigma_xy>  -0.00025713 </sigma_xy>
   <sigma_yz>  -0.00175275 </sigma_yz>
   <sigma_xz>   0.00280663 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.225" max="    0.235"/>
</iteration>
<iteration count="24">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166070 </eigenvalue_sum>
  <etotal_int>     -23.19925852 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166079 </eigenvalue_sum>
  <etotal_int>     -23.19925869 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166087 </eigenvalue_sum>
  <etotal_int>     -23.19925884 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166095 </eigenvalue_sum>
  <etotal_int>     -23.19925899 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166103 </eigenvalue_sum>
  <etotal_int>     -23.19925913 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166110 </eigenvalue_sum>
  <etotal_int>     -23.19925926 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166117 </eigenvalue_sum>
  <etotal_int>     -23.19925938 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166123 </eigenvalue_sum>
  <etotal_int>     -23.19925950 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166129 </eigenvalue_sum>
  <etotal_int>     -23.19925961 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166135 </eigenvalue_sum>
  <etotal_int>     -23.19925971 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717880 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717882 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000002 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000003 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000006 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000001 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000001 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000002 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951503 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951503 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000001 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000001 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000001 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000002 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000001 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005758 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000001 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000004 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000006 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754014 </ekin>
  <econf>        0.01791710 </econf>
  <eps>         -2.61419687 </eps>
  <enl>          2.01335239 </enl>
  <ecoul>       -7.84922344 </ecoul>
  <exc>         -2.38160323 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621391 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621391 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000035 0.00000099 -0.00000077 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000144 -0.00000039 0.00000081 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69434541 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69450991 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69411725 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00015954 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00111536 </sigma_eks_yz>
   <sigma_eks_xz>   0.00179385 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69434541 </sigma_xx>
   <sigma_yy>  -1.69450991 </sigma_yy>
   <sigma_zz>  -1.69411725 </sigma_zz>
   <sigma_xy>  -0.00015954 </sigma_xy>
   <sigma_yz>  -0.00111536 </sigma_yz>
   <sigma_xz>   0.00179385 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="25">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166140 </eigenvalue_sum>
  <etotal_int>     -23.19925981 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166145 </eigenvalue_sum>
  <etotal_int>     -23.19925990 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166150 </eigenvalue_sum>
  <etotal_int>     -23.19925999 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166154 </eigenvalue_sum>
  <etotal_int>     -23.19926007 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166158 </eigenvalue_sum>
  <etotal_int>     -23.19926015 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166162 </eigenvalue_sum>
  <etotal_int>     -23.19926022 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166166 </eigenvalue_sum>
  <etotal_int>     -23.19926029 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166170 </eigenvalue_sum>
  <etotal_int>     -23.19926036 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166173 </eigenvalue_sum>
  <etotal_int>     -23.19926042 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166176 </eigenvalue_sum>
  <etotal_int>     -23.19926048 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717880 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717881 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000001 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000002 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000004 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000001 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000000 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000001 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951503 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951503 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000001 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000000 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000001 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000001 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000000 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005758 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000000 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000002 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000004 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754011 </ekin>
  <econf>        0.01791710 </econf>
  <eps>         -2.61419662 </eps>
  <enl>          2.01335206 </enl>
  <ecoul>       -7.84922336 </ecoul>
  <exc>         -2.38160321 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621392 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621392 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000021 0.00000064 -0.00000049 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000090 -0.00000025 0.00000052 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69436053 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69445533 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69422889 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00009910 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00071000 </sigma_eks_yz>
   <sigma_eks_xz>   0.00114635 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69436053 </sigma_xx>
   <sigma_yy>  -1.69445533 </sigma_yy>
   <sigma_zz>  -1.69422889 </sigma_zz>
   <sigma_xy>  -0.00009910 </sigma_xy>
   <sigma_yz>  -0.00071000 </sigma_yz>
   <sigma_xz>   0.00114635 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.295" max="    0.302"/>
</iteration>
<iteration count="26">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166179 </eigenvalue_sum>
  <etotal_int>     -23.19926053 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166182 </eigenvalue_sum>
  <etotal_int>     -23.19926059 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166185 </eigenvalue_sum>
  <etotal_int>     -23.19926063 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166187 </eigenvalue_sum>
  <etotal_int>     -23.19926068 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166189 </eigenvalue_sum>
  <etotal_int>     -23.19926072 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166192 </eigenvalue_sum>
  <etotal_int>     -23.19926077 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166194 </eigenvalue_sum>
  <etotal_int>     -23.19926080 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166196 </eigenvalue_sum>
  <etotal_int>     -23.19926084 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166198 </eigenvalue_sum>
  <etotal_int>     -23.19926088 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166200 </eigenvalue_sum>
  <etotal_int>     -23.19926091 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717881 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717881 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000001 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000001 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000002 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000000 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000000 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000001 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951502 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951503 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000000 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000000 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000001 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000001 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000000 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005759 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000000 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000002 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000002 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754010 </ekin>
  <econf>        0.01791709 </econf>
  <eps>         -2.61419648 </eps>
  <enl>          2.01335188 </enl>
  <ecoul>       -7.84922331 </ecoul>
  <exc>         -2.38160320 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621392 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621392 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000012 0.00000041 -0.00000031 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000056 -0.00000016 0.00000033 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69436909 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69442375 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69429314 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00006160 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00045209 </sigma_eks_yz>
   <sigma_eks_xz>   0.00073246 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69436909 </sigma_xx>
   <sigma_yy>  -1.69442375 </sigma_yy>
   <sigma_zz>  -1.69429314 </sigma_zz>
   <sigma_xy>  -0.00006160 </sigma_xy>
   <sigma_yz>  -0.00045209 </sigma_yz>
   <sigma_xz>   0.00073246 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.264" max="    0.271"/>
</iteration>
<iteration count="27">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166201 </eigenvalue_sum>
  <etotal_int>     -23.19926094 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166203 </eigenvalue_sum>
  <etotal_int>     -23.19926097 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166204 </eigenvalue_sum>
  <etotal_int>     -23.19926100 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166206 </eigenvalue_sum>
  <etotal_int>     -23.19926102 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166207 </eigenvalue_sum>
  <etotal_int>     -23.19926105 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166208 </eigenvalue_sum>
  <etotal_int>     -23.19926107 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166210 </eigenvalue_sum>
  <etotal_int>     -23.19926109 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166211 </eigenvalue_sum>
  <etotal_int>     -23.19926111 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166212 </eigenvalue_sum>
  <etotal_int>     -23.19926113 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166213 </eigenvalue_sum>
  <etotal_int>     -23.19926115 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717881 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717881 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000000 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000001 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000002 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000000 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000000 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000000 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951502 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951502 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000000 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000000 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000000 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000000 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000000 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005759 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000000 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000001 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000002 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754009 </ekin>
  <econf>        0.01791709 </econf>
  <eps>         -2.61419640 </eps>
  <enl>          2.01335177 </enl>
  <ecoul>       -7.84922328 </ecoul>
  <exc>         -2.38160319 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621392 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621392 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000007 0.00000026 -0.00000020 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000035 -0.00000010 0.00000021 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69437396 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69440547 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69433014 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00003832 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00028794 </sigma_eks_yz>
   <sigma_eks_xz>   0.00046795 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69437396 </sigma_xx>
   <sigma_yy>  -1.69440547 </sigma_yy>
   <sigma_zz>  -1.69433014 </sigma_zz>
   <sigma_xy>  -0.00003832 </sigma_xy>
   <sigma_yz>  -0.00028794 </sigma_yz>
   <sigma_xz>   0.00046795 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="28">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166214 </eigenvalue_sum>
  <etotal_int>     -23.19926117 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166215 </eigenvalue_sum>
  <etotal_int>     -23.19926119 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166215 </eigenvalue_sum>
  <etotal_int>     -23.19926120 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166216 </eigenvalue_sum>
  <etotal_int>     -23.19926122 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166217 </eigenvalue_sum>
  <etotal_int>     -23.19926123 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166218 </eigenvalue_sum>
  <etotal_int>     -23.19926124 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166218 </eigenvalue_sum>
  <etotal_int>     -23.19926126 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166219 </eigenvalue_sum>
  <etotal_int>     -23.19926127 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166220 </eigenvalue_sum>
  <etotal_int>     -23.19926128 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166220 </eigenvalue_sum>
  <etotal_int>     -23.19926129 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717881 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717881 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000000 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000001 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000001 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000000 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000000 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000000 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951502 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951502 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000000 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000000 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000000 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000000 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000000 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005759 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000000 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000001 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000001 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754009 </ekin>
  <econf>        0.01791709 </econf>
  <eps>         -2.61419636 </eps>
  <enl>          2.01335171 </enl>
  <ecoul>       -7.84922326 </ecoul>
  <exc>         -2.38160319 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621392 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621392 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000004 0.00000017 -0.00000013 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000022 -0.00000007 0.00000013 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69437672 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69439490 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69435144 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00002386 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00018343 </sigma_eks_yz>
   <sigma_eks_xz>   0.00029892 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69437672 </sigma_xx>
   <sigma_yy>  -1.69439490 </sigma_yy>
   <sigma_zz>  -1.69435144 </sigma_zz>
   <sigma_xy>  -0.00002386 </sigma_xy>
   <sigma_yz>  -0.00018343 </sigma_yz>
   <sigma_xz>   0.00029892 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.214" max="    0.221"/>
</iteration>
<iteration count="29">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166221 </eigenvalue_sum>
  <etotal_int>     -23.19926130 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166221 </eigenvalue_sum>
  <etotal_int>     -23.19926131 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166222 </eigenvalue_sum>
  <etotal_int>     -23.19926132 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166222 </eigenvalue_sum>
  <etotal_int>     -23.19926133 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166223 </eigenvalue_sum>
  <etotal_int>     -23.19926133 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166223 </eigenvalue_sum>
  <etotal_int>     -23.19926134 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166224 </eigenvalue_sum>
  <etotal_int>     -23.19926135 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166224 </eigenvalue_sum>
  <etotal_int>     -23.19926136 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166224 </eigenvalue_sum>
  <etotal_int>     -23.19926136 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166225 </eigenvalue_sum>
  <etotal_int>     -23.19926137 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717881 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717881 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000000 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000000 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000001 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000000 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000000 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000000 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951502 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951502 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000000 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000000 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000000 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000000 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000000 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005759 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000000 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000000 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000001 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754008 </ekin>
  <econf>        0.01791709 </econf>
  <eps>         -2.61419633 </eps>
  <enl>          2.01335168 </enl>
  <ecoul>       -7.84922325 </ecoul>
  <exc>         -2.38160318 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621392 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621392 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000003 0.00000011 -0.00000008 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000014 -0.00000004 0.00000009 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69437829 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69438878 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69436371 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00001486 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00011688 </sigma_eks_yz>
   <sigma_eks_xz>   0.00019094 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69437829 </sigma_xx>
   <sigma_yy>  -1.69438878 </sigma_yy>
   <sigma_zz>  -1.69436371 </sigma_zz>
   <sigma_xy>  -0.00001486 </sigma_xy>
   <sigma_yz>  -0.00011688 </sigma_yz>
   <sigma_xz>   0.00019094 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.219" max="    0.226"/>
</iteration>
<iteration count="30">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166225 </eigenvalue_sum>
  <etotal_int>     -23.19926137 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166225 </eigenvalue_sum>
  <etotal_int>     -23.19926138 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166225 </eigenvalue_sum>
  <etotal_int>     -23.19926138 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166226 </eigenvalue_sum>
  <etotal_int>     -23.19926139 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166226 </eigenvalue_sum>
  <etotal_int>     -23.19926139 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166226 </eigenvalue_sum>
  <etotal_int>     -23.19926140 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166226 </eigenvalue_sum>
  <etotal_int>     -23.19926140 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166227 </eigenvalue_sum>
  <etotal_int>     -23.19926141 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166227 </eigenvalue_sum>
  <etotal_int>     -23.19926141 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166227 </eigenvalue_sum>
  <etotal_int>     -23.19926141 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717881 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717881 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000000 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000000 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000000 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000000 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000000 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000000 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951502 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951502 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000000 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000000 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000000 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000000 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000000 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005759 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000000 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000000 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000000 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754008 </ekin>
  <econf>        0.01791709 </econf>
  <eps>         -2.61419632 </eps>
  <enl>          2.01335166 </enl>
  <ecoul>       -7.84922325 </ecoul>
  <exc>         -2.38160318 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621392 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621392 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000002 0.00000007 -0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000009 -0.00000003 0.00000005 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69437919 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69438524 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69437077 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000925 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00007448 </sigma_eks_yz>
   <sigma_eks_xz>   0.00012195 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69437919 </sigma_xx>
   <sigma_yy>  -1.69438524 </sigma_yy>
   <sigma_zz>  -1.69437077 </sigma_zz>
   <sigma_xy>  -0.00000925 </sigma_xy>
   <sigma_yz>  -0.00007448 </sigma_yz>
   <sigma_xz>   0.00012195 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.213" max="    0.220"/>
</iteration>
<timing name="         charge" min="    2.950" max="    2.986"/>
<timing name="         energy" min="    3.027" max="    3.112"/>
<timing name="           gram" min="    0.177" max="    0.177"/>
<timing name="   psd_residual" min="    0.122" max="    0.166"/>
<timing name="  psd_update_wf" min="    0.021" max="    0.022"/>
<timing name="    update_vhxc" min="    0.184" max="    0.189"/>
<timing name="      wf_update" min="    0.372" max="    0.417"/>
<timing name="           ekin" min="    0.048" max="    0.051"/>
<timing name="            exc" min="    0.122" max="    0.127"/>
<timing name="           hpsi" min="    2.594" max="    2.596"/>
<timing name="       nonlocal" min="    0.374" max="    0.376"/>
<timing name=" charge_compute" min="    2.850" max="    2.884"/>
<timing name="charge_integral" min="    0.011" max="    0.015"/>
<timing name="  charge_rowsum" min="    0.003" max="    0.004"/>
<timing name="     charge_vft" min="    0.044" max="    0.084"/>
[qbox] <cmd>set wf_diag T</cmd>
[qbox] <cmd>run 0</cmd>
  EnergyFunctional: np0v,np1v,np2v: 24 24 24
  EnergyFunctional: vft->np012(): 13824
<wavefunction ecut="7.500" nspin="1" nel="8" nempty="0">
<cell a="5.130000 5.130000 0.000000"
      b="0.000000 5.130000 5.130000"
      c="5.130000 0.000000 5.130000"/>
 reciprocal lattice vectors
 0.612396 0.612396 -0.612396
 -0.612396 0.612396 0.612396
 0.612396 -0.612396 0.612396
<refcell a="5.500000 5.500000 0.000000"
         b="0.000000 5.500000 5.500000"
         c="5.500000 0.000000 5.500000"/>
<grid nx="12" ny="12" nz="12"/>
 kpoint: 0.458800 0.147650 0.311150 weight: 0.083333
<slater_determinant kpoint="0.458800 0.147650 0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: -0.163500 0.147650 -0.311150 weight: 0.083333
<slater_determinant kpoint="-0.163500 0.147650 -0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.458800 0.311150 0.147650 weight: 0.083333
<slater_determinant kpoint="0.458800 0.311150 0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.163500 0.311150 -0.147650 weight: 0.083333
<slater_determinant kpoint="0.163500 0.311150 -0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.311150 0.458800 0.147650 weight: 0.083333
<slater_determinant kpoint="0.311150 0.458800 0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: -0.311150 -0.163500 0.147650 weight: 0.083333
<slater_determinant kpoint="-0.311150 -0.163500 0.147650" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.147650 0.458800 0.311150 weight: 0.083333
<slater_determinant kpoint="0.147650 0.458800 0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: -0.147650 0.163500 0.311150 weight: 0.083333
<slater_determinant kpoint="-0.147650 0.163500 0.311150" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.147650 0.311150 0.458800 weight: 0.083333
<slater_determinant kpoint="0.147650 0.311150 0.458800" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.147650 -0.311150 -0.163500 weight: 0.083333
<slater_determinant kpoint="0.147650 -0.311150 -0.163500" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.311150 0.147650 0.458800 weight: 0.083333
<slater_determinant kpoint="0.311150 0.147650 0.458800" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
 kpoint: 0.311150 -0.147650 0.163500 weight: 0.083333
<slater_determinant kpoint="0.311150 -0.147650 0.163500" size="4">
 sdcontext: 4x1
 basis size: 328
 c dimensions: 340x4   (85x4 blocks)
 <density_matrix form="diagonal" size="4">
 </density_matrix>
</slater_determinant>
</wavefunction>
<iteration count="1">
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34166227 </eigenvalue_sum>
<eigenset>
  <eigenvalues spin="0" kpoint="0.45880000 0.14765000 0.31115000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="-0.16350000 0.14765000 -0.31115000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.45880000 0.31115000 0.14765000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.16350000 0.31115000 -0.14765000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.31115000 0.45880000 0.14765000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="-0.31115000 -0.16350000 0.14765000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.14765000 0.45880000 0.31115000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="-0.14765000 0.16350000 0.31115000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.14765000 0.31115000 0.45880000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.14765000 -0.31115000 -0.16350000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.31115000 0.14765000 0.45880000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
  <eigenvalues spin="0" kpoint="0.31115000 -0.14765000 0.16350000" weight="0.08333333" n="4">
    -9.42960    -4.74765    -2.98236    -1.75622
  </eigenvalues>
</eigenset>
  <etotal_int>     -23.19926142 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00717881 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00717881 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717881 </sigma_ekin_zz>
   <sigma_ekin_xy>   0.00000000 </sigma_ekin_xy>
   <sigma_ekin_yz>  -0.00000000 </sigma_ekin_yz>
   <sigma_ekin_xz>   0.00000000 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025654 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>  -0.00000000 </sigma_econf_xy>
   <sigma_econf_yz>   0.00000000 </sigma_econf_yz>
   <sigma_econf_xz>  -0.00000000 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103064 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103064 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103064 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000000 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000000 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000000 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951502 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951502 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951502 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000000 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000000 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000000 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387578 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387578 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387578 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000000 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000000 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000000 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268020 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268020 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268020 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057867 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057867 </sigma_esr_yy>
   <sigma_esr_zz>   0.00057867 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000000 </sigma_esr_xy>
   <sigma_esr_yz>   0.00000000 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000000 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005759 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005759 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005759 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000000 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000000 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000000 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90754008 </ekin>
  <econf>        0.01791709 </econf>
  <eps>         -2.61419631 </eps>
  <enl>          2.01335165 </enl>
  <ecoul>       -7.84922325 </ecoul>
  <exc>         -2.38160318 </exc>
  <esr>          0.04409336 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90621392 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90621392 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13000000   5.13000000   0.00000000"
    b="  0.00000000   5.13000000   5.13000000"
    c="  5.13000000   0.00000000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.28250000 1.28250000 1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000001 0.00000007 -0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28250000 -1.28250000 -1.28250000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000008 -0.00000003 0.00000005 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.254916 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254916 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254916 </unit_cell_c_norm>
<unit_cell_alpha>  60.000 </unit_cell_alpha>
<unit_cell_beta>   60.000 </unit_cell_beta>
<unit_cell_gamma>  60.000 </unit_cell_gamma>
<unit_cell_volume> 270.011 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.69437925 </sigma_eks_xx>
   <sigma_eks_yy>  -1.69438498 </sigma_eks_yy>
   <sigma_eks_zz>  -1.69437129 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000883 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00007120 </sigma_eks_yz>
   <sigma_eks_xz>   0.00011660 </sigma_eks_xz>

   <sigma_kin_xx>   0.00000000 </sigma_kin_xx>
   <sigma_kin_yy>   0.00000000 </sigma_kin_yy>
   <sigma_kin_zz>   0.00000000 </sigma_kin_zz>
   <sigma_kin_xy>   0.00000000 </sigma_kin_xy>
   <sigma_kin_yz>   0.00000000 </sigma_kin_yz>
   <sigma_kin_xz>   0.00000000 </sigma_kin_xz>

   <sigma_ext_xx>   0.00000000 </sigma_ext_xx>
   <sigma_ext_yy>   0.00000000 </sigma_ext_yy>
   <sigma_ext_zz>   0.00000000 </sigma_ext_zz>
   <sigma_ext_xy>   0.00000000 </sigma_ext_xy>
   <sigma_ext_yz>   0.00000000 </sigma_ext_yz>
   <sigma_ext_xz>   0.00000000 </sigma_ext_xz>

   <sigma_xx>  -1.69437925 </sigma_xx>
   <sigma_yy>  -1.69438498 </sigma_yy>
   <sigma_zz>  -1.69437129 </sigma_zz>
   <sigma_xy>  -0.00000883 </sigma_xy>
   <sigma_yz>  -0.00007120 </sigma_yz>
   <sigma_xz>   0.00011660 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.161" max="    0.168"/>
</iteration>
<timing name="         charge" min="    0.018" max="    0.023"/>
<timing name="         energy" min="    0.021" max="    0.024"/>
<timing name="           gram" min="    0.001" max="    0.001"/>
<timing name="   psd_residual" min="    0.000" max="    0.000"/>
<timing name="  psd_update_wf" min="    0.000" max="    0.000"/>
<timing name="    update_vhxc" min="    0.001" max="    0.001"/>
<timing name="      wf_update" min="    0.001" max="    0.001"/>
<timing name="         wfdiag" min="    0.114" max="    0.114"/>
<timing name="           ekin" min="    0.000" max="    0.000"/>
<timing name="            exc" min="    0.001" max="    0.001"/>
<timing name="           hpsi" min="    0.017" max="    0.017"/>
<timing name="       nonlocal" min="    0.004" max="    0.004"/>
<timing name=" charge_compute" min="    0.018" max="    0.023"/>
<timing name="charge_integral" min="    0.000" max="    0.000"/>
<timing name="  charge_rowsum" min="    0.000" max="    0.000"/>
<timing name="     charge_vft" min="    0.000" max="    0.000"/>
[qbox] <cmd>save test.xml</cmd>
 SampleWriter: write time: 0.011 s
 SampleWriter: file size: 1920297
 SampleWriter: aggregate write rate: 161.35 MB/s
[qbox]  End of command stream 
<real_time> 7.18 </real_time>
<end_time> 2016-04-06T12:25:08Z </end_time>
</fpmd:simulation>
