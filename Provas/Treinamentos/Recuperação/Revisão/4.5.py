# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:28:35 2022

@author: Leonardo Falango
"""
while True:
    try:
        linha = int(input("Entre com o tamanho do tabuleiro: "))
        if linha < 0:
            print("Tamanho inválido")
            continue
        if linha == 0 :
            break
        for i in range(linha):
            for j in range(linha):
                print('x',end='')
            print('\n',end='')

    except ValueError:
        print("Valor inválido.")
        continue