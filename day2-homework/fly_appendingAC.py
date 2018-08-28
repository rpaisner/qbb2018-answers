#!/usr/bin/env python3

import sys
fly_data = open( sys.argv[1] )
t_data = open( sys.argv[2] )

fly_dict = {}
for line in fly_data:
    fields = line.rstrip("\r\n").split()
    fly_dict[fields[0]] = fields[1]
print(fly_dict)

for line2 in t_data:
    count = 0
    if "FBgn" in line2:
        fields2 = line2.rstrip("\r\n").split()
        if fields2[8] in fly_dict.keys():
            if count < 100:
                print(fly_dict[fields2[8]], "\t", line2)
                count = count + 1
        else:
            if sys.argv[3] == 'print':
                print('Found no match')
