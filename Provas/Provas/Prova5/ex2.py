# -*- coding: utf-8 -*-
"""
Created on Mon May 16 08:22:57 2022

@author: Leonardo Falango
"""

## Faça um algoritmo que trate os dados em um pré-processamento e realize
# três modelos de regressão linear.Ao final deve apresentar as métricas
# de erro com o melhor resultado possível.




# Importando:

# Para tratamento de dados
import pandas as pd
from locale import atof # Para tratamento de vírgulas Ex: 123,45 --> 123.45

# Para utilizar modelo de regressão
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# Para visualização dos dados
import matplotlib.pyplot as plt



# Criando o dataset
df = pd.read_csv('Dados/measurements.csv')


# Devemos associar as váriaveis X e y de acordo com suas respectivas colunas
# O .values.reshape(-1,1) garantirá que nossos dados sairão no formato de array
df = df[['distance', 'consume', 'speed', 'temp_inside', 'temp_outside', 'AC', 'rain', 'sun', 'gas_type']]
df = df.dropna()
df = df.astype(str)
df = df.applymap(lambda x: str(x.replace(',','.'))) # Trocando todas as vírgulas do X por pontos
y = df.iloc[:, -1:] # y é qual nós devemos prever
y = y['gas_type'].astype('category')
y = y.cat.codes # transformando o y em 0 e 1
y = y.values
X = df.iloc[:, :-1] # Pegando todas as colunas menos a ultima
X = X.values # Pegando os valores de X em arrays
# Separando os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# # Instanciamos o algoritmo
lin_reg = LinearRegression()

lin_reg.fit(X_train, y_train)

# Predição
y_pred = lin_reg.predict(X_test)


a = lin_reg.coef_
b = lin_reg.intercept_

# visualizando os dados
print("## Regressão Linear ##")
print(f"Score da Regressão Linear: {lin_reg.score(X_train, y_train)}")
print(f"Erro médio absoluto para regressão linear: {mean_absolute_error(y_test,y_pred)}")
# Esse modelo de regressão linear é ruim para esse tipo de teste

#Algoritmo de árvore
# Aplicando os mesmos conceitos porém utilizando um algoritmo de árvore
# Instanciamos o algoritmo
# Faremos um loop para testar vários valores para max_depth e observar a influencia nos gráficos.
regr = DecisionTreeRegressor(max_depth=None)# Profundidade máxima é um hyperparâmetro
regr.fit(X_train,y_train)

y_pred = regr.predict(X_test)
print("\n\n## Decision Tree##")
print(f"Score Decision Tree: {regr.score(X,y)}")
print(f"Erro médio absoluto Decision Tree: {mean_absolute_error(y_test,y_pred)}")



# Instanciamos o algoritmo
rfr = RandomForestRegressor(max_depth=8, random_state=1) # a profundidade padrão é 8

# Aplicamos ele nos dados de treino para gerar o modelo
rfr.fit(X_train, y_train)

# Predizendo valores baseado no X de treino
y_pred = rfr.predict(X_test)

print("\n\n##Random Forest Regressor##")
print(f"Score Random Forest Regressor: {rfr.score(X,y)}")
print(f"Erro médio absoluto DRandom Forest Regressor: {mean_absolute_error(y_test,y_pred)}")


 