# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:44:48 2022

@author: Leonardo Falango
"""

import os

def move(arquivo):
    if not os.path.isfile(os.path.join(arquivo)):
        return -1
    
    pasta = os.path.join('S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Treinamentos/Recuperação/Módulo 2','A pasta')
    if not os.path.isdir(pasta):
            os.mkdir(pasta)
    os.rename(arquivo,os.path.join(pasta,arquivo))
    return 1
    
arq = input("Entre com o nome do arquivo: ")
result = move(arq)
if result == 1:
    print("Movido")
else:
    print("ERRO!!!!")