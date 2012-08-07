import sys

blastfile = open(sys.argv[1], 'r')
earlyfasta = open(sys.argv[2], 'r')
latefasta = open(sys.argv[3], 'r')
earlycore = open(sys.argv[4], 'w')
latecore = open(sys.argv[5], 'w')

late = []
early = []

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

for line in blastfile:
    line = line.split()
    late.append(line[0])
    early.append(line[1])
    
for header, seq in get_next_fasta(earlyfasta):
    if header[1:].strip() in early:
        earlycore.write("%s\n%s\n" % (header, seq))
        
for header, seq in get_next_fasta(latefasta):
    if header[1:].strip() in late:
        latecore.write("%s\n%s\n" % (header, seq))
