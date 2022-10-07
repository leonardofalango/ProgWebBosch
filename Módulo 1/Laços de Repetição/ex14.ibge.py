# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:34:48 2022

@author: DISRCT
"""

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



while True:
   ibge(banco)
        

        