#!/usr/bin/env python3
import sys
f = open( sys.argv[1] )

count = 0
for i, line in enumerate( f ):
    if line.startswith("@)"):
        continue
    #fields = line.rstrip("\r\n").split("\t")
    #flag = fields[1]
    if "XM:i:0" in line:
        count +=1
print(count)