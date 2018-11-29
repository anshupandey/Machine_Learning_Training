# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:45:11 2018

@author: Anshu Pandey
"""

# pip install opencv-python
# scikit-image (skimage) = pip install scikit-image
import cv2
img=cv2.imread(r"C:\Python35\images\dhonikohli1.jpg")
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import matplotlib.pyplot as plt

plt.imshow(img)
plt.show()


img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2.shape
cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


img3=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img3)
plt.show()

import time
vid=cv2.VideoCapture(r"F:\MLIoT\ML\dataset\people-walking.mp4")
while True:
    ret,img=vid.read()
    cv2.imshow("img",img)
    time.sleep(0.3)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()




