# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:03:03 2022

@author: DISRCT
"""


import pandas as pd

data_frame = pd.read_csv('pessoas1.csv',usecols=['id','nome','telefone','idade'])

print(data_frame)

print('\n'*9)
print(data_frame.loc[data_frame['id'] <= 8])
