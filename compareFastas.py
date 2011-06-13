import sys
"""Usage: python compareFastas.py path/to/first.fasta /path/to/second.fasta path/to/oufile.fasta

This script compares two fasta files and writes a third fasta will all the sequences that appear in either of the two fasta files, but not both. Sequences do not have to be in the same order.
"""

fasta1 = open(sys.argv[1], 'r')
fasta2 = open(sys.argv[2], 'r')
outfasta = open(sys.argv[3], 'w')

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

fasta1list = []
fasta2list = []

for header, seq in get_next_fasta(fasta1):
    fasta1list.append(header)
for header, seq in get_next_fasta(fasta2):
    fasta2list.append(header)

print header
print type(header)
uniques = set(fasta1list) ^ set(fasta2list)

fasta1.close()
fasta1 = fasta1 = open(sys.argv[1], 'r')

fasta2.close()
fasta2 = fasta2 = open(sys.argv[1], 'r')

for header, seq in get_next_fasta(fasta1):
    if header in uniques:
        outfasta.write("%s\n%s\n" %(header, seq) )
    else:
        pass
        
for header, seq in get_next_fasta(fasta2):
    if header in uniques:
        outfasta.write("%s\n%s\n" %(header, seq) )
    else:
        pass