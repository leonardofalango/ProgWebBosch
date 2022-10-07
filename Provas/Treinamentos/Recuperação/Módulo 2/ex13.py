# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:24:12 2022

@author: Leonardo Falango
"""

import os 

def ext(arquivo):
    arq = arquivo.split(".")
    ind = (len(arq)-1)
    return arq[ind]


def organizaImgs(caminho):
    destino = os.path.join(caminho, "Imagens")
    if not os.path.isdir(destino):
        os.mkdir(destino)
    
    lista = os.listdir(caminho)
    
    for arquivo in lista:
        extencao = ext(arquivo)
        
        if extencao == "png" or extencao == "jpg" or extencao == "jpeg":
            os.rename(os.path.join(caminho, arquivo), os.path.join(caminho,destino,arquivo)) # Mudando o arquivo de pasta


organizaImgs("C:/Users/disrct/Pictures")
