# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:53:16 2022

@author: Leonardo Falango
"""

def diaMes(mes):
    if mes > 0 and mes <=12:
        if mes <= 7:
            if mes == 2:
                return 28
            elif mes%2 == 0:
                return 30
            else:
                return 31
                
        elif mes > 7:
            if mes%2 == 0:
                return 31
            else:
                return 30
      
    else:
        return -1

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
              'novembro', 'desembro']



data = input("Insira sua data de nascimento: ")
dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
if dia <= 0 or mes<=0 or int(ano) <= 0: # O certo seria ano<= 1800 pois ninguem tem mais de 200 anos
    print("Data inválida")
else:
    quantdias = diaMes(mes)
    if quantdias == -1:
        print("Erro, mes inválido")
    elif quantdias < dia:
        print(f"O mes {meses[mes-1]}, possui apenas {quantdias} dias.")
    
    else:
        print(f"{dia} de {meses[mes-1]} de {ano}")





