# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:16:17 2018

@author: Anshu Pandey
"""

x=int(input('Enter the first number '))
y=int(input('Enter the second number '))
z=x+y
print(z)
print('the addition is ',z)
print('the addition is '+str(z))
print('the addition is %d'%z)
print('the addtion of %d and %d is %d '%(x,y,z))



name=input('enter your name ')
age=int(input('enter your age '))
print('Hi %s your age is %d '%(name,age))
if age<18:
    print('you are underage')
    print('you can not vote')
    print('play games, read books and enjoy childhood')
elif age>18 and age<30:
    print('you are young now')
    print('this is the time to get into Data Science')
    print('Work hard and learn hard and enjoy')
else:
    print('you are adult now')
    print('this is the time to do something big ')
    print('Read books and learn and learn')
    print('Use stairs otherwise you will get tummy out')


#for loop in python

for i in range(10):
    print('Hello from python')
    
for i in range(12):
    print(i)
    
for i in range(3,12):
    print(i)
    
for i in range(3,12,2):
    print(i)
    
for i in range(12,1,-1):
    print(i)

x=10
for i in range(x):
    print('python is awesome')
    
temp=[24,26,25,26,24,25,26,24,24,25,26,26,25,24,25,27,28,27]
temp1=[]

for i in temp:
    if i>26:
        print(i)
        temp1.append(i)
print(temp1)

#list comprehension
temp2=[i for i in temp if i>26]
temp2

#while loop in python
x=5
while x<15:
    print('python is amazing')
    x=x+1
    
x=5
while True:
    print('I love python')
    x=x+1
    if x>15:
        break


x=2
while True:
    x=x+1
    if x%2==0:
        continue
    print(x)
    if x>12:
        break
    
    
for i in range(1,6):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
    

    
    
    
    


