# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:15:58 2022

@author: Leonadro Falango
"""

#subplots

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

fig, eixo = plt.subplots(nrows=2, ncols=1, figsize=(12,12), sharex= True)


eixo[0].plot(df['month_number'], df['bathingsoap'], marker='o', c='black', linewidth=4, markersize=10)
eixo[0].set_title('Sales data of a Bathingsoap')


eixo[1].plot(df['month_number'], df['facewash'], marker='o', c='r', linewidth=4, markersize=10)
eixo[1].set_title('Sales data of a facewash')

plt.ylabel('Sales units in number')
plt.xticks(df['month_number'])




