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
<start_time> 2016-04-06T12:25:21Z </start_time>
<mpi_processes count="4">
<process id="0"> theobook68 </process>
<process id="1"> theobook68 </process>
<process id="2"> theobook68 </process>
<process id="3"> theobook68 </process>
</mpi_processes>
[qbox] <cmd># Si4 geometry optimization</cmd>
[qbox] <cmd>load ../si4gs/test.xml</cmd>
 LoadCmd: loading from ../si4gs/test.xml
 XMLGFPreprocessor: reading from ../si4gs/test.xml size: 357985
 XMLGFPreprocessor: read time: 9.68e-05
 XMLGFPreprocessor: local read rate: 881.7 MB/s  aggregate read rate: 3527 MB/s
 XMLGFPreprocessor: tag fixing time: 6.819e-05
 XMLGFPreprocessor: segment definition time: 0.001933
 XMLGFPreprocessor: boundary adjustment time: 1.907e-06
 XMLGFPreprocessor: transcoding time: 5.96e-06
 XMLGFPreprocessor: data redistribution time: 0.000613
 XMLGFPreprocessor: XML compacting time: 0.000165
 XMLGFPreprocessor: total time: 0.003887
 xmlcontent.size(): 120537
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
 WavefunctionHandler::startElement: wavefunction nspin=1 nel=16 nempty=0
 WavefunctionHandler::startElement: slater_determinant
 kpoint=0 0 0 weight=1 size=8
 WavefunctionHandler::endElement: slater_determinant
 XML parsing done
 SampleReader: read time: 0.03414 s
[qbox] <cmd>set wf_dyn PSDA</cmd>
[qbox] <cmd>set ecutprec 2</cmd>
[qbox] <cmd>set atoms_dyn CG</cmd>
[qbox] <cmd>run 50 5</cmd>
  EnergyFunctional: np0v,np1v,np2v: 30 30 30
  EnergyFunctional: vft->np012(): 27000
<wavefunction ecut="3" nspin="1" nel="16" nempty="0">
<cell a="16.000000 0.000000 0.000000"
      b="0.000000 16.000000 0.000000"
      c="0.000000 0.000000 16.000000"/>
 reciprocal lattice vectors
 0.392699 0.000000 0.000000
 0.000000 0.392699 0.000000
 0.000000 0.000000 0.392699
<refcell a="0.000000 0.000000 0.000000"
         b="0.000000 0.000000 0.000000"
         c="0.000000 0.000000 0.000000"/>
<grid nx="14" ny="14" nz="14"/>
 kpoint: 0.000000 0.000000 0.000000 weight: 1.000000
<slater_determinant kpoint="0.000000 0.000000 0.000000" size="8">
 sdcontext: 4x1
 basis size: 511
 c dimensions: 536x8   (134x8 blocks)
 <density_matrix form="diagonal" size="8">
 </density_matrix>
</slater_determinant>
</wavefunction>
<iteration count="1">
  total_electronic_charge: 16.00000000
  <ekin>         5.34839630 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48138467 </eps>
  <enl>          4.77521374 </enl>
  <ecoul>      -15.60248420 </ecoul>
  <exc>         -4.41268632 </exc>
  <esr>          0.07326880 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294516 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294516 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000000 0.00000000 0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00284355 0.00000008 -0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20000000 0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000007 0.01705782 0.00000183 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000000 0.00000000 0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00284366 -0.00000006 -0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20000000 0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000009 -0.01705783 0.00000110 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294516 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 1.00000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32616286 </eigenvalue_sum>
  <etotal_int>     -15.37304547 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33906383 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93095585 (0.93095585)
  <etotal_int>     -15.37334465 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35086272 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06341176 (0.06341176)
  <etotal_int>     -15.37345925 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35137080 </eigenvalue_sum>
  Anderson extrapolation: theta=1.57021327 (1.57021327)
  <etotal_int>     -15.37346590 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35193587 </eigenvalue_sum>
  Anderson extrapolation: theta=0.20169051 (0.20169051)
  <etotal_int>     -15.37347218 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="2">
  total_electronic_charge: 16.00000000
  <ekin>         5.33348530 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47058867 </eps>
  <enl>          4.77254405 </enl>
  <ecoul>      -15.60213347 </ecoul>
  <exc>         -4.40678055 </exc>
  <esr>          0.07073843 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37347332 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37347332 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70284355 0.00000008 -0.00000141 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00158000 0.00000005 -0.00000109 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000007 2.21705782 0.00000183 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000005 0.01323308 0.00000136 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70284366 -0.00000006 -0.00000133 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00158004 -0.00000004 -0.00000103 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000009 -2.21705783 0.00000110 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000004 -0.01323309 0.00000089 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37347332 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.10000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31854852 </eigenvalue_sum>
  <etotal_int>     -15.37338506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33259603 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93018377 (0.93018377)
  <etotal_int>     -15.37374178 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34544112 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06701596 (0.06701596)
  <etotal_int>     -15.37388101 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34603525 </eigenvalue_sum>
  Anderson extrapolation: theta=1.70003630 (1.70003630)
  <etotal_int>     -15.37389059 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34675330 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23233649 (0.23233649)
  <etotal_int>     -15.37390100 </etotal_int>
  <timing name="iteration" min="    0.036" max="    0.036"/>
