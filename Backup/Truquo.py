# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:23:01 2022

@author: Leonardo Falango
"""

import random as rd
import time
#from termcolors import colored

 #  ____                         _           _                      
 # |  _ \                       (_)         | |                     
 # | |_) | ___ _ __ ___   __   ___ _ __   __| | ___     __ _  ___   
 # |  _ < / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \   / _` |/ _ \  
 # | |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) | | (_| | (_) | 
 # |____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/   \__,_|\___/  
 #             _______ _____  _    _  _____ ____                    
 #            |__   __|  __ \| |  | |/ ____/ __ \                   
 #               | |  | |__) | |  | | |   | |  | |                  
 #               | |  |  _  /| |  | | |   | |  | |                  
 #               | |  | | \ \| |__| | |___| |__| |                  
 #               |_|  |_|  \_\\____/ \_____\____/                   
     
 
 
dinheiro = 'Não Faça apostas no Truco! :)'
baralho = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
naipes = ["♦", "♠", "♥", "♣"]
wait = time.sleep(0.25)


def givecards(x):
    global baralho, naipes, all_cards
    cartas = []
    for i in range(x):
        carta = baralho[rd.randint(0,9)]
        naipe = naipes[rd.randint(0, 3)]
        while carta+naipe in all_cards: # Verificando se tem carta repetida
            carta = baralho[rd.randint(0, 9)]
            naipe = naipes[rd.randint(0, 3)]
        all_cards.append(carta+naipe)
        cartas.append(carta+naipe)
    return cartas
    










def init():
    global baralho, naipes, cartas_player, cartas_bot, all_cards, mesa, vira, rodada
    all_cards = []
    rodada = []
    cartas_player = givecards(3)
    cartas_bot = givecards(3)
    vira = givecards(1)
    mesa = [vira[0]]
    for i in '♦♠♥♣EMBARALHANDO♦♠♥♣':
        print(i)
        time.sleep(0.25)




def compara(pessoa):
    global baralho, naipes, cartas_player, cartas_bot, all_cards, mesa, vira
    if pessoa == 'player':
        manilha = baralho.index(mesa[0][0])

        jogo = []
        
        for i in range(len(mesa)):
            jogo.append(baralho.index(mesa[i][0]))
            
        if manilha == 9:
            manilha = 0
        else:
            manilha += 1
        
        if manilha in jogo:
            if jogo[1] == manilha and jogo[2] != manilha:
                return 1
            elif jogo[2] == manilha and jogo[1] != manilha:
                return 0
            elif jogo[1] == manilha and jogo[2] == manilha:
                if naipes.index(mesa[1][1]) > naipes.index(mesa[2][1]):
                    return 1
                else:
                    return 0
        else:
            p1 = mesa[1][0]
            b1 = mesa[2][0]
            if baralho.index(p1) > baralho.index(b1):
                return 1
            elif baralho.index(p1) < baralho.index(b1):
                return 0
            else:
                return 2
            
            
            
    if pessoa == 'bot':
        manilha = baralho.index(mesa[0][0])
        jogo = []
        for i in range(len(mesa)):
            jogo.append(baralho.index(mesa[i][0]))
        if manilha == 9:
            manilha = 0
        else:
            manilha += 1
        
        if manilha in jogo:
            if jogo[1] == manilha and jogo[2] != manilha:
                return 0
            elif jogo[2] == manilha and jogo[1] != manilha:
                return 1
            elif jogo[1] == manilha and jogo[2] == manilha:
                if naipes.index(mesa[1][1]) > naipes.index(mesa[2][1]):
                    return 0
                else:
                    return 1
        else:
            p1 = mesa[1][0]
            b1 = mesa[2][0]
            if baralho.index(p1) > baralho.index(b1):
                return 0
            elif baralho.index(p1) < baralho.index(b1):
                return 1
            else:
                return 2
    
                
            
        




def torna(pessoa):
    global baralho, naipes, cartas_player, cartas_bot, all_cards, mesa, vira, rodada
    if len(rodada) >= 2:
        if rodada[0] == rodada[1] and rodada[0] != 2:
            time.sleep(0.5)
            return rodada
        elif rodada[0] == rodada[1] and rodada[0] == 2:
            torna("player")
        elif rodada[0] == 2 and rodada[1] != 2:
            time.sleep(0.5)
            return rodada
        elif rodada[1] == 2 and rodada[0] != 2:
            time.sleep(0.5)
            return rodada

    elif len(rodada) == 3:
        if rodada[2] == 2:
            time.sleep(0.5)
            return rodada
    
    if len(cartas_bot) == 0:
        time.sleep(0.5)
        return rodada
    
    
    mesa = mesa[:1]
    
    
    if pessoa == 'player':
        print(f"\nMesa: {mesa}\n\nSua mão: {cartas_player}")
        entrada = int(input())
        entrada -= 1
        jogada = cartas_player[entrada]
        mesa.append(jogada)
        all_cards.append(jogada)
        jogada1 = cartas_bot[rd.randint(0,len(cartas_bot)-1)]
        mesa.append(jogada1)
        all_cards.append(jogada1)
        ganhou = compara('player')
        
        cartas_player.pop(cartas_player.index(jogada))
        cartas_bot.pop(cartas_bot.index(jogada1))
        time.sleep(0.25)
        print("Mesa: {}".format(mesa))
        
        if ganhou == 1:
            print("Você venceu a rodada!")
            rodada.append(ganhou)
            torna("player")
        elif ganhou == 0:
            print("Você perdeu a rodada!")
            rodada.append(ganhou)
            torna("bot")
        elif ganhou == 2:
            print("Embuxou!")
            rodada.append(ganhou)
            torna("player")
            
    elif pessoa == 'bot':
        print(f"\nMesa: {mesa}")
        time.sleep(0.25)
        jogada1 = cartas_bot[rd.randint(0,len(cartas_bot)-1)]
        mesa.append(jogada1)
        all_cards.append(jogada1)
        print(f"\nMesa: {mesa}\n\nSua mão: {cartas_player}")
        entrada = int(input())
        entrada -= 1
        jogada = cartas_player[entrada]
        mesa.append(jogada)
        all_cards.append(jogada)
        ganhou = compara('bot')
        
        cartas_player.pop(cartas_player.index(jogada))
        cartas_bot.pop(cartas_bot.index(jogada1))
        
        print("Mesa: {}".format(mesa))
        
        if ganhou == 1:
            print("Você venceu a rodada!")
            rodada.append(ganhou)
            torna("player")
        elif ganhou == 0:
            print("Você perdeu a rodada!")
            rodada.append(ganhou)
            torna("bot")
        elif ganhou == 2:
            print("Embuxou!")
            rodada.append(ganhou)
            torna("player")
    


#cartas_bot = ['J♦','2♦','2♠']
#cartas_player = ['4♦','2♣','2♥']
#mesa = ['A♦']
#torna("bot") # Ele da um return, só que como a função fica em loop, nao da pra pegar o return assim.

score = 0
scoreCpu = 0
ganhou = -1
while score < 11 or scoreCpu < 11:
    init()
    torna("player")
    if rodada[0] == rodada[1] and rodada[0] != 2:
        ganhou = rodada[0]
    elif rodada[0] == 2 and rodada[1] != 2:
        ganhou = rodada[1]
    elif rodada[1] == 2 and rodada[0] != 2:
        ganhou = rodada[0]
    if len(rodada) == 3:
        if rodada[0] == rodada[1] and rodada[1] == 2:
            ganhou == rodada[2]
    
    if ganhou == 1:
        print('Você ganhou!!!')
        score+=1
    elif ganhou == 0:
        print('Você perdeu!!!')
        scoreCpu+=1
    else:
        print("Vo^c[e Q{e~brO1u ´1o J~sdogo")
        
    continue



# ♦ ♠ ♥ ♣ 