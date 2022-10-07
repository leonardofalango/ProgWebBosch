# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:05:29 2022

@author: Leonardo Falango
"""

#JOGO DA VELHA


import random as rd
from termcolor import colored
import sys





def recomeca():
    recomeca = input("Deseja jogar novamente? ")
    recomeca = recomeca.lower()
    if recomeca == "s" or recomeca == "sim" or recomeca == "yes" or recomeca == "y" or recomeca == '1':
        return 1
    elif recomeca == "n" or recomeca == "no" or recomeca == "não" or recomeca == "nao" or recomeca == '0':
        return 2
    else:
        return 0



#Definir a jogada do Player
def jogadaPlayer(xo, jogo):
    
    while True:
        try:
            lugar = int(input("Entre com a posição 1-9: "))
            lugar -=1
            if jogo[lugar] == " ":
                jogo[lugar] = xo
                return 1
            
            else:
                print("Jogada inválida, por favor escolha um lugar livre.")
        except ValueError:
            print("Entre com um inteiro")
            continue
        except IndexError:
            print(colored("1 - 9!!!!!","red"))
            continue
    
    
 
def jogadaMaquina(xo, jogo):
    while True:
        lugar = rd.randint(0, 8)
        if jogo[lugar] == " ":
            jogo[lugar] = xo
            return 1
            
        else:
            continue
 
 
 
 
 
    

def printJogo(m):
    print(f"\n\n\n\n  {m[0]}  |  {m[1]}  |  {m[2]}",
          "\n   ___________",
          f"\n  {m[3]}  |  {m[4]}  |  {m[5]}",
          "\n   ___________",
          f"\n  {m[6]}  |  {m[7]}  |  {m[8]}")
        




def compara(matrix):    # 0, 1, 2
#                         3, 4, 5
#                         6, 7, 8
    # if ((matrix[0] == matrix[1] == matrix[2]) and matrix[0] != " ") or ((matrix[3] == matrix[4] == matrix[5]) and matrix[0] != " ") or ((matrix[6] == matrix[7] == matrix[8]) and matrix[0] != " "):
    #     return 1
    #CASO O JOGO TENHA ACABADO!!! POREM, 0,1,2 --> 3,4,5 SAO SUCESSORES
    #Posicao 0,4,8 ou 2,4,6 ou seja, todas as posições pares
   
    for i in range(9):
        try:
            if (matrix[i] == matrix[i+1] and matrix[i+1] == matrix[i+2]) and (i == 0 or i == 3 or i == 6):
                if matrix[i] == "X":
                    return "X"
                elif matrix[i] == "O":
                    return "O"
                else:
                    continue
                
            elif matrix[0] == matrix[4] == matrix[8]:
                if matrix[0] == "X":
                        return "X"
                elif matrix[0] == "O":
                        return "O"
                else:
                        continue
            elif matrix[2] == matrix[4] == matrix[6]:
                if matrix[2] == "X":
                        return "X"
                elif matrix[2] == "O":
                        return "O"    
                else:
                        continue
                    
                
                
            elif(matrix[i] == matrix[i+3] == matrix[i+6])and (i == 0 or i == 1 or i == 2):
                if matrix[i] == "X":
                    return "X"
                elif matrix[i] == "O":
                    return "O"
                else:
                    continue      
        
        
        
        except IndexError:
            continue

def checkavelha(jogo):        
    for i in range(len(jogo)):
    
        if jogo[i] == " ":
                espaco = 1
                break
        else:
                espaco = 0
    if espaco == 0:
        return 0
        
                    
        



def score():
    global scoreJogador, scoreCpu
    print("-------PLACAR-------")
    print(f"JOGADOR: {scoreJogador} | CPU: {scoreCpu}")






scoreJogador = 0
scoreCpu = 0
def jogodavelha():
    global scoreJogador, scoreCpu
    
    jogo = [" "," "," "," "," "," "," "," "," "]
    comeca = rd.randint(1, 2) #1 = player começa 2 = maquina começa
    
    exemplo = [1,2,3,4,5,6,7,8,9]
    printJogo(exemplo)
   
    if comeca == 1:
        print("Você começa, você é 'X'")
        while True:
            jogadaPlayer("X", jogo)
            printJogo(jogo)
            acabou = compara(jogo)
            if acabou == "X":
                print(colored("Parabens, Você ganhou!",'green'))
                scoreJogador += 1
                break
            if checkavelha(jogo) == 0:
                print("Deu velha!")
                break
            jogadaMaquina("O", jogo)
            printJogo(jogo)
            acabou = compara(jogo)
            if acabou == "O":
                print(colored("Você perdeu!",'red'))
                scoreCpu += 1
                break
            
        score()
        
        a = recomeca()
        while a == 0:
            print("Valor inválido")
            a = recomeca()
        if a == 1:
            jogodavelha()
        else:
            print("Obrigado por jogar!")
            sys.exit()
                
            
                
    elif comeca == 2:
        print("CPU começa. Você é 'O'")
        while True:
            jogadaMaquina("X", jogo)
            printJogo(jogo)
            acabou = compara(jogo)
            if acabou == "X":
                print(colored("Você perdeu!",'red'))
                scoreCpu += 1
                break
            if checkavelha(jogo) == 0:
                print("Deu velha!")
                break
            jogadaPlayer("O", jogo)
            printJogo(jogo)
            acabou = compara(jogo)
            if acabou == "O":
                print(colored("Parabens, Você ganhou!",'green'))
                scoreJogador += 1
                break
            
        score()
        
        a = recomeca()
        while a == 0:
            print("Valor inválido")
            a = recomeca()
        if a == 1:
            jogodavelha()
        else:
            print("Obrigado por jogar!")
            sys.exit()
                
        
















jogodavelha()