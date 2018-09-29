#!/usr/bin/env python
"""
Usage: ./manhattanplot.py <plink2 file from both genotype and phenotype> <output>
Steph and I modifed a script for GWAS that I found on StackOverflow:
https://stackoverflow.com/questions/37463184/how-to-create-a-manhattan-plot-with-matplotlib-in-python

After some digging I found a way to color by group also on StackOverflow:
https://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category


"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools
import os
import math


df = pd.read_table( sys.argv[1], delim_whitespace=True )
bp = df.loc[:, "BP"].tolist()

positions = []
count = 0
x_labels_pos = []

for i, pos in enumerate(bp):
    if i == 0:
        positions.append(0)
        x_labels_pos.append(0)
    elif bp[i] < bp[i-1]:
        positions.append(count + 1)
        count += 1
        x_labels_pos.append(count + 1)
    else:
        difference = bp[i] - bp[i-1]
        positions.append(count + difference)
        count += difference


p_Val = -np.log(df.loc[:,"P"])
df2 = df.assign(pvalue=p_Val, position=positions)
df2.to_csv(sys.stdout, sep="\t")

# adding significant values as different color
pval = df2.loc[:,"P"]
print(pval)
pval2 = df.iloc[i]["P"]

# this is to make a new col of significant values, and append only those that are greater than p = .00001

df2.loc[df2['pvalue'] > 5, 'Sigval'] = df2['pvalue']
# print(df2)

# this is to assign the chromosome column by its type
df2.CHR = df2.CHR.astype('category')
df2.CHR = df2.CHR.cat.set_categories((
    'chrI', 'chrII', 'chrIII', 'chrIV', 'chrV', 'chrVI', 'chrVII', 'chrVIII', 'chrIX', 'chrX', \
    'chrXI', 'chrXII', 'chrXIII', 'chrXIV', 'chrXV', 'chrXVI', '23', '26'), ordered=True)

groups = df2.groupby('CHR')

# for plotting

fig, ax = plt.subplots(figsize=(16,8))
x_labels = []
for (name, group) in (groups):
    ax.scatter(group.position, group.pvalue, s=0.2)
    x_labels.append(name)
ax.scatter(x=df2.loc[:,"position"],y=df2.loc[:,"Sigval"], color="black", marker="x", s= 1, label='Significant Values')
plt.legend(loc='upper right')
ax.set_xticklabels(x_labels, rotation=50, fontsize=7)
ax.set_xticks(x_labels_pos)
ax.set_xlabel("SNPs at Chromosomes")
ax.set_ylabel("-log(p-value)")
ax.set_title(sys.argv[1][6: -7] + " GWAS")

fname = (sys.argv[1][6:-7] + "_Manhattan_Plot")
# ax.scatter(x=df2.loc[:,"position"],y=df2.loc[:,"pvalue"], color="blue")
#fig.savefig("test.png")
fig.savefig(fname + ".png")
plt.close()

