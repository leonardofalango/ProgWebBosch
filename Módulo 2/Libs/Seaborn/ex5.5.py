# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:40:15 2022

@author: Leonardo Falango
"""

import pandas as pd
import seaborn as sns

df = pd.read_csv('diamonds.csv', sep=';')

sns.catplot(data=df,x='cut', y='price', kind='box')


sns.catplot(data=df,x='cut', y='price', kind='violin')

