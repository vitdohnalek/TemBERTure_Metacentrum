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

Once the interactive job starts, you should cd  to your working directory. Try pwd command to see where you are currently located. Then you need to activate the TemBERTure environment.

```bash
# Add mambaforge to your module path
module add mambaforge

# Activate the environment
mamba activate /storage/{CITY}/home/{USER}/TemBERTure

# Set PYTHONPATH to ensure the right version of python and its packages are used
export PYTHONPATH=/storage/{CITY}/home/{USER}/TemBERTure/lib/python3.9/site-packages/

# Start Python interactive shell
python
```

Now we can actually run the tool 

```python
# Initialize TemBERTureCLS model with specified parameters
from temBERTure import TemBERTure
model = TemBERTure(
    adapter_path='./temBERTure_CLS/',  # Path to the model adapter weights
    device='cuda',                                # Device to run the model on
    batch_size=1,                                 # Batch size for inference
    task='classification'                         # Task type (e.g., classification for TemBERTureCLS)
)

# Change the sequence below to you protein. This is just an example.
seq = MEKVYGLIGFPVEHSLSPLMHNDAFARLGIPARYHLFSVEPGQVGAAIAGVRALGIAGVNVTIPHKLAVIPFLDEVDEHARRIGAVNTIINNDGRLIGFNTDGPGYVQALEEEMNITLDGKRILVIGAGGGARGIYFSLLSTAAERIDMANRTVEKAERLVREGEGGRSAYFSLAEAETRLDEYDIIINTTSVGMHPRVEVQPLSLERLRPGVIVSNIIYNPLETKWLKEAKARGARVQNGVGMLVYQGALAFEKWTGQWPDVNRMKQLVIEALRR'

# Predict the properties
model.predict(seq)

# Expected outcome for the example sequence
100%|██████████████████████████| 1/1 [00:00<00:00, 22.27it/s]
Predicted thermal class: Thermophilic
Thermophilicity prediction score: 0.999098474215349
Out[1]: ['Thermophilic', 0.999098474215349]

# For melting temperature prediction use different model

# Initialize all TemBERTureTM replicas with specified inference parameters
model_replica1 = TemBERTure(
    adapter_path='./temBERTure_TM/replica1/',  # Path to the adapter for replica 1
    device='cuda',                                        # Device to run the model on
    batch_size=16,                                        # Batch size for inference
    task='regression'                                     # Task type (e.g., regression for TemBERTureTM)
)

model_replica1.predict(seq)

# Expected outcome for the example sequence
100%|██████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.50it/s]
Predicted melting temperature: [77.86847686767578]
[77.86847686767578]
```

## Batch Usage

If you have a large dataset and you don't want to manually type in all your sequences you can use the python script provided in this repository. You can start an interactive job and follow all the instructions normally. Instead of starting the interactive python shell you copy the TemBERTure_batch.py to Metacentrum and run the following command:

```bash
python TemBERTure_batch.py
```

Please, note that you have to change the name of the fasta file in the script to the name of the fasta file of your interest. If the fasta file is not in the same directory as the script, you have to provide a path to the file. Results are written into a .tsv file.

Alternatively, you can avoid the usage of interactive job altogether using the TemBERTure_batch.sh script. In this case, you simply log in to metacentrum and copy there both TemBERTure_batch.sh and TemBERTure_batch.py scripts from this repository. You still have to provide the name of the fasta file to the python script. Also, you have to provide the path to the working directory to the .sh script. Once it is done you can do:

```bash
qsub TemBERTure_batch.sh
```

The scirpt then do all the work for you. Once it is done, the job is terminated. You can check whether it is still running with:

```bash
watch qstat -u  YOUR_USERNAME
```
