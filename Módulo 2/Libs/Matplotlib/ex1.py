# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:21:56 2022

@author: DISRCT
"""

#month_number,facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer,total_units,total_profit

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('company_sales_data.csv',usecols=['month_number','total_profit'])



plt.plot(df['month_number'],df['total_profit'], linestyle='-')
plt.xlabel('Número do mês')
plt.ylabel('Lucro Total')
plt.axis([0,13,0,500000])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.grid(True, linewidth='0.5', linestyle=':')
plt.title('Company profit per month')