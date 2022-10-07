# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:13:49 2022

@author: DISRCT
"""

import pandas as pd

df = pd.read_csv('pessoas1.csv',usecols=['id','nome','telefone','idade'])

quant_pessoas = df['id'].count()

print(df[df['id'] >= (quant_pessoas/2)])
