import sys
""""""
fasta1 = open(sys.argv[1], 'r')
fasta2 = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], 'w')
outfile2 = open(sys.argv[4], 'w')
outfile3 = open(sys.argv[5], 'w')

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
    fasta1list.append(header.strip())
for header, seq in get_next_fasta(fasta2):
    fasta2list.append(header.strip())

fasta1set = frozenset(fasta1list)
fasta2set = frozenset(fasta2list)

#print header
#print type(header)
#uniques = set(fasta1list) ^ set(fasta2list)
uniques = fasta1set.symmetric_difference(fasta2set)
fasta1len = len(fasta1list)
fasta2len = len(fasta2list)
print fasta1list[0]
print fasta2list[0]
print "fasta1:", fasta1len 
print "fasta2:", fasta2len
print "uniques:", len(uniques)
print "number of diff seqs:", fasta1len-fasta2len
print "fasta 2 subset of fasta 1:", fasta1set <= fasta2set
print "fasta 1 suset of fasta 2:", fasta2set <= fasta1set
#for item in uniques:
#    print item
#    print type(item)
fasta1.close()
#fasta1 = fasta1 = open(sys.argv[1], 'r')
onlyInFasta1 = fasta1set.difference(fasta2set)
onlyInFasta2 = fasta2set.difference(fasta1set)
for item in uniques:
    outfile.write("%s\n" %(item))
for item in onlyInFasta1:
    outfile2.write("%s\n" %(item))
for item in onlyInFasta2:
    outfile3.write("%s\n" %(item))
#for header, seq in get_next_fasta(fasta1):
#    if header in uniques:
#        outfasta.write("%s\n%s\n" %(header, seq) )
#    else:
#        pass


