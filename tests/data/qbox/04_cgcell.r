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
<start_time> 2016-04-06T12:25:08Z </start_time>
<mpi_processes count="4">
<process id="0"> theobook68 </process>
<process id="1"> theobook68 </process>
<process id="2"> theobook68 </process>
<process id="3"> theobook68 </process>
</mpi_processes>
[qbox] <cmd># cgcell.i</cmd>
[qbox] <cmd># test cell_dyn=CG option</cmd>
[qbox] [qbox] <cmd>load ../si2gs/test.xml</cmd>
 LoadCmd: loading from ../si2gs/test.xml
 XMLGFPreprocessor: reading from ../si2gs/test.xml size: 1920297
 XMLGFPreprocessor: read time: 0.0006859
 XMLGFPreprocessor: local read rate: 667.5 MB/s  aggregate read rate: 2670 MB/s
 XMLGFPreprocessor: tag fixing time: 0.000366
 XMLGFPreprocessor: segment definition time: 0.001754
 XMLGFPreprocessor: boundary adjustment time: 0.000468
 XMLGFPreprocessor: transcoding time: 0.001486
 XMLGFPreprocessor: data redistribution time: 0.001587
 XMLGFPreprocessor: XML compacting time: 0.0001781
 XMLGFPreprocessor: total time: 0.007608
 xmlcontent.size(): 126201
 Starting XML parsing

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
 <mass>28.09</mass>
 <norm_conserving_pseudopotential>
 <valence_charge>4</valence_charge>
 <lmax>2</lmax>
 <llocal>2</llocal>
 <nquad>0</nquad>
 <rquad>0</rquad>
 <mesh_spacing>0.01</mesh_spacing>
 </norm_conserving_pseudopotential>
</species>
 Kleinman-Bylander potential
 rcps_ =   1.5
 WavefunctionHandler::startElement: wavefunction nspin=1 nel=8 nempty=0
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.4588 0.1477 0.3111 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=-0.1635 0.1477 -0.3111 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.4588 0.3111 0.1477 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.1635 0.3111 -0.1477 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.3111 0.4588 0.1477 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=-0.3111 -0.1635 0.1477 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.1477 0.4588 0.3111 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=-0.1477 0.1635 0.3111 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.1477 0.3111 0.4588 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.1477 -0.3111 -0.1635 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.3111 0.1477 0.4588 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0.3111 -0.1477 0.1635 weight=0.08333 size=4
 WavefunctionHandler::endElement: slater_determinant
 XML parsing done
 SampleReader: read time: 0.04374 s
[qbox] <cmd>set stress ON</cmd>
[qbox] <cmd>set debug STRESS</cmd>
[qbox] <cmd>set ecut 15 </cmd>
[qbox] <cmd>set ecuts 10</cmd>
[qbox] <cmd>set wf_dyn PSD</cmd>
[qbox] <cmd>set ecutprec 4</cmd>
[qbox] [qbox] <cmd>set cell_dyn CG</cmd>
[qbox] <cmd>move Si1 by  0.01 -0.02 -0.005</cmd>
 MoveCmd: atom Si1 moved to 1.292 1.262 1.278
[qbox] <cmd>move Si2 by -0.01  0.02  0.005</cmd>
 MoveCmd: atom Si2 moved to -1.292 -1.262 -1.278
[qbox] <cmd>strain 0 0 0 0.01 0 0</cmd>
<unit_cell 
    a="  5.18130000   5.18130000   0.00000000"
    b="  0.05130000   5.13000000   5.13000000"
    c="  5.13000000   0.05130000   5.13000000" />
[qbox] <cmd>run 0 30</cmd>
  EnergyFunctional: np0v,np1v,np2v: 24 24 24
  EnergyFunctional: vft->np012(): 13824
<wavefunction ecut="7.50000000" nspin="1" nel="8" nempty="0">
<cell a="5.181300 5.181300 0.000000"
      b="0.051300 5.130000 5.130000"
      c="5.130000 0.051300 5.130000"/>
 reciprocal lattice vectors
 0.606333 0.606333 -0.612396
 -0.618582 0.618582 0.612396
 0.618582 -0.618582 0.612396
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
  <eigenvalue_sum>  -8.33575087 </eigenvalue_sum>
  <etotal_int>     -23.18697975 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33890055 </eigenvalue_sum>
  <etotal_int>     -23.19330541 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34008073 </eigenvalue_sum>
  <etotal_int>     -23.19571474 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34052057 </eigenvalue_sum>
  <etotal_int>     -23.19664237 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34067917 </eigenvalue_sum>
  <etotal_int>     -23.19699965 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34073218 </eigenvalue_sum>
  <etotal_int>     -23.19713712 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34074769 </eigenvalue_sum>
  <etotal_int>     -23.19719205 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34075186 </eigenvalue_sum>
  <etotal_int>     -23.19721833 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34075429 </eigenvalue_sum>
  <etotal_int>     -23.19723657 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34075805 </eigenvalue_sum>
  <etotal_int>     -23.19725403 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34076369 </eigenvalue_sum>
  <etotal_int>     -23.19727270 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34077090 </eigenvalue_sum>
  <etotal_int>     -23.19729263 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34077913 </eigenvalue_sum>
  <etotal_int>     -23.19731324 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34078790 </eigenvalue_sum>
  <etotal_int>     -23.19733389 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34079680 </eigenvalue_sum>
  <etotal_int>     -23.19735404 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34080553 </eigenvalue_sum>
  <etotal_int>     -23.19737329 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34081388 </eigenvalue_sum>
  <etotal_int>     -23.19739138 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34082174 </eigenvalue_sum>
  <etotal_int>     -23.19740816 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34082902 </eigenvalue_sum>
  <etotal_int>     -23.19742357 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34083570 </eigenvalue_sum>
  <etotal_int>     -23.19743759 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34084177 </eigenvalue_sum>
  <etotal_int>     -23.19745027 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34084725 </eigenvalue_sum>
  <etotal_int>     -23.19746166 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34085215 </eigenvalue_sum>
  <etotal_int>     -23.19747184 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34085651 </eigenvalue_sum>
  <etotal_int>     -23.19748088 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34086037 </eigenvalue_sum>
  <etotal_int>     -23.19748888 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34086377 </eigenvalue_sum>
  <etotal_int>     -23.19749592 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34086673 </eigenvalue_sum>
  <etotal_int>     -23.19750208 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34086931 </eigenvalue_sum>
  <etotal_int>     -23.19750745 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34087153 </eigenvalue_sum>
  <etotal_int>     -23.19751209 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34087343 </eigenvalue_sum>
  <etotal_int>     -23.19751608 </etotal_int>
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718122 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00718130 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717945 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00005221 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000989 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002107 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025650 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025648 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025651 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000035 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000012 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000039 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103356 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103236 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103519 </sigma_eps_zz>
   <sigma_eps_xy>   0.00003770 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002774 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005544 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951734 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951660 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951827 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00002369 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001624 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003221 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387616 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387682 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387500 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001341 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001991 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00004015 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268058 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268058 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268058 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057960 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057893 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058074 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00002300 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001703 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003318 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005564 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005645 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005581 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00007426 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001567 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002941 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90799707 </ekin>
  <econf>        0.01791458 </econf>
  <eps>         -2.61463561 </eps>
  <enl>          2.01362215 </enl>
  <ecoul>       -7.84911861 </ecoul>
  <exc>         -2.38169484 </exc>
  <esr>          0.04421525 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90591524 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90591524 </enthalpy>
<atomset>
<unit_cell 
    a="  5.18130000   5.18130000   0.00000000"
    b="  0.05130000   5.13000000   5.13000000"
    c="  5.13000000   0.05130000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.30512500 1.27542500 1.27750000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00274826 0.00531202 -0.00271186 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30512500 -1.27542500 -1.27750000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00274827 -0.00531201 0.00271186 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.327465 </unit_cell_a_norm>
<unit_cell_b_norm> 7.255097 </unit_cell_b_norm>
<unit_cell_c_norm> 7.255097 </unit_cell_c_norm>
<unit_cell_alpha>  59.338 </unit_cell_alpha>
<unit_cell_beta>   59.669 </unit_cell_beta>
<unit_cell_gamma>  59.669 </unit_cell_gamma>
<unit_cell_volume> 269.984 </unit_cell_volume>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.63707739 </sigma_eks_xx>
   <sigma_eks_yy>  -1.66089678 </sigma_eks_yy>
   <sigma_eks_zz>  -1.64201435 </sigma_eks_zz>
   <sigma_eks_xy>  -2.18497488 </sigma_eks_xy>
   <sigma_eks_yz>  -0.46108436 </sigma_eks_yz>
   <sigma_eks_xz>   0.86523495 </sigma_eks_xz>

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

   <sigma_xx>  -1.63707739 </sigma_xx>
   <sigma_yy>  -1.66089678 </sigma_yy>
   <sigma_zz>  -1.64201435 </sigma_zz>
   <sigma_xy>  -2.18497488 </sigma_xy>
   <sigma_yz>  -0.46108436 </sigma_yz>
   <sigma_xz>   0.86523495 </sigma_xz>
 </stress_tensor>
  <timing name="iteration" min="    0.633" max="    0.639"/>
</iteration>
<timing name="         charge" min="    0.273" max="    0.275"/>
<timing name="         energy" min="    0.296" max="    0.299"/>
<timing name="           gram" min="    0.018" max="    0.018"/>
<timing name="   psd_residual" min="    0.011" max="    0.016"/>
<timing name="  psd_update_wf" min="    0.002" max="    0.002"/>
<timing name="    update_vhxc" min="    0.017" max="    0.018"/>
<timing name="      wf_update" min="    0.037" max="    0.041"/>
<timing name="           ekin" min="    0.005" max="    0.006"/>
<timing name="            exc" min="    0.011" max="    0.011"/>
<timing name="           hpsi" min="    0.249" max="    0.250"/>
<timing name="       nonlocal" min="    0.041" max="    0.041"/>
<timing name=" charge_compute" min="    0.264" max="    0.267"/>
<timing name="charge_integral" min="    0.001" max="    0.001"/>
<timing name="  charge_rowsum" min="    0.000" max="    0.001"/>
<timing name="     charge_vft" min="    0.004" max="    0.007"/>
[qbox] <cmd>set cell_dyn CG</cmd>
[qbox] <cmd>run 50 10 </cmd>
  EnergyFunctional: np0v,np1v,np2v: 24 24 24
  EnergyFunctional: vft->np012(): 13824
<wavefunction ecut="7.500" nspin="1" nel="8" nempty="0">
<cell a="5.181300 5.181300 0.000000"
      b="0.051300 5.130000 5.130000"
      c="5.130000 0.051300 5.130000"/>
 reciprocal lattice vectors
 0.606333 0.606333 -0.612396
 -0.618582 0.618582 0.612396
 0.618582 -0.618582 0.612396
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
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718122 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00718130 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00717945 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00005221 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000989 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002107 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025650 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025648 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025651 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000035 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000012 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000039 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103356 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103236 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103519 </sigma_eps_zz>
   <sigma_eps_xy>   0.00003770 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002774 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005544 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951734 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951660 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951827 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00002369 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001624 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003221 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387616 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387682 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387500 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001341 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001991 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00004015 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268058 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268058 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268058 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057960 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057893 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058074 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00002300 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001703 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003318 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005564 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005645 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005581 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00007426 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001567 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002941 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90799707 </ekin>
  <econf>        0.01791458 </econf>
  <eps>         -2.61463561 </eps>
  <enl>          2.01362215 </enl>
  <ecoul>       -7.84911861 </ecoul>
  <exc>         -2.38169484 </exc>
  <esr>          0.04421525 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90591524 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90591524 </enthalpy>
<atomset>
<unit_cell 
    a="  5.18130000   5.18130000   0.00000000"
    b="  0.05130000   5.13000000   5.13000000"
    c="  5.13000000   0.05130000   5.13000000" />
  <atom name="Si1" species="silicon">
    <position> 1.30512500 1.27542500 1.27750000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00274826 0.00531202 -0.00271186 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30512500 -1.27542500 -1.27750000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00274827 -0.00531201 0.00271186 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.327465 </unit_cell_a_norm>
<unit_cell_b_norm> 7.255097 </unit_cell_b_norm>
<unit_cell_c_norm> 7.255097 </unit_cell_c_norm>
<unit_cell_alpha>  59.338 </unit_cell_alpha>
<unit_cell_beta>   59.669 </unit_cell_beta>
<unit_cell_gamma>  59.669 </unit_cell_gamma>
<unit_cell_volume> 269.984 </unit_cell_volume>
  <econst> -7.90591524 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.63707739 </sigma_eks_xx>
   <sigma_eks_yy>  -1.66089678 </sigma_eks_yy>
   <sigma_eks_zz>  -1.64201435 </sigma_eks_zz>
   <sigma_eks_xy>  -2.18497488 </sigma_eks_xy>
   <sigma_eks_yz>  -0.46108436 </sigma_eks_yz>
   <sigma_eks_xz>   0.86523495 </sigma_eks_xz>

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

   <sigma_xx>  -1.63707739 </sigma_xx>
   <sigma_yy>  -1.66089678 </sigma_yy>
   <sigma_zz>  -1.64201435 </sigma_zz>
   <sigma_xy>  -2.18497488 </sigma_xy>
   <sigma_yz>  -0.46108436 </sigma_yz>
   <sigma_xz>   0.86523495 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.00200000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34028044 </eigenvalue_sum>
  <etotal_int>     -23.19643283 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34036241 </eigenvalue_sum>
  <etotal_int>     -23.19658349 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34041904 </eigenvalue_sum>
  <etotal_int>     -23.19668767 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34045892 </eigenvalue_sum>
  <etotal_int>     -23.19676110 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34048753 </eigenvalue_sum>
  <etotal_int>     -23.19681383 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34050845 </eigenvalue_sum>
  <etotal_int>     -23.19685242 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34052401 </eigenvalue_sum>
  <etotal_int>     -23.19688118 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34053578 </eigenvalue_sum>
  <etotal_int>     -23.19690297 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34054484 </eigenvalue_sum>
  <etotal_int>     -23.19691975 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34055190 </eigenvalue_sum>
  <etotal_int>     -23.19693287 </etotal_int>
  <timing name="iteration" min="    0.222" max="    0.222"/>
</iteration>
<iteration count="2">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718220 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00718227 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00718024 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00004939 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001007 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002138 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025653 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025651 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025654 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000032 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000012 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000040 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103505 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103383 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103666 </sigma_eps_zz>
   <sigma_eps_xy>   0.00003743 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002779 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005561 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951851 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951775 </sigma_enl_yy>
   <sigma_enl_zz>   0.00951943 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00002350 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001629 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003235 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387640 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387704 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387523 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001254 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001969 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003968 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268088 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268088 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268088 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00057980 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057914 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058093 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00002288 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001699 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003312 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005529 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005608 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005563 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00007057 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001523 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002855 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90810430 </ekin>
  <econf>        0.01791532 </econf>
  <eps>         -2.61473054 </eps>
  <enl>          2.01367270 </enl>
  <ecoul>       -7.84913837 </ecoul>
  <exc>         -2.38174461 </exc>
  <esr>          0.04422848 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90592120 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90592120 </enthalpy>
<atomset>
<unit_cell 
    a="  5.18093655   5.18093429   0.00003843"
    b="  0.05117420   5.12979816   5.12980281"
    c="  5.12992527   0.05104931   5.12992643" />
  <atom name="Si1" species="silicon">
    <position> 1.30504943 1.27533360 1.27746601 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00269779 0.00521572 -0.00262070 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30504943 -1.27533360 -1.27746601 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00269780 -0.00521571 0.00262070 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.326949 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254814 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254990 </unit_cell_c_norm>
<unit_cell_alpha>  59.340 </unit_cell_alpha>
<unit_cell_beta>   59.671 </unit_cell_beta>
<unit_cell_gamma>  59.670 </unit_cell_gamma>
<unit_cell_volume> 269.960 </unit_cell_volume>
  <econst> -7.90592120 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.62664726 </sigma_eks_xx>
   <sigma_eks_yy>  -1.65007669 </sigma_eks_yy>
   <sigma_eks_zz>  -1.63666543 </sigma_eks_zz>
   <sigma_eks_xy>  -2.07640420 </sigma_eks_xy>
   <sigma_eks_yz>  -0.44810354 </sigma_eks_yz>
   <sigma_eks_xz>   0.83999855 </sigma_eks_xz>

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

   <sigma_xx>  -1.62664726 </sigma_xx>
   <sigma_yy>  -1.65007669 </sigma_yy>
   <sigma_zz>  -1.63666543 </sigma_zz>
   <sigma_xy>  -2.07640420 </sigma_xy>
   <sigma_yz>  -0.44810354 </sigma_yz>
   <sigma_xz>   0.83999855 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.00420000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33990300 </eigenvalue_sum>
  <etotal_int>     -23.19574703 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33999620 </eigenvalue_sum>
  <etotal_int>     -23.19591804 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34006092 </eigenvalue_sum>
  <etotal_int>     -23.19603682 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34010676 </eigenvalue_sum>
  <etotal_int>     -23.19612097 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34013989 </eigenvalue_sum>
  <etotal_int>     -23.19618179 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34016429 </eigenvalue_sum>
  <etotal_int>     -23.19622661 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34018262 </eigenvalue_sum>
  <etotal_int>     -23.19626029 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34019664 </eigenvalue_sum>
  <etotal_int>     -23.19628607 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34020757 </eigenvalue_sum>
  <etotal_int>     -23.19630616 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.34021621 </eigenvalue_sum>
  <etotal_int>     -23.19632206 </etotal_int>
  <timing name="iteration" min="    0.223" max="    0.223"/>
</iteration>
<iteration count="3">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718326 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00718332 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00718116 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00004769 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001017 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002156 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025656 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025654 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025657 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000030 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000012 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000040 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01103667 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103544 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01103824 </sigma_eps_zz>
   <sigma_eps_xy>   0.00003701 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002776 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005560 </sigma_eps_xz>

   <sigma_enl_xx>   0.00951975 </sigma_enl_xx>
   <sigma_enl_yy>   0.00951898 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952065 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00002321 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001627 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003235 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387666 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387729 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387548 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001214 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001958 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003945 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268121 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268121 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268121 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00058002 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057936 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058115 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00002274 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001695 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003305 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005494 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005573 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005541 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00006846 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001499 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002809 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90822316 </ekin>
  <econf>        0.01791597 </econf>
  <eps>         -2.61482696 </eps>
  <enl>          2.01371759 </enl>
  <ecoul>       -7.84915704 </ecoul>
  <exc>         -2.38179844 </exc>
  <esr>          0.04424303 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90592573 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90592573 </enthalpy>
<atomset>
<unit_cell 
    a="  5.18053676   5.18053201   0.00008071"
    b="  0.05103583   5.12957613   5.12958590"
    c="  5.12984307   0.05077355   5.12984551" />
  <atom name="Si1" species="silicon">
    <position> 1.30496631 1.27523306 1.27742862 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00267363 0.00517124 -0.00257026 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30496631 -1.27523306 -1.27742862 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00267364 -0.00517123 0.00257026 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.326382 </unit_cell_a_norm>
<unit_cell_b_norm> 7.254503 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254873 </unit_cell_c_norm>
<unit_cell_alpha>  59.343 </unit_cell_alpha>
<unit_cell_beta>   59.672 </unit_cell_beta>
<unit_cell_gamma>  59.671 </unit_cell_gamma>
<unit_cell_volume> 269.933 </unit_cell_volume>
  <econst> -7.90592573 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.61647199 </sigma_eks_xx>
   <sigma_eks_yy>  -1.63970721 </sigma_eks_yy>
   <sigma_eks_zz>  -1.63011619 </sigma_eks_zz>
   <sigma_eks_xy>  -2.01418831 </sigma_eks_xy>
   <sigma_eks_yz>  -0.44097899 </sigma_eks_yz>
   <sigma_eks_xz>   0.82651269 </sigma_eks_xz>

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

   <sigma_xx>  -1.61647199 </sigma_xx>
   <sigma_yy>  -1.63970721 </sigma_yy>
   <sigma_zz>  -1.63011619 </sigma_zz>
   <sigma_xy>  -2.01418831 </sigma_xy>
   <sigma_yz>  -0.44097899 </sigma_yz>
   <sigma_xz>   0.82651269 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.00882000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33884806 </eigenvalue_sum>
  <etotal_int>     -23.19382133 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33904026 </eigenvalue_sum>
  <etotal_int>     -23.19417379 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33917335 </eigenvalue_sum>
  <etotal_int>     -23.19441786 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33926740 </eigenvalue_sum>
  <etotal_int>     -23.19459032 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33933522 </eigenvalue_sum>
  <etotal_int>     -23.19471470 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33938514 </eigenvalue_sum>
  <etotal_int>     -23.19480624 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33942262 </eigenvalue_sum>
  <etotal_int>     -23.19487498 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33945133 </eigenvalue_sum>
  <etotal_int>     -23.19492763 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33947374 </eigenvalue_sum>
  <etotal_int>     -23.19496875 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33949156 </eigenvalue_sum>
  <etotal_int>     -23.19500143 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.221"/>
</iteration>
<iteration count="4">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718543 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00718549 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00718324 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00004631 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001030 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002180 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025662 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025661 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025663 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000029 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000013 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000041 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01104007 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01103883 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01104161 </sigma_eps_zz>
   <sigma_eps_xy>   0.00003638 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002765 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005542 </sigma_eps_xz>

   <sigma_enl_xx>   0.00952237 </sigma_enl_xx>
   <sigma_enl_yy>   0.00952160 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952325 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00002279 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001620 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003225 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387719 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387782 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387602 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001174 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001946 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003923 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268190 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268190 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268190 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00058050 </sigma_esr_xx>
   <sigma_esr_yy>   0.00057984 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058160 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00002244 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001686 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003291 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005425 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005503 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005480 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00006661 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001470 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002758 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90848090 </ekin>
  <econf>        0.01791733 </econf>
  <eps>         -2.61503504 </eps>
  <enl>          2.01381543 </enl>
  <ecoul>       -7.84919924 </ecoul>
  <exc>         -2.38191297 </exc>
  <esr>          0.04427363 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90593359 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90593359 </enthalpy>
<atomset>
<unit_cell 
    a="  5.17969721   5.17968722   0.00016948"
    b="  0.05074524   5.12910988   5.12913038"
    c="  5.12967046   0.05019445   5.12967556" />
  <atom name="Si1" species="silicon">
    <position> 1.30479174 1.27502192 1.27735010 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00265123 0.00513298 -0.00251199 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30479174 -1.27502192 -1.27735010 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00265124 -0.00513298 0.00251199 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.325191 </unit_cell_a_norm>
