# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:10:38 2022

@author: Leonardo Falango
"""

##Funcionando


import requests as r
import pyodbc
import time

proxie = {'https' : 'https://disrct:saladigital0311@10.224.200.26:8080'}

url_temp = 'https://prova-98629-default-rtdb.firebaseio.com/DHT/Temperatura.json'
url_umi = 'https://prova-98629-default-rtdb.firebaseio.com/DHT/Umidade.json'

proxie = {'https' : 'https://disrct:saladigital0311@10.224.200.26:8080'}

def insertDB(dados):
    temp, umi = dados[0], dados[1]
    server = 'JVLPC0587\SQLSERVER'
    database = 'ProvaLeonardoFalango'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"INSERT INTO dbo.Prova3 (Temperatura, Umidade) values ({temp}, {umi});") ##Não precisa colcoar o timestamp pois já é DEFAULT
    cursor.commit()


def pegaDados():
    temp = float(r.get(url_temp, proxies=proxie).content)
    umi = int(r.get(url_umi, proxies=proxie).content)
    return temp, umi


while True:
    temp, umi = pegaDados()
    print("Enviando dados de Temperatura e Umidade.")
    print(f"Temperatura: {temp}\nUmidade: {umi}")
    lista_dados = (temp, umi)
    insertDB(lista_dados)
    time.sleep(30)
