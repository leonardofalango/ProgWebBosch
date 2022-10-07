# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:07:10 2022

@author: DISRCT
"""


# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score
from mlxtend.plotting import plot_decision_regions
from sklearn.decomposition import PCA



db = pd.read_csv('Dados/candy-data.csv')


y = db.iloc[:, 1] # O chocolate é qual nós temos que prever
x = db.iloc[:, 2:] # Pegando as colunas depois do chocolate

# Usaremos o PCA para pegar a coluna(feature) de maior influência
pca = PCA(n_components=2)


# Para esse problema iremos usar o Support Vector Classifirer
# SVC

# Splitting x and y for training and test
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0) # random_state=0 --> 100% acurácia
x_train = pca.fit_transform(x_train)
x_test = pca.fit_transform(x_test)
y_train = np.ravel(y_train)

# Creating svm
svm = svm.LinearSVC(max_iter=10000, random_state=0) # Support Vector Classifier

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


# No gráfico, os pontos que estão dentro de outros, quer dizer que aceteram a previsão
y_train = np.ravel(y_train)
plot_decision_regions(x_train, y_train, clf=svm, legend=2)
plt.show()
