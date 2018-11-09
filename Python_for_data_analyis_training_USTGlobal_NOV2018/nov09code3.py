# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:52:40 2018

@author: Anshu Pandey
"""

import numpy
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv(r"C:\Users\Roboindia\Desktop\Churn_Modelling.csv")

df.drop(['RowNumber','CustomerId','Surname'],axis=1,inplace=True)


#CreditScore v/s Exited
plt.figure(figsize=(8,4))
sns.distplot(df['CreditScore'][df['Exited']==0])
sns.distplot(df['CreditScore'][df['Exited']==1])
plt.legend(['0','1'])
plt.show()

#Age v/s Exited 
plt.figure(figsize=(8,4))
sns.distplot(df['Age'][df['Exited']==0])
sns.distplot(df['Age'][df['Exited']==1])
plt.legend(['0','1'])
plt.show()

plt.figure(figsize=(8,3))
sns.countplot(df['Geography'])
plt.show()
plt.figure(figsize=(8,3))
sns.countplot(df['Geography'][df['Exited']==1])
plt.show()


plt.figure(figsize=(8,3))
sns.countplot(df['Gender'])
plt.show()
plt.figure(figsize=(8,3))
sns.countplot(df['Gender'][df['Exited']==1])
plt.show()


plt.figure(figsize=(8,3))
sns.countplot(df['HasCrCard'])
plt.show()
plt.figure(figsize=(8,3))
sns.countplot(df['HasCrCard'][df['Exited']==1])
plt.show()

corr=df.corr()
plt.figure(figsize=(8,8))
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()

#age v/s geography v/s Exited
plt.figure(figsize=(8,4))
sns.swarmplot(x='Geography',y='Age',hue='Exited',data=df)
plt.show()


#age v/s gender v/s Exited
plt.figure(figsize=(8,4))
sns.swarmplot(x='Gender',y='Age',hue='Exited',data=df)
plt.show()


plt.figure(figsize=(8,4))
sns.boxplot(x='Gender',y='CreditScore',hue='Exited',data=df)
plt.show()



