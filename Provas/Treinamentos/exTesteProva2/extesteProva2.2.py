# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:19:45 2022

@author: Leonardo Falango
"""

import matplotlib.pyplot as plt
import numpy as np


'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- EX 1 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''

x = np.linspace(-3,3,num=1000,endpoint=True) # Para criar 1000 pontos entre -3 e 3

def seno(x):
    seno = np.sin(x)
    return seno
def cos(x):
    cos = np.cos(x)
    return cos
def tan(x):
    tan = np.tan(x)
    return tan



plt.plot(x, seno(x), c='r', label='Seno')
plt.plot(x, cos(x), c='b', label='Cosseno')
plt.plot(x, tan(x), c='y', label='Tangente')
plt.title('Funções Trigonométricas')
plt.axis([-3,3,-40,40])
plt.legend()
plt.show()





'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- EX 2 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''


fig, eixo = plt.subplots(nrows=4, ncols=1, figsize=(12,12), sharex= True, sharey=True)

eixo[0].plot(x, seno(x), c='r', label='Seno')
eixo[0].plot(x, cos(x), c='b', label='Cosseno')
eixo[0].plot(x, tan(x), c='y', label='Tangente')
eixo[0].set_title('Funções Trigonométricas')



eixo[1].plot(x, seno(x), c='r')
eixo[1].set_title('Seno')



eixo[2].plot(x, cos(x), c='b')
eixo[2].set_title('Cosseno')

eixo[3].plot(x, tan(x), c='y')
eixo[3].set_title('Tangente')

plt.axis([-3,3,-40,40])
plt.show()


'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- EX 3 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''


import pandas
                                            # NAO SEI PQ, MAS O STACKOVERFLOW MANDOU
df = pandas.read_csv('Dados/cidades.csv', encoding=('latin-1'),usecols=['cidade','area'], sep=',')

df = df.sort_values(by='area')

df = df.head(5)

plt.pie(df['area'],labels=df['cidade'],autopct='%1.1f%%')
plt.axis('equal')
plt.show()

















