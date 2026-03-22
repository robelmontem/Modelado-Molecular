#!/bin/bash
#
#SBATCH -p eck-q
#SBATCH --chdir=/home/alumno02/MM/caso_practico/extended_report
#SBATCH -J produccion_extended
#SBATCH --cpus-per-task=4
#SBATCH --ntasks=1
#SBATCH --mem=4G

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PROC_BIND=close
export OMP_PLACES=cores

date
gmx mdrun -deffnm arm_298 -c arm_298.g96 -ntmpi $SLURM_NTASKS -ntomp $SLURM_CPUS_PER_TASK
date
