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
<start_time> 2016-04-06T12:25:23Z </start_time>
<mpi_processes count="4">
<process id="0"> theobook68 </process>
<process id="1"> theobook68 </process>
<process id="2"> theobook68 </process>
<process id="3"> theobook68 </process>
</mpi_processes>
[qbox] <cmd># Si4 BO dynamics</cmd>
[qbox] <cmd>load ../si4gs/test.xml</cmd>
 LoadCmd: loading from ../si4gs/test.xml
 XMLGFPreprocessor: reading from ../si4gs/test.xml size: 357985
 XMLGFPreprocessor: read time: 9.394e-05
 XMLGFPreprocessor: local read rate: 908.6 MB/s  aggregate read rate: 3634 MB/s
 XMLGFPreprocessor: tag fixing time: 7.296e-05
 XMLGFPreprocessor: segment definition time: 0.002136
 XMLGFPreprocessor: boundary adjustment time: 2.146e-06
 XMLGFPreprocessor: transcoding time: 3.099e-06
 XMLGFPreprocessor: data redistribution time: 0.000772
 XMLGFPreprocessor: XML compacting time: 0.000169
 XMLGFPreprocessor: total time: 0.003748
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
 SampleReader: read time: 0.02957 s
[qbox] <cmd>set wf_dyn PSDA</cmd>
[qbox] <cmd>set ecutprec 2</cmd>
[qbox] <cmd>set atoms_dyn MD</cmd>
[qbox] <cmd>set dt 40</cmd>
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
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35622829 </eigenvalue_sum>
  <etotal_int>     -15.37295438 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35642769 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93178739 (0.93178739)
  <etotal_int>     -15.37295446 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35661217 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06300154 (0.06300154)
  <etotal_int>     -15.37295448 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35662006 </eigenvalue_sum>
  Anderson extrapolation: theta=1.57746246 (1.57746246)
  <etotal_int>     -15.37295448 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35662893 </eigenvalue_sum>
  Anderson extrapolation: theta=0.20290723 (0.20290723)
  <etotal_int>     -15.37295449 </etotal_int>
  <timing name="iteration" min="    0.032" max="    0.032"/>
</iteration>
<iteration count="2">
  total_electronic_charge: 16.00000000
  <ekin>         5.34816119 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48121316 </eps>
  <enl>          4.77517059 </enl>
  <ecoul>      -15.60247946 </ecoul>
  <exc>         -4.41259364 </exc>
  <esr>          0.07322845 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37295449 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37295449 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70004443 0.00000000 -0.00000002 </position>
    <velocity> 0.00000221 0.00000000 -0.00000000 </velocity>
    <force> 0.00282357 0.00000005 -0.00000116 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20026655 0.00000003 </position>
    <velocity> -0.00000000 0.00001330 0.00000000 </velocity>
    <force> -0.00000004 0.01699648 0.00000147 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70004443 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000221 -0.00000000 -0.00000000 </velocity>
    <force> -0.00282362 -0.00000004 -0.00000110 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20026655 0.00000002 </position>
    <velocity> 0.00000000 -0.00001330 0.00000000 </velocity>
    <force> 0.00000006 -0.01699649 0.00000095 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294518 </econst>
  <ekin_ion> 0.00000931 </ekin_ion>
  <temp_ion> 0.49008740 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35560689 </eigenvalue_sum>
  <etotal_int>     -15.37298178 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35600223 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93054350 (0.93054350)
  <etotal_int>     -15.37298207 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35636789 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06725977 (0.06725977)
  <etotal_int>     -15.37298218 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35638476 </eigenvalue_sum>
  Anderson extrapolation: theta=1.71730531 (1.71730531)
  <etotal_int>     -15.37298219 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35640537 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23655545 (0.23655545)
  <etotal_int>     -15.37298220 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="3">
  total_electronic_charge: 16.00000000
  <ekin>         5.34745423 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48071775 </eps>
  <enl>          4.77506747 </enl>
  <ecoul>      -15.60246993 </ecoul>
  <exc>         -4.41231622 </exc>
  <esr>          0.07310786 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37298220 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37298220 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70017711 0.00000000 -0.00000008 </position>
    <velocity> 0.00000440 0.00000000 -0.00000000 </velocity>
    <force> 0.00276234 0.00000001 -0.00000074 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20106426 0.00000010 </position>
    <velocity> -0.00000000 0.00002651 0.00000000 </velocity>
    <force> -0.00000001 0.01681646 0.00000088 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70017711 -0.00000000 -0.00000008 </position>
    <velocity> -0.00000440 -0.00000000 -0.00000000 </velocity>
    <force> -0.00276234 -0.00000001 -0.00000072 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20106426 0.00000006 </position>
    <velocity> 0.00000000 -0.00002651 0.00000000 </velocity>
    <force> 0.00000001 -0.01681646 0.00000068 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294523 </econst>
  <ekin_ion> 0.00003698 </ekin_ion>
  <temp_ion> 1.94609905 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35524732 </eigenvalue_sum>
  <etotal_int>     -15.37302709 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35563568 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92810824 (0.92810824)
  <etotal_int>     -15.37302737 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35599433 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07093047 (0.07093047)
  <etotal_int>     -15.37302748 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35601185 </eigenvalue_sum>
  Anderson extrapolation: theta=1.88134119 (1.88134119)
  <etotal_int>     -15.37302749 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35603518 </eigenvalue_sum>
  Anderson extrapolation: theta=0.27344694 (0.27344694)
  <etotal_int>     -15.37302750 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="4">
  total_electronic_charge: 16.00000000
  <ekin>         5.34628003 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47992128 </eps>
  <enl>          4.77493131 </enl>
  <ecoul>      -15.60246066 </ecoul>
  <exc>         -4.41185690 </exc>
  <esr>          0.07290849 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37302751 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37302751 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70039611 0.00000001 -0.00000016 </position>
    <velocity> 0.00000651 0.00000000 -0.00000000 </velocity>
    <force> 0.00266003 -0.00000001 -0.00000026 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000001 2.20238753 0.00000021 </position>
    <velocity> -0.00000000 0.00003954 0.00000000 </velocity>
    <force> 0.00000001 0.01652157 0.00000025 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70039612 -0.00000001 -0.00000015 </position>
    <velocity> -0.00000651 -0.00000000 -0.00000000 </velocity>
    <force> -0.00266001 0.00000001 -0.00000027 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000001 -2.20238753 0.00000013 </position>
    <velocity> 0.00000000 -0.00003954 0.00000000 </velocity>
    <force> -0.00000002 -0.01652157 0.00000033 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294531 </econst>
  <ekin_ion> 0.00008220 </ekin_ion>
  <temp_ion> 4.32618569 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35475059 </eigenvalue_sum>
  <etotal_int>     -15.37308871 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35513086 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92644062 (0.92644062)
  <etotal_int>     -15.37308898 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35548142 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06801675 (0.06801675)
  <etotal_int>     -15.37308908 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35549789 </eigenvalue_sum>
  Anderson extrapolation: theta=1.83121409 (1.83121409)
  <etotal_int>     -15.37308909 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35551928 </eigenvalue_sum>
  Anderson extrapolation: theta=0.27170891 (0.27170891)
  <etotal_int>     -15.37308910 </etotal_int>
  <timing name="iteration" min="    0.036" max="    0.036"/>
</iteration>
<iteration count="5">
  total_electronic_charge: 16.00000000
  <ekin>         5.34465349 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47882590 </eps>
  <enl>          4.77475383 </enl>
  <ecoul>      -15.60244989 </ecoul>
  <exc>         -4.41122063 </exc>
  <esr>          0.07263267 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37308910 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37308910 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70069825 0.00000001 -0.00000025 </position>
    <velocity> 0.00000854 0.00000000 -0.00000000 </velocity>
    <force> 0.00251848 -0.00000002 0.00000017 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000001 2.20422713 0.00000031 </position>
    <velocity> -0.00000000 0.00005228 0.00000000 </velocity>
    <force> 0.00000002 0.01611129 -0.00000029 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70069826 -0.00000001 -0.00000024 </position>
    <velocity> -0.00000854 -0.00000000 -0.00000000 </velocity>
    <force> -0.00251845 0.00000002 0.00000014 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000001 -2.20422713 0.00000021 </position>
    <velocity> 0.00000000 -0.00005228 0.00000000 </velocity>
    <force> -0.00000003 -0.01611128 -0.00000005 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294542 </econst>
  <ekin_ion> 0.00014368 </ekin_ion>
  <temp_ion> 7.56228196 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35411548 </eigenvalue_sum>
  <etotal_int>     -15.37316487 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35448567 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92978214 (0.92978214)
  <etotal_int>     -15.37316513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35482783 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06795580 (0.06795580)
  <etotal_int>     -15.37316523 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35484375 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77684499 (1.77684499)
  <etotal_int>     -15.37316524 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35486380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25532610 (0.25532610)
  <etotal_int>     -15.37316524 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="6">
  total_electronic_charge: 16.00000000
  <ekin>         5.34258949 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47744047 </eps>
  <enl>          4.77453334 </enl>
  <ecoul>      -15.60243520 </ecoul>
  <exc>         -4.41041241 </exc>
  <esr>          0.07228364 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316525 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316525 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70107909 0.00000001 -0.00000034 </position>
    <velocity> 0.00001044 0.00000000 -0.00000000 </velocity>
    <force> 0.00233979 -0.00000002 0.00000049 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000001 2.20657024 0.00000042 </position>
    <velocity> -0.00000000 0.00006467 0.00000000 </velocity>
    <force> 0.00000002 0.01559280 -0.00000065 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70107910 -0.00000001 -0.00000032 </position>
    <velocity> -0.00001044 -0.00000000 -0.00000000 </velocity>
    <force> -0.00233977 0.00000002 0.00000046 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000001 -2.20657024 0.00000029 </position>
    <velocity> 0.00000000 -0.00006467 0.00000000 </velocity>
    <force> -0.00000003 -0.01559280 -0.00000037 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294556 </econst>
  <ekin_ion> 0.00021968 </ekin_ion>
  <temp_ion> 11.56235340 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35335400 </eigenvalue_sum>
  <etotal_int>     -15.37325345 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35371022 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93141983 (0.93141983)
  <etotal_int>     -15.37325368 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35403996 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06820003 (0.06820003)
  <etotal_int>     -15.37325378 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35405535 </eigenvalue_sum>
  Anderson extrapolation: theta=1.76363123 (1.76363123)
  <etotal_int>     -15.37325378 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35407466 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24905403 (0.24905403)
  <etotal_int>     -15.37325379 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="7">
  total_electronic_charge: 16.00000000
  <ekin>         5.34010724 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47577905 </eps>
  <enl>          4.77427202 </enl>
  <ecoul>      -15.60241498 </ecoul>
  <exc>         -4.40943902 </exc>
  <esr>          0.07186541 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325379 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325379 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70153306 0.00000001 -0.00000041 </position>
    <velocity> 0.00001218 0.00000000 -0.00000000 </velocity>
    <force> 0.00212596 -0.00000001 0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000001 2.20940065 0.00000050 </position>
    <velocity> -0.00000000 0.00007661 0.00000000 </velocity>
    <force> 0.00000001 0.01497244 -0.00000080 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70153307 -0.00000001 -0.00000039 </position>
    <velocity> -0.00001218 -0.00000000 -0.00000000 </velocity>
    <force> -0.00212595 0.00000001 0.00000064 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000001 -2.20940065 0.00000035 </position>
    <velocity> 0.00000000 -0.00007661 0.00000000 </velocity>
    <force> -0.00000001 -0.01497244 -0.00000059 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294572 </econst>
  <ekin_ion> 0.00030807 </ekin_ion>
  <temp_ion> 16.21415599 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35247192 </eigenvalue_sum>
  <etotal_int>     -15.37335198 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35281119 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93236281 (0.93236281)
  <etotal_int>     -15.37335219 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35312553 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06844592 (0.06844592)
  <etotal_int>     -15.37335228 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35314024 </eigenvalue_sum>
  Anderson extrapolation: theta=1.76531846 (1.76531846)
  <etotal_int>     -15.37335228 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35315877 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24850486 (0.24850486)
  <etotal_int>     -15.37335229 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="8">
  total_electronic_charge: 16.00000000
  <ekin>         5.33723007 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47385956 </eps>
  <enl>          4.77397418 </enl>
  <ecoul>      -15.60238811 </ecoul>
  <exc>         -4.40830887 </exc>
  <esr>          0.07138270 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37335229 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37335229 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70205346 0.00000001 -0.00000045 </position>
    <velocity> 0.00001374 0.00000000 -0.00000000 </velocity>
    <force> 0.00187946 0.00000000 0.00000067 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000001 2.21269898 0.00000055 </position>
    <velocity> -0.00000000 0.00008803 0.00000000 </velocity>
    <force> 0.00000000 0.01425704 -0.00000076 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70205348 -0.00000001 -0.00000044 </position>
    <velocity> -0.00001374 -0.00000000 -0.00000000 </velocity>
    <force> -0.00187946 0.00000000 0.00000066 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.21269898 0.00000040 </position>
    <velocity> 0.00000000 -0.00008803 0.00000000 </velocity>
    <force> -0.00000000 -0.01425704 -0.00000067 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294590 </econst>
  <ekin_ion> 0.00040639 </ekin_ion>
  <temp_ion> 21.38900885 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35147596 </eigenvalue_sum>
  <etotal_int>     -15.37345778 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35179576 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93371931 (0.93371931)
  <etotal_int>     -15.37345797 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35209236 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06884077 (0.06884077)
  <etotal_int>     -15.37345805 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35210627 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77068786 (1.77068786)
  <etotal_int>     -15.37345805 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35212384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24942453 (0.24942453)
  <etotal_int>     -15.37345806 </etotal_int>
  <timing name="iteration" min="    0.037" max="    0.038"/>
