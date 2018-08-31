#!/usr/bin/env python3
"""this is for non-protein_coding"""
import sys
gtf_data = open( sys.argv[1] )

for line in gtf_data:
    if line.startswith("t"):
         continue
    fields = line.rstrip("\r\n").split()
    

    if fields[2] == "+":
         start = int( fields[3]) - 500
         if start < 0:
             start = 0
         end = fields[3]
         print( fields[1] + "\t" + str(start) + "\t" + str(end) + "\t" + fields[5] )
         
    else:
        start = int( fields[4]) + 500
        end = fields[4] 
        print( fields[1] + "\t" + str(end) + "\t" + str(start) + "\t" + fields[5] )
#    else:
#        fields[2] = fields[2] + 500
         
#         if find_pos < int(fields[3]):
#             my_dist = int(fields[3]) - find_pos
#         elif find_pos > int(fields[4]):
#             my_dist = find_pos - int(fields[4])
#         if shortest_dist > my_dist:
#             shortest_dist = my_dist
#             closest_gene = fields[13]
#
# print(closest_gene, shortest_dist)