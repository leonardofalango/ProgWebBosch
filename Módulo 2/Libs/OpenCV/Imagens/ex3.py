# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:59:04 2022

@author: Leonardo Falango
"""

import cv2
import numpy as np


img = np.zeros((512,512,3), np.uint8)

def funcao(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_MOUSEWHEEL:
        cv2.circle(img, (x, y), 50, (255,255,0), -1)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.ellipse(img, (x, y), (40,50), 30, 0, 360, (255,0,255), -1)
    

cv2.namedWindow('janela')
cv2.setMouseCallback('janela', funcao)

while True:
    
    cv2.imshow('janela',img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
