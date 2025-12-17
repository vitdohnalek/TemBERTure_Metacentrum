# Script to predict the Thermophilicity prediction score for all sequences contains in a fasta file
# Please provide a name (or path to the file) of a fasta file
from Bio import SeqIO
from temBERTure import TemBERTure

model = TemBERTure(
    adapter_path='./temBERTure_CLS/',
    device='cuda',
    batch_size=1,
    task='classification'
)

tsv = "Protein ID\tPredicted thermal class\tThermophilicity prediction score\n"

for seq_rec in SeqIO.parse("FASTA_FILE", "fasta"): # Change the name to your fasta file

    seq_ID = seq_rec.id
    seq = str(seq_rec.seq.strip("*"))

    prediction_results = model.predict(seq)

    tsv += seq_ID + "\t"
    tsv += str(prediction_results[0][0]) + "\t"
    tsv += str(prediction_results[1][0]) + "\n"

with open("Predictions.tsv", "w") as f: # You can rename the result file
    f.write(tsv)

