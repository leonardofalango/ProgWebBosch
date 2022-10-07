# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:52:39 2022

@author: Leonardo Falango
"""

arq = open('03.banco_de_nomes.txt', mode='r')
arquivoFinal = open('03.banco_de_nomes_ordem.txt', mode='w+')

banco = []

for linha in arq:
    banco.append(linha)
    print(linha)
banco.sort()
for i in range(len(banco)):
    nome = banco[i]
    arquivoFinal.write(nome)
    print(f"Nome {nome} Registrado com sucesso!")
# OS NOMES ESTAO SALVOS COMO 'EXEMPLO \n'
# LOGO PRA PRINTAR E SALVAR ELES FICAM COM A QUEBRA DE LINHA


arq.close()
arquivoFinal.close()