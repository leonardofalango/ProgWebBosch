# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:30:29 2022

@author: Leonardo Falango
"""

import seaborn as sns
import pandas as pd

df = pd.read_csv('diamonds.csv', sep=';')



sns.catplot(x='cut', y='price', data=df, kind='swarm')
sns.catplot(x='color', y='price', data=df, kind='swarm')
sns.catplot(x='clarity', y='carat', data=df, kind='swarm')