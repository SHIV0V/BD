import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = [[1, 2], [1, 4], [2, 3], [10, 2], [10, 4], [11, 3]]

model = KMeans(n_clusters=2, n_init=10)
model.fit(X)

print("Labels:", model.labels_)
print("Centers:", model.cluster_centers_)

plt.scatter([p[0] for p in X], [p[1] for p in X], c=model.labels_)
plt.show()