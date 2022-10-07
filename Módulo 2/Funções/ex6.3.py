# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:33:49 2022

@author: Leonardo Falango
"""

def contador(inicial,fim,passo):
    print(f"---------------CONTADOR INICIO: {inicial} FIM: {fim} PASSO: {passo}-------------------")
    
    x = inicial
    if inicial < fim:
        for i in range(inicial,fim+1,passo):
            print(i)
    else:
        for i in range(fim,inicial+1,passo):
            print(x)
            x -= passo
            
            
            
            
contador(20,0,2)        
contador(0,105,5)
contador(96,52,2)
contador(3,41,1)
contador(75,15,5)
contador(390,39,10)
usr = int(input("Digite o inicio do contador: "))
usr1 = int(input("Digite o fim do contador: "))
usr2 = int(input("Digite o passo do contador: "))
contador(usr,usr1,usr2)