<unit_cell_b_norm> 7.253849 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254627 </unit_cell_c_norm>
<unit_cell_alpha>  59.348 </unit_cell_alpha>
<unit_cell_beta>   59.675 </unit_cell_beta>
<unit_cell_gamma>  59.672 </unit_cell_gamma>
<unit_cell_volume> 269.876 </unit_cell_volume>
  <econst> -7.90593359 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.59606893 </sigma_eks_xx>
   <sigma_eks_yy>  -1.61901423 </sigma_eks_yy>
   <sigma_eks_zz>  -1.61223668 </sigma_eks_zz>
   <sigma_eks_xy>  -1.95961919 </sigma_eks_xy>
   <sigma_eks_yz>  -0.43255673 </sigma_eks_yz>
   <sigma_eks_xz>   0.81138872 </sigma_eks_xz>

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

   <sigma_xx>  -1.59606893 </sigma_xx>
   <sigma_yy>  -1.61901423 </sigma_yy>
   <sigma_zz>  -1.61223668 </sigma_zz>
   <sigma_xy>  -1.95961919 </sigma_xy>
   <sigma_yz>  -0.43255673 </sigma_yz>
   <sigma_xz>   0.81138872 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.01852200
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33661683 </eigenvalue_sum>
  <etotal_int>     -23.18974616 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33702105 </eigenvalue_sum>
  <etotal_int>     -23.19048750 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33730079 </eigenvalue_sum>
  <etotal_int>     -23.19100047 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33749846 </eigenvalue_sum>
  <etotal_int>     -23.19136294 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33764108 </eigenvalue_sum>
  <etotal_int>     -23.19162446 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33774616 </eigenvalue_sum>
  <etotal_int>     -23.19181712 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33782519 </eigenvalue_sum>
  <etotal_int>     -23.19196202 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33788584 </eigenvalue_sum>
  <etotal_int>     -23.19207323 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33793332 </eigenvalue_sum>
  <etotal_int>     -23.19216029 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33797118 </eigenvalue_sum>
  <etotal_int>     -23.19222970 </etotal_int>
  <timing name="iteration" min="    0.224" max="    0.225"/>
</iteration>
<iteration count="5">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00718994 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00719001 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00718773 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00004474 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001054 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002221 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025675 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025674 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025676 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000028 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000013 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000041 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01104721 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01104598 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01104869 </sigma_eps_zz>
   <sigma_eps_xy>   0.00003528 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002739 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005497 </sigma_eps_xz>

   <sigma_enl_xx>   0.00952787 </sigma_enl_xx>
   <sigma_enl_yy>   0.00952709 </sigma_enl_yy>
   <sigma_enl_zz>   0.00952871 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00002210 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001604 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003198 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00387830 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00387892 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387715 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00001106 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001927 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003888 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268336 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268336 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268336 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00058149 </sigma_esr_xx>
   <sigma_esr_yy>   0.00058083 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058256 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00002182 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001669 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003262 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00005283 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005359 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005343 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00006416 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001420 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002671 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.90902534 </ekin>
  <econf>        0.01792013 </econf>
  <eps>         -2.61547267 </eps>
  <enl>          2.01401995 </enl>
  <ecoul>       -7.84928814 </ecoul>
  <exc>         -2.38215383 </exc>
  <esr>          0.04433804 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90594921 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90594921 </enthalpy>
<atomset>
<unit_cell 
    a="  5.17793413   5.17791316   0.00035591"
    b="  0.05013501   5.12813074   5.12817380"
    c="  5.12930796   0.04897835   5.12931869" />
  <atom name="Si1" species="silicon">
    <position> 1.30442513 1.27457854 1.27718522 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00261660 0.00507637 -0.00241226 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30442513 -1.27457854 -1.27718522 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00261661 -0.00507637 0.00241226 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.322690 </unit_cell_a_norm>
<unit_cell_b_norm> 7.252476 </unit_cell_b_norm>
<unit_cell_c_norm> 7.254110 </unit_cell_c_norm>
<unit_cell_alpha>  59.360 </unit_cell_alpha>
<unit_cell_beta>   59.682 </unit_cell_beta>
<unit_cell_gamma>  59.675 </unit_cell_gamma>
<unit_cell_volume> 269.758 </unit_cell_volume>
  <econst> -7.90594921 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.55429565 </sigma_eks_xx>
   <sigma_eks_yy>  -1.57665511 </sigma_eks_yy>
   <sigma_eks_zz>  -1.57213292 </sigma_eks_zz>
   <sigma_eks_xy>  -1.88759243 </sigma_eks_xy>
   <sigma_eks_yz>  -0.41790625 </sigma_eks_yz>
   <sigma_eks_xz>   0.78574849 </sigma_eks_xz>

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

   <sigma_xx>  -1.55429565 </sigma_xx>
   <sigma_yy>  -1.57665511 </sigma_yy>
   <sigma_zz>  -1.57213292 </sigma_zz>
   <sigma_xy>  -1.88759243 </sigma_xy>
   <sigma_yz>  -0.41790625 </sigma_yz>
   <sigma_xz>   0.78574849 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.03889620
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33193030 </eigenvalue_sum>
  <etotal_int>     -23.18118366 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33278238 </eigenvalue_sum>
  <etotal_int>     -23.18274702 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33337100 </eigenvalue_sum>
  <etotal_int>     -23.18382670 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33378663 </eigenvalue_sum>
  <etotal_int>     -23.18458898 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33408650 </eigenvalue_sum>
  <etotal_int>     -23.18513888 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33430748 </eigenvalue_sum>
  <etotal_int>     -23.18554412 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33447381 </eigenvalue_sum>
  <etotal_int>     -23.18584911 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33460159 </eigenvalue_sum>
  <etotal_int>     -23.18608343 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33470174 </eigenvalue_sum>
  <etotal_int>     -23.18626707 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.33478171 </eigenvalue_sum>
  <etotal_int>     -23.18641371 </etotal_int>
  <timing name="iteration" min="    0.238" max="    0.238"/>
</iteration>
<iteration count="6">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00719940 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00719950 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00719725 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00004222 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001101 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002304 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025702 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025701 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025703 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000027 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000014 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000041 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01106223 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01106101 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01106362 </sigma_eps_zz>
   <sigma_eps_xy>   0.00003312 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002684 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005400 </sigma_eps_xz>

   <sigma_enl_xx>   0.00953942 </sigma_enl_xx>
   <sigma_enl_yy>   0.00953866 </sigma_enl_yy>
   <sigma_enl_zz>   0.00954021 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00002077 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001570 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003140 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00388063 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00388123 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00387954 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000972 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001891 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003820 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00268643 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00268643 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00268643 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00058357 </sigma_esr_xx>
   <sigma_esr_yy>   0.00058293 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058458 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00002051 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001631 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003201 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00004986 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00005058 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00005050 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00005984 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001321 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002497 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.91017221 </ekin>
  <econf>        0.01792596 </econf>
  <eps>         -2.61639380 </eps>
  <enl>          2.01444955 </enl>
  <ecoul>       -7.84947431 </ecoul>
  <exc>         -2.38266020 </exc>
  <esr>          0.04447395 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90598060 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90598060 </enthalpy>
<atomset>
<unit_cell 
    a="  5.17423168   5.17418763   0.00074742"
    b="  0.04885352   5.12607455   5.12616498"
    c="  5.12854672   0.04642454   5.12856924" />
  <atom name="Si1" species="silicon">
    <position> 1.30365521 1.27364741 1.27683895 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00254972 0.00496803 -0.00221325 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30365521 -1.27364741 -1.27683895 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00254973 -0.00496803 0.00221325 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.317438 </unit_cell_a_norm>
<unit_cell_b_norm> 7.249593 </unit_cell_b_norm>
<unit_cell_c_norm> 7.253025 </unit_cell_c_norm>
<unit_cell_alpha>  59.384 </unit_cell_alpha>
<unit_cell_beta>   59.696 </unit_cell_beta>
<unit_cell_gamma>  59.681 </unit_cell_gamma>
<unit_cell_volume> 269.508 </unit_cell_volume>
  <econst> -7.90598060 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.46708026 </sigma_eks_xx>
   <sigma_eks_yy>  -1.48820720 </sigma_eks_yy>
   <sigma_eks_zz>  -1.48590531 </sigma_eks_zz>
   <sigma_eks_xy>  -1.76062218 </sigma_eks_xy>
   <sigma_eks_yz>  -0.38861017 </sigma_eks_yz>
   <sigma_eks_xz>   0.73475123 </sigma_eks_xz>

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

   <sigma_xx>  -1.46708026 </sigma_xx>
   <sigma_yy>  -1.48820720 </sigma_yy>
   <sigma_zz>  -1.48590531 </sigma_zz>
   <sigma_xy>  -1.76062218 </sigma_xy>
   <sigma_yz>  -0.38861017 </sigma_yz>
   <sigma_xz>   0.73475123 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.08168202
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32207890 </eigenvalue_sum>
  <etotal_int>     -23.16317444 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32388062 </eigenvalue_sum>
  <etotal_int>     -23.16648301 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32512001 </eigenvalue_sum>
  <etotal_int>     -23.16875769 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32599319 </eigenvalue_sum>
  <etotal_int>     -23.17035977 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32662244 </eigenvalue_sum>
  <etotal_int>     -23.17151411 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32708597 </eigenvalue_sum>
  <etotal_int>     -23.17236438 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32743484 </eigenvalue_sum>
  <etotal_int>     -23.17300430 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32770296 </eigenvalue_sum>
  <etotal_int>     -23.17349610 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32791320 </eigenvalue_sum>
  <etotal_int>     -23.17388172 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.32808121 </eigenvalue_sum>
  <etotal_int>     -23.17418988 </etotal_int>
  <timing name="iteration" min="    0.220" max="    0.220"/>
</iteration>
<iteration count="7">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00721933 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00721948 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00721736 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00003741 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001200 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002478 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025760 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025758 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025761 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000024 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000015 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000042 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01109390 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01109270 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01109511 </sigma_eps_zz>
   <sigma_eps_xy>   0.00002869 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002568 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00005195 </sigma_eps_xz>

   <sigma_enl_xx>   0.00956378 </sigma_enl_xx>
   <sigma_enl_yy>   0.00956303 </sigma_enl_yy>
   <sigma_enl_zz>   0.00956448 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00001808 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001499 </sigma_enl_yz>
   <sigma_enl_xz>   0.00003018 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00388551 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00388609 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00388456 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000692 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001815 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003679 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00269289 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00269289 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00269289 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00058799 </sigma_esr_xx>
   <sigma_esr_yy>   0.00058736 </sigma_esr_yy>
   <sigma_esr_zz>   0.00058887 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00001774 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001553 </sigma_esr_yz>
   <sigma_esr_xz>   0.00003072 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00004360 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00004423 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00004425 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00005122 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00001114 </sigma_eks_yz>
   <sigma_eks_xz>   0.00002137 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.91259268 </ekin>
  <econf>        0.01793813 </econf>
  <eps>         -2.61834001 </eps>
  <enl>          2.01535809 </enl>
  <ecoul>       -7.84986352 </ecoul>
  <exc>         -2.38372648 </exc>
  <esr>          0.04476231 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90604110 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90604110 </enthalpy>
<atomset>
<unit_cell 
    a="  5.16645652   5.16636402   0.00156958"
    b="  0.04616240   5.12175657   5.12194646"
    c="  5.12694810   0.04106154   5.12699541" />
  <atom name="Si1" species="silicon">
    <position> 1.30203814 1.27169202 1.27611178 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00241265 0.00474463 -0.00179746 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.30203814 -1.27169202 -1.27611178 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00241265 -0.00474463 0.00179746 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.306408 </unit_cell_a_norm>
<unit_cell_b_norm> 7.243539 </unit_cell_b_norm>
<unit_cell_c_norm> 7.250749 </unit_cell_c_norm>
<unit_cell_alpha>  59.436 </unit_cell_alpha>
<unit_cell_beta>   59.725 </unit_cell_beta>
<unit_cell_gamma>  59.693 </unit_cell_gamma>
<unit_cell_volume> 268.985 </unit_cell_volume>
  <econst> -7.90604110 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -1.28278007 </sigma_eks_xx>
   <sigma_eks_yy>  -1.30131874 </sigma_eks_yy>
   <sigma_eks_zz>  -1.30203561 </sigma_eks_zz>
   <sigma_eks_xy>  -1.50685953 </sigma_eks_xy>
   <sigma_eks_yz>  -0.32787904 </sigma_eks_yz>
   <sigma_eks_xz>   0.62861197 </sigma_eks_xz>

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

   <sigma_xx>  -1.28278007 </sigma_xx>
   <sigma_yy>  -1.30131874 </sigma_yy>
   <sigma_zz>  -1.30203561 </sigma_zz>
   <sigma_xy>  -1.50685953 </sigma_xy>
   <sigma_yz>  -0.32787904 </sigma_yz>
   <sigma_xz>   0.62861197 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.17153224
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30133048 </eigenvalue_sum>
  <etotal_int>     -23.12519970 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30516685 </eigenvalue_sum>
  <etotal_int>     -23.13225710 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30778203 </eigenvalue_sum>
  <etotal_int>     -23.13706255 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30961513 </eigenvalue_sum>
  <etotal_int>     -23.14042889 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31093243 </eigenvalue_sum>
  <etotal_int>     -23.14284722 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31190142 </eigenvalue_sum>
  <etotal_int>     -23.14462582 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31263030 </eigenvalue_sum>
  <etotal_int>     -23.14596358 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31319046 </eigenvalue_sum>
  <etotal_int>     -23.14699163 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31362984 </eigenvalue_sum>
  <etotal_int>     -23.14779800 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.31398115 </eigenvalue_sum>
  <etotal_int>     -23.14844275 </etotal_int>
  <timing name="iteration" min="    0.226" max="    0.226"/>
</iteration>
<iteration count="8">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00726155 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00726180 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00725995 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00002746 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001407 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002847 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025880 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025878 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025881 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000018 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000018 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000044 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01116103 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01115988 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01116192 </sigma_eps_zz>
   <sigma_eps_xy>   0.00001933 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002325 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00004759 </sigma_eps_xz>

   <sigma_enl_xx>   0.00961539 </sigma_enl_xx>
   <sigma_enl_yy>   0.00961468 </sigma_enl_yy>
   <sigma_enl_zz>   0.00961592 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00001241 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001351 </sigma_enl_yz>
   <sigma_enl_xz>   0.00002758 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00389579 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00389632 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00389512 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000099 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001656 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003382 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00270655 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00270655 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00270655 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00059744 </sigma_esr_xx>
   <sigma_esr_yy>   0.00059685 </sigma_esr_yy>
   <sigma_esr_zz>   0.00059806 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00001180 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001389 </sigma_esr_yz>
   <sigma_esr_xz>   0.00002797 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00003019 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00003063 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00003085 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00003314 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000683 </sigma_eks_yz>
   <sigma_eks_xz>   0.00001373 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.91772799 </ekin>
  <econf>        0.01796348 </econf>
  <eps>         -2.62248249 </eps>
  <enl>          2.01729927 </enl>
  <ecoul>       -7.85067378 </ecoul>
  <exc>         -2.38597899 </exc>
  <esr>          0.04538096 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90614452 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90614452 </enthalpy>
<atomset>
<unit_cell 
    a="  5.15012870   5.14993443   0.00329611"
    b="  0.04051104   5.11268879   5.11308756"
    c="  5.12359102   0.02979923   5.12369035" />
  <atom name="Si1" species="silicon">
    <position> 1.29864126 1.26758552 1.27458469 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00212893 0.00427360 -0.00091090 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.29864125 -1.26758551 -1.27458469 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00212893 -0.00427360 0.00091090 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.283245 </unit_cell_a_norm>
<unit_cell_b_norm> 7.230829 </unit_cell_b_norm>
<unit_cell_c_norm> 7.245983 </unit_cell_c_norm>
<unit_cell_alpha>  59.544 </unit_cell_alpha>
<unit_cell_beta>   59.786 </unit_cell_beta>
<unit_cell_gamma>  59.719 </unit_cell_gamma>
<unit_cell_volume> 267.887 </unit_cell_volume>
  <econst> -7.90614452 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.88812144 </sigma_eks_xx>
   <sigma_eks_yy>  -0.90125496 </sigma_eks_yy>
   <sigma_eks_zz>  -0.90757075 </sigma_eks_zz>
   <sigma_eks_xy>  -0.97490372 </sigma_eks_xy>
   <sigma_eks_yz>  -0.20100646 </sigma_eks_yz>
   <sigma_eks_xz>   0.40406634 </sigma_eks_xz>

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

   <sigma_xx>  -0.88812144 </sigma_xx>
   <sigma_yy>  -0.90125496 </sigma_yy>
   <sigma_zz>  -0.90757075 </sigma_zz>
   <sigma_xy>  -0.97490372 </sigma_xy>
   <sigma_yz>  -0.20100646 </sigma_yz>
   <sigma_xz>   0.40406634 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.17153224
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29940020 </eigenvalue_sum>
  <etotal_int>     -23.12173703 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30163697 </eigenvalue_sum>
  <etotal_int>     -23.12584426 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30320219 </eigenvalue_sum>
  <etotal_int>     -23.12871714 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30432630 </eigenvalue_sum>
  <etotal_int>     -23.13077996 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30515382 </eigenvalue_sum>
  <etotal_int>     -23.13229838 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30577770 </eigenvalue_sum>
  <etotal_int>     -23.13344311 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30625896 </eigenvalue_sum>
  <etotal_int>     -23.13432614 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30663834 </eigenvalue_sum>
  <etotal_int>     -23.13502225 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30694352 </eigenvalue_sum>
  <etotal_int>     -23.13558222 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.30719360 </eigenvalue_sum>
  <etotal_int>     -23.13604109 </etotal_int>
  <timing name="iteration" min="    0.224" max="    0.224"/>
</iteration>
<iteration count="9">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00728501 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00728529 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00728388 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00002588 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001417 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002882 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00025940 </sigma_econf_xx>
   <sigma_econf_yy>   0.00025939 </sigma_econf_yy>
   <sigma_econf_zz>   0.00025941 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000019 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000018 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000042 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01119800 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01119690 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01119871 </sigma_eps_zz>
   <sigma_eps_xy>   0.00001516 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002184 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00004469 </sigma_eps_xz>

   <sigma_enl_xx>   0.00964307 </sigma_enl_xx>
   <sigma_enl_yy>   0.00964239 </sigma_enl_yy>
   <sigma_enl_zz>   0.00964349 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00000977 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001265 </sigma_enl_yz>
   <sigma_enl_xz>   0.00002583 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00390194 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00390244 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00390140 </sigma_ehart_zz>
   <sigma_ehart_xy>  -0.00000049 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001603 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003259 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00271420 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00271420 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00271420 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00060286 </sigma_esr_xx>
   <sigma_esr_yy>   0.00060230 </sigma_esr_yy>
   <sigma_esr_zz>   0.00060336 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000963 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001307 </sigma_esr_yz>
   <sigma_esr_xz>   0.00002634 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00002380 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00002417 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00002417 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00003042 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000592 </sigma_eks_yz>
   <sigma_eks_xz>   0.00001168 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.92049063 </ekin>
  <econf>        0.01797288 </econf>
  <eps>         -2.62451186 </eps>
  <enl>          2.01802862 </enl>
  <ecoul>       -7.85097543 </ecoul>
  <exc>         -2.38719135 </exc>
  <esr>          0.04573908 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90618651 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90618651 </enthalpy>
<atomset>
<unit_cell 
    a="  5.14276242   5.14250992   0.00412407"
    b="  0.03853476   5.10806090   5.10842093"
    c="  5.12121976   0.02562340   5.12120071" />
  <atom name="Si1" species="silicon">
    <position> 1.29693307 1.26607348 1.27376193 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00202236 0.00405888 -0.00075580 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.29693307 -1.26607348 -1.27376193 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00202236 -0.00405888 0.00075580 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.272787 </unit_cell_a_norm>
<unit_cell_b_norm> 7.224246 </unit_cell_b_norm>
<unit_cell_c_norm> 7.242530 </unit_cell_c_norm>
<unit_cell_alpha>  59.584 </unit_cell_alpha>
<unit_cell_beta>   59.807 </unit_cell_beta>
<unit_cell_gamma>  59.726 </unit_cell_gamma>
<unit_cell_volume> 267.271 </unit_cell_volume>
  <econst> -7.90618651 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.70021854 </sigma_eks_xx>
   <sigma_eks_yy>  -0.71101533 </sigma_eks_yy>
   <sigma_eks_zz>  -0.71118477 </sigma_eks_zz>
   <sigma_eks_xy>  -0.89488020 </sigma_eks_xy>
   <sigma_eks_yz>  -0.17428993 </sigma_eks_yz>
   <sigma_eks_xz>   0.34356627 </sigma_eks_xz>

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

   <sigma_xx>  -0.70021854 </sigma_xx>
   <sigma_yy>  -0.71101533 </sigma_yy>
   <sigma_zz>  -0.71118477 </sigma_zz>
   <sigma_xy>  -0.89488020 </sigma_xy>
   <sigma_yz>  -0.17428993 </sigma_yz>
   <sigma_xz>   0.34356627 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.36021771
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29107004 </eigenvalue_sum>
  <etotal_int>     -23.10650178 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29343990 </eigenvalue_sum>
  <etotal_int>     -23.11085361 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29508829 </eigenvalue_sum>
  <etotal_int>     -23.11387911 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29626511 </eigenvalue_sum>
  <etotal_int>     -23.11603855 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29712633 </eigenvalue_sum>
  <etotal_int>     -23.11761871 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29777189 </eigenvalue_sum>
  <etotal_int>     -23.11880312 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29826712 </eigenvalue_sum>
  <etotal_int>     -23.11971171 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29865552 </eigenvalue_sum>
  <etotal_int>     -23.12042430 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29896650 </eigenvalue_sum>
  <etotal_int>     -23.12099487 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29922029 </eigenvalue_sum>
  <etotal_int>     -23.12146051 </etotal_int>
  <timing name="iteration" min="    0.220" max="    0.220"/>
