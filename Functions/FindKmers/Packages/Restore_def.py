import os
import shutil

def main():
    Old_target_folder = "/scratch/hpc/chiayicheng/users/Kai/New_Kmer_Pipeline/Results/" + sorted(os.listdir("/scratch/hpc/chiayicheng/users/Kai/New_Kmer_Pipeline/Results"))[-1]
    # print(sorted(os.listdir("/scratch/hpc/chiayicheng/users/Kai/New_Kmer_Pipeline/Results")))
    New_Gff_and_Genome_folder = "/scratch/hpc/chiayicheng/users/Kai/New_Kmer_Pipeline/InputData/FindKmers/Gff_and_Genome/"
    New_TP_and_TN_folder = "/scratch/hpc/chiayicheng/users/Kai/New_Kmer_Pipeline/InputData/FindKmers/TP_and_TN/"
    print(f"target_folder: {Old_target_folder}")
    print(f"New_Gff_and_Genome_folder: {New_Gff_and_Genome_folder}")
    print(f"New_TP_and_TN_folder: {New_TP_and_TN_folder}")

    Old_Gff = f"{Old_target_folder}/Gff_and_Genome/" + [gff for gff in os.listdir(os.path.join(Old_target_folder, "Gff_and_Genome")) if gff.endswith(".gff3") or gff.endswith(".gff")][0]
    Old_Genome = f"{Old_target_folder}/Gff_and_Genome/" + [genome for genome in os.listdir(os.path.join(Old_target_folder, "Gff_and_Genome")) if genome.endswith(".fasta")][0]
    Old_TP = f"{Old_target_folder}/TP_and_TN/" + [TP for TP in os.listdir(os.path.join(Old_target_folder, "TP_and_TN")) if TP.endswith(".tp")][0]
    Old_TN = f"{Old_target_folder}/TP_and_TN/" + [TN for TN in os.listdir(os.path.join(Old_target_folder, "TP_and_TN")) if TN.endswith(".tn")][0]

    shutil.copy(Old_Gff, New_Gff_and_Genome_folder)
    shutil.copy(Old_Genome, New_Gff_and_Genome_folder)
    shutil.copy(Old_TP, New_TP_and_TN_folder)
    shutil.copy(Old_TN, New_TP_and_TN_folder)

    # os.remove(Old_Gff)
    # os.remove(Old_Genome)
    # os.remove(Old_TP)
    # os.remove(Old_TN)