import sys

infasta = open(sys.argv[1], 'r')
infile = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], 'w')

aligned = set()

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

for line in infile:
    line = line.split("\t")
    read = line[0]
    aligned.add(read)

aligned = frozenset(aligned)

for header, seq in get_next_fasta(infasta):
    header = header.strip()
    if header[1:] not in aligned:
        outfile.write("%s\n%s\n" %(header, seq) )
