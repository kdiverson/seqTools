import sys
import operator
from collections import defaultdict

geneDict = defaultdict(lambda: defaultdict(int))

for n in sys.argv[1:]:
    infile = open(n, 'r')
    for line in infile:
        if line.startswith("#"):
            pass
        else:
            line = line.split("\t")
            geneDict[line[0].strip()] += 1
        
    infile.close()
    
outfile = open("snpgenes.txt", 'w')

sortedgenes = sorted(geneDict.iteritems(), key=operator.itemgetter(1), reverse=True)

for gene in sortedgenes:
    outfile.write("%s\t%s\n" % (gene[0], gene[1]) )