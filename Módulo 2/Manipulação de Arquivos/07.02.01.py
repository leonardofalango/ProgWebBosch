# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:29:33 2022

@author: Leonardo Falango
"""

contador = 1

def verificaIP(ip):
    ips = ip.split(".")
    if len(ips) > 4 or len(ips) < 3:
        return False
    try:
        for i in range(len(ips)):
            if int(ips[i]) < 1000 and int(ips[i]) >= 0:
                pass
            else:
                return False
        return True
    except ValueError:
        return False




arquivo = open('01.banco_de_ip.txt', mode='a+')
entrada = '   '
while True:
    entrada = input(f"Entre com o enereço de ip {contador}: ")
    ip_certo = verificaIP(entrada)
    if entrada == '':
        break
    while ip_certo == False:
        print("Endereço de ip inválido. Aperte enter para salvar as entradas.\nEx: 128.128.128.128")
        entrada = input(f"Entre com o enereço de ip {contador}: ")
        ip_certo = verificaIP(entrada)
        if entrada == '':
            break
    if entrada == '':
        break
    arquivo.write('\n'+entrada)
    contador += 1
arquivo.close()




