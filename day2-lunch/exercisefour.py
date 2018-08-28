#!/usr/bin/env python3
import sys
f = open( sys.argv[1] )

count = 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    count +=1
    #flag = fields[1]
    if count > 10 in line:
        break
    else:
        print(fields[2])