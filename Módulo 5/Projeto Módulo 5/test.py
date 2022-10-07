# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:16:12 2022

@author: Leonardo Falango
"""

# Importing
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
# all_skills = all_skills.dropna()
# 16122 after drop

ATTACKING = all_skills[['ST', 'LF', 'RF', 'RW', 'LW', 'CF']]
MIDDLE = all_skills[['LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM']]
DEFENDING = all_skills[['RCB', 'LCB', 'CB', 'LB', 'RDM', 'RB', 'RWB', 'LWB']]
GK = all_skills[['GKDiving', 'GKPositioning']]

name_positions = ['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
           'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB',
           'RB']

all_skills = all_skills.values
for i in range(len(name_positions)):
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

all_skills = pd.DataFrame(all_skills)
X = all_skills.iloc[:, :-1]
y = all_skills.iloc[:, -1:]
unicos = y['64'].unique()

