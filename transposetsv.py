import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

cat = []
count = []

for line in infile:
    line = line.split("\t")
    cat.append(line[0])
    count.append(line[1])

for item in cat:
    outfile.write(str(item) + "\t")

outfile.write("\n")
for item in count:
    outfile.write(str(item).strip() + "\t")
#outfile.writelines(count)

outfile.write("\n")
