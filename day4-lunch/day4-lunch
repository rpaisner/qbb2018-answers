#!/usr/bin/env python3

""" usage: ./day4-lunch-exercise1.py <threh> <sample1> <sample2>
""" 

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

threshold = float( sys.argv[1] )

fpkms = {}
for filename in sys.argv[2:]:
    name = filename.split( os.sep )[-2]
    fpkm = pd.read_csv( filename, sep="\t", index_col="t_name" ).loc[:,"FPKM"]
    
    fpkms[name] = fpkm
    
# no longer needed
# name2 =  sys.argv[2].split( os.sep )[-2]
# fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col="t_name" ).loc[:,"FPKM"]

#fpkms = { name1 : fpkm1,
 #         name2 : fpkm2 }

fpkms_df = pd.DataFrame(fpkms)
df = fpkms_df.sum(axis=1)
          
#df = fpkm1 + fpkm2

roi = df > threshold
total2 = df.loc[roi]
print(total2)
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