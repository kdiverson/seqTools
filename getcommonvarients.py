import sys

infile1 = open(sys.argv[1], 'r')
infile2 = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], 'w')

genedict1 = {}
genedict2 = {}

for line in infile1:
    line = line.split("\t")
    gene = line[0]
    poslist = line[1:-1]
    genedict1[gene] = poslist[::2]
    
for line in infile2:
    line = line.split("\t")
    gene = line[0]
    poslist = line[1:-1]
    genedict2[gene] = poslist[::2]
    
tmp = [k for k in genedict2 if k in genedict1]

for gene in tmp:
    if set(genedict1[gene]) & set(genedict2[gene]):
        outfile.write("%s\n" % gene)