# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:21:15 2019

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("C:\\Users\\disrct\\Documents\\company_sales_data.csv", sep=",",encoding= "latin_1")
print(df)

sb=df["bathingsoap"].values
fc=df["facewash"].values
meses=df["month_number"].values

fig, (ax1,ax2)= plt.subplots(2,1, sharex=True, linewidth=2)
ax1.plot(meses, sb,marker="o",markerfacecolor="red")
ax2.plot(meses, fc,marker="o",markerfacecolor="red")
plt.xticks(meses)
ax2.set_xlabel("Monthseses")
ax1.set_ylabel("Sales units")
ax2.set_ylabel("Sales units")
ax2.set_title("Sales data of a facewash")
ax1.set_title("Sales data of a facewash")
plt.show
