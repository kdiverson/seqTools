import sqlite3
import sys
import operator
from collections import defaultdict

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
nohits = open(sys.argv[3], 'w')


con = sqlite3.connect('/users/kiverson/eggNOGproteinaliasesDB3-2')
c = con.cursor()

catcount = defaultdict(int)
nobact1 = 0
nobact = defaultdict(int)

for line in infile:
    line = line.split()
    gene = (line[0].strip(),)
    c.execute("SELECT cat FROM funccat INNER JOIN bactmembers ON (funccat.NOGmember == bactmembers.NOGmember) WHERE bactmembers.eggNOGid == (SELECT nog FROM earlygenes2NOGs WHERE gene = ?);", gene)
    cat = c.fetchall()
    try:
        catcount[str(cat[0][0])] += int(line[1].strip())
    except IndexError:
        nobact1 += int(line[1].strip())
        nobact[line[0].strip()] += int(line[1].strip())

#for k in catcount:
    #outfile.write("%s\t%s\n" % (k, catcount[k]) )
    
#outfile.write("nomatch: %s\n" % nobact1)

sortedcats = sorted(catcount.iteritems(), key=operator.itemgetter(1), reverse=True)
sortednobact = sorted(nobact.iteritems(), key=operator.itemgetter(1), reverse=True)

for cat in sortedcats:
    outfile.write("%s\t%s\n" % (cat[0], cat[1]) )

outfile.write("nomatch\t%s\n" % nobact1)
    
for k in sortednobact:
    nohits.write("%s\t%s\n" % (k[0], k[1]) )
