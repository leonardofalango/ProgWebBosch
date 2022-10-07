# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 08:32:49 2022

@author: Leonardo Falango
"""

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.line(img, (150,0), (150,512),(255,255,255),5)
cv2.line(img, (350,0), (350,512),(255,255,255),5)


cv2.line(img, (0,150), (512,150),(255,255,255),5)
cv2.line(img, (0,350), (512,350),(255,255,255),5)

cv2.imshow('Jogo da velha',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# FAZENDO O PRIMEIRO X
cv2.line(img, (0,0), (145,145), (255),5)
cv2.line(img, (145,0), (0,145), (255),5)

cv2.imshow('Jogo da velha',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# FAZENDO O PRIMEIRO CÍRCULO
cv2.circle(img,(256,65), 72,(255),5)


cv2.imshow('Jogo da velha',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


