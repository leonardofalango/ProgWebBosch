# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:31:10 2022

@author: Leonardo Falango
"""

import cv2

cvt = ''
while True:
    efeito = input("Efeitos:\n 1 - Preto e Branco\n 2 - HSV\n 3 - RGB\n\nEntre com a opção: ")
    if efeito == '1':
        cvt = cv2.COLOR_BGR2GRAY
        break
    elif efeito == '2':
        cvt = cv2.COLOR_BGR2HSV
        break
    elif efeito == '3':
        cvt = cv2.COLOR_BGR2RGB
        break
    else:
        print("Entre com uma opção válida.")
        continue



cap = cv2.VideoCapture('Dados/flor.mp4') # Abrindo  o vídeo
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # codex
framesporsec = 30 # Settando os frames por segundo
width, height = 1280,720 # Largura e Altura
output = cv2.VideoWriter("novo_video.mp4", 0, framesporsec, (width,height)) # OUTPUT, será o vídeo que vai ser salvo,

while (cap.isOpened()):
    ret, frame = cap.read() # ret, vai ser o return se o vídeo ainda está rodando
    if ret == False: # Quando o vídeo acabar
        break # Sai do loop
    frame_mod = cv2.cvtColor(frame, cvt) # Criando um outro frame, alterando o frame original de RGB para BGR
    output.write(frame_mod) # Colocando frame por frame no output
    cv2.imshow('output', frame) # Mostrando apenas o frame já modificado para o usuário
    
output.release()
cap.release()
cv2.destroyAllWindows()
