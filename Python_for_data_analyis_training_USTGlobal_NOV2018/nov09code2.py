# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:26:30 2018

@author: Anshu Pandey
"""

import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns


x=numpy.arange(10,20,0.5)
y=numpy.sin(x)
z=numpy.exp(0.08*x)

plt.figure(figsize=(8,4))
plt.plot(x,y,'r',label='sin(x)')
plt.plot(x,z,'g',label='exp(0.08*x)')
plt.xlabel('value of x')
plt.ylabel('value of y and z')
plt.title('Graph of x v/s sin(x) and exp(x)')
plt.legend()
plt.grid(True)
plt.show()


#scatter plot
plt.scatter(x,y)
plt.show()


#pie chart
data=[78,45,65,35]
lb=['BLR','DEL','GOI','HYD']
ex=[0,0.25,0,0]
plt.figure(figsize=(6,6))
plt.pie(data,labels=lb,explode=ex)
plt.title('THe Pie Chart')
plt.show()



temp=[25,24,25,26,25,24,26,23,25,24,27,22,24,25,26,26]

plt.hist(temp,bins=50)
plt.show()


#subplot - plotting with multiple axes
plt.subplot(211)
plt.plot(x,y,'r')
plt.plot(x,z,'g')
plt.title('x v/s y and z')
plt.subplot(212)

plt.hist(temp)
plt.show()