</iteration>
<iteration count="10">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00731117 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00731148 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00731045 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00002318 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001449 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002957 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026010 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026009 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026011 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000019 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000019 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000041 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01123944 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01123839 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01123996 </sigma_eps_zz>
   <sigma_eps_xy>   0.00001111 </sigma_eps_xy>
   <sigma_eps_yz>   0.00002040 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00004166 </sigma_eps_xz>

   <sigma_enl_xx>   0.00967443 </sigma_enl_xx>
   <sigma_enl_yy>   0.00967379 </sigma_enl_yy>
   <sigma_enl_zz>   0.00967476 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00000726 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001179 </sigma_enl_yz>
   <sigma_enl_xz>   0.00002403 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00390856 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00390901 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00390816 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000108 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001523 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00003089 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00272269 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00272269 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00272269 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00060889 </sigma_esr_xx>
   <sigma_esr_yy>   0.00060837 </sigma_esr_yy>
   <sigma_esr_zz>   0.00060926 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000721 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001217 </sigma_esr_yz>
   <sigma_esr_xz>   0.00002454 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00001608 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00001635 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00001622 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00002528 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000448 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000864 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.92361680 </ekin>
  <econf>        0.01798541 </econf>
  <eps>         -2.62692077 </eps>
  <enl>          2.01902059 </enl>
  <ecoul>       -7.85137003 </ecoul>
  <exc>         -2.38855562 </exc>
  <esr>          0.04613803 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90622362 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90622362 </enthalpy>
<atomset>
<unit_cell 
    a="  5.13465951   5.13434296   0.00503484"
    b="  0.03636086   5.10297023   5.10328763"
    c="  5.11861139   0.02102998   5.11846209" />
  <atom name="Si1" species="silicon">
    <position> 1.29505367 1.26440975 1.27285663 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00188573 0.00378924 -0.00047963 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.29505367 -1.26440975 -1.27285663 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00188573 -0.00378924 0.00047963 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.261283 </unit_cell_a_norm>
<unit_cell_b_norm> 7.217006 </unit_cell_b_norm>
<unit_cell_c_norm> 7.238735 </unit_cell_c_norm>
<unit_cell_alpha>  59.628 </unit_cell_alpha>
<unit_cell_beta>   59.830 </unit_cell_beta>
<unit_cell_gamma>  59.734 </unit_cell_gamma>
<unit_cell_volume> 266.594 </unit_cell_volume>
  <econst> -7.90622362 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.47298938 </sigma_eks_xx>
   <sigma_eks_yy>  -0.48104938 </sigma_eks_yy>
   <sigma_eks_zz>  -0.47720671 </sigma_eks_zz>
   <sigma_eks_xy>  -0.74364699 </sigma_eks_xy>
   <sigma_eks_yz>  -0.13190421 </sigma_eks_yz>
   <sigma_eks_xz>   0.25422676 </sigma_eks_xz>

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

   <sigma_xx>  -0.47298938 </sigma_xx>
   <sigma_yy>  -0.48104938 </sigma_yy>
   <sigma_zz>  -0.47720671 </sigma_zz>
   <sigma_xy>  -0.74364699 </sigma_xy>
   <sigma_yz>  -0.13190421 </sigma_yz>
   <sigma_xz>   0.25422676 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28297664 </eigenvalue_sum>
  <etotal_int>     -23.09168670 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28540680 </eigenvalue_sum>
  <etotal_int>     -23.09615625 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28708404 </eigenvalue_sum>
  <etotal_int>     -23.09923802 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28827590 </eigenvalue_sum>
  <etotal_int>     -23.10142684 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28914565 </eigenvalue_sum>
  <etotal_int>     -23.10302370 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28979643 </eigenvalue_sum>
  <etotal_int>     -23.10421839 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29029510 </eigenvalue_sum>
  <etotal_int>     -23.10513379 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29068590 </eigenvalue_sum>
  <etotal_int>     -23.10585118 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29099866 </eigenvalue_sum>
  <etotal_int>     -23.10642530 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.29125382 </eigenvalue_sum>
  <etotal_int>     -23.10689371 </etotal_int>
  <timing name="iteration" min="    0.222" max="    0.223"/>
</iteration>
<iteration count="11">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00733752 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00733787 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00733695 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00001559 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001547 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00003119 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026080 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026079 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026081 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000013 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000020 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000042 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01128103 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01128007 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01128136 </sigma_eps_zz>
   <sigma_eps_xy>   0.00000345 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001812 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00003724 </sigma_eps_xz>

   <sigma_enl_xx>   0.00970592 </sigma_enl_xx>
   <sigma_enl_yy>   0.00970533 </sigma_enl_yy>
   <sigma_enl_zz>   0.00970613 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00000260 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00001042 </sigma_enl_yz>
   <sigma_enl_xz>   0.00002140 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00391518 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00391558 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00391494 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000554 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001379 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002808 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00273120 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00273120 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00273120 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00061496 </sigma_esr_xx>
   <sigma_esr_yy>   0.00061450 </sigma_esr_yy>
   <sigma_esr_zz>   0.00061518 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000227 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001068 </sigma_esr_yz>
   <sigma_esr_xz>   0.00002178 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000822 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000836 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000844 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00001135 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000149 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000325 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.92674133 </ekin>
  <econf>        0.01799797 </econf>
  <eps>         -2.62933217 </eps>
  <enl>          2.02001539 </enl>
  <ecoul>       -7.85176418 </ecoul>
  <exc>         -2.38992055 </exc>
  <esr>          0.04653733 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90626220 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90626220 </enthalpy>
<atomset>
<unit_cell 
    a="  5.12274822   5.12235579   0.00620433"
    b="  0.03125381   5.09724876   5.09773924"
    c="  5.11674520   0.01214203   5.11665606" />
  <atom name="Si1" species="silicon">
    <position> 1.29231697 1.26187291 1.27199005 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00164354 0.00335493 0.00022159 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.29231696 -1.26187291 -1.27199005 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00164354 -0.00335493 -0.00022159 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.244385 </unit_cell_a_norm>
<unit_cell_b_norm> 7.209013 </unit_cell_b_norm>
<unit_cell_c_norm> 7.236118 </unit_cell_c_norm>
<unit_cell_alpha>  59.717 </unit_cell_alpha>
<unit_cell_beta>   59.880 </unit_cell_beta>
<unit_cell_gamma>  59.760 </unit_cell_gamma>
<unit_cell_volume> 265.918 </unit_cell_volume>
  <econst> -7.90626220 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.24178764 </sigma_eks_xx>
   <sigma_eks_yy>  -0.24608206 </sigma_eks_yy>
   <sigma_eks_zz>  -0.24833070 </sigma_eks_zz>
   <sigma_eks_xy>  -0.33388695 </sigma_eks_xy>
   <sigma_eks_yz>  -0.04390019 </sigma_eks_yz>
   <sigma_eks_xz>   0.09568955 </sigma_eks_xz>

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

   <sigma_xx>  -0.24178764 </sigma_xx>
   <sigma_yy>  -0.24608206 </sigma_yy>
   <sigma_zz>  -0.24833070 </sigma_zz>
   <sigma_xy>  -0.33388695 </sigma_xy>
   <sigma_yz>  -0.04390019 </sigma_yz>
   <sigma_xz>   0.09568955 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28474641 </eigenvalue_sum>
  <etotal_int>     -23.09497036 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28581928 </eigenvalue_sum>
  <etotal_int>     -23.09693970 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28658375 </eigenvalue_sum>
  <etotal_int>     -23.09834260 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28714349 </eigenvalue_sum>
  <etotal_int>     -23.09936970 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28756421 </eigenvalue_sum>
  <etotal_int>     -23.10014168 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28788848 </eigenvalue_sum>
  <etotal_int>     -23.10073670 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28814439 </eigenvalue_sum>
  <etotal_int>     -23.10120630 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28835083 </eigenvalue_sum>
  <etotal_int>     -23.10158513 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28852070 </eigenvalue_sum>
  <etotal_int>     -23.10189686 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28866295 </eigenvalue_sum>
  <etotal_int>     -23.10215792 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.221"/>
</iteration>
<iteration count="12">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00734826 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00734859 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00734793 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00001562 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001492 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00003020 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026105 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026104 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026106 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000015 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000019 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000040 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01129781 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01129689 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01129805 </sigma_eps_zz>
   <sigma_eps_xy>   0.00000106 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001699 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00003477 </sigma_eps_xz>

   <sigma_enl_xx>   0.00971816 </sigma_enl_xx>
   <sigma_enl_yy>   0.00971761 </sigma_enl_yy>
   <sigma_enl_zz>   0.00971831 </sigma_enl_zz>
   <sigma_enl_xy>  -0.00000107 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000974 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001993 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00391818 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00391855 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00391800 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000506 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001335 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002706 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00273472 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00273472 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00273472 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00061753 </sigma_esr_xx>
   <sigma_esr_yy>   0.00061710 </sigma_esr_yy>
   <sigma_esr_zz>   0.00061770 </sigma_esr_zz>
   <sigma_esr_xy>  -0.00000111 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00001004 </sigma_esr_yz>
   <sigma_esr_xz>   0.00002041 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000571 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000582 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000577 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00001153 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000142 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000282 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.92795357 </ekin>
  <econf>        0.01800046 </econf>
  <eps>         -2.63014573 </eps>
  <enl>          2.02020513 </enl>
  <ecoul>       -7.85183598 </ecoul>
  <exc>         -2.39045352 </exc>
  <esr>          0.04670757 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90627607 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90627607 </enthalpy>
<atomset>
<unit_cell 
    a="  5.11893528   5.11851122   0.00652329"
    b="  0.02971957   5.09525455   5.09572623"
    c="  5.11547154   0.00991825   5.11532539" />
  <atom name="Si1" species="silicon">
    <position> 1.29117808 1.26151392 1.27169701 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00157244 0.00319532 0.00023564 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.29117808 -1.26151391 -1.27169701 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00157244 -0.00319532 -0.00023564 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.238971 </unit_cell_a_norm>
<unit_cell_b_norm> 7.206173 </unit_cell_b_norm>
<unit_cell_c_norm> 7.234273 </unit_cell_c_norm>
<unit_cell_alpha>  59.742 </unit_cell_alpha>
<unit_cell_beta>   59.892 </unit_cell_beta>
<unit_cell_gamma>  59.768 </unit_cell_gamma>
<unit_cell_volume> 265.637 </unit_cell_volume>
  <econst> -7.90627607 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.16800257 </sigma_eks_xx>
   <sigma_eks_yy>  -0.17137511 </sigma_eks_yy>
   <sigma_eks_zz>  -0.16973696 </sigma_eks_zz>
   <sigma_eks_xy>  -0.33914634 </sigma_eks_xy>
   <sigma_eks_yz>  -0.04168576 </sigma_eks_yz>
   <sigma_eks_xz>   0.08300050 </sigma_eks_xz>

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

   <sigma_xx>  -0.16800257 </sigma_xx>
   <sigma_yy>  -0.17137511 </sigma_yy>
   <sigma_zz>  -0.16973696 </sigma_zz>
   <sigma_xy>  -0.33914634 </sigma_xy>
   <sigma_yz>  -0.04168576 </sigma_yz>
   <sigma_xz>   0.08300050 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28193819 </eigenvalue_sum>
  <etotal_int>     -23.08983340 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28296296 </eigenvalue_sum>
  <etotal_int>     -23.09171587 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368091 </eigenvalue_sum>
  <etotal_int>     -23.09303400 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28419823 </eigenvalue_sum>
  <etotal_int>     -23.09398353 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28458104 </eigenvalue_sum>
  <etotal_int>     -23.09468610 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28487166 </eigenvalue_sum>
  <etotal_int>     -23.09521944 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28509772 </eigenvalue_sum>
  <etotal_int>     -23.09563430 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28527761 </eigenvalue_sum>
  <etotal_int>     -23.09596444 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28542380 </eigenvalue_sum>
  <etotal_int>     -23.09623275 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28554488 </eigenvalue_sum>
  <etotal_int>     -23.09645496 </etotal_int>
  <timing name="iteration" min="    0.223" max="    0.223"/>
</iteration>
<iteration count="13">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00735940 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00735974 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00735917 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00001250 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001490 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00003004 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026134 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026133 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026134 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000013 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000019 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000039 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01131536 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01131451 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01131552 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000256 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001555 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00003181 </sigma_eps_xz>

   <sigma_enl_xx>   0.00973131 </sigma_enl_xx>
   <sigma_enl_yy>   0.00973081 </sigma_enl_yy>
   <sigma_enl_zz>   0.00973142 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000115 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000889 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001819 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392106 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392139 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392095 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000675 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001243 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002518 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00273833 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00273833 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00273833 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062014 </sigma_esr_xx>
   <sigma_esr_yy>   0.00061975 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062025 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000122 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000913 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001859 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000255 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000261 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000261 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000581 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000019 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000049 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.92925495 </ekin>
  <econf>        0.01800508 </econf>
  <eps>         -2.63112345 </eps>
  <enl>          2.02056980 </enl>
  <ecoul>       -7.85197398 </ecoul>
  <exc>         -2.39102197 </exc>
  <esr>          0.04688041 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90628956 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90628956 </enthalpy>
<atomset>
<unit_cell 
    a="  5.11333593   5.11287518   0.00697872"
    b="  0.02686764   5.09292172   5.09346289"
    c="  5.11455883   0.00568215   5.11443200" />
  <atom name="Si1" species="silicon">
    <position> 1.28964967 1.26073137 1.27141591 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00143261 0.00292391 0.00052984 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28964966 -1.26073137 -1.27141591 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00143261 -0.00292391 -0.00052984 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.231027 </unit_cell_a_norm>
<unit_cell_b_norm> 7.202912 </unit_cell_b_norm>
<unit_cell_c_norm> 7.232991 </unit_cell_c_norm>
<unit_cell_alpha>  59.787 </unit_cell_alpha>
<unit_cell_beta>   59.916 </unit_cell_beta>
<unit_cell_gamma>  59.784 </unit_cell_gamma>
<unit_cell_volume> 265.351 </unit_cell_volume>
  <econst> -7.90628956 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.07512603 </sigma_eks_xx>
   <sigma_eks_yy>  -0.07671928 </sigma_eks_yy>
   <sigma_eks_zz>  -0.07691310 </sigma_eks_zz>
   <sigma_eks_xy>  -0.17097808 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00561717 </sigma_eks_yz>
   <sigma_eks_xz>   0.01448356 </sigma_eks_xz>

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

   <sigma_xx>  -0.07512603 </sigma_xx>
   <sigma_yy>  -0.07671928 </sigma_yy>
   <sigma_zz>  -0.07691310 </sigma_zz>
   <sigma_xy>  -0.17097808 </sigma_xy>
   <sigma_yz>  -0.00561717 </sigma_yz>
   <sigma_xz>   0.01448356 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28399961 </eigenvalue_sum>
  <etotal_int>     -23.09362624 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28430708 </eigenvalue_sum>
  <etotal_int>     -23.09419061 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28453309 </eigenvalue_sum>
  <etotal_int>     -23.09460537 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28470421 </eigenvalue_sum>
  <etotal_int>     -23.09491938 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28483741 </eigenvalue_sum>
  <etotal_int>     -23.09516381 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28494378 </eigenvalue_sum>
  <etotal_int>     -23.09535900 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28503070 </eigenvalue_sum>
  <etotal_int>     -23.09551850 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28510318 </eigenvalue_sum>
  <etotal_int>     -23.09565152 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28516470 </eigenvalue_sum>
  <etotal_int>     -23.09576442 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28521770 </eigenvalue_sum>
  <etotal_int>     -23.09586169 </etotal_int>
  <timing name="iteration" min="    0.223" max="    0.223"/>
</iteration>
<iteration count="14">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00736202 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00736233 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00736188 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00001277 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001430 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002884 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026139 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026138 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026139 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000014 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000018 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000037 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01131935 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01131854 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01131947 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000357 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001479 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00003018 </sigma_eps_xz>

   <sigma_enl_xx>   0.00973404 </sigma_enl_xx>
   <sigma_enl_yy>   0.00973356 </sigma_enl_yy>
   <sigma_enl_zz>   0.00973412 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000180 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000844 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001723 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392192 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392222 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392183 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000630 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001207 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002440 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00273920 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00273920 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00273920 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062079 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062043 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062088 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000172 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000869 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001767 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000223 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000228 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000223 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000638 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00000029 </sigma_eks_yz>
   <sigma_eks_xz>   0.00000063 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.92951757 </ekin>
  <econf>        0.01800472 </econf>
  <eps>         -2.63124866 </eps>
  <enl>          2.02052606 </enl>
  <ecoul>       -7.85195499 </ecoul>
  <exc>         -2.39114069 </exc>
  <esr>          0.04692398 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90629599 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90629599 </enthalpy>
<atomset>
<unit_cell 
    a="  5.11179412   5.11132350   0.00697385"
    b="  0.02572790   5.09250506   5.09304889"
    c="  5.11405495   0.00463932   5.11392197" />
  <atom name="Si1" species="silicon">
    <position> 1.28898314 1.26090883 1.27142023 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00138477 0.00282003 0.00051453 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28898314 -1.26090883 -1.27142023 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00138477 -0.00282003 -0.00051453 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.228839 </unit_cell_a_norm>
<unit_cell_b_norm> 7.202320 </unit_cell_b_norm>
<unit_cell_c_norm> 7.232273 </unit_cell_c_norm>
<unit_cell_alpha>  59.802 </unit_cell_alpha>
<unit_cell_beta>   59.923 </unit_cell_beta>
<unit_cell_gamma>  59.791 </unit_cell_gamma>
<unit_cell_volume> 265.280 </unit_cell_volume>
  <econst> -7.90629599 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.06560214 </sigma_eks_xx>
   <sigma_eks_yy>  -0.06699405 </sigma_eks_yy>
   <sigma_eks_zz>  -0.06570049 </sigma_eks_zz>
   <sigma_eks_xy>  -0.18766603 </sigma_eks_xy>
   <sigma_eks_yz>  -0.00861462 </sigma_eks_yz>
   <sigma_eks_xz>   0.01867613 </sigma_eks_xz>

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

   <sigma_xx>  -0.06560214 </sigma_xx>
   <sigma_yy>  -0.06699405 </sigma_yy>
   <sigma_zz>  -0.06570049 </sigma_zz>
   <sigma_xy>  -0.18766603 </sigma_xy>
   <sigma_yz>  -0.00861462 </sigma_yz>
   <sigma_xz>   0.01867613 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28234616 </eigenvalue_sum>
  <etotal_int>     -23.09060138 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28277811 </eigenvalue_sum>
  <etotal_int>     -23.09139461 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28308106 </eigenvalue_sum>
  <etotal_int>     -23.09195069 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28329955 </eigenvalue_sum>
  <etotal_int>     -23.09235165 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28346141 </eigenvalue_sum>
  <etotal_int>     -23.09264866 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28358448 </eigenvalue_sum>
  <etotal_int>     -23.09287447 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368039 </eigenvalue_sum>
  <etotal_int>     -23.09305047 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375690 </eigenvalue_sum>
  <etotal_int>     -23.09319087 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381927 </eigenvalue_sum>
  <etotal_int>     -23.09330530 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28387108 </eigenvalue_sum>
  <etotal_int>     -23.09340038 </etotal_int>
  <timing name="iteration" min="    0.220" max="    0.220"/>
</iteration>
<iteration count="15">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00736691 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00736721 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00736680 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00001092 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001395 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002810 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026152 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026150 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026152 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000012 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000018 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000036 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01132707 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01132632 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01132716 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000538 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001371 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002792 </sigma_eps_xz>

   <sigma_enl_xx>   0.00973985 </sigma_enl_xx>
   <sigma_enl_yy>   0.00973941 </sigma_enl_yy>
   <sigma_enl_zz>   0.00973991 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000291 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000781 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001591 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392316 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392344 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392310 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000711 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001130 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002280 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274079 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274079 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274079 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062194 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062161 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062200 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000292 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000801 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001627 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000080 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000081 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000081 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000323 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000036 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000068 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93009059 </ekin>
  <econf>        0.01800696 </econf>
  <eps>         -2.63169110 </eps>
  <enl>          2.02070112 </enl>
  <ecoul>       -7.85201960 </ecoul>
  <exc>         -2.39139145 </exc>
  <esr>          0.04700032 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90630348 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90630348 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10876209   5.10827473   0.00709113"
    b="  0.02371144   5.09158904   5.09217182"
    c="  5.11346641   0.00231177   5.11335271" />
  <atom name="Si1" species="silicon">
    <position> 1.28792426 1.26085316 1.27138987 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00127789 0.00260251 0.00066329 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28792426 -1.26085316 -1.27138987 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00127789 -0.00260251 -0.00066329 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.224540 </unit_cell_a_norm>
<unit_cell_b_norm> 7.201045 </unit_cell_b_norm>
<unit_cell_c_norm> 7.231454 </unit_cell_c_norm>
<unit_cell_alpha>  59.830 </unit_cell_alpha>
<unit_cell_beta>   59.937 </unit_cell_beta>
<unit_cell_gamma>  59.804 </unit_cell_gamma>
<unit_cell_volume> 265.156 </unit_cell_volume>
  <econst> -7.90630348 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.02363732 </sigma_eks_xx>
   <sigma_eks_yy>  -0.02378952 </sigma_eks_yy>
   <sigma_eks_zz>  -0.02393432 </sigma_eks_zz>
   <sigma_eks_xy>  -0.09497985 </sigma_eks_xy>
   <sigma_eks_yz>   0.01049909 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02003044 </sigma_eks_xz>

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

   <sigma_xx>  -0.02363732 </sigma_xx>
   <sigma_yy>  -0.02378952 </sigma_yy>
   <sigma_zz>  -0.02393432 </sigma_zz>
   <sigma_xy>  -0.09497985 </sigma_xy>
   <sigma_yz>   0.01049909 </sigma_yz>
   <sigma_xz>  -0.02003044 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28355047 </eigenvalue_sum>
  <etotal_int>     -23.09281589 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28363856 </eigenvalue_sum>
  <etotal_int>     -23.09297768 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28370541 </eigenvalue_sum>
  <etotal_int>     -23.09310041 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375776 </eigenvalue_sum>
  <etotal_int>     -23.09319652 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379993 </eigenvalue_sum>
  <etotal_int>     -23.09327391 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383471 </eigenvalue_sum>
  <etotal_int>     -23.09333774 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28386401 </eigenvalue_sum>
  <etotal_int>     -23.09339151 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28388911 </eigenvalue_sum>
  <etotal_int>     -23.09343759 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28391094 </eigenvalue_sum>
  <etotal_int>     -23.09347765 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28393015 </eigenvalue_sum>
  <etotal_int>     -23.09351291 </etotal_int>
  <timing name="iteration" min="    0.224" max="    0.224"/>
