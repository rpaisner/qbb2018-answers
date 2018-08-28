#!/usr/bin/env python3
import sys
f = open( sys.argv[1] )

count = 0
mapq_sum= 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    mapq = int(fields[4])
    count +=1
    mapq_sum += mapq
    average = mapq_sum/count
    #flag = fields[1]
print(average)