# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 08:52:15 2022

@author: Leonardo Falango
"""

#Definindos os quadrantes
# 1ºq = x>0 and y>0
# 2ºq = x<0 and y>0
# 3ºq = x<0 and y<0
# 4ºq = x>0 and y<0
while True:
    try:
        x = float(input("Entre com o valor de x: "))
        y = float(input("Entre com o valor de y: "))
        
        if x == 0 and y == 0:
            print("Está na origem")
        
        elif x == 0 and y != 0:
            print("Eixo X")
            
        elif y == 0 and x != 0:
            print("Eixo Y")
        
        elif x>0 and y>0:
            print("Está no 1º Quadrante")
        
        elif x<0 and y>0:
            print("Está no 2º Quadrante")
        
        
        elif x<0 and y<0:
            print("Está no 3º Quadrante")
        
        
        elif x>0 and y<0:
            print("Está no 4º Quadrante")
    
    except ValueError:
        print("Entre apenas com valores float")
   







