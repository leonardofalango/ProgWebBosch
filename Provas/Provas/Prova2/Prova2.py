# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 08:08:07 2022

@author: Leonardo Falango
"""
# =============================================================================
# Importando as Blibliotecas necessárias
# =============================================================================
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
import time
'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- PROVA 2 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 1 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
# 1) Crie uma  array 5x5 com números inteiros aleatórios. Depois utilize uma condição para substituir
# os números ímpares desse array por 0. Printe os dois arrays

# Criando a array inicial
array = np.random.randint(10,size=25) # Crianado um array de 25 números completo por números aletórios
array = np.resize(array, (5,5)) # Mudando o tamanho do array para 5x5
print(f'A array original:\n{array}\n') # Printando o  array inicial
count=0
#colocanhdo a condição
impares = array % 2 != 0
for i in impares:
    for j in i:
        if j:
            count+=1
array[impares] = array[impares]**2 # Alterando os valores que sao impares, para 0
print(f'A array substituindo os números ímpares: \n{array}\n') # Printando o array com as substituições
arquivo=open("Impares.txt","a")
arquivo.write(f"{count} números ímpares foram encontradas\n")
arquivo.close()
arquivo2 = open("Impares.txt","r")
reg=len(arquivo2.read().split("\n"))
print(f"Existem {reg} registros.")






# '''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 2 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# '''
# # 2) Um cliente deseja comprar uma casa no Rio de Janeiro. 3 Quartos, Barra da Tijuca, área > 130m²
# # Opção mais barata presente na tabel

# dfcasas = pd.read_csv("Dados/dados.csv", encoding='latin-1') # Enconding latin-1 para funcionar o dataframe
# dfcasas = dfcasas[dfcasas['bairro'] == 'Tijuca'] # Mudando o dataframe para aparecer apenas os que são do bairro Tijuca
# dfcasas = dfcasas[dfcasas['area'] > 130] # Alterando o dqataframe para aparecer apenas os que tem 130m² pra cima
# dfcasas = dfcasas.sort_values(by='preco') # Ordenando o dataframe por preço, do menor para o maior
# print(dfcasas.head(1)) # Pegando o primeiro valor do DataFrame







# '''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 3 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# '''
# # 3) Plote um gráfico mostrando a quantidade de gol dos times paranaenses em cada ano da década.
# import numpy as np
# import pandas as pd
# dffut = pd.read_csv('Dados/gols_pr.csv', encoding='utf-8')


# #Separando os dataframes
# cwb = dffut[dffut['clube'] == 'coritiba'] # Criando um DataFrame apenas com o clube Coritiba
# atle = dffut[dffut['clube'] == 'athletico-pr'] # Criando um DataFrame apenas com o clube Athletico
# parana = dffut[dffut['clube'] == 'parana'] # Criando um DataFrame apenas com o clube Paraná



# #plotando coritiba
# plt.plot(cwb['ano'], cwb['gols_pro'], c='green', label='Coritiba', marker='o')
# #plotando athletico
# plt.plot(atle['ano'], atle['gols_pro'], c='r', label='Athlético-pr', marker='o')
# #plotando parana
# plt.plot(parana['ano'], parana['gols_pro'], c='blue', label='Paraná', marker='o')

# #mostrando a legenda e o plot
# lista = []
# for i in range(2010,2020,1):
#     lista.append(i) #Criando uma lista de valores para x, poderia criar como: [2010,2011,2012...]
# plt.grid(True) #Grade
# plt.title("Gols dos times paranaenses na década") #Título
# plt.xticks(lista) #Lista criada de 2010 até 2019, de 1 em 1 --> [2010,2011,2012...,2019]
# plt.legend()#Plotar a legenda
# plt.show()







# '''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 4 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# #'''
# # 4) Plote dois graficas na mesma figura utilizando o subplots, f(x)=x² e g(x) = x³

# fig, eixo = plt.subplots(nrows=1, ncols=2, figsize=(12,12)) # Criando os eixos do subplot


# x = np.arange(-20,21,1)
# # setando os eixos
# # Primeiro eixo, com o f(x) = x²
# eixo[0].plot(x, x**2, c='blue', linewidth=5)
# eixo[0].set_title('f(x) = x²')

# # Segundo eixo, com o g(x) = x³
# eixo[1].plot(x, x**3, c='red', linewidth = 5)
# eixo[1].set_title('g(x) = x³')

# plt.show()




# '''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 5 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# '''
# # 5) A partir da planilha 'flights.csv' plote um grafico através da lib seaborn do tipo barras horizontais

# dfvoo = pd.read_csv('Dados/flights.csv')
# dfvoo = dfvoo[dfvoo['year'] == 1950]

# # plotando com seaborn
# sns.barplot(x='passengers', y='month', data=dfvoo) # Plotando o gráfico de barras
# plt.show()








# '''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 6 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# '''

# # 6) Crie um programa que remova o efeito sal e pimenta da foto "mulher.png"

# img = cv2.imread('Dados/mulher.png')
# img1 = cv2.GaussianBlur(img, (7,7), 0) # Testando a imagem com glaussianblur
# img2 = cv2.blur(img,(6,6)) # Testando a imagem com o blur padrão
# img3 = cv2.medianBlur(img, 3) # Testando a imagem com o blur médio


# cv2.imshow('Imagem Original', img) # Printando a imagem original
# #cv2.imshow('Gaussian Blur', img1) # Printando a imagem com o Glaussian Blur, não ficou tão bom
# #cv2.imshow('Blur Padrao', img2) # Printando a imagem com o Blur padrão, também nao ficou tão bom
# cv2.imshow('Blur Medio', img3) # Melhor efeito dentre os testados
# cv2.waitKey(0) & 0xFF # Esperar até que o usuário aperte alguma tecla
# cv2.destroyAllWindows() # Fechar as janelas de imagem








# '''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 7 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# '''
# # 7) Edite o vídeo 'flor.mp4' virando ele de ponta cabeça e transformando o espaço de cor de RGB para BGR
# # Salve o novo vídeo como "nova_flor.mp4" fps =30 e dimensão 1280x720


# cap = cv2.VideoCapture('Dados/flor.mp4') # Abrindo  o vídeo
# fourcc = cv2.VideoWriter_fourcc(*'DIVX') # codex
# framesporsec = 30 # Settando os frames por segundo
# width, height = 1280,720 # Largura e Altura
# output = cv2.VideoWriter("nova_flor.mp4", 0, framesporsec, (width,height)) # OUTPUT, será o vídeo que vai ser salvo,
#                             # Vai ser salvo no diretório "Provas", não no diretório aonde está salvo o arquivo original

# while (cap.isOpened()):
#     ret, frame = cap.read() # ret, vai ser o return se o vídeo ainda está rodando
#     if ret == False: # Quando o vídeo acabar
#         break # Sai do loop
#     frame_correto = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Criando um outro frame, alterando o frame original de RGB para BGR
#     frame_correto = cv2.flip(frame_correto,0) # Flippando frame por fram enquanto o vídeo estiver rodando
#     output.write(frame_correto) # Colocando frame por frame no output
#     cv2.imshow('output', frame_correto) # Mostrando apenas o frame já modificado para o usuário
# output.release()
# cap.release()
# cv2.destroyAllWindows()







# '''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercício 8 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# '''
# # 8) Crie um programa que move todos os arquivos de uma pasta para outra pasta. A cada arquivo movido, deve-se escrever um JSON
# # Contendo 3 dados: Caminho antigo, Caminho novo, timeStamp da mudança de pasta


# def mover(diretorio, novo):

#     pasta = os.path.join(novo)

#     if not os.path.isdir(pasta): # Se o diretório novo, não for um diretório, ele cria um diretório
#         os.mkdir(pasta)

#     lista = os.listdir(diretorio) # Listar os itens (arquivos,pastas, etc) do diretorio de origem
   
#     for arquivo in lista: # Mover todos os itens que estão nesse diretório
#         try:
#             origem = os.path.join(diretorio, arquivo) # Entrando no diretório de origem
#             destino = os.path.join(diretorio,pasta,arquivo) # Entrando no diretório de destino
#             os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio,pasta,arquivo)) # Mudando o arquivo de pasta
            
#             json1 = {"Caminho Antigo" : origem, "Caminho Novo" : destino, "timeStamp" : time.ctime()} # Criando um dicionário para colocar em JSON
#             print(json.dumps(json1)) # Mudando o dicionário criado para JSON
#         except PermissionError: # Esse erro acontece quando o arquivo que você está tenatndo mover é um diretório, não arquivo
#             continue
        
    
# # Chamando a função para mover todos os itens da pasta "Ex08", para a "Nova_pasta", dentro da pasta "Ex08"
# mover("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Ex08", "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Ex08/Nova_pasta")













