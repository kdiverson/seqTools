import sys
from collections import defaultdict
import operator

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

hits = defaultdict(int)

for line in infile:
    line = line.split("\t")
    hit = line[1]
    hits[hit] += 1

sortedhits = sorted(hits.iteritems(), key=operator.itemgetter(1), reverse=True)

for hit in sortedhits:
    outfile.write("%s\t%s\n" %(hit[0], hit[1]) ) 
