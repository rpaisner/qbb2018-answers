#!/usr/bin/env python3

""" Usage ./linear_regression.py <H3K27ac.tab> <H3K27me3.tab <H3K4me1.tab> <H3K4me3.tab> <H3K9ac.tab> <.ctab> 
                                       
Making linear regression for Log function
                                      
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df_H3K27ac = pd.read_csv(sys.argv[1], sep="\t", index_col=0).iloc[:,5-1]
df_H3K27me3 = pd.read_csv(sys.argv[2], sep="\t", index_col=0).iloc[:,5-1]   
df_H3K4me1 = pd.read_csv(sys.argv[3], sep="\t", index_col=0).iloc[:,5-1]   
df_H3K4me3 = pd.read_csv(sys.argv[4], sep="\t", index_col=0).iloc[:,5-1]    
df_H3K9ac = pd.read_csv(sys.argv[5], sep="\t", index_col=0).iloc[:,5-1]
df_ctab = pd.read_csv(sys.argv[6], sep="\t", index_col = "t_name")

coi = ["FPKM"]
fpkm_df= df_ctab.loc[:,coi]
log_fpkm_df = np.log(fpkm_df+1)



log_df = pd.concat([df_H3K27ac, df_H3K27me3, df_H3K4me1, df_H3K4me3, df_H3K9ac, log_fpkm_df], ignore_index = True, axis=1, sort=True)
log_df.rename(index = str, columns={ 0:"H3K27ac", 1:"H3K27me3", 2:"H3K4me1", 3:"H3K4me3",4:"H3K9ac",5:"FPKM"}, inplace = True)
# print(log_df)


function = 'FPKM ~ H3K27ac + H3K27me3 + H3K4me1 + H3K4me3 + H3K9ac'
mod = smf.ols(formula=function, data=log_df)
res = mod.fit()
print(res.summary())
# print(res.resid)

fig, ax = plt.subplots()
fig.suptitle( "log of Residual Histogram with Regression" )
ax.hist(res.resid, bins =100)
ax.set_xlim(-20,20)
ax.set_xlabel( "Regression standardized Residual" )
ax.set_ylabel( "Frequency" )
fig.savefig( "log_residuals.png" )
plt.close(fig)
