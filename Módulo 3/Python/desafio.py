# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:38:54 2022

@author: Leonardo Falango
"""

import requests as r
import json

proxie = {'https' : 'https://disrct:saladigital0311@10.224.200.26:8080'}

nome = input("Entre com um nome: ")

url = 'https://api.agify.io/?name='+nome

pessoa = r.get(url, proxies=proxie).content

nome = json.loads(pessoa)['name'].capitalize()
idade = json.loads(pessoa)['age']

print(f'A previsão da idade de {nome} é: {idade}')