import csv

import pandas as pd
from joblib import dump
from nltk.cluster import GAAClusterer
from nltk.cluster import KMeansClusterer
from nltk.cluster import cosine_distance
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.cluster import OPTICS
from sklearn.cluster import SpectralClustering

data = pd.read_csv('../data/documents_advanced_vectors.csv', delimiter=',', index_col=0)
vectors = data[[str(i) for i in range(1024)]].to_numpy()

cluster_number = 15
epochs = 30

#sklearn means
model = KMeans(n_clusters=cluster_number, max_iter=epochs, n_jobs=8)
model.fit(vectors)
dump(model, '../data/advanced_sklearn_kmeans.joblib')

data['cluster'] = pd.DataFrame(model.labels_)
data[['text', 'cluster']].to_csv('../data/text_clustered_sklearn_kmeans.csv', index=True, quoting=csv.QUOTE_ALL)

