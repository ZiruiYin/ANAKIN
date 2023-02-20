from clustering import clustering
from prepare_data import prepare_normal_false
from prepare_data import read_users
from prepare_data import read_ratings
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommend(uid, n=5):
    age = read_users().loc[uid, 'age']
    minage = age - 10
    maxage = age + 10
    cluster_df = clustering(minage, maxage)
    cluster_value = cluster_df.loc[uid, 'Cluster']
    df = prepare_normal_false(minage, maxage)
    #filtered_df = df[cluster_df['Cluster'] == cluster_value]
    #print("DF_NO_NORMAL/////////////////////////////////")
    #print(df.head())
    joined = pd.merge(df, cluster_df, left_index = True, right_index = True, how = 'inner')
    filtered_df = joined[joined['Cluster'] == cluster_value]
    target_user_ratings = filtered_df.drop(columns = 'Cluster') #get a clean copy of ratings, not normalized
    #print(target_user_ratings.head())
    #print(type(target_user_ratings))
    #print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    user_sim_matrix = cosine_similarity(filtered_df)
    user_sim_df = pd.DataFrame(user_sim_matrix, index=filtered_df.index, columns=filtered_df.index)
    #target_user_id = uid
    #ratings_df = read_ratings(minage, maxage)
    #target_user_ratings = ratings_df[ratings_df['uid'] == target_user_id]
    #print(target_user_ratings.head())
    #print(">>>>>>>>>>>>>>>>>>>>>>>>")
    target_user_similarities = user_sim_df[uid] #get a pandas series of user similarities
    norm_s = target_user_similarities / target_user_similarities.sum()
    weighted = target_user_ratings.mul(norm_s, axis=0)
    movie_weighted_ratings = weighted.sum()
    #print(type(weighted))
    #print(target_user_similarities)
    #movie_weighted_ratings = target_user_ratings.groupby('mid').apply(
    #    lambda x: (x['rating'] * target_user_similarities[x['uid']]).sum() / target_user_similarities[x['uid']].sum()
    #)
    #print(movie_weighted_ratings)
    top_movies = movie_weighted_ratings.sort_values(ascending=False).head(n)
    return top_movies