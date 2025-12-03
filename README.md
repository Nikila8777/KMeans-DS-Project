```markdown

\# 📌 \*\*K-Means Clustering \& Image Compression\*\*



A complete Data Science project built from scratch using NumPy, Matplotlib, and Scikit-Learn.



---



\## 🚀 \*\*Project Overview\*\*



This project demonstrates:



\- \*\*K-Means clustering from scratch (NumPy implementation)\*\*

\- \*\*Elbow Method\*\* to find the optimal number of clusters

\- \*\*Silhouette Score\*\* to measure cluster quality

\- \*\*Customer Segmentation\*\* using Mall Customers dataset

\- \*\*Image Compression\*\* using RGB K-Means clustering

\- \*\*Interactive Jupyter Notebook\*\* for analysis and visualization



---



\## 📁 \*\*Project Structure\*\*



```



KMeans-DS-Project/

│

├── data/

│   ├── Mall\_Customers.csv

│   └── images/

│       ├── Elbow\_Method.png

│       ├── Silhouette\_Method.png

│       ├── pic.jpg

│       ├── pic\_compressed\_8.png

│       └── pic\_compressed\_8\_from\_notebook.png

│

├── src/

│   ├── kmeans.py                 # K-Means from scratch

│   ├── clustering\_analysis.py    # Elbow + Silhouette + plotting

│   ├── image\_compression.py      # RGB image compression

│   └── utils.py

│

├── notebooks/

│   └── KMeans\_Project.ipynb

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



---



\### \*\*1️⃣ Elbow Method\*\*



Used to choose the optimal number of clusters \*\*K\*\*  

(Shows the point where inertia decreases slowly → “elbow point”)



```



data/images/Elbow\_Method.png



```



---



\### \*\*2️⃣ Silhouette Score Plot\*\*



Measures how well each point fits inside its cluster.  

Highest average score → optimal K.



```



data/images/Silhouette\_Method.png



```



---



\## 🧠 \*\*How K-Means Works (Simple Explanation)\*\*



1\. Choose the number of clusters \*\*K\*\*

2\. Randomly initialize K centroids

3\. Assign each point to the nearest centroid

4\. Update centroids as the mean of assigned points

5\. Repeat until convergence



---



\## 🖼 \*\*Image Compression using K-Means\*\*



Your images folder contains:



```



pic.jpg

pic\_compressed\_8.png

pic\_compressed\_8\_from\_notebook.png



````



The notebook demonstrates:



\- Loading the original image  

\- Converting it to RGB pixel data  

\- Running K-Means with K=8  

\- Reconstructing the compressed image  

\- Saving output files  



Run:



```python

compress\_image("../data/images/pic.jpg", K=8)

````



---



\## 🧪 \*\*Run the Project Locally\*\*



\### \*\*1. Create \& activate environment\*\*



```bash

python -m venv env

env\\Scripts\\activate

pip install -r requirements.txt

```



\### \*\*2. Launch Jupyter Notebook\*\*



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







