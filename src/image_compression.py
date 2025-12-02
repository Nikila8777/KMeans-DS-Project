import numpy as np
from matplotlib.image import imread, imsave
from src.kmeans import KMeans_init_centroids, run_KMeans

def load_image(image_path):
    img = imread(image_path).astype(float)
    if img.max() > 1.0:
        img = img / 255.0
    return img

def compress_image(image_path, K=8, max_iters=20, seed=0):
    img = load_image(image_path)
    X = img.reshape(-1, 3)
    centroids_init = KMeans_init_centroids(X, K, seed=seed)
    centroids, idx = run_KMeans(X, centroids_init, max_iters=max_iters)
    compressed = centroids[idx].reshape(img.shape)
    return img, compressed, centroids

def save_compressed(compressed, path):
    imsave(path, np.clip(compressed, 0, 1))


# ----------------------------------------------
# Test run (optional): Compress your JPG image
# ----------------------------------------------
if __name__ == "__main__":
    img_path = "data/images/pic.jpg"        # your image file
    output_path = "data/images/pic_compressed_8.jpg"

    orig, comp, centroids = compress_image(img_path, K=8)
    save_compressed(comp, output_path)

    print("Image compression completed successfully!")
    print(f"Saved compressed image as: {output_path}")
