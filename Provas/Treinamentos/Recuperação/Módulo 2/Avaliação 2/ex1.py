# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 08:57:51 2022

@author: DISRCT
"""

import pandas as pd



df = pd.read_csv('Exercício1.csv', encoding='utf-8')
# Montando o csv em lista para colocar no dicionario e reecrever os dados ja existentes
nomes = list(df['Nome'])
cursos = list(df['Curso'])
matriculas = list(df['Matricula'])

nome = ' '
cont = 0 # Sempre tem que ter o aluno exemplo para continuar adicionando alunos

print("Alunos já cadastrados:\n{}".format(df))


while True:
    try:
        nome = input("Entre com o nome do aluno: ")
        if nome == '':
            int('')
        curso = input("Entre como o curso: ")
        if curso == '':
            int('')
        matricula = int(input("Entre com a matrícula: "))
        
        
        nomes.append(nome)
        cursos.append(curso)
        matriculas.append(matricula)
        
        csv = {'Nome' : nomes, 'Curso' : cursos, 'Matricula' : matriculas}
        
        df = pd.DataFrame(csv)
        df.to_csv('Exercício1.csv', encoding=('utf-8'),index=False)
        
        print("Número de alunos cadastrados: {}".format(len(df)+cont))
        cont+=1
        

    except ValueError:
        break
