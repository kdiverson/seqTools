import sys

infile = open(sys.argv[1], 'r')

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

for header, seq in get_next_fasta(infile):
    print header
    print seq[1:-1]
