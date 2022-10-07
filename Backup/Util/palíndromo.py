# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:32:32 2022

@author: Leonardo Falango
"""

def palindromo(string): # Palindromo é uma função booleana, que retorna se a string de parametro é ou não palíndromo
    string = string.upper()
    palavras = string.split(" ")
    letras = []
    for i in range(len(palavras)):
        for j in range(len(palavras[i])):
            letras.append(palavras[i][j])
    for i in range(len(letras)):
        if letras[i] == letras[len(letras) - (i+1)]:
            pass
        else:
            return 0
    return 1


while True:
    print("-"*15,"Verificação de palíndromo","-"*15)
    frase = input("Entre com a frase: ")
    if frase == '':
        break
    if palindromo(frase):
        print(f"{frase} é palíndromo")
    else:
        print(f"{frase} não é palíndromo")