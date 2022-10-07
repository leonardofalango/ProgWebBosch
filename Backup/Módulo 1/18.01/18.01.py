# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:20:59 2022

@author: LEONARDO FALANGO
"""

"""
#====================================== EX 1 ======================================


idade = "a"

nome = input("Entre com seu nome: ")

while(idade.isalpha() == True):
    idade = input("Entre com sua idade: ")
    
cidade = input("Entre com sua cidade: ")

print(f'\nNome: {nome}\nCidade: {cidade}\nIdade: {idade}')

"""
"""
#====================================== EX 2 ======================================

n1 = int(input("Entre com o primeiro numero: "))
n2 = int(input("Entre com o segundo numero: "))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
print(f'Soma: {soma}\nSubitração: {sub}\nMultiplicação: {mult}\nDivisão: {div}')
"""

"""
#====================================== EX 3 ======================================

dist = int(input("Entre com a distância total percorrida: "))
comb = int(input("Entre com o total de combustivel gasto: "))
kml = dist / comb
print("O automovel tem um consumo médio de",kml,"Km/L")
"""

"""
#====================================== EX 4 ======================================

numeroAlunos = int(input("Entre com a quantidade de alunos para calcular suas medias: "))
alunos = []

for i in range(numeroAlunos):
    nome = input("Entre com o nome do aluno: ")
    nota = []
    alunos.append(nome)
    
    for i in range (3):
        print("Entre com a nota da prova",i+1)
        nota.append(int(input()))
        tamanho = i+1;
    
    #soma = 0
    #for i in range(len(notas)):
       # soma += notas[i]
    soma = sum(nota)
    media = soma / tamanho
    print("Aluno: ",nome,"\nMédia:" , media)
print("Todos os alunos cadastrados:\n", alunos)
"""

"""
#====================================== EX 5 ======================================
a = "a"
b = "a"
while(a.isalpha() == True):
    a = input("Entre com o valor de A: ")
while(b.isalpha() == True):
    b = input("Entre com o valor de B: ")
a = int(a) #CASO QUEIRA FAZER CONTAS COM A E B
b = int(b)
print(f'Valor de A: {a}\nValor de B: {b}')
aux = a 
a = b
b = aux
print(f'Resultado da troca:\nValor de A: {a}\nValor de B: {b}')
"""

"""
#====================================== EX 6 ======================================

celsius = float(input("Entre com a temperatura em graus Celsius: "))
fahrenheit = (9* celsius + 180) / 5
print(f'A temperatura em graus Fahrenheit é: {round(fahrenheit, 2)}')

"""


"""
#====================================== EX 7 ======================================
cotDolar = float(input("Entre com o valor da cotação do dólar hoje: "))
dolar = float(input("Quantos dólares você irá converter em reais: "))
valor = dolar*cotDolar
print('O valor de U${:.2f} em reais é R${:.2f}'.format(dolar,valor))
"""



"""
#====================================== EX 8 ======================================

nota1 = float(input("Entre com o valor da nota 1 (Peso 4): "))
nota2 = float(input("Entre com o valor da nota 2 (Peso 6): "))
media = (nota1*4 + nota2*6) /10
print(f'A média das notas: {media}')
"""




"""
#====================================== EX 9 ======================================
def menu():
    byte = float(input("Entre com o valor em bytes: "))
    opcao = int(input("(1) Calcular giga como 1.073.741.824 bytes\n(2) Calcular giga como: 1.000.000.000 bytes\n"))
    if opcao == 1:
        giga = 1073741824
        gigabytes = byte / giga
        print(f'Valor de 1 gigabyte: {giga} bytes\nValor de {byte} em gigabytes: {gigabytes}')
    elif opcao == 2:
        giga = 1000000000
        gigabytes = byte / giga
        print(f'Valor de 1 gigabyte: {giga} bytes\nValor de {byte} em gigabytes: {gigabytes}')
    else:
        menu()
menu()
"""




"""
#FIBONACCI
n = 0
while n <= 0:
    n = int(input("Entre com um numero: "))


def fibonacci(n):
    numero = 1
    num = 0
    print(1)
    if n == 1:
        pass
    elif n == 2:
            print(1)
    else:
        for i in range(n):
            fib = numero + num
            num = numero
            numero = fib        
            print(fib)
    
fibonacci(n)


"""

 