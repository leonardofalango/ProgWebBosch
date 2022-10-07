
"""
import requests
def sinal():
    proxies = {'https': 'https://disrct:saladigital0311@10.224.200.26:8080'}
    url_temperatura = 'https://fb-py-esp-default-rtdb.firebaseio.com/Sensor/Thiago/Temperatura.json'
    url_umidade = 'https://fb-py-esp-default-rtdb.firebaseio.com/Sensor/Thiago/Umidade.json'
    temperatura = float(requests.get(url_temperatura, proxies=proxies).content)
    umidade = float(requests.get(url_umidade, proxies=proxies).content)
    return temperatura, umidade

import pyodbc
def InserirBD(sinal):
    server = 'JVLPC0524'
    database = 'Steicy-Arduino'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"INSERT dbo.Sensor (Temperatura, Umidade) VALUES ({sinal[0]},{sinal[1]});")
    cursor.commit()
    print("Inserido com sucesso!")

def apresentar(sinal):
    print(f"Temperatura: {sinal[0]}")
    print(f"Umidade: {sinal[1]}")
    
import time
while True:
    valores=sinal();
    apresentar(valores)
    InserirBD(valores)
    time.sleep(60)

"""
#=================================================================EX1=============================================================
def ex1():
    lista = []
    pesoMax = -999999
    try:
        for i in range(5):
            peso = int(input(f"Entre com o peso da pessoa {i+1}: "))
            lista.append(peso)
    except ValueError:
        print("ERRO: Apenas valores inteiros.")
    for i in range(len(lista)):
        if pesoMax < lista[i]:
            pesoMax = lista[i]
            index = i
    print(f"A pessoa mais pesada é a pessoa {index+1}, pesando {pesoMax}kg")
    
    



#=================================================================EX2=============================================================



def ex2():
    listaA = []
    listaB = []
    listaFinal = []
    tamanhoA = int(input("Entre com o tamanho da lista A: "))
    for i in range(tamanhoA):
        elemento = input(f"Entre com o Elemento {i} da lista A: ")
        listaA.append(elemento)
    tamanhoB = int(input("Entre com o tamanho da lista B: "))
    for i in range(tamanhoB):
        elemento = input(f"Entre com o Elemento {i} da lista B:")
        listaB.append(elemento)
    print(f"Lista A:\n{listaA}\nLista B:\n{listaB}")
    listaFinal.append(listaA)
    listaFinal.append(listaB)
    print("="*80,"\nLista:\n",listaFinal)
    i = -1
    j = -1
    while(i < 0 or i > tamanhoA):
        i = int(input("Digite a linha do Elemento que deseja remover: "))
    while(j < 0 or j > tamanhoB):
        j = int(input("Digite a coluna do Elemento que deseja remover: "))
    listaFinal[i].pop(j)
    print(f"Lista sem o item {i}, {j}:\n{listaFinal}")




#=================================================================EX3=============================================================



def ex3():
    lista = []
    valorMin = 99999
    tam = int(input("Entre com o tamanho da lista: "))
    try:
        for i in range(tam):
            elem = int(input(f"Entre com o valor do elemento {i+1}: "))
            lista.append(elem)
    except ValueError:
        print("ERRO: Apenas valores inteiros.")
    for i in range(len(lista)):
        if valorMin > lista[i]:
            valorMin = lista[i]
    print(lista)
    print(f"O valo minimo da lista: {valorMin}")



#=================================================================EX4=============================================================





def ex4():
    lista = []
    listaFinal = []
    for i in range(2):
        nome = input(f"Entre com o nome da pessoa {i+1}: ")
        tele = input(f"Entre com o telefone da pessoa {i+1}: ")
        idade = input(f"Entre com a idade da pessoa {i+1}: ") 
        lista.append(nome)
        lista.append(tele)
        lista.append(idade)
        
    for i in range(len(lista)):
        if lista[i].isdigit():
            listaFinal.append(lista[i])
    print(f"Elementos não numéricos: {listaFinal}")
    




#=================================================================EX5=============================================================


    
def ex5():
    lista1 = []
    lista2 = []
    lista = []
    tam = int(input("Entre com o tamanho da lista 1: "))
    for i in range(tam):
        elem = int(input(f"Entre com o valor do elemento {i+1}: "))
        lista1.append(elem)
    tam1 = int(input("Entre com o tam da lista 2: "))
    for i in range(tam1):
        elem = input(f"Entre com a String elemento {i+1}: ")
        while elem.isdigit() == True:
            elem = input(f"Entre com a String não numérica {i+1}: ")
        lista2.append(elem)
    lista.append(lista1)
    lista.append(lista2)
    lista[0].sort()
    lista[1].sort()
    print(f"Resultado: {lista}")


