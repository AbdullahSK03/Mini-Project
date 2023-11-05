#!/usr/bin/env python
# coding: utf-8

# # Importing dependencies

# In[1]:


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# # Read CSV

# In[2]:


artist = pd.read_csv('artists.csv')
artist.head()


# In[3]:


artist.isna().sum()


# In[4]:


songs = pd.read_csv('tracks.csv')
songs.head()


# #### Cleaning data by removing null values

# In[5]:


songs.isna().sum()


# In[6]:


artist.dropna(inplace=True)
artist.isna().sum()


# In[7]:


songs.dropna(inplace=True)
songs.isna().sum()


# ##### Dropping unnecessary columns

# In[8]:


columns_to_drop = ['release_date', 'danceability', 'energy', 'key', 'loudness', 'mode', 
                   'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
                   'valence', 'tempo', 'time_signature']

songs = songs.drop(columns=columns_to_drop)

songs.head()


# In[9]:


artist.shape


# In[10]:


songs.shape


# Combining the data

# In[11]:


df = pd.merge(artist, songs, left_on='id_artists', right_on='id_artists', how='inner')
df.tail()


# ## Data Preprocessing

# #### creating new feature combining title and artist name

# In[12]:


df['song'] = df['name_x']+' - '+df['name_y']
# df['song'] = df['name_y'] + '(' + df['genres'] + ')'
df.head()


# In[13]:


df.sample(250000, replace=True).to_csv('newdataset.csv')


# Taking random 30,000 samples

# In[14]:


df = pd.read_csv('newdataset.csv')


# Dropping duplicates

# In[15]:


df.drop_duplicates(inplace=True)


# In[16]:


df = df.head(30000)


# In[17]:


song_grouped = df.groupby(['song']).agg({'genres':'first'}).reset_index()
song_grouped.head()


# ## Creating recommendation engin

# Create a CountVectorizer and fit it to the combined features

# In[18]:


vectorizer = CountVectorizer().fit(df['song'])


# Transform the combined features into a matrix of token counts

# In[19]:


count_matrix = vectorizer.transform(df['song'])


# Compute the cosine similarity matrix from the count matrix

# In[20]:


cosine_sim = cosine_similarity(count_matrix)


# In[21]:


df[df['song'] == 'Eminem - Lose Yourself']


# In[22]:


cosine_sim[0]


# In[23]:


def recommend_songs(title):
    if title not in df['song'].values:
        return 'Song not found in the dataset'
    idx = df[df['song'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    song_indices = [i[0] for i in sim_scores[1:21]]
    return df['song'].iloc[song_indices]


# # Printing Recommendation

# In[28]:


recommend_songs(title='Eminem - Music Box')


# In[29]:


# import pickle
# pickle.dump(cosine_sim,open('similarity.pkl','wb'))
# pickle.dump(df,open('df.pkl','wb'))

