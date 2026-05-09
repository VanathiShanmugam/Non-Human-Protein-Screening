from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import pandas as pd
import time
import warnings

warnings.filterwarnings("ignore")

results = []
fasta_file = "data/sample.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):

    print("Running BLAST for:", record.id)

    success = False

    while not success:
        try:
            result_handle = NCBIWWW.qblast(
                "blastp",
                "nr",
                record.seq,
                entrez_query="Homo sapiens[Organism]",
                hitlist_size=5
            )

            blast_record = NCBIXML.read(result_handle)
            success = True

        except Exception as e:
            print("BLAST taking long or connection error. Retrying in 60 seconds...")
            time.sleep(60)

    best_identity = 0

    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:

            identity_percent = (hsp.identities / hsp.align_length) * 100

            if identity_percent > best_identity:
                best_identity = identity_percent

    identity_fraction = best_identity / 100
    non_human_score = 1 - identity_fraction

    results.append({
        "Protein_ID": record.id,
        "Best_Human_Identity(%)": round(best_identity,2),
        "Non_Human_Score": round(non_human_score,3)
    })

    # increased delay to avoid NCBI rate limits
    time.sleep(30)

df = pd.DataFrame(results)
df.to_csv("non_human_similarity_scores.csv", index=False)

print("Analysis complete.")
