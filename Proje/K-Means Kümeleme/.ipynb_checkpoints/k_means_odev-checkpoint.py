import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


data = pd.read_csv('dava.csv')
data


X = data[["Case Duration (Days)", "Number of Witnesses", 
        "Legal Fees (USD)", "Number of Evidence Items", "Severity"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia = []
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10, max_iter=300)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(7,4))
plt.plot(K, inertia, 'o-')
plt.xlabel("Küme Sayısı (k)")
plt.ylabel("Inertia")
plt.title("Elbow Yöntemi")
plt.grid(True)
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10, max_iter=300)
data["Cluster"] = kmeans.fit_predict(X_scaled)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(7,5))
plt.scatter(X_pca[:,0], X_pca[:,1], c=data["Cluster"], cmap="viridis", alpha=0.7)
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.title("K-Means Kümeleme Sonucu (PCA ile 2D)")
plt.colorbar(label="Cluster")
plt.show()

print("Küme Merkezleri (orijinal ölçekte):")
centers = scaler.inverse_transform(kmeans.cluster_centers_)
print(pd.DataFrame(centers, columns=X.columns))