# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:37:07 2019

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("C:\\Users\\disrct\\Documents\\company_sales_data.csv", sep=",",encoding= "latin_1")
print(df)

dd=(df["total_profit"].values)
plt.xlabel(dd)
plt.line( dd, color="lightblue") 
plt.ylabel
plt.show()