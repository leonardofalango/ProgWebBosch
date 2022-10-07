# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:30:57 2022

"""
# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor



# Creating Database
db = pd.read_csv('Dados/Advertising.csv')
db = db.dropna()


# Setting database
db = db[['TV', 'radio', 'newspaper', 'sales']] # First one is relation of temperature and humidity
x = db[['TV', 'radio', 'newspaper']].values # setting x

y = db['sales'].values # setting y
y = y.reshape(-1, 1) # Reshaping y
# Splitting into train and test data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=0)



# Instanciamos o algoritmo
rfr = RandomForestRegressor(max_depth=2, random_state=27) # a profundidade padrão é 8

# Aplicamos ele nos dados de treino para gerar o modelo
rfr.fit(x_train, y_train)

y_pred = rfr.predict(x_test)

# test_x = np.arange(0,66,1) # For same x, y_pred and y_real should be the same
x_graph = (x_test[:, 1:2])

plt.scatter(x_graph, y_test, color=np.random.rand(3,), label='Dado Real')
plt.scatter(x_graph, y_pred, color=np.random.rand(3,), label='Predição')
plt.legend()
plt.show()

# Verifying the accuracy of the model
print('Métricas para dados de teste: ')
print('R2 (treino) - {:.1%}'.format(rfr.score(x_train, y_train)))
print('R2 (teste) - {:.1%}'.format(rfr.score(x_test, y_test)))
print('Erro médio absoluto - {:.3f}'.format(mean_absolute_error(y_test, y_pred)))
print('Erro médio quadrático - {:.3f}'.format(mean_squared_error(y_test, y_pred)))