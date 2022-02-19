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
<start_time> 2016-04-06T12:25:29Z </start_time>
<mpi_processes count="4">
<process id="0"> theobook68 </process>
<process id="1"> theobook68 </process>
<process id="2"> theobook68 </process>
<process id="3"> theobook68 </process>
</mpi_processes>
[qbox] <cmd>set nrowmax 3 </cmd>
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
[qbox] <cmd>atom Si1 silicon  3.700  0.000  1.000</cmd>
[qbox] <cmd>atom Si2 silicon  0.000  2.200  1.000</cmd>
[qbox] <cmd>atom Si3 silicon -3.700  0.000  1.000</cmd>
[qbox] <cmd>atom Si4 silicon  0.000 -2.200  1.000</cmd>
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
 sdcontext: 2x2
 basis size: 511
 c dimensions: 518x8   (259x4 blocks)
 <density_matrix form="diagonal" size="8">
 </density_matrix>
</slater_determinant>
</wavefunction>
<iteration count="1">
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  0.25643576 </eigenvalue_sum>
  <etotal_int>       0.74977894 </etotal_int>
  total_electronic_charge: 15.99999999
  <eigenvalue_sum>  -1.85901561 </eigenvalue_sum>
  Anderson extrapolation: theta=-0.19039585 (-0.19039585)
  <etotal_int>      -3.87279667 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -3.08079023 </eigenvalue_sum>
  Anderson extrapolation: theta=-0.09704876 (-0.09704876)
  <etotal_int>      -6.97300176 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -3.87898291 </eigenvalue_sum>
  Anderson extrapolation: theta=0.56544413 (0.56544413)
  <etotal_int>      -9.93529576 </etotal_int>
  total_electronic_charge: 15.99999999
  <eigenvalue_sum>  -3.70593757 </eigenvalue_sum>
  Anderson extrapolation: theta=0.38342103 (0.38342103)
  <etotal_int>     -12.78400232 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -3.05531692 </eigenvalue_sum>
  Anderson extrapolation: theta=0.33709112 (0.33709112)
  <etotal_int>     -13.76471622 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.82132779 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72203691 (0.72203691)
  <etotal_int>     -14.17478495 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.72803354 </eigenvalue_sum>
  Anderson extrapolation: theta=0.57601520 (0.57601520)
  <etotal_int>     -14.51783209 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.72166156 </eigenvalue_sum>
  Anderson extrapolation: theta=0.62283437 (0.62283437)
  <etotal_int>     -14.73914133 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.72477985 </eigenvalue_sum>
  Anderson extrapolation: theta=0.64038722 (0.64038722)
  <etotal_int>     -14.89065524 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.70969587 </eigenvalue_sum>
  Anderson extrapolation: theta=0.63298551 (0.63298551)
  <etotal_int>     -14.99646234 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.67307821 </eigenvalue_sum>
  Anderson extrapolation: theta=0.67599206 (0.67599206)
  <etotal_int>     -15.07176601 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.62164741 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72640718 (0.72640718)
  <etotal_int>     -15.12979038 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.56478180 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77582381 (0.77582381)
  <etotal_int>     -15.17668797 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.51132657 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82967618 (0.82967618)
  <etotal_int>     -15.21533091 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.46759570 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85822066 (0.85822066)
  <etotal_int>     -15.24739324 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.43780427 </eigenvalue_sum>
  Anderson extrapolation: theta=0.81838848 (0.81838848)
  <etotal_int>     -15.27308643 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.42223929 </eigenvalue_sum>
  Anderson extrapolation: theta=0.73733637 (0.73733637)
  <etotal_int>     -15.29161123 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.41496517 </eigenvalue_sum>
  Anderson extrapolation: theta=0.69695852 (0.69695852)
  <etotal_int>     -15.30353591 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.40965983 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71265654 (0.71265654)
  <etotal_int>     -15.31129225 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.40409941 </eigenvalue_sum>
  Anderson extrapolation: theta=0.74542869 (0.74542869)
  <etotal_int>     -15.31703513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.39827608 </eigenvalue_sum>
  Anderson extrapolation: theta=0.73078957 (0.73078957)
  <etotal_int>     -15.32188290 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.39268408 </eigenvalue_sum>
  Anderson extrapolation: theta=0.80534380 (0.80534380)
  <etotal_int>     -15.32620045 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.38734315 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83469118 (0.83469118)
  <etotal_int>     -15.33048791 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.38244247 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89254935 (0.89254935)
  <etotal_int>     -15.33484471 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.37792374 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91014213 (0.91014213)
  <etotal_int>     -15.33942635 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.37386453 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97378131 (0.97378131)
  <etotal_int>     -15.34417872 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.37013865 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02943696 (1.02943696)
  <etotal_int>     -15.34921834 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36672585 </eigenvalue_sum>
  Anderson extrapolation: theta=1.07471228 (1.07471228)
  <etotal_int>     -15.35454959 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36373231 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02050131 (1.02050131)
  <etotal_int>     -15.36000482 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36149632 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93758730 (0.93758730)
  <etotal_int>     -15.36484919 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.36012850 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90116543 (0.90116543)
  <etotal_int>     -15.36842245 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35946593 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83444706 (0.83444706)
  <etotal_int>     -15.37064603 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35926533 </eigenvalue_sum>
  Anderson extrapolation: theta=0.78244125 (0.78244125)
  <etotal_int>     -15.37169994 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35924323 </eigenvalue_sum>
  Anderson extrapolation: theta=0.69846289 (0.69846289)
  <etotal_int>     -15.37200636 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35916611 </eigenvalue_sum>
  Anderson extrapolation: theta=0.68216920 (0.68216920)
  <etotal_int>     -15.37197940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35896619 </eigenvalue_sum>
  Anderson extrapolation: theta=0.67162229 (0.67162229)
  <etotal_int>     -15.37188244 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35867205 </eigenvalue_sum>
  Anderson extrapolation: theta=0.76291214 (0.76291214)
  <etotal_int>     -15.37181622 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35832249 </eigenvalue_sum>
  Anderson extrapolation: theta=0.79613755 (0.79613755)
  <etotal_int>     -15.37178940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35796201 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88461181 (0.88461181)
  <etotal_int>     -15.37180007 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35760706 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90464281 (0.90464281)
  <etotal_int>     -15.37184157 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35728894 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00814095 (1.00814095)
  <etotal_int>     -15.37190915 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35700505 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02841044 (1.02841044)
  <etotal_int>     -15.37200160 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35677269 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08967920 (1.08967920)
  <etotal_int>     -15.37211358 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35659256 </eigenvalue_sum>
  Anderson extrapolation: theta=1.04295574 (1.04295574)
  <etotal_int>     -15.37224191 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35648017 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03200975 (1.03200975)
  <etotal_int>     -15.37237214 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35643510 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95791120 (0.95791120)
  <etotal_int>     -15.37249409 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35645222 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94130763 (0.94130763)
  <etotal_int>     -15.37259491 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35651543 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89364263 (0.89364263)
  <etotal_int>     -15.37267329 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35660373 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90576850 (0.90576850)
  <etotal_int>     -15.37272963 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670114 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88501694 (0.88501694)
  <etotal_int>     -15.37276948 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35679150 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91011974 (0.91011974)
  <etotal_int>     -15.37279634 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35686759 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88658609 (0.88658609)
  <etotal_int>     -15.37281401 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35692096 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89855815 (0.89855815)
  <etotal_int>     -15.37282464 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35695038 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86174604 (0.86174604)
  <etotal_int>     -15.37283047 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35695536 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86896315 (0.86896315)
  <etotal_int>     -15.37283341 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35694044 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84123550 (0.84123550)
  <etotal_int>     -15.37283521 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35691148 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87042220 (0.87042220)
  <etotal_int>     -15.37283722 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35687398 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86829136 (0.86829136)
  <etotal_int>     -15.37284017 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35683344 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92496824 (0.92496824)
  <etotal_int>     -15.37284441 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35679228 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93627582 (0.93627582)
  <etotal_int>     -15.37285006 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35675398 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99558380 (0.99558380)
  <etotal_int>     -15.37285696 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671952 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99119254 (0.99119254)
  <etotal_int>     -15.37286506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35669175 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02418370 (1.02418370)
  <etotal_int>     -15.37287391 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35667161 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99339959 (0.99339959)
  <etotal_int>     -15.37288322 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35666073 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00190478 (1.00190478)
  <etotal_int>     -15.37289229 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35665876 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96226702 (0.96226702)
  <etotal_int>     -15.37290079 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35666456 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96741674 (0.96741674)
  <etotal_int>     -15.37290816 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35667596 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93529794 (0.93529794)
  <etotal_int>     -15.37291437 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35669016 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94655282 (0.94655282)
  <etotal_int>     -15.37291926 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670495 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92023521 (0.92023521)
  <etotal_int>     -15.37292301 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671800 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93135363 (0.93135363)
  <etotal_int>     -15.37292570 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672822 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90195401 (0.90195401)
  <etotal_int>     -15.37292752 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673466 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90802773 (0.90802773)
  <etotal_int>     -15.37292865 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673744 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87638549 (0.87638549)
  <etotal_int>     -15.37292929 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673695 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88539598 (0.88539598)
  <etotal_int>     -15.37292966 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35673406 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86260189 (0.86260189)
  <etotal_int>     -15.37292991 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672971 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88751381 (0.88751381)
  <etotal_int>     -15.37293020 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672465 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88159791 (0.88159791)
  <etotal_int>     -15.37293060 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671960 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92636733 (0.92636733)
  <etotal_int>     -15.37293117 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671486 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93280889 (0.93280889)
  <etotal_int>     -15.37293190 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671076 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98594734 (0.98594734)
  <etotal_int>     -15.37293280 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670735 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98851419 (0.98851419)
  <etotal_int>     -15.37293387 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670475 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02946444 (1.02946444)
  <etotal_int>     -15.37293505 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670290 </eigenvalue_sum>
  Anderson extrapolation: theta=1.01334005 (1.01334005)
  <etotal_int>     -15.37293633 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670183 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03053757 (1.03053757)
  <etotal_int>     -15.37293762 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670140 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99583285 (0.99583285)
  <etotal_int>     -15.37293886 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670151 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99492848 (0.99492848)
  <etotal_int>     -15.37293997 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670199 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95270000 (0.95270000)
  <etotal_int>     -15.37294089 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670267 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94613767 (0.94613767)
  <etotal_int>     -15.37294157 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670340 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90615496 (0.90615496)
  <etotal_int>     -15.37294204 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670407 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90295272 (0.90295272)
  <etotal_int>     -15.37294231 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670463 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87013380 (0.87013380)
  <etotal_int>     -15.37294244 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670506 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87616254 (0.87616254)
  <etotal_int>     -15.37294249 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670538 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85414213 (0.85414213)
  <etotal_int>     -15.37294249 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670561 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87517815 (0.87517815)
  <etotal_int>     -15.37294250 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670577 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86759535 (0.86759535)
  <etotal_int>     -15.37294253 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670589 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90762642 (0.90762642)
  <etotal_int>     -15.37294258 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670596 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91422196 (0.91422196)
  <etotal_int>     -15.37294268 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670600 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96894055 (0.96894055)
  <etotal_int>     -15.37294281 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670599 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97965978 (0.97965978)
  <etotal_int>     -15.37294297 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670592 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03158917 (1.03158917)
  <etotal_int>     -15.37294317 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670579 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02784799 (1.02784799)
  <etotal_int>     -15.37294339 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670559 </eigenvalue_sum>
  Anderson extrapolation: theta=1.05539662 (1.05539662)
  <etotal_int>     -15.37294363 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670531 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02509558 (1.02509558)
  <etotal_int>     -15.37294387 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670499 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02249624 (1.02249624)
  <etotal_int>     -15.37294410 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670463 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97301629 (0.97301629)
  <etotal_int>     -15.37294430 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670427 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95576598 (0.95576598)
  <etotal_int>     -15.37294445 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670395 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90648431 (0.90648431)
  <etotal_int>     -15.37294455 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670368 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89538099 (0.89538099)
  <etotal_int>     -15.37294461 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670348 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86056187 (0.86056187)
  <etotal_int>     -15.37294464 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670336 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86718393 (0.86718393)
  <etotal_int>     -15.37294465 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670332 </eigenvalue_sum>
  Anderson extrapolation: theta=0.85026874 (0.85026874)
  <etotal_int>     -15.37294465 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670334 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87662877 (0.87662877)
  <etotal_int>     -15.37294465 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670341 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87445363 (0.87445363)
  <etotal_int>     -15.37294465 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670353 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91671191 (0.91671191)
  <etotal_int>     -15.37294466 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670368 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92238514 (0.92238514)
  <etotal_int>     -15.37294468 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97140079 (0.97140079)
  <etotal_int>     -15.37294470 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670400 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97481695 (0.97481695)
  <etotal_int>     -15.37294473 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670416 </eigenvalue_sum>
  Anderson extrapolation: theta=1.01745445 (1.01745445)
  <etotal_int>     -15.37294477 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670430 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00843760 (1.00843760)
  <etotal_int>     -15.37294481 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670441 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03373824 (1.03373824)
  <etotal_int>     -15.37294485 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670447 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00790237 (1.00790237)
  <etotal_int>     -15.37294489 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670449 </eigenvalue_sum>
  Anderson extrapolation: theta=1.01390112 (1.01390112)
  <etotal_int>     -15.37294494 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670446 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97557220 (0.97557220)
  <etotal_int>     -15.37294497 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670439 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96997629 (0.96997629)
  <etotal_int>     -15.37294500 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670427 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92901000 (0.92901000)
  <etotal_int>     -15.37294502 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670414 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92337607 (0.92337607)
  <etotal_int>     -15.37294504 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670400 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88886429 (0.88886429)
  <etotal_int>     -15.37294505 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670387 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89218726 (0.89218726)
  <etotal_int>     -15.37294506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670376 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86877298 (0.86877298)
  <etotal_int>     -15.37294506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670367 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88540074 (0.88540074)
  <etotal_int>     -15.37294506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670362 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87368633 (0.87368633)
  <etotal_int>     -15.37294506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670359 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90411026 (0.90411026)
  <etotal_int>     -15.37294506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670360 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90185790 (0.90185790)
  <etotal_int>     -15.37294506 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670362 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94278370 (0.94278370)
  <etotal_int>     -15.37294507 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670366 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94472746 (0.94472746)
  <etotal_int>     -15.37294507 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670371 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98825297 (0.98825297)
  <etotal_int>     -15.37294508 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670377 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98613634 (0.98613634)
  <etotal_int>     -15.37294508 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670383 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02127245 (1.02127245)
  <etotal_int>     -15.37294509 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670389 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00689574 (1.00689574)
  <etotal_int>     -15.37294510 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670394 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02514513 (1.02514513)
  <etotal_int>     -15.37294511 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670397 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99557947 (0.99557947)
  <etotal_int>     -15.37294511 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670399 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99676865 (0.99676865)
  <etotal_int>     -15.37294512 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670400 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95708002 (0.95708002)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670398 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94982353 (0.94982353)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670395 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91009132 (0.91009132)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670392 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90616620 (0.90616620)
  <etotal_int>     -15.37294513 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670388 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87535652 (0.87535652)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88361364 (0.88361364)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86608491 (0.86608491)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89039280 (0.89039280)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670376 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88592475 (0.88592475)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670375 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92495052 (0.92495052)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670374 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92877039 (0.92877039)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670374 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97486127 (0.97486127)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670375 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97737122 (0.97737122)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670376 </eigenvalue_sum>
  Anderson extrapolation: theta=1.01744119 (1.01744119)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00762664 (1.00762664)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02998884 (1.02998884)
  <etotal_int>     -15.37294514 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00273526 (1.00273526)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670383 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00554684 (1.00554684)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96591509 (0.96591509)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95840773 (0.95840773)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670385 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91788145 (0.91788145)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91320919 (0.91320919)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670384 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88183294 (0.88183294)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670383 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88941468 (0.88941468)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670382 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87151735 (0.87151735)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89472399 (0.89472399)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88930072 (0.88930072)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92589927 (0.92589927)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92753167 (0.92753167)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96974662 (0.96974662)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96944724 (0.96944724)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670378 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00587610 (1.00587610)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99471641 (0.99471641)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=1.01636021 (1.01636021)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99105664 (0.99105664)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670379 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99720206 (0.99720206)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96232069 (0.96232069)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96041144 (0.96041144)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92485980 (0.92485980)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92495131 (0.92495131)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89638366 (0.89638366)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90578230 (0.90578230)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88763140 (0.88763140)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90904632 (0.90904632)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670381 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90057022 (0.90057022)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.93222535 (0.93222535)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92919925 (0.92919925)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96513767 (0.96513767)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96077471 (0.96077471)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99251413 (0.99251413)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98011054 (0.98011054)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00083790 (1.00083790)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97767020 (0.97767020)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98649237 (0.98649237)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95569877 (0.95569877)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95805247 (0.95805247)
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <ekin>         5.34839628 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48138470 </eps>
  <enl>          4.77521379 </enl>
  <ecoul>      -15.60248421 </ecoul>
  <exc>         -4.41268632 </exc>
  <esr>          0.07326880 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37294515 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>      0.00000000 </eefield>
  <enthalpy>   -15.37294515 </enthalpy>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00284363 -0.00000002 -0.00000222 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000003 0.01705783 0.00000241 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00284358 0.00000003 -0.00000221 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000003 -0.01705783 0.00000242 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <timing name="iteration" min="    1.496" max="    1.500"/>
