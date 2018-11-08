# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:20:17 2018

@author: Anshu Pandey
"""

import numpy

x=[4,5,6]
y=[7,2,9]
x+y

x=numpy.array([7,4,2,6])
y=numpy.array([2,3,9,8])
type(x)
x.size
x+y
x*y
x-y
x/y

x=numpy.array([[7,4,2,6],[1,2,5,8],[3,6,9,4]])
x.dtype #data type of the elements
x.size #total number of elements in the numpy array
x.shape #the shape of the numpy array
x.max() #maximum value from the array
x.min() #minimum value from the array
x.mean() #mean of all values in the array

x.max(axis=1) #row wise operation
x.min(axis=1)
x.mean(axis=1)
x.max(axis=0)#column wise operation

x.reshape(6,2)
x.reshape(4,3)
x.reshape(-1,6)

#creating numpy arrays
a=numpy.arange(15)
a=numpy.arange(3,15)
a=numpy.arange(3,15,2)
a

b=numpy.linspace(10,15,9)
b=numpy.logspace(1,5,5,dtype='int32')
b=numpy.zeros((4,3))

c=numpy.ones(6)
c=numpy.ones((4,3))
c

#Random values as arrays using numpy
numpy.random.rand(5)
numpy.random.randn(6)

numpy.random.seed(9)
numpy.random.randint(40,60,5)


#merging stacking pf arrays
a=numpy.array([4,8,7,5,6]).reshape(1,5)
b=numpy.array([9,8,5,1,2]).reshape(1,5)

c=numpy.concatenate([a,b],axis=1)
c.shape

numpy.hstack((a,b))
numpy.vstack((a,b))

#indexing and slicing of arrays
x=numpy.array([[7,8,6,4,1],[3,2,4,8,2],[7,5,4,1,2],[9,7,4,5,2]])
x.shape
x[:,-1]
x[:,3:7]
x[-1,:]
x[2:4,:]

#mathematics and statiscs with numpy
numpy.mean(x)
numpy.median(x)
numpy.var(x)
numpy.std(x)
numpy.min(x)
numpy.max(x)
numpy.sin(90)
numpy.cos(50)
numpy.exp(x)

#linear algebra with numpy
#3x+y=11
#5x-8y=-1

a=[[3,1],[5,-8]]
b=[[11],[-1]]
numpy.linalg.solve(a,b)


m=numpy.matrix([[7,5,2],[3,6,9],[8,4,1]])
m.shape
type(m)
numpy.linalg.inv(m)
numpy.linalg.det(m)
numpy.linalg.matrix_rank(m)
numpy.linalg.eig(m)




