#!/usr/bin/env python3

import sys
gtf_data = open( sys.argv[1] )

count = 0
for line in gtf_data:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split()
    #for i, col in enumerate(fields):
        #print(i, col)
    #break
    if fields[2] == "gene" and fields[17] == "\"protein_coding\";":
        count = count + 1
print(count)
        