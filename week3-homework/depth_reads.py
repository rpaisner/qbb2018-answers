#!/usr/bin/env python

"""
Usage:
./depth_reads.py <vcf> <output.png>
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DP_X_Value = []
DP_Y_Value = []
AF_Y_Value = []
x = 1

vcf = open( sys.argv[1] )
for line in vcf:
    if line.startswith("#"):
        continue    
    fields = line.rstrip("\r\n").split("\t")
    DP_List = fields[7].split(";")
    try:
        Depth = DP_List[7]
    except IndexError:
        continue
    DP_Value = Depth.split("=")
    DP_Y_Value.append(float(DP_Value[1]))
    DP_X_Value.append(x)
    AF_Value = DP_List[3].split("=")
    AF_Y_Value.append(float(AF_Value[1]))
    # GQ_Value = DP_List[3].split("=")
    # GQ_Y_Value.append(float(AF_Value[1]))
    x += 1
# print(AF_Y_Value)

GQ_Y_Value = []
i = 1

# having problems with my other vcf file, so made another one
vcf = open( sys.argv[2] )
for line in vcf:
    if line.startswith("#"):
        continue    
    fields = line.rstrip("\r\n").split("\t")
    DP_List = fields[7].split(";")
    try:
        Depth = DP_List[7]
    except IndexError:
        continue
    col9 = fields[9].split(":")
    try:
        GQ_Value = col9[1]
    except IndexError:
        i += 1
    GQ_Y_Value.append(float(GQ_Value)) 
    i += 1

    # to get the summary of predicted effect of each variant
    ann = line.split('|')
    # ann_type = ann[1]
    # print(ann[1])
 
 # bar plot summary text

List = []
List_X = []

vcf = open( sys.argv[3] )
for line in vcf:
    fields = line.rstrip("\r\n").split("\t")
    fields[1] = int(fields[1])
    List.append((fields[1]))
    List_X.append(fields[0])
# print(List_X)
height = List
bars = List_X
y_pos = np.arange(len(bars))


   


   
        



fig, axes = plt.subplots(nrows= 2, ncols=2)
axes = axes.flatten()
fig.set_size_inches(20, 12)
axes[0].hist(np.log10(DP_Y_Value), bins=40, color="cyan")
axes[1].hist((GQ_Y_Value), bins=40, color="magenta")
axes[2].hist((AF_Y_Value), bins=40, color="brown")
axes[3].bar(List_X, height,)
axes[3].set_xticklabels(List_X, rotation=20)
# axes[3].xticks(y_pos, bars)

# ax.scatter(DP_X_Value, DP_Y_Value, alpha=0.17, s=1.5, color="magenta")
axes[0].set_xlabel("Log of Assembled contigs Depth")
axes[0].set_ylabel("Positions from the reference")
axes[1].set_xlabel("High Frequency Variants")
axes[1].set_ylabel("Genotype Quality")
axes[2].set_xlabel("High Quality Variants")
axes[2].set_ylabel("Allele Frequency")
axes[3].set_xlabel("Predicted Effect")
axes[3].set_ylabel("Number of Variants")
fig.suptitle("Variant Plot")
fig.savefig("_dotplot.png")
plt.tight_layout()
plt.close(fig)


# axes[0,1]
# fig, axes = plt.subplots(nrows=2, ncol=2, figsize(10,10))


# vcf
#
# fig, ax = plt.subplots()
# i=1
# for line in vcf:
#     if line.startswith("#"):
#         continue
#     fields = line.rstrip("\r\n").split("\t")
#     column = fields[7].split(";")
#     dp = column[7].split("=")
#     dp_num = dp[1]
#     i += 1
#     ax.(i, dp_num, alpha=0.5, color="red")
#
# ax.set_title("Graph for DP")
# fig.savefig("depth.png")
# plt.close(fig)
#