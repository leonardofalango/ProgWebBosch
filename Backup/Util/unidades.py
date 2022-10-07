# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:09:41 2022

@author: Leonardo Falango
"""

def unidades(numero):
    if numero>1000:
        print("Numero invalido")
    else:
        centenas = int(numero / 100)
        dezenas = int((numero-(centenas*100))/10)
        unidades = int(numero - (centenas*100 + dezenas*10))
        return centenas, dezenas, unidades