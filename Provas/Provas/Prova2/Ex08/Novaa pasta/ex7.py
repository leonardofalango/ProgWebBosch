# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:21:26 2019

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

df= pd.read_csv("C:\\Users\\disrct\\Documents\\company_sales_data.csv", sep=",",encoding= "latin_1")
print(df)
bins = np.arange(150000,375000,25000)
profit=df["total_profit"]





plt.ylabel("Actual Profit range in dollar")
plt.xlabel("Profit range in dollar")
plt.title("Profit data")
plt.legend(loc="upper right")
plt.show()


plt.hist(profit, bins=bins, edgecolor="pink",label="Profit data")
























