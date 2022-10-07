# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:16:19 2022

@author: Leonardo Falango
"""

import pandas as pd
import matplotlib.pyplot as plt

# 3) flights.csv plote um grafico mostrando a quantidade de passageiros por ano em março


df = pd.read_csv("Dados/flights.csv")

df_march = df[df['month'] == 'May']
df_march = df_march['passengers']

x = df['year'].unique()


plt.ylabel("Passageiros")
plt.xlabel("Ano")
plt.title("Passageiros de avião", fontsize=32)
plt.xticks(x)
plt.grid()
plt.plot(x,df_march, marker = 'o', color='g', markerfacecolor='black', markeredgecolor='black')

