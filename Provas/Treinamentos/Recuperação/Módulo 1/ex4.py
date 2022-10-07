# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:01:59 2022

@author: Leonardo Falango
"""
import random as rd

lista = []
listapar = []
listaimpar = []
listafinal = []

for i in range(15):
    lista.append(rd.randint(0,9))

for i in range(len(lista)):
    if len(listapar) == 5:
        print(listapar)
        listapar.clear()
    
    if len(listaimpar) == 5:
        print(listaimpar)
        listaimpar.clear()
    
    
    if lista[i] % 2 == 0:
        listapar.append(lista[i])
    else:
        listaimpar.append(lista[i])
print(f"Vetores incompletos:\n{listapar}\n{listaimpar}")

