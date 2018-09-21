#!/usr/bin/env python

"""
Usage: ./contig.py <contig.fasta> <assembler_name>
"""

import fasta
import sys
import operator
import numpy as np

# N50 is the minimum contig length to cover the rest 50% of the genome

nuc_seq = []

for ident, seq in fasta.FASTAReader( open( sys.argv[1] )):
    nuc_seq.append(seq)

nuc_len = []
for i in range(len(nuc_seq)):
    nuc_len.append(len(nuc_seq[i]))

nuc_len.sort()
# print(nuc_len)

print( "Number of Contigs = " + str(len(nuc_len)))
print( "Max Contig Length = " + str(max(nuc_len)))
print( "Min Contig Length = " + str(min(nuc_len)))
print( "Avg Contig Length = " + str(np.mean(nuc_len)))

contig_len = 0
for i in nuc_len:
    contig_len += i

# print(contig_len)


# print(contig_len/2)
N50 = contig_len *.50

count = 0
for i in nuc_len:
    if count < N50:
        count += i
    else:
        print("N50 = " + str(i))
        break
