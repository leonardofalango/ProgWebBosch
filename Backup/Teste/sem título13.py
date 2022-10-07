# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:52:39 2022

@author: DISRCT
"""

import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

def showCartas(cartas):
    img = np.zeros((750, 1200,3),np.uint8)
    fontpath = "Fontes/NotoSans-Regular.ttf"
    font = ImageFont.truetype(fontpath, 80)
    pil_im = Image.fromarray(img)  
    draw = ImageDraw.Draw(pil_im)
    
    for i in range(len(cartas)):
        if i == 0:
            local = (200,500)
        elif i == 1:
            local = (500,500)
        elif i == 2:
            local = (900,500)
        draw.text(local, cartas[i], font=font, fill=(0,255,0,0))
    img = np.array(pil_im)
    cv2.imshow('Truco', img)
    tecla = cv2.waitKey(0)
    cv2.destroyAllWindows()
    return tecla
cartas = ['4♦','2♣','2♥']
print(int(showCartas(cartas)))
print(ord("1"))