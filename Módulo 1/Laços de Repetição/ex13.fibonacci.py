# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:34:22 2022

@author: DISRCT
"""

def fibonacci(n):
    numeros = [0,1,1]
    anterior = numeros[1]
    atual = numeros[2]
    limite = n
    ind = 0
    while atual <= limite:
        aux = atual
        atual = atual+anterior
        anterior = aux
        numeros.append(atual)
        ind = ind + 1
        
    ind += 2
    numeros.pop(ind)
        
    return numeros





def fibo():
    fib = 1
    n = int(input("Entre com o limite: "))
    if n < 1:
        print("Valor inválido")
        fibo()
    elif n == 0:
        print("0")
    elif n == 1:
        print("[0, 1]")
    elif n == 2:
        print("[0, 1, 1]")
    else:
        fib = fibonacci(n)
        print(fib)
 
fibo()