# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:41:58 2022

@author: Leonardo Falango
"""

import cv2

img = cv2.imread('../dados/Flor.png')
imgfiltro = cv2.medianBlur(img, 5)


cv2.imshow('Sem Ruídos', imgfiltro)
#cv2.imwrite('../dados/FlorSemRuidos(1).png', imgfiltro)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()