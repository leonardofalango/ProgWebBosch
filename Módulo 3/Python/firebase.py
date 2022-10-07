# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:27:05 2022

@author: Leonardo Falango
"""

import requests as req
import time
from datetime import date
from datetime import datetime
import pyodbc

proxie = {'https' : 'https://disrct:saladigital0311@10.224.200.26:8080'}


url_temp = 'https://espfirebaseteste-default-rtdb.firebaseio.com/Sensor/temperatura.json'
url_umi = 'https://espfirebaseteste-default-rtdb.firebaseio.com/Sensor/umidade.json'

temps=[]
umis=[]
timestamps=[]

def InserirBD(lista_dados):
    server = 'CTPC3626'
    database = 'TempControl'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    data,temp, umi = lista_dados[0], lista_dados[1], lista_dados[2]
    cursor.execute(f"insert into dbo.Sensor (Horario, Temperatura, Umidade)	VALUES (convert(datetime, '{data}', 3), {temp}, {umi});")
    cursor.commit()




while True:

    ## RECEBENDO OS VALORES DE TEMPERATURA E UMIDADE DO FIREBASE
    temp = int(req.get(url_temp, proxies=proxie).content)
    umi = int(req.get(url_umi, proxies = proxie).content)
    temps.append(temp)
    umis.append(umi)
    
    ## DATA E HORA:
    timestamp = datetime.now()
    mes = timestamp.month
    if mes < 10:
        mes = f'0{mes}'
    year = str(timestamp.year)
    year = year[2:]
    timestamp = f'{year}-{mes}-{timestamp.day} {timestamp.hour}:{timestamp.minute}:{timestamp.second}'
    

    dados_temp = (timestamp, temp, umi)
    InserirBD(dados_temp)
    print(timestamp)
    print(temp, umi)
    time.sleep(2)
    for i in '....Medindo....':
        print(i)
        time.sleep(0.1)
    time.sleep(3)

dicio = {"Horario" : timestamps, "Temperatura" : temps, "Umidade" : umis}
print(dicio)