</iteration>
<timing name="         charge" min="    0.354" max="    0.373"/>
<timing name="         energy" min="    0.447" max="    0.468"/>
<timing name="    ortho_align" min="    0.103" max="    0.125"/>
<timing name="      psda_prec" min="    0.003" max="    0.003"/>
<timing name="  psda_residual" min="    0.023" max="    0.047"/>
<timing name=" psda_update_wf" min="    0.006" max="    0.027"/>
<timing name="    update_vhxc" min="    0.457" max="    0.473"/>
<timing name="      wf_update" min="    0.172" max="    0.196"/>
<timing name="           ekin" min="    0.015" max="    0.048"/>
<timing name="            exc" min="    0.269" max="    0.282"/>
<timing name="           hpsi" min="    0.308" max="    0.322"/>
<timing name="       nonlocal" min="    0.109" max="    0.109"/>
<timing name=" charge_compute" min="    0.167" max="    0.188"/>
<timing name="charge_integral" min="    0.018" max="    0.020"/>
<timing name="  charge_rowsum" min="    0.021" max="    0.033"/>
<timing name="     charge_vft" min="    0.127" max="    0.144"/>
[qbox] [qbox] <cmd>set e_field 0 0  0.001</cmd>
[qbox] <cmd>set polarization BERRY</cmd>
[qbox] <cmd>run 0 100</cmd>
  EnergyFunctional: np0v,np1v,np2v: 30 30 30
  EnergyFunctional: vft->np012(): 27000
