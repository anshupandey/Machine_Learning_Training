# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:39:25 2018

@author: Anshu Pandey
"""

import cv2
import time
#vid=cv2.VideoCapture(r"F:\MLIoT\ML\dataset\people-walking.mp4")
vid=cv2.VideoCapture(0)
bs=cv2.createBackgroundSubtractorMOG2()

while True:
    ret,img=vid.read()
    time.sleep(0.2)
    back=bs.apply(img)
    cv2.imshow('img',back)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()