</iteration>
<iteration count="16">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00736752 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00736781 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00736746 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00001109 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001341 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002698 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026152 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026151 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026152 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000013 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000017 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000034 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01132798 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01132726 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01132806 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000574 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001313 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002669 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974040 </sigma_enl_xx>
   <sigma_enl_yy>   0.00973998 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974045 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000315 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000748 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001520 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392342 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392368 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392336 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000672 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001096 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002210 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274100 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274100 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274100 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062211 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062179 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062216 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000310 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000768 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001558 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000084 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000084 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000082 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000373 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000026 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000046 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93014058 </ekin>
  <econf>        0.01800653 </econf>
  <eps>         -2.63169438 </eps>
  <enl>          2.02065728 </enl>
  <ecoul>       -7.85200165 </ecoul>
  <exc>         -2.39141603 </exc>
  <esr>          0.04701159 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90630766 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90630766 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10800467   5.10751900   0.00695560"
    b="  0.02279658   5.09161396   5.09219567"
    c="  5.11307248   0.00181412   5.11296354" />
  <atom name="Si1" species="silicon">
    <position> 1.28742275 1.26119816 1.27146465 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00123912 0.00252087 0.00063892 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28742274 -1.26119816 -1.27146465 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00123912 -0.00252087 -0.00063892 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.223469 </unit_cell_a_norm>
<unit_cell_b_norm> 7.201077 </unit_cell_b_norm>
<unit_cell_c_norm> 7.230900 </unit_cell_c_norm>
<unit_cell_alpha>  59.839 </unit_cell_alpha>
<unit_cell_beta>   59.941 </unit_cell_beta>
<unit_cell_gamma>  59.810 </unit_cell_gamma>
<unit_cell_volume> 265.138 </unit_cell_volume>
  <econst> -7.90630766 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.02462671 </sigma_eks_xx>
   <sigma_eks_yy>  -0.02472312 </sigma_eks_yy>
   <sigma_eks_zz>  -0.02417615 </sigma_eks_zz>
   <sigma_eks_xy>  -0.10979884 </sigma_eks_xy>
   <sigma_eks_yz>   0.00750446 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01363536 </sigma_eks_xz>

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

   <sigma_xx>  -0.02462671 </sigma_xx>
   <sigma_yy>  -0.02472312 </sigma_yy>
   <sigma_zz>  -0.02417615 </sigma_zz>
   <sigma_xy>  -0.10979884 </sigma_xy>
   <sigma_yz>   0.00750446 </sigma_yz>
   <sigma_xz>  -0.01363536 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28290196 </eigenvalue_sum>
  <etotal_int>     -23.09163174 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28305891 </eigenvalue_sum>
  <etotal_int>     -23.09192006 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28316900 </eigenvalue_sum>
  <etotal_int>     -23.09212215 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28324849 </eigenvalue_sum>
  <etotal_int>     -23.09226805 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28330751 </eigenvalue_sum>
  <etotal_int>     -23.09237636 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28335252 </eigenvalue_sum>
  <etotal_int>     -23.09245895 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338773 </eigenvalue_sum>
  <etotal_int>     -23.09252356 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341594 </eigenvalue_sum>
  <etotal_int>     -23.09257532 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28343903 </eigenvalue_sum>
  <etotal_int>     -23.09261770 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28345831 </eigenvalue_sum>
  <etotal_int>     -23.09265309 </etotal_int>
  <timing name="iteration" min="    0.220" max="    0.221"/>
</iteration>
<iteration count="17">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00736938 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00736966 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00736932 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000992 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001292 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002598 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026157 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026156 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026157 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000012 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000016 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000033 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133091 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133024 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133097 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000654 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001231 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002495 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974261 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974222 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974265 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000364 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000700 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001420 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392388 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392412 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392385 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000701 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00001033 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002077 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274160 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274160 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274160 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062255 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062225 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062258 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000366 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000717 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001451 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000029 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000027 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000029 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000202 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000057 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000112 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93035825 </ekin>
  <econf>        0.01800742 </econf>
  <eps>         -2.63186537 </eps>
  <enl>          2.02072574 </enl>
  <ecoul>       -7.85202695 </ecoul>
  <exc>         -2.39151197 </exc>
  <esr>          0.04704086 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90631288 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90631288 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10635883   5.10587220   0.00687031"
    b="  0.02127451   5.09140479   5.09200383"
    c="  5.11257769   0.00057861   5.11248800" />
  <atom name="Si1" species="silicon">
    <position> 1.28663356 1.26149146 1.27154406 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00115623 0.00234916 0.00070360 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28663355 -1.26149146 -1.27154406 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00115623 -0.00234916 -0.00070360 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.221141 </unit_cell_a_norm>
<unit_cell_b_norm> 7.200789 </unit_cell_b_norm>
<unit_cell_c_norm> 7.230213 </unit_cell_c_norm>
<unit_cell_alpha>  59.856 </unit_cell_alpha>
<unit_cell_beta>   59.950 </unit_cell_beta>
<unit_cell_gamma>  59.821 </unit_cell_gamma>
<unit_cell_volume> 265.091 </unit_cell_volume>
  <econst> -7.90631288 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00856572 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00788937 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00845246 </sigma_eks_zz>
   <sigma_eks_xy>  -0.05946708 </sigma_eks_xy>
   <sigma_eks_yz>   0.01673654 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03308355 </sigma_eks_xz>

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

   <sigma_xx>  -0.00856572 </sigma_xx>
   <sigma_yy>  -0.00788937 </sigma_yy>
   <sigma_zz>  -0.00845246 </sigma_zz>
   <sigma_xy>  -0.05946708 </sigma_xy>
   <sigma_yz>   0.01673654 </sigma_yz>
   <sigma_xz>  -0.03308355 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28334527 </eigenvalue_sum>
  <etotal_int>     -23.09244869 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28337869 </eigenvalue_sum>
  <etotal_int>     -23.09251016 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28340386 </eigenvalue_sum>
  <etotal_int>     -23.09255641 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28342350 </eigenvalue_sum>
  <etotal_int>     -23.09259248 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28343930 </eigenvalue_sum>
  <etotal_int>     -23.09262149 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28345234 </eigenvalue_sum>
  <etotal_int>     -23.09264542 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28346333 </eigenvalue_sum>
  <etotal_int>     -23.09266561 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28347277 </eigenvalue_sum>
  <etotal_int>     -23.09268294 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28348101 </eigenvalue_sum>
  <etotal_int>     -23.09269805 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28348827 </eigenvalue_sum>
  <etotal_int>     -23.09271139 </etotal_int>
  <timing name="iteration" min="    0.224" max="    0.224"/>
</iteration>
<iteration count="18">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00736967 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00736994 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00736963 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000985 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001244 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002499 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026158 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026157 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026158 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000012 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000016 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000031 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133134 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133071 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133140 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000665 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001179 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002388 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974288 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974251 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974292 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000372 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000671 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001358 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392399 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392421 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392396 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000672 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000997 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00002005 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274170 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274170 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274170 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062262 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062235 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062266 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000372 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000687 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001389 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000028 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000026 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000027 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000222 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000053 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000103 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93038463 </ekin>
  <econf>        0.01800732 </econf>
  <eps>         -2.63187415 </eps>
  <enl>          2.02071272 </enl>
  <ecoul>       -7.85202179 </ecoul>
  <exc>         -2.39152497 </exc>
  <esr>          0.04704618 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90631624 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90631624 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10582167   5.10534309   0.00669284"
    b="  0.02044160   5.09153280   5.09212567"
    c="  5.11216676   0.00027675   5.11208418" />
  <atom name="Si1" species="silicon">
    <position> 1.28617558 1.26188398 1.27163459 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00111738 0.00226807 0.00068391 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28617558 -1.26188398 -1.27163459 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00111738 -0.00226807 -0.00068391 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.220387 </unit_cell_a_norm>
<unit_cell_b_norm> 7.200963 </unit_cell_b_norm>
<unit_cell_c_norm> 7.229637 </unit_cell_c_norm>
<unit_cell_alpha>  59.864 </unit_cell_alpha>
<unit_cell_beta>   59.953 </unit_cell_beta>
<unit_cell_gamma>  59.827 </unit_cell_gamma>
<unit_cell_volume> 265.082 </unit_cell_volume>
  <econst> -7.90631624 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00836329 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00756230 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00791544 </sigma_eks_zz>
   <sigma_eks_xy>  -0.06531098 </sigma_eks_xy>
   <sigma_eks_yz>   0.01558363 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03036990 </sigma_eks_xz>

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

   <sigma_xx>  -0.00836329 </sigma_xx>
   <sigma_yy>  -0.00756230 </sigma_yy>
   <sigma_zz>  -0.00791544 </sigma_zz>
   <sigma_xy>  -0.06531098 </sigma_xy>
   <sigma_yz>   0.01558363 </sigma_yz>
   <sigma_xz>  -0.03036990 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28320788 </eigenvalue_sum>
  <etotal_int>     -23.09220049 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28325431 </eigenvalue_sum>
  <etotal_int>     -23.09228588 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28328688 </eigenvalue_sum>
  <etotal_int>     -23.09234573 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28331050 </eigenvalue_sum>
  <etotal_int>     -23.09238910 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28332815 </eigenvalue_sum>
  <etotal_int>     -23.09242152 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28334173 </eigenvalue_sum>
  <etotal_int>     -23.09244645 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28335246 </eigenvalue_sum>
  <etotal_int>     -23.09246615 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28336115 </eigenvalue_sum>
  <etotal_int>     -23.09248210 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28336835 </eigenvalue_sum>
  <etotal_int>     -23.09249531 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28337442 </eigenvalue_sum>
  <etotal_int>     -23.09250645 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.221"/>
</iteration>
<iteration count="19">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737026 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737052 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737023 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000915 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001195 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002398 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026158 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000011 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000015 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000030 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133228 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133168 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133233 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000690 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001117 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002258 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974358 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974324 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974362 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000388 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000635 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001284 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392414 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392435 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392411 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000672 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000948 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001904 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274189 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274189 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274189 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062276 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062251 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062279 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000391 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000649 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001311 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000011 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000007 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000011 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000143 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000064 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000128 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93045467 </ekin>
  <econf>        0.01800761 </econf>
  <eps>         -2.63192946 </eps>
  <enl>          2.02073331 </enl>
  <ecoul>       -7.85202975 </ecoul>
  <exc>         -2.39155641 </exc>
  <esr>          0.04705587 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90632003 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90632003 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10495018   5.10448112   0.00651642"
    b="  0.01931695   5.09162072   5.09221341"
    c="  5.11170272  -0.00030529   5.11163483" />
  <atom name="Si1" species="silicon">
    <position> 1.28558560 1.26229108 1.27174077 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00105710 0.00214259 0.00069955 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28558560 -1.26229108 -1.27174077 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00105710 -0.00214259 -0.00069955 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.219161 </unit_cell_a_norm>
<unit_cell_b_norm> 7.201084 </unit_cell_b_norm>
<unit_cell_c_norm> 7.228991 </unit_cell_c_norm>
<unit_cell_alpha>  59.875 </unit_cell_alpha>
<unit_cell_beta>   59.958 </unit_cell_beta>
<unit_cell_gamma>  59.836 </unit_cell_gamma>
<unit_cell_volume> 265.067 </unit_cell_volume>
  <econst> -7.90632003 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00332481 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00214478 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00311778 </sigma_eks_zz>
   <sigma_eks_xy>  -0.04221870 </sigma_eks_xy>
   <sigma_eks_yz>   0.01896649 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03771194 </sigma_eks_xz>

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

   <sigma_xx>  -0.00332481 </sigma_xx>
   <sigma_yy>  -0.00214478 </sigma_yy>
   <sigma_zz>  -0.00311778 </sigma_zz>
   <sigma_xy>  -0.04221870 </sigma_xy>
   <sigma_yz>   0.01896649 </sigma_yz>
   <sigma_xz>  -0.03771194 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28334539 </eigenvalue_sum>
  <etotal_int>     -23.09245583 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28335664 </eigenvalue_sum>
  <etotal_int>     -23.09247661 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28336484 </eigenvalue_sum>
  <etotal_int>     -23.09249174 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28337114 </eigenvalue_sum>
  <etotal_int>     -23.09250333 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28337615 </eigenvalue_sum>
  <etotal_int>     -23.09251255 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338027 </eigenvalue_sum>
  <etotal_int>     -23.09252012 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338374 </eigenvalue_sum>
  <etotal_int>     -23.09252649 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338672 </eigenvalue_sum>
  <etotal_int>     -23.09253197 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338933 </eigenvalue_sum>
  <etotal_int>     -23.09253677 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28339164 </eigenvalue_sum>
  <etotal_int>     -23.09254101 </etotal_int>
  <timing name="iteration" min="    0.220" max="    0.220"/>
</iteration>
<iteration count="20">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737042 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737067 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737039 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000889 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001149 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002304 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026158 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000011 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000014 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000029 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133251 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133195 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133256 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000688 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001069 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002158 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974374 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974342 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974377 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000388 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000607 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001226 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392419 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392438 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000649 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000911 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001828 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274194 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274194 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274194 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062280 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062256 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062283 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000391 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000621 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001252 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000009 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000008 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000138 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000064 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000127 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93047150 </ekin>
  <econf>        0.01800762 </econf>
  <eps>         -2.63194015 </eps>
  <enl>          2.02073246 </enl>
  <ecoul>       -7.85202981 </ecoul>
  <exc>         -2.39156463 </exc>
  <esr>          0.04705873 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90632301 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90632301 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10450162   5.10404542   0.00631445"
    b="  0.01850003   5.09180184   5.09238383"
    c="  5.11126784  -0.00051882   5.11120801" />
  <atom name="Si1" species="silicon">
    <position> 1.28513712 1.26271266 1.27184088 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00101544 0.00205597 0.00068377 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28513712 -1.26271266 -1.27184088 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00101544 -0.00205597 -0.00068377 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.218536 </unit_cell_a_norm>
<unit_cell_b_norm> 7.201331 </unit_cell_b_norm>
<unit_cell_c_norm> 7.228382 </unit_cell_c_norm>
<unit_cell_alpha>  59.882 </unit_cell_alpha>
<unit_cell_beta>   59.961 </unit_cell_beta>
<unit_cell_gamma>  59.842 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90632301 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00263588 </sigma_eks_xx>
   <sigma_eks_yy>  -0.00129315 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00235959 </sigma_eks_zz>
   <sigma_eks_xy>  -0.04057731 </sigma_eks_xy>
   <sigma_eks_yz>   0.01890570 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03746395 </sigma_eks_xz>

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

   <sigma_xx>  -0.00263588 </sigma_xx>
   <sigma_yy>  -0.00129315 </sigma_yy>
   <sigma_zz>  -0.00235959 </sigma_zz>
   <sigma_xy>  -0.04057731 </sigma_xy>
   <sigma_yz>   0.01890570 </sigma_yz>
   <sigma_xz>  -0.03746395 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28336193 </eigenvalue_sum>
  <etotal_int>     -23.09248911 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28337026 </eigenvalue_sum>
  <etotal_int>     -23.09250456 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28337599 </eigenvalue_sum>
  <etotal_int>     -23.09251514 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338015 </eigenvalue_sum>
  <etotal_int>     -23.09252280 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338329 </eigenvalue_sum>
  <etotal_int>     -23.09252860 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338577 </eigenvalue_sum>
  <etotal_int>     -23.09253316 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338778 </eigenvalue_sum>
  <etotal_int>     -23.09253687 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28338946 </eigenvalue_sum>
  <etotal_int>     -23.09253996 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28339090 </eigenvalue_sum>
  <etotal_int>     -23.09254260 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28339215 </eigenvalue_sum>
  <etotal_int>     -23.09254490 </etotal_int>
  <timing name="iteration" min="    0.225" max="    0.225"/>
</iteration>
<iteration count="21">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737058 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737082 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737056 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000845 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001103 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002210 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000010 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000014 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000027 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133276 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133224 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133281 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000685 </sigma_eps_xy>
   <sigma_eps_yz>   0.00001020 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00002055 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974392 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974362 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974395 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000387 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000579 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001167 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392423 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392441 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392421 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000634 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000871 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001745 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274199 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274199 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274199 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062284 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062261 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062286 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000392 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000592 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001192 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000004 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000001 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000004 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000107 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000067 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000133 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93049096 </ekin>
  <econf>        0.01800770 </econf>
  <eps>         -2.63195601 </eps>
  <enl>          2.02073739 </enl>
  <ecoul>       -7.85203220 </ecoul>
  <exc>         -2.39157381 </exc>
  <esr>          0.04706157 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90632596 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90632596 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10401026   5.10356936   0.00610370"
    b="  0.01762156   5.09199543   5.09256577"
    c="  5.11081237  -0.00076321   5.11076237" />
  <atom name="Si1" species="silicon">
    <position> 1.28466326 1.26314630 1.27194706 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00096883 0.00195907 0.00067538 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28466325 -1.26314629 -1.27194706 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00096883 -0.00195907 -0.00067538 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.217851 </unit_cell_a_norm>
<unit_cell_b_norm> 7.201594 </unit_cell_b_norm>
<unit_cell_c_norm> 7.227745 </unit_cell_c_norm>
<unit_cell_alpha>  59.889 </unit_cell_alpha>
<unit_cell_beta>   59.964 </unit_cell_beta>
<unit_cell_gamma>  59.849 </unit_cell_gamma>
<unit_cell_volume> 265.059 </unit_cell_volume>
  <econst> -7.90632596 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00132040 </sigma_eks_xx>
   <sigma_eks_yy>   0.00019023 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00116501 </sigma_eks_zz>
   <sigma_eks_xy>  -0.03137898 </sigma_eks_xy>
   <sigma_eks_yz>   0.01963789 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03913954 </sigma_eks_xz>

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

   <sigma_xx>  -0.00132040 </sigma_xx>
   <sigma_yy>   0.00019023 </sigma_yy>
   <sigma_zz>  -0.00116501 </sigma_zz>
   <sigma_xy>  -0.03137898 </sigma_xy>
   <sigma_yz>   0.01963789 </sigma_yz>
   <sigma_xz>  -0.03913954 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341756 </eigenvalue_sum>
  <etotal_int>     -23.09259378 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341739 </eigenvalue_sum>
  <etotal_int>     -23.09259360 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341713 </eigenvalue_sum>
  <etotal_int>     -23.09259320 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341694 </eigenvalue_sum>
  <etotal_int>     -23.09259290 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341686 </eigenvalue_sum>
  <etotal_int>     -23.09259276 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341685 </eigenvalue_sum>
  <etotal_int>     -23.09259277 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341691 </eigenvalue_sum>
  <etotal_int>     -23.09259289 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341702 </eigenvalue_sum>
  <etotal_int>     -23.09259309 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341716 </eigenvalue_sum>
  <etotal_int>     -23.09259336 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28341732 </eigenvalue_sum>
  <etotal_int>     -23.09259366 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.221"/>
</iteration>
<iteration count="22">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737064 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737087 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737062 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000812 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001059 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002120 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000010 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000013 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000026 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133285 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133235 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133290 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000674 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000975 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001963 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974398 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974370 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974401 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000381 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000554 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001115 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392424 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392441 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392422 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000613 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000835 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001672 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274201 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274201 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274201 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062285 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062264 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062287 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000386 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000566 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001138 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000003 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000003 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000095 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000066 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000132 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93049848 </ekin>
  <econf>        0.01800773 </econf>
  <eps>         -2.63196233 </eps>
  <enl>          2.02073844 </enl>
  <ecoul>       -7.85203320 </ecoul>
  <exc>         -2.39157770 </exc>
  <esr>          0.04706278 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90632858 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90632858 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10365527   5.10323117   0.00588753"
    b="  0.01685418   5.09221042   5.09276483"
    c="  5.11036592  -0.00088562   5.11032308" />
  <atom name="Si1" species="silicon">
    <position> 1.28423936 1.26357776 1.27204896 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00092818 0.00187479 0.00065798 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28423936 -1.26357776 -1.27204896 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00092818 -0.00187479 -0.00065798 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.217361 </unit_cell_a_norm>
<unit_cell_b_norm> 7.201885 </unit_cell_b_norm>
<unit_cell_c_norm> 7.227119 </unit_cell_c_norm>
<unit_cell_alpha>  59.895 </unit_cell_alpha>
<unit_cell_beta>   59.966 </unit_cell_beta>
<unit_cell_gamma>  59.856 </unit_cell_gamma>
<unit_cell_volume> 265.058 </unit_cell_volume>
  <econst> -7.90632858 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00091172 </sigma_eks_xx>
   <sigma_eks_yy>   0.00070462 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00079097 </sigma_eks_zz>
   <sigma_eks_xy>  -0.02808034 </sigma_eks_xy>
   <sigma_eks_yz>   0.01955141 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03895983 </sigma_eks_xz>

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

   <sigma_xx>  -0.00091172 </sigma_xx>
   <sigma_yy>   0.00070462 </sigma_yy>
   <sigma_zz>  -0.00079097 </sigma_zz>
   <sigma_xy>  -0.02808034 </sigma_xy>
   <sigma_yz>   0.01955141 </sigma_yz>
   <sigma_xz>  -0.03895983 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28345420 </eigenvalue_sum>
  <etotal_int>     -23.09266342 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28345150 </eigenvalue_sum>
  <etotal_int>     -23.09265860 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344937 </eigenvalue_sum>
  <etotal_int>     -23.09265475 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344775 </eigenvalue_sum>
  <etotal_int>     -23.09265182 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344654 </eigenvalue_sum>
  <etotal_int>     -23.09264962 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344562 </eigenvalue_sum>
  <etotal_int>     -23.09264795 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344492 </eigenvalue_sum>
  <etotal_int>     -23.09264668 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344439 </eigenvalue_sum>
  <etotal_int>     -23.09264571 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344397 </eigenvalue_sum>
  <etotal_int>     -23.09264496 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28344365 </eigenvalue_sum>
  <etotal_int>     -23.09264437 </etotal_int>
  <timing name="iteration" min="    0.222" max="    0.222"/>