</iteration>
<iteration count="3">
  total_electronic_charge: 16.00000000
  <ekin>         5.31726498 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45968222 </eps>
  <enl>          4.77064770 </enl>
  <ecoul>      -15.60179675 </ecoul>
  <exc>         -4.40033689 </exc>
  <esr>          0.06807333 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37390318 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37390318 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70597146 0.00000016 -0.00000297 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00018337 0.00000003 -0.00000082 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000014 2.23582142 0.00000385 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000003 0.00935608 0.00000099 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70597168 -0.00000012 -0.00000278 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00018336 -0.00000003 -0.00000078 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000019 -2.23582145 0.00000231 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00935608 0.00000070 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37390318 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 4.41000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.27688197 </eigenvalue_sum>
  <etotal_int>     -15.37206839 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.30657892 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92930951 (0.92930951)
  <etotal_int>     -15.37363028 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33337235 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06561213 (0.06561213)
  <etotal_int>     -15.37423282 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33459594 </eigenvalue_sum>
  Anderson extrapolation: theta=1.64511182 (1.64511182)
  <etotal_int>     -15.37427159 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33602694 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22172666 (0.22172666)
  <etotal_int>     -15.37431173 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="4">
  total_electronic_charge: 16.00000000
  <ekin>         5.28435591 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43762928 </eps>
  <enl>          4.76661471 </enl>
  <ecoul>      -15.60063969 </ecoul>
  <exc>         -4.38702154 </exc>
  <esr>          0.06285069 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37431989 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37431989 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71254007 0.00000034 -0.00000624 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00256902 0.00000003 -0.00000051 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000030 2.27522498 0.00000808 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000002 0.00177280 0.00000057 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71254053 -0.00000025 -0.00000585 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00256908 -0.00000003 -0.00000049 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000041 -2.27522505 0.00000484 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000004 -0.00177280 0.00000046 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37431989 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 4.41000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34576221 </eigenvalue_sum>
  <etotal_int>     -15.37424411 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34164701 </eigenvalue_sum>
  Anderson extrapolation: theta=1.31511679 (1.31511679)
  <etotal_int>     -15.37432838 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33681534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09385946 (0.09385946)
  <etotal_int>     -15.37438018 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33682820 </eigenvalue_sum>
  Anderson extrapolation: theta=1.66229517 (1.66229517)
  <etotal_int>     -15.37438424 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33699394 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25352780 (0.25352780)
  <etotal_int>     -15.37438872 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="5">
  total_electronic_charge: 16.00000000
  <ekin>         5.28966634 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44315556 </eps>
  <enl>          4.76994524 </enl>
  <ecoul>      -15.60158660 </ecoul>
  <exc>         -4.38925919 </exc>
  <esr>          0.06367134 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37438978 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37438978 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70065754 0.00000044 -0.00000821 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00114149 0.00000001 -0.00000036 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000039 2.27972472 0.00001025 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 0.00150927 0.00000039 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70065769 -0.00000036 -0.00000776 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00114148 -0.00000002 -0.00000036 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000020 -2.27972477 0.00000665 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00150926 0.00000032 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37438978 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33425013 </eigenvalue_sum>
  <etotal_int>     -15.37439008 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33551350 </eigenvalue_sum>
  Anderson extrapolation: theta=1.12913104 (1.12913104)
  <etotal_int>     -15.37439708 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33679854 </eigenvalue_sum>
  Anderson extrapolation: theta=0.12598713 (0.12598713)
  <etotal_int>     -15.37440120 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33683594 </eigenvalue_sum>
  Anderson extrapolation: theta=2.06778619 (2.00000000)
  <etotal_int>     -15.37440181 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33686443 </eigenvalue_sum>
  Anderson extrapolation: theta=0.34438384 (0.34438384)
  <etotal_int>     -15.37440268 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="6">
  total_electronic_charge: 16.00000000
  <ekin>         5.28828515 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44294033 </eps>
  <enl>          4.77062314 </enl>
  <ecoul>      -15.60166109 </ecoul>
  <exc>         -4.38870980 </exc>
  <esr>          0.06348050 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37440292 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37440292 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69920546 0.00000046 -0.00000887 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00081570 0.00000001 -0.00000030 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000038 2.28296710 0.00001096 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00122672 0.00000032 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69920569 -0.00000038 -0.00000843 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00081571 -0.00000001 -0.00000030 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000023 -2.28296714 0.00000724 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 -0.00122671 0.00000028 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37440292 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33558381 </eigenvalue_sum>
  <etotal_int>     -15.37440359 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612906 </eigenvalue_sum>
  Anderson extrapolation: theta=1.26899101 (1.26899101)
  <etotal_int>     -15.37440765 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33668016 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10380241 (0.10380241)
  <etotal_int>     -15.37441010 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33664983 </eigenvalue_sum>
  Anderson extrapolation: theta=1.63599037 (1.63599037)
  <etotal_int>     -15.37441031 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33660058 </eigenvalue_sum>
  Anderson extrapolation: theta=0.26191247 (0.26191247)
  <etotal_int>     -15.37441055 </etotal_int>
  <timing name="iteration" min="    0.037" max="    0.038"/>
</iteration>
<iteration count="7">
  total_electronic_charge: 16.00000000
  <ekin>         5.28782625 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44285241 </eps>
  <enl>          4.77085491 </enl>
  <ecoul>      -15.60171897 </ecoul>
  <exc>         -4.38852040 </exc>
  <esr>          0.06340751 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441061 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441061 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69741452 0.00000048 -0.00000950 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00061106 0.00000001 -0.00000024 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000038 2.28547943 0.00001164 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00083639 0.00000025 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69741472 -0.00000041 -0.00000907 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00061106 -0.00000001 -0.00000025 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.28547946 0.00000784 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 -0.00083639 0.00000023 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441061 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33585510 </eigenvalue_sum>
  <etotal_int>     -15.37441133 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33618486 </eigenvalue_sum>
  Anderson extrapolation: theta=1.29118809 (1.29118809)
  <etotal_int>     -15.37441296 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33652315 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10432685 (0.10432685)
  <etotal_int>     -15.37441396 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33650433 </eigenvalue_sum>
  Anderson extrapolation: theta=1.63800554 (1.63800554)
  <etotal_int>     -15.37441405 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33647441 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25274722 (0.25274722)
  <etotal_int>     -15.37441415 </etotal_int>
  <timing name="iteration" min="    0.038" max="    0.038"/>
