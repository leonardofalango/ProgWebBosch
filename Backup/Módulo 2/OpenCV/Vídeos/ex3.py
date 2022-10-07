# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:39:16 2022

@author: Leonardo Falango
"""

import cv2
import random as rd
import numpy as np

fps = 30

codex = cv2.VideoWriter_fourcc(*"DIVX")
video = cv2.VideoWriter('VídeoEx2.avi', codex, fps, (500,500))

frame = np.zeros((500,500,3), np.uint8)

antx = 0
anty = 0
contagem =0
color = (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
while contagem <= 300:
    if contagem % 30 == 0:
        color = (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
    cv2.circle(frame, (antx,anty), 50, (0,0,0), -1)
    x = rd.randint(0,500)
    y = rd.randint(0,500)
    cv2.circle(frame, (x,y), 50,color, -1)
    antx = x
    anty = y
    cv2.imshow('frame', frame)
    
    video.write(frame)
    
    if cv2.waitKey(10) & 0xFF == ord('x'):
        break
    contagem += 1
video.release()
cv2.destroyAllWindows()


