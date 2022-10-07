# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:34:50 2022

@author: Leonardo Falango
"""

import cv2



cap = cv2.VideoCapture('csv/video_padrao.mp4') # Abrindo  o vídeo
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # codex
framesporsec = 30 # Settando os frames por segundo
width, height = 1280,720 # Largura e Altura
output = cv2.VideoWriter("video_padrao.mp4", 0, framesporsec, (width,height)) # OUTPUT, será o vídeo que vai ser salvo,
                            # Vai ser salvo no diretório "Provas", não no diretório aonde está salvo o arquivo original

while (cap.isOpened()):
    ret, frame = cap.read() # ret, vai ser o return se o vídeo ainda está rodando
    if ret == False: # Quando o vídeo acabar
        break # Sai do loop
    frame_correto = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Criando um outro frame, alterando o frame original de RGB para BGR
    output.write(frame_correto) # Colocando frame por frame no output
    cv2.imshow('output', frame_correto) # Mostrando apenas o frame já modificado para o usuário
output.release()
cap.release()
cv2.destroyAllWindows()