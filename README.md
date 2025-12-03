\# 📌 \*\*K-Means Clustering \& Image Compression\*\*



\*A complete Data Science project built from scratch using NumPy, Matplotlib, and Scikit-Learn.\*



---



\## 🚀 \*\*Project Overview\*\*



This project demonstrates:



\* \*\*K-Means clustering from scratch (NumPy implementation)\*\*

\* \*\*Elbow Method\*\* to identify the optimal number of clusters

\* \*\*Silhouette Score\*\* to validate clustering quality

\* \*\*Customer segmentation\*\* using the Mall Customers dataset

\* \*\*Image compression\*\* using K-Means on RGB pixel values

\* \*\*Interactive Jupyter Notebook\*\* for analysis and visualization



---



\## 📁 \*\*Project Structure\*\*



```

KMeans-DS-Project/

│

├── data/

│   ├── Mall\_Customers.csv

│   └── images/

│       └── pic.jpg

│

├── src/

│   ├── kmeans.py                 # K-Means from scratch

│   ├── clustering\_analysis.py    # Elbow + Silhouette + plotting

│   ├── image\_compression.py      # RGB K-Means compression

│   └── utils.py

│

├── notebooks/

│   └── KMeans\_Project.ipynb      # Complete project walkthrough

│

├── requirements.txt

├── .gitignore

└── README.md

```



---



\## 📊 \*\*K-Means Analysis (Graphs)\*\*



Generated inside:



```

notebooks/KMeans\_Project.ipynb

```



\### \*\*1️⃣ Elbow Method\*\*



Used to choose the optimal number of clusters \*\*K\*\*

(Shows the point where inertia decreases slowly → "elbow point")



!\[Elbow Method Plot](data/images/Elbow\_Method.png)



\### \*\*2️⃣ Silhouette Score Plot\*\*



Measures how well each point fits inside its cluster.

Highest average score → optimal K.



!\[Silhouette Score Plot](data/images/silhouette\_plot.png)



\## 🧠 \*\*How K-Means Works (Simple Explanation)\*\*



1\. Choose the number of clusters \*\*K\*\*

2\. Randomly initialize K centroids

3\. Assign each point to the nearest centroid

4\. Update centroids as the mean of assigned points

5\. Repeat until convergence



---



\## 🔍 \*\*Mall Customer Segmentation\*\*



Using:



\* Annual Income

\* Spending Score



You can visualize:



\* Elbow Method

\* Silhouette Method

\* Customer clusters



Run:



```python

run\_example\_mall("../data/Mall\_Customers.csv")

```



---



\## 🖼 \*\*Image Compression using K-Means\*\*



Even though graphs only are in README,

your notebook demonstrates:



\* Original image

\* Compressed image with K clusters

\* Reduction of colors

\* Visualization of compression quality



Run:



```python

compress\_image("../data/images/pic.jpg", K=8)

```



---



\## 🧪 \*\*Run the Project Locally\*\*



\### \*\*1. Create and activate environment\*\*



```bash

python -m venv env

env\\Scripts\\activate

pip install -r requirements.txt

```



\### \*\*2. Run the notebook\*\*



```bash

jupyter lab

```



Open:



```

notebooks/KMeans\_Project.ipynb

```



\### \*\*3. Run scripts manually\*\*



```bash

python -m src.image\_compression

python -m src.clustering\_analysis

```



