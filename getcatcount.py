import sqlite3
import sys
from collections import defaultdict

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

con = sqlite3.connect('/users/kiverson/eggNOGproteinaliasesDB3')
c = con.cursor()

catcount = defaultdict(int)
nobact = 0

for line in infile:
    line = line.split()
    id = (line[1].strip(),)
    c.execute("SELECT cat FROM funccat INNER JOIN bactmembers ON (funccat.NOGmember == bactmembers.NOGmember) WHERE bactmembers.eggNOGid == ?;", id)
    cat = c.fetchall()
    try:
        catcount[str(cat[0][0])] += 1
    except IndexError:
        nobact += 1

for k in catcount:
    outfile.write("%s\t%s\n" % (k, catcount[k]) )
    
print "nobact: %s" % nobact