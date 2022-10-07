# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:22:36 2022

@author: DISRCT
"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('company_sales_data.csv')

meses = df['month_number']


plt.axis([0,13,0,15000])
plt.bar(meses,df['bathingsoap'], color=[0,0.5,0.8])
plt.grid(True, linestyle='--')
plt.xticks(meses)
plt.title('bathingsoap sales data')
plt.xlabel('Sales units in number')
plt.ylabel('Month number')


