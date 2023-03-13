#####################################
#
#  Variables
#
#####################################

Beta                    = 386.80
U_wechselwirk           = 10.0
J_Hund                  = 1.0
Density_Required        = 21.0
LDA_Chemical_potential  = -4.1
Chemical_potential      = -4.0
N_DMFT_Iterations       = 1
Charge_Self_Consistency = False

#####################################
#
#  Solver
#
#####################################
#from Solver_RI import Solver_2_or_3_bands_Hubbard_RI_1_0
#import pytriqs.utility.mpi as MPI

from Solver_RI import Solver_5_band_Hubbard
import pytriqs.utility.mpi as MPI

#S_ti = Solver_2_or_3_bands_Hubbard_RI_1_0(Beta = Beta, Norb = 5, U_interact = U_wechselwirk, J_Hund = J_Hund, J_C = J_Hund)
S_ti = Solver_5_band_Hubbard(Beta = Beta)

mixing_coefficient    = 0.47

n_cycles              = 1500000000/MPI.size
n_warmup_cycles       = 5000000
legendre_accumulation = False
n_legendre            = 90
time_accumulation     = True
fit_start             = 500
fit_stop              = 700
use_segment_picture   = False


#####################################
#
#  SumK
#
#####################################

from sumk_from_lda_projections_mbpp import *
SK = SumKFromLDAProjectionsMBPP (Substract_Fermi_energy = False)

from DFT_step import DFT_step
dftstep = DFT_step(Code="mbpp")   # <-- dran denken!

#####################################
#
#  N-Matrix
#
#####################################

import Nmatrix

Nm_up = Nmatrix.DeltaN(N_kpts=SK.n_kpts(), Bloch_Indices=SK.GFBlocBlochIndices, Hopping=SK.hopping, Projection=SK.Projection, Copy=False)


#####################################
#
#  Green's functions
#
#####################################

G = BlockGf (name_block_generator = [ (s, GfImFreq(indices = SK.GFBlocIndices, mesh = S_ti.G_iw.mesh)) for s in ['up','down'] ], make_copies = False)
Sigma = G.copy()
Gbl = BlockGf (name_block_generator = [ (s, GfImFreq(indices = SK.GFBlocBlochIndices, mesh = S_ti.G_iw.mesh)) for s in ['up','down'] ], make_copies = False)
Gbltau = BlockGf (name_block_generator = [ (s, GfImTime(indices = SK.GFBlocBlochIndices, beta = Beta, n_points = 4099)) for s in ['up','down'] ], make_copies = False)

#####################################
#
#  Double Counting
#
#####################################

Sigma_zero = G.copy()
Sigma_zero.zero()
DC = G.copy()
Gu_imp = G.copy()
DC_imp = G.copy()

# Opens the results shelve
#Results = HDF_Archive("Results.h5",'w')

#####################################
#
#  Load previous result
#
#####################################
from pytriqs.archive import *

try:
  A = HDFArchive("LTO.h5", 'r')
  S_ti.Sigma_iw << A["Sigma_next"]

  del A
except IOError: pass

#####################################
#
#  Main DMFT loop
#
#####################################
import os
import pytriqs.utility.dichotomy as dichotomy
import shutil

for iteration_number in range(1, N_DMFT_Iterations + 1):
   if os.path.exists('STOP'): break #together
   MPI.report("\nIteration Number = %d"%iteration_number)
   
   # Initial computation of the Sum over k to get LDA occupation numbers
   F0 = lambda mu : SK(mu = mu, Sigma = Sigma_zero, Project = False).total_density()

   if ((iteration_number <= 1) or Charge_Self_Consistency):
      if Density_Required and (iteration_number > 0):
         LDA_Chemical_potential = dichotomy.dichotomy(function       = F0,
                                                      x_init         = LDA_Chemical_potential,
                                                      y_value        = Density_Required,
                                                      precision_on_y = 0.000001,
                                                      delta_x        = 0.5,
                                                      max_loops      = 100,
                                                      x_name         = "LDA_Chemical_Potential",
                                                      y_name         = "Total Density",
                                                      verbosity      = 3)[0]
      else:
         MPI.report("No adjustment of LDA chemical potential.\nTotal density = %.3f"%F0(LDA_Chemical_potential))

      MPI.report("Total density of LDA GF = %.3f"%SK(mu = LDA_Chemical_potential, Sigma = Sigma_zero, DoubleCounting = None, Res = G, Project = True).total_density())

      # Calculation of Double Counting correction
