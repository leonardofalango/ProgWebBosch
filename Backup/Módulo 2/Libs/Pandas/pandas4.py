# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:29:16 2022

@author: DISRCT
"""


import pandas as pd

dataframe = pd.read_csv('pessoas1.csv',usecols=['id','nome','telefone','idade'])

print(dataframe)

dataframe.sort_values(by='nome')
print(dataframe)
