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
<start_time> 2016-04-06T12:25:25Z </start_time>
<mpi_processes count="4">
<process id="0"> theobook68 </process>
<process id="1"> theobook68 </process>
<process id="2"> theobook68 </process>
<process id="3"> theobook68 </process>
</mpi_processes>
[qbox] <cmd># Si4 CP dynamics</cmd>
[qbox] <cmd>load ../si4gs/test.xml</cmd>
 LoadCmd: loading from ../si4gs/test.xml
 XMLGFPreprocessor: reading from ../si4gs/test.xml size: 357985
 XMLGFPreprocessor: read time: 9.799e-05
 XMLGFPreprocessor: local read rate: 871 MB/s  aggregate read rate: 3484 MB/s
 XMLGFPreprocessor: tag fixing time: 7.296e-05
 XMLGFPreprocessor: segment definition time: 0.001894
 XMLGFPreprocessor: boundary adjustment time: 2.861e-06
 XMLGFPreprocessor: transcoding time: 3.099e-06
 XMLGFPreprocessor: data redistribution time: 0.0007331
 XMLGFPreprocessor: XML compacting time: 0.0001621
 XMLGFPreprocessor: total time: 0.003486
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
 SampleReader: read time: 0.02955 s
[qbox] <cmd>set wf_dyn MD</cmd>
[qbox] <cmd>set atoms_dyn MD</cmd>
[qbox] <cmd>set dt 4</cmd>
[qbox] <cmd>run 500</cmd>
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
  total_electronic_charge: 16.00000000
<iteration count="1">
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
    <position> 3.70000044 0.00000000 -0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00284355 0.00000008 -0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20000267 0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000007 0.01705782 0.00000183 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000044 -0.00000000 -0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00284366 -0.00000006 -0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20000267 0.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000009 -0.01705783 0.00000110 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000000 </ekin_e>
  <ekin_ion> 0.00000000 </ekin_ion>
  <temp_ion> 0.00000000 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294516 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="2">
  <ekin>         5.34839630 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48138420 </eps>
  <enl>          4.77521419 </enl>
  <ecoul>      -15.60248522 </ecoul>
  <exc>         -4.41268632 </exc>
  <esr>          0.07326840 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294525 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294525 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000178 0.00000000 -0.00000000 </position>
    <velocity> 0.00000022 0.00000000 -0.00000000 </velocity>
    <force> 0.00284160 0.00000008 -0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20001066 0.00000000 </position>
    <velocity> -0.00000000 0.00000133 0.00000000 </velocity>
    <force> -0.00000007 0.01705356 0.00000182 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000178 -0.00000000 -0.00000000 </position>
    <velocity> -0.00000022 -0.00000000 -0.00000000 </velocity>
    <force> -0.00284170 -0.00000006 -0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20001066 0.00000000 </position>
    <velocity> 0.00000000 -0.00000133 0.00000000 </velocity>
    <force> 0.00000009 -0.01705358 0.00000110 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000000 </ekin_e>
  <ekin_ion> 0.00000009 </ekin_ion>
  <temp_ion> 0.00491772 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294516 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="3">
  <ekin>         5.34839590 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48138251 </eps>
  <enl>          4.77521527 </enl>
  <ecoul>      -15.60248805 </ecoul>
  <exc>         -4.41268615 </exc>
  <esr>          0.07326719 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294553 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294553 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000400 0.00000000 -0.00000000 </position>
    <velocity> 0.00000044 0.00000000 -0.00000000 </velocity>
    <force> 0.00283612 0.00000007 -0.00000140 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20002398 0.00000000 </position>
    <velocity> -0.00000000 0.00000266 0.00000000 </velocity>
    <force> -0.00000007 0.01704156 0.00000180 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000400 -0.00000000 -0.00000000 </position>
    <velocity> -0.00000044 -0.00000000 -0.00000000 </velocity>
    <force> -0.00283623 -0.00000005 -0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20002398 0.00000000 </position>
    <velocity> 0.00000000 -0.00000266 0.00000000 </velocity>
    <force> 0.00000009 -0.01704158 0.00000109 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000000 </ekin_e>
  <ekin_ion> 0.00000037 </ekin_ion>
  <temp_ion> 0.01966106 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294516 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="4">
  <ekin>         5.34839398 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48137878 </eps>
  <enl>          4.77521630 </enl>
  <ecoul>      -15.60249216 </ecoul>
  <exc>         -4.41268534 </exc>
  <esr>          0.07326517 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294600 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294600 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000710 0.00000000 -0.00000000 </position>
    <velocity> 0.00000067 0.00000000 -0.00000000 </velocity>
    <force> 0.00282818 0.00000007 -0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20004262 0.00000000 </position>
    <velocity> -0.00000000 0.00000400 0.00000000 </velocity>
    <force> -0.00000006 0.01702392 0.00000176 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000710 -0.00000000 -0.00000000 </position>
    <velocity> -0.00000067 -0.00000000 -0.00000000 </velocity>
    <force> -0.00282827 -0.00000005 -0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20004262 0.00000000 </position>
    <velocity> 0.00000000 -0.00000400 0.00000000 </velocity>
    <force> 0.00000009 -0.01702394 0.00000108 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000000 </ekin_e>
  <ekin_ion> 0.00000084 </ekin_ion>
  <temp_ion> 0.04420321 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294516 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="5">
  <ekin>         5.34838889 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48137188 </eps>
  <enl>          4.77521625 </enl>
  <ecoul>      -15.60249672 </ecoul>
  <exc>         -4.41268320 </exc>
  <esr>          0.07326235 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294665 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294665 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70001108 0.00000000 -0.00000001 </position>
    <velocity> 0.00000089 0.00000000 -0.00000000 </velocity>
    <force> 0.00281924 0.00000007 -0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20006658 0.00000001 </position>
    <velocity> -0.00000000 0.00000532 0.00000000 </velocity>
    <force> -0.00000006 0.01700359 0.00000170 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70001108 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000089 -0.00000000 -0.00000000 </velocity>
    <force> -0.00281933 -0.00000005 -0.00000125 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20006658 0.00000000 </position>
    <velocity> 0.00000000 -0.00000532 0.00000000 </velocity>
    <force> 0.00000008 -0.01700360 0.00000106 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000000 </ekin_e>
  <ekin_ion> 0.00000149 </ekin_ion>
  <temp_ion> 0.07850738 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294516 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="6">
  <ekin>         5.34837879 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48136050 </eps>
  <enl>          4.77521403 </enl>
  <ecoul>      -15.60250084 </ecoul>
  <exc>         -4.41267898 </exc>
  <esr>          0.07325872 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294749 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294749 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70001594 0.00000000 -0.00000001 </position>
    <velocity> 0.00000111 0.00000000 -0.00000000 </velocity>
    <force> 0.00281087 0.00000006 -0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20009584 0.00000001 </position>
    <velocity> -0.00000000 0.00000665 0.00000000 </velocity>
    <force> -0.00000006 0.01698363 0.00000163 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70001594 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000111 -0.00000000 -0.00000000 </velocity>
    <force> -0.00281095 -0.00000005 -0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20009584 0.00000001 </position>
    <velocity> 0.00000000 -0.00000665 0.00000000 </velocity>
    <force> 0.00000007 -0.01698364 0.00000103 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000000 </ekin_e>
  <ekin_ion> 0.00000233 </ekin_ion>
  <temp_ion> 0.12253600 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294516 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="7">
  <ekin>         5.34836196 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48134350 </eps>
  <enl>          4.77520870 </enl>
  <ecoul>      -15.60250366 </ecoul>
  <exc>         -4.41267201 </exc>
  <esr>          0.07325429 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294851 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294851 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70002168 0.00000000 -0.00000001 </position>
    <velocity> 0.00000133 0.00000000 -0.00000000 </velocity>
    <force> 0.00280436 0.00000006 -0.00000127 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20013041 0.00000001 </position>
    <velocity> -0.00000000 0.00000798 0.00000000 </velocity>
    <force> -0.00000005 0.01696657 0.00000155 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70002168 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000133 -0.00000000 -0.00000000 </velocity>
    <force> -0.00280443 -0.00000004 -0.00000116 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20013041 0.00000001 </position>
    <velocity> 0.00000000 -0.00000798 0.00000000 </velocity>
    <force> 0.00000007 -0.01696657 0.00000100 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000001 </ekin_e>
  <ekin_ion> 0.00000335 </ekin_ion>
  <temp_ion> 0.17625905 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294515 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="8">
  <ekin>         5.34833710 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48132015 </eps>
  <enl>          4.77519973 </enl>
  <ecoul>      -15.60250458 </ecoul>
  <exc>         -4.41266182 </exc>
  <esr>          0.07324906 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294972 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294972 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70002830 0.00000000 -0.00000001 </position>
    <velocity> 0.00000154 0.00000000 -0.00000000 </velocity>
    <force> 0.00280046 0.00000005 -0.00000120 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20017027 0.00000002 </position>
    <velocity> -0.00000000 0.00000930 0.00000000 </velocity>
    <force> -0.00000004 0.01695386 0.00000145 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70002830 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000154 -0.00000000 -0.00000000 </velocity>
    <force> -0.00280052 -0.00000004 -0.00000110 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20017027 0.00000001 </position>
    <velocity> 0.00000000 -0.00000930 0.00000000 </velocity>
    <force> 0.00000006 -0.01695387 0.00000096 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000001 </ekin_e>
  <ekin_ion> 0.00000455 </ekin_ion>
  <temp_ion> 0.23965910 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294515 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="9">
  <ekin>         5.34830356 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48129028 </eps>
  <enl>          4.77518715 </enl>
  <ecoul>      -15.60250332 </ecoul>
  <exc>         -4.41264823 </exc>
  <esr>          0.07324303 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37295112 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37295112 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70003578 0.00000000 -0.00000002 </position>
    <velocity> 0.00000176 0.00000000 -0.00000000 </velocity>
    <force> 0.00279925 0.00000004 -0.00000112 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20021543 0.00000002 </position>
    <velocity> -0.00000000 0.00001063 0.00000000 </velocity>
    <force> -0.00000003 0.01694569 0.00000134 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70003579 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000176 -0.00000000 -0.00000000 </velocity>
    <force> -0.00279929 -0.00000003 -0.00000103 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20021543 0.00000001 </position>
    <velocity> 0.00000000 -0.00001063 0.00000000 </velocity>
    <force> 0.00000004 -0.01694570 0.00000091 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000002 </ekin_e>
  <ekin_ion> 0.00000594 </ekin_ion>
  <temp_ion> 0.31273166 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294514 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="10">
  <ekin>         5.34826141 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48125440 </eps>
  <enl>          4.77517163 </enl>
  <ecoul>      -15.60250001 </ecoul>
  <exc>         -4.41263132 </exc>
  <esr>          0.07323620 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37295269 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37295269 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70004415 0.00000000 -0.00000002 </position>
    <velocity> 0.00000198 0.00000000 -0.00000000 </velocity>
    <force> 0.00280016 0.00000003 -0.00000102 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20026588 0.00000003 </position>
    <velocity> -0.00000000 0.00001195 0.00000000 </velocity>
    <force> -0.00000002 0.01694106 0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70004415 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000198 -0.00000000 -0.00000000 </velocity>
    <force> -0.00280018 -0.00000002 -0.00000096 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20026588 0.00000002 </position>
    <velocity> 0.00000000 -0.00001195 0.00000000 </velocity>
    <force> 0.00000003 -0.01694106 0.00000086 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000002 </ekin_e>
  <ekin_ion> 0.00000751 </ekin_ion>
  <temp_ion> 0.39548090 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294514 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="11">
  <ekin>         5.34821137 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48121360 </eps>
  <enl>          4.77515439 </enl>
  <ecoul>      -15.60249514 </ecoul>
  <exc>         -4.41261147 </exc>
  <esr>          0.07322857 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37295446 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37295446 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70005339 0.00000000 -0.00000003 </position>
    <velocity> 0.00000220 0.00000000 -0.00000000 </velocity>
    <force> 0.00280214 0.00000002 -0.00000092 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20032163 0.00000003 </position>
    <velocity> -0.00000000 0.00001328 0.00000000 </velocity>
    <force> -0.00000002 0.01693816 0.00000109 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70005339 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000220 -0.00000000 -0.00000000 </velocity>
    <force> -0.00280215 -0.00000002 -0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20032163 0.00000002 </position>
    <velocity> 0.00000000 -0.00001328 0.00000000 </velocity>
    <force> 0.00000002 -0.01693816 0.00000081 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000003 </ekin_e>
  <ekin_ion> 0.00000927 </ekin_ion>
  <temp_ion> 0.48791225 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294513 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="12">
  <ekin>         5.34815465 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48116939 </eps>
  <enl>          4.77513700 </enl>
  <ecoul>      -15.60248948 </ecoul>
  <exc>         -4.41258919 </exc>
  <esr>          0.07322014 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37295640 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37295640 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70006350 0.00000000 -0.00000003 </position>
    <velocity> 0.00000242 0.00000000 -0.00000000 </velocity>
    <force> 0.00280392 0.00000001 -0.00000081 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20038267 0.00000004 </position>
    <velocity> -0.00000000 0.00001460 0.00000000 </velocity>
    <force> -0.00000001 0.01693486 0.00000094 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70006351 -0.00000000 -0.00000003 </position>
    <velocity> -0.00000242 -0.00000000 -0.00000000 </velocity>
    <force> -0.00280391 -0.00000001 -0.00000078 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20038267 0.00000002 </position>
    <velocity> 0.00000000 -0.00001460 0.00000000 </velocity>
    <force> 0.00000001 -0.01693486 0.00000074 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000004 </ekin_e>
  <ekin_ion> 0.00001121 </ekin_ion>
  <temp_ion> 0.59002436 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294512 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="13">
  <ekin>         5.34809270 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48112337 </eps>
  <enl>          4.77512109 </enl>
  <ecoul>      -15.60248391 </ecoul>
  <exc>         -4.41256504 </exc>
  <esr>          0.07321091 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37295853 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37295853 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70007450 0.00000000 -0.00000003 </position>
    <velocity> 0.00000264 0.00000000 -0.00000000 </velocity>
    <force> 0.00280428 -0.00000000 -0.00000070 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20044900 0.00000004 </position>
    <velocity> -0.00000000 0.00001592 0.00000000 </velocity>
    <force> 0.00000000 0.01692921 0.00000079 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70007450 -0.00000000 -0.00000003 </position>
    <velocity> -0.00000264 -0.00000000 -0.00000000 </velocity>
    <force> -0.00280426 -0.00000000 -0.00000068 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20044900 0.00000003 </position>
    <velocity> 0.00000000 -0.00001592 0.00000000 </velocity>
    <force> -0.00000001 -0.01692920 0.00000068 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000004 </ekin_e>
  <ekin_ion> 0.00001333 </ekin_ion>
  <temp_ion> 0.70180243 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294512 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="14">
  <ekin>         5.34802690 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48107695 </eps>
  <enl>          4.77510800 </enl>
  <ecoul>      -15.60247925 </ecoul>
  <exc>         -4.41253955 </exc>
  <esr>          0.07320088 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37296085 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37296085 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70008636 0.00000000 -0.00000004 </position>
    <velocity> 0.00000286 0.00000000 -0.00000000 </velocity>
    <force> 0.00280231 -0.00000001 -0.00000059 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20052062 0.00000005 </position>
    <velocity> -0.00000000 0.00001724 0.00000000 </velocity>
    <force> 0.00000001 0.01691980 0.00000063 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70008637 -0.00000000 -0.00000004 </position>
    <velocity> -0.00000286 -0.00000000 -0.00000000 </velocity>
    <force> -0.00280227 0.00000001 -0.00000058 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20052062 0.00000003 </position>
    <velocity> 0.00000000 -0.00001724 0.00000000 </velocity>
    <force> -0.00000002 -0.01691979 0.00000061 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000005 </ekin_e>
  <ekin_ion> 0.00001564 </ekin_ion>
  <temp_ion> 0.82321485 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294511 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="15">
  <ekin>         5.34795834 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48103103 </eps>
  <enl>          4.77509855 </enl>
  <ecoul>      -15.60247614 </ecoul>
  <exc>         -4.41251307 </exc>
  <esr>          0.07319006 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37296334 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37296334 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70009911 0.00000000 -0.00000004 </position>
    <velocity> 0.00000308 0.00000000 -0.00000000 </velocity>
    <force> 0.00279753 -0.00000002 -0.00000048 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20059752 0.00000005 </position>
    <velocity> -0.00000000 0.00001857 0.00000000 </velocity>
    <force> 0.00000002 0.01690600 0.00000047 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70009911 -0.00000000 -0.00000004 </position>
    <velocity> -0.00000308 -0.00000000 -0.00000000 </velocity>
    <force> -0.00279747 0.00000001 -0.00000047 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20059752 0.00000003 </position>
    <velocity> 0.00000000 -0.00001857 0.00000000 </velocity>
    <force> -0.00000003 -0.01690599 0.00000054 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000005 </ekin_e>
  <ekin_ion> 0.00001813 </ekin_ion>
  <temp_ion> 0.95421363 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294511 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="16">
  <ekin>         5.34788763 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48098583 </eps>
  <enl>          4.77509284 </enl>
  <ecoul>      -15.60247488 </ecoul>
  <exc>         -4.41248578 </exc>
  <esr>          0.07317844 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37296602 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37296602 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70011272 0.00000000 -0.00000005 </position>
    <velocity> 0.00000329 0.00000000 -0.00000000 </velocity>
    <force> 0.00278996 -0.00000003 -0.00000036 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20067970 0.00000006 </position>
    <velocity> -0.00000000 0.00001989 0.00000000 </velocity>
    <force> 0.00000003 0.01688790 0.00000031 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70011272 -0.00000000 -0.00000005 </position>
    <velocity> -0.00000329 -0.00000000 -0.00000000 </velocity>
    <force> -0.00278989 0.00000002 -0.00000036 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20067970 0.00000004 </position>
    <velocity> 0.00000000 -0.00001989 0.00000000 </velocity>
    <force> -0.00000004 -0.01688789 0.00000046 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000006 </ekin_e>
  <ekin_ion> 0.00002080 </ekin_ion>
  <temp_ion> 1.09473821 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294510 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="17">
  <ekin>         5.34781485 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48094092 </eps>
  <enl>          4.77509026 </enl>
  <ecoul>      -15.60247544 </ecoul>
  <exc>         -4.41245763 </exc>
  <esr>          0.07316602 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37296887 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37296887 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70012720 0.00000000 -0.00000005 </position>
    <velocity> 0.00000351 0.00000000 -0.00000000 </velocity>
    <force> 0.00278010 -0.00000004 -0.00000024 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20076715 0.00000007 </position>
    <velocity> -0.00000000 0.00002120 0.00000000 </velocity>
    <force> 0.00000003 0.01686624 0.00000014 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70012721 -0.00000000 -0.00000005 </position>
    <velocity> -0.00000351 -0.00000000 -0.00000000 </velocity>
    <force> -0.00278001 0.00000003 -0.00000025 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20076715 0.00000004 </position>
    <velocity> 0.00000000 -0.00002120 0.00000000 </velocity>
    <force> -0.00000005 -0.01686623 0.00000038 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000007 </ekin_e>
  <ekin_ion> 0.00002365 </ekin_ion>
  <temp_ion> 1.24472145 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294509 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="18">
  <ekin>         5.34773959 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48089526 </eps>
  <enl>          4.77508963 </enl>
  <ecoul>      -15.60247746 </ecoul>
  <exc>         -4.41242841 </exc>
  <esr>          0.07315281 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37297191 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37297191 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70014255 0.00000000 -0.00000006 </position>
    <velocity> 0.00000373 0.00000000 -0.00000000 </velocity>
    <force> 0.00276871 -0.00000005 -0.00000012 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20085987 0.00000007 </position>
    <velocity> -0.00000000 0.00002252 0.00000000 </velocity>
    <force> 0.00000004 0.01684209 -0.00000003 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70014255 -0.00000000 -0.00000005 </position>
    <velocity> -0.00000373 -0.00000000 -0.00000000 </velocity>
    <force> -0.00276863 0.00000003 -0.00000014 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20085987 0.00000005 </position>
    <velocity> 0.00000000 -0.00002252 0.00000000 </velocity>
    <force> -0.00000006 -0.01684208 0.00000029 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000007 </ekin_e>
  <ekin_ion> 0.00002668 </ekin_ion>
  <temp_ion> 1.40409615 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294509 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="19">
  <ekin>         5.34766106 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48084752 </eps>
  <enl>          4.77508949 </enl>
  <ecoul>      -15.60248036 </ecoul>
  <exc>         -4.41239779 </exc>
  <esr>          0.07313881 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37297512 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37297512 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70015876 0.00000000 -0.00000006 </position>
    <velocity> 0.00000394 0.00000000 -0.00000000 </velocity>
    <force> 0.00275675 -0.00000006 0.00000001 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20095783 0.00000008 </position>
    <velocity> -0.00000000 0.00002384 0.00000000 </velocity>
    <force> 0.00000005 0.01681665 -0.00000019 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70015876 -0.00000000 -0.00000006 </position>
    <velocity> -0.00000394 -0.00000000 -0.00000000 </velocity>
    <force> -0.00275666 0.00000004 -0.00000003 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20095784 0.00000005 </position>
    <velocity> 0.00000000 -0.00002384 0.00000000 </velocity>
    <force> -0.00000007 -0.01681663 0.00000021 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000008 </ekin_e>
  <ekin_ion> 0.00002988 </ekin_ion>
  <temp_ion> 1.57280060 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294508 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="20">
  <ekin>         5.34757831 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48079634 </eps>
  <enl>          4.77508838 </enl>
  <ecoul>      -15.60248346 </ecoul>
  <exc>         -4.41236541 </exc>
  <esr>          0.07312402 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37297852 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37297852 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70017583 0.00000000 -0.00000007 </position>
    <velocity> 0.00000416 0.00000000 -0.00000000 </velocity>
    <force> 0.00274510 -0.00000007 0.00000013 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20106105 0.00000008 </position>
    <velocity> -0.00000000 0.00002515 0.00000000 </velocity>
    <force> 0.00000006 0.01679095 -0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70017583 -0.00000000 -0.00000006 </position>
    <velocity> -0.00000416 -0.00000000 -0.00000000 </velocity>
    <force> -0.00274500 0.00000005 0.00000008 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20106105 0.00000006 </position>
    <velocity> 0.00000000 -0.00002515 0.00000000 </velocity>
    <force> -0.00000008 -0.01679094 0.00000011 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000009 </ekin_e>
  <ekin_ion> 0.00003326 </ekin_ion>
  <temp_ion> 1.75078198 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294507 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="21">
  <ekin>         5.34749045 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48074062 </eps>
  <enl>          4.77508516 </enl>
  <ecoul>      -15.60248614 </ecoul>
  <exc>         -4.41233094 </exc>
  <esr>          0.07310844 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37298208 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37298208 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70019375 0.00000000 -0.00000007 </position>
    <velocity> 0.00000437 0.00000000 -0.00000000 </velocity>
    <force> 0.00273445 -0.00000007 0.00000026 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20116951 0.00000009 </position>
    <velocity> -0.00000000 0.00002646 0.00000000 </velocity>
    <force> 0.00000006 0.01676573 -0.00000051 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70019375 -0.00000000 -0.00000007 </position>
    <velocity> -0.00000437 -0.00000000 -0.00000000 </velocity>
    <force> -0.00273434 0.00000005 0.00000019 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20116951 0.00000006 </position>
    <velocity> 0.00000000 -0.00002646 0.00000000 </velocity>
    <force> -0.00000008 -0.01676571 0.00000002 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000010 </ekin_e>
  <ekin_ion> 0.00003682 </ekin_ion>
  <temp_ion> 1.93799712 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294505 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="22">
  <ekin>         5.34739674 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48067971 </eps>
  <enl>          4.77507922 </enl>
  <ecoul>      -15.60248794 </ecoul>
  <exc>         -4.41229414 </exc>
  <esr>          0.07309208 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37298583 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37298583 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70021252 0.00000000 -0.00000008 </position>
    <velocity> 0.00000459 0.00000000 -0.00000000 </velocity>
    <force> 0.00272517 -0.00000007 0.00000038 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20128320 0.00000010 </position>
    <velocity> -0.00000000 0.00002777 0.00000000 </velocity>
    <force> 0.00000007 0.01674130 -0.00000066 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70021253 -0.00000000 -0.00000007 </position>
    <velocity> -0.00000459 -0.00000000 -0.00000000 </velocity>
    <force> -0.00272506 0.00000005 0.00000030 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20128320 0.00000007 </position>
    <velocity> 0.00000000 -0.00002777 0.00000000 </velocity>
    <force> -0.00000009 -0.01674128 -0.00000008 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000012 </ekin_e>
  <ekin_ion> 0.00004055 </ekin_ion>
  <temp_ion> 2.13441054 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294504 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="23">
  <ekin>         5.34729680 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48061351 </eps>
  <enl>          4.77507049 </enl>
  <ecoul>      -15.60248863 </ecoul>
  <exc>         -4.41225491 </exc>
  <esr>          0.07307493 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37298975 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37298975 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70023215 0.00000000 -0.00000008 </position>
    <velocity> 0.00000480 0.00000000 -0.00000000 </velocity>
    <force> 0.00271730 -0.00000008 0.00000051 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20140211 0.00000010 </position>
    <velocity> -0.00000000 0.00002908 0.00000000 </velocity>
    <force> 0.00000007 0.01671755 -0.00000080 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70023215 -0.00000000 -0.00000008 </position>
    <velocity> -0.00000480 -0.00000000 -0.00000000 </velocity>
    <force> -0.00271719 0.00000006 0.00000041 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20140211 0.00000007 </position>
    <velocity> 0.00000000 -0.00002908 0.00000000 </velocity>
    <force> -0.00000009 -0.01671753 -0.00000017 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000013 </ekin_e>
  <ekin_ion> 0.00004446 </ekin_ion>
  <temp_ion> 2.33999035 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294503 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="24">
  <ekin>         5.34719061 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48054240 </eps>
  <enl>          4.77505946 </enl>
  <ecoul>      -15.60248822 </ecoul>
  <exc>         -4.41221329 </exc>
  <esr>          0.07305701 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37299384 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37299384 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70025262 0.00000000 -0.00000009 </position>
    <velocity> 0.00000501 0.00000000 -0.00000000 </velocity>
    <force> 0.00271054 -0.00000008 0.00000062 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20152624 0.00000011 </position>
    <velocity> -0.00000000 0.00003038 0.00000000 </velocity>
    <force> 0.00000007 0.01669402 -0.00000094 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70025262 -0.00000000 -0.00000008 </position>
    <velocity> -0.00000501 -0.00000000 -0.00000000 </velocity>
    <force> -0.00271043 0.00000006 0.00000052 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20152624 0.00000007 </position>
    <velocity> 0.00000000 -0.00003038 0.00000000 </velocity>
    <force> -0.00000009 -0.01669401 -0.00000027 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000014 </ekin_e>
  <ekin_ion> 0.00004854 </ekin_ion>
  <temp_ion> 2.55470293 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294502 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="25">
  <ekin>         5.34707846 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48046709 </eps>
  <enl>          4.77504691 </enl>
  <ecoul>      -15.60248696 </ecoul>
  <exc>         -4.41216943 </exc>
  <esr>          0.07303830 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37299811 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37299811 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70027393 0.00000000 -0.00000009 </position>
    <velocity> 0.00000522 -0.00000000 -0.00000000 </velocity>
    <force> 0.00270434 -0.00000008 0.00000074 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20165558 0.00000011 </position>
    <velocity> 0.00000000 0.00003168 0.00000000 </velocity>
    <force> 0.00000007 0.01667003 -0.00000107 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70027393 -0.00000000 -0.00000009 </position>
    <velocity> -0.00000522 -0.00000000 -0.00000000 </velocity>
    <force> -0.00270425 0.00000006 0.00000063 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20165558 0.00000008 </position>
    <velocity> -0.00000000 -0.00003168 0.00000000 </velocity>
    <force> -0.00000009 -0.01667002 -0.00000037 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000016 </ekin_e>
  <ekin_ion> 0.00005279 </ekin_ion>
  <temp_ion> 2.77850755 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294500 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="26">
  <ekin>         5.34696088 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48038845 </eps>
  <enl>          4.77503377 </enl>
  <ecoul>      -15.60248518 </ecoul>
  <exc>         -4.41212356 </exc>
  <esr>          0.07301882 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37300254 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37300254 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70029609 0.00000000 -0.00000010 </position>
    <velocity> 0.00000543 -0.00000000 -0.00000000 </velocity>
    <force> 0.00269806 -0.00000008 0.00000084 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20179012 0.00000012 </position>
    <velocity> 0.00000000 0.00003299 0.00000000 </velocity>
    <force> 0.00000007 0.01664481 -0.00000119 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70029609 -0.00000000 -0.00000009 </position>
    <velocity> -0.00000543 0.00000000 -0.00000000 </velocity>
    <force> -0.00269797 0.00000006 0.00000073 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20179012 0.00000008 </position>
    <velocity> -0.00000000 -0.00003299 0.00000000 </velocity>
    <force> -0.00000009 -0.01664480 -0.00000047 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000017 </ekin_e>
  <ekin_ion> 0.00005722 </ekin_ion>
  <temp_ion> 3.01135217 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294499 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="27">
  <ekin>         5.34683852 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48030724 </eps>
  <enl>          4.77502079 </enl>
  <ecoul>      -15.60248330 </ecoul>
  <exc>         -4.41207592 </exc>
  <esr>          0.07299856 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37300715 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37300715 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70031909 0.00000000 -0.00000010 </position>
    <velocity> 0.00000564 -0.00000000 -0.00000000 </velocity>
    <force> 0.00269102 -0.00000007 0.00000094 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20192986 0.00000012 </position>
    <velocity> 0.00000000 0.00003428 0.00000000 </velocity>
    <force> 0.00000007 0.01661770 -0.00000130 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70031909 -0.00000000 -0.00000009 </position>
    <velocity> -0.00000564 0.00000000 -0.00000000 </velocity>
    <force> -0.00269094 0.00000006 0.00000083 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20192986 0.00000009 </position>
    <velocity> -0.00000000 -0.00003428 0.00000000 </velocity>
    <force> -0.00000009 -0.01661769 -0.00000056 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000018 </ekin_e>
  <ekin_ion> 0.00006181 </ekin_ion>
  <temp_ion> 3.25317121 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294498 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="28">
  <ekin>         5.34671196 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48022396 </eps>
  <enl>          4.77500845 </enl>
  <ecoul>      -15.60248165 </ecoul>
  <exc>         -4.41202673 </exc>
  <esr>          0.07297753 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37301192 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37301192 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70034293 0.00000000 -0.00000010 </position>
    <velocity> 0.00000585 -0.00000000 -0.00000000 </velocity>
    <force> 0.00268272 -0.00000007 0.00000103 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20207478 0.00000012 </position>
    <velocity> 0.00000000 0.00003558 0.00000000 </velocity>
    <force> 0.00000006 0.01658826 -0.00000139 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70034293 -0.00000000 -0.00000010 </position>
    <velocity> -0.00000585 0.00000000 -0.00000000 </velocity>
    <force> -0.00268265 0.00000006 0.00000092 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20207478 0.00000009 </position>
    <velocity> -0.00000000 -0.00003558 0.00000000 </velocity>
    <force> -0.00000008 -0.01658825 -0.00000066 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000019 </ekin_e>
  <ekin_ion> 0.00006657 </ekin_ion>
  <temp_ion> 3.50388583 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294497 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.008"/>
<iteration count="29">
  <ekin>         5.34658168 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48013878 </eps>
  <enl>          4.77499681 </enl>
  <ecoul>      -15.60248045 </ecoul>
  <exc>         -4.41197613 </exc>
  <esr>          0.07295573 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37301687 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37301687 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70036760 0.00000000 -0.00000011 </position>
    <velocity> 0.00000606 -0.00000000 -0.00000000 </velocity>
    <force> 0.00267285 -0.00000006 0.00000111 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20222487 0.00000013 </position>
    <velocity> 0.00000000 0.00003688 0.00000000 </velocity>
    <force> 0.00000006 0.01655634 -0.00000148 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70036760 -0.00000000 -0.00000010 </position>
    <velocity> -0.00000606 0.00000000 -0.00000000 </velocity>
    <force> -0.00267279 0.00000005 0.00000100 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20222487 0.00000009 </position>
    <velocity> -0.00000000 -0.00003688 0.00000000 </velocity>
    <force> -0.00000008 -0.01655634 -0.00000075 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000020 </ekin_e>
  <ekin_ion> 0.00007150 </ekin_ion>
  <temp_ion> 3.76340672 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294496 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="30">
  <ekin>         5.34644792 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48005152 </eps>
  <enl>          4.77498558 </enl>
  <ecoul>      -15.60247979 </ecoul>
  <exc>         -4.41192417 </exc>
  <esr>          0.07293316 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37302197 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37302197 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70039311 0.00000000 -0.00000011 </position>
    <velocity> 0.00000627 -0.00000000 -0.00000000 </velocity>
    <force> 0.00266136 -0.00000006 0.00000118 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20238013 0.00000013 </position>
    <velocity> 0.00000000 0.00003817 0.00000000 </velocity>
    <force> 0.00000006 0.01652209 -0.00000154 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70039311 -0.00000000 -0.00000010 </position>
    <velocity> -0.00000627 0.00000000 -0.00000000 </velocity>
    <force> -0.00266131 0.00000005 0.00000108 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20238013 0.00000010 </position>
    <velocity> -0.00000000 -0.00003817 0.00000000 </velocity>
    <force> -0.00000007 -0.01652209 -0.00000084 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000021 </ekin_e>
  <ekin_ion> 0.00007660 </ekin_ion>
  <temp_ion> 4.03163842 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294495 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="31">
  <ekin>         5.34631069 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47996171 </eps>
  <enl>          4.77497416 </enl>
  <ecoul>      -15.60247959 </ecoul>
  <exc>         -4.41187080 </exc>
  <esr>          0.07290982 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37302725 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37302725 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70041944 0.00000000 -0.00000011 </position>
    <velocity> 0.00000648 -0.00000000 -0.00000000 </velocity>
    <force> 0.00264842 -0.00000005 0.00000124 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20254054 0.00000013 </position>
    <velocity> 0.00000000 0.00003946 0.00000000 </velocity>
    <force> 0.00000005 0.01648589 -0.00000160 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70041944 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000648 0.00000000 -0.00000000 </velocity>
    <force> -0.00264839 0.00000005 0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20254054 0.00000010 </position>
    <velocity> -0.00000000 -0.00003946 0.00000000 </velocity>
    <force> -0.00000006 -0.01648589 -0.00000092 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000023 </ekin_e>
  <ekin_ion> 0.00008186 </ekin_ion>
  <temp_ion> 4.30848438 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294493 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="32">
  <ekin>         5.34616981 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47986879 </eps>
  <enl>          4.77496188 </enl>
  <ecoul>      -15.60247966 </ecoul>
  <exc>         -4.41181593 </exc>
  <esr>          0.07288572 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37303268 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37303268 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70044659 0.00000000 -0.00000011 </position>
    <velocity> 0.00000669 -0.00000000 -0.00000000 </velocity>
    <force> 0.00263438 -0.00000004 0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20270609 0.00000013 </position>
    <velocity> 0.00000000 0.00004074 0.00000000 </velocity>
    <force> 0.00000004 0.01644824 -0.00000164 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70044660 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000669 0.00000000 -0.00000000 </velocity>
    <force> -0.00263437 0.00000004 0.00000120 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20270609 0.00000010 </position>
    <velocity> -0.00000000 -0.00004074 0.00000000 </velocity>
    <force> -0.00000005 -0.01644824 -0.00000100 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000024 </ekin_e>
  <ekin_ion> 0.00008728 </ekin_ion>
  <temp_ion> 4.59385130 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294492 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="33">
  <ekin>         5.34602495 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47977218 </eps>
  <enl>          4.77494811 </enl>
  <ecoul>      -15.60247977 </ecoul>
  <exc>         -4.41175939 </exc>
  <esr>          0.07286086 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37303828 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37303828 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70047457 0.00000000 -0.00000012 </position>
    <velocity> 0.00000689 -0.00000000 -0.00000000 </velocity>
    <force> 0.00261966 -0.00000003 0.00000134 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20287677 0.00000013 </position>
    <velocity> 0.00000000 0.00004203 0.00000000 </velocity>
    <force> 0.00000004 0.01640964 -0.00000167 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70047457 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000689 0.00000000 -0.00000000 </velocity>
    <force> -0.00261967 0.00000003 0.00000125 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20287677 0.00000011 </position>
    <velocity> -0.00000000 -0.00004203 0.00000000 </velocity>
    <force> -0.00000004 -0.01640965 -0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000025 </ekin_e>
  <ekin_ion> 0.00009287 </ekin_ion>
  <temp_ion> 4.88765185 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294491 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="34">
  <ekin>         5.34587577 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47967151 </eps>
  <enl>          4.77493245 </enl>
  <ecoul>      -15.60247969 </ecoul>
  <exc>         -4.41170106 </exc>
  <esr>          0.07283525 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37304403 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37304403 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70050336 0.00000000 -0.00000012 </position>
    <velocity> 0.00000710 -0.00000000 -0.00000000 </velocity>
    <force> 0.00260469 -0.00000002 0.00000137 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20305256 0.00000013 </position>
    <velocity> 0.00000000 0.00004331 0.00000000 </velocity>
    <force> 0.00000003 0.01637048 -0.00000168 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70050336 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000710 0.00000000 -0.00000000 </velocity>
    <force> -0.00260471 0.00000003 0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20305256 0.00000011 </position>
    <velocity> -0.00000000 -0.00004331 0.00000000 </velocity>
    <force> -0.00000002 -0.01637048 -0.00000114 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000027 </ekin_e>
  <ekin_ion> 0.00009861 </ekin_ion>
  <temp_ion> 5.18980528 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294489 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="35">
  <ekin>         5.34572195 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47956659 </eps>
  <enl>          4.77491475 </enl>
  <ecoul>      -15.60247925 </ecoul>
  <exc>         -4.41164080 </exc>
  <esr>          0.07280888 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37304995 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37304995 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70053296 0.00000000 -0.00000012 </position>
    <velocity> 0.00000730 -0.00000000 -0.00000000 </velocity>
    <force> 0.00258978 -0.00000001 0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20323346 0.00000013 </position>
    <velocity> 0.00000000 0.00004459 0.00000000 </velocity>
    <force> 0.00000002 0.01633095 -0.00000167 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70053296 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000730 0.00000000 -0.00000000 </velocity>
    <force> -0.00258982 0.00000002 0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20323346 0.00000011 </position>
    <velocity> -0.00000000 -0.00004459 0.00000000 </velocity>
    <force> -0.00000001 -0.01633095 -0.00000120 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000028 </ekin_e>
  <ekin_ion> 0.00010450 </ekin_ion>
  <temp_ion> 5.50023584 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294487 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="36">
  <ekin>         5.34556329 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47945753 </eps>
  <enl>          4.77489516 </enl>
  <ecoul>      -15.60247837 </ecoul>
  <exc>         -4.41157857 </exc>
  <esr>          0.07278176 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37305602 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37305602 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70056336 0.00000000 -0.00000012 </position>
    <velocity> 0.00000750 -0.00000000 -0.00000000 </velocity>
    <force> 0.00257513 0.00000000 0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20341945 0.00000013 </position>
    <velocity> 0.00000000 0.00004586 -0.00000000 </velocity>
    <force> 0.00000001 0.01629105 -0.00000166 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70056336 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000750 0.00000000 -0.00000000 </velocity>
    <force> -0.00257518 0.00000001 0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20341945 0.00000011 </position>
    <velocity> -0.00000000 -0.00004586 0.00000000 </velocity>
    <force> -0.00000000 -0.01629106 -0.00000126 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000030 </ekin_e>
  <ekin_ion> 0.00011056 </ekin_ion>
  <temp_ion> 5.81886963 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294486 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="37">
  <ekin>         5.34539972 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47934464 </eps>
  <enl>          4.77487408 </enl>
  <ecoul>      -15.60247705 </ecoul>
  <exc>         -4.41151435 </exc>
  <esr>          0.07275389 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37306224 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37306224 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70059456 0.00000000 -0.00000012 </position>
    <velocity> 0.00000770 -0.00000000 0.00000000 </velocity>
    <force> 0.00256076 0.00000001 0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20361052 0.00000013 </position>
    <velocity> 0.00000000 0.00004713 -0.00000000 </velocity>
    <force> 0.00000000 0.01625061 -0.00000162 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70059456 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000770 0.00000000 -0.00000000 </velocity>
    <force> -0.00256083 0.00000000 0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20361052 0.00000011 </position>
    <velocity> -0.00000000 -0.00004713 0.00000000 </velocity>
    <force> 0.00000001 -0.01625062 -0.00000130 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000032 </ekin_e>
  <ekin_ion> 0.00011677 </ekin_ion>
  <temp_ion> 6.14563078 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294484 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="38">
  <ekin>         5.34523129 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47922831 </eps>
  <enl>          4.77485199 </enl>
  <ecoul>      -15.60247539 </ecoul>
  <exc>         -4.41144820 </exc>
  <esr>          0.07272528 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37306862 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37306862 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70062656 0.00000000 -0.00000012 </position>
    <velocity> 0.00000790 -0.00000000 0.00000000 </velocity>
    <force> 0.00254659 0.00000002 0.00000140 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20380665 0.00000013 </position>
    <velocity> 0.00000000 0.00004840 -0.00000000 </velocity>
    <force> -0.00000001 0.01620932 -0.00000158 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70062656 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000790 0.00000000 0.00000000 </velocity>
    <force> -0.00254667 -0.00000001 0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20380665 0.00000011 </position>
    <velocity> -0.00000000 -0.00004840 0.00000000 </velocity>
    <force> 0.00000002 -0.01620934 -0.00000134 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000034 </ekin_e>
  <ekin_ion> 0.00012313 </ekin_ion>
  <temp_ion> 6.48043780 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294483 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="39">
  <ekin>         5.34505816 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47910900 </eps>
  <enl>          4.77482939 </enl>
  <ecoul>      -15.60247350 </ecoul>
  <exc>         -4.41138020 </exc>
  <esr>          0.07269593 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37307515 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37307515 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70065935 0.00000000 -0.00000012 </position>
    <velocity> 0.00000810 -0.00000000 0.00000000 </velocity>
    <force> 0.00253241 0.00000003 0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20400784 0.00000013 </position>
    <velocity> 0.00000000 0.00004966 -0.00000000 </velocity>
    <force> -0.00000002 0.01616686 -0.00000152 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70065935 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000810 0.00000000 0.00000000 </velocity>
    <force> -0.00253250 -0.00000001 0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20400784 0.00000011 </position>
    <velocity> -0.00000000 -0.00004966 0.00000000 </velocity>
    <force> 0.00000003 -0.01616687 -0.00000137 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000035 </ekin_e>
  <ekin_ion> 0.00012964 </ekin_ion>
  <temp_ion> 6.82320078 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294481 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="40">
  <ekin>         5.34488051 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47898705 </eps>
  <enl>          4.77480668 </enl>
  <ecoul>      -15.60247152 </ecoul>
  <exc>         -4.41131046 </exc>
  <esr>          0.07266584 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37308183 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37308183 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70069293 0.00000000 -0.00000011 </position>
    <velocity> 0.00000830 -0.00000000 0.00000000 </velocity>
    <force> 0.00251799 0.00000004 0.00000135 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20421406 0.00000013 </position>
    <velocity> 0.00000000 0.00005093 -0.00000000 </velocity>
    <force> -0.00000003 0.01612290 -0.00000145 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70069293 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000830 0.00000000 0.00000000 </velocity>
    <force> -0.00251808 -0.00000002 0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20421406 0.00000011 </position>
    <velocity> -0.00000000 -0.00005093 -0.00000000 </velocity>
    <force> 0.00000004 -0.01612291 -0.00000139 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00013630 </ekin_ion>
  <temp_ion> 7.17382016 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="41">
  <ekin>         5.34469850 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47886266 </eps>
  <enl>          4.77478411 </enl>
  <ecoul>      -15.60246956 </ecoul>
  <exc>         -4.41123905 </exc>
  <esr>          0.07263502 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37308866 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37308866 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70072729 0.00000000 -0.00000011 </position>
    <velocity> 0.00000849 -0.00000000 0.00000000 </velocity>
    <force> 0.00250310 0.00000005 0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20442531 0.00000012 </position>
    <velocity> 0.00000000 0.00005218 -0.00000000 </velocity>
    <force> -0.00000004 0.01607722 -0.00000137 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70072729 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000849 0.00000000 0.00000000 </velocity>
    <force> -0.00250320 -0.00000003 0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20442531 0.00000011 </position>
    <velocity> -0.00000000 -0.00005218 -0.00000000 </velocity>
    <force> 0.00000005 -0.01607723 -0.00000139 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000039 </ekin_e>
  <ekin_ion> 0.00014311 </ekin_ion>
  <temp_ion> 7.53218690 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="42">
  <ekin>         5.34451223 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47873590 </eps>
  <enl>          4.77476173 </enl>
  <ecoul>      -15.60246767 </ecoul>
  <exc>         -4.41116603 </exc>
  <esr>          0.07260346 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37309563 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37309563 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70076242 0.00000000 -0.00000011 </position>
    <velocity> 0.00000869 -0.00000000 0.00000000 </velocity>
    <force> 0.00248758 0.00000006 0.00000126 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20464157 0.00000012 </position>
    <velocity> 0.00000000 0.00005344 -0.00000000 </velocity>
    <force> -0.00000004 0.01602972 -0.00000128 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70076242 -0.00000000 -0.00000011 </position>
    <velocity> -0.00000869 0.00000000 0.00000000 </velocity>
    <force> -0.00248768 -0.00000004 0.00000126 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20464157 0.00000011 </position>
    <velocity> -0.00000000 -0.00005344 -0.00000000 </velocity>
    <force> 0.00000006 -0.01602973 -0.00000139 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000040 </ekin_e>
  <ekin_ion> 0.00015006 </ekin_ion>
  <temp_ion> 7.89818434 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294476 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="43">
  <ekin>         5.34432172 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47860667 </eps>
  <enl>          4.77473949 </enl>
  <ecoul>      -15.60246585 </ecoul>
  <exc>         -4.41109144 </exc>
  <esr>          0.07257118 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37310274 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37310274 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70079833 0.00000000 -0.00000011 </position>
    <velocity> 0.00000888 -0.00000000 0.00000000 </velocity>
    <force> 0.00247134 0.00000006 0.00000120 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20486282 0.00000012 </position>
    <velocity> 0.00000000 0.00005469 -0.00000000 </velocity>
    <force> -0.00000005 0.01598045 -0.00000117 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70079833 -0.00000000 -0.00000010 </position>
    <velocity> -0.00000888 0.00000000 0.00000000 </velocity>
    <force> -0.00247144 -0.00000004 0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20486282 0.00000011 </position>
    <velocity> -0.00000000 -0.00005469 -0.00000000 </velocity>
    <force> 0.00000007 -0.01598046 -0.00000138 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000042 </ekin_e>
  <ekin_ion> 0.00015716 </ekin_ion>
  <temp_ion> 8.27169106 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294474 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="44">
  <ekin>         5.34412692 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47847482 </eps>
  <enl>          4.77471721 </enl>
  <ecoul>      -15.60246408 </ecoul>
  <exc>         -4.41101523 </exc>
  <esr>          0.07253818 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37311000 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37311000 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70083501 0.00000000 -0.00000010 </position>
    <velocity> 0.00000907 -0.00000000 0.00000000 </velocity>
    <force> 0.00245439 0.00000007 0.00000114 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20508905 0.00000011 </position>
    <velocity> 0.00000000 0.00005594 -0.00000000 </velocity>
    <force> -0.00000006 0.01592960 -0.00000107 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70083501 -0.00000000 -0.00000010 </position>
    <velocity> -0.00000907 0.00000000 0.00000000 </velocity>
    <force> -0.00245449 -0.00000005 0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20508905 0.00000010 </position>
    <velocity> -0.00000000 -0.00005594 -0.00000000 </velocity>
    <force> 0.00000008 -0.01592961 -0.00000135 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000044 </ekin_e>
  <ekin_ion> 0.00016440 </ekin_ion>
  <temp_ion> 8.65258458 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294472 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="45">
  <ekin>         5.34392773 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47834015 </eps>
  <enl>          4.77469468 </enl>
  <ecoul>      -15.60246229 </ecoul>
  <exc>         -4.41093736 </exc>
  <esr>          0.07250446 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37311740 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37311740 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70087245 0.00000000 -0.00000010 </position>
    <velocity> 0.00000926 -0.00000000 0.00000000 </velocity>
    <force> 0.00243682 0.00000007 0.00000106 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20532025 0.00000011 </position>
    <velocity> 0.00000000 0.00005718 -0.00000000 </velocity>
    <force> -0.00000006 0.01587747 -0.00000095 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70087245 -0.00000000 -0.00000010 </position>
    <velocity> -0.00000926 0.00000000 0.00000000 </velocity>
    <force> -0.00243692 -0.00000005 0.00000109 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20532025 0.00000010 </position>
    <velocity> -0.00000000 -0.00005718 -0.00000000 </velocity>
    <force> 0.00000008 -0.01587748 -0.00000132 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000046 </ekin_e>
  <ekin_ion> 0.00017177 </ekin_ion>
  <temp_ion> 9.04074494 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294470 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="46">
  <ekin>         5.34372405 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47820251 </eps>
  <enl>          4.77467171 </enl>
  <ecoul>      -15.60246041 </ecoul>
  <exc>         -4.41085777 </exc>
  <esr>          0.07247002 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37312493 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37312493 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70091064 0.00000000 -0.00000010 </position>
    <velocity> 0.00000945 -0.00000000 0.00000000 </velocity>
    <force> 0.00241877 0.00000008 0.00000097 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20555639 0.00000010 </position>
    <velocity> 0.00000000 0.00005842 -0.00000000 </velocity>
    <force> -0.00000007 0.01582440 -0.00000083 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70091064 0.00000000 -0.00000009 </position>
    <velocity> -0.00000945 0.00000000 0.00000000 </velocity>
    <force> -0.00241887 -0.00000006 0.00000101 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.20555639 0.00000010 </position>
    <velocity> -0.00000000 -0.00005842 -0.00000000 </velocity>
    <force> 0.00000009 -0.01582441 -0.00000127 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000048 </ekin_e>
  <ekin_ion> 0.00017928 </ekin_ion>
  <temp_ion> 9.43605772 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294468 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="47">
  <ekin>         5.34351582 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47806178 </eps>
  <enl>          4.77464813 </enl>
  <ecoul>      -15.60245839 </ecoul>
  <exc>         -4.41077638 </exc>
  <esr>          0.07243487 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37313260 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37313260 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70094959 0.00000000 -0.00000009 </position>
    <velocity> 0.00000964 -0.00000000 0.00000000 </velocity>
    <force> 0.00240040 0.00000008 0.00000087 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20579745 0.00000010 </position>
    <velocity> 0.00000000 0.00005965 -0.00000000 </velocity>
    <force> -0.00000007 0.01577074 -0.00000070 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70094959 0.00000000 -0.00000009 </position>
    <velocity> -0.00000964 0.00000000 0.00000000 </velocity>
    <force> -0.00240048 -0.00000006 0.00000093 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.20579745 0.00000009 </position>
    <velocity> -0.00000000 -0.00005965 -0.00000000 </velocity>
    <force> 0.00000009 -0.01577075 -0.00000121 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000051 </ekin_e>
  <ekin_ion> 0.00018693 </ekin_ion>
  <temp_ion> 9.83841558 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294466 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="48">
  <ekin>         5.34330303 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47791794 </eps>
  <enl>          4.77462386 </enl>
  <ecoul>      -15.60245619 </ecoul>
  <exc>         -4.41069316 </exc>
  <esr>          0.07239901 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37314040 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37314040 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70098927 0.00000000 -0.00000009 </position>
    <velocity> 0.00000983 0.00000000 0.00000000 </velocity>
    <force> 0.00238181 0.00000008 0.00000077 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20604343 0.00000009 </position>
    <velocity> 0.00000000 0.00006088 -0.00000000 </velocity>
    <force> -0.00000007 0.01571675 -0.00000057 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70098927 0.00000000 -0.00000009 </position>
    <velocity> -0.00000983 0.00000000 0.00000000 </velocity>
    <force> -0.00238189 -0.00000006 0.00000084 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.20604343 0.00000009 </position>
    <velocity> 0.00000000 -0.00006088 -0.00000000 </velocity>
    <force> 0.00000009 -0.01571676 -0.00000114 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000053 </ekin_e>
  <ekin_ion> 0.00019471 </ekin_ion>
  <temp_ion> 10.24771804 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294463 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="49">
  <ekin>         5.34308576 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47777103 </eps>
  <enl>          4.77459886 </enl>
  <ecoul>      -15.60245383 </ecoul>
  <exc>         -4.41060809 </exc>
  <esr>          0.07236245 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37314833 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37314833 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70102970 0.00000000 -0.00000008 </position>
    <velocity> 0.00001001 0.00000000 0.00000000 </velocity>
    <force> 0.00236309 0.00000008 0.00000067 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20629431 0.00000009 </position>
    <velocity> -0.00000000 0.00006211 -0.00000000 </velocity>
    <force> -0.00000007 0.01566256 -0.00000043 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70102970 0.00000000 -0.00000008 </position>
    <velocity> -0.00001001 0.00000000 0.00000000 </velocity>
    <force> -0.00236316 -0.00000006 0.00000074 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20629431 0.00000009 </position>
    <velocity> 0.00000000 -0.00006211 -0.00000000 </velocity>
    <force> 0.00000009 -0.01566257 -0.00000106 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000055 </ekin_e>
  <ekin_ion> 0.00020261 </ekin_ion>
  <temp_ion> 10.66386934 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294461 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="50">
  <ekin>         5.34286415 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47762118 </eps>
  <enl>          4.77457319 </enl>
  <ecoul>      -15.60245134 </ecoul>
  <exc>         -4.41052121 </exc>
  <esr>          0.07232520 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315639 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315639 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70107086 0.00000000 -0.00000008 </position>
    <velocity> 0.00001020 0.00000000 0.00000000 </velocity>
    <force> 0.00234421 0.00000007 0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20655006 0.00000008 </position>
    <velocity> -0.00000000 0.00006333 -0.00000000 </velocity>
    <force> -0.00000007 0.01560813 -0.00000030 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70107086 0.00000000 -0.00000008 </position>
    <velocity> -0.00001020 -0.00000000 0.00000000 </velocity>
    <force> -0.00234426 -0.00000006 0.00000063 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20655006 0.00000008 </position>
    <velocity> 0.00000000 -0.00006333 -0.00000000 </velocity>
    <force> 0.00000009 -0.01560813 -0.00000098 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000058 </ekin_e>
  <ekin_ion> 0.00021065 </ekin_ion>
  <temp_ion> 11.08677479 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294458 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="51">
  <ekin>         5.34263836 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47746855 </eps>
  <enl>          4.77454699 </enl>
  <ecoul>      -15.60244880 </ecoul>
  <exc>         -4.41043257 </exc>
  <esr>          0.07228724 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316458 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316458 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70111275 0.00000000 -0.00000007 </position>
    <velocity> 0.00001038 0.00000000 0.00000000 </velocity>
    <force> 0.00232510 0.00000007 0.00000045 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20681067 0.00000008 </position>
    <velocity> -0.00000000 0.00006455 -0.00000000 </velocity>
    <force> -0.00000007 0.01555328 -0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70111275 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001038 -0.00000000 0.00000000 </velocity>
    <force> -0.00232514 -0.00000006 0.00000052 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20681067 0.00000008 </position>
    <velocity> 0.00000000 -0.00006455 -0.00000000 </velocity>
    <force> 0.00000008 -0.01555328 -0.00000088 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000061 </ekin_e>
  <ekin_ion> 0.00021881 </ekin_ion>
  <temp_ion> 11.51633651 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294456 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="52">
  <ekin>         5.34240854 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47731336 </eps>
  <enl>          4.77452044 </enl>
  <ecoul>      -15.60244626 </ecoul>
  <exc>         -4.41034225 </exc>
  <esr>          0.07224860 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317289 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317289 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70115535 0.00000000 -0.00000007 </position>
    <velocity> 0.00001056 0.00000000 0.00000000 </velocity>
    <force> 0.00230564 0.00000006 0.00000035 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20707613 0.00000007 </position>
    <velocity> -0.00000000 0.00006576 -0.00000000 </velocity>
    <force> -0.00000007 0.01549775 -0.00000003 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70115535 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001056 -0.00000000 0.00000000 </velocity>
    <force> -0.00230566 -0.00000006 0.00000041 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20707613 0.00000007 </position>
    <velocity> 0.00000000 -0.00006576 -0.00000000 </velocity>
    <force> 0.00000008 -0.01549775 -0.00000077 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000063 </ekin_e>
  <ekin_ion> 0.00022710 </ekin_ion>
  <temp_ion> 11.95244958 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294453 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="53">
  <ekin>         5.34217483 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47715580 </eps>
  <enl>          4.77449379 </enl>
  <ecoul>      -15.60244382 </ecoul>
  <exc>         -4.41025033 </exc>
  <esr>          0.07220927 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318132 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318132 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70119867 0.00000000 -0.00000006 </position>
    <velocity> 0.00001074 0.00000000 0.00000000 </velocity>
    <force> 0.00228572 0.00000006 0.00000023 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20734641 0.00000007 </position>
    <velocity> -0.00000000 0.00006697 -0.00000000 </velocity>
    <force> -0.00000006 0.01544123 0.00000010 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70119868 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001074 -0.00000000 0.00000000 </velocity>
    <force> -0.00228572 -0.00000006 0.00000029 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20734641 0.00000007 </position>
    <velocity> 0.00000000 -0.00006697 -0.00000000 </velocity>
    <force> 0.00000007 -0.01544123 -0.00000065 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000065 </ekin_e>
  <ekin_ion> 0.00023550 </ekin_ion>
  <temp_ion> 12.39499964 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294451 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="54">
  <ekin>         5.34193727 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47699607 </eps>
  <enl>          4.77446731 </enl>
  <ecoul>      -15.60244153 </ecoul>
  <exc>         -4.41015686 </exc>
  <esr>          0.07216926 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318987 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318987 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70124270 0.00000000 -0.00000006 </position>
    <velocity> 0.00001092 0.00000000 0.00000000 </velocity>
    <force> 0.00226525 0.00000005 0.00000012 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20762150 0.00000006 </position>
    <velocity> -0.00000000 0.00006817 -0.00000000 </velocity>
    <force> -0.00000006 0.01538347 0.00000023 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70124270 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001092 -0.00000000 0.00000000 </velocity>
    <force> -0.00226524 -0.00000005 0.00000017 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20762150 0.00000006 </position>
    <velocity> 0.00000000 -0.00006817 -0.00000000 </velocity>
    <force> 0.00000006 -0.01538347 -0.00000053 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000068 </ekin_e>
  <ekin_ion> 0.00024403 </ekin_ion>
  <temp_ion> 12.84386245 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294448 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="55">
  <ekin>         5.34169583 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47683429 </eps>
  <enl>          4.77444122 </enl>
  <ecoul>      -15.60243942 </ecoul>
  <exc>         -4.41006189 </exc>
  <esr>          0.07212858 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319854 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319854 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70128743 0.00000000 -0.00000005 </position>
    <velocity> 0.00001109 0.00000000 0.00000000 </velocity>
    <force> 0.00224422 0.00000004 0.00000000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20790138 0.00000006 </position>
    <velocity> -0.00000000 0.00006937 -0.00000000 </velocity>
    <force> -0.00000005 0.01532432 0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70128744 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001109 -0.00000000 0.00000000 </velocity>
    <force> -0.00224419 -0.00000005 0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20790138 0.00000006 </position>
    <velocity> 0.00000000 -0.00006937 -0.00000000 </velocity>
    <force> 0.00000005 -0.01532432 -0.00000040 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000070 </ekin_e>
  <ekin_ion> 0.00025268 </ekin_ion>
  <temp_ion> 13.29890553 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294446 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="56">
  <ekin>         5.34145042 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47667051 </eps>
  <enl>          4.77441568 </enl>
  <ecoul>      -15.60243749 </ecoul>
  <exc>         -4.40996542 </exc>
  <esr>          0.07208722 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320733 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320733 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70133286 0.00000000 -0.00000005 </position>
    <velocity> 0.00001127 0.00000000 0.00000000 </velocity>
    <force> 0.00222269 0.00000003 -0.00000011 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20818603 0.00000005 </position>
    <velocity> -0.00000000 0.00007057 -0.00000000 </velocity>
    <force> -0.00000005 0.01526375 0.00000047 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70133286 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001127 -0.00000000 0.00000000 </velocity>
    <force> -0.00222265 -0.00000004 -0.00000007 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20818603 0.00000005 </position>
    <velocity> 0.00000000 -0.00007057 -0.00000000 </velocity>
    <force> 0.00000004 -0.01526374 -0.00000026 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000073 </ekin_e>
  <ekin_ion> 0.00026144 </ekin_ion>
  <temp_ion> 13.75999125 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294444 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="57">
  <ekin>         5.34120090 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47650471 </eps>
  <enl>          4.77439074 </enl>
  <ecoul>      -15.60243571 </ecoul>
  <exc>         -4.40986744 </exc>
  <esr>          0.07204519 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321622 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321622 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70137897 0.00000000 -0.00000005 </position>
    <velocity> 0.00001144 0.00000000 0.00000000 </velocity>
    <force> 0.00220078 0.00000002 -0.00000023 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20847543 0.00000005 </position>
    <velocity> -0.00000000 0.00007176 -0.00000000 </velocity>
    <force> -0.00000004 0.01520181 0.00000058 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70137897 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001144 -0.00000000 0.00000000 </velocity>
    <force> -0.00220072 -0.00000004 -0.00000019 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20847543 0.00000005 </position>
    <velocity> 0.00000000 -0.00007176 -0.00000000 </velocity>
    <force> 0.00000003 -0.01520180 -0.00000012 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000075 </ekin_e>
  <ekin_ion> 0.00027031 </ekin_ion>
  <temp_ion> 14.22698030 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294441 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="58">
  <ekin>         5.34094716 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47633676 </eps>
  <enl>          4.77436634 </enl>
  <ecoul>      -15.60243404 </ecoul>
  <exc>         -4.40976793 </exc>
  <esr>          0.07200250 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37322523 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37322523 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70142576 0.00000000 -0.00000004 </position>
    <velocity> 0.00001161 0.00000000 0.00000000 </velocity>
    <force> 0.00217863 0.00000001 -0.00000035 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20876956 0.00000004 </position>
    <velocity> -0.00000000 0.00007294 -0.00000000 </velocity>
    <force> -0.00000003 0.01513863 0.00000069 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70142577 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001161 -0.00000000 0.00000000 </velocity>
    <force> -0.00217856 -0.00000003 -0.00000031 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20876956 0.00000004 </position>
    <velocity> 0.00000000 -0.00007294 -0.00000000 </velocity>
    <force> 0.00000002 -0.01513862 0.00000002 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000077 </ekin_e>
  <ekin_ion> 0.00027929 </ekin_ion>
  <temp_ion> 14.69973450 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294439 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="59">
  <ekin>         5.34068913 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47616654 </eps>
  <enl>          4.77434233 </enl>
  <ecoul>      -15.60243239 </ecoul>
  <exc>         -4.40966687 </exc>
  <esr>          0.07195915 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37323434 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37323434 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70147323 0.00000000 -0.00000004 </position>
    <velocity> 0.00001178 0.00000000 0.00000000 </velocity>
    <force> 0.00215637 0.00000000 -0.00000047 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20906840 0.00000004 </position>
    <velocity> -0.00000000 0.00007412 -0.00000000 </velocity>
    <force> -0.00000002 0.01507437 0.00000078 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70147323 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001178 -0.00000000 0.00000000 </velocity>
    <force> -0.00215630 -0.00000002 -0.00000042 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20906840 0.00000003 </position>
    <velocity> 0.00000000 -0.00007412 -0.00000000 </velocity>
    <force> 0.00000001 -0.01507436 0.00000016 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000080 </ekin_e>
  <ekin_ion> 0.00028838 </ekin_ion>
  <temp_ion> 15.17811829 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294437 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="60">
  <ekin>         5.34042682 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47599386 </eps>
  <enl>          4.77431845 </enl>
  <ecoul>      -15.60243073 </ecoul>
  <exc>         -4.40956424 </exc>
  <esr>          0.07191515 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37324356 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37324356 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70152137 0.00000000 -0.00000003 </position>
    <velocity> 0.00001195 0.00000000 0.00000000 </velocity>
    <force> 0.00213410 -0.00000001 -0.00000058 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20937193 0.00000003 </position>
    <velocity> -0.00000000 0.00007530 -0.00000000 </velocity>
    <force> -0.00000001 0.01500911 0.00000087 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70152137 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001195 -0.00000000 0.00000000 </velocity>
    <force> -0.00213401 -0.00000001 -0.00000054 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20937193 0.00000003 </position>
    <velocity> 0.00000000 -0.00007530 -0.00000000 </velocity>
    <force> -0.00000000 -0.01500909 0.00000031 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000082 </ekin_e>
  <ekin_ion> 0.00029758 </ekin_ion>
  <temp_ion> 15.66199847 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294434 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="61">
  <ekin>         5.34016034 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47581863 </eps>
  <enl>          4.77429447 </enl>
  <ecoul>      -15.60242902 </ecoul>
  <exc>         -4.40946004 </exc>
  <esr>          0.07187050 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325288 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325288 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70157016 0.00000000 -0.00000003 </position>
    <velocity> 0.00001212 0.00000000 0.00000000 </velocity>
    <force> 0.00211183 -0.00000002 -0.00000068 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20968013 0.00000003 </position>
    <velocity> -0.00000000 0.00007647 -0.00000000 </velocity>
    <force> 0.00000000 0.01494289 0.00000095 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70157016 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001212 -0.00000000 0.00000000 </velocity>
    <force> -0.00211174 -0.00000000 -0.00000065 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20968013 0.00000002 </position>
    <velocity> 0.00000000 -0.00007647 -0.00000000 </velocity>
    <force> -0.00000002 -0.01494287 0.00000045 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000085 </ekin_e>
  <ekin_ion> 0.00030687 </ekin_ion>
  <temp_ion> 16.15124273 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294432 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="62">
  <ekin>         5.33988987 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47564077 </eps>
  <enl>          4.77427016 </enl>
  <ecoul>      -15.60242726 </ecoul>
  <exc>         -4.40935431 </exc>
  <esr>          0.07182521 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37326230 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37326230 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70161961 0.00000000 -0.00000002 </position>
    <velocity> 0.00001228 0.00000000 0.00000000 </velocity>
    <force> 0.00208951 -0.00000003 -0.00000078 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.20999299 0.00000003 </position>
    <velocity> -0.00000000 0.00007763 -0.00000000 </velocity>
    <force> 0.00000001 0.01487570 0.00000103 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70161961 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001228 -0.00000000 0.00000000 </velocity>
    <force> -0.00208941 0.00000001 -0.00000076 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20999299 0.00000002 </position>
    <velocity> 0.00000000 -0.00007763 -0.00000000 </velocity>
    <force> -0.00000003 -0.01487569 0.00000060 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000087 </ekin_e>
  <ekin_ion> 0.00031627 </ekin_ion>
  <temp_ion> 16.64571776 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294429 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="63">
  <ekin>         5.33961566 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47546027 </eps>
  <enl>          4.77424532 </enl>
  <ecoul>      -15.60242545 </ecoul>
  <exc>         -4.40924708 </exc>
  <esr>          0.07177928 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37327182 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37327182 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70166970 0.00000000 -0.00000002 </position>
    <velocity> 0.00001244 0.00000000 0.00000000 </velocity>
    <force> 0.00206704 -0.00000004 -0.00000087 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21031046 0.00000002 </position>
    <velocity> -0.00000000 0.00007879 -0.00000000 </velocity>
    <force> 0.00000002 0.01480752 0.00000109 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70166970 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001244 -0.00000000 0.00000000 </velocity>
    <force> -0.00206694 0.00000002 -0.00000086 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21031047 0.00000001 </position>
    <velocity> 0.00000000 -0.00007879 -0.00000000 </velocity>
    <force> -0.00000004 -0.01480751 0.00000074 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000090 </ekin_e>
  <ekin_ion> 0.00032576 </ekin_ion>
  <temp_ion> 17.14528771 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294427 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="64">
  <ekin>         5.33933796 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47527719 </eps>
  <enl>          4.77421983 </enl>
  <ecoul>      -15.60242363 </ecoul>
  <exc>         -4.40913840 </exc>
  <esr>          0.07173271 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37328143 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37328143 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70172043 0.00000000 -0.00000002 </position>
    <velocity> 0.00001260 0.00000000 0.00000000 </velocity>
    <force> 0.00204427 -0.00000004 -0.00000096 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21063255 0.00000002 </position>
    <velocity> -0.00000000 0.00007995 -0.00000000 </velocity>
    <force> 0.00000003 0.01473833 0.00000114 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70172044 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001260 -0.00000000 0.00000000 </velocity>
    <force> -0.00204417 0.00000002 -0.00000096 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21063255 0.00000001 </position>
    <velocity> 0.00000000 -0.00007995 -0.00000000 </velocity>
    <force> -0.00000005 -0.01473832 0.00000087 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000092 </ekin_e>
  <ekin_ion> 0.00033535 </ekin_ion>
  <temp_ion> 17.64981385 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294424 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="65">
  <ekin>         5.33905695 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47509157 </eps>
  <enl>          4.77419361 </enl>
  <ecoul>      -15.60242182 </ecoul>
  <exc>         -4.40902830 </exc>
  <esr>          0.07168552 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37329113 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37329113 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70177180 0.00000000 -0.00000001 </position>
    <velocity> 0.00001276 0.00000000 0.00000000 </velocity>
    <force> 0.00202110 -0.00000005 -0.00000103 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21095922 0.00000002 </position>
    <velocity> -0.00000000 0.00008109 -0.00000000 </velocity>
    <force> 0.00000004 0.01466815 0.00000119 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70177180 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001276 -0.00000000 0.00000000 </velocity>
    <force> -0.00202099 0.00000003 -0.00000105 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21095922 0.00000001 </position>
    <velocity> 0.00000000 -0.00008109 -0.00000000 </velocity>
    <force> -0.00000006 -0.01466814 0.00000101 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000095 </ekin_e>
  <ekin_ion> 0.00034502 </ekin_ion>
  <temp_ion> 18.15915546 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294422 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="66">
  <ekin>         5.33877276 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47490342 </eps>
  <enl>          4.77416658 </enl>
  <ecoul>      -15.60242002 </ecoul>
  <exc>         -4.40891682 </exc>
  <esr>          0.07163770 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37330093 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37330093 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70182379 0.00000000 -0.00000001 </position>
    <velocity> 0.00001292 0.00000000 0.00000000 </velocity>
    <force> 0.00199741 -0.00000006 -0.00000111 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21129045 0.00000002 </position>
    <velocity> -0.00000000 0.00008224 -0.00000000 </velocity>
    <force> 0.00000005 0.01459708 0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70182379 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001292 -0.00000000 0.00000000 </velocity>
    <force> -0.00199731 0.00000004 -0.00000113 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21129045 0.00000000 </position>
    <velocity> 0.00000000 -0.00008224 -0.00000000 </velocity>
    <force> -0.00000007 -0.01459706 0.00000113 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000097 </ekin_e>
  <ekin_ion> 0.00035479 </ekin_ion>
  <temp_ion> 18.67317170 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294419 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="67">
  <ekin>         5.33848540 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47471269 </eps>
  <enl>          4.77413866 </enl>
  <ecoul>      -15.60241821 </ecoul>
  <exc>         -4.40880396 </exc>
  <esr>          0.07158927 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37331081 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37331081 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70187639 0.00000000 -0.00000001 </position>
    <velocity> 0.00001307 0.00000000 0.00000000 </velocity>
    <force> 0.00197318 -0.00000006 -0.00000117 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21162622 0.00000002 </position>
    <velocity> -0.00000000 0.00008338 -0.00000000 </velocity>
    <force> 0.00000005 0.01452522 0.00000125 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70187639 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001307 -0.00000000 0.00000000 </velocity>
    <force> -0.00197309 0.00000005 -0.00000120 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21162622 -0.00000000 </position>
    <velocity> 0.00000000 -0.00008338 -0.00000000 </velocity>
    <force> -0.00000007 -0.01452521 0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000100 </ekin_e>
  <ekin_ion> 0.00036464 </ekin_ion>
  <temp_ion> 19.19172364 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294416 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="68">
  <ekin>         5.33819477 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47451928 </eps>
  <enl>          4.77410978 </enl>
  <ecoul>      -15.60241634 </ecoul>
  <exc>         -4.40868970 </exc>
  <esr>          0.07154022 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37332077 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37332077 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70192960 0.00000000 -0.00000001 </position>
    <velocity> 0.00001323 0.00000000 0.00000000 </velocity>
    <force> 0.00194840 -0.00000007 -0.00000123 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21196651 0.00000002 </position>
    <velocity> -0.00000000 0.00008451 -0.00000000 </velocity>
    <force> 0.00000006 0.01445273 0.00000126 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70192961 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001323 -0.00000000 0.00000000 </velocity>
    <force> -0.00194832 0.00000005 -0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21196651 -0.00000001 </position>
    <velocity> 0.00000000 -0.00008451 -0.00000000 </velocity>
    <force> -0.00000008 -0.01445272 0.00000136 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000103 </ekin_e>
  <ekin_ion> 0.00037458 </ekin_ion>
  <temp_ion> 19.71467561 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294414 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="69">
  <ekin>         5.33790070 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47432306 </eps>
  <enl>          4.77407986 </enl>
  <ecoul>      -15.60241432 </ecoul>
  <exc>         -4.40857400 </exc>
  <esr>          0.07149057 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37333081 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37333081 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70198342 0.00000000 -0.00000000 </position>
    <velocity> 0.00001338 0.00000000 0.00000000 </velocity>
    <force> 0.00192313 -0.00000007 -0.00000128 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21231129 0.00000001 </position>
    <velocity> -0.00000000 0.00008563 -0.00000000 </velocity>
    <force> 0.00000006 0.01437968 0.00000127 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70198342 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001338 -0.00000000 0.00000000 </velocity>
    <force> -0.00192305 0.00000006 -0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21231129 -0.00000001 </position>
    <velocity> 0.00000000 -0.00008563 -0.00000000 </velocity>
    <force> -0.00000009 -0.01437967 0.00000146 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000105 </ekin_e>
  <ekin_ion> 0.00038459 </ekin_ion>
  <temp_ion> 20.24189514 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294411 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="70">
  <ekin>         5.33760297 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47412389 </eps>
  <enl>          4.77404887 </enl>
  <ecoul>      -15.60241207 </ecoul>
  <exc>         -4.40845682 </exc>
  <esr>          0.07144031 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37334094 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37334094 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70203783 0.00000000 -0.00000000 </position>
    <velocity> 0.00001353 0.00000000 0.00000000 </velocity>
    <force> 0.00189741 -0.00000007 -0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21266054 0.00000001 </position>
    <velocity> -0.00000000 0.00008675 -0.00000000 </velocity>
    <force> 0.00000007 0.01430609 0.00000127 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70203783 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001353 -0.00000000 0.00000000 </velocity>
    <force> -0.00189735 0.00000006 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21266054 -0.00000001 </position>
    <velocity> 0.00000000 -0.00008675 -0.00000000 </velocity>
    <force> -0.00000009 -0.01430608 0.00000154 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000108 </ekin_e>
  <ekin_ion> 0.00039469 </ekin_ion>
  <temp_ion> 20.77325127 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294408 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="71">
  <ekin>         5.33730132 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47392169 </eps>
  <enl>          4.77401685 </enl>
  <ecoul>      -15.60240952 </ecoul>
  <exc>         -4.40833810 </exc>
  <esr>          0.07138946 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37335114 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37335114 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70209282 0.00000000 -0.00000000 </position>
    <velocity> 0.00001368 0.00000000 0.00000000 </velocity>
    <force> 0.00187130 -0.00000007 -0.00000135 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21301424 0.00000001 </position>
    <velocity> -0.00000000 0.00008787 -0.00000000 </velocity>
    <force> 0.00000007 0.01423188 0.00000125 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70209282 -0.00000000 0.00000000 </position>
    <velocity> -0.00001367 -0.00000000 0.00000000 </velocity>
    <force> -0.00187125 0.00000006 -0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21301424 -0.00000001 </position>
    <velocity> 0.00000000 -0.00008787 -0.00000000 </velocity>
    <force> -0.00000009 -0.01423188 0.00000162 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000111 </ekin_e>
  <ekin_ion> 0.00040486 </ekin_ion>
  <temp_ion> 21.30861171 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294406 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="72">
  <ekin>         5.33699555 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47371649 </eps>
  <enl>          4.77398393 </enl>
  <ecoul>      -15.60240662 </ecoul>
  <exc>         -4.40821778 </exc>
  <esr>          0.07133802 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37336141 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37336141 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70214839 0.00000000 -0.00000000 </position>
    <velocity> 0.00001382 -0.00000000 0.00000000 </velocity>
    <force> 0.00184484 -0.00000007 -0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21337236 0.00000001 </position>
    <velocity> -0.00000000 0.00008898 0.00000000 </velocity>
    <force> 0.00000007 0.01415690 0.00000123 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70214839 -0.00000000 0.00000000 </position>
    <velocity> -0.00001382 -0.00000000 0.00000000 </velocity>
    <force> -0.00184480 0.00000007 -0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21337236 -0.00000001 </position>
    <velocity> -0.00000000 -0.00008898 -0.00000000 </velocity>
    <force> -0.00000009 -0.01415690 0.00000168 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000113 </ekin_e>
  <ekin_ion> 0.00041511 </ekin_ion>
  <temp_ion> 21.84783931 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294403 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="73">
  <ekin>         5.33668550 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47350839 </eps>
  <enl>          4.77395033 </enl>
  <ecoul>      -15.60240335 </ecoul>
  <exc>         -4.40809583 </exc>
  <esr>          0.07128599 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37337175 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37337175 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70220453 0.00000000 -0.00000000 </position>
    <velocity> 0.00001396 -0.00000000 0.00000000 </velocity>
    <force> 0.00181804 -0.00000007 -0.00000137 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21373489 0.00000002 </position>
    <velocity> 0.00000000 0.00009008 0.00000000 </velocity>
    <force> 0.00000007 0.01408093 0.00000121 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70220453 -0.00000000 0.00000000 </position>
    <velocity> -0.00001396 -0.00000000 0.00000000 </velocity>
    <force> -0.00181802 0.00000007 -0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21373489 -0.00000001 </position>
    <velocity> -0.00000000 -0.00009008 -0.00000000 </velocity>
    <force> -0.00000009 -0.01408093 0.00000172 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000116 </ekin_e>
  <ekin_ion> 0.00042542 </ekin_ion>
  <temp_ion> 22.39078920 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294401 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="74">
  <ekin>         5.33637108 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47329757 </eps>
  <enl>          4.77391628 </enl>
  <ecoul>      -15.60239973 </ecoul>
  <exc>         -4.40797222 </exc>
  <esr>          0.07123338 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37338216 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37338216 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70226122 0.00000000 -0.00000000 </position>
    <velocity> 0.00001410 -0.00000000 -0.00000000 </velocity>
    <force> 0.00179092 -0.00000007 -0.00000137 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21410179 0.00000002 </position>
    <velocity> 0.00000000 0.00009118 0.00000000 </velocity>
    <force> 0.00000007 0.01400375 0.00000117 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70226122 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001410 0.00000000 -0.00000000 </velocity>
    <force> -0.00179091 0.00000007 -0.00000139 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21410179 -0.00000001 </position>
    <velocity> -0.00000000 -0.00009118 -0.00000000 </velocity>
    <force> -0.00000009 -0.01400375 0.00000176 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000118 </ekin_e>
  <ekin_ion> 0.00043581 </ekin_ion>
  <temp_ion> 22.93730731 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294398 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="75">
  <ekin>         5.33605229 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47308424 </eps>
  <enl>          4.77388201 </enl>
  <ecoul>      -15.60239577 </ecoul>
  <exc>         -4.40784693 </exc>
  <esr>          0.07118020 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37339263 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37339263 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70231847 0.00000000 -0.00000000 </position>
    <velocity> 0.00001424 -0.00000000 -0.00000000 </velocity>
    <force> 0.00176346 -0.00000006 -0.00000135 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21447304 0.00000002 </position>
    <velocity> 0.00000000 0.00009227 0.00000000 </velocity>
    <force> 0.00000007 0.01392521 0.00000113 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70231847 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001424 0.00000000 -0.00000000 </velocity>
    <force> -0.00176347 0.00000007 -0.00000137 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21447304 -0.00000001 </position>
    <velocity> -0.00000000 -0.00009227 0.00000000 </velocity>
    <force> -0.00000008 -0.01392522 0.00000177 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000121 </ekin_e>
  <ekin_ion> 0.00044626 </ekin_ion>
  <temp_ion> 23.48723096 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294396 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="76">
  <ekin>         5.33572921 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47286856 </eps>
  <enl>          4.77384766 </enl>
  <ecoul>      -15.60239152 </ecoul>
  <exc>         -4.40771995 </exc>
  <esr>          0.07112645 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37340317 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37340317 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70237626 0.00000000 -0.00000000 </position>
    <velocity> 0.00001438 -0.00000000 -0.00000000 </velocity>
    <force> 0.00173568 -0.00000006 -0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21484862 0.00000002 </position>
    <velocity> 0.00000000 0.00009335 0.00000000 </velocity>
    <force> 0.00000007 0.01384526 0.00000108 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70237626 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001438 0.00000000 -0.00000000 </velocity>
    <force> -0.00173571 0.00000006 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21484862 -0.00000001 </position>
    <velocity> -0.00000000 -0.00009335 0.00000000 </velocity>
    <force> -0.00000007 -0.01384526 0.00000177 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000124 </ekin_e>
  <ekin_ion> 0.00045677 </ekin_ion>
  <temp_ion> 24.04039145 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294393 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="77">
  <ekin>         5.33540199 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47265061 </eps>
  <enl>          4.77381319 </enl>
  <ecoul>      -15.60238701 </ecoul>
  <exc>         -4.40759132 </exc>
  <esr>          0.07107214 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37341376 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37341376 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70243459 0.00000000 -0.00000001 </position>
    <velocity> 0.00001451 -0.00000000 -0.00000000 </velocity>
    <force> 0.00170761 -0.00000005 -0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21522850 0.00000002 </position>
    <velocity> 0.00000000 0.00009443 0.00000000 </velocity>
    <force> 0.00000006 0.01376395 0.00000103 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70243459 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001451 0.00000000 -0.00000000 </velocity>
    <force> -0.00170765 0.00000006 -0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21522850 -0.00000001 </position>
    <velocity> -0.00000000 -0.00009443 0.00000000 </velocity>
    <force> -0.00000007 -0.01376395 0.00000175 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000126 </ekin_e>
  <ekin_ion> 0.00046733 </ekin_ion>
  <temp_ion> 24.59661834 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294390 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="78">
  <ekin>         5.33507085 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47243038 </eps>
  <enl>          4.77377844 </enl>
  <ecoul>      -15.60238226 </ecoul>
  <exc>         -4.40746106 </exc>
  <esr>          0.07101728 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37342441 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37342441 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70249343 0.00000000 -0.00000001 </position>
    <velocity> 0.00001465 -0.00000000 -0.00000000 </velocity>
    <force> 0.00167929 -0.00000004 -0.00000126 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21561266 0.00000002 </position>
    <velocity> 0.00000000 0.00009550 0.00000000 </velocity>
    <force> 0.00000006 0.01368145 0.00000097 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70249343 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001465 0.00000000 -0.00000000 </velocity>
    <force> -0.00167934 0.00000006 -0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21561266 -0.00000001 </position>
    <velocity> -0.00000000 -0.00009550 0.00000000 </velocity>
    <force> -0.00000006 -0.01368145 0.00000172 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000129 </ekin_e>
  <ekin_ion> 0.00047796 </ekin_ion>
  <temp_ion> 25.15574418 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294388 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="79">
  <ekin>         5.33473604 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47220777 </eps>
  <enl>          4.77374313 </enl>
  <ecoul>      -15.60237728 </ecoul>
  <exc>         -4.40732923 </exc>
  <esr>          0.07096186 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37343512 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37343512 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70255280 0.00000000 -0.00000001 </position>
    <velocity> 0.00001478 -0.00000000 -0.00000000 </velocity>
    <force> 0.00165079 -0.00000004 -0.00000121 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21600107 0.00000003 </position>
    <velocity> 0.00000000 0.00009657 0.00000000 </velocity>
    <force> 0.00000005 0.01359801 0.00000090 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70255280 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001478 0.00000000 -0.00000000 </velocity>
    <force> -0.00165085 0.00000005 -0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21600107 -0.00000001 </position>
    <velocity> -0.00000000 -0.00009657 0.00000000 </velocity>
    <force> -0.00000005 -0.01359802 0.00000167 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000132 </ekin_e>
  <ekin_ion> 0.00048863 </ekin_ion>
  <temp_ion> 25.71760881 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294385 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="80">
  <ekin>         5.33439781 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47198264 </eps>
  <enl>          4.77370695 </enl>
  <ecoul>      -15.60237209 </ecoul>
  <exc>         -4.40719591 </exc>
  <esr>          0.07090590 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37344587 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37344587 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70261267 0.00000000 -0.00000001 </position>
    <velocity> 0.00001490 -0.00000000 -0.00000000 </velocity>
    <force> 0.00162216 -0.00000003 -0.00000116 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21639370 0.00000003 </position>
    <velocity> 0.00000000 0.00009763 0.00000000 </velocity>
    <force> 0.00000004 0.01351391 0.00000084 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70261267 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001490 0.00000000 -0.00000000 </velocity>
    <force> -0.00162223 0.00000004 -0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21639370 -0.00000000 </position>
    <velocity> -0.00000000 -0.00009763 0.00000000 </velocity>
    <force> -0.00000004 -0.01351392 0.00000161 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000135 </ekin_e>
  <ekin_ion> 0.00049936 </ekin_ion>
  <temp_ion> 26.28206214 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294382 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="81">
  <ekin>         5.33405642 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47175491 </eps>
  <enl>          4.77366970 </enl>
  <ecoul>      -15.60236671 </ecoul>
  <exc>         -4.40706117 </exc>
  <esr>          0.07084940 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37345667 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37345667 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70267304 0.00000000 -0.00000002 </position>
    <velocity> 0.00001503 -0.00000000 -0.00000000 </velocity>
    <force> 0.00159346 -0.00000002 -0.00000110 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21679053 0.00000003 </position>
    <velocity> 0.00000000 0.00009868 0.00000000 </velocity>
    <force> 0.00000004 0.01342940 0.00000077 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70267304 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001503 0.00000000 -0.00000000 </velocity>
    <force> -0.00159354 0.00000004 -0.00000108 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21679053 0.00000000 </position>
    <velocity> -0.00000000 -0.00009868 0.00000000 </velocity>
    <force> -0.00000002 -0.01342942 0.00000153 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000138 </ekin_e>
  <ekin_ion> 0.00051013 </ekin_ion>
  <temp_ion> 26.84896454 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294379 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="82">
  <ekin>         5.33371205 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47152460 </eps>
  <enl>          4.77363136 </enl>
  <ecoul>      -15.60236122 </ecoul>
  <exc>         -4.40692511 </exc>
  <esr>          0.07079236 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37346752 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37346752 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70273390 0.00000000 -0.00000002 </position>
    <velocity> 0.00001515 -0.00000000 -0.00000000 </velocity>
    <force> 0.00156471 -0.00000001 -0.00000103 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21719152 0.00000004 </position>
    <velocity> 0.00000000 0.00009973 0.00000000 </velocity>
    <force> 0.00000003 0.01334464 0.00000069 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70273390 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001515 0.00000000 -0.00000000 </velocity>
    <force> -0.00156480 0.00000003 -0.00000100 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21719152 0.00000001 </position>
    <velocity> -0.00000000 -0.00009973 0.00000000 </velocity>
    <force> -0.00000001 -0.01334465 0.00000144 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000141 </ekin_e>
  <ekin_ion> 0.00052094 </ekin_ion>
  <temp_ion> 27.41818500 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294376 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="83">
  <ekin>         5.33336486 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47129190 </eps>
  <enl>          4.77359214 </enl>
  <ecoul>      -15.60235570 </ecoul>
  <exc>         -4.40678781 </exc>
  <esr>          0.07073480 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37347841 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37347841 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70279524 0.00000000 -0.00000003 </position>
    <velocity> 0.00001527 -0.00000000 -0.00000000 </velocity>
    <force> 0.00153591 0.00000000 -0.00000095 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21759666 0.00000004 </position>
    <velocity> 0.00000000 0.00010077 0.00000000 </velocity>
    <force> 0.00000002 0.01325967 0.00000061 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70279524 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001527 0.00000000 -0.00000000 </velocity>
    <force> -0.00153600 0.00000002 -0.00000091 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21759666 0.00000001 </position>
    <velocity> -0.00000000 -0.00010077 0.00000000 </velocity>
    <force> -0.00000000 -0.01325969 0.00000134 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000144 </ekin_e>
  <ekin_ion> 0.00053180 </ekin_ion>
  <temp_ion> 27.98959719 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294373 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="84">
  <ekin>         5.33301490 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47105712 </eps>
  <enl>          4.77355252 </enl>
  <ecoul>      -15.60235027 </ecoul>
  <exc>         -4.40664937 </exc>
  <esr>          0.07067672 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37348934 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37348934 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70285705 0.00000000 -0.00000003 </position>
    <velocity> 0.00001539 -0.00000000 -0.00000000 </velocity>
    <force> 0.00150702 0.00000001 -0.00000086 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21800592 0.00000004 </position>
    <velocity> 0.00000000 0.00010180 0.00000000 </velocity>
    <force> 0.00000001 0.01317442 0.00000054 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70285705 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001539 0.00000000 -0.00000000 </velocity>
    <force> -0.00150711 0.00000001 -0.00000081 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21800592 0.00000001 </position>
    <velocity> -0.00000000 -0.00010180 0.00000000 </velocity>
    <force> 0.00000001 -0.01317444 0.00000122 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000147 </ekin_e>
  <ekin_ion> 0.00054270 </ekin_ion>
  <temp_ion> 28.56307439 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294369 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="85">
  <ekin>         5.33266219 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47082072 </eps>
  <enl>          4.77351312 </enl>
  <ecoul>      -15.60234505 </ecoul>
  <exc>         -4.40650984 </exc>
  <esr>          0.07061813 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37350030 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37350030 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70291932 0.00000000 -0.00000003 </position>
    <velocity> 0.00001551 -0.00000000 -0.00000000 </velocity>
    <force> 0.00147797 0.00000002 -0.00000077 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21841927 0.00000005 </position>
    <velocity> 0.00000000 0.00010283 0.00000000 </velocity>
    <force> 0.00000000 0.01308872 0.00000046 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70291932 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001551 0.00000000 -0.00000000 </velocity>
    <force> -0.00147807 0.00000000 -0.00000071 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21841927 0.00000002 </position>
    <velocity> -0.00000000 -0.00010283 0.00000000 </velocity>
    <force> 0.00000002 -0.01308873 0.00000110 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000150 </ekin_e>
  <ekin_ion> 0.00055363 </ekin_ion>
  <temp_ion> 29.13848444 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294366 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="86">
  <ekin>         5.33230667 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47058313 </eps>
  <enl>          4.77347461 </enl>
  <ecoul>      -15.60234016 </ecoul>
  <exc>         -4.40636928 </exc>
  <esr>          0.07055903 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37351130 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37351130 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70298204 0.00000000 -0.00000004 </position>
    <velocity> 0.00001562 -0.00000000 -0.00000000 </velocity>
    <force> 0.00144869 0.00000003 -0.00000067 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21883669 0.00000005 </position>
    <velocity> 0.00000000 0.00010385 0.00000000 </velocity>
    <force> -0.00000001 0.01300232 0.00000037 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70298204 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001562 0.00000000 -0.00000000 </velocity>
    <force> -0.00144878 -0.00000001 -0.00000060 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21883669 0.00000003 </position>
    <velocity> -0.00000000 -0.00010385 0.00000000 </velocity>
    <force> 0.00000003 -0.01300233 0.00000096 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000154 </ekin_e>
  <ekin_ion> 0.00056460 </ekin_ion>
  <temp_ion> 29.71568583 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294363 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="87">
  <ekin>         5.33194825 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47034474 </eps>
  <enl>          4.77343753 </enl>
  <ecoul>      -15.60233568 </ecoul>
  <exc>         -4.40622770 </exc>
  <esr>          0.07049942 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37352233 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37352233 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70304521 0.00000000 -0.00000004 </position>
    <velocity> 0.00001574 -0.00000000 -0.00000000 </velocity>
    <force> 0.00141910 0.00000004 -0.00000057 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21925813 0.00000006 </position>
    <velocity> 0.00000000 0.00010486 0.00000000 </velocity>
    <force> -0.00000002 0.01291498 0.00000029 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70304521 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001574 0.00000000 -0.00000000 </velocity>
    <force> -0.00141919 -0.00000002 -0.00000048 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21925813 0.00000003 </position>
    <velocity> -0.00000000 -0.00010486 0.00000000 </velocity>
    <force> 0.00000004 -0.01291499 0.00000081 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000157 </ekin_e>
  <ekin_ion> 0.00057559 </ekin_ion>
  <temp_ion> 30.29452574 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294360 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="88">
  <ekin>         5.33158685 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.47010574 </eps>
  <enl>          4.77340220 </enl>
  <ecoul>      -15.60233162 </ecoul>
  <exc>         -4.40608508 </exc>
  <esr>          0.07043932 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37353338 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37353338 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70310881 0.00000000 -0.00000005 </position>
    <velocity> 0.00001585 -0.00000000 -0.00000000 </velocity>
    <force> 0.00138913 0.00000004 -0.00000045 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.21968359 0.00000006 </position>
    <velocity> 0.00000000 0.00010586 0.00000000 </velocity>
    <force> -0.00000003 0.01282652 0.00000021 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70310881 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001585 0.00000000 -0.00000000 </velocity>
    <force> -0.00138921 -0.00000003 -0.00000037 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.21968359 0.00000004 </position>
    <velocity> -0.00000000 -0.00010586 0.00000000 </velocity>
    <force> 0.00000005 -0.01282653 0.00000066 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000159 </ekin_e>
  <ekin_ion> 0.00058662 </ekin_ion>
  <temp_ion> 30.87484067 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294357 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="89">
  <ekin>         5.33122237 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46986612 </eps>
  <enl>          4.77336861 </enl>
  <ecoul>      -15.60232793 </ecoul>
  <exc>         -4.40594139 </exc>
  <esr>          0.07037873 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37354446 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37354446 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70317284 0.00000000 -0.00000005 </position>
    <velocity> 0.00001595 -0.00000000 -0.00000000 </velocity>
    <force> 0.00135872 0.00000005 -0.00000034 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22011303 0.00000007 </position>
    <velocity> 0.00000000 0.00010686 0.00000000 </velocity>
    <force> -0.00000004 0.01273684 0.00000012 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70317284 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001595 0.00000000 -0.00000000 </velocity>
    <force> -0.00135880 -0.00000003 -0.00000025 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22011303 0.00000004 </position>
    <velocity> -0.00000000 -0.00010686 0.00000000 </velocity>
    <force> 0.00000006 -0.01273685 0.00000050 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000162 </ekin_e>
  <ekin_ion> 0.00059767 </ekin_ion>
  <temp_ion> 31.45645938 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294354 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="90">
  <ekin>         5.33085473 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46962563 </eps>
  <enl>          4.77333640 </enl>
  <ecoul>      -15.60232451 </ecoul>
  <exc>         -4.40579657 </exc>
  <esr>          0.07031766 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37355557 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37355557 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70323728 0.00000000 -0.00000006 </position>
    <velocity> 0.00001606 -0.00000000 -0.00000000 </velocity>
    <force> 0.00132787 0.00000006 -0.00000021 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22054642 0.00000007 </position>
    <velocity> 0.00000000 0.00010785 0.00000000 </velocity>
    <force> -0.00000005 0.01264597 0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70323728 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001606 0.00000000 -0.00000000 </velocity>
    <force> -0.00132794 -0.00000004 -0.00000014 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22054642 0.00000005 </position>
    <velocity> -0.00000000 -0.00010785 0.00000000 </velocity>
    <force> 0.00000007 -0.01264598 0.00000033 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000165 </ekin_e>
  <ekin_ion> 0.00060874 </ekin_ion>
  <temp_ion> 32.03920776 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294351 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="91">
  <ekin>         5.33048391 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46938386 </eps>
  <enl>          4.77330499 </enl>
  <ecoul>      -15.60232118 </ecoul>
  <exc>         -4.40565054 </exc>
  <esr>          0.07025611 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37356669 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37356669 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70330213 0.00000000 -0.00000006 </position>
    <velocity> 0.00001616 -0.00000000 -0.00000000 </velocity>
    <force> 0.00129658 0.00000006 -0.00000009 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22098373 0.00000007 </position>
    <velocity> 0.00000000 0.00010884 0.00000000 </velocity>
    <force> -0.00000005 0.01255406 -0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70330213 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001616 0.00000000 -0.00000000 </velocity>
    <force> -0.00129664 -0.00000005 -0.00000002 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22098373 0.00000006 </position>
    <velocity> -0.00000000 -0.00010884 0.00000000 </velocity>
    <force> 0.00000007 -0.01255407 0.00000015 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000169 </ekin_e>
  <ekin_ion> 0.00061983 </ekin_ion>
  <temp_ion> 32.62291446 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294348 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="92">
  <ekin>         5.33010989 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46914029 </eps>
  <enl>          4.77327362 </enl>
  <ecoul>      -15.60231778 </ecoul>
  <exc>         -4.40550326 </exc>
  <esr>          0.07019409 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37357783 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37357783 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70336737 0.00000000 -0.00000007 </position>
    <velocity> 0.00001626 -0.00000000 -0.00000000 </velocity>
    <force> 0.00126489 0.00000007 0.00000004 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22142494 0.00000008 </position>
    <velocity> 0.00000000 0.00010982 0.00000000 </velocity>
    <force> -0.00000006 0.01246135 -0.00000012 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70336737 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001626 0.00000000 -0.00000000 </velocity>
    <force> -0.00126494 -0.00000006 0.00000010 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22142494 0.00000006 </position>
    <velocity> -0.00000000 -0.00010982 0.00000000 </velocity>
    <force> 0.00000008 -0.01246135 -0.00000002 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000172 </ekin_e>
  <ekin_ion> 0.00063094 </ekin_ion>
  <temp_ion> 33.20741635 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294345 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="93">
  <ekin>         5.32973270 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46889444 </eps>
  <enl>          4.77324157 </enl>
  <ecoul>      -15.60231413 </ecoul>
  <exc>         -4.40535467 </exc>
  <esr>          0.07013160 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37358898 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37358898 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70343300 0.00000000 -0.00000007 </position>
    <velocity> 0.00001636 -0.00000000 -0.00000000 </velocity>
    <force> 0.00123286 0.00000007 0.00000016 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.22187001 0.00000008 </position>
    <velocity> 0.00000000 0.00011079 0.00000000 </velocity>
    <force> -0.00000007 0.01236813 -0.00000020 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70343300 0.00000000 -0.00000007 </position>
    <velocity> -0.00001636 0.00000000 -0.00000000 </velocity>
    <force> -0.00123290 -0.00000006 0.00000021 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22187001 0.00000007 </position>
    <velocity> -0.00000000 -0.00011079 0.00000000 </velocity>
    <force> 0.00000008 -0.01236813 -0.00000020 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000175 </ekin_e>
  <ekin_ion> 0.00064206 </ekin_ion>
  <temp_ion> 33.79256244 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294342 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="94">
  <ekin>         5.32935241 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46864596 </eps>
  <enl>          4.77320829 </enl>
  <ecoul>      -15.60231012 </ecoul>
  <exc>         -4.40520476 </exc>
  <esr>          0.07006866 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37360014 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37360014 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70349900 0.00000000 -0.00000008 </position>
    <velocity> 0.00001645 -0.00000000 -0.00000000 </velocity>
    <force> 0.00120057 0.00000007 0.00000029 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.22231892 0.00000009 </position>
    <velocity> 0.00000000 0.00011175 0.00000000 </velocity>
    <force> -0.00000007 0.01227468 -0.00000027 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70349900 0.00000000 -0.00000007 </position>
    <velocity> -0.00001645 0.00000000 -0.00000000 </velocity>
    <force> -0.00120059 -0.00000007 0.00000032 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22231892 0.00000007 </position>
    <velocity> -0.00000000 -0.00011175 0.00000000 </velocity>
    <force> 0.00000009 -0.01227468 -0.00000037 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000179 </ekin_e>
  <ekin_ion> 0.00065318 </ekin_ion>
  <temp_ion> 34.37821550 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294338 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="95">
  <ekin>         5.32896910 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46839469 </eps>
  <enl>          4.77317350 </enl>
  <ecoul>      -15.60230570 </ecoul>
  <exc>         -4.40505352 </exc>
  <esr>          0.07000526 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37361131 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37361131 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70356537 0.00000000 -0.00000008 </position>
    <velocity> 0.00001655 0.00000000 -0.00000000 </velocity>
    <force> 0.00116810 0.00000007 0.00000041 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.22277164 0.00000009 </position>
    <velocity> 0.00000000 0.00011270 0.00000000 </velocity>
    <force> -0.00000007 0.01218122 -0.00000034 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70356537 0.00000000 -0.00000008 </position>
    <velocity> -0.00001655 0.00000000 -0.00000000 </velocity>
    <force> -0.00116811 -0.00000007 0.00000043 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22277164 0.00000008 </position>
    <velocity> -0.00000000 -0.00011270 0.00000000 </velocity>
    <force> 0.00000009 -0.01218122 -0.00000054 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000182 </ekin_e>
  <ekin_ion> 0.00066432 </ekin_ion>
  <temp_ion> 34.96425099 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294335 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="96">
  <ekin>         5.32858289 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46814074 </eps>
  <enl>          4.77313727 </enl>
  <ecoul>      -15.60230089 </ecoul>
  <exc>         -4.40490101 </exc>
  <esr>          0.06994142 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37362248 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37362248 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70363209 0.00000000 -0.00000009 </position>
    <velocity> 0.00001664 0.00000000 -0.00000000 </velocity>
    <force> 0.00113553 0.00000007 0.00000053 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.22322813 0.00000009 </position>
    <velocity> 0.00000000 0.00011365 0.00000000 </velocity>
    <force> -0.00000008 0.01208785 -0.00000042 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70363209 0.00000000 -0.00000008 </position>
    <velocity> -0.00001664 0.00000000 -0.00000000 </velocity>
    <force> -0.00113553 -0.00000007 0.00000054 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22322813 0.00000009 </position>
    <velocity> 0.00000000 -0.00011365 0.00000000 </velocity>
    <force> 0.00000009 -0.01208785 -0.00000070 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000185 </ekin_e>
  <ekin_ion> 0.00067546 </ekin_ion>
  <temp_ion> 35.55055319 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294332 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="97">
  <ekin>         5.32819388 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46788442 </eps>
  <enl>          4.77309995 </enl>
  <ecoul>      -15.60229580 </ecoul>
  <exc>         -4.40474726 </exc>
  <esr>          0.06987714 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37363366 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37363366 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70369916 0.00000000 -0.00000009 </position>
    <velocity> 0.00001672 0.00000000 -0.00000000 </velocity>
    <force> 0.00110293 0.00000006 0.00000064 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.22368838 0.00000010 </position>
    <velocity> -0.00000000 0.00011459 0.00000000 </velocity>
    <force> -0.00000008 0.01199452 -0.00000048 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70369916 0.00000000 -0.00000009 </position>
    <velocity> -0.00001672 -0.00000000 -0.00000000 </velocity>
    <force> -0.00110292 -0.00000007 0.00000064 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22368838 0.00000009 </position>
    <velocity> 0.00000000 -0.00011459 0.00000000 </velocity>
    <force> 0.00000009 -0.01199452 -0.00000086 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000189 </ekin_e>
  <ekin_ion> 0.00068660 </ekin_ion>
  <temp_ion> 36.13700928 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294328 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="98">
  <ekin>         5.32780215 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46762620 </eps>
  <enl>          4.77306214 </enl>
  <ecoul>      -15.60229057 </ecoul>
  <exc>         -4.40459234 </exc>
  <esr>          0.06981243 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37364483 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37364483 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70376656 0.00000000 -0.00000010 </position>
    <velocity> 0.00001681 0.00000000 -0.00000000 </velocity>
    <force> 0.00107034 0.00000006 0.00000074 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.22415234 0.00000010 </position>
    <velocity> -0.00000000 0.00011553 0.00000000 </velocity>
    <force> -0.00000008 0.01190106 -0.00000055 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70376656 0.00000000 -0.00000009 </position>
    <velocity> -0.00001681 -0.00000000 -0.00000000 </velocity>
    <force> -0.00107031 -0.00000007 0.00000074 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.22415234 0.00000010 </position>
    <velocity> 0.00000000 -0.00011553 0.00000000 </velocity>
    <force> 0.00000008 -0.01190105 -0.00000100 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000192 </ekin_e>
  <ekin_ion> 0.00069774 </ekin_ion>
  <temp_ion> 36.72350245 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294325 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="99">
  <ekin>         5.32740776 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46736662 </eps>
  <enl>          4.77302452 </enl>
  <ecoul>      -15.60228534 </ecoul>
  <exc>         -4.40443631 </exc>
  <esr>          0.06974729 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37365600 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37365600 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70383429 0.00000000 -0.00000010 </position>
    <velocity> 0.00001689 0.00000000 -0.00000000 </velocity>
    <force> 0.00103777 0.00000006 0.00000084 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.22461999 0.00000011 </position>
    <velocity> -0.00000000 0.00011645 0.00000000 </velocity>
    <force> -0.00000007 0.01180717 -0.00000062 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70383429 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001689 -0.00000000 -0.00000000 </velocity>
    <force> -0.00103773 -0.00000007 0.00000083 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22461999 0.00000010 </position>
    <velocity> 0.00000000 -0.00011645 0.00000000 </velocity>
    <force> 0.00000008 -0.01180716 -0.00000114 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000195 </ekin_e>
  <ekin_ion> 0.00070889 </ekin_ion>
  <temp_ion> 37.30990524 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294322 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="100">
  <ekin>         5.32701070 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46710613 </eps>
  <enl>          4.77298771 </enl>
  <ecoul>      -15.60228023 </ecoul>
  <exc>         -4.40427922 </exc>
  <esr>          0.06968174 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37366717 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37366717 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70390233 0.00000000 -0.00000010 </position>
    <velocity> 0.00001697 0.00000000 -0.00000000 </velocity>
    <force> 0.00100518 0.00000005 0.00000093 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22509130 0.00000011 </position>
    <velocity> -0.00000000 0.00011737 0.00000000 </velocity>
    <force> -0.00000007 0.01171249 -0.00000068 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70390233 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001697 -0.00000000 -0.00000000 </velocity>
    <force> -0.00100513 -0.00000006 0.00000092 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22509130 0.00000011 </position>
    <velocity> 0.00000000 -0.00011737 0.00000000 </velocity>
    <force> 0.00000007 -0.01171248 -0.00000127 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000197 </ekin_e>
  <ekin_ion> 0.00072002 </ekin_ion>
  <temp_ion> 37.89607480 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294320 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="101">
  <ekin>         5.32661092 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46684498 </eps>
  <enl>          4.77295209 </enl>
  <ecoul>      -15.60227529 </ecoul>
  <exc>         -4.40412106 </exc>
  <esr>          0.06961577 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37367832 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37367832 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70397067 0.00000000 -0.00000011 </position>
    <velocity> 0.00001705 0.00000000 -0.00000000 </velocity>
    <force> 0.00097253 0.00000004 0.00000102 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22556624 0.00000011 </position>
    <velocity> -0.00000000 0.00011828 0.00000000 </velocity>
    <force> -0.00000007 0.01161671 -0.00000074 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70397067 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001705 -0.00000000 -0.00000000 </velocity>
    <force> -0.00097246 -0.00000006 0.00000100 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22556624 0.00000011 </position>
    <velocity> 0.00000000 -0.00011828 0.00000000 </velocity>
    <force> 0.00000006 -0.01161670 -0.00000139 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000200 </ekin_e>
  <ekin_ion> 0.00073115 </ekin_ion>
  <temp_ion> 38.48185101 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294317 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="102">
  <ekin>         5.32620833 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46658319 </eps>
  <enl>          4.77291773 </enl>
  <ecoul>      -15.60227049 </ecoul>
  <exc>         -4.40396185 </exc>
  <esr>          0.06954939 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37368947 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37368947 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70403931 0.00000000 -0.00000011 </position>
    <velocity> 0.00001712 0.00000000 -0.00000000 </velocity>
    <force> 0.00093972 0.00000004 0.00000110 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22604479 0.00000011 </position>
    <velocity> -0.00000000 0.00011919 0.00000000 </velocity>
    <force> -0.00000006 0.01151956 -0.00000080 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70403931 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001712 -0.00000000 -0.00000000 </velocity>
    <force> -0.00093965 -0.00000006 0.00000107 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22604479 0.00000011 </position>
    <velocity> 0.00000000 -0.00011919 0.00000000 </velocity>
    <force> 0.00000005 -0.01151955 -0.00000150 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000202 </ekin_e>
  <ekin_ion> 0.00074227 </ekin_ion>
  <temp_ion> 39.06705825 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294315 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="103">
  <ekin>         5.32580284 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46632051 </eps>
  <enl>          4.77288432 </enl>
  <ecoul>      -15.60226570 </ecoul>
  <exc>         -4.40380154 </exc>
  <esr>          0.06948261 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37370059 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37370059 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70410823 0.00000000 -0.00000011 </position>
    <velocity> 0.00001719 0.00000000 -0.00000000 </velocity>
    <force> 0.00090667 0.00000003 0.00000117 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22652690 0.00000012 </position>
    <velocity> -0.00000000 0.00012008 0.00000000 </velocity>
    <force> -0.00000006 0.01142096 -0.00000086 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70410823 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001719 -0.00000000 -0.00000000 </velocity>
    <force> -0.00090659 -0.00000005 0.00000113 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22652690 0.00000012 </position>
    <velocity> 0.00000000 -0.00012008 0.00000000 </velocity>
    <force> 0.00000004 -0.01142095 -0.00000159 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000205 </ekin_e>
  <ekin_ion> 0.00075338 </ekin_ion>
  <temp_ion> 39.65151076 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294312 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="104">
  <ekin>         5.32539434 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46605647 </eps>
  <enl>          4.77285127 </enl>
  <ecoul>      -15.60226077 </ecoul>
  <exc>         -4.40364008 </exc>
  <esr>          0.06941544 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37371170 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37371170 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70417743 0.00000000 -0.00000012 </position>
    <velocity> 0.00001726 0.00000000 -0.00000000 </velocity>
    <force> 0.00087331 0.00000002 0.00000124 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22701255 0.00000012 </position>
    <velocity> -0.00000000 0.00012097 0.00000000 </velocity>
    <force> -0.00000005 0.01132099 -0.00000091 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70417743 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001726 -0.00000000 -0.00000000 </velocity>
    <force> -0.00087323 -0.00000004 0.00000118 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22701255 0.00000012 </position>
    <velocity> 0.00000000 -0.00012097 0.00000000 </velocity>
    <force> 0.00000003 -0.01132097 -0.00000167 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000207 </ekin_e>
  <ekin_ion> 0.00076446 </ekin_ion>
  <temp_ion> 40.23502059 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294310 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="105">
  <ekin>         5.32498277 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46579046 </eps>
  <enl>          4.77281779 </enl>
  <ecoul>      -15.60225549 </ecoul>
  <exc>         -4.40347740 </exc>
  <esr>          0.06934788 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37372279 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37372279 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70424688 0.00000000 -0.00000012 </position>
    <velocity> 0.00001733 0.00000000 -0.00000000 </velocity>
    <force> 0.00083961 0.00000001 0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22750170 0.00000012 </position>
    <velocity> -0.00000000 0.00012185 0.00000000 </velocity>
    <force> -0.00000004 0.01121988 -0.00000095 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70424688 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001733 -0.00000000 -0.00000000 </velocity>
    <force> -0.00083952 -0.00000003 0.00000123 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22750170 0.00000012 </position>
    <velocity> 0.00000000 -0.00012185 0.00000000 </velocity>
    <force> 0.00000002 -0.01121986 -0.00000173 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000210 </ekin_e>
  <ekin_ion> 0.00077553 </ekin_ion>
  <temp_ion> 40.81740661 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294308 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="106">
  <ekin>         5.32456813 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46552194 </eps>
  <enl>          4.77278309 </enl>
  <ecoul>      -15.60224968 </ecoul>
  <exc>         -4.40331345 </exc>
  <esr>          0.06927995 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37373386 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37373386 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70431659 0.00000000 -0.00000012 </position>
    <velocity> 0.00001740 0.00000000 -0.00000000 </velocity>
    <force> 0.00080557 0.00000001 0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22799433 0.00000012 </position>
    <velocity> -0.00000000 0.00012272 0.00000000 </velocity>
    <force> -0.00000003 0.01111800 -0.00000100 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70431659 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001740 -0.00000000 -0.00000000 </velocity>
    <force> -0.00080549 -0.00000003 0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22799433 0.00000012 </position>
    <velocity> 0.00000000 -0.00012272 0.00000000 </velocity>
    <force> 0.00000001 -0.01111798 -0.00000178 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000212 </ekin_e>
  <ekin_ion> 0.00078657 </ekin_ion>
  <temp_ion> 41.39850260 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294305 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="107">
  <ekin>         5.32415046 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46525048 </eps>
  <enl>          4.77274653 </enl>
  <ecoul>      -15.60224323 </ecoul>
  <exc>         -4.40314819 </exc>
  <esr>          0.06921163 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37374490 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37374490 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70438654 0.00000000 -0.00000012 </position>
    <velocity> 0.00001746 0.00000000 -0.00000000 </velocity>
    <force> 0.00077126 -0.00000000 0.00000140 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22849041 0.00000012 </position>
    <velocity> -0.00000000 0.00012359 0.00000000 </velocity>
    <force> -0.00000002 0.01101576 -0.00000103 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70438654 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001746 -0.00000000 -0.00000000 </velocity>
    <force> -0.00077117 -0.00000002 0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22849041 0.00000012 </position>
    <velocity> 0.00000000 -0.00012359 0.00000000 </velocity>
    <force> -0.00000000 -0.01101574 -0.00000181 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000215 </ekin_e>
  <ekin_ion> 0.00079758 </ekin_ion>
  <temp_ion> 41.97816229 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294302 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="108">
  <ekin>         5.32372987 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46497588 </eps>
  <enl>          4.77270777 </enl>
  <ecoul>      -15.60223608 </ecoul>
  <exc>         -4.40298159 </exc>
  <esr>          0.06914296 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37375592 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37375592 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70445672 0.00000000 -0.00000012 </position>
    <velocity> 0.00001752 0.00000000 -0.00000000 </velocity>
    <force> 0.00073674 -0.00000001 0.00000143 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22898989 0.00000012 </position>
    <velocity> -0.00000000 0.00012444 0.00000000 </velocity>
    <force> -0.00000001 0.01091351 -0.00000106 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70445672 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001752 -0.00000000 -0.00000000 </velocity>
    <force> -0.00073666 -0.00000001 0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22898989 0.00000012 </position>
    <velocity> 0.00000000 -0.00012444 0.00000000 </velocity>
    <force> -0.00000001 -0.01091350 -0.00000183 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000218 </ekin_e>
  <ekin_ion> 0.00080857 </ekin_ion>
  <temp_ion> 42.55626013 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294299 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="109">
  <ekin>         5.32330649 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46469824 </eps>
  <enl>          4.77266682 </enl>
  <ecoul>      -15.60222829 </ecoul>
  <exc>         -4.40281368 </exc>
  <esr>          0.06907392 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37376690 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37376690 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70452712 0.00000000 -0.00000012 </position>
    <velocity> 0.00001757 0.00000000 -0.00000000 </velocity>
    <force> 0.00070210 -0.00000002 0.00000144 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22949276 0.00000012 </position>
    <velocity> -0.00000000 0.00012529 0.00000000 </velocity>
    <force> -0.00000000 0.01081148 -0.00000109 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70452712 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001757 -0.00000000 -0.00000000 </velocity>
    <force> -0.00070203 0.00000000 0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22949276 0.00000012 </position>
    <velocity> 0.00000000 -0.00012529 -0.00000000 </velocity>
    <force> -0.00000002 -0.01081147 -0.00000182 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000221 </ekin_e>
  <ekin_ion> 0.00081952 </ekin_ion>
  <temp_ion> 43.13268726 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294297 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="110">
  <ekin>         5.32288050 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46441784 </eps>
  <enl>          4.77262399 </enl>
  <ecoul>      -15.60221997 </ecoul>
  <exc>         -4.40264452 </exc>
  <esr>          0.06900452 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37377784 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37377784 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70459773 0.00000000 -0.00000012 </position>
    <velocity> 0.00001763 0.00000000 0.00000000 </velocity>
    <force> 0.00066740 -0.00000003 0.00000145 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.22999896 0.00000012 </position>
    <velocity> -0.00000000 0.00012613 0.00000000 </velocity>
    <force> 0.00000001 0.01070970 -0.00000111 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70459773 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001763 -0.00000000 0.00000000 </velocity>
    <force> -0.00066733 0.00000001 0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.22999897 0.00000012 </position>
    <velocity> 0.00000000 -0.00012613 -0.00000000 </velocity>
    <force> -0.00000003 -0.01070969 -0.00000180 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000224 </ekin_e>
  <ekin_ion> 0.00083044 </ekin_ion>
  <temp_ion> 43.70734343 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294294 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.007" max="    0.007"/>
<iteration count="111">
  <ekin>         5.32245209 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46413516 </eps>
  <enl>          4.77257981 </enl>
  <ecoul>      -15.60221129 </ecoul>
  <exc>         -4.40247420 </exc>
  <esr>          0.06893479 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37378876 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37378876 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70466853 0.00000000 -0.00000012 </position>
    <velocity> 0.00001768 0.00000000 0.00000000 </velocity>
    <force> 0.00063264 -0.00000003 0.00000144 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23050849 0.00000012 </position>
    <velocity> -0.00000000 0.00012697 -0.00000000 </velocity>
    <force> 0.00000002 0.01060801 -0.00000113 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70466853 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001768 -0.00000000 0.00000000 </velocity>
    <force> -0.00063257 0.00000002 0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23050849 0.00000012 </position>
    <velocity> 0.00000000 -0.00012697 -0.00000000 </velocity>
    <force> -0.00000004 -0.01060800 -0.00000177 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000226 </ekin_e>
  <ekin_ion> 0.00084132 </ekin_ion>
  <temp_ion> 44.28012679 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294291 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.016" max="    0.016"/>
<iteration count="112">
  <ekin>         5.32202147 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46385069 </eps>
  <enl>          4.77253490 </enl>
  <ecoul>      -15.60220246 </ecoul>
  <exc>         -4.40230286 </exc>
  <esr>          0.06886471 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37379963 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37379963 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70473952 0.00000000 -0.00000012 </position>
    <velocity> 0.00001772 0.00000000 0.00000000 </velocity>
    <force> 0.00059776 -0.00000004 0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23102130 0.00000012 </position>
    <velocity> -0.00000000 0.00012779 -0.00000000 </velocity>
    <force> 0.00000003 0.01050609 -0.00000113 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70473953 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001772 -0.00000000 0.00000000 </velocity>
    <force> -0.00059771 0.00000003 0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23102130 0.00000012 </position>
    <velocity> 0.00000000 -0.00012779 -0.00000000 </velocity>
    <force> -0.00000005 -0.01050608 -0.00000172 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000229 </ekin_e>
  <ekin_ion> 0.00085216 </ekin_ion>
  <temp_ion> 44.85092381 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294288 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.015" max="    0.015"/>
<iteration count="113">
  <ekin>         5.32158886 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46356487 </eps>
  <enl>          4.77248981 </enl>
  <ecoul>      -15.60219363 </ecoul>
  <exc>         -4.40213062 </exc>
  <esr>          0.06879429 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37381046 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37381046 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70481069 0.00000000 -0.00000012 </position>
    <velocity> 0.00001777 0.00000000 0.00000000 </velocity>
    <force> 0.00056268 -0.00000005 0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23153736 0.00000012 </position>
    <velocity> -0.00000000 0.00012861 -0.00000000 </velocity>
    <force> 0.00000004 0.01040355 -0.00000114 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70481069 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001777 -0.00000000 0.00000000 </velocity>
    <force> -0.00056264 0.00000004 0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23153736 0.00000012 </position>
    <velocity> 0.00000000 -0.00012861 -0.00000000 </velocity>
    <force> -0.00000006 -0.01040354 -0.00000165 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000232 </ekin_e>
  <ekin_ion> 0.00086297 </ekin_ion>
  <temp_ion> 45.41960195 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294286 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.014" max="    0.015"/>
<iteration count="114">
  <ekin>         5.32115444 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46327805 </eps>
  <enl>          4.77244496 </enl>
  <ecoul>      -15.60218497 </ecoul>
  <exc>         -4.40195762 </exc>
  <esr>          0.06872355 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37382124 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37382124 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70488202 0.00000000 -0.00000011 </position>
    <velocity> 0.00001781 0.00000000 0.00000000 </velocity>
    <force> 0.00052727 -0.00000005 0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23205664 0.00000012 </position>
    <velocity> -0.00000000 0.00012942 -0.00000000 </velocity>
    <force> 0.00000005 0.01029998 -0.00000113 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70488203 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001781 -0.00000000 0.00000000 </velocity>
    <force> -0.00052724 0.00000005 0.00000123 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23205664 0.00000011 </position>
    <velocity> 0.00000000 -0.00012942 -0.00000000 </velocity>
    <force> -0.00000007 -0.01029998 -0.00000158 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000234 </ekin_e>
  <ekin_ion> 0.00087373 </ekin_ion>
  <temp_ion> 45.98600684 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294283 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.016" max="    0.016"/>
<iteration count="115">
  <ekin>         5.32071837 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46299045 </eps>
  <enl>          4.77240061 </enl>
  <ecoul>      -15.60217656 </ecoul>
  <exc>         -4.40178395 </exc>
  <esr>          0.06865249 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37383198 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37383198 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70495351 0.00000000 -0.00000011 </position>
    <velocity> 0.00001785 0.00000000 0.00000000 </velocity>
    <force> 0.00049142 -0.00000006 0.00000128 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23257910 0.00000012 </position>
    <velocity> -0.00000000 0.00013022 -0.00000000 </velocity>
    <force> 0.00000006 0.01019511 -0.00000112 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70495351 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001785 -0.00000000 0.00000000 </velocity>
    <force> -0.00049140 0.00000005 0.00000118 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23257910 0.00000011 </position>
    <velocity> 0.00000000 -0.00013022 -0.00000000 </velocity>
    <force> -0.00000007 -0.01019511 -0.00000149 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000236 </ekin_e>
  <ekin_ion> 0.00088445 </ekin_ion>
  <temp_ion> 46.54996469 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294281 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.025" max="    0.025"/>
<iteration count="116">
  <ekin>         5.32028074 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46270220 </eps>
  <enl>          4.77235691 </enl>
  <ecoul>      -15.60216844 </ecoul>
  <exc>         -4.40160969 </exc>
  <esr>          0.06858111 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37384267 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37384267 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70502514 0.00000000 -0.00000011 </position>
    <velocity> 0.00001789 0.00000000 0.00000000 </velocity>
    <force> 0.00045508 -0.00000006 0.00000122 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23310472 0.00000012 </position>
    <velocity> -0.00000000 0.00013101 -0.00000000 </velocity>
    <force> 0.00000006 0.01008882 -0.00000111 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70502514 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001789 -0.00000000 0.00000000 </velocity>
    <force> -0.00045507 0.00000006 0.00000113 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23310472 0.00000011 </position>
    <velocity> 0.00000000 -0.00013101 -0.00000000 </velocity>
    <force> -0.00000008 -0.01008882 -0.00000138 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000239 </ekin_e>
  <ekin_ion> 0.00089511 </ekin_ion>
  <temp_ion> 47.11128954 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294279 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.013"/>
<iteration count="117">
  <ekin>         5.31984157 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46241337 </eps>
  <enl>          4.77231394 </enl>
  <ecoul>      -15.60216061 </ecoul>
  <exc>         -4.40143484 </exc>
  <esr>          0.06850943 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37385331 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37385331 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70509690 0.00000000 -0.00000011 </position>
    <velocity> 0.00001792 0.00000000 0.00000000 </velocity>
    <force> 0.00041826 -0.00000006 0.00000115 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23363346 0.00000012 </position>
    <velocity> -0.00000000 0.00013179 -0.00000000 </velocity>
    <force> 0.00000007 0.00998118 -0.00000108 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70509690 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001792 -0.00000000 0.00000000 </velocity>
    <force> -0.00041826 0.00000006 0.00000106 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23363346 0.00000010 </position>
    <velocity> 0.00000000 -0.00013179 -0.00000000 </velocity>
    <force> -0.00000008 -0.00998119 -0.00000127 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000241 </ekin_e>
  <ekin_ion> 0.00090572 </ekin_ion>
  <temp_ion> 47.66979362 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294276 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.037" max="    0.037"/>
<iteration count="118">
  <ekin>         5.31940076 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46212403 </eps>
  <enl>          4.77227177 </enl>
  <ecoul>      -15.60215302 </ecoul>
  <exc>         -4.40125937 </exc>
  <esr>          0.06843745 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37386389 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37386389 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70516878 0.00000000 -0.00000010 </position>
    <velocity> 0.00001795 0.00000000 0.00000000 </velocity>
    <force> 0.00038106 -0.00000006 0.00000107 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23416528 0.00000011 </position>
    <velocity> -0.00000000 0.00013257 -0.00000000 </velocity>
    <force> 0.00000008 0.00987247 -0.00000105 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70516878 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001795 -0.00000000 0.00000000 </velocity>
    <force> -0.00038107 0.00000007 0.00000099 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23416528 0.00000010 </position>
    <velocity> 0.00000000 -0.00013257 -0.00000000 </velocity>
    <force> -0.00000008 -0.00987247 -0.00000114 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000244 </ekin_e>
  <ekin_ion> 0.00091628 </ekin_ion>
  <temp_ion> 48.22529855 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294274 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="119">
  <ekin>         5.31895813 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46183421 </eps>
  <enl>          4.77223047 </enl>
  <ecoul>      -15.60214559 </ecoul>
  <exc>         -4.40108321 </exc>
  <esr>          0.06836517 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37387441 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37387441 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70524076 0.00000000 -0.00000010 </position>
    <velocity> 0.00001798 0.00000000 0.00000000 </velocity>
    <force> 0.00034367 -0.00000006 0.00000098 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23470015 0.00000011 </position>
    <velocity> -0.00000000 0.00013334 -0.00000000 </velocity>
    <force> 0.00000008 0.00976307 -0.00000101 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70524076 -0.00000000 -0.00000009 </position>
    <velocity> -0.00001798 -0.00000000 0.00000000 </velocity>
    <force> -0.00034370 0.00000007 0.00000092 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23470015 0.00000009 </position>
    <velocity> -0.00000000 -0.00013334 -0.00000000 </velocity>
    <force> -0.00000008 -0.00976307 -0.00000100 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000247 </ekin_e>
  <ekin_ion> 0.00092677 </ekin_ion>
  <temp_ion> 48.77764517 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294271 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="120">
  <ekin>         5.31851344 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46154395 </eps>
  <enl>          4.77219013 </enl>
  <ecoul>      -15.60213823 </ecoul>
  <exc>         -4.40090627 </exc>
  <esr>          0.06829260 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37388488 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37388488 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70531284 0.00000000 -0.00000009 </position>
    <velocity> 0.00001801 -0.00000000 0.00000000 </velocity>
    <force> 0.00030632 -0.00000006 0.00000089 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23523804 0.00000011 </position>
    <velocity> -0.00000000 0.00013410 -0.00000000 </velocity>
    <force> 0.00000008 0.00965343 -0.00000096 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70531284 -0.00000000 -0.00000009 </position>
    <velocity> -0.00001801 -0.00000000 0.00000000 </velocity>
    <force> -0.00030635 0.00000007 0.00000084 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23523804 0.00000009 </position>
    <velocity> -0.00000000 -0.00013410 -0.00000000 </velocity>
    <force> -0.00000008 -0.00965344 -0.00000086 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000250 </ekin_e>
  <ekin_ion> 0.00093720 </ekin_ion>
  <temp_ion> 49.32669989 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294267 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="121">
  <ekin>         5.31806645 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46125323 </eps>
  <enl>          4.77215077 </enl>
  <ecoul>      -15.60213084 </ecoul>
  <exc>         -4.40072844 </exc>
  <esr>          0.06821976 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37389528 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37389528 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70538501 0.00000000 -0.00000009 </position>
    <velocity> 0.00001803 -0.00000000 0.00000000 </velocity>
    <force> 0.00026921 -0.00000006 0.00000078 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23577892 0.00000010 </position>
    <velocity> 0.00000000 0.00013485 -0.00000000 </velocity>
    <force> 0.00000008 0.00954399 -0.00000090 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70538501 -0.00000000 -0.00000009 </position>
    <velocity> -0.00001803 0.00000000 0.00000000 </velocity>
    <force> -0.00026926 0.00000007 0.00000075 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23577892 0.00000008 </position>
    <velocity> -0.00000000 -0.00013485 -0.00000000 </velocity>
    <force> -0.00000008 -0.00954400 -0.00000071 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000254 </ekin_e>
  <ekin_ion> 0.00094757 </ekin_ion>
  <temp_ion> 49.87235659 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294264 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="122">
  <ekin>         5.31761697 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46096196 </eps>
  <enl>          4.77211233 </enl>
  <ecoul>      -15.60212332 </ecoul>
  <exc>         -4.40054965 </exc>
  <esr>          0.06814664 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37390562 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37390562 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70545725 0.00000000 -0.00000009 </position>
    <velocity> 0.00001805 -0.00000000 0.00000000 </velocity>
    <force> 0.00023254 -0.00000005 0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23632274 0.00000010 </position>
    <velocity> 0.00000000 0.00013559 -0.00000000 </velocity>
    <force> 0.00000008 0.00943508 -0.00000084 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70545725 -0.00000000 -0.00000008 </position>
    <velocity> -0.00001805 0.00000000 0.00000000 </velocity>
    <force> -0.00023259 0.00000007 0.00000066 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23632274 0.00000008 </position>
    <velocity> -0.00000000 -0.00013559 -0.00000000 </velocity>
    <force> -0.00000008 -0.00943509 -0.00000055 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000257 </ekin_e>
  <ekin_ion> 0.00095787 </ekin_ion>
  <temp_ion> 50.41453378 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294260 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="123">
  <ekin>         5.31716490 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46067000 </eps>
  <enl>          4.77207464 </enl>
  <ecoul>      -15.60211558 </ecoul>
  <exc>         -4.40036985 </exc>
  <esr>          0.06807326 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37391589 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37391589 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70552955 0.00000000 -0.00000008 </position>
    <velocity> 0.00001807 -0.00000000 0.00000000 </velocity>
    <force> 0.00019638 -0.00000005 0.00000054 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23686948 0.00000010 </position>
    <velocity> 0.00000000 0.00013632 -0.00000000 </velocity>
    <force> 0.00000008 0.00932689 -0.00000077 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70552955 -0.00000000 -0.00000008 </position>
    <velocity> -0.00001807 0.00000000 0.00000000 </velocity>
    <force> -0.00019644 0.00000007 0.00000056 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23686948 0.00000007 </position>
    <velocity> -0.00000000 -0.00013632 -0.00000000 </velocity>
    <force> -0.00000007 -0.00932690 -0.00000039 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000261 </ekin_e>
  <ekin_ion> 0.00096811 </ekin_ion>
  <temp_ion> 50.95316762 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294256 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="124">
  <ekin>         5.31671027 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46037719 </eps>
  <enl>          4.77203746 </enl>
  <ecoul>      -15.60210759 </ecoul>
  <exc>         -4.40018904 </exc>
  <esr>          0.06799962 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37392610 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37392610 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70560190 0.00000000 -0.00000008 </position>
    <velocity> 0.00001808 -0.00000000 0.00000000 </velocity>
    <force> 0.00016071 -0.00000005 0.00000042 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23741909 0.00000009 </position>
    <velocity> 0.00000000 0.00013704 -0.00000000 </velocity>
    <force> 0.00000008 0.00921942 -0.00000070 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70560190 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001808 0.00000000 0.00000000 </velocity>
    <force> -0.00016078 0.00000007 0.00000047 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23741909 0.00000006 </position>
    <velocity> -0.00000000 -0.00013704 -0.00000000 </velocity>
    <force> -0.00000007 -0.00921943 -0.00000024 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000265 </ekin_e>
  <ekin_ion> 0.00097827 </ekin_ion>
  <temp_ion> 51.48820225 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294253 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="125">
  <ekin>         5.31625322 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.46008338 </eps>
  <enl>          4.77200054 </enl>
  <ecoul>      -15.60209935 </ecoul>
  <exc>         -4.40000726 </exc>
  <esr>          0.06792572 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37393623 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37393623 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70567429 0.00000000 -0.00000007 </position>
    <velocity> 0.00001809 -0.00000000 0.00000000 </velocity>
    <force> 0.00012540 -0.00000004 0.00000030 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23797156 0.00000009 </position>
    <velocity> 0.00000000 0.00013776 -0.00000000 </velocity>
    <force> 0.00000007 0.00911251 -0.00000062 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70567429 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001809 0.00000000 0.00000000 </velocity>
    <force> -0.00012547 0.00000006 0.00000036 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23797156 0.00000006 </position>
    <velocity> -0.00000000 -0.00013776 -0.00000000 </velocity>
    <force> -0.00000006 -0.00911252 -0.00000008 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000268 </ekin_e>
  <ekin_ion> 0.00098837 </ekin_ion>
  <temp_ion> 52.01957879 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294249 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="126">
  <ekin>         5.31579400 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45978854 </eps>
  <enl>          4.77196374 </enl>
  <ecoul>      -15.60209091 </ecoul>
  <exc>         -4.39982458 </exc>
  <esr>          0.06785158 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37394628 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37394628 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70574670 0.00000000 -0.00000007 </position>
    <velocity> 0.00001810 -0.00000000 0.00000000 </velocity>
    <force> 0.00009022 -0.00000003 0.00000017 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23852684 0.00000008 </position>
    <velocity> 0.00000000 0.00013847 -0.00000000 </velocity>
    <force> 0.00000007 0.00900585 -0.00000053 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70574670 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001810 0.00000000 0.00000000 </velocity>
    <force> -0.00009030 0.00000006 0.00000025 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23852684 0.00000005 </position>
    <velocity> -0.00000000 -0.00013847 -0.00000000 </velocity>
    <force> -0.00000005 -0.00900586 0.00000008 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000272 </ekin_e>
  <ekin_ion> 0.00099839 </ekin_ion>
  <temp_ion> 52.54722520 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294246 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="127">
  <ekin>         5.31533290 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45949273 </eps>
  <enl>          4.77192703 </enl>
  <ecoul>      -15.60208236 </ecoul>
  <exc>         -4.39964110 </exc>
  <esr>          0.06777719 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37395627 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37395627 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70581914 0.00000000 -0.00000006 </position>
    <velocity> 0.00001811 -0.00000000 0.00000000 </velocity>
    <force> 0.00005491 -0.00000003 0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23908490 0.00000008 </position>
    <velocity> 0.00000000 0.00013917 -0.00000000 </velocity>
    <force> 0.00000006 0.00889904 -0.00000044 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70581914 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001811 0.00000000 0.00000000 </velocity>
    <force> -0.00005499 0.00000005 0.00000014 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23908490 0.00000005 </position>
    <velocity> -0.00000000 -0.00013917 -0.00000000 </velocity>
    <force> -0.00000004 -0.00889905 0.00000023 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000274 </ekin_e>
  <ekin_ion> 0.00100835 </ekin_ion>
  <temp_ion> 53.07104843 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294243 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="128">
  <ekin>         5.31487019 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45919616 </eps>
  <enl>          4.77189057 </enl>
  <ecoul>      -15.60207384 </ecoul>
  <exc>         -4.39945693 </exc>
  <esr>          0.06770257 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37396617 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37396617 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70589158 0.00000000 -0.00000006 </position>
    <velocity> 0.00001811 -0.00000000 0.00000000 </velocity>
    <force> 0.00001920 -0.00000002 -0.00000007 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.23964571 0.00000007 </position>
    <velocity> 0.00000000 0.00013986 -0.00000000 </velocity>
    <force> 0.00000005 0.00879165 -0.00000033 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70589158 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001811 0.00000000 0.00000000 </velocity>
    <force> -0.00001928 0.00000004 0.00000003 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.23964571 0.00000004 </position>
    <velocity> -0.00000000 -0.00013986 -0.00000000 </velocity>
    <force> -0.00000003 -0.00879167 0.00000037 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000277 </ekin_e>
  <ekin_ion> 0.00101822 </ekin_ion>
  <temp_ion> 53.59093059 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294241 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="129">
  <ekin>         5.31440609 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45889910 </eps>
  <enl>          4.77185461 </enl>
  <ecoul>      -15.60206545 </ecoul>
  <exc>         -4.39927215 </exc>
  <esr>          0.06762773 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37397599 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37397599 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70596401 0.00000000 -0.00000005 </position>
    <velocity> 0.00001811 -0.00000000 0.00000000 </velocity>
    <force> -0.00001712 -0.00000001 -0.00000018 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24020923 0.00000007 </position>
    <velocity> 0.00000000 0.00014054 -0.00000000 </velocity>
    <force> 0.00000004 0.00868333 -0.00000023 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70596401 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001811 0.00000000 0.00000000 </velocity>
    <force> 0.00001705 0.00000003 -0.00000008 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24020923 0.00000004 </position>
    <velocity> -0.00000000 -0.00014054 -0.00000000 </velocity>
    <force> -0.00000002 -0.00868335 0.00000051 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000279 </ekin_e>
  <ekin_ion> 0.00102802 </ekin_ion>
  <temp_ion> 54.10672967 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294238 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="130">
  <ekin>         5.31394072 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45860178 </eps>
  <enl>          4.77181942 </enl>
  <ecoul>      -15.60205727 </ecoul>
  <exc>         -4.39908682 </exc>
  <esr>          0.06755266 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37398573 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37398573 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70603643 0.00000000 -0.00000005 </position>
    <velocity> 0.00001811 -0.00000000 0.00000000 </velocity>
    <force> -0.00005417 -0.00000001 -0.00000030 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24077544 0.00000006 </position>
    <velocity> 0.00000000 0.00014122 -0.00000000 </velocity>
    <force> 0.00000003 0.00857385 -0.00000012 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70603643 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001811 0.00000000 0.00000000 </velocity>
    <force> 0.00005410 0.00000002 -0.00000020 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24077544 0.00000003 </position>
    <velocity> -0.00000000 -0.00014122 -0.00000000 </velocity>
    <force> -0.00000001 -0.00857386 0.00000064 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000281 </ekin_e>
  <ekin_ion> 0.00103774 </ekin_ion>
  <temp_ion> 54.61828517 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294236 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="131">
  <ekin>         5.31347412 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45830433 </eps>
  <enl>          4.77178512 </enl>
  <ecoul>      -15.60204934 </ecoul>
  <exc>         -4.39890095 </exc>
  <esr>          0.06747738 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37399539 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37399539 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70610882 0.00000000 -0.00000004 </position>
    <velocity> 0.00001810 -0.00000000 0.00000000 </velocity>
    <force> -0.00009194 0.00000000 -0.00000041 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24134428 0.00000006 </position>
    <velocity> 0.00000000 0.00014188 -0.00000000 </velocity>
    <force> 0.00000002 0.00846314 0.00000000 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70610882 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001810 0.00000000 0.00000000 </velocity>
    <force> 0.00009187 0.00000001 -0.00000031 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24134428 0.00000003 </position>
    <velocity> -0.00000000 -0.00014188 -0.00000000 </velocity>
    <force> 0.00000000 -0.00846315 0.00000077 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000283 </ekin_e>
  <ekin_ion> 0.00104738 </ekin_ion>
  <temp_ion> 55.12542740 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294235 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="132">
  <ekin>         5.31300625 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45800669 </eps>
  <enl>          4.77175161 </enl>
  <ecoul>      -15.60204159 </ecoul>
  <exc>         -4.39871453 </exc>
  <esr>          0.06740189 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37400495 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37400495 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70618117 0.00000000 -0.00000004 </position>
    <velocity> 0.00001809 -0.00000000 0.00000000 </velocity>
    <force> -0.00013029 0.00000001 -0.00000052 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24191574 0.00000005 </position>
    <velocity> 0.00000000 0.00014254 -0.00000000 </velocity>
    <force> 0.00000001 0.00835132 0.00000012 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70618117 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001809 0.00000000 0.00000000 </velocity>
    <force> 0.00013023 0.00000001 -0.00000043 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24191574 0.00000002 </position>
    <velocity> -0.00000000 -0.00014254 -0.00000000 </velocity>
    <force> 0.00000001 -0.00835133 0.00000089 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000285 </ekin_e>
  <ekin_ion> 0.00105693 </ekin_ion>
  <temp_ion> 55.62798889 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294233 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="133">
  <ekin>         5.31253701 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45770858 </eps>
  <enl>          4.77171853 </enl>
  <ecoul>      -15.60203389 </ecoul>
  <exc>         -4.39852751 </exc>
  <esr>          0.06732620 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37401443 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37401443 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70625347 0.00000000 -0.00000003 </position>
    <velocity> 0.00001808 -0.00000000 0.00000000 </velocity>
    <force> -0.00016901 0.00000002 -0.00000063 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24248977 0.00000005 </position>
    <velocity> 0.00000000 0.00014319 -0.00000000 </velocity>
    <force> 0.00000000 0.00823865 0.00000024 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70625347 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001808 0.00000000 0.00000000 </velocity>
    <force> 0.00016895 -0.00000000 -0.00000053 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24248977 0.00000002 </position>
    <velocity> -0.00000000 -0.00014319 -0.00000000 </velocity>
    <force> 0.00000002 -0.00823866 0.00000100 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000287 </ekin_e>
  <ekin_ion> 0.00106639 </ekin_ion>
  <temp_ion> 56.12581531 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294231 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="134">
  <ekin>         5.31206632 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45740955 </eps>
  <enl>          4.77168530 </enl>
  <ecoul>      -15.60202607 </ecoul>
  <exc>         -4.39833982 </exc>
  <esr>          0.06725032 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37402382 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37402382 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70632570 0.00000000 -0.00000003 </position>
    <velocity> 0.00001807 -0.00000000 0.00000000 </velocity>
    <force> -0.00020783 0.00000002 -0.00000074 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24306634 0.00000004 </position>
    <velocity> 0.00000000 0.00014383 -0.00000000 </velocity>
    <force> -0.00000001 0.00812551 0.00000036 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70632570 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001807 0.00000000 0.00000000 </velocity>
    <force> 0.00020778 -0.00000001 -0.00000064 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24306634 0.00000001 </position>
    <velocity> -0.00000000 -0.00014383 -0.00000000 </velocity>
    <force> 0.00000003 -0.00812552 0.00000110 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000289 </ekin_e>
  <ekin_ion> 0.00107575 </ekin_ion>
  <temp_ion> 56.61877354 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294229 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="135">
  <ekin>         5.31159408 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45710909 </eps>
  <enl>          4.77165120 </enl>
  <ecoul>      -15.60201792 </ecoul>
  <exc>         -4.39815138 </exc>
  <esr>          0.06717425 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37403311 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37403311 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70639785 0.00000000 -0.00000002 </position>
    <velocity> 0.00001805 -0.00000000 0.00000000 </velocity>
    <force> -0.00024649 0.00000003 -0.00000084 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24364542 0.00000004 </position>
    <velocity> 0.00000000 0.00014446 -0.00000000 </velocity>
    <force> -0.00000002 0.00801225 0.00000048 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70639785 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001805 0.00000000 0.00000000 </velocity>
    <force> 0.00024645 -0.00000002 -0.00000074 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24364542 0.00000001 </position>
    <velocity> -0.00000000 -0.00014446 -0.00000000 </velocity>
    <force> 0.00000004 -0.00801225 0.00000120 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000291 </ekin_e>
  <ekin_ion> 0.00108502 </ekin_ion>
  <temp_ion> 57.10675509 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294227 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="136">
  <ekin>         5.31112025 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45680671 </eps>
  <enl>          4.77161557 </enl>
  <ecoul>      -15.60200927 </ecoul>
  <exc>         -4.39796214 </exc>
  <esr>          0.06709800 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37404231 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37404231 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70646992 0.00000000 -0.00000002 </position>
    <velocity> 0.00001803 -0.00000000 0.00000000 </velocity>
    <force> -0.00028481 0.00000003 -0.00000094 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24422696 0.00000004 </position>
    <velocity> 0.00000000 0.00014508 -0.00000000 </velocity>
    <force> -0.00000003 0.00789915 0.00000060 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70646992 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001803 0.00000000 0.00000000 </velocity>
    <force> 0.00028478 -0.00000003 -0.00000083 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.24422696 0.00000001 </position>
    <velocity> -0.00000000 -0.00014508 -0.00000000 </velocity>
    <force> 0.00000005 -0.00789915 0.00000128 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000293 </ekin_e>
  <ekin_ion> 0.00109420 </ekin_ion>
  <temp_ion> 57.58967406 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294224 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="137">
  <ekin>         5.31064479 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45650207 </eps>
  <enl>          4.77157793 </enl>
  <ecoul>      -15.60199999 </ecoul>
  <exc>         -4.39777207 </exc>
  <esr>          0.06702157 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37405141 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37405141 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70654188 0.00000000 -0.00000002 </position>
    <velocity> 0.00001800 -0.00000000 0.00000000 </velocity>
    <force> -0.00032267 0.00000004 -0.00000103 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24481094 0.00000003 </position>
    <velocity> 0.00000000 0.00014569 -0.00000000 </velocity>
    <force> -0.00000004 0.00778637 0.00000072 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70654188 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001800 0.00000000 0.00000000 </velocity>
    <force> 0.00032265 -0.00000004 -0.00000092 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24481094 0.00000000 </position>
    <velocity> -0.00000000 -0.00014569 -0.00000000 </velocity>
    <force> 0.00000006 -0.00778637 0.00000135 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000296 </ekin_e>
  <ekin_ion> 0.00110328 </ekin_ion>
  <temp_ion> 58.06746026 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294222 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="138">
  <ekin>         5.31016772 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45619507 </eps>
  <enl>          4.77153811 </enl>
  <ecoul>      -15.60199002 </ecoul>
  <exc>         -4.39758115 </exc>
  <esr>          0.06694497 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37406041 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37406041 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70661373 0.00000000 -0.00000001 </position>
    <velocity> 0.00001798 -0.00000000 0.00000000 </velocity>
    <force> -0.00036008 0.00000004 -0.00000111 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24539732 0.00000003 </position>
    <velocity> 0.00000000 0.00014629 -0.00000000 </velocity>
    <force> -0.00000005 0.00767387 0.00000083 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70661373 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001798 0.00000000 0.00000000 </velocity>
    <force> 0.00036008 -0.00000005 -0.00000100 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24539732 0.00000000 </position>
    <velocity> -0.00000000 -0.00014629 -0.00000000 </velocity>
    <force> 0.00000006 -0.00767387 0.00000140 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000298 </ekin_e>
  <ekin_ion> 0.00111226 </ekin_ion>
  <temp_ion> 58.54004942 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294220 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="139">
  <ekin>         5.30968904 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45588589 </eps>
  <enl>          4.77149632 </enl>
  <ecoul>      -15.60197939 </ecoul>
  <exc>         -4.39738940 </exc>
  <esr>          0.06686822 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37406931 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37406931 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70668546 0.00000000 -0.00000001 </position>
    <velocity> 0.00001795 -0.00000000 0.00000000 </velocity>
    <force> -0.00039714 0.00000005 -0.00000118 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.24598605 0.00000002 </position>
    <velocity> 0.00000000 0.00014689 -0.00000000 </velocity>
    <force> -0.00000006 0.00756151 0.00000094 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70668546 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001795 0.00000000 0.00000000 </velocity>
    <force> 0.00039715 -0.00000006 -0.00000108 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24598605 -0.00000000 </position>
    <velocity> -0.00000000 -0.00014689 -0.00000000 </velocity>
    <force> 0.00000007 -0.00756151 0.00000145 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000300 </ekin_e>
  <ekin_ion> 0.00112114 </ekin_ion>
  <temp_ion> 59.00737296 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294218 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="140">
  <ekin>         5.30920879 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45557491 </eps>
  <enl>          4.77145310 </enl>
  <ecoul>      -15.60196820 </ecoul>
  <exc>         -4.39719688 </exc>
  <esr>          0.06679130 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37407811 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37407811 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70675705 0.00000000 -0.00000001 </position>
    <velocity> 0.00001791 -0.00000000 0.00000000 </velocity>
    <force> -0.00043400 0.00000005 -0.00000124 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.24657712 0.00000002 </position>
    <velocity> 0.00000000 0.00014748 -0.00000000 </velocity>
    <force> -0.00000007 0.00744902 0.00000104 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70675705 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001791 0.00000000 0.00000000 </velocity>
    <force> 0.00043402 -0.00000006 -0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24657712 -0.00000000 </position>
    <velocity> -0.00000000 -0.00014748 -0.00000000 </velocity>
    <force> 0.00000007 -0.00744902 0.00000148 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000302 </ekin_e>
  <ekin_ion> 0.00112991 </ekin_ion>
  <temp_ion> 59.46934996 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294216 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="141">
  <ekin>         5.30872696 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45526271 </eps>
  <enl>          4.77140919 </enl>
  <ecoul>      -15.60195660 </ecoul>
  <exc>         -4.39700364 </exc>
  <esr>          0.06671424 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37408680 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37408680 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70682849 0.00000000 -0.00000001 </position>
    <velocity> 0.00001788 -0.00000000 0.00000000 </velocity>
    <force> -0.00047084 0.00000005 -0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.24717048 0.00000002 </position>
    <velocity> 0.00000000 0.00014805 -0.00000000 </velocity>
    <force> -0.00000008 0.00733614 0.00000114 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70682850 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001788 0.00000000 0.00000000 </velocity>
    <force> 0.00047086 -0.00000006 -0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24717048 -0.00000000 </position>
    <velocity> -0.00000000 -0.00014805 -0.00000000 </velocity>
    <force> 0.00000008 -0.00733613 0.00000149 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000304 </ekin_e>
  <ekin_ion> 0.00113859 </ekin_ion>
  <temp_ion> 59.92588317 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294214 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="142">
  <ekin>         5.30824358 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45494988 </eps>
  <enl>          4.77136541 </enl>
  <ecoul>      -15.60194476 </ecoul>
  <exc>         -4.39680974 </exc>
  <esr>          0.06663704 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37409539 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37409539 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70689978 0.00000000 -0.00000001 </position>
    <velocity> 0.00001784 -0.00000000 0.00000000 </velocity>
    <force> -0.00050782 0.00000005 -0.00000134 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.24776610 0.00000002 </position>
    <velocity> 0.00000000 0.00014862 -0.00000000 </velocity>
    <force> -0.00000008 0.00722263 0.00000123 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70689978 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001784 0.00000000 0.00000000 </velocity>
    <force> 0.00050785 -0.00000007 -0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24776610 -0.00000001 </position>
    <velocity> -0.00000000 -0.00014862 -0.00000000 </velocity>
    <force> 0.00000008 -0.00722262 0.00000150 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000305 </ekin_e>
  <ekin_ion> 0.00114716 </ekin_ion>
  <temp_ion> 60.37685968 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294212 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="143">
  <ekin>         5.30775864 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45463693 </eps>
  <enl>          4.77132250 </enl>
  <ecoul>      -15.60193283 </ecoul>
  <exc>         -4.39661524 </exc>
  <esr>          0.06655970 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37410386 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37410386 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70697090 0.00000000 -0.00000000 </position>
    <velocity> 0.00001780 -0.00000000 0.00000000 </velocity>
    <force> -0.00054505 0.00000005 -0.00000137 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.24836393 0.00000001 </position>
    <velocity> 0.00000000 0.00014918 -0.00000000 </velocity>
    <force> -0.00000008 0.00710838 0.00000131 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70697090 0.00000000 -0.00000000 </position>
    <velocity> -0.00001780 0.00000000 0.00000000 </velocity>
    <force> 0.00054509 -0.00000007 -0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24836394 -0.00000001 </position>
    <velocity> -0.00000000 -0.00014918 -0.00000000 </velocity>
    <force> 0.00000008 -0.00710837 0.00000149 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000307 </ekin_e>
  <ekin_ion> 0.00115562 </ekin_ion>
  <temp_ion> 60.82215587 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294211 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="144">
  <ekin>         5.30727220 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45432425 </eps>
  <enl>          4.77128096 </enl>
  <ecoul>      -15.60192095 </ecoul>
  <exc>         -4.39642019 </exc>
  <esr>          0.06648223 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37411223 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37411223 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70704183 0.00000000 -0.00000000 </position>
    <velocity> 0.00001776 0.00000000 0.00000000 </velocity>
    <force> -0.00058260 0.00000005 -0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.24896396 0.00000001 </position>
    <velocity> 0.00000000 0.00014973 -0.00000000 </velocity>
    <force> -0.00000009 0.00699341 0.00000139 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70704183 0.00000000 -0.00000000 </position>
    <velocity> -0.00001776 0.00000000 0.00000000 </velocity>
    <force> 0.00058265 -0.00000007 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24896396 -0.00000000 </position>
    <velocity> 0.00000000 -0.00014973 0.00000000 </velocity>
    <force> 0.00000008 -0.00699340 0.00000147 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000308 </ekin_e>
  <ekin_ion> 0.00116397 </ekin_ion>
  <temp_ion> 61.26164491 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294209 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="145">
  <ekin>         5.30678433 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45401196 </eps>
  <enl>          4.77124096 </enl>
  <ecoul>      -15.60190918 </ecoul>
  <exc>         -4.39622464 </exc>
  <esr>          0.06640463 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37412048 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37412048 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70711257 0.00000000 -0.00000000 </position>
    <velocity> 0.00001771 0.00000000 0.00000000 </velocity>
    <force> -0.00062050 0.00000005 -0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.24956613 0.00000001 </position>
    <velocity> -0.00000000 0.00015027 -0.00000000 </velocity>
    <force> -0.00000009 0.00687785 0.00000145 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70711257 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001771 -0.00000000 0.00000000 </velocity>
    <force> 0.00062055 -0.00000007 -0.00000137 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.24956613 -0.00000000 </position>
    <velocity> 0.00000000 -0.00015027 0.00000000 </velocity>
    <force> 0.00000008 -0.00687783 0.00000144 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000310 </ekin_e>
  <ekin_ion> 0.00117220 </ekin_ion>
  <temp_ion> 61.69520493 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294208 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="146">
  <ekin>         5.30629520 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45370000 </eps>
  <enl>          4.77120236 </enl>
  <ecoul>      -15.60189754 </ecoul>
  <exc>         -4.39602863 </exc>
  <esr>          0.06632692 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37412862 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37412862 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70718310 0.00000000 -0.00000000 </position>
    <velocity> 0.00001766 0.00000000 -0.00000000 </velocity>
    <force> -0.00065871 0.00000005 -0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.25017042 0.00000001 </position>
    <velocity> -0.00000000 0.00015081 -0.00000000 </velocity>
    <force> -0.00000009 0.00676190 0.00000151 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70718310 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001766 -0.00000000 0.00000000 </velocity>
    <force> 0.00065877 -0.00000007 -0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.25017042 -0.00000000 </position>
    <velocity> 0.00000000 -0.00015081 0.00000000 </velocity>
    <force> 0.00000007 -0.00676188 0.00000140 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000312 </ekin_e>
  <ekin_ion> 0.00118033 </ekin_ion>
  <temp_ion> 62.12272560 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294206 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="147">
  <ekin>         5.30580500 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45338813 </eps>
  <enl>          4.77116471 </enl>
  <ecoul>      -15.60188601 </ecoul>
  <exc>         -4.39583221 </exc>
  <esr>          0.06624910 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37413665 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37413665 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70725342 0.00000000 -0.00000001 </position>
    <velocity> 0.00001761 0.00000000 -0.00000000 </velocity>
    <force> -0.00069721 0.00000005 -0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.25077678 0.00000001 </position>
    <velocity> -0.00000000 0.00015133 -0.00000000 </velocity>
    <force> -0.00000008 0.00664579 0.00000155 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70725342 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001761 -0.00000000 -0.00000000 </velocity>
    <force> 0.00069728 -0.00000007 -0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.25077678 -0.00000000 </position>
    <velocity> 0.00000000 -0.00015133 0.00000000 </velocity>
    <force> 0.00000007 -0.00664578 0.00000135 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000314 </ekin_e>
  <ekin_ion> 0.00118833 </ekin_ion>
  <temp_ion> 62.54411207 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294204 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="148">
  <ekin>         5.30531400 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45307598 </eps>
  <enl>          4.77112739 </enl>
  <ecoul>      -15.60187455 </ecoul>
  <exc>         -4.39563542 </exc>
  <esr>          0.06617118 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37414456 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37414456 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70732350 0.00000000 -0.00000001 </position>
    <velocity> 0.00001755 0.00000000 -0.00000000 </velocity>
    <force> -0.00073595 0.00000005 -0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.25138518 0.00000001 </position>
    <velocity> -0.00000000 0.00015185 -0.00000000 </velocity>
    <force> -0.00000008 0.00652975 0.00000159 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70732351 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001755 -0.00000000 -0.00000000 </velocity>
    <force> 0.00073602 -0.00000007 -0.00000137 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.25138519 0.00000000 </position>
    <velocity> 0.00000000 -0.00015185 0.00000000 </velocity>
    <force> 0.00000006 -0.00652974 0.00000129 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000316 </ekin_e>
  <ekin_ion> 0.00119622 </ekin_ion>
  <temp_ion> 62.95928528 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294202 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="149">
  <ekin>         5.30482246 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45276324 </eps>
  <enl>          4.77108981 </enl>
  <ecoul>      -15.60186309 </ecoul>
  <exc>         -4.39543829 </exc>
  <esr>          0.06609315 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37415235 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37415235 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70739335 0.00000000 -0.00000001 </position>
    <velocity> 0.00001749 0.00000000 -0.00000000 </velocity>
    <force> -0.00077486 0.00000004 -0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25199559 0.00000001 </position>
    <velocity> -0.00000000 0.00015235 0.00000000 </velocity>
    <force> -0.00000008 0.00641390 0.00000161 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70739335 -0.00000000 -0.00000000 </position>
    <velocity> -0.00001749 -0.00000000 -0.00000000 </velocity>
    <force> 0.00077493 -0.00000006 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25199559 0.00000000 </position>
    <velocity> 0.00000000 -0.00015235 0.00000000 </velocity>
    <force> 0.00000005 -0.00641389 0.00000122 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000318 </ekin_e>
  <ekin_ion> 0.00120399 </ekin_ion>
  <temp_ion> 63.36817908 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294200 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="150">
  <ekin>         5.30433061 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45244965 </eps>
  <enl>          4.77105147 </enl>
  <ecoul>      -15.60185158 </ecoul>
  <exc>         -4.39524086 </exc>
  <esr>          0.06601504 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37416002 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37416002 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70746294 0.00000000 -0.00000001 </position>
    <velocity> 0.00001743 0.00000000 -0.00000000 </velocity>
    <force> -0.00081390 0.00000004 -0.00000125 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25260797 0.00000001 </position>
    <velocity> -0.00000000 0.00015285 0.00000000 </velocity>
    <force> -0.00000007 0.00629828 0.00000161 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70746294 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001743 -0.00000000 -0.00000000 </velocity>
    <force> 0.00081396 -0.00000006 -0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25260797 0.00000001 </position>
    <velocity> 0.00000000 -0.00015285 0.00000000 </velocity>
    <force> 0.00000005 -0.00629827 0.00000115 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000320 </ekin_e>
  <ekin_ion> 0.00121164 </ekin_ion>
  <temp_ion> 63.77073498 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294198 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.011" max="    0.011"/>
<iteration count="151">
  <ekin>         5.30383857 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45213515 </eps>
  <enl>          4.77101217 </enl>
  <ecoul>      -15.60184000 </ecoul>
  <exc>         -4.39504315 </exc>
  <esr>          0.06593684 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37416757 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37416757 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70753226 0.00000000 -0.00000001 </position>
    <velocity> 0.00001736 0.00000000 -0.00000000 </velocity>
    <force> -0.00085298 0.00000003 -0.00000121 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25322228 0.00000001 </position>
    <velocity> -0.00000000 0.00015334 0.00000000 </velocity>
    <force> -0.00000006 0.00618284 0.00000160 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70753226 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001736 -0.00000000 -0.00000000 </velocity>
    <force> 0.00085304 -0.00000005 -0.00000128 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25322228 0.00000001 </position>
    <velocity> 0.00000000 -0.00015334 0.00000000 </velocity>
    <force> 0.00000004 -0.00618283 0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000322 </ekin_e>
  <ekin_ion> 0.00121917 </ekin_ion>
  <temp_ion> 64.16689591 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294196 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="152">
  <ekin>         5.30334634 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45181985 </eps>
  <enl>          4.77097202 </enl>
  <ecoul>      -15.60182833 </ecoul>
  <exc>         -4.39484517 </exc>
  <esr>          0.06585856 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37417499 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37417499 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70760130 0.00000000 -0.00000002 </position>
    <velocity> 0.00001730 0.00000000 -0.00000000 </velocity>
    <force> -0.00089203 0.00000003 -0.00000115 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25383848 0.00000002 </position>
    <velocity> -0.00000000 0.00015381 0.00000000 </velocity>
    <force> -0.00000005 0.00606743 0.00000158 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70760131 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001730 -0.00000000 -0.00000000 </velocity>
    <force> 0.00089210 -0.00000004 -0.00000124 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25383848 0.00000001 </position>
    <velocity> 0.00000000 -0.00015381 0.00000000 </velocity>
    <force> 0.00000003 -0.00606742 0.00000098 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000324 </ekin_e>
  <ekin_ion> 0.00122657 </ekin_ion>
  <temp_ion> 64.55660060 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294194 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="153">
  <ekin>         5.30285377 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45150403 </eps>
  <enl>          4.77093143 </enl>
  <ecoul>      -15.60181658 </ecoul>
  <exc>         -4.39464689 </exc>
  <esr>          0.06578021 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37418229 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37418229 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70767006 0.00000000 -0.00000002 </position>
    <velocity> 0.00001722 0.00000000 -0.00000000 </velocity>
    <force> -0.00093097 0.00000002 -0.00000110 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25445655 0.00000002 </position>
    <velocity> -0.00000000 0.00015428 0.00000000 </velocity>
    <force> -0.00000005 0.00595188 0.00000154 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70767006 -0.00000000 -0.00000001 </position>
    <velocity> -0.00001722 -0.00000000 -0.00000000 </velocity>
    <force> 0.00093104 -0.00000003 -0.00000118 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25445655 0.00000002 </position>
    <velocity> 0.00000000 -0.00015428 0.00000000 </velocity>
    <force> 0.00000002 -0.00595187 0.00000089 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000326 </ekin_e>
  <ekin_ion> 0.00123385 </ekin_ion>
  <temp_ion> 64.93977977 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294192 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="154">
  <ekin>         5.30236061 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45118804 </eps>
  <enl>          4.77089100 </enl>
  <ecoul>      -15.60180473 </ecoul>
  <exc>         -4.39444830 </exc>
  <esr>          0.06570179 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37418947 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37418947 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70773851 0.00000000 -0.00000002 </position>
    <velocity> 0.00001715 0.00000000 -0.00000000 </velocity>
    <force> -0.00096974 0.00000001 -0.00000104 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25507644 0.00000002 </position>
    <velocity> -0.00000000 0.00015474 0.00000000 </velocity>
    <force> -0.00000004 0.00583603 0.00000148 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70773851 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001715 -0.00000000 -0.00000000 </velocity>
    <force> 0.00096979 -0.00000002 -0.00000112 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25507644 0.00000002 </position>
    <velocity> 0.00000000 -0.00015474 0.00000000 </velocity>
    <force> 0.00000001 -0.00583603 0.00000079 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000328 </ekin_e>
  <ekin_ion> 0.00124101 </ekin_ion>
  <temp_ion> 65.31635531 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294190 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="155">
  <ekin>         5.30186654 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45087226 </eps>
  <enl>          4.77085136 </enl>
  <ecoul>      -15.60179281 </ecoul>
  <exc>         -4.39424934 </exc>
  <esr>          0.06562331 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37419651 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37419651 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70780664 0.00000000 -0.00000003 </position>
    <velocity> 0.00001707 0.00000000 -0.00000000 </velocity>
    <force> -0.00100825 0.00000001 -0.00000097 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25569811 0.00000002 </position>
    <velocity> -0.00000000 0.00015520 0.00000000 </velocity>
    <force> -0.00000003 0.00571979 0.00000141 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70780664 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001707 -0.00000000 -0.00000000 </velocity>
    <force> 0.00100830 -0.00000001 -0.00000104 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25569812 0.00000002 </position>
    <velocity> 0.00000000 -0.00015520 0.00000000 </velocity>
    <force> 0.00000000 -0.00571979 0.00000069 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000330 </ekin_e>
  <ekin_ion> 0.00124803 </ekin_ion>
  <temp_ion> 65.68624252 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294188 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="156">
  <ekin>         5.30137126 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45055697 </eps>
  <enl>          4.77081304 </enl>
  <ecoul>      -15.60178080 </ecoul>
  <exc>         -4.39404997 </exc>
  <esr>          0.06554478 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37420343 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37420343 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70787445 0.00000000 -0.00000003 </position>
    <velocity> 0.00001699 0.00000000 -0.00000000 </velocity>
    <force> -0.00104646 -0.00000000 -0.00000089 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25632154 0.00000003 </position>
    <velocity> -0.00000000 0.00015564 0.00000000 </velocity>
    <force> -0.00000001 0.00560316 0.00000133 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70787445 -0.00000000 -0.00000002 </position>
    <velocity> -0.00001699 -0.00000000 -0.00000000 </velocity>
    <force> 0.00104651 -0.00000000 -0.00000096 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25632154 0.00000003 </position>
    <velocity> 0.00000000 -0.00015564 0.00000000 </velocity>
    <force> -0.00000001 -0.00560315 0.00000059 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000332 </ekin_e>
  <ekin_ion> 0.00125493 </ekin_ion>
  <temp_ion> 66.04935511 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294186 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="157">
  <ekin>         5.30087455 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.45024229 </eps>
  <enl>          4.77077633 </enl>
  <ecoul>      -15.60176868 </ecoul>
  <exc>         -4.39385013 </exc>
  <esr>          0.06546619 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37421022 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37421022 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70794192 0.00000000 -0.00000003 </position>
    <velocity> 0.00001691 0.00000000 -0.00000000 </velocity>
    <force> -0.00108436 -0.00000001 -0.00000080 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25694668 0.00000003 </position>
    <velocity> -0.00000000 0.00015607 0.00000000 </velocity>
    <force> -0.00000000 0.00548623 0.00000124 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70794192 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001691 -0.00000000 -0.00000000 </velocity>
    <force> 0.00108440 0.00000001 -0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25694669 0.00000003 </position>
    <velocity> 0.00000000 -0.00015607 0.00000000 </velocity>
    <force> -0.00000002 -0.00548623 0.00000049 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000334 </ekin_e>
  <ekin_ion> 0.00126170 </ekin_ion>
  <temp_ion> 66.40561161 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294184 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="158">
  <ekin>         5.30037636 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44992821 </eps>
  <enl>          4.77074123 </enl>
  <ecoul>      -15.60175644 </ecoul>
  <exc>         -4.39364982 </exc>
  <esr>          0.06538757 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37421688 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37421688 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70800904 0.00000000 -0.00000004 </position>
    <velocity> 0.00001682 0.00000000 -0.00000000 </velocity>
    <force> -0.00112195 -0.00000001 -0.00000070 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25757351 0.00000004 </position>
    <velocity> -0.00000000 0.00015650 0.00000000 </velocity>
    <force> 0.00000001 0.00536921 0.00000114 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70800904 -0.00000000 -0.00000003 </position>
    <velocity> -0.00001682 -0.00000000 -0.00000000 </velocity>
    <force> 0.00112197 0.00000002 -0.00000078 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25757351 0.00000004 </position>
    <velocity> 0.00000000 -0.00015650 0.00000000 </velocity>
    <force> -0.00000003 -0.00536921 0.00000038 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000336 </ekin_e>
  <ekin_ion> 0.00126834 </ekin_ion>
  <temp_ion> 66.75494155 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294182 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="159">
  <ekin>         5.29987678 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44961458 </eps>
  <enl>          4.77070747 </enl>
  <ecoul>      -15.60174406 </ecoul>
  <exc>         -4.39344901 </exc>
  <esr>          0.06530891 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37422341 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37422341 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70807579 0.00000000 -0.00000004 </position>
    <velocity> 0.00001673 0.00000000 -0.00000000 </velocity>
    <force> -0.00115924 -0.00000002 -0.00000059 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25820197 0.00000004 </position>
    <velocity> -0.00000000 0.00015691 0.00000000 </velocity>
    <force> 0.00000002 0.00525232 0.00000102 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70807579 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001673 -0.00000000 -0.00000000 </velocity>
    <force> 0.00115926 0.00000003 -0.00000067 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25820197 0.00000004 </position>
    <velocity> 0.00000000 -0.00015691 0.00000000 </velocity>
    <force> -0.00000004 -0.00525232 0.00000028 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000338 </ekin_e>
  <ekin_ion> 0.00127484 </ekin_ion>
  <temp_ion> 67.09728959 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294179 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="160">
  <ekin>         5.29937603 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44930117 </eps>
  <enl>          4.77067464 </enl>
  <ecoul>      -15.60173155 </ecoul>
  <exc>         -4.39324774 </exc>
  <esr>          0.06523022 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37422980 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37422980 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70814218 0.00000000 -0.00000005 </position>
    <velocity> 0.00001664 0.00000000 -0.00000000 </velocity>
    <force> -0.00119630 -0.00000003 -0.00000048 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25883203 0.00000005 </position>
    <velocity> -0.00000000 0.00015732 0.00000000 </velocity>
    <force> 0.00000003 0.00513577 0.00000090 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70814218 -0.00000000 -0.00000004 </position>
    <velocity> -0.00001664 -0.00000000 -0.00000000 </velocity>
    <force> 0.00119630 0.00000003 -0.00000056 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25883203 0.00000005 </position>
    <velocity> 0.00000000 -0.00015732 0.00000000 </velocity>
    <force> -0.00000005 -0.00513578 0.00000018 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000341 </ekin_e>
  <ekin_ion> 0.00128122 </ekin_ion>
  <temp_ion> 67.43261626 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294177 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="161">
  <ekin>         5.29887443 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44898778 </eps>
  <enl>          4.77064227 </enl>
  <ecoul>      -15.60171893 </ecoul>
  <exc>         -4.39304605 </exc>
  <esr>          0.06515150 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37423606 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37423606 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70820817 0.00000000 -0.00000005 </position>
    <velocity> 0.00001655 0.00000000 -0.00000000 </velocity>
    <force> -0.00123318 -0.00000003 -0.00000037 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.25946367 0.00000005 </position>
    <velocity> -0.00000000 0.00015771 0.00000000 </velocity>
    <force> 0.00000004 0.00501970 0.00000077 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70820817 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001655 -0.00000000 -0.00000000 </velocity>
    <force> 0.00123317 0.00000004 -0.00000045 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.25946367 0.00000005 </position>
    <velocity> 0.00000000 -0.00015771 0.00000000 </velocity>
    <force> -0.00000005 -0.00501971 0.00000008 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000343 </ekin_e>
  <ekin_ion> 0.00128745 </ekin_ion>
  <temp_ion> 67.76089489 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294175 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="162">
  <ekin>         5.29837232 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44867426 </eps>
  <enl>          4.77061001 </enl>
  <ecoul>      -15.60170624 </ecoul>
  <exc>         -4.39284401 </exc>
  <esr>          0.06507277 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37424218 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37424218 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70827377 0.00000000 -0.00000006 </position>
    <velocity> 0.00001645 0.00000000 -0.00000000 </velocity>
    <force> -0.00126997 -0.00000004 -0.00000025 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26009684 0.00000006 </position>
    <velocity> -0.00000000 0.00015810 0.00000000 </velocity>
    <force> 0.00000005 0.00490414 0.00000063 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70827377 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001645 -0.00000000 -0.00000000 </velocity>
    <force> 0.00126996 0.00000005 -0.00000033 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26009684 0.00000006 </position>
    <velocity> 0.00000000 -0.00015810 0.00000000 </velocity>
    <force> -0.00000006 -0.00490415 -0.00000002 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000345 </ekin_e>
  <ekin_ion> 0.00129356 </ekin_ion>
  <temp_ion> 68.08210538 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294173 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="163">
  <ekin>         5.29786999 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44836058 </eps>
  <enl>          4.77057765 </enl>
  <ecoul>      -15.60169352 </ecoul>
  <exc>         -4.39264171 </exc>
  <esr>          0.06499402 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37424817 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37424817 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70833896 0.00000000 -0.00000006 </position>
    <velocity> 0.00001635 0.00000000 -0.00000000 </velocity>
    <force> -0.00130677 -0.00000004 -0.00000013 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26073150 0.00000007 </position>
    <velocity> -0.00000000 0.00015848 0.00000000 </velocity>
    <force> 0.00000006 0.00478899 0.00000048 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70833896 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001635 -0.00000000 -0.00000000 </velocity>
    <force> 0.00130675 0.00000006 -0.00000021 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26073150 0.00000006 </position>
    <velocity> 0.00000000 -0.00015848 0.00000000 </velocity>
    <force> -0.00000007 -0.00478900 -0.00000011 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000346 </ekin_e>
  <ekin_ion> 0.00129952 </ekin_ion>
  <temp_ion> 68.39622637 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294172 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="164">
  <ekin>         5.29736765 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44804676 </eps>
  <enl>          4.77054514 </enl>
  <ecoul>      -15.60168082 </ecoul>
  <exc>         -4.39243922 </exc>
  <esr>          0.06491527 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37425401 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37425401 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70840374 0.00000000 -0.00000007 </position>
    <velocity> 0.00001625 0.00000000 -0.00000000 </velocity>
    <force> -0.00134369 -0.00000004 -0.00000002 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26136763 0.00000007 </position>
    <velocity> -0.00000000 0.00015885 0.00000000 </velocity>
    <force> 0.00000007 0.00467406 0.00000033 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70840374 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001625 -0.00000000 -0.00000000 </velocity>
    <force> 0.00134366 0.00000006 -0.00000008 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26136763 0.00000007 </position>
    <velocity> 0.00000000 -0.00015885 0.00000000 </velocity>
    <force> -0.00000007 -0.00467407 -0.00000021 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000348 </ekin_e>
  <ekin_ion> 0.00130536 </ekin_ion>
  <temp_ion> 68.70322793 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294170 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="165">
  <ekin>         5.29686542 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44773292 </eps>
  <enl>          4.77051259 </enl>
  <ecoul>      -15.60166818 </ecoul>
  <exc>         -4.39223664 </exc>
  <esr>          0.06483651 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37425972 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37425972 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70846808 0.00000000 -0.00000007 </position>
    <velocity> 0.00001614 0.00000000 -0.00000000 </velocity>
    <force> -0.00138082 -0.00000005 0.00000010 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26200518 0.00000008 </position>
    <velocity> -0.00000000 0.00015921 0.00000000 </velocity>
    <force> 0.00000008 0.00455911 0.00000017 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70846808 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001614 -0.00000000 -0.00000000 </velocity>
    <force> 0.00138078 0.00000007 0.00000004 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26200518 0.00000007 </position>
    <velocity> 0.00000000 -0.00015921 0.00000000 </velocity>
    <force> -0.00000007 -0.00455912 -0.00000030 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000349 </ekin_e>
  <ekin_ion> 0.00131105 </ekin_ion>
  <temp_ion> 69.00306689 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294169 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="166">
  <ekin>         5.29636331 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44741913 </eps>
  <enl>          4.77048013 </enl>
  <ecoul>      -15.60165560 </ecoul>
  <exc>         -4.39203401 </exc>
  <esr>          0.06475776 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37426529 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37426529 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70853197 0.00000000 -0.00000008 </position>
    <velocity> 0.00001603 0.00000000 -0.00000000 </velocity>
    <force> -0.00141825 -0.00000005 0.00000021 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26264412 0.00000008 </position>
    <velocity> -0.00000000 0.00015956 0.00000000 </velocity>
    <force> 0.00000008 0.00444393 0.00000002 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70853197 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001603 -0.00000000 -0.00000000 </velocity>
    <force> 0.00141821 0.00000007 0.00000016 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26264412 0.00000007 </position>
    <velocity> 0.00000000 -0.00015956 0.00000000 </velocity>
    <force> -0.00000007 -0.00444395 -0.00000039 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000350 </ekin_e>
  <ekin_ion> 0.00131661 </ekin_ion>
  <temp_ion> 69.29568587 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294168 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="167">
  <ekin>         5.29586131 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44710545 </eps>
  <enl>          4.77044786 </enl>
  <ecoul>      -15.60164306 </ecoul>
  <exc>         -4.39183138 </exc>
  <esr>          0.06467902 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37427072 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37427072 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70859541 0.00000000 -0.00000008 </position>
    <velocity> 0.00001592 0.00000000 -0.00000000 </velocity>
    <force> -0.00145602 -0.00000005 0.00000032 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26328441 0.00000009 </position>
    <velocity> -0.00000000 0.00015990 0.00000000 </velocity>
    <force> 0.00000009 0.00432838 -0.00000015 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70859541 -0.00000000 -0.00000008 </position>
    <velocity> -0.00001592 -0.00000000 -0.00000000 </velocity>
    <force> 0.00145597 0.00000007 0.00000028 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26328441 0.00000008 </position>
    <velocity> 0.00000000 -0.00015990 0.00000000 </velocity>
    <force> -0.00000007 -0.00432839 -0.00000047 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000351 </ekin_e>
  <ekin_ion> 0.00132203 </ekin_ion>
  <temp_ion> 69.58101626 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294167 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="168">
  <ekin>         5.29535934 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44679187 </eps>
  <enl>          4.77041581 </enl>
  <ecoul>      -15.60163054 </ecoul>
  <exc>         -4.39162876 </exc>
  <esr>          0.06460030 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37427601 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37427601 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70865839 0.00000000 -0.00000009 </position>
    <velocity> 0.00001580 0.00000000 -0.00000000 </velocity>
    <force> -0.00149413 -0.00000005 0.00000042 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26392602 0.00000010 </position>
    <velocity> -0.00000000 0.00016024 0.00000000 </velocity>
    <force> 0.00000009 0.00421240 -0.00000031 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70865839 -0.00000000 -0.00000008 </position>
    <velocity> -0.00001580 -0.00000000 -0.00000000 </velocity>
    <force> 0.00149407 0.00000007 0.00000040 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26392602 0.00000008 </position>
    <velocity> -0.00000000 -0.00016024 0.00000000 </velocity>
    <force> -0.00000007 -0.00421241 -0.00000055 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000352 </ekin_e>
  <ekin_ion> 0.00132732 </ekin_ion>
  <temp_ion> 69.85898409 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294166 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="169">
  <ekin>         5.29485736 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44647833 </eps>
  <enl>          4.77038391 </enl>
  <ecoul>      -15.60161797 </ecoul>
  <exc>         -4.39142613 </exc>
  <esr>          0.06452160 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37428116 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37428116 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70872088 0.00000000 -0.00000009 </position>
    <velocity> 0.00001568 -0.00000000 -0.00000000 </velocity>
    <force> -0.00153250 -0.00000005 0.00000053 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26456891 0.00000010 </position>
    <velocity> -0.00000000 0.00016056 0.00000000 </velocity>
    <force> 0.00000009 0.00409604 -0.00000047 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70872088 -0.00000000 -0.00000009 </position>
    <velocity> -0.00001568 0.00000000 -0.00000000 </velocity>
    <force> 0.00153244 0.00000007 0.00000051 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26456891 0.00000009 </position>
    <velocity> -0.00000000 -0.00016056 0.00000000 </velocity>
    <force> -0.00000007 -0.00409605 -0.00000063 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000352 </ekin_e>
  <ekin_ion> 0.00133246 </ekin_ion>
  <temp_ion> 70.12951689 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294166 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="170">
  <ekin>         5.29435531 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44616474 </eps>
  <enl>          4.77035204 </enl>
  <ecoul>      -15.60160531 </ecoul>
  <exc>         -4.39122346 </exc>
  <esr>          0.06444293 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37428616 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37428616 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70878289 0.00000000 -0.00000010 </position>
    <velocity> 0.00001556 -0.00000000 -0.00000000 </velocity>
    <force> -0.00157102 -0.00000005 0.00000063 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26521304 0.00000011 </position>
    <velocity> 0.00000000 0.00016088 0.00000000 </velocity>
    <force> 0.00000009 0.00397941 -0.00000062 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70878289 -0.00000000 -0.00000009 </position>
    <velocity> -0.00001556 0.00000000 -0.00000000 </velocity>
    <force> 0.00157096 0.00000007 0.00000062 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26521304 0.00000009 </position>
    <velocity> -0.00000000 -0.00016088 0.00000000 </velocity>
    <force> -0.00000007 -0.00397943 -0.00000069 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000353 </ekin_e>
  <ekin_ion> 0.00133745 </ekin_ion>
  <temp_ion> 70.39254961 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294165 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="171">
  <ekin>         5.29385318 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44585104 </eps>
  <enl>          4.77032006 </enl>
  <ecoul>      -15.60159250 </ecoul>
  <exc>         -4.39102071 </exc>
  <esr>          0.06436428 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37429102 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37429102 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70884439 0.00000000 -0.00000010 </position>
    <velocity> 0.00001544 -0.00000000 -0.00000000 </velocity>
    <force> -0.00160952 -0.00000005 0.00000073 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26585838 0.00000011 </position>
    <velocity> 0.00000000 0.00016118 0.00000000 </velocity>
    <force> 0.00000009 0.00386266 -0.00000077 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70884439 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001544 0.00000000 -0.00000000 </velocity>
    <force> 0.00160946 0.00000007 0.00000073 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26585838 0.00000009 </position>
    <velocity> -0.00000000 -0.00016118 0.00000000 </velocity>
    <force> -0.00000007 -0.00386268 -0.00000075 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000353 </ekin_e>
  <ekin_ion> 0.00134231 </ekin_ion>
  <temp_ion> 70.64802817 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294165 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="172">
  <ekin>         5.29335095 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44553717 </eps>
  <enl>          4.77028782 </enl>
  <ecoul>      -15.60157949 </ecoul>
  <exc>         -4.39081784 </exc>
  <esr>          0.06428568 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37429573 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37429573 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70890538 0.00000000 -0.00000010 </position>
    <velocity> 0.00001531 -0.00000000 -0.00000000 </velocity>
    <force> -0.00164784 -0.00000005 0.00000082 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26650489 0.00000012 </position>
    <velocity> 0.00000000 0.00016148 0.00000000 </velocity>
    <force> 0.00000009 0.00374591 -0.00000092 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70890538 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001531 0.00000000 -0.00000000 </velocity>
    <force> 0.00164777 0.00000006 0.00000083 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26650489 0.00000010 </position>
    <velocity> -0.00000000 -0.00016148 0.00000000 </velocity>
    <force> -0.00000006 -0.00374593 -0.00000081 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000354 </ekin_e>
  <ekin_ion> 0.00134702 </ekin_ion>
  <temp_ion> 70.89590971 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294164 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="173">
  <ekin>         5.29284864 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44522309 </eps>
  <enl>          4.77025521 </enl>
  <ecoul>      -15.60156626 </ecoul>
  <exc>         -4.39061481 </exc>
  <esr>          0.06420712 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37430030 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37430030 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70896584 0.00000000 -0.00000011 </position>
    <velocity> 0.00001518 -0.00000000 -0.00000000 </velocity>
    <force> -0.00168580 -0.00000005 0.00000090 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26715253 0.00000012 </position>
    <velocity> 0.00000000 0.00016177 0.00000000 </velocity>
    <force> 0.00000008 0.00362922 -0.00000106 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70896584 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001518 0.00000000 -0.00000000 </velocity>
    <force> 0.00168574 0.00000006 0.00000093 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26715253 0.00000010 </position>
    <velocity> -0.00000000 -0.00016177 0.00000000 </velocity>
    <force> -0.00000006 -0.00362923 -0.00000086 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000354 </ekin_e>
  <ekin_ion> 0.00135158 </ekin_ion>
  <temp_ion> 71.13616026 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294164 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="174">
  <ekin>         5.29234625 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44490878 </eps>
  <enl>          4.77022214 </enl>
  <ecoul>      -15.60155276 </ecoul>
  <exc>         -4.39041158 </exc>
  <esr>          0.06412862 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37430473 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37430473 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70902576 0.00000000 -0.00000011 </position>
    <velocity> 0.00001505 -0.00000000 -0.00000000 </velocity>
    <force> -0.00172331 -0.00000004 0.00000098 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26780127 0.00000013 </position>
    <velocity> 0.00000000 0.00016205 0.00000000 </velocity>
    <force> 0.00000008 0.00351260 -0.00000120 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70902576 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001505 0.00000000 -0.00000000 </velocity>
    <force> 0.00172325 0.00000005 0.00000102 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26780127 0.00000010 </position>
    <velocity> -0.00000000 -0.00016205 0.00000000 </velocity>
    <force> -0.00000005 -0.00351261 -0.00000091 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000355 </ekin_e>
  <ekin_ion> 0.00135600 </ekin_ion>
  <temp_ion> 71.36875065 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294163 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="175">
  <ekin>         5.29184379 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44459418 </eps>
  <enl>          4.77018850 </enl>
  <ecoul>      -15.60153898 </ecoul>
  <exc>         -4.39020814 </exc>
  <esr>          0.06405016 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37430901 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37430901 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70908513 0.00000000 -0.00000011 </position>
    <velocity> 0.00001491 -0.00000000 -0.00000000 </velocity>
    <force> -0.00176032 -0.00000004 0.00000105 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26845108 0.00000013 </position>
    <velocity> 0.00000000 0.00016232 0.00000000 </velocity>
    <force> 0.00000007 0.00339601 -0.00000132 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70908513 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001491 0.00000000 -0.00000000 </velocity>
    <force> 0.00176026 0.00000005 0.00000110 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26845108 0.00000011 </position>
    <velocity> -0.00000000 -0.00016232 0.00000000 </velocity>
    <force> -0.00000004 -0.00339601 -0.00000095 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000355 </ekin_e>
  <ekin_ion> 0.00136027 </ekin_ion>
  <temp_ion> 71.59365230 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294163 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="176">
  <ekin>         5.29134125 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44427920 </eps>
  <enl>          4.77015414 </enl>
  <ecoul>      -15.60152485 </ecoul>
  <exc>         -4.39000447 </exc>
  <esr>          0.06397177 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37431314 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37431314 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70914394 0.00000000 -0.00000012 </position>
    <velocity> 0.00001477 -0.00000000 -0.00000000 </velocity>
    <force> -0.00179686 -0.00000003 0.00000111 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26910190 0.00000014 </position>
    <velocity> 0.00000000 0.00016258 0.00000000 </velocity>
    <force> 0.00000006 0.00327936 -0.00000143 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70914394 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001477 0.00000000 -0.00000000 </velocity>
    <force> 0.00179681 0.00000004 0.00000117 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26910190 0.00000011 </position>
    <velocity> -0.00000000 -0.00016258 0.00000000 </velocity>
    <force> -0.00000003 -0.00327937 -0.00000098 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000356 </ekin_e>
  <ekin_ion> 0.00136440 </ekin_ion>
  <temp_ion> 71.81083412 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294162 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="177">
  <ekin>         5.29083859 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44396374 </eps>
  <enl>          4.77011896 </enl>
  <ecoul>      -15.60151034 </ecoul>
  <exc>         -4.38980059 </exc>
  <esr>          0.06389345 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37431712 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37431712 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70920218 0.00000000 -0.00000012 </position>
    <velocity> 0.00001463 -0.00000000 -0.00000000 </velocity>
    <force> -0.00183305 -0.00000003 0.00000116 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.26975372 0.00000014 </position>
    <velocity> 0.00000000 0.00016283 0.00000000 </velocity>
    <force> 0.00000005 0.00316261 -0.00000153 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70920218 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001463 0.00000000 -0.00000000 </velocity>
    <force> 0.00183300 0.00000003 0.00000124 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.26975372 0.00000011 </position>
    <velocity> -0.00000000 -0.00016283 0.00000000 </velocity>
    <force> -0.00000003 -0.00316262 -0.00000101 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000356 </ekin_e>
  <ekin_ion> 0.00136838 </ekin_ion>
  <temp_ion> 72.02026135 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294162 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="178">
  <ekin>         5.29033579 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44364771 </eps>
  <enl>          4.77008287 </enl>
  <ecoul>      -15.60149541 </ecoul>
  <exc>         -4.38959649 </exc>
  <esr>          0.06381519 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37432096 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37432096 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70925983 0.00000000 -0.00000012 </position>
    <velocity> 0.00001449 -0.00000000 -0.00000000 </velocity>
    <force> -0.00186904 -0.00000002 0.00000121 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27040649 0.00000014 </position>
    <velocity> 0.00000000 0.00016307 0.00000000 </velocity>
    <force> 0.00000004 0.00304572 -0.00000162 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70925983 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001449 0.00000000 -0.00000000 </velocity>
    <force> 0.00186900 0.00000002 0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.27040649 0.00000011 </position>
    <velocity> -0.00000000 -0.00016307 0.00000000 </velocity>
    <force> -0.00000002 -0.00304572 -0.00000104 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000356 </ekin_e>
  <ekin_ion> 0.00137221 </ekin_ion>
  <temp_ion> 72.22189628 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294161 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="179">
  <ekin>         5.28983275 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44333109 </eps>
  <enl>          4.77004591 </enl>
  <ecoul>      -15.60148004 </ecoul>
  <exc>         -4.38939218 </exc>
  <esr>          0.06373701 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37432464 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37432464 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70931689 0.00000000 -0.00000012 </position>
    <velocity> 0.00001434 -0.00000000 -0.00000000 </velocity>
    <force> -0.00190501 -0.00000001 0.00000125 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27106017 0.00000014 </position>
    <velocity> 0.00000000 0.00016331 0.00000000 </velocity>
    <force> 0.00000003 0.00292868 -0.00000169 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70931689 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001434 0.00000000 -0.00000000 </velocity>
    <force> 0.00190498 0.00000001 0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.27106017 0.00000011 </position>
    <velocity> -0.00000000 -0.00016331 0.00000000 </velocity>
    <force> -0.00000001 -0.00292868 -0.00000106 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000357 </ekin_e>
  <ekin_ion> 0.00137589 </ekin_ion>
  <temp_ion> 72.41570058 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294161 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="180">
  <ekin>         5.28932941 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44301399 </eps>
  <enl>          4.77000831 </enl>
  <ecoul>      -15.60146423 </ecoul>
  <exc>         -4.38918769 </exc>
  <esr>          0.06365892 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37432818 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37432818 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70937334 0.00000000 -0.00000012 </position>
    <velocity> 0.00001419 -0.00000000 -0.00000000 </velocity>
    <force> -0.00194114 -0.00000001 0.00000128 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27171473 0.00000014 </position>
    <velocity> 0.00000000 0.00016353 0.00000000 </velocity>
    <force> 0.00000001 0.00281155 -0.00000175 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70937334 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001419 0.00000000 -0.00000000 </velocity>
    <force> 0.00194111 0.00000000 0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.27171474 0.00000011 </position>
    <velocity> -0.00000000 -0.00016353 0.00000000 </velocity>
    <force> 0.00000000 -0.00281155 -0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000358 </ekin_e>
  <ekin_ion> 0.00137943 </ekin_ion>
  <temp_ion> 72.60163825 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294160 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="181">
  <ekin>         5.28882567 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44269666 </eps>
  <enl>          4.76997047 </enl>
  <ecoul>      -15.60144804 </ecoul>
  <exc>         -4.38898302 </exc>
  <esr>          0.06358091 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433157 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433157 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70942917 0.00000000 -0.00000012 </position>
    <velocity> 0.00001404 -0.00000000 -0.00000000 </velocity>
    <force> -0.00197754 -0.00000000 0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27237014 0.00000015 </position>
    <velocity> 0.00000000 0.00016375 0.00000000 </velocity>
    <force> 0.00000000 0.00269443 -0.00000178 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70942917 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001404 0.00000000 -0.00000000 </velocity>
    <force> 0.00197752 -0.00000001 0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.27237014 0.00000011 </position>
    <velocity> -0.00000000 -0.00016375 0.00000000 </velocity>
    <force> 0.00000001 -0.00269442 -0.00000108 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000358 </ekin_e>
  <ekin_ion> 0.00138281 </ekin_ion>
  <temp_ion> 72.77967856 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294160 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="182">
  <ekin>         5.28832149 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44237949 </eps>
  <enl>          4.76993294 </enl>
  <ecoul>      -15.60143156 </ecoul>
  <exc>         -4.38877819 </exc>
  <esr>          0.06350300 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433481 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433481 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70948437 0.00000000 -0.00000012 </position>
    <velocity> 0.00001388 -0.00000000 -0.00000000 </velocity>
    <force> -0.00201426 0.00000001 0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27302635 0.00000015 </position>
    <velocity> 0.00000000 0.00016395 0.00000000 </velocity>
    <force> -0.00000001 0.00257740 -0.00000181 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70948438 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001388 0.00000000 -0.00000000 </velocity>
    <force> 0.00201425 -0.00000002 0.00000141 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.27302635 0.00000011 </position>
    <velocity> -0.00000000 -0.00016395 0.00000000 </velocity>
    <force> 0.00000002 -0.00257739 -0.00000108 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000359 </ekin_e>
  <ekin_ion> 0.00138604 </ekin_ion>
  <temp_ion> 72.94979823 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294159 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="183">
  <ekin>         5.28781687 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44206297 </eps>
  <enl>          4.76989636 </enl>
  <ecoul>      -15.60141492 </ecoul>
  <exc>         -4.38857325 </exc>
  <esr>          0.06342518 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433790 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433790 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70953894 0.00000000 -0.00000012 </position>
    <velocity> 0.00001372 -0.00000000 -0.00000000 </velocity>
    <force> -0.00205127 0.00000001 0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27368333 0.00000015 </position>
    <velocity> 0.00000000 0.00016415 0.00000000 </velocity>
    <force> -0.00000002 0.00246057 -0.00000181 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70953894 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001372 0.00000000 0.00000000 </velocity>
    <force> 0.00205127 -0.00000003 0.00000141 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.27368333 0.00000011 </position>
    <velocity> -0.00000000 -0.00016415 -0.00000000 </velocity>
    <force> 0.00000003 -0.00246056 -0.00000108 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000360 </ekin_e>
  <ekin_ion> 0.00138912 </ekin_ion>
  <temp_ion> 73.11198271 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294158 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="184">
  <ekin>         5.28731189 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44174757 </eps>
  <enl>          4.76986130 </enl>
  <ecoul>      -15.60139824 </ecoul>
  <exc>         -4.38836821 </exc>
  <esr>          0.06334747 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434084 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434084 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70959285 0.00000000 -0.00000012 </position>
    <velocity> 0.00001356 -0.00000000 0.00000000 </velocity>
    <force> -0.00208846 0.00000002 0.00000134 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27434104 0.00000014 </position>
    <velocity> 0.00000000 0.00016434 -0.00000000 </velocity>
    <force> -0.00000003 0.00234405 -0.00000181 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70959285 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001356 0.00000000 0.00000000 </velocity>
    <force> 0.00208847 -0.00000003 0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27434104 0.00000011 </position>
    <velocity> -0.00000000 -0.00016434 -0.00000000 </velocity>
    <force> 0.00000004 -0.00234404 -0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000361 </ekin_e>
  <ekin_ion> 0.00139205 </ekin_ion>
  <temp_ion> 73.26622650 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294157 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="185">
  <ekin>         5.28680670 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44143369 </eps>
  <enl>          4.76982817 </enl>
  <ecoul>      -15.60138168 </ecoul>
  <exc>         -4.38816313 </exc>
  <esr>          0.06326987 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434363 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434363 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70964609 0.00000000 -0.00000012 </position>
    <velocity> 0.00001339 -0.00000000 0.00000000 </velocity>
    <force> -0.00212566 0.00000002 0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27499945 0.00000014 </position>
    <velocity> 0.00000000 0.00016451 -0.00000000 </velocity>
    <force> -0.00000004 0.00222791 -0.00000178 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70964609 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001339 0.00000000 0.00000000 </velocity>
    <force> 0.00212567 -0.00000004 0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27499945 0.00000011 </position>
    <velocity> -0.00000000 -0.00016451 -0.00000000 </velocity>
    <force> 0.00000004 -0.00222790 -0.00000106 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000362 </ekin_e>
  <ekin_ion> 0.00139483 </ekin_ion>
  <temp_ion> 73.41253280 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294156 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="186">
  <ekin>         5.28630155 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44112157 </eps>
  <enl>          4.76979715 </enl>
  <ecoul>      -15.60136534 </ecoul>
  <exc>         -4.38795807 </exc>
  <esr>          0.06319238 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434627 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434627 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70969866 0.00000000 -0.00000012 </position>
    <velocity> 0.00001323 -0.00000000 0.00000000 </velocity>
    <force> -0.00216266 0.00000003 0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.27565851 0.00000014 </position>
    <velocity> 0.00000000 0.00016468 -0.00000000 </velocity>
    <force> -0.00000005 0.00211222 -0.00000175 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70969866 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001323 0.00000000 0.00000000 </velocity>
    <force> 0.00216269 -0.00000005 0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27565851 0.00000011 </position>
    <velocity> -0.00000000 -0.00016468 -0.00000000 </velocity>
    <force> 0.00000005 -0.00211221 -0.00000104 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000363 </ekin_e>
  <ekin_ion> 0.00139746 </ekin_ion>
  <temp_ion> 73.55091255 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294155 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="187">
  <ekin>         5.28579673 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44081124 </eps>
  <enl>          4.76976810 </enl>
  <ecoul>      -15.60134928 </ecoul>
  <exc>         -4.38775308 </exc>
  <esr>          0.06311501 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434876 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434876 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70975054 0.00000000 -0.00000012 </position>
    <velocity> 0.00001306 -0.00000000 0.00000000 </velocity>
    <force> -0.00219930 0.00000003 0.00000127 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.27631821 0.00000014 </position>
    <velocity> 0.00000000 0.00016484 -0.00000000 </velocity>
    <force> -0.00000006 0.00199703 -0.00000169 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70975054 -0.00000000 -0.00000012 </position>
    <velocity> -0.00001306 0.00000000 0.00000000 </velocity>
    <force> 0.00219933 -0.00000006 0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27631821 0.00000011 </position>
    <velocity> -0.00000000 -0.00016484 -0.00000000 </velocity>
    <force> 0.00000006 -0.00199701 -0.00000102 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000364 </ekin_e>
  <ekin_ion> 0.00139994 </ekin_ion>
  <temp_ion> 73.68138310 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294154 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="188">
  <ekin>         5.28529255 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44050255 </eps>
  <enl>          4.76974066 </enl>
  <ecoul>      -15.60133353 </ecoul>
  <exc>         -4.38754823 </exc>
  <esr>          0.06303776 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435110 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435110 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70980173 0.00000000 -0.00000012 </position>
    <velocity> 0.00001288 -0.00000000 0.00000000 </velocity>
    <force> -0.00223541 0.00000004 0.00000123 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.27697849 0.00000014 </position>
    <velocity> 0.00000000 0.00016500 -0.00000000 </velocity>
    <force> -0.00000007 0.00188235 -0.00000163 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70980173 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001288 0.00000000 0.00000000 </velocity>
    <force> 0.00223546 -0.00000006 0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27697849 0.00000011 </position>
    <velocity> -0.00000000 -0.00016500 -0.00000000 </velocity>
    <force> 0.00000006 -0.00188233 -0.00000099 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00140227 </ekin_ion>
  <temp_ion> 73.80396641 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294153 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.012" max="    0.012"/>
<iteration count="189">
  <ekin>         5.28478927 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.44019520 </eps>
  <enl>          4.76971429 </enl>
  <ecoul>      -15.60131806 </ecoul>
  <exc>         -4.38734359 </exc>
  <esr>          0.06296064 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435329 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435329 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70985220 0.00000000 -0.00000011 </position>
    <velocity> 0.00001271 -0.00000000 0.00000000 </velocity>
    <force> -0.00227095 0.00000004 0.00000117 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.27763932 0.00000013 </position>
    <velocity> 0.00000000 0.00016514 -0.00000000 </velocity>
    <force> -0.00000008 0.00176817 -0.00000155 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70985220 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001271 0.00000000 0.00000000 </velocity>
    <force> 0.00227100 -0.00000006 0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27763932 0.00000010 </position>
    <velocity> -0.00000000 -0.00016514 -0.00000000 </velocity>
    <force> 0.00000007 -0.00176815 -0.00000096 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000366 </ekin_e>
  <ekin_ion> 0.00140445 </ekin_ion>
  <temp_ion> 73.91868678 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294152 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.013" max="    0.013"/>
<iteration count="190">
  <ekin>         5.28428712 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43988880 </eps>
  <enl>          4.76968838 </enl>
  <ecoul>      -15.60130280 </ecoul>
  <exc>         -4.38713923 </exc>
  <esr>          0.06288366 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435533 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435533 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70990195 0.00000000 -0.00000011 </position>
    <velocity> 0.00001253 -0.00000000 0.00000000 </velocity>
    <force> -0.00230593 0.00000005 0.00000111 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.27830067 0.00000013 </position>
    <velocity> 0.00000000 0.00016527 -0.00000000 </velocity>
    <force> -0.00000009 0.00165445 -0.00000145 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70990196 -0.00000000 -0.00000011 </position>
    <velocity> -0.00001253 0.00000000 0.00000000 </velocity>
    <force> 0.00230599 -0.00000007 0.00000114 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27830067 0.00000010 </position>
    <velocity> -0.00000000 -0.00016527 -0.00000000 </velocity>
    <force> 0.00000007 -0.00165443 -0.00000093 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000367 </ekin_e>
  <ekin_ion> 0.00140648 </ekin_ion>
  <temp_ion> 74.02556797 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294151 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.017" max="    0.017"/>
<iteration count="191">
  <ekin>         5.28378624 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43958297 </eps>
  <enl>          4.76966239 </enl>
  <ecoul>      -15.60128768 </ecoul>
  <exc>         -4.38693520 </exc>
  <esr>          0.06280681 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435722 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435722 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70995098 0.00000000 -0.00000011 </position>
    <velocity> 0.00001235 -0.00000000 0.00000000 </velocity>
    <force> -0.00234045 0.00000005 0.00000104 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.27896250 0.00000012 </position>
    <velocity> 0.00000000 0.00016540 -0.00000000 </velocity>
    <force> -0.00000009 0.00154110 -0.00000134 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70995098 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001235 0.00000000 0.00000000 </velocity>
    <force> 0.00234050 -0.00000007 0.00000107 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27896250 0.00000010 </position>
    <velocity> -0.00000000 -0.00016540 -0.00000000 </velocity>
    <force> 0.00000007 -0.00154108 -0.00000088 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000367 </ekin_e>
  <ekin_ion> 0.00140836 </ekin_ion>
  <temp_ion> 74.12463003 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294151 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="192">
  <ekin>         5.28328665 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43927740 </eps>
  <enl>          4.76963591 </enl>
  <ecoul>      -15.60127260 </ecoul>
  <exc>         -4.38673152 </exc>
  <esr>          0.06273011 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435895 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435895 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70999925 0.00000000 -0.00000010 </position>
    <velocity> 0.00001216 -0.00000000 0.00000000 </velocity>
    <force> -0.00237465 0.00000005 0.00000096 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.27962478 0.00000012 </position>
    <velocity> 0.00000000 0.00016551 -0.00000000 </velocity>
    <force> -0.00000009 0.00142798 -0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70999926 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001216 0.00000000 0.00000000 </velocity>
    <force> 0.00237471 -0.00000007 0.00000099 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.27962478 0.00000010 </position>
    <velocity> -0.00000000 -0.00016551 -0.00000000 </velocity>
    <force> 0.00000007 -0.00142796 -0.00000084 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000368 </ekin_e>
  <ekin_ion> 0.00141010 </ekin_ion>
  <temp_ion> 74.21588606 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294150 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="193">
  <ekin>         5.28278830 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43897188 </eps>
  <enl>          4.76960873 </enl>
  <ecoul>      -15.60125747 </ecoul>
  <exc>         -4.38652822 </exc>
  <esr>          0.06265356 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436054 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436054 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71004678 0.00000000 -0.00000010 </position>
    <velocity> 0.00001198 -0.00000000 0.00000000 </velocity>
    <force> -0.00240872 0.00000005 0.00000088 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.28028747 0.00000011 </position>
    <velocity> 0.00000000 0.00016562 -0.00000000 </velocity>
    <force> -0.00000009 0.00131494 -0.00000109 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71004678 -0.00000000 -0.00000010 </position>
    <velocity> -0.00001198 -0.00000000 0.00000000 </velocity>
    <force> 0.00240878 -0.00000007 0.00000089 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28028747 0.00000009 </position>
    <velocity> 0.00000000 -0.00016562 -0.00000000 </velocity>
    <force> 0.00000007 -0.00131493 -0.00000079 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000368 </ekin_e>
  <ekin_ion> 0.00141168 </ekin_ion>
  <temp_ion> 74.29933966 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294150 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="194">
  <ekin>         5.28229108 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43866634 </eps>
  <enl>          4.76958082 </enl>
  <ecoul>      -15.60124223 </ecoul>
  <exc>         -4.38632530 </exc>
  <esr>          0.06257716 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436197 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436197 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71009355 0.00000000 -0.00000010 </position>
    <velocity> 0.00001179 0.00000000 0.00000000 </velocity>
    <force> -0.00244282 0.00000006 0.00000079 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.28095053 0.00000011 </position>
    <velocity> -0.00000000 0.00016572 -0.00000000 </velocity>
    <force> -0.00000009 0.00120182 -0.00000095 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71009355 -0.00000000 -0.00000009 </position>
    <velocity> -0.00001179 -0.00000000 0.00000000 </velocity>
    <force> 0.00244289 -0.00000007 0.00000079 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28095053 0.00000009 </position>
    <velocity> 0.00000000 -0.00016572 -0.00000000 </velocity>
    <force> 0.00000007 -0.00120181 -0.00000073 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000367 </ekin_e>
  <ekin_ion> 0.00141312 </ekin_ion>
  <temp_ion> 74.37498371 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294151 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="195">
  <ekin>         5.28179483 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43836083 </eps>
  <enl>          4.76955235 </enl>
  <ecoul>      -15.60122685 </ecoul>
  <exc>         -4.38612275 </exc>
  <esr>          0.06250092 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436326 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436326 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71013953 0.00000000 -0.00000009 </position>
    <velocity> 0.00001159 0.00000000 0.00000000 </velocity>
    <force> -0.00247709 0.00000006 0.00000070 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.28161393 0.00000010 </position>
    <velocity> -0.00000000 0.00016581 -0.00000000 </velocity>
    <force> -0.00000009 0.00108848 -0.00000081 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71013954 -0.00000000 -0.00000009 </position>
    <velocity> -0.00001159 -0.00000000 0.00000000 </velocity>
    <force> 0.00247715 -0.00000007 0.00000069 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28161393 0.00000009 </position>
    <velocity> 0.00000000 -0.00016581 -0.00000000 </velocity>
    <force> 0.00000007 -0.00108847 -0.00000067 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000367 </ekin_e>
  <ekin_ion> 0.00141441 </ekin_ion>
  <temp_ion> 74.44280120 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294151 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="196">
  <ekin>         5.28129937 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43805548 </eps>
  <enl>          4.76952357 </enl>
  <ecoul>      -15.60121131 </ecoul>
  <exc>         -4.38592055 </exc>
  <esr>          0.06242484 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436439 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436439 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71018474 0.00000000 -0.00000009 </position>
    <velocity> 0.00001140 0.00000000 0.00000000 </velocity>
    <force> -0.00251156 0.00000005 0.00000061 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.28227764 0.00000010 </position>
    <velocity> -0.00000000 0.00016589 -0.00000000 </velocity>
    <force> -0.00000009 0.00097483 -0.00000065 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71018474 -0.00000000 -0.00000008 </position>
    <velocity> -0.00001140 -0.00000000 0.00000000 </velocity>
    <force> 0.00251162 -0.00000006 0.00000058 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28227764 0.00000008 </position>
    <velocity> 0.00000000 -0.00016589 -0.00000000 </velocity>
    <force> 0.00000006 -0.00097482 -0.00000060 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000367 </ekin_e>
  <ekin_ion> 0.00141555 </ekin_ion>
  <temp_ion> 74.50276834 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294151 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="197">
  <ekin>         5.28080460 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43775048 </eps>
  <enl>          4.76949481 </enl>
  <ecoul>      -15.60119562 </ecoul>
  <exc>         -4.38571869 </exc>
  <esr>          0.06234892 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436538 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436538 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71022915 0.00000000 -0.00000008 </position>
    <velocity> 0.00001120 0.00000000 0.00000000 </velocity>
    <force> -0.00254623 0.00000005 0.00000051 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.28294162 0.00000009 </position>
    <velocity> -0.00000000 0.00016596 -0.00000000 </velocity>
    <force> -0.00000008 0.00086087 -0.00000050 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71022915 -0.00000000 -0.00000008 </position>
    <velocity> -0.00001120 -0.00000000 0.00000000 </velocity>
    <force> 0.00254629 -0.00000006 0.00000047 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28294162 0.00000008 </position>
    <velocity> 0.00000000 -0.00016596 -0.00000000 </velocity>
    <force> 0.00000006 -0.00086087 -0.00000053 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000366 </ekin_e>
  <ekin_ion> 0.00141654 </ekin_ion>
  <temp_ion> 74.55485963 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294152 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="198">
  <ekin>         5.28031043 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43744605 </eps>
  <enl>          4.76946636 </enl>
  <ecoul>      -15.60117982 </ecoul>
  <exc>         -4.38551713 </exc>
  <esr>          0.06227318 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436621 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436621 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71027275 0.00000000 -0.00000008 </position>
    <velocity> 0.00001100 0.00000000 0.00000000 </velocity>
    <force> -0.00258101 0.00000005 0.00000040 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.28360583 0.00000009 </position>
    <velocity> -0.00000000 0.00016602 -0.00000000 </velocity>
    <force> -0.00000008 0.00074670 -0.00000034 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71027275 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001100 -0.00000000 0.00000000 </velocity>
    <force> 0.00258107 -0.00000005 0.00000035 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28360583 0.00000007 </position>
    <velocity> 0.00000000 -0.00016602 -0.00000000 </velocity>
    <force> 0.00000005 -0.00074670 -0.00000046 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000366 </ekin_e>
  <ekin_ion> 0.00141738 </ekin_ion>
  <temp_ion> 74.59905424 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294152 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.011" max="    0.011"/>
<iteration count="199">
  <ekin>         5.27981687 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43714240 </eps>
  <enl>          4.76943846 </enl>
  <ecoul>      -15.60116396 </ecoul>
  <exc>         -4.38531587 </exc>
  <esr>          0.06219762 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436690 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436690 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71031553 0.00000000 -0.00000007 </position>
    <velocity> 0.00001080 0.00000000 0.00000000 </velocity>
    <force> -0.00261578 0.00000005 0.00000030 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28427024 0.00000008 </position>
    <velocity> -0.00000000 0.00016608 -0.00000000 </velocity>
    <force> -0.00000007 0.00063247 -0.00000018 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71031553 -0.00000000 -0.00000007 </position>
    <velocity> -0.00001080 -0.00000000 0.00000000 </velocity>
    <force> 0.00261583 -0.00000005 0.00000023 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28427024 0.00000007 </position>
    <velocity> 0.00000000 -0.00016608 -0.00000000 </velocity>
    <force> 0.00000005 -0.00063247 -0.00000038 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00141807 </ekin_ion>
  <temp_ion> 74.63534211 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294152 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="200">
  <ekin>         5.27932398 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43683971 </eps>
  <enl>          4.76941129 </enl>
  <ecoul>      -15.60114810 </ecoul>
  <exc>         -4.38511489 </exc>
  <esr>          0.06212223 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436744 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436744 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71035749 0.00000000 -0.00000007 </position>
    <velocity> 0.00001059 0.00000000 0.00000000 </velocity>
    <force> -0.00265039 0.00000004 0.00000018 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28493481 0.00000007 </position>
    <velocity> -0.00000000 0.00016612 -0.00000000 </velocity>
    <force> -0.00000006 0.00051840 -0.00000002 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71035749 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001059 -0.00000000 0.00000000 </velocity>
    <force> 0.00265044 -0.00000004 0.00000012 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.28493481 0.00000007 </position>
    <velocity> 0.00000000 -0.00016612 -0.00000000 </velocity>
    <force> 0.00000004 -0.00051840 -0.00000030 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00141861 </ekin_ion>
  <temp_ion> 74.66372852 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294153 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="201">
  <ekin>         5.27883187 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43653813 </eps>
  <enl>          4.76938492 </enl>
  <ecoul>      -15.60113230 </ecoul>
  <exc>         -4.38491418 </exc>
  <esr>          0.06204703 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436783 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436783 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71039861 0.00000000 -0.00000006 </position>
    <velocity> 0.00001038 0.00000000 0.00000000 </velocity>
    <force> -0.00268473 0.00000003 0.00000007 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28559951 0.00000007 </position>
    <velocity> -0.00000000 0.00016616 -0.00000000 </velocity>
    <force> -0.00000005 0.00040471 0.00000014 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71039861 -0.00000000 -0.00000006 </position>
    <velocity> -0.00001038 -0.00000000 0.00000000 </velocity>
    <force> 0.00268476 -0.00000003 0.00000000 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.28559951 0.00000006 </position>
    <velocity> 0.00000000 -0.00016616 -0.00000000 </velocity>
    <force> 0.00000003 -0.00040471 -0.00000021 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00141900 </ekin_ion>
  <temp_ion> 74.68423582 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294153 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="202">
  <ekin>         5.27834067 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43623777 </eps>
  <enl>          4.76935937 </enl>
  <ecoul>      -15.60111657 </ecoul>
  <exc>         -4.38471376 </exc>
  <esr>          0.06197202 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436807 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436807 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71043887 0.00000000 -0.00000006 </position>
    <velocity> 0.00001017 0.00000000 0.00000000 </velocity>
    <force> -0.00271870 0.00000003 -0.00000004 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28626430 0.00000006 </position>
    <velocity> -0.00000000 0.00016619 -0.00000000 </velocity>
    <force> -0.00000004 0.00029157 0.00000030 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71043887 -0.00000000 -0.00000005 </position>
    <velocity> -0.00001017 -0.00000000 0.00000000 </velocity>
    <force> 0.00271873 -0.00000002 -0.00000011 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.28626430 0.00000006 </position>
    <velocity> 0.00000000 -0.00016619 -0.00000000 </velocity>
    <force> 0.00000002 -0.00029157 -0.00000013 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00141924 </ekin_ion>
  <temp_ion> 74.69690163 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294153 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="203">
  <ekin>         5.27785045 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43593867 </eps>
  <enl>          4.76933461 </enl>
  <ecoul>      -15.60110094 </ecoul>
  <exc>         -4.38451361 </exc>
  <esr>          0.06189721 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436816 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436816 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71047828 0.00000000 -0.00000005 </position>
    <velocity> 0.00000996 0.00000000 0.00000000 </velocity>
    <force> -0.00275227 0.00000002 -0.00000015 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28692914 0.00000006 </position>
    <velocity> -0.00000000 0.00016620 -0.00000000 </velocity>
    <force> -0.00000003 0.00017906 0.00000045 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71047828 -0.00000000 -0.00000005 </position>
    <velocity> -0.00000996 -0.00000000 0.00000000 </velocity>
    <force> 0.00275229 -0.00000001 -0.00000023 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.28692914 0.00000005 </position>
    <velocity> 0.00000000 -0.00016620 -0.00000000 </velocity>
    <force> 0.00000002 -0.00017906 -0.00000004 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00141933 </ekin_ion>
  <temp_ion> 74.70177410 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294153 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="204">
  <ekin>         5.27736124 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43564084 </eps>
  <enl>          4.76931058 </enl>
  <ecoul>      -15.60108538 </ecoul>
  <exc>         -4.38431371 </exc>
  <esr>          0.06182259 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436810 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436810 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71051682 0.00000000 -0.00000005 </position>
    <velocity> 0.00000974 0.00000000 0.00000000 </velocity>
    <force> -0.00278548 0.00000002 -0.00000027 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28759401 0.00000005 </position>
    <velocity> -0.00000000 0.00016621 -0.00000000 </velocity>
    <force> -0.00000002 0.00006716 0.00000060 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71051682 -0.00000000 -0.00000004 </position>
    <velocity> -0.00000974 -0.00000000 0.00000000 </velocity>
    <force> 0.00278549 -0.00000000 -0.00000034 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.28759401 0.00000005 </position>
    <velocity> 0.00000000 -0.00016621 -0.00000000 </velocity>
    <force> 0.00000001 -0.00006718 0.00000005 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00141927 </ekin_ion>
  <temp_ion> 74.69890509 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294153 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="205">
  <ekin>         5.27687299 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43534420 </eps>
  <enl>          4.76928716 </enl>
  <ecoul>      -15.60106980 </ecoul>
  <exc>         -4.38411405 </exc>
  <esr>          0.06174818 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436790 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436790 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71055447 0.00000000 -0.00000004 </position>
    <velocity> 0.00000952 0.00000000 0.00000000 </velocity>
    <force> -0.00281838 0.00000001 -0.00000038 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28825886 0.00000005 </position>
    <velocity> -0.00000000 0.00016621 -0.00000000 </velocity>
    <force> -0.00000001 -0.00004421 0.00000075 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71055447 -0.00000000 -0.00000004 </position>
    <velocity> -0.00000952 -0.00000000 0.00000000 </velocity>
    <force> 0.00281838 0.00000001 -0.00000045 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.28825886 0.00000004 </position>
    <velocity> 0.00000000 -0.00016621 -0.00000000 </velocity>
    <force> -0.00000000 0.00004420 0.00000014 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000365 </ekin_e>
  <ekin_ion> 0.00141907 </ekin_ion>
  <temp_ion> 74.68834335 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294153 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="206">
  <ekin>         5.27638556 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43504859 </eps>
  <enl>          4.76926418 </enl>
  <ecoul>      -15.60105411 </ecoul>
  <exc>         -4.38391459 </exc>
  <esr>          0.06167398 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436755 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436755 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71059124 0.00000000 -0.00000004 </position>
    <velocity> 0.00000930 0.00000000 0.00000000 </velocity>
    <force> -0.00285108 0.00000000 -0.00000048 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28892366 0.00000004 </position>
    <velocity> -0.00000000 0.00016621 -0.00000000 </velocity>
    <force> 0.00000001 -0.00015523 0.00000088 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71059124 -0.00000000 -0.00000004 </position>
    <velocity> -0.00000930 -0.00000000 0.00000000 </velocity>
    <force> 0.00285107 0.00000002 -0.00000056 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.28892366 0.00000004 </position>
    <velocity> 0.00000000 -0.00016621 -0.00000000 </velocity>
    <force> -0.00000001 0.00015522 0.00000023 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000364 </ekin_e>
  <ekin_ion> 0.00141873 </ekin_ion>
  <temp_ion> 74.67012936 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294154 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="207">
  <ekin>         5.27589877 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43475375 </eps>
  <enl>          4.76924137 </enl>
  <ecoul>      -15.60103815 </ecoul>
  <exc>         -4.38371529 </exc>
  <esr>          0.06159998 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436705 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436705 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71062710 0.00000000 -0.00000004 </position>
    <velocity> 0.00000908 0.00000000 0.00000000 </velocity>
    <force> -0.00288366 -0.00000001 -0.00000059 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.28958838 0.00000004 </position>
    <velocity> -0.00000000 0.00016619 -0.00000000 </velocity>
    <force> 0.00000002 -0.00026606 0.00000101 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71062710 -0.00000000 -0.00000003 </position>
    <velocity> -0.00000908 -0.00000000 0.00000000 </velocity>
    <force> 0.00288364 0.00000002 -0.00000067 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.28958838 0.00000003 </position>
    <velocity> 0.00000000 -0.00016619 -0.00000000 </velocity>
    <force> -0.00000002 0.00026604 0.00000033 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000364 </ekin_e>
  <ekin_ion> 0.00141824 </ekin_ion>
  <temp_ion> 74.64429329 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294154 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="208">
  <ekin>         5.27541245 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43445936 </eps>
  <enl>          4.76921839 </enl>
  <ecoul>      -15.60102178 </ecoul>
  <exc>         -4.38351612 </exc>
  <esr>          0.06152621 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436641 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436641 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71066206 0.00000000 -0.00000003 </position>
    <velocity> 0.00000885 0.00000000 0.00000000 </velocity>
    <force> -0.00291619 -0.00000001 -0.00000070 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29025299 0.00000003 </position>
    <velocity> -0.00000000 0.00016617 -0.00000000 </velocity>
    <force> 0.00000003 -0.00037680 0.00000112 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71066206 -0.00000000 -0.00000003 </position>
    <velocity> -0.00000885 -0.00000000 0.00000000 </velocity>
    <force> 0.00291617 0.00000003 -0.00000077 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29025299 0.00000003 </position>
    <velocity> 0.00000000 -0.00016617 -0.00000000 </velocity>
    <force> -0.00000003 0.00037679 0.00000042 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000363 </ekin_e>
  <ekin_ion> 0.00141760 </ekin_ion>
  <temp_ion> 74.61085664 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294155 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="209">
  <ekin>         5.27492646 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43416504 </eps>
  <enl>          4.76919485 </enl>
  <ecoul>      -15.60100487 </ecoul>
  <exc>         -4.38331703 </exc>
  <esr>          0.06145265 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436563 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436563 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71069609 0.00000000 -0.00000003 </position>
    <velocity> 0.00000862 0.00000000 0.00000000 </velocity>
    <force> -0.00294870 -0.00000002 -0.00000080 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29091744 0.00000003 </position>
    <velocity> -0.00000000 0.00016613 -0.00000000 </velocity>
    <force> 0.00000004 -0.00048750 0.00000123 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71069609 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000862 -0.00000000 0.00000000 </velocity>
    <force> 0.00294867 0.00000004 -0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29091744 0.00000003 </position>
    <velocity> 0.00000000 -0.00016613 -0.00000000 </velocity>
    <force> -0.00000003 0.00048749 0.00000051 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000363 </ekin_e>
  <ekin_ion> 0.00141682 </ekin_ion>
  <temp_ion> 74.56983671 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294155 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="210">
  <ekin>         5.27444079 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43387049 </eps>
  <enl>          4.76917036 </enl>
  <ecoul>      -15.60098734 </ecoul>
  <exc>         -4.38311802 </exc>
  <esr>          0.06137932 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436470 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436470 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71072919 0.00000000 -0.00000002 </position>
    <velocity> 0.00000839 0.00000000 0.00000000 </velocity>
    <force> -0.00298116 -0.00000003 -0.00000089 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29158170 0.00000002 </position>
    <velocity> -0.00000000 0.00016609 -0.00000000 </velocity>
    <force> 0.00000005 -0.00059810 0.00000132 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71072918 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000839 -0.00000000 0.00000000 </velocity>
    <force> 0.00298112 0.00000005 -0.00000096 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29158170 0.00000002 </position>
    <velocity> 0.00000000 -0.00016609 -0.00000000 </velocity>
    <force> -0.00000004 0.00059809 0.00000061 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000362 </ekin_e>
  <ekin_ion> 0.00141590 </ekin_ion>
  <temp_ion> 74.52125274 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294156 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="211">
  <ekin>         5.27395552 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43357552 </eps>
  <enl>          4.76914465 </enl>
  <ecoul>      -15.60096919 </ecoul>
  <exc>         -4.38291908 </exc>
  <esr>          0.06130621 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436363 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436363 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71076134 0.00000000 -0.00000002 </position>
    <velocity> 0.00000816 0.00000000 0.00000000 </velocity>
    <force> -0.00301351 -0.00000003 -0.00000098 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29224574 0.00000002 </position>
    <velocity> -0.00000000 0.00016604 -0.00000000 </velocity>
    <force> 0.00000006 -0.00070849 0.00000141 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71076134 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000816 -0.00000000 0.00000000 </velocity>
    <force> 0.00301346 0.00000005 -0.00000104 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29224574 0.00000002 </position>
    <velocity> 0.00000000 -0.00016604 -0.00000000 </velocity>
    <force> -0.00000005 0.00070847 0.00000070 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000361 </ekin_e>
  <ekin_ion> 0.00141483 </ekin_ion>
  <temp_ion> 74.46513136 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294156 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="212">
  <ekin>         5.27347087 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43328014 </eps>
  <enl>          4.76911764 </enl>
  <ecoul>      -15.60095050 </ecoul>
  <exc>         -4.38272028 </exc>
  <esr>          0.06123334 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436241 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436241 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71079255 0.00000000 -0.00000002 </position>
    <velocity> 0.00000792 0.00000000 0.00000000 </velocity>
    <force> -0.00304564 -0.00000004 -0.00000106 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29290953 0.00000002 </position>
    <velocity> -0.00000000 0.00016598 -0.00000000 </velocity>
    <force> 0.00000007 -0.00081852 0.00000148 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71079255 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000792 -0.00000000 0.00000000 </velocity>
    <force> 0.00304559 0.00000006 -0.00000111 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29290953 0.00000002 </position>
    <velocity> 0.00000000 -0.00016598 -0.00000000 </velocity>
    <force> -0.00000006 0.00081850 0.00000080 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000361 </ekin_e>
  <ekin_ion> 0.00141362 </ekin_ion>
  <temp_ion> 74.40150987 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294157 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="213">
  <ekin>         5.27298709 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43298460 </eps>
  <enl>          4.76908955 </enl>
  <ecoul>      -15.60093143 </ecoul>
  <exc>         -4.38252167 </exc>
  <esr>          0.06116071 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37436105 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37436105 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71082279 0.00000000 -0.00000002 </position>
    <velocity> 0.00000768 0.00000000 0.00000000 </velocity>
    <force> -0.00307748 -0.00000004 -0.00000113 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29357302 0.00000002 </position>
    <velocity> -0.00000000 0.00016591 -0.00000000 </velocity>
    <force> 0.00000008 -0.00092807 0.00000154 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71082279 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000768 -0.00000000 0.00000000 </velocity>
    <force> 0.00307742 0.00000006 -0.00000118 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29357302 0.00000001 </position>
    <velocity> 0.00000000 -0.00016591 -0.00000000 </velocity>
    <force> -0.00000006 0.00092806 0.00000089 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000360 </ekin_e>
  <ekin_ion> 0.00141227 </ekin_ion>
  <temp_ion> 74.33043607 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294158 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="214">
  <ekin>         5.27250450 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43268938 </eps>
  <enl>          4.76906087 </enl>
  <ecoul>      -15.60091219 </ecoul>
  <exc>         -4.38232334 </exc>
  <esr>          0.06108831 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435955 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435955 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71085206 0.00000000 -0.00000001 </position>
    <velocity> 0.00000744 0.00000000 0.00000000 </velocity>
    <force> -0.00310896 -0.00000005 -0.00000119 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29423619 0.00000001 </position>
    <velocity> -0.00000000 0.00016583 -0.00000000 </velocity>
    <force> 0.00000009 -0.00103711 0.00000158 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71085206 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000744 -0.00000000 0.00000000 </velocity>
    <force> 0.00310890 0.00000006 -0.00000123 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29423619 0.00000001 </position>
    <velocity> 0.00000000 -0.00016583 -0.00000000 </velocity>
    <force> -0.00000006 0.00103710 0.00000097 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000359 </ekin_e>
  <ekin_ion> 0.00141078 </ekin_ion>
  <temp_ion> 74.25196468 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294159 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="215">
  <ekin>         5.27202337 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43239511 </eps>
  <enl>          4.76903229 </enl>
  <ecoul>      -15.60089304 </ecoul>
  <exc>         -4.38212542 </exc>
  <esr>          0.06101616 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435791 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435791 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71088036 0.00000000 -0.00000001 </position>
    <velocity> 0.00000720 0.00000000 0.00000000 </velocity>
    <force> -0.00314006 -0.00000005 -0.00000125 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29489901 0.00000001 </position>
    <velocity> -0.00000000 0.00016575 -0.00000000 </velocity>
    <force> 0.00000009 -0.00114568 0.00000161 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71088035 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000720 -0.00000000 0.00000000 </velocity>
    <force> 0.00314000 0.00000007 -0.00000128 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29489901 0.00000001 </position>
    <velocity> 0.00000000 -0.00016575 -0.00000000 </velocity>
    <force> -0.00000007 0.00114567 0.00000105 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000358 </ekin_e>
  <ekin_ion> 0.00140915 </ekin_ion>
  <temp_ion> 74.16615151 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294160 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.012" max="    0.012"/>
<iteration count="216">
  <ekin>         5.27154390 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43210243 </eps>
  <enl>          4.76900458 </enl>
  <ecoul>      -15.60087419 </ecoul>
  <exc>         -4.38192800 </exc>
  <esr>          0.06094426 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435613 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435613 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71090766 0.00000000 -0.00000001 </position>
    <velocity> 0.00000695 0.00000000 0.00000000 </velocity>
    <force> -0.00317084 -0.00000005 -0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29556143 0.00000001 </position>
    <velocity> -0.00000000 0.00016565 -0.00000000 </velocity>
    <force> 0.00000009 -0.00125391 0.00000163 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71090765 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000695 -0.00000000 0.00000000 </velocity>
    <force> 0.00317078 0.00000007 -0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29556143 0.00000001 </position>
    <velocity> 0.00000000 -0.00016565 -0.00000000 </velocity>
    <force> -0.00000007 0.00125390 0.00000113 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000357 </ekin_e>
  <ekin_ion> 0.00140738 </ekin_ion>
  <temp_ion> 74.07304704 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294161 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="217">
  <ekin>         5.27106623 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43181187 </eps>
  <enl>          4.76897840 </enl>
  <ecoul>      -15.60085578 </ecoul>
  <exc>         -4.38173120 </exc>
  <esr>          0.06087261 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435422 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435422 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71093395 0.00000000 -0.00000001 </position>
    <velocity> 0.00000670 0.00000000 0.00000000 </velocity>
    <force> -0.00320139 -0.00000006 -0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29622343 0.00000001 </position>
    <velocity> -0.00000000 0.00016555 -0.00000000 </velocity>
    <force> 0.00000010 -0.00136199 0.00000163 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71093395 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000670 0.00000000 0.00000000 </velocity>
    <force> 0.00320132 0.00000007 -0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29622343 0.00000000 </position>
    <velocity> 0.00000000 -0.00016555 -0.00000000 </velocity>
    <force> -0.00000007 0.00136198 0.00000119 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000356 </ekin_e>
  <ekin_ion> 0.00140548 </ekin_ion>
  <temp_ion> 73.97269162 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294162 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="218">
  <ekin>         5.27059036 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43152374 </eps>
  <enl>          4.76895417 </enl>
  <ecoul>      -15.60083788 </ecoul>
  <exc>         -4.38153508 </exc>
  <esr>          0.06080122 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37435216 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37435216 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71095924 0.00000000 -0.00000001 </position>
    <velocity> 0.00000645 0.00000000 0.00000000 </velocity>
    <force> -0.00323182 -0.00000006 -0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29688496 0.00000001 </position>
    <velocity> 0.00000000 0.00016544 0.00000000 </velocity>
    <force> 0.00000010 -0.00147009 0.00000161 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71095924 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000645 0.00000000 0.00000000 </velocity>
    <force> 0.00323176 0.00000006 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29688496 0.00000000 </position>
    <velocity> -0.00000000 -0.00016544 -0.00000000 </velocity>
    <force> -0.00000007 0.00147009 0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000355 </ekin_e>
  <ekin_ion> 0.00140343 </ekin_ion>
  <temp_ion> 73.86511385 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294163 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="219">
  <ekin>         5.27011627 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43123804 </eps>
  <enl>          4.76893194 </enl>
  <ecoul>      -15.60082044 </ecoul>
  <exc>         -4.38133969 </exc>
  <esr>          0.06073009 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434997 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434997 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71098351 0.00000000 -0.00000001 </position>
    <velocity> 0.00000619 -0.00000000 0.00000000 </velocity>
    <force> -0.00326225 -0.00000006 -0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29754601 0.00000001 </position>
    <velocity> 0.00000000 0.00016532 0.00000000 </velocity>
    <force> 0.00000009 -0.00157834 0.00000159 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71098351 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000619 0.00000000 0.00000000 </velocity>
    <force> 0.00326219 0.00000006 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29754601 0.00000000 </position>
    <velocity> -0.00000000 -0.00016532 -0.00000000 </velocity>
    <force> -0.00000007 0.00157833 0.00000130 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000354 </ekin_e>
  <ekin_ion> 0.00140125 </ekin_ion>
  <temp_ion> 73.75033276 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294164 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="220">
  <ekin>         5.26964385 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43095450 </eps>
  <enl>          4.76891139 </enl>
  <ecoul>      -15.60080333 </ecoul>
  <exc>         -4.38114504 </exc>
  <esr>          0.06065922 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434764 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434764 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71100675 0.00000000 -0.00000001 </position>
    <velocity> 0.00000594 -0.00000000 -0.00000000 </velocity>
    <force> -0.00329273 -0.00000006 -0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29820652 0.00000001 </position>
    <velocity> 0.00000000 0.00016519 0.00000000 </velocity>
    <force> 0.00000009 -0.00168675 0.00000155 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71100675 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000594 0.00000000 -0.00000000 </velocity>
    <force> 0.00329267 0.00000006 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29820652 0.00000000 </position>
    <velocity> -0.00000000 -0.00016519 -0.00000000 </velocity>
    <force> -0.00000007 0.00168675 0.00000134 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000352 </ekin_e>
  <ekin_ion> 0.00139893 </ekin_ion>
  <temp_ion> 73.62836363 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294165 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="221">
  <ekin>         5.26917301 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43067263 </eps>
  <enl>          4.76889193 </enl>
  <ecoul>      -15.60078638 </ecoul>
  <exc>         -4.38095110 </exc>
  <esr>          0.06058862 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434517 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434517 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71102896 0.00000000 -0.00000001 </position>
    <velocity> 0.00000568 -0.00000000 -0.00000000 </velocity>
    <force> -0.00332326 -0.00000006 -0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29886648 0.00000002 </position>
    <velocity> 0.00000000 0.00016506 0.00000000 </velocity>
    <force> 0.00000009 -0.00179522 0.00000150 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71102896 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000568 0.00000000 -0.00000000 </velocity>
    <force> 0.00332321 0.00000005 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29886648 0.00000000 </position>
    <velocity> -0.00000000 -0.00016506 -0.00000000 </velocity>
    <force> -0.00000006 0.00179522 0.00000137 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000351 </ekin_e>
  <ekin_ion> 0.00139648 </ekin_ion>
  <temp_ion> 73.49922576 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294166 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="222">
  <ekin>         5.26870367 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43039189 </eps>
  <enl>          4.76887287 </enl>
  <ecoul>      -15.60076938 </ecoul>
  <exc>         -4.38075785 </exc>
  <esr>          0.06051829 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37434257 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37434257 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71105011 0.00000000 -0.00000001 </position>
    <velocity> 0.00000542 -0.00000000 -0.00000000 </velocity>
    <force> -0.00335374 -0.00000005 -0.00000137 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.29952584 0.00000002 </position>
    <velocity> 0.00000000 0.00016491 0.00000000 </velocity>
    <force> 0.00000008 -0.00190355 0.00000144 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71105011 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000542 0.00000000 -0.00000000 </velocity>
    <force> 0.00335370 0.00000005 -0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.29952584 0.00000000 </position>
    <velocity> -0.00000000 -0.00016491 0.00000000 </velocity>
    <force> -0.00000006 0.00190356 0.00000139 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000350 </ekin_e>
  <ekin_ion> 0.00139389 </ekin_ion>
  <temp_ion> 73.36295031 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294167 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="223">
  <ekin>         5.26823580 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.43011179 </eps>
  <enl>          4.76885356 </enl>
  <ecoul>      -15.60075219 </ecoul>
  <exc>         -4.38056521 </exc>
  <esr>          0.06044824 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433984 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433984 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71107021 0.00000000 -0.00000001 </position>
    <velocity> 0.00000516 -0.00000000 -0.00000000 </velocity>
    <force> -0.00338403 -0.00000005 -0.00000134 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30018457 0.00000002 </position>
    <velocity> 0.00000000 0.00016476 0.00000000 </velocity>
    <force> 0.00000008 -0.00201149 0.00000138 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71107021 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000516 0.00000000 -0.00000000 </velocity>
    <force> 0.00338399 0.00000004 -0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30018457 0.00000000 </position>
    <velocity> -0.00000000 -0.00016476 0.00000000 </velocity>
    <force> -0.00000005 0.00201150 0.00000140 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000350 </ekin_e>
  <ekin_ion> 0.00139117 </ekin_ion>
  <temp_ion> 73.21958600 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294168 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="224">
  <ekin>         5.26776939 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42983206 </eps>
  <enl>          4.76883358 </enl>
  <ecoul>      -15.60073473 </ecoul>
  <exc>         -4.38037316 </exc>
  <esr>          0.06037846 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433698 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433698 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71108924 0.00000000 -0.00000001 </position>
    <velocity> 0.00000489 -0.00000000 -0.00000000 </velocity>
    <force> -0.00341395 -0.00000005 -0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30084264 0.00000002 </position>
    <velocity> 0.00000000 0.00016460 0.00000000 </velocity>
    <force> 0.00000007 -0.00211877 0.00000130 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71108924 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000489 0.00000000 -0.00000000 </velocity>
    <force> 0.00341392 0.00000003 -0.00000125 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30084264 0.00000000 </position>
    <velocity> -0.00000000 -0.00016460 0.00000000 </velocity>
    <force> -0.00000005 0.00211878 0.00000141 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000349 </ekin_e>
  <ekin_ion> 0.00138831 </ekin_ion>
  <temp_ion> 73.06920103 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294169 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="225">
  <ekin>         5.26730450 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42955264 </eps>
  <enl>          4.76881281 </enl>
  <ecoul>      -15.60071699 </ecoul>
  <exc>         -4.38018166 </exc>
  <esr>          0.06030897 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433398 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433398 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71110719 0.00000000 -0.00000002 </position>
    <velocity> 0.00000462 -0.00000000 -0.00000000 </velocity>
    <force> -0.00344334 -0.00000004 -0.00000127 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30150001 0.00000003 </position>
    <velocity> 0.00000000 0.00016443 0.00000000 </velocity>
    <force> 0.00000006 -0.00222520 0.00000121 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71110719 -0.00000000 -0.00000001 </position>
    <velocity> -0.00000462 0.00000000 -0.00000000 </velocity>
    <force> 0.00344332 0.00000003 -0.00000120 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30150001 0.00000000 </position>
    <velocity> -0.00000000 -0.00016443 0.00000000 </velocity>
    <force> -0.00000004 0.00222521 0.00000141 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000348 </ekin_e>
  <ekin_ion> 0.00138532 </ekin_ion>
  <temp_ion> 72.91188058 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294170 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="226">
  <ekin>         5.26684119 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42927372 </eps>
  <enl>          4.76879142 </enl>
  <ecoul>      -15.60069904 </ecoul>
  <exc>         -4.37999071 </exc>
  <esr>          0.06023976 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37433085 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37433085 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71112406 0.00000000 -0.00000002 </position>
    <velocity> 0.00000435 -0.00000000 -0.00000000 </velocity>
    <force> -0.00347210 -0.00000004 -0.00000122 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30215666 0.00000003 </position>
    <velocity> 0.00000000 0.00016425 0.00000000 </velocity>
    <force> 0.00000004 -0.00233069 0.00000112 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71112406 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000435 0.00000000 -0.00000000 </velocity>
    <force> 0.00347209 0.00000002 -0.00000114 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30215666 0.00000001 </position>
    <velocity> -0.00000000 -0.00016425 0.00000000 </velocity>
    <force> -0.00000004 0.00233070 0.00000139 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000348 </ekin_e>
  <ekin_ion> 0.00138220 </ekin_ion>
  <temp_ion> 72.74772036 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294170 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="227">
  <ekin>         5.26637954 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42899565 </eps>
  <enl>          4.76876982 </enl>
  <ecoul>      -15.60068099 </ecoul>
  <exc>         -4.37980032 </exc>
  <esr>          0.06017084 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37432760 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37432760 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71113983 0.00000000 -0.00000002 </position>
    <velocity> 0.00000408 -0.00000000 -0.00000000 </velocity>
    <force> -0.00350024 -0.00000003 -0.00000117 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30281254 0.00000003 </position>
    <velocity> 0.00000000 0.00016407 0.00000000 </velocity>
    <force> 0.00000003 -0.00243531 0.00000102 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71113983 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000408 0.00000000 -0.00000000 </velocity>
    <force> 0.00350024 0.00000001 -0.00000107 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30281254 0.00000001 </position>
    <velocity> -0.00000000 -0.00016407 0.00000000 </velocity>
    <force> -0.00000003 0.00243532 0.00000137 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000347 </ekin_e>
  <ekin_ion> 0.00137895 </ekin_ion>
  <temp_ion> 72.57681773 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294171 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="228">
  <ekin>         5.26591963 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42871885 </eps>
  <enl>          4.76874851 </enl>
  <ecoul>      -15.60066299 </ecoul>
  <exc>         -4.37961052 </exc>
  <esr>          0.06010222 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37432422 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37432422 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71115451 0.00000000 -0.00000003 </position>
    <velocity> 0.00000381 -0.00000000 -0.00000000 </velocity>
    <force> -0.00352783 -0.00000002 -0.00000111 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30346763 0.00000004 </position>
    <velocity> 0.00000000 0.00016387 0.00000000 </velocity>
    <force> 0.00000002 -0.00253922 0.00000091 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71115451 -0.00000000 -0.00000002 </position>
    <velocity> -0.00000381 0.00000000 -0.00000000 </velocity>
    <force> 0.00352784 0.00000000 -0.00000100 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30346763 0.00000001 </position>
    <velocity> -0.00000000 -0.00016387 0.00000000 </velocity>
    <force> -0.00000002 0.00253924 0.00000133 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000346 </ekin_e>
  <ekin_ion> 0.00137558 </ekin_ion>
  <temp_ion> 72.39926248 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294172 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="229">
  <ekin>         5.26546151 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42844368 </eps>
  <enl>          4.76872797 </enl>
  <ecoul>      -15.60064515 </ecoul>
  <exc>         -4.37942136 </exc>
  <esr>          0.06003389 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37432071 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37432071 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71116807 0.00000000 -0.00000003 </position>
    <velocity> 0.00000353 -0.00000000 -0.00000000 </velocity>
    <force> -0.00355505 -0.00000002 -0.00000104 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30412190 0.00000004 </position>
    <velocity> 0.00000000 0.00016367 0.00000000 </velocity>
    <force> 0.00000001 -0.00264270 0.00000079 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71116807 -0.00000000 -0.00000003 </position>
    <velocity> -0.00000353 0.00000000 -0.00000000 </velocity>
    <force> 0.00355507 -0.00000000 -0.00000092 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30412190 0.00000002 </position>
    <velocity> -0.00000000 -0.00016367 0.00000000 </velocity>
    <force> -0.00000001 0.00264272 0.00000128 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000345 </ekin_e>
  <ekin_ion> 0.00137208 </ekin_ion>
  <temp_ion> 72.21512972 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294173 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="230">
  <ekin>         5.26500521 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42817040 </eps>
  <enl>          4.76870853 </enl>
  <ecoul>      -15.60062754 </ecoul>
  <exc>         -4.37923288 </exc>
  <esr>          0.05996586 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37431707 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37431707 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71118051 0.00000000 -0.00000003 </position>
    <velocity> 0.00000325 -0.00000000 -0.00000000 </velocity>
    <force> -0.00358211 -0.00000001 -0.00000096 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30477531 0.00000005 </position>
    <velocity> 0.00000000 0.00016346 0.00000000 </velocity>
    <force> -0.00000000 -0.00274602 0.00000068 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71118051 -0.00000000 -0.00000003 </position>
    <velocity> -0.00000325 0.00000000 -0.00000000 </velocity>
    <force> 0.00358214 -0.00000001 -0.00000084 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30477531 0.00000002 </position>
    <velocity> -0.00000000 -0.00016346 0.00000000 </velocity>
    <force> -0.00000000 0.00274604 0.00000122 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000344 </ekin_e>
  <ekin_ion> 0.00136846 </ekin_ion>
  <temp_ion> 72.02447656 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294174 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="231">
  <ekin>         5.26455074 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42789910 </eps>
  <enl>          4.76869034 </enl>
  <ecoul>      -15.60061018 </ecoul>
  <exc>         -4.37904510 </exc>
  <esr>          0.05989813 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37431331 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37431331 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71119182 0.00000000 -0.00000004 </position>
    <velocity> 0.00000297 -0.00000000 -0.00000000 </velocity>
    <force> -0.00360921 -0.00000000 -0.00000087 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30542782 0.00000005 </position>
    <velocity> 0.00000000 0.00016324 0.00000000 </velocity>
    <force> -0.00000002 -0.00284940 0.00000056 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71119182 -0.00000000 -0.00000004 </position>
    <velocity> -0.00000297 0.00000000 -0.00000000 </velocity>
    <force> 0.00360924 -0.00000002 -0.00000075 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.30542782 0.00000002 </position>
    <velocity> -0.00000000 -0.00016324 0.00000000 </velocity>
    <force> 0.00000001 0.00284942 0.00000115 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000342 </ekin_e>
  <ekin_ion> 0.00136471 </ekin_ion>
  <temp_ion> 71.82734367 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294176 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="232">
  <ekin>         5.26409806 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42762971 </eps>
  <enl>          4.76867331 </enl>
  <ecoul>      -15.60059305 </ecoul>
  <exc>         -4.37885805 </exc>
  <esr>          0.05983071 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37430943 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37430943 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71120200 0.00000000 -0.00000004 </position>
    <velocity> 0.00000269 -0.00000000 -0.00000000 </velocity>
    <force> -0.00363647 0.00000001 -0.00000078 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30607942 0.00000006 </position>
    <velocity> 0.00000000 0.00016301 0.00000000 </velocity>
    <force> -0.00000003 -0.00295295 0.00000043 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71120200 -0.00000000 -0.00000004 </position>
    <velocity> -0.00000269 0.00000000 -0.00000000 </velocity>
    <force> 0.00363651 -0.00000003 -0.00000066 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.30607942 0.00000003 </position>
    <velocity> -0.00000000 -0.00016301 0.00000000 </velocity>
    <force> 0.00000001 0.00295297 0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000341 </ekin_e>
  <ekin_ion> 0.00136085 </ekin_ion>
  <temp_ion> 71.62376119 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294177 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="233">
  <ekin>         5.26364713 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42736204 </eps>
  <enl>          4.76865724 </enl>
  <ecoul>      -15.60057606 </ecoul>
  <exc>         -4.37867170 </exc>
  <esr>          0.05976360 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37430543 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37430543 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71121103 0.00000000 -0.00000005 </position>
    <velocity> 0.00000240 -0.00000000 -0.00000000 </velocity>
    <force> -0.00366393 0.00000001 -0.00000067 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30673006 0.00000006 </position>
    <velocity> 0.00000000 0.00016278 0.00000000 </velocity>
    <force> -0.00000004 -0.00305663 0.00000031 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71121103 -0.00000000 -0.00000005 </position>
    <velocity> -0.00000240 0.00000000 -0.00000000 </velocity>
    <force> 0.00366398 -0.00000003 -0.00000056 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.30673006 0.00000003 </position>
    <velocity> -0.00000000 -0.00016278 0.00000000 </velocity>
    <force> 0.00000002 0.00305665 0.00000098 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000339 </ekin_e>
  <ekin_ion> 0.00135686 </ekin_ion>
  <temp_ion> 71.41375783 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294178 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="234">
  <ekin>         5.26319790 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42709586 </eps>
  <enl>          4.76864180 </enl>
  <ecoul>      -15.60055911 </ecoul>
  <exc>         -4.37848604 </exc>
  <esr>          0.05969681 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37430130 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37430130 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71121891 0.00000000 -0.00000005 </position>
    <velocity> 0.00000211 -0.00000000 -0.00000000 </velocity>
    <force> -0.00369154 0.00000002 -0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.30737971 0.00000007 </position>
    <velocity> 0.00000000 0.00016254 0.00000000 </velocity>
    <force> -0.00000005 -0.00316028 0.00000019 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71121891 -0.00000000 -0.00000005 </position>
    <velocity> -0.00000211 0.00000000 -0.00000000 </velocity>
    <force> 0.00369159 -0.00000004 -0.00000046 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.30737971 0.00000004 </position>
    <velocity> -0.00000000 -0.00016254 0.00000000 </velocity>
    <force> 0.00000003 0.00316029 0.00000087 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000338 </ekin_e>
  <ekin_ion> 0.00135275 </ekin_ion>
  <temp_ion> 71.19737065 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294180 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="235">
  <ekin>         5.26275032 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42683092 </eps>
  <enl>          4.76862668 </enl>
  <ecoul>      -15.60054212 </ecoul>
  <exc>         -4.37830102 </exc>
  <esr>          0.05963032 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37429706 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37429706 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71122563 0.00000000 -0.00000006 </position>
    <velocity> 0.00000182 -0.00000000 -0.00000000 </velocity>
    <force> -0.00371912 0.00000003 -0.00000044 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.30802834 0.00000007 </position>
    <velocity> 0.00000000 0.00016229 0.00000000 </velocity>
    <force> -0.00000006 -0.00326362 0.00000007 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71122563 -0.00000000 -0.00000006 </position>
    <velocity> -0.00000182 0.00000000 -0.00000000 </velocity>
    <force> 0.00371918 -0.00000004 -0.00000036 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.30802834 0.00000004 </position>
    <velocity> -0.00000000 -0.00016229 0.00000000 </velocity>
    <force> 0.00000004 0.00326363 0.00000076 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000337 </ekin_e>
  <ekin_ion> 0.00134851 </ekin_ion>
  <temp_ion> 70.97465331 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294181 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="236">
  <ekin>         5.26230435 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42656705 </eps>
  <enl>          4.76861164 </enl>
  <ecoul>      -15.60052502 </ecoul>
  <exc>         -4.37811663 </exc>
  <esr>          0.05956416 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37429270 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37429270 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71123117 0.00000000 -0.00000006 </position>
    <velocity> 0.00000153 -0.00000000 -0.00000000 </velocity>
    <force> -0.00374647 0.00000004 -0.00000032 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.30867592 0.00000008 </position>
    <velocity> 0.00000000 0.00016203 0.00000000 </velocity>
    <force> -0.00000007 -0.00336634 -0.00000005 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71123117 -0.00000000 -0.00000006 </position>
    <velocity> -0.00000153 0.00000000 -0.00000000 </velocity>
    <force> 0.00374653 -0.00000005 -0.00000026 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.30867592 0.00000005 </position>
    <velocity> -0.00000000 -0.00016203 0.00000000 </velocity>
    <force> 0.00000005 0.00336635 0.00000064 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000336 </ekin_e>
  <ekin_ion> 0.00134416 </ekin_ion>
  <temp_ion> 70.74568027 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294182 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="237">
  <ekin>         5.26186001 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42630418 </eps>
  <enl>          4.76859652 </enl>
  <ecoul>      -15.60050774 </ecoul>
  <exc>         -4.37793283 </exc>
  <esr>          0.05949832 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37428822 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37428822 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71123554 0.00000000 -0.00000007 </position>
    <velocity> 0.00000124 -0.00000000 -0.00000000 </velocity>
    <force> -0.00377335 0.00000004 -0.00000019 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.30932241 0.00000009 </position>
    <velocity> 0.00000000 0.00016176 0.00000000 </velocity>
    <force> -0.00000008 -0.00346819 -0.00000017 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71123554 -0.00000000 -0.00000007 </position>
    <velocity> -0.00000124 0.00000000 -0.00000000 </velocity>
    <force> 0.00377341 -0.00000005 -0.00000016 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.30932241 0.00000005 </position>
    <velocity> -0.00000000 -0.00016176 0.00000000 </velocity>
    <force> 0.00000005 0.00346820 0.00000051 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000335 </ekin_e>
  <ekin_ion> 0.00133970 </ekin_ion>
  <temp_ion> 70.51054618 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294183 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="238">
  <ekin>         5.26141734 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42604232 </eps>
  <enl>          4.76858128 </enl>
  <ecoul>      -15.60049031 </ecoul>
  <exc>         -4.37774962 </exc>
  <esr>          0.05943281 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37428363 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37428363 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71123872 0.00000000 -0.00000007 </position>
    <velocity> 0.00000094 -0.00000000 -0.00000000 </velocity>
    <force> -0.00379959 0.00000005 -0.00000006 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.30996779 0.00000009 </position>
    <velocity> 0.00000000 0.00016148 0.00000000 </velocity>
    <force> -0.00000008 -0.00356902 -0.00000028 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71123872 -0.00000000 -0.00000007 </position>
    <velocity> -0.00000094 0.00000000 -0.00000000 </velocity>
    <force> 0.00379966 -0.00000006 -0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.30996779 0.00000006 </position>
    <velocity> -0.00000000 -0.00016148 0.00000000 </velocity>
    <force> 0.00000006 0.00356902 0.00000038 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000334 </ekin_e>
  <ekin_ion> 0.00133511 </ekin_ion>
  <temp_ion> 70.26936025 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294184 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="239">
  <ekin>         5.26097643 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42578157 </eps>
  <enl>          4.76856599 </enl>
  <ecoul>      -15.60047274 </ecoul>
  <exc>         -4.37756703 </exc>
  <esr>          0.05936762 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37427892 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37427892 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71124070 0.00000000 -0.00000008 </position>
    <velocity> 0.00000065 -0.00000000 -0.00000000 </velocity>
    <force> -0.00382511 0.00000005 0.00000007 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31061202 0.00000010 </position>
    <velocity> 0.00000000 0.00016120 0.00000000 </velocity>
    <force> -0.00000009 -0.00366882 -0.00000038 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71124070 -0.00000000 -0.00000008 </position>
    <velocity> -0.00000065 0.00000000 -0.00000000 </velocity>
    <force> 0.00382517 -0.00000006 0.00000006 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31061202 0.00000007 </position>
    <velocity> -0.00000000 -0.00016120 0.00000000 </velocity>
    <force> 0.00000006 0.00366883 0.00000024 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000332 </ekin_e>
  <ekin_ion> 0.00133042 </ekin_ion>
  <temp_ion> 70.02223720 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294185 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="240">
  <ekin>         5.26053738 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42552204 </eps>
  <enl>          4.76855073 </enl>
  <ecoul>      -15.60045507 </ecoul>
  <exc>         -4.37738510 </exc>
  <esr>          0.05930276 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37427410 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37427410 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71124148 0.00000000 -0.00000008 </position>
    <velocity> 0.00000035 -0.00000000 -0.00000000 </velocity>
    <force> -0.00384990 0.00000006 0.00000019 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31125508 0.00000010 </position>
    <velocity> 0.00000000 0.00016091 0.00000000 </velocity>
    <force> -0.00000009 -0.00376775 -0.00000048 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71124148 -0.00000000 -0.00000008 </position>
    <velocity> -0.00000035 0.00000000 -0.00000000 </velocity>
    <force> 0.00384996 -0.00000006 0.00000017 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31125508 0.00000007 </position>
    <velocity> -0.00000000 -0.00016091 0.00000000 </velocity>
    <force> 0.00000007 0.00376775 0.00000011 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000331 </ekin_e>
  <ekin_ion> 0.00132561 </ekin_ion>
  <temp_ion> 69.76928706 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294187 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="241">
  <ekin>         5.26010034 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42526383 </eps>
  <enl>          4.76853557 </enl>
  <ecoul>      -15.60043737 </ecoul>
  <exc>         -4.37720387 </exc>
  <esr>          0.05923824 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37426917 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37426917 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71124105 0.00000000 -0.00000009 </position>
    <velocity> 0.00000004 -0.00000000 -0.00000000 </velocity>
    <force> -0.00387409 0.00000006 0.00000031 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31189693 0.00000010 </position>
    <velocity> 0.00000000 0.00016061 0.00000000 </velocity>
    <force> -0.00000009 -0.00386606 -0.00000057 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71124105 -0.00000000 -0.00000009 </position>
    <velocity> -0.00000004 -0.00000000 -0.00000000 </velocity>
    <force> 0.00387416 -0.00000006 0.00000028 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31189693 0.00000008 </position>
    <velocity> -0.00000000 -0.00016061 0.00000000 </velocity>
    <force> 0.00000007 0.00386606 -0.00000004 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000329 </ekin_e>
  <ekin_ion> 0.00132070 </ekin_ion>
  <temp_ion> 69.51060641 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294188 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="242">
  <ekin>         5.25966543 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42500700 </eps>
  <enl>          4.76852052 </enl>
  <ecoul>      -15.60041967 </ecoul>
  <exc>         -4.37702340 </exc>
  <esr>          0.05917406 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37426412 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37426412 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71123940 0.00000000 -0.00000009 </position>
    <velocity> -0.00000026 -0.00000000 -0.00000000 </velocity>
    <force> -0.00389789 0.00000006 0.00000043 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31253753 0.00000011 </position>
    <velocity> 0.00000000 0.00016031 0.00000000 </velocity>
    <force> -0.00000009 -0.00396405 -0.00000066 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71123940 -0.00000000 -0.00000009 </position>
    <velocity> 0.00000026 -0.00000000 -0.00000000 </velocity>
    <force> 0.00389795 -0.00000006 0.00000039 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31253753 0.00000008 </position>
    <velocity> -0.00000000 -0.00016031 0.00000000 </velocity>
    <force> 0.00000007 0.00396405 -0.00000018 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000327 </ekin_e>
  <ekin_ion> 0.00131567 </ekin_ion>
  <temp_ion> 69.24627343 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294190 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="243">
  <ekin>         5.25923272 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42475153 </eps>
  <enl>          4.76850554 </enl>
  <ecoul>      -15.60040199 </ecoul>
  <exc>         -4.37684372 </exc>
  <esr>          0.05911022 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37425897 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37425897 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71123653 0.00000000 -0.00000010 </position>
    <velocity> -0.00000057 -0.00000000 -0.00000000 </velocity>
    <force> -0.00392154 0.00000006 0.00000054 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31317687 0.00000011 </position>
    <velocity> -0.00000000 0.00015999 0.00000000 </velocity>
    <force> -0.00000009 -0.00406198 -0.00000075 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71123653 -0.00000000 -0.00000009 </position>
    <velocity> 0.00000057 -0.00000000 -0.00000000 </velocity>
    <force> 0.00392159 -0.00000005 0.00000050 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31317687 0.00000009 </position>
    <velocity> -0.00000000 -0.00015999 0.00000000 </velocity>
    <force> 0.00000007 0.00406198 -0.00000032 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000325 </ekin_e>
  <ekin_ion> 0.00131055 </ekin_ion>
  <temp_ion> 68.97634769 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294192 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="244">
  <ekin>         5.25880226 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42449732 </eps>
  <enl>          4.76849053 </enl>
  <ecoul>      -15.60038433 </ecoul>
  <exc>         -4.37666486 </exc>
  <esr>          0.05904672 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37425372 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37425372 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71123242 0.00000000 -0.00000010 </position>
    <velocity> -0.00000087 0.00000000 -0.00000000 </velocity>
    <force> -0.00394525 0.00000006 0.00000064 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31381491 0.00000012 </position>
    <velocity> -0.00000000 0.00015967 0.00000000 </velocity>
    <force> -0.00000009 -0.00416004 -0.00000082 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71123242 -0.00000000 -0.00000010 </position>
    <velocity> 0.00000087 -0.00000000 -0.00000000 </velocity>
    <force> 0.00394530 -0.00000005 0.00000060 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31381491 0.00000009 </position>
    <velocity> 0.00000000 -0.00015967 0.00000000 </velocity>
    <force> 0.00000007 0.00416004 -0.00000046 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000323 </ekin_e>
  <ekin_ion> 0.00130531 </ekin_ion>
  <temp_ion> 68.70087474 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294195 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="245">
  <ekin>         5.25837398 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42424427 </eps>
  <enl>          4.76847536 </enl>
  <ecoul>      -15.60036663 </ecoul>
  <exc>         -4.37648679 </exc>
  <esr>          0.05898357 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37424836 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37424836 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71122707 0.00000000 -0.00000011 </position>
    <velocity> -0.00000118 0.00000000 -0.00000000 </velocity>
    <force> -0.00396918 0.00000006 0.00000074 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31445162 0.00000012 </position>
    <velocity> -0.00000000 0.00015934 0.00000000 </velocity>
    <force> -0.00000009 -0.00425827 -0.00000089 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71122707 -0.00000000 -0.00000010 </position>
    <velocity> 0.00000118 -0.00000000 -0.00000000 </velocity>
    <force> 0.00396922 -0.00000005 0.00000069 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31445162 0.00000010 </position>
    <velocity> 0.00000000 -0.00015934 0.00000000 </velocity>
    <force> 0.00000007 0.00425826 -0.00000060 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000321 </ekin_e>
  <ekin_ion> 0.00129997 </ekin_ion>
  <temp_ion> 68.41989377 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294197 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="246">
  <ekin>         5.25794774 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42399224 </eps>
  <enl>          4.76845995 </enl>
  <ecoul>      -15.60034886 </ecoul>
  <exc>         -4.37630948 </exc>
  <esr>          0.05892076 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37424289 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37424289 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71122047 0.00000000 -0.00000011 </position>
    <velocity> -0.00000149 0.00000000 -0.00000000 </velocity>
    <force> -0.00399338 0.00000006 0.00000083 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31508697 0.00000012 </position>
    <velocity> -0.00000000 0.00015901 0.00000000 </velocity>
    <force> -0.00000008 -0.00435659 -0.00000096 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71122047 -0.00000000 -0.00000011 </position>
    <velocity> 0.00000149 -0.00000000 -0.00000000 </velocity>
    <force> 0.00399341 -0.00000004 0.00000078 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31508697 0.00000011 </position>
    <velocity> 0.00000000 -0.00015901 0.00000000 </velocity>
    <force> 0.00000007 0.00435658 -0.00000074 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000318 </ekin_e>
  <ekin_ion> 0.00129453 </ekin_ion>
  <temp_ion> 68.13344630 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294199 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="247">
  <ekin>         5.25752338 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42374116 </eps>
  <enl>          4.76844429 </enl>
  <ecoul>      -15.60033095 </ecoul>
  <exc>         -4.37613289 </exc>
  <esr>          0.05885831 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37423732 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37423732 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71121262 0.00000000 -0.00000012 </position>
    <velocity> -0.00000181 0.00000000 -0.00000000 </velocity>
    <force> -0.00401779 0.00000006 0.00000092 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.31572092 0.00000013 </position>
    <velocity> -0.00000000 0.00015866 0.00000000 </velocity>
    <force> -0.00000008 -0.00445483 -0.00000101 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71121262 -0.00000000 -0.00000011 </position>
    <velocity> 0.00000181 -0.00000000 -0.00000000 </velocity>
    <force> 0.00401781 -0.00000004 0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31572092 0.00000011 </position>
    <velocity> 0.00000000 -0.00015866 0.00000000 </velocity>
    <force> 0.00000006 0.00445482 -0.00000088 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000316 </ekin_e>
  <ekin_ion> 0.00128899 </ekin_ion>
  <temp_ion> 67.84158333 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294202 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="248">
  <ekin>         5.25710068 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42349100 </eps>
  <enl>          4.76842843 </enl>
  <ecoul>      -15.60031284 </ecoul>
  <exc>         -4.37595693 </exc>
  <esr>          0.05879621 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37423165 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37423165 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71120351 0.00000000 -0.00000012 </position>
    <velocity> -0.00000212 0.00000000 -0.00000000 </velocity>
    <force> -0.00404224 0.00000005 0.00000100 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.31635345 0.00000013 </position>
    <velocity> -0.00000000 0.00015831 0.00000000 </velocity>
    <force> -0.00000007 -0.00455279 -0.00000106 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71120351 -0.00000000 -0.00000011 </position>
    <velocity> 0.00000212 -0.00000000 -0.00000000 </velocity>
    <force> 0.00404225 -0.00000003 0.00000095 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31635345 0.00000011 </position>
    <velocity> 0.00000000 -0.00015831 0.00000000 </velocity>
    <force> 0.00000006 0.00455278 -0.00000101 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000314 </ekin_e>
  <ekin_ion> 0.00128334 </ekin_ion>
  <temp_ion> 67.54436939 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294204 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="249">
  <ekin>         5.25667948 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42324180 </eps>
  <enl>          4.76841247 </enl>
  <ecoul>      -15.60029448 </ecoul>
  <exc>         -4.37578155 </exc>
  <esr>          0.05873447 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37422588 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37422588 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71119312 0.00000000 -0.00000012 </position>
    <velocity> -0.00000244 0.00000000 -0.00000000 </velocity>
    <force> -0.00406652 0.00000005 0.00000108 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.31698453 0.00000013 </position>
    <velocity> -0.00000000 0.00015795 0.00000000 </velocity>
    <force> -0.00000006 -0.00465028 -0.00000110 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71119312 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000244 -0.00000000 -0.00000000 </velocity>
    <force> 0.00406652 -0.00000003 0.00000102 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31698453 0.00000012 </position>
    <velocity> 0.00000000 -0.00015795 0.00000000 </velocity>
    <force> 0.00000006 0.00465026 -0.00000113 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000312 </ekin_e>
  <ekin_ion> 0.00127759 </ekin_ion>
  <temp_ion> 67.24188278 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294206 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="250">
  <ekin>         5.25625971 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42299362 </eps>
  <enl>          4.76839650 </enl>
  <ecoul>      -15.60027587 </ecoul>
  <exc>         -4.37560674 </exc>
  <esr>          0.05867308 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37422002 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37422002 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71118146 0.00000000 -0.00000013 </position>
    <velocity> -0.00000276 0.00000000 -0.00000000 </velocity>
    <force> -0.00409040 0.00000004 0.00000115 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.31761412 0.00000014 </position>
    <velocity> -0.00000000 0.00015758 0.00000000 </velocity>
    <force> -0.00000005 -0.00474718 -0.00000113 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71118146 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000276 -0.00000000 -0.00000000 </velocity>
    <force> 0.00409039 -0.00000002 0.00000108 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31761412 0.00000012 </position>
    <velocity> 0.00000000 -0.00015758 0.00000000 </velocity>
    <force> 0.00000005 0.00474716 -0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000310 </ekin_e>
  <ekin_ion> 0.00127175 </ekin_ion>
  <temp_ion> 66.93421241 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294208 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="251">
  <ekin>         5.25584138 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42274655 </eps>
  <enl>          4.76838060 </enl>
  <ecoul>      -15.60025701 </ecoul>
  <exc>         -4.37543248 </exc>
  <esr>          0.05861206 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37421406 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37421406 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71116851 0.00000000 -0.00000013 </position>
    <velocity> -0.00000308 0.00000000 -0.00000000 </velocity>
    <force> -0.00411368 0.00000004 0.00000122 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.31824221 0.00000014 </position>
    <velocity> -0.00000000 0.00015721 0.00000000 </velocity>
    <force> -0.00000004 -0.00484344 -0.00000116 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71116851 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000308 -0.00000000 -0.00000000 </velocity>
    <force> 0.00411366 -0.00000002 0.00000114 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31824221 0.00000013 </position>
    <velocity> 0.00000000 -0.00015721 0.00000000 </velocity>
    <force> 0.00000004 0.00484342 -0.00000135 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000308 </ekin_e>
  <ekin_ion> 0.00126580 </ekin_ion>
  <temp_ion> 66.62145288 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294210 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="252">
  <ekin>         5.25542465 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42250067 </eps>
  <enl>          4.76836478 </enl>
  <ecoul>      -15.60023795 </ecoul>
  <exc>         -4.37525882 </exc>
  <esr>          0.05855141 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37420800 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37420800 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71115427 0.00000000 -0.00000013 </position>
    <velocity> -0.00000340 0.00000000 -0.00000000 </velocity>
    <force> -0.00413626 0.00000003 0.00000128 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.31886874 0.00000014 </position>
    <velocity> -0.00000000 0.00015683 0.00000000 </velocity>
    <force> -0.00000003 -0.00493910 -0.00000117 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71115427 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000340 -0.00000000 -0.00000000 </velocity>
    <force> 0.00413623 -0.00000001 0.00000119 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31886874 0.00000013 </position>
    <velocity> 0.00000000 -0.00015683 0.00000000 </velocity>
    <force> 0.00000003 0.00493908 -0.00000145 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000306 </ekin_e>
  <ekin_ion> 0.00125977 </ekin_ion>
  <temp_ion> 66.30369941 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294212 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="253">
  <ekin>         5.25500975 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42225607 </eps>
  <enl>          4.76834906 </enl>
  <ecoul>      -15.60021876 </ecoul>
  <exc>         -4.37508584 </exc>
  <esr>          0.05849112 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37420185 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37420185 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71113872 0.00000000 -0.00000013 </position>
    <velocity> -0.00000372 0.00000000 -0.00000000 </velocity>
    <force> -0.00415810 0.00000002 0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.31949371 0.00000014 </position>
    <velocity> -0.00000000 0.00015644 0.00000000 </velocity>
    <force> -0.00000002 -0.00503422 -0.00000118 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71113872 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000372 -0.00000000 -0.00000000 </velocity>
    <force> 0.00415806 -0.00000000 0.00000124 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.31949371 0.00000013 </position>
    <velocity> 0.00000000 -0.00015644 0.00000000 </velocity>
    <force> 0.00000003 0.00503420 -0.00000153 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000304 </ekin_e>
  <ekin_ion> 0.00125364 </ekin_ion>
  <temp_ion> 65.98104417 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294214 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="254">
  <ekin>         5.25459700 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42201289 </eps>
  <enl>          4.76833346 </enl>
  <ecoul>      -15.60019954 </ecoul>
  <exc>         -4.37491364 </exc>
  <esr>          0.05843120 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37419561 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37419561 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71112188 0.00000000 -0.00000013 </position>
    <velocity> -0.00000405 0.00000000 -0.00000000 </velocity>
    <force> -0.00417928 0.00000001 0.00000137 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32011707 0.00000014 </position>
    <velocity> -0.00000000 0.00015604 0.00000000 </velocity>
    <force> -0.00000000 -0.00512888 -0.00000118 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71112188 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000405 -0.00000000 -0.00000000 </velocity>
    <force> 0.00417924 0.00000000 0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32011707 0.00000013 </position>
    <velocity> 0.00000000 -0.00015604 0.00000000 </velocity>
    <force> 0.00000002 0.00512887 -0.00000160 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000302 </ekin_e>
  <ekin_ion> 0.00124741 </ekin_ion>
  <temp_ion> 65.65357476 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294215 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="255">
  <ekin>         5.25418669 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42177132 </eps>
  <enl>          4.76831811 </enl>
  <ecoul>      -15.60018042 </ecoul>
  <exc>         -4.37474234 </exc>
  <esr>          0.05837166 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37418928 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37418928 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71110372 0.00000000 -0.00000013 </position>
    <velocity> -0.00000438 0.00000000 -0.00000000 </velocity>
    <force> -0.00419992 0.00000001 0.00000140 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32073880 0.00000014 </position>
    <velocity> -0.00000000 0.00015564 0.00000000 </velocity>
    <force> 0.00000001 -0.00522314 -0.00000118 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71110371 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000438 -0.00000000 -0.00000000 </velocity>
    <force> 0.00419986 0.00000001 0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32073880 0.00000013 </position>
    <velocity> 0.00000000 -0.00015564 0.00000000 </velocity>
    <force> 0.00000001 0.00522312 -0.00000166 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000300 </ekin_e>
  <ekin_ion> 0.00124110 </ekin_ion>
  <temp_ion> 65.32137489 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294518 </econst>
  <ekin_ec> -15.37294217 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="256">
  <ekin>         5.25377908 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42153162 </eps>
  <enl>          4.76830328 </enl>
  <ecoul>      -15.60016155 </ecoul>
  <exc>         -4.37457205 </exc>
  <esr>          0.05831249 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37418286 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37418286 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71108424 0.00000000 -0.00000013 </position>
    <velocity> -0.00000470 0.00000000 -0.00000000 </velocity>
    <force> -0.00422015 -0.00000000 0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32135886 0.00000014 </position>
    <velocity> -0.00000000 0.00015522 0.00000000 </velocity>
    <force> 0.00000002 -0.00531700 -0.00000116 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71108424 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000470 -0.00000000 -0.00000000 </velocity>
    <force> 0.00422010 0.00000002 0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32135886 0.00000014 </position>
    <velocity> 0.00000000 -0.00015522 0.00000000 </velocity>
    <force> -0.00000000 0.00531699 -0.00000170 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000298 </ekin_e>
  <ekin_ion> 0.00123470 </ekin_ion>
  <temp_ion> 64.98452643 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294219 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.011" max="    0.011"/>
<iteration count="257">
  <ekin>         5.25337436 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42129413 </eps>
  <enl>          4.76828935 </enl>
  <ecoul>      -15.60014305 </ecoul>
  <exc>         -4.37440288 </exc>
  <esr>          0.05825370 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37417635 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37417635 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71106343 0.00000000 -0.00000013 </position>
    <velocity> -0.00000504 0.00000000 -0.00000000 </velocity>
    <force> -0.00424013 -0.00000001 0.00000142 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32197724 0.00000014 </position>
    <velocity> -0.00000000 0.00015481 -0.00000000 </velocity>
    <force> 0.00000003 -0.00541047 -0.00000115 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71106343 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000504 -0.00000000 -0.00000000 </velocity>
    <force> 0.00424007 0.00000002 0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32197724 0.00000014 </position>
    <velocity> 0.00000000 -0.00015481 0.00000000 </velocity>
    <force> -0.00000001 0.00541046 -0.00000173 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000296 </ekin_e>
  <ekin_ion> 0.00122821 </ekin_ion>
  <temp_ion> 64.64311186 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294221 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="258">
  <ekin>         5.25297260 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42105920 </eps>
  <enl>          4.76827677 </enl>
  <ecoul>      -15.60012503 </ecoul>
  <exc>         -4.37423491 </exc>
  <esr>          0.05819528 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37416976 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37416976 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71104130 0.00000000 -0.00000013 </position>
    <velocity> -0.00000537 0.00000000 0.00000000 </velocity>
    <force> -0.00425994 -0.00000002 0.00000141 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32259390 0.00000014 </position>
    <velocity> -0.00000000 0.00015438 -0.00000000 </velocity>
    <force> 0.00000004 -0.00550348 -0.00000112 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71104130 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000537 -0.00000000 0.00000000 </velocity>
    <force> 0.00425988 0.00000003 0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32259390 0.00000014 </position>
    <velocity> 0.00000000 -0.00015438 0.00000000 </velocity>
    <force> -0.00000002 0.00550347 -0.00000174 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000295 </ekin_e>
  <ekin_ion> 0.00122164 </ekin_ion>
  <temp_ion> 64.29721631 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294223 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="259">
  <ekin>         5.25257383 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42082707 </eps>
  <enl>          4.76826590 </enl>
  <ecoul>      -15.60010758 </ecoul>
  <exc>         -4.37406817 </exc>
  <esr>          0.05813725 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37416309 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37416309 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71101782 0.00000000 -0.00000013 </position>
    <velocity> -0.00000570 0.00000000 0.00000000 </velocity>
    <force> -0.00427965 -0.00000002 0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32320880 0.00000014 </position>
    <velocity> -0.00000000 0.00015395 -0.00000000 </velocity>
    <force> 0.00000005 -0.00559600 -0.00000110 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71101782 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000570 -0.00000000 0.00000000 </velocity>
    <force> 0.00427959 0.00000003 0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32320880 0.00000013 </position>
    <velocity> 0.00000000 -0.00015395 -0.00000000 </velocity>
    <force> -0.00000003 0.00559600 -0.00000174 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000293 </ekin_e>
  <ekin_ion> 0.00121499 </ekin_ion>
  <temp_ion> 63.94692865 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294225 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="260">
  <ekin>         5.25217800 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42059787 </eps>
  <enl>          4.76825692 </enl>
  <ecoul>      -15.60009070 </ecoul>
  <exc>         -4.37390268 </exc>
  <esr>          0.05807961 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37415633 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37415633 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71099301 0.00000000 -0.00000013 </position>
    <velocity> -0.00000604 0.00000000 0.00000000 </velocity>
    <force> -0.00429928 -0.00000003 0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32382193 0.00000014 </position>
    <velocity> -0.00000000 0.00015350 -0.00000000 </velocity>
    <force> 0.00000006 -0.00568797 -0.00000106 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71099301 -0.00000000 -0.00000013 </position>
    <velocity> 0.00000604 -0.00000000 0.00000000 </velocity>
    <force> 0.00429921 0.00000004 0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32382193 0.00000013 </position>
    <velocity> 0.00000000 -0.00015350 -0.00000000 </velocity>
    <force> -0.00000003 0.00568797 -0.00000173 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000291 </ekin_e>
  <ekin_ion> 0.00120825 </ekin_ion>
  <temp_ion> 63.59234164 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294226 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="261">
  <ekin>         5.25178504 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42037148 </eps>
  <enl>          4.76824971 </enl>
  <ecoul>      -15.60007434 </ecoul>
  <exc>         -4.37373843 </exc>
  <esr>          0.05802235 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37414950 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37414950 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71096684 0.00000000 -0.00000013 </position>
    <velocity> -0.00000637 0.00000000 0.00000000 </velocity>
    <force> -0.00431879 -0.00000004 0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32443326 0.00000013 </position>
    <velocity> -0.00000000 0.00015306 -0.00000000 </velocity>
    <force> 0.00000007 -0.00577936 -0.00000103 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71096684 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000637 -0.00000000 0.00000000 </velocity>
    <force> 0.00431873 0.00000004 0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32443326 0.00000013 </position>
    <velocity> 0.00000000 -0.00015306 -0.00000000 </velocity>
    <force> -0.00000004 0.00577935 -0.00000170 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000289 </ekin_e>
  <ekin_ion> 0.00120143 </ekin_ion>
  <temp_ion> 63.23355122 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294228 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="262">
  <ekin>         5.25139488 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42014756 </eps>
  <enl>          4.76824387 </enl>
  <ecoul>      -15.60005839 </ecoul>
  <exc>         -4.37357538 </exc>
  <esr>          0.05796548 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37414259 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37414259 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71093932 0.00000000 -0.00000013 </position>
    <velocity> -0.00000671 0.00000000 0.00000000 </velocity>
    <force> -0.00433816 -0.00000004 0.00000126 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32504275 0.00000013 </position>
    <velocity> -0.00000000 0.00015260 -0.00000000 </velocity>
    <force> 0.00000008 -0.00587013 -0.00000099 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71093932 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000671 -0.00000000 0.00000000 </velocity>
    <force> 0.00433810 0.00000004 0.00000125 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32504275 0.00000013 </position>
    <velocity> 0.00000000 -0.00015260 -0.00000000 </velocity>
    <force> -0.00000005 0.00587013 -0.00000166 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000287 </ekin_e>
  <ekin_ion> 0.00119454 </ekin_ion>
  <temp_ion> 62.87065554 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294230 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="263">
  <ekin>         5.25100745 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41992562 </eps>
  <enl>          4.76823873 </enl>
  <ecoul>      -15.60004269 </ecoul>
  <exc>         -4.37341346 </exc>
  <esr>          0.05790901 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37413560 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37413560 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71091043 0.00000000 -0.00000012 </position>
    <velocity> -0.00000705 0.00000000 0.00000000 </velocity>
    <force> -0.00435735 -0.00000005 0.00000120 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32565037 0.00000013 </position>
    <velocity> -0.00000000 0.00015214 -0.00000000 </velocity>
    <force> 0.00000008 -0.00596030 -0.00000094 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71091043 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000705 -0.00000000 0.00000000 </velocity>
    <force> 0.00435729 0.00000005 0.00000120 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32565037 0.00000013 </position>
    <velocity> 0.00000000 -0.00015214 -0.00000000 </velocity>
    <force> -0.00000006 0.00596031 -0.00000160 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000286 </ekin_e>
  <ekin_ion> 0.00118757 </ekin_ion>
  <temp_ion> 62.50375367 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294232 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="264">
  <ekin>         5.25062268 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41970510 </eps>
  <enl>          4.76823356 </enl>
  <ecoul>      -15.60002705 </ecoul>
  <exc>         -4.37325262 </exc>
  <esr>          0.05785292 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37412853 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37412853 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71088018 0.00000000 -0.00000012 </position>
    <velocity> -0.00000739 0.00000000 0.00000000 </velocity>
    <force> -0.00437630 -0.00000005 0.00000113 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32625611 0.00000013 </position>
    <velocity> -0.00000000 0.00015167 -0.00000000 </velocity>
    <force> 0.00000009 -0.00604988 -0.00000089 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71088018 -0.00000000 -0.00000012 </position>
    <velocity> 0.00000739 -0.00000000 0.00000000 </velocity>
    <force> 0.00437625 0.00000005 0.00000114 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32625611 0.00000012 </position>
    <velocity> 0.00000000 -0.00015167 -0.00000000 </velocity>
    <force> -0.00000006 0.00604989 -0.00000153 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000284 </ekin_e>
  <ekin_ion> 0.00118052 </ekin_ion>
  <temp_ion> 62.13294433 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294234 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="265">
  <ekin>         5.25024050 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41948549 </eps>
  <enl>          4.76822769 </enl>
  <ecoul>      -15.60001131 </ecoul>
  <exc>         -4.37309278 </exc>
  <esr>          0.05779724 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37412140 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37412140 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71084856 0.00000000 -0.00000012 </position>
    <velocity> -0.00000773 0.00000000 0.00000000 </velocity>
    <force> -0.00439499 -0.00000006 0.00000106 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32685993 0.00000012 </position>
    <velocity> -0.00000000 0.00015119 -0.00000000 </velocity>
    <force> 0.00000009 -0.00613891 -0.00000083 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71084856 -0.00000000 -0.00000011 </position>
    <velocity> 0.00000773 -0.00000000 0.00000000 </velocity>
    <force> 0.00439495 0.00000005 0.00000108 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32685993 0.00000012 </position>
    <velocity> 0.00000000 -0.00015119 -0.00000000 </velocity>
    <force> -0.00000007 0.00613892 -0.00000145 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000282 </ekin_e>
  <ekin_ion> 0.00117340 </ekin_ion>
  <temp_ion> 61.75832455 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294235 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="266">
  <ekin>         5.24986083 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41926647 </eps>
  <enl>          4.76822069 </enl>
  <ecoul>      -15.59999535 </ecoul>
  <exc>         -4.37293389 </exc>
  <esr>          0.05774195 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37411419 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37411419 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71081555 0.00000000 -0.00000011 </position>
    <velocity> -0.00000808 0.00000000 0.00000000 </velocity>
    <force> -0.00441339 -0.00000006 0.00000098 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32746180 0.00000012 </position>
    <velocity> -0.00000000 0.00015071 -0.00000000 </velocity>
    <force> 0.00000009 -0.00622744 -0.00000078 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71081555 -0.00000000 -0.00000011 </position>
    <velocity> 0.00000808 -0.00000000 0.00000000 </velocity>
    <force> 0.00441335 0.00000005 0.00000101 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32746180 0.00000012 </position>
    <velocity> 0.00000000 -0.00015071 -0.00000000 </velocity>
    <force> -0.00000007 0.00622745 -0.00000135 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000280 </ekin_e>
  <ekin_ion> 0.00116622 </ekin_ion>
  <temp_ion> 61.37998862 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294237 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="267">
  <ekin>         5.24948356 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41904794 </eps>
  <enl>          4.76821244 </enl>
  <ecoul>      -15.59997908 </ecoul>
  <exc>         -4.37277589 </exc>
  <esr>          0.05768706 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37410691 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37410691 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71078116 0.00000000 -0.00000011 </position>
    <velocity> -0.00000842 0.00000000 0.00000000 </velocity>
    <force> -0.00443146 -0.00000006 0.00000090 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32806169 0.00000012 </position>
    <velocity> 0.00000000 0.00015022 -0.00000000 </velocity>
    <force> 0.00000009 -0.00631552 -0.00000071 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71078116 -0.00000000 -0.00000011 </position>
    <velocity> 0.00000842 0.00000000 0.00000000 </velocity>
    <force> 0.00443143 0.00000005 0.00000094 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32806169 0.00000011 </position>
    <velocity> 0.00000000 -0.00015022 -0.00000000 </velocity>
    <force> -0.00000008 0.00631554 -0.00000124 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000278 </ekin_e>
  <ekin_ion> 0.00115896 </ekin_ion>
  <temp_ion> 60.99802750 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294239 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="268">
  <ekin>         5.24910860 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41883003 </eps>
  <enl>          4.76820312 </enl>
  <ecoul>      -15.59996250 </ecoul>
  <exc>         -4.37261875 </exc>
  <esr>          0.05763257 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37409957 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37409957 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71074538 0.00000000 -0.00000011 </position>
    <velocity> -0.00000877 0.00000000 0.00000000 </velocity>
    <force> -0.00444918 -0.00000006 0.00000081 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32865959 0.00000011 </position>
    <velocity> 0.00000000 0.00014972 -0.00000000 </velocity>
    <force> 0.00000009 -0.00640321 -0.00000065 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71074538 -0.00000000 -0.00000010 </position>
    <velocity> 0.00000877 0.00000000 0.00000000 </velocity>
    <force> 0.00444916 0.00000005 0.00000086 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32865959 0.00000011 </position>
    <velocity> 0.00000000 -0.00014972 -0.00000000 </velocity>
    <force> -0.00000008 0.00640322 -0.00000112 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000276 </ekin_e>
  <ekin_ion> 0.00115163 </ekin_ion>
  <temp_ion> 60.61252922 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294241 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="269">
  <ekin>         5.24873586 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41861306 </eps>
  <enl>          4.76819315 </enl>
  <ecoul>      -15.59994566 </ecoul>
  <exc>         -4.37246245 </exc>
  <esr>          0.05757849 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37409216 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37409216 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71070821 0.00000000 -0.00000010 </position>
    <velocity> -0.00000912 -0.00000000 0.00000000 </velocity>
    <force> -0.00446651 -0.00000006 0.00000071 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32925546 0.00000011 </position>
    <velocity> 0.00000000 0.00014922 -0.00000000 </velocity>
    <force> 0.00000009 -0.00649049 -0.00000058 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71070821 -0.00000000 -0.00000010 </position>
    <velocity> 0.00000912 0.00000000 0.00000000 </velocity>
    <force> 0.00446650 0.00000005 0.00000077 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32925546 0.00000010 </position>
    <velocity> -0.00000000 -0.00014922 -0.00000000 </velocity>
    <force> -0.00000008 0.00649051 -0.00000099 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000274 </ekin_e>
  <ekin_ion> 0.00114424 </ekin_ion>
  <temp_ion> 60.22358037 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294243 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="270">
  <ekin>         5.24836531 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41839742 </eps>
  <enl>          4.76818305 </enl>
  <ecoul>      -15.59992865 </ecoul>
  <exc>         -4.37230697 </exc>
  <esr>          0.05752481 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37408468 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37408468 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71066963 0.00000000 -0.00000010 </position>
    <velocity> -0.00000947 -0.00000000 0.00000000 </velocity>
    <force> -0.00448341 -0.00000006 0.00000061 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.32984927 0.00000011 </position>
    <velocity> 0.00000000 0.00014871 -0.00000000 </velocity>
    <force> 0.00000008 -0.00657735 -0.00000050 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71066963 -0.00000000 -0.00000009 </position>
    <velocity> 0.00000947 0.00000000 0.00000000 </velocity>
    <force> 0.00448341 0.00000004 0.00000068 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.32984927 0.00000010 </position>
    <velocity> -0.00000000 -0.00014871 -0.00000000 </velocity>
    <force> -0.00000008 0.00657736 -0.00000085 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000272 </ekin_e>
  <ekin_ion> 0.00113679 </ekin_ion>
  <temp_ion> 59.83126872 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294245 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="271">
  <ekin>         5.24799694 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41818350 </eps>
  <enl>          4.76817331 </enl>
  <ecoul>      -15.59991155 </ecoul>
  <exc>         -4.37215234 </exc>
  <esr>          0.05747154 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37407714 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37407714 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71062965 0.00000000 -0.00000009 </position>
    <velocity> -0.00000982 -0.00000000 0.00000000 </velocity>
    <force> -0.00449985 -0.00000006 0.00000051 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33044100 0.00000010 </position>
    <velocity> 0.00000000 0.00014819 -0.00000000 </velocity>
    <force> 0.00000008 -0.00666367 -0.00000043 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71062965 -0.00000000 -0.00000009 </position>
    <velocity> 0.00000982 0.00000000 0.00000000 </velocity>
    <force> 0.00449986 0.00000004 0.00000058 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33044100 0.00000009 </position>
    <velocity> -0.00000000 -0.00014819 -0.00000000 </velocity>
    <force> -0.00000008 0.00666369 -0.00000070 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000270 </ekin_e>
  <ekin_ion> 0.00112927 </ekin_ion>
  <temp_ion> 59.43568610 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294248 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="272">
  <ekin>         5.24763079 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41797159 </eps>
  <enl>          4.76816430 </enl>
  <ecoul>      -15.59989448 </ecoul>
  <exc>         -4.37199858 </exc>
  <esr>          0.05741869 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37406955 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37406955 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71058825 0.00000000 -0.00000009 </position>
    <velocity> -0.00001017 -0.00000000 0.00000000 </velocity>
    <force> -0.00451579 -0.00000006 0.00000040 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33103062 0.00000010 </position>
    <velocity> 0.00000000 0.00014767 -0.00000000 </velocity>
    <force> 0.00000007 -0.00674936 -0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71058825 -0.00000000 -0.00000008 </position>
    <velocity> 0.00001017 0.00000000 0.00000000 </velocity>
    <force> 0.00451580 0.00000004 0.00000048 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33103062 0.00000008 </position>
    <velocity> -0.00000000 -0.00014767 -0.00000000 </velocity>
    <force> -0.00000007 0.00674938 -0.00000055 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000268 </ekin_e>
  <ekin_ion> 0.00112170 </ekin_ion>
  <temp_ion> 59.03693067 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294250 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="273">
  <ekin>         5.24726692 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41776187 </eps>
  <enl>          4.76815626 </enl>
  <ecoul>      -15.59987749 </ecoul>
  <exc>         -4.37184571 </exc>
  <esr>          0.05736624 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37406189 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37406189 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71054544 0.00000000 -0.00000008 </position>
    <velocity> -0.00001053 -0.00000000 0.00000000 </velocity>
    <force> -0.00453121 -0.00000005 0.00000028 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33161811 0.00000009 </position>
    <velocity> 0.00000000 0.00014714 -0.00000000 </velocity>
    <force> 0.00000006 -0.00683429 -0.00000028 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71054544 -0.00000000 -0.00000008 </position>
    <velocity> 0.00001053 0.00000000 0.00000000 </velocity>
    <force> 0.00453123 0.00000003 0.00000037 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33161811 0.00000008 </position>
    <velocity> -0.00000000 -0.00014714 -0.00000000 </velocity>
    <force> -0.00000007 0.00683431 -0.00000040 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000265 </ekin_e>
  <ekin_ion> 0.00111406 </ekin_ion>
  <temp_ion> 58.63510751 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294252 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="274">
  <ekin>         5.24690541 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41755442 </eps>
  <enl>          4.76814926 </enl>
  <ecoul>      -15.59986065 </ecoul>
  <exc>         -4.37169377 </exc>
  <esr>          0.05731421 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37405418 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37405418 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71050121 0.00000000 -0.00000008 </position>
    <velocity> -0.00001088 -0.00000000 0.00000000 </velocity>
    <force> -0.00454613 -0.00000005 0.00000017 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33220343 0.00000009 </position>
    <velocity> 0.00000000 0.00014660 -0.00000000 </velocity>
    <force> 0.00000006 -0.00691842 -0.00000020 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71050121 -0.00000000 -0.00000007 </position>
    <velocity> 0.00001088 0.00000000 0.00000000 </velocity>
    <force> 0.00454616 0.00000003 0.00000025 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33220343 0.00000007 </position>
    <velocity> -0.00000000 -0.00014660 -0.00000000 </velocity>
    <force> -0.00000006 0.00691843 -0.00000024 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000263 </ekin_e>
  <ekin_ion> 0.00110637 </ekin_ion>
  <temp_ion> 58.23032669 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294254 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="275">
  <ekin>         5.24654633 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41734921 </eps>
  <enl>          4.76814327 </enl>
  <ecoul>      -15.59984398 </ecoul>
  <exc>         -4.37154281 </exc>
  <esr>          0.05726260 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37404641 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37404641 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71045555 0.00000000 -0.00000007 </position>
    <velocity> -0.00001124 -0.00000000 0.00000000 </velocity>
    <force> -0.00456058 -0.00000004 0.00000006 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33278656 0.00000008 </position>
    <velocity> 0.00000000 0.00014606 -0.00000000 </velocity>
    <force> 0.00000005 -0.00700176 -0.00000012 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71045555 -0.00000000 -0.00000007 </position>
    <velocity> 0.00001124 0.00000000 0.00000000 </velocity>
    <force> 0.00456062 0.00000002 0.00000013 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33278656 0.00000007 </position>
    <velocity> -0.00000000 -0.00014606 -0.00000000 </velocity>
    <force> -0.00000006 0.00700177 -0.00000009 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000261 </ekin_e>
  <ekin_ion> 0.00109863 </ekin_ion>
  <temp_ion> 57.82269918 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294257 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="276">
  <ekin>         5.24618975 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41714616 </eps>
  <enl>          4.76813818 </enl>
  <ecoul>      -15.59982749 </ecoul>
  <exc>         -4.37139287 </exc>
  <esr>          0.05721140 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37403858 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37403858 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71040847 0.00000000 -0.00000007 </position>
    <velocity> -0.00001159 -0.00000000 0.00000000 </velocity>
    <force> -0.00457467 -0.00000004 -0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33336748 0.00000008 </position>
    <velocity> 0.00000000 0.00014551 -0.00000000 </velocity>
    <force> 0.00000004 -0.00708443 -0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71040847 -0.00000000 -0.00000006 </position>
    <velocity> 0.00001159 0.00000000 0.00000000 </velocity>
    <force> 0.00457472 0.00000002 0.00000001 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33336748 0.00000006 </position>
    <velocity> -0.00000000 -0.00014551 -0.00000000 </velocity>
    <force> -0.00000005 0.00708445 0.00000007 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000258 </ekin_e>
  <ekin_ion> 0.00109083 </ekin_ion>
  <temp_ion> 57.41233142 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294259 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="277">
  <ekin>         5.24583575 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41694515 </eps>
  <enl>          4.76813383 </enl>
  <ecoul>      -15.59981116 </ecoul>
  <exc>         -4.37124398 </exc>
  <esr>          0.05716062 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37403071 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37403071 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71035995 0.00000000 -0.00000006 </position>
    <velocity> -0.00001195 -0.00000000 0.00000000 </velocity>
    <force> -0.00458851 -0.00000003 -0.00000016 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33394616 0.00000008 </position>
    <velocity> 0.00000000 0.00014495 -0.00000000 </velocity>
    <force> 0.00000003 -0.00716665 0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71035995 -0.00000000 -0.00000006 </position>
    <velocity> 0.00001195 0.00000000 0.00000000 </velocity>
    <force> 0.00458857 0.00000001 -0.00000011 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33394616 0.00000005 </position>
    <velocity> -0.00000000 -0.00014495 -0.00000000 </velocity>
    <force> -0.00000004 0.00716666 0.00000023 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000255 </ekin_e>
  <ekin_ion> 0.00108298 </ekin_ion>
  <temp_ion> 56.99932020 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294262 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="278">
  <ekin>         5.24548441 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41674601 </eps>
  <enl>          4.76812998 </enl>
  <ecoul>      -15.59979497 </ecoul>
  <exc>         -4.37109618 </exc>
  <esr>          0.05711027 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37402279 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37402279 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71030999 0.00000000 -0.00000006 </position>
    <velocity> -0.00001231 -0.00000000 0.00000000 </velocity>
    <force> -0.00460225 -0.00000002 -0.00000026 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33452258 0.00000007 </position>
    <velocity> 0.00000000 0.00014439 -0.00000000 </velocity>
    <force> 0.00000001 -0.00724864 0.00000012 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71030999 -0.00000000 -0.00000006 </position>
    <velocity> 0.00001231 0.00000000 0.00000000 </velocity>
    <force> 0.00460230 0.00000001 -0.00000023 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33452258 0.00000005 </position>
    <velocity> -0.00000000 -0.00014439 -0.00000000 </velocity>
    <force> -0.00000003 0.00724865 0.00000039 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000253 </ekin_e>
  <ekin_ion> 0.00107509 </ekin_ion>
  <temp_ion> 56.58374967 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294265 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="279">
  <ekin>         5.24513582 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41654855 </eps>
  <enl>          4.76812632 </enl>
  <ecoul>      -15.59977890 </ecoul>
  <exc>         -4.37094951 </exc>
  <esr>          0.05706033 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37401481 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37401481 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71025859 0.00000000 -0.00000005 </position>
    <velocity> -0.00001267 -0.00000000 0.00000000 </velocity>
    <force> -0.00461599 -0.00000001 -0.00000036 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33509670 0.00000007 </position>
    <velocity> 0.00000000 0.00014382 -0.00000000 </velocity>
    <force> 0.00000000 -0.00733062 0.00000020 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71025859 -0.00000000 -0.00000005 </position>
    <velocity> 0.00001267 0.00000000 0.00000000 </velocity>
    <force> 0.00461605 0.00000000 -0.00000034 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33509670 0.00000004 </position>
    <velocity> -0.00000000 -0.00014382 -0.00000000 </velocity>
    <force> -0.00000002 0.00733063 0.00000054 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000250 </ekin_e>
  <ekin_ion> 0.00106714 </ekin_ion>
  <temp_ion> 56.16569160 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294268 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.011" max="    0.011"/>
<iteration count="280">
  <ekin>         5.24479011 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41635256 </eps>
  <enl>          4.76812251 </enl>
  <ecoul>      -15.59976289 </ecoul>
  <exc>         -4.37080397 </exc>
  <esr>          0.05701083 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37400680 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37400680 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71020574 0.00000000 -0.00000005 </position>
    <velocity> -0.00001303 -0.00000000 0.00000000 </velocity>
    <force> -0.00462983 -0.00000000 -0.00000046 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33566851 0.00000006 </position>
    <velocity> 0.00000000 0.00014324 -0.00000000 </velocity>
    <force> -0.00000001 -0.00741269 0.00000028 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71020574 -0.00000000 -0.00000005 </position>
    <velocity> 0.00001303 0.00000000 0.00000000 </velocity>
    <force> 0.00462990 -0.00000000 -0.00000045 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.33566851 0.00000004 </position>
    <velocity> -0.00000000 -0.00014324 -0.00000000 </velocity>
    <force> -0.00000002 0.00741270 0.00000069 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000247 </ekin_e>
  <ekin_ion> 0.00105916 </ekin_ion>
  <temp_ion> 55.74520913 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294270 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="281">
  <ekin>         5.24444737 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41615780 </eps>
  <enl>          4.76811817 </enl>
  <ecoul>      -15.59974690 </ecoul>
  <exc>         -4.37065957 </exc>
  <esr>          0.05696174 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37399873 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37399873 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71015144 0.00000000 -0.00000004 </position>
    <velocity> -0.00001339 -0.00000000 0.00000000 </velocity>
    <force> -0.00464377 0.00000000 -0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33623797 0.00000006 </position>
    <velocity> 0.00000000 0.00014266 -0.00000000 </velocity>
    <force> -0.00000002 -0.00749485 0.00000036 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71015144 -0.00000000 -0.00000004 </position>
    <velocity> 0.00001339 0.00000000 0.00000000 </velocity>
    <force> 0.00464384 -0.00000001 -0.00000056 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.33623797 0.00000003 </position>
    <velocity> -0.00000000 -0.00014266 -0.00000000 </velocity>
    <force> -0.00000001 0.00749486 0.00000083 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000244 </ekin_e>
  <ekin_ion> 0.00105112 </ekin_ion>
  <temp_ion> 55.32236307 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294273 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="282">
  <ekin>         5.24410768 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41596410 </eps>
  <enl>          4.76811298 </enl>
  <ecoul>      -15.59973090 </ecoul>
  <exc>         -4.37051629 </exc>
  <esr>          0.05691309 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37399063 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37399063 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71009568 0.00000000 -0.00000004 </position>
    <velocity> -0.00001376 -0.00000000 0.00000000 </velocity>
    <force> -0.00465775 0.00000001 -0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33680507 0.00000005 </position>
    <velocity> 0.00000000 0.00014207 -0.00000000 </velocity>
    <force> -0.00000003 -0.00757698 0.00000044 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71009568 -0.00000000 -0.00000004 </position>
    <velocity> 0.00001376 0.00000000 0.00000000 </velocity>
    <force> 0.00465782 -0.00000001 -0.00000066 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.33680507 0.00000003 </position>
    <velocity> -0.00000000 -0.00014207 -0.00000000 </velocity>
    <force> 0.00000000 0.00757698 0.00000097 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000241 </ekin_e>
  <ekin_ion> 0.00104304 </ekin_ion>
  <temp_ion> 54.89721908 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294276 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="283">
  <ekin>         5.24377106 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41577135 </eps>
  <enl>          4.76810675 </enl>
  <ecoul>      -15.59971484 </ecoul>
  <exc>         -4.37037411 </exc>
  <esr>          0.05686487 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37398248 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37398248 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.71003847 0.00000000 -0.00000004 </position>
    <velocity> -0.00001412 -0.00000000 0.00000000 </velocity>
    <force> -0.00467162 0.00000002 -0.00000075 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33736978 0.00000005 </position>
    <velocity> 0.00000000 0.00014148 -0.00000000 </velocity>
    <force> -0.00000004 -0.00765883 0.00000051 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.71003847 -0.00000000 -0.00000003 </position>
    <velocity> 0.00001412 0.00000000 0.00000000 </velocity>
    <force> 0.00467168 -0.00000002 -0.00000076 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.33736978 0.00000002 </position>
    <velocity> -0.00000000 -0.00014148 -0.00000000 </velocity>
    <force> 0.00000001 0.00765883 0.00000109 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000239 </ekin_e>
  <ekin_ion> 0.00103492 </ekin_ion>
  <temp_ion> 54.46985353 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294279 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="284">
  <ekin>         5.24343746 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41557955 </eps>
  <enl>          4.76809950 </enl>
  <ecoul>      -15.59969870 </ecoul>
  <exc>         -4.37023300 </exc>
  <esr>          0.05681708 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37397430 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37397430 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70997979 0.00000000 -0.00000003 </position>
    <velocity> -0.00001449 -0.00000000 0.00000000 </velocity>
    <force> -0.00468519 0.00000003 -0.00000084 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.33793206 0.00000005 </position>
    <velocity> 0.00000000 0.00014087 -0.00000000 </velocity>
    <force> -0.00000005 -0.00774017 0.00000059 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70997979 -0.00000000 -0.00000003 </position>
    <velocity> 0.00001449 0.00000000 0.00000000 </velocity>
    <force> 0.00468525 -0.00000002 -0.00000086 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.33793206 0.00000002 </position>
    <velocity> -0.00000000 -0.00014087 -0.00000000 </velocity>
    <force> 0.00000003 0.00774017 0.00000121 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000236 </ekin_e>
  <ekin_ion> 0.00102676 </ekin_ion>
  <temp_ion> 54.04035652 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294281 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="285">
  <ekin>         5.24310674 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41538888 </eps>
  <enl>          4.76809148 </enl>
  <ecoul>      -15.59968248 </ecoul>
  <exc>         -4.37009294 </exc>
  <esr>          0.05676972 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37396607 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37396607 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70991964 0.00000000 -0.00000003 </position>
    <velocity> -0.00001485 -0.00000000 0.00000000 </velocity>
    <force> -0.00469826 0.00000003 -0.00000093 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.33849190 0.00000004 </position>
    <velocity> 0.00000000 0.00014027 -0.00000000 </velocity>
    <force> -0.00000006 -0.00782076 0.00000067 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70991964 -0.00000000 -0.00000003 </position>
    <velocity> 0.00001485 0.00000000 0.00000000 </velocity>
    <force> 0.00469832 -0.00000003 -0.00000095 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.33849190 0.00000001 </position>
    <velocity> -0.00000000 -0.00014027 -0.00000000 </velocity>
    <force> 0.00000004 0.00782075 0.00000131 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000234 </ekin_e>
  <ekin_ion> 0.00101856 </ekin_ion>
  <temp_ion> 53.60883140 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294283 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="286">
  <ekin>         5.24277873 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41519961 </eps>
  <enl>          4.76808315 </enl>
  <ecoul>      -15.59966619 </ecoul>
  <exc>         -4.36995390 </exc>
  <esr>          0.05672279 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37395782 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37395782 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70985802 0.00000000 -0.00000003 </position>
    <velocity> -0.00001522 -0.00000000 0.00000000 </velocity>
    <force> -0.00471067 0.00000004 -0.00000101 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.33904927 0.00000004 </position>
    <velocity> 0.00000000 0.00013965 -0.00000000 </velocity>
    <force> -0.00000007 -0.00790045 0.00000074 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70985802 -0.00000000 -0.00000002 </position>
    <velocity> 0.00001522 0.00000000 0.00000000 </velocity>
    <force> 0.00471072 -0.00000003 -0.00000104 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.33904927 0.00000001 </position>
    <velocity> -0.00000000 -0.00013965 -0.00000000 </velocity>
    <force> 0.00000004 0.00790044 0.00000141 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000232 </ekin_e>
  <ekin_ion> 0.00101033 </ekin_ion>
  <temp_ion> 53.17539113 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294286 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="287">
  <ekin>         5.24245324 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41501208 </eps>
  <enl>          4.76807507 </enl>
  <ecoul>      -15.59964988 </ecoul>
  <exc>         -4.36981588 </exc>
  <esr>          0.05667631 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37394953 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37394953 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70979493 0.00000000 -0.00000002 </position>
    <velocity> -0.00001559 -0.00000000 0.00000000 </velocity>
    <force> -0.00472230 0.00000005 -0.00000108 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.33960415 0.00000004 </position>
    <velocity> 0.00000000 0.00013903 -0.00000000 </velocity>
    <force> -0.00000007 -0.00797920 0.00000082 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70979493 -0.00000000 -0.00000002 </position>
    <velocity> 0.00001559 0.00000000 0.00000000 </velocity>
    <force> 0.00472234 -0.00000003 -0.00000112 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.33960415 0.00000001 </position>
    <velocity> -0.00000000 -0.00013903 -0.00000000 </velocity>
    <force> 0.00000005 0.00797919 0.00000149 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000229 </ekin_e>
  <ekin_ion> 0.00100206 </ekin_ion>
  <temp_ion> 52.74015290 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294288 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="288">
  <ekin>         5.24213014 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41482667 </eps>
  <enl>          4.76806783 </enl>
  <ecoul>      -15.59963360 </ecoul>
  <exc>         -4.36967891 </exc>
  <esr>          0.05663026 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37394120 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37394120 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70973035 0.00000000 -0.00000002 </position>
    <velocity> -0.00001596 -0.00000000 0.00000000 </velocity>
    <force> -0.00473313 0.00000005 -0.00000115 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34015651 0.00000003 </position>
    <velocity> 0.00000000 0.00013840 -0.00000000 </velocity>
    <force> -0.00000008 -0.00805706 0.00000089 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70973035 -0.00000000 -0.00000002 </position>
    <velocity> 0.00001596 0.00000000 0.00000000 </velocity>
    <force> 0.00473317 -0.00000004 -0.00000119 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34015651 0.00000000 </position>
    <velocity> -0.00000000 -0.00013840 -0.00000000 </velocity>
    <force> 0.00000006 0.00805704 0.00000155 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000227 </ekin_e>
  <ekin_ion> 0.00099376 </ekin_ion>
  <temp_ion> 52.30323262 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294290 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="289">
  <ekin>         5.24180937 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41464368 </eps>
  <enl>          4.76806188 </enl>
  <ecoul>      -15.59961742 </ecoul>
  <exc>         -4.36954301 </exc>
  <esr>          0.05658465 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37393285 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37393285 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70966430 0.00000000 -0.00000002 </position>
    <velocity> -0.00001633 -0.00000000 0.00000000 </velocity>
    <force> -0.00474322 0.00000006 -0.00000120 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34070633 0.00000003 </position>
    <velocity> 0.00000000 0.00013777 -0.00000000 </velocity>
    <force> -0.00000008 -0.00813413 0.00000096 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70966430 -0.00000000 -0.00000002 </position>
    <velocity> 0.00001633 0.00000000 0.00000000 </velocity>
    <force> 0.00474324 -0.00000004 -0.00000126 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34070633 0.00000000 </position>
    <velocity> -0.00000000 -0.00013777 -0.00000000 </velocity>
    <force> 0.00000007 0.00813411 0.00000161 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000225 </ekin_e>
  <ekin_ion> 0.00098543 </ekin_ion>
  <temp_ion> 51.86474079 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294292 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="290">
  <ekin>         5.24149099 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41446331 </eps>
  <enl>          4.76805749 </enl>
  <ecoul>      -15.59960141 </ecoul>
  <exc>         -4.36940823 </exc>
  <esr>          0.05653948 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37392447 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37392447 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70959675 0.00000000 -0.00000002 </position>
    <velocity> -0.00001670 -0.00000000 0.00000000 </velocity>
    <force> -0.00475268 0.00000006 -0.00000124 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34125358 0.00000003 </position>
    <velocity> 0.00000000 0.00013713 -0.00000000 </velocity>
    <force> -0.00000008 -0.00821055 0.00000102 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70959675 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001670 0.00000000 0.00000000 </velocity>
    <force> 0.00475269 -0.00000004 -0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34125358 0.00000000 </position>
    <velocity> -0.00000000 -0.00013713 -0.00000000 </velocity>
    <force> 0.00000007 0.00821053 0.00000165 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000223 </ekin_e>
  <ekin_ion> 0.00097707 </ekin_ion>
  <temp_ion> 51.42478077 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294294 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="291">
  <ekin>         5.24117518 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41428563 </eps>
  <enl>          4.76805468 </enl>
  <ecoul>      -15.59958566 </ecoul>
  <exc>         -4.36927463 </exc>
  <esr>          0.05649476 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37391606 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37391606 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70952772 0.00000000 -0.00000002 </position>
    <velocity> -0.00001707 -0.00000000 0.00000000 </velocity>
    <force> -0.00476167 0.00000006 -0.00000127 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34179824 0.00000003 </position>
    <velocity> 0.00000000 0.00013649 -0.00000000 </velocity>
    <force> -0.00000008 -0.00828643 0.00000107 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70952772 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001707 0.00000000 0.00000000 </velocity>
    <force> 0.00476168 -0.00000004 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34179824 0.00000000 </position>
    <velocity> -0.00000000 -0.00013649 -0.00000000 </velocity>
    <force> 0.00000008 0.00828641 0.00000168 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000221 </ekin_e>
  <ekin_ion> 0.00096868 </ekin_ion>
  <temp_ion> 50.98344927 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294296 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="292">
  <ekin>         5.24086218 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41411060 </eps>
  <enl>          4.76805329 </enl>
  <ecoul>      -15.59957023 </ecoul>
  <exc>         -4.36914227 </exc>
  <esr>          0.05645048 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37390763 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37390763 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70945720 0.00000000 -0.00000002 </position>
    <velocity> -0.00001744 -0.00000000 0.00000000 </velocity>
    <force> -0.00477034 0.00000006 -0.00000129 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34234029 0.00000003 </position>
    <velocity> -0.00000000 0.00013584 -0.00000000 </velocity>
    <force> -0.00000008 -0.00836184 0.00000112 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70945720 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001744 0.00000000 0.00000000 </velocity>
    <force> 0.00477035 -0.00000004 -0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34234029 -0.00000000 </position>
    <velocity> -0.00000000 -0.00013584 -0.00000000 </velocity>
    <force> 0.00000008 0.00836182 0.00000169 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000219 </ekin_e>
  <ekin_ion> 0.00096027 </ekin_ion>
  <temp_ion> 50.54083861 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294298 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="293">
  <ekin>         5.24055229 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41393813 </eps>
  <enl>          4.76805302 </enl>
  <ecoul>      -15.59955516 </ecoul>
  <exc>         -4.36901120 </exc>
  <esr>          0.05640664 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37389918 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37389918 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70938519 0.00000000 -0.00000001 </position>
    <velocity> -0.00001782 0.00000000 0.00000000 </velocity>
    <force> -0.00477885 0.00000006 -0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34287970 0.00000003 </position>
    <velocity> -0.00000000 0.00013518 -0.00000000 </velocity>
    <force> -0.00000008 -0.00843680 0.00000117 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70938519 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001782 -0.00000000 0.00000000 </velocity>
    <force> 0.00477884 -0.00000004 -0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34287970 -0.00000000 </position>
    <velocity> -0.00000000 -0.00013518 -0.00000000 </velocity>
    <force> 0.00000008 0.00843678 0.00000169 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000216 </ekin_e>
  <ekin_ion> 0.00095184 </ekin_ion>
  <temp_ion> 50.09703965 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294301 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="294">
  <ekin>         5.24024578 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41376804 </eps>
  <enl>          4.76805351 </enl>
  <ecoul>      -15.59954049 </ecoul>
  <exc>         -4.36888146 </exc>
  <esr>          0.05636325 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37389070 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37389070 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70931168 0.00000000 -0.00000001 </position>
    <velocity> -0.00001819 0.00000000 0.00000000 </velocity>
    <force> -0.00478728 0.00000006 -0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34341646 0.00000003 </position>
    <velocity> -0.00000000 0.00013452 -0.00000000 </velocity>
    <force> -0.00000008 -0.00851127 0.00000120 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70931168 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001819 -0.00000000 0.00000000 </velocity>
    <force> 0.00478726 -0.00000004 -0.00000141 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34341646 0.00000000 </position>
    <velocity> -0.00000000 -0.00013452 0.00000000 </velocity>
    <force> 0.00000009 0.00851125 0.00000167 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000214 </ekin_e>
  <ekin_ion> 0.00094339 </ekin_ion>
  <temp_ion> 49.65214441 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294303 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="295">
  <ekin>         5.23994286 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41360019 </eps>
  <enl>          4.76805444 </enl>
  <ecoul>      -15.59952623 </ecoul>
  <exc>         -4.36875308 </exc>
  <esr>          0.05632031 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37388221 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37388221 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70923667 0.00000000 -0.00000002 </position>
    <velocity> -0.00001857 0.00000000 -0.00000000 </velocity>
    <force> -0.00479568 0.00000006 -0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34395053 0.00000003 </position>
    <velocity> -0.00000000 0.00013385 -0.00000000 </velocity>
    <force> -0.00000008 -0.00858520 0.00000123 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70923667 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001857 -0.00000000 -0.00000000 </velocity>
    <force> 0.00479565 -0.00000004 -0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34395053 0.00000000 </position>
    <velocity> 0.00000000 -0.00013385 0.00000000 </velocity>
    <force> 0.00000009 0.00858519 0.00000164 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000212 </ekin_e>
  <ekin_ion> 0.00093492 </ekin_ion>
  <temp_ion> 49.20624765 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294305 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="296">
  <ekin>         5.23964360 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41343443 </eps>
  <enl>          4.76805553 </enl>
  <ecoul>      -15.59951234 </ecoul>
  <exc>         -4.36862606 </exc>
  <esr>          0.05627782 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37387369 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37387369 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70916016 0.00000000 -0.00000002 </position>
    <velocity> -0.00001894 0.00000000 -0.00000000 </velocity>
    <force> -0.00480404 0.00000006 -0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34448189 0.00000003 </position>
    <velocity> -0.00000000 0.00013318 -0.00000000 </velocity>
    <force> -0.00000007 -0.00865855 0.00000125 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70916015 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001894 -0.00000000 -0.00000000 </velocity>
    <force> 0.00480401 -0.00000004 -0.00000139 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34448189 0.00000000 </position>
    <velocity> 0.00000000 -0.00013318 0.00000000 </velocity>
    <force> 0.00000008 0.00865854 0.00000160 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000210 </ekin_e>
  <ekin_ion> 0.00092643 </ekin_ion>
  <temp_ion> 48.75944710 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294307 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="297">
  <ekin>         5.23934800 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41327062 </eps>
  <enl>          4.76805662 </enl>
  <ecoul>      -15.59949878 </ecoul>
  <exc>         -4.36850039 </exc>
  <esr>          0.05623578 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37386517 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37386517 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70908214 0.00000000 -0.00000002 </position>
    <velocity> -0.00001932 0.00000000 -0.00000000 </velocity>
    <force> -0.00481233 0.00000006 -0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.34501052 0.00000003 </position>
    <velocity> -0.00000000 0.00013250 0.00000000 </velocity>
    <force> -0.00000007 -0.00873128 0.00000127 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70908214 -0.00000000 -0.00000001 </position>
    <velocity> 0.00001932 -0.00000000 -0.00000000 </velocity>
    <force> 0.00481229 -0.00000004 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34501052 0.00000001 </position>
    <velocity> 0.00000000 -0.00013250 0.00000000 </velocity>
    <force> 0.00000008 0.00873127 0.00000155 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000208 </ekin_e>
  <ekin_ion> 0.00091792 </ekin_ion>
  <temp_ion> 48.31184263 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294309 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="298">
  <ekin>         5.23905593 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41310863 </eps>
  <enl>          4.76805759 </enl>
  <ecoul>      -15.59948546 </ecoul>
  <exc>         -4.36837605 </exc>
  <esr>          0.05619419 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37385663 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37385663 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70900262 0.00000000 -0.00000002 </position>
    <velocity> -0.00001969 0.00000000 -0.00000000 </velocity>
    <force> -0.00482045 0.00000005 -0.00000129 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34553641 0.00000003 </position>
    <velocity> -0.00000000 0.00013181 0.00000000 </velocity>
    <force> -0.00000006 -0.00880338 0.00000128 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70900262 -0.00000000 -0.00000002 </position>
    <velocity> 0.00001969 -0.00000000 -0.00000000 </velocity>
    <force> 0.00482040 -0.00000003 -0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34553641 0.00000001 </position>
    <velocity> 0.00000000 -0.00013181 0.00000000 </velocity>
    <force> 0.00000008 0.00880337 0.00000148 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000205 </ekin_e>
  <ekin_ion> 0.00090940 </ekin_ion>
  <temp_ion> 47.86353465 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294312 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="299">
  <ekin>         5.23876717 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41294834 </eps>
  <enl>          4.76805839 </enl>
  <ecoul>      -15.59947229 </ecoul>
  <exc>         -4.36825300 </exc>
  <esr>          0.05615305 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37384807 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37384807 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70892159 0.00000000 -0.00000002 </position>
    <velocity> -0.00002007 0.00000000 -0.00000000 </velocity>
    <force> -0.00482833 0.00000005 -0.00000126 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34605952 0.00000003 </position>
    <velocity> -0.00000000 0.00013112 0.00000000 </velocity>
    <force> -0.00000005 -0.00887486 0.00000129 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70892159 -0.00000000 -0.00000002 </position>
    <velocity> 0.00002007 -0.00000000 -0.00000000 </velocity>
    <force> 0.00482827 -0.00000003 -0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34605952 0.00000001 </position>
    <velocity> 0.00000000 -0.00013112 0.00000000 </velocity>
    <force> 0.00000007 0.00887485 0.00000140 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000203 </ekin_e>
  <ekin_ion> 0.00090087 </ekin_ion>
  <temp_ion> 47.41462237 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294314 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="300">
  <ekin>         5.23848151 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41278962 </eps>
  <enl>          4.76805898 </enl>
  <ecoul>      -15.59945917 </ecoul>
  <exc>         -4.36813121 </exc>
  <esr>          0.05611237 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37383951 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37383951 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70883905 0.00000000 -0.00000002 </position>
    <velocity> -0.00002045 0.00000000 -0.00000000 </velocity>
    <force> -0.00483585 0.00000004 -0.00000123 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34657983 0.00000003 </position>
    <velocity> -0.00000000 0.00013043 0.00000000 </velocity>
    <force> -0.00000005 -0.00894576 0.00000128 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70883905 -0.00000000 -0.00000002 </position>
    <velocity> 0.00002045 -0.00000000 -0.00000000 </velocity>
    <force> 0.00483579 -0.00000003 -0.00000124 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34657983 0.00000001 </position>
    <velocity> 0.00000000 -0.00013043 0.00000000 </velocity>
    <force> 0.00000006 0.00894575 0.00000132 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000201 </ekin_e>
  <ekin_ion> 0.00089234 </ekin_ion>
  <temp_ion> 46.96520239 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294316 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="301">
  <ekin>         5.23819872 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41263237 </eps>
  <enl>          4.76805935 </enl>
  <ecoul>      -15.59944601 </ecoul>
  <exc>         -4.36801063 </exc>
  <esr>          0.05607214 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37383094 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37383094 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70875499 0.00000000 -0.00000003 </position>
    <velocity> -0.00002082 0.00000000 -0.00000000 </velocity>
    <force> -0.00484292 0.00000003 -0.00000119 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34709733 0.00000003 </position>
    <velocity> -0.00000000 0.00012973 0.00000000 </velocity>
    <force> -0.00000004 -0.00901613 0.00000127 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70875499 -0.00000000 -0.00000002 </position>
    <velocity> 0.00002082 -0.00000000 -0.00000000 </velocity>
    <force> 0.00484286 -0.00000002 -0.00000118 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34709733 0.00000002 </position>
    <velocity> 0.00000000 -0.00012973 0.00000000 </velocity>
    <force> 0.00000006 0.00901612 0.00000122 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000198 </ekin_e>
  <ekin_ion> 0.00088379 </ekin_ion>
  <temp_ion> 46.51536797 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294319 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="302">
  <ekin>         5.23791863 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41247654 </eps>
  <enl>          4.76805953 </enl>
  <ecoul>      -15.59943273 </ecoul>
  <exc>         -4.36789125 </exc>
  <esr>          0.05603237 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37382236 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37382236 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70866942 0.00000000 -0.00000003 </position>
    <velocity> -0.00002120 0.00000000 -0.00000000 </velocity>
    <force> -0.00484948 0.00000003 -0.00000114 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34761199 0.00000004 </position>
    <velocity> -0.00000000 0.00012902 0.00000000 </velocity>
    <force> -0.00000003 -0.00908599 0.00000125 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70866942 -0.00000000 -0.00000003 </position>
    <velocity> 0.00002120 -0.00000000 -0.00000000 </velocity>
    <force> 0.00484941 -0.00000002 -0.00000111 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34761199 0.00000002 </position>
    <velocity> 0.00000000 -0.00012902 0.00000000 </velocity>
    <force> 0.00000005 0.00908599 0.00000112 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000196 </ekin_e>
  <ekin_ion> 0.00087524 </ekin_ion>
  <temp_ion> 46.06520917 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294321 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="303">
  <ekin>         5.23764118 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41232214 </eps>
  <enl>          4.76805956 </enl>
  <ecoul>      -15.59941932 </ecoul>
  <exc>         -4.36777306 </exc>
  <esr>          0.05599306 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37381378 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37381378 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70858233 0.00000000 -0.00000003 </position>
    <velocity> -0.00002158 0.00000000 -0.00000000 </velocity>
    <force> -0.00485546 0.00000002 -0.00000108 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34812378 0.00000004 </position>
    <velocity> -0.00000000 0.00012831 0.00000000 </velocity>
    <force> -0.00000002 -0.00915537 0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70858233 -0.00000000 -0.00000003 </position>
    <velocity> 0.00002158 -0.00000000 -0.00000000 </velocity>
    <force> 0.00485540 -0.00000002 -0.00000104 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34812378 0.00000003 </position>
    <velocity> 0.00000000 -0.00012831 0.00000000 </velocity>
    <force> 0.00000004 0.00915536 0.00000101 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000193 </ekin_e>
  <ekin_ion> 0.00086668 </ekin_ion>
  <temp_ion> 45.61481370 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294324 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="304">
  <ekin>         5.23736638 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41216926 </eps>
  <enl>          4.76805956 </enl>
  <ecoul>      -15.59940580 </ecoul>
  <exc>         -4.36765607 </exc>
  <esr>          0.05595421 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37380520 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37380520 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70849373 0.00000000 -0.00000004 </position>
    <velocity> -0.00002196 0.00000000 -0.00000000 </velocity>
    <force> -0.00486086 0.00000001 -0.00000101 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34863269 0.00000004 </position>
    <velocity> -0.00000000 0.00012759 0.00000000 </velocity>
    <force> -0.00000001 -0.00922425 0.00000118 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70849372 -0.00000000 -0.00000003 </position>
    <velocity> 0.00002196 -0.00000000 -0.00000000 </velocity>
    <force> 0.00486080 -0.00000001 -0.00000096 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34863269 0.00000003 </position>
    <velocity> 0.00000000 -0.00012759 0.00000000 </velocity>
    <force> 0.00000003 0.00922425 0.00000089 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000191 </ekin_e>
  <ekin_ion> 0.00085812 </ekin_ion>
  <temp_ion> 45.16426820 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294326 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="305">
  <ekin>         5.23709432 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41201807 </eps>
  <enl>          4.76805967 </enl>
  <ecoul>      -15.59939223 </ecoul>
  <exc>         -4.36754030 </exc>
  <esr>          0.05591582 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37379661 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37379661 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70840360 0.00000000 -0.00000004 </position>
    <velocity> -0.00002234 0.00000000 -0.00000000 </velocity>
    <force> -0.00486567 0.00000000 -0.00000094 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34913870 0.00000005 </position>
    <velocity> -0.00000000 0.00012687 0.00000000 </velocity>
    <force> 0.00000000 -0.00929261 0.00000113 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70840360 -0.00000000 -0.00000004 </position>
    <velocity> 0.00002234 -0.00000000 -0.00000000 </velocity>
    <force> 0.00486561 -0.00000001 -0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.34913870 0.00000004 </position>
    <velocity> 0.00000000 -0.00012687 0.00000000 </velocity>
    <force> 0.00000002 0.00929261 0.00000077 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000188 </ekin_e>
  <ekin_ion> 0.00084956 </ekin_ion>
  <temp_ion> 44.71365964 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294329 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="306">
  <ekin>         5.23682517 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41186877 </eps>
  <enl>          4.76806009 </enl>
  <ecoul>      -15.59937872 </ecoul>
  <exc>         -4.36742579 </exc>
  <esr>          0.05587788 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37378802 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37378802 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70831195 0.00000000 -0.00000005 </position>
    <velocity> -0.00002272 0.00000000 -0.00000000 </velocity>
    <force> -0.00486995 -0.00000000 -0.00000085 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.34964179 0.00000005 </position>
    <velocity> -0.00000000 0.00012614 0.00000000 </velocity>
    <force> 0.00000001 -0.00936042 0.00000106 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70831195 -0.00000000 -0.00000004 </position>
    <velocity> 0.00002272 -0.00000000 -0.00000000 </velocity>
    <force> 0.00486989 -0.00000000 -0.00000077 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.34964179 0.00000004 </position>
    <velocity> 0.00000000 -0.00012614 0.00000000 </velocity>
    <force> 0.00000001 0.00936043 0.00000065 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000186 </ekin_e>
  <ekin_ion> 0.00084100 </ekin_ion>
  <temp_ion> 44.26307622 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294331 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="307">
  <ekin>         5.23655914 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41172161 </eps>
  <enl>          4.76806099 </enl>
  <ecoul>      -15.59936537 </ecoul>
  <exc>         -4.36731259 </exc>
  <esr>          0.05584042 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37377944 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37377944 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70821877 0.00000000 -0.00000005 </position>
    <velocity> -0.00002310 0.00000000 -0.00000000 </velocity>
    <force> -0.00487375 -0.00000001 -0.00000076 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35014192 0.00000005 </position>
    <velocity> -0.00000000 0.00012540 0.00000000 </velocity>
    <force> 0.00000002 -0.00942766 0.00000099 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70821877 -0.00000000 -0.00000005 </position>
    <velocity> 0.00002310 -0.00000000 -0.00000000 </velocity>
    <force> 0.00487370 0.00000000 -0.00000067 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35014192 0.00000005 </position>
    <velocity> 0.00000000 -0.00012540 0.00000000 </velocity>
    <force> -0.00000000 0.00942767 0.00000052 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000183 </ekin_e>
  <ekin_ion> 0.00083244 </ekin_ion>
  <temp_ion> 43.81260750 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294334 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="308">
  <ekin>         5.23629643 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41157678 </eps>
  <enl>          4.76806253 </enl>
  <ecoul>      -15.59935231 </ecoul>
  <exc>         -4.36720072 </exc>
  <esr>          0.05580341 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37377086 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37377086 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70812408 0.00000000 -0.00000005 </position>
    <velocity> -0.00002348 0.00000000 -0.00000000 </velocity>
    <force> -0.00487715 -0.00000002 -0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35063909 0.00000006 </position>
    <velocity> -0.00000000 0.00012466 0.00000000 </velocity>
    <force> 0.00000003 -0.00949433 0.00000091 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70812408 -0.00000000 -0.00000005 </position>
    <velocity> 0.00002348 -0.00000000 -0.00000000 </velocity>
    <force> 0.00487711 0.00000001 -0.00000057 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35063909 0.00000005 </position>
    <velocity> 0.00000000 -0.00012466 0.00000000 </velocity>
    <force> -0.00000001 0.00949434 0.00000038 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000181 </ekin_e>
  <ekin_ion> 0.00082388 </ekin_ion>
  <temp_ion> 43.36234372 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294336 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="309">
  <ekin>         5.23603721 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41143442 </eps>
  <enl>          4.76806476 </enl>
  <ecoul>      -15.59933962 </ecoul>
  <exc>         -4.36709022 </exc>
  <esr>          0.05576687 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37376228 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37376228 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70802786 0.00000000 -0.00000006 </position>
    <velocity> -0.00002386 0.00000000 -0.00000000 </velocity>
    <force> -0.00488026 -0.00000003 -0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35113328 0.00000006 </position>
    <velocity> -0.00000000 0.00012392 0.00000000 </velocity>
    <force> 0.00000004 -0.00956047 0.00000083 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70802785 -0.00000000 -0.00000006 </position>
    <velocity> 0.00002386 -0.00000000 -0.00000000 </velocity>
    <force> 0.00488022 0.00000001 -0.00000046 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35113328 0.00000006 </position>
    <velocity> 0.00000000 -0.00012392 0.00000000 </velocity>
    <force> -0.00000002 0.00956048 0.00000025 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000178 </ekin_e>
  <ekin_ion> 0.00081533 </ekin_ion>
  <temp_ion> 42.91237434 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294339 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="310">
  <ekin>         5.23578158 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41129452 </eps>
  <enl>          4.76806766 </enl>
  <ecoul>      -15.59932734 </ecoul>
  <exc>         -4.36698109 </exc>
  <esr>          0.05573079 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37375372 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37375372 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70793011 0.00000000 -0.00000006 </position>
    <velocity> -0.00002425 0.00000000 -0.00000000 </velocity>
    <force> -0.00488316 -0.00000003 -0.00000045 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35162445 0.00000007 </position>
    <velocity> -0.00000000 0.00012317 0.00000000 </velocity>
    <force> 0.00000005 -0.00962615 0.00000073 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70793011 -0.00000000 -0.00000006 </position>
    <velocity> 0.00002425 -0.00000000 -0.00000000 </velocity>
    <force> 0.00488313 0.00000002 -0.00000035 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35162445 0.00000006 </position>
    <velocity> 0.00000000 -0.00012317 0.00000000 </velocity>
    <force> -0.00000003 0.00962616 0.00000012 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000176 </ekin_e>
  <ekin_ion> 0.00080679 </ekin_ion>
  <temp_ion> 42.46278657 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294341 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="311">
  <ekin>         5.23552955 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41115701 </eps>
  <enl>          4.76807106 </enl>
  <ecoul>      -15.59931546 </ecoul>
  <exc>         -4.36687330 </exc>
  <esr>          0.05569518 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37374516 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37374516 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70783083 0.00000000 -0.00000007 </position>
    <velocity> -0.00002463 0.00000000 -0.00000000 </velocity>
    <force> -0.00488594 -0.00000004 -0.00000034 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35211259 0.00000007 </position>
    <velocity> -0.00000000 0.00012241 0.00000000 </velocity>
    <force> 0.00000006 -0.00969145 0.00000063 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70783083 -0.00000000 -0.00000007 </position>
    <velocity> 0.00002463 -0.00000000 -0.00000000 </velocity>
    <force> 0.00488592 0.00000002 -0.00000024 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35211259 0.00000007 </position>
    <velocity> 0.00000000 -0.00012241 0.00000000 </velocity>
    <force> -0.00000004 0.00969146 -0.00000001 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000173 </ekin_e>
  <ekin_ion> 0.00079826 </ekin_ion>
  <temp_ion> 42.01366431 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294344 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="312">
  <ekin>         5.23528104 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41102168 </eps>
  <enl>          4.76807474 </enl>
  <ecoul>      -15.59930388 </ecoul>
  <exc>         -4.36676683 </exc>
  <esr>          0.05566004 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37373661 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37373661 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70773003 0.00000000 -0.00000008 </position>
    <velocity> -0.00002501 0.00000000 -0.00000000 </velocity>
    <force> -0.00488865 -0.00000005 -0.00000023 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35259769 0.00000008 </position>
    <velocity> -0.00000000 0.00012166 0.00000000 </velocity>
    <force> 0.00000006 -0.00975643 0.00000052 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70773003 -0.00000000 -0.00000007 </position>
    <velocity> 0.00002501 -0.00000000 -0.00000000 </velocity>
    <force> 0.00488864 0.00000003 -0.00000013 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35259769 0.00000008 </position>
    <velocity> 0.00000000 -0.00012166 0.00000000 </velocity>
    <force> -0.00000005 0.00975644 -0.00000014 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000171 </ekin_e>
  <ekin_ion> 0.00078973 </ekin_ion>
  <temp_ion> 41.56508818 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294346 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="313">
  <ekin>         5.23503586 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41088824 </eps>
  <enl>          4.76807840 </enl>
  <ecoul>      -15.59929250 </ecoul>
  <exc>         -4.36666160 </exc>
  <esr>          0.05562537 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37372808 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37372808 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70762770 0.00000000 -0.00000008 </position>
    <velocity> -0.00002539 0.00000000 -0.00000000 </velocity>
    <force> -0.00489133 -0.00000005 -0.00000011 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35307972 0.00000008 </position>
    <velocity> -0.00000000 0.00012089 0.00000000 </velocity>
    <force> 0.00000007 -0.00982112 0.00000041 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70762770 -0.00000000 -0.00000008 </position>
    <velocity> 0.00002539 -0.00000000 -0.00000000 </velocity>
    <force> 0.00489132 0.00000003 -0.00000002 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35307972 0.00000008 </position>
    <velocity> 0.00000000 -0.00012089 0.00000000 </velocity>
    <force> -0.00000006 0.00982114 -0.00000027 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000168 </ekin_e>
  <ekin_ion> 0.00078122 </ekin_ion>
  <temp_ion> 41.11713686 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294348 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="314">
  <ekin>         5.23479376 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41075639 </eps>
  <enl>          4.76808176 </enl>
  <ecoul>      -15.59928114 </ecoul>
  <exc>         -4.36655754 </exc>
  <esr>          0.05559116 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37371955 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37371955 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70752383 0.00000000 -0.00000009 </position>
    <velocity> -0.00002577 0.00000000 -0.00000000 </velocity>
    <force> -0.00489394 -0.00000006 -0.00000000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35355865 0.00000009 </position>
    <velocity> -0.00000000 0.00012012 0.00000000 </velocity>
    <force> 0.00000007 -0.00988548 0.00000029 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70752383 -0.00000000 -0.00000008 </position>
    <velocity> 0.00002577 -0.00000000 -0.00000000 </velocity>
    <force> 0.00489394 0.00000004 0.00000010 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35355865 0.00000009 </position>
    <velocity> 0.00000000 -0.00012012 0.00000000 </velocity>
    <force> -0.00000007 0.00988550 -0.00000039 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000166 </ekin_e>
  <ekin_ion> 0.00077273 </ekin_ion>
  <temp_ion> 40.66988950 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294351 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="315">
  <ekin>         5.23455447 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41062586 </eps>
  <enl>          4.76808458 </enl>
  <ecoul>      -15.59926966 </ecoul>
  <exc>         -4.36645458 </exc>
  <esr>          0.05555743 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37371105 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37371105 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70741844 0.00000000 -0.00000009 </position>
    <velocity> -0.00002616 0.00000000 -0.00000000 </velocity>
    <force> -0.00489644 -0.00000006 0.00000011 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35403448 0.00000010 </position>
    <velocity> -0.00000000 0.00011935 0.00000000 </velocity>
    <force> 0.00000008 -0.00994940 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70741844 -0.00000000 -0.00000009 </position>
    <velocity> 0.00002616 -0.00000000 -0.00000000 </velocity>
    <force> 0.00489645 0.00000004 0.00000021 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35403448 0.00000009 </position>
    <velocity> 0.00000000 -0.00011935 0.00000000 </velocity>
    <force> -0.00000008 0.00994942 -0.00000050 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000164 </ekin_e>
  <ekin_ion> 0.00076424 </ekin_ion>
  <temp_ion> 40.22342853 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294353 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.012" max="    0.012"/>
<iteration count="316">
  <ekin>         5.23431772 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41049645 </eps>
  <enl>          4.76808677 </enl>
  <ecoul>      -15.59925792 </ecoul>
  <exc>         -4.36635268 </exc>
  <esr>          0.05552416 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37370256 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37370256 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70731152 0.00000000 -0.00000010 </position>
    <velocity> -0.00002654 0.00000000 -0.00000000 </velocity>
    <force> -0.00489871 -0.00000006 0.00000022 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35450718 0.00000010 </position>
    <velocity> -0.00000000 0.00011857 0.00000000 </velocity>
    <force> 0.00000008 -0.01001272 0.00000004 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70731152 -0.00000000 -0.00000009 </position>
    <velocity> 0.00002654 -0.00000000 -0.00000000 </velocity>
    <force> 0.00489873 0.00000004 0.00000032 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35450718 0.00000010 </position>
    <velocity> 0.00000000 -0.00011857 0.00000000 </velocity>
    <force> -0.00000008 0.01001273 -0.00000061 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000162 </ekin_e>
  <ekin_ion> 0.00075578 </ekin_ion>
  <temp_ion> 39.77784206 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294355 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="317">
  <ekin>         5.23408332 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41036811 </eps>
  <enl>          4.76808833 </enl>
  <ecoul>      -15.59924583 </ecoul>
  <exc>         -4.36625179 </exc>
  <esr>          0.05549137 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37369409 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37369409 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70720307 0.00000000 -0.00000010 </position>
    <velocity> -0.00002692 0.00000000 -0.00000000 </velocity>
    <force> -0.00490064 -0.00000006 0.00000033 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35497673 0.00000011 </position>
    <velocity> -0.00000000 0.00011778 0.00000000 </velocity>
    <force> 0.00000008 -0.01007526 -0.00000009 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70720307 -0.00000000 -0.00000010 </position>
    <velocity> 0.00002692 -0.00000000 -0.00000000 </velocity>
    <force> 0.00490067 0.00000004 0.00000042 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35497673 0.00000010 </position>
    <velocity> 0.00000000 -0.00011778 0.00000000 </velocity>
    <force> -0.00000009 0.01007528 -0.00000071 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000160 </ekin_e>
  <ekin_ion> 0.00074733 </ekin_ion>
  <temp_ion> 39.33322486 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294357 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="318">
  <ekin>         5.23385119 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41024093 </eps>
  <enl>          4.76808943 </enl>
  <ecoul>      -15.59923340 </ecoul>
  <exc>         -4.36615193 </exc>
  <esr>          0.05545905 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37368564 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37368564 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70709308 0.00000000 -0.00000011 </position>
    <velocity> -0.00002731 -0.00000000 -0.00000000 </velocity>
    <force> -0.00490209 -0.00000006 0.00000043 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35544311 0.00000011 </position>
    <velocity> 0.00000000 0.00011699 0.00000000 </velocity>
    <force> 0.00000008 -0.01013687 -0.00000023 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70709308 -0.00000000 -0.00000010 </position>
    <velocity> 0.00002730 -0.00000000 -0.00000000 </velocity>
    <force> 0.00490212 0.00000004 0.00000053 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35544311 0.00000011 </position>
    <velocity> 0.00000000 -0.00011699 0.00000000 </velocity>
    <force> -0.00000009 0.01013689 -0.00000080 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000158 </ekin_e>
  <ekin_ion> 0.00073890 </ekin_ion>
  <temp_ion> 38.88967761 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294359 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="319">
  <ekin>         5.23362140 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41011512 </eps>
  <enl>          4.76809036 </enl>
  <ecoul>      -15.59922071 </ecoul>
  <exc>         -4.36605314 </exc>
  <esr>          0.05542720 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37367722 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37367722 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70698156 0.00000000 -0.00000011 </position>
    <velocity> -0.00002769 -0.00000000 -0.00000000 </velocity>
    <force> -0.00490295 -0.00000006 0.00000054 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35590631 0.00000012 </position>
    <velocity> 0.00000000 0.00011620 0.00000000 </velocity>
    <force> 0.00000008 -0.01019747 -0.00000036 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70698156 -0.00000000 -0.00000011 </position>
    <velocity> 0.00002769 -0.00000000 -0.00000000 </velocity>
    <force> 0.00490299 0.00000004 0.00000063 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35590631 0.00000011 </position>
    <velocity> 0.00000000 -0.00011620 0.00000000 </velocity>
    <force> -0.00000009 0.01019748 -0.00000088 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000155 </ekin_e>
  <ekin_ion> 0.00073050 </ekin_ion>
  <temp_ion> 38.44730439 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294361 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="320">
  <ekin>         5.23339417 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40999106 </eps>
  <enl>          4.76809148 </enl>
  <ecoul>      -15.59920792 </ecoul>
  <exc>         -4.36595550 </exc>
  <esr>          0.05539583 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37366882 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37366882 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70686851 0.00000000 -0.00000012 </position>
    <velocity> -0.00002807 -0.00000000 -0.00000000 </velocity>
    <force> -0.00490316 -0.00000006 0.00000064 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35636630 0.00000012 </position>
    <velocity> 0.00000000 0.00011540 0.00000000 </velocity>
    <force> 0.00000008 -0.01025705 -0.00000049 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70686851 -0.00000000 -0.00000011 </position>
    <velocity> 0.00002807 0.00000000 -0.00000000 </velocity>
    <force> 0.00490320 0.00000004 0.00000072 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35636630 0.00000012 </position>
    <velocity> -0.00000000 -0.00011540 0.00000000 </velocity>
    <force> -0.00000009 0.01025706 -0.00000096 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000153 </ekin_e>
  <ekin_ion> 0.00072212 </ekin_ion>
  <temp_ion> 38.00620910 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294363 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="321">
  <ekin>         5.23316984 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40986913 </eps>
  <enl>          4.76809318 </enl>
  <ecoul>      -15.59919522 </ecoul>
  <exc>         -4.36585912 </exc>
  <esr>          0.05536494 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37366044 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37366044 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70675393 0.00000000 -0.00000012 </position>
    <velocity> -0.00002845 -0.00000000 -0.00000000 </velocity>
    <force> -0.00490269 -0.00000006 0.00000075 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35682306 0.00000013 </position>
    <velocity> 0.00000000 0.00011459 0.00000000 </velocity>
    <force> 0.00000007 -0.01031570 -0.00000062 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70675393 -0.00000000 -0.00000012 </position>
    <velocity> 0.00002845 0.00000000 -0.00000000 </velocity>
    <force> 0.00490274 0.00000004 0.00000081 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35682306 0.00000012 </position>
    <velocity> -0.00000000 -0.00011459 0.00000000 </velocity>
    <force> -0.00000009 0.01031571 -0.00000102 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000151 </ekin_e>
  <ekin_ion> 0.00071376 </ekin_ion>
  <temp_ion> 37.56649159 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294365 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="322">
  <ekin>         5.23294885 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40974976 </eps>
  <enl>          4.76809579 </enl>
  <ecoul>      -15.59918286 </ecoul>
  <exc>         -4.36576412 </exc>
  <esr>          0.05533452 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37365209 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37365209 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70663781 0.00000000 -0.00000012 </position>
    <velocity> -0.00002884 -0.00000000 -0.00000000 </velocity>
    <force> -0.00490158 -0.00000005 0.00000085 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35727659 0.00000013 </position>
    <velocity> 0.00000000 0.00011379 0.00000000 </velocity>
    <force> 0.00000007 -0.01037358 -0.00000075 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70663782 -0.00000000 -0.00000012 </position>
    <velocity> 0.00002884 0.00000000 -0.00000000 </velocity>
    <force> 0.00490163 0.00000004 0.00000089 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35727659 0.00000012 </position>
    <velocity> -0.00000000 -0.00011379 0.00000000 </velocity>
    <force> -0.00000009 0.01037358 -0.00000108 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000149 </ekin_e>
  <ekin_ion> 0.00070543 </ekin_ion>
  <temp_ion> 37.12824477 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294368 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="323">
  <ekin>         5.23273162 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40963328 </eps>
  <enl>          4.76809955 </enl>
  <ecoul>      -15.59917104 </ecoul>
  <exc>         -4.36567062 </exc>
  <esr>          0.05530457 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37364377 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37364377 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70652017 0.00000000 -0.00000013 </position>
    <velocity> -0.00002922 -0.00000000 -0.00000000 </velocity>
    <force> -0.00489990 -0.00000005 0.00000095 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35772685 0.00000014 </position>
    <velocity> 0.00000000 0.00011297 0.00000000 </velocity>
    <force> 0.00000006 -0.01043085 -0.00000087 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70652017 -0.00000000 -0.00000012 </position>
    <velocity> 0.00002922 0.00000000 -0.00000000 </velocity>
    <force> 0.00489996 0.00000004 0.00000097 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35772685 0.00000013 </position>
    <velocity> -0.00000000 -0.00011297 0.00000000 </velocity>
    <force> -0.00000008 0.01043086 -0.00000113 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000147 </ekin_e>
  <ekin_ion> 0.00069714 </ekin_ion>
  <temp_ion> 36.69155306 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294370 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="324">
  <ekin>         5.23251852 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40951992 </eps>
  <enl>          4.76810459 </enl>
  <ecoul>      -15.59915995 </ecoul>
  <exc>         -4.36557872 </exc>
  <esr>          0.05527511 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37363548 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37363548 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70640099 0.00000000 -0.00000013 </position>
    <velocity> -0.00002960 -0.00000000 -0.00000000 </velocity>
    <force> -0.00489778 -0.00000004 0.00000104 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35817384 0.00000014 </position>
    <velocity> 0.00000000 0.00011216 0.00000000 </velocity>
    <force> 0.00000006 -0.01048771 -0.00000100 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70640099 -0.00000000 -0.00000013 </position>
    <velocity> 0.00002960 0.00000000 -0.00000000 </velocity>
    <force> 0.00489784 0.00000004 0.00000103 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35817384 0.00000013 </position>
    <velocity> -0.00000000 -0.00011216 0.00000000 </velocity>
    <force> -0.00000008 0.01048771 -0.00000117 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000144 </ekin_e>
  <ekin_ion> 0.00068887 </ekin_ion>
  <temp_ion> 36.25649264 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294372 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="325">
  <ekin>         5.23230977 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40940973 </eps>
  <enl>          4.76811087 </enl>
  <ecoul>      -15.59914965 </ecoul>
  <exc>         -4.36548849 </exc>
  <esr>          0.05524612 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37362722 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37362722 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70628029 0.00000000 -0.00000013 </position>
    <velocity> -0.00002999 -0.00000000 -0.00000000 </velocity>
    <force> -0.00489531 -0.00000004 0.00000112 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35861753 0.00000015 </position>
    <velocity> 0.00000000 0.00011133 0.00000000 </velocity>
    <force> 0.00000005 -0.01054427 -0.00000111 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70628029 -0.00000000 -0.00000013 </position>
    <velocity> 0.00002999 0.00000000 -0.00000000 </velocity>
    <force> 0.00489537 0.00000004 0.00000109 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35861753 0.00000013 </position>
    <velocity> -0.00000000 -0.00011133 0.00000000 </velocity>
    <force> -0.00000007 0.01054427 -0.00000121 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000142 </ekin_e>
  <ekin_ion> 0.00068064 </ekin_ion>
  <temp_ion> 35.82313314 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294375 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="326">
  <ekin>         5.23210543 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40930262 </eps>
  <enl>          4.76811825 </enl>
  <ecoul>      -15.59914014 </ecoul>
  <exc>         -4.36539992 </exc>
  <esr>          0.05521761 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37361900 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37361900 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70615805 0.00000000 -0.00000014 </position>
    <velocity> -0.00003037 -0.00000000 -0.00000000 </velocity>
    <force> -0.00489259 -0.00000003 0.00000120 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35905791 0.00000015 </position>
    <velocity> 0.00000000 0.00011051 0.00000000 </velocity>
    <force> 0.00000004 -0.01060063 -0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70615805 -0.00000000 -0.00000013 </position>
    <velocity> 0.00003037 0.00000000 -0.00000000 </velocity>
    <force> 0.00489265 0.00000003 0.00000114 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35905791 0.00000013 </position>
    <velocity> -0.00000000 -0.00011051 0.00000000 </velocity>
    <force> -0.00000006 0.01060062 -0.00000123 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000139 </ekin_e>
  <ekin_ion> 0.00067244 </ekin_ion>
  <temp_ion> 35.39154008 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294377 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="327">
  <ekin>         5.23190537 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40919833 </eps>
  <enl>          4.76812646 </enl>
  <ecoul>      -15.59913131 </ecoul>
  <exc>         -4.36531300 </exc>
  <esr>          0.05518958 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37361081 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37361081 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70603429 0.00000000 -0.00000014 </position>
    <velocity> -0.00003075 -0.00000000 -0.00000000 </velocity>
    <force> -0.00488968 -0.00000002 0.00000126 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35949495 0.00000015 </position>
    <velocity> 0.00000000 0.00010968 0.00000000 </velocity>
    <force> 0.00000003 -0.01065679 -0.00000132 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70603429 -0.00000000 -0.00000013 </position>
    <velocity> 0.00003075 0.00000000 -0.00000000 </velocity>
    <force> 0.00488973 0.00000003 0.00000118 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35949495 0.00000013 </position>
    <velocity> -0.00000000 -0.00010968 0.00000000 </velocity>
    <force> -0.00000005 0.01065679 -0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000137 </ekin_e>
  <ekin_ion> 0.00066427 </ekin_ion>
  <temp_ion> 34.96177751 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294380 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="328">
  <ekin>         5.23170929 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40909652 </eps>
  <enl>          4.76813521 </enl>
  <ecoul>      -15.59912298 </ecoul>
  <exc>         -4.36522765 </exc>
  <esr>          0.05516203 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37360266 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37360266 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70590900 0.00000000 -0.00000014 </position>
    <velocity> -0.00003113 -0.00000000 -0.00000000 </velocity>
    <force> -0.00488659 -0.00000002 0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.35992865 0.00000016 </position>
    <velocity> 0.00000000 0.00010884 0.00000000 </velocity>
    <force> 0.00000002 -0.01071273 -0.00000141 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70590900 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003113 0.00000000 -0.00000000 </velocity>
    <force> 0.00488664 0.00000003 0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.35992865 0.00000013 </position>
    <velocity> -0.00000000 -0.00010884 0.00000000 </velocity>
    <force> -0.00000004 0.01071272 -0.00000126 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000135 </ekin_e>
  <ekin_ion> 0.00065614 </ekin_ion>
  <temp_ion> 34.53391012 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294382 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="329">
  <ekin>         5.23151678 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40899680 </eps>
  <enl>          4.76814417 </enl>
  <ecoul>      -15.59911492 </ecoul>
  <exc>         -4.36514376 </exc>
  <esr>          0.05513496 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37359454 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37359454 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70578218 0.00000000 -0.00000014 </position>
    <velocity> -0.00003151 -0.00000000 -0.00000000 </velocity>
    <force> -0.00488330 -0.00000001 0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36035899 0.00000016 </position>
    <velocity> 0.00000000 0.00010800 0.00000000 </velocity>
    <force> 0.00000001 -0.01076838 -0.00000149 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70578218 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003151 0.00000000 -0.00000000 </velocity>
    <force> 0.00488334 0.00000002 0.00000124 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.36035899 0.00000014 </position>
    <velocity> -0.00000000 -0.00010800 0.00000000 </velocity>
    <force> -0.00000003 0.01076837 -0.00000126 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000132 </ekin_e>
  <ekin_ion> 0.00064805 </ekin_ion>
  <temp_ion> 34.10800475 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294384 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="330">
  <ekin>         5.23132741 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40889880 </eps>
  <enl>          4.76815307 </enl>
  <ecoul>      -15.59910690 </ecoul>
  <exc>         -4.36506124 </exc>
  <esr>          0.05510837 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37358646 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37358646 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70565384 0.00000000 -0.00000014 </position>
    <velocity> -0.00003189 -0.00000000 -0.00000000 </velocity>
    <force> -0.00487975 -0.00000000 0.00000140 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36078594 0.00000016 </position>
    <velocity> 0.00000000 0.00010716 0.00000000 </velocity>
    <force> 0.00000000 -0.01082364 -0.00000156 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70565384 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003189 0.00000000 -0.00000000 </velocity>
    <force> 0.00487979 0.00000002 0.00000126 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.36078594 0.00000014 </position>
    <velocity> -0.00000000 -0.00010716 0.00000000 </velocity>
    <force> -0.00000002 0.01082363 -0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000130 </ekin_e>
  <ekin_ion> 0.00064000 </ekin_ion>
  <temp_ion> 33.68413120 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294387 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="331">
  <ekin>         5.23114078 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40880223 </eps>
  <enl>          4.76816170 </enl>
  <ecoul>      -15.59909871 </ecoul>
  <exc>         -4.36497998 </exc>
  <esr>          0.05508226 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37357843 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37357843 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70552397 0.00000000 -0.00000015 </position>
    <velocity> -0.00003228 -0.00000000 -0.00000000 </velocity>
    <force> -0.00487587 0.00000001 0.00000142 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36120949 0.00000016 </position>
    <velocity> 0.00000000 0.00010631 0.00000000 </velocity>
    <force> -0.00000001 -0.01087841 -0.00000161 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70552397 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003228 0.00000000 -0.00000000 </velocity>
    <force> 0.00487590 0.00000001 0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36120949 0.00000014 </position>
    <velocity> -0.00000000 -0.00010631 0.00000000 </velocity>
    <force> -0.00000001 0.01087839 -0.00000124 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000128 </ekin_e>
  <ekin_ion> 0.00063198 </ekin_ion>
  <temp_ion> 33.26236277 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294389 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="332">
  <ekin>         5.23095663 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40870689 </eps>
  <enl>          4.76816995 </enl>
  <ecoul>      -15.59909021 </ecoul>
  <exc>         -4.36489991 </exc>
  <esr>          0.05505664 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37357044 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37357044 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70539258 0.00000000 -0.00000015 </position>
    <velocity> -0.00003266 -0.00000000 -0.00000000 </velocity>
    <force> -0.00487159 0.00000001 0.00000144 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36162963 0.00000016 </position>
    <velocity> 0.00000000 0.00010546 0.00000000 </velocity>
    <force> -0.00000001 -0.01093254 -0.00000166 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70539258 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003266 0.00000000 -0.00000000 </velocity>
    <force> 0.00487162 0.00000001 0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36162963 0.00000014 </position>
    <velocity> -0.00000000 -0.00010546 -0.00000000 </velocity>
    <force> -0.00000000 0.01093253 -0.00000121 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000126 </ekin_e>
  <ekin_ion> 0.00062401 </ekin_ion>
  <temp_ion> 32.84277649 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294391 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="333">
  <ekin>         5.23077484 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40861275 </eps>
  <enl>          4.76817777 </enl>
  <ecoul>      -15.59908135 </ecoul>
  <exc>         -4.36482099 </exc>
  <esr>          0.05503149 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37356249 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37356249 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70525967 0.00000000 -0.00000015 </position>
    <velocity> -0.00003304 -0.00000000 0.00000000 </velocity>
    <force> -0.00486684 0.00000002 0.00000144 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36204633 0.00000016 </position>
    <velocity> 0.00000000 0.00010460 0.00000000 </velocity>
    <force> -0.00000002 -0.01098593 -0.00000169 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70525967 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003304 0.00000000 0.00000000 </velocity>
    <force> 0.00486686 -0.00000000 0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36204633 0.00000013 </position>
    <velocity> -0.00000000 -0.00010460 -0.00000000 </velocity>
    <force> 0.00000001 0.01098591 -0.00000118 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000124 </ekin_e>
  <ekin_ion> 0.00061608 </ekin_ion>
  <temp_ion> 32.42545329 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294393 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="334">
  <ekin>         5.23059549 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40851989 </eps>
  <enl>          4.76818524 </enl>
  <ecoul>      -15.59907217 </ecoul>
  <exc>         -4.36474326 </exc>
  <esr>          0.05500684 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37355458 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37355458 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70512524 0.00000000 -0.00000014 </position>
    <velocity> -0.00003342 -0.00000000 0.00000000 </velocity>
    <force> -0.00486159 0.00000003 0.00000144 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36245958 0.00000016 </position>
    <velocity> 0.00000000 0.00010374 -0.00000000 </velocity>
    <force> -0.00000003 -0.01103844 -0.00000171 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70512524 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003342 0.00000000 0.00000000 </velocity>
    <force> 0.00486161 -0.00000001 0.00000128 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36245958 0.00000013 </position>
    <velocity> -0.00000000 -0.00010374 -0.00000000 </velocity>
    <force> 0.00000002 0.01103842 -0.00000115 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000122 </ekin_e>
  <ekin_ion> 0.00060820 </ekin_ion>
  <temp_ion> 32.01047791 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294395 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="335">
  <ekin>         5.23041885 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40842848 </eps>
  <enl>          4.76819245 </enl>
  <ecoul>      -15.59906278 </ecoul>
  <exc>         -4.36466677 </exc>
  <esr>          0.05498266 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37354673 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37354673 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70498930 0.00000000 -0.00000014 </position>
    <velocity> -0.00003380 -0.00000000 0.00000000 </velocity>
    <force> -0.00485584 0.00000003 0.00000142 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36286937 0.00000016 </position>
    <velocity> 0.00000000 0.00010288 -0.00000000 </velocity>
    <force> -0.00000004 -0.01108998 -0.00000171 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70498930 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003380 0.00000000 0.00000000 </velocity>
    <force> 0.00485585 -0.00000001 0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36286937 0.00000013 </position>
    <velocity> -0.00000000 -0.00010288 -0.00000000 </velocity>
    <force> 0.00000003 0.01108997 -0.00000111 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000120 </ekin_e>
  <ekin_ion> 0.00060036 </ekin_ion>
  <temp_ion> 31.59793810 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294396 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="336">
  <ekin>         5.23024533 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40833877 </eps>
  <enl>          4.76819953 </enl>
  <ecoul>      -15.59905339 </ecoul>
  <exc>         -4.36459163 </exc>
  <esr>          0.05495897 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37353892 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37353892 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70485184 0.00000000 -0.00000014 </position>
    <velocity> -0.00003418 -0.00000000 0.00000000 </velocity>
    <force> -0.00484962 0.00000004 0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36327567 0.00000016 </position>
    <velocity> 0.00000000 0.00010201 -0.00000000 </velocity>
    <force> -0.00000005 -0.01114053 -0.00000170 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70485184 -0.00000000 -0.00000014 </position>
    <velocity> 0.00003418 0.00000000 0.00000000 </velocity>
    <force> 0.00484962 -0.00000002 0.00000125 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36327567 0.00000013 </position>
    <velocity> -0.00000000 -0.00010201 -0.00000000 </velocity>
    <force> 0.00000005 0.01114052 -0.00000106 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000118 </ekin_e>
  <ekin_ion> 0.00059257 </ekin_ion>
  <temp_ion> 31.18792312 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294398 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="337">
  <ekin>         5.23007541 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40825104 </eps>
  <enl>          4.76820661 </enl>
  <ecoul>      -15.59904419 </ecoul>
  <exc>         -4.36451796 </exc>
  <esr>          0.05493577 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37353116 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37353116 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70471286 0.00000000 -0.00000014 </position>
    <velocity> -0.00003455 -0.00000000 0.00000000 </velocity>
    <force> -0.00484298 0.00000004 0.00000135 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36367848 0.00000016 </position>
    <velocity> 0.00000000 0.00010114 -0.00000000 </velocity>
    <force> -0.00000005 -0.01119013 -0.00000167 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70471286 -0.00000000 -0.00000013 </position>
    <velocity> 0.00003455 0.00000000 0.00000000 </velocity>
    <force> 0.00484297 -0.00000002 0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36367848 0.00000013 </position>
    <velocity> -0.00000000 -0.00010114 -0.00000000 </velocity>
    <force> 0.00000006 0.01119011 -0.00000101 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000117 </ekin_e>
  <ekin_ion> 0.00058483 </ekin_ion>
  <temp_ion> 30.78052128 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294400 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="338">
  <ekin>         5.22990957 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40816552 </eps>
  <enl>          4.76821379 </enl>
  <ecoul>      -15.59903539 </ecoul>
  <exc>         -4.36444588 </exc>
  <esr>          0.05491305 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37352345 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37352345 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70457238 0.00000000 -0.00000014 </position>
    <velocity> -0.00003493 -0.00000000 0.00000000 </velocity>
    <force> -0.00483602 0.00000005 0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36407778 0.00000016 </position>
    <velocity> 0.00000000 0.00010026 -0.00000000 </velocity>
    <force> -0.00000006 -0.01123888 -0.00000164 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70457237 -0.00000000 -0.00000013 </position>
    <velocity> 0.00003493 0.00000000 0.00000000 </velocity>
    <force> 0.00483600 -0.00000003 0.00000117 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36407778 0.00000013 </position>
    <velocity> -0.00000000 -0.00010026 -0.00000000 </velocity>
    <force> 0.00000006 0.01123887 -0.00000096 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000115 </ekin_e>
  <ekin_ion> 0.00057714 </ekin_ion>
  <temp_ion> 30.37581704 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294402 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="339">
  <ekin>         5.22974817 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40808243 </eps>
  <enl>          4.76822116 </enl>
  <ecoul>      -15.59902718 </ecoul>
  <exc>         -4.36437552 </exc>
  <esr>          0.05489082 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37351579 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37351579 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70443038 0.00000000 -0.00000013 </position>
    <velocity> -0.00003531 -0.00000000 0.00000000 </velocity>
    <force> -0.00482880 0.00000005 0.00000125 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36447354 0.00000015 </position>
    <velocity> 0.00000000 0.00009938 -0.00000000 </velocity>
    <force> -0.00000006 -0.01128700 -0.00000158 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70443038 -0.00000000 -0.00000013 </position>
    <velocity> 0.00003531 0.00000000 0.00000000 </velocity>
    <force> 0.00482878 -0.00000003 0.00000112 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36447354 0.00000012 </position>
    <velocity> -0.00000000 -0.00009938 -0.00000000 </velocity>
    <force> 0.00000007 0.01128698 -0.00000090 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000113 </ekin_e>
  <ekin_ion> 0.00056950 </ekin_ion>
  <temp_ion> 29.97388815 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294404 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="340">
  <ekin>         5.22959145 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40800188 </eps>
  <enl>          4.76822882 </enl>
  <ecoul>      -15.59901966 </ecoul>
  <exc>         -4.36430692 </exc>
  <esr>          0.05486907 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37350819 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37350819 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70428688 0.00000000 -0.00000013 </position>
    <velocity> -0.00003569 -0.00000000 0.00000000 </velocity>
    <force> -0.00482141 0.00000005 0.00000118 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36486577 0.00000015 </position>
    <velocity> 0.00000000 0.00009850 -0.00000000 </velocity>
    <force> -0.00000007 -0.01133470 -0.00000152 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70428688 -0.00000000 -0.00000013 </position>
    <velocity> 0.00003569 0.00000000 0.00000000 </velocity>
    <force> 0.00482137 -0.00000004 0.00000105 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36486577 0.00000012 </position>
    <velocity> -0.00000000 -0.00009850 -0.00000000 </velocity>
    <force> 0.00000008 0.01133469 -0.00000084 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000111 </ekin_e>
  <ekin_ion> 0.00056192 </ekin_ion>
  <temp_ion> 29.57480379 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294406 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="341">
  <ekin>         5.22943943 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40792395 </eps>
  <enl>          4.76823684 </enl>
  <ecoul>      -15.59901286 </ecoul>
  <exc>         -4.36424011 </exc>
  <esr>          0.05484781 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37350064 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37350064 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70414187 0.00000000 -0.00000013 </position>
    <velocity> -0.00003606 -0.00000000 0.00000000 </velocity>
    <force> -0.00481387 0.00000006 0.00000110 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36525444 0.00000015 </position>
    <velocity> 0.00000000 0.00009761 -0.00000000 </velocity>
    <force> -0.00000007 -0.01138219 -0.00000144 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70414187 -0.00000000 -0.00000012 </position>
    <velocity> 0.00003606 0.00000000 0.00000000 </velocity>
    <force> 0.00481383 -0.00000004 0.00000099 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36525444 0.00000012 </position>
    <velocity> -0.00000000 -0.00009761 -0.00000000 </velocity>
    <force> 0.00000009 0.01138218 -0.00000077 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000109 </ekin_e>
  <ekin_ion> 0.00055439 </ekin_ion>
  <temp_ion> 29.17862422 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294408 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="342">
  <ekin>         5.22929191 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40784862 </eps>
  <enl>          4.76824532 </enl>
  <ecoul>      -15.59900673 </ecoul>
  <exc>         -4.36417504 </exc>
  <esr>          0.05482704 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37349315 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37349315 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70399536 0.00000000 -0.00000012 </position>
    <velocity> -0.00003644 -0.00000000 0.00000000 </velocity>
    <force> -0.00480618 0.00000006 0.00000102 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36563953 0.00000014 </position>
    <velocity> 0.00000000 0.00009672 -0.00000000 </velocity>
    <force> -0.00000007 -0.01142963 -0.00000134 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70399536 -0.00000000 -0.00000012 </position>
    <velocity> 0.00003644 0.00000000 0.00000000 </velocity>
    <force> 0.00480614 -0.00000004 0.00000091 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36563953 0.00000011 </position>
    <velocity> -0.00000000 -0.00009672 -0.00000000 </velocity>
    <force> 0.00000009 0.01142963 -0.00000070 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000107 </ekin_e>
  <ekin_ion> 0.00054692 </ekin_ion>
  <temp_ion> 28.78540229 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294410 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="343">
  <ekin>         5.22914851 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40777583 </eps>
  <enl>          4.76825435 </enl>
  <ecoul>      -15.59900114 </ecoul>
  <exc>         -4.36411161 </exc>
  <esr>          0.05480675 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37348572 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37348572 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70384735 0.00000000 -0.00000012 </position>
    <velocity> -0.00003681 0.00000000 0.00000000 </velocity>
    <force> -0.00479830 0.00000006 0.00000093 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36602104 0.00000014 </position>
    <velocity> 0.00000000 0.00009583 -0.00000000 </velocity>
    <force> -0.00000007 -0.01147706 -0.00000124 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70384735 -0.00000000 -0.00000012 </position>
    <velocity> 0.00003681 0.00000000 0.00000000 </velocity>
    <force> 0.00479826 -0.00000005 0.00000083 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36602104 0.00000011 </position>
    <velocity> -0.00000000 -0.00009583 -0.00000000 </velocity>
    <force> 0.00000009 0.01147705 -0.00000063 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000105 </ekin_e>
  <ekin_ion> 0.00053951 </ekin_ion>
  <temp_ion> 28.39518674 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294412 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="344">
  <ekin>         5.22900873 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40770546 </eps>
  <enl>          4.76826398 </enl>
  <ecoul>      -15.59899592 </ecoul>
  <exc>         -4.36404967 </exc>
  <esr>          0.05478695 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37347834 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37347834 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70369785 0.00000000 -0.00000012 </position>
    <velocity> -0.00003719 0.00000000 0.00000000 </velocity>
    <force> -0.00479016 0.00000006 0.00000083 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36639895 0.00000013 </position>
    <velocity> -0.00000000 0.00009493 -0.00000000 </velocity>
    <force> -0.00000007 -0.01152437 -0.00000112 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70369785 -0.00000000 -0.00000011 </position>
    <velocity> 0.00003719 0.00000000 0.00000000 </velocity>
    <force> 0.00479011 -0.00000005 0.00000075 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36639895 0.00000011 </position>
    <velocity> -0.00000000 -0.00009493 -0.00000000 </velocity>
    <force> 0.00000010 0.01152437 -0.00000056 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000103 </ekin_e>
  <ekin_ion> 0.00053215 </ekin_ion>
  <temp_ion> 28.00802633 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294414 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="345">
  <ekin>         5.22887202 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40763732 </eps>
  <enl>          4.76827420 </enl>
  <ecoul>      -15.59899085 </ecoul>
  <exc>         -4.36398909 </exc>
  <esr>          0.05476764 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37347103 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37347103 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70354685 0.00000000 -0.00000011 </position>
    <velocity> -0.00003756 0.00000000 0.00000000 </velocity>
    <force> -0.00478165 0.00000005 0.00000073 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36677324 0.00000013 </position>
    <velocity> -0.00000000 0.00009402 -0.00000000 </velocity>
    <force> -0.00000007 -0.01157138 -0.00000100 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70354685 -0.00000000 -0.00000011 </position>
    <velocity> 0.00003756 0.00000000 0.00000000 </velocity>
    <force> 0.00478159 -0.00000005 0.00000067 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36677324 0.00000010 </position>
    <velocity> 0.00000000 -0.00009403 -0.00000000 </velocity>
    <force> 0.00000010 0.01157138 -0.00000049 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000101 </ekin_e>
  <ekin_ion> 0.00052485 </ekin_ion>
  <temp_ion> 27.62397415 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294416 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="346">
  <ekin>         5.22873791 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40757120 </eps>
  <enl>          4.76828493 </enl>
  <ecoul>      -15.59898573 </ecoul>
  <exc>         -4.36392969 </exc>
  <esr>          0.05474882 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37346377 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37346377 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70339436 0.00000000 -0.00000011 </position>
    <velocity> -0.00003794 0.00000000 0.00000000 </velocity>
    <force> -0.00477269 0.00000005 0.00000062 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36714391 0.00000012 </position>
    <velocity> -0.00000000 0.00009312 -0.00000000 </velocity>
    <force> -0.00000007 -0.01161783 -0.00000086 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70339435 -0.00000000 -0.00000010 </position>
    <velocity> 0.00003794 -0.00000000 0.00000000 </velocity>
    <force> 0.00477263 -0.00000005 0.00000058 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36714391 0.00000010 </position>
    <velocity> 0.00000000 -0.00009312 -0.00000000 </velocity>
    <force> 0.00000010 0.01161783 -0.00000041 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000099 </ekin_e>
  <ekin_ion> 0.00051762 </ekin_ion>
  <temp_ion> 27.24309063 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294417 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="347">
  <ekin>         5.22860602 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40750688 </eps>
  <enl>          4.76829597 </enl>
  <ecoul>      -15.59898036 </ecoul>
  <exc>         -4.36387134 </exc>
  <esr>          0.05473049 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37345658 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37345658 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70324038 0.00000000 -0.00000010 </position>
    <velocity> -0.00003831 0.00000000 0.00000000 </velocity>
    <force> -0.00476322 0.00000005 0.00000051 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36751092 0.00000012 </position>
    <velocity> -0.00000000 0.00009221 -0.00000000 </velocity>
    <force> -0.00000007 -0.01166342 -0.00000072 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70324037 -0.00000000 -0.00000010 </position>
    <velocity> 0.00003831 -0.00000000 0.00000000 </velocity>
    <force> 0.00476316 -0.00000005 0.00000049 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36751092 0.00000009 </position>
    <velocity> 0.00000000 -0.00009221 -0.00000000 </velocity>
    <force> 0.00000009 0.01166343 -0.00000034 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000098 </ekin_e>
  <ekin_ion> 0.00051044 </ekin_ion>
  <temp_ion> 26.86544491 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294419 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="348">
  <ekin>         5.22847617 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40744412 </eps>
  <enl>          4.76830709 </enl>
  <ecoul>      -15.59897462 </ecoul>
  <exc>         -4.36381398 </exc>
  <esr>          0.05471265 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37344946 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37344946 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70308491 0.00000000 -0.00000010 </position>
    <velocity> -0.00003868 0.00000000 0.00000000 </velocity>
    <force> -0.00475322 0.00000004 0.00000040 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.36787428 0.00000011 </position>
    <velocity> -0.00000000 0.00009130 -0.00000000 </velocity>
    <force> -0.00000006 -0.01170795 -0.00000057 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70308491 -0.00000000 -0.00000009 </position>
    <velocity> 0.00003868 -0.00000000 0.00000000 </velocity>
    <force> 0.00475317 -0.00000005 0.00000040 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36787428 0.00000009 </position>
    <velocity> 0.00000000 -0.00009130 -0.00000000 </velocity>
    <force> 0.00000009 0.01170795 -0.00000027 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000096 </ekin_e>
  <ekin_ion> 0.00050333 </ekin_ion>
  <temp_ion> 26.49111396 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294420 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="349">
  <ekin>         5.22834837 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40738276 </eps>
  <enl>          4.76831805 </enl>
  <ecoul>      -15.59896847 </ecoul>
  <exc>         -4.36375758 </exc>
  <esr>          0.05469529 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37344239 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37344239 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70292796 0.00000000 -0.00000009 </position>
    <velocity> -0.00003905 0.00000000 0.00000000 </velocity>
    <force> -0.00474272 0.00000004 0.00000028 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36823396 0.00000010 </position>
    <velocity> -0.00000000 0.00009038 -0.00000000 </velocity>
    <force> -0.00000006 -0.01175127 -0.00000042 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70292796 -0.00000000 -0.00000009 </position>
    <velocity> 0.00003905 -0.00000000 0.00000000 </velocity>
    <force> 0.00474267 -0.00000005 0.00000031 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36823396 0.00000008 </position>
    <velocity> 0.00000000 -0.00009038 -0.00000000 </velocity>
    <force> 0.00000008 0.01175128 -0.00000019 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000095 </ekin_e>
  <ekin_ion> 0.00049628 </ekin_ion>
  <temp_ion> 26.12017992 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294422 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="350">
  <ekin>         5.22822279 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40732276 </eps>
  <enl>          4.76832866 </enl>
  <ecoul>      -15.59896193 </ecoul>
  <exc>         -4.36370216 </exc>
  <esr>          0.05467843 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37343540 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37343540 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70276954 0.00000000 -0.00000009 </position>
    <velocity> -0.00003942 0.00000000 0.00000000 </velocity>
    <force> -0.00473175 0.00000003 0.00000016 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36858996 0.00000010 </position>
    <velocity> -0.00000000 0.00008946 -0.00000000 </velocity>
    <force> -0.00000005 -0.01179338 -0.00000026 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70276954 -0.00000000 -0.00000008 </position>
    <velocity> 0.00003942 -0.00000000 0.00000000 </velocity>
    <force> 0.00473171 -0.00000005 0.00000021 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36858996 0.00000008 </position>
    <velocity> 0.00000000 -0.00008946 -0.00000000 </velocity>
    <force> 0.00000008 0.01179339 -0.00000012 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000093 </ekin_e>
  <ekin_ion> 0.00048930 </ekin_ion>
  <temp_ion> 25.75272636 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294423 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="351">
  <ekin>         5.22809978 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40726417 </eps>
  <enl>          4.76833887 </enl>
  <ecoul>      -15.59895514 </ecoul>
  <exc>         -4.36364780 </exc>
  <esr>          0.05466206 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37342847 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37342847 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70260963 0.00000000 -0.00000008 </position>
    <velocity> -0.00003979 0.00000000 0.00000000 </velocity>
    <force> -0.00472040 0.00000003 0.00000004 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36894226 0.00000009 </position>
    <velocity> -0.00000000 0.00008854 -0.00000000 </velocity>
    <force> -0.00000005 -0.01183437 -0.00000010 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70260963 -0.00000000 -0.00000008 </position>
    <velocity> 0.00003979 -0.00000000 0.00000000 </velocity>
    <force> 0.00472035 -0.00000004 0.00000011 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36894226 0.00000008 </position>
    <velocity> 0.00000000 -0.00008854 -0.00000000 </velocity>
    <force> 0.00000007 0.01183438 -0.00000004 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000092 </ekin_e>
  <ekin_ion> 0.00048239 </ekin_ion>
  <temp_ion> 25.38883425 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294425 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="352">
  <ekin>         5.22797973 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40720721 </eps>
  <enl>          4.76834878 </enl>
  <ecoul>      -15.59894828 </ecoul>
  <exc>         -4.36359462 </exc>
  <esr>          0.05464617 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37342161 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37342161 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70244826 0.00000000 -0.00000008 </position>
    <velocity> -0.00004016 0.00000000 0.00000000 </velocity>
    <force> -0.00470870 0.00000002 -0.00000008 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36929085 0.00000008 </position>
    <velocity> -0.00000000 0.00008761 -0.00000000 </velocity>
    <force> -0.00000004 -0.01187441 0.00000006 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70244826 -0.00000000 -0.00000007 </position>
    <velocity> 0.00004016 -0.00000000 0.00000000 </velocity>
    <force> 0.00470866 -0.00000004 0.00000001 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36929085 0.00000007 </position>
    <velocity> 0.00000000 -0.00008761 -0.00000000 </velocity>
    <force> 0.00000006 0.01187442 0.00000003 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000090 </ekin_e>
  <ekin_ion> 0.00047554 </ekin_ion>
  <temp_ion> 25.02857872 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294426 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="353">
  <ekin>         5.22786308 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40715221 </eps>
  <enl>          4.76835865 </enl>
  <ecoul>      -15.59894158 </ecoul>
  <exc>         -4.36354275 </exc>
  <esr>          0.05463078 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37341481 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37341481 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70228542 0.00000000 -0.00000007 </position>
    <velocity> -0.00004053 0.00000000 0.00000000 </velocity>
    <force> -0.00469669 0.00000002 -0.00000020 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36963572 0.00000008 </position>
    <velocity> -0.00000000 0.00008668 -0.00000000 </velocity>
    <force> -0.00000003 -0.01191372 0.00000021 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70228542 -0.00000000 -0.00000007 </position>
    <velocity> 0.00004053 -0.00000000 0.00000000 </velocity>
    <force> 0.00469666 -0.00000003 -0.00000010 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36963572 0.00000007 </position>
    <velocity> 0.00000000 -0.00008668 -0.00000000 </velocity>
    <force> 0.00000005 0.01191374 0.00000011 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000088 </ekin_e>
  <ekin_ion> 0.00046877 </ekin_ion>
  <temp_ion> 24.67202691 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294428 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="354">
  <ekin>         5.22775019 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40709952 </eps>
  <enl>          4.76836882 </enl>
  <ecoul>      -15.59893526 </ecoul>
  <exc>         -4.36349231 </exc>
  <esr>          0.05461588 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37340809 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37340809 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70212112 0.00000000 -0.00000007 </position>
    <velocity> -0.00004089 0.00000000 0.00000000 </velocity>
    <force> -0.00468437 0.00000001 -0.00000032 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.36997685 0.00000007 </position>
    <velocity> -0.00000000 0.00008575 -0.00000000 </velocity>
    <force> -0.00000003 -0.01195250 0.00000037 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70212111 -0.00000000 -0.00000006 </position>
    <velocity> 0.00004089 -0.00000000 0.00000000 </velocity>
    <force> 0.00468435 -0.00000003 -0.00000020 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.36997685 0.00000006 </position>
    <velocity> 0.00000000 -0.00008575 -0.00000000 </velocity>
    <force> 0.00000004 0.01195252 0.00000018 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000087 </ekin_e>
  <ekin_ion> 0.00046206 </ekin_ion>
  <temp_ion> 24.31923736 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294430 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="355">
  <ekin>         5.22764135 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40704949 </eps>
  <enl>          4.76837960 </enl>
  <ecoul>      -15.59892951 </ecoul>
  <exc>         -4.36344341 </exc>
  <esr>          0.05460147 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37340144 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37340144 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70195535 0.00000000 -0.00000006 </position>
    <velocity> -0.00004126 0.00000000 0.00000000 </velocity>
    <force> -0.00467173 0.00000000 -0.00000044 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37031423 0.00000007 </position>
    <velocity> -0.00000000 0.00008481 -0.00000000 </velocity>
    <force> -0.00000002 -0.01199094 0.00000052 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70195535 -0.00000000 -0.00000006 </position>
    <velocity> 0.00004126 -0.00000000 0.00000000 </velocity>
    <force> 0.00467171 -0.00000002 -0.00000031 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37031423 0.00000006 </position>
    <velocity> 0.00000000 -0.00008481 -0.00000000 </velocity>
    <force> 0.00000003 0.01199095 0.00000026 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000085 </ekin_e>
  <ekin_ion> 0.00045543 </ekin_ion>
  <temp_ion> 23.97026052 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294432 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="356">
  <ekin>         5.22753675 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40700231 </eps>
  <enl>          4.76839125 </enl>
  <ecoul>      -15.59892443 </ecoul>
  <exc>         -4.36339612 </exc>
  <esr>          0.05458755 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37339487 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37339487 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70178813 0.00000000 -0.00000006 </position>
    <velocity> -0.00004162 0.00000000 0.00000000 </velocity>
    <force> -0.00465872 -0.00000000 -0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37064786 0.00000006 </position>
    <velocity> -0.00000000 0.00008388 -0.00000000 </velocity>
    <force> -0.00000001 -0.01202915 0.00000067 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70178813 -0.00000000 -0.00000006 </position>
    <velocity> 0.00004162 -0.00000000 0.00000000 </velocity>
    <force> 0.00465871 -0.00000002 -0.00000041 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37064786 0.00000005 </position>
    <velocity> 0.00000000 -0.00008388 -0.00000000 </velocity>
    <force> 0.00000001 0.01202917 0.00000033 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000083 </ekin_e>
  <ekin_ion> 0.00044888 </ekin_ion>
  <temp_ion> 23.62514023 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294434 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="357">
  <ekin>         5.22743641 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40695804 </eps>
  <enl>          4.76840383 </enl>
  <ecoul>      -15.59892005 </ecoul>
  <exc>         -4.36335051 </exc>
  <esr>          0.05457412 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37338837 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37338837 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70161946 0.00000000 -0.00000005 </position>
    <velocity> -0.00004199 0.00000000 0.00000000 </velocity>
    <force> -0.00464531 -0.00000001 -0.00000067 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37097771 0.00000006 </position>
    <velocity> -0.00000000 0.00008293 -0.00000000 </velocity>
    <force> 0.00000000 -0.01206722 0.00000082 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70161946 -0.00000000 -0.00000005 </position>
    <velocity> 0.00004199 -0.00000000 0.00000000 </velocity>
    <force> 0.00464531 -0.00000001 -0.00000051 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37097771 0.00000005 </position>
    <velocity> 0.00000000 -0.00008293 -0.00000000 </velocity>
    <force> 0.00000000 0.01206724 0.00000041 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000081 </ekin_e>
  <ekin_ion> 0.00044239 </ekin_ion>
  <temp_ion> 23.28391559 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294436 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="358">
  <ekin>         5.22734027 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40691652 </eps>
  <enl>          4.76841720 </enl>
  <ecoul>      -15.59891630 </ecoul>
  <exc>         -4.36330659 </exc>
  <esr>          0.05456118 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37338194 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37338194 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70144934 0.00000000 -0.00000005 </position>
    <velocity> -0.00004235 0.00000000 0.00000000 </velocity>
    <force> -0.00463149 -0.00000002 -0.00000078 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37130378 0.00000005 </position>
    <velocity> -0.00000000 0.00008199 -0.00000000 </velocity>
    <force> 0.00000001 -0.01210518 0.00000096 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70144934 -0.00000000 -0.00000005 </position>
    <velocity> 0.00004235 -0.00000000 0.00000000 </velocity>
    <force> 0.00463149 -0.00000000 -0.00000061 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37130378 0.00000005 </position>
    <velocity> 0.00000000 -0.00008199 -0.00000000 </velocity>
    <force> -0.00000001 0.01210520 0.00000048 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000079 </ekin_e>
  <ekin_ion> 0.00043598 </ekin_ion>
  <temp_ion> 22.94662305 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294437 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="359">
  <ekin>         5.22724815 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40687746 </eps>
  <enl>          4.76843110 </enl>
  <ecoul>      -15.59891303 </ecoul>
  <exc>         -4.36326436 </exc>
  <esr>          0.05454874 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37337559 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37337559 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70127777 0.00000000 -0.00000004 </position>
    <velocity> -0.00004271 0.00000000 0.00000000 </velocity>
    <force> -0.00461726 -0.00000002 -0.00000088 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37162605 0.00000005 </position>
    <velocity> -0.00000000 0.00008104 -0.00000000 </velocity>
    <force> 0.00000002 -0.01214301 0.00000109 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70127777 -0.00000000 -0.00000004 </position>
    <velocity> 0.00004271 -0.00000000 0.00000000 </velocity>
    <force> 0.00461727 0.00000000 -0.00000070 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37162605 0.00000004 </position>
    <velocity> 0.00000000 -0.00008104 -0.00000000 </velocity>
    <force> -0.00000002 0.01214303 0.00000055 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000077 </ekin_e>
  <ekin_ion> 0.00042965 </ekin_ion>
  <temp_ion> 22.61329843 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294439 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="360">
  <ekin>         5.22715986 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40684049 </eps>
  <enl>          4.76844516 </enl>
  <ecoul>      -15.59891006 </ecoul>
  <exc>         -4.36322379 </exc>
  <esr>          0.05453678 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37336931 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37336931 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70110477 0.00000000 -0.00000004 </position>
    <velocity> -0.00004307 0.00000000 0.00000000 </velocity>
    <force> -0.00460263 -0.00000003 -0.00000097 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37194452 0.00000004 </position>
    <velocity> -0.00000000 0.00008009 -0.00000000 </velocity>
    <force> 0.00000003 -0.01218064 0.00000121 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70110477 -0.00000000 -0.00000004 </position>
    <velocity> 0.00004307 -0.00000000 0.00000000 </velocity>
    <force> 0.00460264 0.00000001 -0.00000079 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37194452 0.00000004 </position>
    <velocity> 0.00000000 -0.00008009 -0.00000000 </velocity>
    <force> -0.00000003 0.01218066 0.00000062 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000075 </ekin_e>
  <ekin_ion> 0.00042339 </ekin_ion>
  <temp_ion> 22.28397892 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294441 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="361">
  <ekin>         5.22707518 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40680526 </eps>
  <enl>          4.76845905 </enl>
  <ecoul>      -15.59890722 </ecoul>
  <exc>         -4.36318486 </exc>
  <esr>          0.05452532 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37336311 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37336311 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70093034 0.00000000 -0.00000004 </position>
    <velocity> -0.00004343 0.00000000 0.00000000 </velocity>
    <force> -0.00458763 -0.00000003 -0.00000105 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37225917 0.00000004 </position>
    <velocity> -0.00000000 0.00007914 -0.00000000 </velocity>
    <force> 0.00000003 -0.01221796 0.00000132 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70093034 -0.00000000 -0.00000004 </position>
    <velocity> 0.00004343 -0.00000000 0.00000000 </velocity>
    <force> 0.00458765 0.00000002 -0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37225917 0.00000004 </position>
    <velocity> 0.00000000 -0.00007914 -0.00000000 </velocity>
    <force> -0.00000004 0.01221797 0.00000069 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000074 </ekin_e>
  <ekin_ion> 0.00041721 </ekin_ion>
  <temp_ion> 21.95870476 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294443 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.013" max="    0.013"/>
<iteration count="362">
  <ekin>         5.22699397 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40677157 </eps>
  <enl>          4.76847255 </enl>
  <ecoul>      -15.59890441 </ecoul>
  <exc>         -4.36314755 </exc>
  <esr>          0.05451435 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37335700 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37335700 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70075447 0.00000000 -0.00000003 </position>
    <velocity> -0.00004379 0.00000000 0.00000000 </velocity>
    <force> -0.00457227 -0.00000004 -0.00000112 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37256999 0.00000003 </position>
    <velocity> -0.00000000 0.00007818 -0.00000000 </velocity>
    <force> 0.00000004 -0.01225480 0.00000142 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70075447 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004379 -0.00000000 0.00000000 </velocity>
    <force> 0.00457229 0.00000002 -0.00000095 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37256999 0.00000003 </position>
    <velocity> 0.00000000 -0.00007818 -0.00000000 </velocity>
    <force> -0.00000005 0.01225481 0.00000076 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000072 </ekin_e>
  <ekin_ion> 0.00041111 </ekin_ion>
  <temp_ion> 21.63752058 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294444 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="363">
  <ekin>         5.22691615 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40673937 </eps>
  <enl>          4.76848565 </enl>
  <ecoul>      -15.59890158 </ecoul>
  <exc>         -4.36311181 </exc>
  <esr>          0.05450387 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37335096 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37335096 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70057718 0.00000000 -0.00000003 </position>
    <velocity> -0.00004414 0.00000000 0.00000000 </velocity>
    <force> -0.00455654 -0.00000004 -0.00000119 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37287697 0.00000003 </position>
    <velocity> -0.00000000 0.00007722 -0.00000000 </velocity>
    <force> 0.00000005 -0.01229098 0.00000151 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70057718 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004414 -0.00000000 0.00000000 </velocity>
    <force> 0.00455658 0.00000003 -0.00000102 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37287697 0.00000003 </position>
    <velocity> 0.00000000 -0.00007722 -0.00000000 </velocity>
    <force> -0.00000006 0.01229099 0.00000082 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000071 </ekin_e>
  <ekin_ion> 0.00040509 </ekin_ion>
  <temp_ion> 21.32047610 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294446 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.011" max="    0.011"/>
<iteration count="364">
  <ekin>         5.22684174 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40670885 </eps>
  <enl>          4.76849852 </enl>
  <ecoul>      -15.59889878 </ecoul>
  <exc>         -4.36307762 </exc>
  <esr>          0.05449388 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37334500 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37334500 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70039848 0.00000000 -0.00000003 </position>
    <velocity> -0.00004450 0.00000000 0.00000000 </velocity>
    <force> -0.00454044 -0.00000004 -0.00000124 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37318010 0.00000003 </position>
    <velocity> -0.00000000 0.00007626 -0.00000000 </velocity>
    <force> 0.00000006 -0.01232631 0.00000158 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70039848 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004450 -0.00000000 0.00000000 </velocity>
    <force> 0.00454048 0.00000004 -0.00000109 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37318010 0.00000003 </position>
    <velocity> 0.00000000 -0.00007626 -0.00000000 </velocity>
    <force> -0.00000007 0.01232632 0.00000088 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000069 </ekin_e>
  <ekin_ion> 0.00039914 </ekin_ion>
  <temp_ion> 21.00762581 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294447 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="365">
  <ekin>         5.22677085 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40668034 </eps>
  <enl>          4.76851150 </enl>
  <ecoul>      -15.59889615 </ecoul>
  <exc>         -4.36304499 </exc>
  <esr>          0.05448439 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37333912 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37333912 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70021836 0.00000000 -0.00000003 </position>
    <velocity> -0.00004485 0.00000000 0.00000000 </velocity>
    <force> -0.00452392 -0.00000005 -0.00000129 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37347936 0.00000003 </position>
    <velocity> -0.00000000 0.00007530 -0.00000000 </velocity>
    <force> 0.00000006 -0.01236065 0.00000164 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70021836 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004485 -0.00000000 0.00000000 </velocity>
    <force> 0.00452396 0.00000004 -0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37347936 0.00000002 </position>
    <velocity> 0.00000000 -0.00007530 -0.00000000 </velocity>
    <force> -0.00000008 0.01236065 0.00000093 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000068 </ekin_e>
  <ekin_ion> 0.00039328 </ekin_ion>
  <temp_ion> 20.69902767 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294448 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="366">
  <ekin>         5.22670364 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40665422 </eps>
  <enl>          4.76852498 </enl>
  <ecoul>      -15.59889383 </ecoul>
  <exc>         -4.36301390 </exc>
  <esr>          0.05447539 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37333333 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37333333 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70003683 0.00000000 -0.00000002 </position>
    <velocity> -0.00004521 0.00000000 0.00000000 </velocity>
    <force> -0.00450696 -0.00000005 -0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37377475 0.00000003 </position>
    <velocity> -0.00000000 0.00007433 -0.00000000 </velocity>
    <force> 0.00000007 -0.01239393 0.00000168 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70003683 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004521 -0.00000000 0.00000000 </velocity>
    <force> 0.00450701 0.00000004 -0.00000120 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37377475 0.00000002 </position>
    <velocity> 0.00000000 -0.00007433 -0.00000000 </velocity>
    <force> -0.00000009 0.01239393 0.00000099 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000067 </ekin_e>
  <ekin_ion> 0.00038750 </ekin_ion>
  <temp_ion> 20.39474080 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294450 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="367">
  <ekin>         5.22664024 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40663085 </eps>
  <enl>          4.76853932 </enl>
  <ecoul>      -15.59889198 </ecoul>
  <exc>         -4.36298435 </exc>
  <esr>          0.05446688 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37332762 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37332762 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69985389 0.00000000 -0.00000002 </position>
    <velocity> -0.00004556 0.00000000 0.00000000 </velocity>
    <force> -0.00448955 -0.00000005 -0.00000135 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37406626 0.00000002 </position>
    <velocity> -0.00000000 0.00007336 -0.00000000 </velocity>
    <force> 0.00000007 -0.01242618 0.00000171 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69985389 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004556 -0.00000000 0.00000000 </velocity>
    <force> 0.00448960 0.00000005 -0.00000125 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37406626 0.00000002 </position>
    <velocity> 0.00000000 -0.00007336 -0.00000000 </velocity>
    <force> -0.00000009 0.01242618 0.00000104 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000066 </ekin_e>
  <ekin_ion> 0.00038180 </ekin_ion>
  <temp_ion> 20.09482263 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294451 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="368">
  <ekin>         5.22658077 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40661042 </eps>
  <enl>          4.76855469 </enl>
  <ecoul>      -15.59889069 </ecoul>
  <exc>         -4.36295634 </exc>
  <esr>          0.05445886 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37332199 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37332199 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69966956 0.00000000 -0.00000002 </position>
    <velocity> -0.00004591 0.00000000 0.00000000 </velocity>
    <force> -0.00447171 -0.00000005 -0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37435387 0.00000002 </position>
    <velocity> -0.00000000 0.00007239 -0.00000000 </velocity>
    <force> 0.00000007 -0.01245756 0.00000172 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69966956 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004591 -0.00000000 0.00000000 </velocity>
    <force> 0.00447176 0.00000005 -0.00000129 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37435387 0.00000002 </position>
    <velocity> 0.00000000 -0.00007239 -0.00000000 </velocity>
    <force> -0.00000009 0.01245756 0.00000108 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000064 </ekin_e>
  <ekin_ion> 0.00037619 </ekin_ion>
  <temp_ion> 19.79932612 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294452 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="369">
  <ekin>         5.22652521 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40659291 </eps>
  <enl>          4.76857106 </enl>
  <ecoul>      -15.59888996 </ecoul>
  <exc>         -4.36292985 </exc>
  <esr>          0.05445133 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37331645 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37331645 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69948384 0.00000000 -0.00000002 </position>
    <velocity> -0.00004626 -0.00000000 0.00000000 </velocity>
    <force> -0.00445350 -0.00000005 -0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37463758 0.00000002 </position>
    <velocity> -0.00000000 0.00007142 -0.00000000 </velocity>
    <force> 0.00000007 -0.01248828 0.00000172 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69948384 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004626 -0.00000000 0.00000000 </velocity>
    <force> 0.00445354 0.00000005 -0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37463758 0.00000002 </position>
    <velocity> 0.00000000 -0.00007142 -0.00000000 </velocity>
    <force> -0.00000010 0.01248827 0.00000113 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000063 </ekin_e>
  <ekin_ion> 0.00037066 </ekin_ion>
  <temp_ion> 19.50829780 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294453 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="370">
  <ekin>         5.22647349 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40657805 </eps>
  <enl>          4.76858815 </enl>
  <ecoul>      -15.59888972 </ecoul>
  <exc>         -4.36290487 </exc>
  <esr>          0.05444430 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37331100 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37331100 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69929673 0.00000000 -0.00000002 </position>
    <velocity> -0.00004660 -0.00000000 -0.00000000 </velocity>
    <force> -0.00443500 -0.00000005 -0.00000140 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37491738 0.00000003 </position>
    <velocity> -0.00000000 0.00007044 0.00000000 </velocity>
    <force> 0.00000007 -0.01251859 0.00000170 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69929674 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004660 -0.00000000 0.00000000 </velocity>
    <force> 0.00443504 0.00000006 -0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37491738 0.00000002 </position>
    <velocity> -0.00000000 -0.00007044 -0.00000000 </velocity>
    <force> -0.00000010 0.01251858 0.00000117 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000062 </ekin_e>
  <ekin_ion> 0.00036521 </ekin_ion>
  <temp_ion> 19.22177726 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294454 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="371">
  <ekin>         5.22642543 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40656540 </eps>
  <enl>          4.76860551 </enl>
  <ecoul>      -15.59888981 </ecoul>
  <exc>         -4.36288136 </exc>
  <esr>          0.05443775 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37330563 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37330563 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69910825 0.00000000 -0.00000002 </position>
    <velocity> -0.00004695 -0.00000000 -0.00000000 </velocity>
    <force> -0.00441631 -0.00000004 -0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37519325 0.00000003 </position>
    <velocity> 0.00000000 0.00006946 0.00000000 </velocity>
    <force> 0.00000007 -0.01254871 0.00000167 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69910825 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004695 -0.00000000 -0.00000000 </velocity>
    <force> 0.00441635 0.00000006 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37519325 0.00000002 </position>
    <velocity> -0.00000000 -0.00006946 -0.00000000 </velocity>
    <force> -0.00000010 0.01254870 0.00000120 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000061 </ekin_e>
  <ekin_ion> 0.00035985 </ekin_ion>
  <temp_ion> 18.93979817 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294456 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="372">
  <ekin>         5.22638081 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40655444 </eps>
  <enl>          4.76862260 </enl>
  <ecoul>      -15.59889003 </ecoul>
  <exc>         -4.36285929 </exc>
  <esr>          0.05443170 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37330034 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37330034 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69891838 0.00000000 -0.00000002 </position>
    <velocity> -0.00004729 -0.00000000 -0.00000000 </velocity>
    <force> -0.00439753 -0.00000004 -0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37546520 0.00000003 </position>
    <velocity> 0.00000000 0.00006848 0.00000000 </velocity>
    <force> 0.00000007 -0.01257876 0.00000163 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69891838 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004729 0.00000000 -0.00000000 </velocity>
    <force> 0.00439757 0.00000006 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37546520 0.00000002 </position>
    <velocity> -0.00000000 -0.00006848 0.00000000 </velocity>
    <force> -0.00000009 0.01257875 0.00000123 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000060 </ekin_e>
  <ekin_ion> 0.00035458 </ekin_ion>
  <temp_ion> 18.66239071 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294457 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="373">
  <ekin>         5.22633941 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40654472 </eps>
  <enl>          4.76863897 </enl>
  <ecoul>      -15.59889020 </ecoul>
  <exc>         -4.36283861 </exc>
  <esr>          0.05442614 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37329515 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37329515 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69872715 0.00000000 -0.00000003 </position>
    <velocity> -0.00004764 -0.00000000 -0.00000000 </velocity>
    <force> -0.00437869 -0.00000004 -0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37573320 0.00000003 </position>
    <velocity> 0.00000000 0.00006749 0.00000000 </velocity>
    <force> 0.00000007 -0.01260873 0.00000158 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69872715 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004764 0.00000000 -0.00000000 </velocity>
    <force> 0.00437873 0.00000006 -0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37573320 0.00000002 </position>
    <velocity> -0.00000000 -0.00006749 0.00000000 </velocity>
    <force> -0.00000009 0.01260872 0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000059 </ekin_e>
  <ekin_ion> 0.00034940 </ekin_ion>
  <temp_ion> 18.38958473 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294458 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="374">
  <ekin>         5.22630106 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40653600 </eps>
  <enl>          4.76865436 </enl>
  <ecoul>      -15.59889019 </ecoul>
  <exc>         -4.36281928 </exc>
  <esr>          0.05442108 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37329005 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37329005 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69853456 0.00000000 -0.00000003 </position>
    <velocity> -0.00004798 -0.00000000 -0.00000000 </velocity>
    <force> -0.00435981 -0.00000004 -0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37599726 0.00000003 </position>
    <velocity> 0.00000000 0.00006651 0.00000000 </velocity>
    <force> 0.00000007 -0.01263848 0.00000152 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69853456 -0.00000000 -0.00000002 </position>
    <velocity> 0.00004798 0.00000000 -0.00000000 </velocity>
    <force> 0.00435985 0.00000005 -0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37599726 0.00000002 </position>
    <velocity> -0.00000000 -0.00006651 0.00000000 </velocity>
    <force> -0.00000008 0.01263846 0.00000126 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000058 </ekin_e>
  <ekin_ion> 0.00034431 </ekin_ion>
  <temp_ion> 18.12141270 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294459 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="375">
  <ekin>         5.22626565 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40652827 </eps>
  <enl>          4.76866880 </enl>
  <ecoul>      -15.59888994 </ecoul>
  <exc>         -4.36280126 </exc>
  <esr>          0.05441650 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37328503 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37328503 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69834061 0.00000000 -0.00000003 </position>
    <velocity> -0.00004832 -0.00000000 -0.00000000 </velocity>
    <force> -0.00434082 -0.00000003 -0.00000129 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37625736 0.00000004 </position>
    <velocity> 0.00000000 0.00006552 0.00000000 </velocity>
    <force> 0.00000006 -0.01266775 0.00000144 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69834061 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004832 0.00000000 -0.00000000 </velocity>
    <force> 0.00434085 0.00000005 -0.00000128 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37625736 0.00000002 </position>
    <velocity> -0.00000000 -0.00006552 0.00000000 </velocity>
    <force> -0.00000008 0.01266773 0.00000127 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000057 </ekin_e>
  <ekin_ion> 0.00033930 </ekin_ion>
  <temp_ion> 17.85791167 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294460 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="376">
  <ekin>         5.22623318 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40652184 </eps>
  <enl>          4.76868262 </enl>
  <ecoul>      -15.59888952 </ecoul>
  <exc>         -4.36278454 </exc>
  <esr>          0.05441242 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37328010 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37328010 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69814531 0.00000000 -0.00000003 </position>
    <velocity> -0.00004866 -0.00000000 -0.00000000 </velocity>
    <force> -0.00432157 -0.00000003 -0.00000123 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37651348 0.00000004 </position>
    <velocity> 0.00000000 0.00006453 0.00000000 </velocity>
    <force> 0.00000006 -0.01269624 0.00000136 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69814531 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004866 0.00000000 -0.00000000 </velocity>
    <force> 0.00432160 0.00000005 -0.00000124 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37651348 0.00000002 </position>
    <velocity> -0.00000000 -0.00006453 0.00000000 </velocity>
    <force> -0.00000007 0.01269622 0.00000127 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000056 </ekin_e>
  <ekin_ion> 0.00033438 </ekin_ion>
  <temp_ion> 17.59912365 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294460 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="377">
  <ekin>         5.22620371 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40651717 </eps>
  <enl>          4.76869634 </enl>
  <ecoul>      -15.59888903 </ecoul>
  <exc>         -4.36276913 </exc>
  <esr>          0.05440882 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37327527 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37327527 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69794866 0.00000000 -0.00000004 </position>
    <velocity> -0.00004899 -0.00000000 -0.00000000 </velocity>
    <force> -0.00430192 -0.00000002 -0.00000117 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37676564 0.00000004 </position>
    <velocity> 0.00000000 0.00006354 0.00000000 </velocity>
    <force> 0.00000005 -0.01272367 0.00000126 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69794866 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004899 0.00000000 -0.00000000 </velocity>
    <force> 0.00430194 0.00000004 -0.00000120 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37676564 0.00000003 </position>
    <velocity> -0.00000000 -0.00006354 0.00000000 </velocity>
    <force> -0.00000006 0.01272365 0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000055 </ekin_e>
  <ekin_ion> 0.00032956 </ekin_ion>
  <temp_ion> 17.34509435 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294461 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="378">
  <ekin>         5.22617737 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40651480 </eps>
  <enl>          4.76871055 </enl>
  <ecoul>      -15.59888862 </ecoul>
  <exc>         -4.36275503 </exc>
  <esr>          0.05440572 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37327053 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37327053 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69775068 0.00000000 -0.00000004 </position>
    <velocity> -0.00004933 -0.00000000 -0.00000000 </velocity>
    <force> -0.00428168 -0.00000002 -0.00000110 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37701380 0.00000005 </position>
    <velocity> 0.00000000 0.00006254 0.00000000 </velocity>
    <force> 0.00000005 -0.01274986 0.00000116 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69775068 -0.00000000 -0.00000003 </position>
    <velocity> 0.00004933 0.00000000 -0.00000000 </velocity>
    <force> 0.00428170 0.00000004 -0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37701380 0.00000003 </position>
    <velocity> -0.00000000 -0.00006254 0.00000000 </velocity>
    <force> -0.00000005 0.01274984 0.00000123 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000054 </ekin_e>
  <ekin_ion> 0.00032482 </ekin_ion>
  <temp_ion> 17.09587060 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294462 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="379">
  <ekin>         5.22615431 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40651516 </eps>
  <enl>          4.76872568 </enl>
  <ecoul>      -15.59888844 </ecoul>
  <exc>         -4.36274228 </exc>
  <esr>          0.05440311 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37326587 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37326587 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69755137 0.00000000 -0.00000004 </position>
    <velocity> -0.00004966 -0.00000000 -0.00000000 </velocity>
    <force> -0.00426073 -0.00000001 -0.00000102 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37725798 0.00000005 </position>
    <velocity> 0.00000000 0.00006154 0.00000000 </velocity>
    <force> 0.00000004 -0.01277472 0.00000105 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69755137 -0.00000000 -0.00000004 </position>
    <velocity> 0.00004966 0.00000000 -0.00000000 </velocity>
    <force> 0.00426074 0.00000003 -0.00000110 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37725798 0.00000003 </position>
    <velocity> -0.00000000 -0.00006154 0.00000000 </velocity>
    <force> -0.00000004 0.01277471 0.00000120 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000053 </ekin_e>
  <ekin_ion> 0.00032018 </ekin_ion>
  <temp_ion> 16.85149732 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294463 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="380">
  <ekin>         5.22613469 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40651846 </eps>
  <enl>          4.76874194 </enl>
  <ecoul>      -15.59888857 </ecoul>
  <exc>         -4.36273092 </exc>
  <esr>          0.05440099 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37326132 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37326132 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69735073 0.00000000 -0.00000005 </position>
    <velocity> -0.00004999 -0.00000000 -0.00000000 </velocity>
    <force> -0.00423900 -0.00000001 -0.00000094 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37749816 0.00000006 </position>
    <velocity> 0.00000000 0.00006054 0.00000000 </velocity>
    <force> 0.00000003 -0.01279835 0.00000093 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69735073 -0.00000000 -0.00000004 </position>
    <velocity> 0.00004999 0.00000000 -0.00000000 </velocity>
    <force> 0.00423900 0.00000002 -0.00000104 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37749815 0.00000003 </position>
    <velocity> -0.00000000 -0.00006054 0.00000000 </velocity>
    <force> -0.00000003 0.01279833 0.00000116 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000053 </ekin_e>
  <ekin_ion> 0.00031563 </ekin_ion>
  <temp_ion> 16.61201485 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294464 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="381">
  <ekin>         5.22611864 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40652461 </eps>
  <enl>          4.76875918 </enl>
  <ecoul>      -15.59888905 </ecoul>
  <exc>         -4.36272102 </exc>
  <esr>          0.05439937 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325685 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325685 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69714877 0.00000000 -0.00000005 </position>
    <velocity> -0.00005032 -0.00000000 -0.00000000 </velocity>
    <force> -0.00421651 -0.00000000 -0.00000085 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37773432 0.00000006 </position>
    <velocity> 0.00000000 0.00005954 0.00000000 </velocity>
    <force> 0.00000003 -0.01282092 0.00000080 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69714877 -0.00000000 -0.00000005 </position>
    <velocity> 0.00005032 0.00000000 -0.00000000 </velocity>
    <force> 0.00421650 0.00000002 -0.00000098 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37773432 0.00000004 </position>
    <velocity> -0.00000000 -0.00005954 0.00000000 </velocity>
    <force> -0.00000002 0.01282091 0.00000112 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000052 </ekin_e>
  <ekin_ion> 0.00031117 </ekin_ion>
  <temp_ion> 16.37745727 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294465 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="382">
  <ekin>         5.22610625 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40653329 </eps>
  <enl>          4.76877699 </enl>
  <ecoul>      -15.59888985 </ecoul>
  <exc>         -4.36271259 </exc>
  <esr>          0.05439823 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325248 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325248 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69694550 0.00000000 -0.00000006 </position>
    <velocity> -0.00005065 -0.00000000 -0.00000000 </velocity>
    <force> -0.00419336 0.00000000 -0.00000076 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37796648 0.00000007 </position>
    <velocity> 0.00000000 0.00005854 0.00000000 </velocity>
    <force> 0.00000002 -0.01284270 0.00000067 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69694550 -0.00000000 -0.00000005 </position>
    <velocity> 0.00005065 0.00000000 -0.00000000 </velocity>
    <force> 0.00419335 0.00000001 -0.00000091 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37796648 0.00000004 </position>
    <velocity> -0.00000000 -0.00005854 0.00000000 </velocity>
    <force> -0.00000001 0.01284269 0.00000106 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000051 </ekin_e>
  <ekin_ion> 0.00030681 </ekin_ion>
  <temp_ion> 16.14785226 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294466 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="383">
  <ekin>         5.22609756 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40654405 </eps>
  <enl>          4.76879486 </enl>
  <ecoul>      -15.59889089 </ecoul>
  <exc>         -4.36270568 </exc>
  <esr>          0.05439758 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37324820 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37324820 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69674093 0.00000000 -0.00000006 </position>
    <velocity> -0.00005098 -0.00000000 -0.00000000 </velocity>
    <force> -0.00416974 0.00000001 -0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37819461 0.00000007 </position>
    <velocity> 0.00000000 0.00005754 0.00000000 </velocity>
    <force> 0.00000001 -0.01286397 0.00000054 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69674093 -0.00000000 -0.00000005 </position>
    <velocity> 0.00005098 0.00000000 -0.00000000 </velocity>
    <force> 0.00416973 0.00000000 -0.00000083 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37819461 0.00000005 </position>
    <velocity> -0.00000000 -0.00005754 0.00000000 </velocity>
    <force> 0.00000000 0.01286395 0.00000100 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000050 </ekin_e>
  <ekin_ion> 0.00030254 </ekin_ion>
  <temp_ion> 15.92322220 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294466 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="384">
  <ekin>         5.22609254 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40655648 </eps>
  <enl>          4.76881232 </enl>
  <ecoul>      -15.59889211 </ecoul>
  <exc>         -4.36270029 </exc>
  <esr>          0.05439743 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37324402 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37324402 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69653507 0.00000000 -0.00000007 </position>
    <velocity> -0.00005130 -0.00000000 -0.00000000 </velocity>
    <force> -0.00414584 0.00000001 -0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37841872 0.00000008 </position>
    <velocity> 0.00000000 0.00005653 0.00000000 </velocity>
    <force> -0.00000000 -0.01288494 0.00000040 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69653507 -0.00000000 -0.00000006 </position>
    <velocity> 0.00005130 0.00000000 -0.00000000 </velocity>
    <force> 0.00414582 -0.00000000 -0.00000074 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37841872 0.00000005 </position>
    <velocity> -0.00000000 -0.00005653 0.00000000 </velocity>
    <force> 0.00000002 0.01288493 0.00000093 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000049 </ekin_e>
  <ekin_ion> 0.00029837 </ekin_ion>
  <temp_ion> 15.70358613 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294467 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="385">
  <ekin>         5.22609114 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40657036 </eps>
  <enl>          4.76882918 </enl>
  <ecoul>      -15.59889347 </ecoul>
  <exc>         -4.36269642 </exc>
  <esr>          0.05439776 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37323993 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37323993 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69632791 0.00000000 -0.00000007 </position>
    <velocity> -0.00005163 -0.00000000 -0.00000000 </velocity>
    <force> -0.00412183 0.00000002 -0.00000046 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37863880 0.00000008 </position>
    <velocity> 0.00000000 0.00005552 0.00000000 </velocity>
    <force> -0.00000001 -0.01290577 0.00000027 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69632791 -0.00000000 -0.00000006 </position>
    <velocity> 0.00005163 0.00000000 -0.00000000 </velocity>
    <force> 0.00412180 -0.00000001 -0.00000064 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37863880 0.00000006 </position>
    <velocity> -0.00000000 -0.00005552 0.00000000 </velocity>
    <force> 0.00000003 0.01290576 0.00000085 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000048 </ekin_e>
  <ekin_ion> 0.00029429 </ekin_ion>
  <temp_ion> 15.48896188 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294468 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="386">
  <ekin>         5.22609328 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40658574 </eps>
  <enl>          4.76884558 </enl>
  <ecoul>      -15.59889501 </ecoul>
  <exc>         -4.36269405 </exc>
  <esr>          0.05439858 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37323594 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37323594 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69611948 0.00000000 -0.00000008 </position>
    <velocity> -0.00005195 -0.00000000 -0.00000000 </velocity>
    <force> -0.00409782 0.00000002 -0.00000035 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37885483 0.00000009 </position>
    <velocity> 0.00000000 0.00005451 0.00000000 </velocity>
    <force> -0.00000002 -0.01292652 0.00000014 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69611948 -0.00000000 -0.00000007 </position>
    <velocity> 0.00005195 0.00000000 -0.00000000 </velocity>
    <force> 0.00409779 -0.00000002 -0.00000053 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37885483 0.00000006 </position>
    <velocity> -0.00000000 -0.00005451 0.00000000 </velocity>
    <force> 0.00000004 0.01292651 0.00000076 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000047 </ekin_e>
  <ekin_ion> 0.00029031 </ekin_ion>
  <temp_ion> 15.27936773 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294469 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="387">
  <ekin>         5.22609887 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40660292 </eps>
  <enl>          4.76886196 </enl>
  <ecoul>      -15.59889679 </ecoul>
  <exc>         -4.36269316 </exc>
  <esr>          0.05439990 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37323204 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37323204 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69590977 0.00000000 -0.00000008 </position>
    <velocity> -0.00005227 -0.00000000 -0.00000000 </velocity>
    <force> -0.00407384 0.00000002 -0.00000024 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37906682 0.00000010 </position>
    <velocity> 0.00000000 0.00005350 0.00000000 </velocity>
    <force> -0.00000003 -0.01294714 0.00000001 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69590977 -0.00000000 -0.00000007 </position>
    <velocity> 0.00005227 0.00000000 -0.00000000 </velocity>
    <force> 0.00407380 -0.00000002 -0.00000042 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37906682 0.00000007 </position>
    <velocity> -0.00000000 -0.00005350 0.00000000 </velocity>
    <force> 0.00000005 0.01294714 0.00000067 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000046 </ekin_e>
  <ekin_ion> 0.00028642 </ekin_ion>
  <temp_ion> 15.07482315 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294470 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="388">
  <ekin>         5.22610786 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40662237 </eps>
  <enl>          4.76887892 </enl>
  <ecoul>      -15.59889892 </ecoul>
  <exc>         -4.36269373 </exc>
  <esr>          0.05440170 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37322824 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37322824 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69569879 0.00000000 -0.00000009 </position>
    <velocity> -0.00005259 -0.00000000 -0.00000000 </velocity>
    <force> -0.00404983 0.00000003 -0.00000013 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37927476 0.00000010 </position>
    <velocity> 0.00000000 0.00005249 0.00000000 </velocity>
    <force> -0.00000004 -0.01296755 -0.00000012 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69569879 -0.00000000 -0.00000008 </position>
    <velocity> 0.00005259 0.00000000 -0.00000000 </velocity>
    <force> 0.00404979 -0.00000003 -0.00000029 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37927476 0.00000007 </position>
    <velocity> -0.00000000 -0.00005249 0.00000000 </velocity>
    <force> 0.00000006 0.01296755 0.00000057 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000045 </ekin_e>
  <ekin_ion> 0.00028263 </ekin_ion>
  <temp_ion> 14.87534863 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294471 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="389">
  <ekin>         5.22612022 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40664450 </eps>
  <enl>          4.76889701 </enl>
  <ecoul>      -15.59890152 </ecoul>
  <exc>         -4.36269575 </exc>
  <esr>          0.05440399 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37322454 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37322454 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69548656 0.00000000 -0.00000009 </position>
    <velocity> -0.00005290 -0.00000000 -0.00000000 </velocity>
    <force> -0.00402569 0.00000003 -0.00000002 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37947863 0.00000011 </position>
    <velocity> 0.00000000 0.00005148 0.00000000 </velocity>
    <force> -0.00000005 -0.01298764 -0.00000024 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69548656 -0.00000000 -0.00000009 </position>
    <velocity> 0.00005290 0.00000000 -0.00000000 </velocity>
    <force> 0.00402565 -0.00000003 -0.00000017 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37947863 0.00000008 </position>
    <velocity> -0.00000000 -0.00005148 0.00000000 </velocity>
    <force> 0.00000007 0.01298764 0.00000046 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000044 </ekin_e>
  <ekin_ion> 0.00027894 </ekin_ion>
  <temp_ion> 14.68096483 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294472 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="390">
  <ekin>         5.22613603 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40666961 </eps>
  <enl>          4.76891650 </enl>
  <ecoul>      -15.59890464 </ecoul>
  <exc>         -4.36269922 </exc>
  <esr>          0.05440676 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37322094 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37322094 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69527308 0.00000000 -0.00000010 </position>
    <velocity> -0.00005321 -0.00000000 -0.00000000 </velocity>
    <force> -0.00400127 0.00000003 0.00000009 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37967845 0.00000011 </position>
    <velocity> 0.00000000 0.00005046 0.00000000 </velocity>
    <force> -0.00000005 -0.01300729 -0.00000036 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69527308 -0.00000000 -0.00000009 </position>
    <velocity> 0.00005321 0.00000000 -0.00000000 </velocity>
    <force> 0.00400123 -0.00000004 -0.00000005 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37967845 0.00000008 </position>
    <velocity> -0.00000000 -0.00005046 0.00000000 </velocity>
    <force> 0.00000007 0.01300730 0.00000034 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000044 </ekin_e>
  <ekin_ion> 0.00027534 </ekin_ion>
  <temp_ion> 14.49169150 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294473 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="391">
  <ekin>         5.22615536 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40669767 </eps>
  <enl>          4.76893734 </enl>
  <ecoul>      -15.59890829 </ecoul>
  <exc>         -4.36270417 </exc>
  <esr>          0.05441003 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321743 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321743 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69505835 0.00000000 -0.00000010 </position>
    <velocity> -0.00005353 -0.00000000 -0.00000000 </velocity>
    <force> -0.00397644 0.00000003 0.00000019 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37987419 0.00000012 </position>
    <velocity> 0.00000000 0.00004944 0.00000000 </velocity>
    <force> -0.00000006 -0.01302644 -0.00000047 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69505835 -0.00000000 -0.00000010 </position>
    <velocity> 0.00005353 0.00000000 -0.00000000 </velocity>
    <force> 0.00397640 -0.00000005 0.00000008 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37987419 0.00000009 </position>
    <velocity> -0.00000000 -0.00004944 0.00000000 </velocity>
    <force> 0.00000008 0.01302645 0.00000022 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000043 </ekin_e>
  <ekin_ion> 0.00027184 </ekin_ion>
  <temp_ion> 14.30754658 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294474 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="392">
  <ekin>         5.22617835 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40672843 </eps>
  <enl>          4.76895907 </enl>
  <ecoul>      -15.59891240 </ecoul>
  <exc>         -4.36271062 </exc>
  <esr>          0.05441379 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321402 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321402 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69484239 0.00000000 -0.00000011 </position>
    <velocity> -0.00005384 -0.00000000 -0.00000000 </velocity>
    <force> -0.00395113 0.00000004 0.00000030 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38006585 0.00000012 </position>
    <velocity> 0.00000000 0.00004843 0.00000000 </velocity>
    <force> -0.00000007 -0.01304504 -0.00000058 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69484239 -0.00000000 -0.00000010 </position>
    <velocity> 0.00005384 0.00000000 -0.00000000 </velocity>
    <force> 0.00395108 -0.00000005 0.00000020 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38006585 0.00000009 </position>
    <velocity> -0.00000000 -0.00004843 0.00000000 </velocity>
    <force> 0.00000009 0.01304505 0.00000009 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000042 </ekin_e>
  <ekin_ion> 0.00026844 </ekin_ion>
  <temp_ion> 14.12854593 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294474 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.011" max="    0.011"/>
<iteration count="393">
  <ekin>         5.22620513 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40676144 </eps>
  <enl>          4.76898107 </enl>
  <ecoul>      -15.59891685 </ecoul>
  <exc>         -4.36271863 </exc>
  <esr>          0.05441803 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321071 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321071 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69462521 0.00000000 -0.00000011 </position>
    <velocity> -0.00005414 -0.00000000 -0.00000000 </velocity>
    <force> -0.00392528 0.00000004 0.00000040 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38025343 0.00000013 </position>
    <velocity> 0.00000000 0.00004741 0.00000000 </velocity>
    <force> -0.00000007 -0.01306308 -0.00000067 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69462521 -0.00000000 -0.00000011 </position>
    <velocity> 0.00005414 0.00000000 -0.00000000 </velocity>
    <force> 0.00392524 -0.00000005 0.00000031 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38025343 0.00000010 </position>
    <velocity> -0.00000000 -0.00004741 0.00000000 </velocity>
    <force> 0.00000009 0.01306309 -0.00000004 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000041 </ekin_e>
  <ekin_ion> 0.00026514 </ekin_ion>
  <temp_ion> 13.95470354 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294475 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="394">
  <ekin>         5.22623577 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40679624 </eps>
  <enl>          4.76900272 </enl>
  <ecoul>      -15.59892154 </ecoul>
  <exc>         -4.36272821 </exc>
  <esr>          0.05442276 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320750 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320750 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69440680 0.00000000 -0.00000012 </position>
    <velocity> -0.00005445 -0.00000000 -0.00000000 </velocity>
    <force> -0.00389891 0.00000004 0.00000049 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38043693 0.00000013 </position>
    <velocity> 0.00000000 0.00004638 0.00000000 </velocity>
    <force> -0.00000007 -0.01308052 -0.00000077 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69440680 -0.00000000 -0.00000011 </position>
    <velocity> 0.00005445 0.00000000 -0.00000000 </velocity>
    <force> 0.00389887 -0.00000006 0.00000042 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38043693 0.00000011 </position>
    <velocity> -0.00000000 -0.00004638 0.00000000 </velocity>
    <force> 0.00000009 0.01308053 -0.00000017 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000041 </ekin_e>
  <ekin_ion> 0.00026193 </ekin_ion>
  <temp_ion> 13.78603227 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294476 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="395">
  <ekin>         5.22627029 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40683254 </eps>
  <enl>          4.76902359 </enl>
  <ecoul>      -15.59892634 </ecoul>
  <exc>         -4.36273939 </exc>
  <esr>          0.05442797 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320439 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320439 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69418719 0.00000000 -0.00000012 </position>
    <velocity> -0.00005475 -0.00000000 -0.00000000 </velocity>
    <force> -0.00387204 0.00000004 0.00000059 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38061633 0.00000014 </position>
    <velocity> 0.00000000 0.00004536 0.00000000 </velocity>
    <force> -0.00000008 -0.01309734 -0.00000085 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69418719 -0.00000000 -0.00000012 </position>
    <velocity> 0.00005475 0.00000000 -0.00000000 </velocity>
    <force> 0.00387200 -0.00000006 0.00000052 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38061633 0.00000011 </position>
    <velocity> -0.00000000 -0.00004536 0.00000000 </velocity>
    <force> 0.00000010 0.01309735 -0.00000030 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000040 </ekin_e>
  <ekin_ion> 0.00025883 </ekin_ion>
  <temp_ion> 13.62254465 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294476 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="396">
  <ekin>         5.22630861 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40687024 </eps>
  <enl>          4.76904362 </enl>
  <ecoul>      -15.59893120 </ecoul>
  <exc>         -4.36275217 </exc>
  <esr>          0.05443368 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320138 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320138 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69396637 0.00000000 -0.00000013 </position>
    <velocity> -0.00005505 0.00000000 -0.00000000 </velocity>
    <force> -0.00384468 0.00000004 0.00000068 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38079163 0.00000014 </position>
    <velocity> 0.00000000 0.00004434 0.00000000 </velocity>
    <force> -0.00000008 -0.01311347 -0.00000093 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69396637 -0.00000000 -0.00000012 </position>
    <velocity> 0.00005505 0.00000000 -0.00000000 </velocity>
    <force> 0.00384465 -0.00000006 0.00000062 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38079163 0.00000012 </position>
    <velocity> 0.00000000 -0.00004434 0.00000000 </velocity>
    <force> 0.00000009 0.01311349 -0.00000044 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000040 </ekin_e>
  <ekin_ion> 0.00025582 </ekin_ion>
  <temp_ion> 13.46425343 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294477 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="397">
  <ekin>         5.22635062 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40690952 </eps>
  <enl>          4.76906308 </enl>
  <ecoul>      -15.59893613 </ecoul>
  <exc>         -4.36276651 </exc>
  <esr>          0.05443986 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319847 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319847 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69374436 0.00000000 -0.00000013 </position>
    <velocity> -0.00005535 0.00000000 -0.00000000 </velocity>
    <force> -0.00381687 0.00000004 0.00000077 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38096283 0.00000015 </position>
    <velocity> -0.00000000 0.00004331 0.00000000 </velocity>
    <force> -0.00000008 -0.01312885 -0.00000100 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69374436 -0.00000000 -0.00000013 </position>
    <velocity> 0.00005535 -0.00000000 -0.00000000 </velocity>
    <force> 0.00381683 -0.00000006 0.00000071 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38096283 0.00000012 </position>
    <velocity> 0.00000000 -0.00004331 0.00000000 </velocity>
    <force> 0.00000009 0.01312887 -0.00000057 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000039 </ekin_e>
  <ekin_ion> 0.00025291 </ekin_ion>
  <temp_ion> 13.31117179 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294477 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="398">
  <ekin>         5.22639616 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40695073 </eps>
  <enl>          4.76908246 </enl>
  <ecoul>      -15.59894118 </ecoul>
  <exc>         -4.36278237 </exc>
  <esr>          0.05444654 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319565 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319565 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69352117 0.00000000 -0.00000014 </position>
    <velocity> -0.00005565 0.00000000 -0.00000000 </velocity>
    <force> -0.00378859 0.00000004 0.00000085 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38112992 0.00000015 </position>
    <velocity> -0.00000000 0.00004229 0.00000000 </velocity>
    <force> -0.00000008 -0.01314339 -0.00000106 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69352116 -0.00000000 -0.00000013 </position>
    <velocity> 0.00005565 -0.00000000 -0.00000000 </velocity>
    <force> 0.00378856 -0.00000006 0.00000081 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38112992 0.00000013 </position>
    <velocity> 0.00000000 -0.00004229 0.00000000 </velocity>
    <force> 0.00000009 0.01314340 -0.00000070 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000039 </ekin_e>
  <ekin_ion> 0.00025010 </ekin_ion>
  <temp_ion> 13.16331309 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294477 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="399">
  <ekin>         5.22644508 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40699421 </eps>
  <enl>          4.76910229 </enl>
  <ecoul>      -15.59894639 </ecoul>
  <exc>         -4.36279971 </exc>
  <esr>          0.05445370 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319294 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319294 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69329680 0.00000000 -0.00000014 </position>
    <velocity> -0.00005595 0.00000000 -0.00000000 </velocity>
    <force> -0.00375984 0.00000003 0.00000093 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38129290 0.00000015 </position>
    <velocity> -0.00000000 0.00004126 0.00000000 </velocity>
    <force> -0.00000008 -0.01315702 -0.00000111 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69329680 -0.00000000 -0.00000014 </position>
    <velocity> 0.00005595 -0.00000000 -0.00000000 </velocity>
    <force> 0.00375981 -0.00000006 0.00000090 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38129290 0.00000013 </position>
    <velocity> 0.00000000 -0.00004126 0.00000000 </velocity>
    <force> 0.00000008 0.01315704 -0.00000083 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000039 </ekin_e>
  <ekin_ion> 0.00024739 </ekin_ion>
  <temp_ion> 13.02069033 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="400">
  <ekin>         5.22649729 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40704021 </eps>
  <enl>          4.76912291 </enl>
  <ecoul>      -15.59895185 </ecoul>
  <exc>         -4.36281848 </exc>
  <esr>          0.05446134 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319033 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319033 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69307126 0.00000000 -0.00000014 </position>
    <velocity> -0.00005624 0.00000000 -0.00000000 </velocity>
    <force> -0.00373063 0.00000003 0.00000101 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38145176 0.00000016 </position>
    <velocity> -0.00000000 0.00004023 0.00000000 </velocity>
    <force> -0.00000007 -0.01316974 -0.00000116 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69307126 -0.00000000 -0.00000014 </position>
    <velocity> 0.00005624 -0.00000000 -0.00000000 </velocity>
    <force> 0.00373061 -0.00000005 0.00000098 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38145177 0.00000014 </position>
    <velocity> 0.00000000 -0.00004023 0.00000000 </velocity>
    <force> 0.00000008 0.01316976 -0.00000095 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00024478 </ekin_ion>
  <temp_ion> 12.88331561 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="401">
  <ekin>         5.22655274 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40708878 </eps>
  <enl>          4.76914442 </enl>
  <ecoul>      -15.59895756 </ecoul>
  <exc>         -4.36283864 </exc>
  <esr>          0.05446947 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318781 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318781 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69284457 0.00000000 -0.00000015 </position>
    <velocity> -0.00005653 0.00000000 -0.00000000 </velocity>
    <force> -0.00370099 0.00000003 0.00000107 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38160651 0.00000016 </position>
    <velocity> -0.00000000 0.00003920 0.00000000 </velocity>
    <force> -0.00000007 -0.01318158 -0.00000119 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69284457 -0.00000000 -0.00000014 </position>
    <velocity> 0.00005653 -0.00000000 -0.00000000 </velocity>
    <force> 0.00370098 -0.00000005 0.00000107 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38160651 0.00000014 </position>
    <velocity> 0.00000000 -0.00003920 0.00000000 </velocity>
    <force> 0.00000007 0.01318160 -0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00024227 </ekin_ion>
  <temp_ion> 12.75119964 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="402">
  <ekin>         5.22661144 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40713974 </eps>
  <enl>          4.76916660 </enl>
  <ecoul>      -15.59896353 </ecoul>
  <exc>         -4.36286017 </exc>
  <esr>          0.05447809 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318540 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318540 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69261673 0.00000000 -0.00000015 </position>
    <velocity> -0.00005682 0.00000000 -0.00000000 </velocity>
    <force> -0.00367100 0.00000003 0.00000113 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38175713 0.00000016 </position>
    <velocity> -0.00000000 0.00003817 0.00000000 </velocity>
    <force> -0.00000007 -0.01319263 -0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69261673 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005682 -0.00000000 -0.00000000 </velocity>
    <force> 0.00367100 -0.00000004 0.00000114 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38175713 0.00000015 </position>
    <velocity> 0.00000000 -0.00003817 0.00000000 </velocity>
    <force> 0.00000006 0.01319264 -0.00000118 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00023986 </ekin_ion>
  <temp_ion> 12.62435170 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="403">
  <ekin>         5.22667344 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40719281 </eps>
  <enl>          4.76918908 </enl>
  <ecoul>      -15.59896971 </ecoul>
  <exc>         -4.36288309 </exc>
  <esr>          0.05448718 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318309 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318309 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69238776 0.00000000 -0.00000015 </position>
    <velocity> -0.00005710 0.00000000 -0.00000000 </velocity>
    <force> -0.00364074 0.00000002 0.00000118 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38190363 0.00000016 </position>
    <velocity> -0.00000000 0.00003714 0.00000000 </velocity>
    <force> -0.00000006 -0.01320301 -0.00000123 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69238776 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005710 -0.00000000 -0.00000000 </velocity>
    <force> 0.00364074 -0.00000004 0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38190363 0.00000015 </position>
    <velocity> 0.00000000 -0.00003714 0.00000000 </velocity>
    <force> 0.00000005 0.01320302 -0.00000129 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00023755 </ekin_ion>
  <temp_ion> 12.50277976 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="404">
  <ekin>         5.22673878 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40724766 </eps>
  <enl>          4.76921145 </enl>
  <ecoul>      -15.59897605 </ecoul>
  <exc>         -4.36290740 </exc>
  <esr>          0.05449676 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318088 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318088 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69215765 0.00000000 -0.00000015 </position>
    <velocity> -0.00005739 0.00000000 -0.00000000 </velocity>
    <force> -0.00361031 0.00000002 0.00000123 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38204599 0.00000016 </position>
    <velocity> -0.00000000 0.00003611 0.00000000 </velocity>
    <force> -0.00000005 -0.01321284 -0.00000124 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69215765 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005739 -0.00000000 -0.00000000 </velocity>
    <force> 0.00361031 -0.00000003 0.00000128 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38204599 0.00000015 </position>
    <velocity> 0.00000000 -0.00003611 0.00000000 </velocity>
    <force> 0.00000005 0.01321285 -0.00000139 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00023534 </ekin_ion>
  <temp_ion> 12.38649073 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="405">
  <ekin>         5.22680752 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40730408 </eps>
  <enl>          4.76923344 </enl>
  <ecoul>      -15.59898252 </ecoul>
  <exc>         -4.36293313 </exc>
  <esr>          0.05450682 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317877 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317877 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69192643 0.00000000 -0.00000015 </position>
    <velocity> -0.00005767 0.00000000 -0.00000000 </velocity>
    <force> -0.00357978 0.00000002 0.00000126 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38218423 0.00000017 </position>
    <velocity> -0.00000000 0.00003508 0.00000000 </velocity>
    <force> -0.00000005 -0.01322225 -0.00000125 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69192643 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005767 -0.00000000 -0.00000000 </velocity>
    <force> 0.00357979 -0.00000003 0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38218423 0.00000016 </position>
    <velocity> 0.00000000 -0.00003508 0.00000000 </velocity>
    <force> 0.00000004 0.01322226 -0.00000147 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00023323 </ekin_ion>
  <temp_ion> 12.27549078 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.009"/>
<iteration count="406">
  <ekin>         5.22687968 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40736204 </eps>
  <enl>          4.76925502 </enl>
  <ecoul>      -15.59898912 </ecoul>
  <exc>         -4.36296030 </exc>
  <esr>          0.05451737 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317676 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317676 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69169409 0.00000000 -0.00000016 </position>
    <velocity> -0.00005794 0.00000000 -0.00000000 </velocity>
    <force> -0.00354920 0.00000001 0.00000129 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38231833 0.00000017 </position>
    <velocity> -0.00000000 0.00003404 0.00000000 </velocity>
    <force> -0.00000004 -0.01323131 -0.00000124 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69169409 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005794 -0.00000000 -0.00000000 </velocity>
    <force> 0.00354921 -0.00000002 0.00000137 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38231833 0.00000016 </position>
    <velocity> 0.00000000 -0.00003404 0.00000000 </velocity>
    <force> 0.00000002 0.01323132 -0.00000155 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00023123 </ekin_ion>
  <temp_ion> 12.16978540 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="407">
  <ekin>         5.22695530 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40742167 </eps>
  <enl>          4.76927637 </enl>
  <ecoul>      -15.59899588 </ecoul>
  <exc>         -4.36298896 </exc>
  <esr>          0.05452839 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317485 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317485 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69146066 0.00000000 -0.00000016 </position>
    <velocity> -0.00005822 0.00000000 -0.00000000 </velocity>
    <force> -0.00351856 0.00000001 0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38244829 0.00000017 </position>
    <velocity> -0.00000000 0.00003301 0.00000000 </velocity>
    <force> -0.00000003 -0.01324005 -0.00000123 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69146066 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005822 -0.00000000 -0.00000000 </velocity>
    <force> 0.00351858 -0.00000001 0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38244829 0.00000016 </position>
    <velocity> 0.00000000 -0.00003301 0.00000000 </velocity>
    <force> 0.00000001 0.01324005 -0.00000161 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00022932 </ekin_ion>
  <temp_ion> 12.06937929 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="408">
  <ekin>         5.22703438 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40748324 </eps>
  <enl>          4.76929778 </enl>
  <ecoul>      -15.59900287 </ecoul>
  <exc>         -4.36301911 </exc>
  <esr>          0.05453990 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317304 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317304 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69122614 0.00000000 -0.00000016 </position>
    <velocity> -0.00005849 0.00000000 -0.00000000 </velocity>
    <force> -0.00348783 0.00000000 0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38257411 0.00000017 </position>
    <velocity> -0.00000000 0.00003197 0.00000000 </velocity>
    <force> -0.00000002 -0.01324845 -0.00000121 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69122614 -0.00000000 -0.00000016 </position>
    <velocity> 0.00005849 -0.00000000 -0.00000000 </velocity>
    <force> 0.00348786 -0.00000000 0.00000142 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38257411 0.00000016 </position>
    <velocity> 0.00000000 -0.00003197 0.00000000 </velocity>
    <force> 0.00000000 0.01324845 -0.00000166 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00022751 </ekin_ion>
  <temp_ion> 11.97427601 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="409">
  <ekin>         5.22711696 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40754702 </eps>
  <enl>          4.76931960 </enl>
  <ecoul>      -15.59901013 </ecoul>
  <exc>         -4.36305075 </exc>
  <esr>          0.05455188 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317134 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317134 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69099054 0.00000000 -0.00000016 </position>
    <velocity> -0.00005877 0.00000000 -0.00000000 </velocity>
    <force> -0.00345693 -0.00000000 0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38269579 0.00000017 </position>
    <velocity> -0.00000000 0.00003094 -0.00000000 </velocity>
    <force> -0.00000001 -0.01325646 -0.00000119 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69099054 -0.00000000 -0.00000016 </position>
    <velocity> 0.00005877 -0.00000000 -0.00000000 </velocity>
    <force> 0.00345696 0.00000000 0.00000143 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38269579 0.00000016 </position>
    <velocity> 0.00000000 -0.00003094 0.00000000 </velocity>
    <force> -0.00000001 0.01325646 -0.00000169 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00022580 </ekin_ion>
  <temp_ion> 11.88447761 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="410">
  <ekin>         5.22720305 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40761321 </eps>
  <enl>          4.76934201 </enl>
  <ecoul>      -15.59901771 </ecoul>
  <exc>         -4.36308388 </exc>
  <esr>          0.05456435 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316973 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316973 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69075386 0.00000000 -0.00000016 </position>
    <velocity> -0.00005903 0.00000000 0.00000000 </velocity>
    <force> -0.00342577 -0.00000000 0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38281332 0.00000016 </position>
    <velocity> -0.00000000 0.00002990 -0.00000000 </velocity>
    <force> -0.00000000 -0.01326401 -0.00000116 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69075386 -0.00000000 -0.00000016 </position>
    <velocity> 0.00005903 -0.00000000 0.00000000 </velocity>
    <force> 0.00342580 0.00000001 0.00000143 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38281332 0.00000016 </position>
    <velocity> 0.00000000 -0.00002990 0.00000000 </velocity>
    <force> -0.00000002 0.01326401 -0.00000171 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00022420 </ekin_ion>
  <temp_ion> 11.79998419 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="411">
  <ekin>         5.22729269 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40768184 </eps>
  <enl>          4.76936501 </enl>
  <ecoul>      -15.59902561 </ecoul>
  <exc>         -4.36311848 </exc>
  <esr>          0.05457729 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316823 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316823 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69051613 0.00000000 -0.00000016 </position>
    <velocity> -0.00005930 0.00000000 0.00000000 </velocity>
    <force> -0.00339425 -0.00000001 0.00000129 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38292670 0.00000016 </position>
    <velocity> -0.00000000 0.00002886 -0.00000000 </velocity>
    <force> 0.00000001 -0.01327103 -0.00000112 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69051613 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005930 -0.00000000 0.00000000 </velocity>
    <force> 0.00339429 0.00000002 0.00000142 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38292670 0.00000016 </position>
    <velocity> 0.00000000 -0.00002886 -0.00000000 </velocity>
    <force> -0.00000003 0.01327103 -0.00000172 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00022269 </ekin_ion>
  <temp_ion> 11.72079377 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="412">
  <ekin>         5.22738585 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40775279 </eps>
  <enl>          4.76938841 </enl>
  <ecoul>      -15.59903378 </ecoul>
  <exc>         -4.36315452 </exc>
  <esr>          0.05459071 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316682 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316682 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69027735 0.00000000 -0.00000015 </position>
    <velocity> -0.00005956 0.00000000 0.00000000 </velocity>
    <force> -0.00336231 -0.00000001 0.00000127 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38303594 0.00000016 </position>
    <velocity> -0.00000000 0.00002783 -0.00000000 </velocity>
    <force> 0.00000002 -0.01327745 -0.00000108 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69027735 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005956 -0.00000000 0.00000000 </velocity>
    <force> 0.00336235 0.00000002 0.00000139 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38303594 0.00000016 </position>
    <velocity> 0.00000000 -0.00002783 -0.00000000 </velocity>
    <force> -0.00000004 0.01327744 -0.00000172 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00022129 </ekin_ion>
  <temp_ion> 11.64690223 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="413">
  <ekin>         5.22748248 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40782580 </eps>
  <enl>          4.76941188 </enl>
  <ecoul>      -15.59904213 </ecoul>
  <exc>         -4.36319195 </exc>
  <esr>          0.05460461 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316552 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316552 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.69003752 0.00000000 -0.00000015 </position>
    <velocity> -0.00005983 0.00000000 0.00000000 </velocity>
    <force> -0.00332990 -0.00000001 0.00000124 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38314103 0.00000016 </position>
    <velocity> -0.00000000 0.00002679 -0.00000000 </velocity>
    <force> 0.00000003 -0.01328320 -0.00000104 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.69003752 -0.00000000 -0.00000015 </position>
    <velocity> 0.00005983 -0.00000000 0.00000000 </velocity>
    <force> 0.00332994 0.00000003 0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38314102 0.00000016 </position>
    <velocity> 0.00000000 -0.00002679 -0.00000000 </velocity>
    <force> -0.00000005 0.01328319 -0.00000170 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00021999 </ekin_ion>
  <temp_ion> 11.57830358 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="414">
  <ekin>         5.22758248 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40790056 </eps>
  <enl>          4.76943506 </enl>
  <ecoul>      -15.59905054 </ecoul>
  <exc>         -4.36323075 </exc>
  <esr>          0.05461899 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316432 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316432 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68979666 0.00000000 -0.00000015 </position>
    <velocity> -0.00006009 0.00000000 0.00000000 </velocity>
    <force> -0.00329698 -0.00000002 0.00000120 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38324196 0.00000016 </position>
    <velocity> -0.00000000 0.00002575 -0.00000000 </velocity>
    <force> 0.00000004 -0.01328822 -0.00000099 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68979666 -0.00000000 -0.00000015 </position>
    <velocity> 0.00006009 -0.00000000 0.00000000 </velocity>
    <force> 0.00329702 0.00000003 0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38324196 0.00000016 </position>
    <velocity> 0.00000000 -0.00002575 -0.00000000 </velocity>
    <force> -0.00000006 0.01328821 -0.00000167 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00021878 </ekin_ion>
  <temp_ion> 11.51499032 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="415">
  <ekin>         5.22768571 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40797677 </eps>
  <enl>          4.76945764 </enl>
  <ecoul>      -15.59905891 </ecoul>
  <exc>         -4.36327088 </exc>
  <esr>          0.05463384 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316322 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316322 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68955479 0.00000000 -0.00000015 </position>
    <velocity> -0.00006034 0.00000000 0.00000000 </velocity>
    <force> -0.00326354 -0.00000002 0.00000115 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38333873 0.00000015 </position>
    <velocity> -0.00000000 0.00002471 -0.00000000 </velocity>
    <force> 0.00000005 -0.01329244 -0.00000094 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68955479 -0.00000000 -0.00000015 </position>
    <velocity> 0.00006034 -0.00000000 0.00000000 </velocity>
    <force> 0.00326358 0.00000004 0.00000127 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38333873 0.00000015 </position>
    <velocity> 0.00000000 -0.00002471 -0.00000000 </velocity>
    <force> -0.00000007 0.01329243 -0.00000162 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00021768 </ekin_ion>
  <temp_ion> 11.45695383 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="416">
  <ekin>         5.22779201 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40805426 </eps>
  <enl>          4.76947948 </enl>
  <ecoul>      -15.59906714 </ecoul>
  <exc>         -4.36331230 </exc>
  <esr>          0.05464917 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316221 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316221 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68931190 0.00000000 -0.00000015 </position>
    <velocity> -0.00006060 0.00000000 0.00000000 </velocity>
    <force> -0.00322960 -0.00000002 0.00000110 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38343136 0.00000015 </position>
    <velocity> -0.00000000 0.00002367 -0.00000000 </velocity>
    <force> 0.00000006 -0.01329581 -0.00000088 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68931190 -0.00000000 -0.00000014 </position>
    <velocity> 0.00006060 -0.00000000 0.00000000 </velocity>
    <force> 0.00322965 0.00000004 0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38343136 0.00000015 </position>
    <velocity> 0.00000000 -0.00002367 -0.00000000 </velocity>
    <force> -0.00000007 0.01329580 -0.00000156 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00021668 </ekin_ion>
  <temp_ion> 11.40418469 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="417">
  <ekin>         5.22790128 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40813297 </eps>
  <enl>          4.76950064 </enl>
  <ecoul>      -15.59907523 </ecoul>
  <exc>         -4.36335503 </exc>
  <esr>          0.05466498 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316131 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316131 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68906802 0.00000000 -0.00000014 </position>
    <velocity> -0.00006085 0.00000000 0.00000000 </velocity>
    <force> -0.00319519 -0.00000003 0.00000104 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38351982 0.00000015 </position>
    <velocity> -0.00000000 0.00002264 -0.00000000 </velocity>
    <force> 0.00000006 -0.01329829 -0.00000082 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68906802 -0.00000000 -0.00000014 </position>
    <velocity> 0.00006085 -0.00000000 0.00000000 </velocity>
    <force> 0.00319523 0.00000005 0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38351982 0.00000015 </position>
    <velocity> 0.00000000 -0.00002264 -0.00000000 </velocity>
    <force> -0.00000008 0.01329827 -0.00000149 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00021578 </ekin_ion>
  <temp_ion> 11.35667290 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="418">
  <ekin>         5.22801346 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40821305 </eps>
  <enl>          4.76952135 </enl>
  <ecoul>      -15.59908321 </ecoul>
  <exc>         -4.36339906 </exc>
  <esr>          0.05468126 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316051 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316051 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68882315 0.00000000 -0.00000014 </position>
    <velocity> -0.00006109 0.00000000 0.00000000 </velocity>
    <force> -0.00316034 -0.00000003 0.00000098 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38360413 0.00000015 </position>
    <velocity> -0.00000000 0.00002160 -0.00000000 </velocity>
    <force> 0.00000007 -0.01329987 -0.00000076 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68882315 -0.00000000 -0.00000014 </position>
    <velocity> 0.00006109 -0.00000000 0.00000000 </velocity>
    <force> 0.00316038 0.00000005 0.00000108 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38360413 0.00000014 </position>
    <velocity> 0.00000000 -0.00002160 -0.00000000 </velocity>
    <force> -0.00000008 0.01329985 -0.00000140 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000037 </ekin_e>
  <ekin_ion> 0.00021497 </ekin_ion>
  <temp_ion> 11.31440781 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="419">
  <ekin>         5.22812862 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40829478 </eps>
  <enl>          4.76954201 </enl>
  <ecoul>      -15.59909120 </ecoul>
  <exc>         -4.36344445 </exc>
  <esr>          0.05469801 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315981 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315981 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68857730 0.00000000 -0.00000014 </position>
    <velocity> -0.00006134 0.00000000 0.00000000 </velocity>
    <force> -0.00312509 -0.00000003 0.00000091 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38368429 0.00000014 </position>
    <velocity> -0.00000000 0.00002056 -0.00000000 </velocity>
    <force> 0.00000007 -0.01330059 -0.00000069 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68857730 -0.00000000 -0.00000013 </position>
    <velocity> 0.00006134 -0.00000000 0.00000000 </velocity>
    <force> 0.00312513 0.00000005 0.00000100 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38368429 0.00000014 </position>
    <velocity> 0.00000000 -0.00002056 -0.00000000 </velocity>
    <force> -0.00000008 0.01330058 -0.00000131 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00021427 </ekin_ion>
  <temp_ion> 11.27737798 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294479 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.006"/>
<iteration count="420">
  <ekin>         5.22824691 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40837857 </eps>
  <enl>          4.76956310 </enl>
  <ecoul>      -15.59909940 </ecoul>
  <exc>         -4.36349125 </exc>
  <esr>          0.05471524 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315921 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315921 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68833049 0.00000000 -0.00000013 </position>
    <velocity> -0.00006158 0.00000000 0.00000000 </velocity>
    <force> -0.00308949 -0.00000003 0.00000083 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38376028 0.00000014 </position>
    <velocity> -0.00000000 0.00001952 -0.00000000 </velocity>
    <force> 0.00000008 -0.01330058 -0.00000062 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68833049 -0.00000000 -0.00000013 </position>
    <velocity> 0.00006158 -0.00000000 0.00000000 </velocity>
    <force> 0.00308953 0.00000006 0.00000091 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38376028 0.00000013 </position>
    <velocity> 0.00000000 -0.00001952 -0.00000000 </velocity>
    <force> -0.00000009 0.01330056 -0.00000119 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00021367 </ekin_ion>
  <temp_ion> 11.24557090 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="421">
  <ekin>         5.22836856 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40846487 </eps>
  <enl>          4.76958513 </enl>
  <ecoul>      -15.59910800 </ecoul>
  <exc>         -4.36353953 </exc>
  <esr>          0.05473294 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315870 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315870 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68808272 0.00000000 -0.00000013 </position>
    <velocity> -0.00006182 0.00000000 0.00000000 </velocity>
    <force> -0.00305359 -0.00000004 0.00000075 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38383212 0.00000013 </position>
    <velocity> -0.00000000 0.00001848 -0.00000000 </velocity>
    <force> 0.00000008 -0.01329997 -0.00000056 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68808272 -0.00000000 -0.00000013 </position>
    <velocity> 0.00006182 -0.00000000 0.00000000 </velocity>
    <force> 0.00305362 0.00000006 0.00000081 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38383212 0.00000013 </position>
    <velocity> 0.00000000 -0.00001848 -0.00000000 </velocity>
    <force> -0.00000009 0.01329995 -0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00021316 </ekin_ion>
  <temp_ion> 11.21897280 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="422">
  <ekin>         5.22849383 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40855409 </eps>
  <enl>          4.76960853 </enl>
  <ecoul>      -15.59911722 </ecoul>
  <exc>         -4.36358935 </exc>
  <esr>          0.05475111 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315830 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315830 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68783401 0.00000000 -0.00000012 </position>
    <velocity> -0.00006206 0.00000000 0.00000000 </velocity>
    <force> -0.00301742 -0.00000004 0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38389981 0.00000013 </position>
    <velocity> -0.00000000 0.00001744 -0.00000000 </velocity>
    <force> 0.00000009 -0.01329896 -0.00000049 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68783401 -0.00000000 -0.00000012 </position>
    <velocity> 0.00006206 0.00000000 0.00000000 </velocity>
    <force> 0.00301745 0.00000006 0.00000071 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38389981 0.00000012 </position>
    <velocity> -0.00000000 -0.00001744 -0.00000000 </velocity>
    <force> -0.00000009 0.01329894 -0.00000094 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000038 </ekin_e>
  <ekin_ion> 0.00021275 </ekin_ion>
  <temp_ion> 11.19756869 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="423">
  <ekin>         5.22862297 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40864654 </eps>
  <enl>          4.76963357 </enl>
  <ecoul>      -15.59912722 </ecoul>
  <exc>         -4.36364078 </exc>
  <esr>          0.05476975 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315799 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315799 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68758437 0.00000000 -0.00000012 </position>
    <velocity> -0.00006229 0.00000000 0.00000000 </velocity>
    <force> -0.00298104 -0.00000004 0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38396333 0.00000013 </position>
    <velocity> 0.00000000 0.00001640 -0.00000000 </velocity>
    <force> 0.00000009 -0.01329774 -0.00000042 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68758437 -0.00000000 -0.00000012 </position>
    <velocity> 0.00006229 0.00000000 0.00000000 </velocity>
    <force> 0.00298106 0.00000005 0.00000060 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38396333 0.00000012 </position>
    <velocity> -0.00000000 -0.00001640 -0.00000000 </velocity>
    <force> -0.00000008 0.01329773 -0.00000080 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000039 </ekin_e>
  <ekin_ion> 0.00021244 </ekin_ion>
  <temp_ion> 11.18134254 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294478 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="424">
  <ekin>         5.22875616 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40874236 </eps>
  <enl>          4.76966034 </enl>
  <ecoul>      -15.59913808 </ecoul>
  <exc>         -4.36369384 </exc>
  <esr>          0.05478886 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315779 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315779 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68733380 0.00000000 -0.00000011 </position>
    <velocity> -0.00006253 -0.00000000 0.00000000 </velocity>
    <force> -0.00294448 -0.00000004 0.00000047 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38402271 0.00000012 </position>
    <velocity> 0.00000000 0.00001536 -0.00000000 </velocity>
    <force> 0.00000009 -0.01329646 -0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68733380 -0.00000000 -0.00000011 </position>
    <velocity> 0.00006253 0.00000000 0.00000000 </velocity>
    <force> 0.00294450 0.00000005 0.00000049 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38402271 0.00000011 </position>
    <velocity> -0.00000000 -0.00001536 -0.00000000 </velocity>
    <force> -0.00000008 0.01329644 -0.00000065 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000039 </ekin_e>
  <ekin_ion> 0.00021223 </ekin_ion>
  <temp_ion> 11.17027786 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294477 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="425">
  <ekin>         5.22889348 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40884145 </eps>
  <enl>          4.76968864 </enl>
  <ecoul>      -15.59914981 </ecoul>
  <exc>         -4.36374854 </exc>
  <esr>          0.05480844 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315768 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315768 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68708233 0.00000000 -0.00000011 </position>
    <velocity> -0.00006275 -0.00000000 0.00000000 </velocity>
    <force> -0.00290777 -0.00000004 0.00000036 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38407792 0.00000012 </position>
    <velocity> 0.00000000 0.00001432 -0.00000000 </velocity>
    <force> 0.00000009 -0.01329517 -0.00000028 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68708233 -0.00000000 -0.00000011 </position>
    <velocity> 0.00006275 0.00000000 0.00000000 </velocity>
    <force> 0.00290778 0.00000005 0.00000038 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38407792 0.00000010 </position>
    <velocity> -0.00000000 -0.00001432 -0.00000000 </velocity>
    <force> -0.00000008 0.01329516 -0.00000050 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000039 </ekin_e>
  <ekin_ion> 0.00021212 </ekin_ion>
  <temp_ion> 11.16435818 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294477 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="426">
  <ekin>         5.22903490 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40894350 </eps>
  <enl>          4.76971808 </enl>
  <ecoul>      -15.59916229 </ecoul>
  <exc>         -4.36380485 </exc>
  <esr>          0.05482849 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315767 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315767 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68682996 0.00000000 -0.00000010 </position>
    <velocity> -0.00006298 -0.00000000 0.00000000 </velocity>
    <force> -0.00287093 -0.00000004 0.00000026 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38412899 0.00000011 </position>
    <velocity> 0.00000000 0.00001329 -0.00000000 </velocity>
    <force> 0.00000008 -0.01329386 -0.00000021 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68682996 -0.00000000 -0.00000010 </position>
    <velocity> 0.00006298 0.00000000 0.00000000 </velocity>
    <force> 0.00287093 0.00000005 0.00000027 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38412899 0.00000010 </position>
    <velocity> -0.00000000 -0.00001329 -0.00000000 </velocity>
    <force> -0.00000007 0.01329385 -0.00000035 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000040 </ekin_e>
  <ekin_ion> 0.00021211 </ekin_ion>
  <temp_ion> 11.16356756 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294477 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="427">
  <ekin>         5.22918028 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40904804 </eps>
  <enl>          4.76974808 </enl>
  <ecoul>      -15.59917536 </ecoul>
  <exc>         -4.36386272 </exc>
  <esr>          0.05484901 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315775 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315775 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68657671 0.00000000 -0.00000010 </position>
    <velocity> -0.00006320 -0.00000000 0.00000000 </velocity>
    <force> -0.00283394 -0.00000004 0.00000015 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38417590 0.00000011 </position>
    <velocity> 0.00000000 0.00001225 -0.00000000 </velocity>
    <force> 0.00000008 -0.01329237 -0.00000014 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68657671 -0.00000000 -0.00000010 </position>
    <velocity> 0.00006320 0.00000000 0.00000000 </velocity>
    <force> 0.00283394 0.00000004 0.00000015 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38417590 0.00000009 </position>
    <velocity> -0.00000000 -0.00001225 -0.00000000 </velocity>
    <force> -0.00000007 0.01329236 -0.00000019 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000040 </ekin_e>
  <ekin_ion> 0.00021219 </ekin_ion>
  <temp_ion> 11.16789060 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294476 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="428">
  <ekin>         5.22932939 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40915453 </eps>
  <enl>          4.76977804 </enl>
  <ecoul>      -15.59918879 </ecoul>
  <exc>         -4.36392204 </exc>
  <esr>          0.05486999 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315794 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315794 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68632258 0.00000000 -0.00000009 </position>
    <velocity> -0.00006342 -0.00000000 0.00000000 </velocity>
    <force> -0.00279676 -0.00000003 0.00000005 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38421865 0.00000010 </position>
    <velocity> 0.00000000 0.00001121 -0.00000000 </velocity>
    <force> 0.00000007 -0.01329049 -0.00000007 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68632258 -0.00000000 -0.00000009 </position>
    <velocity> 0.00006342 0.00000000 0.00000000 </velocity>
    <force> 0.00279675 0.00000004 0.00000004 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38421865 0.00000009 </position>
    <velocity> -0.00000000 -0.00001121 -0.00000000 </velocity>
    <force> -0.00000006 0.01329049 -0.00000003 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000041 </ekin_e>
  <ekin_ion> 0.00021237 </ekin_ion>
  <temp_ion> 11.17731196 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294476 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="429">
  <ekin>         5.22948193 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40926250 </eps>
  <enl>          4.76980744 </enl>
  <ecoul>      -15.59920233 </ecoul>
  <exc>         -4.36398275 </exc>
  <esr>          0.05489144 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315822 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315822 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68606759 0.00000000 -0.00000009 </position>
    <velocity> -0.00006364 -0.00000000 0.00000000 </velocity>
    <force> -0.00275933 -0.00000003 -0.00000006 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38425725 0.00000010 </position>
    <velocity> 0.00000000 0.00001017 -0.00000000 </velocity>
    <force> 0.00000007 -0.01328798 0.00000001 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68606759 -0.00000000 -0.00000009 </position>
    <velocity> 0.00006364 0.00000000 0.00000000 </velocity>
    <force> 0.00275932 0.00000003 -0.00000008 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38425725 0.00000008 </position>
    <velocity> -0.00000000 -0.00001017 -0.00000000 </velocity>
    <force> -0.00000005 0.01328798 0.00000013 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000041 </ekin_e>
  <ekin_ion> 0.00021264 </ekin_ion>
  <temp_ion> 11.19181543 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294475 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="430">
  <ekin>         5.22963757 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40937160 </eps>
  <enl>          4.76983599 </enl>
  <ecoul>      -15.59921579 </ecoul>
  <exc>         -4.36404475 </exc>
  <esr>          0.05491336 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315859 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315859 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68581175 0.00000000 -0.00000008 </position>
    <velocity> -0.00006385 -0.00000000 0.00000000 </velocity>
    <force> -0.00272155 -0.00000003 -0.00000016 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38429171 0.00000010 </position>
    <velocity> 0.00000000 0.00000913 -0.00000000 </velocity>
    <force> 0.00000006 -0.01328458 0.00000008 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68581175 -0.00000000 -0.00000008 </position>
    <velocity> 0.00006385 0.00000000 0.00000000 </velocity>
    <force> 0.00272153 0.00000003 -0.00000019 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38429171 0.00000007 </position>
    <velocity> -0.00000000 -0.00000913 -0.00000000 </velocity>
    <force> -0.00000004 0.01328458 0.00000028 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000042 </ekin_e>
  <ekin_ion> 0.00021302 </ekin_ion>
  <temp_ion> 11.21138264 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294475 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="431">
  <ekin>         5.22979602 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40948170 </eps>
  <enl>          4.76986362 </enl>
  <ecoul>      -15.59922904 </ecoul>
  <exc>         -4.36410797 </exc>
  <esr>          0.05493574 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315907 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315907 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68555507 0.00000000 -0.00000008 </position>
    <velocity> -0.00006407 -0.00000000 0.00000000 </velocity>
    <force> -0.00268330 -0.00000003 -0.00000027 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38432201 0.00000009 </position>
    <velocity> 0.00000000 0.00000809 -0.00000000 </velocity>
    <force> 0.00000005 -0.01328011 0.00000016 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68555507 -0.00000000 -0.00000008 </position>
    <velocity> 0.00006407 0.00000000 0.00000000 </velocity>
    <force> 0.00268327 0.00000002 -0.00000030 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38432201 0.00000007 </position>
    <velocity> -0.00000000 -0.00000809 -0.00000000 </velocity>
    <force> -0.00000003 0.01328012 0.00000044 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000042 </ekin_e>
  <ekin_ion> 0.00021348 </ekin_ion>
  <temp_ion> 11.23599187 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294474 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="432">
  <ekin>         5.22995707 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40959290 </eps>
  <enl>          4.76989055 </enl>
  <ecoul>      -15.59924200 </ecoul>
  <exc>         -4.36417236 </exc>
  <esr>          0.05495858 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37315963 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37315963 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68529756 0.00000000 -0.00000007 </position>
    <velocity> -0.00006427 -0.00000000 0.00000000 </velocity>
    <force> -0.00264450 -0.00000002 -0.00000037 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38434816 0.00000009 </position>
    <velocity> 0.00000000 0.00000706 -0.00000000 </velocity>
    <force> 0.00000004 -0.01327446 0.00000024 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68529756 -0.00000000 -0.00000007 </position>
    <velocity> 0.00006427 0.00000000 0.00000000 </velocity>
    <force> 0.00264446 0.00000001 -0.00000042 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38434816 0.00000006 </position>
    <velocity> -0.00000000 -0.00000706 -0.00000000 </velocity>
    <force> -0.00000002 0.01327447 0.00000059 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000042 </ekin_e>
  <ekin_ion> 0.00021405 </ekin_ion>
  <temp_ion> 11.26561740 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294474 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="433">
  <ekin>         5.23012058 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40970543 </eps>
  <enl>          4.76991715 </enl>
  <ecoul>      -15.59925468 </ecoul>
  <exc>         -4.36423791 </exc>
  <esr>          0.05498188 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316030 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316030 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68503924 0.00000000 -0.00000007 </position>
    <velocity> -0.00006448 -0.00000000 0.00000000 </velocity>
    <force> -0.00260508 -0.00000002 -0.00000046 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38437016 0.00000008 </position>
    <velocity> 0.00000000 0.00000602 -0.00000000 </velocity>
    <force> 0.00000003 -0.01326763 0.00000031 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68503924 -0.00000000 -0.00000007 </position>
    <velocity> 0.00006448 0.00000000 0.00000000 </velocity>
    <force> 0.00260504 0.00000001 -0.00000053 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38437016 0.00000006 </position>
    <velocity> -0.00000000 -0.00000602 -0.00000000 </velocity>
    <force> -0.00000001 0.01326764 0.00000074 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000043 </ekin_e>
  <ekin_ion> 0.00021470 </ekin_ion>
  <temp_ion> 11.30022949 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294473 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="434">
  <ekin>         5.23028655 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40981962 </eps>
  <enl>          4.76994382 </enl>
  <ecoul>      -15.59926717 </ecoul>
  <exc>         -4.36430463 </exc>
  <esr>          0.05500565 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316105 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316105 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68478012 0.00000000 -0.00000007 </position>
    <velocity> -0.00006468 -0.00000000 0.00000000 </velocity>
    <force> -0.00256503 -0.00000001 -0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38438803 0.00000008 </position>
    <velocity> 0.00000000 0.00000498 -0.00000000 </velocity>
    <force> 0.00000002 -0.01325968 0.00000039 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68478012 -0.00000000 -0.00000006 </position>
    <velocity> 0.00006468 0.00000000 0.00000000 </velocity>
    <force> 0.00256499 0.00000000 -0.00000064 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38438803 0.00000005 </position>
    <velocity> -0.00000000 -0.00000498 -0.00000000 </velocity>
    <force> -0.00000000 0.01325969 0.00000088 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000044 </ekin_e>
  <ekin_ion> 0.00021546 </ekin_ion>
  <temp_ion> 11.33979537 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294473 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="435">
  <ekin>         5.23045508 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.40993578 </eps>
  <enl>          4.76997092 </enl>
  <ecoul>      -15.59927957 </ecoul>
  <exc>         -4.36437255 </exc>
  <esr>          0.05502988 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316190 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316190 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68452021 0.00000000 -0.00000006 </position>
    <velocity> -0.00006488 -0.00000000 0.00000000 </velocity>
    <force> -0.00252442 -0.00000001 -0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38440175 0.00000007 </position>
    <velocity> 0.00000000 0.00000395 -0.00000000 </velocity>
    <force> 0.00000001 -0.01325076 0.00000047 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68452021 -0.00000000 -0.00000006 </position>
    <velocity> 0.00006488 0.00000000 0.00000000 </velocity>
    <force> 0.00252438 -0.00000001 -0.00000074 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38440175 0.00000005 </position>
    <velocity> -0.00000000 -0.00000395 -0.00000000 </velocity>
    <force> 0.00000001 0.01325077 0.00000101 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000044 </ekin_e>
  <ekin_ion> 0.00021630 </ekin_ion>
  <temp_ion> 11.38428078 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294472 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="436">
  <ekin>         5.23062637 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41005412 </eps>
  <enl>          4.76999863 </enl>
  <ecoul>      -15.59929198 </ecoul>
  <exc>         -4.36444174 </exc>
  <esr>          0.05505456 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316285 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316285 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68425952 0.00000000 -0.00000006 </position>
    <velocity> -0.00006507 -0.00000000 0.00000000 </velocity>
    <force> -0.00248336 -0.00000000 -0.00000075 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38441133 0.00000007 </position>
    <velocity> 0.00000000 0.00000291 -0.00000000 </velocity>
    <force> 0.00000000 -0.01324103 0.00000054 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68425952 -0.00000000 -0.00000005 </position>
    <velocity> 0.00006507 0.00000000 0.00000000 </velocity>
    <force> 0.00248331 -0.00000001 -0.00000084 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38441133 0.00000004 </position>
    <velocity> -0.00000000 -0.00000291 -0.00000000 </velocity>
    <force> 0.00000002 0.01324104 0.00000113 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000045 </ekin_e>
  <ekin_ion> 0.00021724 </ekin_ion>
  <temp_ion> 11.43365172 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294471 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="437">
  <ekin>         5.23080065 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41017471 </eps>
  <enl>          4.77002693 </enl>
  <ecoul>      -15.59930453 </ecoul>
  <exc>         -4.36451224 </exc>
  <esr>          0.05507971 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316389 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316389 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68399807 0.00000000 -0.00000005 </position>
    <velocity> -0.00006527 -0.00000000 0.00000000 </velocity>
    <force> -0.00244199 -0.00000000 -0.00000084 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38441678 0.00000007 </position>
    <velocity> 0.00000000 0.00000188 -0.00000000 </velocity>
    <force> -0.00000001 -0.01323065 0.00000062 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68399807 -0.00000000 -0.00000005 </position>
    <velocity> 0.00006527 0.00000000 0.00000000 </velocity>
    <force> 0.00244194 -0.00000002 -0.00000094 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38441678 0.00000004 </position>
    <velocity> -0.00000000 -0.00000188 -0.00000000 </velocity>
    <force> 0.00000003 0.01323066 0.00000125 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000046 </ekin_e>
  <ekin_ion> 0.00021827 </ekin_ion>
  <temp_ion> 11.48787601 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294471 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="438">
  <ekin>         5.23097818 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41029750 </eps>
  <enl>          4.77005568 </enl>
  <ecoul>      -15.59931728 </ecoul>
  <exc>         -4.36458410 </exc>
  <esr>          0.05510531 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316502 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316502 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68373587 0.00000000 -0.00000005 </position>
    <velocity> -0.00006546 -0.00000000 0.00000000 </velocity>
    <force> -0.00240045 0.00000000 -0.00000092 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38441809 0.00000006 </position>
    <velocity> 0.00000000 0.00000085 -0.00000000 </velocity>
    <force> -0.00000002 -0.01321977 0.00000069 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68373587 -0.00000000 -0.00000005 </position>
    <velocity> 0.00006546 0.00000000 0.00000000 </velocity>
    <force> 0.00240040 -0.00000003 -0.00000102 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38441809 0.00000003 </position>
    <velocity> -0.00000000 -0.00000085 -0.00000000 </velocity>
    <force> 0.00000004 0.01321979 0.00000135 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000046 </ekin_e>
  <ekin_ion> 0.00021939 </ekin_ion>
  <temp_ion> 11.54692413 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294470 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="439">
  <ekin>         5.23115913 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41042236 </eps>
  <enl>          4.77008464 </enl>
  <ecoul>      -15.59933029 </ecoul>
  <exc>         -4.36465735 </exc>
  <esr>          0.05513137 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316624 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316624 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68347293 0.00000000 -0.00000005 </position>
    <velocity> -0.00006564 -0.00000000 0.00000000 </velocity>
    <force> -0.00235885 0.00000001 -0.00000100 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38441528 0.00000006 </position>
    <velocity> 0.00000000 -0.00000019 -0.00000000 </velocity>
    <force> -0.00000003 -0.01320853 0.00000076 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68347293 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006564 0.00000000 0.00000000 </velocity>
    <force> 0.00235880 -0.00000003 -0.00000110 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38441528 0.00000003 </position>
    <velocity> -0.00000000 0.00000019 -0.00000000 </velocity>
    <force> 0.00000005 0.01320855 0.00000144 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000047 </ekin_e>
  <ekin_ion> 0.00022060 </ekin_ion>
  <temp_ion> 11.61076914 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294469 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="440">
  <ekin>         5.23134362 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41054912 </eps>
  <enl>          4.77011354 </enl>
  <ecoul>      -15.59934357 </ecoul>
  <exc>         -4.36473202 </exc>
  <esr>          0.05515789 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316755 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316755 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68320927 0.00000000 -0.00000004 </position>
    <velocity> -0.00006582 -0.00000000 0.00000000 </velocity>
    <force> -0.00231725 0.00000001 -0.00000108 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38440835 0.00000006 </position>
    <velocity> 0.00000000 -0.00000122 -0.00000000 </velocity>
    <force> -0.00000004 -0.01319702 0.00000083 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68320927 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006582 0.00000000 0.00000000 </velocity>
    <force> 0.00231720 -0.00000004 -0.00000116 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38440835 0.00000003 </position>
    <velocity> -0.00000000 0.00000122 -0.00000000 </velocity>
    <force> 0.00000005 0.01319704 0.00000151 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000048 </ekin_e>
  <ekin_ion> 0.00022191 </ekin_ion>
  <temp_ion> 11.67938591 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294468 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.008" max="    0.008"/>
<iteration count="441">
  <ekin>         5.23153169 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41067761 </eps>
  <enl>          4.77014220 </enl>
  <ecoul>      -15.59935712 </ecoul>
  <exc>         -4.36480811 </exc>
  <esr>          0.05518485 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37316896 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37316896 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68294490 0.00000000 -0.00000004 </position>
    <velocity> -0.00006600 -0.00000000 0.00000000 </velocity>
    <force> -0.00227565 0.00000002 -0.00000115 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38439729 0.00000005 </position>
    <velocity> 0.00000000 -0.00000225 -0.00000000 </velocity>
    <force> -0.00000005 -0.01318532 0.00000090 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68294490 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006600 0.00000000 0.00000000 </velocity>
    <force> 0.00227561 -0.00000004 -0.00000122 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38439729 0.00000003 </position>
    <velocity> -0.00000000 0.00000225 -0.00000000 </velocity>
    <force> 0.00000006 0.01318534 0.00000158 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000049 </ekin_e>
  <ekin_ion> 0.00022330 </ekin_ion>
  <temp_ion> 11.75274982 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294467 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="442">
  <ekin>         5.23172328 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41080768 </eps>
  <enl>          4.77017049 </enl>
  <ecoul>      -15.59937093 </ecoul>
  <exc>         -4.36488561 </exc>
  <esr>          0.05521228 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317045 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317045 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68267983 0.00000000 -0.00000004 </position>
    <velocity> -0.00006618 -0.00000000 0.00000000 </velocity>
    <force> -0.00223401 0.00000002 -0.00000121 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38438212 0.00000005 </position>
    <velocity> 0.00000000 -0.00000328 -0.00000000 </velocity>
    <force> -0.00000006 -0.01317350 0.00000096 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68267983 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006618 0.00000000 0.00000000 </velocity>
    <force> 0.00223397 -0.00000004 -0.00000126 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38438212 0.00000002 </position>
    <velocity> -0.00000000 0.00000328 -0.00000000 </velocity>
    <force> 0.00000007 0.01317352 0.00000162 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000050 </ekin_e>
  <ekin_ion> 0.00022479 </ekin_ion>
  <temp_ion> 11.83083552 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294466 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="443">
  <ekin>         5.23191832 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41093924 </eps>
  <enl>          4.77019835 </enl>
  <ecoul>      -15.59938496 </ecoul>
  <exc>         -4.36496450 </exc>
  <esr>          0.05524015 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317203 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317203 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68241407 0.00000000 -0.00000004 </position>
    <velocity> -0.00006635 -0.00000000 0.00000000 </velocity>
    <force> -0.00219225 0.00000003 -0.00000127 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38436283 0.00000005 </position>
    <velocity> 0.00000000 -0.00000431 -0.00000000 </velocity>
    <force> -0.00000007 -0.01316160 0.00000102 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68241407 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006635 0.00000000 0.00000000 </velocity>
    <force> 0.00219221 -0.00000005 -0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38436283 0.00000002 </position>
    <velocity> -0.00000000 0.00000431 -0.00000000 </velocity>
    <force> 0.00000007 0.01316162 0.00000166 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000051 </ekin_e>
  <ekin_ion> 0.00022636 </ekin_ion>
  <temp_ion> 11.91361602 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294465 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="444">
  <ekin>         5.23211673 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41107221 </eps>
  <enl>          4.77022576 </enl>
  <ecoul>      -15.59939918 </ecoul>
  <exc>         -4.36504479 </exc>
  <esr>          0.05526848 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317370 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317370 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68214764 0.00000000 -0.00000004 </position>
    <velocity> -0.00006652 -0.00000000 0.00000000 </velocity>
    <force> -0.00215030 0.00000003 -0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38433943 0.00000005 </position>
    <velocity> 0.00000000 -0.00000534 -0.00000000 </velocity>
    <force> -0.00000007 -0.01314961 0.00000108 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68214764 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006652 0.00000000 0.00000000 </velocity>
    <force> 0.00215027 -0.00000005 -0.00000132 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38433943 0.00000002 </position>
    <velocity> -0.00000000 0.00000534 -0.00000000 </velocity>
    <force> 0.00000008 0.01314963 0.00000168 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000052 </ekin_e>
  <ekin_ion> 0.00022802 </ekin_ion>
  <temp_ion> 12.00106237 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294464 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="445">
  <ekin>         5.23231843 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41120659 </eps>
  <enl>          4.77025274 </enl>
  <ecoul>      -15.59941357 </ecoul>
  <exc>         -4.36512648 </exc>
  <esr>          0.05529725 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317546 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317546 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68188056 0.00000000 -0.00000004 </position>
    <velocity> -0.00006669 -0.00000000 0.00000000 </velocity>
    <force> -0.00210812 0.00000004 -0.00000135 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38431193 0.00000005 </position>
    <velocity> 0.00000000 -0.00000636 -0.00000000 </velocity>
    <force> -0.00000008 -0.01313749 0.00000113 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68188056 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006669 0.00000000 0.00000000 </velocity>
    <force> 0.00210809 -0.00000005 -0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38431193 0.00000002 </position>
    <velocity> -0.00000000 0.00000636 -0.00000000 </velocity>
    <force> 0.00000008 0.01313751 0.00000169 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000053 </ekin_e>
  <ekin_ion> 0.00022977 </ekin_ion>
  <temp_ion> 12.09314377 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294463 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="446">
  <ekin>         5.23252340 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41134238 </eps>
  <enl>          4.77027935 </enl>
  <ecoul>      -15.59942811 </ecoul>
  <exc>         -4.36520957 </exc>
  <esr>          0.05532648 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317731 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317731 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68161282 0.00000000 -0.00000004 </position>
    <velocity> -0.00006685 -0.00000000 0.00000000 </velocity>
    <force> -0.00206565 0.00000004 -0.00000137 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38428033 0.00000005 </position>
    <velocity> 0.00000000 -0.00000739 -0.00000000 </velocity>
    <force> -0.00000009 -0.01312513 0.00000118 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68161282 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006685 0.00000000 0.00000000 </velocity>
    <force> 0.00206563 -0.00000005 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38428033 0.00000002 </position>
    <velocity> -0.00000000 0.00000739 -0.00000000 </velocity>
    <force> 0.00000008 0.01312514 0.00000169 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000054 </ekin_e>
  <ekin_ion> 0.00023161 </ekin_ion>
  <temp_ion> 12.18982795 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294462 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="447">
  <ekin>         5.23273164 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41147968 </eps>
  <enl>          4.77030568 </enl>
  <ecoul>      -15.59944281 </ecoul>
  <exc>         -4.36529407 </exc>
  <esr>          0.05535615 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37317924 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37317924 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68134446 0.00000000 -0.00000004 </position>
    <velocity> -0.00006701 -0.00000000 0.00000000 </velocity>
    <force> -0.00202291 0.00000004 -0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38424462 0.00000005 </position>
    <velocity> 0.00000000 -0.00000841 -0.00000000 </velocity>
    <force> -0.00000009 -0.01311237 0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68134446 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006701 -0.00000000 0.00000000 </velocity>
    <force> 0.00202290 -0.00000005 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38424462 0.00000002 </position>
    <velocity> -0.00000000 0.00000841 0.00000000 </velocity>
    <force> 0.00000008 0.01311238 0.00000167 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000055 </ekin_e>
  <ekin_ion> 0.00023353 </ekin_ion>
  <temp_ion> 12.29108137 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294461 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="448">
  <ekin>         5.23294317 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41161863 </eps>
  <enl>          4.77033188 </enl>
  <ecoul>      -15.59945768 </ecoul>
  <exc>         -4.36538000 </exc>
  <esr>          0.05538627 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318126 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318126 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68107547 0.00000000 -0.00000004 </position>
    <velocity> -0.00006717 -0.00000000 -0.00000000 </velocity>
    <force> -0.00197988 0.00000004 -0.00000139 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38420483 0.00000005 </position>
    <velocity> 0.00000000 -0.00000944 -0.00000000 </velocity>
    <force> -0.00000009 -0.01309900 0.00000126 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68107547 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006717 -0.00000000 -0.00000000 </velocity>
    <force> 0.00197987 -0.00000005 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38420483 0.00000002 </position>
    <velocity> 0.00000000 0.00000944 0.00000000 </velocity>
    <force> 0.00000008 0.01309900 0.00000164 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000056 </ekin_e>
  <ekin_ion> 0.00023554 </ekin_ion>
  <temp_ion> 12.39686908 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294460 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="449">
  <ekin>         5.23315803 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41175944 </eps>
  <enl>          4.77035815 </enl>
  <ecoul>      -15.59947275 </ecoul>
  <exc>         -4.36546735 </exc>
  <esr>          0.05541683 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318337 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318337 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68080589 0.00000000 -0.00000004 </position>
    <velocity> -0.00006732 -0.00000000 -0.00000000 </velocity>
    <force> -0.00193654 0.00000004 -0.00000138 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38416094 0.00000005 </position>
    <velocity> -0.00000000 -0.00001046 0.00000000 </velocity>
    <force> -0.00000009 -0.01308481 0.00000129 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68080589 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006732 -0.00000000 -0.00000000 </velocity>
    <force> 0.00193654 -0.00000005 -0.00000136 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38416094 0.00000003 </position>
    <velocity> 0.00000000 0.00001046 0.00000000 </velocity>
    <force> 0.00000008 0.01308481 0.00000160 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000057 </ekin_e>
  <ekin_ion> 0.00023764 </ekin_ion>
  <temp_ion> 12.50715418 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294459 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="450">
  <ekin>         5.23337623 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41190231 </eps>
  <enl>          4.77038473 </enl>
  <ecoul>      -15.59948808 </ecoul>
  <exc>         -4.36555612 </exc>
  <esr>          0.05544784 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318556 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318556 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68053571 0.00000000 -0.00000004 </position>
    <velocity> -0.00006747 0.00000000 -0.00000000 </velocity>
    <force> -0.00189287 0.00000004 -0.00000136 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38411297 0.00000005 </position>
    <velocity> -0.00000000 -0.00001148 0.00000000 </velocity>
    <force> -0.00000009 -0.01306961 0.00000131 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68053571 -0.00000000 -0.00000003 </position>
    <velocity> 0.00006747 -0.00000000 -0.00000000 </velocity>
    <force> 0.00189288 -0.00000005 -0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38411297 0.00000003 </position>
    <velocity> 0.00000000 0.00001148 0.00000000 </velocity>
    <force> 0.00000008 0.01306961 0.00000155 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000058 </ekin_e>
  <ekin_ion> 0.00023982 </ekin_ion>
  <temp_ion> 12.62189705 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294458 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="451">
  <ekin>         5.23359776 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41204744 </eps>
  <enl>          4.77041183 </enl>
  <ecoul>      -15.59950370 </ecoul>
  <exc>         -4.36564627 </exc>
  <esr>          0.05547930 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37318783 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37318783 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.68026495 0.00000000 -0.00000004 </position>
    <velocity> -0.00006762 0.00000000 -0.00000000 </velocity>
    <force> -0.00184883 0.00000005 -0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38406093 0.00000005 </position>
    <velocity> -0.00000000 -0.00001250 0.00000000 </velocity>
    <force> -0.00000009 -0.01305326 0.00000132 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.68026495 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006762 -0.00000000 -0.00000000 </velocity>
    <force> 0.00184884 -0.00000004 -0.00000133 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38406093 0.00000003 </position>
    <velocity> 0.00000000 0.00001250 0.00000000 </velocity>
    <force> 0.00000007 0.01305326 0.00000149 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000059 </ekin_e>
  <ekin_ion> 0.00024208 </ekin_ion>
  <temp_ion> 12.74105470 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294458 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="452">
  <ekin>         5.23382259 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41219497 </eps>
  <enl>          4.77043961 </enl>
  <ecoul>      -15.59951965 </ecoul>
  <exc>         -4.36573777 </exc>
  <esr>          0.05551119 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319019 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319019 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67999363 0.00000000 -0.00000004 </position>
    <velocity> -0.00006776 0.00000000 -0.00000000 </velocity>
    <force> -0.00180435 0.00000004 -0.00000129 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38400480 0.00000005 </position>
    <velocity> -0.00000000 -0.00001352 0.00000000 </velocity>
    <force> -0.00000009 -0.01303574 0.00000133 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67999363 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006776 -0.00000000 -0.00000000 </velocity>
    <force> 0.00180438 -0.00000004 -0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38400480 0.00000003 </position>
    <velocity> 0.00000000 0.00001352 0.00000000 </velocity>
    <force> 0.00000007 0.01303573 0.00000141 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000060 </ekin_e>
  <ekin_ion> 0.00024443 </ekin_ion>
  <temp_ion> 12.86458063 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294457 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="453">
  <ekin>         5.23405067 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41234494 </eps>
  <enl>          4.77046819 </enl>
  <ecoul>      -15.59953594 </ecoul>
  <exc>         -4.36583060 </exc>
  <esr>          0.05554353 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319262 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319262 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67972175 0.00000000 -0.00000005 </position>
    <velocity> -0.00006790 0.00000000 -0.00000000 </velocity>
    <force> -0.00175943 0.00000004 -0.00000125 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38394461 0.00000005 </position>
    <velocity> -0.00000000 -0.00001454 0.00000000 </velocity>
    <force> -0.00000008 -0.01301706 0.00000133 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67972175 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006790 -0.00000000 -0.00000000 </velocity>
    <force> 0.00175946 -0.00000003 -0.00000126 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38394461 0.00000004 </position>
    <velocity> 0.00000000 0.00001454 0.00000000 </velocity>
    <force> 0.00000006 0.01301706 0.00000133 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000061 </ekin_e>
  <ekin_ion> 0.00024686 </ekin_ion>
  <temp_ion> 12.99242532 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294456 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="454">
  <ekin>         5.23428192 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41249737 </eps>
  <enl>          4.77049761 </enl>
  <ecoul>      -15.59955259 </ecoul>
  <exc>         -4.36592472 </exc>
  <esr>          0.05557631 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319514 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319514 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67944935 0.00000000 -0.00000005 </position>
    <velocity> -0.00006803 0.00000000 -0.00000000 </velocity>
    <force> -0.00171404 0.00000004 -0.00000120 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38388036 0.00000005 </position>
    <velocity> -0.00000000 -0.00001556 0.00000000 </velocity>
    <force> -0.00000008 -0.01299737 0.00000131 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67944935 -0.00000000 -0.00000004 </position>
    <velocity> 0.00006803 -0.00000000 -0.00000000 </velocity>
    <force> 0.00171408 -0.00000003 -0.00000121 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38388036 0.00000004 </position>
    <velocity> 0.00000000 0.00001556 0.00000000 </velocity>
    <force> 0.00000006 0.01299736 0.00000123 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000061 </ekin_e>
  <ekin_ion> 0.00024937 </ekin_ion>
  <temp_ion> 13.12453745 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294455 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.005" max="    0.005"/>
<iteration count="455">
  <ekin>         5.23451625 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41265221 </eps>
  <enl>          4.77052791 </enl>
  <ecoul>      -15.59956958 </ecoul>
  <exc>         -4.36602011 </exc>
  <esr>          0.05560952 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37319774 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37319774 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67917642 0.00000000 -0.00000005 </position>
    <velocity> -0.00006817 0.00000000 -0.00000000 </velocity>
    <force> -0.00166822 0.00000004 -0.00000114 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.38381205 0.00000006 </position>
    <velocity> -0.00000000 -0.00001657 0.00000000 </velocity>
    <force> -0.00000007 -0.01297685 0.00000129 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67917642 -0.00000000 -0.00000005 </position>
    <velocity> 0.00006817 -0.00000000 -0.00000000 </velocity>
    <force> 0.00166827 -0.00000003 -0.00000115 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38381205 0.00000005 </position>
    <velocity> 0.00000000 0.00001657 0.00000000 </velocity>
    <force> 0.00000005 0.01297684 0.00000112 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000062 </ekin_e>
  <ekin_ion> 0.00025196 </ekin_ion>
  <temp_ion> 13.26086547 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294454 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.006" max="    0.006"/>
<iteration count="456">
  <ekin>         5.23475356 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41280946 </eps>
  <enl>          4.77055916 </enl>
  <ecoul>      -15.59958694 </ecoul>
  <exc>         -4.36611675 </exc>
  <esr>          0.05564317 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320042 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320042 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67890298 0.00000000 -0.00000006 </position>
    <velocity> -0.00006830 0.00000000 -0.00000000 </velocity>
    <force> -0.00162204 0.00000004 -0.00000108 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38373969 0.00000006 </position>
    <velocity> -0.00000000 -0.00001758 0.00000000 </velocity>
    <force> -0.00000006 -0.01295571 0.00000126 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67890298 -0.00000000 -0.00000005 </position>
    <velocity> 0.00006830 -0.00000000 -0.00000000 </velocity>
    <force> 0.00162209 -0.00000002 -0.00000109 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38373969 0.00000005 </position>
    <velocity> 0.00000000 0.00001758 0.00000000 </velocity>
    <force> 0.00000004 0.01295569 0.00000101 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000063 </ekin_e>
  <ekin_ion> 0.00025462 </ekin_ion>
  <temp_ion> 13.40135918 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294453 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="457">
  <ekin>         5.23499373 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41296914 </eps>
  <enl>          4.77059148 </enl>
  <ecoul>      -15.59960464 </ecoul>
  <exc>         -4.36621461 </exc>
  <esr>          0.05567726 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320318 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320318 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67862905 0.00000000 -0.00000006 </position>
    <velocity> -0.00006842 0.00000000 -0.00000000 </velocity>
    <force> -0.00157557 0.00000003 -0.00000101 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38366330 0.00000006 </position>
    <velocity> -0.00000000 -0.00001859 0.00000000 </velocity>
    <force> -0.00000005 -0.01293413 0.00000122 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67862905 -0.00000000 -0.00000006 </position>
    <velocity> 0.00006842 -0.00000000 -0.00000000 </velocity>
    <force> 0.00157562 -0.00000002 -0.00000101 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38366329 0.00000005 </position>
    <velocity> 0.00000000 0.00001859 0.00000000 </velocity>
    <force> 0.00000003 0.01293411 0.00000089 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000065 </ekin_e>
  <ekin_ion> 0.00025737 </ekin_ion>
  <temp_ion> 13.54597082 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294452 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="458">
  <ekin>         5.23523664 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41313132 </eps>
  <enl>          4.77062503 </enl>
  <ecoul>      -15.59962269 </ecoul>
  <exc>         -4.36631368 </exc>
  <esr>          0.05571178 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320602 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320602 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67835465 0.00000000 -0.00000006 </position>
    <velocity> -0.00006854 0.00000000 -0.00000000 </velocity>
    <force> -0.00152888 0.00000003 -0.00000094 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38358286 0.00000007 </position>
    <velocity> -0.00000000 -0.00001960 0.00000000 </velocity>
    <force> -0.00000004 -0.01291227 0.00000117 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67835465 -0.00000000 -0.00000006 </position>
    <velocity> 0.00006854 -0.00000000 -0.00000000 </velocity>
    <force> 0.00152893 -0.00000001 -0.00000093 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38358286 0.00000006 </position>
    <velocity> 0.00000000 0.00001960 0.00000000 </velocity>
    <force> 0.00000002 0.01291225 0.00000077 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000066 </ekin_e>
  <ekin_ion> 0.00026020 </ekin_ion>
  <temp_ion> 13.69465550 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294451 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="459">
  <ekin>         5.23548216 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41329602 </eps>
  <enl>          4.77065993 </enl>
  <ecoul>      -15.59964107 </ecoul>
  <exc>         -4.36641394 </exc>
  <esr>          0.05574674 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37320893 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37320893 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67807978 0.00000000 -0.00000007 </position>
    <velocity> -0.00006866 0.00000000 -0.00000000 </velocity>
    <force> -0.00148202 0.00000002 -0.00000086 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38349840 0.00000007 </position>
    <velocity> -0.00000000 -0.00002061 0.00000000 </velocity>
    <force> -0.00000003 -0.01289022 0.00000111 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67807978 -0.00000000 -0.00000006 </position>
    <velocity> 0.00006866 -0.00000000 -0.00000000 </velocity>
    <force> 0.00148208 -0.00000000 -0.00000084 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38349840 0.00000007 </position>
    <velocity> 0.00000000 0.00002061 0.00000000 </velocity>
    <force> 0.00000002 0.01289020 0.00000065 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000067 </ekin_e>
  <ekin_ion> 0.00026310 </ekin_ion>
  <temp_ion> 13.84737079 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294449 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="460">
  <ekin>         5.23573021 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41346323 </eps>
  <enl>          4.77069618 </enl>
  <ecoul>      -15.59965973 </ecoul>
  <exc>         -4.36651535 </exc>
  <esr>          0.05578212 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321192 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321192 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67780446 0.00000000 -0.00000007 </position>
    <velocity> -0.00006877 0.00000000 -0.00000000 </velocity>
    <force> -0.00143502 0.00000002 -0.00000077 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38340991 0.00000008 </position>
    <velocity> -0.00000000 -0.00002162 0.00000000 </velocity>
    <force> -0.00000002 -0.01286801 0.00000104 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67780446 -0.00000000 -0.00000007 </position>
    <velocity> 0.00006877 -0.00000000 -0.00000000 </velocity>
    <force> 0.00143508 0.00000000 -0.00000074 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.38340991 0.00000007 </position>
    <velocity> 0.00000000 0.00002162 0.00000000 </velocity>
    <force> 0.00000001 0.01286799 0.00000052 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000068 </ekin_e>
  <ekin_ion> 0.00026608 </ekin_ion>
  <temp_ion> 14.00407573 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294448 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="461">
  <ekin>         5.23598073 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41363276 </eps>
  <enl>          4.77073354 </enl>
  <ecoul>      -15.59967859 </ecoul>
  <exc>         -4.36661790 </exc>
  <esr>          0.05581794 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321499 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321499 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67752871 0.00000000 -0.00000008 </position>
    <velocity> -0.00006888 0.00000000 -0.00000000 </velocity>
    <force> -0.00138788 0.00000001 -0.00000067 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38331741 0.00000008 </position>
    <velocity> -0.00000000 -0.00002262 0.00000000 </velocity>
    <force> -0.00000001 -0.01284561 0.00000097 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67752871 -0.00000000 -0.00000007 </position>
    <velocity> 0.00006888 -0.00000000 -0.00000000 </velocity>
    <force> 0.00138794 0.00000001 -0.00000065 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38331741 0.00000008 </position>
    <velocity> 0.00000000 0.00002262 0.00000000 </velocity>
    <force> -0.00000000 0.01284559 0.00000040 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000069 </ekin_e>
  <ekin_ion> 0.00026913 </ekin_ion>
  <temp_ion> 14.16472955 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294447 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="462">
  <ekin>         5.23623370 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41380426 </eps>
  <enl>          4.77077153 </enl>
  <ecoul>      -15.59969755 </ecoul>
  <exc>         -4.36672155 </exc>
  <esr>          0.05585419 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37321813 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37321813 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67725254 0.00000000 -0.00000008 </position>
    <velocity> -0.00006899 0.00000000 -0.00000000 </velocity>
    <force> -0.00134055 0.00000001 -0.00000057 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38322091 0.00000009 </position>
    <velocity> -0.00000000 -0.00002363 0.00000000 </velocity>
    <force> 0.00000000 -0.01282296 0.00000088 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67725254 -0.00000000 -0.00000008 </position>
    <velocity> 0.00006899 -0.00000000 -0.00000000 </velocity>
    <force> 0.00134061 0.00000001 -0.00000054 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38322091 0.00000008 </position>
    <velocity> 0.00000000 0.00002363 0.00000000 </velocity>
    <force> -0.00000001 0.01282294 0.00000028 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000071 </ekin_e>
  <ekin_ion> 0.00027226 </ekin_ion>
  <temp_ion> 14.32929043 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294446 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="463">
  <ekin>         5.23648917 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41397726 </eps>
  <enl>          4.77080950 </enl>
  <ecoul>      -15.59971647 </ecoul>
  <exc>         -4.36682627 </exc>
  <esr>          0.05589086 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37322134 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37322134 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67697596 0.00000000 -0.00000009 </position>
    <velocity> -0.00006909 0.00000000 -0.00000000 </velocity>
    <force> -0.00129301 0.00000000 -0.00000046 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38312040 0.00000009 </position>
    <velocity> -0.00000000 -0.00002463 0.00000000 </velocity>
    <force> 0.00000001 -0.01279994 0.00000079 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67697596 -0.00000000 -0.00000008 </position>
    <velocity> 0.00006909 -0.00000000 -0.00000000 </velocity>
    <force> 0.00129306 0.00000002 -0.00000044 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38312040 0.00000009 </position>
    <velocity> 0.00000000 0.00002463 0.00000000 </velocity>
    <force> -0.00000002 0.01279992 0.00000016 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000072 </ekin_e>
  <ekin_ion> 0.00027546 </ekin_ion>
  <temp_ion> 14.49771447 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294444 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="464">
  <ekin>         5.23674721 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41415124 </eps>
  <enl>          4.77084670 </enl>
  <ecoul>      -15.59973525 </ecoul>
  <exc>         -4.36693205 </exc>
  <esr>          0.05592796 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37322463 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37322463 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67669900 0.00000000 -0.00000009 </position>
    <velocity> -0.00006919 0.00000000 -0.00000000 </velocity>
    <force> -0.00124521 -0.00000000 -0.00000035 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38301590 0.00000010 </position>
    <velocity> -0.00000000 -0.00002563 0.00000000 </velocity>
    <force> 0.00000002 -0.01277645 0.00000069 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67669900 -0.00000000 -0.00000009 </position>
    <velocity> 0.00006919 -0.00000000 -0.00000000 </velocity>
    <force> 0.00124526 0.00000002 -0.00000034 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38301590 0.00000009 </position>
    <velocity> 0.00000000 0.00002563 0.00000000 </velocity>
    <force> -0.00000003 0.01277644 0.00000004 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000073 </ekin_e>
  <ekin_ion> 0.00027873 </ekin_ion>
  <temp_ion> 14.66995516 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294443 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="465">
  <ekin>         5.23700796 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41432578 </eps>
  <enl>          4.77088252 </enl>
  <ecoul>      -15.59975379 </ecoul>
  <exc>         -4.36703889 </exc>
  <esr>          0.05596548 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37322798 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37322798 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67642166 0.00000000 -0.00000010 </position>
    <velocity> -0.00006929 0.00000000 -0.00000000 </velocity>
    <force> -0.00119710 -0.00000001 -0.00000024 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38290742 0.00000010 </position>
    <velocity> -0.00000000 -0.00002662 0.00000000 </velocity>
    <force> 0.00000004 -0.01275237 0.00000059 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67642166 -0.00000000 -0.00000010 </position>
    <velocity> 0.00006929 -0.00000000 -0.00000000 </velocity>
    <force> 0.00119714 0.00000003 -0.00000023 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38290742 0.00000010 </position>
    <velocity> 0.00000000 0.00002662 0.00000000 </velocity>
    <force> -0.00000004 0.01275236 -0.00000007 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000075 </ekin_e>
  <ekin_ion> 0.00028207 </ekin_ion>
  <temp_ion> 14.84596296 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294442 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="466">
  <ekin>         5.23727155 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41450068 </eps>
  <enl>          4.77091661 </enl>
  <ecoul>      -15.59977207 </ecoul>
  <exc>         -4.36714681 </exc>
  <esr>          0.05600343 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37323141 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37323141 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67614397 0.00000000 -0.00000011 </position>
    <velocity> -0.00006938 0.00000000 -0.00000000 </velocity>
    <force> -0.00114866 -0.00000002 -0.00000012 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38279495 0.00000011 </position>
    <velocity> -0.00000000 -0.00002762 0.00000000 </velocity>
    <force> 0.00000005 -0.01272758 0.00000047 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67614397 -0.00000000 -0.00000010 </position>
    <velocity> 0.00006938 -0.00000000 -0.00000000 </velocity>
    <force> 0.00114870 0.00000003 -0.00000013 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38279495 0.00000011 </position>
    <velocity> 0.00000000 0.00002762 0.00000000 </velocity>
    <force> -0.00000005 0.01272757 -0.00000019 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000076 </ekin_e>
  <ekin_ion> 0.00028549 </ekin_ion>
  <temp_ion> 15.02568526 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294441 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="467">
  <ekin>         5.23753811 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41467602 </eps>
  <enl>          4.77094903 </enl>
  <ecoul>      -15.59979017 </ecoul>
  <exc>         -4.36725586 </exc>
  <esr>          0.05604180 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37323491 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37323491 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67586592 0.00000000 -0.00000011 </position>
    <velocity> -0.00006947 0.00000000 -0.00000000 </velocity>
    <force> -0.00109987 -0.00000002 0.00000000 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38267852 0.00000011 </position>
    <velocity> -0.00000000 -0.00002861 0.00000000 </velocity>
    <force> 0.00000006 -0.01270197 0.00000035 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67586593 -0.00000000 -0.00000011 </position>
    <velocity> 0.00006947 -0.00000000 -0.00000000 </velocity>
    <force> 0.00109990 0.00000003 -0.00000002 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38267852 0.00000011 </position>
    <velocity> 0.00000000 0.00002861 0.00000000 </velocity>
    <force> -0.00000005 0.01270196 -0.00000030 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000077 </ekin_e>
  <ekin_ion> 0.00028897 </ekin_ion>
  <temp_ion> 15.20906646 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294439 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="468">
  <ekin>         5.23780778 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41485217 </eps>
  <enl>          4.77098020 </enl>
  <ecoul>      -15.59980819 </ecoul>
  <exc>         -4.36736610 </exc>
  <esr>          0.05608059 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37323847 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37323847 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67558756 0.00000000 -0.00000012 </position>
    <velocity> -0.00006955 0.00000000 -0.00000000 </velocity>
    <force> -0.00105070 -0.00000003 0.00000012 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38255813 0.00000012 </position>
    <velocity> -0.00000000 -0.00002960 0.00000000 </velocity>
    <force> 0.00000007 -0.01267547 0.00000022 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67558756 -0.00000000 -0.00000011 </position>
    <velocity> 0.00006955 -0.00000000 -0.00000000 </velocity>
    <force> 0.00105073 0.00000004 0.00000008 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38255813 0.00000012 </position>
    <velocity> 0.00000000 0.00002960 0.00000000 </velocity>
    <force> -0.00000006 0.01267546 -0.00000041 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000079 </ekin_e>
  <ekin_ion> 0.00029252 </ekin_ion>
  <temp_ion> 15.39604828 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294438 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="469">
  <ekin>         5.23808068 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41502969 </eps>
  <enl>          4.77101083 </enl>
  <ecoul>      -15.59982634 </ecoul>
  <exc>         -4.36747759 </exc>
  <esr>          0.05611979 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37324211 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37324211 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67530887 0.00000000 -0.00000012 </position>
    <velocity> -0.00006963 0.00000000 -0.00000000 </velocity>
    <force> -0.00100118 -0.00000003 0.00000024 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38243378 0.00000013 </position>
    <velocity> -0.00000000 -0.00003059 0.00000000 </velocity>
    <force> 0.00000007 -0.01264804 0.00000009 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67530887 -0.00000000 -0.00000012 </position>
    <velocity> 0.00006963 -0.00000000 -0.00000000 </velocity>
    <force> 0.00100119 0.00000004 0.00000018 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38243378 0.00000012 </position>
    <velocity> 0.00000000 0.00003059 0.00000000 </velocity>
    <force> -0.00000006 0.01264804 -0.00000051 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000080 </ekin_e>
  <ekin_ion> 0.00029614 </ekin_ion>
  <temp_ion> 15.58657047 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294436 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="470">
  <ekin>         5.23835688 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41520918 </eps>
  <enl>          4.77104168 </enl>
  <ecoul>      -15.59984477 </ecoul>
  <exc>         -4.36759041 </exc>
  <esr>          0.05615942 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37324581 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37324581 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67502990 0.00000000 -0.00000013 </position>
    <velocity> -0.00006971 0.00000000 -0.00000000 </velocity>
    <force> -0.00095131 -0.00000004 0.00000035 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38230549 0.00000013 </position>
    <velocity> -0.00000000 -0.00003158 0.00000000 </velocity>
    <force> 0.00000008 -0.01261973 -0.00000005 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67502990 -0.00000000 -0.00000012 </position>
    <velocity> 0.00006971 -0.00000000 -0.00000000 </velocity>
    <force> 0.00095132 0.00000004 0.00000028 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38230549 0.00000013 </position>
    <velocity> 0.00000000 0.00003158 0.00000000 </velocity>
    <force> -0.00000007 0.01261973 -0.00000061 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000081 </ekin_e>
  <ekin_ion> 0.00029983 </ekin_ion>
  <temp_ion> 15.78057198 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294435 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="471">
  <ekin>         5.23863646 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41539114 </eps>
  <enl>          4.77107340 </enl>
  <ecoul>      -15.59986366 </ecoul>
  <exc>         -4.36770463 </exc>
  <esr>          0.05619946 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37324957 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37324957 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67475063 0.00000000 -0.00000013 </position>
    <velocity> -0.00006978 0.00000000 -0.00000000 </velocity>
    <force> -0.00090116 -0.00000004 0.00000046 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38217327 0.00000014 </position>
    <velocity> -0.00000000 -0.00003256 0.00000000 </velocity>
    <force> 0.00000009 -0.01259064 -0.00000019 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67475063 -0.00000000 -0.00000013 </position>
    <velocity> 0.00006978 -0.00000000 -0.00000000 </velocity>
    <force> 0.00090116 0.00000004 0.00000038 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38217327 0.00000013 </position>
    <velocity> 0.00000000 0.00003256 0.00000000 </velocity>
    <force> -0.00000007 0.01259064 -0.00000070 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000083 </ekin_e>
  <ekin_ion> 0.00030358 </ekin_ion>
  <temp_ion> 15.97799268 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294434 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="472">
  <ekin>         5.23891944 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41557580 </eps>
  <enl>          4.77110632 </enl>
  <ecoul>      -15.59988306 </ecoul>
  <exc>         -4.36782031 </exc>
  <esr>          0.05623991 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325341 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325341 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67447111 0.00000000 -0.00000014 </position>
    <velocity> -0.00006985 0.00000000 -0.00000000 </velocity>
    <force> -0.00085081 -0.00000005 0.00000056 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38203712 0.00000014 </position>
    <velocity> -0.00000000 -0.00003355 0.00000000 </velocity>
    <force> 0.00000009 -0.01256093 -0.00000033 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67447111 -0.00000000 -0.00000013 </position>
    <velocity> 0.00006985 -0.00000000 -0.00000000 </velocity>
    <force> 0.00085080 0.00000004 0.00000048 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38203712 0.00000014 </position>
    <velocity> 0.00000000 0.00003355 0.00000000 </velocity>
    <force> -0.00000008 0.01256093 -0.00000079 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000085 </ekin_e>
  <ekin_ion> 0.00030740 </ekin_ion>
  <temp_ion> 16.17877527 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294432 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="473">
  <ekin>         5.23920582 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41576310 </eps>
  <enl>          4.77114041 </enl>
  <ecoul>      -15.59990296 </ecoul>
  <exc>         -4.36793746 </exc>
  <esr>          0.05628078 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37325730 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37325730 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67419133 0.00000000 -0.00000014 </position>
    <velocity> -0.00006991 0.00000000 -0.00000000 </velocity>
    <force> -0.00080036 -0.00000005 0.00000066 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38189705 0.00000015 </position>
    <velocity> -0.00000000 -0.00003453 0.00000000 </velocity>
    <force> 0.00000009 -0.01253080 -0.00000046 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67419133 -0.00000000 -0.00000014 </position>
    <velocity> 0.00006991 -0.00000000 -0.00000000 </velocity>
    <force> 0.00080034 0.00000004 0.00000058 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38189705 0.00000014 </position>
    <velocity> 0.00000000 0.00003453 0.00000000 </velocity>
    <force> -0.00000008 0.01253081 -0.00000087 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000086 </ekin_e>
  <ekin_ion> 0.00031127 </ekin_ion>
  <temp_ion> 16.38286699 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294430 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="474">
  <ekin>         5.23949552 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41595268 </eps>
  <enl>          4.77117528 </enl>
  <ecoul>      -15.59992329 </ecoul>
  <exc>         -4.36805609 </exc>
  <esr>          0.05632205 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37326126 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37326126 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67391132 0.00000000 -0.00000015 </position>
    <velocity> -0.00006997 0.00000000 -0.00000000 </velocity>
    <force> -0.00074992 -0.00000005 0.00000076 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38175308 0.00000016 </position>
    <velocity> -0.00000000 -0.00003551 0.00000000 </velocity>
    <force> 0.00000009 -0.01250046 -0.00000060 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67391132 -0.00000000 -0.00000014 </position>
    <velocity> 0.00006997 0.00000000 -0.00000000 </velocity>
    <force> 0.00074989 0.00000004 0.00000068 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38175308 0.00000015 </position>
    <velocity> 0.00000000 0.00003550 0.00000000 </velocity>
    <force> -0.00000008 0.01250047 -0.00000093 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000088 </ekin_e>
  <ekin_ion> 0.00031521 </ekin_ion>
  <temp_ion> 16.59022063 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294428 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="475">
  <ekin>         5.23978842 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41614404 </eps>
  <enl>          4.77121034 </enl>
  <ecoul>      -15.59994386 </ecoul>
  <exc>         -4.36817614 </exc>
  <esr>          0.05636374 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37326528 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37326528 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67363109 0.00000000 -0.00000015 </position>
    <velocity> -0.00007003 0.00000000 -0.00000000 </velocity>
    <force> -0.00069956 -0.00000005 0.00000085 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38160521 0.00000016 </position>
    <velocity> 0.00000000 -0.00003648 0.00000000 </velocity>
    <force> 0.00000009 -0.01247005 -0.00000073 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67363109 -0.00000000 -0.00000015 </position>
    <velocity> 0.00007003 0.00000000 -0.00000000 </velocity>
    <force> 0.00069953 0.00000004 0.00000078 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38160521 0.00000015 </position>
    <velocity> -0.00000000 0.00003648 0.00000000 </velocity>
    <force> -0.00000008 0.01247006 -0.00000099 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000090 </ekin_e>
  <ekin_ion> 0.00031921 </ekin_ion>
  <temp_ion> 16.80079430 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294427 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="476">
  <ekin>         5.24008435 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41633664 </eps>
  <enl>          4.77124499 </enl>
  <ecoul>      -15.59996452 </ecoul>
  <exc>         -4.36829754 </exc>
  <esr>          0.05640583 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37326936 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37326936 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67335066 0.00000000 -0.00000016 </position>
    <velocity> -0.00007008 -0.00000000 -0.00000000 </velocity>
    <force> -0.00064933 -0.00000005 0.00000093 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38145345 0.00000017 </position>
    <velocity> 0.00000000 -0.00003745 0.00000000 </velocity>
    <force> 0.00000009 -0.01243966 -0.00000086 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67335066 -0.00000000 -0.00000015 </position>
    <velocity> 0.00007008 0.00000000 -0.00000000 </velocity>
    <force> 0.00064929 0.00000004 0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38145345 0.00000015 </position>
    <velocity> -0.00000000 0.00003745 0.00000000 </velocity>
    <force> -0.00000008 0.01243967 -0.00000105 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000092 </ekin_e>
  <ekin_ion> 0.00032328 </ekin_ion>
  <temp_ion> 17.01454967 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294516 </econst>
  <ekin_ec> -15.37294425 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="477">
  <ekin>         5.24038306 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41653004 </eps>
  <enl>          4.77127874 </enl>
  <ecoul>      -15.59998509 </ecoul>
  <exc>         -4.36842016 </exc>
  <esr>          0.05644833 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37327349 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37327349 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67307004 0.00000000 -0.00000016 </position>
    <velocity> -0.00007013 -0.00000000 -0.00000000 </velocity>
    <force> -0.00059920 -0.00000005 0.00000100 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38129781 0.00000017 </position>
    <velocity> 0.00000000 -0.00003842 0.00000000 </velocity>
    <force> 0.00000009 -0.01240924 -0.00000098 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67307004 -0.00000000 -0.00000016 </position>
    <velocity> 0.00007013 0.00000000 -0.00000000 </velocity>
    <force> 0.00059914 0.00000004 0.00000096 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38129781 0.00000016 </position>
    <velocity> -0.00000000 0.00003842 0.00000000 </velocity>
    <force> -0.00000007 0.01240925 -0.00000109 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000093 </ekin_e>
  <ekin_ion> 0.00032740 </ekin_ion>
  <temp_ion> 17.23144909 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294423 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="478">
  <ekin>         5.24068432 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41672405 </eps>
  <enl>          4.77131140 </enl>
  <ecoul>      -15.60000547 </ecoul>
  <exc>         -4.36854390 </exc>
  <esr>          0.05649123 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37327769 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37327769 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67278925 0.00000000 -0.00000016 </position>
    <velocity> -0.00007018 -0.00000000 -0.00000000 </velocity>
    <force> -0.00054905 -0.00000005 0.00000107 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38113831 0.00000018 </position>
    <velocity> 0.00000000 -0.00003939 0.00000000 </velocity>
    <force> 0.00000009 -0.01237867 -0.00000110 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67278925 -0.00000000 -0.00000016 </position>
    <velocity> 0.00007018 0.00000000 -0.00000000 </velocity>
    <force> 0.00054899 0.00000003 0.00000105 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38113831 0.00000016 </position>
    <velocity> -0.00000000 0.00003939 0.00000000 </velocity>
    <force> -0.00000007 0.01237868 -0.00000113 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000095 </ekin_e>
  <ekin_ion> 0.00033158 </ekin_ion>
  <temp_ion> 17.45145195 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294422 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="479">
  <ekin>         5.24098789 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41691870 </eps>
  <enl>          4.77134310 </enl>
  <ecoul>      -15.60002562 </ecoul>
  <exc>         -4.36866862 </exc>
  <esr>          0.05653453 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37328194 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37328194 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67250830 0.00000000 -0.00000017 </position>
    <velocity> -0.00007022 -0.00000000 -0.00000000 </velocity>
    <force> -0.00049874 -0.00000005 0.00000114 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38097494 0.00000018 </position>
    <velocity> 0.00000000 -0.00004036 0.00000000 </velocity>
    <force> 0.00000008 -0.01234773 -0.00000121 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67250830 -0.00000000 -0.00000016 </position>
    <velocity> 0.00007022 0.00000000 -0.00000000 </velocity>
    <force> 0.00049868 0.00000003 0.00000113 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38097494 0.00000016 </position>
    <velocity> -0.00000000 0.00004036 0.00000000 </velocity>
    <force> -0.00000006 0.01234775 -0.00000116 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000097 </ekin_e>
  <ekin_ion> 0.00033581 </ekin_ion>
  <temp_ion> 17.67451126 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294420 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="480">
  <ekin>         5.24129359 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41711427 </eps>
  <enl>          4.77137421 </enl>
  <ecoul>      -15.60004556 </ecoul>
  <exc>         -4.36879423 </exc>
  <esr>          0.05657824 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37328625 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37328625 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67222721 0.00000000 -0.00000017 </position>
    <velocity> -0.00007025 -0.00000000 -0.00000000 </velocity>
    <force> -0.00044810 -0.00000005 0.00000119 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38080773 0.00000018 </position>
    <velocity> 0.00000000 -0.00004132 0.00000000 </velocity>
    <force> 0.00000008 -0.01231621 -0.00000132 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67222721 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007025 0.00000000 -0.00000000 </velocity>
    <force> 0.00044804 0.00000003 0.00000120 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38080773 0.00000016 </position>
    <velocity> -0.00000000 0.00004132 0.00000000 </velocity>
    <force> -0.00000006 0.01231623 -0.00000118 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000098 </ekin_e>
  <ekin_ion> 0.00034011 </ekin_ion>
  <temp_ion> 17.90057139 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294419 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="481">
  <ekin>         5.24160131 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41731114 </eps>
  <enl>          4.77140528 </enl>
  <ecoul>      -15.60006540 </ecoul>
  <exc>         -4.36892067 </exc>
  <esr>          0.05662234 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37329062 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37329062 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67194600 0.00000000 -0.00000017 </position>
    <velocity> -0.00007029 -0.00000000 -0.00000000 </velocity>
    <force> -0.00039697 -0.00000004 0.00000124 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38063668 0.00000019 </position>
    <velocity> 0.00000000 -0.00004228 0.00000000 </velocity>
    <force> 0.00000007 -0.01228389 -0.00000141 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67194600 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007029 0.00000000 -0.00000000 </velocity>
    <force> 0.00039690 0.00000002 0.00000126 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38063668 0.00000016 </position>
    <velocity> -0.00000000 0.00004228 0.00000000 </velocity>
    <force> -0.00000005 0.01228391 -0.00000119 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000099 </ekin_e>
  <ekin_ion> 0.00034446 </ekin_ion>
  <temp_ion> 18.12956740 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294417 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="482">
  <ekin>         5.24191103 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41750978 </eps>
  <enl>          4.77143689 </enl>
  <ecoul>      -15.60008525 </ecoul>
  <exc>         -4.36904792 </exc>
  <esr>          0.05666684 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37329504 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37329504 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67166468 0.00000000 -0.00000017 </position>
    <velocity> -0.00007032 -0.00000000 -0.00000000 </velocity>
    <force> -0.00034524 -0.00000004 0.00000128 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38046180 0.00000019 </position>
    <velocity> 0.00000000 -0.00004324 0.00000000 </velocity>
    <force> 0.00000006 -0.01225063 -0.00000150 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67166468 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007032 0.00000000 -0.00000000 </velocity>
    <force> 0.00034517 0.00000002 0.00000131 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38046180 0.00000017 </position>
    <velocity> -0.00000000 0.00004324 0.00000000 </velocity>
    <force> -0.00000005 0.01225065 -0.00000120 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000101 </ekin_e>
  <ekin_ion> 0.00034887 </ekin_ion>
  <temp_ion> 18.36142652 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294416 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="483">
  <ekin>         5.24222284 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41771057 </eps>
  <enl>          4.77146951 </enl>
  <ecoul>      -15.60010527 </ecoul>
  <exc>         -4.36917603 </exc>
  <esr>          0.05671174 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37329951 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37329951 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67138327 0.00000000 -0.00000017 </position>
    <velocity> -0.00007034 -0.00000000 -0.00000000 </velocity>
    <force> -0.00029288 -0.00000003 0.00000131 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38028310 0.00000019 </position>
    <velocity> 0.00000000 -0.00004420 0.00000000 </velocity>
    <force> 0.00000005 -0.01221640 -0.00000158 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67138327 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007034 0.00000000 -0.00000000 </velocity>
    <force> 0.00029282 0.00000001 0.00000135 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38028310 0.00000017 </position>
    <velocity> -0.00000000 0.00004420 0.00000000 </velocity>
    <force> -0.00000004 0.01221641 -0.00000120 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000102 </ekin_e>
  <ekin_ion> 0.00035332 </ekin_ion>
  <temp_ion> 18.59607122 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294415 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="484">
  <ekin>         5.24253693 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41791379 </eps>
  <enl>          4.77150346 </enl>
  <ecoul>      -15.60012557 </ecoul>
  <exc>         -4.36930507 </exc>
  <esr>          0.05675703 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37330403 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37330403 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67110178 0.00000000 -0.00000017 </position>
    <velocity> -0.00007036 -0.00000000 -0.00000000 </velocity>
    <force> -0.00023996 -0.00000003 0.00000133 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.38010059 0.00000019 </position>
    <velocity> 0.00000000 -0.00004515 0.00000000 </velocity>
    <force> 0.00000004 -0.01218122 -0.00000164 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67110178 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007036 0.00000000 -0.00000000 </velocity>
    <force> 0.00023990 0.00000001 0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.38010059 0.00000017 </position>
    <velocity> -0.00000000 0.00004515 0.00000000 </velocity>
    <force> -0.00000003 0.01218123 -0.00000120 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000103 </ekin_e>
  <ekin_ion> 0.00035783 </ekin_ion>
  <temp_ion> 18.83342323 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294413 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="485">
  <ekin>         5.24285353 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41811956 </eps>
  <enl>          4.77153882 </enl>
  <ecoul>      -15.60014625 </ecoul>
  <exc>         -4.36943515 </exc>
  <esr>          0.05680271 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37330861 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37330861 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67082024 0.00000000 -0.00000018 </position>
    <velocity> -0.00007038 -0.00000000 -0.00000000 </velocity>
    <force> -0.00018662 -0.00000002 0.00000134 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37991429 0.00000019 </position>
    <velocity> 0.00000000 -0.00004610 0.00000000 </velocity>
    <force> 0.00000003 -0.01214521 -0.00000169 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67082024 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007038 0.00000000 -0.00000000 </velocity>
    <force> 0.00018656 0.00000000 0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37991429 0.00000017 </position>
    <velocity> -0.00000000 0.00004610 0.00000000 </velocity>
    <force> -0.00000002 0.01214522 -0.00000119 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000105 </ekin_e>
  <ekin_ion> 0.00036239 </ekin_ion>
  <temp_ion> 19.07340762 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294412 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="486">
  <ekin>         5.24317290 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41832785 </eps>
  <enl>          4.77157549 </enl>
  <ecoul>      -15.60016738 </ecoul>
  <exc>         -4.36956638 </exc>
  <esr>          0.05684878 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37331323 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37331323 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67053866 0.00000000 -0.00000018 </position>
    <velocity> -0.00007039 -0.00000000 -0.00000000 </velocity>
    <force> -0.00013305 -0.00000002 0.00000135 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37972421 0.00000019 </position>
    <velocity> 0.00000000 -0.00004705 0.00000000 </velocity>
    <force> 0.00000001 -0.01210851 -0.00000172 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67053865 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007039 0.00000000 -0.00000000 </velocity>
    <force> 0.00013299 0.00000000 0.00000142 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.37972421 0.00000017 </position>
    <velocity> -0.00000000 0.00004705 0.00000000 </velocity>
    <force> -0.00000001 0.01210852 -0.00000118 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000106 </ekin_e>
  <ekin_ion> 0.00036700 </ekin_ion>
  <temp_ion> 19.31595584 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294410 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="487">
  <ekin>         5.24349526 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41853853 </eps>
  <enl>          4.77161320 </enl>
  <ecoul>      -15.60018898 </ecoul>
  <exc>         -4.36969885 </exc>
  <esr>          0.05689524 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37331790 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37331790 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.67025704 0.00000000 -0.00000018 </position>
    <velocity> -0.00007040 -0.00000000 0.00000000 </velocity>
    <force> -0.00007943 -0.00000001 0.00000134 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37953035 0.00000019 </position>
    <velocity> 0.00000000 -0.00004799 0.00000000 </velocity>
    <force> 0.00000000 -0.01207126 -0.00000175 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.67025704 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007040 0.00000000 -0.00000000 </velocity>
    <force> 0.00007939 -0.00000000 0.00000142 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37953035 0.00000017 </position>
    <velocity> -0.00000000 0.00004799 -0.00000000 </velocity>
    <force> -0.00000001 0.01207128 -0.00000116 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000108 </ekin_e>
  <ekin_ion> 0.00037166 </ekin_ion>
  <temp_ion> 19.56100707 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294409 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="488">
  <ekin>         5.24382075 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41875137 </eps>
  <enl>          4.77165163 </enl>
  <ecoul>      -15.60021100 </ecoul>
  <exc>         -4.36983263 </exc>
  <esr>          0.05694208 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37332262 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37332262 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66997543 0.00000000 -0.00000017 </position>
    <velocity> -0.00007040 -0.00000000 0.00000000 </velocity>
    <force> -0.00002595 -0.00000000 0.00000132 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37933273 0.00000019 </position>
    <velocity> 0.00000000 -0.00004893 -0.00000000 </velocity>
    <force> -0.00000001 -0.01203356 -0.00000175 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66997543 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007040 0.00000000 0.00000000 </velocity>
    <force> 0.00002591 -0.00000001 0.00000141 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37933273 0.00000017 </position>
    <velocity> -0.00000000 0.00004893 -0.00000000 </velocity>
    <force> 0.00000000 0.01203357 -0.00000114 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000109 </ekin_e>
  <ekin_ion> 0.00037636 </ekin_ion>
  <temp_ion> 19.80850752 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294407 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="489">
  <ekin>         5.24414942 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41896613 </eps>
  <enl>          4.77169044 </enl>
  <ecoul>      -15.60023339 </ecoul>
  <exc>         -4.36996772 </exc>
  <esr>          0.05698931 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37332738 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37332738 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66969382 0.00000000 -0.00000017 </position>
    <velocity> -0.00007040 -0.00000000 0.00000000 </velocity>
    <force> 0.00002734 0.00000001 0.00000130 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37913137 0.00000019 </position>
    <velocity> 0.00000000 -0.00004987 -0.00000000 </velocity>
    <force> -0.00000002 -0.01199542 -0.00000174 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66969382 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007040 0.00000000 0.00000000 </velocity>
    <force> -0.00002737 -0.00000001 0.00000140 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37913137 0.00000016 </position>
    <velocity> -0.00000000 0.00004987 -0.00000000 </velocity>
    <force> 0.00000001 0.01199543 -0.00000111 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000111 </ekin_e>
  <ekin_ion> 0.00038111 </ekin_ion>
  <temp_ion> 20.05840781 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294406 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="490">
  <ekin>         5.24448118 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41918258 </eps>
  <enl>          4.77172936 </enl>
  <ecoul>      -15.60025605 </ecoul>
  <exc>         -4.37010410 </exc>
  <esr>          0.05703692 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37333219 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37333219 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66941223 0.00000000 -0.00000017 </position>
    <velocity> -0.00007040 -0.00000000 0.00000000 </velocity>
    <force> 0.00008043 0.00000001 0.00000127 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37892626 0.00000019 </position>
    <velocity> 0.00000000 -0.00005081 -0.00000000 </velocity>
    <force> -0.00000003 -0.01195680 -0.00000172 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66941223 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007040 0.00000000 0.00000000 </velocity>
    <force> -0.00008045 -0.00000002 0.00000138 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37892626 0.00000016 </position>
    <velocity> -0.00000000 0.00005081 -0.00000000 </velocity>
    <force> 0.00000002 0.01195681 -0.00000107 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000112 </ekin_e>
  <ekin_ion> 0.00038590 </ekin_ion>
  <temp_ion> 20.31065916 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294404 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.010" max="    0.010"/>
<iteration count="491">
  <ekin>         5.24481584 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41940054 </eps>
  <enl>          4.77176822 </enl>
  <ecoul>      -15.60027888 </ecoul>
  <exc>         -4.37024169 </exc>
  <esr>          0.05708492 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37333704 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37333704 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66913069 0.00000000 -0.00000017 </position>
    <velocity> -0.00007039 -0.00000000 0.00000000 </velocity>
    <force> 0.00013345 0.00000002 0.00000123 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> -0.00000000 2.37871743 0.00000019 </position>
    <velocity> 0.00000000 -0.00005174 -0.00000000 </velocity>
    <force> -0.00000004 -0.01191763 -0.00000168 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66913069 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007039 0.00000000 0.00000000 </velocity>
    <force> -0.00013346 -0.00000002 0.00000134 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37871743 0.00000016 </position>
    <velocity> -0.00000000 0.00005174 -0.00000000 </velocity>
    <force> 0.00000003 0.01191763 -0.00000103 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000114 </ekin_e>
  <ekin_ion> 0.00039074 </ekin_ion>
  <temp_ion> 20.56520916 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294403 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.011" max="    0.011"/>
<iteration count="492">
  <ekin>         5.24515313 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41961988 </eps>
  <enl>          4.77180699 </enl>
  <ecoul>      -15.60030178 </ecoul>
  <exc>         -4.37038039 </exc>
  <esr>          0.05713329 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37334194 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37334194 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66884920 0.00000000 -0.00000017 </position>
    <velocity> -0.00007038 -0.00000000 0.00000000 </velocity>
    <force> 0.00018658 0.00000003 0.00000118 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37850489 0.00000019 </position>
    <velocity> 0.00000000 -0.00005267 -0.00000000 </velocity>
    <force> -0.00000005 -0.01187779 -0.00000163 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66884920 -0.00000000 -0.00000017 </position>
    <velocity> 0.00007038 0.00000000 0.00000000 </velocity>
    <force> -0.00018659 -0.00000003 0.00000130 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37850489 0.00000016 </position>
    <velocity> -0.00000000 0.00005267 -0.00000000 </velocity>
    <force> 0.00000004 0.01187779 -0.00000099 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000115 </ekin_e>
  <ekin_ion> 0.00039562 </ekin_ion>
  <temp_ion> 20.82199833 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294401 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="493">
  <ekin>         5.24549274 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.41984056 </eps>
  <enl>          4.77184570 </enl>
  <ecoul>      -15.60032467 </ecoul>
  <exc>         -4.37052008 </exc>
  <esr>          0.05718203 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37334687 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37334687 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66856779 0.00000000 -0.00000017 </position>
    <velocity> -0.00007036 -0.00000000 0.00000000 </velocity>
    <force> 0.00024007 0.00000003 0.00000113 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37828866 0.00000018 </position>
    <velocity> 0.00000000 -0.00005360 -0.00000000 </velocity>
    <force> -0.00000006 -0.01183722 -0.00000157 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66856779 -0.00000000 -0.00000016 </position>
    <velocity> 0.00007036 0.00000000 0.00000000 </velocity>
    <force> -0.00024006 -0.00000003 0.00000125 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37828866 0.00000016 </position>
    <velocity> -0.00000000 0.00005360 -0.00000000 </velocity>
    <force> 0.00000005 0.01183721 -0.00000094 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000117 </ekin_e>
  <ekin_ion> 0.00040054 </ekin_ion>
  <temp_ion> 21.08095827 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294400 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="494">
  <ekin>         5.24583441 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42006256 </eps>
  <enl>          4.77188446 </enl>
  <ecoul>      -15.60034750 </ecoul>
  <exc>         -4.37066066 </exc>
  <esr>          0.05723115 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37335185 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37335185 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66828647 0.00000000 -0.00000016 </position>
    <velocity> -0.00007034 -0.00000000 0.00000000 </velocity>
    <force> 0.00029414 0.00000004 0.00000107 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37806873 0.00000018 </position>
    <velocity> 0.00000000 -0.00005452 -0.00000000 </velocity>
    <force> -0.00000007 -0.01179588 -0.00000149 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66828648 -0.00000000 -0.00000016 </position>
    <velocity> 0.00007034 0.00000000 0.00000000 </velocity>
    <force> -0.00029412 -0.00000003 0.00000119 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37806873 0.00000015 </position>
    <velocity> -0.00000000 0.00005452 -0.00000000 </velocity>
    <force> 0.00000006 0.01179588 -0.00000089 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000118 </ekin_e>
  <ekin_ion> 0.00040550 </ekin_ion>
  <temp_ion> 21.34201216 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294398 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="495">
  <ekin>         5.24617797 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42028593 </eps>
  <enl>          4.77192342 </enl>
  <ecoul>      -15.60037026 </ecoul>
  <exc>         -4.37080206 </exc>
  <esr>          0.05728064 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37335686 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37335686 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66800527 0.00000000 -0.00000016 </position>
    <velocity> -0.00007032 -0.00000000 0.00000000 </velocity>
    <force> 0.00034893 0.00000004 0.00000101 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37784513 0.00000018 </position>
    <velocity> 0.00000000 -0.00005544 -0.00000000 </velocity>
    <force> -0.00000008 -0.01175386 -0.00000140 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66800527 -0.00000000 -0.00000016 </position>
    <velocity> 0.00007032 0.00000000 0.00000000 </velocity>
    <force> -0.00034890 -0.00000003 0.00000112 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37784513 0.00000015 </position>
    <velocity> -0.00000000 0.00005544 -0.00000000 </velocity>
    <force> 0.00000006 0.01175385 -0.00000083 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000120 </ekin_e>
  <ekin_ion> 0.00041049 </ekin_ion>
  <temp_ion> 21.60507749 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294397 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="496">
  <ekin>         5.24652339 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42051073 </eps>
  <enl>          4.77196268 </enl>
  <ecoul>      -15.60039298 </ecoul>
  <exc>         -4.37094428 </exc>
  <esr>          0.05733050 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37336191 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37336191 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66772418 0.00000000 -0.00000016 </position>
    <velocity> -0.00007029 -0.00000000 0.00000000 </velocity>
    <force> 0.00040449 0.00000005 0.00000094 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37761787 0.00000017 </position>
    <velocity> 0.00000000 -0.00005636 -0.00000000 </velocity>
    <force> -0.00000008 -0.01171129 -0.00000131 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66772418 -0.00000000 -0.00000015 </position>
    <velocity> 0.00007029 0.00000000 0.00000000 </velocity>
    <force> -0.00040445 -0.00000003 0.00000104 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37761787 0.00000015 </position>
    <velocity> -0.00000000 0.00005636 -0.00000000 </velocity>
    <force> 0.00000007 0.01171128 -0.00000078 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000122 </ekin_e>
  <ekin_ion> 0.00041553 </ekin_ion>
  <temp_ion> 21.87007072 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294395 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="497">
  <ekin>         5.24687077 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42073702 </eps>
  <enl>          4.77200233 </enl>
  <ecoul>      -15.60041573 </ecoul>
  <exc>         -4.37108734 </exc>
  <esr>          0.05738073 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37336700 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37336700 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66744324 0.00000000 -0.00000015 </position>
    <velocity> -0.00007025 -0.00000000 0.00000000 </velocity>
    <force> 0.00046075 0.00000005 0.00000086 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37738697 0.00000017 </position>
    <velocity> 0.00000000 -0.00005727 -0.00000000 </velocity>
    <force> -0.00000009 -0.01166838 -0.00000120 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66744325 -0.00000000 -0.00000015 </position>
    <velocity> 0.00007025 0.00000000 0.00000000 </velocity>
    <force> -0.00046070 -0.00000004 0.00000096 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37738696 0.00000014 </position>
    <velocity> -0.00000000 0.00005727 -0.00000000 </velocity>
    <force> 0.00000007 0.01166837 -0.00000072 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000123 </ekin_e>
  <ekin_ion> 0.00042060 </ekin_ion>
  <temp_ion> 22.13691262 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294393 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="498">
  <ekin>         5.24722032 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42096489 </eps>
  <enl>          4.77204236 </enl>
  <ecoul>      -15.60043859 </ecoul>
  <exc>         -4.37123132 </exc>
  <esr>          0.05743133 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37337212 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37337212 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66716247 0.00000000 -0.00000015 </position>
    <velocity> -0.00007021 -0.00000000 0.00000000 </velocity>
    <force> 0.00051749 0.00000005 0.00000078 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37715243 0.00000016 </position>
    <velocity> 0.00000000 -0.00005818 -0.00000000 </velocity>
    <force> -0.00000009 -0.01162534 -0.00000108 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66716247 -0.00000000 -0.00000014 </position>
    <velocity> 0.00007021 0.00000000 0.00000000 </velocity>
    <force> -0.00051744 -0.00000004 0.00000087 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37715243 0.00000014 </position>
    <velocity> -0.00000000 0.00005818 -0.00000000 </velocity>
    <force> 0.00000007 0.01162533 -0.00000066 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000125 </ekin_e>
  <ekin_ion> 0.00042570 </ekin_ion>
  <temp_ion> 22.40553305 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294391 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<iteration count="499">
  <ekin>         5.24757234 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42119436 </eps>
  <enl>          4.77208272 </enl>
  <ecoul>      -15.60046166 </ecoul>
  <exc>         -4.37137631 </exc>
  <esr>          0.05748229 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37337728 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37337728 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66688187 0.00000000 -0.00000014 </position>
    <velocity> -0.00007017 -0.00000000 0.00000000 </velocity>
    <force> 0.00057444 0.00000006 0.00000069 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37691427 0.00000016 </position>
    <velocity> 0.00000000 -0.00005909 -0.00000000 </velocity>
    <force> -0.00000010 -0.01158233 -0.00000095 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66688187 -0.00000000 -0.00000014 </position>
    <velocity> 0.00007017 0.00000000 0.00000000 </velocity>
    <force> -0.00057437 -0.00000004 0.00000078 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37691427 0.00000014 </position>
    <velocity> -0.00000000 0.00005909 -0.00000000 </velocity>
    <force> 0.00000008 0.01158231 -0.00000059 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000127 </ekin_e>
  <ekin_ion> 0.00043084 </ekin_ion>
  <temp_ion> 22.67587381 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294389 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.009"/>
<iteration count="500">
  <ekin>         5.24792713 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.42142545 </eps>
  <enl>          4.77212330 </enl>
  <ecoul>      -15.60048504 </ecoul>
  <exc>         -4.37152240 </exc>
  <esr>          0.05753361 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37338247 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37338247 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.66660147 0.00000000 -0.00000014 </position>
    <velocity> -0.00007012 -0.00000000 0.00000000 </velocity>
    <force> 0.00063126 0.00000006 0.00000060 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.37667250 0.00000015 </position>
    <velocity> 0.00000000 -0.00005999 -0.00000000 </velocity>
    <force> -0.00000010 -0.01153938 -0.00000081 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.66660147 -0.00000000 -0.00000014 </position>
    <velocity> 0.00007012 -0.00000000 0.00000000 </velocity>
    <force> -0.00063119 -0.00000004 0.00000068 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> -0.00000000 -2.37667250 0.00000013 </position>
    <velocity> -0.00000000 0.00005999 -0.00000000 </velocity>
    <force> 0.00000008 0.01153936 -0.00000053 </force>
  </atom>
</atomset>
  <ekin_e> 0.00000129 </ekin_e>
  <ekin_ion> 0.00043601 </ekin_ion>
  <temp_ion> 22.94788864 </temp_ion>
  <eta_ion> 0.00000000 </eta_ion>
  <econst> -15.37294517 </econst>
  <ekin_ec> -15.37294387 </ekin_ec>
  total_electronic_charge: 16.00000000
</iteration>
  <timing name="iteration" min="    0.009" max="    0.010"/>
<timing name="         charge" min="    0.708" max="    1.915"/>
<timing name="         ekin_e" min="    0.006" max="    0.009"/>
<timing name="   md_update_wf" min="    0.004" max="    0.005"/>
<timing name="        riccati" min="    0.138" max="    0.235"/>
<timing name="           ekin" min="    0.026" max="    0.061"/>
<timing name="            exc" min="    0.376" max="    0.386"/>
<timing name="           hpsi" min="    0.847" max="    0.856"/>
<timing name="       nonlocal" min="    0.175" max="    0.176"/>
<timing name=" charge_compute" min="    0.471" max="    1.676"/>
<timing name="charge_integral" min="    0.020" max="    0.053"/>
<timing name="  charge_rowsum" min="    0.006" max="    0.012"/>
<timing name="     charge_vft" min="    0.161" max="    0.204"/>
[qbox]  End of command stream 
<real_time> 4.426 </real_time>
<end_time> 2016-04-06T12:25:29Z </end_time>
</fpmd:simulation>
