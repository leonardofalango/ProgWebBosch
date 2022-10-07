# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:56:33 2022

@author: Leonardo Falango
"""

agenda = {}
ind = 1 

while True:
    nome = input(f"Entre com o nome da pessoa {ind}: ")
    if nome == "":
        break
    idade = int(input(f"Entre com a idade da pessoa {ind}: "))
    cpf = input("Entre com o cpf da pessoa {}: ".format(ind))
    pessoa = {"Nome" : nome, "Idade" : idade, "Cpf" : cpf}
    
    numeroPessoa = "Pessoa " + str(ind)
    agenda[numeroPessoa] = pessoa
    ind += 1

for i in range(len(agenda)):
    i += 1
    pessoa = "Pessoa "+ str(i)
    print("="*30,pessoa,"="*30)
    print(f'Nome: {agenda[pessoa]["Nome"]}')
    print(f'Idade: {agenda[pessoa]["Idade"]}')
    print(f'Cpf: {agenda[pessoa]["Cpf"]}')