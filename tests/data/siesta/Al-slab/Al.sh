#!/bin/bash
##
## Copyright The NOMAD Authors.
##
## This file is part of NOMAD.
## See https://nomad-lab.eu for further info.
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##

#SBATCH --nodes=1
#SBATCH --time=30:00
#SBATCH --ntasks=8
#SBATCH -p debug
#SBATCH --output=out.log
#SBATCH --error=err.out.log
#SBATCH --exclusive

#load the environment

ulimit -s unlimited
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so
export I_MPI_FABRICS=shm:dapl
module load   intel/2016a    

srun  --resv-ports  -N 1 -n 8 /home/andrea/siesta-4.0/Obj/siesta < input.fdf > out