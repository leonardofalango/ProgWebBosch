# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:36:21 2022

@author: Leonardo Falango
"""
import random as rd
numeroSecreto = rd.randint(0,10)
chance = 0
while True:
    try:
        if chance == 3:
            print("Você perdeu tudo!")
            break
        print("JOGO DA ADIVINHAÇÃO\n-------------------------------------\n")
        palpite = int(input("Digite seu palpite: "))
        if palpite > 10 or palpite < 0:
            int("a")
        elif palpite == numeroSecreto:
            print("Você Venceu!")
            break
        else:
            chance += 1
            print("Você Errou!")
        
    except ValueError:
        print("Entre com números de 0 a 10")
        continue