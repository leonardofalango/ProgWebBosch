# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:23:30 2022

@author: DISRCT
"""
lista0 = []
lista1 =[]
listafinal = []

for i in range(10):
    try:
        a = int(input(f"Entre com o valor {i+1} da lista {1}: "))
    except ValueError:
        print("Entrada  inválida. Apenas números.\n")
        continue
    lista0.append(a)
    
    
    
for i in range(10):
    try:
        a = int(input(f"Entre com o valor {i+1} da lista {2}: "))
    except ValueError:
        print("Entrada  inválida. Apenas números.\n")
        continue
    lista1.append(a)
        
        
for i in range(len(lista1)+ len(lista0)):
    try: 
        listafinal.append(lista0[i])
    except IndexError as error:
        pass
    try: 
        listafinal.append(lista1[i])
    except IndexError as error:
        continue

print(f"Lista 1:\n{lista0}\nLista 2:\n{lista1}\nLista Intercalada:\n{listafinal}")