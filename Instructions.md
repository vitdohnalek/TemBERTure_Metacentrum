## Installation

Follow these commands to set up the environment:

```bash
# Clone the repository
git clone https://github.com/ibmm-unibe-ch/TemBERTure.git
cd TemBERTure
git filter-branch --subdirectory-filter temBERTure -- --all

# Add mambaforge to your module path
module add mambaforge

# Create a new conda environment with Python 3.12
mamba create --prefix /storage/{CITY}/home/{USER}/TemBERTure python=3.9.18 -y

# Activate the newly created environment
mamba activate /storage/{CITY}/home/{USER}/TemBERTure

# Set PYTHONUSERBASE to your environment directory
export PYTHONUSERBASE=/storage/{CITY}/home/{USER}/TemBERTure/

# Install the dependencies
pip install --no-cache-dir -r requirements.txt
```
## Usage

Follow the instruction to run the TemBERTure tool:

Fisrtly, you need to start an interactive job. TemBERTure specifically requires gpu_cap=sm_60! You can easily construct your job request command [here](https://metavo.metacentrum.cz/pbsmon2/qsub_pbspro). Don't forget to add the -I flag to make the job interactive.

You can use the example of interactive job request below:

```bash
 qsub -I -l walltime=24:0:0 -q default@pbs-m1.metacentrum.cz -l select=1:ncpus=1:ngpus=1:mem=20gb:gpu_mem=10gb:scratch_local=400mb:gpu_cap=sm_60 
```
Once the interactive job starts, you should cd  to your working directory. Try ``bash pwd``` to see where you are currently located.
