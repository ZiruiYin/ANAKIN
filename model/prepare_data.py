import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def read_ratings(minage, maxage):
    cols = ['uid', 'mid', 'rating', 'age']
    df = pd.read_csv('../db/rating.csv', names = cols, header = None)
    df.columns = cols
    filtered_df = df[(df['age'] >= minage) & (df['age'] <= maxage)]
    return filtered_df

def read_users():
    df = pd.read_csv('../db/user.csv', header = None)
    cols = ['uid', 'name', 'age']
    df.columns = cols
    return df

def prepare(minage, maxage):
    ratings = read_ratings(minage, maxage)
    prepared_df = pd.crosstab(index=ratings['uid'], columns=ratings['mid'], values=ratings['rating'], aggfunc='last')
    #print("PREPARED RAW")
    #print(prepared_df.head())
    scaler = StandardScaler()
    scaler.fit(prepared_df)
    scaled_df = pd.DataFrame(scaler.transform(prepared_df), columns=prepared_df.columns)
    return scaled_df.fillna(0)

def prepare_normal_false(minage, maxage):
    ratings = read_ratings(minage, maxage)
    #print("RATINGS RAW")
    #print(ratings.head(20))
    prepared_df = pd.crosstab(index=ratings['uid'], columns=ratings['mid'], values=ratings['rating'], aggfunc='last')
    return prepared_df.apply(lambda row: row.fillna(row.mean()), axis=1)