# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:33:56 2022

@author: DISRCT
"""


idades = []
alturas = []
alunos = []
for i in range(10):
    try:
        idade = int(input(f"Entre com a idade do aluno {i+1}: "))
        altura = float(input(f"Entre com a altura do aluno {i+1}: "))
    except ValueError:
        print("ERRO.\nApenas números são aceitos.")
        continue
    idades.append(idade)
    alturas.append(altura)
    
media = sum(alturas)/len(alturas)

for i in range(len(idades)):
    temp = []
    if idades[i] > 13 and alturas[i] < media:
        aluno = "aluno " + str(i)
        temp.append(aluno)
        temp.append(idades[i])
        temp.append(alturas[i])
        alunos.append(temp)
print(f"Os alunos que possuem a altura abaixo da média ({media}):\n{alunos}\nTotal: {len(alunos)}") 