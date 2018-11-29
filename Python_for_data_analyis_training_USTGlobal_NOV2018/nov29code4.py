# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:30:08 2018

@author: Anshu Pandey
"""

from textblob import TextBlob
data=TextBlob("Hello Everyone, Hope you like python programming.")

# Machine Translation
data.translate(to='hi')
data.translate(to='te')
data.translate(to='ta')
data.translate(to='ar')
data.translate(to='fr')
data.translate(to='gu')

# sentiment analysis
data=TextBlob("RACE 3 is an amazing movie.")
data.sentiment.polarity

data=TextBlob("RACE 3 is a good movie.")
data.sentiment.polarity

data=TextBlob("RACE 3 is a bad movie.")
data.sentiment.polarity

data=TextBlob("RACE 3 is an worst movie.")
data.sentiment.polarity

data=TextBlob("RACE 3 is an awesome movie.")
data.sentiment.polarity

data=TextBlob("the training is good and i loved it.")
data.sentiment.polarity

data=TextBlob("I hate such trainings")
data.sentiment.polarity

#############
#sentence spelling corrrection
data=TextBlob("I havv lost my watch")
data.correct()


from textblob import Word
w=Word('car')
w.definitions
