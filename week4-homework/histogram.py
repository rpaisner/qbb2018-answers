#!/usr/bin/env python

"""
Usage: ./histogram.py <genotype file from GWAS> <histo.png>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

genotype = open(sys.argv[1])

# AF = allele frequency

AF = []

for line in genotype:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    # print(fields[7])
    AF_Values = fields[7][3:]
    AF_Value = AF_Values.split(",")
    for line in AF_Value:
        AF.append(float(line))

fig, ax = plt.subplots()
ax.hist(AF, bins=500, color="magenta")
ax.set_ylabel('Frequency')
ax.set_xlabel('Allele Frequency')
ax.set_title('Histogram for Allele Frequencies of Genotype')
plt.tight_layout()

fig.savefig("histo.png")
plt.close(fig) 