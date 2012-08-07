import sys
from collections import defaultdict

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

taxdb = defaultdict(int)

for line in infile:
    (queryId, subjectId, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore) = line.split("\t")
    tax = subjectId.split(":")[0]
    taxdb[tax]+=1

for org in taxdb:
    outfile.write("%s\t%s\n" %(org, taxdb[org]) )
