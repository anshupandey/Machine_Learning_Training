# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:57:11 2018

@author: Anshu Pandey
"""

#importing data with pandas
import pandas
import numpy

df=pandas.read_csv(r"D:\python\USTGlobal\datawh.csv",index_col=['Dates'])

df=pandas.read_html(r"https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20181108")
df=df[0]
df.to_csv('bitcoin.csv')

df=pandas.read_csv(r"D:\python\USTGlobal\datanh.csv",header=None)

df.columns=['machine1','machine2','machine3','machine4']


df=pandas.read_csv(r"D:\python\USTGlobal\datawh_missing.csv",
                   index_col=['Dates'],na_values=['.','?'])

df.isnull().sum()

df.info()
# to drop the rows where more than 3 values are missing
df.dropna(thresh=2,inplace=True)

df['Temperature'].fillna(df['Temperature'].mean(),inplace=True)
df.fillna(df.median(),inplace=True)

df.shape

df.drop_duplicates(inplace=True)

#############loading data in chunks#############
dfs=[]
path=r"C:\Users\Roboindia\Desktop\Churn_Modelling.csv"
for chunks in pandas.read_csv(path,chunksize=5000):
    dfs.append(chunks)
    

df=pandas.concat(dfs,axis=0)