</iteration>
<iteration count="9">
  total_electronic_charge: 16.00000000
  <ekin>         5.33398475 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47170319 </eps>
  <enl>          4.77364583 </enl>
  <ecoul>      -15.60235374 </ecoul>
  <exc>         -4.40703170 </exc>
  <esr>          0.07084083 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37345806 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37345806 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70263260 0.00000001 -0.00000048 </position>
    <velocity> 0.00001510 0.00000000 -0.00000000 </velocity>
    <force> 0.00160326 0.00000001 0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000001 2.21644287 0.00000058 </position>
    <velocity> -0.00000000 0.00009885 0.00000000 </velocity>
    <force> -0.00000001 0.01345457 -0.00000059 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70263262 -0.00000001 -0.00000046 </position>
    <velocity> -0.00001510 -0.00000000 -0.00000000 </velocity>
    <force> -0.00160326 -0.00000001 0.00000056 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.21644287 0.00000043 </position>
    <velocity> 0.00000000 -0.00009885 0.00000000 </velocity>
    <force> 0.00000001 -0.01345457 -0.00000061 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294609 </econst>
  <ekin_ion> 0.00051197 </ekin_ion>
  <temp_ion> 26.94613301 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35037405 </eigenvalue_sum>
  <etotal_int>     -15.37356804 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35067210 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93561264 (0.93561264)
  <etotal_int>     -15.37356820 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35094894 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06937376 (0.06937376)
  <etotal_int>     -15.37356827 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35096195 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77509362 (1.77509362)
  <etotal_int>     -15.37356828 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35097839 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24982454 (0.24982454)
  <etotal_int>     -15.37356828 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="10">
  total_electronic_charge: 16.00000000
  <ekin>         5.33040091 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46933310 </eps>
  <enl>          4.77329329 </enl>
  <ecoul>      -15.60231101 </ecoul>
  <exc>         -4.40561837 </exc>
  <esr>          0.07024563 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37356828 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37356828 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70326185 0.00000002 -0.00000049 </position>
    <velocity> 0.00001624 0.00000000 -0.00000000 </velocity>
    <force> 0.00130063 0.00000001 0.00000037 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000001 2.22060724 0.00000060 </position>
    <velocity> -0.00000000 0.00010902 0.00000000 </velocity>
    <force> -0.00000001 0.01257374 -0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70326187 -0.00000001 -0.00000047 </position>
    <velocity> -0.00001624 -0.00000000 -0.00000000 </velocity>
    <force> -0.00130064 -0.00000001 0.00000037 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.22060725 0.00000043 </position>
    <velocity> 0.00000000 -0.00010902 0.00000000 </velocity>
    <force> 0.00000001 -0.01257374 -0.00000044 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294628 </econst>
  <ekin_ion> 0.00062201 </ekin_ion>
  <temp_ion> 32.73735844 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34917500 </eigenvalue_sum>
  <etotal_int>     -15.37367987 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34944933 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93820254 (0.93820254)
  <etotal_int>     -15.37368002 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34970464 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07006562 (0.07006562)
  <etotal_int>     -15.37368007 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34971666 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77683215 (1.77683215)
  <etotal_int>     -15.37368008 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34973187 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24915444 (0.24915444)
  <etotal_int>     -15.37368008 </etotal_int>
  <timing name="iteration" min="    0.032" max="    0.033"/>
</iteration>
<iteration count="11">
  total_electronic_charge: 16.00000000
  <ekin>         5.32651057 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46677372 </eps>
  <enl>          4.77292265 </enl>
  <ecoul>      -15.60225896 </ecoul>
  <exc>         -4.40408063 </exc>
  <esr>          0.06960329 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37368009 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37368009 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70393175 0.00000002 -0.00000049 </position>
    <velocity> 0.00001713 0.00000000 0.00000000 </velocity>
    <force> 0.00097508 0.00000001 0.00000014 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.22516457 0.00000060 </position>
    <velocity> -0.00000000 0.00011847 0.00000000 </velocity>
    <force> -0.00000001 0.01162377 -0.00000010 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70393177 -0.00000001 -0.00000047 </position>
    <velocity> -0.00001713 -0.00000000 0.00000000 </velocity>
    <force> -0.00097508 -0.00000001 0.00000015 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.22516457 0.00000043 </position>
    <velocity> 0.00000000 -0.00011847 -0.00000000 </velocity>
    <force> 0.00000000 -0.01162377 -0.00000021 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294646 </econst>
  <ekin_ion> 0.00073362 </ekin_ion>
  <temp_ion> 38.61185977 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34788850 </eigenvalue_sum>
  <etotal_int>     -15.37379045 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34813738 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94169639 (0.94169639)
  <etotal_int>     -15.37379057 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34836962 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07098810 (0.07098810)
  <etotal_int>     -15.37379062 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34838057 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77662972 (1.77662972)
  <etotal_int>     -15.37379063 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34839444 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24772877 (0.24772877)
  <etotal_int>     -15.37379063 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="12">
  total_electronic_charge: 16.00000000
  <ekin>         5.32234768 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46405041 </eps>
  <enl>          4.77253980 </enl>
  <ecoul>      -15.60219668 </ecoul>
  <exc>         -4.40243103 </exc>
  <esr>          0.06892029 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37379063 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37379063 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70463211 0.00000002 -0.00000049 </position>
    <velocity> 0.00001776 0.00000000 0.00000000 </velocity>
    <force> 0.00063026 0.00000000 -0.00000007 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.23008516 0.00000060 </position>
    <velocity> -0.00000000 0.00012716 0.00000000 </velocity>
    <force> -0.00000000 0.01061417 0.00000011 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70463214 -0.00000001 -0.00000046 </position>
    <velocity> -0.00001776 -0.00000000 0.00000000 </velocity>
    <force> -0.00063025 -0.00000000 -0.00000007 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.23008517 0.00000041 </position>
    <velocity> 0.00000000 -0.00012716 -0.00000000 </velocity>
    <force> 0.00000000 -0.01061417 0.00000003 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294664 </econst>
  <ekin_ion> 0.00084399 </ekin_ion>
  <temp_ion> 44.42074813 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34652478 </eigenvalue_sum>
  <etotal_int>     -15.37389706 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34674675 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94641450 (0.94641450)
  <etotal_int>     -15.37389716 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34695458 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07224385 (0.07224385)
  <etotal_int>     -15.37389720 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34696441 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77535347 (1.77535347)
  <etotal_int>     -15.37389720 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34697681 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24595912 (0.24595912)
  <etotal_int>     -15.37389721 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="13">
  total_electronic_charge: 16.00000000
  <ekin>         5.31794776 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46118922 </eps>
  <enl>          4.77215043 </enl>
  <ecoul>      -15.60212339 </ecoul>
  <exc>         -4.40068278 </exc>
  <esr>          0.06820328 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37389721 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37389721 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70535218 0.00000002 -0.00000048 </position>
    <velocity> 0.00001811 0.00000000 -0.00000000 </velocity>
    <force> 0.00026996 0.00000000 -0.00000023 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.23533747 0.00000060 </position>
    <velocity> -0.00000000 0.00013504 0.00000000 </velocity>
    <force> -0.00000000 0.00955458 0.00000027 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70535220 -0.00000002 -0.00000046 </position>
    <velocity> -0.00001811 -0.00000000 0.00000000 </velocity>
    <force> -0.00026996 -0.00000000 -0.00000023 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.23533747 0.00000040 </position>
    <velocity> 0.00000000 -0.00013504 -0.00000000 </velocity>
    <force> -0.00000000 -0.00955458 0.00000023 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294681 </econst>
  <ekin_ion> 0.00095040 </ekin_ion>
  <temp_ion> 50.02135842 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34509440 </eigenvalue_sum>
  <etotal_int>     -15.37399718 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34528828 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95295898 (0.95295898)
  <etotal_int>     -15.37399725 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34547063 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07398649 (0.07398649)
  <etotal_int>     -15.37399728 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34547925 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77270812 (1.77270812)
  <etotal_int>     -15.37399729 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34549009 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24395425 (0.24395425)
  <etotal_int>     -15.37399729 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="14">
  total_electronic_charge: 16.00000000
  <ekin>         5.31334739 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45821654 </eps>
  <enl>          4.77176005 </enl>
  <ecoul>      -15.60203854 </ecoul>
  <exc>         -4.39884965 </exc>
  <esr>          0.06745893 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37399729 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37399729 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70608068 0.00000002 -0.00000049 </position>
    <velocity> 0.00001817 0.00000000 -0.00000000 </velocity>
    <force> -0.00010194 -0.00000000 -0.00000032 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.24088838 0.00000061 </position>
    <velocity> -0.00000000 0.00014208 0.00000000 </velocity>
    <force> 0.00000000 0.00845462 0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70608070 -0.00000002 -0.00000046 </position>
    <velocity> -0.00001817 -0.00000000 -0.00000000 </velocity>
    <force> 0.00010194 0.00000000 -0.00000033 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.24088838 0.00000040 </position>
    <velocity> 0.00000000 -0.00014208 0.00000000 </velocity>
    <force> -0.00000001 -0.00845461 0.00000035 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294695 </econst>
  <ekin_ion> 0.00105034 </ekin_ion>
  <temp_ion> 55.28108894 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34360816 </eigenvalue_sum>
  <etotal_int>     -15.37408852 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34377303 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96246562 (0.96246562)
  <etotal_int>     -15.37408858 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34392910 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07646430 (0.07646430)
  <etotal_int>     -15.37408860 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34393646 </eigenvalue_sum>
  Anderson extrapolation: theta=1.76701950 (1.76701950)
  <etotal_int>     -15.37408861 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34394563 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24156687 (0.24156687)
  <etotal_int>     -15.37408861 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="15">
  total_electronic_charge: 16.00000000
  <ekin>         5.30858386 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45515877 </eps>
  <enl>          4.77137384 </enl>
  <ecoul>      -15.60194178 </ecoul>
  <exc>         -4.39694575 </exc>
  <esr>          0.06669392 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37408861 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37408861 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70680600 0.00000002 -0.00000050 </position>
    <velocity> 0.00001794 0.00000000 -0.00000000 </velocity>
    <force> -0.00048154 -0.00000000 -0.00000034 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.24670351 0.00000063 </position>
    <velocity> -0.00000000 0.00014824 0.00000000 </velocity>
    <force> 0.00000000 0.00732370 0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70680602 -0.00000002 -0.00000047 </position>
    <velocity> -0.00001794 -0.00000000 -0.00000000 </velocity>
    <force> 0.00048154 0.00000000 -0.00000035 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.24670351 0.00000040 </position>
    <velocity> 0.00000000 -0.00014824 0.00000000 </velocity>
    <force> -0.00000001 -0.00732370 0.00000038 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294708 </econst>
  <ekin_ion> 0.00114153 </ekin_ion>
  <temp_ion> 60.08068781 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34207702 </eigenvalue_sum>
  <etotal_int>     -15.37416914 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34221228 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97717299 (0.97717299)
  <etotal_int>     -15.37416918 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34234153 </eigenvalue_sum>
  Anderson extrapolation: theta=0.08009217 (0.08009217)
  <etotal_int>     -15.37416920 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34234757 </eigenvalue_sum>
  Anderson extrapolation: theta=1.75490714 (1.75490714)
  <etotal_int>     -15.37416920 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34235495 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23859043 (0.23859043)
  <etotal_int>     -15.37416920 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.035"/>
