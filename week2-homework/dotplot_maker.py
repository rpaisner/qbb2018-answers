#!/usr/bin/env python

""""

./dotplot_maker.py <sorted_lastz.out> <output_graph.png>

Makes a dotplot from lastz data

"""

import fasta
import sys
import operator
import numpy as np
import matplotlib.pyplot as plt

sorted_lastz = open( sys.argv[1] )


count = 0
plt.figure()


for line in sorted_lastz:
    
    if line.startswith("#"): # takes away the header
         pass
    else:
        fields = line.rstrip('\r\n').split('\t')  # strips into a list separated by tabs
        start, end = int(fields[0]), int(fields[1]) # shows only the start and end columns
        plt.plot( [start, end], [count, count + abs(end - start)] )
        count += abs(end - start) # so that every dot is shifted to the end of the last position 

plt.xlim( 0, 1E5 )
plt.ylim( 0, 1E5 )
plt.xlabel( 'reference position' )
plt.ylabel( 'contig position' )
plt.title( sys.argv[2].split('_')[0] + ' aligned contigs to reference dot plot' )
plt.savefig( sys.argv[2].split('.')[0] )

plt.close()