</iteration>
<iteration count="23">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737068 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737090 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737066 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000777 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00001016 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00002033 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000010 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000013 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000025 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133290 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133244 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133295 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000660 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000933 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001875 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974402 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974375 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974404 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000373 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000530 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001065 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392425 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392440 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392423 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000593 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000800 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001600 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274202 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274202 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274202 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062286 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062266 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062288 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000379 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000541 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001086 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000002 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000002 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000082 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000066 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000132 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050367 </ekin>
  <econf>        0.01800775 </econf>
  <eps>         -2.63196744 </eps>
  <enl>          2.02073984 </enl>
  <ecoul>       -7.85203436 </ecoul>
  <exc>         -2.39158048 </exc>
  <esr>          0.04706358 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90633102 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90633102 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10333016   5.10292430   0.00566909"
    b="  0.01610807   5.09243321   5.09296968"
    c="  5.10991862  -0.00097952   5.10988241" />
  <atom name="Si1" species="silicon">
    <position> 1.28382698 1.26400648 1.27214985 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00088833 0.00179225 0.00064050 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28382697 -1.26400648 -1.27214985 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00088833 -0.00179225 -0.00064050 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.216914 </unit_cell_a_norm>
<unit_cell_b_norm> 7.202185 </unit_cell_b_norm>
<unit_cell_c_norm> 7.226491 </unit_cell_c_norm>
<unit_cell_alpha>  59.900 </unit_cell_alpha>
<unit_cell_beta>   59.968 </unit_cell_beta>
<unit_cell_gamma>  59.862 </unit_cell_gamma>
<unit_cell_volume> 265.057 </unit_cell_volume>
  <econst> -7.90633102 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00057280 </sigma_eks_xx>
   <sigma_eks_yy>   0.00111253 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00051977 </sigma_eks_zz>
   <sigma_eks_xy>  -0.02407229 </sigma_eks_xy>
   <sigma_eks_yz>   0.01939814 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03870801 </sigma_eks_xz>

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

   <sigma_xx>  -0.00057280 </sigma_xx>
   <sigma_yy>   0.00111253 </sigma_yy>
   <sigma_zz>  -0.00051977 </sigma_zz>
   <sigma_xy>  -0.02407229 </sigma_xy>
   <sigma_yz>   0.01939814 </sigma_yz>
   <sigma_xz>  -0.03870801 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28349084 </eigenvalue_sum>
  <etotal_int>     -23.09273284 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28348618 </eigenvalue_sum>
  <etotal_int>     -23.09272443 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28348267 </eigenvalue_sum>
  <etotal_int>     -23.09271804 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28348003 </eigenvalue_sum>
  <etotal_int>     -23.09271323 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28347803 </eigenvalue_sum>
  <etotal_int>     -23.09270959 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28347649 </eigenvalue_sum>
  <etotal_int>     -23.09270679 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28347530 </eigenvalue_sum>
  <etotal_int>     -23.09270460 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28347435 </eigenvalue_sum>
  <etotal_int>     -23.09270287 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28347359 </eigenvalue_sum>
  <etotal_int>     -23.09270148 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28347297 </eigenvalue_sum>
  <etotal_int>     -23.09270034 </etotal_int>
  <timing name="iteration" min="    0.223" max="    0.224"/>
</iteration>
<iteration count="24">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737069 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737090 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737067 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000746 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000975 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001949 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000009 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000012 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000024 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133291 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133248 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133296 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000642 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000893 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001793 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974402 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974378 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974405 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000364 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000507 </sigma_enl_yz>
   <sigma_enl_xz>   0.00001018 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392425 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392439 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392423 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000572 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000766 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001532 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274203 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274203 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274203 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062286 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062268 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062288 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000370 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000517 </sigma_esr_yz>
   <sigma_esr_xz>   0.00001038 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000073 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000065 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000129 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050609 </ekin>
  <econf>        0.01800777 </econf>
  <eps>         -2.63197044 </eps>
  <enl>          2.02074063 </enl>
  <ecoul>       -7.85203530 </ecoul>
  <exc>         -2.39158200 </exc>
  <esr>          0.04706398 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90633324 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90633324 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10305584   5.10266890   0.00545267"
    b="  0.01541311   5.09265831   5.09317496"
    c="  5.10948026  -0.00102956   5.10944941" />
  <atom name="Si1" species="silicon">
    <position> 1.28343889 1.26442563 1.27224716 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00085103 0.00171518 0.00062081 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28343889 -1.26442563 -1.27224716 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00085103 -0.00171518 -0.00062081 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.216539 </unit_cell_a_norm>
<unit_cell_b_norm> 7.202488 </unit_cell_b_norm>
<unit_cell_c_norm> 7.225875 </unit_cell_c_norm>
<unit_cell_alpha>  59.905 </unit_cell_alpha>
<unit_cell_beta>   59.970 </unit_cell_beta>
<unit_cell_gamma>  59.867 </unit_cell_gamma>
<unit_cell_volume> 265.057 </unit_cell_volume>
  <econst> -7.90633324 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00041556 </sigma_eks_xx>
   <sigma_eks_yy>   0.00130859 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00041069 </sigma_eks_zz>
   <sigma_eks_xy>  -0.02152995 </sigma_eks_xy>
   <sigma_eks_yz>   0.01905336 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03802387 </sigma_eks_xz>

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

   <sigma_xx>  -0.00041556 </sigma_xx>
   <sigma_yy>   0.00130859 </sigma_yy>
   <sigma_zz>  -0.00041069 </sigma_zz>
   <sigma_xy>  -0.02152995 </sigma_xy>
   <sigma_yz>   0.01905336 </sigma_yz>
   <sigma_xz>  -0.03802387 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28352280 </eigenvalue_sum>
  <etotal_int>     -23.09279352 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28351741 </eigenvalue_sum>
  <etotal_int>     -23.09278375 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28351336 </eigenvalue_sum>
  <etotal_int>     -23.09277637 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28351032 </eigenvalue_sum>
  <etotal_int>     -23.09277082 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28350801 </eigenvalue_sum>
  <etotal_int>     -23.09276660 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28350622 </eigenvalue_sum>
  <etotal_int>     -23.09276333 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28350481 </eigenvalue_sum>
  <etotal_int>     -23.09276076 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28350368 </eigenvalue_sum>
  <etotal_int>     -23.09275870 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28350276 </eigenvalue_sum>
  <etotal_int>     -23.09275702 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28350200 </eigenvalue_sum>
  <etotal_int>     -23.09275563 </etotal_int>
  <timing name="iteration" min="    0.220" max="    0.220"/>
</iteration>
<iteration count="25">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737069 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737089 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737067 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000715 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000935 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001868 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000009 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000012 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000023 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133291 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133250 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133295 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000623 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000855 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001715 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974402 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974379 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974404 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000353 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000485 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000974 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392424 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392438 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392423 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000552 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000734 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001467 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274203 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274203 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274203 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062286 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062269 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062288 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000359 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000495 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000993 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000005 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000066 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000063 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000126 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050732 </ekin>
  <econf>        0.01800779 </econf>
  <eps>         -2.63197260 </eps>
  <enl>          2.02074130 </enl>
  <ecoul>       -7.85203617 </ecoul>
  <exc>         -2.39158294 </exc>
  <esr>          0.04706419 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90633530 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90633530 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10281007   5.10244254   0.00523944"
    b="  0.01475113   5.09288261   5.09337824"
    c="  5.10905014  -0.00105614   5.10902384" />
  <atom name="Si1" species="silicon">
    <position> 1.28306765 1.26483428 1.27234137 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00081538 0.00164165 0.00060061 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28306765 -1.26483428 -1.27234137 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00081538 -0.00164165 -0.00060061 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.216205 </unit_cell_a_norm>
<unit_cell_b_norm> 7.202789 </unit_cell_b_norm>
<unit_cell_c_norm> 7.225269 </unit_cell_c_norm>
<unit_cell_alpha>  59.910 </unit_cell_alpha>
<unit_cell_beta>   59.972 </unit_cell_beta>
<unit_cell_gamma>  59.873 </unit_cell_gamma>
<unit_cell_volume> 265.057 </unit_cell_volume>
  <econst> -7.90633530 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00031666 </sigma_eks_xx>
   <sigma_eks_yy>   0.00141895 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00035849 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01931530 </sigma_eks_xy>
   <sigma_eks_yz>   0.01861423 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03715313 </sigma_eks_xz>

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

   <sigma_xx>  -0.00031666 </sigma_xx>
   <sigma_yy>   0.00141895 </sigma_yy>
   <sigma_zz>  -0.00035849 </sigma_zz>
   <sigma_xy>  -0.01931530 </sigma_xy>
   <sigma_yz>   0.01861423 </sigma_yz>
   <sigma_xz>  -0.03715313 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28355202 </eigenvalue_sum>
  <etotal_int>     -23.09284899 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28354635 </eigenvalue_sum>
  <etotal_int>     -23.09283870 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28354211 </eigenvalue_sum>
  <etotal_int>     -23.09283097 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28353892 </eigenvalue_sum>
  <etotal_int>     -23.09282516 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28353650 </eigenvalue_sum>
  <etotal_int>     -23.09282073 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28353462 </eigenvalue_sum>
  <etotal_int>     -23.09281729 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28353313 </eigenvalue_sum>
  <etotal_int>     -23.09281457 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28353194 </eigenvalue_sum>
  <etotal_int>     -23.09281239 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28353096 </eigenvalue_sum>
  <etotal_int>     -23.09281059 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28353014 </eigenvalue_sum>
  <etotal_int>     -23.09280910 </etotal_int>
  <timing name="iteration" min="    0.266" max="    0.266"/>
</iteration>
<iteration count="26">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737069 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737087 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737067 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000686 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000897 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001791 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000009 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000011 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000022 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133290 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133294 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000603 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000819 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001641 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974401 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974379 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974403 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000342 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000465 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000932 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392424 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392437 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392422 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000531 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000704 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001405 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274202 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274202 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274202 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062286 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062270 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062287 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000348 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000474 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000950 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000005 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000060 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000062 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000123 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050777 </ekin>
  <econf>        0.01800780 </econf>
  <eps>         -2.63197413 </eps>
  <enl>          2.02074183 </enl>
  <ecoul>       -7.85203695 </ecoul>
  <exc>         -2.39158350 </exc>
  <esr>          0.04706428 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90633718 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90633718 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10259037   5.10224235   0.00503125"
    b="  0.01412395   5.09310327   5.09357711"
    c="  5.10863142  -0.00106306   5.10860884" />
  <atom name="Si1" species="silicon">
    <position> 1.28271409 1.26523026 1.27243204 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00078148 0.00157188 0.00057998 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28271409 -1.26523026 -1.27243204 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00078148 -0.00157188 -0.00057998 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.215908 </unit_cell_a_norm>
<unit_cell_b_norm> 7.203085 </unit_cell_b_norm>
<unit_cell_c_norm> 7.224680 </unit_cell_c_norm>
<unit_cell_alpha>  59.914 </unit_cell_alpha>
<unit_cell_beta>   59.973 </unit_cell_beta>
<unit_cell_gamma>  59.878 </unit_cell_gamma>
<unit_cell_volume> 265.058 </unit_cell_volume>
  <econst> -7.90633718 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00026299 </sigma_eks_xx>
   <sigma_eks_yy>   0.00146365 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00034307 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01760634 </sigma_eks_xy>
   <sigma_eks_yz>   0.01810924 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03613884 </sigma_eks_xz>

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

   <sigma_xx>  -0.00026299 </sigma_xx>
   <sigma_yy>   0.00146365 </sigma_yy>
   <sigma_zz>  -0.00034307 </sigma_zz>
   <sigma_xy>  -0.01760634 </sigma_xy>
   <sigma_yz>   0.01810924 </sigma_yz>
   <sigma_xz>  -0.03613884 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28357857 </eigenvalue_sum>
  <etotal_int>     -23.09289941 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28357293 </eigenvalue_sum>
  <etotal_int>     -23.09288918 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28356873 </eigenvalue_sum>
  <etotal_int>     -23.09288152 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28356558 </eigenvalue_sum>
  <etotal_int>     -23.09287575 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28356317 </eigenvalue_sum>
  <etotal_int>     -23.09287136 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28356130 </eigenvalue_sum>
  <etotal_int>     -23.09286794 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28355982 </eigenvalue_sum>
  <etotal_int>     -23.09286523 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28355862 </eigenvalue_sum>
  <etotal_int>     -23.09286305 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28355764 </eigenvalue_sum>
  <etotal_int>     -23.09286125 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28355682 </eigenvalue_sum>
  <etotal_int>     -23.09285975 </etotal_int>
  <timing name="iteration" min="    0.223" max="    0.224"/>
</iteration>
<iteration count="27">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737068 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737085 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737066 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000658 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000860 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001716 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000008 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000011 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000021 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133288 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133292 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000583 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000784 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001571 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974399 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974379 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974401 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000330 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000445 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000892 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392423 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392435 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392422 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000511 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000675 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001346 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274202 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274202 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274202 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062285 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062271 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062287 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000336 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000454 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000909 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000005 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000055 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000060 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000119 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050781 </ekin>
  <econf>        0.01800781 </econf>
  <eps>         -2.63197529 </eps>
  <enl>          2.02074228 </enl>
  <ecoul>       -7.85203767 </ecoul>
  <exc>         -2.39158385 </exc>
  <esr>          0.04706430 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90633891 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90633891 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10239015   5.10206154   0.00482872"
    b="  0.01352666   5.09331904   5.09377068"
    c="  5.10822463  -0.00105682   5.10820511" />
  <atom name="Si1" species="silicon">
    <position> 1.28237619 1.26561313 1.27251931 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00074912 0.00150540 0.00055932 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28237619 -1.26561313 -1.27251931 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00074912 -0.00150540 -0.00055932 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.215639 </unit_cell_a_norm>
<unit_cell_b_norm> 7.203373 </unit_cell_b_norm>
<unit_cell_c_norm> 7.224107 </unit_cell_c_norm>
<unit_cell_alpha>  59.918 </unit_cell_alpha>
<unit_cell_beta>   59.974 </unit_cell_beta>
<unit_cell_gamma>  59.883 </unit_cell_gamma>
<unit_cell_volume> 265.058 </unit_cell_volume>
  <econst> -7.90633891 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00023048 </sigma_eks_xx>
   <sigma_eks_yy>   0.00146971 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00034285 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01618397 </sigma_eks_xy>
   <sigma_eks_yz>   0.01756034 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03503357 </sigma_eks_xz>

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

   <sigma_xx>  -0.00023048 </sigma_xx>
   <sigma_yy>   0.00146971 </sigma_yy>
   <sigma_zz>  -0.00034285 </sigma_zz>
   <sigma_xy>  -0.01618397 </sigma_xy>
   <sigma_yz>   0.01756034 </sigma_yz>
   <sigma_xz>  -0.03503357 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28360282 </eigenvalue_sum>
  <etotal_int>     -23.09294549 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28359739 </eigenvalue_sum>
  <etotal_int>     -23.09293562 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28359334 </eigenvalue_sum>
  <etotal_int>     -23.09292824 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28359030 </eigenvalue_sum>
  <etotal_int>     -23.09292268 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28358799 </eigenvalue_sum>
  <etotal_int>     -23.09291845 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28358618 </eigenvalue_sum>
  <etotal_int>     -23.09291515 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28358475 </eigenvalue_sum>
  <etotal_int>     -23.09291253 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28358360 </eigenvalue_sum>
  <etotal_int>     -23.09291042 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28358264 </eigenvalue_sum>
  <etotal_int>     -23.09290868 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28358185 </eigenvalue_sum>
  <etotal_int>     -23.09290722 </etotal_int>
  <timing name="iteration" min="    0.226" max="    0.226"/>
</iteration>
<iteration count="28">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737067 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737083 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737065 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000631 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000825 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001645 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000008 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000010 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000020 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133286 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133289 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000562 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000752 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001504 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974397 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974379 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974400 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000319 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000427 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000854 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392423 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392434 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392421 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000491 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000647 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001289 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274201 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274201 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274201 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062285 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062271 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062287 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000325 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000435 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000870 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000005 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000051 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000058 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000115 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050762 </ekin>
  <econf>        0.01800781 </econf>
  <eps>         -2.63197621 </eps>
  <enl>          2.02074267 </enl>
  <ecoul>       -7.85203833 </ecoul>
  <exc>         -2.39158406 </exc>
  <esr>          0.04706429 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634050 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634050 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10220622   5.10189672   0.00463253"
    b="  0.01295762   5.09352883   5.09395819"
    c="  5.10783081  -0.00104099   5.10781378" />
  <atom name="Si1" species="silicon">
    <position> 1.28205326 1.26598239 1.27260320 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00071822 0.00144201 0.00053883 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28205326 -1.26598238 -1.27260320 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00071822 -0.00144201 -0.00053883 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.215392 </unit_cell_a_norm>
<unit_cell_b_norm> 7.203653 </unit_cell_b_norm>
<unit_cell_c_norm> 7.223552 </unit_cell_c_norm>
<unit_cell_alpha>  59.921 </unit_cell_alpha>
<unit_cell_beta>   59.976 </unit_cell_beta>
<unit_cell_gamma>  59.888 </unit_cell_gamma>
<unit_cell_volume> 265.059 </unit_cell_volume>
  <econst> -7.90634050 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00021042 </sigma_eks_xx>
   <sigma_eks_yy>   0.00144999 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00034879 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01500927 </sigma_eks_xy>
   <sigma_eks_yz>   0.01698770 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03387733 </sigma_eks_xz>

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

   <sigma_xx>  -0.00021042 </sigma_xx>
   <sigma_yy>   0.00144999 </sigma_yy>
   <sigma_zz>  -0.00034879 </sigma_zz>
   <sigma_xy>  -0.01500927 </sigma_xy>
   <sigma_yz>   0.01698770 </sigma_yz>
   <sigma_xz>  -0.03387733 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28362503 </eigenvalue_sum>
  <etotal_int>     -23.09298767 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28361989 </eigenvalue_sum>
  <etotal_int>     -23.09297833 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28361605 </eigenvalue_sum>
  <etotal_int>     -23.09297134 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28361318 </eigenvalue_sum>
  <etotal_int>     -23.09296608 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28361098 </eigenvalue_sum>
  <etotal_int>     -23.09296207 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28360927 </eigenvalue_sum>
  <etotal_int>     -23.09295894 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28360791 </eigenvalue_sum>
  <etotal_int>     -23.09295646 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28360682 </eigenvalue_sum>
  <etotal_int>     -23.09295445 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28360591 </eigenvalue_sum>
  <etotal_int>     -23.09295280 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28360516 </eigenvalue_sum>
  <etotal_int>     -23.09295141 </etotal_int>
  <timing name="iteration" min="    0.232" max="    0.232"/>
</iteration>
<iteration count="29">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737066 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737081 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737064 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000606 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000791 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001577 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000008 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000010 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000019 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133283 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133287 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000542 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000720 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001441 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974396 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974378 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974398 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000307 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000409 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000818 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392422 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392432 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392421 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000472 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000620 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001235 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274201 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274201 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274201 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062285 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062272 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062286 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000313 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000417 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000834 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000005 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000048 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000056 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000111 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050730 </ekin>
  <econf>        0.01800782 </econf>
  <eps>         -2.63197697 </eps>
  <enl>          2.02074302 </enl>
  <ecoul>       -7.85203894 </ecoul>
  <exc>         -2.39158420 </exc>
  <esr>          0.04706425 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634196 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634196 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10203564   5.10174478   0.00444293"
    b="  0.01241450   5.09373211   5.09413936"
    c="  5.10745027  -0.00101857   5.10743525" />
  <atom name="Si1" species="silicon">
    <position> 1.28174429 1.26633801 1.27268381 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00068866 0.00138150 0.00051867 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28174429 -1.26633801 -1.27268381 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00068866 -0.00138150 -0.00051867 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.215164 </unit_cell_a_norm>
<unit_cell_b_norm> 7.203924 </unit_cell_b_norm>
<unit_cell_c_norm> 7.223015 </unit_cell_c_norm>
<unit_cell_alpha>  59.925 </unit_cell_alpha>
<unit_cell_beta>   59.977 </unit_cell_beta>
<unit_cell_gamma>  59.893 </unit_cell_gamma>
<unit_cell_volume> 265.059 </unit_cell_volume>
  <econst> -7.90634196 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00019646 </sigma_eks_xx>
   <sigma_eks_yy>   0.00141365 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00035536 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01401274 </sigma_eks_xy>
   <sigma_eks_yz>   0.01640246 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03269446 </sigma_eks_xz>

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

   <sigma_xx>  -0.00019646 </sigma_xx>
   <sigma_yy>   0.00141365 </sigma_yy>
   <sigma_zz>  -0.00035536 </sigma_zz>
   <sigma_xy>  -0.01401274 </sigma_xy>
   <sigma_yz>   0.01640246 </sigma_yz>
   <sigma_xz>  -0.03269446 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28364539 </eigenvalue_sum>
  <etotal_int>     -23.09302636 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28364057 </eigenvalue_sum>
  <etotal_int>     -23.09301760 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28363698 </eigenvalue_sum>
  <etotal_int>     -23.09301105 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28363428 </eigenvalue_sum>
  <etotal_int>     -23.09300612 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28363223 </eigenvalue_sum>
  <etotal_int>     -23.09300236 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28363062 </eigenvalue_sum>
  <etotal_int>     -23.09299943 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28362935 </eigenvalue_sum>
  <etotal_int>     -23.09299711 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28362832 </eigenvalue_sum>
  <etotal_int>     -23.09299522 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28362747 </eigenvalue_sum>
  <etotal_int>     -23.09299367 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28362676 </eigenvalue_sum>
  <etotal_int>     -23.09299237 </etotal_int>
  <timing name="iteration" min="    0.219" max="    0.219"/>
</iteration>
<iteration count="30">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737065 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737080 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737063 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000581 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000759 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001511 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000007 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000009 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000019 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133281 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133285 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000521 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000690 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001380 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974394 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974378 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974396 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000296 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000392 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000783 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392421 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392431 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392420 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000453 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000594 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001184 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274201 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274201 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274201 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062284 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062272 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062286 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000301 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000400 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000798 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000005 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000045 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000054 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000107 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050693 </ekin>
  <econf>        0.01800783 </econf>
  <eps>         -2.63197761 </eps>
  <enl>          2.02074333 </enl>
  <ecoul>       -7.85203950 </ecoul>
  <exc>         -2.39158428 </exc>
  <esr>          0.04706421 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634331 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634331 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10187639   5.10160360   0.00426010"
    b="  0.01189570   5.09392852   5.09431403"
    c="  5.10708326  -0.00099165   5.10706983" />
  <atom name="Si1" species="silicon">
    <position> 1.28144857 1.26668008 1.27276126 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00066036 0.00132367 0.00049893 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28144857 -1.26668008 -1.27276126 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00066036 -0.00132367 -0.00049893 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.214951 </unit_cell_a_norm>
