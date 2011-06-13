#!/usr/bin/python
'''usage: python removeShortContigs.py path/to/infile/ path/to/outfile/ cutoff
removes all sequences in a file that are shorter than the cutoff
'''
import sys

infasta = open(sys.argv[1], 'r')
cutoff = int(sys.argv[3])
outfasta = open(sys.argv[2], 'w')

def get_next_fasta (fileObject):
    '''usage: for header, seq in get_next_fasta(fileObject):
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

for header, seq in get_next_fasta(infasta):
    if len(seq) > cutoff:
        outfasta.write("%s\n%s\n" %(header, seq) )
    else:
        pass

infasta.close()
outfasta.close()
