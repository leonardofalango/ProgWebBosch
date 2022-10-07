# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:00:42 2022

@author: Leonardo Falango
"""

import matplotlib.pyplot as plt
import pyodbc


server = 'JVLPC0587\SQLSERVER'
database = 'ProvaLeonardoFalango'
driver= '{ODBC Driver 17 for SQL Server}'
conn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor=conn.cursor()
cursor.execute("SELECT Horario, Umidade, Temperatura FROM dbo.Prova3")
row = cursor.fetchone()

horario=[]
temperatura=[]
umidade=[]




while row:
    hora = str(row[0]).split('.')
    horario.append(hora[0])
    temperatura.append(row[1])
    umidade.append(row[2])
    row = cursor.fetchone()
    

fig, eixo = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(10,6))


#EIXOS
eixo[0].plot(horario, temperatura, color='r', linewidth=5)
eixo[0].set_title("Temperatura")

eixo[1].plot(horario, umidade, color='blue', linewidth=5)
eixo[1].set_title("Umidade")


plt.xticks(rotation=45)
plt.grid(False)
plt.title("Temperatura e Umidade por Horário")


plt.show()

cursor2 = conn.cursor()
cursor2.execute("SELECT Horario, Umidade, Temperatura FROM dbo.Prova3")
print(f"A quantidade de Dados presentes no banco de dados é: {len(cursor2.fetchall())}")

