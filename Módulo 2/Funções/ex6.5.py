# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:22:51 2022

@author: Leonardo Falango
"""
import random as rd



limin = int(input("Entre com o valor limite mínimo: "))

limax = int(input("Entre com o valor limite máximo: "))

tamanho = int(input("Entre com o tamanho: "))

lista = []

for i in range(tamanho):
    numero = rd.randint(limin, limax)
    lista.append(numero)
       
print(f"LISTA: {lista}")            
    
for i in range(len(lista)):
    menor = lista[i]
    for j in range(i+1,len(lista)):
        if menor > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            menor = lista[i]
    

    
print(f"Lista ordenada: {lista}")   