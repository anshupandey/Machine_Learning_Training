# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:01:07 2018

@author: Anshu Pandey
"""

#Functions in python 

x=[4,5,2,6,8.2]
min(x)
max(x)
sum(x)

def myfun():
    print('hii from python')
    print('hope you like python')
    

def myfun2(a,b):
    "this function will add two values with 2, try it"
    c=a+b
    return c

def myfun3(a,b=6):
    "this function will add two values with 2, try it"
    c=a+b
    myfun()
    return c


def myfun4(a,*b):
    c=a
    for i in b:
        c=c+i
    return c




def myfun5(a):
    if a>6:
        return a+10
    else:
        myfun5(a+1)

        

y=lambda x:x+5

