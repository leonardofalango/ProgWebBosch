# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:15:13 2022

@author: Leonardo Falango
"""


def fatorial(x):
    lista = []
    fatorial = 1
    fat = x
    while fat > 1:
        lista.append(fat)
        fat -= 1
    for i in range(len(lista)):
        numero = lista[i]
        fatorial = fatorial * numero
    print(f"O fatorial de {x} = {fatorial}")
    return x # CASO QUEIRA FAZER CONTAS

def inverso(x):
    print(f"O inverso de {x} = {1/x}")
    return x # CASO QUEIRA FAZER CONTAS

def quadrado(x):
    print(f"O quadrado de {x} = {x*x}")
    return x*x

def raiz(x):
    print(f"A raiz quadrada de {x} = {x**0.5}")
    return x** 0.5








def operacoes(x):
    if x < 0:
        print("Impossivel realizar as operações.")
    else:
        fatorial(x)
        inverso(x)
        quadrado(x)
        raiz(x)







while True:
    try:
        entrada = float(input("Entre com o número: "))
    except ValueError:
        print("Erro. Digite um número.")
        continue
    operacoes(entrada)

    