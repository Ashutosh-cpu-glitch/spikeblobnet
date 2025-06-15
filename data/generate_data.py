# data/generate_data.py

import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Settings
centers = [[-5, 2], [-2, -2], [1, 2], [5, -2]]
std = 1.0
n_samples = 2000
random_state = 30

# Generate blob data
X, y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=std, random_state=random_state)

# Save data
np.savez('data/blob_data.npz', X=X, y=y)

# Optional: plot the data
plt.scatter(X[:,0], X[:,1], c=y, cmap='viridis', alpha=0.6)
plt.title("Generated Blob Data (4 classes)")
plt.savefig("outputs/blob_data.png")
plt.show()
