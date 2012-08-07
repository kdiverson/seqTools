import sqlite3
import sys
import operator
from collections import defaultdict

con = sqlite3.connect('/users/kiverson/eggNOGproteinaliasesDB3')
c = con.cursor()

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
errorfile = open(sys.argv[3], 'w')

for line in infile:
    line = line.split()
    gi = line[1].split("|")
    gi = (gi[1].strip(),)
    c.execute("SELECT taxid FROM gi2tax WHERE gid = ?;", gi)
    data = c.fetchall()
    try:
        taxid = data[0][0]
        outfile.write("%s\n" % taxid)
    except IndexError:
        errorfile.write("%s\n" % gi[0])
        continue
        