<e_field> 0.00000000 0.00000000 0.00100000 </e_field>
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
 sdcontext: 2x2
 basis size: 511
 c dimensions: 518x8   (259x4 blocks)
 <density_matrix form="diagonal" size="8">
 </density_matrix>
</slater_determinant>
</wavefunction>
<iteration count="1">
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670380 </eigenvalue_sum>
  <etotal_int>     -15.37294515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670056 </eigenvalue_sum>
  Anderson extrapolation: theta=1.30862457 (1.30862457)
  <etotal_int>     -15.37294022 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35669369 </eigenvalue_sum>
  Anderson extrapolation: theta=0.13795280 (0.13795280)
  <etotal_int>     -15.37291868 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35669685 </eigenvalue_sum>
  Anderson extrapolation: theta=1.62839839 (1.62839839)
  <etotal_int>     -15.37291464 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670525 </eigenvalue_sum>
  Anderson extrapolation: theta=0.21070734 (0.21070734)
  <etotal_int>     -15.37290774 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35670883 </eigenvalue_sum>
  Anderson extrapolation: theta=1.65398446 (1.65398446)
  <etotal_int>     -15.37290685 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671575 </eigenvalue_sum>
  Anderson extrapolation: theta=0.35622973 (0.35622973)
  <etotal_int>     -15.37290548 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35671857 </eigenvalue_sum>
  Anderson extrapolation: theta=1.41172676 (1.41172676)
  <etotal_int>     -15.37290515 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672250 </eigenvalue_sum>
  Anderson extrapolation: theta=0.45194879 (0.45194879)
  <etotal_int>     -15.37290474 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672397 </eigenvalue_sum>
  Anderson extrapolation: theta=1.59604292 (1.59604292)
  <etotal_int>     -15.37290463 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672593 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72244298 (0.72244298)
  <etotal_int>     -15.37290443 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672689 </eigenvalue_sum>
  Anderson extrapolation: theta=1.71908323 (1.71908323)
  <etotal_int>     -15.37290425 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672815 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82180869 (0.82180869)
  <etotal_int>     -15.37290383 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672882 </eigenvalue_sum>
  Anderson extrapolation: theta=1.18420747 (1.18420747)
  <etotal_int>     -15.37290334 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672931 </eigenvalue_sum>
  Anderson extrapolation: theta=0.58868478 (0.58868478)
  <etotal_int>     -15.37290261 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672927 </eigenvalue_sum>
  Anderson extrapolation: theta=0.80714575 (0.80714575)
  <etotal_int>     -15.37290211 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672897 </eigenvalue_sum>
  Anderson extrapolation: theta=0.45308399 (0.45308399)
  <etotal_int>     -15.37290168 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672858 </eigenvalue_sum>
  Anderson extrapolation: theta=0.81666065 (0.81666065)
  <etotal_int>     -15.37290150 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672805 </eigenvalue_sum>
  Anderson extrapolation: theta=0.45660231 (0.45660231)
  <etotal_int>     -15.37290138 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672763 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08716098 (1.08716098)
  <etotal_int>     -15.37290136 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672706 </eigenvalue_sum>
  Anderson extrapolation: theta=0.57385948 (0.57385948)
  <etotal_int>     -15.37290136 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672665 </eigenvalue_sum>
  Anderson extrapolation: theta=1.45529508 (1.45529508)
  <etotal_int>     -15.37290140 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672603 </eigenvalue_sum>
  Anderson extrapolation: theta=0.75093938 (0.75093938)
  <etotal_int>     -15.37290148 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672558 </eigenvalue_sum>
  Anderson extrapolation: theta=1.55653892 (1.55653892)
  <etotal_int>     -15.37290156 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672498 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83810413 (0.83810413)
  <etotal_int>     -15.37290170 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672460 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39027957 (1.39027957)
  <etotal_int>     -15.37290182 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672423 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82090777 (0.82090777)
  <etotal_int>     -15.37290199 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672409 </eigenvalue_sum>
  Anderson extrapolation: theta=1.21730078 (1.21730078)
  <etotal_int>     -15.37290213 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672408 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77568822 (0.77568822)
  <etotal_int>     -15.37290228 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672421 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09197729 (1.09197729)
  <etotal_int>     -15.37290240 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672444 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71034354 (0.71034354)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672467 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98044948 (0.98044948)
  <etotal_int>     -15.37290259 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672493 </eigenvalue_sum>
  Anderson extrapolation: theta=0.62985554 (0.62985554)
  <etotal_int>     -15.37290266 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672510 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91754759 (0.91754759)
  <etotal_int>     -15.37290270 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672523 </eigenvalue_sum>
  Anderson extrapolation: theta=0.57849935 (0.57849935)
  <etotal_int>     -15.37290273 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96915313 (0.96915313)
  <etotal_int>     -15.37290274 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672532 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60071772 (0.60071772)
  <etotal_int>     -15.37290275 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672531 </eigenvalue_sum>
  Anderson extrapolation: theta=1.17280500 (1.17280500)
  <etotal_int>     -15.37290275 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72649547 (0.72649547)
  <etotal_int>     -15.37290274 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672525 </eigenvalue_sum>
  Anderson extrapolation: theta=1.44316342 (1.44316342)
  <etotal_int>     -15.37290273 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672518 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90111820 (0.90111820)
  <etotal_int>     -15.37290272 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672513 </eigenvalue_sum>
  Anderson extrapolation: theta=1.51484293 (1.51484293)
  <etotal_int>     -15.37290269 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672506 </eigenvalue_sum>
  Anderson extrapolation: theta=0.95425183 (0.95425183)
  <etotal_int>     -15.37290266 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672501 </eigenvalue_sum>
  Anderson extrapolation: theta=1.30243473 (1.30243473)
  <etotal_int>     -15.37290262 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672497 </eigenvalue_sum>
  Anderson extrapolation: theta=0.83043077 (0.83043077)
  <etotal_int>     -15.37290256 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672497 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02801421 (1.02801421)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672500 </eigenvalue_sum>
  Anderson extrapolation: theta=0.67639654 (0.67639654)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672505 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88341688 (0.88341688)
  <etotal_int>     -15.37290243 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672511 </eigenvalue_sum>
  Anderson extrapolation: theta=0.59383282 (0.59383282)
  <etotal_int>     -15.37290240 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672517 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89313631 (0.89313631)
  <etotal_int>     -15.37290239 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672523 </eigenvalue_sum>
  Anderson extrapolation: theta=0.58741920 (0.58741920)
  <etotal_int>     -15.37290237 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672527 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03613112 (1.03613112)
  <etotal_int>     -15.37290237 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672531 </eigenvalue_sum>
  Anderson extrapolation: theta=0.65798332 (0.65798332)
  <etotal_int>     -15.37290237 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.26909660 (1.26909660)
  <etotal_int>     -15.37290237 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672538 </eigenvalue_sum>
  Anderson extrapolation: theta=0.79498046 (0.79498046)
  <etotal_int>     -15.37290237 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672540 </eigenvalue_sum>
  Anderson extrapolation: theta=1.44839798 (1.44839798)
  <etotal_int>     -15.37290238 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672542 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91740833 (0.91740833)
  <etotal_int>     -15.37290239 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672543 </eigenvalue_sum>
  Anderson extrapolation: theta=1.42444305 (1.42444305)
  <etotal_int>     -15.37290240 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672543 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92027046 (0.92027046)
  <etotal_int>     -15.37290242 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672542 </eigenvalue_sum>
  Anderson extrapolation: theta=1.22647321 (1.22647321)
  <etotal_int>     -15.37290244 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672540 </eigenvalue_sum>
  Anderson extrapolation: theta=0.80518020 (0.80518020)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672537 </eigenvalue_sum>
  Anderson extrapolation: theta=1.00929405 (1.00929405)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.67586790 (0.67586790)
  <etotal_int>     -15.37290249 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672532 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89390106 (0.89390106)
  <etotal_int>     -15.37290250 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60313038 (0.60313038)
  <etotal_int>     -15.37290250 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.91090581 (0.91090581)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672526 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60218885 (0.60218885)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672525 </eigenvalue_sum>
  Anderson extrapolation: theta=1.05954557 (1.05954557)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672525 </eigenvalue_sum>
  Anderson extrapolation: theta=0.68308542 (0.68308542)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672524 </eigenvalue_sum>
  Anderson extrapolation: theta=1.29412250 (1.29412250)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672524 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82575849 (0.82575849)
  <etotal_int>     -15.37290251 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672524 </eigenvalue_sum>
  Anderson extrapolation: theta=1.44668640 (1.44668640)
  <etotal_int>     -15.37290250 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672524 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92715209 (0.92715209)
  <etotal_int>     -15.37290250 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672524 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37650362 (1.37650362)
  <etotal_int>     -15.37290250 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672524 </eigenvalue_sum>
  Anderson extrapolation: theta=0.89305923 (0.89305923)
  <etotal_int>     -15.37290249 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672525 </eigenvalue_sum>
  Anderson extrapolation: theta=1.16385952 (1.16385952)
  <etotal_int>     -15.37290248 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672526 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77056666 (0.77056666)
  <etotal_int>     -15.37290248 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672526 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98270574 (0.98270574)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672527 </eigenvalue_sum>
  Anderson extrapolation: theta=0.66891085 (0.66891085)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92128397 (0.92128397)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.63314565 (0.63314565)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98104739 (0.98104739)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.66450826 (0.66450826)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=1.12749517 (1.12749517)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.74773938 (0.74773938)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=1.26955783 (1.26955783)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82945311 (0.82945311)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=1.29523506 (1.29523506)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84547086 (0.84547086)
  <etotal_int>     -15.37290246 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=1.20470963 (1.20470963)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.79981810 (0.79981810)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672529 </eigenvalue_sum>
  Anderson extrapolation: theta=1.10092002 (1.10092002)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.75391528 (0.75391528)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=1.06343429 (1.06343429)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.74933103 (0.74933103)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09599345 (1.09599345)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.78031707 (0.78031707)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=1.14219900 (1.14219900)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=0.80524680 (0.80524680)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35672528 </eigenvalue_sum>
  Anderson extrapolation: theta=1.13453831 (1.13453831)
  <etotal_int>     -15.37290247 </etotal_int>
  total_electronic_charge: 16.00000000
  <ekin>         5.34836094 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48134251 </eps>
  <enl>          4.77517496 </enl>
  <ecoul>      -15.60242715 </ecoul>
  <exc>         -4.41266872 </exc>
  <esr>          0.07326880 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37290248 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>     -0.00008536 </eefield>
  <enthalpy>   -15.37298784 </enthalpy>
 <dipole>
   <dipole_ion>     0.0000000000   0.0000000000   0.0000000000 </dipole_ion>
   <dipole_el>     -0.0000000016   0.0000000002   0.0853603022 </dipole_el>
   <dipole_total>  -0.0000000016   0.0000000002   0.0853603022 </dipole_total>
 </dipole>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00284338 -0.00000000 -0.00027011 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000000 0.01706088 0.00027015 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00284338 0.00000000 -0.00027011 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00000000 -0.01706088 0.00027015 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <timing name="iteration" min="    0.983" max="    0.988"/>
