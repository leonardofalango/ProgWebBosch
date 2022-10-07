# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:33:14 2022

@author: DISRCT
"""

def calculadora():
    x = float(input("Entre com o valor de x: "))
    y  = float(input("Entre com o valor de y: "))
    opcao = int(input("Entre com a opção:\n(1) Soma\n(2) Subtração\n(3) Divisão\n(4) Multiplicação"))
    if opcao == 1:
        print(x+y)
    elif opcao == 2:
        print(x-1)
    elif opcao == 3:
        print(x/y)
    elif opcao == 4:
        print(x*y)
    else:
        print("Valor inválido")
        calculadora()

calculadora()