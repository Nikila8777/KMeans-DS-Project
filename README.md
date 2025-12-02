\# KMeans-DS-Project



A complete project demonstrating:

\- K-Means clustering from scratch (NumPy)

\- Elbow method

\- Silhouette method

\- Mall customer clustering example

\- Image compression using K-Means (RGB clustering)



📁 Project Structure

```



KMeans-DS-Project/

│-- data/

│-- data/images/

│-- src/

│   ├─ kmeans.py

│   ├─ clustering\_analysis.py

│   ├─ image\_compression.py

│   └─ utils.py

│-- notebooks/

│-- README.md

│-- requirements.txt

│-- .gitignore



```



🚀 How to Set Up

```



python -m venv env

env\\Scripts\\activate

pip install -r requirements.txt



````



▶️ Run Mall Customer Analysis



```python

from src.clustering\_analysis import run\_example\_mall

run\_example\_mall("data/mall\_customers.csv")

````



▶️ Run Image Compression



```python

from src.image\_compression import compress\_image, save\_compressed



orig, comp, centroids = compress\_image("data/images/bird.png", K=8)

save\_compressed(comp, "compressed\_8.png")

```



📓 Use Notebook



Open Jupyter:



```

jupyter lab

```



Open the notebook inside `notebooks/`.



```







