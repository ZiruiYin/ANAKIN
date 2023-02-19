import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

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
    scaler = StandardScaler()
    scaler.fit(prepared_df)
    scaled_df = pd.DataFrame(scaler.transform(prepared_df), columns=prepared_df.columns)
    return scaled_df.fillna(0)