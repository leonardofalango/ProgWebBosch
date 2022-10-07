# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:33:22 2022

@author: Leonardo Falango
"""

# Carregar Pacotes

#import io
#import sklearn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Ignorar warnings
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("iris.csv", header=0)
#df.head() # Tamanho ta setosa, pétala,classe

x= df.iloc[:,:-1]
y= df.iloc[:, -1]


labels=["Setosa", "Versicolor", "Virginica"]
print("Tamanho do Dataset Completo {} amostras".format(len(x)))
print("{} {} amostras, {} {} amostras, {} {} amostras".format(
        labels[0], y.value_counts()[0],
        labels[1], y.value_counts()[1],
        labels[2], y.value_counts()[2]))


#Definindo os x's e y's de treino
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=9, shuffle=True)


from sklearn import svm

model = svm.LinearSVC(max_iter=100000000, random_state=0)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(y_pred) #Printando a previsão



#Agora precisamos fazer o mapa de confusão
from sklearn.metrics import confusion_matrix #Importando a matrix de confusão

cm = confusion_matrix(y_test, y_pred) #Criando a matrix de confusão
SetosaVer, SetosaFal, SetosaFalsa, VersicolorFal, VersicolorVer, VersicolorFalsa, VirginicaFal, VirginicaFalsa, VirginicaVer = cm.ravel() #Contagem de observações


# Visualização da Matriz de Confusão
group_names = ['TrueSetosa','FalseSetosa','FalseSetosa','FalseVersicolor', 'TrueVersicolor', 'FalseVersicolor', 'FalseVirginica', 'FalseVirginica', 'TrueVirginica']
group_counts = ['{0:0.0f}'.format(value) for value in
                cm.flatten()]
group_percentages = ['{0:.2%}'.format(value) for value in
                     cm.flatten()/np.sum(cm)]
labels = [f'{v1}\n{v2}\n{v3}' for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(3,3)


import seaborn

seaborn.heatmap(cm, annot=labels, fmt='', cmap='Blues', cbar=False)

print("Confusion Matrix : ")


listaTrue = [SetosaVer, VersicolorVer, VirginicaVer]
listaTotal = [SetosaVer, SetosaFal, SetosaFalsa, VersicolorVer, VersicolorFal, VersicolorFalsa, VirginicaVer, VirginicaFal, VirginicaFalsa]

accuracy = (sum(listaTrue))/(sum(listaTotal))
print("Acurácia de {0:0.2f}%".format(accuracy*100))
     
precision = (SetosaVer)/(SetosaVer+SetosaFal+SetosaFalsa) #É uma precisão para apenas uma das classes
print("Precisão de Setosas: {0:0.0f}%".format(precision*100))

recall = (SetosaVer)/(SetosaVer+SetosaFal+SetosaFalsa)
print("Recall de Setosas: {0:0.2f}%".format(recall*100))

f1 = (2*precision*recall)/(recall+precision)
print("F1 - Score de {0:0.2f}%".format(f1*100))

#Destravando o plot com o matplotlib
from matplotlib.pyplot import show
show()


cm_per = []
#Fazendo o mapa de calor
#Fazendo o vetor como porcentagem
for i in range(len(cm)):
    cm_per = cm/sum(cm)
seaborn.heatmap(data=cm_per, cmap='mako_r')








