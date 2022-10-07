# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:53:50 2022

@author: Leonardo Falango
"""

import cv2
import numpy as np

img = cv2.imread("csv/terra.jpg")

img = cv2.rectangle(img, (70,40), (660,630), (255,255,255),4)

cv2.imshow('Terra',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


