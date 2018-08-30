#!/usr/bin/env python3

""" usage: ./day4-lunch-exercise1.py <threh> <sample1> <sample2>
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
ax.scatter(log_fpkm1, log_fpkm2, alpha=0.1)
ax.set_xlabel("SRR072893")
ax.set_ylabel("SRR072915")
ax.set_title("FPKM Values")

coeff = np.polyfit(log_fpkm1, log_fpkm2, 1)
x = np.linspace(0.000, 8)
f = np.poly1d(coeff)
y = f(x)
ax.plot(x,y)

fig.savefig( "fpkms_scatter_log.png" )
plt.close(fig)


#fpkms_df = pd.DataFrame( fpkms )
#sum = fpkms_df.sum
#fpkms_df.to_csv( sys.stdout )
#print(sum)

# roi_fpkm = df.loc[:, "FPKM"] > float(sys.argv[2])
# roi_chr  = df.loc[:,"chr"] == sys.argv[3]
#
# roi = roi_fpkm & roi_chr
#
# df.loc[roi,:].to_csv( sys.stdout, sep="\t", index=False )


#print( name1, name2 )