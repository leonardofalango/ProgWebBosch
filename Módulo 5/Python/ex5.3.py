# -*- coding: utf-8 -*-
"""
Created on Thu May  5 08:14:25 2022

@author: Leonardo Falango
"""
# Importando bibliotecas importantes:

# Para manipulação dos dados
import pandas as pd

# Para utilizar modelo de regressão e dividir os dados em treino e teste
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

# Para visualização dos dados
import matplotlib.pyplot as plt

# Setando configurações dos gráficos (opcional)
#plt.style.use('ggplot')

# Importando os dados
df = pd.read_csv('S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Módulo 5/3_grade.csv', sep=',')
print(df.head())

# Devemos associar as váriaveis X e y de acordo com suas respectivas colunas
# O .values.reshape(-1,1) garantirá que nossos dados sairão no formato de array
X = df['SAT'].values.reshape(-1,1)
y = df['GPA'].values.reshape(-1,1)
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Visualizando dados

# Ajuste da imagem


# Instanciamos o algoritmo
linreg = LinearRegression()

linreg.fit(X, y)

a = linreg.coef_
b = linreg.intercept_
# # Visualizando dados
# print('Dados: {}\nPredicões: {}'.format((X,y), (X, linreg.predict(X))))


# Visualizando linha gerada pela função
plt.scatter(X, y, label='Dados')
plt.plot(X, linreg.predict(X), color = 'b', label='Predição')
# plt.show();

# Observando os coeficientes da função
print('Para Regressão Linear')
print('Nosso [b0]: ', )
print('Nosso [b1]: ', )
print(f'Nossa função gerada foi: Y = {round(float(b), 3)} + {round(float(a), 3)}*X')


# Visualizando dados de treino e teste
# plt.scatter(X_train, y_train, color='blue', label='Dados de teste')
plt.scatter(X_test, y_test, color='green', label='Dados de treino')
# plt.scatter(x_new, linreg.predict(X), color='red', label='Pontos novos')
plt.legend()
plt.title("Linear Regression")
plt.show()



# =============================================================================
# Colors
# =============================================================================

rosa = 'm'
azul = 'b'





import numpy as np
#Algoritmo de árvore
# Aplicando os mesmos conceitos porém utilizando um algoritmo de árvore
# Instanciamos o algoritmo
# Faremos um loop para testar vários valores para max_depth e observar a influencia nos gráficos.
for i in [None, 5, 1, 2]:
    regr = DecisionTreeRegressor(max_depth=i)# Profundidade máxima é um hyperparâmetro
    regr.fit(X,y)
    #porque nós setamos de forma manual 
    #None você deixa a árvore crescer indefinidademente 
    #Nesta árvore é possível verificar que a árvore abraçou quase todos os pontos com alta
    #variância
    
    # Aplicamos ele nos dados de treino para gerar o modelo
    X_test = sorted(X_test)    
    # Predizendo valores baseado no X de treino
    y_predict = regr.predict(X_test)

    # Visualizando dados
    # df_dados = {"X_train" : list(X),
    #             "Y_train" : list(y),
    #             "X_test" : list(X_test),
    #             "Y_test" : list(y)}
    # df_dados = pd.DataFrame(df_dados)
    # print(df.head(5))

    # Visualizando linha gerada pela função
    plt.scatter(X_train, y_train,color= rosa)
    plt.scatter(X_test, y_test, color = azul)
    plt.plot(X_test, y_predict, color='black', lw = 3)
    plt.title("Decision Tree Regressor")
    plt.show()

    # Ajuste da imagem


 

# Instanciamos o algoritmo
rfr = RandomForestRegressor(max_depth=2, random_state=27) # a profundidade padrão é 8

# Aplicamos ele nos dados de treino para gerar o modelo
rfr.fit(X_train, y_train)

# Predizendo valores baseado no X de treino
y_predict = rfr.predict(X_test)

plt.scatter(X_train, y_train, label="Treino", color = rosa)
plt.scatter(X_test, y_test, label ="Teste", color = azul)
plt.plot(X_test, y_predict, label="Predição", color="black", lw=3)
plt.title("Random Forest")
plt.legend()

# Informações dos modelos

clf = [linreg, regr, rfr]
nomes = ['Linear Regression', 'Decision Tree', 'Random Forest']

for i, model in enumerate(clf):
    print('\n')
    print(nomes[i])
    print('Métricas para dados de teste: ')
    print('R2 (treino) - {:.1%}'.format(model.score(X_train, y_train)))
    print('R2 (teste) - {:.1%}'.format(model.score(X_test, y_test)))
    print('Erro médio absoluto - {:.3f}'.format(mean_absolute_error(y_test, model.predict(X_test))))
    print('Erro médio quadrático - {:.3f}'.format(mean_squared_error(y_test, model.predict(X_test))))



