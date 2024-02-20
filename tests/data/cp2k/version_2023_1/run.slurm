#!/bin/bash -l
# Job Name and Files (also --job-name)
#SBATCH -J Defect_level_D_mode

#Output and error (also --output, --error):
#SBATCH -o ./%x.%j.out
#SBATCH -e ./%x.%j.err

#Mailing
#SBATCH --mail-user=maximilian.graml@ur.de
#SBATCH --mail-type=ALL

#Initial working directory (also --chdir):
#SBATCH -D ./

# Change here the job size and time limit:
#SBATCH --time=4:00:00
#SBATCH --nodes=3
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks=216
#SBATCH --partition=multinode

#Setup of execution environment
#SBATCH --export=NONE
unset SLURM_EXPORT_ENV

module load intel
module load mkl
module load intelmpi

source /home/atuin/b165da/b165da10/01_CP2K_compilations/09_toolchain_with_MKL_without_libtorch/cp2k/tools/toolchain/install/setup

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

exec="/home/atuin/b165da/b165da10/01_CP2K_compilations/09_toolchain_with_MKL_without_libtorch/cp2k/exe/local/cp2k.psmp"

srun $exec Energy_calc.inp