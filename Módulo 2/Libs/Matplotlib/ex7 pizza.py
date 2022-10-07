# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:57:17 2022

@author: Leonardo Falango
"""


import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('company_sales_data.csv')

#Função de pizza = plt.pie()

# .axis('equal') para garantir que o gráfico sja um pizza

x = 'facecream facewash toothpaste bathingsoap shampoo moisturizer'
lista_produtos = x.split(' ') #preguiça de escrever todos os terecoteco que tem

# soma_facecream = df[lista_produtos[0]].sum() ##Fazendo sem laços de repetição

# soma_facewash = df[lista_produtos[1]].sum()

# pizza = plt.pie([soma_facecream, soma_facewash], labels=['facecream','facewash'])

produtostotal = []

for i in range(len(lista_produtos)):
    produtostotal.append(df[lista_produtos[i]].sum())


plt.figure(figsize=(8,10))
pizaa = plt.pie(produtostotal, labels=lista_produtos, autopct='%1.1f%%')
plt.legend(loc='lower right')
