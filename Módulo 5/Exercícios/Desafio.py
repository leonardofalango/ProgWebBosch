# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:19:14 2022

@author: Leonardo Falango
"""

# Para o desafio usaremos TODOS os algoritmos

# Bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Classificadores e métricas
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, plot_roc_curve 
from sklearn.decomposition import PCA

# Algoritmos de Regressão e métricas 
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score

print("Finalizado!")

sns.set()

# Carregando dataset e printando as informações básicas
df_train = pd.read_csv('Dados/train.csv')
df_test = pd.read_csv('Dados/test.csv')
df_train.dropna()
df_test.dropna()


# Montando X e y com base no PCA
y_train = df_train.iloc[:, -1:]
x_train = df_train.iloc[:, 2:-1]

y_test = df_test.iloc[:, -1:]
x_test = df_test.iloc[:, 2:-1]


pca = PCA(n_components=2)

x_train = pca.fit_transform(x_train)
x_test = pca.fit_transform(x_test)


# Instancie os classificadores

logistic_reg = LogisticRegression(random_state = 0) # Regressão Logística
decision_tree = DecisionTreeRegressor(random_state = 0) # Decision Tree Classifier
knn = KNeighborsClassifier() # K-NeighborsClassifier
random_forest = RandomForestRegressor(random_state = 0) # Random Forest
svm = svm.LinearSVC(max_iter=10000, random_state=0) # Support Vector Classifier



# Treine os classificadores

y_train = np.ravel(y_train)
# Regressão Logística
logistic_reg.fit(x_train, y_train)

# Decision Tree Classifier
decision_tree.fit(x_train, y_train)

# K-NeighborsClassifier
knn.fit(x_train, y_train)

# Random Forest
random_forest.fit(x_train, y_train)

# Support Vector Classifier
svm.fit(x_train, y_train)

print("Finalizado!")


# Avalie a acurácia dos Classificadores

# Regressão Logística
y_pred_logistic_reg = logistic_reg.predict(x_test)
y_train = y_train.reshape(-1,1)

print(accuracy_score(y_test, y_pred_logistic_reg))


# Decision Tree Classifier
y_pred_decision_tree = decision_tree.predict(x_test)
y_train = y_train.reshape(-1,1)

print(accuracy_score(y_test, y_pred_decision_tree))


# K-NeighborsClassifier
y_pred_knn = knn.predict(x_test)
y_train = y_train.reshape(-1,1)

print(accuracy_score(y_test, y_pred_knn))


# Random Forest
y_pred_random_forest = random_forest.predict(x_test)
y_train = y_train.reshape(-1,1)

print(random_forest.score(x_test, y_pred_random_forest))


# Support Vector Classifier
y_pred_svm = svm.predict(x_test)
y_train = y_train.reshape(-1,1)

print(accuracy_score(y_test, y_pred_svm))



# Avalie a matriz confusão dos classificadores 

# Regressão Logística
cm_log_reg = confusion_matrix(y_test, y_pred_logistic_reg)
print("Logistic Reg")
print(cm_log_reg)
print('\n\n')


# Decision Tree Classifier
cm_decision_tree = confusion_matrix(y_test, y_pred_decision_tree)
print("Decision Tree Classifier")
print(cm_decision_tree)
print('\n\n')


# K-NeighborsClassifier
cm_knn = confusion_matrix(y_test, y_pred_knn)
print("KNN")
print(cm_knn)
print('\n\n')


# Random Forest
print("Random Forest")
cm_random_forest = confusion_matrix(y_test, y_pred_random_forest.astype(int))
print(cm_random_forest)
print('\n\n')


# Support Vector Classifier
print("SVC / SVM")
cm_svm = confusion_matrix(y_test, y_pred_svm)
print(cm_svm)
print('\n\n')



tests = [cm_log_reg, cm_decision_tree, cm_knn, cm_random_forest, cm_svm]

for i in tests:
    sns.heatmap(i)
    plt.show()




# Bônus: Plote as fronteiras de decisão dos classificadores.

# Regressão Logística
plot_decision_regions(x_train, y_train.flatten(), logistic_reg)
plt.show()
# Decision Tree Classifier
plot_decision_regions(x_train, y_train.flatten(), decision_tree)
plt.show()
# K-NeighborsClassifier
plot_decision_regions(x_train, y_train.flatten(), knn)
plt.show()
# Random Forest
plot_decision_regions(x_train, y_train.flatten(), random_forest)
plt.show()
# Support Vector Classifier
plot_decision_regions(x_train, y_train.flatten(), svm)
plt.show()

