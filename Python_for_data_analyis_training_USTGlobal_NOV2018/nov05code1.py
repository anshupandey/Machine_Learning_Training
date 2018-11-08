# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:28:51 2018

@author: Anshu Pandey
"""

# i am a single line comment
'''
i am into a multiline comment
i am also a part of multiline comment
'''

'''
Data Types
Control Flow
Functions
Object Oriented Programming
'''
#python strings
x="Hello WOrld"
print(x)
type(x)
x.upper()
x.lower()
x.capitalize()
dir(x)
help(str) # to check all the methods which can be applied to string

#integer
y=45
type(y)
y.__gt__(62)

#float
z=0.25
type(z)

#boolean
q=True
type(q)

#complex
w=5+1.2j
type(w)
w.conjugate()
w.imag
w.real

###################################
'''
List
Tuple
Dictionary
set
'''
#list
#a collection of elements, which can be of different data type
#defined using [] brackets
x=[4,2.5,45,'hi',12,0.25]
type(x)
len(x)
#indexing of elements
x[0]
x[1]
x[-1]
x[-2]
x[-3]
#slicing of list
x[0:3]
x[2:4]
x[2:6]
x[2:8]
print(x)
#customization of lists
x[0]=12
x.append(56)
x.insert(2,23)
x.remove(0.25)
x.remove(x[2])
x.pop(2)

#Tuples
#collection of elements into () brackets
y=(12,0.25,'python',6,1.3)
type(y)
len(y)
#indexing
y[0]
y[1]
y[-1]
y[-2]
#slicing of tuples
y[0:3]
y[2:4]
#tuples can not be customized
y[0]=23

#Dictionary
z={'name':'Anshu','age':18,'city':'Surat','country':'India'}
type(z)

z['name']
z['age']

z.keys()
z.values()
z['gender']='male'
z['temp']=[224,215,26,24,25,25,55]
z

#set
d={45,2.5,45,'hi',25,1.2,2.5}
type(d)
d
e={1.2,54,39,2.5,'python'}
type(e)
d.union(e)
d.intersection(e)

x=[4,2.5,3]
y=[7,5,1]

x+y
#string
d="hello world"
d[0]
d[2:6]
i="helllo "
j='world'
i+j
i*2

x=1.2
int(x)
str(x)

g=5
float(g)
str(g)

w='12'
w.isdigit()
int(w)
float(w)

q="Hello from Python"
q.split(' ')
list(q)



