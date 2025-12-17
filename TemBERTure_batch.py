# Script to predict the Thermophilicity prediction score for all sequences contains in a fasta file
# Please provide a name (or path to the file) of a fasta file
from Bio import SeqIO
from temBERTure import TemBERTure

# Models initialization
model = TemBERTure(
    adapter_path='./temBERTure_CLS/',
    device='cuda',
    batch_size=1,
    task='classification'
)

model_replica1 = TemBERTure(
    adapter_path='./temBERTure_TM/replica1/',
    device='cuda',
    batch_size=16,
    task='regression'
)

# Header of the results .tsv file
tsv = "Protein ID\tPredicted thermal class\tThermophilicity prediction score\tPredicted melting temperature\n"

# Iterate over sequences in your fasta file and predict properties of proteins
for seq_rec in SeqIO.parse("FASTA_FILE", "fasta"): # Change the name to your fasta file

    seq_ID = seq_rec.id
    seq = str(seq_rec.seq.strip("*"))

    prediction_results = model.predict(seq)
    melting_temp = model_replica1.predict(seq)

    # Add results to the tsv
    tsv += seq_ID + "\t"
    tsv += str(prediction_results[0][0]) + "\t"
    tsv += str(prediction_results[1][0]) + "\t"
    tsv += str(melting_temp[0]) + "\n"

# Write results into a .tsv file
with open("Predictions.tsv", "w") as f: # You can rename the result file
    f.write(tsv)


