# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:03:55 2018

@author: Anshu Pandey
"""

import pandas
import numpy

data=pandas.read_csv(r"D:\python\USTGlobal\regiment.csv",index_col=['index'])

data.describe()

data.groupby(by='regiment').mean()

data.groupby(by='regiment')['preTestScore'].mean()

data.groupby(by=['regiment','company']).mean()


data['learning']=data['postTestScore']-data['preTestScore']

data.groupby(by='regiment')['learning'].mean()
data.groupby(by=['regiment','company'])['learning'].mean()


data['comparison']=data.groupby(by='regiment')['learning'].transform(lambda x:x-x.mean())

data['eligiblity']=numpy.where(data['learning']>50,'yes','no')

bins=[0,25,50,75,100]
names=['low','avg','good','great']

data['category']=pandas.cut(data['postTestScore'],bins,labels=names)

df_new=pandas.get_dummies(data['company'])

df=pandas.concat([data,df_new],axis=1)

df['learning'].plot(kind='barh')
