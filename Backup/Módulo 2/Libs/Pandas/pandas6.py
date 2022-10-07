# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:39:57 2022

@author: DISRCT
"""


import pandas as pd


nomes = []
anos = []

while True:
    titulo = input('Entre com o título de lançamento: ')
    if titulo == '':
        break
    ano = int(input('Entre com o ano de lançamento: '))
    if ano == '':
        break
    nomes.append(titulo)
    anos.append(ano)
    
csv = {'Música' : nomes, 'Ano' : anos}
df = pd.DataFrame(csv)
df.to_csv('TesteCSVPython.csv', index=False)

soma = df['Ano'].sum()
quant = df['Ano'].count()
media = soma/quant

print(df[df['Ano']>media])
