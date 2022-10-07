# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:34:44 2022

@author: Leonardo Falango
"""

import requests as req
import pyodbc

def getDados():
    proxie = {"https" : "https://disrct:saladigital0311@10.224.200.26:8080"}
    url_temp = 'https://espfirebaseteste-default-rtdb.firebaseio.com/Sensor/temperatura.json'
    url_umi = 'https://espfirebaseteste-default-rtdb.firebaseio.com/Sensor/umidade.json'
    temp = float(req.get(url_temp, proxies=proxie).content)
    umi = int(req.get(url_umi, proxies = proxie).content)
    
    return temp, umi

def InserirBD(lista_dados):
    server = 'CTPC3626'
    database = 'TempControl'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    temp, umi = lista_dados[0],lista_dados[1]
    cursor.execute(f"INSERT dbo.SensorAula (Temperatura, Umidade) VALUES ({temp}, {umi});") # sql query
    cursor.commit()
    print(f"Inserido com sucesso!\n{temp}\n{umi}") # message to indicate to user the operation was succesful

def show(lista_dados):
    temp, umi = lista_dados[0],lista_dados[1]
    print(f"Temperatura: {temp}\nUmidade: {umi}")

while True:
    lista_dados = getDados()
    show(lista_dados)
    InserirBD(lista_dados)
