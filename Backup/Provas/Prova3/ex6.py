# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:06:02 2022

@author: Leonardo Falango
"""

imposto = {"mg": 0.07 , "sp" : 0.12, "rj": 0.15, "ms" : 0.08}

try:
    dolar = float(input("Insira o valor do produto em dólares: "))
    real = dolar * 5.12
    if dolar <= 0:
        int('')
    est = input("O estado para qual ele será transportado (MG, SP, RJ ou MS): ")
    est = est.lower()
    imp = imposto[est] * real
    final = real + imp
    print(f"Valor final: {round(final,2)}")
    
except ValueError:
    print("Valor inválido")
except KeyError:
    print("Estado inválido")