#      SK.FLL(U_interact = U_wechselwirk, J_Hund = J_Hund, LDA_Occupations = G.density(), Res = DC)
#      DC = 1.0*DC # <---------------------------------
#      for ind, Gflock in DC:
#         MPI.report("Double counting correction for block " + ind + ': ' + str(Gflock.data[0,0,0].real))

      for k in range(1):   # Number of impurities

         for s in ['up', 'down']:
            for i in range(5):
               for j in range(5):
                  Gu_imp[s][i, j] = G[s][5*k+i, 5*k+j]

         SK.FLL(U_interact = U_wechselwirk, J_Hund = J_Hund, LDA_Occupations = Gu_imp.density(), Res = DC_imp)

         for s in ['up', 'down']:
            for i in range(5):
               for j in range(5):
                  DC[s][5*k+i, 5*k+j] = DC_imp[s][i,j]

   #Embedding(self):
   k = 0
   for i in range(5):
     for j in range(5):
       for s in [ 'up', 'down' ]:
         Sigma[s][i+k,j+k] = 0.5 * (S_ti.Sigma_iw['up'][i,j] + S_ti.Sigma_iw['down'][i,j])
#        Sigma[s][i+k,j+k] = S_ti1.Sigma[s][i,j]
#
   if Charge_Self_Consistency:
      # Compute the SumK for the determination of the NMatrix
      Fbl = lambda mu : SK(mu = mu, Sigma = Sigma, DoubleCounting = DC, Res = Gbl, Project = False).total_density()

      if Density_Required and (iteration_number > 0):
         Chemical_potential = dichotomy.dichotomy(function = Fbl,
                                                  x_init         = Chemical_potential,
                                                  y_value        = Density_Required,
                                                  precision_on_y = 0.000001,
                                                  delta_x        = 0.5,
                                                  max_loops      = 100,
                                                  x_name         = "Nmatrix_Chemical_Potential",
                                                  y_name         = "Total Density",
                                                  verbosity      = 3)[0]
      else:
         MPI.report("No adjustment of Nmatrix chemical potential\nTotal density = %.3f"%Fbl(Chemical_potential))
      
      Nm_up(mu = Chemical_potential, SelectedBlock = 'up', mu_KS =  LDA_Chemical_potential, Sigma = Sigma,
             DoubleCounting = DC, Hopping = SK.hopping, Projection = SK.Projection, Normalize = False)
      
      if (MPI.is_master_node()):
         Nm_up.save("NMATRIX", False)

      #DFT:
      print("dft_step")
      dftstep(G = G, Sigma = Sigma - DC)
      print("dft_step2")
      SK.reread()
   print("dft_step3")
   # Compute the SumK, possibly fixing mu by dichotomy
   Fbl = lambda mu : SK(mu = mu, Sigma = Sigma, DoubleCounting = DC, Res = Gbl, Project = False).total_density()
   
   if Density_Required and (iteration_number > 0):
      Chemical_potential = dichotomy.dichotomy(function = Fbl,
                                               x_init         = Chemical_potential,
                                               y_value        = Density_Required,
                                               precision_on_y = 0.000001,
                                               delta_x        = 0.5,
                                               max_loops      = 100,
                                               x_name         = "Chemical_Potential",
                                               y_name         = "Total Density",
                                               verbosity      = 3)[0]
   else:
      MPI.report("No adjustment of chemical potential\nTotal density = %.3f"%Fbl(Chemical_potential))

   MPI.report("Total density of projected (impurity) GF = %.3f"%SK(mu = Chemical_potential, Sigma = Sigma, DoubleCounting = DC, Res = G, Project = True).total_density())

   MPI.report('Occupation matrix')
   MPI.report(G['up'].density().real )
   MPI.report(G['down'].density().real)

   density_matrix1 = G['up'].density() + G['down'].density()
   MPI.report('Diagonal occupations')
   for i in range(5):
      MPI.report(density_matrix1[i,i])

   for ind, Gbli in Gbl:
      #print Gbltau.mesh
      #print S_ti.G_iw.mesh
      Gbltau[ind].set_from_inverse_fourier(Gbli)

   dftstep.calculate_two_particle_energy(G = G, Sigma = Sigma - DC)

   #Extraction(self):
   for i in range(5):
      for j in range(5):
         for s in [ 'up', 'down' ]:
            S_ti.G_iw[s][i,j]     = G[s][i,j]
            S_ti.Sigma_iw[s][i,j] = Sigma[s][i,j]

#   for s in [ 'up', 'down' ]:
#      S_ti.Sigma_iw[s][1,1] = (S_ti.Sigma_iw[s][1,1] + S_ti.Sigma_iw[s][2,2] + S_ti.Sigma_iw[s][4,4])/3.0
#      S_ti.Sigma_iw[s][2,2] = S_ti.Sigma_iw[s][1,1]      
#      S_ti.Sigma_iw[s][4,4] = S_ti.Sigma_iw[s][1,1]

   
   S_ti.G0_iw << inverse(S_ti.Sigma_iw + inverse(S_ti.G_iw))   # Finally get S.G0

   if (MPI.is_master_node()):
      R = HDFArchive("LTO.h5",'w')
      R["G"] = G
      R["Sigma"] = Sigma
      R["Gbltau"] = Gbltau
      
   p = {}
   p["h_loc"] = S_ti.Hamiltonian
   p["max_time"] = -1
   p["random_name"] = ""
   p["random_seed"] = 123 * mpi.rank + 567
   p["length_cycle"] = 50
   p["n_warmup_cycles"] = n_warmup_cycles
   p["n_cycles"] = n_cycles
