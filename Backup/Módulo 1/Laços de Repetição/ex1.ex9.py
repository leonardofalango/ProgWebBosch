# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:44:55 2022

@author: DISRCT
"""




"""
#============================================================================== EX 1 ==============================================================================


total = 0
for i in range(5):
    x = int(input(f"Entre com o valor do número {i+1}: "))
    total += x
print(f"A soma de todas as variaveis: {total}")




#============================================================================== EX 2 ==============================================================================

lista = []
maximo = -999999
try:
    for i in range(10):
        peso = int(input(f"Entre com o valor {i+1}: "))
        lista.append(peso)
except ValueError:
    print("ERRO: Apenas valores inteiros.")
for i in range(10):
    if maximo < lista[i]:
        maximo = lista[i]

print(f"O maior valor entre os 10 é: {maximo}")
print(f"O menor valor entre os 10 é: {min(lista)}")







#============================================================================== EX 3 ==============================================================================

input("Aperta qualquer tecla.")
valores = [] #Caso for usar algum valor
for i in range(1000, 2000):
    valores.append(i)
    print(i)





#============================================================================== EX 4 ==============================================================================



pares = []
impares = []
i = 0
while True:
    try:
        numero = int(input(f"Entre com o numero {i+1}: "))
    except ValueError:
        print("ERRO: Apenas valores inteiros.")
    if numero > 1000:
        break
    elif numero % 2 == 0:
        pares.append(numero)
    elif numero %  2 != 0:
        impares.append(numero)
somaPar = sum(pares)
somaImpar = sum(impares)
print(f"A soma dos numeros pares:\n{pares}\nÉ igual: {somaPar}\nA soma dos numeros impares:\n{impares}\nÉ igual: {somaImpar}")






#============================================================================== EX 5 ==============================================================================



numerosPar = []
numerosImpar = []

for i in range(10):
    try:
        numero = int(input(f"Entre com o numero {i+1}: "))
    except ValueError:
        print("ERRO: Apenas valores inteiros.")
   
    if numero % 2 == 0:
        numerosPar.append(numero)
    else:
        numerosImpar.append(numero)
print(f"Numeros impares: {numerosImpar}\nNumeros pares: {numerosPar}")





#============================================================================== EX 6 ==============================================================================



lista = []
for i in range(8):
    try:
        numero = int(input(f"Entre com o numero {i+1}: "))
    except ValueError:
        print("ERRO: Apenas valores inteiros.")
    lista.append(numero)
lista.sort(reverse = True)
print(f"Lista: {lista}")


#============================================================================== EX 7 ==============================================================================

lista = []

for i in range(10):
    try:
        numero = int(input(f"Entre com o numero {i+1}: "))
    except ValueError:
        print("ERRO: Apenas valores inteiros.")
    
    if numero < 0:
        numero = 0
    lista.append(numero)

print(f"Lista sem valores negativos: {lista}")





#============================================================================== EX 8 ==============================================================================



numero = int(input("Entre com o número: "))
for i in range(10):
    print(f"{numero} x {i+1} = {numero*(i+1)}")





#============================================================================== EX 9 ==============================================================================


todos = []
anterior = 0
atual = 1
while anterior != atual:
    atual = int(input("Entre com o número: "))
    todos.append(atual)
    for i in range(len(todos) - 1):
        anterior = todos[i]
        if anterior == atual:
            print(f"A soma da lista {todos}\nÉ de {sum(todos)}")
            break
        else:
            pass
    print(f"A soma da lista {todos}\nÉ de {sum(todos)}")