</iteration>
<iteration count="8">
  total_electronic_charge: 16.00000000
  <ekin>         5.28755334 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44282546 </eps>
  <enl>          4.77101578 </enl>
  <ecoul>      -15.60175135 </ecoul>
  <exc>         -4.38840647 </exc>
  <esr>          0.06336649 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441417 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441417 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69625947 0.00000049 -0.00000997 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00046502 0.00000001 -0.00000021 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000039 2.28704772 0.00001214 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00063024 0.00000022 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69625967 -0.00000043 -0.00000956 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00046502 -0.00000001 -0.00000022 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.28704775 0.00000830 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 -0.00063024 0.00000021 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441417 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33586718 </eigenvalue_sum>
  <etotal_int>     -15.37441444 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613493 </eigenvalue_sum>
  Anderson extrapolation: theta=1.29303947 (1.29303947)
  <etotal_int>     -15.37441555 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33640918 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10005088 (0.10005088)
  <etotal_int>     -15.37441622 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33639266 </eigenvalue_sum>
  Anderson extrapolation: theta=1.57618213 (1.57618213)
  <etotal_int>     -15.37441627 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33636728 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23440200 (0.23440200)
  <etotal_int>     -15.37441632 </etotal_int>
  <timing name="iteration" min="    0.037" max="    0.037"/>
</iteration>
<iteration count="9">
  total_electronic_charge: 16.00000000
  <ekin>         5.28733720 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44278571 </eps>
  <enl>          4.77111931 </enl>
  <ecoul>      -15.60177289 </ecoul>
  <exc>         -4.38831425 </exc>
  <esr>          0.06333333 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441634 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441634 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69530991 0.00000050 -0.00001042 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00035145 0.00000000 -0.00000019 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000039 2.28833415 0.00001259 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00045756 0.00000019 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69531011 -0.00000045 -0.00001001 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00035145 -0.00000001 -0.00000020 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.28833418 0.00000873 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 -0.00045755 0.00000019 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441634 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33599297 </eigenvalue_sum>
  <etotal_int>     -15.37441654 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33615951 </eigenvalue_sum>
  Anderson extrapolation: theta=1.32090839 (1.32090839)
  <etotal_int>     -15.37441708 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33633029 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09927446 (0.09927446)
  <etotal_int>     -15.37441742 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33631797 </eigenvalue_sum>
  Anderson extrapolation: theta=1.59646107 (1.59646107)
  <etotal_int>     -15.37441744 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33630004 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23439195 (0.23439195)
  <etotal_int>     -15.37441747 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="10">
  total_electronic_charge: 16.00000000
  <ekin>         5.28721090 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44277731 </eps>
  <enl>          4.77119789 </enl>
  <ecoul>      -15.60178918 </ecoul>
  <exc>         -4.38825977 </exc>
  <esr>          0.06331421 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441748 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441748 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69461537 0.00000051 -0.00001082 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00026774 0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000039 2.28922865 0.00001298 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00034072 0.00000018 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69461557 -0.00000046 -0.00001041 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00026774 -0.00000001 -0.00000018 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.28922867 0.00000912 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 -0.00034071 0.00000018 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441748 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33602548 </eigenvalue_sum>
  <etotal_int>     -15.37441758 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614840 </eigenvalue_sum>
  Anderson extrapolation: theta=1.32737965 (1.32737965)
  <etotal_int>     -15.37441790 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33627425 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09724113 (0.09724113)
  <etotal_int>     -15.37441810 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33626453 </eigenvalue_sum>
  Anderson extrapolation: theta=1.58527655 (1.58527655)
  <etotal_int>     -15.37441812 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33625067 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22930312 (0.22930312)
  <etotal_int>     -15.37441813 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="11">
  total_electronic_charge: 16.00000000
  <ekin>         5.28712075 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44277248 </eps>
  <enl>          4.77125505 </enl>
  <ecoul>      -15.60180110 </ecoul>
  <exc>         -4.38822035 </exc>
  <esr>          0.06330053 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441813 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441813 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69407586 0.00000052 -0.00001120 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00020241 0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000039 2.28991324 0.00001335 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00025140 0.00000017 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69407605 -0.00000047 -0.00001080 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00020241 -0.00000001 -0.00000018 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.28991325 0.00000949 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00025140 0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441813 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33606591 </eigenvalue_sum>
  <etotal_int>     -15.37441820 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614927 </eigenvalue_sum>
  Anderson extrapolation: theta=1.34162523 (1.34162523)
  <etotal_int>     -15.37441837 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33623444 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09618001 (0.09618001)
  <etotal_int>     -15.37441848 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33622716 </eigenvalue_sum>
  Anderson extrapolation: theta=1.59595087 (1.59595087)
  <etotal_int>     -15.37441849 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33621704 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22848776 (0.22848776)
  <etotal_int>     -15.37441849 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="12">
  total_electronic_charge: 16.00000000
  <ekin>         5.28706280 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44277468 </eps>
  <enl>          4.77129823 </enl>
  <ecoul>      -15.60181015 </ecoul>
  <exc>         -4.38819470 </exc>
  <esr>          0.06329179 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441850 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441850 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69367233 0.00000053 -0.00001157 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00015314 0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000040 2.29041166 0.00001370 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00018717 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69367253 -0.00000048 -0.00001117 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00015314 -0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.29041168 0.00000985 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00018717 0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441850 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33608414 </eigenvalue_sum>
  <etotal_int>     -15.37441853 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614443 </eigenvalue_sum>
  Anderson extrapolation: theta=1.34791122 (1.34791122)
  <etotal_int>     -15.37441863 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33620589 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09499931 (0.09499931)
  <etotal_int>     -15.37441869 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33620033 </eigenvalue_sum>
  Anderson extrapolation: theta=1.59540495 (1.59540495)
  <etotal_int>     -15.37441869 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33619271 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22631094 (0.22631094)
  <etotal_int>     -15.37441870 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="13">
  total_electronic_charge: 16.00000000
  <ekin>         5.28702238 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44277799 </eps>
  <enl>          4.77133047 </enl>
  <ecoul>      -15.60181695 </ecoul>
  <exc>         -4.38817661 </exc>
  <esr>          0.06328571 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441870 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441870 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69336528 0.00000053 -0.00001193 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00011548 0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000040 2.29078596 0.00001404 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00013912 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69336547 -0.00000049 -0.00001153 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00011548 -0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.29078597 0.00001020 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00013912 0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441870 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33609908 </eigenvalue_sum>
  <etotal_int>     -15.37441872 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614180 </eigenvalue_sum>
  Anderson extrapolation: theta=1.35546529 (1.35546529)
  <etotal_int>     -15.37441877 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33618523 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09420622 (0.09420622)
  <etotal_int>     -15.37441881 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33618107 </eigenvalue_sum>
  Anderson extrapolation: theta=1.60095615 (1.60095615)
  <etotal_int>     -15.37441881 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33617543 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22542289 (0.22542289)
  <etotal_int>     -15.37441881 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="14">
  total_electronic_charge: 16.00000000
  <ekin>         5.28699490 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44278219 </eps>
  <enl>          4.77135474 </enl>
  <ecoul>      -15.60182209 </ecoul>
  <exc>         -4.38816418 </exc>
  <esr>          0.06328158 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441881 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441881 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69313452 0.00000054 -0.00001229 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00008703 0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000040 2.29106313 0.00001437 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00010376 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69313471 -0.00000050 -0.00001189 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00008703 -0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.29106314 0.00001056 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00010376 0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441881 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33610770 </eigenvalue_sum>
  <etotal_int>     -15.37441882 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613873 </eigenvalue_sum>
  Anderson extrapolation: theta=1.35996291 (1.35996291)
  <etotal_int>     -15.37441885 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33617021 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09349170 (0.09349170)
  <etotal_int>     -15.37441887 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33616707 </eigenvalue_sum>
  Anderson extrapolation: theta=1.60260544 (1.60260544)
  <etotal_int>     -15.37441887 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33616285 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22428110 (0.22428110)
  <etotal_int>     -15.37441888 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="15">
  total_electronic_charge: 16.00000000
  <ekin>         5.28697556 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44278607 </eps>
  <enl>          4.77137294 </enl>
  <ecoul>      -15.60182597 </ecoul>
  <exc>         -4.38815535 </exc>
  <esr>          0.06327869 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441888 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441888 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69296033 0.00000055 -0.00001266 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00006548 0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000041 2.29127043 0.00001470 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00007740 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69296052 -0.00000051 -0.00001224 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00006548 -0.00000000 -0.00000017 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000021 -2.29127044 0.00001091 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00007740 0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441888 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33611395 </eigenvalue_sum>
  <etotal_int>     -15.37441888 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613645 </eigenvalue_sum>
  Anderson extrapolation: theta=1.36422451 (1.36422451)
  <etotal_int>     -15.37441890 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33615921 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09296562 (0.09296562)
  <etotal_int>     -15.37441891 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33615686 </eigenvalue_sum>
  Anderson extrapolation: theta=1.60570117 (1.60570117)
  <etotal_int>     -15.37441891 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33615372 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22360232 (0.22360232)
  <etotal_int>     -15.37441891 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.035"/>
