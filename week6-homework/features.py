#!/usr/bin/env python3

"""
Usage:
./depth_reads.py <vcf> <output.png>
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

with open(sys.argv[1]) as f:
    with open("features_exon.bed", "w") as f1:
        for line in f:
            if "exon" in line:
                f1.write(line)
            else:
                continue

with open(sys.argv[1]) as f:
    with open("features_intron.bed", "w") as f1:
        for line in f:
            if "intron" in line:
                f1.write(line)
            else:
                continue
                
with open(sys.argv[1]) as f:
    with open("features_promoter.bed", "w") as f1:
        for line in f:
            if "promoter" in line:
                f1.write(line)
            else:
                continue