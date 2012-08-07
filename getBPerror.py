import linecache
import sys

line = linecache.getline(sys.argv[1], 2)

line = line.split()

print line[-1]
