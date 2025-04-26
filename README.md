---
title: PREDICT

---

# PREDICT
PREDICT is a modular machine learning pipeline designed to perform predictive modeling based on **c**is-**r**egulatory **e**lements(CREs) sequence-derived features, particularly k-mer counts from genomic datasets. It is structured to be adaptable, interpretable, and usable in various biological research contexts.

## Modules Overview
PREDICT includes the following main modules:

### 1. FindKmers
**Purpose**: Identify enriched K-mers that are crucial for distinguishing Differentially Expressed Genes (DEGs, TP) and non-DEGs (TN).

**Input**: 
*     Gene IDs of DEGs(TP) and non-DEGs(TN)
*     Species Genome (e.g: .fasta file)
*     Annotations (e.g: .gff3 file)

**Output**:
*     AllCopies_FeatureImportance.txt: Ranked potential transcription factor binding site(TFBS) K-mers
*     ALLCopies_mean_score.txt: Machine learning elvaluating scores for this run.
*     Additional outputs for downstream module
     *     Kmer_ShortTable.tsv: Contains only Ranked K-mer and their IDs.
     *     KmerXKmer_table.tsv: Indicates K-mers’ co-occurrences.
     *     TPGeneXKmer_Table.tsv: Indicates K-mers’ counts in TP genes(DEGs).
     *     TNGeneXKmer_Table.tsv: Indicates K-mers’ counts in TN genes(non-DEGs).
     *     BestModel_Copyi.joblib(ABANDONED): A trained model available in predicting DEGs.

**Note 1**
1. None


---
### 2. Kmer2Motif
**Purpose**: Map K-mers to known motifs of TFs to ‘translate’ the K-mer sequence to biologically meaningful interpretation.

**Input**: 
*     K-mers list (e.g., Mod.1 Output: Kmer_ShortTable.tsv)
*     Motifs sequence of known TF (check format detail in note 2-1)

**Output**:
*     Kmer2Motif.tsv: Maps K-mers and their top-related motifs.

**Note 2**:
1. Filename extension should be ".motif" or ".fasta", and the contents has no difference.
>\>MotifName
MotisConsensusSequence
![image](https://hackmd.io/_uploads/H1pQYlc1le.png)

---
### 3. RanKmers
**Purpose**: Evaluate and rank the TFBS potential of user-specified K-mers within genes. (check more description in note 3-1)

**Input**: 
*     Gene IDs of DEGs(TP) and non-DEGs(TN)
*     Species Genome (e.g: .fasta file)
*     Annotations (e.g: .gff3 file)
*     Kmers List (file extension must be ".kmer" or ".tsv")

**Output (Same as FindKmers)**:
*     AllCopies_FeatureImportance.txt: Ranked potential transcription factor binding site(TFBS) K-mers
*     ALLCopies_mean_score.txt: Machine learning elvaluating scores for this run.
*     Additional outputs for downstream module
     *     Kmer_ShortTable.tsv: Contains only Ranked K-mer and their IDs.
     *     KmerXKmer_table.tsv: Indicates K-mers’ co-occurrences.
     *     TPGeneXKmer_Table.tsv: Indicates K-mers’ counts in TP genes(DEGs).
     *     TNGeneXKmer_Table.tsv: Indicates K-mers’ counts in TN genes(non-DEGs).
     *     BestModel_Copyi.joblib(ABANDONED): A trained model available in predicting DEGs.

**Note 3**
1. RanKmers is highly similar to FindKmers, except that users must provide the specific K-mers they wish to investigate.

---
### 4. TeamKmers
**Purpose**: Identify co-occurrences of K-mers, which may suggest co-occurring TFs. (Directly translate Kmer2Motif is supported)

**Input**: 
*     TP KmerXKmer Table (must be Mod.1|3 Output: TPGeneXKmer_Table.tsv)
*     TN KmerXKmer Table (must be Mod.1|3 Output: TNGeneXKmer_Table.tsv)
*     Motif List (Optional)

**Output (Same as FindKmers)**:
*     CoocurredKmerPairs.tsv: Kmer pairs which co-occurred more than others.
*     MotifCoocurrenceScore.tsv (if Motif==True): Motif pairs which co-occurred more than others.
*     KmerXKmerTPCosineSimilarityTable.tsv: (Not useful) Calculated and filtered CosineSimilarity score for Kmers in TP.
*     KmerXKmerTPTNCosineSimilarityTable.tsv: (Not useful) Calculated and filtered CosineSimilarity score for Kmers in comparism of TP and TN.

**Note 4**
1. None

---
### 5. TeamKmers
**Purpose**: Visualize the positions of kmers in genes of interest. (check **IMPORTANT** description in Note 5-1, 5-2)

**Input**: 
*     Gene IDs
*     Species Genome (e.g: .fasta file)
*     Annotations (e.g: .gff3 file)
*     Kmer list (extendable on web page)

**Output (Same as FindKmers)**:
*     A url direct web page, which is interatable for selecting kmers and genes.
*     Selected kmers' average distance (at the bottom of web page).

**Note 5**
1. Running this module on HPC is **NOT** recommanned, users should run by streamlit commands. (e.g: streamlit run ViewKmers.py)
2. Design of the Module is **NOT** for viewing many kmers/many genes. Recommanded amount of kmers<=5, genes<=20

---
## Environment Setup

The environment should be initialized via Conda. Use the provided YAML file to install dependencies.

    conda env create -f PREDICT_Python.yml
    conda env create -f PREDICT_R.yml
    conda activate PREDICT_Python

---
## Example Usage
After preparing input files and configuring parameters:

bash ExampleRUN.sh

This script executes Mod1: FindKmers with predefined settings. You can also run modules manually via:
    
    python Functions/FindKmers/FindKmers.py

