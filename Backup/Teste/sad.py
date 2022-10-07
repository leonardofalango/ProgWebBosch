# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:08:01 2022

@author: DISRCT
"""


import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


baralho = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
naipes = ["♦", "♠", "♥", "♣"]


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
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def showMesa(mesa):
    img = np.zeros((750, 1200,3),np.uint8)
    fontpath = "Fontes/NotoSans-Regular.ttf"
    font = ImageFont.truetype(fontpath, 80)
    pil_im = Image.fromarray(img)  
    draw = ImageDraw.Draw(pil_im)
    
    if len(mesa) == 1:
        local = (500,200)
        draw.text(local, mesa[0], font=font, fill=(0,255,0,0))
    else:
        for i in range(len(mesa)):
            local = (i*200+350,200)
            draw.text(local, mesa[i], font=font, fill=(0,255,0,0))
        
    img = np.array(pil_im)
    cv2.imshow('Truco', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()








