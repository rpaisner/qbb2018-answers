#!/usr/bin/env python3

import sys
import fasta

reader = fasta.FASTAReader( open( sys.argv[1] ) )
query = open(sys.argv[2])

kmers = {}
k = int(sys.argv[3])

for ident, sequence in reader:
    for i in range(0, len(sequence) - k ):
        target_kmer = sequence[i:i+k]
        if target_kmer not in kmers:
            kmers[target_kmer] = [[ident,i]]
        else:
            kmers[target_kmer].append([ident,i])

reader2 = fasta.FASTAReader( query )

for q_ident, q_sequence in reader2:
    for i in range(0, len(q_sequence) - k):
        kmer = q_sequence[i:i+k]
        if kmer in kmers:
            hits_list = kmers[kmer]
            for tlist in hits_list:
                print(tlist[0], tlist[1], i, kmer)
            #print(ident, i, hits_list, target_kmer)
#print( "Target Sequence Name: " +  

#     print
# for key in kmers:
#     print( key, kmers[key] )