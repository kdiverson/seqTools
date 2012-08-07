import sys
from collections import defaultdict

#infile = open(sys.argv[1], 'r')
outfile = open("testsnpdepth.txt", 'w')

genedict = defaultdict(lambda: defaultdict(int))

for n in sys.argv[1:]:
    infile = open(n, 'r')
    for line in infile:
        if line.startswith("#"):
            continue
        line = line.split("\t")
        gene = line[0].strip()
        pos = int(line[1].strip())
        info = line[7]
        info = info.split(";")
        depth = info[0].split("=")
        depth = int(depth[1])
        #ref = line[2]
        #alt = line[3]
#         try: 
#             alt = alt.split(",")
#             for snp in alt:
#                 genedict[gene].append(snp)
#         except:
#             genedict[gene][pos] += 1
        if depth < 5:
            continue
        else:
            genedict[gene][pos] += 1
    infile.close()
            
for gene in genedict:
    outfile.write("%s\t" % gene)
    for position in genedict[gene]:
        outfile.write("%s\t%s\t" %(position,genedict[gene][position]) )
    outfile.write("\n")
