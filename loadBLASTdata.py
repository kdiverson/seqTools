import sqlite3
import sys

infile = open(sys.argv[1], 'r')

con = sqlite3.connect('/users/kiverson/eggNOGproteinaliasesDB3')
c = con.cursor()

for line in infile:
    line = line.split("\t")
    t = (line[0].strip(), line[1].strip())
    c.execute("INSERT INTO allFull2nog (gene, nog) VALUES (?,?);", t)
    
con.commit()
c.close()
