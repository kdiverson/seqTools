import os
import sys
#path = sys.arv[1]
outfile = open("outfile.csv", 'w')#open(sys.argv[2], 'w')
path='../local/db/by_source/ncbi/dacc_reference_genomes/20110315/all_nuc_20110315/'
dirList = os.listdir(path)
for fname in dirList:
    outfile.write("/users/kiverson/local/db/by_source/ncbi/dacc_reference_genomes/20110315/all_nuc_20110315/%s,"%(fname))
