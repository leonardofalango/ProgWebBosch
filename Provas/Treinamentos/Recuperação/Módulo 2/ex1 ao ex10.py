# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 08:16:26 2022

@author: Leonardo Falango
"""

# =============================================================================
# Importando as libs
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os



# =============================================================================
# Exercício 1
# =============================================================================

df = pd.read_csv("csv/gols_pr.csv")
cwb = df[df['clube'] == 'coritiba']
atle = df[df['clube'] == 'athletico-pr']
parana = df[df['clube'] == 'parana']


plt.plot(cwb['ano'], cwb['gols_pro'], label= 'Coritiba', c='g', marker = 'o')
plt.plot(atle['ano'], atle['gols_pro'], label= 'Athlético', c='r', marker = 'o')
plt.plot(parana['ano'], parana['gols_pro'], label= 'Paraná', c='b', marker = 'o')


plt.yticks([30,40,50,60,70,80,90,100,110,120,130,140])
plt.xticks(cwb['ano'])
plt.grid(True)
plt.legend()


plt.show()



# =============================================================================
# Exercício 2
# =============================================================================

df = pd.read_csv('csv/tips.csv', sep=';', usecols=['day','total_bill'])
sat = df[df['day'] == 'Sat']
sun = df[df['day'] == 'Sun']
thur = df[df['day'] == 'Thur']
fri = df[df['day'] == 'Fri']

days = ['Sat', 'Sun', 'Thur', 'Fri']

plt.plot(days, [sat['total_bill'].sum(), sun['total_bill'].sum(), thur['total_bill'].sum(), fri['total_bill'].sum()],
                color = 'Blue', linewidth = 4, marker='o', linestyle='--')
plt.grid(True)
plt.show()



# =============================================================================
# Exercício 3
# =============================================================================


df = pd.read_csv('csv/train.csv')
df = df[df['Age'] > -99999]
ome = df[df['Sex'] == 'male']
muié = df[df['Sex'] == 'female']

plt.figure(figsize=(30,5))

plt.scatter(ome['PassengerId'],ome['Age'], color='b', label='Homens')
plt.scatter(muié['PassengerId'], muié['Age'], color='fuchsia', label='Mulheres')

plt.xlabel('PassengerId')
plt.ylabel('Idade')

plt.legend()
plt.show()


sns.catplot(x='Sex', y='Age', data=df, kind='swarm', hue='Sex', palette='hls')
plt.show()






# =============================================================================
# Exercício 4
# =============================================================================

plt.figure(figsize=(30,7))
plt.scatter(ome['PassengerId'],ome['Fare'], color='b')
plt.scatter(muié['PassengerId'], muié['Fare'], color='fuchsia')

plt.show()


sns.catplot(x='Sex', y='Fare', data=df, kind='swarm', hue='Sex', palette='hls')
plt.show()



# =============================================================================
# Exercício 5
# =============================================================================


df = pd.read_csv('csv/company_sales_data.csv')

produtos = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

meses = df['month_number']

for i in produtos:
    plt.plot(meses, df[i], linewidth=3, marker='o')
plt.grid(True)
plt.xticks(meses)
plt.show()




# =============================================================================
# Exercício 6
# =============================================================================

df = pd.read_csv('csv/dados.csv', encoding = 'latin-1')

bairros = pd.unique(df['bairro'])

quant = []

#bota = len(df[df['bairro']=='Botafogo'])
#Eu ia fazer manualmente, mas temos uma lista com os nomes dos bairros
for i in bairros:
    tam = len(df[df['bairro'] == i])
    quant.append(tam)




plt.plot(bairros, quant, linewidth=3, marker='o')
plt.show()




# =============================================================================
# Exercício 7
# =============================================================================

def quadrado(x):
    return x**2

def cubo(x):
    return x**3

x = np.linspace(-20,20,50000)

fig, eixo = plt.subplots(nrows=1, ncols=2)

eixo[0].plot(x, quadrado(x), color='b', linewidth=4)
eixo[0].set_title("f(x) = x²")

eixo[1].plot(x, cubo(x), color='r', linewidth=4)
eixo[1].set_title("g(x) = x³")

plt.show()



# =============================================================================
# Exercício 8
# =============================================================================


def f(x):
    y = 1/ (x+1)
    return y

x = np.linspace(-20,20,1000)

plt.plot(x,f(x),color='fuchsia')

plt.title("f(x) = 1/(x+1)")

plt.show()




# =============================================================================
# Exercício 9
# =============================================================================



def f(x):
    y = x**(1/2)
    return y

x = np.linspace(-20,20,1000)

plt.plot(x,f(x),color='fuchsia')

plt.title("f(x) = √x")






# =============================================================================
# Exercício 10
# =============================================================================




def f(x):
    y = x**(1/2)
    return y

def quadrado(x):
    return x**2

x = np.linspace(-40,40,50000)

fig, eixo = plt.subplots(nrows=1, ncols=2)

eixo[0].plot(x, quadrado(x), color='b', linewidth=4)
eixo[0].set_title("f(x) = x²")

eixo[1].plot(x, f(x), color='r', linewidth=4)
eixo[1].set_title("g(x) = √x")
plt.show()



