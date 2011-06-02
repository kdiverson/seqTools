import sys
"""Simple script to generate some simple states about a fasta file. I use it for contigs, but it will work with any fasta file
Usage: python contigstats.py path/to/contigs.fa [y]
if y is entered as an option then an output file called contigs_summary.tsv will be wtitten. It's a tsv file that lists the length of each conting and the same summary that's printed to the screen will be written at the bottom of the fille."""
infile = open(sys.argv[1], 'r')

try: 
    if sys.argv[2]:
        writeOutFile = True
        outfile = open("contigs_summary.tsv", 'w')
except IndexError:
    writeOutFile = False

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

totalLen = 0
totalSeqs = 0
longest = 0
shortest = 10000000000000000000000000000
for header, seq in get_next_fasta(infile):
    length = len(seq)
    totalLen += length
    totalSeqs += 1
    if length > longest:
        longest = length
    if length < shortest:
        shortest = length
    if writeOutFile:
        outfile.write("%s\t%s\n" %(header,length))

avgLen = totalLen/totalSeqs
trimmedAvg = (totalLen-(longest+shortest))/(totalSeqs-2)

print "total contigs:", totalSeqs
print "average length:", avgLen, "bp"
print "trimmed average length:", trimmedAvg, "bp"
print "shortest conting:", shortest, "bp"
print "longest contig:", longest, "bp"

infile.close()

if writeOutFile:
    outfile.write("total contigs: %s\naverage length: %s\ntrimmed average length: %s\nshortest contig: %s\nlongest contig: %s" %(totalSeqs, avgLen, trimmedAvg, shortest, longest))
    outfile.close()
