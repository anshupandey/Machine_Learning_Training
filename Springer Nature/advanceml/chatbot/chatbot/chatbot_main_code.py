# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 00:24:19 2020

@author: anshu
"""

#Loading intent Recognizer

from tensorflow.keras import models

model = models.load_model("intent_recognizer.h5")

# loading tokenizer
import pickle
with open('tokenizer.pickle', 'rb') as handle:
    tok = pickle.load(handle)


#######################################################################
## Loading answers

import json
import numpy as np
answers = open(r"data\ans_data.txt","r").read()
answers = answers.replace("'", "\"")
answers = json.loads(answers)
intents = list(answers.keys())

config = json.loads(open(r"chatbot_config.txt",'r').read().replace("'", "\""))

#######################################################################
### chatbot flow
MAX_SEQUENCE_LENGTH = config['max_seq_len']
from tensorflow.keras.preprocessing.sequence import pad_sequences

while True:
    qus = input("You: ")
    if qus=='exit':
        print("Thank you for your time, Have a good day!")
        break
    seq = tok.texts_to_sequences([qus])
    seq = pad_sequences(seq,maxlen=MAX_SEQUENCE_LENGTH)
    ans = model.predict_classes(seq)[0]
    print(ans)
    current_intent = intents[ans]
    print("recognized Intent is ",current_intent)
    ans = np.random.choice(answers[current_intent])
    print("Bot: ",ans)
    
    
    
    
    
    
