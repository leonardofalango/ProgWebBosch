# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:40:22 2022

@author: Leonardo Falango
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions
from sklearn.decomposition import PCA


# Dataset
from sklearn.datasets import load_breast_cancer #Esta base de dados contém tipos de Câncer entre Benignos e Malignos
dados=load_breast_cancer()
cancer=pd.DataFrame(data=dados.data, columns=dados.feature_names) 
cancer['Class']=dados.target
cancer.dropna()

x = cancer.iloc[:,:-1]
y = cancer.iloc[:,-1:]

# Para esse problema iremos usar o Support Vector Classifirer
# SVC

# Splitting x and y for training and test
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20, random_state=0) # random_state=0 --> 100% acurácia

y_train = np.ravel(y_train)

# Creating svm
svm = svm.LinearSVC(max_iter=100000, random_state=0) # Support Vector Classifier


# =- =-= -= -= -= -=- =- =- =- =- = PCA =- == = -=- - =-= =  COMPENENTE PRINCIPAL DE ANÁLISE
pca = PCA(n_components=2)

x_train = pca.fit_transform(x_train)
x_test = pca.fit_transform(x_test)


# Training
svm.fit(x_train, y_train)

# Predicting
y_pred_svm = svm.predict(x_test)
y_train = y_train.reshape(-1,1)
print(f'\n\nAcurácia: {accuracy_score(y_test, y_pred_svm)}')

# Confusion Matrix
print("SVC / SVM")
cm_svm = confusion_matrix(y_test, y_pred_svm)
print(cm_svm)
print('\n\n')

# Plottando os gráficos
# plt.scatter(x, y, color=np.random.rand(3,))
x_graph = np.arange(0, 114,1)
plt.scatter(x_graph, y_test, color=np.random.rand(3,), label='Real')
plt.scatter(x_graph, y_pred_svm, color=np.random.rand(3,), label = 'Prediction')
plt.legend()
plt.show()
# No gráfico, os pontos que estão sobrepostos são aqueles que a previsão foi correta


# Verifying the accuracy of the model
print('Métricas para dados de teste: ')
print('R2 (treino) - {:.1%}'.format(svm.score(x_train, y_train)))
print('R2 (teste) - {:.1%}'.format(svm.score(x_test, y_test)))
print('Erro médio absoluto - {:.3f}'.format(mean_absolute_error(y_test, y_pred_svm)))
print('Erro médio quadrático - {:.3f}'.format(mean_squared_error(y_test, y_pred_svm)))


# Plottando a decision region



y_train = np.ravel(y_train)
plot_decision_regions(x_train, y_train, clf=svm, legend=2)
plt.show()


