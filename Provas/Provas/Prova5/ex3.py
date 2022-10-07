# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:54:44 2022

@author: Leonardo Falango
"""
# Bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Classificadores e métricas
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import confusion_matrix, classification_report

# Algoritmos de Regressão e métricas 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA


# Criando o dataset
df = pd.read_csv('Dados/Churn_Modelling.csv')

# Instanciando o pca
pca = PCA(n_components=2)

# Devemos associar as váriaveis X e y de acordo com suas respectivas colunas
# O .values.reshape(-1,1) garantirá que nossos dados sairão no formato de array
df = df.dropna()
y = df.iloc[:, -1:].values # y é qual nós devemos prever
X = df[['CreditScore', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']] # Pegando todas as colunas menos a ultima
# X = pca.fit_transform(X, y) # Principal Componente de Análise, mas não vamos usar ele nesses modelos

x_train, x_test, y_train, y_test = train_test_split(X, y , random_state=0)

y_train = np.ravel(y_train)

# Instancie os classificadores
logistic_reg = LogisticRegression(random_state = 3) # Regressão Logística
decision_tree = DecisionTreeRegressor(random_state = 0) # Decision Tree Classifier
knn = KNeighborsClassifier() # K-NeighborsClassifier


# Treine os classificadores

# Regressão Logística
logistic_reg.fit(x_train, y_train)

# Decision Tree Classifier
decision_tree.fit(x_train, y_train)

# K-NeighborsClassifier
knn.fit(x_train, y_train)





# Avaliando tudo

y_pred_logistic_reg = logistic_reg.predict(x_test)
y_pred_decision_tree = decision_tree.predict(x_test)
y_pred_knn = knn.predict(x_test)

# Confusion Matrix
cm_log_reg = confusion_matrix(y_test, y_pred_logistic_reg)
cm_decision_tree = confusion_matrix(y_test, y_pred_decision_tree)
cm_knn = confusion_matrix(y_test, y_pred_knn)

names = ['Logistic Regression', 'Decision Tree', 'KNewighbors']
models = [logistic_reg, decision_tree, knn]

for i in range(len(names)):
    print('_'*50)
    print(f'\nMatriz confusão {names[i]}:')
    print(f'\nScore: {models[i].score(X,y)}')
    print(f'{confusion_matrix(y_test, models[i].predict(x_test))}')
    print(f'Acurácia de {accuracy_score(y_test, models[i].predict(x_test))*100}%\n')
    print(classification_report(y_test, models[i].predict(x_test)))
    
