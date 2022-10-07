# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:11:50 2022

@author: Leonardo Falango
"""

import random as rd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas


'''----------------------------------------EX1-----------------------------------------'''
#1) Crie um array 4x4 com números inteiros aleatórios 
#(pesquisar: np.random.randint()). 
#Depois utilize uma condição para substituir os números pares desse array por 0. 
#Printe os dois arrays


lista_ini= []
for i in range(4):
    lista_aux = []
    for j in range(4):
        lista_aux.append(rd.randint(0,9))
    lista_ini.append(lista_aux)

array_ini = np.array(lista_ini)

print(array_ini)
par = (array_ini % 2 == 0)
array_ini[par] = 0
print(f'\n{array_ini}')



'''----------------------------------------EX2-----------------------------------------'''

#2) Uma pessoa quer comprar um apartamento, e deseja ver as melhores opções.
#Mostre os dados em um Dataframe (dados.csv) com as seguintes condições:
#•	O apartamento deve ser no bairro Botafogo;
#•	Deve ter no mínimo 2 quartos;
#•	Mostre as 5 opções de menor preço;


dfdados = pandas.read_csv('Dados/dados.csv', encoding='utf-8')
dfdados = dfdados[dfdados['bairro'] == 'Botafogo'] # O próprio DataFrame esta diminuindo de tamanho com isso, mas como eu só vou usar ele para fazer isso, é tranquilo.
dfdados = dfdados[dfdados['quartos'] >= 2]
dfdados = dfdados.sort_values(by='preco')
print(dfdados.head(5))





'''----------------------------------------EX3-----------------------------------------'''

#3)	Uma pessoa quer comprar um carro, e deseja ver as opções mais econômicas. Mostre os dados em um Dataframe (Car93_miss.csv) com as seguintes condições:
#•	Deve ser um carro com 5 lugares;
#•	Selecione os 10 carros com maior MPG(Miles Per Gallon) na cidade;
#•	Dos 10 mais econômicos, mostre os 5 modelos mais baratos;
#•	Mostre somente as colunas 'Manufacturer','Make','Price','MPG.city','Type','Passengers'



dfcarros = pandas.read_csv('Dados/Cars93_miss.csv', usecols=['Manufacturer','Make','Price','MPG.city','Type','Passengers'])

dfcarros = dfcarros[dfcarros['Passengers'] >= 5]
dfcarros = dfcarros[dfcarros['MPG.city'] > 1] # Fiz isso antes de saber a função dropna
dfcarros = dfcarros.sort_values(by='MPG.city')
dfcarros = dfcarros.tail(10)
dfcarros = dfcarros.sort_values(by='Price')
print(dfcarros.head(5))








'''----------------------------------------EX4-----------------------------------------'''

#4)	Edite a imagem "imagem.jpg" transformando de BGR para HSV, escreva “Olho psicodelico” 
#ajustando os parâmetros para que a frase encaixe na imagem, 
#depois gire verticalmente e horizontalmente a imagem.


img = cv2.imread('Dados/imagem.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow('Imagem Original',img)


img2 = img
cv2.putText(img2, 'Olho Psicodelico', (0,23), font, 1, (0,0,0), 2, cv2.LINE_AA)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img2 = cv2.flip(img2,-1)

cv2.imshow('Imagem HSV', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()







'''----------------------------------------EX5-----------------------------------------'''

#5)	Edite o vídeo “pixar_inv.mp4” virando ele de ponta cabeça,
#salve o novo vídeo com o nome “pixar.mp4”.
#Informações importantes: fps: 30, dimensão: 1280x720.



cap = cv2.VideoCapture('dados/pixar_inv.avi')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
framesporsec = 60
width, height = 1280,720
output = cv2.VideoWriter("dados/pixar.avi", fourcc, framesporsec, (width,height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('X') or ret == False or cv2.waitKey(1) == ord('x'):
        break
    frame_inv = cv2.flip(frame, 0)
    output.write(frame_inv)
    cv2.imshow('frame Correto', frame_inv)
output.release()
cap.release()
cv2.destroyAllWindows()





















'''----------------------------------------EX6-----------------------------------------'''

#6)	Crie um programa no qual o usuário insira números até ser inserido o valor 0.
#Ao inserir um valor 0 deve ser gerado um gráfico de pizza mostrando o percentual de números
#ímpares e pares, a formatação do gráfico fica a critério do aluno. 


par = 0
impar = 0

while True:
    try:
        valor = int(input('Entre com o valor: '))
        if valor == 0:
            break
        else:
            if valor % 2 == 0:
                par += 1
            else:
                impar += 1
            
    except ValueError:
        print('Entre apenas com valores inteiros')
        continue

labels= ['Pares', 'Impares']
valores = [par, impar]
pizza = plt.pie(valores, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Gráfico de pares e ímpares')
arq = 'graficoPizza.png'
plt.savefig(arq)
plt.show()


'''----------------------------------------EX7-----------------------------------------'''

#7)	Salve o gráfico que você criou no exercícios anterior como uma figura na sua pasta, e mova ele para uma pasta
#específica chamada ‘Gráficos’, utilizando o módulo OS.

import os


origem = os.path.join('S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Treinamentos', arq)
destino = os.path.join('S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Provas/Treinamentos/Dados',arq)
os.rename(origem, destino)




