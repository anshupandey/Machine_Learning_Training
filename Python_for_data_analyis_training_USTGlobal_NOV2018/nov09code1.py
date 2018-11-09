# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:36:57 2018

@author: Anshu Pandey
"""
import pandas
import numpy

df=pandas.read_excel(r"F:\MLIoT\ML\dataset\Online Retail.xlsx")

df.columns

df=df[['Quantity', 'InvoiceDate',
       'UnitPrice', 'CustomerID',]]

#check for missing values
df.isnull().sum()
print(df.shape)
df.dropna(inplace=True)
#df=pandas.notnull(df['CustomerID'])
print(df.shape)

df.describe()

df=df[df['Quantity']>0]
#calculation of Monetary
df['Monetary']=df['Quantity']*df['UnitPrice']

df['Monetary']=df.groupby(by='CustomerID')['Monetary'].transform(lambda x:sum(x))

#calculation of frequency
df['Frequency']=df.groupby(by='CustomerID')['CustomerID'].transform(lambda x:x.size)
#cross check
df['CustomerID'][df['CustomerID']==17850].size
#calculation of Recency
maxdate=df['InvoiceDate'].max()
now=pandas.datetime(2011,12,11)

(now-maxdate).days
df['Recency']=df.groupby(by='CustomerID')['InvoiceDate'].transform(lambda x:(now-x.max()).days)


#take recency, frequency and monetary and customerID separately

df=df[['Recency','Frequency','Monetary','CustomerID']]

df.drop_duplicates(inplace=True)
print(df.shape)


df.describe()

#calculation of R
bins=[df['Recency'].min()-1,numpy.percentile(df['Recency'],25),
      numpy.percentile(df['Recency'],50),numpy.percentile(df['Recency'],75),
      df['Recency'].max()+1]
cat=['Q1','Q2','Q3','Q4']
df['R']=pandas.cut(df['Recency'],bins,labels=cat)


#Calculation of F
cat=['Q4','Q3','Q2','Q1']
bins=[df['Frequency'].min()-1,numpy.percentile(df['Frequency'],25),
      numpy.percentile(df['Frequency'],50),numpy.percentile(df['Frequency'],75),
      df['Frequency'].max()+1]
df['F']=pandas.cut(df['Frequency'],bins,labels=cat)

#calculation of M
bins=[df['Monetary'].min()-1,numpy.percentile(df['Monetary'],25),
      numpy.percentile(df['Monetary'],50),numpy.percentile(df['Monetary'],75),
      df['Monetary'].max()+1]
df['M']=pandas.cut(df['Monetary'],bins,labels=cat)


#Best Customers - 111
CID_best=df['CustomerID'][df['R']=='Q1'][df['F']=='Q1'][df['M']=='Q1']
CID_best.to_csv('Best_Cusotmers.csv')

#Almost Lost - 311
CID_almost_lost=df['CustomerID'][df['R']=='Q3'][df['F']=='Q1'][df['M']=='Q1']
CID_almost_lost.to_csv('Almost_lost_Customers.csv')

#Lost Customers - 411
CID_lost_customers=df['CustomerID'][df['R']=='Q4'][df['F']=='Q1'][df['M']=='Q1']
CID_lost_customers.to_csv('Lost_customers.csv')

#Unimortatnt Customers - 444
CID_less_imp=df['CustomerID'][df['R']=='Q4'][df['F']=='Q4'][df['M']=='Q4']
CID_less_imp.to_csv('Less_important_customers.csv')
