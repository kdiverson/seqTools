import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

for line in infile:
    line = line.split("\t")
    if int(line[2]) > 0:
        outfile.write("%s\t%s\n"% (line[0], line[2]) )