</iteration>
<iteration count="16">
  total_electronic_charge: 16.00000000
  <ekin>         5.28696196 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44278952 </eps>
  <enl>          4.77138662 </enl>
  <ecoul>      -15.60182889 </ecoul>
  <exc>         -4.38814908 </exc>
  <esr>          0.06327665 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441891 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441891 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69282941 0.00000055 -0.00001302 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00004924 0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000041 2.29142493 0.00001504 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00005783 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69282960 -0.00000052 -0.00001261 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00004924 -0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000022 -2.29142494 0.00001126 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00005783 0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441891 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33611799 </eigenvalue_sum>
  <etotal_int>     -15.37441892 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613448 </eigenvalue_sum>
  Anderson extrapolation: theta=1.36716685 (1.36716685)
  <etotal_int>     -15.37441892 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33615113 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09252601 (0.09252601)
  <etotal_int>     -15.37441893 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614936 </eigenvalue_sum>
  Anderson extrapolation: theta=1.60735384 (1.60735384)
  <etotal_int>     -15.37441893 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614702 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22294035 (0.22294035)
  <etotal_int>     -15.37441893 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="17">
  total_electronic_charge: 16.00000000
  <ekin>         5.28695223 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44279238 </eps>
  <enl>          4.77139688 </enl>
  <ecoul>      -15.60183109 </ecoul>
  <exc>         -4.38814457 </exc>
  <esr>          0.06327520 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441893 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441893 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69273091 0.00000056 -0.00001340 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00003700 0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000041 2.29154047 0.00001538 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00004322 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69273110 -0.00000053 -0.00001298 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00003700 -0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000022 -2.29154047 0.00001162 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00004322 0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441893 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612086 </eigenvalue_sum>
  <etotal_int>     -15.37441893 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613296 </eigenvalue_sum>
  Anderson extrapolation: theta=1.36968551 (1.36968551)
  <etotal_int>     -15.37441894 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614517 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09218931 (0.09218931)
  <etotal_int>     -15.37441894 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614384 </eigenvalue_sum>
  Anderson extrapolation: theta=1.60919731 (1.60919731)
  <etotal_int>     -15.37441894 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614210 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22247972 (0.22247972)
  <etotal_int>     -15.37441894 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="18">
  total_electronic_charge: 16.00000000
  <ekin>         5.28694523 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44279471 </eps>
  <enl>          4.77140459 </enl>
  <ecoul>      -15.60183274 </ecoul>
  <exc>         -4.38814131 </exc>
  <esr>          0.06327416 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441894 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441894 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69265693 0.00000057 -0.00001378 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00002779 0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000042 2.29162681 0.00001573 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00003233 0.00000017 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69265712 -0.00000054 -0.00001335 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00002779 -0.00000000 -0.00000018 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000023 -2.29162681 0.00001199 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00003233 0.00000018 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441894 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612282 </eigenvalue_sum>
  <etotal_int>     -15.37441894 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613176 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37155532 (1.37155532)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33614075 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09191637 (0.09191637)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613976 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61044140 (1.61044140)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613846 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22208326 (0.22208326)
  <etotal_int>     -15.37441895 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="19">
  total_electronic_charge: 16.00000000
  <ekin>         5.28694015 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44279656 </eps>
  <enl>          4.77141037 </enl>
  <ecoul>      -15.60183399 </ecoul>
  <exc>         -4.38813893 </exc>
  <esr>          0.06327340 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441895 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441895 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69260136 0.00000057 -0.00001417 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00002086 0.00000000 -0.00000019 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000042 2.29169141 0.00001608 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00002419 0.00000017 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69260155 -0.00000054 -0.00001374 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00002086 -0.00000000 -0.00000019 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000023 -2.29169141 0.00001237 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00002419 0.00000018 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441895 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612422 </eigenvalue_sum>
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613083 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37308815 (1.37308815)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613748 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09170364 (0.09170364)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613674 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61160334 (1.61160334)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613576 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22179477 (0.22179477)
  <etotal_int>     -15.37441895 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="20">
  total_electronic_charge: 16.00000000
  <ekin>         5.28693645 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44279800 </eps>
  <enl>          4.77141471 </enl>
  <ecoul>      -15.60183492 </ecoul>
  <exc>         -4.38813719 </exc>
  <esr>          0.06327285 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441895 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441895 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69255965 0.00000058 -0.00001457 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00001565 0.00000000 -0.00000019 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000043 2.29173975 0.00001645 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00001811 0.00000018 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69255984 -0.00000055 -0.00001413 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00001565 -0.00000000 -0.00000019 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000024 -2.29173975 0.00001275 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00001811 0.00000019 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441895 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612521 </eigenvalue_sum>
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613012 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37426782 (1.37426782)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613505 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09153382 (0.09153382)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613449 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61249810 (1.61249810)
  <etotal_int>     -15.37441895 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613376 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22157257 (0.22157257)
  <etotal_int>     -15.37441895 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="21">
  total_electronic_charge: 16.00000000
  <ekin>         5.28693373 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44279912 </eps>
  <enl>          4.77141796 </enl>
  <ecoul>      -15.60183563 </ecoul>
  <exc>         -4.38813590 </exc>
  <esr>          0.06327244 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441895 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441895 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69252834 0.00000059 -0.00001498 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00001174 0.00000000 -0.00000020 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000043 2.29177594 0.00001682 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00001356 0.00000018 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69252854 -0.00000056 -0.00001454 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00001174 -0.00000000 -0.00000020 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000024 -2.29177594 0.00001315 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00001356 0.00000019 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441895 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612592 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612957 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37521886 (1.37521886)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613323 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09140128 (0.09140128)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613282 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61332144 (1.61332144)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613227 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22143317 (0.22143317)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="22">
  total_electronic_charge: 16.00000000
  <ekin>         5.28693173 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44279998 </eps>
  <enl>          4.77142040 </enl>
  <ecoul>      -15.60183615 </ecoul>
  <exc>         -4.38813495 </exc>
  <esr>          0.06327215 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69250486 0.00000060 -0.00001540 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000881 0.00000000 -0.00000020 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000044 2.29180304 0.00001720 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00001015 0.00000019 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69250505 -0.00000057 -0.00001495 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000881 -0.00000000 -0.00000020 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000024 -2.29180303 0.00001355 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00001015 0.00000020 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612644 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612916 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37596591 (1.37596591)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613188 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09129802 (0.09129802)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613157 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61408297 (1.61408297)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613116 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22138033 (0.22138033)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="23">
  total_electronic_charge: 16.00000000
  <ekin>         5.28693025 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280064 </eps>
  <enl>          4.77142223 </enl>
  <ecoul>      -15.60183655 </ecoul>
  <exc>         -4.38813425 </exc>
  <esr>          0.06327193 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69248724 0.00000060 -0.00001583 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000661 0.00000000 -0.00000021 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000044 2.29182334 0.00001760 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000761 0.00000019 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69248744 -0.00000058 -0.00001538 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000661 -0.00000000 -0.00000021 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000025 -2.29182333 0.00001396 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000761 0.00000020 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612681 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612884 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37656784 (1.37656784)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613087 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09122098 (0.09122098)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613064 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61493508 (1.61493508)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613033 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22145411 (0.22145411)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="24">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692916 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280114 </eps>
  <enl>          4.77142360 </enl>
  <ecoul>      -15.60183685 </ecoul>
  <exc>         -4.38813373 </exc>
  <esr>          0.06327177 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69247403 0.00000061 -0.00001627 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000495 0.00000000 -0.00000022 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000045 2.29183854 0.00001800 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000570 0.00000020 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69247422 -0.00000059 -0.00001581 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000495 -0.00000000 -0.00000021 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000025 -2.29183853 0.00001439 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000570 0.00000021 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612709 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612860 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37705187 (1.37705187)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33613012 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09116856 (0.09116856)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612994 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61604445 (1.61604445)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612971 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22172665 (0.22172665)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="25">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692834 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280152 </eps>
  <enl>          4.77142463 </enl>
  <ecoul>      -15.60183707 </ecoul>
  <exc>         -4.38813334 </exc>
  <esr>          0.06327164 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69246412 0.00000062 -0.00001673 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000372 0.00000000 -0.00000022 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000045 2.29184993 0.00001842 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000427 0.00000020 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69246432 -0.00000060 -0.00001626 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000372 -0.00000000 -0.00000022 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000026 -2.29184992 0.00001482 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000427 0.00000021 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612729 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612842 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37745358 (1.37745358)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612956 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09114383 (0.09114383)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612942 </eigenvalue_sum>
  Anderson extrapolation: theta=1.61774774 (1.61774774)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612925 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22234570 (0.22234570)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.032" max="    0.032"/>
