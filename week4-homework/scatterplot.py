#!/usr/bin/env python

""" 
Usage: ./scatterplot.py <eigenvec>
"""
import sys
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], sep=" ", header=None)


fig, ax = plt.subplots()
ax.scatter(df.iloc[:, 2], df.iloc[:, 3])
ax.set_title("Genetic Relatedness Between Strains")
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
fig.savefig("pca_scatterplot.png")
plt.close(fig)

