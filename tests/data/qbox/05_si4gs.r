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
<start_time> 2016-04-06T12:25:20Z </start_time>
<mpi_processes count="4">
<process id="0"> theobook68 </process>
<process id="1"> theobook68 </process>
<process id="2"> theobook68 </process>
<process id="3"> theobook68 </process>
</mpi_processes>
[qbox] <cmd># Si4 ground state</cmd>
[qbox] <cmd>set cell 16 0 0  0 16 0  0 0 16</cmd>
<unit_cell 
    a="16.00000000  0.00000000   0.00000000  "
    b="0.00000000   16.00000000  0.00000000  "
    c="0.00000000   0.00000000   16.00000000 " />
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
[qbox] <cmd>atom Si1 silicon  3.700  0.000  0.000</cmd>
[qbox] <cmd>atom Si2 silicon  0.000  2.200  0.000</cmd>
[qbox] <cmd>atom Si3 silicon -3.700  0.000  0.000</cmd>
[qbox] <cmd>atom Si4 silicon  0.000 -2.200  0.000</cmd>
[qbox] [qbox] <cmd>set ecut 6</cmd>
[qbox] <cmd>set wf_dyn PSDA</cmd>
[qbox] <cmd>set ecutprec 2</cmd>
[qbox] [qbox] <cmd>randomize_wf</cmd>
[qbox] <cmd>run 0 200</cmd>
  EnergyFunctional: np0v,np1v,np2v: 30 30 30
  EnergyFunctional: vft->np012(): 27000
