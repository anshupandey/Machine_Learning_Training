# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:12:20 2018

@author: Anshu Pandey
"""

'''
pandas has 3 data types
1. Series - 1D
2. Dataframe - 2D
3. Panel - 3D
Dataframe is the most popular,
Pandas Dataframe is rich with a number of methods
related to Data Analysis and very much user friendly
'''


import numpy
import pandas

data=numpy.random.randint(40,80,(20,3))
cols=['server1','server2','server3']
rows=pandas.date_range('20181025',periods=20)
df=pandas.DataFrame(data,index=rows,columns=cols)

# to fetch the data of server 1
df['server1']
df.iloc[:,0]

df['2018-10-29':'2018-11-05']
df['2018-10-29':'2018-11-05']['server2']


df[df['server2']>70]
df['server2'][df['server2']>70]

df[['server2','server3']][df['server2']>70]

#AND Condition
df[(df['server2']>60) & (df['server3']>60)]
df[df['server2']>60][df['server3']>60]

#OR operations
df[(df['server2']>70) | (df['server3']>70)]

df.to_excel('serverdata.xlsx')
df2=df[(df['server2']>70) | (df['server3']>70)]
df2.to_excel('heavyload_server23.xlsx')

#statistical analysis with pandas

#to get the stat summary
df.describe()

df['server1'].min()
df['server1'].max()
df['server1'].mean()
df['server1'].median()
df['server1'].mode()
df['server1'].var()
df['server1'].std()
df['server1'].skew()
df['server1'].kurt()

df.corr()
df.cov()

df.min()

df[['server2','server3']].min()







