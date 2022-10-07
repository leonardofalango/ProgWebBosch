# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:05:13 2022

@author: Leonardo Falango
"""

import matplotlib.pyplot as plt
import pyodbc
import pandas as pd
import seaborn as sns







server = 'CTPC3626'
database = 'TempControl'

driver= '{ODBC Driver 17 for SQL Server}'

conn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

cursor=conn.cursor()

cursor.execute("SELECT Temperatura, timestamp FROM dbo.SensorAula")
row = cursor.fetchone()
lista=[]
listatempo=[]

while row:
    lista.append(row[0])
    tempo = str(row[1])
    tempo = tempo.split(" ")
    tempo = tempo[1]
    listatempo.append(tempo)
    row = cursor.fetchone()

df=pd.DataFrame({"Temperatura":lista, "Tempo":listatempo})
plt.xticks(rotation=45)
plt.figure(figsize=(15,8))
plt.xticks(rotation=45)
plt.grid(False)
plote = sns.scatterplot(x="Tempo", y="Temperatura", data=df,hue='Temperatura', linewidth=0)
for ind, label in enumerate(plote.get_xticklabels()):
    if ind % 18 == 0:  # Mantém apenas os rótulos múltiplos de 4 no eixo x
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.title("Temperatura por Tempo")
sns.despine(fig=None, ax=None, top=False, right=False, left=False, bottom=False, offset=None, trim=False)

plt.show()