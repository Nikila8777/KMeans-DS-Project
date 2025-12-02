import numpy as np

def KMeans_init_centroids(X, K, seed=None):
    if seed is not None:
        np.random.seed(seed)
    m = X.shape[0]
    idx = np.random.choice(m, K, replace=False)
    return X[idx]

def find_closest_centroids(X, centroids):
    dists = np.linalg.norm(X[:, None, :] - centroids[None, :, :], axis=2)
    return np.argmin(dists, axis=1)

def compute_centroids(X, idx, K):
    n = X.shape[1]
    centroids = np.zeros((K, n))
    for k in range(K):
        points = X[idx == k]
        if len(points) > 0:
            centroids[k] = points.mean(axis=0)
    return centroids

def run_KMeans(X, initial_centroids, max_iters=20, tol=1e-6):
    centroids = initial_centroids.copy()
    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        new_centroids = compute_centroids(X, idx, centroids.shape[0])
        shift = np.linalg.norm(new_centroids - centroids)
        centroids = new_centroids
        if shift < tol:
            break
    idx = find_closest_centroids(X, centroids)
    return centroids, idx
