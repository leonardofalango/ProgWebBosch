# -*- coding: utf-8 -*-
"""
Created on Tue May 17 08:29:05 2022

@author: Leonardo Falango
"""


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.metrics import accuracy_score


df = pd.read_csv('data.csv')

all_skills = df[['Age', 'Overall', 'Potential', 'Weak Foot', 'Skill Moves', 'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
           'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB',
           'RB', 'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
           'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping',
           'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
           'Marking', 'StandingTackle', 'GKDiving', 'GKPositioning', 'GKReflexes', 'Position']]

# 18207 before drop
all_skills = all_skills.fillna(0)
# 16122 after drop


category_value = [] # são os uniques de posição

position_skills = {}



DEFENDING = ["CB","LB","LCB","LWB","RB","RCB","RWB"]
MIDFIELD = ["CAM","CDM","CM","LAM","LCM","LDM","LM","RAM","RCM","RDM","RM"]
ATTACKING = ["CF","LF","RF","RS","RW","LW","LS","ST"]
GOALKEEPER = ["GK"]

main = []

for i in df["Position"]:
    if i in DEFENDING:
        main.append("Defensor")
    elif i in MIDFIELD:
        main.append("Meio-Campo")
    elif i in ATTACKING:
        main.append("Atacante")
    elif i in GOALKEEPER:
        main.append("Goleiro")
    else:
        main.append(np.nan)
all_skills["Posição principal"] = main
all_skills = all_skills.values

# A ideia primeiramente era fazer um pca pra tudo, mas, eu pensei que ficaria mais preciso a IA, se ela se utiliza-se um pca para cada posição
# Por isso, vamos separar o y(posição) para cada posição.


# # Separando as funções
# striker_skills = all_skills.loc[all_skills['Position'] == 'ST']

# atk_right = all_skills.loc[all_skills['Position'] == 'RF']

# atk_left = all_skills.loc[all_skills['Position'] == 'LF']

# atk_center = all_skills.loc[all_skills['Position'] == 'CF']


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
                     
        except AttributeError: # Se o split nao funcionar, continuar tentando até o final
            continue


# Trasformando os valores em float



all_skills = pd.DataFrame(all_skills)
all_skills = all_skills.drop(columns=[64])

test = all_skills.loc[all_skills.isnull().values] # Os valores de teste são os valores nulos na tabela
train = all_skills.loc[all_skills[65].notnull().values]

X_train, y_train = train.iloc[:,:-1], train.iloc[:,-1:]
X_test, y_test= test.iloc[:,:-1], test.iloc[:,-1:]



# Não precisa dividir em treino e teste, pois ja temos qual devemos testar

knn = KNeighborsClassifier() # K-NeighborsClassifier
y_train = np.ravel(y_train)

# K-NeighborsClassifier Training
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)

skills_notnull = all_skills.loc[all_skills.notnull().values]
x_train, x_test, y_train, y_test = train_test_split(skills_notnull.iloc[:, :-1], skills_notnull.iloc[:,-1:], random_state=0,test_size=0.25)
y_pred_test = knn.predict(x_test)
print("Acurracy: {}".format(accuracy_score(y_test, y_pred)))

# Prevendo a acurácia na parte do campo em que o jogador joga
# print(name_positions)


# # Poderia simplesmente fazer um loop para adicionar o indice de cada posição, mas como eu ja tinha um material base, eu peguei ele mesmo



# for i in range(len(y_pred)):
#     for j in range(len(listas)):
#         for x in range(len(listas[j])):           
#             if (listas[j][x] == y_pred[i]):
#                 # print(j, end= ' | ')
#                 # print(listas[j][x])
#                 y_pred[i] = j

# print("Acurracy (atk, defense, midlefield, gk): {}".format(accuracy_score(y_test, y_pred)))
