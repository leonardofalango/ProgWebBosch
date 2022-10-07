# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:31:23 2022

@author: Leonardo Falango
"""

import matplotlib.pyplot as plt
import pyodbc
import pandas as pd
import seaborn as sns







server = 'CTPC3626'
database = 'LumiSensor'

driver= '{ODBC Driver 17 for SQL Server}'

conn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

cursor=conn.cursor()

cursor.execute("SELECT Luminosidade, Horario, Gás FROM dbo.LumiSensor")
row = cursor.fetchone()
lumi=[]
horario=[]
gas=[]

while row:
    lumi.append(row[0])
    hora = str(row[1]).split('.')
    horario.append(hora[0])
    gas.append(row[2])
    row = cursor.fetchone()

#print(horario, lumi)
    
df=pd.DataFrame({"Luminosidade" : lumi, "Gás" : gas,"Hora" : horario})
plt.xticks(rotation=45)
plt.figure(figsize=(15,8))
plt.xticks(rotation=85)
plt.grid(False)
sns.scatterplot(x="Hora", y="Luminosidade", data=df,hue='Luminosidade', linewidth=0)
plt.title("Luz por Tempo")

plt.show()

plt.xticks(rotation=45)
plt.figure(figsize=(15,8))
plt.xticks(rotation=85)
plt.grid(False)
sns.scatterplot(x="Hora", y="Gás", data=df,hue='Gás', linewidth=0)
plt.title("Gás por Tempo")

plt.show()