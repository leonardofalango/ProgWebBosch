# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 08:01:35 2022

@author: Leonardo Falango
"""

#===========================================================EX 1==================================================
#Crie um programa que recebe um valor em dólar americano do usuário e printa o valor em reais

#Considere 1 USD = 3,77 (10/07/2019)


def conversao(moeda1, moeda2):
    valor_final = moeda1 / moeda2
    return valor_final



#while True: #Para deixar o programa em loop

try:
    reais = float(input("Entre com o valor em Reais: ")) #Pedindo para o usuario entrar com o valor em reais e armazenando em uma variável chamada reais
    if reais < 0:
        print("Erro. Entrada inválida")
    else:
        dolar = 3.77
        dolares = conversao(reais,dolar) #Chamando a função de conversão
        print("O valor de R${:.02f} em dólares é: U${:.02f}".format(reais, dolares)) #Printando o valor formatado
except ValueError:
    print("Erro. Entrada inválida") #Tratamento de erro caso a entrada nao seja um float.



#===========================================================EX 2==================================================
#Crie um programma que mostre o cardápio do BIG MANIA COMBOS para o usuário, ele escolhe qual combo quer, e o programa retorna o valor da compra
cardapio_bigmania = [["Combo 1", "X Salada + Fritas + KS (sabores)", 23.99], ["Combo 2", "X Picanha Bacon + Fritas + KS sabores", 27.99], 
            ["Combo 3", "X Calabresa Vinagrete + Nuggets + KS sabores", 26.99], ["Combo 4", "X Frango Salada + Anéis de Cebola + KS sabores", 25.99], 
            ["Combo 5", "Duplo Cheddar Bacon + Fritas + KS sabores", 32.99], ["Combo KIDS", "X Burguer + Batata Sorriso + Coca 200ml ou Suco (consulte) + Danoninho", 16.99],
            ["Lanche 1","Duplo Cheddar Bacon", 27.00], ["Lanche 2","KIDS", 6.00]]





#Definindo o cardápio 


#Função cardápio que serve para printar o cardápio: 
def cardapio():
    global cardapio_bigmania
    print("="*30)
    print("Cardapio do BIG MANIA COMBOS: ")
    for combos in range(len(cardapio_bigmania)):
        print("="*15,"Opção",combos+1,"="*15)
        for descricao in range(3):
            print(cardapio_bigmania[combos][descricao])
        print("="*30,"\n")
    print("Para consultar o preço apenas dos lanches, opção 7.")
    print("Para finalizar sua compra, opção 0.")
        


opcao = 99999 #Definindo a opcao como um numero positivo para entrar no while: 

escolha = [] #Criando a lista de escolha do usuário

total = 0 #Criando o valor final do usuário para somar com as opções dele

while opcao > 0: #Chamando a funcao de printar o cardápio até o usuario digitar 0 ou números negativos
    cardapio()
    try:
        opcao = int(input("Entre com a opcao: "))
    except ValueError:
        print("Erro. Entre com uma opção válida")
        continue
    if opcao == 1: #Se o usuario escolher a opcao 1:
        escolha.append(cardapio_bigmania[opcao-1]) #As escolhas do usuário são salvas em uma lista
        total = total + cardapio_bigmania[opcao-1][2] #Para ir somando o total, porem eu fiz com listas, entao tem como usar o sum()
    elif opcao == 2:
        escolha.append(cardapio_bigmania[opcao-1]) #O indice '[opcao + 1]' pois a lista de opcoes começa com indice 0, porem estamos pedindo para o usuario a opção de Combo, que começa em 1
        total = total + cardapio_bigmania[opcao-1][2] #O indico '[2]' é o indice do valor do combo ou do lanche
    elif opcao == 3:
        escolha.append(cardapio_bigmania[opcao-1])
        total = total + cardapio_bigmania[opcao-1][2]
    elif opcao == 4:
        escolha.append(cardapio_bigmania[opcao-1])
        total = total + cardapio_bigmania[opcao-1][2]
    elif opcao == 5:
        escolha.append(cardapio_bigmania[opcao-1])
        total = total + cardapio_bigmania[opcao-1][2]
    elif opcao == 6: #Se o usuário escolher a opcao de combo KIDS
        escolha.append(cardapio_bigmania[opcao-1])
        total = total + cardapio_bigmania[opcao-1][2]
    elif opcao == 7:
        escolha.append(cardapio_bigmania[opcao-1])
        total = total + cardapio_bigmania[opcao-1][2]
    elif opcao == 8:
        escolha.append(cardapio_bigmania[opcao-1])
        total = total + cardapio_bigmania[opcao-1][2]
    elif opcao == 0:
        break
    else:
        print("Entre com uma opção válida")
        continue

confirmar = input(f"Confirmar pedido: {escolha}\nValor: R${total}\nConfirmar? (s/n)") #Retornando ao usuário o valor da compra

if confirmar.lower() == "sim" or confirmar.lower() == "1" or confirmar.lower() == "s": #Se a resposta for sim, a compra é confirmada
    print(f"Pedido confirmado!\nValor da compra: {total}")
else: #Se a resposta for não, ou qualquer coisa diferente de sim, a compra é cancelada
    print("Compra cancelada!")


    
    
#===========================================================EX 3====================================================
#Utilize a função "while" para cirar um programa que multiplique o número definido pelo usuário por 2, e o adicione numa lista, até o usuario mandar parar.
    
lista_2 = []
while True:
    try:
        x = float(input("Entre com o número: "))
    except ValueError:
        print("Erro. Entrada inválida") #É possivel colocar o 'break' para quando o usuário digitar algo inválido concluir a lista.
        continue
    if x == 0: #Porém, eu prefiro usar um número caso o usuário deseja parar de entrar com números
        break
    else:
        lista_2.append(x*2) #Colocando o número do usuário multiplicado por 2 numa lista
        print(f"Lista: {lista_2}")
    print("Entre com '0' para finalizar a lista.") #Mostrando como parar de adicionar numeros a lista para o usuário
    
print(f"A lista com as entradas multuplicadas por 2: {lista_2}") #Printando a lista com os números que o usuário colocou multiplicados por 2




#===========================================================EX 4====================================================
#Crie um programa de uma calculadora que faça soma, subtração, divisão e multiplicação.

def entrada_numeros():
    entrada = 0
    entrada2 = 0
    try:
        entrada = float(input("Entre com o número: "))
        entrada2 = float(input("Entre com o segundo número: "))
        return entrada, entrada2
    except ValueError:
        pass



def calculadora():
    operacao = 0
    x=0
    y=0
    print("\n(1) Soma\n(2) Subtração\n(3) Divisão\n(4) Multiplicação")
    try:
        operacao = int(input("Entre com a opção: "))
    except ValueError:
        print("Erro. Entrada inválida.")
        calculadora()   
    
    try:
        if operacao == 1: #Verificando a entrada do usuário para saber qual operação ele quer fazer
            x,y = entrada_numeros()
            soma = x+y
            print(f"{x} + {y} = {soma}") #Printando para o usuário a soma dos números
        elif operacao == 2:
            x,y = entrada_numeros()
            subtracao = x - y
            print(f"{x} - {y} = {subtracao}")
        elif operacao == 3:
            x,y = entrada_numeros()
            try:
                divisao = x / y
                print(f"{x} / {y} = {divisao}")
            except ZeroDivisionError:
                print("Impossível dividir por 0")
            
        elif operacao == 4:
            x,y = entrada_numeros()
            multiplicacao = x * y
            print(f"{x} * {y} = {multiplicacao}")
        
        else:
            print("Operação inválida.")
            calculadora()
    except TypeError:
        print("Erro. Entrada inválida")
        calculadora()
calculadora()  
    


#===========================================================EX 5====================================================
#Faça um programa semelhante ao seguinte, mas que conte de 0 até um valor definido pelo usuário. (Cire uma função def count)

def count(fim):
    if fim > 0:
        for i in range(fim+1):
            print(i)
    elif fim < 0:
        for i in range(-fim+1):
            if i == 0:
                print("0")
            else:
                print(f"-{i}")

try:
    entradausuario = int(input("Entre com o valor final: "))
except ValueError:
    print("Erro. Entrada inválida.")
count(entradausuario)
    




#===========================================================EX 6====================================================
#Crie um programa que recebe um número do usuário e diz se esse número é primo ou nao. O programa deve se repetir até que um numero escolhido seja primo.


def primo(numero):
    contador = 0
    if numero == 0 or numero == 1:
        print(f"o número {numero} não é primo")
        return 0
    for i in range(1,numero+1,1):
        if numero % i == 0: #Primeiro i, vai ser = 0, entao 0/x será sempre 0
            contador += 1 #Quando o numero for divisivel pelo i, adiciona-se 1 ao contador
    if contador > 2: #3 pois o 1 e o próprio numero vão ser divisiveis
        print(f"O número {numero} não é primo.")
        return 0
    else:
        print(f"O número {numero} é primo.")
        return 1

while True:
    try:
        x = int(input("Entre com o número: "))
    except ValueError:
        print("Erro. Entrada inválida")
        continue
    ehprimo = primo(x)
    if ehprimo == 1:
        break




#===========================================================EX 7====================================================

hora24 = input("Entre com a hora: ")

try:
    hora,minuto = hora24.split(":") #Dividindo a hora em horas e minutos
    hora = int(hora)
    minuto = int(minuto)
    if hora > 24 or hora < 0 or minuto > 60 or minuto < 0:
        print("Entrada inválida")
    else:
        if hora >= 0 and hora < 12:
            print(f"Hora convertida: {hora}:{minuto} A.M.")
        elif hora >= 12 and hora < 25:
            print(f"Hora convertida: {hora-12}:{minuto} P.M.")
except ValueError:
    print("Erro. Entrada inválida")
