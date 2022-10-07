# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:24:28 2022

@author: DISRCT
"""

import pandas as pd

df = pd.read_csv('Exercício7.csv', encoding=('utf-8'))

print(df)
print('\n\n\n')
df2 = df[df['Data da venda'] >= 2020]
print(df2)
df2.to_csv('Exercício7Data2020.csv', index=False)