# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:23:03 2022

@author: Leonardo Falango
"""

banco_de_dados = open('Banco.txt', 'r+')

# preco_total = 0

# for linha in banco_de_dados:
#     produto, preco = linha.split(':')
#     preco = float(preco)
#     preco_total += preco
#     print(f'Produto: {produto}\nPreço: {preco}\n\n')

# banco_de_dados.close()
# print(f'Preço total dos produtos: {preco_total}')




banco_de_dados = open('Banco.txt', 'r+', encoding='utf-8')

preco_total = 0

produtos = []
preco_produtos = []
carrinho = []

for linha in banco_de_dados:
    produto, preco = linha.split(':')
    preco = float(preco)
    produtos.append(produto)
    preco_produtos.append(preco)
    print(f'Produto: {produto}\nPreço: {preco}\n\n')

while True:
    try:
        entrada = input("Entre com o produto que você quer: ")
        if entrada == '':
            break
        for i in range(len(produtos)):
            if produtos[i].lower() == entrada.lower():
                preco_total += preco_produtos[i]
                carrinho.append(produtos[i])
                print(f"Carrinho: {carrinho}\nTotal: {preco_total}")
                confir = 1
                break
                
            elif entrada.isdigit() == True:
                
                entrada = int(entrada)
                preco_total += preco_produtos[entrada]
                carrinho.append(produtos[entrada])
                print(f"Carrinho: {carrinho}\nTotal: {preco_total}")
                confir = 1
                break
        else:
            confir = 0
        if confir == 0:
            print('Produto não encontrado.')
            continue
        else:
            pass
    except IndexError:
        print('Produto não encontrado.')
        continue
    
    
    
banco_de_dados.close()
print(f'Valor total: {preco_total}')