</iteration>
<iteration count="16">
  total_electronic_charge: 16.00000000
  <ekin>         5.30369466 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45204191 </eps>
  <enl>          4.77099655 </enl>
  <ecoul>      -15.60183305 </ecoul>
  <exc>         -4.39498545 </exc>
  <esr>          0.06591478 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37416920 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37416920 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70751626 0.00000003 -0.00000052 </position>
    <velocity> 0.00001742 0.00000000 -0.00000000 </velocity>
    <force> -0.00086496 -0.00000000 -0.00000030 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.25274752 0.00000066 </position>
    <velocity> -0.00000000 0.00015351 0.00000000 </velocity>
    <force> 0.00000000 0.00617097 0.00000030 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70751629 -0.00000002 -0.00000049 </position>
    <velocity> -0.00001742 -0.00000000 -0.00000000 </velocity>
    <force> 0.00086497 0.00000000 -0.00000030 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.25274752 0.00000042 </position>
    <velocity> 0.00000000 -0.00015351 0.00000000 </velocity>
    <force> -0.00000000 -0.00617097 0.00000034 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294718 </econst>
  <ekin_ion> 0.00122202 </ekin_ion>
  <temp_ion> 64.31691474 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34051205 </eigenvalue_sum>
  <etotal_int>     -15.37423740 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34061735 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00196881 (1.00196881)
  <etotal_int>     -15.37423743 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34071952 </eigenvalue_sum>
  Anderson extrapolation: theta=0.08554629 (0.08554629)
  <etotal_int>     -15.37423744 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34072417 </eigenvalue_sum>
  Anderson extrapolation: theta=1.72997148 (1.72997148)
  <etotal_int>     -15.37423744 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34072964 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23501029 (0.23501029)
  <etotal_int>     -15.37423745 </etotal_int>
  <timing name="iteration" min="    0.032" max="    0.032"/>
</iteration>
<iteration count="17">
  total_electronic_charge: 16.00000000
  <ekin>         5.29871716 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44889133 </eps>
  <enl>          4.77063242 </enl>
  <ecoul>      -15.60171252 </ecoul>
  <exc>         -4.39298318 </exc>
  <esr>          0.06512784 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37423745 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37423745 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70819950 0.00000003 -0.00000056 </position>
    <velocity> 0.00001659 0.00000000 -0.00000000 </velocity>
    <force> -0.00124840 0.00000000 -0.00000021 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.25898438 0.00000071 </position>
    <velocity> -0.00000000 0.00015788 0.00000000 </velocity>
    <force> 0.00000000 0.00500516 0.00000021 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70819952 -0.00000002 -0.00000053 </position>
    <velocity> -0.00001659 -0.00000000 -0.00000000 </velocity>
    <force> 0.00124840 -0.00000000 -0.00000021 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.25898439 0.00000045 </position>
    <velocity> 0.00000000 -0.00015788 0.00000000 </velocity>
    <force> -0.00000000 -0.00500516 0.00000024 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294726 </econst>
  <ekin_ion> 0.00129018 </ekin_ion>
  <temp_ion> 67.90453932 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33892431 </eigenvalue_sum>
  <etotal_int>     -15.37429206 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33899954 </eigenvalue_sum>
  Anderson extrapolation: theta=1.04911012 (1.04911012)
  <etotal_int>     -15.37429208 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33907463 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09361660 (0.09361660)
  <etotal_int>     -15.37429209 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33907778 </eigenvalue_sum>
  Anderson extrapolation: theta=1.68080697 (1.68080697)
  <etotal_int>     -15.37429209 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33908123 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23160098 (0.23160098)
  <etotal_int>     -15.37429209 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="18">
  total_electronic_charge: 16.00000000
  <ekin>         5.29368822 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44573145 </eps>
  <enl>          4.77028515 </enl>
  <ecoul>      -15.60158065 </ecoul>
  <exc>         -4.39095335 </exc>
  <esr>          0.06433919 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37429209 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37429209 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70884372 0.00000003 -0.00000060 </position>
    <velocity> 0.00001547 0.00000000 -0.00000000 </velocity>
    <force> -0.00162814 0.00000000 -0.00000010 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000002 2.26537767 0.00000076 </position>
    <velocity> -0.00000000 0.00016133 0.00000000 </velocity>
    <force> -0.00000000 0.00383453 0.00000010 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70884375 -0.00000002 -0.00000057 </position>
    <velocity> -0.00001547 -0.00000000 -0.00000000 </velocity>
    <force> 0.00162815 -0.00000000 -0.00000010 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.26537767 0.00000049 </position>
    <velocity> 0.00000000 -0.00016133 0.00000000 </velocity>
    <force> -0.00000000 -0.00383453 0.00000012 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294732 </econst>
  <ekin_ion> 0.00134477 </ekin_ion>
  <temp_ion> 70.77766715 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33732471 </eigenvalue_sum>
  <etotal_int>     -15.37433225 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33737005 </eigenvalue_sum>
  Anderson extrapolation: theta=1.15389045 (1.15389045)
  <etotal_int>     -15.37433226 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33741810 </eigenvalue_sum>
  Anderson extrapolation: theta=0.10230895 (0.10230895)
  <etotal_int>     -15.37433226 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33741959 </eigenvalue_sum>
  Anderson extrapolation: theta=1.60175376 (1.60175376)
  <etotal_int>     -15.37433226 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33742103 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23139818 (0.23139818)
  <etotal_int>     -15.37433226 </etotal_int>
  <timing name="iteration" min="    0.043" max="    0.044"/>
</iteration>
<iteration count="19">
  total_electronic_charge: 16.00000000
  <ekin>         5.28864388 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44258562 </eps>
  <enl>          4.76995786 </enl>
  <ecoul>      -15.60143817 </ecoul>
  <exc>         -4.38891022 </exc>
  <esr>          0.06355459 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433226 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433226 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70943706 0.00000003 -0.00000064 </position>
    <velocity> 0.00001405 0.00000000 -0.00000000 </velocity>
    <force> -0.00200064 0.00000000 -0.00000000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000003 2.27189079 0.00000081 </position>
    <velocity> -0.00000000 0.00016387 0.00000000 </velocity>
    <force> -0.00000000 0.00266679 -0.00000000 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70943708 -0.00000002 -0.00000061 </position>
    <velocity> -0.00001405 -0.00000000 -0.00000000 </velocity>
    <force> 0.00200064 -0.00000000 0.00000000 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.27189079 0.00000053 </position>
    <velocity> 0.00000000 -0.00016387 0.00000000 </velocity>
    <force> -0.00000000 -0.00266679 -0.00000000 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294735 </econst>
  <ekin_ion> 0.00138491 </ekin_ion>
  <temp_ion> 72.89041274 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33572400 </eigenvalue_sum>
  <etotal_int>     -15.37435747 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33573983 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39360991 (1.39360991)
  <etotal_int>     -15.37435747 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33575933 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09033940 (0.09033940)
  <etotal_int>     -15.37435748 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33575960 </eigenvalue_sum>
  Anderson extrapolation: theta=1.64025263 (1.64025263)
  <etotal_int>     -15.37435748 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33576023 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22868920 (0.22868920)
  <etotal_int>     -15.37435748 </etotal_int>
  <timing name="iteration" min="    0.084" max="    0.084"/>
