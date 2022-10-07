# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:51:18 2019

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("C:\\Users\\disrct\\Documents\\company_sales_data.csv", sep=",",encoding= "latin_1")
print(df)

fc=df["facecream"].values
fw=df["facewash"].values
width=0.25
index=np.arange(1,13,1)

plt.xlabel('Month number')
plt.ylabel("Series units in number")
plt.xticks(index)

plt.bar(index, fc, width=wid, color="lightblue") 
plt.bar(index-width, fw, width=width, color="lightgreen") 



plt.show()
