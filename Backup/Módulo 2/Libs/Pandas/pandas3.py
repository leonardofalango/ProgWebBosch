# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:31:50 2022

@author: DISRCT
"""

import pandas as pd

dataframe = pd.read_csv('pessoas1.csv',usecols=['id','nome','telefone','idade'])

comum = dataframe['idade'].value_counts()


