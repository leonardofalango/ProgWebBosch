# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:38:23 2022

@author: Leonardo Falango
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv/alunos.csv")
media = 6
aprov = df[df['Aprovado'] == True]
reprov = df[df['Aprovado'] == False]


plt.pie([len(aprov),len(reprov)],labels=["Aprovados", 'Reprovados'], autopct='%0.02f%%')
plt.show()