</iteration>
<iteration count="26">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692774 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280181 </eps>
  <enl>          4.77142540 </enl>
  <ecoul>      -15.60183724 </ecoul>
  <exc>         -4.38813305 </exc>
  <esr>          0.06327155 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69245669 0.00000063 -0.00001719 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000279 0.00000000 -0.00000023 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000045 2.29185847 0.00001884 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000320 0.00000021 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69245688 -0.00000060 -0.00001672 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000279 -0.00000000 -0.00000022 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000026 -2.29185846 0.00001527 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000320 0.00000022 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612744 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612829 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37780119 (1.37780119)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612913 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09115578 (0.09115578)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612904 </eigenvalue_sum>
  Anderson extrapolation: theta=1.62062760 (1.62062760)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612891 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22358718 (0.22358718)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.032"/>
</iteration>
<iteration count="27">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692729 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280202 </eps>
  <enl>          4.77142598 </enl>
  <ecoul>      -15.60183736 </ecoul>
  <exc>         -4.38813284 </exc>
  <esr>          0.06327149 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69245112 0.00000063 -0.00001767 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000209 0.00000000 -0.00000023 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000046 2.29186487 0.00001928 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000240 0.00000021 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69245131 -0.00000061 -0.00001719 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000209 -0.00000000 -0.00000023 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000027 -2.29186486 0.00001573 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000240 0.00000022 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612755 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612819 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37813112 (1.37813112)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612882 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09122434 (0.09122434)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612874 </eigenvalue_sum>
  Anderson extrapolation: theta=1.62575991 (1.62575991)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612865 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22596219 (0.22596219)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="28">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692695 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280219 </eps>
  <enl>          4.77142641 </enl>
  <ecoul>      -15.60183745 </ecoul>
  <exc>         -4.38813268 </exc>
  <esr>          0.06327144 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69244694 0.00000064 -0.00001817 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000157 0.00000000 -0.00000024 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000046 2.29186967 0.00001973 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000180 0.00000022 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69244713 -0.00000062 -0.00001768 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000157 -0.00000000 -0.00000024 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000027 -2.29186965 0.00001620 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000180 0.00000023 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612763 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612811 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37849049 (1.37849049)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612858 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09138792 (0.09138792)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612853 </eigenvalue_sum>
  Anderson extrapolation: theta=1.63508666 (1.63508666)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612845 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23038717 (0.23038717)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="29">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692670 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280231 </eps>
  <enl>          4.77142674 </enl>
  <ecoul>      -15.60183753 </ecoul>
  <exc>         -4.38813256 </exc>
  <esr>          0.06327140 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69244380 0.00000065 -0.00001867 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000117 0.00000000 -0.00000025 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000047 2.29187327 0.00002020 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000135 0.00000023 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69244399 -0.00000063 -0.00001818 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000117 -0.00000000 -0.00000024 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000028 -2.29187325 0.00001669 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000135 0.00000024 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612769 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612805 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37895215 (1.37895215)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612841 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09171630 (0.09171630)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612836 </eigenvalue_sum>
  Anderson extrapolation: theta=1.65204814 (1.65204814)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612831 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23843340 (0.23843340)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="30">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692651 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280241 </eps>
  <enl>          4.77142699 </enl>
  <ecoul>      -15.60183758 </ecoul>
  <exc>         -4.38813247 </exc>
  <esr>          0.06327137 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69244144 0.00000066 -0.00001920 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000088 0.00000000 -0.00000025 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000047 2.29187597 0.00002067 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000101 0.00000023 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69244163 -0.00000064 -0.00001869 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000088 -0.00000000 -0.00000025 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000028 -2.29187595 0.00001719 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000101 0.00000024 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612774 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612801 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37962949 (1.37962949)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612827 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09232740 (0.09232740)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612824 </eigenvalue_sum>
  Anderson extrapolation: theta=1.68243092 (1.68243092)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612820 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25256865 (0.25256865)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="31">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692637 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280248 </eps>
  <enl>          4.77142717 </enl>
  <ecoul>      -15.60183762 </ecoul>
  <exc>         -4.38813240 </exc>
  <esr>          0.06327135 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243967 0.00000067 -0.00001974 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000066 0.00000000 -0.00000026 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000048 2.29187800 0.00002117 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000076 0.00000024 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243986 -0.00000065 -0.00001923 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000066 -0.00000000 -0.00000026 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000029 -2.29187799 0.00001770 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000075 0.00000025 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612777 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612797 </eigenvalue_sum>
  Anderson extrapolation: theta=1.38069081 (1.38069081)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612817 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09339834 (0.09339834)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612815 </eigenvalue_sum>
  Anderson extrapolation: theta=1.73502497 (1.73502497)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612812 </eigenvalue_sum>
  Anderson extrapolation: theta=0.27602890 (0.27602890)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="32">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692627 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280254 </eps>
  <enl>          4.77142731 </enl>
  <ecoul>      -15.60183765 </ecoul>
  <exc>         -4.38813235 </exc>
  <esr>          0.06327134 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243833 0.00000068 -0.00002030 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000049 0.00000000 -0.00000027 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000049 2.29187953 0.00002168 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000056 0.00000025 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243852 -0.00000066 -0.00001978 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000049 -0.00000000 -0.00000027 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000029 -2.29187952 0.00001824 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000056 0.00000026 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612779 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612795 </eigenvalue_sum>
  Anderson extrapolation: theta=1.38234189 (1.38234189)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612810 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09513500 (0.09513500)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612808 </eigenvalue_sum>
  Anderson extrapolation: theta=1.82051687 (1.82051687)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612805 </eigenvalue_sum>
  Anderson extrapolation: theta=0.31147106 (0.31147106)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.038" max="    0.038"/>
