#!/usr/bin/env python

"""
Usage: ./histogramplotwee8.py ER4_fimo.bed
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab

ER4_fimo = open(sys.argv[1])

percentage = []

for line in ER4_fimo:
    fields = line.rstrip("\r\n").split("\t")
    Sm = fields[3]
    Em = fields[4]
    Sp = fields[10]
    Ep = fields[11]
    percentage.append(100*(abs(float(Sm)-float(Sp))/abs(float(Ep)-float(Sp))))
# print(percentage)

""" line of best fit"""





fig, ax = plt.subplots()

plt.hist(percentage, bins=200)




ax.set_xlabel("Motif Position")
ax.set_ylabel("Frequency")
fig.suptitle("Motif Position Proportional to Peak Sequence")
fig.savefig("Week8.png")
plt.tight_layout()
plt.close(fig)
       