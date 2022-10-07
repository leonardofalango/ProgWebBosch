# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 08:12:08 2022

@author: Leonardo Falango
"""

def subs_caractere(string, caractere_a_ser_substituido, caractere_que_substitui):
    co = caractere_a_ser_substituido
    cs = caractere_que_substitui # Só pra encurtar a chamada dessas variáveis
    letras = []
    
    for i in range(len(string)):
        if string[i] == co:
            letras.append(cs)
        else:
            letras.append(string[i])
    final = "".join(letras)
    return final
        
    
print(subs_caractere("palavara com banana", " ", "-"))
print(subs_caractere("desodorante", "o", "i"))
