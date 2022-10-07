# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:16:55 2022

@author: Leonardo Falango
"""
from datetime import datetime

while True:
    ano = (input("Entre com o seu ano de nascimento: "))
    if ano.isdigit() == False:
        print('Entre apenas com número')
        continue
    ano = int(ano)
    if ano < 0:
        print("Entre com uma idade válida.")
        continue
    time = datetime.today()
    print(time.year())
    idade = ano - anoatual
    if idade >= 16 and idade < 18:
        print("Seu voto é facultativo.")
    elif idade >= 18 and idade < 70:
        print("Você TEM que votar!")
    elif idade >= 70:
        print("Seu voto é facultativo")