</iteration>
<timing name="         charge" min="    0.186" max="    0.200"/>
<timing name="         energy" min="    0.211" max="    0.216"/>
<timing name="    ortho_align" min="    0.049" max="    0.063"/>
<timing name="      psda_prec" min="    0.002" max="    0.002"/>
<timing name="  psda_residual" min="    0.015" max="    0.032"/>
<timing name=" psda_update_wf" min="    0.002" max="    0.016"/>
<timing name="    update_vhxc" min="    0.460" max="    0.472"/>
<timing name="      wf_update" min="    0.085" max="    0.103"/>
<timing name="    mlwf_update" min="    0.071" max="    0.104"/>
<timing name="           ekin" min="    0.005" max="    0.006"/>
<timing name=" el_enth_energy" min="    0.001" max="    0.001"/>
<timing name="            exc" min="    0.134" max="    0.141"/>
<timing name="           hpsi" min="    0.157" max="    0.162"/>
<timing name="       nonlocal" min="    0.046" max="    0.046"/>
<timing name=" charge_compute" min="    0.084" max="    0.106"/>
<timing name="charge_integral" min="    0.009" max="    0.011"/>
<timing name="  charge_rowsum" min="    0.009" max="    0.030"/>
<timing name="     charge_vft" min="    0.061" max="    0.075"/>
[qbox] <cmd>set polarization MLWF_REF</cmd>
[qbox] <cmd>run 0 100</cmd>
  EnergyFunctional: np0v,np1v,np2v: 30 30 30
  EnergyFunctional: vft->np012(): 27000
