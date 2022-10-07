# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:09:48 2022

@author: Leonardo Falango
"""
'''

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PROVA 3 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


'''

string = input("Entre com a palavra ou frase: ")
frase = string
palavras = string.split()

# 1º JEITO QUE EU PENSEI
#
#letras = []
#for i in range(len(palavras)):
#    for j in range(len(palavras[i])):
#        letras.append(palavras[i][j])  
#
#for i in range(int(len(letras)/2)):
#    letraanterior = letras[i]
#    letras[i] = letras[len(letras) - (1+i)]
#    letras[len(letras) - (1+i)] = letraanterior
#    
#print("".join(letras))


print('Você digitou: {}'.format(frase))
string = frase[::-1]
print('Frase invertida: {}'.format(string))









