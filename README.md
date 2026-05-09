# Non-Human Protein Screening

### Automated BLAST-Based Similarity Analysis Using Biopython

---

## Features

- Automated BLASTP analysis against human proteins
- Identification of pathogen-specific proteins
- Non-human similarity scoring framework
- Retry handling for stable NCBI querying
- CSV-based result generation

---

## Project Overview

This project presents a Python-based computational workflow for identifying proteins with low similarity to human proteins using the NCBI BLAST API and Biopython.

Protein sequences are queried against the `nr` database restricted to *Homo sapiens*, enabling prioritization of proteins that may serve as potential pathogen-specific therapeutic targets.

The workflow calculates:

* Highest human sequence identity
* Non-human similarity score

Applications include:

* Drug target prioritization
* Comparative proteomics
* Computational pathogen analysis

---

## Workflow

### 📥 1. Input Processing

* Protein FASTA sequences parsed using Biopython `SeqIO`

---

### 🌐 2. BLASTP Search

Each sequence is queried against:

* Database: `nr`
* Organism filter: `Homo sapiens`

using the NCBI BLAST web service.

---

### 📊 3. Similarity Scoring

For each protein:

* Best human identity (%) is extracted
* Non-human similarity score is calculated:

```text id="z5x3mq"
Non_Human_Score = 1 - (Best_Identity / 100)
```

Higher scores indicate proteins with lower similarity to human proteins.

---

### 📤 4. Output Generation

Results are exported as:

```bash id="m4w2oe"
non_human_similarity_scores.csv
```

containing:

* Protein ID
* Best human identity (%)
* Non-human similarity score

---

## 🗂️ Project Structure

```bash id="w1o7kj"
non-human-protein-screening/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── blast_screening.py
│
├── data/
│   └── sample.fasta
│
└── results/
```

---

## Usage

### Install Dependencies

```bash id="p9t1za"
pip install -r requirements.txt
```

---

### Run the Pipeline

```bash id="d4u8km"
python src/blast_screening.py
```

---

## Output

Generated CSV file:

```bash id="h7x5cn"
non_human_similarity_scores.csv
```

---

## Important Notes

* Internet connection is required
* BLAST requests may take time depending on server load
* Delays are included to comply with NCBI usage policies

---

## Data Source & Acknowledgement

Protein FASTA sequences and BLAST services were obtained from the NCBI database and tools.

NCBI Resource:

* https://www.ncbi.nlm.nih.gov/

---

## Scientific Relevance

This workflow supports:

* Pathogen-specific protein prioritization
* Drug discovery pipelines
* Comparative sequence analysis
* Bioinformatics-driven therapeutic target screening

---

## Author

**Vanathi Shanmugam**
Bioinformatics | Genomics | Machine Learning

🔗 LinkedIn: https://www.linkedin.com/in/vanathi-shanmugam-26127928a

---

## 📜 License

This project is intended for academic and research purposes.
