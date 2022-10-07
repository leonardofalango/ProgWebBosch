# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 08:20:44 2022

@author: Leonardo Falango
"""

try:
    dinheiro = float(input("Entre com o valor: "))
    notas = []
    moedas = []
#    if dinheiro <= 0:
#        int("")
        
    
    
    while dinheiro // 2 >= 1:
        if dinheiro // 100 >= 1:
            notas.append(100)
            dinheiro -= 100
            
        elif dinheiro // 50 >= 1:
            notas.append(50)
            dinheiro -= 50
            
        elif dinheiro // 20 >= 1:
            notas.append(20)
            dinheiro -= 20
            
        elif dinheiro // 10 >= 1:
            notas.append(10)
            dinheiro -= 10
            
        elif dinheiro // 5 >= 1:
            notas.append(5)
            dinheiro -= 5
        
        elif  dinheiro // 2 >= 1:
            notas.append(2)
            dinheiro -= 2
            
    
    while dinheiro > 0:
        if dinheiro // 1 >= 1:
            moedas.append(1)
            dinheiro -= 1
        
        elif dinheiro // 0.5 >= 1:
            moedas.append(0.5)
            dinheiro -= 0.5
            
        elif dinheiro // 0.25 >= 1:
            moedas.append(0.25)
            dinheiro -= 0.25
            
        elif dinheiro // 0.10 >= 1:
            moedas.append(0.1)
            dinheiro -= 0.1
            
        elif dinheiro // 0.05 >= 1:
            moedas.append(0.05)
            dinheiro -= 0.05
            
        elif dinheiro // 0.01 >= 1:
            moedas.append(0.01)
            dinheiro -= 0.01
        
        else:
            break
        
    
    listanotas = [notas.count(100), notas.count(50), notas.count(20), notas.count(10), notas.count(5), notas.count(2)]
    listamoedas = [moedas.count(1), moedas.count(0.5), moedas.count(0.25), moedas.count(0.1), moedas.count(0.05), moedas.count(0.01)]
    
    listan = [100,50,20,10,5,2]
    print("NOTAS:")
    for i in range(len(listanotas)):
        print('{} nota(s) de R${:.2f}'.format(listanotas[i], listan[i]))
    
    listam = [1,0.5,0.25,0.1,0.05,0.01]
    print('MOEDAS:')
    for i in range(len(listamoedas)):
        print('{} moeda(s) de R${:.2f}'.format(listamoedas[i], listam[i]))
    
        
    
except ValueError:
    print("Entre com valores válidos para saque!")