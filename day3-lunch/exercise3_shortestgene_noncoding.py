#!/usr/bin/env python3
"""this is for non-protein_coding"""
import sys
gtf_data = open( sys.argv[1] )

find_pos = 21378950
shortest_dist = 10**9
closest_gene = "poop"

for line in gtf_data:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split()
    #for i, col in enumerate(fields):
        #print(i, col)
    #break
    if fields[0] == "3R" and fields[2] == "gene" and fields[17] != "\"protein_coding\";":
        my_dist = 0
        if find_pos < int(fields[3]):
            my_dist = int(fields[3]) - find_pos
        elif find_pos > int(fields[4]):
            my_dist = find_pos - int(fields[4])
        if shortest_dist > my_dist:
            shortest_dist = my_dist
            closest_gene = fields[13]
            
print(closest_gene, shortest_dist)
            