#!/user/bin/env python

"""Usage: blastXMLparser.py /path/to/blast/results.xml /path/to/output.csv

requires python > 2.5 or cElementTree module.

This script parses a blast output xml file and writes a csv file of select data

output example:

query, hit, bit score, e value

created 2/10 by Kathryn Iverson kiverson@umich.edu
"""

import sys
import xml.etree.cElementTree as cet

infile = sys.argv[1]
output = sys.arv[2]

source = open(infile, 'r')

# get an iterable
context = cet.iterparse(source, events=("start", "end"))

# turn it into an iterator
context = iter(context)

# get the root element
event, root = context.next()

query = ''
hit = ''
bitScore = 0.0
eValue = 0.0

outfile = open(output, 'w')

for event, elem in context:
    if event == "end" and elem.tag == "Iteration_query-def":
       query = elem.text
       
    if event == "end" and elem.tag == "Hit_def":
        hit = elem.text
        
    if event == "end" and elem.tag == "Hsp_bit-score":
        bitScore = elem.text
            
    if event == "end" and elem.tag == "Hsp_evalue":
        eValue = elem.text
        outfile.write('%s, %s, %s, %s\n' %(query, hit, bitScore, eValue))
        root.clear()
    
