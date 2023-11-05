# %% [markdown]
# # Importing dependencies

# %%
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# %% [markdown]
# # Read CSV

# %%
artist = pd.read_csv('receiptify-flask-main/artists.csv')
artist.head()

# %%
artist.isna().sum()

# %%
songs = pd.read_csv('receiptify-flask-main/tracks.csv')
songs.head()

# %% [markdown]
# #### Cleaning data by removing null values

# %%
songs.isna().sum()

# %%
artist.dropna(inplace=True)
artist.isna().sum()

# %%
songs.dropna(inplace=True)
songs.isna().sum()

# %% [markdown]
# ##### Dropping unnecessary columns

# %%
columns_to_drop = ['release_date', 'danceability', 'energy', 'key', 'loudness', 'mode', 
                   'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
                   'valence', 'tempo', 'time_signature']

songs = songs.drop(columns=columns_to_drop)

songs.head()

# %%
artist.shape


# %%
songs.shape

# %% [markdown]
# Combining the data

# %%
df = pd.merge(artist, songs, left_on='id_artists', right_on='id_artists', how='inner')
df.tail()

# %% [markdown]
# ## Data Preprocessing

# %% [markdown]
# #### creating new feature combining title and artist name

# %%
df['song'] = df['name_x']+' - '+df['name_y']
# df['song'] = df['name_y'] + '(' + df['genres'] + ')'
df.head()

# %%
df.sample(250000, replace=True).to_csv('newdataset.csv')

# %% [markdown]
# Taking random 30,000 samples

# %%
df = pd.read_csv('newdataset.csv')

# %% [markdown]
# Dropping duplicates

# %%
df.drop_duplicates(inplace=True)

# %%
df = df.head(30000)

# %%
song_grouped = df.groupby(['song']).agg({'genres':'first'}).reset_index()
song_grouped.head()

# %% [markdown]
# ## Creating recommendation engin

# %% [markdown]
# Create a CountVectorizer and fit it to the combined features

# %%
vectorizer = CountVectorizer().fit(df['song'])

# %% [markdown]
# Transform the combined features into a matrix of token counts

# %%
count_matrix = vectorizer.transform(df['song'])

# %% [markdown]
# Compute the cosine similarity matrix from the count matrix

# %%
cosine_sim = cosine_similarity(count_matrix)

# %%
df[df['song'] == 'Eminem - Lose Yourself']

# %%
cosine_sim[0]

# %%
def recommend_songs(title):
    if title not in df['song'].values:
        return 'Song not found in the dataset'
    idx = df[df['song'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    song_indices = [i[0] for i in sim_scores[1:21]]
    return df['song'].iloc[song_indices]


# %% [markdown]
# # Printing Recommendation

# %%
recommend_songs(title='Eminem - Music Box')

# %%
import pickle
pickle.dump(cosine_sim,open('similarity.pkl','wb'))
pickle.dump(df,open('df.pkl','wb'))


