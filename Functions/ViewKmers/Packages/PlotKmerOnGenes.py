import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random


def main(new_folder, SeqencesDict, KmerList):

    kmer_colors = {kmer: (random.random(), random.random(), random.random()) for kmer in KmerList}

    fig, ax = plt.subplots(figsize=(10, len(SeqencesDict) * 0.6))
    ax.set_xlim(0, max(len(seq) for seq in SeqencesDict.values()))
    ax.set_ylim(-0.5, len(SeqencesDict) - 0.5)

    for i, (gene, sequence) in enumerate(SeqencesDict.items()):
        y_pos = i - 0.4
        ax.add_patch(mpatches.Rectangle((0, y_pos), len(sequence), 0.8, color="lightgray", alpha=0.5))

        for kmer in KmerList:
            color = kmer_colors[kmer]
            start = 0
            pos = sequence.find(kmer, start)
            while pos != -1:
                ax.add_patch(mpatches.Rectangle((pos, y_pos), len(kmer), 0.8, color=color, alpha=1.0))
                start = pos + 1 
                pos = sequence.find(kmer, start)

    ax.set_yticks(range(len(SeqencesDict)))
    ax.set_yticklabels(SeqencesDict.keys(), va="center")

    legend_patches = [mpatches.Patch(color=color, label=kmer) for kmer, color in kmer_colors.items()]
    fig.legend(handles=legend_patches, loc="upper left", bbox_to_anchor=(0.89, 1+(0.05/len(SeqencesDict)*20)))

    plt.xlabel("Sequence Position")
    plt.title("Kmer Occurrences in Gene Sequences")
    plt.tight_layout(rect=[0, 0, 1, 1])
    plt.savefig(f"{new_folder}/KmersVisualization.png", dpi=300, bbox_inches="tight")
