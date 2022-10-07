# -*- coding: utf-8 -*-
"""
Created on Fri May 13 08:14:00 2022

@author: Leonardo Falango
"""



# A segmentação de clientes é a subdivisão de um mercado em grupos distintos de clientes que compartilham características semelhantes. 
# A segmentação de clientes pode ser um meio poderoso para identificar necessidades insatisfeitas dos clientes.
# Usando os dados acima, as empresas podem superar a concorrência desenvolvendo produtos e serviços atraentes.
# Você está devendo um shopping de supermercado e por meio de cartões de associado, você tem alguns dados básicos sobre seus clientes como ID do cliente,
# idade, sexo, renda anual e pontuação de gastos. 
# Você quer entender os clientes como quem são os clientes-alvo para que o sentido possa ser dado à equipe de marketing e planejar a estratégia de acordo.


# O problema acima é um problema de clusterização
# Para resolvermos iremos usar o k-means e o DBSCAN

# Imports
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN



# Função de plot
def plot_clusters(x, y_pred):
    for i in range(1000):
        indexes = y_pred == i
        color = np.random.rand(3,)
        plt.scatter(x[indexes, 0], x[indexes, 1], s=100, color=color, label=f"Cluster {i}")
    plt.show()
# Função para gerar cores aleatórias para plottar
def rdcolor():
    return np.random.rand(3,)



# Criando o dataset
db = pd.read_csv('Dados/segmentation_data.csv')
db = db.iloc[:,1:] # Retirar ids, a id do cliente não influencia em nada.


# Arrumando o dataset e criando x e y
db = db.dropna()
x = db.iloc[:,:-1].values # Pegando todas as linhas do dataset e pegando todas as colunas menos a última
y = db.iloc[:, -1:].values # Pegando apenas a última coluna do dataset, mas com todas as linhas que ela possui

pca = PCA(n_components=2)
x = pca.fit_transform(x)


# Separando o x e y em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)


# Instanciando o k-means e o DBSCAN
# K-means
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=0) # O problema de usar o k-means, é precisar colocar qual o número de clusters
y_pred = kmeans.fit_predict(x_train, y_train) # Treinando o kmeans
y_pred_kmeans = kmeans.predict(x_test) # O predict tem que ser o mais próximo possível do y_test

# DBSCAN
dbscan = DBSCAN(eps=0.1, min_samples=2) # Você escolhe apenas a distancia do raio, para o dbscan separar os cluster
dbscan.fit(x_train, y_train) # Treinando o kmeans
y_pred_dbscan = dbscan.fit_predict(x_train) # O predict tem que ser o mais próximo possível do y_test



# Plotting
plot_clusters(x_train, y_pred)


dbscan = DBSCAN(eps=1, min_samples=2)
dbscan.fit(x)
y_pred = dbscan.fit_predict(x)
print(y_pred)
y_pred += 1
plot_clusters(x, y_pred)




