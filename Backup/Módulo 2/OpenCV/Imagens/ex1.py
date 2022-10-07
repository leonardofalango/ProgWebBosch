# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:20:57 2022

@author: Leonardo Falango
"""

import cv2

import numpy as np

img = np.zeros((1920,1080,3), np.uint8)

cv2.circle(img, (75,75), 50, (0,255,0), -1)
cv2.rectangle(img, (210,210), (310,310), (0,0,255), -1)
cv2.ellipse(img, (437,437), (40,50), 30, 0, 360, (255,0,0), -1)
tecla = ''
while True:
    if tecla == '-1' or tecla== '27' or tecla == '13':
        break
    
    
    img2 = np.zeros((521,512,3), np.uint8)
    cv2.imshow('teste', img)
    tecla = cv2.waitKey(0)
    cv2.destroyAllWindows()
    tecla = str(tecla)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img2, tecla, (100,260), cv2.FONT_HERSHEY_SIMPLEX, 7,(255,255,255),5, cv2.LINE_AA)
    cv2.imshow('img2',img2)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()