<e_field> 0.00000000 0.00000000 0.00100000 </e_field>
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
 sdcontext: 2x2
 basis size: 511
 c dimensions: 518x8   (259x4 blocks)
 <density_matrix form="diagonal" size="8">
 </density_matrix>
</slater_determinant>
</wavefunction>
<iteration count="1">
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35660978 </eigenvalue_sum>
  <etotal_int>     -15.37267148 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35661258 </eigenvalue_sum>
  Anderson extrapolation: theta=2.06966218 (2.00000000)
  <etotal_int>     -15.37267213 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35662067 </eigenvalue_sum>
  Anderson extrapolation: theta=0.15825463 (0.15825463)
  <etotal_int>     -15.37267207 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35662381 </eigenvalue_sum>
  Anderson extrapolation: theta=1.46424301 (1.46424301)
  <etotal_int>     -15.37267147 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35662958 </eigenvalue_sum>
  Anderson extrapolation: theta=0.30486133 (0.30486133)
  <etotal_int>     -15.37267033 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663194 </eigenvalue_sum>
  Anderson extrapolation: theta=1.25909894 (1.25909894)
  <etotal_int>     -15.37266990 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663490 </eigenvalue_sum>
  Anderson extrapolation: theta=0.27686083 (0.27686083)
  <etotal_int>     -15.37266940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663556 </eigenvalue_sum>
  Anderson extrapolation: theta=1.12791358 (1.12791358)
  <etotal_int>     -15.37266931 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663608 </eigenvalue_sum>
  Anderson extrapolation: theta=0.32430596 (0.32430596)
  <etotal_int>     -15.37266925 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663606 </eigenvalue_sum>
  Anderson extrapolation: theta=1.27396025 (1.27396025)
  <etotal_int>     -15.37266926 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663593 </eigenvalue_sum>
  Anderson extrapolation: theta=0.34281447 (0.34281447)
  <etotal_int>     -15.37266929 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663581 </eigenvalue_sum>
  Anderson extrapolation: theta=1.23142933 (1.23142933)
  <etotal_int>     -15.37266931 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663563 </eigenvalue_sum>
  Anderson extrapolation: theta=0.38062974 (0.38062974)
  <etotal_int>     -15.37266934 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663555 </eigenvalue_sum>
  Anderson extrapolation: theta=1.39475251 (1.39475251)
  <etotal_int>     -15.37266936 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663543 </eigenvalue_sum>
  Anderson extrapolation: theta=0.46306325 (0.46306325)
  <etotal_int>     -15.37266938 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663537 </eigenvalue_sum>
  Anderson extrapolation: theta=1.29200390 (1.29200390)
  <etotal_int>     -15.37266939 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663532 </eigenvalue_sum>
  Anderson extrapolation: theta=0.43079331 (0.43079331)
  <etotal_int>     -15.37266940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663530 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08960835 (1.08960835)
  <etotal_int>     -15.37266940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663529 </eigenvalue_sum>
  Anderson extrapolation: theta=0.40058953 (0.40058953)
  <etotal_int>     -15.37266940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663530 </eigenvalue_sum>
  Anderson extrapolation: theta=1.16424634 (1.16424634)
  <etotal_int>     -15.37266940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663530 </eigenvalue_sum>
  Anderson extrapolation: theta=0.45772981 (0.45772981)
  <etotal_int>     -15.37266940 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663531 </eigenvalue_sum>
  Anderson extrapolation: theta=1.35824238 (1.35824238)
  <etotal_int>     -15.37266939 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663532 </eigenvalue_sum>
  Anderson extrapolation: theta=0.55018354 (0.55018354)
  <etotal_int>     -15.37266939 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663532 </eigenvalue_sum>
  Anderson extrapolation: theta=1.33787507 (1.33787507)
  <etotal_int>     -15.37266939 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663533 </eigenvalue_sum>
  Anderson extrapolation: theta=0.56342345 (0.56342345)
  <etotal_int>     -15.37266938 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663533 </eigenvalue_sum>
  Anderson extrapolation: theta=1.15716878 (1.15716878)
  <etotal_int>     -15.37266938 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.53380393 (0.53380393)
  <etotal_int>     -15.37266938 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08366678 (1.08366678)
  <etotal_int>     -15.37266938 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.54553241 (0.54553241)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.12813565 (1.12813565)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.59976708 (0.59976708)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.17680886 (1.17680886)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.64249978 (0.64249978)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.11862963 (1.11862963)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.61248016 (0.61248016)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.98651189 (0.98651189)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.54763596 (0.54763596)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92867152 (0.92867152)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.52475600 (0.52475600)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99432388 (0.99432388)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.55539417 (0.55539417)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.11138596 (1.11138596)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.61539278 (0.61539278)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.22038444 (1.22038444)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71704784 (0.71704784)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.34704227 (1.34704227)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86077113 (0.86077113)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.37281481 (1.37281481)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88966723 (0.88966723)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.14060033 (1.14060033)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72770335 (0.72770335)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86707656 (0.86707656)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.57601091 (0.57601091)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77611675 (0.77611675)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.53566664 (0.53566664)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87495234 (0.87495234)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60172963 (0.60172963)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.11085120 (1.11085120)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.74966930 (0.74966930)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.31295872 (1.31295872)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87846969 (0.87846969)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.32192475 (1.32192475)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90770158 (0.90770158)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.20940361 (1.20940361)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86535627 (0.86535627)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.07997181 (1.07997181)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.79487341 (0.79487341)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.96688002 (0.96688002)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71916759 (0.71916759)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88702301 (0.88702301)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.66159432 (0.66159432)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86743104 (0.86743104)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.65001138 (0.65001138)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.94032018 (0.94032018)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71514130 (0.71514130)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.11858615 (1.11858615)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.86282099 (0.86282099)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.30828075 (1.30828075)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.99749950 (0.99749950)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.31671482 (1.31671482)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.97495772 (0.97495772)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.12266933 (1.12266933)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82437926 (0.82437926)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.92131987 (0.92131987)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.70292058 (0.70292058)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84898258 (0.84898258)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.67684515 (0.67684515)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.90876296 (0.90876296)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.73420702 (0.73420702)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.04554298 (1.04554298)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82920851 (0.82920851)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.15235519 (1.15235519)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.88769370 (0.88769370)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.15322467 (1.15322467)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.87893522 (0.87893522)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08998831 (1.08998831)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.84252759 (0.84252759)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.03813066 (1.03813066)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.82209891 (0.82209891)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.02794787 (1.02794787)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <ekin>         5.34834545 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48133990 </eps>
  <enl>          4.77517621 </enl>
  <ecoul>      -15.60242050 </ecoul>
  <exc>         -4.41265866 </exc>
  <esr>          0.07326880 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37289740 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>     -0.00009778 </eefield>
  <enthalpy>   -15.37299518 </enthalpy>
 <mlwf_set size="8">
 <mlwf center="  0.93172504   0.00000000   1.32834554 "
       spread=" 2.34759969 "/>
 <mlwf_ref center="  0.90412208   0.00000000   1.31463731 "/>
 <mlwf center="  0.07466192  -0.00000000   0.40890497 "
       spread=" 2.99787754 "/>
 <mlwf_ref center="  0.06091886  -0.00000000   0.53711439 "/>
 <mlwf center="  4.65130709  -0.00000000   0.99449085 "
       spread=" 2.22829011 "/>
 <mlwf_ref center="  4.59135467  -0.00000000   0.99397975 "/>
 <mlwf center=" -1.73958497   1.64357211   1.06255877 "
       spread=" 2.28902730 "/>
 <mlwf_ref center=" -1.62661690   1.59779627   1.06341210 "/>
 <mlwf center=" -1.73958497  -1.64357211   1.06255878 "
       spread=" 2.28902730 "/>
 <mlwf_ref center=" -1.62661690  -1.59779627   1.06341210 "/>
 <mlwf center=" -4.66380004  -0.00000000   0.98889503 "
       spread=" 2.25271866 "/>
 <mlwf_ref center=" -4.58576035  -0.00000000   0.98832458 "/>
 <mlwf center="  1.14390443  -2.57153702   0.99567056 "
       spread=" 2.53535609 "/>
 <mlwf_ref center="  1.12183414  -2.42729854   0.99511534 "/>
 <mlwf center="  1.14390443   2.57153702   0.99567056 "
       spread=" 2.53535609 "/>
 <mlwf_ref center="  1.12183414   2.42729854   0.99511534 "/>
 </mlwf_set>
 <dipole>
   <dipole_ion>     0.0000000000   0.0000000000   0.0000000000 </dipole_ion>
   <dipole_el>      0.0778605294  -0.0000000002   0.0977781764 </dipole_el>
   <dipole_total>   0.0778605294  -0.0000000002   0.0977781764 </dipole_total>
 </dipole>
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00284432 0.00000000 -0.00026400 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000005 0.01706233 0.00027265 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00284425 -0.00000000 -0.00026421 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000005 -0.01706233 0.00027265 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <timing name="iteration" min="    0.961" max="    0.969"/>
</iteration>
<timing name="         charge" min="    0.177" max="    0.192"/>
<timing name="         energy" min="    0.206" max="    0.215"/>
<timing name="    ortho_align" min="    0.049" max="    0.063"/>
<timing name="      psda_prec" min="    0.001" max="    0.002"/>
<timing name="  psda_residual" min="    0.011" max="    0.028"/>
<timing name=" psda_update_wf" min="    0.002" max="    0.016"/>
<timing name="    update_vhxc" min="    0.452" max="    0.467"/>
<timing name="      wf_update" min="    0.083" max="    0.100"/>
<timing name="     correction" min="    0.116" max="    0.116"/>
<timing name="           dsum" min="    0.001" max="    0.001"/>
<timing name="             ft" min="    0.033" max="    0.040"/>
<timing name="     mlwf_trans" min="    0.028" max="    0.029"/>
<timing name="    mlwf_update" min="    0.069" max="    0.096"/>
<timing name="           real" min="    0.062" max="    0.066"/>
<timing name="           ekin" min="    0.005" max="    0.005"/>
<timing name=" el_enth_energy" min="    0.001" max="    0.001"/>
<timing name="            exc" min="    0.133" max="    0.143"/>
<timing name="           hpsi" min="    0.153" max="    0.161"/>
<timing name="       nonlocal" min="    0.046" max="    0.046"/>
<timing name=" charge_compute" min="    0.085" max="    0.098"/>
<timing name="charge_integral" min="    0.008" max="    0.009"/>
<timing name="  charge_rowsum" min="    0.008" max="    0.021"/>
<timing name="     charge_vft" min="    0.061" max="    0.077"/>
[qbox] <cmd>set polarization MLWF_REF_Q</cmd>
[qbox] <cmd>run 0 100</cmd>
  EnergyFunctional: np0v,np1v,np2v: 30 30 30
  EnergyFunctional: vft->np012(): 27000