<unit_cell_b_norm> 7.204185 </unit_cell_b_norm>
<unit_cell_c_norm> 7.222497 </unit_cell_c_norm>
<unit_cell_alpha>  59.928 </unit_cell_alpha>
<unit_cell_beta>   59.978 </unit_cell_beta>
<unit_cell_gamma>  59.897 </unit_cell_gamma>
<unit_cell_volume> 265.059 </unit_cell_volume>
  <econst> -7.90634331 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00018553 </sigma_eks_xx>
   <sigma_eks_yy>   0.00136650 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00036004 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01315699 </sigma_eks_xy>
   <sigma_eks_yz>   0.01581468 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03150580 </sigma_eks_xz>

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

   <sigma_xx>  -0.00018553 </sigma_xx>
   <sigma_yy>   0.00136650 </sigma_yy>
   <sigma_zz>  -0.00036004 </sigma_zz>
   <sigma_xy>  -0.01315699 </sigma_xy>
   <sigma_yz>   0.01581468 </sigma_yz>
   <sigma_xz>  -0.03150580 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28366407 </eigenvalue_sum>
  <etotal_int>     -23.09306186 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28365959 </eigenvalue_sum>
  <etotal_int>     -23.09305371 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28365625 </eigenvalue_sum>
  <etotal_int>     -23.09304761 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28365374 </eigenvalue_sum>
  <etotal_int>     -23.09304303 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28365183 </eigenvalue_sum>
  <etotal_int>     -23.09303953 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28365033 </eigenvalue_sum>
  <etotal_int>     -23.09303681 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28364915 </eigenvalue_sum>
  <etotal_int>     -23.09303464 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28364819 </eigenvalue_sum>
  <etotal_int>     -23.09303288 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28364740 </eigenvalue_sum>
  <etotal_int>     -23.09303144 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28364674 </eigenvalue_sum>
  <etotal_int>     -23.09303023 </etotal_int>
  <timing name="iteration" min="    0.239" max="    0.240"/>
</iteration>
<iteration count="31">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737064 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737078 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737062 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000557 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000728 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001449 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000007 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000009 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000018 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133279 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133283 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000501 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000662 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001322 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974392 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974377 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974394 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000284 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000376 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000751 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392421 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392430 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392420 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000435 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000570 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001134 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274200 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274200 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274200 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062284 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062273 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062285 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000290 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000383 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000765 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000042 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000052 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000103 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050654 </ekin>
  <econf>        0.01800783 </econf>
  <eps>         -2.63197817 </eps>
  <enl>          2.02074361 </enl>
  <ecoul>       -7.85204001 </ecoul>
  <exc>         -2.39158434 </exc>
  <esr>          0.04706416 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634454 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634454 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10172683   5.10147146   0.00408405"
    b="  0.01139967   5.09411793   5.09448221"
    c="  5.10672975  -0.00096183   5.10671759" />
  <atom name="Si1" species="silicon">
    <position> 1.28116539 1.26700884 1.27283567 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00063327 0.00126839 0.00047970 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28116539 -1.26700884 -1.27283567 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00063327 -0.00126839 -0.00047970 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.214752 </unit_cell_a_norm>
<unit_cell_b_norm> 7.204437 </unit_cell_b_norm>
<unit_cell_c_norm> 7.221998 </unit_cell_c_norm>
<unit_cell_alpha>  59.931 </unit_cell_alpha>
<unit_cell_beta>   59.979 </unit_cell_beta>
<unit_cell_gamma>  59.902 </unit_cell_gamma>
<unit_cell_volume> 265.060 </unit_cell_volume>
  <econst> -7.90634454 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00017586 </sigma_eks_xx>
   <sigma_eks_yy>   0.00131247 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00036173 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01240934 </sigma_eks_xy>
   <sigma_eks_yz>   0.01523063 </sigma_eks_yz>
   <sigma_eks_xz>  -0.03032465 </sigma_eks_xz>

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

   <sigma_xx>  -0.00017586 </sigma_xx>
   <sigma_yy>   0.00131247 </sigma_yy>
   <sigma_zz>  -0.00036173 </sigma_zz>
   <sigma_xy>  -0.01240934 </sigma_xy>
   <sigma_yz>   0.01523063 </sigma_yz>
   <sigma_xz>  -0.03032465 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368123 </eigenvalue_sum>
  <etotal_int>     -23.09309447 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28367708 </eigenvalue_sum>
  <etotal_int>     -23.09308691 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28367398 </eigenvalue_sum>
  <etotal_int>     -23.09308126 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28367166 </eigenvalue_sum>
  <etotal_int>     -23.09307702 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28366988 </eigenvalue_sum>
  <etotal_int>     -23.09307378 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28366850 </eigenvalue_sum>
  <etotal_int>     -23.09307125 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28366741 </eigenvalue_sum>
  <etotal_int>     -23.09306924 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28366652 </eigenvalue_sum>
  <etotal_int>     -23.09306761 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28366578 </eigenvalue_sum>
  <etotal_int>     -23.09306627 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28366517 </eigenvalue_sum>
  <etotal_int>     -23.09306515 </etotal_int>
  <timing name="iteration" min="    0.238" max="    0.238"/>
</iteration>
<iteration count="32">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737063 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737076 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737061 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000535 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000698 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001388 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000007 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000009 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000017 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133277 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133280 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000482 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000635 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001267 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974391 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974377 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974393 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000274 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000360 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000719 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392420 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392429 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392419 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000418 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000546 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001087 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274200 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274200 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274200 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062283 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062273 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062285 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000279 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000367 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000733 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000040 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000050 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000099 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050616 </ekin>
  <econf>        0.01800784 </econf>
  <eps>         -2.63197867 </eps>
  <enl>          2.02074386 </enl>
  <ecoul>       -7.85204048 </ecoul>
  <exc>         -2.39158438 </exc>
  <esr>          0.04706411 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634568 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634568 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10158577   5.10134709   0.00391474"
    b="  0.01092514   5.09430029   5.09464398"
    c="  5.10638962  -0.00093024   5.10637846" />
  <atom name="Si1" species="silicon">
    <position> 1.28089413 1.26732459 1.27290715 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00060731 0.00121549 0.00046102 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28089413 -1.26732459 -1.27290715 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00060731 -0.00121549 -0.00046102 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.214564 </unit_cell_a_norm>
<unit_cell_b_norm> 7.204680 </unit_cell_b_norm>
<unit_cell_c_norm> 7.221518 </unit_cell_c_norm>
<unit_cell_alpha>  59.934 </unit_cell_alpha>
<unit_cell_beta>   59.980 </unit_cell_beta>
<unit_cell_gamma>  59.906 </unit_cell_gamma>
<unit_cell_volume> 265.060 </unit_cell_volume>
  <econst> -7.90634568 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00016661 </sigma_eks_xx>
   <sigma_eks_yy>   0.00125428 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00036018 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01174706 </sigma_eks_xy>
   <sigma_eks_yz>   0.01465525 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02916136 </sigma_eks_xz>

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

   <sigma_xx>  -0.00016661 </sigma_xx>
   <sigma_yy>   0.00125428 </sigma_yy>
   <sigma_zz>  -0.00036018 </sigma_zz>
   <sigma_xy>  -0.01174706 </sigma_xy>
   <sigma_yz>   0.01465525 </sigma_yz>
   <sigma_xz>  -0.02916136 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28369700 </eigenvalue_sum>
  <etotal_int>     -23.09312442 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28369316 </eigenvalue_sum>
  <etotal_int>     -23.09311744 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28369030 </eigenvalue_sum>
  <etotal_int>     -23.09311222 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368815 </eigenvalue_sum>
  <etotal_int>     -23.09310830 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368651 </eigenvalue_sum>
  <etotal_int>     -23.09310530 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368523 </eigenvalue_sum>
  <etotal_int>     -23.09310297 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368422 </eigenvalue_sum>
  <etotal_int>     -23.09310111 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368340 </eigenvalue_sum>
  <etotal_int>     -23.09309961 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368272 </eigenvalue_sum>
  <etotal_int>     -23.09309837 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28368215 </eigenvalue_sum>
  <etotal_int>     -23.09309733 </etotal_int>
  <timing name="iteration" min="    0.274" max="    0.274"/>
</iteration>
<iteration count="33">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737062 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737074 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737061 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000513 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000669 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001331 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000006 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000008 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000016 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133275 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133278 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000463 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000608 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001214 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974389 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974376 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974391 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000263 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000345 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000689 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392420 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392428 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392419 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000401 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000524 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00001042 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274199 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274199 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274199 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062283 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062274 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062284 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000268 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000352 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000702 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000038 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000048 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000095 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050578 </ekin>
  <econf>        0.01800784 </econf>
  <eps>         -2.63197912 </eps>
  <enl>          2.02074409 </enl>
  <ecoul>       -7.85204091 </ecoul>
  <exc>         -2.39158441 </exc>
  <esr>          0.04706406 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634672 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634672 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10145223   5.10122948   0.00375205"
    b="  0.01047094   5.09447565   5.09479948"
    c="  5.10606264  -0.00089772   5.10605226" />
  <atom name="Si1" species="silicon">
    <position> 1.28063423 1.26762770 1.27297582 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00058242 0.00116486 0.00044292 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28063422 -1.26762770 -1.27297582 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00058242 -0.00116486 -0.00044292 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.214386 </unit_cell_a_norm>
<unit_cell_b_norm> 7.204913 </unit_cell_b_norm>
<unit_cell_c_norm> 7.221056 </unit_cell_c_norm>
<unit_cell_alpha>  59.937 </unit_cell_alpha>
<unit_cell_beta>   59.981 </unit_cell_beta>
<unit_cell_gamma>  59.909 </unit_cell_gamma>
<unit_cell_volume> 265.061 </unit_cell_volume>
  <econst> -7.90634672 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00015738 </sigma_eks_xx>
   <sigma_eks_yy>   0.00119385 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00035557 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01115244 </sigma_eks_xy>
   <sigma_eks_yz>   0.01409180 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02802277 </sigma_eks_xz>

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

   <sigma_xx>  -0.00015738 </sigma_xx>
   <sigma_yy>   0.00119385 </sigma_yy>
   <sigma_zz>  -0.00035557 </sigma_zz>
   <sigma_xy>  -0.01115244 </sigma_xy>
   <sigma_yz>   0.01409180 </sigma_yz>
   <sigma_xz>  -0.02802277 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371148 </eigenvalue_sum>
  <etotal_int>     -23.09315195 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28370794 </eigenvalue_sum>
  <etotal_int>     -23.09314550 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28370530 </eigenvalue_sum>
  <etotal_int>     -23.09314069 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28370332 </eigenvalue_sum>
  <etotal_int>     -23.09313708 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28370181 </eigenvalue_sum>
  <etotal_int>     -23.09313431 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28370063 </eigenvalue_sum>
  <etotal_int>     -23.09313216 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28369970 </eigenvalue_sum>
  <etotal_int>     -23.09313045 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28369894 </eigenvalue_sum>
  <etotal_int>     -23.09312906 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28369831 </eigenvalue_sum>
  <etotal_int>     -23.09312792 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28369779 </eigenvalue_sum>
  <etotal_int>     -23.09312696 </etotal_int>
  <timing name="iteration" min="    0.236" max="    0.237"/>
</iteration>
<iteration count="34">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737061 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737073 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737060 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000492 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000642 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001276 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000006 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000008 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000016 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133274 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133277 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000445 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000583 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001163 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974388 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974376 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974390 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000252 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000331 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000660 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392420 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392427 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392419 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000385 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000502 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000998 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274199 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274199 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274199 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062283 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062274 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062284 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000257 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000338 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000673 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000001 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000036 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000046 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000091 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050543 </ekin>
  <econf>        0.01800785 </econf>
  <eps>         -2.63197952 </eps>
  <enl>          2.02074430 </enl>
  <ecoul>       -7.85204131 </ecoul>
  <exc>         -2.39158443 </exc>
  <esr>          0.04706402 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634768 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634768 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10132547   5.10111786   0.00359583"
    b="  0.01003602   5.09464413   5.09494887"
    c="  5.10574853  -0.00086489   5.10573874" />
  <atom name="Si1" species="silicon">
    <position> 1.28038516 1.26791855 1.27304179 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00055855 0.00111638 0.00042541 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28038515 -1.26791854 -1.27304179 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00055855 -0.00111638 -0.00042541 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.214218 </unit_cell_a_norm>
<unit_cell_b_norm> 7.205137 </unit_cell_b_norm>
<unit_cell_c_norm> 7.220612 </unit_cell_c_norm>
<unit_cell_alpha>  59.939 </unit_cell_alpha>
<unit_cell_beta>   59.982 </unit_cell_beta>
<unit_cell_gamma>  59.913 </unit_cell_gamma>
<unit_cell_volume> 265.061 </unit_cell_volume>
  <econst> -7.90634768 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00014806 </sigma_eks_xx>
   <sigma_eks_yy>   0.00113256 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00034829 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01061235 </sigma_eks_xy>
   <sigma_eks_yz>   0.01354263 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02691376 </sigma_eks_xz>

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

   <sigma_xx>  -0.00014806 </sigma_xx>
   <sigma_yy>   0.00113256 </sigma_yy>
   <sigma_zz>  -0.00034829 </sigma_zz>
   <sigma_xy>  -0.01061235 </sigma_xy>
   <sigma_yz>   0.01354263 </sigma_yz>
   <sigma_xz>  -0.02691376 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372479 </eigenvalue_sum>
  <etotal_int>     -23.09317724 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372153 </eigenvalue_sum>
  <etotal_int>     -23.09317131 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371910 </eigenvalue_sum>
  <etotal_int>     -23.09316688 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371728 </eigenvalue_sum>
  <etotal_int>     -23.09316355 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371589 </eigenvalue_sum>
  <etotal_int>     -23.09316100 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371480 </eigenvalue_sum>
  <etotal_int>     -23.09315902 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371394 </eigenvalue_sum>
  <etotal_int>     -23.09315744 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371324 </eigenvalue_sum>
  <etotal_int>     -23.09315616 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371266 </eigenvalue_sum>
  <etotal_int>     -23.09315511 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28371218 </eigenvalue_sum>
  <etotal_int>     -23.09315422 </etotal_int>
  <timing name="iteration" min="    0.227" max="    0.227"/>
</iteration>
<iteration count="35">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737061 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737071 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737059 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000472 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000615 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001223 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000006 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000008 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000015 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133272 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133275 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000427 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000559 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001115 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974387 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974376 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974388 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000242 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000318 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000633 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392419 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392426 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392418 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000369 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000482 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000957 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274199 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274199 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274199 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062283 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062274 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062284 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000247 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000324 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000645 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000004 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000034 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000044 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000088 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050510 </ekin>
  <econf>        0.01800785 </econf>
  <eps>         -2.63197989 </eps>
  <enl>          2.02074450 </enl>
  <ecoul>       -7.85204167 </ecoul>
  <exc>         -2.39158444 </exc>
  <esr>          0.04706397 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634856 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634856 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10120486   5.10101161   0.00344591"
    b="  0.00961946   5.09480586   5.09509236"
    c="  5.10544693  -0.00083219   5.10543760" />
  <atom name="Si1" species="silicon">
    <position> 1.28014643 1.26819755 1.27310516 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00053567 0.00106995 0.00040850 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.28014643 -1.26819755 -1.27310516 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00053567 -0.00106995 -0.00040850 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.214057 </unit_cell_a_norm>
<unit_cell_b_norm> 7.205353 </unit_cell_b_norm>
<unit_cell_c_norm> 7.220186 </unit_cell_c_norm>
<unit_cell_alpha>  59.942 </unit_cell_alpha>
<unit_cell_beta>   59.982 </unit_cell_beta>
<unit_cell_gamma>  59.917 </unit_cell_gamma>
<unit_cell_volume> 265.061 </unit_cell_volume>
  <econst> -7.90634856 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00013864 </sigma_eks_xx>
   <sigma_eks_yy>   0.00107141 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00033878 </sigma_eks_zz>
   <sigma_eks_xy>  -0.01011676 </sigma_eks_xy>
   <sigma_eks_yz>   0.01300922 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02583743 </sigma_eks_xz>

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

   <sigma_xx>  -0.00013864 </sigma_xx>
   <sigma_yy>   0.00107141 </sigma_yy>
   <sigma_zz>  -0.00033878 </sigma_zz>
   <sigma_xy>  -0.01011676 </sigma_xy>
   <sigma_yz>   0.01300922 </sigma_yz>
   <sigma_xz>  -0.02583743 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373703 </eigenvalue_sum>
  <etotal_int>     -23.09320049 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373403 </eigenvalue_sum>
  <etotal_int>     -23.09319503 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373179 </eigenvalue_sum>
  <etotal_int>     -23.09319095 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373011 </eigenvalue_sum>
  <etotal_int>     -23.09318789 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372883 </eigenvalue_sum>
  <etotal_int>     -23.09318554 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372783 </eigenvalue_sum>
  <etotal_int>     -23.09318372 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372704 </eigenvalue_sum>
  <etotal_int>     -23.09318226 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372639 </eigenvalue_sum>
  <etotal_int>     -23.09318109 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372586 </eigenvalue_sum>
  <etotal_int>     -23.09318012 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28372542 </eigenvalue_sum>
  <etotal_int>     -23.09317930 </etotal_int>
  <timing name="iteration" min="    0.222" max="    0.222"/>
</iteration>
<iteration count="36">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737060 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737070 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737059 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000453 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000590 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001172 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000006 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000007 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000014 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133271 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133273 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000410 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000536 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001068 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974386 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974375 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974387 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000233 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000304 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000606 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392419 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392425 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392418 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000354 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000462 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000917 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274198 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274198 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274198 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062282 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062275 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062283 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000237 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000310 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000618 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000003 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000033 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000042 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000084 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050479 </ekin>
  <econf>        0.01800785 </econf>
  <eps>         -2.63198022 </eps>
  <enl>          2.02074468 </enl>
  <ecoul>       -7.85204201 </ecoul>
  <exc>         -2.39158446 </exc>
  <esr>          0.04706393 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90634937 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90634937 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10108992   5.10091022   0.00330210"
    b="  0.00922037   5.09496103   5.09523014"
    c="  5.10515747  -0.00079993   5.10514847" />
  <atom name="Si1" species="silicon">
    <position> 1.27991760 1.26846512 1.27316605 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00051372 0.00102547 0.00039219 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27991760 -1.26846512 -1.27316605 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00051372 -0.00102547 -0.00039219 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213904 </unit_cell_a_norm>
<unit_cell_b_norm> 7.205559 </unit_cell_b_norm>
<unit_cell_c_norm> 7.219777 </unit_cell_c_norm>
<unit_cell_alpha>  59.944 </unit_cell_alpha>
<unit_cell_beta>   59.983 </unit_cell_beta>
<unit_cell_gamma>  59.920 </unit_cell_gamma>
<unit_cell_volume> 265.061 </unit_cell_volume>
  <econst> -7.90634937 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00012919 </sigma_eks_xx>
   <sigma_eks_yy>   0.00101114 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00032752 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00965804 </sigma_eks_xy>
   <sigma_eks_yz>   0.01249253 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02479575 </sigma_eks_xz>

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

   <sigma_xx>  -0.00012919 </sigma_xx>
   <sigma_yy>   0.00101114 </sigma_yy>
   <sigma_zz>  -0.00032752 </sigma_zz>
   <sigma_xy>  -0.00965804 </sigma_xy>
   <sigma_yz>   0.01249253 </sigma_yz>
   <sigma_xz>  -0.02479575 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374828 </eigenvalue_sum>
  <etotal_int>     -23.09322187 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374551 </eigenvalue_sum>
  <etotal_int>     -23.09321684 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374346 </eigenvalue_sum>
  <etotal_int>     -23.09321309 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374191 </eigenvalue_sum>
  <etotal_int>     -23.09321026 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374073 </eigenvalue_sum>
  <etotal_int>     -23.09320811 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373981 </eigenvalue_sum>
  <etotal_int>     -23.09320643 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373908 </eigenvalue_sum>
  <etotal_int>     -23.09320509 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373849 </eigenvalue_sum>
  <etotal_int>     -23.09320401 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373800 </eigenvalue_sum>
  <etotal_int>     -23.09320312 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28373759 </eigenvalue_sum>
  <etotal_int>     -23.09320237 </etotal_int>
  <timing name="iteration" min="    0.223" max="    0.223"/>
</iteration>
<iteration count="37">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737060 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737069 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737058 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000434 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000566 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001123 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000005 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000007 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000014 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133269 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133272 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000394 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000514 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00001024 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974385 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974375 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974386 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000223 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000292 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000581 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392419 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392424 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392418 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000340 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000443 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000879 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274198 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274198 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274198 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062282 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062275 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062283 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000228 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000298 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000592 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000003 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000031 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000041 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000081 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050450 </ekin>
  <econf>        0.01800786 </econf>
  <eps>         -2.63198053 </eps>
  <enl>          2.02074484 </enl>
  <ecoul>       -7.85204232 </ecoul>
  <exc>         -2.39158447 </exc>
  <esr>          0.04706390 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635011 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635011 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10098022   5.10081330   0.00316418"
    b="  0.00883796   5.09510984   5.09536242"
    c="  5.10487975  -0.00076833   5.10487101" />
  <atom name="Si1" species="silicon">
    <position> 1.27969824 1.26872169 1.27322455 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00049266 0.00098286 0.00037647 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27969824 -1.26872169 -1.27322455 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00049266 -0.00098286 -0.00037647 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213758 </unit_cell_a_norm>
