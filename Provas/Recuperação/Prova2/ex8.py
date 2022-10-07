# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:31:23 2022

@author: Leonardo Falango
"""
import json
import os
import time

# 8) Crie um programa que move todos os arquivos de uma pasta para outra pasta. A cada arquivo movido, deve-se escrever um JSON
# Contendo 3 dados: Caminho antigo, Caminho novo, timeStamp da mudança de pasta


def mover(diretorio, novo):

    pasta = os.path.join(novo)

    if not os.path.isdir(pasta): # Se o diretório novo, não for um diretório, ele cria um diretório
        os.mkdir(pasta)

    lista = os.listdir(diretorio) # Listar os itens (arquivos,pastas, etc) do diretorio de origem
   
    for arquivo in lista: # Mover todos os itens que estão nesse diretório
        try:
            origem = os.path.join(diretorio, arquivo) # Entrando no diretório de origem
            destino = os.path.join(diretorio,pasta,arquivo) # Entrando no diretório de destino
            os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio,pasta,arquivo)) # Mudando o arquivo de pasta
            
            json1 = {"Caminho Antigo" : origem, "Caminho Novo" : destino, "timeStamp" : time.ctime()} # Criando um dicionário para colocar em JSON
            print(json.dumps(json1)) # Mudando o dicionário criado para JSON
        except PermissionError: # Esse erro acontece quando o arquivo que você está tenatndo mover é um diretório, não arquivo
            continue
        
    
# Chamando a função para mover todos os itens da pasta "Ex08", para a "Nova_pasta", dentro da pasta "Ex08"
            
mover("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Recuperação/Prova2/Ex8", 
      "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Recuperação/Prova2/Nova Pasta")
