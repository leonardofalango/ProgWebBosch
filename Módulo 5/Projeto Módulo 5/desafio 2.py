# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:39:56 2022

@author: Leonardo Falango
"""

# Imports
import pandas as pd
import numpy as np
from  sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, mean_absolute_error


# Funções

def transform(x):
    if 10**6<x or x<-10**6:
        x = x/(10**6)
        conversao = 'M'
    elif 10**3<x or x<-10**3:
        x = x/(10**3)
        conversao = 'k'
    else:
        conversao = ''
    
    if x<0: # O algoritmo, por se tratar de uma regressão linear, ele preve alguns números negativos. Para concertar isso eu só alterei para eles serem positivos também
        x = x*-1
    
    x = round(x,0) # arredondando o x
    x = str(x) # Transformando o x para string 
    x = x[:-2] # Tirando a vírgula do número
    x = '€' + x + conversao # conversao seria a conversão das unidades de medidas
    return x







df = pd.read_csv('data.csv')

all_skills = df[['Age', 'Overall', 'Potential', 'Weak Foot', 'Skill Moves', 'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
           'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB',
           'RB', 'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
           'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping',
           'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
           'Marking', 'StandingTackle', 'GKDiving', 'GKPositioning', 'GKReflexes', 'Value']]

all_skills = all_skills.dropna().values

# Predição de valor do jogador

# Tratando os dados

all_skills = list(all_skills)
X_test = []
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
x_test = all_skills.loc[all_skills[64] == 0]
x_train = all_skills.loc[all_skills[64] != 0]

y_train = x_train.iloc[:,-1:]
x_train = x_train.iloc[:,:-1]

y_test = x_test.iloc[:,-1:]
x_test = x_test.iloc[:,:-1]

# for linha in range(len(all_skills)):
#     try:
#         count = 0
#         for coluna in range(len(all_skills[linha])):
#             for x in range(len(all_skills[linha])):
#                 if count > 10:
#                     del all_skills[linha]
#                     break
#                 if (all_skills[linha][coluna] == X_test[x][coluna]):
#                     count+=1
#             if count > 10:
#                 break
#     except IndexError:
#         print(".", end='')
#         continue
            

# all_skills = pd.DataFrame(all_skills)
# X_train = all_skills.iloc[:,:-1]
# y = all_skills.iloc[:, -1:]

# pca = PCA(n_components = 2)
# X = pca.fit_transform(X)




regr = linear_model.LinearRegression()
regr.fit(x_train,y_train)

y_pred = regr.predict(x_test)

# comparation = pd.DataFrame(y_pred)

# comparation = pd.DataFrame(comparation)
# print(comparation)


y_predtrans = []
# Para deixar no formato que possui o dataset original (€xxM)

for i in range(len(y_pred)):
    predict = float(y_pred[i])
    y_predtrans.append(transform(predict))


comparation = pd.DataFrame(y_predtrans) # Tabela pronta para fazer a comparação


print("\n\n\nLinear Regression Score(R²): {}".format(regr.score(x_train,y_train)))
print("MSE: {}".format(mean_squared_error(y_test, y_pred)))
print("MAE: {}".format(mean_absolute_error(y_test, y_pred)))


import matplotlib.pyplot as plt
plt.scatter(x_test.iloc[:,0:1], y_test, label='True Y', color=np.random.rand(3,))
plt.scatter(x_test.iloc[:,0:1], y_pred, label='Pred Y', color=np.random.rand(3,))
plt.title('Prediction')
plt.legend()
plt.show()

