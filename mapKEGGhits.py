import sys
import sqlite3
import csv

kofile = open(sys.argv[1], 'r')
modulefile = open(sys.argv[2], 'r')
mapfile = open(sys.argv[3], 'r')

con = sqlite3.connect('/users/kiverson/mouseIllumina/dbs/KEGGmap')
c = con.cursor()

c.execute('CREATE TABLE kogene (ko, gene);')
c.execute('CREATE TABLE komod (ko, module);')
c.execute('CREATE TABLE moddesc (module, desc);') 

c.execute("CREATE INDEX kogene_gene ON kogene (gene);")
c.execute("CREATE INDEX komod_ko ON komod (ko);")
c.execute("CREATE INDEX moddesc_module ON moddesc (module);")

for line in kofile:
    line = line.split()
    ko = line[0]
    to_db = [(ko, line[i]) for i in range(1, len(line))]
    c.executemany('INSERT INTO kogene (ko, gene) values (?,?);', to_db)
    con.commit()

for line in modulefile:
    line = line.split()
    module = line[0]
    to_db = [(module, line[i]) for i in range(1, len(line))]
    c.executemany('INSERT INTO komod (module, ko) values (?,?);', to_db)
    con.commit()
    
for line in mapfile:
    line = line.split("\t")
    module = line[0]
    to_db = [(line[0], line[1])]
    c.execute('INSERT INTO moddesc (module, desc) values (?,?);', to_db)
    con.commit()
    
con.close()

#SELECT moddesc.module, moddesc.desc FROM moddesc, komod, kogene WHERE kogene.gene = 'RSL:RPSI07_1442' AND kogene.ko = komod.ko AND komod.module = moddesc.module;

#SELECT moddesc.module, moddesc.desc FROM moddesc INNER JOIN ON (komod.module = moddesc.module) AND kogene INNER JOIN ON (kogene.ko = komod.ko) WHERE kogene.gene = 'RSL:RPSI07_1442';

# for line in blastfile:
#     gene = line.split()[1]
#     gene = gene.upper()


#CONSTRAINT "ko" FOREIGN KEY("ko") REFERENCES "komod"("ko")
#CONSTRAINT "module" FOREIGN KEY("module") REFERENCES "moddesc"("module")