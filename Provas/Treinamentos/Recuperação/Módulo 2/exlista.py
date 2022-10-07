# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:41:24 2022

@author: Leonardo Falango
"""

import pandas as pd
import matplotlib.pyplot as plt


#df = pd.read_csv("csv/salaries.csv")
#
#
#print(df.columns)
#
#
#df['BasePay'].dropna()
#
#maxsal = df["BasePay"].max()
#print("\nSalário médio: R${:.02f}".format(df['BasePay'].mean()))
#print("\nSalário máximo: R${:.02f}".format(maxsal))
#joseph = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']
#
#print("\nEmprego do JOSEPH DRISCOLL: {}".format(joseph['JobTitle']))
#
#maior = df[df['BasePay'] == maxsal]
#print("\nPessoa que possui o maior salário: {}".format(maior['EmployeeName']))
#
#
##salario médio por ano
#
#ano = df['Year'].unique()
#media = []
#for i in ano:
#    x = df[df['Year'] == i]
#    x = x['BasePay'].mean()
#    media.append(round(x,2))
#
#mediasal = sum(media)/len(media)
#
#print("\nA média de salário por ano é : R${:.02f}".format(mediasal))
#
#jtitles = df.groupby(['JobTitle']).size()
#jtitles = jtitles.sort_values(ascending=False)
#print("\nOs empregos mais comuns são:\n{}".format(jtitles.head(5)))
#
#
#
#plt.bar(ano, media, width= 0.5)
#plt.xticks(ano)
#plt.axis([2010, 2015, 0, 80000])
#plt.grid(True, axis='y', ls='--')
#
#plt.xlabel("Ano")
#plt.ylabel("Salário")
#plt.title("Relação entre ano e salário")
#plt.show()




df = pd.read_csv('S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Treinamentos/Recuperação/Módulo 2/csv/Salaries.csv')


salario_maior = df['BasePay'].max()
pessoa_maior = df.loc[df['BasePay'] == salario_maior]
pessoa_maior = pessoa_maior['EmployeeName'].values[0]

salario_medio = df['BasePay'].mean()

joseph = df.loc[df['EmployeeName'] == 'JOSEPH DRISCOLL']
jobtitle_joseph = joseph['JobTitle'].values[0]




jtitles = df.groupby(['JobTitle']).size()
jtitles = jtitles.sort_values(ascending=False)
empregos_comuns = jtitles.head(5)
empregos_comuns = list(empregos_comuns.index)




#salario médio por ano

ano = df['Year'].unique()
media = []
for i in ano:
    x = df[df['Year'] == i]
    x = x['BasePay'].mean()
    media.append(round(x,2))
mediasal = sum(media)/len(media)




plt.bar(ano, media, width= 0.5)
plt.xticks(ano)
plt.axis([2010, 2015, 0, 80000])
plt.grid(True, axis='y', ls='--')

plt.xlabel("Ano")
plt.ylabel("Salário")
plt.title("Relação entre ano e salário")
plt.show()




print("Colunas: ")

for column in df:
    print(column,end=', ')
print('\n')


print(f'Salário médio: {salario_medio}\nSalário Máximo: {salario_maior}'
      f'\nEmprego do Joseph Driscoll: {jobtitle_joseph}'
      f'\nNome da pessoa que possui o maior salário: {pessoa_maior}\nMédia dos salários por ano é: {mediasal}',
      f'\nA lista de empregos mais comuns são: \n{empregos_comuns}\n',
      f'\n')
