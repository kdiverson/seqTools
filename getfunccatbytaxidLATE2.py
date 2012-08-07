import sqlite3
import sys
from collections import defaultdict

#infile = open(sys.argv[1], 'r')
outfile = open("funcatbytaxLATE.txt", 'w')


con = sqlite3.connect('/users/kiverson/eggNOGproteinaliasesDB3')
c = con.cursor()

taxid = defaultdict(int)
na = 0

taxidcat = defaultdict(lambda: defaultdict(int))
for n in sys.argv[1:]:
    infile = open(n, 'r')
    for line in infile:
        line = line.split()
        gene = (line[0].strip(),)
        c.execute("SELECT cat FROM funccat INNER JOIN bactmembers ON (funccat.NOGmember == bactmembers.NOGmember) WHERE bactmembers.eggNOGid == (SELECT nog FROM lategenes2NOGs WHERE gene = ?);", gene)
        cat = c.fetchall()
        c.execute("SELECT taxid FROM gi2tax WHERE gid = (select substr(alias,4,10000000) from aliases where eggNOGid = (SELECT nog FROM lategenes2NOGs WHERE gene = ?) AND alias LIKE 'GI:%');", gene)
        taxid = c.fetchall()
        
        try:
            taxidcat[str(taxid[0][0])][str(cat[0][0])] += int(line[1].strip())
        except IndexError:
            na += 1

for tax in taxidcat:
    outfile.write("%s" % tax)
    for cat in taxidcat[tax]: 
        outfile.write("\t%s\t%s" % (cat, taxidcat[tax][cat]) )
    outfile.write("\n")
    
print "na: %s" % na


#SELECT taxid FROM gi2tax WHERE gid = (select substr(alias,4,10000000) from aliases where eggNOGid = (SELECT nog FROM earlygenes2NOGs WHERE gene = "1216833_gene_5") AND alias LIKE 'GI:%');

#SELECT funccat.cat, taxid FROM gi2tax WHERE gid = (select substr(alias,4,10000000) from aliases where eggNOGid = (SELECT nog FROM earlygenes2NOGs WHERE gene = ?) AND alias LIKE 'GI:%');