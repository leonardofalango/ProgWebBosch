# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:36:20 2022

@author: Leonardo Falango
"""

cardapio = {"hamburguer" : 10, "hotdog": 6.5, "salada" : 4, "suco" : 4, "refrigerante":4.5, "água":2}
print(f"Menu FastFood\n{cardapio}")
entrada = input("Digite a comida que você deseja: ")
entrada1 = input("Digite a bebida que você deseja: ")
entrada = entrada.lower()
entrada1 = entrada1.lower()
try:
    print(f'O valor total é de: {cardapio[entrada] + cardapio[entrada1]}')
except KeyError:
    print("Não possuimos isso no cardapio")
