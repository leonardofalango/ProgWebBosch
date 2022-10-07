# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:14:30 2022

@author: Leonardo Falango
"""


lista =[]
resposta = 's'



while True:
    try:
        n = int(input("Digite um valor: "))
        lista.append(n*2)
        print(lista)
        resposta = input("Deseja continuar? ")
        if resposta == "n":
            break
        elif resposta == "s":
            continue
        else:
            int('')
        
    except ValueError:
        print("Valor invalido")
        resposta = input("Deseja continuar? ")
        if resposta == "n":
            break
        elif resposta == "s":
            continue
        else:
            int('')
        