</iteration>
<iteration count="33">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692619 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280258 </eps>
  <enl>          4.77142742 </enl>
  <ecoul>      -15.60183767 </ecoul>
  <exc>         -4.38813231 </exc>
  <esr>          0.06327132 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243731 0.00000069 -0.00002088 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000037 0.00000000 -0.00000028 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000049 2.29188070 0.00002222 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000042 0.00000026 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243750 -0.00000067 -0.00002036 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000037 -0.00000000 -0.00000028 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000030 -2.29188068 0.00001879 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000042 0.00000027 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612781 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612793 </eigenvalue_sum>
  Anderson extrapolation: theta=1.38472292 (1.38472292)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612804 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09763271 (0.09763271)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612803 </eigenvalue_sum>
  Anderson extrapolation: theta=1.94554481 (1.94554481)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612801 </eigenvalue_sum>
  Anderson extrapolation: theta=0.35773725 (0.35773725)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.036"/>
</iteration>
<iteration count="34">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692613 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280261 </eps>
  <enl>          4.77142750 </enl>
  <ecoul>      -15.60183769 </ecoul>
  <exc>         -4.38813228 </exc>
  <esr>          0.06327132 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243654 0.00000070 -0.00002150 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000027 0.00000000 -0.00000029 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000050 2.29188158 0.00002279 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000031 0.00000027 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243673 -0.00000068 -0.00002097 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000027 -0.00000000 -0.00000029 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000030 -2.29188157 0.00001938 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000031 0.00000028 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612782 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612791 </eigenvalue_sum>
  Anderson extrapolation: theta=1.38770168 (1.38770168)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612800 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10062762 (0.10062762)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612799 </eigenvalue_sum>
  Anderson extrapolation: theta=2.10122124 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612797 </eigenvalue_sum>
  Anderson extrapolation: theta=0.46452474 (0.46452474)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="35">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692608 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280264 </eps>
  <enl>          4.77142757 </enl>
  <ecoul>      -15.60183771 </ecoul>
  <exc>         -4.38813226 </exc>
  <esr>          0.06327131 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243594 0.00000071 -0.00002217 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000020 0.00000000 -0.00000031 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000050 2.29188226 0.00002340 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000023 0.00000028 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243613 -0.00000069 -0.00002162 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000020 -0.00000000 -0.00000031 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000031 -2.29188225 0.00002001 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000023 0.00000029 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612783 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612790 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39047995 (1.39047995)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612796 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10332046 (0.10332046)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612796 </eigenvalue_sum>
  Anderson extrapolation: theta=2.25842900 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612794 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60024580 (0.60024580)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="36">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692605 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280266 </eps>
  <enl>          4.77142761 </enl>
  <ecoul>      -15.60183772 </ecoul>
  <exc>         -4.38813225 </exc>
  <esr>          0.06327130 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243548 0.00000072 -0.00002289 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000014 0.00000000 -0.00000033 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000051 2.29188278 0.00002406 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000016 0.00000030 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243567 -0.00000070 -0.00002234 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000014 -0.00000000 -0.00000032 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000032 -2.29188277 0.00002070 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000016 0.00000031 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612784 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612789 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39232130 (1.39232130)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612794 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10513018 (0.10513018)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612793 </eigenvalue_sum>
  Anderson extrapolation: theta=2.38265172 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612792 </eigenvalue_sum>
  Anderson extrapolation: theta=0.70515291 (0.70515291)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="37">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692602 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280267 </eps>
  <enl>          4.77142765 </enl>
  <ecoul>      -15.60183772 </ecoul>
  <exc>         -4.38813223 </exc>
  <esr>          0.06327130 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243514 0.00000073 -0.00002368 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000010 0.00000000 -0.00000034 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000052 2.29188317 0.00002478 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000011 0.00000031 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243533 -0.00000071 -0.00002312 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000010 -0.00000000 -0.00000034 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000032 -2.29188316 0.00002144 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000011 0.00000032 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612785 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39342365 (1.39342365)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612792 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10615377 (0.10615377)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612792 </eigenvalue_sum>
  Anderson extrapolation: theta=2.46347214 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612791 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77176283 (0.77176283)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="38">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692601 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142767 </enl>
  <ecoul>      -15.60183773 </ecoul>
  <exc>         -4.38813222 </exc>
  <esr>          0.06327130 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243489 0.00000074 -0.00002453 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000006 0.00000001 -0.00000036 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000052 2.29188345 0.00002556 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000007 0.00000032 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243509 -0.00000072 -0.00002396 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000006 -0.00000001 -0.00000035 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000033 -2.29188344 0.00002225 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000007 0.00000033 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612785 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39403851 (1.39403851)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612791 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10667448 (0.10667448)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612790 </eigenvalue_sum>
  Anderson extrapolation: theta=2.51042141 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612790 </eigenvalue_sum>
  Anderson extrapolation: theta=0.81004010 (0.81004010)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="39">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692599 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142768 </enl>
  <ecoul>      -15.60183773 </ecoul>
  <exc>         -4.38813222 </exc>
  <esr>          0.06327130 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243473 0.00000075 -0.00002544 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000004 0.00000001 -0.00000037 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000053 2.29188365 0.00002639 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000005 0.00000034 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243492 -0.00000074 -0.00002486 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000004 -0.00000001 -0.00000037 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000034 -2.29188363 0.00002310 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000005 0.00000035 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612786 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39437657 (1.39437657)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612790 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10691706 (0.10691706)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612790 </eigenvalue_sum>
  Anderson extrapolation: theta=2.53628450 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612789 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83135832 (0.83135832)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="40">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692598 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280269 </eps>
  <enl>          4.77142769 </enl>
  <ecoul>      -15.60183773 </ecoul>
  <exc>         -4.38813221 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243462 0.00000077 -0.00002639 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000002 0.00000001 -0.00000038 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000054 2.29188377 0.00002725 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000003 0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243481 -0.00000075 -0.00002580 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000002 -0.00000001 -0.00000038 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000035 -2.29188376 0.00002399 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000003 0.00000036 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612786 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39455349 (1.39455349)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612789 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10702060 (0.10702060)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612789 </eigenvalue_sum>
  Anderson extrapolation: theta=2.55014054 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612789 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84307529 (0.84307529)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="41">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692597 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142770 </enl>
  <ecoul>      -15.60183773 </ecoul>
  <exc>         -4.38813221 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243455 0.00000078 -0.00002739 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000001 0.00000001 -0.00000040 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000055 2.29188385 0.00002816 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000002 0.00000036 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243475 -0.00000076 -0.00002678 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000001 -0.00000001 -0.00000039 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000035 -2.29188384 0.00002492 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000002 0.00000037 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612787 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39462981 (1.39462981)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612789 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10706356 (0.10706356)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612789 </eigenvalue_sum>
  Anderson extrapolation: theta=2.55739264 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84939581 (0.84939581)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.097" max="    0.097"/>
