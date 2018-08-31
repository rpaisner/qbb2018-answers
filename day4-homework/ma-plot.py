#!/usr/bin/env python3

""" usage: ./day4-lunch-exercise1.py <sample1> <sample2>
""" 

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


name1 =  sys.argv[1].split( os.sep )[-2]
fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col="t_name" ).loc[:,"FPKM"]
log_fpkm1 = np.log(fpkm1+1)
name2 =  sys.argv[2].split( os.sep )[-2]
fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col="t_name" ).loc[:,"FPKM"]
log_fpkm2 = np.log(fpkm2+1)
fig, ax = plt.subplots()
# ax.scatter(log_fpkm1, log_fpkm2, alpha=0.1)
ax.set_xlabel("SRR072893")
ax.set_ylabel("SRR072915")
ax.set_title("FPKM Values")

coeff = np.polyfit(log_fpkm1, log_fpkm2, 1)
x = np.linspace(0.000, 8)
f = np.poly1d(coeff)
y = f(x)
# ax.plot(x,y)

# df_concat = pd.concat(fpkm1, fpkm2)
df_mean = 0.5 * ( log_fpkm2 + log_fpkm1 )
df_ratio = np.log((fpkm1+1)/(fpkm2+1))
ax.scatter(df_mean, df_ratio, alpha= 0.1302)

plt.savefig('poo.png')
plt.close(fig)