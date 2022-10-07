z# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:52:29 2022

@author: DISRCT
"""

import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX

img = np.ones((512,512,3), np.uint8)
b,g,r = 0,0,0
def funcao(event,x,y,flags,param):
    global img,b,g,r
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 50, (b,g,r), -1)
    

cv2.namedWindow('janela')
cv2.setMouseCallback('janela', funcao)


while True:
    cv2.putText(img, f"red: {r}",(5,20), font, 1,(255,255,255), 1, cv2.LINE_AA)

    cv2.putText(img, f"green: {g}",(5,45), font, 1,(255,255,255), 1, cv2.LINE_AA)
    
    cv2.putText(img, f"blue: {b}",(5,70), font, 1,(255,255,255), 1, cv2.LINE_AA)
    
    cv2.imshow('janela',img)
    
    tecla = cv2.waitKey(1)
    
    if tecla == ord('g') or tecla == ord('G'):
          g += 10
          cv2.circle(img, (100,20), 100, (0,0,0), -1)
          if g > 255:
              g = 0
    if tecla == ord('b') or tecla == ord('B'):
          b += 10
          cv2.circle(img, (100,20), 100, (0,0,0), -1)
          if b > 255:
              b = 0
    if tecla == ord('r') or tecla == ord('R'):
          r += 10
          cv2.circle(img, (100,20), 100, (0,0,0), -1)
          if r > 255:
              r = 0
    if tecla == ord('x') or tecla == ord('X'):
        break
    else:
        cv2.circle(img, (100,20), 100, (0,0,0), -1)


cv2.destroyAllWindows()