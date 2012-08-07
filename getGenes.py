#!/usr/bin/python
"""Usage: getGenes.py path/to/metagene/outfile.out path/to/contig/file.fasta /path/to/gene.fasta /path/to/ORF.fasta"""

import sys
from itertools import tee, islice, izip_longest
import string

mgFile = open(sys.argv[1], 'r')
infasta = open(sys.argv[2], 'r')
geneFasta = open(sys.argv[3], 'w')
ORFfasta = open(sys.argv[4], 'w')

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

def get_next(some_iterable, window=2):
    items, nexts = tee(some_iterable, 2)
    nexts = islice(nexts, window, None)
    return izip_longest(items, nexts)

#TRANS = { "T": "A", "A": "T", "G": "C", "C": "G" }

def complementary_strand(strand):
    return strand.translate(string.maketrans('TAGCtagc', 'ATCGATCG'))


#def complement(strand):
#    comp = ''
#    for base in strand.upper():
#        comp = comp.join(TRANS[base])
#    yield TRANS[base]

geneDict = {}
ORFdict = {}
#firstLine = True

lastLine = ''

for line, next_lines in get_next(mgFile):
    #window size of two; check that current line and next two lines start with '#' this means were on contig name
    if next_lines and next_lines.startswith("#") and line.startswith('#'): #and not (lastLine.startswith("#"):
        contigName = line.strip("#").strip()
        #print "contig name:", contigName
        #print "next line:", next_lines
    elif not line.startswith("#"):
        #print "in else"
        #print "line:", line
        line = line.split()
        name = line[0]
        start = line[1]
        stop = line[2]
        strand = line[3]
        frame = line[4]
        
        if line[6] > 0:
            #predicted gene
            if contigName in geneDict.keys():
                geneDict[contigName].append([name,start,stop,strand,frame])
            else:
                geneDict[contigName]=[[name,start,stop,strand,frame]]

        else:
            #predicted ORF
            if contigName in ORFdict.keys():
                ORFdict[contigName].append([name,start,stop,strand,frame])
            else:
                ORFdict[contigName]=[[name,start,stop,strand,frame]]

    #lastLine = line

    else:
        continue

print "ORFs: ", len(ORFdict.keys())
print "Genes: ", len(geneDict.keys())

for header, seq in get_next_fasta(infasta):
    ORF = False
    
    try:
        geneList = geneDict[header[1:]]    
    except KeyError:
        try:
            geneList = ORFdict[header[1:]]
            ORF = True
        except KeyError:
            print header[1:], "nothing predicted!!"
            continue
        
    for gene in geneList:
        name = gene[0]
        start =int(gene[1])
        stop = int(gene[2])
        strand = gene[3]
        frame = gene[4]

        if strand == '-':
            seq = complementary_strand(seq)
        
        if ORF is False:
            geneFasta.write("%s_%s\n%s\n" %(header, name, seq[start-1:stop]) )
        else:
            ORFfasta.write("%s_%s\n%s\n" %(header, name, seq[start-1:stop]) )

