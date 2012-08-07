import sys

mgFile = open(sys.argv[1], 'r')

geneDict = {}
head = []
contigName = ''
count = 0
count2 = 0
for line in mgFile:
    count += 1
    while(line.startswith("#")):
        if len(head) > 2:
            head = []
        head.append(line[2:])
        line = mgFile.next()
    
    contigName = str(head[0]).strip()
    
    linecount = 0
    line = line.split()
    name = line[0]
    start = line[1]
    stop = line[2]
    strand = line[3]
    frame = int(line[4])
    part = int(line[5])
    if part == 00:#part == 10 or part == 11:
        #print contigName, start, stop
        count2 += 1
print count2, "out of ", count
    #if contigName in geneDict.keys():
    #    geneDict[contigName].append([name,start,stop,strand,frame])
    #else:
    #    geneDict[contigName]=[[name,start,stop,strand,frame]]
