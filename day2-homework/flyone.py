#!/usr/bin/env python3

import sys
f = open( sys.argv[1] )

for i, line in enumerate( f ):
    if "DROME" in line and "FBgn" in line:
        fields = line.rstrip("\r\n").split()
        print(fields[3], "\t", fields[2])
