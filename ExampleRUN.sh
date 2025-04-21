#!/bin/bash
#PBS -l select=2:ncpus=16
#PBS -N PREDICT
#PBS -q XXX
#PBS -V

cd /home/hpc/chiayicheng/scratch/users/Kai/PREDICT ### Your "PREDICT" folder path
source /home/hpc/chiayicheng/package/miniforge3/etc/profile.d/conda.sh
conda activate PREDICT_Python; 
python /home/hpc/chiayicheng/scratch/users/Kai/PREDICT/PREDICT.py FindKmers

