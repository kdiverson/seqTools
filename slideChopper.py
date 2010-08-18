#!/usr/bin/env python

"""Usage: seqChopperSlide.py /path/to/fasta /path/to/chopped/fasta window_size slide_length
example: python seqChopper.py myFasta.fasta myNewFasta.fasta 50 15"""

import sys

def get_next_fasta (fileObject):
    '''usage: for header, seq in get_next_fasta(fileObject):
    This is a generator that returns one fasta record's header and
sequence at a time from a multiple fasta file. Return character is removed
from the header. The sequence is returned as one continuous string
with no returns. The returned value is a tuple (header, sequence)
If their is no sequence associated with a header, seq will be an
empty string
Code simplification contributed by Dattatreya Mellacheruvu
01/16/2009, Jeffrey R. de Wet

    '''
    header = ''
    seq = ''
    #The following for loop gets the header of the first fasta
    #record. Skips any leading junk in the file
    for line in fileObject:
        if line.startswith('>'):
            header = line.strip()
            break
    
    for line in fileObject:
        if line.startswith('>'):
            yield header, seq
            header = line.strip()
            seq = ''
        else:
            seq += line.strip()
    #yield the last entry
    if header:
        yield header, seq
        

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
window = int(sys.argv[3])
slide = int(sys.argv[4])



#while start < maxseqlength:
for header, seq in get_next_fasta(infile):
    start = 0
    end = window
    outfile.write("%s&\n%s\n" %(header, seq))
    while end < len(seq)+window:
        seqFrag = seq[start:end]
        outfile.write("%s@%s-%s\n%s\n"%(header,start, end, seqFrag))
        start = start+slide
        end = end+slide

infile.close()
infile = open(sys.argv[1], 'r')
