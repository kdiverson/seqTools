import sys
from collections import defaultdict

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

contigDict = defaultdict(int)

for line in infile:
    line = line.split("\t")
    contigDict[line[1]] += 1

for contig in contigDict:
    outfile.write("%s\t%s\n" %(contig, contigDict[contig]))
