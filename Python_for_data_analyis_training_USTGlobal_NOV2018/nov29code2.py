# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:50:53 2018

@author: Anshu Pandey
"""

# pip install pyaudio
# pip install SpeechRecognition

import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone(1) as source:
    audio=r.listen(source,phrase_time_limit=10)

text=r.recognize_google(audio)
print(text)

