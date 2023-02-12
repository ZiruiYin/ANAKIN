import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import random
from scipy import sparse
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

def read_ratings(minage, maxage):
    cols = ['uid', 'mid', 'rating', 'age']
    df = pd.read_csv('../db/rating.csv', names = cols)
    df.columns = cols
    filtered_df = df[(df['age'] >= minage) & (df['age'] <= maxage)]
    return filtered_df

def read_users():
    df = pd.read_csv('../db/user.csv')
    cols = ['uid', 'name', 'age']
    df.columns = cols
    return df

def prepare(minage, maxage, n=10):
    ratings = read_ratings(minage, maxage)

    user_groups = ratings.groupby('uid')['rating'].count()
    top_users = user_groups.sort_values(ascending=False)[:n]

    movie_groups = ratings.groupby('mid')['rating'].count()
    top_movies = movie_groups.sort_values(ascending=False)[:n]

    top = (
        ratings.
        join(top_users, rsuffix='_r', how='inner', on='uid').
        join(top_movies, rsuffix='_r', how='inner', on='mid'))

    return pd.crosstab(top.uid, top.mid, top.rating, aggfunc=np.sum)

def split(minage, maxage):
    df = read_ratings(minage, maxage)
    split_value = int(len(df) * 0.80)
    train_data = df[:split_value]
    test_data = df[split_value:]
    return train_data, test_data

def get_user_item_sparse_matrix(df):
    sparse_data = sparse.csr_matrix((df.rating, (df.uid, df.mid)))
    return sparse_data

train_data = split(20,50)[0]
plt.figure(figsize = (12, 8))
ax = sns.countplot(x="rating", data=train_data)
plt.title("Count Ratings in train data", fontsize = 20)
plt.xlabel("Ratings", fontsize = 20)
plt.ylabel("Number of Ratings", fontsize = 20)
plt.show()
