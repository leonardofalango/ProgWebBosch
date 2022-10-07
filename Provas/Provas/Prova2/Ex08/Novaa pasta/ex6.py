# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:52:10 2019

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("C:\\Users\\disrct\\Documents\\company_sales_data.csv", sep=",",encoding= "latin_1")
print(df)

fb=df["bathingsoap"].values

plt.xlabel('Mounth Number')

index=np.arange(1,13,1)
plt.bar(index, fb, width=0.5, color="pink") 
plt.grid(color="lightblue")
plt.show