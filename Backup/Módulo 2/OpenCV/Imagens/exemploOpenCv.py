# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 08:16:26 2022

@author: Leonardo Falango
"""
import cv2


marmota = cv2.imread("imgs/marmota.png")
marmota_cinza = cv2.imread("imgs/marmota.png", cv2.IMREAD_GRAYSCALE)




cv2.imshow('Marmotera', marmota)
x = cv2.waitKey(0)
print(x)
cv2.destroyAllWindows()


cv2.imshow('Marmotera cinza', marmota_cinza)
x = cv2.waitKey(0)
print(x)
cv2.destroyAllWindows()


# PARA SALVAR -> IMWRITE

cv2.imwrite('imgs/marmoteracinza.png', marmota_cinza)


