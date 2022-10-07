# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:48:36 2022

@author: DISRCT
"""

import cv2
import numpy as np
import random as rd


def funcao(event,x,y,flas,parma):
    global a,b,c
    if event == cv2.EVENT_LBUTTONDOWN:
        a = rd.randint(0,255)
        b = rd.randint(0,255)
        c = rd.randint(0,255)

cv2.namedWindow('janela')
cv2.setMouseCallback('janela',funcao)


while True:
    img = np.full((512,512,3), (a,b,c), np.uint8)
    cv2.imshow('janela',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()


