# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 08:19:00 2022

@author: Leonaro Falango
"""

#=========================== EX 1 =======================


"""
def ex1():
    nota = float(input('\033[37m'+"Entre com a nota do aluno: "))
    if nota >= 0 and nota <= 10:
        
        if nota < 5:
            print('\033[31m'+'Nota: ', nota)
            
        elif nota >=5 and nota <= 8:
            print('\033[34m'+'Nota:',nota)
            
        else:
            print('\033[37m'+'Nota:',nota,'\nPARABÉNS')
    else:
        print('\033[37m'+"Valor da nota invalida")

ex1()
"""


#=========================== EX 2 =======================



"""
def ex2():
    nome = input("Digite o nome: ")
    confirmaNome = input("Digite novamente seu nome: ")
    if confirmaNome.lower() == nome.lower(): #lower() para tirar o case sensitive
        print("Nome Correto")
    else:
        print("Nome Errado")
ex2()
"""


#=========================== EX 3 =======================



"""
def ex3():
    capMax = float(input("Entre com a capacidade máxima do elevador: "))
    pessoas = []
    for i in range(5):
        pessoa = float(input(f"Entre com o peso da pessoa {i + 1}: "))
        pessoas.append(pessoa)
    if capMax < sum(pessoas):
        print("PESO MAXIMO EXCEDIDO")
    else:
        print("Pronto para subir")
    
ex3()
"""



#=========================== EX 4 =======================



"""
def ex4():
    ano = int(input("Entre com o ano: "))
    if ano % 400 == 0 or (ano%4 == 0 and ano%100 != 0):
        print("É um ano bissexto")
    else:
        print("Não é um ano bissexto")
ex4()
"""



#=========================== EX 5 =======================




"""
def ex5():
    numero = int(input("Entre com um numero até 1000: "))
    if numero>1000:
        print("Numero invalido")
        ex5()
    else:
        centenas = int(numero / 100)
        dezenas = int((numero-(centenas*100))/10)
        unidades = int(numero - (centenas*100 + dezenas*10))
        print(f'O numero {numero} possui {centenas} centenas, {dezenas} dezenas, {unidades} unidades.')
        
ex5()        
"""



#=========================== EX 6 =======================



"""
def ex6():
    nome = input("Entre com o nome do aluno: ")
    dias = 0
    while dias > 7 or dias <= 0:
        dias = int(input("Entre com o número de dias da semana: "))
    curso = input("Entre com o tipo de curso:\n(B) Básico\n(I) Intermediário\n(A) Avançado\n")
    if curso.lower() == "a" or curso.lower() == "avançado":
        total = dias*10*25
        print(f"O valor total do Curso Avançado é de: {total}")
    elif curso.lower() == "b" or curso.lower() == "básico":
        total = dias*7*15
        print(f"O valor total do Curso Básico é de: {total}")
    elif curso.lower() == "i" or curso.lower() == "intermediário":
        total = dias*8.5*20
        print(f"O valor total do Curso Intermediário é de: {total}")
    else:
        print("Valor invalido.")
        ex6()    
ex6()
"""



#=========================== EX 7 =======================


"""
def ex7():
    mesesb = []
    mesesb.append("janeiro")
    mesesb.append("fevereiro")
    mesesb.append("março")
    mesesb.append("abril")
    mesesb.append("maio")
    mesesb.append("junho")
    mesesb.append("julho")
    mesesb.append("agosto")
    mesesb.append("setembro")
    mesesb.append("outubro")
    mesesb.append("novembro")
    mesesb.append("dezembro")
    
    try:
        mes = int(input("Entre com o mês: "))
        if mes > 0 and mes <=12:
            if mes <= 7:
                if mes == 2:
                    print(f"O mes {mesesb[mes-1]} possui 28 dias.")
                elif mes%2 == 0:
                    print(f"O mês {mesesb[mes-1]} possui 30 dias.")
                else:
                    print(f"O mês {mesesb[mes-1]} possui 31 dias.")'
            elif mes > 7:
                if mes%2 == 0:
                    print(f"O mês {mesesb[mes-1]} possui 31 dias.")
                else:
                    print(f"O mês {mesesb[mes-1]} possui 30 dias.")
          
        else:
            print("Valor invalido")
        ex7()
    except ValueError:
        print("Valor inválido, apenas numeros inteiros são aceitos")

                     
ex7()
"""    
    
    
    
           
            
            
            