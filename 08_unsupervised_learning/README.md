# 08 — Unsupervised Learning

## Clustering
Clustering groups examples by a similarity notion. K-means assigns examples to k centroids and iteratively updates assignments and centroids. It works best when its distance-based assumptions are reasonably suitable.

## Dimensionality reduction
Principal Component Analysis (PCA) finds orthogonal directions that capture variance in numeric data. PCA can help explore correlated features or create compact representations, but it is not a guarantee of better predictive performance.

## Practical cautions
- Scaling often matters for distance-based methods.
- A cluster is a mathematical grouping, not automatically a real-world category.
- Choose the number of clusters using multiple forms of evidence, domain context, and stability—not one plot alone.
