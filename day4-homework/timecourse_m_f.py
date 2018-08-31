#!/usr/bin/env python3

""" Usage ./03-timecourse.py <t_name> <samples.csv> <ctab_dir>

Create a timecourse of a given transcript (FBtr033) for females

"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt



replicate_file = sys.argv[4]



def timecourse(gender):
    # gets the samples of your desired sex
    df = pd.read_csv( sys.argv[2] )
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]
    
    fpkms = []
    # loops over the samples and gets the data
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab"  )
        ctab_df = pd.read_table( filename, index_col="t_name" )
    
        #roi = ctab_df.loc[:,"gene_name"] == sys.argv[1]
        fpkms.append( ctab_df.loc[sys.argv[1],"FPKM"] )
    return fpkms 

def timecourse_rep(gender):
    
    df = pd.read_csv(replicate_file)
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]
    
    fpkms = []
    # loops over the samples and gets the data
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab"  )
        ctab_df = pd.read_table( filename, index_col="t_name" )
    
        #roi = ctab_df.loc[:,"gene_name"] == sys.argv[1]
        fpkms.append( ctab_df.loc[sys.argv[1],"FPKM"] )
    return fpkms 
    
    
    

fig, ax = plt.subplots()
fpkm_f = timecourse('female')
fpkm_m = timecourse('male')

reps_m = timecourse_rep('male')
reps_f = timecourse_rep('female')


ax.plot( fpkm_f )
ax.plot( fpkm_m )



fig, ax = plt.subplots()
ax.plot( fpkm_f )
ax.plot( fpkm_m )
ax.plot(fpkm_f, label='female', color='red')
ax.plot(fpkm_m, label='male', color='blue')

ax.plot([4,5,6,7], reps_f, label="Replicate Female", color="orange")
ax.plot([4,5,6,7], reps_m, label="Replicate Male", color="green")

plt.xlabel('developmental stage')
plt.ylabel('mRNA abundance (FPKM)')
plt.title('FBtr0331261', style = 'italic', fontsize='30')
my_xticks = ["9", "10", "11", "12", "13", "14A", "14B", "14C", "14D"]
ax.set_xticklabels(labels = my_xticks)
plt.xticks(rotation=90)
plt.legend(bbox_to_anchor=(1.06, 0.5), loc=2, borderaxespad=0.)
plt.close(fig)
fig.savefig( "timecourse.png", bbox_inches='tight' )