<wavefunction ecut="3.00000000" nspin="1" nel="16" nempty="0">
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
  <eigenvalue_sum>  0.15252926 </eigenvalue_sum>
  <etotal_int>       0.53023823 </etotal_int>
  total_electronic_charge: 15.99999999
  <eigenvalue_sum>  -1.90531677 </eigenvalue_sum>
  Anderson extrapolation: theta=0.00193954 (0.00193954)
  <etotal_int>      -4.01738848 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -3.15148531 </eigenvalue_sum>
  Anderson extrapolation: theta=0.03791214 (0.03791214)
  <etotal_int>      -7.21613637 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -3.81026727 </eigenvalue_sum>
  Anderson extrapolation: theta=0.68785285 (0.68785285)
  <etotal_int>      -9.68441269 </etotal_int>
  total_electronic_charge: 15.99999999
  <eigenvalue_sum>  -3.71899091 </eigenvalue_sum>
  Anderson extrapolation: theta=0.29985197 (0.29985197)
  <etotal_int>     -11.86360884 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -3.26166749 </eigenvalue_sum>
  Anderson extrapolation: theta=0.13493533 (0.13493533)
  <etotal_int>     -12.55997964 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -3.00388481 </eigenvalue_sum>
  Anderson extrapolation: theta=0.03057259 (0.03057259)
  <etotal_int>     -12.93068465 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.84487993 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71318984 (0.71318984)
  <etotal_int>     -13.21850715 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.65184169 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71909187 (0.71909187)
  <etotal_int>     -13.62278828 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.55797575 </eigenvalue_sum>
  Anderson extrapolation: theta=0.51747792 (0.51747792)
  <etotal_int>     -13.98064813 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.54624674 </eigenvalue_sum>
  Anderson extrapolation: theta=0.39279125 (0.39279125)
  <etotal_int>     -14.19347688 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.52900860 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82499827 (0.82499827)
  <etotal_int>     -14.32248604 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.51330744 </eigenvalue_sum>
  Anderson extrapolation: theta=0.67841105 (0.67841105)
  <etotal_int>     -14.45691865 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.51953918 </eigenvalue_sum>
  Anderson extrapolation: theta=0.51644133 (0.51644133)
  <etotal_int>     -14.56099240 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.53186584 </eigenvalue_sum>
  Anderson extrapolation: theta=0.34255690 (0.34255690)
  <etotal_int>     -14.63063827 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.53384827 </eigenvalue_sum>
  Anderson extrapolation: theta=0.04720558 (0.04720558)
  <etotal_int>     -14.67767567 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.52985010 </eigenvalue_sum>
  Anderson extrapolation: theta=-1.11776151 (0.00000000)
  <etotal_int>     -14.70596573 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.52667467 </eigenvalue_sum>
  Anderson extrapolation: theta=-2.03216678 (0.00000000)
  <etotal_int>     -14.73245298 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.52305050 </eigenvalue_sum>
  Anderson extrapolation: theta=-2.41164378 (0.00000000)
  <etotal_int>     -14.75946382 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.51823088 </eigenvalue_sum>
  Anderson extrapolation: theta=-2.48559561 (0.00000000)
  <etotal_int>     -14.78705313 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.51188074 </eigenvalue_sum>
  Anderson extrapolation: theta=-2.27028654 (0.00000000)
  <etotal_int>     -14.81519229 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.50391644 </eigenvalue_sum>
  Anderson extrapolation: theta=-1.77815364 (0.00000000)
  <etotal_int>     -14.84378050 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.49442472 </eigenvalue_sum>
  Anderson extrapolation: theta=-1.03496018 (0.00000000)
  <etotal_int>     -14.87265456 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.48361563 </eigenvalue_sum>
  Anderson extrapolation: theta=-0.09162788 (-0.09162788)
  <etotal_int>     -14.90160150 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.47290799 </eigenvalue_sum>
  Anderson extrapolation: theta=1.04742555 (1.04742555)
  <etotal_int>     -14.92774968 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.44807149 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09698906 (1.09698906)
  <etotal_int>     -14.98268962 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.40783855 </eigenvalue_sum>
  Anderson extrapolation: theta=1.18400456 (1.18400456)
  <etotal_int>     -15.06406398 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36275002 </eigenvalue_sum>
  Anderson extrapolation: theta=0.74173173 (0.74173173)
  <etotal_int>     -15.16101275 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.34832025 </eigenvalue_sum>
  Anderson extrapolation: theta=0.56519664 (0.56519664)
  <etotal_int>     -15.22163821 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35133578 </eigenvalue_sum>
  Anderson extrapolation: theta=0.66646126 (0.66646126)
  <etotal_int>     -15.25175660 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35718639 </eigenvalue_sum>
  Anderson extrapolation: theta=0.64928622 (0.64928622)
  <etotal_int>     -15.27175353 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36119566 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84526569 (0.84526569)
  <etotal_int>     -15.28660423 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36481837 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85582979 (0.85582979)
  <etotal_int>     -15.30098026 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36825320 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94326596 (0.94326596)
  <etotal_int>     -15.31459616 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.37170302 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83259190 (0.83259190)
  <etotal_int>     -15.32774964 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.37370904 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87236128 (0.87236128)
  <etotal_int>     -15.33839550 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.37395215 </eigenvalue_sum>
  Anderson extrapolation: theta=0.76925942 (0.76925942)
  <etotal_int>     -15.34684668 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.37224219 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85485915 (0.85485915)
  <etotal_int>     -15.35263362 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36938554 </eigenvalue_sum>
  Anderson extrapolation: theta=0.70159750 (0.70159750)
  <etotal_int>     -15.35690169 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36633138 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90484819 (0.90484819)
  <etotal_int>     -15.35968519 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36334406 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72722323 (0.72722323)
  <etotal_int>     -15.36205119 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36121837 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02452708 (1.02452708)
  <etotal_int>     -15.36382656 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35944570 </eigenvalue_sum>
  Anderson extrapolation: theta=0.80682061 (0.80682061)
  <etotal_int>     -15.36562084 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35837870 </eigenvalue_sum>
  Anderson extrapolation: theta=1.07540992 (1.07540992)
  <etotal_int>     -15.36708307 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35762389 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86028743 (0.86028743)
  <etotal_int>     -15.36855652 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35723880 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06880665 (1.06880665)
  <etotal_int>     -15.36971710 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35707719 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85315255 (0.85315255)
  <etotal_int>     -15.37074639 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35707136 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98190945 (0.98190945)
  <etotal_int>     -15.37142695 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35716362 </eigenvalue_sum>
  Anderson extrapolation: theta=0.78398352 (0.78398352)
  <etotal_int>     -15.37187345 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35724189 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89001756 (0.89001756)
  <etotal_int>     -15.37207401 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35730634 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71989824 (0.71989824)
  <etotal_int>     -15.37213829 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35731829 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84878985 (0.84878985)
  <etotal_int>     -15.37213637 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35730892 </eigenvalue_sum>
  Anderson extrapolation: theta=0.69429014 (0.69429014)
  <etotal_int>     -15.37211265 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35727844 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87767591 (0.87767591)
  <etotal_int>     -15.37210390 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35723875 </eigenvalue_sum>
  Anderson extrapolation: theta=0.73455287 (0.73455287)
  <etotal_int>     -15.37211074 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35719501 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98725278 (0.98725278)
  <etotal_int>     -15.37213858 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35714407 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83779844 (0.83779844)
  <etotal_int>     -15.37218651 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35709348 </eigenvalue_sum>
  Anderson extrapolation: theta=1.11675746 (1.11675746)
  <etotal_int>     -15.37224714 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35703505 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93567619 (0.93567619)
  <etotal_int>     -15.37232864 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35697866 </eigenvalue_sum>
  Anderson extrapolation: theta=1.16154447 (1.16154447)
  <etotal_int>     -15.37241494 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35691687 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95341122 (0.95341122)
  <etotal_int>     -15.37251563 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35686145 </eigenvalue_sum>
  Anderson extrapolation: theta=1.10234957 (1.10234957)
  <etotal_int>     -15.37260746 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35680892 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89991584 (0.89991584)
  <etotal_int>     -15.37269605 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35676920 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00894682 (1.00894682)
  <etotal_int>     -15.37276250 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35674014 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83309450 (0.83309450)
  <etotal_int>     -15.37281363 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672425 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93984033 (0.93984033)
  <etotal_int>     -15.37284436 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671836 </eigenvalue_sum>
  Anderson extrapolation: theta=0.78980578 (0.78980578)
  <etotal_int>     -15.37286278 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671917 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91141630 (0.91141630)
  <etotal_int>     -15.37287132 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672458 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77311204 (0.77311204)
  <etotal_int>     -15.37287468 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673056 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91227838 (0.91227838)
  <etotal_int>     -15.37287559 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673704 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77325043 (0.77325043)
  <etotal_int>     -15.37287550 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35674148 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93064821 (0.93064821)
  <etotal_int>     -15.37287586 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35674475 </eigenvalue_sum>
  Anderson extrapolation: theta=0.78799975 (0.78799975)
  <etotal_int>     -15.37287683 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35674584 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96888234 (0.96888234)
  <etotal_int>     -15.37287884 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35674547 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82638979 (0.82638979)
  <etotal_int>     -15.37288194 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35674357 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03291264 (1.03291264)
  <etotal_int>     -15.37288585 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35674030 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89028590 (0.89028590)
  <etotal_int>     -15.37289096 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673613 </eigenvalue_sum>
  Anderson extrapolation: theta=1.10339338 (1.10339338)
  <etotal_int>     -15.37289651 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673079 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95137759 (0.95137759)
  <etotal_int>     -15.37290319 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672523 </eigenvalue_sum>
  Anderson extrapolation: theta=1.13077446 (1.13077446)
  <etotal_int>     -15.37290983 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671917 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96236017 (0.96236017)
  <etotal_int>     -15.37291699 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671391 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08297687 (1.08297687)
  <etotal_int>     -15.37292325 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670941 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90900487 (0.90900487)
  <etotal_int>     -15.37292884 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670649 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98933965 (0.98933965)
  <etotal_int>     -15.37293274 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670488 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83090964 (0.83090964)
  <etotal_int>     -15.37293531 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670437 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90970718 (0.90970718)
  <etotal_int>     -15.37293654 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670451 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77587752 (0.77587752)
  <etotal_int>     -15.37293696 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670484 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88105753 (0.88105753)
  <etotal_int>     -15.37293696 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670522 </eigenvalue_sum>
  Anderson extrapolation: theta=0.76536520 (0.76536520)
  <etotal_int>     -15.37293681 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670550 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90886531 (0.90886531)
  <etotal_int>     -15.37293674 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670577 </eigenvalue_sum>
  Anderson extrapolation: theta=0.79812475 (0.79812475)
  <etotal_int>     -15.37293676 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670602 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97698972 (0.97698972)
  <etotal_int>     -15.37293695 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670636 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85835251 (0.85835251)
  <etotal_int>     -15.37293728 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670672 </eigenvalue_sum>
  Anderson extrapolation: theta=1.05251806 (1.05251806)
  <etotal_int>     -15.37293773 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670718 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91813833 (0.91813833)
  <etotal_int>     -15.37293834 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670761 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09847124 (1.09847124)
  <etotal_int>     -15.37293900 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670803 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95044355 (0.95044355)
  <etotal_int>     -15.37293979 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670829 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09836177 (1.09836177)
  <etotal_int>     -15.37294057 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670839 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94624050 (0.94624050)
  <etotal_int>     -15.37294138 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670825 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06158934 (1.06158934)
  <etotal_int>     -15.37294210 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670787 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91405921 (0.91405921)
  <etotal_int>     -15.37294275 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670729 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00738185 (1.00738185)
  <etotal_int>     -15.37294323 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670655 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86831973 (0.86831973)
  <etotal_int>     -15.37294360 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670578 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95294043 (0.95294043)
  <etotal_int>     -15.37294381 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670500 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82324905 (0.82324905)
  <etotal_int>     -15.37294393 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670434 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91343377 (0.91343377)
  <etotal_int>     -15.37294397 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=0.79329684 (0.79329684)
  <etotal_int>     -15.37294397 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670340 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90379665 (0.90379665)
  <etotal_int>     -15.37294396 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670316 </eigenvalue_sum>
  Anderson extrapolation: theta=0.79240202 (0.79240202)
  <etotal_int>     -15.37294395 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670307 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93540487 (0.93540487)
  <etotal_int>     -15.37294396 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670310 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82957690 (0.82957690)
  <etotal_int>     -15.37294399 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670323 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00681045 (1.00681045)
  <etotal_int>     -15.37294404 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670345 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89879259 (0.89879259)
  <etotal_int>     -15.37294411 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670370 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08977112 (1.08977112)
  <etotal_int>     -15.37294419 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670402 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96726997 (0.96726997)
  <etotal_int>     -15.37294430 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670431 </eigenvalue_sum>
  Anderson extrapolation: theta=1.13234850 (1.13234850)
  <etotal_int>     -15.37294441 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670461 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98828706 (0.98828706)
  <etotal_int>     -15.37294453 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670484 </eigenvalue_sum>
  Anderson extrapolation: theta=1.10052841 (1.10052841)
  <etotal_int>     -15.37294465 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670500 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94446752 (0.94446752)
  <etotal_int>     -15.37294476 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670506 </eigenvalue_sum>
  Anderson extrapolation: theta=1.01520724 (1.01520724)
  <etotal_int>     -15.37294485 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670502 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86801436 (0.86801436)
  <etotal_int>     -15.37294491 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670489 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93155846 (0.93155846)
  <etotal_int>     -15.37294494 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670469 </eigenvalue_sum>
  Anderson extrapolation: theta=0.80622605 (0.80622605)
  <etotal_int>     -15.37294495 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670447 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89041005 (0.89041005)
  <etotal_int>     -15.37294496 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670423 </eigenvalue_sum>
  Anderson extrapolation: theta=0.78437611 (0.78437611)
  <etotal_int>     -15.37294496 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670402 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90249219 (0.90249219)
  <etotal_int>     -15.37294495 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670383 </eigenvalue_sum>
  Anderson extrapolation: theta=0.80544235 (0.80544235)
  <etotal_int>     -15.37294495 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670369 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95865831 (0.95865831)
  <etotal_int>     -15.37294496 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670358 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85916298 (0.85916298)
  <etotal_int>     -15.37294496 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670352 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03390959 (1.03390959)
  <etotal_int>     -15.37294497 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670350 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92202207 (0.92202207)
  <etotal_int>     -15.37294499 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670351 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09138788 (1.09138788)
  <etotal_int>     -15.37294500 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670356 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96294410 (0.96294410)
  <etotal_int>     -15.37294502 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670363 </eigenvalue_sum>
  Anderson extrapolation: theta=1.10247616 (1.10247616)
  <etotal_int>     -15.37294504 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670372 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96229296 (0.96229296)
  <etotal_int>     -15.37294506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06615203 (1.06615203)
  <etotal_int>     -15.37294507 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670391 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92489005 (0.92489005)
  <etotal_int>     -15.37294509 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670398 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00562886 (1.00562886)
  <etotal_int>     -15.37294510 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670403 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87324707 (0.87324707)
  <etotal_int>     -15.37294511 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670405 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95004392 (0.95004392)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670405 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83078576 (0.83078576)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670402 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91959648 (0.91959648)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670398 </eigenvalue_sum>
  Anderson extrapolation: theta=0.81170637 (0.81170637)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670393 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92261085 (0.92261085)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670388 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82133366 (0.82133366)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670383 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95815641 (0.95815641)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85780694 (0.85780694)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670376 </eigenvalue_sum>
  Anderson extrapolation: theta=1.01500022 (1.01500022)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670373 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90907022 (0.90907022)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670372 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06896889 (1.06896889)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670371 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95137249 (0.95137249)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670372 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09086603 (1.09086603)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670373 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96023267 (0.96023267)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670375 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06657701 (1.06657701)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670377 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92954621 (0.92954621)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00992182 (1.00992182)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87810070 (0.87810070)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670382 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95274284 (0.95274284)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83450975 (0.83450975)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92285017 (0.92285017)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.81861207 (0.81861207)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93194281 (0.93194281)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670383 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83603519 (0.83603519)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670382 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97519240 (0.97519240)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87886778 (0.87886778)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03161351 (1.03161351)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92556086 (0.92556086)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06976053 (1.06976053)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94924146 (0.94924146)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06746606 (1.06746606)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93693524 (0.93693524)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02952836 (1.02952836)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89996999 (0.89996999)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98198222 (0.98198222)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86262822 (0.86262822)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95095285 (0.95095285)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84385144 (0.84385144)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94868344 (0.94868344)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84972940 (0.84972940)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97256270 (0.97256270)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87496907 (0.87496907)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00876561 (1.00876561)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90599383 (0.90599383)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03793803 (1.03793803)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92649068 (0.92649068)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=1.04505057 (1.04505057)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92636610 (0.92636610)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02828407 (1.02828407)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90774442 (0.90774442)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99887151 (0.99887151)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88233930 (0.88233930)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97276024 (0.97276024)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86339794 (0.86339794)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96197661 (0.96197661)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85939048 (0.85939048)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97067429 (0.97067429)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87188006 (0.87188006)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99467596 (0.99467596)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89541116 (0.89541116)
  <etotal_int>     -15.37294516 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02260425 (1.02260425)
  <etotal_int>     -15.37294516 </etotal_int>
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
  <timing name="iteration" min="    1.087" max="    1.091"/>
