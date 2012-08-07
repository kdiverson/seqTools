import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

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

for header, seq in get_next_fasta(infile):
    seq = seq.upper()
    if 'N' not in seq:
        outfile.write("%s\n%s\n" % (header, seq))