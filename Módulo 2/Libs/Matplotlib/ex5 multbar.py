# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:29:07 2022

@author: DISRCT
"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('company_sales_data.csv')

meses = df['month_number']


plt.bar(meses-0.2, df['facecream'], color=[0,0.5,0.8],label='Face Cream sales data', width=0.4)
plt.bar(meses+0.2, df['facewash'], color=[0.8,0.8,0], label='Face Wash sales data', width=0.4)


plt.grid(True, linestyle='--')
plt.xticks(meses)
plt.title('bathingsoap sales data')
plt.xlabel('Sales units in number')
plt.ylabel('Month number')
plt.legend(loc='upper left')
