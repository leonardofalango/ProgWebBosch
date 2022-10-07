# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:36:22 2022

@author: DISRCT
"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('company_sales_data.csv',usecols=['month_number','total_profit'])


# print(df['month_number'])



plt.plot(df['month_number'],df['total_profit'], linestyle='--', color='red',marker='o',markerfacecolor='black')
# plt.plot(df['month_number'],df['total_profit'], linestyle='',color='black', marker='o')


plt.xlabel('Número do mês')
plt.ylabel('Lucro Total')
plt.axis([0,13,10000,500000])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([10000,200000,300000,400000,500000])
plt.grid(True, linewidth='0.5', linestyle=':')
plt.title('Company profit per month')
