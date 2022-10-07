# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 08:51:06 2022

@author: Leonardo Falango
"""

from termcolor import colored
import random as rd
import sys
import time

dinheiro = 500
baralho = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]
naipes = ["♦️", "♠", "♥", "♣"]






def checkcards(card,naip):
    global cartas_usuario,cartas_banca,baralho,naipe,carta,naipe
    
    for i in range(len(cartas_usuario)):
        if baralho[card]+naipes[naip] == cartas_usuario[i]:
            return 0
    for i in range(len(cartas_banca)):
           if baralho[card]+naipes[naip] == cartas_banca[i]:
               return 0
    return 1
                
    
    
def saiu():
    global dinheiro
    print(f"Você volta pra casa com R${dinheiro}")
    sys.exit()
    




def confirmar():
    global dinheiro, aposta
    print(colored("","white"))
    entrada = input(f"Você tem certeza que deseja jogar?\nVocê tem R${dinheiro}\n")
    entrada = entrada.lower()
    if entrada == "s" or entrada == "sim" or entrada == "1" or entrada == "y" or entrada == "yes":
        confirmacao = True
    elif entrada == "n" or entrada == "nao" or entrada == "não" or entrada == "no" or entrada == "0":
        saiu()
    else:
        confirmacao = False
    return confirmacao
   
    
def perdeu():
    global dinheiro, aposta
    print(colored("Você perdeu!","red"))
    dinheiro = dinheiro - aposta
    if dinheiro == 0:
        print(colored("PARABENS, VOCÊ PERDEU TODO SEU DINHEIRO","red"))
        sys.exit()


def ganhou(vitoria):
    global dinheiro, aposta
    print(colored(f"{vitoria}! Você ganhou!", "green"))
    dinheiro += aposta

        

def verificar(soma_banca, soma_usuario, cartas_banca, cartas_usuario):
    if sum(soma_banca) + len(soma_banca) > sum(soma_usuario) + len(soma_usuario):
        return 0
    elif sum(soma_banca) + len(soma_banca) < sum(soma_usuario) + len(soma_usuario):
        return 1
    else:
        return 2




def blackjack():
    global dinheiro, baralho, aposta, naipes, cartas_usuario, cartas_banca, naipe, carta
    if confirmar():
        try:
            aposta = float(input("Qual sua aposta? "))
        except ValueError:
            print("Valor inválido")
            blackjack()
            
        if (dinheiro - aposta) < 0:
            print("Você não tem esse dinheiro.")
            blackjack()
        elif aposta <= 0:
            print("Valor inválido")
            blackjack()
            
        cartas_usuario = []
        cartas_banca = []
        soma_usuario = []
        carta = rd.randint(0,12)
        naipe = rd.randint(0, 3)
                
        cartas_usuario.append(baralho[carta] + naipes[naipe])
        
        if carta > 9:
            carta = 9
        soma_usuario.append(carta)#ESCOLHER AS CARTAS DO USR
        
        carta = rd.randint(0,12)
        naipe = rd.randint(0, 3)
        
        while checkcards(carta, naipe) == 0:
            carta = rd.randint(0,12)
            naipe = rd.randint(0, 3)
        
        cartas_usuario.append(baralho[carta]+naipes[naipe])
        if carta > 9:
             carta = 9
        soma_usuario.append(carta)
        
        
        somauser = sum(soma_usuario) + 2
        
        
        print(f"Suas cartas: {cartas_usuario}     Soma: {somauser}")
        
        
        
        
        
        soma_banca = []
        
        carta = rd.randint(0,12)
        naipe = rd.randint(0, 3)
        
        while checkcards(carta, naipe) == 0:
            carta = rd.randint(0,12)
            naipe = rd.randint(0, 3)
        
        cartas_banca.append(baralho[carta]+naipes[naipe])
        if carta > 9:
            carta = 9
        soma_banca.append(carta)#ESCOLHER AS CARTAS DA BANCA
        
        
        print(f"Carta da banca: {cartas_banca}")
        
        
#        carta = rd.randint(0,12)
#        naipe = rd.randint(0, 3)
#        
#        
#        while checkcards(carta, naipe) == 0:
#            carta = rd.randint(0,12)
#            naipe = rd.randint(0, 3)
#        
#        
#        cartas_banca.append(baralho[carta]+naipes[naipe])
#        
#        if carta > 9:
#            carta = 9
#        soma_banca.append(carta)
#        somabanc = sum(soma_banca) + 2
        
        
        
        
        ## USUARIO
        while True:
            if cartas_usuario[0] == baralho[0] and cartas_usuario[1] == baralho[12]: #GANHA INSTANTANEAMENTE
                ganhou("BLACKJACK")
                blackjack()
            elif sum(soma_usuario) + len(soma_usuario) > 21:
                perdeu()
                blackjack()
            
            elif sum(soma_usuario) + len(soma_usuario) == 21:
                ganhou("21")
                blackjack()
            else:
                entrada = input("Deseja mais um hit?(s/n): ")
                entrada = entrada.lower()
                if entrada == "s" or entrada == "sim" or entrada == "1" or entrada == "y" or entrada == "yes":
                    
                    carta = rd.randint(0,12)
                    naipe = rd.randint(0, 3)
                    
                    while checkcards(carta, naipe) == 0:
                        carta = rd.randint(0,12)
                        naipe = rd.randint(0, 3)
                    
                    cartas_usuario.append(baralho[carta]+naipes[naipe])
                    
                    if carta > 9:
                        carta = 9
                    soma_usuario.append(carta)
                    somauser = sum(soma_usuario) + len(soma_usuario)
                    
                    print(f"Suas cartas: {cartas_usuario}     Soma: {somauser}")
                    time.sleep(1)
                else:
                    break
        
    
        somabanc = sum(soma_banca) + len(soma_banca)
        ## BANCA
        while somabanc < 17:
            
            carta = rd.randint(0,12)
            naipe = rd.randint(0, 3)
            
            while checkcards(carta, naipe) == 0:
                carta = rd.randint(0,12)
                naipe = rd.randint(0, 3)
            
            cartas_banca.append(baralho[carta]+naipes[naipe])
            
            if carta > 9:
                carta = 9
            soma_banca.append(carta)
            somabanc = sum(soma_banca) + len(soma_banca)
            
            print(f"Cartas da banca: {cartas_banca}   Soma: {somabanc}")
            time.sleep(1)
        
        time.sleep(1)
        if somabanc > 21:
            ganhou("Parabéns")
            print(colored(f"\nSuas cartas: {cartas_usuario}   Soma: {somauser} \nJogo da banca: {cartas_banca}   Soma: {sum(soma_banca) + len(soma_banca)}","green"))
            blackjack()
        concl = verificar(soma_banca, soma_usuario, cartas_banca, cartas_usuario)
        if concl == 1:
            ganhou("Parabéns")
            print(colored(f"\nSuas cartas: {cartas_usuario}   Soma: {somauser} \nJogo da banca: {cartas_banca}   Soma: {sum(soma_banca) + len(soma_banca)}","green"))
            blackjack()
        elif concl == 2:
            print("\nEMPATE!!!")
            print(f"\nSuas cartas: {cartas_usuario}   Soma: {somauser} \nJogo da banca: {cartas_banca}   Soma: {sum(soma_banca) + len(soma_banca)}")
            blackjack()
        elif concl == 0:
            perdeu()
            print(colored(f"\nSuas cartas: {cartas_usuario}   Soma: {somauser} \nJogo da banca: {cartas_banca}   Soma: {sum(soma_banca) + len(soma_banca)}", "red"))
            blackjack()
    else:
        blackjack()
            
blackjack()      

    
    
