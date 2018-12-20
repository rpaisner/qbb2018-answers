#!/usr/bin/env python3

import matplotlib
matplotlib.use("Agg")

import scanpy.api as sc
sc.settings.autoshow = False

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

#
# X_pca = sc.tl.pca(adata)
# sc.pl.pca(adata, save="pca_unfiltered")

sc.pp.recipe_zheng17(adata)

# X_pca = sc.tl.pca(adata)
# sc.pl.pca(adata, save="pca_filtered")




sc.pp.neighbors(adata)
sc.tl.louvain(adata, copy=False)
sc.tl.tsne(adata)
# sc.pl.tsne(adata, color= "louvain", save="tsne_clusters")
# sc.tl.umap(adata)
# sc.pl.umap(adata, color= "louvain", save="umap_clusters")


# sc.tl.rank_genes_groups(adata, groupby= 'louvain', method="logreg")
# sc.pl.rank_genes_groups(adata, save="logreg_ranked")
# sc.tl.rank_genes_groups(adata, groupby= 'louvain', method="t-test")
# sc.pl.rank_genes_groups(adata, save='ttest_ranked')

sc.pl.tsne(adata, color= ["louvain", "Stmn1"], save="2plot_clusters_Stmn1")
sc.pl.tsne(adata, color= ["louvain", "Cldn5"], save="2plot_clusters_Cldn5")
sc.pl.tsne(adata, color= ["louvain", "Rgs5"], save="2plot_clusters_Rgs5")
sc.pl.tsne(adata, color= ["louvain", "Tyrobp"], save="2plot_clusters_Tyrobp")
    
    
