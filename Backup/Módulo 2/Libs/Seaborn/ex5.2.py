# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 08:55:26 2022

@author: Leonardo Falango
"""

import pandas as pd
import seaborn as sns

df = pd.read_csv('firearm.csv', sep=',')

sns.lineplot(data=df , x='month', y='permit', style='state', hue='state')