6# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:28:31 2022

@author: Leonardo Falango
"""

#s = 1+1/2+1/4
def s(termos):
    s = 0
    soma = 1
    for i in range(termos):
        if not s==0:
            soma += 1/s        
        s+=2                
    return soma


try:
    entrada = int(input("Insira o número de termos desejado: "))
    print(s(entrada))
except ValueError:
    print("Entre com números inteiros.")
