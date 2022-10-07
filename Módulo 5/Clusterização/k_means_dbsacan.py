# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:16:59 2022

@author: Leonardo Falango
"""

# Importando as libs
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import time

# Criando o dataset
n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None




'''=--==--==--==--==--==--==--==--==--==--==--==--= CIRCULOS =--==--==--==--==--==--==--==--==--==--==--==--='''
print('''=--==--==--==--==--==--==--==--==--==--==--==--= CIRCULOS =--==--==--==--==--==--==--==--==--==--==--==--=''')
"""____________________________________________ K-MEANS _____________________________________________________"""
# Testando a separação com o k-means
print("__ K-MEANS __")
# Testando a separação com o k-means")
x = noisy_circles[0]

tempo0 = time.time()
kmeans = KMeans(n_clusters=2, init="k-means++", random_state=0)
y_pred = kmeans.fit_predict(x)
print(kmeans.inertia_)
print(y_pred)

def plot_clusters(x, y_pred):
    for i in range(100):
        indexes = y_pred == i
        color = np.random.rand(3,)
        plt.scatter(x[indexes, 0], x[indexes, 1], s=100, color=color, label=f"Cluster {i}")
    plt.show()

plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))

"""____________________________________________ DBSCAN _____________________________________________________"""
tempo0 = time.time()
print("__ DBSCAN __")
# Testando a separação com o dbscan

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.2, min_samples=2)
dbscan.fit(x)
y_pred = dbscan.fit_predict(x)
print(y_pred)
y_pred += 1
plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))








'''=--==--==--==--==--==--==--==--==--==--==--==--= LUAS =--==--==--==--==--==--==--==--==--==--==--==--='''
print('''=--==--==--==--==--==--==--==--==--==--==--==--= LUAS =--==--==--==--==--==--==--==--==--==--==--==--=''')
"""____________________________________________ K-MEANS _____________________________________________________"""
# Testando a separação com o k-means

print("__ K-MEANS __")
x = noisy_moons[0]

tempo0 = time.time()
kmeans = KMeans(n_clusters=4, init="k-means++", random_state=0)
y_pred = kmeans.fit_predict(x)
print(kmeans.inertia_)
print(y_pred)

def plot_clusters(x, y_pred):
    for i in range(100):
        indexes = y_pred == i
        color = np.random.rand(3,)
        plt.scatter(x[indexes, 0], x[indexes, 1], s=100, color=color, label=f"Cluster {i}")
    plt.show()

plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))



"""____________________________________________ DBSCAN _____________________________________________________"""
tempo0 = time.time()
print("__ DBSCAN __")
# Testando a separação com o dbscan

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.25, min_samples=2)
dbscan.fit(x)
y_pred = dbscan.fit_predict(x)
print(y_pred)
y_pred += 1
plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))









'''=--==--==--==--==--==--==--==--==--==--==--==--= 3 MANCHAS =--==--==--==--==--==--==--==--==--==--==--==--='''
print('''=--==--==--==--==--==--==--==--==--==--==--==--= 3 MANCHAS =--==--==--==--==--==--==--==--==--==--==--==--=''')
"""____________________________________________ K-MEANS _____________________________________________________"""
# Testando a separação com o k-means
print("__ K-MEANS __")
x = blobs[0]

tempo0 = time.time()
kmeans = KMeans(n_clusters=3, init="k-means++", random_state=0)
y_pred = kmeans.fit_predict(x)
print(kmeans.inertia_)
print(y_pred)

def plot_clusters(x, y_pred):
    for i in range(100):
        indexes = y_pred == i
        color = np.random.rand(3,)
        plt.scatter(x[indexes, 0], x[indexes, 1], s=100, color=color, label=f"Cluster {i}")
    plt.show()

plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))



"""____________________________________________ DBSCAN _____________________________________________________"""
tempo0 = time.time()
print("__ DBSCAN __")
# Testando a separação com o dbscan

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=3)
dbscan.fit(x)
y_pred = dbscan.fit_predict(x)
print(y_pred)
y_pred += 1
plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))











'''=--==--==--==--==--==--==--==--==--==--==--==--= QUADRADÃO  =--==--==--==--==--==--==--==--==--==--==--==--='''
print('''=--==--==--==--==--==--==--==--==--==--==--==--= QUADRADÃO  =--==--==--==--==--==--==--==--==--==--==--==--=''')
"""____________________________________________ K-MEANS _____________________________________________________"""
# Testando a separação com o k-means
print("__ K-MEANS __")
x = no_structure[0]

tempo0 = time.time()
kmeans = KMeans(n_clusters=4, init="k-means++", random_state=0)
y_pred = kmeans.fit_predict(x)
print(kmeans.inertia_)
print(y_pred)

def plot_clusters(x, y_pred):
    for i in range(100):
        indexes = y_pred == i
        color = np.random.rand(3,)
        plt.scatter(x[indexes, 0], x[indexes, 1], s=100, color=color, label=f"Cluster {i}")
    plt.show()

plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))



"""____________________________________________ DBSCAN _____________________________________________________"""
tempo0 = time.time()
print("__ DBSCAN __")
# Testando a separação com o dbscan

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.03, min_samples=3)
dbscan.fit(x)
y_pred = dbscan.fit_predict(x)
print(y_pred)
y_pred += 1
plot_clusters(x, y_pred)

print("Para separação dos círculos, o tempo foi de: {}".format(time.time()- tempo0))
