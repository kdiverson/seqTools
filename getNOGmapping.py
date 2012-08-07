#!/usr/bin/python

import sys

infile = open(sys.argv[1], 'r')
mapfile = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], 'w')

nogDict = {}

for line in mapfile:
    line = line.split("\t")
    nogDict[line[0]] = line[4]

for line in infile:
    try:
        outfile.write("%s\n" %(nogDict[line.strip()]) )
    except KeyError:
        print "couldn't find %s in map file" %(line.strip())
