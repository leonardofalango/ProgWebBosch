# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:36:50 2022

@author: Leonardo Falango
"""

agenda = {}
ind = 1 

while True:
    nome = input(f"Entre com o nome da pessoa {ind}: ")
    if nome == "":
        break
    telefone = input(f"Entre com o telefone da pessoa {ind}: ")
    pessoa = {"Nome" : nome, "Telefone" : telefone}
    
    numeroPessoa = "Pessoa " + str(ind)
    agenda[numeroPessoa] = pessoa
    ind += 1

print(agenda)

