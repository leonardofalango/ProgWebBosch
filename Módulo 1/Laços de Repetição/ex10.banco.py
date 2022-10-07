# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:31:57 2022

@author: DISRCT
"""

def saldo():
    print("O valor do seu saldo é de: {:.02f}".format(usr))


def saque():
    global usr
    print("O valor disponível para saques é de: {:.02f}".format(usr))
    saque = float(input("Entre com o valor de saque: "))
    if saque > usr:
        print("Valor inválido.\nVocê possui disponível R${:.02f} para saques".format(usr))
    else:
        usr = usr - saque
        print("Saque feito.")
        saldo()

def deposito():
    global usr
    deposito = float(input("Entre com o valor do depósito: "))
    usr = usr + deposito
    saldo()



def menu():
    opcao = int(input("______________________________________________________________________________________\n(1) Consulta de saldo\n(2) Saque\n(3) Depósito\n(4) Sair\nEntre com a opção desejada: "))
    if opcao == 1:
        saldo()
        menu()
    elif opcao == 2:
        saque()
        menu()
    elif opcao == 3:
        deposito()
        menu()
    elif opcao == 4:
        pass
    else:
        print("Opção inválida")
        menu()


usr = 0

menu()
