# -*- coding: utf-8 -*-
"""
Created on Thu May 12 08:19:33 2022

@author: Leonardo Falango
"""

# Existe alguma relação entre os valores de humidade e temperatura?
# E entre a humidade e temperatura aparente? 
# Verifique essas duas relações graficamente e crie uma forma de prever a temperatura em função da humidade.


# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt




# Database
db_complete = pd.read_csv('Dados/weatherHistory.csv') # Reading csv
db_complete = db_complete[['Temperature (C)', 'Humidity', 'Apparent Temperature (C)']] # Just the values that will be used
db_complete = db_complete.dropna() # Dropping n/a or invalid values

# =============================================================================
# Humidity x Temperature
# =============================================================================

# Setting database
db_ht = db_complete[['Temperature (C)', 'Humidity']] # First one is relation of temperature and humidity
x = db_ht['Temperature (C)'].values # setting x
x = x.reshape(-1,1) # Reshaping x
y = db_ht['Humidity'].values # setting y
# Splitting into train and test data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=0)


lin_reg = LinearRegression() # Creating the model
lin_reg.fit(x_train, y_train) # Training model
y_pred = lin_reg.predict(x_test) # Predicting Y

# Plotting

fig, eixo = plt.subplots(nrows=2, ncols=2, figsize=(10,10))

# plotting real x and y
eixo[0][0].scatter(y, x, color=np.random.rand(3,), label='Real')
eixo[0][0].set_title('Real')
eixo[0][0].legend(loc="upper right")


# plotting training data
eixo[0][1].scatter(y_train, x_train, color=np.random.rand(3,), label='Train')
eixo[0][1].set_title('Train')
eixo[0][1].legend(loc="upper right")


# plotting predict x data
eixo[1][0].plot(y_pred, x_test, color=np.random.rand(3,), label='Predict', lw=3)
eixo[1][0].scatter(y, x, color=np.random.rand(3,), label='Data')
eixo[1][0].set_title('Linear Regression')
eixo[1][0].legend(loc="upper right")


# plotting training data x test data
eixo[1][1].scatter(y_train, x_train, color=np.random.rand(3,), label='Train')
eixo[1][1].scatter(y_test, x_test, color=np.random.rand(3,), label='Test')
eixo[1][1].set_title('Train x Real')
eixo[1][1].legend(loc="upper right")

plt.show()


# Verifying the accuracy of the model
print('Métricas para dados de teste: ')
print('R2 (treino) - {:.1%}'.format(lin_reg.score(x_train, y_train)))
print('R2 (teste) - {:.1%}'.format(lin_reg.score(x_test, y_test)))
print('Erro médio absoluto - {:.3f}'.format(mean_absolute_error(y_test, y_pred)))
print('Erro médio quadrático - {:.3f}'.format(mean_squared_error(y_test, y_pred)))


# =============================================================================
# Humidity x Apparent Temperature
# =============================================================================

# Setting database
db_ha = db_complete[['Apparent Temperature (C)', 'Humidity']]
x = db_ha['Apparent Temperature (C)'].values # setting x
x = x.reshape(-1,1) # Reshaping x
y = db_ht['Humidity'].values # setting y
# Splitting into train and test data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=0)

lin_reg = LinearRegression() # Creating the model
lin_reg.fit(x_train, y_train) # Training model
y_pred = lin_reg.predict(x_test) # Predicting Y

# Plotting
fig, eixo = plt.subplots(nrows=1, ncols=2, figsize=(12,8))

# plotting training data x test data
eixo[0].scatter(y_train, x_train, color=np.random.rand(3,), label='Train')
eixo[0].scatter(y_test, x_test, color=np.random.rand(3,), label='Test')
eixo[0].set_title('Train x Real')
eixo[0].legend(loc="upper right")


# plotting predict x data
eixo[1].plot(y_pred, x_test, color=np.random.rand(3,), label='Predict', lw=3)
eixo[1].scatter(y, x, color=np.random.rand(3,), label='Data')
eixo[1].set_title('Linear Regression')
eixo[1].legend(loc="upper right")

plt.show()




# Verifying the accuracy of the model
print('Métricas para dados de teste: ')
print('R2 (treino) - {:.1%}'.format(lin_reg.score(x_train, y_train)))
print('R2 (teste) - {:.1%}'.format(lin_reg.score(x_test, y_test)))
print('Erro médio absoluto - {:.3f}'.format(mean_absolute_error(y_test, y_pred)))
print('Erro médio quadrático - {:.3f}'.format(mean_squared_error(y_test, y_pred)))