#!/bin/bash
#PBS -q default@pbs-m1.metacentrum.cz
#PBS -l walltime=24:0:0
#PBS -l select=1:ncpus=1:ngpus=1:mem=20gb:gpu_mem=10gb:scratch_local=400mb:gpu_cap=sm_60
#PBS -N TemBERTure_job

# Please change according to your working directory
# Most likely, it will be something like /storage/brno2/home/jannovak/TemBERTure
cd YOUR_WORKING_DIRECTORY

# Add mambaforge to your module path
module add mambaforge

# Activate the environment
mamba activate /storage/{CITY}/home/{USER}/TemBERTure

# Set PYTHONPATH to ensure the right version of python and its packages are used
export PYTHONPATH=/storage/{CITY}/home/{USER}/TemBERTure/lib/python3.9/site-packages/

# Run TemBERTure
python TemBERTure_batch.py
