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

def prepare(minage, maxage, n=15):
    ratings = read_ratings(minage, maxage)

    return pd.crosstab(index=ratings['uid'], columns=ratings['mid'], values=ratings['rating'], aggfunc='last')