# -*- coding: utf-8 -*-
"""
Created on Tue May 17 08:29:05 2022

@author: Leonardo Falango
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error


df = pd.read_csv('data.csv')

all_skills = df[['Age', 'Overall', 'Potential', 'Weak Foot', 'Skill Moves', 'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
           'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB',
           'RB', 'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
           'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping',
           'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
           'Marking', 'StandingTackle', 'GKDiving', 'GKPositioning', 'GKReflexes', 'Position', 'Value']]

# 18207 before drop
all_skills = all_skills.fillna(0)
# 16122 after drop

# A ideia primeiramente era fazer um pca pra tudo, mas, eu pensei que ficaria mais preciso a IA, se ela se utiliza-se um pca para cada posição
# Por isso, vamos separar o y(posição) para cada posição.


# # Separando as funções
name_positions = []

all_skills = all_skills.loc[all_skills['Position'] == 'GK']
all_skills = all_skills.drop(columns=['Position'])
all_skills = all_skills.values


# Antes de usarmos o PCA, precisa ter apenas int ou float

for linha in range(len(all_skills)):
    for coluna in range(len(all_skills[linha])):
        try:
            valor = all_skills[linha][coluna] 
            aux = valor.split("'") # Tirando o ' da altura dos jogadores --> 7'4 vira 7+4 = 11
            if (len(aux) == 2):
                aux = aux[0] + aux[1]
                all_skills[linha][coluna] = aux
            
            aux = valor.split("+") # Tirando o '+' do overall dos jogadores --> 92+4 coloquei apenas 92
            
            if (len(aux) == 2):
                aux = aux[0]
                all_skills[linha][coluna] = aux
                
            aux = valor.split("l") # Tirando o 'lbs' do peso dos jogadores
            
            if (len(aux) == 2):
                aux = aux[0]
                all_skills[linha][coluna] = aux
                
            aux = valor.split("€")
            
            if (valor == '€0'):
                all_skills[linha][coluna] = 0
            
            if (len(aux) == 2):
                if (aux[1] == 0):
                    break
                if aux[1][-1:] == 'M':
                    aux[1] = aux[1][:-1]
                    aux[1] = float(aux[1])
                    aux[1] = aux[1]*1000000
                    all_skills[linha][coluna] = aux[1]
                elif aux[1][-1:] == 'K':
                    aux[1] = aux[1][:-1]
                    aux[1] = float(aux[1])
                    aux[1] = aux[1]*1000
                    all_skills[linha][coluna] = aux[1]

        except AttributeError: # Se o split nao funcionar, continuar tentando até o final
            continue




all_skills = pd.DataFrame(all_skills)
X = all_skills.iloc[:,:-1]
y = all_skills.iloc[:,-1:]
y = y.astype('int')
y = np.ravel(y)

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0,test_size=0.25)
x_plot = np.linspace(0, 507, 507)
print('-'*80)
# =============================================================================
# KNeighbors Classifier
# =============================================================================
knn = KNeighborsClassifier() # K-NeighborsClassifier
knn.fit(x_train, y_train)
y_pred_knn = knn.predict(x_test)

plt.title('KFC ◑﹏◐')
plt.scatter(x_plot, y_test, color=np.random.rand(3,), label='Real')
plt.scatter(x_plot, y_pred_knn, color=np.random.rand(3,), label='Predict')
plt.legend()
plt.show()

print("\n\n\nKNeighbors Score: {}".format(knn.score(X,y)))
print("MSE: {}".format(mean_squared_error(y_test, y_pred_knn)))
print("MAE: {}".format(mean_absolute_error(y_test, y_pred_knn)))


# =============================================================================
# Random Forest Regressor
# =============================================================================
rfr = RandomForestRegressor(random_state=0)
rfr.fit(x_train, y_train)
y_pred_rfr = rfr.predict(x_test)

plt.title('Random Forest ╰(*°▽°*)╯')
plt.scatter(x_plot, y_test, color=np.random.rand(3,), label='Real')
plt.scatter(x_plot, y_pred_rfr, color=np.random.rand(3,), label='Predict')
plt.legend()
plt.show()

print("\n\n\nRandom Forest Regressor Score (R²): {}".format(rfr.score(X,y)))
print("MSE: {}".format(mean_squared_error(y_test, y_pred_rfr)))
print("MAE: {}".format(mean_absolute_error(y_test, y_pred_rfr)))


# =============================================================================
# Logistic Regressor
# =============================================================================
log_reg = LogisticRegression(random_state=0)
log_reg.fit(x_train, y_train)
y_pred_log = log_reg.predict(x_test)


plt.title('Longistic Regression (⊙_⊙;)')
plt.scatter(x_plot, y_test, color=np.random.rand(3,), label='Real')
plt.scatter(x_plot, y_pred_log, color=np.random.rand(3,), label='Predict')
plt.legend()
plt.show()

print("\n\n\nLogistic Regression Score(R²): {}".format(log_reg.score(X,y)))
print("MSE: {}".format(mean_squared_error(y_test, y_pred_log)))
print("MAE: {}".format(mean_absolute_error(y_test, y_pred_log)))


# =============================================================================
# Linear Regressor
# =============================================================================

lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)
y_pred_lin = lin_reg.predict(x_test)


plt.title('Milenar Regression ~(¹▽¹)~*')
plt.scatter(x_plot, y_test, color=np.random.rand(3,), label='Real')
plt.scatter(x_plot, y_pred_lin, color=np.random.rand(3,), label='Predict')
plt.legend()
plt.show()

print("\n\n\nLinear Regression Score(R²): {}".format(lin_reg.score(X,y)))
print("MSE: {}".format(mean_squared_error(y_test, y_pred_lin)))
print("MAE: {}".format(mean_absolute_error(y_test, y_pred_lin)))


# =============================================================================
# RESULTS
# =============================================================================




