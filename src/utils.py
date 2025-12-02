import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_rgb_scatter(X, centroids=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:,0], X[:,1], X[:,2], s=1)
    if centroids is not None:
        ax.scatter(centroids[:,0], centroids[:,1], centroids[:,2], c='red', s=80, marker='x')
    ax.set_xlabel("Red")
    ax.set_ylabel("Green")
    ax.set_zlabel("Blue")
    plt.show()
