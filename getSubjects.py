import sys

blastfile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

for line in blastfile:
    line = line.split()
    outfile.write("%s\n" % line[1].strip() )
