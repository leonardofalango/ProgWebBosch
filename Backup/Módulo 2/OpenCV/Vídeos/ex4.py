# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:46:24 2022

@author: Leonardo Falango
"""

import cv2

cap = cv2.VideoCapture('../dados/video.avi')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
framesporsec = 20
width, height = 300,300
output = cv2.VideoWriter("../dados/teste.avi", 0, framesporsec, (width,height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('X') or ret == False or cv2.waitKey(1) == ord('x'):
        break
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    output.write(frame_hsv)
    cv2.imshow('frame', frame)
output.release()
cap.release()
cv2.destroyAllWindows()