<e_field> 0.00000000 0.00000000 0.00100000 </e_field>
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
 sdcontext: 2x2
 basis size: 511
 c dimensions: 518x8   (259x4 blocks)
 <density_matrix form="diagonal" size="8">
 </density_matrix>
</slater_determinant>
</wavefunction>
<iteration count="1">
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=23.13629241 (2.00000000)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=7.18529394 (2.00000000)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=2.31958252 (2.00000000)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.18518998 (0.18518998)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.65175681 (0.65175681)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.34574245 (1.34574245)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.57173693 (0.57173693)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.22349746 (1.22349746)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.54151219 (0.54151219)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.29669620 (1.29669620)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.56382762 (0.56382762)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.42850444 (1.42850444)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60766988 (0.60766988)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.48272916 (1.48272916)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.63623983 (0.63623983)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.43406545 (1.43406545)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.63255925 (0.63255925)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.34133746 (1.34133746)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60178702 (0.60178702)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.26624044 (1.26624044)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.56556351 (0.56556351)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.26378098 (1.26378098)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.55636250 (0.55636250)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.36959990 (1.36959990)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.60320055 (0.60320055)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.53975367 (1.53975367)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.69837099 (0.69837099)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.60785916 (1.60785916)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.76462319 (0.76462319)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.46149933 (1.46149933)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72596275 (0.72596275)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.22176824 (1.22176824)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.62395889 (0.62395889)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.07349003 (1.07349003)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.54551630 (0.54551630)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.09175567 (1.09175567)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.52604231 (0.52604231)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.27330674 (1.27330674)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.57779775 (0.57779775)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.53127811 (1.53127811)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.68697290 (0.68697290)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.65937669 (1.65937669)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77685814 (0.77685814)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.54691605 (1.54691605)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77285878 (0.77285878)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.31720721 (1.31720721)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.69448421 (0.69448421)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.13931020 (1.13931020)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.61658973 (0.61658973)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.08909775 (1.08909775)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.58071757 (0.58071757)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.16222754 (1.16222754)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.59255456 (0.59255456)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.31033056 (1.31033056)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.64117730 (0.64117730)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.43075668 (1.43075668)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.69114903 (0.69114903)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.44183573 (1.44183573)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71139168 (0.71139168)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.36909467 (1.36909467)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.70619131 (0.70619131)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.30040182 (1.30040182)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.70165729 (0.70165729)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.27866494 (1.27866494)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.70744280 (0.70744280)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.27884709 (1.27884709)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.70902648 (0.70902648)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.25345080 (1.25345080)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.69191672 (0.69191672)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.19579093 (1.19579093)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.65588892 (0.65588892)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.16190591 (1.16190591)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.62706467 (0.62706467)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.19117815 (1.19117815)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.63033975 (0.63033975)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.29228535 (1.29228535)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.67554562 (0.67554562)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.40326416 (1.40326416)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.74339552 (0.74339552)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.44192121 (1.44192121)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.78756016 (0.78756016)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.36574279 (1.36574279)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.77498338 (0.77498338)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.23990518 (1.23990518)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.72065677 (0.72065677)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.14820808 (1.14820808)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.66183802 (0.66183802)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.12587170 (1.12587170)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.63635652 (0.63635652)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.16350723 (1.16350723)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.63592980 (0.63592980)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.24953248 (1.24953248)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.66624876 (0.66624876)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.31192320 (1.31192320)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.71106288 (0.71106288)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.35365632 (1.35365632)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.73778761 (0.73778761)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=1.38428279 (1.38428279)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <eigenvalue_sum>  -2.35663534 </eigenvalue_sum>
  Anderson extrapolation: theta=0.74566310 (0.74566310)
  <etotal_int>     -15.37266937 </etotal_int>
  total_electronic_charge: 16.00000000
  <ekin>         5.34834545 </ekin>
  <econf>        0.00000000 </econf>
  <eps>         -5.48133990 </eps>
  <enl>          4.77517621 </enl>
  <ecoul>      -15.60242050 </ecoul>
  <exc>         -4.41265866 </exc>
  <esr>          0.07326880 </esr>
  <eself>       17.02153730 </eself>
  <ets>          0.00000000 </ets>
  <eexf>         0.00000000 </eexf>
  <etotal>     -15.37289740 </etotal>
  <epv>          0.00000000 </epv>
  <eefield>     -0.00009778 </eefield>
  <enthalpy>   -15.37299518 </enthalpy>
 <mlwf_set size="8">
 <mlwf center="  0.93172504   0.00000000   1.32834555 "
       spread=" 2.34759970 "/>
 <mlwf_ref center="  0.90412208   0.00000000   1.31463731 " 
     spread=" 2.62985939 "/>
    <quad>  2.41362801   3.01362625   1.48890614  -0.00000000   0.10278995  -0.00000000 </quad>
 <mlwf center="  0.07466192  -0.00000000   0.40890496 "
       spread=" 2.99787753 "/>
 <mlwf_ref center="  0.06091886  -0.00000000   0.53711438 " 
     spread=" 3.46827544 "/>
    <quad>  4.73484362   3.06290264   4.23118825   0.00000000  -0.16434459   0.00000000 </quad>
 <mlwf center="  4.65130709  -0.00000000   0.99449085 "
       spread=" 2.22829011 "/>
 <mlwf_ref center="  4.59135467  -0.00000000   0.99397975 " 
     spread=" 2.43044435 "/>
    <quad>  1.96205503   1.93065293   2.01435178   0.00000000   0.00057578  -0.00000000 </quad>
 <mlwf center=" -1.73958497   1.64357211   1.06255878 "
       spread=" 2.28902730 "/>
 <mlwf_ref center=" -1.62661690   1.59779627   1.06341210 " 
     spread=" 2.55107914 "/>
    <quad>  2.78981944   2.24592110   1.47226427   0.11467310  -0.01042877   0.01911152 </quad>
 <mlwf center=" -1.73958497  -1.64357211   1.06255878 "
       spread=" 2.28902730 "/>
 <mlwf_ref center=" -1.62661690  -1.59779627   1.06341210 " 
     spread=" 2.55107914 "/>
    <quad>  2.78981944   2.24592110   1.47226427  -0.11467310  -0.01042877  -0.01911152 </quad>
 <mlwf center=" -4.66380004  -0.00000000   0.98889502 "
       spread=" 2.25271866 "/>
 <mlwf_ref center=" -4.58576035  -0.00000000   0.98832458 " 
     spread=" 2.46678240 "/>
    <quad>  2.17718925   1.90644682   2.00137936   0.00000000   0.00208296   0.00000000 </quad>
 <mlwf center="  1.14390443  -2.57153702   0.99567056 "
       spread=" 2.53535609 "/>
 <mlwf_ref center="  1.12183414  -2.42729854   0.99511534 " 
     spread=" 2.85751528 "/>
    <quad>  2.77911897   3.58669187   1.79958272   0.25115226   0.00256071   0.00360650 </quad>
 <mlwf center="  1.14390443   2.57153702   0.99567056 "
       spread=" 2.53535609 "/>
 <mlwf_ref center="  1.12183414   2.42729854   0.99511534 " 
     spread=" 2.85751528 "/>
    <quad>  2.77911897   3.58669187   1.79958272  -0.25115226   0.00256071  -0.00360650 </quad>
 </mlwf_set>
 <dipole>
   <dipole_ion>     0.0000000000   0.0000000000   0.0000000000 </dipole_ion>
   <dipole_el>      0.0778605292  -0.0000000000   0.0977781797 </dipole_el>
   <dipole_total>   0.0778605292  -0.0000000000   0.0977781797 </dipole_total>
 </dipole>
 <quadrupole> 
   <quadrupole_ion> 
  109.52000000     0.00000000     0.00000000
    0.00000000    38.72000000     0.00000000
    0.00000000     0.00000000    16.00000000
   </quadrupole_ion>
   <quadrupole_el> 
 -150.70862710     0.00000000     0.42338902
    0.00000000   -80.41423689    -0.00000000
    0.42338902    -0.00000000   -48.83786426
   </quadrupole_el>
   <quadrupole_total> 
  -41.18862710     0.00000000     0.42338902
    0.00000000   -41.69423689    -0.00000000
    0.42338902    -0.00000000   -32.83786426
   </quadrupole_total>
   <traceless_quadrupole> 
   -2.61505102     0.00000000     0.42338902
    0.00000000    -3.12066080    -0.00000000
    0.42338902    -0.00000000     5.73571183
   </traceless_quadrupole>
   <traceless_quadrupole_eigval> 
    -3.12066080 -2.63646222 5.75712302
   </traceless_quadrupole_eigval>
   <traceless_quadrupole_eigvec> 
   -0.00000000    -0.99872374     0.05050643
    1.00000000    -0.00000000    -0.00000000
    0.00000000     0.05050643     0.99872374
   </traceless_quadrupole_eigvec>
 </quadrupole> 
