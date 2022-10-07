# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:17:56 2022

@author: Leonardo Falango
"""
import requests as r
import pyodbc
import time

proxie = {'https' : 'https://disrct:saladigital0311@10.224.200.26:8080'}

urlLuminosidade = 'https://extesteprova-default-rtdb.firebaseio.com/LumiSensor/Luminosidade.json'
urlanalogLuminosidade = 'https://extesteprova-default-rtdb.firebaseio.com/LumiSensor/analogLuminosidade.json'
urlgas = 'https://extesteprova-default-rtdb.firebaseio.com/LumiSensor/G%C3%A1s.json'



def insertDB(lista_dados):
    server = 'CTPC3626'
    database = 'LumiSensor'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    luminosidade, analogLuminosidade, gas = lista_dados[0], lista_dados[1], lista_dados[2]
    cursor.execute(f"INSERT into dbo.LumiSensor (Luminosidade, analogLuminosidade, Gás)	VALUES ({luminosidade}, {analogLuminosidade}, {gas});")
    cursor.commit()


while True:
    lumi = int(r.get(urlLuminosidade, proxies=proxie).content)
    analoglumi = int(r.get(urlanalogLuminosidade, proxies=proxie).content)
    gas = int(r.get(urlgas, proxies=proxie).content)
    
    dados = (lumi, analoglumi, gas)
    print(f"INSERINDO...\nLuminosidade {lumi}\nanalogLuminosidade: {analoglumi}\nGás: {gas}\n\n")
    
    insertDB(dados)
    time.sleep(10)
    