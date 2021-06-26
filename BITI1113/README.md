# Music Recommendation System

## A. PROJECT SUMMARY

**Project Title: Music Recommendation System**

**Team Members:**

![Coding](https://github.com/ThivyaTS/Artificial-Intelligence-Project/blob/main/BITI1113/team%20members.PNG)
<p align="center">
Figure 1 : Team Members Of The Project
</p>


Music recommender system is one in all the foremost used machine learning algorithms in recommendation systems. A recommender (or recommendation) system (or engine) could be a filtering system that aim to predict a rating or preference a user would offer to Associate in Nursing item, eg. a movie title, a product, a song, etc.

There are two main types of recommender systems we have used in our project: 

**1)Popularity based recommender**

The popularity-based recommender, as the name implies, works with the current trend. It mostly consists of items that are currently trending. For example, if a product is frequently purchased by new users, it is possible that it will propose that item to the user who has just signed up.

**2) Content-based recommender**

This type of recommender system is user-specific classification downside. This classifier learns the user's likes and dislikes from the options of the song. The most straightforward approach is **keyword matching**. In a few words, the thought behind is to extract purposeful keywords gift in an exceedingly song description a user likes, rummage around for the keywords in different song descriptions to estimate similarities among them, and supported that, recommend those songs to the user.


- [ ] **Objectives:**
- The objective is to provide music recommendation systems that fit listeners profile in terms of content-based and popularity-based  with continuation of past exploration.

##  B. ABSTRACT 

&nbsp; &nbsp; According to Nielsen’s Music 360 2014 study, 93 % of the U.S. population listens to music, defrayal quite twenty five hours every week electronic jamming intent on their favorite tunes. Recommender systems have taken the diversion and e-commerce industries by storm. Amazon, Netflix, and Spotify square measure nice examples.

&nbsp; &nbsp; In this project, we've designed, enforced and analyzed song recommendation systems exploitation varied algorithms. Music recommendation may be a terribly difficult drawback as we've to structure music during a method that we have a tendency to advocate the favourite songs to users that is rarely a precise prediction. it's dynamic and generally influenced by factors apart from users’ or songs’ listening history. We've used Million Song Dataset , a freely-available collection of audio options and data for 1,000,000 contemporary music genre tracks provided by Echo Nest, to seek out the correlations between users and songs and to find out from the previous listening history of users to provide recommendations for songs that users would like to pay attention most. We will discuss the issues we have a tendency to Janus-faced, ways we've enforced, results and analysis. We have achieved best results exploitation neural network cooperative filtering formula.

## C.  DATASET

We’ll review the dataset we use in our music recommendation system.

Million Songs Dataset contains of two files: triplet_file and metadata_file. The triplet_file contains user_id, song_id and listen count and it has over 2000000 data. The song_data file contains song_id, title, release, year and artist_name and it has 1000000 datas. Million Songs Dataset is a mixture of song from various website with the rating that users gave after listening to the song. In this project we work with , combining this two datasets, and we get about 2000000 datasets.

There are 2 types of recommendation system used in this project: popularity & content-based.

I’ll show you how to train our dataset for Popularity based Recommender System model using Popularity filtering algorithm and Content based Recommender System model using Cosine Similarity.

**Popularity filtering - Popularity recommendation model**

We will get a count of user_ids for each unique song as recommendation score,then sort the songs based upon recommendation score. After that we will generate a recommendation rank based upon score and get the top 10 recommendations.


**Cosine Similarity**

We will be using Cosine Similarity to calculate a numeric quantity that denotes the similarity between song titles. Mathematically, it is defined as follows:

cosine(x,y)=x.y⊺||x||.||y|| 

We’ll use this algorithms in Python script to train our music recommendation system and review the results.

The figures below shows the analysis of the dataset. 

![image](https://github.com/ThivyaTS/Artificial-Intelligence-Project/blob/main/BITI1113/tableModel1.jpg)
<p align="center" width="100%">
Table 1 : Table of datasets;
</p>

![image](https://github.com/ThivyaTS/Artificial-Intelligence-Project/blob/main/BITI1113/histModel1.jpg)
<p align="center">
Figure 1 : Histogram of the parameter listen count and percentage of the listen count.
</p>

![image](https://github.com/ThivyaTS/Artificial-Intelligence-Project/blob/main/BITI1113/tableModel2.jpg)
<p align="center">
Table 2 : Table of datasets
</p>

![image](https://github.com/ThivyaTS/Artificial-Intelligence-Project/blob/main/BITI1113/histModel2.jpg)
<p align="center">
Figure 2 : Histogram of the parameter listen count and year of release of the songs.
</p>

## D.   PROJECT STRUCTURE

The following directories are our structure of our project:
- $ two --dirsfirst --filelimit 5
- .
- ├── dataset
- │   ├── song_data.csv [1000001 entries]
- │   └── triplets_file.csv [1048576 entries]
- ├── music_recommender
- │   ├── PopularityBased_Recommenders.py
- │   ├── contentBased_recommender.py
- │   └── Music_Recommendation.py


- 2 directories, 5 files


The dataset directory contains the data described in the “Our music recommendation system dataset” section.

There are two datasets in our system. 
First, song_data.csv. Song_data.csv dataset consist of 1000001 rows and 5 columns
which are song_id, title, release, artist name and year. 

Second, triplets_file.csv dataset contains 1048576 rows and 3 columns
which are user_id, song_id and listen_count. The song_data.csv dataset is holding the main data for the system and
the triplets_file.csv dataset contains the data that have been collected from the user and counting the time for each song being played
according to the counter data that the recommender can predict from it and give the recommendation.


Explanation of the three Python scripts:

- popularityBased_recommender.py: Accepts our input dataset and make the ‎recommendation for the user based on the data popularity that the sysytem
will identify that from the song_data.csv.

- contentBased_recommender.py: Processes the data based on the content which the system can get from the  triplets_file.csv dataset.

- Main.py: Manipulation of the objects and controlling of the system classes.

In the next sections, we will train our music recommender.



## E. RESULT

After training the program, it now can recommend songs based on popularity and content. However, there is a great difference of succession between the two methods.

![image](https://user-images.githubusercontent.com/86180936/123402779-b0291000-d5da-11eb-8051-c83d73513220.png)

It is apparent that the method of recommending based on content have fluctuating results. It seems that the model is unable to correctly choose the right songs based on the content of a target song. Assumably, a subjective input such as the content of a song cannot be easily categorize by the model and thus the impercise output.

In contrary to content based recommendation, the model can easily recommend songs to the user based on popularity of the song.

![image](https://user-images.githubusercontent.com/86180936/123404891-e4510080-d5db-11eb-99d6-f68acd814962.png)

![image](https://user-images.githubusercontent.com/86180936/123404933-ee72ff00-d5db-11eb-9e8d-dd6a84d3b222.png)

As shown above, the model is able to consistently recommend any user the most popular song. This is thanks to popularity being a more objective input for the model to evaluate easily. 

From this comparison, more training will be required for recommending songs by content more than than by popularity.

## F. CONCLUSION

The project was successful in developing a model for music recommendation based on content or popularity. However, there is one major flaw that should be put to light.

The one major flaw for the model is the music recommendation based on content not having a high accuracy score. This is presumed to be caused by the datasets not having suitable data to train the model for content based recommendation. Content being a very subjective category might require more consideration when choosing datasets for model training. In the future, the model should be retrained when more suitable datasets are available to help train the model.

Overall despite the flaw, the model is still able to perform its intended task with not much error. Hopefully it can be used in other systems and contribute towards those systems greatly.
