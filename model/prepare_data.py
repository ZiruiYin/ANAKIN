import pandas as pd
import numpy as np

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

def prepare(minage, maxage):
    ratings = read_ratings(minage, maxage)
    prepared_df = pd.crosstab(index=ratings['uid'], columns=ratings['mid'], values=ratings['rating'], aggfunc='last')
    normalized_df = prepared_df.apply(normalize, axis=1)
    return normalized_df.round(2)

def normalize(row):
    mean = np.mean(row)
    normalized = [(value - mean) / mean if not np.isnan(value) else 0 for value in row]
    return pd.Series(normalized)