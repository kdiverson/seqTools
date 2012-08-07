import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

for line in infile:
    line = line.split("\t")
    outfile.write(line[1]+"\n")
