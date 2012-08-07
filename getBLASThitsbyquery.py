import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

previousQuery = ''
hitdict = {}

for line in infile:
    line = line.split("\t")
    query = line[0]
    hit = line[1]
        
    if query in hitdict.keys():
        if hit not in hitdict[query]:
            hitdict[query].append(hit)
    else:
        if len(hitdict) > 0:
            for hit in hitdict:
                outfile.write("%s\t%s\n" % (hit, ', '.join(hitdict[hit])))
        hitdict = {}
        hitdict[query] = [hit]

#get the last one
for hit in hitdict:
    outfile.write("%s\t%s\n" % (hit, ', '.join(hitdict[hit])))


#     while(query == previousQuery):
#         if query in hitdict.keys():
#             if hit not in hitdict[query]:
#                 hitdict[query].append(hit)
#         else: 
#             hitdict[query] = [hit]
#         try:
#             line = infile.readline()
#             line = line.split("\t")
#             previousQuery = query
#             query = line[0]
#             hit = line[1]
#         except StopIteration:
#             break


# for line in infile:
#     line = line.split("\t")
#     query = line[0]
#     hit = line[1]
#     previousQuery = query
#     
#     while(query == previousQuery):
#         if query in hitdict.keys():
#             if hit not in hitdict[query]:
#                 hitdict[query].append(hit)
#         else: 
#             hitdict[query] = [hit]
#         try:
#             line = infile.next()
#             line = line.split("\t")
#             previousQuery = query
#             query = line[0]
#             hit = line[1]
#         except StopIteration:
#             break