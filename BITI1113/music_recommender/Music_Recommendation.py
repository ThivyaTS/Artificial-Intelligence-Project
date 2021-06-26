#!/usr/bin/env python
# coding: utf-8

# ## Import modules

# In[45]:


import pandas as pd
import numpy as np
import PopularityBased_Recommenders as Recommenders
import contentBased_recommender as contentBased_recommender


# In[46]:


import matplotlib.pyplot as plt


# In[47]:


from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ## Loading the dataset

# # ....................................................................

# In[48]:


# First Dataset
#  - This dataset contains , user_id, song_id and listen_count
song_dataset1 = pd.read_csv('triplets_file.csv')
song_dataset1.head()


# In[49]:


# Second Dataset
#  - This dataset contains , song_id, title, release,artist_name and year of release
song_dataset2 = pd.read_csv('song_data.csv')
song_dataset2.head()


# In[50]:


# Combining both the datasets (First dataset + Second dataset)
song_datasetMaster = pd.merge(song_dataset1, song_dataset2.drop_duplicates(['song_id']), on='song_id', how='left')
song_datasetMaster.head()


# In[51]:


# Displaying the length of first dataset(song1) & second dataset(song2)
print(len(song_dataset1), len(song_dataset2))


# In[52]:


# Displaying the length of the combined dataset
len(song_datasetMaster)


# ## Data Preprocessing

# In[53]:


# creating new feature combining title and artist name
song_datasetMaster['song'] = song_datasetMaster['title']+' - '+song_datasetMaster['artist_name']
song_datasetMaster.head()


# In[54]:


# taking top 10k samples for quick results
song_datasetMaster = song_datasetMaster.head(10000)


# In[55]:


# cummulative sum of listen count of the songs
song_grouped = song_datasetMaster.groupby(['song']).agg({'listen_count':'count'}).reset_index()
song_grouped.head()


# In[56]:


grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage'] = (song_grouped['listen_count'] / grouped_sum ) * 100
song_grouped.sort_values(['listen_count', 'song'], ascending=[0,1])


# In[88]:


#exploring dataset
get_ipython().run_line_magic('matplotlib', 'inline')


# In[96]:


song_datasetMaster = song_datasetMaster.sample(frac=0.1, random_state = 1)


# In[97]:


song_datasetMaster.hist(figsize = (20, 20))
plt.show()


# In[98]:


song_grouped = song_grouped.sample(frac=0.1, random_state = 1)


# In[99]:


song_grouped.hist(figsize = (20, 20))
plt.show()


# ## Popularity Recommendation Engine

# In[62]:


pr = Recommenders.popularity_recommender_py()


# In[63]:


pr.create(song_datasetMaster, 'user_id', 'song')


# In[64]:


# display the top 10 popular songs
pr.recommend(song_datasetMaster['user_id'][5])


# In[65]:


pr.recommend(song_datasetMaster['user_id'][100])


# # Content-Based Recommendation Engine

# In[66]:


#taking a sample of 5000 songs
song_ = song_datasetMaster.sample(n=5000).reset_index(drop=True)


# In[67]:


#We use TF-IDF vectorizer that calculates the TF-IDF score for each song title, word-by-word. 
#Here, we pay particular attention to the arguments we specify.
tfidf = TfidfVectorizer(analyzer='word', stop_words='english')


# In[68]:


title_matrix = tfidf.fit_transform(song_['title'])


# In[69]:


#How do we use this matrix for a recommendation?
#We now need to calculate the similarity of one title to another. We are going to use cosine similarity.
#We want to calculate the cosine similarity of each item with every other item in the dataset. So we just pass the title_matrix as argument.


# In[70]:


#Cosine similarity - passing the title_matrix as argument.
cosine_similarities = cosine_similarity(title_matrix)


# In[71]:


#Once we get the similarities, we store in a dictionary with the names of the 50 most similar songs for each song in the dataset.
similarities = {}


# In[72]:


for i in range(len(cosine_similarities)):
    # Now we'll sort each element in cosine_similarities and get the indexes of the songs. 
    similar_indices = cosine_similarities[i].argsort()[:-50:-1] 
    # After that, we'll store in similarities each name of the 50 most similar songs.
    # Except the first one that is the same song.
    similarities[song_['song'].iloc[i]] = [(cosine_similarities[i][x], song_['song'][x], song_['year'][x]) for x in similar_indices][1:]


# In[73]:


#We can use that similarity scores to access the most similar items and give a recommendation.
#For that, we'll define our Content based recommender class. We already done that in the contentBased_recommender module.


# In[74]:


#Now,we instantiate class
cbr_recommedations = contentBased_recommender.ContentBasedRecommender(similarities)


# In[75]:


#Then, we are ready to pick a song from the dataset and make a recommendation.
recommendation = {
    "song": song_['song'].iloc[20],
    "number_songs": 4
}


# In[76]:


cbr_recommedations.recommend(recommendation)


# In[77]:


#And we can pick another random song and recommend again and lets recommend 7 songs this time:
recommendation = {
    "song": song_['song'].iloc[10],
    "number_songs": 7
}


# In[78]:


cbr_recommedations.recommend(recommendation)


# In[ ]:




