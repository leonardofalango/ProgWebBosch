# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:09:43 2022

@author: DISRCT
"""







entrada = 1
conjunto = []

def multiplo(lista):
    listamultiplode10 = []
    for i in range(len(lista)):
        if lista[i] % 10 == 0:
            listamultiplode10.append(lista[i])
    return listamultiplode10






lista = []
while True:
    try:
        entrada = int(input("Entre com o valor: "))
    except ValueError:
        print("ERRO.\n Entre apenas com valores inteiros.")
    if entrada == -1:
        print(f"\n\nLista final multiplos de 10:\n{lista}")
        break
    conjunto.append(entrada)
    lista = multiplo(conjunto)
    print(f"A lista completa:\n{conjunto}\n\nA lista com apenas multiplos de 10:\n{lista}")
    