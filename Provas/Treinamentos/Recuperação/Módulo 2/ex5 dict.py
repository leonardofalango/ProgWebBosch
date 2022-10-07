# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:39:32 2022

@author: DISRCT
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/dados.csv', encoding = 'latin-1')

bairros = pd.unique(df['bairro'])

quant = []

dic = {}

for i in bairros:
    tam = len(df[df['bairro'] == i])
    quant.append(tam)
    dic[tam] = i

print(dic)
lista = list(dic)
lista = sorted(lista, reverse = True)
dicio = {}
for i in lista:
    dicio[i] = dic[i]


plt.plot(list(dicio.values()), list(dicio.keys()), linewidth=3, marker='o')
plt.show()
