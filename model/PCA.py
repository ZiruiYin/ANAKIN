import pandas as pd
from sklearn.decomposition import PCA
from prepare_data import prepare

def get_data(minage, maxage):
    return prepare(minage, maxage)

pca = PCA(n_components=2)

def get_pca(df):
    pca_df = pca.fit_transform(df)
    pca_df = pd.DataFrame(data=pca_df, columns=['PC1', 'PC2'])
    return pca_df