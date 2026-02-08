# spatial-transcriptomic-visum-pipeline
A multimodal pipeline for integrating spatial transcriptomics using Scanpy

## Project Overview
This project use 10X Visuim spatial transcriptomic data, combing AI image feature extraction and gene statistical analysis, to analyze adulat mouse brain (V1 Adult Mouse Brain)[https://squidpy.readthedocs.io/en/stable/api.html#module-squidpy.datasets] Multimodal analysis.

## Technical Pipeline
### 1. QC & Feature Selection
I first filter low quality spots by filting 2000 high variable genes (HVGs)

![image](results/qc_metrics.png)
*Figure: Comparison of QC of total UMIs and MT percentage. Thus this is pre-processed data, the percentage of mitochondria genes is low.*

I filter the cells which have at least **500** genes, and at least 10 cells need to have this gene. Then the data is normalized to achieve high variable genes.

![image](results/highly_variable_genes.png)
*Figure: Left: Comparison of highly variable genes after normalization. Right: Without normalization*

### 2. Spatial Clustering & Annotation
Here I used Leiden algorithm to do unsupervised clustering and visualize result using UMP.

![image](results/spatial_cluster.png)
*Figure: Left: UMAP visualize cluster based on normalized gene expression. Right: Re-mapped the cluster back to the spatial transcriptomic projection*
