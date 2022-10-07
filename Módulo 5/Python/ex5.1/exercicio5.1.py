# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:33:22 2022

@author: Leonardo Falango
"""
# =============================================================================
# Imports
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# =============================================================================
# DataBase
# =============================================================================
df = pd.read_csv("1_salary.csv", sep=";")



#Separando os valores
independente = df['Experience'].values
dependente = df['Salary ($)'].values

#Transpondo valores
independente = independente.reshape(-1,1)

#Criando o regressor
regressor = LinearRegression() #Iniciando o regressor
regressor = regressor.fit(independente, dependente)
previsao = regressor.predict(independente)

# =============================================================================
# Gráficos
# =============================================================================
# plt.scatter(independente, dependente)
# plt.plot(independente, regressor.predict(independente), color='r')
# plt.grid(True)

# plt.show()


print(previsao)