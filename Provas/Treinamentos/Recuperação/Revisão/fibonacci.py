# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:07:47 2022

@author: Leonardo falango
"""

def fib(n):
    numero = 1
    lista = [1]
    num = 0
    if n == 1:
        return lista
        pass
    elif n == 2:
            return 1,1
    else:
        for i in range(n-1):
            fib = numero + num
            num = numero
            numero = fib        
            lista.append(fib)
        return lista
            
            
def fibonacci(n):
    numeros = [1,1]
    anterior = numeros[0]
    atual = numeros[1]
    limite = n
    ind = 0
    while atual <= limite:
        aux = atual
        atual = atual+anterior
        anterior = aux
        numeros.append(atual)
        ind = ind + 1
        
    ind += 1
    numeros.pop(ind)
        
    return numeros