</iteration>
<iteration count="20">
  total_electronic_charge: 16.00000000
  <ekin>         5.28361912 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43947575 </eps>
  <enl>          4.76965285 </enl>
  <ecoul>      -15.60128597 </ecoul>
  <exc>         -4.38686773 </exc>
  <esr>          0.06277948 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435748 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435748 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70996787 0.00000003 -0.00000069 </position>
    <velocity> 0.00001235 0.00000000 -0.00000000 </velocity>
    <force> -0.00236237 0.00000000 0.00000008 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000003 2.27848726 0.00000086 </position>
    <velocity> -0.00000000 0.00016550 0.00000000 </velocity>
    <force> -0.00000000 0.00150910 -0.00000009 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70996790 -0.00000003 -0.00000065 </position>
    <velocity> -0.00001235 -0.00000000 -0.00000000 </velocity>
    <force> 0.00236237 -0.00000000 0.00000009 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.27848726 0.00000057 </position>
    <velocity> 0.00000000 -0.00016550 0.00000000 </velocity>
    <force> -0.00000000 -0.00150910 -0.00000009 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294736 </econst>
  <ekin_ion> 0.00141012 </ekin_ion>
  <temp_ion> 74.21698001 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33413291 </eigenvalue_sum>
  <etotal_int>     -15.37436761 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33411972 </eigenvalue_sum>
  Anderson extrapolation: theta=1.42030896 (1.42030896)
  <etotal_int>     -15.37436761 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33410567 </eigenvalue_sum>
  Anderson extrapolation: theta=0.08338481 (0.08338481)
  <etotal_int>     -15.37436761 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33410743 </eigenvalue_sum>
  Anderson extrapolation: theta=1.54083418 (1.54083418)
  <etotal_int>     -15.37436761 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33411043 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22206048 (0.22206048)
  <etotal_int>     -15.37436761 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="21">
  total_electronic_charge: 16.00000000
  <ekin>         5.27864743 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43642240 </eps>
  <enl>          4.76937199 </enl>
  <ecoul>      -15.60112518 </ecoul>
  <exc>         -4.38483945 </exc>
  <esr>          0.06201891 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436761 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436761 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71042486 0.00000003 -0.00000073 </position>
    <velocity> 0.00001037 0.00000000 -0.00000000 </velocity>
    <force> -0.00270965 0.00000000 0.00000013 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000003 2.28513088 0.00000091 </position>
    <velocity> -0.00000000 0.00016623 0.00000000 </velocity>
    <force> -0.00000000 0.00036849 -0.00000014 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71042488 -0.00000003 -0.00000069 </position>
    <velocity> -0.00001037 -0.00000000 -0.00000000 </velocity>
    <force> 0.00270966 -0.00000000 0.00000014 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000003 -2.28513089 0.00000060 </position>
    <velocity> 0.00000000 -0.00016623 0.00000000 </velocity>
    <force> -0.00000000 -0.00036849 -0.00000015 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294734 </econst>
  <ekin_ion> 0.00142027 </ekin_ion>
  <temp_ion> 74.75135842 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33256227 </eigenvalue_sum>
  <etotal_int>     -15.37436291 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33252013 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09061138 (1.09061138)
  <etotal_int>     -15.37436291 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33247893 </eigenvalue_sum>
  Anderson extrapolation: theta=0.09601512 (0.09601512)
  <etotal_int>     -15.37436292 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33247899 </eigenvalue_sum>
  Anderson extrapolation: theta=1.40028862 (1.40028862)
  <etotal_int>     -15.37436292 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33248062 </eigenvalue_sum>
  Anderson extrapolation: theta=0.19283119 (0.19283119)
  <etotal_int>     -15.37436292 </etotal_int>
  <timing name="iteration" min="    0.032" max="    0.032"/>
</iteration>
<iteration count="22">
  total_electronic_charge: 16.00000000
  <ekin>         5.27376157 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43344652 </eps>
  <enl>          4.76911884 </enl>
  <ecoul>      -15.60095791 </ecoul>
  <exc>         -4.38283889 </exc>
  <esr>          0.06127754 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436292 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436292 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71079716 0.00000004 -0.00000077 </position>
    <velocity> 0.00000812 0.00000000 -0.00000000 </velocity>
    <force> -0.00304038 0.00000000 0.00000015 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000003 2.29178603 0.00000095 </position>
    <velocity> -0.00000000 0.00016609 0.00000000 </velocity>
    <force> -0.00000000 -0.00074976 -0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71079719 -0.00000003 -0.00000073 </position>
    <velocity> -0.00000812 -0.00000000 -0.00000000 </velocity>
    <force> 0.00304038 -0.00000000 0.00000015 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000003 -2.29178603 0.00000064 </position>
    <velocity> 0.00000000 -0.00016609 0.00000000 </velocity>
    <force> -0.00000000 0.00074976 -0.00000017 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294731 </econst>
  <ekin_ion> 0.00141561 </ekin_ion>
  <temp_ion> 74.50609283 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33101877 </eigenvalue_sum>
  <etotal_int>     -15.37434394 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33094977 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97438039 (0.97438039)
  <etotal_int>     -15.37434395 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33088527 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07821561 (0.07821561)
  <etotal_int>     -15.37434395 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33088344 </eigenvalue_sum>
  Anderson extrapolation: theta=1.52439290 (1.52439290)
  <etotal_int>     -15.37434395 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.33088266 </eigenvalue_sum>
  Anderson extrapolation: theta=0.19413884 (0.19413884)
  <etotal_int>     -15.37434395 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="23">
  total_electronic_charge: 16.00000000
  <ekin>         5.26899137 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43056444 </eps>
  <enl>          4.76889269 </enl>
  <ecoul>      -15.60078519 </ecoul>
  <exc>         -4.38087839 </exc>
  <esr>          0.06055965 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434395 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434395 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71107444 0.00000004 -0.00000080 </position>
    <velocity> 0.00000562 0.00000000 -0.00000000 </velocity>
    <force> -0.00335146 0.00000000 0.00000014 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000003 2.29841774 0.00000099 </position>
    <velocity> -0.00000000 0.00016507 0.00000000 </velocity>
    <force> -0.00000000 -0.00183955 -0.00000014 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71107447 -0.00000003 -0.00000076 </position>
    <velocity> -0.00000562 -0.00000000 -0.00000000 </velocity>
    <force> 0.00335146 -0.00000000 0.00000014 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000003 -2.29841774 0.00000066 </position>
    <velocity> 0.00000000 -0.00016507 0.00000000 </velocity>
    <force> -0.00000000 0.00183955 -0.00000015 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294725 </econst>
  <ekin_ion> 0.00139670 </ekin_ion>
  <temp_ion> 73.51101632 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32951550 </eigenvalue_sum>
  <etotal_int>     -15.37431156 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32941992 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93444435 (0.93444435)
  <etotal_int>     -15.37431158 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32933189 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06631455 (0.06631455)
  <etotal_int>     -15.37431158 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32932858 </eigenvalue_sum>
  Anderson extrapolation: theta=1.59568714 (1.59568714)
  <etotal_int>     -15.37431159 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32932554 </eigenvalue_sum>
  Anderson extrapolation: theta=0.20979410 (0.20979410)
  <etotal_int>     -15.37431159 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.032"/>
</iteration>
<iteration count="24">
  total_electronic_charge: 16.00000000
  <ekin>         5.26436575 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42779252 </eps>
  <enl>          4.76869415 </enl>
  <ecoul>      -15.60060884 </ecoul>
  <exc>         -4.37897012 </exc>
  <esr>          0.05986912 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37431159 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37431159 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71124699 0.00000004 -0.00000083 </position>
    <velocity> 0.00000289 0.00000000 -0.00000000 </velocity>
    <force> -0.00364038 0.00000000 0.00000010 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000003 2.30499196 0.00000103 </position>
    <velocity> -0.00000000 0.00016322 0.00000000 </velocity>
    <force> 0.00000000 -0.00289627 -0.00000011 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71124702 -0.00000003 -0.00000078 </position>
    <velocity> -0.00000289 -0.00000000 -0.00000000 </velocity>
    <force> 0.00364039 -0.00000000 0.00000010 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000003 -2.30499196 0.00000068 </position>
    <velocity> 0.00000000 -0.00016322 0.00000000 </velocity>
    <force> -0.00000000 0.00289627 -0.00000011 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294717 </econst>
  <ekin_ion> 0.00136442 </ekin_ion>
  <temp_ion> 71.81175208 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32805948 </eigenvalue_sum>
  <etotal_int>     -15.37426691 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32793854 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91976809 (0.91976809)
  <etotal_int>     -15.37426693 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32782762 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06115394 (0.06115394)
  <etotal_int>     -15.37426694 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32782299 </eigenvalue_sum>
  Anderson extrapolation: theta=1.63971608 (1.63971608)
  <etotal_int>     -15.37426695 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32781796 </eigenvalue_sum>
  Anderson extrapolation: theta=0.22283668 (0.22283668)
  <etotal_int>     -15.37426695 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.031"/>
</iteration>
<iteration count="25">
  total_electronic_charge: 16.00000000
  <ekin>         5.25991183 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42514560 </eps>
  <enl>          4.76852332 </enl>
  <ecoul>      -15.60043087 </ecoul>
  <exc>         -4.37712562 </exc>
  <esr>          0.05920944 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37426695 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37426695 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71130577 0.00000004 -0.00000085 </position>
    <velocity> -0.00000006 0.00000000 -0.00000000 </velocity>
    <force> -0.00390480 0.00000000 0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000003 2.31147567 0.00000106 </position>
    <velocity> -0.00000000 0.00016056 0.00000000 </velocity>
    <force> 0.00000000 -0.00391583 -0.00000006 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71130579 -0.00000003 -0.00000081 </position>
    <velocity> 0.00000006 -0.00000000 -0.00000000 </velocity>
    <force> 0.00390481 -0.00000000 0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000003 -2.31147567 0.00000070 </position>
    <velocity> -0.00000000 -0.00016056 0.00000000 </velocity>
    <force> -0.00000000 0.00391583 -0.00000005 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294707 </econst>
  <ekin_ion> 0.00131988 </ekin_ion>
  <temp_ion> 69.46746398 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32665879 </eigenvalue_sum>
  <etotal_int>     -15.37421133 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32651385 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91370051 (0.91370051)
  <etotal_int>     -15.37421136 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32638103 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05877133 (0.05877133)
  <etotal_int>     -15.37421138 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32637520 </eigenvalue_sum>
  Anderson extrapolation: theta=1.66938855 (1.66938855)
  <etotal_int>     -15.37421138 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32636835 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23161125 (0.23161125)
  <etotal_int>     -15.37421138 </etotal_int>
  <timing name="iteration" min="    0.040" max="    0.040"/>
