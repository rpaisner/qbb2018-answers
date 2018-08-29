#!/usr/bin/env python3

import sys

fly_dict = {}

gtf_data = open( sys.argv[1] )

for line in gtf_data:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split()
    if fields[2] == "gene":
        biotype = fields[17]
        
        if biotype not in fly_dict:
            fly_dict[biotype] = 1
        else:
            fly_dict[biotype] += 1
print(fly_dict)