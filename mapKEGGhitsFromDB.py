import sys
import sqlite3
from collections import defaultdict

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

con = sqlite3.connect('/users/kiverson/mouseIllumina/dbs/KEGGmap')
c = con.cursor()

genes = []
modcount = defaultdict(int)

for line in infile:
    line = line.split();
    gene = line[1].strip().upper()
    genes.append(gene)

for gene in genes:
    t = (gene,)
    c.execute('SELECT moddesc2.module, moddesc2.desc FROM moddesc2, komod, kogene WHERE kogene.gene = ? AND kogene.ko = komod.ko AND komod.module = moddesc2.module;', t)
    data = c.fetchall()
    for item in data:
        modcount[data[0][1]] += 1

for key in modcount:
    outfile.write("%s\t%s\n" % (key, modcount[key]))
