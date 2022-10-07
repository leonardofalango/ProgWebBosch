# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:37:33 2022

@author: DISRCT
"""

import seaborn as sns
import pandas as pd
df = pd.read_csv('seaborn.csv', sep=';')
sns.regplot(x='total_bill', y='tip', data=df)
sns.lmplot(x='total_bill', y='tip',data=df)