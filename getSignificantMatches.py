#!/usr/bin/python
import sys
from optparse import OptionParser

usage = "usage: %prog [options] arg"
parser = OptionParser(usage)
parser.add_option("-t", "--tophits", action="store_true", dest="tophits", default="False", help="only report the top hit for each query [default: %default]")
parser.add_option("-m","--smm", action="store", type="float", dest="smm", default="10", help="significant matches are "
"<= (smm*evalue of top hit) [default: %default]")

(options, args) = parser.parse_args()

blastinfile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

sigmatches = []
previousQuery = ''

for line in blastinfile:
    (query, subject, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore) = line.split("\t")
    eVal = float(eVal)
    if query == previousQuery:
        if options.tophits == True:
            pass
        else:
            if eVal <= sigMatchEvalue:
                sigmatches.append(line)
            else:
                #no match
                pass
    else:
        #query not equal to previous query
        sigmatches.append(line)
        sigMatchEvalue = options.smm*eVal
    previousQuery = query
            
for match in sigmatches:
    outfile.write("%s" %(match) )
