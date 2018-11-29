# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:26:27 2018

@author: Anshu Pandey
"""

import cv2
import time

vid=cv2.VideoCapture(r"C:\Python35\images\FC1.mp4")
fd=cv2.CascadeClassifier(r"C:\Python35\images\haarcascade_frontalface_alt.xml")
while True:
    ret,img=vid.read()
    time.sleep(0.05)
    faces=fd.detectMultiScale(img,scaleFactor=1.3,minNeighbors=4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),[0,0,255],2)
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()


