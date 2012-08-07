import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

for line in infile:
    line = line.split("\t")
    outfile.write("%s\t%s\n" % (line[0].strip(), line[1].strip()) )
