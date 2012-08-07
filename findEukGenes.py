import sys
from collections import defaultdict

inblast = open(sys.argv[1], 'r')
infile = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], 'w')

genedict = defaultdict(int)

for line in infile:
    genes = line.split()

for line in inblast:
    line = line.split()
    gene = line[1].upper()
    if gene in genes:
        genedict[gene] += 1

for gene in genedict:
    ourfile.write("%s\t%s\n" %(gene, genedict[gene]) )