<unit_cell_b_norm> 7.205757 </unit_cell_b_norm>
<unit_cell_c_norm> 7.219384 </unit_cell_c_norm>
<unit_cell_alpha>  59.947 </unit_cell_alpha>
<unit_cell_beta>   59.984 </unit_cell_beta>
<unit_cell_gamma>  59.923 </unit_cell_gamma>
<unit_cell_volume> 265.062 </unit_cell_volume>
  <econst> -7.90635011 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00011980 </sigma_eks_xx>
   <sigma_eks_yy>   0.00095228 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00031495 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00923036 </sigma_eks_xy>
   <sigma_eks_yz>   0.01199307 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02378972 </sigma_eks_xz>

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

   <sigma_xx>  -0.00011980 </sigma_xx>
   <sigma_yy>   0.00095228 </sigma_yy>
   <sigma_zz>  -0.00031495 </sigma_zz>
   <sigma_xy>  -0.00923036 </sigma_xy>
   <sigma_yz>   0.01199307 </sigma_yz>
   <sigma_xz>  -0.02378972 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375861 </eigenvalue_sum>
  <etotal_int>     -23.09324151 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375607 </eigenvalue_sum>
  <etotal_int>     -23.09323689 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375418 </eigenvalue_sum>
  <etotal_int>     -23.09323343 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375276 </eigenvalue_sum>
  <etotal_int>     -23.09323084 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375168 </eigenvalue_sum>
  <etotal_int>     -23.09322886 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375083 </eigenvalue_sum>
  <etotal_int>     -23.09322731 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375016 </eigenvalue_sum>
  <etotal_int>     -23.09322608 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374961 </eigenvalue_sum>
  <etotal_int>     -23.09322509 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374917 </eigenvalue_sum>
  <etotal_int>     -23.09322427 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28374879 </eigenvalue_sum>
  <etotal_int>     -23.09322358 </etotal_int>
  <timing name="iteration" min="    0.239" max="    0.239"/>
</iteration>
<iteration count="38">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737059 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737067 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737058 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000417 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000542 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001076 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026160 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000005 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000007 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000013 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133268 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133252 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133270 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000378 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000493 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000981 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974384 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974375 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974385 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000214 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000280 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000557 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392418 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392423 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392418 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000326 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000424 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000842 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274198 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274198 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274198 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062282 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062275 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062283 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000219 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000285 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000568 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000003 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000030 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000039 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000078 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050424 </ekin>
  <econf>        0.01800786 </econf>
  <eps>         -2.63198081 </eps>
  <enl>          2.02074499 </enl>
  <ecoul>       -7.85204260 </ecoul>
  <exc>         -2.39158447 </exc>
  <esr>          0.04706386 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635080 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635080 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10087543   5.10072052   0.00303194"
    b="  0.00847149   5.09525249   5.09548939"
    c="  5.10461336  -0.00073754   5.10460481" />
  <atom name="Si1" species="silicon">
    <position> 1.27948795 1.26896767 1.27328075 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00047246 0.00094202 0.00036134 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27948794 -1.26896767 -1.27328075 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00047246 -0.00094202 -0.00036134 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213618 </unit_cell_a_norm>
<unit_cell_b_norm> 7.205948 </unit_cell_b_norm>
<unit_cell_c_norm> 7.219007 </unit_cell_c_norm>
<unit_cell_alpha>  59.949 </unit_cell_alpha>
<unit_cell_beta>   59.985 </unit_cell_beta>
<unit_cell_gamma>  59.927 </unit_cell_gamma>
<unit_cell_volume> 265.062 </unit_cell_volume>
  <econst> -7.90635080 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00011057 </sigma_eks_xx>
   <sigma_eks_yy>   0.00089523 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00030144 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00882923 </sigma_eks_xy>
   <sigma_eks_yz>   0.01151103 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02281973 </sigma_eks_xz>

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

   <sigma_xx>  -0.00011057 </sigma_xx>
   <sigma_yy>   0.00089523 </sigma_yy>
   <sigma_zz>  -0.00030144 </sigma_zz>
   <sigma_xy>  -0.00882923 </sigma_xy>
   <sigma_yz>   0.01151103 </sigma_yz>
   <sigma_xz>  -0.02281973 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376812 </eigenvalue_sum>
  <etotal_int>     -23.09325957 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376578 </eigenvalue_sum>
  <etotal_int>     -23.09325531 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376404 </eigenvalue_sum>
  <etotal_int>     -23.09325214 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376273 </eigenvalue_sum>
  <etotal_int>     -23.09324975 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376174 </eigenvalue_sum>
  <etotal_int>     -23.09324793 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376096 </eigenvalue_sum>
  <etotal_int>     -23.09324651 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376034 </eigenvalue_sum>
  <etotal_int>     -23.09324538 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375984 </eigenvalue_sum>
  <etotal_int>     -23.09324446 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375943 </eigenvalue_sum>
  <etotal_int>     -23.09324371 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28375908 </eigenvalue_sum>
  <etotal_int>     -23.09324308 </etotal_int>
  <timing name="iteration" min="    0.244" max="    0.244"/>
</iteration>
<iteration count="39">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737059 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737066 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737057 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000399 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000520 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00001032 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026160 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000005 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000006 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000013 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133267 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133269 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000363 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000473 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000940 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974383 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974375 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974384 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000206 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000268 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000534 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392418 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392423 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392417 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000313 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000407 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000807 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274198 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274198 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274198 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062282 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062276 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062282 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000210 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000274 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000544 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000003 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000029 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000038 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000074 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050399 </ekin>
  <econf>        0.01800786 </econf>
  <eps>         -2.63198107 </eps>
  <enl>          2.02074513 </enl>
  <ecoul>       -7.85204286 </ecoul>
  <exc>         -2.39158448 </exc>
  <esr>          0.04706383 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635143 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635143 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10077524   5.10063159   0.00290519"
    b="  0.00812025   5.09538919   5.09561126"
    c="  5.10435791  -0.00070767   5.10434949" />
  <atom name="Si1" species="silicon">
    <position> 1.27928634 1.26920346 1.27333473 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00045308 0.00090289 0.00034678 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27928633 -1.26920346 -1.27333473 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00045308 -0.00090289 -0.00034678 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213485 </unit_cell_a_norm>
<unit_cell_b_norm> 7.206130 </unit_cell_b_norm>
<unit_cell_c_norm> 7.218646 </unit_cell_c_norm>
<unit_cell_alpha>  59.951 </unit_cell_alpha>
<unit_cell_beta>   59.985 </unit_cell_beta>
<unit_cell_gamma>  59.930 </unit_cell_gamma>
<unit_cell_volume> 265.062 </unit_cell_volume>
  <econst> -7.90635143 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00010158 </sigma_eks_xx>
   <sigma_eks_yy>   0.00084027 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00028733 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00845116 </sigma_eks_xy>
   <sigma_eks_yz>   0.01104640 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02188569 </sigma_eks_xz>

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

   <sigma_xx>  -0.00010158 </sigma_xx>
   <sigma_yy>   0.00084027 </sigma_yy>
   <sigma_zz>  -0.00028733 </sigma_zz>
   <sigma_xy>  -0.00845116 </sigma_xy>
   <sigma_yz>   0.01104640 </sigma_yz>
   <sigma_xz>  -0.02188569 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377685 </eigenvalue_sum>
  <etotal_int>     -23.09327616 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377470 </eigenvalue_sum>
  <etotal_int>     -23.09327225 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377310 </eigenvalue_sum>
  <etotal_int>     -23.09326934 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377190 </eigenvalue_sum>
  <etotal_int>     -23.09326714 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377098 </eigenvalue_sum>
  <etotal_int>     -23.09326547 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377027 </eigenvalue_sum>
  <etotal_int>     -23.09326416 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376970 </eigenvalue_sum>
  <etotal_int>     -23.09326312 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376924 </eigenvalue_sum>
  <etotal_int>     -23.09326228 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376886 </eigenvalue_sum>
  <etotal_int>     -23.09326158 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28376855 </eigenvalue_sum>
  <etotal_int>     -23.09326100 </etotal_int>
  <timing name="iteration" min="    0.242" max="    0.242"/>
</iteration>
<iteration count="40">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737058 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737065 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737057 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000383 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000499 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000989 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000005 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000006 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000012 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133266 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133268 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000348 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000453 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000901 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974382 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974383 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000197 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000257 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000512 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392418 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392422 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392417 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000300 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000390 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000774 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274197 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274197 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274197 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062281 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062276 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062282 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000201 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000262 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000521 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000003 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000028 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000036 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000071 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050377 </ekin>
  <econf>        0.01800786 </econf>
  <eps>         -2.63198130 </eps>
  <enl>          2.02074525 </enl>
  <ecoul>       -7.85204310 </ecoul>
  <exc>         -2.39158449 </exc>
  <esr>          0.04706380 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635200 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635200 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10067938   5.10054628   0.00278370"
    b="  0.00778358   5.09552015   5.09572824"
    c="  5.10411297  -0.00067876   5.10410466" />
  <atom name="Si1" species="silicon">
    <position> 1.27909305 1.26942947 1.27338660 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00043449 0.00086539 0.00033277 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27909304 -1.26942947 -1.27338660 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00043449 -0.00086539 -0.00033277 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213356 </unit_cell_a_norm>
<unit_cell_b_norm> 7.206305 </unit_cell_b_norm>
<unit_cell_c_norm> 7.218300 </unit_cell_c_norm>
<unit_cell_alpha>  59.953 </unit_cell_alpha>
<unit_cell_beta>   59.986 </unit_cell_beta>
<unit_cell_gamma>  59.933 </unit_cell_gamma>
<unit_cell_volume> 265.062 </unit_cell_volume>
  <econst> -7.90635200 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00009289 </sigma_eks_xx>
   <sigma_eks_yy>   0.00078757 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00027291 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00809343 </sigma_eks_xy>
   <sigma_eks_yz>   0.01059898 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02098714 </sigma_eks_xz>

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

   <sigma_xx>  -0.00009289 </sigma_xx>
   <sigma_yy>   0.00078757 </sigma_yy>
   <sigma_zz>  -0.00027291 </sigma_zz>
   <sigma_xy>  -0.00809343 </sigma_xy>
   <sigma_yz>   0.01059898 </sigma_yz>
   <sigma_xz>  -0.02098714 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378488 </eigenvalue_sum>
  <etotal_int>     -23.09329142 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378291 </eigenvalue_sum>
  <etotal_int>     -23.09328783 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378143 </eigenvalue_sum>
  <etotal_int>     -23.09328514 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378033 </eigenvalue_sum>
  <etotal_int>     -23.09328313 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377949 </eigenvalue_sum>
  <etotal_int>     -23.09328159 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377883 </eigenvalue_sum>
  <etotal_int>     -23.09328038 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377831 </eigenvalue_sum>
  <etotal_int>     -23.09327943 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377789 </eigenvalue_sum>
  <etotal_int>     -23.09327866 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377754 </eigenvalue_sum>
  <etotal_int>     -23.09327802 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28377724 </eigenvalue_sum>
  <etotal_int>     -23.09327748 </etotal_int>
  <timing name="iteration" min="    0.230" max="    0.230"/>
</iteration>
<iteration count="41">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737058 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737064 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737056 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000367 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000478 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000948 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000005 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000006 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000012 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133265 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133267 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000334 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000435 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000864 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974381 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974382 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000189 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000247 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000490 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392418 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392422 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392417 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000288 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000374 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000742 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274197 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274197 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274197 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062281 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062276 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062282 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000193 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000251 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000500 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000003 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000026 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000035 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000068 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050356 </ekin>
  <econf>        0.01800787 </econf>
  <eps>         -2.63198151 </eps>
  <enl>          2.02074537 </enl>
  <ecoul>       -7.85204332 </ecoul>
  <exc>         -2.39158449 </exc>
  <esr>          0.04706377 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635254 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635254 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10058764   5.10046439   0.00266727"
    b="  0.00746087   5.09564561   5.09584050"
    c="  5.10387815  -0.00065086   5.10386991" />
  <atom name="Si1" species="silicon">
    <position> 1.27890773 1.26964609 1.27343642 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00041665 0.00082944 0.00031929 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27890773 -1.26964609 -1.27343642 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00041665 -0.00082944 -0.00031929 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213234 </unit_cell_a_norm>
<unit_cell_b_norm> 7.206473 </unit_cell_b_norm>
<unit_cell_c_norm> 7.217968 </unit_cell_c_norm>
<unit_cell_alpha>  59.955 </unit_cell_alpha>
<unit_cell_beta>   59.986 </unit_cell_beta>
<unit_cell_gamma>  59.935 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90635254 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00008455 </sigma_eks_xx>
   <sigma_eks_yy>   0.00073728 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00025839 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00775387 </sigma_eks_xy>
   <sigma_eks_yz>   0.01016846 </sigma_eks_yz>
   <sigma_eks_xz>  -0.02012341 </sigma_eks_xz>

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

   <sigma_xx>  -0.00008455 </sigma_xx>
   <sigma_yy>   0.00073728 </sigma_yy>
   <sigma_zz>  -0.00025839 </sigma_zz>
   <sigma_xy>  -0.00775387 </sigma_xy>
   <sigma_yz>   0.01016846 </sigma_yz>
   <sigma_xz>  -0.02012341 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379226 </eigenvalue_sum>
  <etotal_int>     -23.09330545 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379045 </eigenvalue_sum>
  <etotal_int>     -23.09330214 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378909 </eigenvalue_sum>
  <etotal_int>     -23.09329967 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378808 </eigenvalue_sum>
  <etotal_int>     -23.09329782 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378730 </eigenvalue_sum>
  <etotal_int>     -23.09329640 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378670 </eigenvalue_sum>
  <etotal_int>     -23.09329530 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378622 </eigenvalue_sum>
  <etotal_int>     -23.09329442 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378583 </eigenvalue_sum>
  <etotal_int>     -23.09329371 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378551 </eigenvalue_sum>
  <etotal_int>     -23.09329312 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28378524 </eigenvalue_sum>
  <etotal_int>     -23.09329263 </etotal_int>
  <timing name="iteration" min="    0.236" max="    0.236"/>
</iteration>
<iteration count="42">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737057 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737063 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737056 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000352 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000458 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000908 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000004 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000006 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000011 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133264 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133266 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000320 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000417 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000828 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974381 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974381 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000182 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000237 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000470 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392417 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392421 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392417 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000276 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000359 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000711 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274197 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274197 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274197 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062281 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062276 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062282 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000185 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000241 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000479 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000025 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000033 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000066 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050336 </ekin>
  <econf>        0.01800787 </econf>
  <eps>         -2.63198171 </eps>
  <enl>          2.02074547 </enl>
  <ecoul>       -7.85204352 </ecoul>
  <exc>         -2.39158450 </exc>
  <esr>          0.04706375 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635302 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635302 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10049979   5.10038575   0.00255571"
    b="  0.00715152   5.09576576   5.09594824"
    c="  5.10365305  -0.00062398   5.10364487" />
  <atom name="Si1" species="silicon">
    <position> 1.27873007 1.26985370 1.27348427 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00039953 0.00079499 0.00030635 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27873006 -1.26985370 -1.27348427 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00039953 -0.00079499 -0.00030635 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213116 </unit_cell_a_norm>
<unit_cell_b_norm> 7.206634 </unit_cell_b_norm>
<unit_cell_c_norm> 7.217650 </unit_cell_c_norm>
<unit_cell_alpha>  59.957 </unit_cell_alpha>
<unit_cell_beta>   59.987 </unit_cell_beta>
<unit_cell_gamma>  59.938 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90635302 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00007661 </sigma_eks_xx>
   <sigma_eks_yy>   0.00068944 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00024396 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00743076 </sigma_eks_xy>
   <sigma_eks_yz>   0.00975447 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01929364 </sigma_eks_xz>

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

   <sigma_xx>  -0.00007661 </sigma_xx>
   <sigma_yy>   0.00068944 </sigma_yy>
   <sigma_zz>  -0.00024396 </sigma_zz>
   <sigma_xy>  -0.00743076 </sigma_xy>
   <sigma_yz>   0.00975447 </sigma_yz>
   <sigma_xz>  -0.01929364 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379905 </eigenvalue_sum>
  <etotal_int>     -23.09331834 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379738 </eigenvalue_sum>
  <etotal_int>     -23.09331530 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379613 </eigenvalue_sum>
  <etotal_int>     -23.09331303 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379520 </eigenvalue_sum>
  <etotal_int>     -23.09331133 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379449 </eigenvalue_sum>
  <etotal_int>     -23.09331002 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379393 </eigenvalue_sum>
  <etotal_int>     -23.09330901 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379349 </eigenvalue_sum>
  <etotal_int>     -23.09330820 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379313 </eigenvalue_sum>
  <etotal_int>     -23.09330755 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379284 </eigenvalue_sum>
  <etotal_int>     -23.09330701 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379259 </eigenvalue_sum>
  <etotal_int>     -23.09330656 </etotal_int>
  <timing name="iteration" min="    0.236" max="    0.236"/>
</iteration>
<iteration count="43">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737057 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737063 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737056 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000338 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000439 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000871 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000004 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000005 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000011 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133263 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133265 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000307 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000400 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000793 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974380 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974381 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000174 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000227 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000450 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392417 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392421 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392417 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000265 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000344 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000681 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274197 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274197 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274197 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062281 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062277 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062282 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000178 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000231 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000459 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000024 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000032 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000063 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050318 </ekin>
  <econf>        0.01800787 </econf>
  <eps>         -2.63198189 </eps>
  <enl>          2.02074557 </enl>
  <ecoul>       -7.85204370 </ecoul>
  <exc>         -2.39158450 </exc>
  <esr>          0.04706373 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635347 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635347 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10041566   5.10031019   0.00244880"
    b="  0.00685498   5.09588082   5.09605163"
    c="  5.10343729  -0.00059812   5.10342916" />
  <atom name="Si1" species="silicon">
    <position> 1.27855973 1.27005266 1.27353024 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00038311 0.00076197 0.00029390 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27855973 -1.27005266 -1.27353024 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00038311 -0.00076197 -0.00029390 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.213003 </unit_cell_a_norm>
<unit_cell_b_norm> 7.206788 </unit_cell_b_norm>
<unit_cell_c_norm> 7.217345 </unit_cell_c_norm>
<unit_cell_alpha>  59.959 </unit_cell_alpha>
<unit_cell_beta>   59.988 </unit_cell_beta>
<unit_cell_gamma>  59.941 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90635347 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00006909 </sigma_eks_xx>
   <sigma_eks_yy>   0.00064408 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00022977 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00712270 </sigma_eks_xy>
   <sigma_eks_yz>   0.00935656 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01849688 </sigma_eks_xz>

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

   <sigma_xx>  -0.00006909 </sigma_xx>
   <sigma_yy>   0.00064408 </sigma_yy>
   <sigma_zz>  -0.00022977 </sigma_zz>
   <sigma_xy>  -0.00712270 </sigma_xy>
   <sigma_yz>   0.00935656 </sigma_yz>
   <sigma_xz>  -0.01849688 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380528 </eigenvalue_sum>
  <etotal_int>     -23.09333019 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380375 </eigenvalue_sum>
  <etotal_int>     -23.09332739 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380260 </eigenvalue_sum>
  <etotal_int>     -23.09332531 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380175 </eigenvalue_sum>
  <etotal_int>     -23.09332374 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380109 </eigenvalue_sum>
  <etotal_int>     -23.09332255 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380058 </eigenvalue_sum>
  <etotal_int>     -23.09332161 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380018 </eigenvalue_sum>
  <etotal_int>     -23.09332087 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379985 </eigenvalue_sum>
  <etotal_int>     -23.09332027 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379958 </eigenvalue_sum>
  <etotal_int>     -23.09331977 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28379935 </eigenvalue_sum>
  <etotal_int>     -23.09331936 </etotal_int>
  <timing name="iteration" min="    0.243" max="    0.243"/>
</iteration>
<iteration count="44">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737057 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737062 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737056 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000324 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000421 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000834 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000004 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000005 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000010 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133262 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133264 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000295 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000383 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000760 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974379 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974380 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000167 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000217 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000432 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392417 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392420 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000254 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000330 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000653 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274197 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274197 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274197 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062281 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062277 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062281 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000170 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000222 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000440 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000023 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000031 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000060 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050302 </ekin>
  <econf>        0.01800787 </econf>
  <eps>         -2.63198205 </eps>
  <enl>          2.02074566 </enl>
  <ecoul>       -7.85204387 </ecoul>
  <exc>         -2.39158450 </exc>
  <esr>          0.04706371 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635388 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635388 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10033506   5.10023758   0.00234637"
    b="  0.00657069   5.09599099   5.09615086"
    c="  5.10323049  -0.00057326   5.10322241" />
  <atom name="Si1" species="silicon">
    <position> 1.27839642 1.27024333 1.27357439 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00036736 0.00073032 0.00028195 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27839642 -1.27024333 -1.27357439 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00036736 -0.00073032 -0.00028195 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.212894 </unit_cell_a_norm>
<unit_cell_b_norm> 7.206936 </unit_cell_b_norm>
<unit_cell_c_norm> 7.217052 </unit_cell_c_norm>
<unit_cell_alpha>  59.961 </unit_cell_alpha>
<unit_cell_beta>   59.988 </unit_cell_beta>
<unit_cell_gamma>  59.943 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90635388 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00006200 </sigma_eks_xx>
   <sigma_eks_yy>   0.00060119 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00021594 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00682853 </sigma_eks_xy>
   <sigma_eks_yz>   0.00897425 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01773210 </sigma_eks_xz>

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

   <sigma_xx>  -0.00006200 </sigma_xx>
   <sigma_yy>   0.00060119 </sigma_yy>
   <sigma_zz>  -0.00021594 </sigma_zz>
   <sigma_xy>  -0.00682853 </sigma_xy>
   <sigma_yz>   0.00897425 </sigma_yz>
   <sigma_xz>  -0.01773210 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381102 </eigenvalue_sum>
  <etotal_int>     -23.09334108 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380960 </eigenvalue_sum>
  <etotal_int>     -23.09333851 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380855 </eigenvalue_sum>
  <etotal_int>     -23.09333660 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380776 </eigenvalue_sum>
  <etotal_int>     -23.09333516 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380716 </eigenvalue_sum>
  <etotal_int>     -23.09333405 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380669 </eigenvalue_sum>
  <etotal_int>     -23.09333320 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380632 </eigenvalue_sum>
  <etotal_int>     -23.09333251 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380602 </eigenvalue_sum>
  <etotal_int>     -23.09333196 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380577 </eigenvalue_sum>
  <etotal_int>     -23.09333151 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28380556 </eigenvalue_sum>
  <etotal_int>     -23.09333112 </etotal_int>
  <timing name="iteration" min="    0.223" max="    0.223"/>
</iteration>
<iteration count="45">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737056 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737061 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737055 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000311 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000404 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000800 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000004 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000005 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000010 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133262 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133263 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000283 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000367 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000729 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974379 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974379 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000160 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000209 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000414 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392417 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392420 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000243 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000316 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000626 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274197 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274197 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274197 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062281 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062277 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062281 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000163 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000213 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000422 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000022 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000029 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000058 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050286 </ekin>
  <econf>        0.01800787 </econf>
  <eps>         -2.63198220 </eps>
  <enl>          2.02074574 </enl>
  <ecoul>       -7.85204403 </ecoul>
  <exc>         -2.39158451 </exc>
  <esr>          0.04706369 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635426 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635426 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10025785   5.10016778   0.00224822"
    b="  0.00629817   5.09609647   5.09624607"
    c="  5.10303230  -0.00054938   5.10302426" />
  <atom name="Si1" species="silicon">
    <position> 1.27823985 1.27042604 1.27361679 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00035225 0.00069998 0.00027046 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27823985 -1.27042604 -1.27361679 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00035225 -0.00069998 -0.00027046 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.212790 </unit_cell_a_norm>
