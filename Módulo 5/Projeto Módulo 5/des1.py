# -*- coding: utf-8 -*-
"""
Created on Tue May 17 08:29:05 2022

@author: Leonardo Falango
"""


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from  sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
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

# A ideia primeiramente era fazer um pca pra tudo, mas, eu pensei que ficaria mais preciso a IA, se ela se utiliza-se um pca para cada posição
# Por isso, vamos separar o y(posição) para cada posição.


# # Separando as funções
# striker_skills = all_skills.loc[all_skills['Position'] == 'ST']

# atk_right = all_skills.loc[all_skills['Position'] == 'RF']

# atk_left = all_skills.loc[all_skills['Position'] == 'LF']

# atk_center = all_skills.loc[all_skills['Position'] == 'CF']

name_positions = []

name_positions = all_skills['Position'].unique()
name_positions = name_positions[0:-1] # Tirando o valor 'nan' do array

category_value = [] # são os uniques de posição

position_skills = {}

for i in range(len(name_positions)):
    position_skills[name_positions[i]] = all_skills.loc[all_skills['Position'] == name_positions[i]]
    category_value.append(i)
# Antes de usarmos o PCA, precisa ter apenas int ou float
for i in range(len(name_positions)):
    df_position = position_skills[name_positions[i]].values
    for linha in range(len(df_position)):
        for coluna in range(len(df_position[linha])):
            try:
                valor = df_position[linha][coluna] 
                aux = valor.split("'") # Tirando o ' da altura dos jogadores --> 7'4 vira 7+4 = 11
                if (len(aux) == 2):
                    aux = aux[0] + aux[1]
                    df_position[linha][coluna] = aux
                
                aux = valor.split("+") # Tirando o '+' do overall dos jogadores --> 92+4 coloquei apenas 92
                
                if (len(aux) == 2):
                    aux = aux[0]
                    df_position[linha][coluna] = aux
                    
                aux = valor.split("l") # Tirando o 'lbs' do peso dos jogadores
                
                if (len(aux) == 2):
                    aux = aux[0]
                    df_position[linha][coluna] = aux
                
                if (coluna == len(df_position[linha]) - 1): # Arrumando as posições, trocando para números --> RF = 1, ST = 2... 
                    for j in range(len(name_positions)):
                        if name_positions[j] == df_position[linha][coluna]:
                            df_position[linha][coluna] = category_value[j]
                            

                position_skills[name_positions[i]] = df_position

                
            except AttributeError: # Se o split nao funcionar, continuar tentando até o final
                continue


new_data_base = []
for i in range(len(name_positions)):
    new_data_base.extend(position_skills[name_positions[i]])
new_data_base = pd.DataFrame(new_data_base)

X = new_data_base.iloc[:,:-1]
y = new_data_base.iloc[:,-1:]

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0,test_size=0.25)


knn = KNeighborsClassifier() # K-NeighborsClassifier
y_train = np.ravel(y_train)

# K-NeighborsClassifier Training
knn.fit(x_train, y_train)


# =============================================================================
# Testing other algs
# =============================================================================
knn = KNeighborsClassifier()
dct = DecisionTreeClassifier()
rfr = RandomForestClassifier()

knn.fit(x_train,y_train)
dct.fit(x_train,y_train)
rfr.fit(x_train,y_train)

y_predknn = knn.predict(x_test)
y_preddct = dct.predict(x_test)
y_predrfr = rfr.predict(x_test)


y_pred = knn.predict(x_test)
print("Acurracy: {}".format(accuracy_score(y_test, y_pred)))
print("Acurácia baixa, pois ele define a posição completa do jogador, não apenas na parte do ataque, defesa, etc")

# Prevendo a acurácia na parte do campo em que o jogador joga
# print(name_positions)
name_positions_list = list(name_positions)

# Poderia simplesmente fazer um loop para adicionar o indice de cada posição, mas como eu ja tinha um material base, eu peguei ele mesmo
DEFENDING = [name_positions_list.index("CB"),name_positions_list.index("LB"),
             name_positions_list.index("LCB"),name_positions_list.index("LWB"),
             name_positions_list.index("RB"),name_positions_list.index("RCB"),
             name_positions_list.index("RWB")]

MIDFIELD = [name_positions_list.index("CAM"),name_positions_list.index("CDM"),
            name_positions_list.index("CM"),name_positions_list.index("LAM"),
            name_positions_list.index("LCM"),name_positions_list.index("LDM"),
            name_positions_list.index("LM"),name_positions_list.index("RAM"),
            name_positions_list.index("RCM"),name_positions_list.index("RDM"),
            name_positions_list.index("RM")]

ATTACKING = [name_positions_list.index("CF"),name_positions_list.index("LF"),
             name_positions_list.index("RF"),name_positions_list.index("RS"),
             name_positions_list.index("RW"),name_positions_list.index("LW"),
             name_positions_list.index("LS"),name_positions_list.index("ST")]

GK = [name_positions_list.index("GK")]

listas = [ATTACKING, MIDFIELD, DEFENDING, GK]
y_test = y_test.values

for i in range(len(y_test)):
    for j in range(len(listas)):
        for x in range(len(listas[j])):
            if (listas[j][x] == y_test[i]):
                y_test[i] = j


for i in range(len(y_pred)):
    for j in range(len(listas)):
        for x in range(len(listas[j])):           
            if (listas[j][x] == y_pred[i]):
                y_pred[i] = j
            if (listas[j][x] == y_predknn[i]):
                y_predknn[i] = j
            if (listas[j][x] == y_preddct[i]):
                y_preddct[i] = j
            if (listas[j][x] == y_predrfr[i]):
                y_predrfr[i] = j

print("Acurracy (atk, defense, midlefield, gk): {}".format(accuracy_score(y_test, y_pred)))


print("\n"*5)
models = [y_predknn, y_preddct, y_predrfr]
nomes = ['KNN', 'DTC', 'RFR']
for i in range(len(models)):
    print("Acurácia {}: {}".format(nomes[i],accuracy_score(y_test, models[i])))