</iteration>
<iteration count="26">
  total_electronic_charge: 16.00000000
  <ekin>         5.25565470 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42263721 </eps>
  <enl>          4.76838024 </enl>
  <ecoul>      -15.60025336 </ecoul>
  <exc>         -4.37535575 </exc>
  <esr>          0.05858372 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37421138 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37421138 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71124251 0.00000004 -0.00000088 </position>
    <velocity> -0.00000320 0.00000000 -0.00000000 </velocity>
    <force> -0.00414254 0.00000000 -0.00000000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000004 2.31783700 0.00000109 </position>
    <velocity> -0.00000000 0.00015712 0.00000000 </velocity>
    <force> 0.00000000 -0.00489444 -0.00000000 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71124254 -0.00000003 -0.00000083 </position>
    <velocity> 0.00000320 -0.00000000 -0.00000000 </velocity>
    <force> 0.00414254 -0.00000000 -0.00000000 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000003 -2.31783700 0.00000072 </position>
    <velocity> -0.00000000 -0.00015712 0.00000000 </velocity>
    <force> -0.00000000 0.00489444 0.00000001 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294696 </econst>
  <ekin_ion> 0.00126442 </ekin_ion>
  <temp_ion> 66.54883872 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32532134 </eigenvalue_sum>
  <etotal_int>     -15.37414634 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32515376 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91122078 (0.91122078)
  <etotal_int>     -15.37414639 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32500014 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05765704 (0.05765704)
  <etotal_int>     -15.37414641 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32499319 </eigenvalue_sum>
  Anderson extrapolation: theta=1.69074389 (1.69074389)
  <etotal_int>     -15.37414641 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32498466 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23722724 (0.23722724)
  <etotal_int>     -15.37414641 </etotal_int>
  <timing name="iteration" min="    0.031" max="    0.032"/>
</iteration>
<iteration count="27">
  total_electronic_charge: 16.00000000
  <ekin>         5.25161745 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42027953 </eps>
  <enl>          4.76826474 </enl>
  <ecoul>      -15.60007845 </ecoul>
  <exc>         -4.37367062 </exc>
  <esr>          0.05799473 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37414641 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37414641 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71104979 0.00000004 -0.00000090 </position>
    <velocity> -0.00000652 0.00000000 -0.00000000 </velocity>
    <force> -0.00435169 0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000004 2.32404537 0.00000112 </position>
    <velocity> -0.00000000 0.00015293 0.00000000 </velocity>
    <force> 0.00000000 -0.00582875 0.00000005 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71104982 -0.00000004 -0.00000085 </position>
    <velocity> 0.00000652 -0.00000000 -0.00000000 </velocity>
    <force> 0.00435169 -0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000003 -2.32404537 0.00000074 </position>
    <velocity> -0.00000000 -0.00015293 0.00000000 </velocity>
    <force> -0.00000000 0.00582875 0.00000006 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294683 </econst>
  <ekin_ion> 0.00119958 </ekin_ion>
  <temp_ion> 63.13596454 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32405434 </eigenvalue_sum>
  <etotal_int>     -15.37407361 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32386555 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91036870 (0.91036870)
  <etotal_int>     -15.37407367 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32369235 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05716338 (0.05716338)
  <etotal_int>     -15.37407370 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32368434 </eigenvalue_sum>
  Anderson extrapolation: theta=1.70758458 (1.70758458)
  <etotal_int>     -15.37407370 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32367425 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24103070 (0.24103070)
  <etotal_int>     -15.37407370 </etotal_int>
  <timing name="iteration" min="    0.032" max="    0.032"/>
</iteration>
<iteration count="28">
  total_electronic_charge: 16.00000000
  <ekin>         5.24782122 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41808338 </eps>
  <enl>          4.76817640 </enl>
  <ecoul>      -15.59990831 </ecoul>
  <exc>         -4.37207963 </exc>
  <esr>          0.05744489 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37407370 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37407370 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71072107 0.00000005 -0.00000093 </position>
    <velocity> -0.00000999 0.00000000 -0.00000000 </velocity>
    <force> -0.00453058 0.00000000 -0.00000008 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000004 2.33007157 0.00000115 </position>
    <velocity> -0.00000000 0.00014803 0.00000000 </velocity>
    <force> -0.00000000 -0.00671585 0.00000009 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71072110 -0.00000004 -0.00000087 </position>
    <velocity> 0.00000999 -0.00000000 -0.00000000 </velocity>
    <force> 0.00453058 -0.00000000 -0.00000008 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.33007158 0.00000076 </position>
    <velocity> -0.00000000 -0.00014803 0.00000000 </velocity>
    <force> -0.00000000 0.00671585 0.00000009 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294670 </econst>
  <ekin_ion> 0.00112700 </ekin_ion>
  <temp_ion> 59.31609292 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32286438 </eigenvalue_sum>
  <etotal_int>     -15.37399490 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32265590 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91030963 (0.91030963)
  <etotal_int>     -15.37399497 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32246441 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05698913 (0.05698913)
  <etotal_int>     -15.37399500 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32245542 </eigenvalue_sum>
  Anderson extrapolation: theta=1.72146195 (1.72146195)
  <etotal_int>     -15.37399500 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32244385 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24374507 (0.24374507)
  <etotal_int>     -15.37399501 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="29">
  total_electronic_charge: 16.00000000
  <ekin>         5.24428522 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41605829 </eps>
  <enl>          4.76811460 </enl>
  <ecoul>      -15.59974509 </ecoul>
  <exc>         -4.37059145 </exc>
  <esr>          0.05693630 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37399501 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37399501 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71025076 0.00000005 -0.00000095 </position>
    <velocity> -0.00001359 0.00000000 -0.00000000 </velocity>
    <force> -0.00467777 0.00000000 -0.00000010 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000004 2.33588790 0.00000119 </position>
    <velocity> -0.00000000 0.00014246 0.00000000 </velocity>
    <force> -0.00000000 -0.00755324 0.00000010 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71025079 -0.00000004 -0.00000090 </position>
    <velocity> 0.00001359 -0.00000000 -0.00000000 </velocity>
    <force> 0.00467777 -0.00000000 -0.00000010 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.33588791 0.00000078 </position>
    <velocity> -0.00000000 -0.00014246 0.00000000 </velocity>
    <force> -0.00000000 0.00755324 0.00000011 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294656 </econst>
  <ekin_ion> 0.00104844 </ekin_ion>
  <temp_ion> 55.18139279 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32175746 </eigenvalue_sum>
  <etotal_int>     -15.37391200 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32153084 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91066764 (0.91066764)
  <etotal_int>     -15.37391209 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32132244 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05699077 (0.05699077)
  <etotal_int>     -15.37391213 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32131252 </eigenvalue_sum>
  Anderson extrapolation: theta=1.73308746 (1.73308746)
  <etotal_int>     -15.37391213 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32129958 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24572711 (0.24572711)
  <etotal_int>     -15.37391213 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="30">
  total_electronic_charge: 16.00000000
  <ekin>         5.24102674 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41421261 </eps>
  <enl>          4.76807861 </enl>
  <ecoul>      -15.59959090 </ecoul>
  <exc>         -4.36921398 </exc>
  <esr>          0.05647078 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37391213 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37391213 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70963427 0.00000005 -0.00000098 </position>
    <velocity> -0.00001728 0.00000000 -0.00000000 </velocity>
    <force> -0.00479201 0.00000000 -0.00000010 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000004 2.34146817 0.00000123 </position>
    <velocity> -0.00000000 0.00013625 0.00000000 </velocity>
    <force> 0.00000000 -0.00833878 0.00000010 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70963429 -0.00000004 -0.00000093 </position>
    <velocity> 0.00001728 -0.00000000 -0.00000000 </velocity>
    <force> 0.00479202 -0.00000000 -0.00000010 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.34146818 0.00000081 </position>
    <velocity> -0.00000000 -0.00013625 0.00000000 </velocity>
    <force> -0.00000000 0.00833878 0.00000011 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294643 </econst>
  <ekin_ion> 0.00096570 </ekin_ion>
  <temp_ion> 50.82675917 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32073898 </eigenvalue_sum>
  <etotal_int>     -15.37382674 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32049580 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91125608 (0.91125608)
  <etotal_int>     -15.37382685 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32027192 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05709714 (0.05709714)
  <etotal_int>     -15.37382689 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32026116 </eigenvalue_sum>
  Anderson extrapolation: theta=1.74296613 (1.74296613)
  <etotal_int>     -15.37382689 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32024695 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24719176 (0.24719176)
  <etotal_int>     -15.37382689 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="31">
  total_electronic_charge: 16.00000000
  <ekin>         5.23806117 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41255354 </eps>
  <enl>          4.76806764 </enl>
  <ecoul>      -15.59944779 </ecoul>
  <exc>         -4.36795438 </exc>
  <esr>          0.05604985 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37382689 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37382689 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70886801 0.00000005 -0.00000102 </position>
    <velocity> -0.00002106 0.00000000 -0.00000000 </velocity>
    <force> -0.00487228 0.00000000 -0.00000009 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000004 2.34678784 0.00000127 </position>
    <velocity> -0.00000000 0.00012945 0.00000000 </velocity>
    <force> 0.00000000 -0.00907066 0.00000009 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70886804 -0.00000004 -0.00000096 </position>
    <velocity> 0.00002106 -0.00000000 -0.00000000 </velocity>
    <force> 0.00487228 -0.00000000 -0.00000009 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.34678785 0.00000083 </position>
    <velocity> -0.00000000 -0.00012945 0.00000000 </velocity>
    <force> -0.00000000 0.00907066 0.00000009 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294629 </econst>
  <ekin_ion> 0.00088060 </ekin_ion>
  <temp_ion> 46.34771582 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31981375 </eigenvalue_sum>
  <etotal_int>     -15.37374091 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31955564 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91197542 (0.91197542)
  <etotal_int>     -15.37374103 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31931775 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05727172 (0.05727172)
  <etotal_int>     -15.37374108 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31930622 </eigenvalue_sum>
  Anderson extrapolation: theta=1.75150100 (1.75150100)
  <etotal_int>     -15.37374108 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31929085 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24828431 (0.24828431)
  <etotal_int>     -15.37374108 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="32">
  total_electronic_charge: 16.00000000
  <ekin>         5.23540204 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41108729 </eps>
  <enl>          4.76808087 </enl>
  <ecoul>      -15.59931769 </ecoul>
  <exc>         -4.36681901 </exc>
  <esr>          0.05567482 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37374108 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37374108 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70794949 0.00000005 -0.00000106 </position>
    <velocity> -0.00002488 0.00000000 -0.00000000 </velocity>
    <force> -0.00491773 0.00000000 -0.00000007 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000004 2.35182403 0.00000131 </position>
    <velocity> -0.00000000 0.00012210 0.00000000 </velocity>
    <force> 0.00000000 -0.00974737 0.00000007 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70794951 -0.00000005 -0.00000100 </position>
    <velocity> 0.00002488 -0.00000000 -0.00000000 </velocity>
    <force> 0.00491773 -0.00000000 -0.00000007 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.35182404 0.00000087 </position>
    <velocity> -0.00000000 -0.00012210 0.00000000 </velocity>
    <force> -0.00000000 0.00974737 0.00000007 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294615 </econst>
  <ekin_ion> 0.00079493 </ekin_ion>
  <temp_ion> 41.83844347 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31898598 </eigenvalue_sum>
  <etotal_int>     -15.37365625 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31871460 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91277108 (0.91277108)
  <etotal_int>     -15.37365638 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31846422 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05749542 (0.05749542)
  <etotal_int>     -15.37365643 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31845199 </eigenvalue_sum>
  Anderson extrapolation: theta=1.75899669 (1.75899669)
  <etotal_int>     -15.37365643 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31843557 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24910291 (0.24910291)
  <etotal_int>     -15.37365643 </etotal_int>
  <timing name="iteration" min="    0.035" max="    0.036"/>
