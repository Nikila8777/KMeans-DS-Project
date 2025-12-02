import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from src.kmeans import KMeans_init_centroids, run_KMeans

def load_mall_data(path):
    df = pd.read_csv(path)
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']].values
    return X, df

def elbow_method(X, K_range=range(1,10), max_iters=50, seed=0):
    inertias = []
    for K in K_range:
        centroids = KMeans_init_centroids(X, K, seed=seed)
        c, idx = run_KMeans(X, centroids, max_iters=max_iters)
        dists = np.linalg.norm(X - c[idx], axis=1)**2
        inertias.append(dists.sum())
    return list(K_range), inertias

def silhouette_scores(X, K_range=range(2,10), max_iters=50, seed=0):
    scores = []
    for K in K_range:
        centroids = KMeans_init_centroids(X, K, seed=seed)
        c, idx = run_KMeans(X, centroids, max_iters=max_iters)
        scores.append(silhouette_score(X, idx))
    return list(K_range), scores

def plot_elbow(Ks, inertias):
    plt.plot(Ks, inertias, marker='o')
    plt.xlabel("K")
    plt.ylabel("Inertia")
    plt.title("Elbow Method")
    plt.grid()
    plt.show()

def plot_silhouette(Ks, scores):
    plt.plot(Ks, scores, marker='o')
    plt.xlabel("K")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Method")
    plt.grid()
    plt.show()

def run_example_mall(path_to_csv):
    X, df = load_mall_data(path_to_csv)
    Ks, inertia = elbow_method(X)
    plot_elbow(Ks, inertia)
    Ks2, scores = silhouette_scores(X)
    plot_silhouette(Ks2, scores)
