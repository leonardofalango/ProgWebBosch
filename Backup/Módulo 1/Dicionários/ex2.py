# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:56:33 2022

@author: Leonardo Falango
"""
agendamenor = {}
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
    agendamenor[numeroPessoa] = pessoa
    ind += 1

i=0
print("="*30,"MAIORES","="*30,"\n",)
for j in range(len(agenda)):
    i += 1
    pessoa = "Pessoa "+ str(i)
    if agenda[pessoa]["Idade"] < 18:
        agenda.pop(pessoa)
    else:
        print("="*30,j,"="*30)
        print(f'Nome: {agenda[pessoa]["Nome"]}')
        print(f'Idade: {agenda[pessoa]["Idade"]}')
        print(f'Cpf: {agenda[pessoa]["Cpf"]}')

i=0
j=0
print("="*30,"MENORES","="*30,"\n",)
for j in range(len(agendamenor)):
    i += 1
    pessoa = "Pessoa "+ str(i)
    if agendamenor[pessoa]["Idade"] < 18:
        print("="*30,j,"="*30)
        print(f'Nome: {agendamenor[pessoa]["Nome"]}')
        print(f'Idade: {agendamenor[pessoa]["Idade"]}')
        print(f'Cpf: {agendamenor[pessoa]["Cpf"]}')