</iteration>
<iteration count="33">
  total_electronic_charge: 16.00000000
  <ekin>         5.23306102 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40981903 </eps>
  <enl>          4.76811751 </enl>
  <ecoul>      -15.59920244 </ecoul>
  <exc>         -4.36581350 </exc>
  <esr>          0.05534673 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37365643 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37365643 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70687727 0.00000006 -0.00000109 </position>
    <velocity> -0.00002873 0.00000000 -0.00000000 </velocity>
    <force> -0.00492768 0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000005 2.35655560 0.00000136 </position>
    <velocity> -0.00000000 0.00011424 0.00000000 </velocity>
    <force> 0.00000000 -0.01036764 0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70687730 -0.00000005 -0.00000103 </position>
    <velocity> 0.00002873 -0.00000000 -0.00000000 </velocity>
    <force> 0.00492768 -0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.35655561 0.00000090 </position>
    <velocity> -0.00000000 -0.00011424 0.00000000 </velocity>
    <force> -0.00000000 0.01036764 0.00000004 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294603 </econst>
  <ekin_ion> 0.00071041 </ekin_ion>
  <temp_ion> 37.38995839 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31825934 </eigenvalue_sum>
  <etotal_int>     -15.37357438 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31797635 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91361339 (0.91361339)
  <etotal_int>     -15.37357452 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31771501 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05775855 (0.05775855)
  <etotal_int>     -15.37357458 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31770217 </eigenvalue_sum>
  Anderson extrapolation: theta=1.76567493 (1.76567493)
  <etotal_int>     -15.37357458 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31768482 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24971306 (0.24971306)
  <etotal_int>     -15.37357459 </etotal_int>
  <timing name="iteration" min="    0.037" max="    0.037"/>
</iteration>
<iteration count="34">
  total_electronic_charge: 16.00000000
  <ekin>         5.23104805 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40875305 </eps>
  <enl>          4.76817679 </enl>
  <ecoul>      -15.59910370 </ecoul>
  <exc>         -4.36494268 </exc>
  <esr>          0.05506643 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37357459 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37357459 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70565106 0.00000006 -0.00000113 </position>
    <velocity> -0.00003257 0.00000000 -0.00000000 </velocity>
    <force> -0.00490166 0.00000000 -0.00000002 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000005 2.36096316 0.00000140 </position>
    <velocity> -0.00000000 0.00010592 0.00000000 </velocity>
    <force> 0.00000000 -0.01093047 0.00000001 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70565109 -0.00000005 -0.00000107 </position>
    <velocity> 0.00003257 -0.00000000 -0.00000000 </velocity>
    <force> 0.00490166 -0.00000000 -0.00000002 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.36096317 0.00000094 </position>
    <velocity> -0.00000000 -0.00010592 0.00000000 </velocity>
    <force> -0.00000000 0.01093047 0.00000002 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294591 </econst>
  <ekin_ion> 0.00062868 </ekin_ion>
  <temp_ion> 33.08846000 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31763691 </eigenvalue_sum>
  <etotal_int>     -15.37349684 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31734399 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91448729 (0.91448729)
  <etotal_int>     -15.37349699 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31707324 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05805676 (0.05805676)
  <etotal_int>     -15.37349705 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31705988 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77169645 (1.77169645)
  <etotal_int>     -15.37349705 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31704173 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25015833 (0.25015833)
  <etotal_int>     -15.37349706 </etotal_int>
  <timing name="iteration" min="    0.039" max="    0.040"/>
</iteration>
<iteration count="35">
  total_electronic_charge: 16.00000000
  <ekin>         5.22937127 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40789274 </eps>
  <enl>          4.76825799 </enl>
  <ecoul>      -15.59902295 </ecoul>
  <exc>         -4.36421063 </exc>
  <esr>          0.05483456 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37349706 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37349706 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70427166 0.00000006 -0.00000118 </position>
    <velocity> -0.00003638 0.00000000 -0.00000000 </velocity>
    <force> -0.00483935 0.00000000 0.00000000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000005 2.36502912 0.00000145 </position>
    <velocity> -0.00000000 0.00009718 0.00000000 </velocity>
    <force> 0.00000000 -0.01143503 -0.00000001 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70427168 -0.00000005 -0.00000111 </position>
    <velocity> 0.00003638 -0.00000000 -0.00000000 </velocity>
    <force> 0.00483934 -0.00000000 0.00000000 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.36502913 0.00000097 </position>
    <velocity> -0.00000000 -0.00009718 0.00000000 </velocity>
    <force> -0.00000000 0.01143503 -0.00000000 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294580 </econst>
  <ekin_ion> 0.00055126 </ekin_ion>
  <temp_ion> 29.01386159 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31712120 </eigenvalue_sum>
  <etotal_int>     -15.37342499 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31682005 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91538700 (0.91538700)
  <etotal_int>     -15.37342516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31654146 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05838909 (0.05838909)
  <etotal_int>     -15.37342522 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31652765 </eigenvalue_sum>
  Anderson extrapolation: theta=1.77717709 (1.77717709)
  <etotal_int>     -15.37342522 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31650884 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25046700 (0.25046700)
  <etotal_int>     -15.37342523 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="36">
  total_electronic_charge: 16.00000000
  <ekin>         5.22803715 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40724068 </eps>
  <enl>          4.76836047 </enl>
  <ecoul>      -15.59896151 </ecoul>
  <exc>         -4.36362066 </exc>
  <esr>          0.05465159 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37342523 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37342523 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70274102 0.00000006 -0.00000122 </position>
    <velocity> -0.00004012 0.00000000 -0.00000000 </velocity>
    <force> -0.00474059 0.00000000 0.00000001 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000005 2.36873771 0.00000150 </position>
    <velocity> -0.00000000 0.00008807 0.00000000 </velocity>
    <force> 0.00000000 -0.01188070 -0.00000002 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70274105 -0.00000005 -0.00000115 </position>
    <velocity> 0.00004012 -0.00000000 -0.00000000 </velocity>
    <force> 0.00474059 -0.00000000 0.00000001 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.36873772 0.00000101 </position>
    <velocity> -0.00000000 -0.00008807 0.00000000 </velocity>
    <force> 0.00000000 0.01188070 -0.00000001 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294570 </econst>
  <ekin_ion> 0.00047953 </ekin_ion>
  <temp_ion> 25.23851421 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31671418 </eigenvalue_sum>
  <etotal_int>     -15.37336006 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31640649 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91631332 (0.91631332)
  <etotal_int>     -15.37336023 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31612164 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05875682 (0.05875682)
  <etotal_int>     -15.37336030 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31610748 </eigenvalue_sum>
  Anderson extrapolation: theta=1.78219775 (1.78219775)
  <etotal_int>     -15.37336030 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31608813 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25065579 (0.25065579)
  <etotal_int>     -15.37336031 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="37">
  total_electronic_charge: 16.00000000
  <ekin>         5.22705049 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40679864 </eps>
  <enl>          4.76848365 </enl>
  <ecoul>      -15.59892046 </ecoul>
  <exc>         -4.36317535 </exc>
  <esr>          0.05451784 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37336031 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37336031 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70106223 0.00000006 -0.00000126 </position>
    <velocity> -0.00004377 0.00000000 -0.00000000 </velocity>
    <force> -0.00460540 0.00000000 0.00000002 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000005 2.37207501 0.00000155 </position>
    <velocity> -0.00000000 0.00007864 0.00000000 </velocity>
    <force> 0.00000000 -0.01226700 -0.00000002 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70106225 -0.00000006 -0.00000119 </position>
    <velocity> 0.00004377 -0.00000000 -0.00000000 </velocity>
    <force> 0.00460540 -0.00000000 0.00000002 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.37207502 0.00000104 </position>
    <velocity> -0.00000000 -0.00007864 0.00000000 </velocity>
    <force> 0.00000000 0.01226700 -0.00000002 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294561 </econst>
  <ekin_ion> 0.00041469 </ekin_ion>
  <temp_ion> 21.82613033 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31641728 </eigenvalue_sum>
  <etotal_int>     -15.37330307 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31610474 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91727248 (0.91727248)
  <etotal_int>     -15.37330325 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31581521 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05916307 (0.05916307)
  <etotal_int>     -15.37330331 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31580079 </eigenvalue_sum>
  Anderson extrapolation: theta=1.78681084 (1.78681084)
  <etotal_int>     -15.37330332 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31578104 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25073252 (0.25073252)
  <etotal_int>     -15.37330332 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="38">
  total_electronic_charge: 16.00000000
  <ekin>         5.22641442 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40656763 </eps>
  <enl>          4.76862705 </enl>
  <ecoul>      -15.59890067 </ecoul>
  <exc>         -4.36287649 </exc>
  <esr>          0.05443344 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37330333 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37330333 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69923951 0.00000007 -0.00000130 </position>
    <velocity> -0.00004730 0.00000000 -0.00000000 </velocity>
    <force> -0.00443395 0.00000000 0.00000001 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000005 2.37502894 0.00000159 </position>
    <velocity> -0.00000000 0.00006893 0.00000000 </velocity>
    <force> 0.00000000 -0.01259361 -0.00000002 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69923953 -0.00000006 -0.00000123 </position>
    <velocity> 0.00004730 -0.00000000 -0.00000000 </velocity>
    <force> 0.00443395 -0.00000000 0.00000001 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.37502895 0.00000108 </position>
    <velocity> -0.00000000 -0.00006893 0.00000000 </velocity>
    <force> 0.00000000 0.01259361 -0.00000001 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294554 </econst>
  <ekin_ion> 0.00035779 </ekin_ion>
  <temp_ion> 18.83091128 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31623137 </eigenvalue_sum>
  <etotal_int>     -15.37325486 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31591568 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91827578 (0.91827578)
  <etotal_int>     -15.37325504 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31562305 </eigenvalue_sum>
  Anderson extrapolation: theta=0.05961257 (0.05961257)
  <etotal_int>     -15.37325511 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31560847 </eigenvalue_sum>
  Anderson extrapolation: theta=1.79104500 (1.79104500)
  <etotal_int>     -15.37325511 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31558846 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25069821 (0.25069821)
  <etotal_int>     -15.37325512 </etotal_int>
  <timing name="iteration" min="    0.037" max="    0.037"/>
