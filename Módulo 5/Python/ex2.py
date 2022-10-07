# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:34:27 2022

@author: Leonardo Falango
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

df = {"Idades" : [14.0, 17.0, 18.0, 15.0, 15.0, 16.0, 17.0, 15.0, 16.0, 16.0, 15.0, 17.0, 15.0, 16.0, 16.0, 18.0, 19.0, 17.0, 16.0, 17.0, 15.0, 16.0, 17.0, 17.0, 19.0, 20.0, 18.0, 17.0, 16.0, 15.0, 16.0, 16.0, 17.0, 18.0, 18.0, 17.0, 17.0, 15.0, 16.0, 16.0, 15.0]}
df = pd.DataFrame(df)

# calculando média e desvio padrao

desvio_padrao = df.std()
media = df.mean()

print(f'{desvio_padrao}\n{media}')

#Plotando a curva de distribuição normal
dominio = np.linspace(np.min(df['Idades']), np.max(df['Idades']))
plt.plot(dominio, norm.pdf(dominio, media, desvio_padrao))
plt.show()

#Plotando o box plot
df.boxplot(grid=False)
plt.show()
df.hist(grid=False)
plt.show()