<unit_cell_b_norm> 7.207077 </unit_cell_b_norm>
<unit_cell_c_norm> 7.216772 </unit_cell_c_norm>
<unit_cell_alpha>  59.962 </unit_cell_alpha>
<unit_cell_beta>   59.989 </unit_cell_beta>
<unit_cell_gamma>  59.945 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90635426 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00005535 </sigma_eks_xx>
   <sigma_eks_yy>   0.00056073 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00020255 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00654729 </sigma_eks_xy>
   <sigma_eks_yz>   0.00860705 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01699822 </sigma_eks_xz>

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

   <sigma_xx>  -0.00005535 </sigma_xx>
   <sigma_yy>   0.00056073 </sigma_yy>
   <sigma_zz>  -0.00020255 </sigma_zz>
   <sigma_xy>  -0.00654729 </sigma_xy>
   <sigma_yz>   0.00860705 </sigma_yz>
   <sigma_xz>  -0.01699822 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381629 </eigenvalue_sum>
  <etotal_int>     -23.09335109 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381499 </eigenvalue_sum>
  <etotal_int>     -23.09334873 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381402 </eigenvalue_sum>
  <etotal_int>     -23.09334697 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381330 </eigenvalue_sum>
  <etotal_int>     -23.09334565 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381274 </eigenvalue_sum>
  <etotal_int>     -23.09334463 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381231 </eigenvalue_sum>
  <etotal_int>     -23.09334385 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381197 </eigenvalue_sum>
  <etotal_int>     -23.09334322 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381169 </eigenvalue_sum>
  <etotal_int>     -23.09334271 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381146 </eigenvalue_sum>
  <etotal_int>     -23.09334229 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381127 </eigenvalue_sum>
  <etotal_int>     -23.09334194 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.221"/>
</iteration>
<iteration count="46">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737056 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737061 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737055 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000298 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000387 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000766 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000004 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000005 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000009 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133261 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133262 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000271 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000352 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000699 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974378 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974379 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000154 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000200 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000397 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392417 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392419 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000233 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000303 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000600 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274197 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274197 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274197 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062280 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062277 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062281 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000157 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000204 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000404 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000021 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000028 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000055 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050272 </ekin>
  <econf>        0.01800787 </econf>
  <eps>         -2.63198234 </eps>
  <enl>          2.02074581 </enl>
  <ecoul>       -7.85204417 </ecoul>
  <exc>         -2.39158451 </exc>
  <esr>          0.04706367 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635461 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635461 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10018385   5.10010069   0.00215419"
    b="  0.00603691   5.09619746   5.09633744"
    c="  5.10284236  -0.00052646   5.10283437" />
  <atom name="Si1" species="silicon">
    <position> 1.27808975 1.27060113 1.27365751 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00033775 0.00067090 0.00025944 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27808974 -1.27060113 -1.27365751 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00033775 -0.00067090 -0.00025944 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.212691 </unit_cell_a_norm>
<unit_cell_b_norm> 7.207213 </unit_cell_b_norm>
<unit_cell_c_norm> 7.216503 </unit_cell_c_norm>
<unit_cell_alpha>  59.964 </unit_cell_alpha>
<unit_cell_beta>   59.989 </unit_cell_beta>
<unit_cell_gamma>  59.948 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90635461 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00004915 </sigma_eks_xx>
   <sigma_eks_yy>   0.00052265 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00018967 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00627818 </sigma_eks_xy>
   <sigma_eks_yz>   0.00825444 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01629416 </sigma_eks_xz>

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

   <sigma_xx>  -0.00004915 </sigma_xx>
   <sigma_yy>   0.00052265 </sigma_yy>
   <sigma_zz>  -0.00018967 </sigma_zz>
   <sigma_xy>  -0.00627818 </sigma_xy>
   <sigma_yz>   0.00825444 </sigma_yz>
   <sigma_xz>  -0.01629416 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382113 </eigenvalue_sum>
  <etotal_int>     -23.09336030 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381994 </eigenvalue_sum>
  <etotal_int>     -23.09335813 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381905 </eigenvalue_sum>
  <etotal_int>     -23.09335651 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381838 </eigenvalue_sum>
  <etotal_int>     -23.09335529 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381787 </eigenvalue_sum>
  <etotal_int>     -23.09335436 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381748 </eigenvalue_sum>
  <etotal_int>     -23.09335363 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381716 </eigenvalue_sum>
  <etotal_int>     -23.09335306 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381691 </eigenvalue_sum>
  <etotal_int>     -23.09335259 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381670 </eigenvalue_sum>
  <etotal_int>     -23.09335221 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28381652 </eigenvalue_sum>
  <etotal_int>     -23.09335188 </etotal_int>
  <timing name="iteration" min="    0.230" max="    0.230"/>
</iteration>
<iteration count="47">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737056 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737060 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737055 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000286 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000371 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000735 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000004 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000005 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000009 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133260 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133262 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000260 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000338 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000670 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974378 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974374 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974378 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000147 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000192 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000380 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392417 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392419 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000224 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000290 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000575 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274196 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274196 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274196 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062280 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062277 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062281 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000150 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000195 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000387 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000020 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000027 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000053 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050259 </ekin>
  <econf>        0.01800787 </econf>
  <eps>         -2.63198247 </eps>
  <enl>          2.02074588 </enl>
  <ecoul>       -7.85204430 </ecoul>
  <exc>         -2.39158451 </exc>
  <esr>          0.04706365 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635493 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635493 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10011295   5.10003618   0.00206410"
    b="  0.00578646   5.09629415   5.09642512"
    c="  5.10266033  -0.00050448   5.10265239" />
  <atom name="Si1" species="silicon">
    <position> 1.27794584 1.27076891 1.27369661 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00032385 0.00064303 0.00024885 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27794584 -1.27076891 -1.27369661 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00032385 -0.00064303 -0.00024885 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.212595 </unit_cell_a_norm>
<unit_cell_b_norm> 7.207343 </unit_cell_b_norm>
<unit_cell_c_norm> 7.216246 </unit_cell_c_norm>
<unit_cell_alpha>  59.965 </unit_cell_alpha>
<unit_cell_beta>   59.990 </unit_cell_beta>
<unit_cell_gamma>  59.950 </unit_cell_gamma>
<unit_cell_volume> 265.063 </unit_cell_volume>
  <econst> -7.90635493 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00004337 </sigma_eks_xx>
   <sigma_eks_yy>   0.00048687 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00017733 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00602048 </sigma_eks_xy>
   <sigma_eks_yz>   0.00791593 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01561882 </sigma_eks_xz>

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

   <sigma_xx>  -0.00004337 </sigma_xx>
   <sigma_yy>   0.00048687 </sigma_yy>
   <sigma_zz>  -0.00017733 </sigma_zz>
   <sigma_xy>  -0.00602048 </sigma_xy>
   <sigma_yz>   0.00791593 </sigma_yz>
   <sigma_xz>  -0.01561882 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382558 </eigenvalue_sum>
  <etotal_int>     -23.09336876 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382449 </eigenvalue_sum>
  <etotal_int>     -23.09336676 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382367 </eigenvalue_sum>
  <etotal_int>     -23.09336527 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382306 </eigenvalue_sum>
  <etotal_int>     -23.09336415 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382259 </eigenvalue_sum>
  <etotal_int>     -23.09336330 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382222 </eigenvalue_sum>
  <etotal_int>     -23.09336263 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382193 </eigenvalue_sum>
  <etotal_int>     -23.09336210 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382170 </eigenvalue_sum>
  <etotal_int>     -23.09336167 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382151 </eigenvalue_sum>
  <etotal_int>     -23.09336132 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382134 </eigenvalue_sum>
  <etotal_int>     -23.09336102 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.221"/>
</iteration>
<iteration count="48">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737056 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737059 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737055 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000274 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000356 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000704 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000003 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000004 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000009 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133260 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133261 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000249 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000324 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000642 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974377 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974373 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974378 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000141 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000184 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000364 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392416 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392419 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000215 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000278 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000551 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274196 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274196 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274196 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062280 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062277 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062281 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000144 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000187 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000371 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000002 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000020 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000026 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000051 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050247 </ekin>
  <econf>        0.01800788 </econf>
  <eps>         -2.63198258 </eps>
  <enl>          2.02074594 </enl>
  <ecoul>       -7.85204442 </ecoul>
  <exc>         -2.39158451 </exc>
  <esr>          0.04706363 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635523 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635523 </enthalpy>
<atomset>
<unit_cell 
    a="  5.10004500   5.09997416   0.00197778"
    b="  0.00554636   5.09638670   5.09650925"
    c="  5.10248588  -0.00048339   5.10247801" />
  <atom name="Si1" species="silicon">
    <position> 1.27780788 1.27092968 1.27373416 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00031051 0.00061631 0.00023868 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27780787 -1.27092968 -1.27373416 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00031051 -0.00061631 -0.00023868 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.212503 </unit_cell_a_norm>
<unit_cell_b_norm> 7.207468 </unit_cell_b_norm>
<unit_cell_c_norm> 7.215999 </unit_cell_c_norm>
<unit_cell_alpha>  59.967 </unit_cell_alpha>
<unit_cell_beta>   59.990 </unit_cell_beta>
<unit_cell_gamma>  59.952 </unit_cell_gamma>
<unit_cell_volume> 265.064 </unit_cell_volume>
  <econst> -7.90635523 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00003802 </sigma_eks_xx>
   <sigma_eks_yy>   0.00045331 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00016556 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00577357 </sigma_eks_xy>
   <sigma_eks_yz>   0.00759099 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01497113 </sigma_eks_xz>

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

   <sigma_xx>  -0.00003802 </sigma_xx>
   <sigma_yy>   0.00045331 </sigma_yy>
   <sigma_zz>  -0.00016556 </sigma_zz>
   <sigma_xy>  -0.00577357 </sigma_xy>
   <sigma_yz>   0.00759099 </sigma_yz>
   <sigma_xz>  -0.01497113 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382968 </eigenvalue_sum>
  <etotal_int>     -23.09337653 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382867 </eigenvalue_sum>
  <etotal_int>     -23.09337470 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382792 </eigenvalue_sum>
  <etotal_int>     -23.09337333 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382735 </eigenvalue_sum>
  <etotal_int>     -23.09337230 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382692 </eigenvalue_sum>
  <etotal_int>     -23.09337152 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382659 </eigenvalue_sum>
  <etotal_int>     -23.09337090 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382632 </eigenvalue_sum>
  <etotal_int>     -23.09337042 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382611 </eigenvalue_sum>
  <etotal_int>     -23.09337002 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382593 </eigenvalue_sum>
  <etotal_int>     -23.09336970 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382578 </eigenvalue_sum>
  <etotal_int>     -23.09336942 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.222"/>
</iteration>
<iteration count="49">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737055 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737059 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737055 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000263 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000341 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000675 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000003 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000004 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000008 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133259 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133260 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000239 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000310 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000615 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974377 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974373 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974377 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000136 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000176 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000349 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392416 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392418 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000206 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000267 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000528 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274196 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274196 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274196 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062280 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062278 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062281 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000138 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000180 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000356 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000001 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000001 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000019 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000025 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000049 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050236 </ekin>
  <econf>        0.01800788 </econf>
  <eps>         -2.63198268 </eps>
  <enl>          2.02074600 </enl>
  <ecoul>       -7.85204454 </ecoul>
  <exc>         -2.39158451 </exc>
  <esr>          0.04706362 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635550 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635550 </enthalpy>
<atomset>
<unit_cell 
    a="  5.09997987   5.09991454   0.00189508"
    b="  0.00531619   5.09647531   5.09658998"
    c="  5.10231872  -0.00046318   5.10231091" />
  <atom name="Si1" species="silicon">
    <position> 1.27767561 1.27108373 1.27377022 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00029771 0.00059070 0.00022892 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27767561 -1.27108373 -1.27377022 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00029771 -0.00059070 -0.00022892 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.212415 </unit_cell_a_norm>
<unit_cell_b_norm> 7.207588 </unit_cell_b_norm>
<unit_cell_c_norm> 7.215763 </unit_cell_c_norm>
<unit_cell_alpha>  59.968 </unit_cell_alpha>
<unit_cell_beta>   59.990 </unit_cell_beta>
<unit_cell_gamma>  59.954 </unit_cell_gamma>
<unit_cell_volume> 265.064 </unit_cell_volume>
  <econst> -7.90635550 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00003308 </sigma_eks_xx>
   <sigma_eks_yy>   0.00042188 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00015439 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00553691 </sigma_eks_xy>
   <sigma_eks_yz>   0.00727914 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01435003 </sigma_eks_xz>

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

   <sigma_xx>  -0.00003308 </sigma_xx>
   <sigma_yy>   0.00042188 </sigma_yy>
   <sigma_zz>  -0.00015439 </sigma_zz>
   <sigma_xy>  -0.00553691 </sigma_xy>
   <sigma_yz>   0.00727914 </sigma_yz>
   <sigma_xz>  -0.01435003 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383344 </eigenvalue_sum>
  <etotal_int>     -23.09338368 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383251 </eigenvalue_sum>
  <etotal_int>     -23.09338200 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383182 </eigenvalue_sum>
  <etotal_int>     -23.09338074 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383130 </eigenvalue_sum>
  <etotal_int>     -23.09337979 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383091 </eigenvalue_sum>
  <etotal_int>     -23.09337907 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383060 </eigenvalue_sum>
  <etotal_int>     -23.09337851 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383036 </eigenvalue_sum>
  <etotal_int>     -23.09337806 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383016 </eigenvalue_sum>
  <etotal_int>     -23.09337770 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382999 </eigenvalue_sum>
  <etotal_int>     -23.09337740 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28382986 </eigenvalue_sum>
  <etotal_int>     -23.09337715 </etotal_int>
  <timing name="iteration" min="    0.221" max="    0.221"/>
</iteration>
<iteration count="50">
  total_electronic_charge: 8.00000000
 <stress_tensor unit="atomic_units">
   <sigma_ekin_xx>   0.00737055 </sigma_ekin_xx>
   <sigma_ekin_yy>   0.00737058 </sigma_ekin_yy>
   <sigma_ekin_zz>   0.00737054 </sigma_ekin_zz>
   <sigma_ekin_xy>  -0.00000252 </sigma_ekin_xy>
   <sigma_ekin_yz>   0.00000327 </sigma_ekin_yz>
   <sigma_ekin_xz>  -0.00000647 </sigma_ekin_xz>

   <sigma_econf_xx>   0.00026159 </sigma_econf_xx>
   <sigma_econf_yy>   0.00026159 </sigma_econf_yy>
   <sigma_econf_zz>   0.00026159 </sigma_econf_zz>
   <sigma_econf_xy>   0.00000003 </sigma_econf_xy>
   <sigma_econf_yz>  -0.00000004 </sigma_econf_yz>
   <sigma_econf_xz>   0.00000008 </sigma_econf_xz>

   <sigma_eps_xx>  -0.01133259 </sigma_eps_xx>
   <sigma_eps_yy>  -0.01133253 </sigma_eps_yy>
   <sigma_eps_zz>  -0.01133260 </sigma_eps_zz>
   <sigma_eps_xy>  -0.00000229 </sigma_eps_xy>
   <sigma_eps_yz>   0.00000298 </sigma_eps_yz>
   <sigma_eps_xz>  -0.00000589 </sigma_eps_xz>

   <sigma_enl_xx>   0.00974377 </sigma_enl_xx>
   <sigma_enl_yy>   0.00974373 </sigma_enl_yy>
   <sigma_enl_zz>   0.00974377 </sigma_enl_zz>
   <sigma_enl_xy>   0.00000130 </sigma_enl_xy>
   <sigma_enl_yz>  -0.00000169 </sigma_enl_yz>
   <sigma_enl_xz>   0.00000335 </sigma_enl_xz>

   <sigma_ehart_xx>  -0.00392416 </sigma_ehart_xx>
   <sigma_ehart_yy>  -0.00392418 </sigma_ehart_yy>
   <sigma_ehart_zz>  -0.00392416 </sigma_ehart_zz>
   <sigma_ehart_xy>   0.00000197 </sigma_ehart_xy>
   <sigma_ehart_yz>  -0.00000256 </sigma_ehart_yz>
   <sigma_ehart_xz>   0.00000506 </sigma_ehart_xz>

   <sigma_exc_xx>  -0.00274196 </sigma_exc_xx>
   <sigma_exc_yy>  -0.00274196 </sigma_exc_yy>
   <sigma_exc_zz>  -0.00274196 </sigma_exc_zz>
   <sigma_exc_xy>   0.00000000 </sigma_exc_xy>
   <sigma_exc_yz>   0.00000000 </sigma_exc_yz>
   <sigma_exc_xz>   0.00000000 </sigma_exc_xz>

   <sigma_esr_xx>   0.00062280 </sigma_esr_xx>
   <sigma_esr_yy>   0.00062278 </sigma_esr_yy>
   <sigma_esr_zz>   0.00062281 </sigma_esr_zz>
   <sigma_esr_xy>   0.00000133 </sigma_esr_xy>
   <sigma_esr_yz>  -0.00000172 </sigma_esr_yz>
   <sigma_esr_xz>   0.00000341 </sigma_esr_xz>

   <sigma_eks_xx>  -0.00000000 </sigma_eks_xx>
   <sigma_eks_yy>   0.00000001 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00000000 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00000018 </sigma_eks_xy>
   <sigma_eks_yz>   0.00000024 </sigma_eks_yz>
   <sigma_eks_xz>  -0.00000047 </sigma_eks_xz>
 </stress_tensor>
  <ekin>         2.93050225 </ekin>
  <econf>        0.01800788 </econf>
  <eps>         -2.63198278 </eps>
  <enl>          2.02074605 </enl>
  <ecoul>       -7.85204464 </ecoul>
  <exc>         -2.39158451 </exc>
  <esr>          0.04706361 </esr>
  <eself>        8.51076865 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>      -7.90635574 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>    -7.90635574 </enthalpy>
<atomset>
<unit_cell 
    a="  5.09991746   5.09985721   0.00181584"
    b="  0.00509554   5.09656013   5.09666744"
    c="  5.10215853  -0.00044380   5.10215080" />
  <atom name="Si1" species="silicon">
    <position> 1.27754882 1.27123135 1.27380484 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00028544 0.00056615 0.00021955 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -1.27754881 -1.27123135 -1.27380484 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00028544 -0.00056615 -0.00021955 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 7.212330 </unit_cell_a_norm>
<unit_cell_b_norm> 7.207702 </unit_cell_b_norm>
<unit_cell_c_norm> 7.215536 </unit_cell_c_norm>
<unit_cell_alpha>  59.969 </unit_cell_alpha>
<unit_cell_beta>   59.991 </unit_cell_beta>
<unit_cell_gamma>  59.956 </unit_cell_gamma>
<unit_cell_volume> 265.064 </unit_cell_volume>
  <econst> -7.90635574 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
 <stress_tensor unit="GPa">
   <sigma_eks_xx>  -0.00002854 </sigma_eks_xx>
   <sigma_eks_yy>   0.00039247 </sigma_eks_yy>
   <sigma_eks_zz>  -0.00014381 </sigma_eks_zz>
   <sigma_eks_xy>  -0.00531001 </sigma_eks_xy>
   <sigma_eks_yz>   0.00697987 </sigma_eks_yz>
   <sigma_eks_xz>  -0.01375448 </sigma_eks_xz>

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

   <sigma_xx>  -0.00002854 </sigma_xx>
   <sigma_yy>   0.00039247 </sigma_yy>
   <sigma_zz>  -0.00014381 </sigma_zz>
   <sigma_xy>  -0.00531001 </sigma_xy>
   <sigma_yz>   0.00697987 </sigma_yz>
   <sigma_xz>  -0.01375448 </sigma_xz>
 </stress_tensor>
  CGCellStepper: alpha = 0.25000000
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383690 </eigenvalue_sum>
  <etotal_int>     -23.09339026 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383604 </eigenvalue_sum>
  <etotal_int>     -23.09338870 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383541 </eigenvalue_sum>
  <etotal_int>     -23.09338755 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383493 </eigenvalue_sum>
  <etotal_int>     -23.09338668 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383457 </eigenvalue_sum>
  <etotal_int>     -23.09338601 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383429 </eigenvalue_sum>
  <etotal_int>     -23.09338550 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383406 </eigenvalue_sum>
  <etotal_int>     -23.09338508 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383388 </eigenvalue_sum>
  <etotal_int>     -23.09338475 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383373 </eigenvalue_sum>
  <etotal_int>     -23.09338448 </etotal_int>
  total_electronic_charge: 8.00000000
  <eigenvalue_sum>  -8.28383360 </eigenvalue_sum>
  <etotal_int>     -23.09338425 </etotal_int>
  <timing name="iteration" min="    0.235" max="    0.235"/>
</iteration>
<timing name="         charge" min="    4.928" max="    4.984"/>
<timing name="         energy" min="    5.010" max="    5.153"/>
<timing name="           gram" min="    0.285" max="    0.290"/>
<timing name="   psd_residual" min="    0.187" max="    0.263"/>
<timing name="  psd_update_wf" min="    0.035" max="    0.038"/>
<timing name="    update_vhxc" min="    0.323" max="    0.326"/>
<timing name="      wf_update" min="    0.596" max="    0.669"/>
<timing name="           ekin" min="    0.073" max="    0.079"/>
<timing name="            exc" min="    0.213" max="    0.216"/>
<timing name="           hpsi" min="    4.298" max="    4.299"/>
<timing name="       nonlocal" min="    0.622" max="    0.623"/>
<timing name=" charge_compute" min="    4.762" max="    4.823"/>
<timing name="charge_integral" min="    0.015" max="    0.022"/>
<timing name="  charge_rowsum" min="    0.009" max="    0.010"/>
<timing name="     charge_vft" min="    0.069" max="    0.134"/>
[qbox]  End of command stream 
<real_time> 12.164 </real_time>
<end_time> 2016-04-06T12:25:20Z </end_time>
</fpmd:simulation>
