# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:57:17 2022

@author: Leonardo Falango
"""


import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('company_sales_data.csv')

# facecream facewash toothpaste bathingsouap shampoo moisturize
meses = df['month_number']

plt.plot(meses,df['facecream'], label='Face cream Salas Data', c='blue',marker='o')

plt.plot(meses,df['facewash'], label='Face wash Salas Data', c='orange',marker='o')

plt.plot(meses,df['toothpaste'], label='ToothPaste Salas Data', c='green',marker='o')

plt.plot(meses,df['bathingsoap'], label='BathingSoap Salas Data', c='r',marker='o')

plt.plot(meses,df['shampoo'], label='Shampoo Salas Data', c=[0.5, 0, 0.5, 1],marker='o')

plt.plot(meses,df['moisturizer'], label='Moisturizer Salas Data', c=[0.4, 0.2, 0.2],marker='o')

plt.legend()


plt.title('Sales data')
plt.ylabel('Sales units in number')
plt.xlabel('Month number')
plt.yticks([1000,2000,4000,6000,8000,10000,12000,15000,18000])
plt.axis([0,13,1000,18000])
plt.xticks(df['month_number'])