</iteration>
<iteration count="39">
  total_electronic_charge: 16.00000000
  <ekin>         5.22613051 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40654795 </eps>
  <enl>          4.76879025 </enl>
  <ecoul>      -15.59890277 </ecoul>
  <exc>         -4.36272516 </exc>
  <esr>          0.05439839 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325512 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325512 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69727822 0.00000007 -0.00000134 </position>
    <velocity> -0.00005068 0.00000000 -0.00000000 </velocity>
    <force> -0.00422655 0.00000000 0.00000000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000005 2.37758930 0.00000164 </position>
    <velocity> -0.00000000 0.00005898 0.00000000 </velocity>
    <force> 0.00000000 -0.01286035 -0.00000001 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69727824 -0.00000006 -0.00000126 </position>
    <velocity> 0.00005068 -0.00000000 -0.00000000 </velocity>
    <force> 0.00422655 -0.00000000 0.00000000 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.37758930 0.00000111 </position>
    <velocity> -0.00000000 -0.00005898 0.00000000 </velocity>
    <force> 0.00000000 0.01286035 -0.00000000 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294548 </econst>
  <ekin_ion> 0.00030964 </ekin_ion>
  <temp_ion> 16.29687953 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31615683 </eigenvalue_sum>
  <etotal_int>     -15.37321606 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31583968 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91933984 (0.91933984)
  <etotal_int>     -15.37321624 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31554553 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06011169 (0.06011169)
  <etotal_int>     -15.37321631 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31553087 </eigenvalue_sum>
  Anderson extrapolation: theta=1.79490808 (1.79490808)
  <etotal_int>     -15.37321632 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31551075 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25054875 (0.25054875)
  <etotal_int>     -15.37321632 </etotal_int>
  <timing name="iteration" min="    0.037" max="    0.037"/>
</iteration>
<iteration count="40">
  total_electronic_charge: 16.00000000
  <ekin>         5.22619871 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40673912 </eps>
  <enl>          4.76897292 </enl>
  <ecoul>      -15.59892715 </ecoul>
  <exc>         -4.36272169 </exc>
  <esr>          0.05441256 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321633 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321633 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69518484 0.00000007 -0.00000138 </position>
    <velocity> -0.00005389 0.00000000 -0.00000000 </velocity>
    <force> -0.00398368 0.00000000 -0.00000001 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000006 2.37974774 0.00000168 </position>
    <velocity> -0.00000000 0.00004886 0.00000000 </velocity>
    <force> 0.00000000 -0.01306717 0.00000001 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69518487 -0.00000006 -0.00000130 </position>
    <velocity> 0.00005389 -0.00000000 -0.00000000 </velocity>
    <force> 0.00398368 -0.00000000 -0.00000001 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.37974775 0.00000115 </position>
    <velocity> -0.00000000 -0.00004886 0.00000000 </velocity>
    <force> 0.00000000 0.01306717 0.00000001 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294544 </econst>
  <ekin_ion> 0.00027089 </ekin_ion>
  <temp_ion> 14.25741531 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31619350 </eigenvalue_sum>
  <etotal_int>     -15.37318710 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31587655 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92048730 (0.92048730)
  <etotal_int>     -15.37318729 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31558246 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06066868 (0.06066868)
  <etotal_int>     -15.37318736 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31556782 </eigenvalue_sum>
  Anderson extrapolation: theta=1.79838775 (1.79838775)
  <etotal_int>     -15.37318736 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31554775 </eigenvalue_sum>
  Anderson extrapolation: theta=0.25027591 (0.25027591)
  <etotal_int>     -15.37318737 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="41">
  total_electronic_charge: 16.00000000
  <ekin>         5.22661744 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40713997 </eps>
  <enl>          4.76917478 </enl>
  <ecoul>      -15.59897396 </ecoul>
  <exc>         -4.36286567 </exc>
  <esr>          0.05447567 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318737 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318737 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69296697 0.00000007 -0.00000142 </position>
    <velocity> -0.00005689 0.00000000 -0.00000000 </velocity>
    <force> -0.00370597 0.00000000 -0.00000003 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000006 2.38149781 0.00000173 </position>
    <velocity> -0.00000000 0.00003859 0.00000000 </velocity>
    <force> 0.00000000 -0.01321411 0.00000002 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69296699 -0.00000006 -0.00000134 </position>
    <velocity> 0.00005689 -0.00000000 -0.00000000 </velocity>
    <force> 0.00370597 -0.00000000 -0.00000003 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38149782 0.00000118 </position>
    <velocity> -0.00000000 -0.00003859 0.00000000 </velocity>
    <force> 0.00000000 0.01321411 0.00000003 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294541 </econst>
  <ekin_ion> 0.00024196 </ekin_ion>
  <temp_ion> 12.73499471 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31634070 </eigenvalue_sum>
  <etotal_int>     -15.37316821 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31602564 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92174813 (0.92174813)
  <etotal_int>     -15.37316839 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31573317 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06129395 (0.06129395)
  <etotal_int>     -15.37316846 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31571864 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80144977 (1.80144977)
  <etotal_int>     -15.37316847 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31569877 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24986763 (0.24986763)
  <etotal_int>     -15.37316847 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="42">
  total_electronic_charge: 16.00000000
  <ekin>         5.22738356 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40774859 </eps>
  <enl>          4.76939562 </enl>
  <ecoul>      -15.59904310 </ecoul>
  <exc>         -4.36315596 </exc>
  <esr>          0.05458729 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316847 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316847 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69063328 0.00000007 -0.00000146 </position>
    <velocity> -0.00005967 0.00000000 -0.00000000 </velocity>
    <force> -0.00339421 0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000006 2.38283491 0.00000178 </position>
    <velocity> -0.00000000 0.00002823 0.00000000 </velocity>
    <force> 0.00000000 -0.01330134 0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69063330 -0.00000007 -0.00000138 </position>
    <velocity> 0.00005967 -0.00000000 -0.00000000 </velocity>
    <force> 0.00339421 -0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38283492 0.00000122 </position>
    <velocity> -0.00000000 -0.00002823 0.00000000 </velocity>
    <force> 0.00000000 0.01330134 0.00000004 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294539 </econst>
  <ekin_ion> 0.00022308 </ekin_ion>
  <temp_ion> 11.74112544 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31659726 </eigenvalue_sum>
  <etotal_int>     -15.37315938 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31628574 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92316145 (0.92316145)
  <etotal_int>     -15.37315956 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31599644 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06200057 (0.06200057)
  <etotal_int>     -15.37315963 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31598213 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80403377 (1.80403377)
  <etotal_int>     -15.37315964 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31596261 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24930809 (0.24930809)
  <etotal_int>     -15.37315965 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="43">
  total_electronic_charge: 16.00000000
  <ekin>         5.22849237 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40856234 </eps>
  <enl>          4.76963525 </enl>
  <ecoul>      -15.59913422 </ecoul>
  <exc>         -4.36359072 </exc>
  <esr>          0.05474687 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315965 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315965 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68819351 0.00000008 -0.00000150 </position>
    <velocity> -0.00006219 0.00000000 -0.00000000 </velocity>
    <force> -0.00304936 -0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000006 2.38375632 0.00000182 </position>
    <velocity> -0.00000000 0.00001783 0.00000000 </velocity>
    <force> 0.00000000 -0.01332913 0.00000005 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68819353 -0.00000007 -0.00000142 </position>
    <velocity> 0.00006219 -0.00000000 -0.00000000 </velocity>
    <force> 0.00304935 -0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38375633 0.00000125 </position>
    <velocity> -0.00000000 -0.00001783 0.00000000 </velocity>
    <force> 0.00000000 0.01332913 0.00000005 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294539 </econst>
  <ekin_ion> 0.00021425 </ekin_ion>
  <temp_ion> 11.27647466 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31696151 </eigenvalue_sum>
  <etotal_int>     -15.37316044 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31665516 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92477820 (0.92477820)
  <etotal_int>     -15.37316062 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31637057 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06280495 (0.06280495)
  <etotal_int>     -15.37316069 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31635657 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80604677 (1.80604677)
  <etotal_int>     -15.37316069 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31633756 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24857753 (0.24857753)
  <etotal_int>     -15.37316070 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="44">
  total_electronic_charge: 16.00000000
  <ekin>         5.22993767 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40957781 </eps>
  <enl>          4.76989353 </enl>
  <ecoul>      -15.59924672 </ecoul>
  <exc>         -4.36416736 </exc>
  <esr>          0.05495372 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316070 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316070 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68565844 0.00000008 -0.00000154 </position>
    <velocity> -0.00006442 0.00000000 -0.00000000 </velocity>
    <force> -0.00267253 -0.00000000 -0.00000006 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000006 2.38426117 0.00000187 </position>
    <velocity> -0.00000000 0.00000743 0.00000000 </velocity>
    <force> 0.00000000 -0.01329788 0.00000006 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68565846 -0.00000007 -0.00000146 </position>
    <velocity> 0.00006442 -0.00000000 -0.00000000 </velocity>
    <force> 0.00267253 -0.00000000 -0.00000006 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38426118 0.00000129 </position>
    <velocity> -0.00000000 -0.00000743 0.00000000 </velocity>
    <force> 0.00000000 0.01329789 0.00000006 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294541 </econst>
  <ekin_ion> 0.00021529 </ekin_ion>
  <temp_ion> 11.33118208 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31743127 </eigenvalue_sum>
  <etotal_int>     -15.37317101 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31713172 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92666484 (0.92666484)
  <etotal_int>     -15.37317118 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31685334 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06372763 (0.06372763)
  <etotal_int>     -15.37317125 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31683975 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80735395 (1.80735395)
  <etotal_int>     -15.37317125 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31682141 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24765217 (0.24765217)
  <etotal_int>     -15.37317126 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="45">
  total_electronic_charge: 16.00000000
  <ekin>         5.23171171 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41079083 </eps>
  <enl>          4.77017028 </enl>
  <ecoul>      -15.59937980 </ecoul>
  <exc>         -4.36488262 </exc>
  <esr>          0.05520698 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317126 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317126 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68303985 0.00000008 -0.00000159 </position>
    <velocity> -0.00006635 0.00000000 -0.00000000 </velocity>
    <force> -0.00226504 -0.00000000 -0.00000006 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000006 2.38435043 0.00000193 </position>
    <velocity> -0.00000000 -0.00000293 0.00000000 </velocity>
    <force> 0.00000000 -0.01320809 0.00000006 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68303987 -0.00000007 -0.00000150 </position>
    <velocity> 0.00006635 -0.00000000 -0.00000000 </velocity>
    <force> 0.00226504 -0.00000000 -0.00000006 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38435044 0.00000133 </position>
    <velocity> -0.00000000 0.00000293 0.00000000 </velocity>
    <force> 0.00000000 0.01320809 0.00000006 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294544 </econst>
  <ekin_ion> 0.00022582 </ekin_ion>
  <temp_ion> 11.88535044 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31800387 </eigenvalue_sum>
  <etotal_int>     -15.37319052 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31771271 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92890868 (0.92890868)
  <etotal_int>     -15.37319069 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31744203 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06479445 (0.06479445)
  <etotal_int>     -15.37319075 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31742895 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80776605 (1.80776605)
  <etotal_int>     -15.37319076 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31741145 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24650443 (0.24650443)
  <etotal_int>     -15.37319076 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="46">
  total_electronic_charge: 16.00000000
  <ekin>         5.23380522 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41219643 </eps>
  <enl>          4.77046532 </enl>
  <ecoul>      -15.59953239 </ecoul>
  <exc>         -4.36573249 </exc>
  <esr>          0.05550566 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319076 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319076 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68035047 0.00000008 -0.00000163 </position>
    <velocity> -0.00006795 0.00000000 -0.00000000 </velocity>
    <force> -0.00182835 -0.00000000 -0.00000006 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000006 2.38402692 0.00000198 </position>
    <velocity> -0.00000000 -0.00001319 0.00000000 </velocity>
    <force> 0.00000000 -0.01306035 0.00000005 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68035049 -0.00000007 -0.00000155 </position>
    <velocity> 0.00006795 -0.00000000 -0.00000000 </velocity>
    <force> 0.00182835 -0.00000000 -0.00000006 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38402692 0.00000138 </position>
    <velocity> -0.00000000 0.00001319 0.00000000 </velocity>
    <force> 0.00000000 0.01306035 0.00000006 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294548 </econst>
  <ekin_ion> 0.00024528 </ekin_ion>
  <temp_ion> 12.90970369 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31867614 </eigenvalue_sum>
  <etotal_int>     -15.37321826 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31839496 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93162542 (0.93162542)
  <etotal_int>     -15.37321842 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31813343 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06603794 (0.06603794)
  <etotal_int>     -15.37321848 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31812096 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80702199 (1.80702199)
  <etotal_int>     -15.37321849 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31810445 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24510343 (0.24510343)
  <etotal_int>     -15.37321849 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="47">
  total_electronic_charge: 16.00000000
  <ekin>         5.23620739 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41378878 </eps>
  <enl>          4.77077841 </enl>
  <ecoul>      -15.59970323 </ecoul>
  <exc>         -4.36671230 </exc>
  <esr>          0.05584858 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321849 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321849 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67760396 0.00000008 -0.00000168 </position>
    <velocity> -0.00006920 0.00000000 -0.00000000 </velocity>
    <force> -0.00136415 -0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000007 2.38329524 0.00000203 </position>
    <velocity> -0.00000000 -0.00002331 0.00000000 </velocity>
    <force> 0.00000000 -0.01285542 0.00000005 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67760398 -0.00000008 -0.00000160 </position>
    <velocity> 0.00006920 -0.00000000 -0.00000000 </velocity>
    <force> 0.00136415 -0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38329524 0.00000142 </position>
    <velocity> 0.00000000 0.00002331 0.00000000 </velocity>
    <force> 0.00000000 0.01285542 0.00000006 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294553 </econst>
  <ekin_ion> 0.00027296 </ekin_ion>
  <temp_ion> 14.36640199 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31944443 </eigenvalue_sum>
  <etotal_int>     -15.37325337 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31917478 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93497027 (0.93497027)
  <etotal_int>     -15.37325352 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31892383 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06749913 (0.06749913)
  <etotal_int>     -15.37325357 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31891206 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80476558 (1.80476558)
  <etotal_int>     -15.37325358 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31889671 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24341622 (0.24341622)
  <etotal_int>     -15.37325358 </etotal_int>
  <timing name="iteration" min="    0.034" max="    0.034"/>
