# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:27:29 2018

@author: Anshu Pandey
"""

#Object Oriented Programming

class A:
    x=5
    __y=12
    def fun1(self):
        print('i am a function of class A')
        print('i can do anything')
        print(self.x+self.__y)
        print(self.x)
    
    def fun2(self,a,b):
        self.c=a+b
        return self.c
    
      
class B(A):
    def fun3(self):
        self.d=self.x
        print(A.x)
        print('i am afunction of class B')
        print('welcome to the python programming community')
    x=2
    z=6

