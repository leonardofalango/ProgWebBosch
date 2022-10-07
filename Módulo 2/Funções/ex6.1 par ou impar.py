# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 08:16:07 2022

@author: Leonardo Falango
"""

import random as rd


score = 0
def parimpar():
    global score
    maquina = rd.randint(0, 10)
    print("=================================== PAR OU IMPAR =============================")
    try: 
        entrada = int(input("Entre com a opção\n(1) PAR\n(2) IMPAR\n"))
    except ValueError:
        print("ERRO. ENTRADA INVÁLIDA.")
        parimpar()
    
    if entrada == 1:
        try:
            print("="*7,"Você é Par.","="*7)
            usr = int(input("Entre com o número: "))
        except ValueError:
            print("ERRO. ENTRADA INVÁLIDA.")
            parimpar()
        
        if (maquina + usr) % 2 == 0:
            print(f"Opção da máquina: {maquina}")
            score += 1            
            print("VOCÊ GANHOU!")
            parimpar()
        else:
            print(f"Opção da máquina: {maquina}")
            print("VOCÊ PERDEU!")
            continuar = input("Deseja continuar?\nAperte Enter para continuar\nAperte 0 para SAIR\n")
            try:
                if int(continuar) == 0:
                    pass
                else:
                    score = 0
                    parimpar()
            except ValueError:
                score = 0
                parimpar()
                    
    
    
    elif entrada == 2:
        try:
            print("="*8,"Você é Impar.","="*8)
            usr = int(input("Entre com o número: "))
        except ValueError:
            print("ERRO. ENTRADA INVÁLIDA.")
            parimpar()
        
        if (maquina + usr) % 2 != 0:
            print(f"Opção da máquina: {maquina}")
            score += 1            
            print("VOCÊ GANHOU!")
            parimpar()
        else:
            print(f"Opção da máquina: {maquina}")
            print("VOCÊ PERDEU!")
            continuar = input("Deseja continuar?\nAperte Enter para continuar\nAperte 0 para SAIR")
            try:
                if int(continuar) == 0:
                    pass
                else:
                    score = 0
                    parimpar()
            except ValueError:
                score = 0
                parimpar()
                    
    elif entrada == 0:
        pass
    else:
        print("ERRO. ENTRADA INVÁLIDA.")
        parimpar()
    
    
parimpar()
print("FIM DE JOGO.")
print(f"Seu score foi de: {score}")