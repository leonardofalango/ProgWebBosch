# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:49:54 2022

@author: DISRCT
"""

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('company_sales_data.csv')
x = 'facecream facewash toothpaste bathingsoap shampoo moisturizer'
lista_produtos = x.split(' ') #preguiça de escrever todos os terecoteco que tem


plt.scatter(df['month_number'],df[lista_produtos[2]], label='Tooth paste Sales data')
plt.xticks(df['month_number'])

plt.title('Tooth paste Sales data')
plt.legend(loc='upper left')

plt.grid(True, linestyle='--')