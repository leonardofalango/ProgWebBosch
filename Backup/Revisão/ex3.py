# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:59:18 2022

@author: Leonardo Falango
"""

nome = input("Entre com seu nome completo com letras minúsculas: ")
nome = nome.lower()
nome = nome.split(' ')
tam = len(nome)

for i in range(tam):
    nome[i] = nome[i][0].upper() + nome[i][1:]
nome = ' '.join(nome)
print(nome)
print(f'Seu nome possui {len(nome) - tam} caracteres')



# =============================================================================
# Temos tambem a opção de usar o .capitalize
# =============================================================================
nome = nome.lower()
nome = nome.split(' ')
for i in range(len(nome)):
    nome[i] = nome[i].capitalize()
nome = ' '.join(nome)
print(nome)



# =============================================================================
# Temos tambem a opção de usar o .title()
# =============================================================================

nome = nome.lower()
nome = nome.title()
print(nome)


