from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from PCA import get_pca
from prepare_data import prepare
import pandas as pd

#determine k for k-mean clustering
def find_k(minage, maxage):
    silhouette_scores = []
    df = get_data(minage, maxage)
    df_pca = get_pca(df)
    for k in range(4, 8):
        kmeans = KMeans(n_clusters=k)
        labels = kmeans.fit_predict(df_pca)
        score = silhouette_score(df_pca, labels)
        silhouette_scores.append(score)
    best_k = silhouette_scores.index(max(silhouette_scores)) + 4
    return best_k

def clustering(minage, maxage):
    k = 6 #CHANGE THIS LINE, DEBUGGING ONLY
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10)
    df = prepare(minage, maxage)
    #print("DF//////////////////////////////////////")
    #print(df.head())
    df_pca = get_pca(df)
    #print("PCA//////////////////////////////////////")
    #print(df_pca.head())
    kmeans.fit(df_pca)
    labels = kmeans.predict(df_pca)
    df_labels = pd.DataFrame(labels, columns=['Cluster'])
    #print("LABELS//////////////////////////////////////")
    #print(df_labels.head())
    return df_labels