<atomset>
<unit_cell 
    a=" 16.00000000   0.00000000   0.00000000"
    b="  0.00000000  16.00000000   0.00000000"
    c="  0.00000000   0.00000000  16.00000000" />
  <atom name="Si1" species="silicon">
    <position> 3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> 0.00284432 0.00000000 -0.00026400 </force>
  </atom>
  <atom name="Si2" species="silicon">
    <position> 0.00000000 2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000005 0.01706233 0.00027265 </force>
  </atom>
  <atom name="Si3" species="silicon">
    <position> -3.70000000 0.00000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00284425 -0.00000000 -0.00026421 </force>
  </atom>
  <atom name="Si4" species="silicon">
    <position> 0.00000000 -2.20000000 1.00000000 </position>
    <velocity> 0.00000000 0.00000000 0.00000000 </velocity>
    <force> -0.00000005 -0.01706233 0.00027265 </force>
  </atom>
</atomset>
<unit_cell_a_norm> 16.000000 </unit_cell_a_norm>
<unit_cell_b_norm> 16.000000 </unit_cell_b_norm>
<unit_cell_c_norm> 16.000000 </unit_cell_c_norm>
<unit_cell_alpha>  90.000 </unit_cell_alpha>
<unit_cell_beta>   90.000 </unit_cell_beta>
<unit_cell_gamma>  90.000 </unit_cell_gamma>
<unit_cell_volume> 4096.000 </unit_cell_volume>
  <timing name="iteration" min="    0.994" max="    1.094"/>
