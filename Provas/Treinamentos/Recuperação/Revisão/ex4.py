# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:22:33 2022

@author: Leonardo Falango
"""


lista = []

for i in range(10):
    try: 
        x = float(input(f"Valor {i+1}: "))
        lista.append(x)
    except ValueError:
        print('Entre apenas com números')
        continue
lista = sorted(lista)
print(f"Tamanho da lista: {len(lista)}\n{lista}")

