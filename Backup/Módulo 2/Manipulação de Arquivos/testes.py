# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:09:23 2022

@author: Leonardo Falango
"""
# arquivo = open('meuarquivo.txt', mode='modo_de_uso')]
# modos 
# r =  somente leitura
# r+ = leitura + escrita, o ponteiro é colocado no início do arquivo
# w = escrita, apaga todas as informações e cria um arquivo caso nao exista, o ponteiro é colocado no início do arquivo
# w+ = escrita + leituraapaga todas as informações e cria um arquio caso nao exista, o ponteiro é colocado no início do arquivo
# a = escrita, mas NÃO apaga as coisas que estão escritas
# a+ = escrita + leitura, nao apaga as coisas que estão escritas

strings = []

arquivo = open("teste.txt", mode='r+')
for linha in arquivo:
    usuario, senha = linha.split('|')
    print('Usuário: {}\nSenha: {}'.format(usuario, senha))
arquivo.close()



# testes