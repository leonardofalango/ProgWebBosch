# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:30:53 2022

@author: DISRCT
"""

import pandas as pd

dataframe = pd.read_csv('pessoas1.csv',usecols=['id','nome','telefone','idade'])

print(dataframe)

soma = dataframe['idade'].sum()
div = dataframe['idade'].count()

print(soma/div)
