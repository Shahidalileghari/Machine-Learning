import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

X, _ = make_blobs(n_samples=450, centers=4, cluster_std=1.3, random_state=15)
scaled = StandardScaler().fit_transform(X)
clusterer = KMeans(n_clusters=4, n_init=10, random_state=15)
labels = clusterer.fit_predict(scaled)
reduced = PCA(n_components=2).fit_transform(scaled)

plt.scatter(reduced[:, 0], reduced[:, 1], c=labels, s=20)
plt.xlabel("Principal component 1")
plt.ylabel("Principal component 2")
plt.title("K-means groups viewed in a 2D PCA projection")
plt.tight_layout()
plt.show()
print("These are synthetic clusters; labels are algorithmic groupings, not ground truth.")
