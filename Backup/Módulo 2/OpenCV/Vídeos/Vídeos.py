# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:21:05 2022

@author: Leonardo Falango
"""

import cv2

cap = cv2.VideoCapture('imgs/video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
framesporsec = 20
width, height = 640,480
output = cv2.VideoWriter("../dados/NovoVídeo.mp4", fourcc, framesporsec, (width,height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('X') or ret == False or cv2.waitKey(1) == ord('x'):
        break
    cv2.imshow('frame', frame)
    output.write(frame)

output.release()
cap.release()
cv2.destroyAllWindows()