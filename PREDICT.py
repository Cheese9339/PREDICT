import sys
import os
sys.path.append('./Functions/FindKmers')
sys.path.append('./Functions/Kmer2Motif')
sys.path.append('./Functions/RanKmers')
sys.path.append('./Functions/TeamKmers')
sys.path.append('./Functions/ViewKmers')
from Functions.FindKmers import FindKmers
from Functions.Kmer2Motif import Kmer2Motif
from Functions.RanKmers import RanKmers
from Functions.TeamKmers import TeamKmers
from Functions.ViewKmers import ViewKmers

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the module you want to execute. e.g.:python PREDICT.py FindKmers")
        sys.exit(1)

    module = sys.argv[1]

    if module == 'FindKmers':
        FindKmers.main()
    elif module == 'Kmer2Motif':
        Kmer2Motif.main()
    elif module == 'RanKmers':
        RanKmers.main()
    elif module == 'TeamKmers':
        TeamKmers.main()
    elif module == 'ViewKmers':
        ViewKmers.main()
    else:
        print(f"UnKnown module：{module}")