</iteration>
<iteration count="48">
  total_electronic_charge: 16.00000000
  <ekin>         5.23890588 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41556120 </eps>
  <enl>          4.77110925 </enl>
  <ecoul>      -15.59989086 </ecoul>
  <exc>         -4.36781665 </exc>
  <esr>          0.05623442 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325358 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325358 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67481481 0.00000009 -0.00000173 </position>
    <velocity> -0.00007007 0.00000000 -0.00000000 </velocity>
    <force> -0.00087430 -0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000007 2.38216181 0.00000209 </position>
    <velocity> -0.00000000 -0.00003326 0.00000000 </velocity>
    <force> 0.00000000 -0.01259415 0.00000005 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67481483 -0.00000008 -0.00000165 </position>
    <velocity> 0.00007007 -0.00000000 -0.00000000 </velocity>
    <force> 0.00087429 -0.00000000 -0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38216181 0.00000147 </position>
    <velocity> 0.00000000 0.00003326 0.00000000 </velocity>
    <force> 0.00000000 0.01259415 0.00000005 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294560 </econst>
  <ekin_ion> 0.00030799 </ekin_ion>
  <temp_ion> 16.21000099 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32030461 </eigenvalue_sum>
  <etotal_int>     -15.37329485 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32004801 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93915428 (0.93915428)
  <etotal_int>     -15.37329498 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31980900 </eigenvalue_sum>
  Anderson extrapolation: theta=0.06922961 (0.06922961)
  <etotal_int>     -15.37329504 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31979803 </eigenvalue_sum>
  Anderson extrapolation: theta=1.80051481 (1.80051481)
  <etotal_int>     -15.37329504 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.31978402 </eigenvalue_sum>
  Anderson extrapolation: theta=0.24141015 (0.24141015)
  <etotal_int>     -15.37329505 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="49">
  total_electronic_charge: 16.00000000
  <ekin>         5.24188681 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41750611 </eps>
  <enl>          4.77145739 </enl>
  <ecoul>      -15.60009363 </ecoul>
  <exc>         -4.36903950 </exc>
  <esr>          0.05666165 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37329505 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37329505 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67199833 0.00000009 -0.00000179 </position>
    <velocity> -0.00007055 0.00000000 -0.00000000 </velocity>
    <force> -0.00036088 -0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000007 2.38063478 0.00000215 </position>
    <velocity> -0.00000000 -0.00004297 0.00000000 </velocity>
    <force> 0.00000000 -0.01227756 0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67199836 -0.00000008 -0.00000170 </position>
    <velocity> 0.00007055 -0.00000000 -0.00000000 </velocity>
    <force> 0.00036087 -0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.38063478 0.00000151 </position>
    <velocity> 0.00000000 0.00004297 0.00000000 </velocity>
    <force> 0.00000000 0.01227756 0.00000005 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294567 </econst>
  <ekin_ion> 0.00034938 </ekin_ion>
  <temp_ion> 18.38854061 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32125205 </eigenvalue_sum>
  <etotal_int>     -15.37334161 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32100998 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94446912 (0.94446912)
  <etotal_int>     -15.37334173 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32078423 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07129375 (0.07129375)
  <etotal_int>     -15.37334178 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32077418 </eigenvalue_sum>
  Anderson extrapolation: theta=1.79362300 (1.79362300)
  <etotal_int>     -15.37334179 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32076166 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23905723 (0.23905723)
  <etotal_int>     -15.37334179 </etotal_int>
  <timing name="iteration" min="    0.033" max="    0.033"/>
</iteration>
<iteration count="50">
  total_electronic_charge: 16.00000000
  <ekin>         5.24513476 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41961499 </eps>
  <enl>          4.77182229 </enl>
  <ecoul>      -15.60030974 </ecoul>
  <exc>         -4.37037412 </exc>
  <esr>          0.05712855 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37334179 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37334179 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66917058 0.00000009 -0.00000184 </position>
    <velocity> -0.00007063 0.00000000 -0.00000000 </velocity>
    <force> 0.00017382 -0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000007 2.37872405 0.00000221 </position>
    <velocity> -0.00000000 -0.00005242 0.00000000 </velocity>
    <force> 0.00000000 -0.01190680 0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66917061 -0.00000008 -0.00000175 </position>
    <velocity> 0.00007063 -0.00000000 -0.00000000 </velocity>
    <force> -0.00017382 -0.00000000 -0.00000004 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000002 -2.37872406 0.00000156 </position>
    <velocity> 0.00000000 0.00005242 0.00000000 </velocity>
    <force> 0.00000000 0.01190680 0.00000004 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <econst> -15.37294575 </econst>
  <ekin_ion> 0.00039605 </ekin_ion>
  <temp_ion> 20.84474711 </temp_ion>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32228167 </eigenvalue_sum>
  <etotal_int>     -15.37339249 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32205554 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95132499 (0.95132499)
  <etotal_int>     -15.37339260 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32184435 </eigenvalue_sum>
  Anderson extrapolation: theta=0.07377042 (0.07377042)
  <etotal_int>     -15.37339265 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32183530 </eigenvalue_sum>
  Anderson extrapolation: theta=1.78323353 (1.78323353)
  <etotal_int>     -15.37339265 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.32182445 </eigenvalue_sum>
  Anderson extrapolation: theta=0.23634144 (0.23634144)
  <etotal_int>     -15.37339266 </etotal_int>
  <timing name="iteration" min="    0.039" max="    0.039"/>
</iteration>
  total_electronic_charge: 16.00000000
  total_electronic_charge: 16.00000000
<timing name="          align" min="    0.010" max="    0.031"/>
<timing name="         charge" min="    0.413" max="    0.448"/>
<timing name="         energy" min="    0.552" max="    0.570"/>
<timing name="           gram" min="    0.000" max="    0.001"/>
<timing name="         lowdin" min="    0.010" max="    0.010"/>
<timing name="    ortho_align" min="    0.054" max="    0.076"/>
<timing name="      psda_prec" min="    0.004" max="    0.004"/>
<timing name="  psda_residual" min="    0.015" max="    0.047"/>
<timing name=" psda_update_wf" min="    0.005" max="    0.027"/>
<timing name="    update_vhxc" min="    0.387" max="    0.406"/>
<timing name="      wf_update" min="    0.116" max="    0.147"/>
<timing name="           ekin" min="    0.016" max="    0.035"/>
<timing name="            exc" min="    0.249" max="    0.262"/>
<timing name="           hpsi" min="    0.434" max="    0.443"/>
<timing name="       nonlocal" min="    0.086" max="    0.094"/>
<timing name=" charge_compute" min="    0.274" max="    0.297"/>
<timing name="charge_integral" min="    0.015" max="    0.034"/>
<timing name="  charge_rowsum" min="    0.003" max="    0.006"/>
<timing name="     charge_vft" min="    0.095" max="    0.127"/>
[qbox]  End of command stream 
<real_time> 1.814 </real_time>
<end_time> 2016-04-06T12:25:25Z </end_time>
</fpmd:simulation>
