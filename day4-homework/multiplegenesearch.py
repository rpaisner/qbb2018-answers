#!/usr/bin/env python3

"""
usage: ./random_gene_search.py <gene_name> <samples> <ctab_dir>
create s a random gene search for females and males
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

for search in sys.argv[3:]:
    def genderfilter_s(gender, gene):
        df = pd.read_csv(sys.argv[1])
        
        soi = df.loc[:, "sex"] == gender
        df = df.loc[soi,:]
        stages = []
        fpkms = []
        for index, sample, sex, stage in df.itertuples():
            filename = os.path.join(sys.argv[2], sample, "t_data.ctab", )
            ctab_df = pd.read_table(filename, index_col="t_name")
            roi = ctab_df.loc[:,"gene_name"] == gene
            fpkms.append(ctab_df.loc[roi, "FPKM"].mean())

        
            stages.append(stage)
    
        return fpkms, stages

    
    fpkms_m, stages = genderfilter_s('male', search)
    fpkms_f, stages = genderfilter_s('female', search)



    fig, ax = plt.subplots()
    ax.plot(fpkms_f, label="female", c="red")
    ax.plot(fpkms_m, label="male", c="blue")
    ax.set_title(search)
    ax.set_xlabel("developmental stage")
    ax.set_ylabel("mean mRNA abudance (RPKM)")
    ax.set_xticklabels(stages, rotation=90)
    plt.legend(bbox_to_anchor=(1.04, 0.5), loc=2, borderaxespad=0)
    plt.tight_layout()
    fig.savefig(search, bbox_inches='tight')
    plt.close(fig)