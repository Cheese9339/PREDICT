import ahocorasick
import os
from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests
import itertools
import pandas as pd
from datetime import datetime


def generate_kmers(min_k, max_k, alphabet='ATCG'):
    kmers = []
    for k in range(min_k, max_k + 1):
        kmers.extend([''.join(p) for p in itertools.product(alphabet, repeat=k)])
    return kmers

def Get_Seqences(new_folder, fold_num):
    PosPath = sorted([f"{new_folder}/Kmer/Train/" + pos for pos in sorted(os.listdir(f"{new_folder}/Kmer/Train/")) if pos.endswith(".tp.fa")])[fold_num]
    NegPath = sorted([f"{new_folder}/Kmer/Train/" + neg for neg in sorted(os.listdir(f"{new_folder}/Kmer/Train/")) if neg.endswith(".tn.fa")])[fold_num]
    
    PosSeqences = []
    with open(PosPath, "r") as PosFile:
        PosSeqences = [seq.strip().upper() for seq in PosFile.readlines() if not ">" in seq]
    NegSeqences = []
    with open(NegPath, "r") as NegFile:
        NegSeqences = [seq.strip().upper() for seq in NegFile.readlines() if not ">" in seq]
    return PosSeqences, NegSeqences

def Auto_init(Kmers):
    Kmer_Auto = ahocorasick.Automaton()
    for Kmer in Kmers:
        Kmer_Auto.add_word(Kmer, Kmer)
    Kmer_Auto.make_automaton()
    return Kmer_Auto

def Auto_CountKmers(PosSeqences):
    Not_ExistsKmers = set()
    PosKmer_counts = {}
    for k in range(6):
        print(f"Searching K={k+5}...")
        Kmers = [Kmer for Kmer in generate_kmers(5+k, 5+k) if all(N_Kmer not in Kmer for N_Kmer in Not_ExistsKmers)]
        print(f"Searching by {len(Kmers)} {k+5}mers")
        Auto = Auto_init(Kmers)

        temp_SeqsKmersCounts = {}
        for index, PosSequence in enumerate(PosSeqences):
            temp_PosKmer_counts = {kmer: 0 for kmer in Kmers}
            for _, found_kmer in Auto.iter(PosSequence):
                temp_PosKmer_counts[found_kmer] += 1
            temp_SeqsKmersCounts.update({PosSequence: temp_PosKmer_counts})
            print(f"Processed {index+1} sequences", end="\r")

        Uncleaned_df = pd.DataFrame.from_dict(temp_SeqsKmersCounts, orient='index')
        print()
        Cleaned_df = Uncleaned_df.loc[:, (Uncleaned_df != 0).any(axis=0)]
        Not_ExistsKmers.update(set(Uncleaned_df.columns) - set(Cleaned_df.columns))
        print(f"Dropped {len(Uncleaned_df.columns)-len(Cleaned_df.columns)} {k+5}mers")
        
        
    # NegKmer_counts = {kmer: 0 for kmer in Kmers}
    # for NegSequence in NegSeqences:
    #     temp_NegKmer_counts = {kmer: 0 for kmer in Kmers}
    #     for _, found_kmer in Auto.iter(NegSequence):
    #         temp_NegKmer_counts[found_kmer] = 1
    #     for key in NegKmer_counts:
    #         NegKmer_counts[key] += temp_NegKmer_counts[key]

    PosKmer_counts_df = pd.DataFrame.from_dict(PosKmer_counts, orient='index')
    return PosKmer_counts_df#, NegKmer_counts


def main(new_folder, pThreshold=0.01):
    for fold in range(5):
        PosSeqences, NegSeqences = Get_Seqences(new_folder, fold)
        PosKmer_counts = Auto_CountKmers(PosSeqences)

        PosKmer_counts.to_csv(f"{new_folder}/Kmer/Train/Fold{fold+1:02d}KmerCounts.tsv", sep="\t")
        break
        # p_values = [float(value.split("\t")[2]) for value in KmerFET_Dict_Result.values()]
        # _, adjusted_p_values, _, _ = multipletests(p_values, method="fdr_bh")
        # OutPut_KmerFET_Dict = {key: "{}\t{}\t{}".format(value.split('\t')[0], value.split('\t')[1], adj_p) for (key, value), adj_p in zip(KmerFET_Dict_Result.items(), adjusted_p_values) if adj_p<pThreshold}
        # # OutPut_KmerFET_Dict = sorted_KmerFET_Dict_Result

        # OutputPath = f"{new_folder}/Kmer/Train/TPTN_{fold+1:02d}.pcre_FETresults.txt"
        # with open(OutputPath, "w") as OutputFile:
        #     OutputFile.write("Kmer\tPoscounts\tNegcounts\tP-value\n")
        #     for key, value in OutPut_KmerFET_Dict.items():
        #         OutputFile.write(f"{key}\t{value}\n")

start = datetime.now()
# new_folder = "/home/hpc/chiayicheng/user/Kai/New_Kmer_Pipeline/Results/2024_12_04_FindKmers01"
main(new_folder)
end = datetime.now()
print(f"Spent {(end-start).seconds} seconds")