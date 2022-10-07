# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:02:40 2019

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("C:\\Users\\disrct\\Documents\\company_sales_data.csv", sep=",",encoding= "latin_1")
print(df)
explode=[0,0,0,0,0.05,0]
fc=sum(df["facecream"])
fw=sum(df["facewash"])
tp=sum(df["toothpaste"])
sh=sum(df["shampoo"])
bs=sum(df["bathingsoap"])
mt=sum(df["moisturizer"])
plt.subplots(figsize=(5,5))
prod=[fc,fw,tp,sh,bs,mt]
label=["Facecream", "Facewash", "Toothpaste", "Shampoo", "Bathingsoap", "Moisturizer"]
plt.pie(prod,labels=label,autopct='%1.1f%%', wedgeprops={"edgecolor":"white"}, shadow=True,explode=explode )



plt.show
