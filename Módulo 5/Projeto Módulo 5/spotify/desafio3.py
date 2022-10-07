# -*- coding: utf-8 -*-
"""
Created on Fri May 20 08:08:20 2022

@author: Leonardo Falango
"""

import pandas as pd
import numpy as np
from  sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



df = pd.read_csv('data.csv')
df = df.dropna()

df = df.iloc[:, :2500]

df = df[['year','danceability','liveness','tempo','speechiness','duration_ms','popularity']]

X = df.iloc[:, :-1]
y = df.iloc[:, -1:]
y = np.ravel(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0, test_size=0.25)


knn = KNeighborsClassifier()
dct = DecisionTreeClassifier()
rfr = RandomForestClassifier()


names = ['KNeighbors Classifier', 'Decision Tree', 'Random Forest']
models = [knn, dct, rfr]


tests = []
for model in models:
    model.fit(X_train, y_train)
    tests.append(model.predict(X_test))

for i in range(len(names)):
    print('_'*80)
    print(f"Model: {names[i]}")
    print("Accuracy: {}".format(accuracy_score(y_test,tests[i])))