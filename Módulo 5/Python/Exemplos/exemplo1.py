# -*- coding: utf-8 -*-
"""
Created on Mon May  2 08:40:09 2022

@author: Leonardo Falango
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Criando a DataBase

dados = {"Valor" : [200,  220,  300,  290,  450, 457, 500, 530, 700, 800],
        "Idade": [18, 22, 23, 30, 35, 44, 49, 50, 67, 75]}

df = pd.DataFrame(dados)

#Separando os dados
#X é a variável independente
#Y é a variável dependente
X = df["Idade"].values
Y = df["Valor"].values

#Função para usar o X transposto
X = X.reshape(-1,1)

#Definindo o regressor linear
regressor = LinearRegression()
#Passando os dados para treinar o regressor
regressor.fit(X, Y)

#Visualizando o gráfico
plt.scatter(X, Y) #Criando o gráfico de Pontos
plt.plot(X, regressor.predict(X), color = 'r') #Criando o gráfico de linha

plt.title("Regressão Linear Simples")
plt.xlabel("Idade")
plt.ylabel("Valor do plano de saúde")
plt.show()


#Prevendo novos valores
idade = np.array(57)
previsao1 = regressor.predict(idade.reshape(-1, 1))
previsao2 = regressor.intercept_ + regressor.coef_*idade

print(f"Previsão 1: {previsao1}")
print(f"Previsão 2: {previsao2}")