#   p["partition_method"] = "quantum_numbers" 
   p["partition_method"] = "autopartition" 
#   p["perform_post_proc"] = True   
   p["perform_tail_fit"] = True
   p["fit_min_n"] = fit_start   
   p["fit_max_n"] = fit_stop

   QN=[S_ti.QuantumNumbers["Sz"],S_ti.QuantumNumbers["Ntot"]]
   #print ("Sz: ")
   #print S_ti.QuantumNumbers["Sz"]
   #print ("Ntot: ")
   #print S_ti.QuantumNumbers["Ntot"]
   #print QN   
   
   if p["partition_method"] == "quantum_numbers": p["quantum_numbers"] = QN
   print p
   S_ti.solve(**p)

   for s in [ 'up', 'down' ]:
      S_ti.Sigma_iw[s][1,1] = 0.5 * (S_ti.Sigma_iw[s][1,1] + S_ti.Sigma_iw[s][2,2])
      S_ti.Sigma_iw[s][2,2] = S_ti.Sigma_iw[s][1,1]
#      S_ti.Sigma_iw[s][3,3] = S_ti.Sigma_iw[s][0,0]
#      S_ti.Sigma_iw[s][4,4] = S_ti.Sigma_iw[s][1,1]


   if (MPI.is_master_node()):
      R["G_tau"] = S_ti.G_tau
      R["Sigma_next"] = S_ti.Sigma_iw
      del R
      
   for i in range(5):
     fobj_out = open("Sigma_"+ str(i) + "-" + str(i) + "_down.dat","w")
     for iw, w in enumerate(S_ti.Sigma_iw['down'][i,i].mesh):
       fobj_out.write(repr(w.imag) + '  ' +  repr(S_ti.Sigma_iw['down'].data[iw][i,i].real) + '  ' + repr(S_ti.Sigma_iw['down'].data[iw][i,i].imag) + '\n')
     fobj_out.close()
      
   for i in range(5):
     fobj_out = open("G_tau_"+ str(i) + "-" + str(i) + "_down.dat","w")
     for iw, w in enumerate(S_ti.G_tau['down'][i,i].mesh):
       fobj_out.write(repr(w.real) + '  ' +  repr(S_ti.G_tau['down'].data[iw][i,i].real) + '\n')
     fobj_out.close()

   for i in range(12):
     fobj_out = open("Gbltau_"+ str(i) + "-" + str(i) + "_down.dat","w")
     for iw, w in enumerate(Gbltau['down'][i,i].mesh):
       fobj_out.write(repr(w.real) + '  ' +  repr(Gbltau['down'].data[iw][i,i].real) + '\n')
     fobj_out.close()

   #print ("Sigma_old")
   #print (S_ti.Sigma_old)
   S_ti.Sigma_iw = mixing_coefficient * S_ti.Sigma_iw + (1.0 - mixing_coefficient) * S_ti.Sigma_old
   S_ti.Sigma_old = S_ti.Sigma_iw.copy()
   
   # Compute the SumK for the determination of the NMatrix
   Fbl = lambda mu : SK(mu = mu, Sigma = Sigma, DoubleCounting = DC, Res = Gbl, Project = False).total_density()

   #if Charge_Self_Consistency:

   if Density_Required and (iteration_number > 0):
      Chemical_potential = dichotomy.dichotomy(function = Fbl,
                                                  x_init         = Chemical_potential,
                                                  y_value        = Density_Required,
                                                  precision_on_y = 0.000001,
                                                  delta_x        = 0.5,
                                                  max_loops      = 100,
                                                  x_name         = "Nmatrix_Chemical_Potential",
                                                  y_name         = "Total Density",
                                                  verbosity      = 3)[0]
   else:
      MPI.report("No adjustment of Nmatrix chemical potential\nTotal density = %.3f"%Fbl(Chemical_potential))

   Nm_up(mu = Chemical_potential, SelectedBlock = 'up', mu_KS =  LDA_Chemical_potential, Sigma = Sigma,
          DoubleCounting = DC, Hopping = SK.hopping, Projection = SK.Projection, Normalize = False)

   if (MPI.is_master_node()):
      Nm_up.save("NMATRIX", False)



#####################################
#
#  Save new results
#
#####################################
  
if (MPI.is_master_node()):
   R = HDFArchive("LTO.h5")
   R["Sigma_next"] = S_ti.Sigma_iw
   del R
   shutil.copyfile("LTO.h5", "LTO_back.h5")
   #os.remove('STOP')

#Nm_new.save("NMATRIX", False)