</iteration>
<timing name="         charge" min="    0.285" max="    0.303"/>
<timing name="         energy" min="    0.406" max="    0.423"/>
<timing name="    ortho_align" min="    0.044" max="    0.072"/>
<timing name="      psda_prec" min="    0.003" max="    0.003"/>
<timing name="  psda_residual" min="    0.012" max="    0.043"/>
<timing name=" psda_update_wf" min="    0.004" max="    0.031"/>
<timing name="    update_vhxc" min="    0.227" max="    0.245"/>
<timing name="      wf_update" min="    0.098" max="    0.131"/>
<timing name="           ekin" min="    0.011" max="    0.028"/>
<timing name="            exc" min="    0.147" max="    0.148"/>
<timing name="           hpsi" min="    0.338" max="    0.339"/>
<timing name="       nonlocal" min="    0.054" max="    0.055"/>
<timing name=" charge_compute" min="    0.194" max="    0.206"/>
<timing name="charge_integral" min="    0.008" max="    0.020"/>
<timing name="  charge_rowsum" min="    0.002" max="    0.003"/>
<timing name="     charge_vft" min="    0.061" max="    0.080"/>
[qbox] <cmd>save test.xml</cmd>
 SampleWriter: write time: 0.007 s
 SampleWriter: file size: 357985
 SampleWriter: aggregate write rate: 50.90 MB/s
[qbox]  End of command stream 
<real_time> 1.16 </real_time>
<end_time> 2016-04-06T12:25:21Z </end_time>
</fpmd:simulation>
