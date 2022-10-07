# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:11:19 2022

@author: Leonardo Falango
"""

def diaMes(mes):
    mesesb = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
              'novembro', 'desembro']
    
    if mes > 0 and mes <=12:
        if mes <= 7:
            if mes == 2:
                print(f"O mes {mesesb[mes-1]} possui 28 dias.")
            elif mes%2 == 0:
                print(f"O mês {mesesb[mes-1]} possui 30 dias.")
            else:
                print(f"O mês {mesesb[mes-1]} possui 31 dias.")
                
        elif mes > 7:
            if mes%2 == 0:
                print(f"O mês {mesesb[mes-1]} possui 31 dias.")
            else:
                print(f"O mês {mesesb[mes-1]} possui 30 dias.")
      
    else:
        print("Valor invalido")


def diaMesFunction(mes):
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
                     
