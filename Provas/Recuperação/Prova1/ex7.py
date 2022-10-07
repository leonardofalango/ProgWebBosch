# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:18:08 2022

@author: DISRCT
"""
def cod(a):
    import string
    alfabeto = list(string.ascii_lowercase)

    a = str(a)
    palavras = a.split()
    letras = []
    letrasf = []
    for i in range(len(palavras)):
        for j in range(len(palavras[i])):
            letras.append(palavras[i][j])  
    
    for i in range(len(letras)):
        if letras[i].isalnum() == True:
            if letras[i].isdigit() == True:
                letrasf.append(alfabeto[int(a[i])])
            else:
                letrasf.append(str(alfabeto.index(a[i])))

        else:
            pass
    return "".join(letrasf)
    
senha = input("Digite sua senha: ")
print(f"Senha criptografada: {cod(senha)}")