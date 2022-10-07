# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:33:57 2022

@author: Leonardo Falango
"""

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
                                                         
 





#♠♣♥♦

from termcolor import colored
import random as rd
import sys
import time


# baralho = {'A♠': 1,'2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 'Q♠': 11, 'K♠': 13, 'J♠': 12,
#           'A♣': 1,'2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'Q♣': 11, 'K♣': 13, 'J♣': 12,
#           'A♥': 1,'2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, 'Q♥': 11, 'K♥': 13, 'J♥': 12,
#           'A♦': 1,'2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, 'Q♦': 11, 'K♦': 13, 'J♦': 12,}
# Nao ia dar certo por causa dos naipes
# A verificação de qual é o maior naipe nas manilhas





dinheiro = 'Não Faça apostas no Truco! :)'
baralho = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"] # Quanto maior o index, maior o valor da carta, desconsiderando as manilhas
naipes = ["♦", "♠", "♥", "♣"] # index[0] < index[1] < index[2] Então precisa verificar apenas o index.


corfirmations = {'sim': 1, 's': 1, 'yes': 1,'y': 1,'ye': 1,'si': 1,'aceito': 1,'1' : 1}









#----------------------DAR CARTAS---------------------------------------------
def giveCards(n_cartas):
    global baralho, naipes, all_cards
    
    cartas = []
    
    for i in range(n_cartas):
        carta = baralho[rd.randint(0,9)]
        naipe = naipes[rd.randint(0, 3)]
        while carta+naipe in all_cards: # Verificando se tem carta repetida
            carta = baralho[rd.randint(0, 9)]
            naipe = naipes[rd.randint(0, 3)]
        all_cards.append(carta+naipe)
        cartas.append(carta+naipe)
        
    return cartas
    





#-----------INICIO------------------------------------------------------------

def init():
    global baralho, naipes, all_cards, player1_cards, bot1_cards, mesa_cards, vira, player_score, bot_score
    global rodada_player, rodada_bot, rodadas, mesa_cards
    
    for i in range(len('♠♥♦♣Embaralhando♠♥♦♣')):
        print('♠♥♦♣EMBARALHANDO♠♥♦♣'[i])
        time.sleep(0.25)
    
    all_cards = []
    rodada_player = 0
    rodada_bot = 0
    rodadas = []
    mesa_cards = []

   
    
# Player
    player1_cards = giveCards(3)
    
    
    
# Mesa
    vira = baralho[rd.randint(0, 9)] + naipes[rd.randint(0,3)]
    all_cards.append(vira)
    print("O vira é: {}".format(vira))
    
    
    
 # Bots   
    bot1_cards = giveCards(3)
    

    
def playerIniciar():
    global baralho, naipes, all_cards, player1_cards, bot1_cards, mesa_cards, vira, player_score, bot_score 
    global rodada_player, rodada_bot, rodadas, mesa_cards
    init()
    
    
        
        
    
    
    cartaplayer = turnoPlayer()
    cartabot = turnoBot()
    verificar = check(vira, cartaplayer, cartabot)
    if verificar == 1:
        print("Você venceu a rodada!")
        rodada_player += 1
        rodadas.append('Player')
    elif verificar == 2:
        print("Embuxou!")
        rodada_player, rodada_bot = rodada_player+1, rodada_bot + 1
        rodadas.append('Empate')
    elif verificar == 0:
        print("Você perdeu a rodada.")
        rodada_bot += 1
        rodadas.append('Bot')
    x=-1
    while len(rodadas) < 3:
        
        if (rodada_player == 2 or rodada_bot == 2) and len(rodadas) == 2:
            if rodadas[0] == 'Player' or rodadas[1] == 'Player':
                print('Você ganhou um ponto!')
                player_score +=1
                break
            elif rodadas[0] == 'Bot' or rodadas[1] == 'Bot':
                print('Você perdeu!')
                bot_score += 1
                break
            
        elif (len(rodadas) == 3):
            if rodadas[0] == 'Player':
                print('Você ganhou um ponto!')
                player_score +=1
                break
            elif rodadas[0] == 'Bot':
                print('Você perdeu!')
                bot_score += 1
                break
        
        
        
        
        
        
        
        
        
        x += 1
        
        
        if rodadas[x] == 'Player': # SE O PLAYER GANHAR A RODADA ANTERIOR
            cartaplayer = turnoPlayer()
            cartabot = turnoBot()
            verificar = check(vira, cartaplayer, cartabot)
            
            
            if verificar == 1:
                print("Você venceu a rodada!")
                rodada_player += 1
                rodadas.append('Player')
                continue
            
            elif verificar == 2:
                print("Embuxou!")
                rodada_player, rodada_bot = rodada_player+1, rodada_bot + 1
                rodadas.append('Empate')
                continue
                
            elif verificar == 0:
                print("Você perdeu a rodada.")
                rodada_bot += 1
                rodadas.append('Bot')
                continue
        
        
        elif rodadas[x] == 'Bot' or rodadas[0] == 'Empate':
            cartabot = turnoBot()
            cartaplayer = turnoPlayer()
            verificar = check(vira, cartaplayer, cartabot)
            if verificar == 1:
                print("Você venceu a rodada!")
                rodada_player += 1
                rodadas.append('Player')
                continue
            
            elif verificar == 2:
                print("Embuxou!")
                rodada_player, rodada_bot = rodada_player+1, rodada_bot + 1
                rodadas.append('Empate')
                continue
                
            elif verificar == 0:
                print("Você perdeu a rodada.")
                rodada_bot += 1
                rodadas.append('Bot')
                continue
            
        else:
            print('Erro!')
            sys.exit()
            
            
            
            
        

        
        
    









#------------------------------TURNOS-----------------------------------------
def turnoPlayer():
    global player1_cards, mesa_cards
    print(f'Suas cartas: {player1_cards}')
    jogada = input('Jogar.\n')
    jogada = int(jogada) - 1
    mesa_cards.append(player1_cards[jogada])
    print('Sua jogada: ',player1_cards[jogada])
    return player1_cards[jogada]
    
        
    


# POR ENQUANTO ESTA SENDO CARTAS ALEÁTORIAS
def turnoBot():
    global bot1_cards, mesa_cards
    
    jogada = rd.randint(0, len(bot1_cards)-1)
    mesa_cards.append(bot1_cards[jogada])
    time.sleep(1)
    print('Jogada do bot:',bot1_cards[jogada])
    time.sleep(1)
    return bot1_cards[jogada]







#--------------------------------------------------------------------------------APAGANDO CARTAS-----
    














#-----------------------------------------------------------CHECKANDO----------------------------

def check(vira,cart,cart1):
    global baralho, naipes
    
    vira_carta = (baralho.index(vira[0]))
    
    if baralho.index(vira[0]) == 9:
        vira_carta =  0
    
    if baralho.index(cart[0]) == vira_carta+1 and baralho.index(cart1[0]) == vira_carta+1:
        # Nesse caso, os dois sao manilhas
        if naipes.index(cart[1]) > naipes.index(cart1[1]): # SE O INDEX DO NAIPE DA CARTA DO PLAYER FOR MAIOR DO QUE O INDEX DA DO BOT, O PLAYER GANHA
            apagaCartas(cart, cart1)
            return 1
        else:
            return 0
    
    # (baralho.index(vira[0])+1) == index do vira na lista de baralhos, +1, sendo a manilha correspondente ao vira
    
    elif baralho.index(cart[0]) == vira_carta+1 and baralho.index(cart1[0]) != vira_carta+1:
        return 1
    
    elif baralho.index(cart[0]) != vira_carta+1 and baralho.index(cart1[0]) == vira_carta+1:
        return 0
    
    elif baralho.index(cart[0]) > baralho.index(cart1[0]):
        return 1
    
    elif baralho.index(cart[0]) < baralho.index(cart1[0]):
        return 0
    
    elif baralho.index(cart[0]) == baralho.index(cart1[0]):
        return 2
    
    else:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        return -1
        
    
    











#-MAIN-----------------------------------------------
def main():
    global confimation, naipes, baralho, all_cards, mesa_cards, vira
    print('\n'
' _______  _______  __   __    __   __  ___   __    _  ______   _______    _______  _______  ''\n'
'|  _    ||       ||  |_|  |  |  | |  ||   | |  |  | ||      | |       |  |   _   ||       | ''\n'
'| |_|   ||    ___||       |  |  |_|  ||   | |   |_| ||  _    ||   _   |  |  |_|  ||   _   | ''\n'
'|       ||   |___ |       |  |       ||   | |       || | |   ||  | |  |  |       ||  | |  | ''\n'
'|  _   | |    ___||       |  |       ||   | |  _    || |_|   ||  |_|  |  |       ||  |_|  | ''\n'
'| |_|   ||   |___ | ||_|| |   |     | |   | | | |   ||       ||       |  |   _   ||       | ''\n'
'|_______||_______||_|   |_|    |___|  |___| |_|  |__||______| |_______|  |__| |__||_______| ''\n'
'                       _______  ______    __   __  _______  _______                         ''\n'
'                      |       ||    _ |  |  | |  ||       ||       |                        ''\n'
'                      |_     _||   | ||  |  | |  ||       ||   _   |                        ''\n'
'                        |   |  |   |_||_ |  |_|  ||       ||  | |  |                        ''\n'
'                        |   |  |    __  ||       ||      _||  |_|  |                        ''\n'
'                        |   |  |   |  | ||       ||     |_ |       |                        ''\n'
'                        |___|  |___|  |_||_______||_______||_______|                        ''\n')
    
    inicio = input('♠♥♦♣ Desejas iniciar o Truco? ♠♥♦♣\n')
    inicio = inicio.lower()
    for i in corfirmations:
        if i == inicio:
            player_score = 0
            bot_score = 0
            while player_score < 11 or bot_score < 12:
                
                if (player_score + bot_score) % 2 == 0:
                    playerIniciar()
                else:
                    botIniciar()
                


#♠♥♦♣

player_score = 0
bot_score = 0
main()
    
    
        
    

