# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:55:29 2022

@author: DISRCT
"""

mesesb = []
mesesb.append("janeiro")
mesesb.append("fevereiro")
mesesb.append("março")
mesesb.append("abril")
mesesb.append("maio")
mesesb.append("junho")
mesesb.append("julho")
mesesb.append("agosto")
mesesb.append("setembro")
mesesb.append("outubro")
mesesb.append("novembro")
mesesb.append("dezembro")

calendario = {}
calen = {}

temperatura = []
for i in range(12):
    try:
        temp = float(input(f"Entre com a temperatura média de {mesesb[i]}: "))
    except ValueError:
        print("ERRO. Apenas números são aceitos.")
        break
    temperatura.append(temp)
    calendario = {mesesb[i] : temp}
    mes = "mes "+ str(i+1)
    calen[mes] = calendario
    

media = sum(temperatura) / len(temperatura)
for i in range(len(calen)):
    mes = "mes "+ str(i+1)
    print(f'Mes: {calen[mes]}')



