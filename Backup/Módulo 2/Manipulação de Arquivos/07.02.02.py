# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:44:59 2022

@author: Leonardo Falango
"""



def verificaIP(ip):
    ips = ip.split(".")
    if len(ips) > 4 or len(ips) < 3:
        return False
    try:
        for i in range(len(ips)):
            if int(ips[i]) <= 255 and int(ips[i]) >= 0:
                pass
            else:
                return False
        return True
    except ValueError:
        return False



contador = 1

todos = open('02.ip_todos.txt', mode='r+')

certos = open('02.ip_validos.txt', mode='w+')

errados = open('02.ip_invalidos.txt', mode='w+')

banco = []
for linhas in todos:
    linha, descarte = linhas.split('\n')
    banco.append(linha)
    
for i in range(len(banco)):
    ip = banco[i]
    if verificaIP(ip) == True:
        certos.write(ip+'\n')
    else:
        errados.write(ip+'\n')
    
todos.close()
certos.close()
errados.close()
