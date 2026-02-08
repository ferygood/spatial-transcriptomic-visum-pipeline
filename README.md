# spatial-transcriptomic-visum-pipeline
A multimodal pipeline for integrating spatial transcriptomics using Scanpy

## Project Overview
This project use 10X Visuim spatial transcriptomic data, combing AI image feature extraction and gene statistical analysis, to analyze adulat mouse brain (V1 Adult Mouse Brain) Multimodal analysis.

## Technical Pipeline
### 1. QC & Feature Selection
I first filter low quality spots by filting 2000 high variable genes (HVGs)

![image]("results/qc_metrics.png")