</iteration>
<iteration count="42">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692597 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142770 </enl>
  <ecoul>      -15.60183773 </ecoul>
  <exc>         -4.38813221 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243451 0.00000079 -0.00002842 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000001 0.00000001 -0.00000041 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000055 2.29188390 0.00002910 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 0.00000038 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243471 -0.00000078 -0.00002780 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000001 -0.00000001 -0.00000041 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000036 -2.29188389 0.00002589 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 0.00000039 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612787 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39465157 (1.39465157)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10708412 (0.10708412)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56115711 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85277637 (0.85277637)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.044" max="    0.045"/>
</iteration>
<iteration count="43">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692596 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142770 </enl>
  <ecoul>      -15.60183773 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243449 0.00000081 -0.00002950 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000001 0.00000001 -0.00000043 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000056 2.29188393 0.00003007 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 0.00000039 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243468 -0.00000079 -0.00002886 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000001 -0.00000001 -0.00000042 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000037 -2.29188392 0.00002689 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 0.00000040 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612787 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39464988 (1.39464988)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10709609 (0.10709609)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56312719 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85459506 (0.85459506)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="44">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692596 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142770 </enl>
  <ecoul>      -15.60183773 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243448 0.00000082 -0.00003061 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 -0.00000044 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000057 2.29188395 0.00003109 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000000 0.00000040 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243467 -0.00000081 -0.00002996 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 -0.00000044 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000038 -2.29188393 0.00002793 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000000 0.00000041 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39464163 (1.39464163)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10710393 (0.10710393)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56418267 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85559263 (0.85559263)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="45">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692596 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142770 </enl>
  <ecoul>      -15.60183774 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243447 0.00000084 -0.00003176 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 -0.00000046 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000058 2.29188396 0.00003214 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000000 0.00000042 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243466 -0.00000082 -0.00003110 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 -0.00000046 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000039 -2.29188395 0.00002900 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000000 0.00000043 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39463357 (1.39463357)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10710910 (0.10710910)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56476294 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85615146 (0.85615146)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="46">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692596 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142771 </enl>
  <ecoul>      -15.60183774 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243446 0.00000085 -0.00003296 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 -0.00000048 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000059 2.29188397 0.00003323 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000000 0.00000044 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243465 -0.00000084 -0.00003229 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 -0.00000047 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000040 -2.29188395 0.00003012 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000000 0.00000045 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39462760 (1.39462760)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10711248 (0.10711248)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56508991 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85647083 (0.85647083)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="47">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692595 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142771 </enl>
  <ecoul>      -15.60183774 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243446 0.00000087 -0.00003420 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 -0.00000050 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000060 2.29188397 0.00003436 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000000 0.00000045 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243465 -0.00000085 -0.00003351 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 -0.00000049 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000040 -2.29188396 0.00003127 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000000 0.00000046 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39462368 (1.39462368)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10711464 (0.10711464)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56527734 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85665596 (0.85665596)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="48">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692595 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142771 </enl>
  <ecoul>      -15.60183774 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243446 0.00000088 -0.00003548 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 -0.00000051 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000061 2.29188398 0.00003553 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000000 0.00000047 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243465 -0.00000087 -0.00003478 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 -0.00000051 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000041 -2.29188396 0.00003247 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000000 0.00000048 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39462131 (1.39462131)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10711602 (0.10711602)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56538622 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85676453 (0.85676453)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="49">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692595 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142771 </enl>
  <ecoul>      -15.60183774 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243446 0.00000090 -0.00003682 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 -0.00000053 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000062 2.29188398 0.00003675 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000000 0.00000049 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243465 -0.00000088 -0.00003610 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 -0.00000053 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000042 -2.29188396 0.00003371 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000000 0.00000050 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39461996 (1.39461996)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10711690 (0.10711690)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56544991 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85682870 (0.85682870)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="50">
  total_electronic_charge: 16.00000000
  <ekin>         5.28692595 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44280268 </eps>
  <enl>          4.77142771 </enl>
  <ecoul>      -15.60183774 </ecoul>
  <exc>         -4.38813220 </exc>
  <esr>          0.06327129 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37441896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37441896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69243446 0.00000092 -0.00003820 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000001 -0.00000055 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000062 2.29188398 0.00003801 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.00000000 0.00000050 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69243465 -0.00000090 -0.00003747 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000001 -0.00000055 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000043 -2.29188396 0.00003500 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.00000000 0.00000051 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37441896 </econst>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  CGIonicStepper: alpha = 2.50000000
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39461925 (1.39461925)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10711748 (0.10711748)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=2.56548739 (2.00000000)
  <etotal_int>     -15.37441896 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33612788 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85686697 (0.85686697)
  <etotal_int>     -15.37441896 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
  total_electronic_charge: 16.00000000
