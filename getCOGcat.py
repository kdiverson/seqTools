import sys
import sqlite3
import csv

cogfile = open("/users/kiverson/cog/whog.txt", 'r')

con = sqlite3.connect('/users/kiverson/mouseIllumina/dbs/late')
c = con.cursor()

c.execute("create table cogblast (queryId, subjectId, cogcat, cogdesc, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore);")

c.execute("create index cogcat_index on cogblast (cogcat);")

cogdict = {}

for line in cogfile:
    if line.startswith("["):
        cat = line[1]
        line = cogfile.next()
    line = line.split("  ")
    fun = line[0]
    proteins = line[1].split()
    for protein in proteins:
        cogdict[protein] = (fun, cat)

#for line in blastfile:
#    (queryId, subjectId, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore) = line.split("\t")
    
with open('/share/scratch/kiverson/mouseIllumina/lategenesVcogSigMatches.out', "rb") as blastfile:
    dr = csv.DictReader(blastfile, fieldnames= ['queryId', 'subjectId', 'percIdentity', 'alnLength', 'mismatchCount', 'gapOpenCount', 'queryStart', 'queryEnd', 'subjectStart', 'subjectEnd', 'eVal', 'bitScore'], delimiter="\t")
    to_db = []
    for i in dr:
        try:
            cogcat = cogdict[i['subjectId']][1]
            cogdesc = cogdict[i['subjectId']][0]
        except KeyError:
            cogcat = 'NULL'
            cogdesc = 'NULL'
        to_db.append((i['queryId'], i['subjectId'], cogcat, cogdesc, i['percIdentity'], i['alnLength'], i['mismatchCount'], i['gapOpenCount'], i['queryStart'], i['queryEnd'], i['subjectStart'], i['subjectEnd'], i['eVal'], i['bitScore']))
    
    #to_db = [(i['queryId'], i['subjectId'], cogcat, i['percIdentity'], i['alnLength'], i['mismatchCount'], i['gapOpenCount'], i['queryStart'], i['queryEnd'], i['subjectStart'], i['subjectEnd'], i['eVal'], i['bitScore']) for i in dr]

c.executemany("insert into cogblast (queryId, subjectId, cogcat, cogdesc, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)

con.commit()
