import sys
import operator
from collections import defaultdict

geneDict = defaultdict(int)

for n in sys.argv[1:]:
    infile = open(n, 'r')
    for line in infile:
        line = line.split("\t")
        geneDict[line[0].strip()] += int(line[1].strip())
        
    infile.close()
    
outfile = open("NINgenes.txt", 'w')

sortedgenes = sorted(geneDict.iteritems(), key=operator.itemgetter(1), reverse=True)

for gene in sortedgenes:
    outfile.write("%s\t%s\n" % (gene[0], gene[1]) )
