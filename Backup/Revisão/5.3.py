# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:05:14 2022

@author: Leonardo Falango
"""

try:
    lim = int(input("Entre com o número limite: "))
    lista = []
    for i in range(lim):
        lista.append(i+1)
    soma = sum(lista)
    print(f"O valor total da soma é: {soma}")
except ValueError:
    print("O limite deve ser inteiro.")


