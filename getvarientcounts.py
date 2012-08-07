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
    variants = len(poslist[::2])
#     for item in poslist[1::2]:
#         if int(item) > 1:
#             variants.append(
#         
    genedict1[gene] = variants
    
for line in infile2:
    line = line.split("\t")
    gene = line[0]
    poslist = line[1:-1]
    variants = len(poslist[::2])
    #variants = 
    for item in poslist[1::2]:
        if int(item) > 1:
            #variants.append(    
            genedict2[gene] = variants
    
tmp = [k for k in genedict2 if k in genedict1]

for gene in tmp:
    if genedict1[gene] < genedict2[gene]:
        outfile.write("%s\t%s|%s\n" % (gene,genedict1[gene], genedict2[gene]))
    #if set(genedict1[gene]) & set(genedict2[gene]):
        #outfile.write("%s\n" % gene)