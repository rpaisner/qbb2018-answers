#!/usr/bin/env python

import sys
import numpy
import hifive
import pandas as pd
import seaborn as sns


f = open(sys.argv[1])

midpoint_list = []
for i, line in enumerate(f):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    if chrom == "chr17" and start >= 15000000 and end <= 17500000:
        midpoint = ((end - start)/2) + start
        midpoint_list.append(midpoint)
# print(len(midpoint_list))


    


hic = hifive.HiC('week13.hcp')
data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')

data[:, :, 1] *= numpy.sum(data[:, :, 0]) / numpy.sum(data[:, :, 1])
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]
# print(data)

bin_list = []
for j in midpoint_list:
    i = (j - 15000000)/10000 
    bin_list.append(i)

CTCF= numpy.unique(bin_list)

enriched = []
for i in range(len(CTCF)):
    for j in range(i, len(CTCF)):
        coordinate = data[CTCF[i], CTCF[j]]
        if data[CTCF[i], CTCF[j]] > 1:
            enriched.append((CTCF[i], CTCF[j], coordinate))
# print(enriched)

genomic_enriched = []
for row, col, value in enriched:
    genomic_row = (row*10000) + 15000000
    genomic_col = (col*10000) + 15000000
    genomic_enriched.append((genomic_row, genomic_col, value))
# print(genomic_enriched)

df10 = pd.DataFrame(genomic_enriched)
df10.columns = ["Start", "End", "Enrichment"]
ascending = df10.sort_values(by=["Enrichment"], ascending=False)    
# print(ascending)
print(ascending.values.tolist())


