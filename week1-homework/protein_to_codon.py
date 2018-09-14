#!/usr/bin/env python

"""
	$ ./protein_to_codon.py hspnuc.fa aligned_proteinHSP.fa
"""

import sys
import fasta
import numpy as np
import matplotlib.pyplot as plt

dnaReader = fasta.FASTAReader(open(sys.argv[1]))
protReader = fasta.FASTAReader(open(sys.argv[2]))

prot_list = []

for ident, seq in fasta.FASTAReader(open(sys.argv[2])):
    prot_list.append( seq )
    
# This will contain a list of aligned DNA sequences for the 1000 homologues
# Index one of this list contains the aligned query DNA sequence
alignedDNA = []

for (dnaID, dnaSeq), (protID, protSeq) in zip(dnaReader, protReader):
	dnaGapped = []
	# Stores current position in dna sequence
	dnaIndex = 0
	for aa in protSeq:
		if aa == '-':
			dnaGapped.append('---')
		else:
			dnaGapped.append(dnaSeq[dnaIndex:dnaIndex + 3])
			# Only increase dnaIndex on ungapped amino acids
			dnaIndex += 3
	alignedDNA.append(dnaGapped)


#this iterates through the list not including the query, because thats not a homologous sequence
dS = []
dN = []
x = []
for i in range(len(alignedDNA[0])):
    dN.append(0)
    dS.append(0)
    x.append(i)


for i in range(1, len(alignedDNA)):
    for j in range(0, len(alignedDNA[i])):
        if alignedDNA[0][j] == "---":
            pass
        elif alignedDNA[i][j] == alignedDNA[0][j]:
            pass
        else:
            #
            if prot_list[i][j] != prot_list[0][j]:
                dN[j] += 1
            else:
                dS[j] += 1



#print(dN, dS)
diff = (np.array(dN) - np.array(dS)).tolist()
ratio = (np.array(dN) / np.array(dS)).tolist()


plt.figure()
plt.scatter(x, diff)
plt.title('Positive Selection on a query sequence', fontsize='22')
plt.xlabel('query sequence codon position', fontsize=15)
plt.ylabel('dN - dS', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()
plt.close()
