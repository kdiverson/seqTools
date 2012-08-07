import sys

infile = open(sys.argv[1], 'r')

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

def sd(myList, avg):
    tmp = []
    for item in myList:
        tmp.append((item - avg)**2)
    SD = (float(sum(tmp))/len(tmp))**0.5
    return SD
    
def median(s):
    s= sorted(s)
    i = len(s)
    if not i%2:
        return (s[(i/2)-1]+s[i/2])/2.0
    return s[i/2]

totalLen = 0
totalSeqs = 0
longest = 0
tmpcount = 0
shortest = 10000000000000000000000000000
lengthlist = []
for header, seq in get_next_fasta(infile):
    length = len(seq)
    lengthlist.append(length)
    totalLen += length
    totalSeqs += 1
    if length > longest:
        longest = length
    if length < shortest:
        shortest = length
    if length >= 100:
        tmpcount += 1

avgLen = totalLen/totalSeqs
trimmedAvg = (totalLen-(longest+shortest))/(totalSeqs-2)

print "total contigs:", totalSeqs
print "average length:", avgLen, "bp"
print "trimmed average length:", trimmedAvg, "bp"
#print "other avg: ", float(sum(lengthlist))/len(lengthlist)
print "standard deviation: ", sd(lengthlist, avgLen)
print "median: ", median(lengthlist)
print "greater than or equal to 100: ", tmpcount
print "shortest conting:", shortest, "bp"
print "longest contig:", longest, "bp"
print "total length:", totalLen/1000000.00, "Mb"

infile.close()
