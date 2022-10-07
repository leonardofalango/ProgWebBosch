# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:40:03 2022

@author: Leonardo Falango
"""

notas = [100,50,20,10,5,2]
moedas = [1,0.5,0.25,0.1,0.05,0.01]

final = []
finalmoedas = []
dinheiro = float(input("Entre com o valor: "))

for i in range(len(notas)):
    if (int(dinheiro // notas[i])>=1):
        pass
    else:
        final.append(0)
        continue
    for j in range(1,(int(dinheiro // notas[i]))+1,1):
        dinheiro -= notas[i]
    final.append(j)


for i in range(len(moedas)):
    if (int(dinheiro // moedas[i]) >= 1):
        pass
    else:
        finalmoedas.append(0)
        continue
    for j in range(1,(int(dinheiro // moedas[i]))+1,1):
        dinheiro -= moedas[i]
    finalmoedas.append(j)


print("NOTAS")
for i in range(len(notas)):
    print("{} nota(s) de R${:.02f}".format(final[i],notas[i]))
print("MOEDAS")
for i in range(len(notas)):
    print("{} moeda(s) de R${:.02f}".format(finalmoedas[i],moedas[i]))

