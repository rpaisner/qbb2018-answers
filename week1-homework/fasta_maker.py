#!/usr/bin/env python3

import sys
fasta = open( sys.argv[1] )

for line in fasta:
    line = line.rstrip("\r\n").split()
    print("> " + line[0] + '\n' + line[1])
    
    