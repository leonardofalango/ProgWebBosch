3# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:05:29 2022

@author: Leonardo Falango
"""

#JOGO DA VELHA


import random as rd
from termcolor import colored
import sys


import cv2
import numpy as np






def recomeca():
    
    img = np.zeros((512,512,3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"Deseja jogar novamente?",(30,100),font,1.0,(255,255,255),1,cv2.LINE_AA)
    cv2.putText(img,"Esc para sair",(30,500),font,0.5,(255,255,255),1,cv2.LINE_AA)

    cv2.imshow('Play again?', img)
    recomeca = cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    recomeca = str(recomeca)
    if recomeca == "115" or recomeca == "121" or recomeca == "49" or recomeca == '13':
        return 1
    elif recomeca == "110" or recomeca == "48" or recomeca == "-1" or recomeca == "27":
        return 2
    else:
        return 0



#Definir a jogada do Player
def jogadaPlayer(xo, jogo):
    global valor_tecla,img, scoreCpu
    
    while True:
        try:
            lugar = int(inter(jogo,img,0))
            if  lugar in valor_tecla:
                lugar = valor_tecla.index(lugar)
            elif lugar == 110 or lugar == 48 or lugar == -1 or lugar == 27:
                scoreCpu +=1
                return 2
            else:
                int('a')
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
    
    
# No fácil a maquina joga apenas no aleatório
def jogadaMaquina(xo, jogo):
    global dif
    if dif == 1:
        while True:
            lugar = rd.randint(0, 8)
            if jogo[lugar] == " ":
                jogo[lugar] = xo
                return 1
                
            else:
                continue
    elif dif == 2:
        print("Travou man!")
 
 
 
 
 
    

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
    img = np.zeros((522,522,3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"-------PLACAR-------",(0,70),font,1.0,(255,255,255),3,cv2.LINE_AA)
    cv2.putText(img,f"JOGADOR: {scoreJogador} | CPU: {scoreCpu}",(0,150),font,1.5,(255,255,255),3,cv2.LINE_AA)
    
    cv2.imshow('Placar', img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    
    print("-------PLACAR-------")
    print(f"JOGADOR: {scoreJogador} | CPU: {scoreCpu}")







def jogodavelha():
    global scoreJogador, scoreCpu,img, dif
    img = np.zeros((512,512,3), np.uint8)
    jogo = [" "," "," "," "," "," "," "," "," "]
    comeca = rd.randint(1, 2) #1 = player começa 2 = maquina começa
    cv2.line(img, (150,0), (150,512),(255,255,255),5)
    cv2.line(img, (350,0), (350,512),(255,255,255),5)
    
    
    cv2.line(img, (0,150), (512,150),(255,255,255),5)
    cv2.line(img, (0,350), (512,350),(255,255,255),5)

    exemplo = [1,2,3,4,5,6,7,8,9]
    printJogo(exemplo)
    dif = int(input("Entre com a dificuldade:\n(1) - Fácil\n(2) - Difícil\n"))
   
    if comeca == 1:
        print("Você começa, você é 'X'")
        while True:
            x = jogadaPlayer("X", jogo)
            if x == 2:
                break
            printJogo(jogo)
            acabou = compara(jogo)
            if acabou == "X":
                print(colored("Parabens, Você ganhou!",'green'))
                scoreJogador += 1
                inter(jogo, img,1000)
                break
            if checkavelha(jogo) == 0:
                print("Deu velha!")
                inter(jogo,img,1000)
                break
            jogadaMaquina("O", jogo)
            printJogo(jogo)
            acabou = compara(jogo)
            if acabou == "O":
                print(colored("Você perdeu!",'red'))
                scoreCpu += 1
                inter(jogo,img,1000)
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
                inter(jogo,img,1000)
                break
            if checkavelha(jogo) == 0:
                print("Deu velha!")
                inter(jogo,img,1000)
                break
            x = jogadaPlayer("O", jogo)
            if x == 2:
                break
            printJogo(jogo)
            acabou = compara(jogo)
            if acabou == "O":
                print(colored("Parabens, Você ganhou!",'green'))
                scoreJogador += 1
                inter(jogo,img,1000)
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
                
        












#--------------------- FEZ O TABULEIRO ------------------#


# FUNCAO PARA PRINTAR AS POSICOES.
#for i in range(len(matrix)):
#    if i == 0:
#        local = (0,145)
#    if i == 1:
#        local = (170,145)
#    if i == 2:
#        local = (345,145)
#    if i == 3:
#        local = (0,340)
#    if i == 4:
#        local = (170,340)
#    if i == 5:
#        local = (345,340)
#    if i == 6:
#        local = (0, 511)
#    if i == 7:
#        local = (170, 511)
#    if i == 8:
#        local = (345, 511)
#        
#    cv2.putText(img, matrix[i], local, cv2.FONT_HERSHEY_SIMPLEX, 7,(255,255,255),5, cv2.LINE_AA)
#
#
#    cv2.imshow('Jogo da velha', img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()




def inter(matrix,img,x):
    for i in range(len(matrix)):
        if i == 0:
            local = (0,145)
        if i == 1:
            local = (170,145)
        if i == 2:
            local = (345,145)
        if i == 3:
            local = (0,340)
        if i == 4:
            local = (170,340)
        if i == 5:
            local = (345,340)
        if i == 6:
            local = (0, 511)
        if i == 7:
            local = (170, 511)
        if i == 8:
            local = (345, 511)
            
        cv2.putText(img, matrix[i], local, cv2.FONT_HERSHEY_SIMPLEX, 7,(255,255,255),5, cv2.LINE_AA)
    
    
    cv2.imshow('Jogo da velha', img)
    tecla = cv2.waitKey(x)
    cv2.destroyAllWindows()
    return tecla





valor_tecla = [55,56,57,52,53,54,49,50,51]

scoreJogador = 0
scoreCpu = 0


# VALORES DAS TECLAS
#1 = 49
#2 = 50
#.
#.
#.
#9 = 57


jogodavelha()