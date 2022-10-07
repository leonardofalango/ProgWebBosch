# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:31:21 2022

@author: Leonardo Falango
"""
pos = ''
try:
    horario = input("Entre com a hora: ")
    hora, minu = horario.split(':')
    hora=int(hora)
    minu = int(minu)
    if hora < 0 or minu < 0:
        int('')
    elif hora >= 0 and hora < 11:
        pos = "AM"
    elif hora >= 12 and hora <= 24:
        pos = "PM"
    else:
        int('')
    print(f"Horário em formato de 12 horas: {hora}:{minu} {pos}")


except ValueError:
    print("Entre com uma hora válida. Ex (15:24)")

