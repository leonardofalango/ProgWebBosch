# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:41:58 2022

@author: Leonardo Falango
"""

import cv2

img = cv2.imread('../dados/ruido.jpg')
blurimg = cv2.blur(img,(6,6))

cv2.imshow('Sem Ruídos', blurimg)

#cv2.imwrite('../dados/Sem ruídos.jpg', blurimg)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()