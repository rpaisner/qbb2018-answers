#!/usr/bin/env python3

""" Usage ./linear_regression.py <H3K27ac.tab> <H3K27me3.tab <H3K4me1.tab> <H3K4me3.tab> <H3K9ac.tab> <.ctab> 
                                       
Making linear regression
                                      
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

mean1 = pd.read_table( sys.argv[1], index_col=0 ).iloc[:,5-1]
mean2 = pd.read_table( sys.argv[2], index_col=0 ).iloc[:,5-1]
mean3 = pd.read_table( sys.argv[3], index_col=0 ).iloc[:,5-1]
mean4 = pd.read_table( sys.argv[4], index_col=0 ).iloc[:,5-1]
mean5 = pd.read_table( sys.argv[5], index_col=0 ).iloc[:,5-1]
ctab1 = pd.read_table( sys.argv[6], index_col='t_name' ).loc[:,"FPKM"]

name1 = sys.argv[1].split(os.sep)[-1]
name2 = sys.argv[2].split(os.sep)[-1]
name3 = sys.argv[3].split(os.sep)[-1]
name4 = sys.argv[4].split(os.sep)[-1]
name5 = sys.argv[5].split(os.sep)[-1]
cname1 = sys.argv[6].split(os.sep)[-1]

d = { name1:mean1,
      name2:mean2,
      name3:mean3,
      name4:mean4,
      name5:mean5,
      cname1:ctab1 }
df = pd.DataFrame( d )
roi = df.loc[:,name1].notna()


small_df = df.loc[roi,:]

y = small_df.loc[:,cname1]
x = small_df.loc[:,[name1,name2,name3,name4,name5]]

small_df.columns = small_df.columns.str.replace(".","_")
# print(small_df)
#
mod = smf.ols(formula='t_data_ctab ~ H3K27ac_tab + H3K27me3_tab + H3K4me1_tab + H3K4me3_tab + H3K9ac_tab', data=small_df)
res = mod.fit()
print(res.summary())


# ax.plot(x, res.fittedvalues)