# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:59:12 2021

@author: DISRCT
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import time
from sqlalchemy import create_engine


def Firebase():
	proxies = {'https' : 'https://disrct:saladigital0305@rb-proxy-de.bosch.com:8080'}
	url_temp = "https://treinamento-ets-default-rtdb.firebaseio.com/Gabriel/Temperatura.json"
	url_umi = "https://treinamento-ets-default-rtdb.firebaseio.com/Gabriel/Umidade.json"
	Temperatura = float(requests.get(url_temp, proxies = proxies).content)
	Umidade = float(requests.get(url_umi, proxies = proxies).content)
	return Temperatura, Umidade



def Inserir(sinal):
	con = mysql.connector.connect(user='root', password='saladigitalsql',
                              host='localhost',
                              port='3306',
                              database='gabriel_b',
                              use_pure=True)
	cursor = con.cursor()
	insert_query = """INSERT INTO DHT11 (Temperatura, Umidade) values({},{})""".format(sinal[0],sinal[1])
	print(insert_query)
	cursor.execute(insert_query)
	con.commit()
	print("Dados inseridos no banco com sucesso!")
	
	
	
def Pegar():
	con = create_engine('mysql+pymysql://root:saladigitalsql@localhost/gabriel_b') 
	df = pd.read_sql('SELECT * FROM DHT11', con) 
	print(df)
	return df


def plot(df):
	plt.plot(df.ID, df.Temperatura)
	plt.xlabel("ID")
	plt.ylabel("Temperatura")
	plt.show()
	
	plt.plot(df.ID, df.Umidade)
	plt.xlabel("ID")
	plt.ylabel("Umidade")
	plt.show()
	print("Dados Inseridos:", len(df))
	

	
dados= Firebase()
Inserir(dados)
df = Pegar()
plot(df)
time.sleep(35);
	