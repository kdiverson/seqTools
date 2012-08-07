import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

for line in infile:
    line = line.split()
    sub = line[0].strip()
    query = line[1].strip()
    per = line[2].strip()
    if sub != query:
        outfile.write("%s\t%s\t%s\n" % (sub, query, per) )