</iteration>
<timing name="         charge" min="    0.175" max="    0.188"/>
<timing name="         energy" min="    0.213" max="    0.222"/>
<timing name="    ortho_align" min="    0.051" max="    0.066"/>
<timing name="      psda_prec" min="    0.001" max="    0.002"/>
<timing name="  psda_residual" min="    0.011" max="    0.028"/>
<timing name=" psda_update_wf" min="    0.002" max="    0.016"/>
<timing name="    update_vhxc" min="    0.480" max="    0.487"/>
<timing name="      wf_update" min="    0.085" max="    0.102"/>
<timing name="     correction" min="    0.128" max="    0.128"/>
<timing name="           dsum" min="    0.001" max="    0.001"/>
<timing name="             ft" min="    0.033" max="    0.046"/>
<timing name="     mlwf_trans" min="    0.021" max="    0.022"/>
<timing name="    mlwf_update" min="    0.084" max="    0.099"/>
<timing name="           real" min="    0.067" max="    0.079"/>
<timing name="           ekin" min="    0.005" max="    0.005"/>
<timing name=" el_enth_energy" min="    0.001" max="    0.001"/>
<timing name="            exc" min="    0.141" max="    0.142"/>
<timing name="           hpsi" min="    0.153" max="    0.162"/>
<timing name="       nonlocal" min="    0.053" max="    0.053"/>
<timing name=" charge_compute" min="    0.084" max="    0.097"/>
<timing name="charge_integral" min="    0.009" max="    0.010"/>
<timing name="  charge_rowsum" min="    0.009" max="    0.022"/>
<timing name="     charge_vft" min="    0.060" max="    0.072"/>
[qbox]  End of command stream 
<real_time> 4.664 </real_time>
<end_time> 2016-04-06T12:25:34Z </end_time>
</fpmd:simulation>
