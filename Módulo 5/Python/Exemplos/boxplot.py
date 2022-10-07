# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:00:55 2022

@author: Leonardo Falango
"""

import pandas as pd

dados = {'Mistura 1' : [22.02, 23.83, 26.67, 25.38, 25.49, 23.50, 25.90, 24.89],
         'Mistura 2' : [21.49, 22.67, 24.62, 24.18, 22.78, 22.56, 24.46, 23.79],
         'Mistura 3' : [20.33, 21.67, 24.67, 22.45, 22.29, 21.95, 20.49, 21.81]}

#Transformando os dados em DataFrame
df = pd.DataFrame(dados)


#Calculos misturas
for i in range(3):
    mist = "Mistura " + str(i + 1)
    print("-="*8, mist, "=-"*8)
    
    print("Média: {:.2f}".format(df[mist].mean()))
    print("Mediana: {:.2f}".format(df[mist].median()))
    print("Desvio padrão: {:.2f}".format(df[mist].std()))

df.boxplot(column= ['Mistura 1', 'Mistura 2', 'Mistura 3'], grid=False)
