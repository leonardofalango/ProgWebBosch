# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:21:16 2022

@author: Leonardo Falango
"""




def continuar():
    entrada = input("Digite 0 se quiser sair, para continuar, aperte enter.\n")
    if entrada == '0':
        print("Obrigado!")
    else:
        calculadora()







def calculadora():
    x = float(input("Entre com o valor de x: "))
    y  = float(input("Entre com o valor de y: "))
    opcao = int(input("Entre com a opção:\n(1) Soma\n(2) Subtração\n(3) Divisão\n(4) Multiplicação\n(0) Sair\n"))
    
    if opcao == 1:
        print(x+y)
        continuar()
        
    elif opcao == 2:
        print(x-y)
        continuar()
        
    elif opcao == 3:
        print(x/y)
        continuar()
        
    elif opcao == 4:
        print(x*y)
        continuar()
        
    elif opcao == 0:
        pass
    
    else:
        print("Valor inválido")
        continuar()

calculadora()

