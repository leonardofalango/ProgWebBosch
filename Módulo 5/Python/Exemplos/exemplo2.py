# -*- coding: utf-8 -*-
"""
Created on Mon May  2 08:40:09 2022

@author: Leonardo Falango
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



#Criando a DataBase
dados = {"Area" : [40,45,50,53,60,65,100,110,113,130],
         "Valor" : [120,180,190,187,195,200,300,320,305,400]}
df = pd.DataFrame(dados)

#Separando as variáveis
independente = df["Area"].values
dependente = df["Valor"].values

#Trasnpondo os valores
independente = independente.reshape(-1, 1)

#Criando o regressor
regressor = LinearRegression() #Iniciando o Regressor
regressor = regressor.fit(independente, dependente) #Treinando o rehgressor com vários dados


#Plottando o gráfico
plt.scatter(independente, dependente)
plt.plot(independente, regressor.predict(independente), color='r')
plt.show()


#Verificando se há outliers
#Gerando um grádico de boxplot
df.boxplot(column=['Area', 'Valor'], grid=False)
plt.show()

#Usando o Regressor para prever novos valores
area = np.array(35)
area = area.reshape(-1, 1)
previsao = regressor.predict(area)
print("O valor previsto é:", previsao)
