#!/usr/bin/env python3

"""
Usage: ./01-merge.py <ctab_file1> <ctab_file2>
Merge FPKM values from two ctab files

"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

fpkm_dic = {}
df = pd.read_csv(sys.argv[1])

for index, sample, sex, stage in df.itertuples():
    filename = os.path.join( sys.argv[2], sample, "t_data.ctab"  )
    ctab_df = pd.read_table( filename, index_col="t_name" ).loc[:,"FPKM"]
    fpkm_dic[str(sex) + str(stage)] = ctab_df


dataframe = pd.DataFrame(fpkm_dic)
dataframe.to_csv(sys.stdout)


