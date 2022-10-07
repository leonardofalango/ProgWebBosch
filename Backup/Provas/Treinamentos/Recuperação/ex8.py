# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:27:58 2022

@author: Leonardo Falango
"""


lista = [ [2,4,6,8], [1,3,5,7,9], [10,11,12,13,14], [15,16,17,18,19]] 
multi = 1
soma = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        soma += lista[i][j]
        multi = multi * lista[i][j]
print(f"Lista:{lista}\nSoma: {soma}\nMultiplicação: {multi}")

#for i in lista:
#    for j in i:
#        soma+=j
#        multi=mult*j


