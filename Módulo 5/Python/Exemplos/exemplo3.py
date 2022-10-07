# -*- coding: utf-8 -*-
"""
Created on Mon May  2 08:40:09 2022

@author: Leonardo Falango
"""

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing

database = { 'Tempo' : ['Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso', 'Chuvoso', 'Chuvoso', 'Nublado', 'Ensolarado', 'Ensolarado', 'Chuvoso'],
            'Humidade' : ['Alta', 'Alta', 'Alta', 'Alta', 'Normal', 'Normal', 'Normal', 'Alta', 'Normal', 'Normal'],
            'Vento' : ['Fraco', 'Forte', 'Fraco', 'Fraco', 'Fraco', 'Forte', 'Forte', 'Fraco', 'Fraco', 'Fraco'],
            'Treinou' : ['Não', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Sim']}


db = pd.DataFrame(database)

#Criando o LabelEncoder
tempo_lbencoder = preprocessing.LabelEncoder()
humidade_lbencoder = preprocessing.LabelEncoder()
vento_lbencoder = preprocessing.LabelEncoder()
treinou_lbencoder = preprocessing.LabelEncoder()

#Usando o LabelEncoder para atribuir números as variáveis qualitativas
tempo_lbencoder.fit(db["Tempo"].unique())
humidade_lbencoder.fit(db["Humidade"].unique())
vento_lbencoder.fit(db["Vento"].unique())
treinou_lbencoder.fit(db["Treinou"].unique())


db["Tempo"] = tempo_lbencoder.transform(db["Tempo"])
db["Humidade"] = humidade_lbencoder.transform(db["Humidade"])
db["Vento"] = vento_lbencoder.transform(db["Vento"])
db["Treinou"] = treinou_lbencoder.transform(db["Treinou"])

#Separando a nossa database nos atributos previsores e na classe objetivo
previsor = db[["Tempo", "Humidade", "Vento"]]
classe = db["Treinou"]

#Criando o classificado NaiveBayes
gnb = GaussianNB()
gnb.fit(previsor, classe)

#Verificando a precisão
print(f"Precisao: {gnb.score(previsor, classe)*100}%")


#Inserindo novos dados para serem previstos
previsao = {"Tempo" : ['Ensolarado', 'Nublado', 'Nublado', 'Chuvoso'],
            "Humidade" : ['Normal', 'Alta', 'Normal', 'Alta'],
            "Vento" : ['Forte', 'Forte', 'Fraco', 'Forte']}
previsao = pd.DataFrame(previsao)

previsao["Tempo"] = tempo_lbencoder.transform(previsao["Tempo"])
previsao["Humidade"] = humidade_lbencoder.transform(previsao["Humidade"])
previsao["Vento"] = vento_lbencoder.transform(previsao["Vento"]) 
#Printando o resultado

print(gnb.predict(previsao))
print(treinou_lbencoder.inverse_transform(gnb.predict(previsao)))
print(gnb.predict_proba(previsao))