"""



#============================================================================== EX 10 ==============================================================================




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



#Para iniciar apenas descomentar a linha 236
#menu()








#============================================================================== EX 11 ==============================================================================





def calculadora():
    x = float(input("Entre com o valor de x: "))
    y  = float(input("Entre com o valor de y: "))
    opcao = int(input("Entre com a opção:\n(1) Soma\n(2) Subtração\n(3) Divisão\n(4) Multiplicação"))
    if opcao == 1:
        print(x+y)
    elif opcao == 2:
        print(x-1)
    elif opcao == 3:
        print(x/y)
    elif opcao == 4:
        print(x*y)
    else:
        print("Valor inválido")
        calculadora()



#Para iniciar apenas descomentar a linha 270
#calculadora()




#============================================================================== EX 12 ==============================================================================


votoMS = 0
votoAR = 0
votoCS = 0
voto = 0
votoNulo = 0
votoBranco = 0
candidatos = ["Maria Santos", "Carlos Silva", "Antônio Rocha", "NULO", "Branco"]


def urna():
    
    global votoMS,votoCS, votoAR, votoNulo, candidatos, voto, votoBranco
    
    
    votos = [votoMS, votoCS, votoAR, votoNulo, votoBranco]
    print("_"*30,"Urna","_"*30)
    try:
        opcao = int(input("1. Candidato Maria Santos \n2. Candidato Carlos Silva \n3. Candidato Antônio Rocha \n4. Nulo \n5. Branco\nEntre com seu voto:"))
        
    except ValueError:
        print("ERRO: Apenas números inteiros são aceitos.")
        urna()
        
    if opcao == 1:
        votoMS += 1
        voto += 1
        urna()
        
    elif opcao == 2:
        votoCS += 1
        voto += 1
        urna()
        
    elif opcao == 3:
        votoAR += 1
        voto += 1
        urna()
        
    elif opcao == 4:
        votoNulo += 1
        voto += 1
        urna()
        
    elif opcao == 5:
        votoBranco += 1
        
        for i in range(len(candidatos)):
            print(f"\nCandidato: {candidatos[i]}\n Votos: {votos[i]}")
        print("Porcentagem de votos nulos: {:.02f}%".format(votoNulo * 100 / voto))
        print("Porcentagem de votos brancos: {:.02f}%".format(votoBranco * 100 / voto))
        maior = (max(votos))
        ind = votos.index(maior)
        
        
        
        if ind > 2:
            print("Eleição cancelada.")
            urna()
        else:
            vencedor = candidatos[ind]
            print(f"O candidato vencedor: {vencedor}")
            urna()
    else:
        print("Valor invalido")
        urna()
 
#Para iniciar apenas descomentar a linha 345
#urna()
        





#============================================================================== EX 13 ==============================================================================




def fibonacci(n):
    numeros = [1,1]
    anterior = numeros[0]
    atual = numeros[1]
    limite = n
    ind = 0
    while atual <= limite:
        aux = atual
        atual = atual+anterior
        anterior = aux
        numeros.append(atual)
        ind = ind + 1
        
    ind += 1
    numeros.pop(ind)
        
    return numeros





def fibo():
    fib = 1
    n = int(input("Entre com o limite: "))
    if n < 1:
        print("Valor inválido")
        fibo()
    elif n == 1:
        print("1")
    elif n == 2:
        print("[1,1]")
    else:
        fib = fibonacci(n)
        print(fib)
 
#Para iniciar apenas descomentar a linha 394
#fibo()










#============================================================================== EX 14 ==============================================================================



def ibge(banco_de_dados):
    print("="*30,"IBGE","="*30,"\n(A) Média dos salarios.\n(B) Maior e menor idade.\n(C) Quantidade de mulheres.\n(D) Pessoa que possui o menor salário.")
    opcao = input("\nEntre com a opção: ")
    sexos = []
    salarios = []
    idades = []
    for i in range(len(banco_de_dados)):
            idades.append(banco_de_dados[i][0])
            
            sexos.append(banco_de_dados[i][1])
        
            salarios.append(banco_de_dados[i][2])
    
    opcao = opcao.lower()
    if opcao == "a" or opcao == "media":
        media = sum(salarios)
        tamanho = len(salarios)
        media = media/tamanho
        print("A media dos salários é de: {:.02f}".format(media))
    elif opcao == "b" or opcao == "maior":
        maioridade = max(idades)
        menoridade = min(idades)
        print("Maior idade do grupo {}({})\nMenor idade do grupo: {}({})".format(maioridade, sexos[idades.index(maioridade)], menoridade, sexos[idades.index(menoridade)]))
    elif opcao == "c" or opcao == "mulheres":
        quant_pessoas = len(sexos)
        quant_mulheres = 0
        for i in range(quant_pessoas):
            if sexos[i] == "F":
                quant_mulheres += 1
        print("A quantidade de Mulheres no grupo é de: {}".format(quant_mulheres))
    elif opcao == "d" or opcao == "menor":
        salario_min = min(salarios)
        ind = salarios.index(salario_min)
        sexo_pessoa_min = sexos[ind]
        print("O menor salário é de: {}".format(salario_min))
        if sexo_pessoa_min == "F":
            print("Sendo uma mulher que recebe esse salário.")
        else:
            print("Sendo um homem que recebe este salário")


entrada = -1
#Caso banco de dados pre-existente:
#banco = [ [17, "M", 1500], [19, "F", 1800], [18, "M", 1985], [22, "F", 9000], [25, "F", 680]]
banco = []

while True: 
    pessoa= []  #RESETA TODO LOOP
    print("================================= CADASTRO DE PESSOAS ===================================")
    try: 
        entrada = int(input("Entre com a idade: "))
    except ValueError:
        print("Pessoa não cadastrada.")
        break
    if entrada > 0:
        print("Pessoa não cadastrada.")
        pessoa.append(entrada)

    else:
        print("Pessoa não cadastrada.")
        break
    
    entrada = input("Entre com o sexo (M) ou (F): ")
    if entrada.lower() == "m":
        entrada = "M"
        pessoa.append(entrada)
    elif entrada.lower() == "f":
        entrada = "F"
        pessoa.append(entrada)
    else:
        print("Entrada inválida.\nPessoa nao cadastrada.")
        break
        
    try:    
        entrada = int(input("Entre com o salário: "))
    except ValueError:
        print("Pessoa não cadastrada.")
        break
    
    if entrada > 0:
        pessoa.append(entrada)
    else:
        print("Pessoa não cadastrada.")
        break
    banco.append(pessoa)

print(f"\nO Banco de dados: {banco}\n\n")



#Para iniciar apenas descomentar a linha 500 e 501
#while True:
#   ibge(banco)
        

        