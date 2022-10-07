# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:03:20 2022

@author: Leonardo Falango
"""

import cv2

#img = cv2.imread('Dados/sunset.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#n_preto = gray != 0
#img[n_preto] = 255
#cv2.imshow('Output', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img = cv2.imread('Dados/sunset.jpg')
cinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, prova = cv2.threshold(cinza, 80, 255, cv2.THRESH_BINARY)
ret, correcao = cv2.threshold(cinza, 30, 255, cv2.THRESH_BINARY)



cv2.imshow('Imagem prova', prova)
cv2.imshow('Imagem Correção da Prova', correcao)

cv2.waitKey(0)
cv2.destroyAllWindows()