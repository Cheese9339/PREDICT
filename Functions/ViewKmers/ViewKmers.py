import sys
import os
sys.path.append(f"{os.path.dirname(os.path.realpath(__file__))}/Packages")
from datetime import datetime
import streamlit as st
import Dealing_with_Folders
import Gff_to_Coord
import Coord_to_Fasta
import Gene_to_Fasta
import GetSequencesNKmers
import SentToKmer2Motif
import PlotKmer

def main(gff, genome, gene, Kmer, Motif, features = "gene", up_stream = 1000, down_stream = 500):
    if 'round' in st.session_state:
        st.session_state.round += 1
    else:
        st.session_state.round = 0

    if st.session_state.round == 0:
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
            ## 1. Copy "ViewKmers" folder(in "Demanded_Data" folder, old folder) to "Result" folder's new folder ##
        print("Dealing_with_folders...")
        st.session_state.new_folder = Dealing_with_Folders.main(gff, genome, gene, Kmer, Motif)
        print("Dealing_with_folders Done!")
        print("=======================================================")
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
            ## 2. From Gff file extract sequnce coord(start nucleotide number & end nucleotide number) ##
        print("Gff_to_Coord...")
        Gff_to_Coord.main(st.session_state.new_folder, features=features, up_stream=up_stream, down_stream=down_stream)
        print ("Gff_to_Coord Done!")
        print("=======================================================")
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
            ## 3. Use Coord to get exact sequence
        print("Coord_to_Fasta...")
        Coord_to_Fasta.main(st.session_state.new_folder)
        print("Coord_to_Fasta Done!")
        print("=======================================================")
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
            ## 4. Generate train/test_set's fasta file
        print("TPTN_to_Fasta...")
        Gene_to_Fasta.main(st.session_state.new_folder)
        print("TPTN_to_Fasta Done!")
        print("=======================================================")
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
        if Motif != "":
            print("Kmer2Motif...")
            st.session_state.K2M_Dict = SentToKmer2Motif.main(st.session_state.new_folder)
            print("Kmer2Motif Done!")
        else:
            st.session_state.K2M_Dict = None
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
    print("Get Gene Sequences and Kmers...")
    SeqencesDict, KmerList = GetSequencesNKmers.main(st.session_state.new_folder)
    print("Get Gene Sequences and Kmers Done!")
    print("=======================================================")
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
    print("Plotting Kmers...")
    PlotKmer.main(st.session_state.new_folder, SeqencesDict, KmerList, up_stream, K2M_Dict=st.session_state.K2M_Dict)
    print("Plotting Kmers Done! You can interact with streamlit app now.")
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

if __name__ == "__main__":
    main()