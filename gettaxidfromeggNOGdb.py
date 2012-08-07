import sqlite3
import sys
from collections import defaultdict

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

con = sqlite3.connect('/users/kiverson/eggNOGproteinaliasesDB3')
c = con.cursor()

taxid = defaultdict(int)
na = 0

for line in infile:
    line = line.split()
    id = (line[1].strip(),)
    c.execute("SELECT taxid FROM gi2tax WHERE gid = (select substr(alias,4,10000000) from aliases where eggNOGid = ? AND alias LIKE 'GI:%');", id)
    cat = c.fetchall()
    try:
        taxid[str(cat[0][0])] += 1
    except IndexError:
        na += 1

for k in taxid:
    outfile.write("%s\t%s\n" % (k, taxid[k]) )
    
print "na: %s" % na