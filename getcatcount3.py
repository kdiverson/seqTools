import sqlite3
import sys
from collections import defaultdict

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

con = sqlite3.connect('/users/kiverson/eggNOGproteinaliasesDB3')
c = con.cursor()

catcount = defaultdict(int)
nobact = defaultdict(int)

for line in infile:
    line = line.split()
    gene = (line[0].strip(),)
    c.execute("SELECT cat FROM funccat INNER JOIN bactmembers ON (funccat.NOGmember == bactmembers.NOGmember) WHERE bactmembers.eggNOGid == (SELECT nog FROM earlygenes2NOGs WHERE gene = ?);", gene)
    cat = c.fetchall()
    try:
        catcount[str(cat[0][0])] += int(line[1].strip())
    except IndexError:
        nobact[line[0].strip()] += int(line[1].strip())

#for k in catcount:
#    outfile.write("%s\t%s\n" % (k, catcount[k]) )
    
for k in nobact:
    outfile.write("%s\t%s\n" % (k, nobact[k]) )

#outfile.write("nomatch: %s\n" % nobact)