# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:45:18 2022

@author: DISRCT
"""

alunos = {}
p = 1
while True:
     nome = "Aluno " + str(p)
     notas = []
     aluno = input("Digite o nome do aluno: ")
     if aluno == "": #Condição de parada eh colocar uma empty string no nome do jogador
         break
     try:
        
         quantProvas = int(input("Digite a quantidade de provas feitas: "))
        
         if quantProvas < 0 :
             a = int("a") # Forçar um erro caso a quantidade de pertidas jogadas seja menor que 0
            
            
         for i in range(quantProvas):
             nota = int(input(f"Qual a nota da prova {i}? "))
            
             if nota < 0:
                 notas.append(0)
                 continue
                
             notas.append(nota)
            
     except ValueError:
         print("ERRO. Valor inválido")
         continue
    
     auxiliar = {"Nome" : aluno, "Notas" : notas, "Média" : sum(notas)/len(notas)}
     alunos[nome] = auxiliar
     p+=1

print(alunos)