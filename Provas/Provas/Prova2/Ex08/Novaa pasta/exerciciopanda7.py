# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 08:05:51 2019

@author: DISRCT
"""
import pandas as pd
df=pd.read_csv("Cars93_miss.csv", sep=",",encoding="latin_1")
x=df.loc[df['Price'].idxmin()]
y=(df.loc[x.name:x.name,['Manufacturer','Type','Model']])
print(y)
