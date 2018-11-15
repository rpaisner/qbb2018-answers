#!/usr/bin/env python3


from scipy.cluster.hierarchy import dendrogram, linkage
from scipy import stats
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns



""" make heatmap """

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)
# df_array = np.array(df)
# data.columns = ["CFU", "poly", "unk", "int", "mys", ""]
# print(df["CFU"])
# print(df.iloc[[0]])

""" starts here """

cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)

ax = sns.clustermap(df, metric='euclidean', cmap=cmap)
# plt.show()
ax.savefig("heatmap.png")
# plt.close(ax)

""" make kmeans plot"""

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)

plt.figure()
plt.title("k-means")
plt.scatter(df["CFU"], df['poly'], c=y_kmeans, s=5, cmap='viridis')
# plt.scatter(df["CFU"], df['poly'], c = kmeans[1])
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("test_kmeans.png")
plt.close()


""" last question is find the genes in the same cluster as 23100 Ribo transporter"""
print(len(y_kmeans))
""" 2310046K01Rik is 9th gene, so cluster 2 """
print(kmeans.fit(df))
ribo_cluster = y_kmeans[2]
similar_genes = df.index[y_kmeans == ribo_cluster]
print(similar_genes)
print(similar_genes.tolist())

file = open('similargenes_incluster.txt','w')
for line in similar_genes.tolist():
    print(line)
    file.write(line)
    file.write('\n')
file.close()







""" determining differentially expressed genes CFU, mys and poly, unc"""
d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df2 = pd.DataFrame(data=d)

df3 = df2.filter(['CFU','mys','poly', 'unk'], axis=1)
# print(df3)

df3['avg_early'] = df3[['CFU', 'mys']].mean(axis=1)
# print(df2['avg_early'])

df3['avg_late'] = df3[['poly', 'unk']].mean(axis=1)

# print(df2['avg_late'])


df3['fold_change'] = df3['avg_late']/df3['avg_early']

df3.loc[df3['fold_change'] < .5, 'Downregulated'] = df3['fold_change']
df3.loc[df3['fold_change'] > 2, 'Upregulated'] = df3['fold_change']

p_value = []
for index, row in df3.iterrows():
   CFU = row['CFU']
   mys = row['mys']
   early = [CFU, mys]
   poly = row['poly']
   unk = row['unk']
   late = [poly, unk]
   t_test, p_val = stats.ttest_ind( early, late)
   if p_val < .05:
       p_value.append(p_val)
   else:
       p_value.append(int(-1))
df3['p_value'] = p_value

Down_sig = []
for index, row in df3.iterrows():
    Downregulated = row['Downregulated']
    p_value = row['p_value']
    if Downregulated and p_value > 0:
            Down_sig.append(Downregulated)
    else:
        Down_sig.append(int(-1))
df3['Down_sig'] = Down_sig

Up_sig = []
for index, row in df3.iterrows():
    Upregulated = row['Upregulated']
    p_value = row['p_value']
    if Upregulated and p_value > 0:
            Up_sig.append(Upregulated)
    else:
        Up_sig.append(int(-1))
df3['Up_sig'] = Up_sig



df4 = df3.filter(['Down_sig','Up_sig','p_value'], axis=1)


df4_sorted = (df4.sort_values(['Down_sig', 'Up_sig'], ascending=True))
df4_sorted1 = (df4.sort_values(['Up_sig'], ascending=False))

""" for significant 2 fold upregulated genes, I made a text file"""

file = open('Up_sig_list.txt','w') 
for index, row in df4_sorted1.iterrows():
    Up_sig = row['Up_sig']
    p_value = row['p_value']
    if Up_sig > int(0):
        print(index, "\t", Up_sig, "\t", p_value)
        file.write(index)
        file.write("\t")
        file.write(str(Up_sig))
        file.write("\t")
        file.write(str(p_value))
        file.write("\n")
    else:
        continue
file.close()
""" for significant 2 fold downregulated genes, I made a text file """

file = open('Down_sig_list.txt','w') 
for index, row in df4_sorted.iterrows():
    Down_sig = row['Down_sig']
    p_value = row['p_value']
    if Down_sig > int(0):
        print(index, "\t", Down_sig, "\t", p_value)
        file.write(index)
        file.write("\t")
        file.write(str(Down_sig))
        file.write("\t")
        file.write(str(p_value))
        file.write("\n")
    else:
        continue
file.close()

