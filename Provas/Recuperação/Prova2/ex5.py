# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:48:50 2022

@author: Leonardo Falango
"""

import pandas as pd
import seaborn as sns

df = pd.read_csv("Dados/flights.csv")

sns.barplot(x='year',y='passengers',data=df)
