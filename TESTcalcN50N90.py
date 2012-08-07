#!/usr/bin/python
import sys

infile = open(sys.argv[1], 'r')

def get_next_fasta (fileObject):
    '''usage: for header, seq in get_next_fasta(fileObject):
    '''
    header = ''
    seq = ''
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

contigs = []
total = 0

for header, seq in get_next_fasta(infile):
   length = len(seq) 
   contigs.append(length)
   total += length

halfTot = 0
contigs.sort()

for contig in contigs:
    halfTot += contig
    if halfTot>total/2:
        print "N50:", contig
        break
