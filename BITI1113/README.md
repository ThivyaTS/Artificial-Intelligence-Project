# Music Recommendation System

## A. PROJECT SUMMARY

**Project Title:** Music Recommendation System

In this project, we will show you how a music recommendation system works. Music recommender system is one of the most used machine learning algorithms in recommendation systems. A recommender (or recommendation) system (or engine) is a filtering system which aim to predict a rating or preference a user would give to an item, eg. a film title, a product, a song, etc.

There are two main types of recommender systems we have used in our project: 

**1) Content-based recommender**

**2)Popularity based recommender**

**Content-based recommender**

This type of receommender system is user-specific classification problem. This classifier learns the user's likes and dislikes from the features of the song.

The most straightforward approach is **keyword matching**.

In a few words, the idea behind is to extract meaningful keywords present in a song description a user likes, search for the keywords in other song descriptions to estimate similarities among them, and based on that, recommend those songs to the user.

How is this performed?

In our project, since we are working with text and words, Term Frequency-Inverse Document Frequency (TF-IDF) can be used for this matching process.

**Team Members:** 
- Thivya Tamil Selvam
- Anbu Selvi A/P M Paramasivan
- Noah Brynner
- Redwan


- [ ] **Objectives:**
- Break out the project goal into more specific objectives
- [insert]
- [insert]
- [insert]


##  B. ABSTRACT 

In late December 2019, a previous unidentified coronavirus, currently named as the 2019 novel coronavirus, emerged from Wuhan, China, and resulted in a formidable outbreak in many cities in China and expanded globally, including Thailand, Republic of Korea, Japan, United States, Philippines, Viet Nam, and our country (as of 2/6/2020 at least 25 countries). Covid-19 are Person-to-person transmission may occur through droplet or contact transmission and if there is a lack of stringent infection control or if no proper personal protective equipment available, it may jeopardize the first-line healthcare workers.

The best safety measure that can be taken is enforcing the people to wear a face mask whenever they are outside to slow down the COVID-19 infection rate. Mask wearing significantly reduced the amounts of various airborne viruses coming from infected patients, measured using the breath-capturing "Gesundheit II machine" developed by Dr. Don Milton, a professor of applied environmental health and a senior author of the study published April 3 in the journal Nature Medicine. In short, masks can help prevent the spread of COVID-19 and that the more people wearing masks, the better.

As for now, you as a Data Scientist or Machine Learning Engineer or Practitioner are going to use AI technology to recognize people whether they are wearing face mask or not in the public or open space.


![Coding]()
Figure 1 shows the AI output of detecting which user is not wearing a face mask or inappropriate face mask.


## C.  DATASET

The datasets for this project are contained within two cvs files.
The song_data.csv file holds all songs that used for the project. It includes the name, artist, genre and publish date of the song.

The triplets_file.csv holds user data that relates to the songs. The included data that is in the file is the userid, songid and the number of times the user has listened to the song named as 'listen'.


## D   Result of training

After training the program, it now can recommend songs based on popularity and content. However, there is a great difference of succession between the two methods.

![image](https://user-images.githubusercontent.com/86180936/123402779-b0291000-d5da-11eb-8051-c83d73513220.png)

It is apparent that the method of recommending based on content have fluctuating results. It seems that the model is unable to correctly choose the right songs based on the content of a target song. Assumably, a subjective input such as the content of a song cannot be easily categorize by the model and thus the impercise output.

In contrary to content based recommendation, the model can easily recommend songs to the user based on popularity of the song.

![image](https://user-images.githubusercontent.com/86180936/123404891-e4510080-d5db-11eb-99d6-f68acd814962.png)

![image](https://user-images.githubusercontent.com/86180936/123404933-ee72ff00-d5db-11eb-9e8d-dd6a84d3b222.png)

As shown above, the model is able to consistently recommend any user the most popular song. This is thanks to popularity being a more objective input for the model to evaluate easily. 

From this comparison, more training will be required for recommending songs by content more than than by popularity.

## F.  RESULT AND CONCLUSION

Detecting COVID-19 face masks with OpenCV in real-time

You can then launch the mask detector in real-time video streams using the following command:
- $ python detect_mask_video.py
- [INFO] loading face detector model...
- INFO] loading face mask detector model...
- [INFO] starting video stream...

[![Figure5](https://i9.ytimg.com/vi/jIUN4k0gE-Q/mq1.jpg?sqp=CKCh54MG&rs=AOn4CLBi6Ge6x7CWNenhJ7pK-LKRnwJvMA)](https://youtu.be/jIUN4k0gE-Q)

Figure 5: Mask detector in real-time video streams

In Figure 5, you can see that our face mask detector is capable of running in real-time (and is correct in its predictions as well.



## G.   PROJECT PRESENTATION 

In this project, you learned how to create a COVID-19 face mask detector using OpenCV, Keras/TensorFlow, and Deep Learning.

To create our face mask detector, we trained a two-class model of people wearing masks and people not wearing masks.

We fine-tuned MobileNetV2 on our mask/no mask dataset and obtained a classifier that is ~99% accurate.

We then took this face mask classifier and applied it to both images and real-time video streams by:

- Detecting faces in images/video
- Extracting each individual face
- Applying our face mask classifier

Our face mask detector is accurate, and since we used the MobileNetV2 architecture, it’s also computationally efficient, making it easier to deploy the model to embedded systems (Raspberry Pi, Google Coral, Jetosn, Nano, etc.).

[![demo](https://i9.ytimg.com/vi/pA9An19rEVQ/mq3.jpg?sqp=CKCh54MG&rs=AOn4CLAHhKrP9UG9l5h2Y2gJpaV4DDSZUw)](https://youtu.be/pA9An19rEVQ)

