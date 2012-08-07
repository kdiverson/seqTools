import sys
from collections import defaultdict

outfile = open(sys.argv[1], 'w')

descdict = defaultdict(int)

for n in sys.argv[2:]:
    infile = open(n, 'r')
    for line in infile:
        line = line.split("\t")
        desc = line[0].strip()
        count = int(line[1].strip())            
        if desc == "":
            desc = "NA"
            #count = int(line[1].strip())
        descdict[desc] += count
for desc in descdict:
    outfile.write("%s\t%s\n" % (desc, descdict[desc]) )