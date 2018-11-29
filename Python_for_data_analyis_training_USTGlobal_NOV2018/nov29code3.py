# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:58:15 2018

@author: Anshu Pandey
"""

data="""Bengaluru (also called Bangalore) is the capital of India's southern 
Karnataka state. The center of India's high-tech industry, 
the city is also known for its parks and nightlife. By Cubbon Park, 
Vidhana Soudha is a Neo-Dravidian legislative building. Former royal 
residences include 19th-century Bangalore Palace, modeled after 
England’s Windsor Castle, and Tipu Sultan’s Summer Palace, 
an 18th-century teak structure. Mr. John is gonna go to 
Bangalore on 13th of this month. Drop him an email on
 john@noemail.com. THank you! Do you have any question?"""


print(data)
data.split('.')

import nltk
nltk.download()

nltk.sent_tokenize(data)
nltk.word_tokenize(data)


#Modphological ANalysis - Converting a word into its root
#                       format.
#1. stemming - faster, slightly inaccurate
#2. Lemmatization - slower , more accurate

from nltk.stem import PorterStemmer

ps=PorterStemmer()
ps.stem('happily')

ps.stem("cats")
ps.stem('boxes')
ps.stem('wives')

from nltk.stem import SnowballStemmer
ss=SnowballStemmer('english')
ss.stem("wives")

from nltk.stem import LancasterStemmer
ls=LancasterStemmer()
ls.stem("wives")

# Lemmatization
from nltk.stem import WordNetLemmatizer
wd=WordNetLemmatizer()
wd.lemmatize('wives')

wd.lemmatize('children')
wd.lemmatize('went','v')

from nltk import pos_tag
pos_tag(["Ram","Delhi",'is',"am",'goining'])






