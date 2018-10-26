#!/usr/bin/env python3

"""
Usage:
./peakscounter.py CTCF_gained.bed CTCF_lost.bed ER4_exons.bed ER4_introns.bed ER4_promoters.bed G1E_exons.bed G1E_introns.bed G1E_promoters.bed

"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gained = 0
lost = 0

peaks_gained = open( sys.argv[1] )
for line in peaks_gained:
    if line.startswith("chr19"):
        gained += 1
        
peaks_lost = open( sys.argv[2] )
for line in peaks_lost:
     if line.startswith("chr19"):
         lost += 1       
# print( gained )
# print( lost )

YVAL = [gained, lost]
XVAL = [0, 1]

# print(YVAL)
xval_ticks_labels = ['Gained', 'Lost']


""" The next plot for features"""


ER4_exons = open(sys.argv[3])
ER4_introns = open(sys.argv[4])
ER4_promoters = open(sys.argv[5])
G1E_exons = open(sys.argv[6])
G1E_introns = open(sys.argv[7])
G1E_promoters = open(sys.argv[8])

ER4_exons_sum = sum(1 for line in ER4_exons)
ER4_introns_sum = sum(1 for line in ER4_introns)
ER4_promoters_sum = sum(1 for line in ER4_promoters)
G1E_exons_sum = sum(1 for line in G1E_exons)
G1E_introns_sum = sum(1 for line in G1E_introns)
G1E_promoters_sum = sum(1 for line in G1E_promoters)


XVAL2 = [0, 1, 2]
YVAL2_ER4 = [ER4_exons_sum, ER4_introns_sum, ER4_promoters_sum]
YVAL2_G1E = [G1E_exons_sum, G1E_introns_sum, G1E_promoters_sum]


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,5))

barlist = ax1.bar(XVAL, YVAL)
ax1.set_xticks(XVAL)
ax1.set_xticklabels(xval_ticks_labels)
barlist[0].set_color('r')
ax1.set_title("CTCF Binding Sites At G1E to ER4 Transition")
ax1.set_ylabel("Counts")
ax1.set_xlabel("CTCF binding sites")

""" axes 2"""
xval2_ticks_labels = ['Exons', 'Introns', 'Promoters']

p1 = ax2.bar(XVAL2, YVAL2_ER4, color='cyan')
p2 = ax2.bar(XVAL2, YVAL2_G1E, color='magenta', bottom=YVAL2_ER4)
ax2.set_xticks(XVAL2)
ax2.set_xticklabels(xval2_ticks_labels)
ax2.set_title("Types of CTCF Binding Sites in G1E and ER4")
ax2.set_ylabel("Counts")
ax2.set_xlabel("Areas of CTCF Binding")

fig.savefig("CTCF_binding.png")
plt.close(fig)