<timing name="         charge" min="    0.431" max="    0.461"/>
<timing name="         energy" min="    0.553" max="    0.580"/>
<timing name="    ortho_align" min="    0.059" max="    0.086"/>
<timing name="      psda_prec" min="    0.004" max="    0.004"/>
<timing name="  psda_residual" min="    0.016" max="    0.063"/>
<timing name=" psda_update_wf" min="    0.004" max="    0.031"/>
<timing name="    update_vhxc" min="    0.361" max="    0.381"/>
<timing name="      wf_update" min="    0.127" max="    0.169"/>
<timing name="           ekin" min="    0.022" max="    0.052"/>
<timing name="            exc" min="    0.224" max="    0.239"/>
<timing name="           hpsi" min="    0.429" max="    0.434"/>
<timing name="       nonlocal" min="    0.088" max="    0.095"/>
<timing name=" charge_compute" min="    0.280" max="    0.310"/>
<timing name="charge_integral" min="    0.013" max="    0.039"/>
<timing name="  charge_rowsum" min="    0.004" max="    0.007"/>
<timing name="     charge_vft" min="    0.103" max="    0.124"/>
[qbox] <cmd>save test.xml</cmd>
 SampleWriter: write time: 0.007 s
 SampleWriter: file size: 357985
 SampleWriter: aggregate write rate: 48.97 MB/s
[qbox]  End of command stream 
<real_time> 1.88 </real_time>
<end_time> 2016-04-06T12:25:23Z </end_time>
</fpmd:simulation>
