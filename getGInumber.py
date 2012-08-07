#!/usr/bin/python

import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

linesSkipped = 0

for line in infile:
    try:
        line = line.split('\t')
        id = line[1]
        giNum = id.split('|')[1]
        outfile.write("%s\n" %(giNum) )
    except IndexError:
        linesSkipped += 1
print "lines skipped:", linesSkipped
